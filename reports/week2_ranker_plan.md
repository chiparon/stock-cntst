# Week 2 Ranker Plan

## Context

Week 1 submission is closed. The week1 candidate remains a completed artifact,
not the active optimization target. Week 2 starts from the best week1 research
state but should treat the next submission as a fresh research cycle.

The active model family constraint is unchanged: keep the work inside XGBoost
for now. XGBRanker is therefore allowed because it changes the objective within
XGBoost rather than switching to a different model family.

## Research Question

Can a ranking objective beat the current XGBRegressor control when everything
else is held fixed?

Fixed controls:

- Feature groups: `momentum_shape`.
- Portfolio: `top_k=30`, `weight_rule=score_positive`.
- Anchor selection: baseline-feature adversarial test-like dates.
- Scoring: 5-trading-day excess return versus CSI500.

Ranker variants:

- `rank_decile`: each date's 5-day forward returns are converted to 10 ordered
  relevance buckets.
- `top20_binary`: top 20% names by 5-day forward return are labeled 1; the
  rest are labeled 0.
- `rank_ventile`: each date's 5-day forward returns are converted to 20 ordered
  relevance buckets.

XGBoost 3.2 ranking objectives require non-negative integer relevance labels, so
continuous return/rank labels are intentionally discretized before training.

## Acceptance Rule

Accept Ranker only if it beats `regressor_current` on mean 5-day excess return
without weakening worst-window excess return. Rank IC remains a diagnostic, not
the primary selector.

Do not combine Ranker with new feature groups, softmax weights, or ensemble
changes until this objective-only comparison is settled.

## Implementation

- Added `scripts/run_ranker_ablation.py`.
- The script writes results to `reports/week2_ranker_ablation_log.md`.
- The script is intentionally independent of the existing week1 candidate
  generator, so week1 artifacts remain reproducible.

## First Readout

The first full run is logged in `reports/week2_ranker_ablation_log.md`.

- Control `regressor_current`: mean 5-day excess `+3.580%`, worst `+0.818%`.
- Best Ranker variant `top20_binary`: mean `+2.743%`, worst `-1.490%`.
- `rank_ventile` and `rank_decile` are weaker and are not accepted.

Decision: do not replace the regressor control with Ranker yet. If Ranker work
continues, focus on `top20_binary` with a small parameter sweep and possibly a
less aggressive portfolio, because the objective-only comparison shows that the
current Ranker setup loses on worst-window stability.

## Rescue Sweep Readout

The focused rescue sweep is logged in
`reports/week2_ranker_rescue_sweep_log.md`. It fixed the only viable Ranker
label (`top20_binary`) and swept a compact grid of regularization settings plus
`top_k` / weighting rules.

- Control best remains `current_d4_mcw10_l5_sub08`, `top_k=30`,
  `score_positive`: mean `+3.580%`, worst `+0.818%`.
- Best Ranker remains the original Ranker parameter set, `top_k=30`,
  `score_positive`: mean `+2.743%`, worst `-1.490%`.
- The most promising stabilized Ranker alternative is
  `ranker_d4_mcw20_l10_sub07`, `top_k=30`, `rank`: mean `+2.579%`, worst
  `-0.371%`. This improves worst-window loss versus the original Ranker but
  still fails the acceptance rule and remains below the regressor control.

Decision: close Ranker as a primary week2 direction for now. Keep it as a logged
negative result. The next week2 research direction should return to the current
regressor control and test small interaction features, especially momentum times
volatility and momentum times liquidity.
