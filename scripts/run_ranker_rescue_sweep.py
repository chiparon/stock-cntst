"""
Focused rescue sweep for the week-2 XGBRanker branch.

The first Ranker ablation showed that `top20_binary` is the only viable label
variant. This script keeps that label fixed, then checks whether stronger
regularization or more conservative portfolio construction can recover the
worst-window weakness.

Usage
-----
  python scripts/run_ranker_rescue_sweep.py
  python scripts/run_ranker_rescue_sweep.py --max-specs 3 --top-dates 2
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
from run_ranker_ablation import CURRENT_PARAMS, DEFAULT_FEATURE_GROUPS, format_groups, parse_groups, train_ranker_for_anchor


LABEL_VARIANT = "top20_binary"
TOP_K_VALUES = [30, 40, 50]
WEIGHT_RULES = ["score_positive", "rank", "equal"]

RANKER_SPECS = [
    {
        "name": "ranker_current_d4_mcw10_l5_sub08",
        "params": CURRENT_PARAMS,
    },
    {
        "name": "ranker_d3_mcw10_l5_sub08",
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
        "name": "ranker_d3_mcw20_l10_sub08",
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
        "name": "ranker_d3_mcw40_l20_sub08",
        "params": {
            "n_estimators": 500,
            "max_depth": 3,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 40,
            "reg_lambda": 20.0,
        },
    },
    {
        "name": "ranker_d4_mcw20_l10_sub08",
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
        "name": "ranker_d4_mcw40_l20_sub08",
        "params": {
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 40,
            "reg_lambda": 20.0,
        },
    },
    {
        "name": "ranker_d4_mcw20_l10_sub07",
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
        "name": "ranker_d3_mcw20_l10_sub07",
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
    {
        "name": "ranker_d3_mcw40_l20_sub07",
        "params": {
            "n_estimators": 500,
            "max_depth": 3,
            "learning_rate": 0.05,
            "subsample": 0.7,
            "colsample_bytree": 0.7,
            "min_child_weight": 40,
            "reg_lambda": 20.0,
        },
    },
    {
        "name": "ranker_d3_mcw20_l10_lr003_sub08",
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
]


def parse_ints(value: str) -> list[int]:
    return [int(v.strip()) for v in value.split(",") if v.strip()]


def format_params(params: dict) -> str:
    return ", ".join(f"{key}={value}" for key, value in params.items())


def evaluate_portfolios(
    pred_df: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    panel: pd.DataFrame,
    anchor: pd.Timestamp,
    top_k_values: list[int],
    weight_rules: list[str],
) -> list[dict]:
    labeled = pred_df.dropna(subset=[TARGET_COLUMN]).copy()
    ic = rank_ic(labeled[TARGET_COLUMN].to_numpy(), labeled["score"].to_numpy(), labeled["date"].to_numpy())
    rows = []
    for top_k in top_k_values:
        for weight_rule in weight_rules:
            weights = build_portfolio(pred_df.set_index("stock_code")["score"], top_k=top_k, weight_rule=weight_rule)
            start, end = window_bounds(panel, anchor, HOLD_DAYS)
            score = score_window(weights, prices, index_df, start, end)
            rows.append(
                {
                    "top_k": top_k,
                    "weight_rule": weight_rule,
                    "rank_ic": ic,
                    "excess_5d": score["excess_return"],
                    "portfolio_5d": score["portfolio_return"],
                    "benchmark_5d": score["benchmark_return"],
                }
            )
    return rows


def evaluate_regressor_control(
    panel: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    anchors: list[pd.Timestamp],
    feature_cols: list[str],
    top_k_values: list[int],
    weight_rules: list[str],
) -> list[dict]:
    rows = []
    for anchor in anchors:
        model = train_for_anchor(panel, anchor, CURRENT_PARAMS, feature_cols)
        pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
        pred_df["score"] = model.predict(pred_df[feature_cols])
        for result in evaluate_portfolios(pred_df, prices, index_df, panel, anchor, top_k_values, weight_rules):
            rows.append(
                {
                    "model": "regressor_control",
                    "spec": "current_d4_mcw10_l5_sub08",
                    "label_variant": "raw_return",
                    "anchor": anchor.date().isoformat(),
                    **result,
                }
            )
    return rows


def evaluate_ranker_specs(
    panel: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    anchors: list[pd.Timestamp],
    feature_cols: list[str],
    specs: list[dict],
    top_k_values: list[int],
    weight_rules: list[str],
) -> list[dict]:
    rows = []
    for spec in specs:
        print(f">> Evaluating {spec['name']}")
        for anchor in anchors:
            model = train_ranker_for_anchor(panel, anchor, feature_cols, LABEL_VARIANT, params=spec["params"])
            pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
            pred_df["score"] = model.predict(pred_df[feature_cols])
            for result in evaluate_portfolios(pred_df, prices, index_df, panel, anchor, top_k_values, weight_rules):
                rows.append(
                    {
                        "model": "xgb_ranker",
                        "spec": spec["name"],
                        "label_variant": LABEL_VARIANT,
                        "anchor": anchor.date().isoformat(),
                        **result,
                    }
                )
    return rows


def summarize(rows: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    return (
        df.groupby(["model", "spec", "label_variant", "top_k", "weight_rule"], as_index=False)
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
    specs: list[dict],
    rows: list[dict],
) -> None:
    summary = summarize(rows)
    details = pd.DataFrame(rows)
    control = summary[summary["model"] == "regressor_control"].iloc[0]
    best_ranker = summary[summary["model"] == "xgb_ranker"].iloc[0]

    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Week 2 Ranker Rescue Sweep",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- As-of date: {as_of.date()}",
        f"- Feature groups: {format_groups(feature_groups)}",
        f"- Ranker label variant: {LABEL_VARIANT}",
        f"- Holding window: {HOLD_DAYS} trading days",
        "- Anchor selection feature groups: baseline",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        "",
        "## Readout",
        "",
        f"- Control best: `{control['spec']}`, top_k={int(control['top_k'])}, "
        f"weight_rule={control['weight_rule']}, mean `{control['mean_excess_5d'] * 100:+.3f}%`, "
        f"worst `{control['min_excess_5d'] * 100:+.3f}%`.",
        f"- Best Ranker: `{best_ranker['spec']}`, top_k={int(best_ranker['top_k'])}, "
        f"weight_rule={best_ranker['weight_rule']}, mean `{best_ranker['mean_excess_5d'] * 100:+.3f}%`, "
        f"worst `{best_ranker['min_excess_5d'] * 100:+.3f}%`.",
        "- Accept Ranker only if it beats the control on mean excess without weakening worst-window excess.",
        "",
        "## Summary",
        "",
        "| model | spec | top_k | weight rule | mean IC | mean excess 5d | min excess 5d | win 5d |",
        "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for _, row in summary.iterrows():
        lines.append(
            f"| {row['model']} | {row['spec']} | {int(row['top_k'])} | {row['weight_rule']} | "
            f"{row['mean_rank_ic']:.4f} | {row['mean_excess_5d'] * 100:+.3f}% | "
            f"{row['min_excess_5d'] * 100:+.3f}% | {row['win_rate_5d']:.2f} |"
        )

    lines.extend(["", "## Ranker Params", ""])
    for spec in specs:
        lines.append(f"- `{spec['name']}`: {format_params(spec['params'])}")

    lines.extend(
        [
            "",
            "## Details",
            "",
            "| anchor | model | spec | top_k | weight rule | rank IC | excess 5d | benchmark 5d |",
            "| --- | --- | --- | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for _, row in details.sort_values(["anchor", "model", "spec", "top_k", "weight_rule"]).iterrows():
        lines.append(
            f"| {row['anchor']} | {row['model']} | {row['spec']} | {int(row['top_k'])} | "
            f"{row['weight_rule']} | {row['rank_ic']:.4f} | {row['excess_5d'] * 100:+.3f}% | "
            f"{row['benchmark_5d'] * 100:+.3f}% |"
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prices", default=str(DATA_DIR / "prices.parquet"))
    parser.add_argument("--index", default=str(DATA_DIR / "index.parquet"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--feature-groups", default=",".join(DEFAULT_FEATURE_GROUPS))
    parser.add_argument("--top-k-values", default=",".join(str(v) for v in TOP_K_VALUES))
    parser.add_argument("--weight-rules", default=",".join(WEIGHT_RULES))
    parser.add_argument("--top-dates", type=int, default=5)
    parser.add_argument("--recent-lookback", type=int, default=80)
    parser.add_argument("--min-stocks-per-date", type=int, default=450)
    parser.add_argument("--negative-multiplier", type=int, default=10)
    parser.add_argument("--max-specs", type=int, default=None)
    parser.add_argument("--report", default="reports/week2_ranker_rescue_sweep_log.md")
    args = parser.parse_args()

    feature_groups = parse_groups(args.feature_groups)
    feature_cols = feature_columns(feature_groups)
    top_k_values = parse_ints(args.top_k_values)
    weight_rules = parse_groups(args.weight_rules)
    specs = RANKER_SPECS[: args.max_specs] if args.max_specs else RANKER_SPECS

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
    print(">> Evaluating regressor control portfolio grid")
    rows.extend(evaluate_regressor_control(panel, prices, index_df, anchors, feature_cols, top_k_values, weight_rules))
    rows.extend(evaluate_ranker_specs(panel, prices, index_df, anchors, feature_cols, specs, top_k_values, weight_rules))

    write_report(Path(args.report), as_of, feature_groups, anchors, auc, specs, rows)
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
