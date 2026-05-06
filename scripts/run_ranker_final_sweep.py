"""
Final XGBRanker optimization attempt before closing the branch.

This pass tests whether the problem is the ranking objective or the top-bucket
definition rather than only tree regularization. The acceptance rule is strict:
the best Ranker configuration must have non-negative worst-window excess return
on the fixed 5-anchor gate.

Usage
-----
  python scripts/run_ranker_final_sweep.py
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
from testlike_xgboost_validation import HOLD_DAYS, labeled_cutoff_date, select_testlike_dates, window_bounds
from run_ranker_ablation import CURRENT_PARAMS, DEFAULT_FEATURE_GROUPS, format_groups, parse_groups, train_ranker_for_anchor


TOP_K_VALUES = [30, 40, 50]
WEIGHT_RULES = ["score_positive", "rank", "equal"]
LABEL_VARIANTS = ["top10_binary", "top15_binary", "top20_binary", "top30_binary"]

PARAM_SPECS = [
    {
        "name": "current_d4_mcw10_l5_sub08",
        "params": CURRENT_PARAMS,
    },
    {
        "name": "stable_d4_mcw20_l10_sub07",
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
        "name": "shallow_d3_mcw10_l5_sub08",
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
        "name": "slow_d3_mcw20_l10_lr003_sub08",
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

OBJECTIVE_SPECS = [
    {"name": "pairwise_ndcg30", "objective": "rank:pairwise", "eval_metric": "ndcg@30"},
    {"name": "ndcg_ndcg30", "objective": "rank:ndcg", "eval_metric": "ndcg@30"},
]


def parse_ints(value: str) -> list[int]:
    return [int(v.strip()) for v in value.split(",") if v.strip()]


def parse_csv(value: str) -> list[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


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


def evaluate_ranker_grid(
    panel: pd.DataFrame,
    prices: pd.DataFrame,
    index_df: pd.DataFrame,
    anchors: list[pd.Timestamp],
    feature_cols: list[str],
    label_variants: list[str],
    param_specs: list[dict],
    objective_specs: list[dict],
    top_k_values: list[int],
    weight_rules: list[str],
) -> list[dict]:
    rows = []
    for label_variant in label_variants:
        for objective_spec in objective_specs:
            for param_spec in param_specs:
                spec_name = f"{label_variant}_{objective_spec['name']}_{param_spec['name']}"
                print(f">> Evaluating {spec_name}")
                for anchor in anchors:
                    model = train_ranker_for_anchor(
                        panel,
                        anchor,
                        feature_cols,
                        label_variant,
                        params=param_spec["params"],
                        objective=objective_spec["objective"],
                        eval_metric=objective_spec["eval_metric"],
                    )
                    pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
                    pred_df["score"] = model.predict(pred_df[feature_cols])
                    for result in evaluate_portfolios(pred_df, prices, index_df, panel, anchor, top_k_values, weight_rules):
                        rows.append(
                            {
                                "label_variant": label_variant,
                                "objective": objective_spec["objective"],
                                "eval_metric": objective_spec["eval_metric"],
                                "param_spec": param_spec["name"],
                                "spec": spec_name,
                                "anchor": anchor.date().isoformat(),
                                **result,
                            }
                        )
    return rows


def summarize(rows: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    return (
        df.groupby(["spec", "label_variant", "objective", "eval_metric", "param_spec", "top_k", "weight_rule"], as_index=False)
        .agg(
            mean_rank_ic=("rank_ic", "mean"),
            mean_excess_5d=("excess_5d", "mean"),
            min_excess_5d=("excess_5d", "min"),
            win_rate_5d=("excess_5d", lambda s: float((s > 0).mean())),
        )
        .sort_values(["min_excess_5d", "mean_excess_5d", "win_rate_5d", "mean_rank_ic"], ascending=False)
    )


def write_report(
    path: Path,
    as_of: pd.Timestamp,
    feature_groups: list[str],
    anchors: list[pd.Timestamp],
    auc: float,
    param_specs: list[dict],
    rows: list[dict],
) -> None:
    summary = summarize(rows)
    details = pd.DataFrame(rows)
    best_by_min = summary.iloc[0]
    accepted = bool(best_by_min["min_excess_5d"] >= 0)

    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Week 2 Ranker Final Sweep",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- As-of date: {as_of.date()}",
        f"- Feature groups: {format_groups(feature_groups)}",
        f"- Holding window: {HOLD_DAYS} trading days",
        "- Anchor selection feature groups: baseline",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        "",
        "## Readout",
        "",
        f"- Best by worst-window excess: `{best_by_min['spec']}`, top_k={int(best_by_min['top_k'])}, "
        f"weight_rule={best_by_min['weight_rule']}, mean `{best_by_min['mean_excess_5d'] * 100:+.3f}%`, "
        f"worst `{best_by_min['min_excess_5d'] * 100:+.3f}%`.",
        f"- Acceptance status: {'accepted' if accepted else 'rejected'}; min_excess_5d must be non-negative.",
        "",
        "## Summary",
        "",
        "| spec | top_k | weight rule | mean IC | mean excess 5d | min excess 5d | win 5d |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for _, row in summary.iterrows():
        lines.append(
            f"| {row['spec']} | {int(row['top_k'])} | {row['weight_rule']} | {row['mean_rank_ic']:.4f} | "
            f"{row['mean_excess_5d'] * 100:+.3f}% | {row['min_excess_5d'] * 100:+.3f}% | "
            f"{row['win_rate_5d']:.2f} |"
        )

    lines.extend(["", "## Parameter Specs", ""])
    for spec in param_specs:
        lines.append(f"- `{spec['name']}`: {format_params(spec['params'])}")

    lines.extend(
        [
            "",
            "## Details",
            "",
            "| anchor | spec | top_k | weight rule | rank IC | excess 5d | benchmark 5d |",
            "| --- | --- | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for _, row in details.sort_values(["anchor", "spec", "top_k", "weight_rule"]).iterrows():
        lines.append(
            f"| {row['anchor']} | {row['spec']} | {int(row['top_k'])} | {row['weight_rule']} | "
            f"{row['rank_ic']:.4f} | {row['excess_5d'] * 100:+.3f}% | {row['benchmark_5d'] * 100:+.3f}% |"
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prices", default=str(DATA_DIR / "prices.parquet"))
    parser.add_argument("--index", default=str(DATA_DIR / "index.parquet"))
    parser.add_argument("--as-of", default=None, help="YYYYMMDD; defaults to latest date in data")
    parser.add_argument("--feature-groups", default=",".join(DEFAULT_FEATURE_GROUPS))
    parser.add_argument("--label-variants", default=",".join(LABEL_VARIANTS))
    parser.add_argument("--top-k-values", default=",".join(str(v) for v in TOP_K_VALUES))
    parser.add_argument("--weight-rules", default=",".join(WEIGHT_RULES))
    parser.add_argument("--top-dates", type=int, default=5)
    parser.add_argument("--recent-lookback", type=int, default=80)
    parser.add_argument("--min-stocks-per-date", type=int, default=450)
    parser.add_argument("--negative-multiplier", type=int, default=10)
    parser.add_argument("--max-param-specs", type=int, default=None)
    parser.add_argument("--max-objective-specs", type=int, default=None)
    parser.add_argument("--report", default="reports/week2_ranker_final_sweep_log.md")
    args = parser.parse_args()

    feature_groups = parse_groups(args.feature_groups)
    label_variants = parse_csv(args.label_variants)
    top_k_values = parse_ints(args.top_k_values)
    weight_rules = parse_csv(args.weight_rules)
    param_specs = PARAM_SPECS[: args.max_param_specs] if args.max_param_specs else PARAM_SPECS
    objective_specs = OBJECTIVE_SPECS[: args.max_objective_specs] if args.max_objective_specs else OBJECTIVE_SPECS
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

    rows = evaluate_ranker_grid(
        panel,
        prices,
        index_df,
        anchors,
        feature_cols,
        label_variants,
        param_specs,
        objective_specs,
        top_k_values,
        weight_rules,
    )
    write_report(Path(args.report), as_of, feature_groups, anchors, auc, param_specs, rows)
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
