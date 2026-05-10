"""
Generate a submission using a local XGBoost spec and portfolio overlay rule.

This is the production companion to `run_portfolio_overlay_sweep.py`: it trains
one selected local model on all legally labeled history, predicts the as-of
cross-section, applies configurable score-positive/vol-adjusted weights, and
validates the output CSV.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import numpy as np
import pandas as pd
import xgboost as xgb

from baseline_xgboost import DATA_DIR, EMBARGO_DAYS, VAL_DAYS, rank_ic
from csi500_ml.features import (
    FORWARD_HORIZON,
    TARGET_COLUMN,
    build_features,
    feature_columns,
    prediction_frame,
    training_frame,
)
from run_portfolio_overlay_sweep import (
    FEATURE_GROUPS,
    PRIMARY_SPEC,
    build_score_weights,
    spec_by_name,
)
from stage1_xgboost_sweep import RANDOM_SEED
from validate_submission import validate


def parse_groups(value: str | None) -> list[str]:
    return [g.strip() for g in (value or "").split(",") if g.strip()]


def trading_date_at(dates: np.ndarray, idx: int) -> pd.Timestamp:
    if idx < 0 or idx >= len(dates):
        raise IndexError(idx)
    return pd.Timestamp(dates[idx])


def split_train_eval(train_pool: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.Timestamp]:
    dates = np.sort(train_pool["date"].unique())
    if len(dates) < VAL_DAYS + EMBARGO_DAYS + 20:
        raise RuntimeError("Not enough dates for internal eval split.")
    val_start = trading_date_at(dates, len(dates) - VAL_DAYS)
    train_end = trading_date_at(dates, len(dates) - (VAL_DAYS + EMBARGO_DAYS + 1))
    train_df = train_pool[train_pool["date"] <= train_end].copy()
    eval_df = train_pool[train_pool["date"] >= val_start].copy()
    return train_df, eval_df, train_end


def train_xgboost(train_df: pd.DataFrame, eval_df: pd.DataFrame, params: dict, feature_cols: list[str]) -> xgb.XGBRegressor:
    model = xgb.XGBRegressor(
        **params,
        objective="reg:squarederror",
        tree_method="hist",
        n_jobs=-1,
        early_stopping_rounds=30,
        random_state=RANDOM_SEED,
    )
    model.fit(
        train_df[feature_cols],
        train_df[TARGET_COLUMN],
        eval_set=[(eval_df[feature_cols], eval_df[TARGET_COLUMN])],
        verbose=False,
    )
    return model


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prices", default=str(DATA_DIR / "prices.parquet"))
    parser.add_argument("--index", default=str(DATA_DIR / "index.parquet"))
    parser.add_argument("--constituents", default=str(DATA_DIR / "constituents.csv"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--local-spec", default=PRIMARY_SPEC)
    parser.add_argument("--feature-groups", default=",".join(FEATURE_GROUPS))
    parser.add_argument("--top-k", type=int, default=30)
    parser.add_argument("--max-weight", type=float, default=0.10)
    parser.add_argument("--score-power", type=float, default=1.0)
    parser.add_argument("--vol-adjust", action="store_true")
    parser.add_argument("--vol-power", type=float, default=1.0)
    parser.add_argument("--out", default="submissions/week2_overlay_candidate.csv")
    args = parser.parse_args()

    enabled_groups = parse_groups(args.feature_groups)
    feature_cols = feature_columns(enabled_groups)
    spec = spec_by_name(args.local_spec)

    print(f">> Loading {args.prices}")
    prices = pd.read_parquet(args.prices)
    prices["stock_code"] = prices["stock_code"].astype(str).str.zfill(6)
    prices["date"] = pd.to_datetime(prices["date"])
    index_df = pd.read_parquet(args.index)
    index_df["date"] = pd.to_datetime(index_df["date"])
    print(
        f"   {len(prices):,} rows, {prices['stock_code'].nunique()} stocks, "
        f"dates {prices['date'].min().date()} to {prices['date'].max().date()}"
    )

    print(">> Building features")
    panel = build_features(prices, index_df=index_df)
    as_of = pd.Timestamp(args.as_of) if args.as_of else pd.Timestamp(panel["date"].max())
    dates = np.sort(panel["date"].unique())
    as_of_idx = int(np.searchsorted(dates, np.datetime64(as_of)))
    cutoff = trading_date_at(dates, as_of_idx - FORWARD_HORIZON)
    train_pool = training_frame(panel, max_date=cutoff).dropna(subset=feature_cols + [TARGET_COLUMN])
    train_df, eval_df, train_end = split_train_eval(train_pool)
    print(f"   local spec: {spec['name']}")
    print(f"   feature groups: {', '.join(enabled_groups) if enabled_groups else 'baseline'}")
    print(f"   feature count: {len(feature_cols)}")
    print(f"   as-of: {as_of.date()}, label cutoff: {cutoff.date()}")
    print(f"   train rows: {len(train_df):,} up to {train_end.date()}")
    print(f"   eval rows: {len(eval_df):,} from {eval_df['date'].min().date()}")

    print(">> Training XGBoost")
    model = train_xgboost(train_df, eval_df, spec["params"], feature_cols)
    eval_pred = model.predict(eval_df[feature_cols])
    ic = rank_ic(eval_df[TARGET_COLUMN].to_numpy(), eval_pred, eval_df["date"].to_numpy())
    print(f"   internal eval rank IC: {ic:.4f}")

    print(">> Predicting overlay portfolio")
    pred_df = prediction_frame(panel, as_of=as_of).dropna(subset=feature_cols).copy()
    pred_df = pred_df.assign(score=model.predict(pred_df[feature_cols]))
    weights = build_score_weights(
        pred_df,
        top_k=args.top_k,
        max_weight=args.max_weight,
        power=args.score_power,
        vol_adjust=args.vol_adjust,
        vol_power=args.vol_power if args.vol_adjust else 0.0,
    )
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out = pd.DataFrame({"stock_code": weights.index, "weight": weights.values})
    out.to_csv(out_path, index=False)
    print(f">> Wrote {len(out)} names to {out_path}")
    print(
        f"   weight summary: min={out['weight'].min():.4f} "
        f"max={out['weight'].max():.4f} sum={out['weight'].sum():.4f}"
    )

    errors = validate(out_path, Path(args.constituents))
    if errors:
        for error in errors:
            print(f"   validation error: {error}")
        raise SystemExit(1)
    print(f"OK: {out_path} passes submission checks")


if __name__ == "__main__":
    main()
