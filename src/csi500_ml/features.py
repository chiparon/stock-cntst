"""
Feature engineering for the CSI500 stock-selection baseline.

A small set of classic technical features + cross-sectional ranks.  Students are
encouraged to extend this (add fundamentals, industry dummies, alternative data,
better cross-sectional normalization, etc.).

The target is the 5-trading-day forward return on the forward-adjusted close,
i.e. what the portfolio earns if you hold a $1 position from close(t) to close(t+5).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# columns used downstream by the baseline
BASE_FEATURE_COLUMNS = [
    "ret_1d", "ret_5d", "ret_10d", "ret_20d", "ret_60d",
    "vol_20d", "volume_z_20d", "turnover_ma_20d",
    "close_over_ma20", "close_over_ma60", "rsi_14",
    "ret_5d_rank", "ret_20d_rank", "vol_20d_rank",
]
FEATURE_COLUMNS = BASE_FEATURE_COLUMNS.copy()
TARGET_COLUMN = "target_5d"
FORWARD_HORIZON = 5

RANK_NORMALIZED_BASES = [
    "ret_1d", "ret_3d", "ret_5d", "ret_10d", "ret_20d", "ret_60d",
    "rel_ret_5d", "rel_ret_20d", "rel_ret_60d",
    "vol_5d", "vol_10d", "vol_20d", "vol_5d_over_20d", "vol_10d_over_20d",
    "volume_z_20d", "log_volume_z_20d", "turnover_ma_20d", "log_turnover_ma_20d",
    "close_over_ma20", "close_over_ma60", "rsi_14",
    "ret_20d_minus_5d", "ret_60d_minus_20d",
]

FEATURE_GROUPS = {
    "rank_all": [f"{col}_rank" for col in RANK_NORMALIZED_BASES],
    "vol_regime": [
        "vol_5d", "vol_10d", "vol_5d_over_20d", "vol_10d_over_20d",
        "vol_5d_rank", "vol_10d_rank", "vol_5d_over_20d_rank", "vol_10d_over_20d_rank",
    ],
    "liquidity_log": [
        "log_volume_z_20d", "log_turnover_ma_20d",
        "log_volume_z_20d_rank", "log_turnover_ma_20d_rank",
    ],
    "momentum_shape": [
        "ret_3d", "ret_20d_minus_5d", "ret_60d_minus_20d",
        "ret_3d_rank", "ret_20d_minus_5d_rank", "ret_60d_minus_20d_rank",
    ],
    "mom_ret3": ["ret_3d", "ret_3d_rank"],
    "mom_trend_20_5": ["ret_20d_minus_5d", "ret_20d_minus_5d_rank"],
    "mom_trend_60_20": ["ret_60d_minus_20d", "ret_60d_minus_20d_rank"],
    "index_relative": [
        "index_ret_5d", "index_ret_20d", "index_ret_60d",
        "rel_ret_5d", "rel_ret_20d", "rel_ret_60d",
        "rel_ret_5d_rank", "rel_ret_20d_rank", "rel_ret_60d_rank",
    ],
}


def feature_columns(enabled_groups: list[str] | tuple[str, ...] | None = None) -> list[str]:
    """Return baseline feature columns plus optional feature-group columns."""
    cols = list(BASE_FEATURE_COLUMNS)
    for group in enabled_groups or []:
        if group not in FEATURE_GROUPS:
            raise ValueError(f"Unknown feature group {group!r}; available: {sorted(FEATURE_GROUPS)}")
        cols.extend(FEATURE_GROUPS[group])
    return list(dict.fromkeys(cols))


def _per_stock_features(df: pd.DataFrame) -> pd.DataFrame:
    """Features that only depend on a single stock's time series."""
    df = df.sort_values("date").copy()
    close = df["close"]

    df["ret_1d"] = close.pct_change(1)
    df["ret_3d"] = close.pct_change(3)
    df["ret_5d"] = close.pct_change(5)
    df["ret_10d"] = close.pct_change(10)
    df["ret_20d"] = close.pct_change(20)
    df["ret_60d"] = close.pct_change(60)
    df["ret_20d_minus_5d"] = df["ret_20d"] - df["ret_5d"]
    df["ret_60d_minus_20d"] = df["ret_60d"] - df["ret_20d"]

    df["vol_5d"] = df["ret_1d"].rolling(5).std()
    df["vol_10d"] = df["ret_1d"].rolling(10).std()
    df["vol_20d"] = df["ret_1d"].rolling(20).std()
    vol_20d_safe = df["vol_20d"].replace(0, np.nan)
    df["vol_5d_over_20d"] = df["vol_5d"] / vol_20d_safe
    df["vol_10d_over_20d"] = df["vol_10d"] / vol_20d_safe

    vol = df["volume"].astype(float)
    vol_mean = vol.rolling(20).mean()
    vol_std = vol.rolling(20).std().replace(0, np.nan)
    df["volume_z_20d"] = (vol - vol_mean) / vol_std
    log_vol = np.log1p(vol.clip(lower=0))
    log_vol_mean = log_vol.rolling(20).mean()
    log_vol_std = log_vol.rolling(20).std().replace(0, np.nan)
    df["log_volume_z_20d"] = (log_vol - log_vol_mean) / log_vol_std

    if "turnover" in df.columns:
        turnover = df["turnover"].astype(float)
        df["turnover_ma_20d"] = turnover.rolling(20).mean()
        df["log_turnover_ma_20d"] = np.log1p(turnover.clip(lower=0)).rolling(20).mean()
    else:
        df["turnover_ma_20d"] = np.nan
        df["log_turnover_ma_20d"] = np.nan

    df["close_over_ma20"] = close / close.rolling(20).mean() - 1.0
    df["close_over_ma60"] = close / close.rolling(60).mean() - 1.0

    delta = close.diff()
    up = delta.clip(lower=0).rolling(14).mean()
    down = (-delta.clip(upper=0)).rolling(14).mean().replace(0, np.nan)
    rs = up / down
    df["rsi_14"] = 100 - 100 / (1 + rs)

    df[TARGET_COLUMN] = close.shift(-FORWARD_HORIZON) / close - 1.0
    return df


def _cross_sectional_ranks(panel: pd.DataFrame) -> pd.DataFrame:
    """Daily cross-sectional rank of selected features (values in [0, 1])."""
    for base in RANK_NORMALIZED_BASES:
        if base not in panel.columns:
            continue
        panel[f"{base}_rank"] = (
            panel.groupby("date")[base].rank(method="average", pct=True)
        )
    return panel


def _index_features(index_df: pd.DataFrame) -> pd.DataFrame:
    """Benchmark features known as of each trading date."""
    required = {"date", "close"}
    missing = required - set(index_df.columns)
    if missing:
        raise ValueError(f"index_df is missing required columns: {missing}")

    idx = index_df[["date", "close"]].copy()
    idx["date"] = pd.to_datetime(idx["date"])
    idx = idx.sort_values("date")
    idx["index_ret_1d"] = idx["close"].pct_change(1)
    idx["index_ret_5d"] = idx["close"].pct_change(5)
    idx["index_ret_20d"] = idx["close"].pct_change(20)
    idx["index_ret_60d"] = idx["close"].pct_change(60)
    return idx.drop(columns=["close"])


def _add_index_relative_features(panel: pd.DataFrame, index_df: pd.DataFrame | None) -> pd.DataFrame:
    if index_df is None:
        return panel
    idx = _index_features(index_df)
    panel = panel.merge(idx, on="date", how="left")
    for horizon in [5, 20, 60]:
        panel[f"rel_ret_{horizon}d"] = panel[f"ret_{horizon}d"] - panel[f"index_ret_{horizon}d"]
    return panel


def build_features(prices: pd.DataFrame, index_df: pd.DataFrame | None = None) -> pd.DataFrame:
    """Build a (date, stock_code) panel of features + target.

    Parameters
    ----------
    prices : DataFrame with columns [date, stock_code, open, close, high, low,
             volume, amount, turnover?]

    Returns
    -------
    DataFrame with FEATURE_COLUMNS and TARGET_COLUMN populated.  Rows where any
    feature is NaN (typically the first ~60 days per stock) are kept so callers
    can decide how to handle them.
    """
    required = {"date", "stock_code", "close", "volume"}
    missing = required - set(prices.columns)
    if missing:
        raise ValueError(f"prices is missing required columns: {missing}")

    prices = prices.copy()
    prices["date"] = pd.to_datetime(prices["date"])
    parts = []
    for code, stock_df in prices.groupby("stock_code", sort=False):
        featured = _per_stock_features(stock_df)
        if "stock_code" not in featured.columns:
            featured["stock_code"] = str(code).zfill(6)
        parts.append(featured)
    panel = pd.concat(parts, ignore_index=True)
    panel = _add_index_relative_features(panel, index_df)
    panel = _cross_sectional_ranks(panel)
    return panel


def training_frame(panel: pd.DataFrame, min_date=None, max_date=None) -> pd.DataFrame:
    """Rows usable for supervised training: all features present AND target present.

    The target for date t uses close(t+5), so rows within the last 5 trading
    days of the panel are dropped automatically (target is NaN there).
    """
    df = panel.dropna(subset=FEATURE_COLUMNS + [TARGET_COLUMN]).copy()
    if min_date is not None:
        df = df[df["date"] >= pd.Timestamp(min_date)]
    if max_date is not None:
        df = df[df["date"] <= pd.Timestamp(max_date)]
    return df


def prediction_frame(panel: pd.DataFrame, as_of=None) -> pd.DataFrame:
    """Rows for a single prediction date (defaults to the latest date)."""
    if as_of is None:
        as_of = panel["date"].max()
    as_of = pd.Timestamp(as_of)
    df = panel[panel["date"] == as_of].dropna(subset=FEATURE_COLUMNS).copy()
    return df
