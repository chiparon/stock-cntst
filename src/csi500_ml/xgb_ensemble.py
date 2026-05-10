"""Shared helpers for the regularized XGBoost ensemble pipeline."""
from __future__ import annotations

import pandas as pd
import xgboost as xgb

from .features import TARGET_COLUMN

RANDOM_SEED = 42

MODEL_SPECS: dict[str, dict] = {
    "primary_momentum": {
        "groups": ["momentum_shape"],
        "params": {
            "n_estimators": 700,
            "max_depth": 4,
            "learning_rate": 0.03,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 8.0,
            "reg_alpha": 0.05,
            "gamma": 0.05,
        },
    },
    "robust_momentum": {
        "groups": ["momentum_shape"],
        "params": {
            "n_estimators": 900,
            "max_depth": 3,
            "learning_rate": 0.03,
            "subsample": 0.7,
            "colsample_bytree": 0.7,
            "min_child_weight": 30,
            "reg_lambda": 15.0,
            "reg_alpha": 0.10,
            "gamma": 0.10,
        },
    },
    "rank_liquidity": {
        "groups": ["rank_all", "liquidity_log"],
        "params": {
            "n_estimators": 700,
            "max_depth": 3,
            "learning_rate": 0.04,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "min_child_weight": 20,
            "reg_lambda": 10.0,
            "reg_alpha": 0.05,
            "gamma": 0.05,
        },
    },
}

ENSEMBLES: dict[str, dict[str, float]] = {
    "primary_only": {"primary_momentum": 1.0},
    "primary_robust_70_30": {"primary_momentum": 0.7, "robust_momentum": 0.3},
    "primary_rankliq_70_30": {"primary_momentum": 0.7, "rank_liquidity": 0.3},
    "primary_robust_equal": {"primary_momentum": 0.5, "robust_momentum": 0.5},
    "primary_robust_rankliq_60_25_15": {
        "primary_momentum": 0.60,
        "robust_momentum": 0.25,
        "rank_liquidity": 0.15,
    },
    "primary_heavy_all": {
        "primary_momentum": 0.6,
        "robust_momentum": 0.2,
        "rank_liquidity": 0.2,
    },
    "all_equal": {
        "primary_momentum": 1 / 3,
        "robust_momentum": 1 / 3,
        "rank_liquidity": 1 / 3,
    },
}

DEFAULT_ENSEMBLE = "primary_rankliq_70_30"
DEFAULT_WEIGHT_RULE = "score_positive"


def train_xgboost(
    train_df: pd.DataFrame,
    eval_df: pd.DataFrame,
    feature_cols: list[str],
    params: dict,
    *,
    seed: int = RANDOM_SEED,
) -> xgb.XGBRegressor:
    """Fit a regularized XGBoost regressor with early stopping."""
    model = xgb.XGBRegressor(
        **params,
        objective="reg:squarederror",
        tree_method="hist",
        n_jobs=-1,
        early_stopping_rounds=30,
        random_state=seed,
        eval_metric="rmse",
    )
    model.fit(
        train_df[feature_cols],
        train_df[TARGET_COLUMN],
        eval_set=[(eval_df[feature_cols], eval_df[TARGET_COLUMN])],
        verbose=False,
    )
    return model


def rank_within_date(frame: pd.DataFrame, score_col: str = "score", date_col: str = "date") -> pd.Series:
    """Return cross-sectional percentile ranks, grouped by date when present."""
    if date_col in frame.columns:
        return frame.groupby(date_col)[score_col].rank(method="average", pct=True)
    return frame[score_col].rank(method="average", pct=True)


def blend_ranked_scores(
    model_outputs: dict[str, pd.DataFrame],
    weights: dict[str, float],
    *,
    key_cols: tuple[str, ...] = ("date", "stock_code"),
) -> pd.DataFrame:
    """Blend model scores after converting each model to per-date percentile rank."""
    merged: pd.DataFrame | None = None
    score_cols: list[str] = []
    total_weight = sum(weights.values())
    if total_weight <= 0:
        raise ValueError("weights must sum to a positive value")

    for model_name, weight in weights.items():
        if model_name not in model_outputs:
            raise KeyError(f"Missing model output for {model_name!r}")
        df = model_outputs[model_name].copy()
        score_col = f"score_{model_name}"
        df[score_col] = rank_within_date(df) * weight
        keep = [*key_cols]
        if TARGET_COLUMN in df.columns:
            keep.append(TARGET_COLUMN)
        keep.append(score_col)
        subset = df[keep]
        if merged is None:
            merged = subset
        else:
            merged = merged.merge(subset[list(key_cols) + [score_col]], on=list(key_cols), how="inner")
        score_cols.append(score_col)

    if merged is None:
        raise ValueError("No model outputs provided")

    merged["score"] = merged[score_cols].sum(axis=1) / total_weight
    return merged
