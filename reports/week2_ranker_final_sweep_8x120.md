# Week 2 Ranker Final Sweep

- Generated at: 2026-05-06 23:43:32
- As-of date: 2026-04-30
- Feature groups: momentum_shape
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-02-02, 2026-04-15, 2026-04-16, 2026-04-17, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Readout

- Best by worst-window excess: `top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07`, top_k=30, weight_rule=equal, mean `+0.846%`, worst `-4.121%`.
- Acceptance status: rejected; min_excess_5d must be non-negative.

## Summary

| spec | top_k | weight rule | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | 0.0564 | +0.846% | -4.121% | 0.88 |

## Parameter Specs

- `stable_d4_mcw20_l10_sub07`: n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.7, colsample_bytree=0.7, min_child_weight=20, reg_lambda=10.0

## Details

| anchor | spec | top_k | weight rule | rank IC | excess 5d | benchmark 5d |
| --- | --- | ---: | --- | ---: | ---: | ---: |
| 2026-02-02 | top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | -0.0135 | +0.117% | +3.412% |
| 2026-04-15 | top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | 0.2925 | +1.607% | +4.129% |
| 2026-04-16 | top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | 0.0869 | -4.121% | +1.407% |
| 2026-04-17 | top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | 0.0527 | +1.808% | +0.410% |
| 2026-04-20 | top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | 0.0608 | +1.844% | +0.109% |
| 2026-04-21 | top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | 0.0129 | +4.035% | -0.802% |
| 2026-04-22 | top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | -0.0652 | +1.075% | -0.403% |
| 2026-04-23 | top20_binary_pairwise_ndcg30_stable_d4_mcw20_l10_sub07 | 30 | equal | 0.0241 | +0.402% | +0.655% |