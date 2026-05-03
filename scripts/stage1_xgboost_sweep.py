"""
Stage-1 XGBoost experiment runner.

This script keeps the baseline feature pipeline and time split unchanged, then
runs a compact set of XGBoost configurations for the May 4 submission. It writes
validated candidate portfolios under submissions/ and a Markdown experiment log
that can be reused in the report.

Usage
-----
  python scripts/stage1_xgboost_sweep.py
  python scripts/stage1_xgboost_sweep.py --as-of 20260421 --out-dir submissions
"""
from __future__ import annotations

import argparse
import platform
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import numpy as np
import pandas as pd
import pyarrow
import scipy
import sklearn
import xgboost as xgb

import xgboost
from baseline_xgboost import (
    DATA_DIR,
    EMBARGO_DAYS,
    VAL_DAYS,
    build_portfolio,
    rank_ic,
)
from csi500_ml.features import (
    FEATURE_COLUMNS,
    FORWARD_HORIZON,
    TARGET_COLUMN,
    build_features,
    prediction_frame,
    training_frame,
)
from validate_submission import validate


RANDOM_SEED = 42

EXPERIMENTS = [
    {
        "name": "baseline_top50",
        "top_k": 50,
        "params": {
            "n_estimators": 400,
            "max_depth": 5,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 10,
            "reg_lambda": 1.0,
        },
    },
    {
        "name": "shallow_regularized_top50",
        "top_k": 50,
        "params": {
            "n_estimators": 500,
            "max_depth": 3,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 5.0,
        },
    },
    {
        "name": "slow_learning_top50",
        "top_k": 50,
        "params": {
            "n_estimators": 800,
            "max_depth": 4,
            "learning_rate": 0.03,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 10,
            "reg_lambda": 5.0,
        },
    },
    {
        "name": "faster_learning_top50",
        "top_k": 50,
        "params": {
            "n_estimators": 300,
            "max_depth": 4,
            "learning_rate": 0.08,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 10,
            "reg_lambda": 1.0,
        },
    },
    {
        "name": "subsampled_top80",
        "top_k": 80,
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.7,
            "colsample_bytree": 0.7,
            "min_child_weight": 10,
            "reg_lambda": 5.0,
        },
    },
    {
        "name": "broad_portfolio_top100",
        "top_k": 100,
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.9,
            "colsample_bytree": 0.9,
            "min_child_weight": 10,
            "reg_lambda": 5.0,
        },
    },
    {
        "name": "concentrated_top30",
        "top_k": 30,
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 10,
            "reg_lambda": 5.0,
        },
    },
    {
        "name": "deep_regularized_top80",
        "top_k": 80,
        "params": {
            "n_estimators": 500,
            "max_depth": 5,
            "learning_rate": 0.03,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
]


def git_status_short() -> str:
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return "git unavailable"
    status = result.stdout.strip()
    return status if status else "clean"


def split_training_data(panel: pd.DataFrame, as_of: str | None) -> tuple[pd.DataFrame, pd.DataFrame, pd.Timestamp]:
    as_of_ts = pd.Timestamp(as_of) if as_of else panel["date"].max()
    trading_dates = np.sort(panel["date"].unique())
    as_of_idx = int(np.searchsorted(trading_dates, np.datetime64(as_of_ts)))
    cutoff_idx = max(0, as_of_idx - FORWARD_HORIZON)
    train_cutoff = pd.Timestamp(trading_dates[cutoff_idx])
    train_pool = training_frame(panel, max_date=train_cutoff)

    all_dates = np.sort(train_pool["date"].unique())
    if len(all_dates) < VAL_DAYS + EMBARGO_DAYS + 20:
        raise RuntimeError("Not enough dates to train; download more history.")

    val_start = pd.Timestamp(all_dates[-VAL_DAYS])
    train_end = pd.Timestamp(all_dates[-(VAL_DAYS + EMBARGO_DAYS + 1)])
    train_df = train_pool[train_pool["date"] <= train_end]
    val_df = train_pool[train_pool["date"] >= val_start]
    return train_df, val_df, train_end


def train_xgboost(train_df: pd.DataFrame, val_df: pd.DataFrame, params: dict) -> xgb.XGBRegressor:
    model = xgb.XGBRegressor(
        **params,
        objective="reg:squarederror",
        tree_method="hist",
        n_jobs=-1,
        early_stopping_rounds=30,
        random_state=RANDOM_SEED,
    )
    model.fit(
        train_df[FEATURE_COLUMNS],
        train_df[TARGET_COLUMN],
        eval_set=[(val_df[FEATURE_COLUMNS], val_df[TARGET_COLUMN])],
        verbose=False,
    )
    return model


def write_portfolio(path: Path, weights: pd.Series) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = pd.DataFrame({"stock_code": weights.index, "weight": weights.values})
    out.to_csv(path, index=False)


def format_params(params: dict) -> str:
    return ", ".join(f"{k}={v}" for k, v in params.items())


def write_report(
    report_path: Path,
    args: argparse.Namespace,
    prices: pd.DataFrame,
    constituents: pd.DataFrame,
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    pred_date: pd.Timestamp,
    rows: list[dict],
) -> None:
    best = max((r for r in rows if r["valid"]), key=lambda r: r["rank_ic"])
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_dates = pd.to_datetime(prices["date"])
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Stage 1 Experiment Log",
        "",
        f"- Generated at: {now}",
        f"- Python: {platform.python_version()}",
        f"- Packages: pandas {pd.__version__}, numpy {np.__version__}, pyarrow {pyarrow.__version__}, xgboost {xgboost.__version__}, sklearn {sklearn.__version__}, scipy {scipy.__version__}",
        f"- Data: prices rows {len(prices):,}, stocks {prices['stock_code'].nunique()}, dates {data_dates.min().date()} to {data_dates.max().date()}, constituents {constituents['stock_code'].nunique()}",
        f"- Git status: {git_status_short()}",
        f"- Command: `python scripts/stage1_xgboost_sweep.py --prices {args.prices} --constituents {args.constituents} --out-dir {args.out_dir} --report {args.report}`",
        "",
        "## Method",
        "",
        "- Factors: reused the technical factors in `src/csi500_ml/features.py`, including recent returns, volatility, volume z-score, turnover average, moving-average distance, RSI, and cross-sectional ranks.",
        "- Model: XGBoost regressor trained from scratch to predict 5-trading-day forward return.",
        "- Split: time-based train/validation split from the baseline, with a 5-trading-day embargo before the last 10 validation trading days.",
        f"- Training rows: {len(train_df):,}; validation rows: {len(val_df):,}; train end: {train_df['date'].max().date()}; validation start: {val_df['date'].min().date()}; prediction date: {pred_date.date()}.",
        "- Portfolio: top-K predicted names with rank-based long-only weights, max weight 10%, fully invested.",
        "",
        "## Results",
        "",
        "| Experiment | top_k | validation rank IC | valid | output | params |",
        "| --- | ---: | ---: | --- | --- | --- |",
    ]
    for r in sorted(rows, key=lambda item: item["rank_ic"], reverse=True):
        valid = "yes" if r["valid"] else "no"
        lines.append(
            f"| {r['name']} | {r['top_k']} | {r['rank_ic']:.4f} | {valid} | `{r['output']}` | {format_params(r['params'])} |"
        )

    lines.extend(
        [
            "",
            "## Stage Conclusion",
            "",
            f"- Selected submission: `{best['output']}` copied to `{args.final_out}`.",
            f"- Best validation rank IC: {best['rank_ic']:.4f} from `{best['name']}`.",
            "- The first-stage choice favors a reproducible XGBoost variant over adding new model families, reducing leakage and integration risk before the May 4 deadline.",
            "- LLM assistance was used for planning and coding support. The portfolio scores and weights are produced by locally trained XGBoost models, not by LLM stock selection.",
            "",
            "## Reproduction",
            "",
            "```powershell",
            ".\\.conda\\python.exe -m pip install -r requirements.txt",
            ".\\.conda\\python.exe scripts\\stage1_xgboost_sweep.py",
            ".\\.conda\\python.exe scripts\\validate_submission.py submissions/week1.csv",
            "```",
            "",
        ]
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prices", default=str(DATA_DIR / "prices.parquet"))
    parser.add_argument("--constituents", default=str(DATA_DIR / "constituents.csv"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--out-dir", default="submissions")
    parser.add_argument("--report", default="reports/stage1_experiment_log.md")
    parser.add_argument("--final-out", default="submissions/week1.csv")
    args = parser.parse_args()

    print(f">> Loading {args.prices}")
    prices = pd.read_parquet(args.prices)
    prices["stock_code"] = prices["stock_code"].astype(str).str.zfill(6)
    constituents = pd.read_csv(args.constituents, dtype={"stock_code": str})
    constituents["stock_code"] = constituents["stock_code"].str.zfill(6)
    print(
        f"   {len(prices):,} rows, {prices['stock_code'].nunique()} stocks, "
        f"dates {pd.to_datetime(prices['date']).min().date()} to {pd.to_datetime(prices['date']).max().date()}"
    )

    print(">> Building features once")
    panel = build_features(prices)
    train_df, val_df, train_end = split_training_data(panel, args.as_of)
    print(f"   train: {len(train_df):,} rows up to {train_end.date()}")
    print(f"   val:   {len(val_df):,} rows from {val_df['date'].min().date()}")

    pred_df = prediction_frame(panel, as_of=args.as_of)
    if pred_df.empty:
        raise RuntimeError(f"No rows available for as_of={args.as_of}. Check data.")
    pred_date = pred_df["date"].iloc[0]
    print(f"   prediction date: {pred_date.date()}, stocks {len(pred_df)}")

    out_dir = Path(args.out_dir)
    rows = []
    for spec in EXPERIMENTS:
        print(f">> Training {spec['name']}")
        model = train_xgboost(train_df, val_df, spec["params"])
        val_pred = model.predict(val_df[FEATURE_COLUMNS])
        ic = rank_ic(val_df[TARGET_COLUMN].to_numpy(), val_pred, val_df["date"].to_numpy())

        scored = pred_df.assign(score=model.predict(pred_df[FEATURE_COLUMNS]))
        scores = scored.set_index("stock_code")["score"]
        weights = build_portfolio(scores, top_k=spec["top_k"])
        out_path = out_dir / f"stage1_{spec['name']}.csv"
        write_portfolio(out_path, weights)

        errors = validate(out_path, Path(args.constituents))
        valid = not errors
        print(f"   rank IC {ic:.4f}; valid={valid}; output={out_path}")
        if errors:
            for error in errors:
                print(f"   validation error: {error}")

        rows.append(
            {
                "name": spec["name"],
                "top_k": spec["top_k"],
                "params": spec["params"],
                "rank_ic": ic,
                "valid": valid,
                "output": str(out_path),
                "errors": errors,
            }
        )

    valid_rows = [r for r in rows if r["valid"]]
    if not valid_rows:
        raise RuntimeError("No valid portfolios were produced.")
    best = max(valid_rows, key=lambda r: r["rank_ic"])
    final_out = Path(args.final_out)
    final_out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(best["output"], final_out)
    print(f">> Selected {best['name']} with rank IC {best['rank_ic']:.4f}")
    print(f">> Copied final submission to {final_out}")

    write_report(Path(args.report), args, prices, constituents, train_df, val_df, pred_date, rows)
    print(f">> Wrote report log to {args.report}")


if __name__ == "__main__":
    main()
