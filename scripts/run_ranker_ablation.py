"""
Evaluate XGBRanker as the first week-2 XGBoost research branch.

The experiment is intentionally isolated: anchors, features, portfolio
construction, and parameter scale stay aligned with the current best regressor
candidate. Only the training objective and ranking labels change.

Usage
-----
  python scripts/run_ranker_ablation.py
  python scripts/run_ranker_ablation.py --top-dates 2 --label-variants rank_decile
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

import numpy as np
import pandas as pd
import xgboost as xgb

from baseline_xgboost import DATA_DIR, rank_ic
from csi500_ml.features import (
    FORWARD_HORIZON,
    TARGET_COLUMN,
    build_features,
    feature_columns,
    prediction_frame,
    training_frame,
)
from csi500_ml.portfolio import build_portfolio
from score_submission import score_window
from stage1_xgboost_sweep import RANDOM_SEED
from testlike_xgboost_validation import (
    HOLD_DAYS,
    labeled_cutoff_date,
    select_testlike_dates,
    split_internal_train_val,
    train_for_anchor,
    trading_date_at,
    window_bounds,
)


DEFAULT_FEATURE_GROUPS = ["momentum_shape"]
TOP_K = 30
WEIGHT_RULE = "score_positive"

CURRENT_PARAMS = {
    "n_estimators": 500,
    "max_depth": 4,
    "learning_rate": 0.05,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "min_child_weight": 10,
    "reg_lambda": 5.0,
}

LABEL_VARIANTS = ["rank_decile", "top20_binary", "rank_ventile"]


def parse_groups(value: str | None) -> list[str]:
    return [g.strip() for g in (value or "").split(",") if g.strip()]


def parse_variants(value: str | None) -> list[str]:
    variants = [v.strip() for v in (value or "").split(",") if v.strip()]
    variants = variants or LABEL_VARIANTS
    unknown = sorted(set(variants) - set(LABEL_VARIANTS))
    if unknown:
        raise ValueError(f"Unknown label variants: {unknown}; available: {LABEL_VARIANTS}")
    return variants


def format_groups(groups: list[str]) -> str:
    return ",".join(groups) if groups else "baseline"


def sorted_for_ranker(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(["date", "stock_code"]).copy()


def group_sizes(df: pd.DataFrame) -> np.ndarray:
    return df.groupby("date", sort=False).size().to_numpy(dtype=np.uint32)


def ranking_label(df: pd.DataFrame, variant: str) -> pd.Series:
    ranks = df.groupby("date")[TARGET_COLUMN].rank(method="average", pct=True)
    if variant == "rank_decile":
        return np.floor((ranks * 10).clip(upper=9.999)).astype(np.uint32)
    if variant == "top20_binary":
        return (ranks >= 0.8).astype(np.uint32)
    if variant == "rank_ventile":
        return np.floor((ranks * 20).clip(upper=19.999)).astype(np.uint32)
    raise ValueError(f"Unknown label variant {variant!r}")


def train_ranker_with_columns(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    feature_cols: list[str],
    label_variant: str,
) -> xgb.XGBRanker:
    train_sorted = sorted_for_ranker(train_df)
    val_sorted = sorted_for_ranker(val_df)
    model = xgb.XGBRanker(
        **CURRENT_PARAMS,
        objective="rank:pairwise",
        eval_metric="ndcg@30",
        tree_method="hist",
        n_jobs=-1,
        early_stopping_rounds=30,
        random_state=RANDOM_SEED,
    )
    model.fit(
        train_sorted[feature_cols],
        ranking_label(train_sorted, label_variant),
        group=group_sizes(train_sorted),
        eval_set=[(val_sorted[feature_cols], ranking_label(val_sorted, label_variant))],
        eval_group=[group_sizes(val_sorted)],
        verbose=False,
    )
    return model


def train_ranker_for_anchor(
    panel: pd.DataFrame,
    anchor: pd.Timestamp,
    feature_cols: list[str],
    label_variant: str,
) -> xgb.XGBRanker:
    dates = np.sort(panel["date"].unique())
    anchor_idx = int(np.searchsorted(dates, np.datetime64(anchor)))
    cutoff = trading_date_at(dates, anchor_idx - FORWARD_HORIZON)
    train_pool = training_frame(panel, max_date=cutoff)
    train_pool = train_pool.dropna(subset=feature_cols + [TARGET_COLUMN]).copy()
    train_df, val_df = split_internal_train_val(train_pool)
    return train_ranker_with_columns(train_df, val_df, feature_cols, label_variant)


def evaluate_scores(
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
        "portfolio_5d": score["portfolio_return"],
        "benchmark_5d": score["benchmark_return"],
    }


def evaluate_regressor_baseline(
    panel: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    anchors: list[pd.Timestamp],
    feature_cols: list[str],
) -> list[dict]:
    rows = []
    for anchor in anchors:
        model = train_for_anchor(panel, anchor, CURRENT_PARAMS, feature_cols)
        pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
        pred_df["score"] = model.predict(pred_df[feature_cols])
        result = evaluate_scores(pred_df, prices, index_df, panel, anchor)
        rows.append({"model": "regressor_current", "label_variant": "raw_return", "anchor": anchor.date().isoformat(), **result})
    return rows


def evaluate_ranker_variant(
    panel: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    anchors: list[pd.Timestamp],
    feature_cols: list[str],
    label_variant: str,
) -> list[dict]:
    rows = []
    for anchor in anchors:
        model = train_ranker_for_anchor(panel, anchor, feature_cols, label_variant)
        pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
        pred_df["score"] = model.predict(pred_df[feature_cols])
        result = evaluate_scores(pred_df, prices, index_df, panel, anchor)
        rows.append({"model": "xgb_ranker", "label_variant": label_variant, "anchor": anchor.date().isoformat(), **result})
    return rows


def summarize(rows: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    return (
        df.groupby(["model", "label_variant"], as_index=False)
        .agg(
            mean_rank_ic=("rank_ic", "mean"),
            mean_excess_5d=("excess_5d", "mean"),
            min_excess_5d=("excess_5d", "min"),
            win_rate_5d=("excess_5d", lambda s: float((s > 0).mean())),
        )
        .sort_values(["mean_excess_5d", "min_excess_5d", "win_rate_5d", "mean_rank_ic"], ascending=False)
    )


def write_report(
    path: Path,
    as_of: pd.Timestamp,
    feature_groups: list[str],
    anchors: list[pd.Timestamp],
    auc: float,
    label_variants: list[str],
    rows: list[dict],
) -> None:
    summary = summarize(rows)
    details = pd.DataFrame(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Week 2 XGBRanker Ablation",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Context: week1 submission is closed; this is week2 XGBoost-only research.",
        f"- As-of date: {as_of.date()}",
        f"- Feature groups: {format_groups(feature_groups)}",
        f"- Portfolio: top_k={TOP_K}, weight_rule={WEIGHT_RULE}",
        f"- Holding window: {HOLD_DAYS} trading days",
        "- Anchor selection feature groups: baseline",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        f"- Ranker label variants: {', '.join(label_variants)}",
        "",
        "## Summary",
        "",
        "| model | label variant | mean IC | mean excess 5d | min excess 5d | win 5d |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for _, row in summary.iterrows():
        lines.append(
            f"| {row['model']} | {row['label_variant']} | {row['mean_rank_ic']:.4f} | "
            f"{row['mean_excess_5d'] * 100:+.3f}% | {row['min_excess_5d'] * 100:+.3f}% | "
            f"{row['win_rate_5d']:.2f} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation Rules",
            "",
            "- Treat `regressor_current` as the control. Ranker is accepted only if it improves mean excess without weakening worst-window excess.",
            "- Rank IC is diagnostic; the primary selector remains 5-trading-day excess return versus CSI500.",
            "- Keep feature groups and portfolio fixed until the objective comparison is settled.",
            "",
            "## Details",
            "",
            "| anchor | model | label variant | rank IC | excess 5d | portfolio 5d | benchmark 5d |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for _, row in details.sort_values(["anchor", "model", "label_variant"]).iterrows():
        lines.append(
            f"| {row['anchor']} | {row['model']} | {row['label_variant']} | {row['rank_ic']:.4f} | "
            f"{row['excess_5d'] * 100:+.3f}% | {row['portfolio_5d'] * 100:+.3f}% | "
            f"{row['benchmark_5d'] * 100:+.3f}% |"
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prices", default=str(DATA_DIR / "prices.parquet"))
    parser.add_argument("--index", default=str(DATA_DIR / "index.parquet"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--feature-groups", default=",".join(DEFAULT_FEATURE_GROUPS))
    parser.add_argument("--label-variants", default=",".join(LABEL_VARIANTS))
    parser.add_argument("--top-dates", type=int, default=5)
    parser.add_argument("--recent-lookback", type=int, default=80)
    parser.add_argument("--min-stocks-per-date", type=int, default=450)
    parser.add_argument("--negative-multiplier", type=int, default=10)
    parser.add_argument("--report", default="reports/week2_ranker_ablation_log.md")
    args = parser.parse_args()

    feature_groups = parse_groups(args.feature_groups)
    label_variants = parse_variants(args.label_variants)
    feature_cols = feature_columns(feature_groups)

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

    rows = []
    print(">> Evaluating regressor control")
    rows.extend(evaluate_regressor_baseline(panel, prices, index_df, anchors, feature_cols))
    for label_variant in label_variants:
        print(f">> Evaluating XGBRanker label={label_variant}")
        rows.extend(evaluate_ranker_variant(panel, prices, index_df, anchors, feature_cols, label_variant))

    report_path = Path(args.report)
    write_report(report_path, as_of, feature_groups, anchors, auc, label_variants, rows)
    print(f">> Wrote {report_path}")


if __name__ == "__main__":
    main()
