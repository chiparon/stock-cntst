"""
Run portfolio-construction ablation for the selected XGBoost signal.

The model and feature set are fixed by default to the current best gate result
(`concentrated_top30` parameters + momentum_shape features). This script trains
one model per anchor, then reuses its scores to compare top_k and weighting
rules under the same 5-day excess-return gate.

Usage
-----
  python scripts/run_portfolio_ablation.py
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
from stage1_xgboost_sweep import EXPERIMENTS
from testlike_xgboost_validation import (
    HOLD_DAYS,
    labeled_cutoff_date,
    select_testlike_dates,
    train_for_anchor,
    window_bounds,
)


DEFAULT_EXPERIMENT = "concentrated_top30"
DEFAULT_FEATURE_GROUPS = ["momentum_shape"]
TOP_K_VALUES = [30, 35, 40, 45, 50, 60]
WEIGHT_RULES = ["rank", "equal", "score_positive"]


def experiment_by_name(name: str) -> dict:
    for spec in EXPERIMENTS:
        if spec["name"] == name:
            return spec
    available = ", ".join(spec["name"] for spec in EXPERIMENTS)
    raise ValueError(f"Unknown experiment {name!r}; available: {available}")


def parse_groups(value: str | None) -> list[str]:
    return [g.strip() for g in (value or "").split(",") if g.strip()]


def parse_ints(value: str) -> list[int]:
    return [int(part.strip()) for part in value.split(",") if part.strip()]


def evaluate_weights(
    weights: pd.Series,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    panel: pd.DataFrame,
    anchor: pd.Timestamp,
) -> dict:
    start, end = window_bounds(panel, anchor, HOLD_DAYS)
    result = score_window(weights, prices, index_df, start, end)
    return {
        "excess_5d": result["excess_return"],
        "portfolio_5d": result["portfolio_return"],
        "benchmark_5d": result["benchmark_return"],
    }


def summarize(rows: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    grouped = df.groupby(["top_k", "weight_rule"], as_index=False).agg(
        mean_excess_5d=("excess_5d", "mean"),
        min_excess_5d=("excess_5d", "min"),
        win_rate_5d=("excess_5d", lambda s: float((s > 0).mean())),
        mean_rank_ic=("rank_ic", "mean"),
    )
    return grouped.sort_values(
        ["mean_excess_5d", "min_excess_5d", "win_rate_5d", "mean_rank_ic"],
        ascending=False,
    )


def write_report(
    path: Path,
    as_of: pd.Timestamp,
    experiment_name: str,
    feature_groups: list[str],
    anchors: list[pd.Timestamp],
    auc: float,
    summary: pd.DataFrame,
    details: pd.DataFrame,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Portfolio Ablation Log",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- As-of date: {as_of.date()}",
        f"- Experiment params: {experiment_name}",
        f"- Feature groups: {','.join(feature_groups) if feature_groups else 'baseline'}",
        f"- Holding window: {HOLD_DAYS} trading days",
        "- Anchor selection feature groups: baseline",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        "",
        "## Summary",
        "",
        "| top_k | weight rule | mean IC | mean excess 5d | min excess 5d | win 5d |",
        "| ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for _, row in summary.iterrows():
        lines.append(
            f"| {int(row['top_k'])} | {row['weight_rule']} | {row['mean_rank_ic']:.4f} | "
            f"{row['mean_excess_5d'] * 100:+.3f}% | {row['min_excess_5d'] * 100:+.3f}% | "
            f"{row['win_rate_5d']:.2f} |"
        )

    lines.extend(
        [
            "",
            "## Details",
            "",
            "| anchor | top_k | weight rule | rank IC | excess 5d | benchmark 5d |",
            "| --- | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for _, row in details.sort_values(["anchor", "top_k", "weight_rule"]).iterrows():
        lines.append(
            f"| {row['anchor']} | {int(row['top_k'])} | {row['weight_rule']} | "
            f"{row['rank_ic']:.4f} | {row['excess_5d'] * 100:+.3f}% | "
            f"{row['benchmark_5d'] * 100:+.3f}% |"
        )

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prices", default=str(DATA_DIR / "prices.parquet"))
    parser.add_argument("--index", default=str(DATA_DIR / "index.parquet"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--experiment", default=DEFAULT_EXPERIMENT)
    parser.add_argument("--feature-groups", default=",".join(DEFAULT_FEATURE_GROUPS))
    parser.add_argument("--top-k-values", default=",".join(str(v) for v in TOP_K_VALUES))
    parser.add_argument("--weight-rules", default=",".join(WEIGHT_RULES))
    parser.add_argument("--top-dates", type=int, default=5)
    parser.add_argument("--recent-lookback", type=int, default=80)
    parser.add_argument("--min-stocks-per-date", type=int, default=450)
    parser.add_argument("--negative-multiplier", type=int, default=10)
    parser.add_argument("--report", default="reports/portfolio_ablation_log.md")
    args = parser.parse_args()

    spec = experiment_by_name(args.experiment)
    feature_groups = parse_groups(args.feature_groups)
    feature_cols = feature_columns(feature_groups)
    top_k_values = parse_ints(args.top_k_values)
    weight_rules = parse_groups(args.weight_rules)

    print(f">> Loading {args.prices}")
    prices = pd.read_parquet(args.prices)
    prices["stock_code"] = prices["stock_code"].astype(str).str.zfill(6)
    prices["date"] = pd.to_datetime(prices["date"])
    index_df = pd.read_parquet(args.index)
    index_df["date"] = pd.to_datetime(index_df["date"])

    print(">> Building features")
    panel = build_features(prices)
    as_of = pd.Timestamp(args.as_of) if args.as_of else pd.Timestamp(panel["date"].max())
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

    rows = []
    for anchor in anchors:
        print(f">> Training anchor {anchor.date()}")
        model = train_for_anchor(panel, anchor, spec["params"], feature_cols)
        pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
        pred_df = pred_df.assign(score=model.predict(pred_df[feature_cols]))
        labeled = pred_df.dropna(subset=[TARGET_COLUMN]).copy()
        ic = rank_ic(labeled[TARGET_COLUMN].to_numpy(), labeled["score"].to_numpy(), labeled["date"].to_numpy())
        scores = pred_df.set_index("stock_code")["score"]
        for top_k in top_k_values:
            for rule in weight_rules:
                weights = build_portfolio(scores, top_k=top_k, weight_rule=rule)
                result = evaluate_weights(weights, prices, index_df, panel, anchor)
                row = {
                    "anchor": anchor.date().isoformat(),
                    "top_k": top_k,
                    "weight_rule": rule,
                    "rank_ic": ic,
                    **result,
                }
                print(
                    f"   top_k={top_k} {rule}: excess={result['excess_5d'] * 100:+.3f}%"
                )
                rows.append(row)

    details = pd.DataFrame(rows)
    summary = summarize(rows)
    write_report(Path(args.report), as_of, args.experiment, feature_groups, anchors, auc, summary, details)
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
