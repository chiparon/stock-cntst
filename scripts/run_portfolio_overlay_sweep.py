"""
Run a portfolio overlay sweep around the current week-2 control signal.

This script intentionally keeps the model feature set fixed to the current
winner (`momentum_shape`) and evaluates small portfolio-construction changes:

- score-positive weighting with different top_k, caps, and score powers
- volatility-adjusted score-positive weighting with configurable vol exponent
- weight-level blends between the primary model and the robust fallback model

The goal is to improve the live-like anchor gate without broad feature stacking.
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

from baseline_xgboost import DATA_DIR, rank_ic
from csi500_ml.features import TARGET_COLUMN, build_features, feature_columns, prediction_frame, training_frame
from run_xgboost_local_sweep import LOCAL_SPECS
from score_submission import score_window
from testlike_xgboost_validation import (
    HOLD_DAYS,
    labeled_cutoff_date,
    select_testlike_dates,
    train_for_anchor,
    window_bounds,
)


FEATURE_GROUPS = ["momentum_shape"]
PRIMARY_SPEC = "current_d4_mcw10_l5_lr005"
ROBUST_SPEC = "d4_mcw20_l10_lr005_sub07"
MIN_STOCKS = 30


def parse_groups(value: str | None) -> list[str]:
    return [g.strip() for g in (value or "").split(",") if g.strip()]


def spec_by_name(name: str) -> dict:
    for spec in LOCAL_SPECS:
        if spec["name"] == name:
            return spec
    available = ", ".join(spec["name"] for spec in LOCAL_SPECS)
    raise ValueError(f"Unknown local spec {name!r}; available: {available}")


def cap_and_redistribute(raw: pd.Series, max_weight: float) -> pd.Series:
    """Normalize positive raw weights with a configurable per-name cap."""
    raw = raw.replace([np.inf, -np.inf], np.nan).dropna()
    raw = raw[raw > 0].astype(float)
    if raw.empty:
        raise ValueError("Cannot build weights from empty raw weights.")
    if len(raw) < MIN_STOCKS:
        raise ValueError(f"Need at least {MIN_STOCKS} positive names, got {len(raw)}.")
    if len(raw) * max_weight < 1.0 - 1e-12:
        raise ValueError(
            f"max_weight={max_weight:.4f} is infeasible for {len(raw)} names."
        )

    weights = pd.Series(0.0, index=raw.index, dtype=float)
    active = raw.copy()
    remaining = 1.0
    for _ in range(len(raw) + 5):
        alloc = active / active.sum() * remaining
        over = alloc > max_weight
        if not over.any():
            weights.loc[alloc.index] = alloc
            break

        capped = alloc[over].index
        weights.loc[capped] = max_weight
        remaining -= max_weight * len(capped)
        active = active.drop(index=capped)
        if active.empty:
            break
    else:
        raise RuntimeError("Weight cap redistribution did not converge.")

    weights = weights[weights > 0]
    weights = weights / weights.sum()
    if (weights > max_weight + 1e-9).any():
        raise RuntimeError("Weight cap violated after redistribution.")
    if abs(weights.sum() - 1.0) > 1e-8:
        raise RuntimeError(f"Weights sum to {weights.sum()}")
    if (weights > 0).sum() < MIN_STOCKS:
        raise RuntimeError("Portfolio has too few positive-weight names.")
    return weights.sort_values(ascending=False)


def score_positive_raw(scores: pd.Series, power: float) -> pd.Series:
    shifted = scores - scores.min()
    base = shifted + max(float(shifted.std()), 1e-9) * 0.1
    return base.pow(power)


def build_score_weights(
    pred_df: pd.DataFrame,
    top_k: int,
    max_weight: float,
    power: float,
    vol_adjust: bool,
    vol_power: float,
) -> pd.Series:
    chosen = pred_df.sort_values("score", ascending=False).head(top_k).copy()
    if len(chosen) < top_k:
        raise ValueError(f"Requested top_k={top_k}, got {len(chosen)} rows.")

    raw = score_positive_raw(chosen.set_index("stock_code")["score"], power=power)
    if vol_adjust:
        vol = chosen.set_index("stock_code")["vol_20d"].astype(float)
        vol = vol.replace([np.inf, -np.inf], np.nan)
        fill = float(vol.median())
        vol = vol.fillna(fill)
        lower = float(vol.quantile(0.20))
        upper = float(vol.quantile(0.90))
        vol = vol.clip(lower=max(lower, 1e-6), upper=max(upper, 1e-6))
        raw = raw / vol.pow(vol_power)
    return cap_and_redistribute(raw, max_weight=max_weight)


def blend_weights(primary: pd.Series, robust: pd.Series, primary_share: float, max_weight: float) -> pd.Series:
    combined = primary.mul(primary_share).add(robust.mul(1.0 - primary_share), fill_value=0.0)
    return cap_and_redistribute(combined, max_weight=max_weight)


def candidate_specs() -> list[dict]:
    specs: list[dict] = []
    top_ks = [30, 35, 40]
    caps = [0.06, 0.075, 0.085, 0.10]
    powers = [0.75, 1.00, 1.10, 1.25, 1.40]
    for top_k in top_ks:
        for max_weight in caps:
            if top_k * max_weight < 1.0:
                continue
            for power in powers:
                specs.append(
                    {
                        "name": f"primary_k{top_k}_cap{int(max_weight * 1000):03d}_p{power:g}",
                        "family": "primary_score_power",
                        "model": "primary",
                        "top_k": top_k,
                        "max_weight": max_weight,
                        "power": power,
                        "vol_adjust": False,
                        "vol_power": 0.0,
                    }
                )

    for top_k in top_ks:
        for max_weight in [0.075, 0.085, 0.10]:
            if top_k * max_weight < 1.0:
                continue
            for power in [1.00, 1.10, 1.25, 1.40]:
                for vol_power in [0.50, 0.75, 1.00]:
                    specs.append(
                        {
                            "name": (
                                f"primary_voladj_v{vol_power:g}_k{top_k}_"
                                f"cap{int(max_weight * 1000):03d}_p{power:g}"
                            ),
                            "family": "primary_vol_adjust",
                            "model": "primary",
                            "top_k": top_k,
                            "max_weight": max_weight,
                            "power": power,
                            "vol_adjust": True,
                            "vol_power": vol_power,
                        }
                    )

    for primary_pct in [80, 70, 50]:
        share = primary_pct / 100.0
        robust_pct = 100 - primary_pct
        specs.append(
            {
                "name": f"blend_primary{primary_pct:02d}_robust{robust_pct:02d}",
                "family": "primary_robust_blend",
                "model": "blend",
                "primary_share": share,
                "max_weight": 0.10,
            }
        )

    specs.append(
        {
            "name": "robust_only_k30_cap100_p1",
            "family": "robust_baseline",
            "model": "robust",
            "top_k": 30,
            "max_weight": 0.10,
            "power": 1.0,
            "vol_adjust": False,
            "vol_power": 0.0,
        }
    )
    return specs


def summarize(details: pd.DataFrame) -> pd.DataFrame:
    summary = details.groupby(["candidate", "family", "params"], as_index=False).agg(
        mean_excess_5d=("excess_5d", "mean"),
        max_excess_5d=("excess_5d", "max"),
        min_excess_5d=("excess_5d", "min"),
        win_rate_5d=("excess_5d", lambda s: float((s > 0).mean())),
        mean_portfolio_5d=("portfolio_5d", "mean"),
        mean_benchmark_5d=("benchmark_5d", "mean"),
        mean_n_names=("n_names", "mean"),
        mean_max_weight=("max_name_weight", "mean"),
        mean_primary_ic=("primary_ic", "mean"),
        mean_robust_ic=("robust_ic", "mean"),
    )
    return summary.sort_values(
        ["mean_excess_5d", "min_excess_5d", "win_rate_5d"],
        ascending=False,
    )


def format_params(spec: dict) -> str:
    if spec["model"] == "blend":
        return f"primary_share={spec['primary_share']:.2f}, max_weight={spec['max_weight']:.3f}"
    return (
        f"model={spec['model']}, top_k={spec['top_k']}, "
        f"max_weight={spec['max_weight']:.3f}, power={spec['power']:.2f}, "
        f"vol_adjust={spec['vol_adjust']}, vol_power={spec['vol_power']:.2f}"
    )


def write_report(
    path: Path,
    as_of: pd.Timestamp,
    anchors: list[pd.Timestamp],
    auc: float,
    summary: pd.DataFrame,
    details: pd.DataFrame,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Portfolio Overlay Sweep",
        "",
        f"- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- As-of date: {as_of.date()}",
        f"- Feature groups: {','.join(FEATURE_GROUPS)}",
        f"- Primary spec: {PRIMARY_SPEC}",
        f"- Robust spec: {ROBUST_SPEC}",
        f"- Holding window: {HOLD_DAYS} trading days",
        "- Anchor selection feature groups: baseline",
        f"- Adversarial validation AUC: {auc:.4f}",
        f"- Selected anchors: {', '.join(d.date().isoformat() for d in anchors)}",
        "",
        "## Summary",
        "",
        "| candidate | family | avg excess 5d | max excess 5d | min excess 5d | win 5d | avg portfolio 5d | avg names | avg max weight | params |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for _, row in summary.iterrows():
        lines.append(
            f"| {row['candidate']} | {row['family']} | "
            f"{row['mean_excess_5d'] * 100:+.3f}% | "
            f"{row['max_excess_5d'] * 100:+.3f}% | "
            f"{row['min_excess_5d'] * 100:+.3f}% | "
            f"{row['win_rate_5d']:.2f} | "
            f"{row['mean_portfolio_5d'] * 100:+.3f}% | "
            f"{row['mean_n_names']:.1f} | "
            f"{row['mean_max_weight'] * 100:.2f}% | "
            f"{row['params']} |"
        )

    lines.extend(
        [
            "",
            "## Details",
            "",
            "| anchor | candidate | excess 5d | portfolio 5d | benchmark 5d | names | max weight | primary IC | robust IC |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for _, row in details.sort_values(["anchor", "candidate"]).iterrows():
        lines.append(
            f"| {row['anchor']} | {row['candidate']} | "
            f"{row['excess_5d'] * 100:+.3f}% | {row['portfolio_5d'] * 100:+.3f}% | "
            f"{row['benchmark_5d'] * 100:+.3f}% | {int(row['n_names'])} | "
            f"{row['max_name_weight'] * 100:.2f}% | {row['primary_ic']:.4f} | "
            f"{row['robust_ic']:.4f} |"
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
    parser.add_argument("--report", default="reports/week2_portfolio_overlay_sweep.md")
    args = parser.parse_args()

    feature_cols = feature_columns(FEATURE_GROUPS)
    anchor_feature_cols = feature_columns([])
    primary_spec = spec_by_name(PRIMARY_SPEC)
    robust_spec = spec_by_name(ROBUST_SPEC)
    candidates = candidate_specs()

    print(f">> Loading {args.prices}")
    prices = pd.read_parquet(args.prices)
    prices["stock_code"] = prices["stock_code"].astype(str).str.zfill(6)
    prices["date"] = pd.to_datetime(prices["date"])
    index_df = pd.read_parquet(args.index)
    index_df["date"] = pd.to_datetime(index_df["date"])

    print(">> Building features")
    panel = build_features(prices, index_df=index_df)
    as_of = pd.Timestamp(args.as_of) if args.as_of else pd.Timestamp(panel["date"].max())
    anchor_pred_df = prediction_frame(panel, as_of=as_of).dropna(subset=anchor_feature_cols)
    cutoff = labeled_cutoff_date(panel, as_of)
    anchor_history_df = training_frame(panel, max_date=cutoff).dropna(subset=anchor_feature_cols)

    print(">> Selecting test-like anchors with baseline features")
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
        raise RuntimeError("No eligible anchors selected.")
    print(f"   adversarial AUC: {auc:.4f}")
    print(f"   anchors: {', '.join(d.date().isoformat() for d in anchors)}")

    rows = []
    for anchor in anchors:
        print(f">> Training anchor {anchor.date()}")
        model_outputs = {}
        ics = {}
        for label, spec in [("primary", primary_spec), ("robust", robust_spec)]:
            model = train_for_anchor(panel, anchor, spec["params"], feature_cols)
            pred_df = prediction_frame(panel, as_of=anchor).dropna(subset=feature_cols).copy()
            pred_df = pred_df.assign(score=model.predict(pred_df[feature_cols]))
            labeled = pred_df.dropna(subset=[TARGET_COLUMN]).copy()
            ics[label] = rank_ic(
                labeled[TARGET_COLUMN].to_numpy(),
                labeled["score"].to_numpy(),
                labeled["date"].to_numpy(),
            )
            model_outputs[label] = pred_df
            print(f"   {label}: rank IC={ics[label]:.4f}")

        base_primary = build_score_weights(model_outputs["primary"], 30, 0.10, 1.0, False, 0.0)
        base_robust = build_score_weights(model_outputs["robust"], 30, 0.10, 1.0, False, 0.0)
        start, end = window_bounds(panel, anchor, HOLD_DAYS)

        for candidate in candidates:
            if candidate["model"] == "blend":
                weights = blend_weights(
                    base_primary,
                    base_robust,
                    primary_share=candidate["primary_share"],
                    max_weight=candidate["max_weight"],
                )
            else:
                weights = build_score_weights(
                    model_outputs[candidate["model"]],
                    top_k=candidate["top_k"],
                    max_weight=candidate["max_weight"],
                    power=candidate["power"],
                    vol_adjust=candidate["vol_adjust"],
                    vol_power=candidate["vol_power"],
                )

            result = score_window(weights, prices, index_df, start, end)
            rows.append(
                {
                    "anchor": anchor.date().isoformat(),
                    "candidate": candidate["name"],
                    "family": candidate["family"],
                    "params": format_params(candidate),
                    "primary_ic": ics["primary"],
                    "robust_ic": ics["robust"],
                    "n_names": int((weights > 0).sum()),
                    "max_name_weight": float(weights.max()),
                    "portfolio_5d": result["portfolio_return"],
                    "benchmark_5d": result["benchmark_return"],
                    "excess_5d": result["excess_return"],
                }
            )

    details = pd.DataFrame(rows)
    summary = summarize(details)
    write_report(Path(args.report), as_of, anchors, auc, summary, details)
    print(">> Top candidates")
    print(
        summary[
            ["candidate", "family", "mean_excess_5d", "max_excess_5d", "min_excess_5d", "win_rate_5d"]
        ]
        .head(12)
        .to_string(index=False, formatters={
            "mean_excess_5d": lambda x: f"{x * 100:+.3f}%",
            "max_excess_5d": lambda x: f"{x * 100:+.3f}%",
            "min_excess_5d": lambda x: f"{x * 100:+.3f}%",
            "win_rate_5d": lambda x: f"{x:.2f}",
        })
    )
    print(f">> Wrote {args.report}")


if __name__ == "__main__":
    main()
