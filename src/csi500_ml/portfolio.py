"""Portfolio construction helpers for CSI500 submissions."""
from __future__ import annotations

import numpy as np
import pandas as pd

MIN_STOCKS = 30
MAX_WEIGHT = 0.10


def _cap_and_redistribute(weights: pd.Series) -> pd.Series:
    weights = weights.astype(float).copy()
    if weights.empty:
        raise ValueError("Cannot normalize empty weights.")
    weights = weights / weights.sum()
    for _ in range(50):
        over = weights > MAX_WEIGHT
        if not over.any():
            break
        excess = (weights[over] - MAX_WEIGHT).sum()
        weights[over] = MAX_WEIGHT
        free = ~over
        if not free.any():
            break
        weights[free] += excess * weights[free] / weights[free].sum()
    weights = weights / weights.sum()
    if (weights > MAX_WEIGHT + 1e-9).any():
        raise RuntimeError("Weight cap violated after redistribution.")
    return weights


def build_portfolio(scores: pd.Series, top_k: int = 50, weight_rule: str = "rank") -> pd.Series:
    """Build a long-only capped portfolio from model scores."""
    if top_k < MIN_STOCKS:
        raise ValueError(f"top_k must be >= {MIN_STOCKS}")
    chosen = scores.sort_values(ascending=False).head(top_k)
    if len(chosen) < top_k:
        raise ValueError(f"Requested top_k={top_k}, but only {len(chosen)} scores are available.")

    if weight_rule == "rank":
        raw = pd.Series(np.arange(top_k, 0, -1, dtype=float), index=chosen.index)
    elif weight_rule == "equal":
        raw = pd.Series(1.0, index=chosen.index)
    elif weight_rule == "score_positive":
        shifted = chosen - chosen.min()
        raw = shifted + max(float(shifted.std()), 1e-9) * 0.1
    else:
        raise ValueError("Unknown weight_rule {!r}; expected rank, equal, or score_positive".format(weight_rule))

    weights = _cap_and_redistribute(raw)
    if abs(weights.sum() - 1.0) > 1e-6:
        raise RuntimeError(f"Weights sum to {weights.sum()}")
    if (weights > 0).sum() < MIN_STOCKS:
        raise RuntimeError("Portfolio has too few positive-weight names.")
    return weights
