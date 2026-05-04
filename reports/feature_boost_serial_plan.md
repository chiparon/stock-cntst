# Feature Boost Serial Plan

## Current Read

The project already has a reproducible XGBoost baseline and a compact stage-1
parameter sweep. The best logged configuration is `shallow_regularized_top50`
with validation rank IC `0.1314`, but the local sanity portfolio for
`2026-04-24` to `2026-04-30` underperformed CSI500 by `-1.965%` excess return.

This means the main bottleneck is not simply another XGBoost parameter or a
larger feature set. The current selection signal is still judged mainly by the
last 10 labeled dates' rank IC, while the live task is a single as-of-date
portfolio evaluated by short-horizon excess return. We are still preparing the
week 1 submission; however, because week 1's evaluation window is shortened by
the holiday calendar, the validation gate keeps using a 5-trading-day holding
window to avoid overfitting to one compressed 3-trading-day event.

## Major Direction

Use a test-like rolling portfolio validation gate before adding more features.

The validation gate should:

- Treat the latest prediction date as the live test domain.
- Select historical anchor dates whose cross-sectional feature distribution is
  closest to that prediction date.
- For every anchor date, train only on information available by that anchor.
- Predict the anchor cross-section, build a top-K portfolio, and score the
  next 5 trading days by excess return versus CSI500.
- Rank experiments by average excess return, win rate, worst window, and rank
  IC as a secondary diagnostic.

## Partner Feature Plan Feasibility

The partner's feature-boosting plan is useful, but should be downstream of the
validation gate. Otherwise, more features may only improve local rank IC without
improving live excess return.

Recommended feature priority:

1. Cross-sectional rank normalization for all continuous features.
   This is low leakage risk and well aligned with CSI500 cross-sectional stock
   selection. Keep raw features and add `_rank` versions rather than replacing
   the originals.
2. Volatility regime features.
   Add `vol_5d`, `vol_10d`, `vol_5d_over_20d`, and `vol_10d_over_20d` to
   distinguish calm markets from short-term volatility spikes.
3. Liquidity log features.
   Add `log1p(volume)` and log-based rolling statistics to reduce heavy-tail
   effects in volume and turnover.
4. CSI500-relative strength features.
   This is highly relevant because scoring is excess return, but it needs a
   cleaner data join with `data/index.parquet`, so it should come after the
   first low-risk feature batch.
5. Momentum-shape features.
   Add slope/acceleration style signals such as `ret_20d - ret_5d` and
   `ret_60d - ret_20d`. A plain `ret_120d` is lower priority because it reduces
   usable early samples and may be less relevant to the 5-day holding window.

Lower priority:

- `rev_1d = -ret_1d` and `rev_5d = -ret_5d` are exact sign flips of existing
  features, so they do not add information. If short-term reversal is tested,
  add a missing horizon such as `ret_3d` / `rev_3d` and rank-normalized forms.

## Serial Execution

1. Build `testlike_xgboost_validation.py` as the experiment gate.
2. Run existing stage-1 XGBoost configs through that gate.
3. Add a feature-group switch for ablation.
4. Test the first low-risk feature group:
   `rank_all + vol_regime + liquidity_log`.
5. Add CSI500-relative features only after the gate is working.
6. Use similar-stock-cluster purged validation as a pressure test, not as the
   primary selector.

## Decision Rule

A feature group is accepted only if it improves the test-like rolling portfolio
metrics without materially worsening worst-window excess return. Rank IC can be
used as a diagnostic, but not as the sole selection metric.

## Implementation Status

- Added `scripts/testlike_xgboost_validation.py`.
- Added this planning note under `reports/`.
- Added optional feature groups in `src/csi500_ml/features.py` while keeping the
  default `FEATURE_COLUMNS` unchanged for existing baseline scripts.
- Available feature groups: `rank_all`, `vol_regime`, `liquidity_log`,
  `momentum_shape`.
- Full baseline-gate result is logged in `reports/testlike_validation_log.md`.
- First low-risk feature batch result is logged in
  `reports/testlike_validation_rank_vol_liquidity_log.md`.
- Added `scripts/generate_xgboost_submission.py` to turn a selected validation
  winner into a checked submission CSV.
- Added `scripts/run_feature_ablation.py` for fixed-anchor feature ablation.
- Generated `submissions/week1_candidate.csv` from the best ablation result; it
  passes submission validation.

## First Gate Readout

Baseline features under the test-like gate selected anchors:
`2026-04-15`, `2026-04-20`, `2026-04-21`, `2026-04-22`, `2026-04-23`.
The best 5-day mean excess return came from `slow_learning_top50` at `+1.362%`,
not from the original last-10-day-IC winner `shallow_regularized_top50`.

The first low-risk feature batch used:
`rank_all`, `vol_regime`, `liquidity_log`.
It now uses the same baseline-selected anchors as the baseline gate, which keeps
feature ablation comparable. The best 5-day mean excess return came from
`concentrated_top30` at `+1.397%`, with 5-day win rate `1.00` and worst 5-day
excess `+0.173%`. This is also more stable than `shallow_regularized_top50`,
which reached `+1.361%` mean 5-day excess but had worst 5-day excess `-0.692%`.

The anchor-selection AUC should be interpreted only as a domain-shift diagnostic
for the validation gate. By default, anchors are selected with baseline features
even when the model uses an expanded feature group, so AUC remains comparable
across feature ablations.

## Feature Ablation Readout

Full ablation results are logged in `reports/feature_ablation_log.md`. The best
feature set is `momentum_shape` with `concentrated_top30`: mean 5-day excess
`+2.808%`, worst 5-day excess `+0.797%`, and 5-day win rate `1.00`.

Important negative result: adding all currently available feature groups is not
better. `rank_all,vol_regime,liquidity_log,momentum_shape` drops to mean 5-day
excess `+1.174%` with worst 5-day excess `-0.820%`, so broad feature stacking is
not accepted at this stage.

## Momentum Follow-up

`momentum_shape` was split into `mom_ret3`, `mom_trend_20_5`, and
`mom_trend_60_20`. The full group remains strongest. The best partial subset is
`mom_ret3,mom_trend_60_20` with `concentrated_top30`: mean 5-day excess
`+1.992%`, worst 5-day excess `+0.672%`, and 5-day win rate `1.00`.

The stability check with a wider anchor set (`top_dates=8`,
`recent_lookback=120`) still favors `momentum_shape + concentrated_top30`, with
mean 5-day excess `+2.509%`. Its worst 5-day excess becomes `-0.116%`, so it is
less perfectly stable under the wider check, but it remains well ahead of the
rank-liquidity alternative (`+1.665%` mean 5-day excess).

## Portfolio Construction Readout

Portfolio ablation is logged in `reports/portfolio_ablation_log.md`. With the
model fixed to `momentum_shape + concentrated_top30`, `score_positive` weighting
dominates the previous rank weighting. The best setting is `top_k=30` with
`score_positive`: mean 5-day excess `+3.580%`, worst 5-day excess `+0.818%`,
and 5-day win rate `1.00`.

The current generated candidate uses `concentrated_top30`, `momentum_shape`,
`top_k=30`, and `score_positive` weighting.

## Local XGBoost Sweep Readout

Local XGBoost parameter results are logged in `reports/xgboost_local_sweep_log.md`
and `reports/xgboost_local_sweep_8x120.md`. The current parameter set remains
the mean-return winner after fixing `momentum_shape`, `top_k=30`, and
`score_positive` weighting:

- 5-anchor gate: mean 5-day excess `+3.580%`, worst 5-day excess `+0.818%`.
- 8-anchor stability gate: mean 5-day excess `+3.142%`, worst 5-day excess
  `-0.163%`.

The strongest robust alternative is `d4_mcw20_l10_lr005_sub07`
(`min_child_weight=20`, `reg_lambda=10`, `subsample=0.7`,
`colsample_bytree=0.7`). It has lower mean 5-day excess, but good stability:

- 5-anchor gate: mean `+3.170%`, worst `+2.415%`.
- 8-anchor stability gate: mean `+2.761%`, worst `-0.105%`.

Decision: keep the current parameters as the primary candidate because they win
on mean excess in both gates. Keep the sub07 variant as a robust fallback if the
final risk preference shifts toward worst-window stability.
