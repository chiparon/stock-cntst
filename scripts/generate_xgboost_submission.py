"""
Generate a CSI500 submission from a selected XGBoost experiment and feature set.

This is the production companion to testlike_xgboost_validation.py: choose an
experiment that passed the 5-day validation gate, train on all available labeled
history up to the as-of cutoff, predict the latest cross-section, and write a
validated portfolio CSV.

Usage
-----
  python scripts/generate_xgboost_submission.py
  python scripts/generate_xgboost_submission.py --experiment slow_learning_top50 --feature-groups ""
  python scripts/generate_xgboost_submission.py --experiment concentrated_top30 --feature-groups momentum_shape
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import pandas as pd
import xgboost as xgb

from baseline_xgboost import DATA_DIR, EMBARGO_DAYS, VAL_DAYS, build_portfolio, rank_ic
from csi500_ml.features import (
    FORWARD_HORIZON,
    TARGET_COLUMN,
    build_features,
    feature_columns,
    prediction_frame,
    training_frame,
)
from csi500_ml.portfolio import build_portfolio
from stage1_xgboost_sweep import EXPERIMENTS, RANDOM_SEED
from validate_submission import validate


DEFAULT_EXPERIMENT = "concentrated_top30"
DEFAULT_FEATURE_GROUPS = "momentum_shape"


def parse_groups(value: str | None) -> list[str]:
    return [g.strip() for g in (value or "").split(",") if g.strip()]


def experiment_by_name(name: str) -> dict:
    for spec in EXPERIMENTS:
        if spec["name"] == name:
            return spec
    available = ", ".join(spec["name"] for spec in EXPERIMENTS)
    raise ValueError(f"Unknown experiment {name!r}; available: {available}")


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
    parser.add_argument("--constituents", default=str(DATA_DIR / "constituents.csv"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--experiment", default=DEFAULT_EXPERIMENT)
    parser.add_argument("--feature-groups", default=DEFAULT_FEATURE_GROUPS)
    parser.add_argument("--top-k", type=int, default=None, help="Override experiment top_k.")
    parser.add_argument("--weight-rule", default="score_positive", choices=["rank", "equal", "score_positive"])
    parser.add_argument("--out", default="submissions/week1_candidate.csv")
    args = parser.parse_args()

    spec = experiment_by_name(args.experiment)
    enabled_groups = parse_groups(args.feature_groups)
    feature_cols = feature_columns(enabled_groups)

    print(f">> Loading {args.prices}")
    prices = pd.read_parquet(args.prices)
    prices["stock_code"] = prices["stock_code"].astype(str).str.zfill(6)
    prices["date"] = pd.to_datetime(prices["date"])
    print(
        f"   {len(prices):,} rows, {prices['stock_code'].nunique()} stocks, "
        f"dates {prices['date'].min().date()} to {prices['date'].max().date()}"
    )

    print(">> Building features")
    panel = build_features(prices)
    as_of = pd.Timestamp(args.as_of) if args.as_of else pd.Timestamp(panel["date"].max())
    dates = np.sort(panel["date"].unique())
    as_of_idx = int(np.searchsorted(dates, np.datetime64(as_of)))
    cutoff = trading_date_at(dates, as_of_idx - FORWARD_HORIZON)
    train_pool = training_frame(panel, max_date=cutoff).dropna(subset=feature_cols + [TARGET_COLUMN])
    train_df, eval_df, train_end = split_train_eval(train_pool)
    top_k = args.top_k if args.top_k is not None else spec["top_k"]
    print(f"   experiment: {spec['name']}, top_k={top_k}, weight_rule={args.weight_rule}")
    print(f"   feature groups: {', '.join(enabled_groups) if enabled_groups else 'baseline'}")
    print(f"   feature count: {len(feature_cols)}")
    print(f"   train rows: {len(train_df):,} up to {train_end.date()}")
    print(f"   eval rows: {len(eval_df):,} from {eval_df['date'].min().date()}")

    print(">> Training XGBoost")
    model = train_xgboost(train_df, eval_df, spec["params"], feature_cols)
    eval_pred = model.predict(eval_df[feature_cols])
    ic = rank_ic(eval_df[TARGET_COLUMN].to_numpy(), eval_pred, eval_df["date"].to_numpy())
    print(f"   internal eval rank IC: {ic:.4f}")

    print(">> Predicting portfolio")
    pred_df = prediction_frame(panel, as_of=as_of).dropna(subset=feature_cols)
    pred_df = pred_df.assign(score=model.predict(pred_df[feature_cols]))
    print(f"   as of {pred_df['date'].iloc[0].date()}, scoring {len(pred_df)} stocks")

    weights = build_portfolio(pred_df.set_index("stock_code")["score"], top_k=top_k, weight_rule=args.weight_rule)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out = pd.DataFrame({"stock_code": weights.index, "weight": weights.values})
    out.to_csv(out_path, index=False)
    print(f">> Wrote {len(out)} names to {out_path}")
    print(f"   weight summary: min={out['weight'].min():.4f} max={out['weight'].max():.4f} sum={out['weight'].sum():.4f}")

    errors = validate(out_path, Path(args.constituents))
    if errors:
        for error in errors:
            print(f"   validation error: {error}")
        raise SystemExit(1)
    print(f"OK: {out_path} passes submission checks")


if __name__ == "__main__":
    main()
