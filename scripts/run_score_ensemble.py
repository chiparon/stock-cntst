"""
Evaluate small score ensembles of XGBoost models.

Models are still trained from scratch with XGBoost. Predictions are converted to
cross-sectional percentile ranks before averaging so score scales are comparable.
The portfolio is fixed to the current best construction: top_k=30 with
score_positive weighting.
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


TOP_K = 30
WEIGHT_RULE = "score_positive"

MODEL_SPECS = {
    "primary_momentum": {
        "groups": ["momentum_shape"],
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
    "robust_momentum": {
        "groups": ["momentum_shape"],
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
    "rank_liquidity": {
        "groups": ["rank_all", "liquidity_log"],
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
}

ENSEMBLES = {
    "primary_only": {"primary_momentum": 1.0},
    "primary_robust_equal": {"primary_momentum": 0.5, "robust_momentum": 0.5},
    "primary_robust_70_30": {"primary_momentum": 0.7, "robust_momentum": 0.3},
    "primary_rankliq_70_30": {"primary_momentum": 0.7, "rank_liquidity": 0.3},
    "all_equal": {"primary_momentum": 1 / 3, "robust_momentum": 1 / 3, "rank_liquidity": 1 / 3},
    "primary_heavy_all": {"primary_momentum": 0.6, "robust_momentum": 0.2, "rank_liquidity": 0.2},
}


def score_to_rank(scores: pd.Series) -> pd.Series:
    return scores.rank(method="average", pct=True)


def train_anchor_models(panel: pd.DataFrame, anchor: pd.Timestamp) -> dict[str, pd.DataFrame]:
    outputs = {}
    for name, spec in MODEL_SPECS.items():
        feature_cols = feature_columns(spec["groups"])
        model = train_for_anchor(panel, anchor, spec["params"], feature_cols)
        pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
        pred_df = pred_df.assign(score=model.predict(pred_df[feature_cols]))
        outputs[name] = pred_df[["date", "stock_code", TARGET_COLUMN, "score"]].copy()
    return outputs


def ensemble_scores(model_outputs: dict[str, pd.DataFrame], weights: dict[str, float]) -> pd.DataFrame:
    merged = None
    score_cols = []
    for model_name, weight in weights.items():
        df = model_outputs[model_name].copy()
        col = f"score_{model_name}"
        df[col] = score_to_rank(df["score"]) * weight
        keep = ["date", "stock_code", TARGET_COLUMN, col]
        if merged is None:
            merged = df[keep]
        else:
            merged = merged.merge(df[["stock_code", col]], on="stock_code", how="inner")
        score_cols.append(col)
    assert merged is not None
    merged["score"] = merged[score_cols].sum(axis=1) / sum(weights.values())
    return merged


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


def write_report(path: Path, as_of: pd.Timestamp, anchors: list[pd.Timestamp], auc: float, rows: list[dict]) -> None:
    summary = summarize(rows)
    details = pd.DataFrame(rows)
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
        "## Summary",
        "",
        "| ensemble | mean IC | mean excess 5d | min excess 5d | win 5d |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for _, row in summary.iterrows():
        lines.append(
            f"| {row['ensemble']} | {row['mean_rank_ic']:.4f} | "
            f"{row['mean_excess_5d'] * 100:+.3f}% | {row['min_excess_5d'] * 100:+.3f}% | "
            f"{row['win_rate_5d']:.2f} |"
        )

    lines.extend(["", "## Details", "", "| anchor | ensemble | rank IC | excess 5d | benchmark 5d |", "| --- | --- | ---: | ---: | ---: |"])
    for _, row in details.sort_values(["anchor", "ensemble"]).iterrows():
        lines.append(
            f"| {row['anchor']} | {row['ensemble']} | {row['rank_ic']:.4f} | "
            f"{row['excess_5d'] * 100:+.3f}% | {row['benchmark_5d'] * 100:+.3f}% |"
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
    parser.add_argument("--report", default="reports/score_ensemble_log.md")
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
            pred_df = ensemble_scores(outputs, weights)
            result = evaluate_ensemble(pred_df, prices, index_df, panel, anchor)
            print(f"   {ensemble_name}: excess={result['excess_5d'] * 100:+.3f}%")
            rows.append({"anchor": anchor.date().isoformat(), "ensemble": ensemble_name, **result})

    write_report(Path(args.report), as_of, anchors, auc, rows)
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
