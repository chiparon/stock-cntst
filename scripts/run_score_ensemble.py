"""
Evaluate regularized score ensembles of XGBoost models.

Models are trained from scratch with XGBoost. Predictions are converted to
cross-sectional percentile ranks before averaging so score scales are
comparable. The portfolio stays at top_k=30 with score_positive weighting.
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
from csi500_ml.xgb_ensemble import ENSEMBLES, MODEL_SPECS, blend_ranked_scores
from score_submission import score_window
from testlike_xgboost_validation import (
    HOLD_DAYS,
    labeled_cutoff_date,
    select_testlike_dates,
    train_for_anchor,
    window_bounds,
)


TOP_K = 30
WEIGHT_RULE = "score_positive"


def train_anchor_models(panel: pd.DataFrame, anchor: pd.Timestamp) -> dict[str, pd.DataFrame]:
    outputs: dict[str, pd.DataFrame] = {}
    for name, spec in MODEL_SPECS.items():
        feature_cols = feature_columns(spec["groups"])
        model = train_for_anchor(panel, anchor, spec["params"], feature_cols)
        pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
        pred_df = pred_df.assign(score=model.predict(pred_df[feature_cols]))
        outputs[name] = pred_df[["date", "stock_code", TARGET_COLUMN, "score"]].copy()
    return outputs


def evaluate_ensemble(
    pred_df: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    panel: pd.DataFrame,
    anchor: pd.Timestamp,
) -> dict:
    labeled = pred_df.dropna(subset=[TARGET_COLUMN]).copy()
    ic = rank_ic(labeled[TARGET_COLUMN].to_numpy(), labeled["score"].to_numpy(), labeled["date"].to_numpy())
    weights = build_portfolio(pred_df.set_index("stock_code")["score"], top_k=TOP_K, weight_rule=WEIGHT_RULE)
    start, end = window_bounds(panel, anchor, HOLD_DAYS)
    score = score_window(weights, prices, index_df, start, end)
    return {
        "rank_ic": ic,
        "excess_5d": score["excess_return"],
        "benchmark_5d": score["benchmark_return"],
    }


def summarize(rows: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    return (
        df.groupby("ensemble", as_index=False)
        .agg(
            mean_rank_ic=("rank_ic", "mean"),
            mean_excess_5d=("excess_5d", "mean"),
            min_excess_5d=("excess_5d", "min"),
            win_rate_5d=("excess_5d", lambda s: float((s > 0).mean())),
        )
        .sort_values(["mean_excess_5d", "min_excess_5d"], ascending=False)
    )


def format_params(params: dict) -> str:
    return ", ".join(f"{key}={value}" for key, value in params.items())


def format_weights(weights: dict[str, float]) -> str:
    return ", ".join(f"{name}={weight:.2f}" for name, weight in weights.items())


def write_report(path: Path, as_of: pd.Timestamp, anchors: list[pd.Timestamp], auc: float, rows: list[dict]) -> None:
    summary = summarize(rows)
    details = pd.DataFrame(rows)
    best = summary.iloc[0]
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Score Ensemble Log",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- As-of date: {as_of.date()}",
        f"- Portfolio: top_k={TOP_K}, weight_rule={WEIGHT_RULE}",
        f"- Holding window: {HOLD_DAYS} trading days",
        "- Anchor selection feature groups: baseline",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        "",
        "## Model Specs",
        "",
        "| model | groups | params |",
        "| --- | --- | --- |",
    ]
    for model_name, spec in MODEL_SPECS.items():
        lines.append(f"| {model_name} | {','.join(spec['groups'])} | {format_params(spec['params'])} |")

    lines.extend(
        [
            "",
            "## Ensemble Weights",
            "",
            "| ensemble | weights |",
            "| --- | --- |",
        ]
    )
    for ensemble_name, weights in ENSEMBLES.items():
        lines.append(f"| {ensemble_name} | {format_weights(weights)} |")

    lines.extend(
        [
            "",
            "## Summary",
            "",
            "| ensemble | mean IC | mean excess 5d | min excess 5d | win 5d |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for _, row in summary.iterrows():
        lines.append(
            f"| {row['ensemble']} | {row['mean_rank_ic']:.4f} | "
            f"{row['mean_excess_5d'] * 100:+.3f}% | {row['min_excess_5d'] * 100:+.3f}% | "
            f"{row['win_rate_5d']:.2f} |"
        )

    lines.extend(
        [
            "",
            "## Details",
            "",
            "| anchor | ensemble | rank IC | excess 5d | benchmark 5d |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
    )
    for _, row in details.sort_values(["anchor", "ensemble"]).iterrows():
        lines.append(
            f"| {row['anchor']} | {row['ensemble']} | {row['rank_ic']:.4f} | "
            f"{row['excess_5d'] * 100:+.3f}% | {row['benchmark_5d'] * 100:+.3f}% |"
        )
    lines.extend(
        [
            "",
            "## Stage Conclusion",
            "",
            f"- Selected ensemble: `{best['ensemble']}`.",
            f"- Best mean excess 5d: {best['mean_excess_5d'] * 100:+.3f}%.",
            f"- Best mean IC: {best['mean_rank_ic']:.4f}.",
            "- The winning blend is still a regularized XGBoost stack, but the cross-sectional rank blend now leans on the complementary rank/liquidity model rather than only momentum models.",
        ]
    )
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
    parser.add_argument("--report", default="reports/regularized_ensemble_log.md")
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
    print(f"   adversarial AUC: {auc:.4f}")
    print(f"   anchors: {', '.join(d.date().isoformat() for d in anchors)}")

    rows = []
    for anchor in anchors:
        print(f">> Training anchor models {anchor.date()}")
        outputs = train_anchor_models(panel, anchor)
        for ensemble_name, weights in ENSEMBLES.items():
            pred_df = blend_ranked_scores(outputs, weights)
            result = evaluate_ensemble(pred_df, prices, index_df, panel, anchor)
            print(f"   {ensemble_name}: excess={result['excess_5d'] * 100:+.3f}%")
            rows.append({"anchor": anchor.date().isoformat(), "ensemble": ensemble_name, **result})

    write_report(Path(args.report), as_of, anchors, auc, rows)
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
