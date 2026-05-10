"""
Generate a CSI500 submission from a selected XGBoost experiment or a
regularized rank-blended ensemble.

The single-model path preserves the original baseline flow. The default path is
an ensemble that blends per-date percentile ranks from multiple strongly
regularized XGBoost models before building the portfolio.

Usage
-----
  python scripts/generate_xgboost_submission.py
  python scripts/generate_xgboost_submission.py --mode single --experiment slow_learning_top50
  python scripts/generate_xgboost_submission.py --mode ensemble --ensemble primary_rankliq_70_30
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

from baseline_xgboost import DATA_DIR, EMBARGO_DAYS, VAL_DAYS, rank_ic
from csi500_ml.features import (
    FORWARD_HORIZON,
    TARGET_COLUMN,
    build_features,
    feature_columns,
    prediction_frame,
    training_frame,
)
from csi500_ml.portfolio import build_portfolio
from csi500_ml.xgb_ensemble import (
    DEFAULT_ENSEMBLE,
    DEFAULT_WEIGHT_RULE,
    ENSEMBLES,
    MODEL_SPECS,
    blend_ranked_scores,
    train_xgboost,
)
from stage1_xgboost_sweep import EXPERIMENTS
from validate_submission import validate


DEFAULT_EXPERIMENT = "concentrated_top30"


def parse_groups(value: str | None) -> list[str]:
    return [g.strip() for g in (value or "").split(",") if g.strip()]


def experiment_by_name(name: str) -> dict:
    for spec in EXPERIMENTS:
        if spec["name"] == name:
            return spec
    available = ", ".join(spec["name"] for spec in EXPERIMENTS)
    raise ValueError(f"Unknown experiment {name!r}; available: {available}")


def ensemble_by_name(name: str) -> dict[str, float]:
    if name in ENSEMBLES:
        return ENSEMBLES[name]
    available = ", ".join(ENSEMBLES)
    raise ValueError(f"Unknown ensemble {name!r}; available: {available}")


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


def fit_and_score_model(
    train_df: pd.DataFrame,
    eval_df: pd.DataFrame,
    pred_df: pd.DataFrame,
    params: dict,
    feature_cols: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    model = train_xgboost(train_df, eval_df, feature_cols, params)

    eval_out = eval_df[["date", "stock_code", TARGET_COLUMN]].copy()
    eval_out["score"] = model.predict(eval_df[feature_cols])

    pred_out = pred_df[["date", "stock_code"]].copy()
    if TARGET_COLUMN in pred_df.columns:
        pred_out[TARGET_COLUMN] = pred_df[TARGET_COLUMN].values
    pred_out["score"] = model.predict(pred_df[feature_cols])
    return eval_out, pred_out


def build_single_model_submission(
    train_df: pd.DataFrame,
    eval_df: pd.DataFrame,
    pred_df: pd.DataFrame,
    params: dict,
    feature_cols: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    return fit_and_score_model(train_df, eval_df, pred_df, params, feature_cols)


def build_ensemble_submission(
    train_df: pd.DataFrame,
    eval_df: pd.DataFrame,
    pred_df: pd.DataFrame,
    ensemble_name: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    weights = ensemble_by_name(ensemble_name)
    eval_outputs: dict[str, pd.DataFrame] = {}
    pred_outputs: dict[str, pd.DataFrame] = {}
    for model_name in weights:
        spec = MODEL_SPECS[model_name]
        feature_cols = feature_columns(spec["groups"])
        eval_out, pred_out = fit_and_score_model(train_df, eval_df, pred_df, spec["params"], feature_cols)
        eval_outputs[model_name] = eval_out
        pred_outputs[model_name] = pred_out
    return blend_ranked_scores(eval_outputs, weights), blend_ranked_scores(pred_outputs, weights)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prices", default=str(DATA_DIR / "prices.parquet"))
    parser.add_argument("--index", default=str(DATA_DIR / "index.parquet"))
    parser.add_argument("--constituents", default=str(DATA_DIR / "constituents.csv"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--mode", choices=["single", "ensemble"], default="ensemble")
    parser.add_argument("--experiment", default=DEFAULT_EXPERIMENT)
    parser.add_argument("--feature-groups", default="momentum_shape")
    parser.add_argument("--ensemble", default=DEFAULT_ENSEMBLE)
    parser.add_argument("--top-k", type=int, default=None, help="Override experiment or ensemble top_k.")
    parser.add_argument("--weight-rule", default=DEFAULT_WEIGHT_RULE, choices=["rank", "equal", "score_positive"])
    parser.add_argument("--out", default="submissions/week1_candidate.csv")
    args = parser.parse_args()

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

    if args.mode == "single":
        enabled_groups = parse_groups(args.feature_groups)
        feature_cols = feature_columns(enabled_groups)
        train_pool = training_frame(panel, max_date=cutoff).dropna(subset=feature_cols + [TARGET_COLUMN])
        train_df, eval_df, train_end = split_train_eval(train_pool)
        top_k = args.top_k if args.top_k is not None else experiment_by_name(args.experiment)["top_k"]
        print(f"   mode: single model")
        print(f"   experiment: {args.experiment}, top_k={top_k}, weight_rule={args.weight_rule}")
        print(f"   feature groups: {', '.join(enabled_groups) if enabled_groups else 'baseline'}")
        print(f"   feature count: {len(feature_cols)}")
        print(f"   train rows: {len(train_df):,} up to {train_end.date()}")
        print(f"   eval rows: {len(eval_df):,} from {eval_df['date'].min().date()}")

        print(">> Training XGBoost")
        spec = experiment_by_name(args.experiment)
        eval_pred, pred_pred = build_single_model_submission(train_df, eval_df, prediction_frame(panel, as_of=as_of).dropna(subset=feature_cols), spec["params"], feature_cols)
        ic = rank_ic(eval_pred[TARGET_COLUMN].to_numpy(), eval_pred["score"].to_numpy(), eval_pred["date"].to_numpy())
        print(f"   internal eval rank IC: {ic:.4f}")
        pred_df = pred_pred
    else:
        ensemble_weights = ensemble_by_name(args.ensemble)
        all_feature_cols: list[str] = []
        for model_name in ensemble_weights:
            spec = MODEL_SPECS[model_name]
            all_feature_cols.extend(feature_columns(spec["groups"]))
        feature_cols = list(dict.fromkeys(all_feature_cols))
        train_pool = training_frame(panel, max_date=cutoff).dropna(subset=feature_cols + [TARGET_COLUMN])
        train_df, eval_df, train_end = split_train_eval(train_pool)
        top_k = args.top_k if args.top_k is not None else 30
        print(f"   mode: ensemble")
        print(f"   ensemble: {args.ensemble}, top_k={top_k}, weight_rule={args.weight_rule}")
        print(f"   ensemble weights: {', '.join(f'{k}={v:.2f}' for k, v in ensemble_weights.items())}")
        print(f"   feature count (union): {len(feature_cols)}")
        print(f"   train rows: {len(train_df):,} up to {train_end.date()}")
        print(f"   eval rows: {len(eval_df):,} from {eval_df['date'].min().date()}")

        pred_source = prediction_frame(panel, as_of=as_of).dropna(subset=feature_cols)
        print(">> Training ensemble members")
        eval_pred, pred_pred = build_ensemble_submission(train_df, eval_df, pred_source, args.ensemble)
        ic = rank_ic(eval_pred[TARGET_COLUMN].to_numpy(), eval_pred["score"].to_numpy(), eval_pred["date"].to_numpy())
        print(f"   internal ensemble rank IC: {ic:.4f}")
        pred_df = pred_pred

    print(">> Predicting portfolio")
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
