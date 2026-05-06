"""
Run a small local XGBoost parameter sweep around the current best setup.

The search is intentionally narrow:
- feature groups fixed to momentum_shape
- portfolio fixed to top_k=30 with score_positive weighting
- anchors fixed by baseline-feature adversarial validation
- metric fixed to 5-day excess return

Usage
-----
  python scripts/run_xgboost_local_sweep.py
"""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import pandas as pd

from baseline_xgboost import DATA_DIR, rank_ic
from csi500_ml.features import TARGET_COLUMN, build_features, feature_columns, prediction_frame, training_frame
from csi500_ml.portfolio import build_portfolio
from score_submission import score_window
from testlike_xgboost_validation import (
    HOLD_DAYS,
    labeled_cutoff_date,
    select_testlike_dates,
    train_for_anchor,
    window_bounds,
)


FEATURE_GROUPS = ["momentum_shape"]
TOP_K = 30
WEIGHT_RULE = "score_positive"

LOCAL_SPECS = [
    {
        "name": "current_d4_mcw10_l5_lr005",
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
        "name": "d3_mcw10_l5_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 3,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 10,
            "reg_lambda": 5.0,
        },
    },
    {
        "name": "d3_mcw20_l5_lr005",
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
        "name": "d3_mcw20_l10_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 3,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d4_mcw20_l5_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 5.0,
        },
    },
    {
        "name": "d4_mcw10_l10_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 10,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d4_mcw20_l10_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d4_mcw40_l10_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 40,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d4_mcw20_l20_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 20.0,
        },
    },
    {
        "name": "d5_mcw10_l5_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 5,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 10,
            "reg_lambda": 5.0,
        },
    },
    {
        "name": "d5_mcw10_l10_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 5,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 10,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d5_mcw20_l10_lr005",
        "params": {
            "n_estimators": 500,
            "max_depth": 5,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d4_mcw10_l5_lr003",
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
        "name": "d4_mcw20_l10_lr003",
        "params": {
            "n_estimators": 800,
            "max_depth": 4,
            "learning_rate": 0.03,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d3_mcw20_l10_lr003",
        "params": {
            "n_estimators": 800,
            "max_depth": 3,
            "learning_rate": 0.03,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d5_mcw20_l10_lr003",
        "params": {
            "n_estimators": 800,
            "max_depth": 5,
            "learning_rate": 0.03,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d4_mcw20_l10_lr005_sub07",
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.7,
            "colsample_bytree": 0.7,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
    {
        "name": "d3_mcw20_l10_lr005_sub07",
        "params": {
            "n_estimators": 500,
            "max_depth": 3,
            "learning_rate": 0.05,
            "subsample": 0.7,
            "colsample_bytree": 0.7,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
        },
    },
]


def evaluate_spec(
    panel: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    anchors: list[pd.Timestamp],
    spec: dict,
    feature_cols: list[str],
) -> dict:
    rows = []
    for anchor in anchors:
        model = train_for_anchor(panel, anchor, spec["params"], feature_cols)
        pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
        pred_df = pred_df.assign(score=model.predict(pred_df[feature_cols]))
        labeled = pred_df.dropna(subset=[TARGET_COLUMN]).copy()
        ic = rank_ic(labeled[TARGET_COLUMN].to_numpy(), labeled["score"].to_numpy(), labeled["date"].to_numpy())
        weights = build_portfolio(
            pred_df.set_index("stock_code")["score"],
            top_k=TOP_K,
            weight_rule=WEIGHT_RULE,
        )
        start, end = window_bounds(panel, anchor, HOLD_DAYS)
        score = score_window(weights, prices, index_df, start, end)
        rows.append(
            {
                "anchor": anchor.date().isoformat(),
                "rank_ic": ic,
                "excess_5d": score["excess_return"],
                "benchmark_5d": score["benchmark_return"],
            }
        )
    details = pd.DataFrame(rows)
    return {
        "name": spec["name"],
        "params": spec["params"],
        "mean_rank_ic": float(details["rank_ic"].mean()),
        "mean_excess_5d": float(details["excess_5d"].mean()),
        "min_excess_5d": float(details["excess_5d"].min()),
        "win_rate_5d": float((details["excess_5d"] > 0).mean()),
        "details": details,
    }


def format_params(params: dict) -> str:
    return ", ".join(f"{key}={value}" for key, value in params.items())


def write_report(
    path: Path,
    as_of: pd.Timestamp,
    anchors: list[pd.Timestamp],
    auc: float,
    results: list[dict],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Local XGBoost Sweep Log",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- As-of date: {as_of.date()}",
        f"- Feature groups: {','.join(FEATURE_GROUPS)}",
        f"- Portfolio: top_k={TOP_K}, weight_rule={WEIGHT_RULE}",
        f"- Holding window: {HOLD_DAYS} trading days",
        "- Anchor selection feature groups: baseline",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        "",
        "## Summary",
        "",
        "| spec | mean IC | mean excess 5d | min excess 5d | win 5d | params |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for result in sorted(results, key=lambda r: (r["mean_excess_5d"], r["min_excess_5d"]), reverse=True):
        lines.append(
            f"| {result['name']} | {result['mean_rank_ic']:.4f} | "
            f"{result['mean_excess_5d'] * 100:+.3f}% | "
            f"{result['min_excess_5d'] * 100:+.3f}% | {result['win_rate_5d']:.2f} | "
            f"{format_params(result['params'])} |"
        )

    lines.extend(["", "## Per-anchor Details", ""])
    for result in results:
        lines.extend(
            [
                f"### {result['name']}",
                "",
                "| anchor | rank IC | excess 5d | benchmark 5d |",
                "| --- | ---: | ---: | ---: |",
            ]
        )
        for _, row in result["details"].iterrows():
            lines.append(
                f"| {row['anchor']} | {row['rank_ic']:.4f} | "
                f"{row['excess_5d'] * 100:+.3f}% | {row['benchmark_5d'] * 100:+.3f}% |"
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prices", default=str(DATA_DIR / "prices.parquet"))
    parser.add_argument("--index", default=str(DATA_DIR / "index.parquet"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--top-dates", type=int, default=5)
    parser.add_argument("--recent-lookback", type=int, default=80)
    parser.add_argument("--min-stocks-per-date", type=int, default=450)
    parser.add_argument("--negative-multiplier", type=int, default=10)
    parser.add_argument("--max-specs", type=int, default=None)
    parser.add_argument("--report", default="reports/xgboost_local_sweep_log.md")
    args = parser.parse_args()

    print(f">> Loading {args.prices}")
    prices = pd.read_parquet(args.prices)
    prices["stock_code"] = prices["stock_code"].astype(str).str.zfill(6)
    prices["date"] = pd.to_datetime(prices["date"])
    index_df = pd.read_parquet(args.index)
    index_df["date"] = pd.to_datetime(index_df["date"])

    print(">> Building features")
    panel = build_features(prices, index_df=index_df)
    as_of = pd.Timestamp(args.as_of) if args.as_of else pd.Timestamp(panel["date"].max())
    feature_cols = feature_columns(FEATURE_GROUPS)
    anchor_feature_cols = feature_columns([])
    anchor_pred_df = prediction_frame(panel, as_of=as_of).dropna(subset=anchor_feature_cols)
    cutoff = labeled_cutoff_date(panel, as_of)
    anchor_history_df = training_frame(panel, max_date=cutoff).dropna(subset=anchor_feature_cols)

    print(">> Selecting fixed test-like anchors with baseline features")
    anchors, auc, _ = select_testlike_dates(
        history_df=anchor_history_df,
        pred_df=anchor_pred_df,
        panel=panel,
        as_of=as_of,
        feature_cols=anchor_feature_cols,
        top_dates=args.top_dates,
        recent_lookback=args.recent_lookback,
        min_stocks_per_date=args.min_stocks_per_date,
        negative_multiplier=args.negative_multiplier,
    )
    print(f"   adversarial AUC: {auc:.4f}")
    print(f"   anchors: {', '.join(d.date().isoformat() for d in anchors)}")

    specs = LOCAL_SPECS[: args.max_specs] if args.max_specs else LOCAL_SPECS
    results = []
    for spec in specs:
        print(f">> Evaluating {spec['name']}")
        result = evaluate_spec(panel, prices, index_df, anchors, spec, feature_cols)
        print(
            f"   mean={result['mean_excess_5d'] * 100:+.3f}%, "
            f"min={result['min_excess_5d'] * 100:+.3f}%, "
            f"win={result['win_rate_5d']:.2f}, IC={result['mean_rank_ic']:.4f}"
        )
        results.append(result)

    write_report(Path(args.report), as_of, anchors, auc, results)
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
