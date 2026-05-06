"""
Run fixed-anchor feature ablation for the XGBoost CSI500 pipeline.

This script intentionally reuses testlike_xgboost_validation.py for selection,
training, and scoring logic. Its job is only orchestration: evaluate a compact
set of feature groups on the same test-like anchors and write one summary report.

Usage
-----
  python scripts/run_feature_ablation.py
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

from baseline_xgboost import DATA_DIR
from csi500_ml.features import build_features, feature_columns, prediction_frame, training_frame
from stage1_xgboost_sweep import EXPERIMENTS
from testlike_xgboost_validation import (
    HOLD_DAYS,
    evaluate_experiment,
    labeled_cutoff_date,
    select_testlike_dates,
)


ABLATIONS = [
    ("baseline", []),
    ("rank_all", ["rank_all"]),
    ("vol_regime", ["vol_regime"]),
    ("liquidity_log", ["liquidity_log"]),
    ("momentum_shape", ["momentum_shape"]),
    ("mom_ret3", ["mom_ret3"]),
    ("mom_trend_20_5", ["mom_trend_20_5"]),
    ("mom_trend_60_20", ["mom_trend_60_20"]),
    ("mom_ret3_trend_20_5", ["mom_ret3", "mom_trend_20_5"]),
    ("mom_ret3_trend_60_20", ["mom_ret3", "mom_trend_60_20"]),
    ("mom_trend_pair", ["mom_trend_20_5", "mom_trend_60_20"]),
    ("rank_vol", ["rank_all", "vol_regime"]),
    ("rank_liquidity", ["rank_all", "liquidity_log"]),
    ("rank_momentum", ["rank_all", "momentum_shape"]),
    ("index_relative", ["index_relative"]),
    ("momentum_index", ["momentum_shape", "index_relative"]),
    ("rank_liquidity_index", ["rank_all", "liquidity_log", "index_relative"]),
    ("rank_vol_liquidity", ["rank_all", "vol_regime", "liquidity_log"]),
    ("rank_vol_liquidity_momentum", ["rank_all", "vol_regime", "liquidity_log", "momentum_shape"]),
]


def format_groups(groups: list[str]) -> str:
    return ",".join(groups) if groups else "baseline"


def parse_names(value: str | None) -> set[str] | None:
    names = {item.strip() for item in (value or "").split(",") if item.strip()}
    return names or None


def best_result(results: list[dict]) -> dict:
    return max(
        results,
        key=lambda r: (
            r["mean_excess_5d"],
            r["min_excess_5d"],
            r["win_rate_5d"],
            r["mean_rank_ic"],
        ),
    )


def evaluate_feature_set(
    panel: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    anchors: list[pd.Timestamp],
    name: str,
    groups: list[str],
    max_experiments: int | None,
) -> dict:
    feature_cols = feature_columns(groups)
    specs = EXPERIMENTS[:max_experiments] if max_experiments else EXPERIMENTS
    results = []
    print(f">> Ablation {name}: {format_groups(groups)} ({len(feature_cols)} features)")
    for spec in specs:
        result = evaluate_experiment(panel, prices, index_df, anchors, spec, feature_cols)
        print(
            f"   {spec['name']}: mean={result['mean_excess_5d'] * 100:+.3f}%, "
            f"min={result['min_excess_5d'] * 100:+.3f}%, win={result['win_rate_5d']:.2f}, "
            f"IC={result['mean_rank_ic']:.4f}"
        )
        results.append(result)
    best = best_result(results)
    return {
        "name": name,
        "groups": groups,
        "feature_count": len(feature_cols),
        "best": best,
        "results": results,
    }


def write_report(
    path: Path,
    as_of: pd.Timestamp,
    anchors: list[pd.Timestamp],
    auc: float,
    ablation_results: list[dict],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Feature Ablation Log",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- As-of date: {as_of.date()}",
        f"- Holding window: {HOLD_DAYS} trading days",
        "- Anchor selection feature groups: baseline",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        "",
        "## Best By Feature Set",
        "",
        "| feature set | groups | n_features | best experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |",
        "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in sorted(ablation_results, key=lambda r: r["best"]["mean_excess_5d"], reverse=True):
        best = item["best"]
        lines.append(
            f"| {item['name']} | {format_groups(item['groups'])} | {item['feature_count']} | "
            f"{best['name']} | {best['top_k']} | {best['mean_rank_ic']:.4f} | "
            f"{best['mean_excess_5d'] * 100:+.3f}% | {best['min_excess_5d'] * 100:+.3f}% | "
            f"{best['win_rate_5d']:.2f} |"
        )

    lines.extend(["", "## Full Results", ""])
    for item in ablation_results:
        lines.extend(
            [
                f"### {item['name']}",
                "",
                f"- Groups: `{format_groups(item['groups'])}`",
                f"- Feature count: {item['feature_count']}",
                "",
                "| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |",
                "| --- | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for result in sorted(item["results"], key=lambda r: r["mean_excess_5d"], reverse=True):
            lines.append(
                f"| {result['name']} | {result['top_k']} | {result['mean_rank_ic']:.4f} | "
                f"{result['mean_excess_5d'] * 100:+.3f}% | "
                f"{result['min_excess_5d'] * 100:+.3f}% | {result['win_rate_5d']:.2f} |"
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
    parser.add_argument("--max-experiments", type=int, default=None)
    parser.add_argument("--only", default=None, help="Comma-separated ablation names to run.")
    parser.add_argument("--report", default="reports/feature_ablation_log.md")
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
    if not anchors:
        raise RuntimeError("No eligible test-like validation dates selected.")
    print(f"   adversarial AUC: {auc:.4f}")
    print(f"   anchors: {', '.join(d.date().isoformat() for d in anchors)}")

    only = parse_names(args.only)
    selected_ablations = [(name, groups) for name, groups in ABLATIONS if only is None or name in only]
    if only is not None:
        missing = sorted(only - {name for name, _ in selected_ablations})
        if missing:
            raise ValueError(f"Unknown ablation names: {missing}")

    ablation_results = []
    for name, groups in selected_ablations:
        ablation_results.append(
            evaluate_feature_set(panel, prices, index_df, anchors, name, groups, args.max_experiments)
        )

    write_report(Path(args.report), as_of, anchors, auc, ablation_results)
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
