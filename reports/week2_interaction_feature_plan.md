# Week 2 Interaction Feature Plan

## Context

The XGBRanker branch was pushed as a documented research path and failed the
wider 8-anchor stability gate. Week 2 development returns to the current
XGBRegressor control.

The current control remains:

- Feature groups: `momentum_shape`.
- XGBoost params: `concentrated_top30`.
- Portfolio construction: `top_k=30`, `score_positive`.

## Experiment

Add small, explicit interaction groups while keeping default feature columns
unchanged:

- `momentum_volatility_interaction`:
  momentum-shape signals multiplied by `vol_20d`.
- `momentum_liquidity_interaction`:
  momentum-shape signals multiplied by `log_turnover_ma_20d`.

The interaction groups include raw interaction values and daily cross-sectional
rank versions.

## 5-anchor Readout

Focused ablation is logged in
`reports/week2_interaction_feature_ablation_log.md`.

- Control `momentum_shape + concentrated_top30`: mean `+2.808%`, worst
  `+0.797%`, win rate `1.00`.
- Best interaction mean did not exceed control.
- `momentum_vol_liq_interaction + shallow_regularized_top50` was the most stable
  interaction candidate in the 5-anchor gate: mean `+1.249%`, worst `+0.863%`,
  win rate `1.00`.

## 8-anchor Readout

Wider gate is logged in `reports/week2_interaction_feature_ablation_8x120.md`.

- Control `momentum_shape + concentrated_top30`: mean `+2.509%`, worst
  `-0.116%`, win rate `0.88`.
- Best stable interaction candidate:
  `momentum_vol_liq_interaction + subsampled_top80`, mean `+1.001%`, worst
  `+0.130%`, win rate `1.00`.

## Portfolio Check

Interaction portfolio ablation is logged in
`reports/week2_interaction_portfolio_ablation_log.md`.

For `momentum_vol_liq_interaction + concentrated_top30`, score-positive weights
did not recover the interaction feature set. It remains below the original
`momentum_shape` primary and still has a negative window.

## Decision

Do not replace the current `momentum_shape` primary with interaction features.

Keep `momentum_vol_liq_interaction + subsampled_top80` as a conservative fallback
idea only: it improves worst-window stability in the 8-anchor gate but gives up
too much mean excess return.

Next direction should test either:

- a narrower interaction subset instead of stacking all interaction features, or
- a fresh non-interaction feature family with stronger economic rationale.
