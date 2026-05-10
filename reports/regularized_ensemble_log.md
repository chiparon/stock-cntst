# Score Ensemble Log

- Generated at: 2026-05-10 20:40:12
- As-of date: 2026-04-30
- Portfolio: top_k=30, weight_rule=score_positive
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-04-15, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Model Specs

| model | groups | params |
| --- | --- | --- |
| primary_momentum | momentum_shape | n_estimators=700, max_depth=4, learning_rate=0.03, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=8.0, reg_alpha=0.05, gamma=0.05 |
| robust_momentum | momentum_shape | n_estimators=900, max_depth=3, learning_rate=0.03, subsample=0.7, colsample_bytree=0.7, min_child_weight=30, reg_lambda=15.0, reg_alpha=0.1, gamma=0.1 |
| rank_liquidity | rank_all,liquidity_log | n_estimators=700, max_depth=3, learning_rate=0.04, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=10.0, reg_alpha=0.05, gamma=0.05 |

## Ensemble Weights

| ensemble | weights |
| --- | --- |
| primary_only | primary_momentum=1.00 |
| primary_robust_70_30 | primary_momentum=0.70, robust_momentum=0.30 |
| primary_rankliq_70_30 | primary_momentum=0.70, rank_liquidity=0.30 |
| primary_robust_equal | primary_momentum=0.50, robust_momentum=0.50 |
| primary_robust_rankliq_60_25_15 | primary_momentum=0.60, robust_momentum=0.25, rank_liquidity=0.15 |
| primary_heavy_all | primary_momentum=0.60, robust_momentum=0.20, rank_liquidity=0.20 |
| all_equal | primary_momentum=0.33, robust_momentum=0.33, rank_liquidity=0.33 |

## Summary

| ensemble | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: |
| primary_rankliq_70_30 | 0.1056 | +2.712% | +1.148% | 1.00 |
| primary_heavy_all | 0.1055 | +2.679% | +1.193% | 1.00 |
| primary_robust_rankliq_60_25_15 | 0.1041 | +2.629% | +1.193% | 1.00 |
| all_equal | 0.1056 | +2.464% | +0.797% | 1.00 |
| primary_only | 0.0987 | +2.390% | +1.121% | 1.00 |
| primary_robust_70_30 | 0.0995 | +2.302% | +1.106% | 1.00 |
| primary_robust_equal | 0.0984 | +2.149% | +0.934% | 1.00 |

## Details

| anchor | ensemble | rank IC | excess 5d | benchmark 5d |
| --- | --- | ---: | ---: | ---: |
| 2026-04-15 | all_equal | 0.2725 | +3.156% | +4.129% |
| 2026-04-15 | primary_heavy_all | 0.2680 | +3.345% | +4.129% |
| 2026-04-15 | primary_only | 0.2458 | +3.091% | +4.129% |
| 2026-04-15 | primary_rankliq_70_30 | 0.2553 | +2.885% | +4.129% |
| 2026-04-15 | primary_robust_70_30 | 0.2646 | +3.449% | +4.129% |
| 2026-04-15 | primary_robust_equal | 0.2754 | +3.628% | +4.129% |
| 2026-04-15 | primary_robust_rankliq_60_25_15 | 0.2693 | +3.476% | +4.129% |
| 2026-04-20 | all_equal | 0.1085 | +4.825% | +0.109% |
| 2026-04-20 | primary_heavy_all | 0.1040 | +5.487% | +0.109% |
| 2026-04-20 | primary_only | 0.0887 | +4.990% | +0.109% |
| 2026-04-20 | primary_rankliq_70_30 | 0.1068 | +5.983% | +0.109% |
| 2026-04-20 | primary_robust_70_30 | 0.0919 | +4.034% | +0.109% |
| 2026-04-20 | primary_robust_equal | 0.0876 | +3.092% | +0.109% |
| 2026-04-20 | primary_robust_rankliq_60_25_15 | 0.1023 | +5.272% | +0.109% |
| 2026-04-21 | all_equal | 0.0907 | +1.702% | -0.802% |
| 2026-04-21 | primary_heavy_all | 0.0883 | +1.656% | -0.802% |
| 2026-04-21 | primary_only | 0.0791 | +1.341% | -0.802% |
| 2026-04-21 | primary_rankliq_70_30 | 0.0954 | +1.959% | -0.802% |
| 2026-04-21 | primary_robust_70_30 | 0.0746 | +1.106% | -0.802% |
| 2026-04-21 | primary_robust_equal | 0.0712 | +0.934% | -0.802% |
| 2026-04-21 | primary_robust_rankliq_60_25_15 | 0.0837 | +1.501% | -0.802% |
| 2026-04-22 | all_equal | 0.0156 | +1.840% | -0.403% |
| 2026-04-22 | primary_heavy_all | 0.0230 | +1.715% | -0.403% |
| 2026-04-22 | primary_only | 0.0302 | +1.121% | -0.403% |
| 2026-04-22 | primary_rankliq_70_30 | 0.0261 | +1.586% | -0.403% |
| 2026-04-22 | primary_robust_70_30 | 0.0215 | +1.634% | -0.403% |
| 2026-04-22 | primary_robust_equal | 0.0148 | +1.815% | -0.403% |
| 2026-04-22 | primary_robust_rankliq_60_25_15 | 0.0214 | +1.703% | -0.403% |
| 2026-04-23 | all_equal | 0.0407 | +0.797% | +0.655% |
| 2026-04-23 | primary_heavy_all | 0.0441 | +1.193% | +0.655% |
| 2026-04-23 | primary_only | 0.0495 | +1.408% | +0.655% |
| 2026-04-23 | primary_rankliq_70_30 | 0.0446 | +1.148% | +0.655% |
| 2026-04-23 | primary_robust_70_30 | 0.0447 | +1.289% | +0.655% |
| 2026-04-23 | primary_robust_equal | 0.0428 | +1.279% | +0.655% |
| 2026-04-23 | primary_robust_rankliq_60_25_15 | 0.0438 | +1.193% | +0.655% |

## Stage Conclusion

- Selected ensemble: `primary_rankliq_70_30`.
- Best mean excess 5d: +2.712%.
- Best mean IC: 0.1056.
- The winning blend is still a regularized XGBoost stack, but the cross-sectional rank blend now leans on the complementary rank/liquidity model rather than only momentum models.