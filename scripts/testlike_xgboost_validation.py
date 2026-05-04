"""
Test-like rolling validation for the CSI500 XGBoost pipeline.

This script is an experiment gate for feature and parameter changes. It uses
adversarial validation to find historical as-of dates whose feature distribution
resembles the latest prediction date, then evaluates existing XGBoost configs
by building portfolios and scoring future 5-trading-day excess returns.

Usage
-----
  python scripts/testlike_xgboost_validation.py
  python scripts/testlike_xgboost_validation.py --as-of 20260430 --top-dates 5
  python scripts/testlike_xgboost_validation.py --feature-groups rank_all,vol_regime
"""
from __future__ import annotations

import argparse
from datetime import datetime
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
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from baseline_xgboost import DATA_DIR, EMBARGO_DAYS, VAL_DAYS, build_portfolio, rank_ic
from csi500_ml.features import (
    FORWARD_HORIZON,
    TARGET_COLUMN,
    build_features,
    feature_columns,
    prediction_frame,
    training_frame,
)
from score_submission import score_window
from stage1_xgboost_sweep import EXPERIMENTS, RANDOM_SEED

HOLD_DAYS = 5


def parse_groups(value: str | None) -> list[str]:
    return [g.strip() for g in (value or "").split(",") if g.strip()]


def trading_date_at(dates: np.ndarray, idx: int) -> pd.Timestamp:
    if idx < 0 or idx >= len(dates):
        raise IndexError(idx)
    return pd.Timestamp(dates[idx])


def labeled_cutoff_date(panel: pd.DataFrame, as_of: pd.Timestamp) -> pd.Timestamp:
    dates = np.sort(panel["date"].unique())
    as_of_idx = int(np.searchsorted(dates, np.datetime64(as_of)))
    if as_of_idx < FORWARD_HORIZON:
        raise RuntimeError("Not enough history before as_of.")
    return trading_date_at(dates, as_of_idx - FORWARD_HORIZON)


def fit_adversarial_classifier(
    history_df: pd.DataFrame,
    pred_df: pd.DataFrame,
    feature_cols: list[str],
    negative_multiplier: int,
) -> tuple[xgb.XGBClassifier, float]:
    positives = pred_df[feature_cols].copy()
    negatives = history_df[feature_cols].copy()
    n_neg = min(len(negatives), len(positives) * negative_multiplier)
    negatives = negatives.sample(n=n_neg, random_state=RANDOM_SEED)

    x_adv = pd.concat([positives, negatives], ignore_index=True)
    y_adv = np.r_[np.ones(len(positives)), np.zeros(len(negatives))]

    x_train, x_eval, y_train, y_eval = train_test_split(
        x_adv,
        y_adv,
        test_size=0.25,
        random_state=RANDOM_SEED,
        stratify=y_adv,
    )
    clf = xgb.XGBClassifier(
        n_estimators=120,
        max_depth=3,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        min_child_weight=10,
        reg_lambda=5.0,
        objective="binary:logistic",
        eval_metric="auc",
        tree_method="hist",
        n_jobs=-1,
        random_state=RANDOM_SEED,
    )
    clf.fit(x_train, y_train, eval_set=[(x_eval, y_eval)], verbose=False)
    auc = roc_auc_score(y_eval, clf.predict_proba(x_eval)[:, 1])
    return clf, float(auc)


def select_testlike_dates(
    history_df: pd.DataFrame,
    pred_df: pd.DataFrame,
    panel: pd.DataFrame,
    as_of: pd.Timestamp,
    feature_cols: list[str],
    top_dates: int,
    recent_lookback: int,
    min_stocks_per_date: int,
    negative_multiplier: int,
) -> tuple[list[pd.Timestamp], float, pd.DataFrame]:
    clf, auc = fit_adversarial_classifier(history_df, pred_df, feature_cols, negative_multiplier)
    scored = history_df[["date", "stock_code"]].copy()
    scored["p_test_like"] = clf.predict_proba(history_df[feature_cols])[:, 1]

    counts = panel.dropna(subset=feature_cols).groupby("date")["stock_code"].nunique()
    date_scores = (
        scored.groupby("date")["p_test_like"]
        .agg(["mean", "median", "max"])
        .join(counts.rename("n_stocks"), how="left")
        .reset_index()
    )

    cutoff = labeled_cutoff_date(panel, as_of)
    eligible_dates = np.sort(history_df.loc[history_df["date"] <= cutoff, "date"].unique())
    recent_dates = set(pd.Timestamp(d) for d in eligible_dates[-recent_lookback:])
    eligible = date_scores[
        (date_scores["date"].map(pd.Timestamp).isin(recent_dates))
        & (date_scores["n_stocks"] >= min_stocks_per_date)
    ].copy()
    eligible = eligible.sort_values(["mean", "median"], ascending=False)
    selected = [pd.Timestamp(d) for d in eligible["date"].head(top_dates)]
    selected = sorted(selected)
    return selected, auc, eligible


def split_internal_train_val(
    train_pool: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    dates = np.sort(train_pool["date"].unique())
    if len(dates) < VAL_DAYS + EMBARGO_DAYS + 20:
        raise RuntimeError("Not enough dates for internal training split.")
    val_start = trading_date_at(dates, len(dates) - VAL_DAYS)
    train_end = trading_date_at(dates, len(dates) - (VAL_DAYS + EMBARGO_DAYS + 1))
    train_df = train_pool[train_pool["date"] <= train_end].copy()
    val_df = train_pool[train_pool["date"] >= val_start].copy()
    return train_df, val_df


def train_for_anchor(
    panel: pd.DataFrame,
    anchor: pd.Timestamp,
    params: dict,
    feature_cols: list[str],
) -> xgb.XGBRegressor:
    dates = np.sort(panel["date"].unique())
    anchor_idx = int(np.searchsorted(dates, np.datetime64(anchor)))
    cutoff = trading_date_at(dates, anchor_idx - FORWARD_HORIZON)
    train_pool = training_frame(panel, max_date=cutoff)
    train_pool = train_pool.dropna(subset=feature_cols + [TARGET_COLUMN]).copy()
    train_df, val_df = split_internal_train_val(train_pool)
    return train_xgboost_with_columns(train_df, val_df, params, feature_cols)


def train_xgboost_with_columns(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    params: dict,
    feature_cols: list[str],
) -> xgb.XGBRegressor:
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
        eval_set=[(val_df[feature_cols], val_df[TARGET_COLUMN])],
        verbose=False,
    )
    return model


def window_bounds(panel: pd.DataFrame, anchor: pd.Timestamp, hold_days: int) -> tuple[pd.Timestamp, pd.Timestamp]:
    dates = np.sort(panel["date"].unique())
    anchor_idx = int(np.searchsorted(dates, np.datetime64(anchor)))
    start = trading_date_at(dates, anchor_idx + 1)
    end = trading_date_at(dates, anchor_idx + hold_days)
    return start, end


def evaluate_experiment(
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
        pred_df = prediction_frame(panel, as_of=anchor)
        pred_df = pred_df.dropna(subset=feature_cols).copy()
        pred_df = pred_df.assign(score=model.predict(pred_df[feature_cols]))

        labeled = pred_df.dropna(subset=[TARGET_COLUMN]).copy()
        ic = rank_ic(
            labeled[TARGET_COLUMN].to_numpy(),
            labeled["score"].to_numpy(),
            labeled["date"].to_numpy(),
        )

        weights = build_portfolio(pred_df.set_index("stock_code")["score"], top_k=spec["top_k"])
        row = {
            "anchor": anchor.date().isoformat(),
            "rank_ic": ic,
        }
        start, end = window_bounds(panel, anchor, HOLD_DAYS)
        result = score_window(weights, prices, index_df, start, end)
        row["excess_5d"] = result["excess_return"]
        row["portfolio_5d"] = result["portfolio_return"]
        row["benchmark_5d"] = result["benchmark_return"]
        rows.append(row)

    df = pd.DataFrame(rows)
    return {
        "name": spec["name"],
        "top_k": spec["top_k"],
        "mean_rank_ic": float(df["rank_ic"].mean()),
        "mean_excess_5d": float(df["excess_5d"].mean()),
        "min_excess_5d": float(df["excess_5d"].min()),
        "win_rate_5d": float((df["excess_5d"] > 0).mean()),
        "details": df,
    }


def write_report(
    path: Path,
    as_of: pd.Timestamp,
    enabled_groups: list[str],
    feature_cols: list[str],
    anchor_groups: list[str],
    anchor_feature_cols: list[str],
    auc: float,
    anchors: list[pd.Timestamp],
    date_scores: pd.DataFrame,
    results: list[dict],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Test-like XGBoost Validation",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- As-of date: {as_of.date()}",
        f"- Feature groups: {', '.join(enabled_groups) if enabled_groups else 'baseline'}",
        f"- Feature count: {len(feature_cols)}",
        f"- Anchor selection feature groups: {', '.join(anchor_groups) if anchor_groups else 'baseline'}",
        f"- Anchor selection feature count: {len(anchor_feature_cols)}",
        f"- Holding window: {HOLD_DAYS} trading days",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        "",
        "## Selected Date Diagnostics",
        "",
        "| date | mean p_test_like | median | max | n_stocks |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    selected_set = {d.date().isoformat() for d in anchors}
    for _, row in date_scores.head(12).iterrows():
        marker = " (selected)" if pd.Timestamp(row["date"]).date().isoformat() in selected_set else ""
        lines.append(
            f"| {pd.Timestamp(row['date']).date()}{marker} | {row['mean']:.6f} | "
            f"{row['median']:.6f} | {row['max']:.6f} | {int(row['n_stocks'])} |"
        )

    lines.extend(
        [
            "",
            "## Experiment Summary",
            "",
            "| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for result in sorted(results, key=lambda x: x["mean_excess_5d"], reverse=True):
        lines.append(
            f"| {result['name']} | {result['top_k']} | {result['mean_rank_ic']:.4f} | "
            f"{result['mean_excess_5d'] * 100:+.3f}% | "
            f"{result['min_excess_5d'] * 100:+.3f}% | {result['win_rate_5d']:.2f} |"
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
    parser.add_argument(
        "--feature-groups",
        default="",
        help="Comma-separated optional feature groups, e.g. rank_all,vol_regime,liquidity_log",
    )
    parser.add_argument(
        "--anchor-feature-groups",
        default="",
        help=(
            "Feature groups used only for adversarial anchor selection. Defaults to baseline "
            "so feature ablations are compared on the same anchor-selection basis."
        ),
    )
    parser.add_argument("--max-experiments", type=int, default=None)
    parser.add_argument("--report", default="reports/testlike_validation_log.md")
    args = parser.parse_args()

    print(f">> Loading {args.prices}")
    prices = pd.read_parquet(args.prices)
    prices["stock_code"] = prices["stock_code"].astype(str).str.zfill(6)
    prices["date"] = pd.to_datetime(prices["date"])
    index_df = pd.read_parquet(args.index)
    index_df["date"] = pd.to_datetime(index_df["date"])

    print(">> Building features")
    panel = build_features(prices)
    enabled_groups = parse_groups(args.feature_groups)
    anchor_groups = parse_groups(args.anchor_feature_groups)
    feature_cols = feature_columns(enabled_groups)
    anchor_feature_cols = feature_columns(anchor_groups)
    print(f"   feature groups: {', '.join(enabled_groups) if enabled_groups else 'baseline'}")
    print(f"   feature count: {len(feature_cols)}")
    print(f"   anchor feature groups: {', '.join(anchor_groups) if anchor_groups else 'baseline'}")
    print(f"   anchor feature count: {len(anchor_feature_cols)}")
    as_of = pd.Timestamp(args.as_of) if args.as_of else pd.Timestamp(panel["date"].max())
    pred_df = prediction_frame(panel, as_of=as_of).dropna(subset=feature_cols)
    anchor_pred_df = prediction_frame(panel, as_of=as_of).dropna(subset=anchor_feature_cols)
    cutoff = labeled_cutoff_date(panel, as_of)
    anchor_history_df = training_frame(panel, max_date=cutoff).dropna(subset=anchor_feature_cols)

    print(">> Selecting test-like validation dates")
    anchors, auc, date_scores = select_testlike_dates(
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

    specs = EXPERIMENTS[: args.max_experiments] if args.max_experiments else EXPERIMENTS
    results = []
    for spec in specs:
        print(f">> Evaluating {spec['name']}")
        result = evaluate_experiment(panel, prices, index_df, anchors, spec, feature_cols)
        print(
            f"   mean excess 5d={result['mean_excess_5d'] * 100:+.3f}%, "
            f"mean IC={result['mean_rank_ic']:.4f}"
        )
        results.append(result)

    write_report(
        Path(args.report),
        as_of,
        enabled_groups,
        feature_cols,
        anchor_groups,
        anchor_feature_cols,
        auc,
        anchors,
        date_scores,
        results,
    )
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
