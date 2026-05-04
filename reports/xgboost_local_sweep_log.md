# Local XGBoost Sweep Log

- Generated at: 2026-05-04 19:13:59
- As-of date: 2026-04-30
- Feature groups: momentum_shape
- Portfolio: top_k=30, weight_rule=score_positive
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-04-15, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Summary

| spec | mean IC | mean excess 5d | min excess 5d | win 5d | params |
| --- | ---: | ---: | ---: | ---: | --- |
| current_d4_mcw10_l5_lr005 | 0.0882 | +3.580% | +0.818% | 1.00 | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=5.0 |
| d4_mcw20_l10_lr005_sub07 | 0.1015 | +3.170% | +2.415% | 1.00 | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.7, colsample_bytree=0.7, min_child_weight=20, reg_lambda=10.0 |
| d4_mcw10_l10_lr005 | 0.0697 | +3.077% | +1.528% | 1.00 | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=10.0 |
| d4_mcw20_l20_lr005 | 0.0860 | +3.062% | +1.295% | 1.00 | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=20.0 |
| d4_mcw40_l10_lr005 | 0.0884 | +2.826% | +0.914% | 1.00 | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=40, reg_lambda=10.0 |
| d4_mcw20_l10_lr005 | 0.0878 | +2.821% | +1.093% | 1.00 | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=10.0 |
| d5_mcw10_l10_lr005 | 0.1008 | +2.712% | -0.025% | 0.80 | n_estimators=500, max_depth=5, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=10.0 |
| d4_mcw20_l10_lr003 | 0.0966 | +2.537% | +1.216% | 1.00 | n_estimators=800, max_depth=4, learning_rate=0.03, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=10.0 |
| d4_mcw20_l5_lr005 | 0.0762 | +2.450% | -0.936% | 0.80 | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=5.0 |
| d4_mcw10_l5_lr003 | 0.1059 | +2.190% | +0.230% | 1.00 | n_estimators=800, max_depth=4, learning_rate=0.03, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=5.0 |
| d5_mcw20_l10_lr003 | 0.1088 | +1.945% | -2.080% | 0.80 | n_estimators=800, max_depth=5, learning_rate=0.03, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=10.0 |
| d3_mcw20_l5_lr005 | 0.0945 | +1.890% | +1.304% | 1.00 | n_estimators=500, max_depth=3, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=5.0 |
| d3_mcw20_l10_lr005 | 0.0897 | +1.884% | +0.707% | 1.00 | n_estimators=500, max_depth=3, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=10.0 |
| d5_mcw10_l5_lr005 | 0.0802 | +1.871% | +0.233% | 1.00 | n_estimators=500, max_depth=5, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=5.0 |
| d3_mcw10_l5_lr005 | 0.0999 | +1.868% | +0.783% | 1.00 | n_estimators=500, max_depth=3, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=5.0 |
| d5_mcw20_l10_lr005 | 0.0991 | +1.706% | -0.981% | 0.80 | n_estimators=500, max_depth=5, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=10.0 |
| d3_mcw20_l10_lr005_sub07 | 0.0885 | +1.591% | +0.364% | 1.00 | n_estimators=500, max_depth=3, learning_rate=0.05, subsample=0.7, colsample_bytree=0.7, min_child_weight=20, reg_lambda=10.0 |
| d3_mcw20_l10_lr003 | 0.0944 | +1.397% | -1.616% | 0.80 | n_estimators=800, max_depth=3, learning_rate=0.03, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=10.0 |

## Per-anchor Details

### current_d4_mcw10_l5_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2942 | +3.578% | +4.129% |
| 2026-04-20 | 0.0810 | +4.775% | +0.109% |
| 2026-04-21 | 0.0322 | +5.629% | -0.802% |
| 2026-04-22 | 0.0330 | +3.099% | -0.403% |
| 2026-04-23 | 0.0004 | +0.818% | +0.655% |

### d3_mcw10_l5_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2629 | +2.451% | +4.129% |
| 2026-04-20 | 0.1076 | +1.145% | +0.109% |
| 2026-04-21 | 0.0912 | +4.031% | -0.802% |
| 2026-04-22 | -0.0045 | +0.931% | -0.403% |
| 2026-04-23 | 0.0423 | +0.783% | +0.655% |

### d3_mcw20_l5_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2524 | +2.195% | +4.129% |
| 2026-04-20 | 0.1246 | +2.650% | +0.109% |
| 2026-04-21 | 0.0594 | +1.304% | -0.802% |
| 2026-04-22 | 0.0251 | +1.624% | -0.403% |
| 2026-04-23 | 0.0112 | +1.675% | +0.655% |

### d3_mcw20_l10_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2228 | +2.235% | +4.129% |
| 2026-04-20 | 0.0958 | +0.707% | +0.109% |
| 2026-04-21 | 0.0550 | +1.732% | -0.802% |
| 2026-04-22 | 0.0267 | +2.501% | -0.403% |
| 2026-04-23 | 0.0485 | +2.245% | +0.655% |

### d4_mcw20_l5_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2114 | +1.223% | +4.129% |
| 2026-04-20 | 0.0793 | +4.084% | +0.109% |
| 2026-04-21 | 0.0347 | +5.499% | -0.802% |
| 2026-04-22 | 0.0173 | +2.382% | -0.403% |
| 2026-04-23 | 0.0381 | -0.936% | +0.655% |

### d4_mcw10_l10_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2182 | +1.528% | +4.129% |
| 2026-04-20 | 0.0814 | +4.066% | +0.109% |
| 2026-04-21 | 0.0326 | +5.404% | -0.802% |
| 2026-04-22 | 0.0003 | +1.534% | -0.403% |
| 2026-04-23 | 0.0159 | +2.854% | +0.655% |

### d4_mcw20_l10_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2235 | +1.238% | +4.129% |
| 2026-04-20 | 0.1376 | +3.941% | +0.109% |
| 2026-04-21 | 0.0351 | +5.352% | -0.802% |
| 2026-04-22 | 0.0344 | +2.484% | -0.403% |
| 2026-04-23 | 0.0084 | +1.093% | +0.655% |

### d4_mcw40_l10_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2629 | +1.945% | +4.129% |
| 2026-04-20 | 0.1062 | +3.392% | +0.109% |
| 2026-04-21 | 0.0352 | +5.433% | -0.802% |
| 2026-04-22 | 0.0252 | +2.447% | -0.403% |
| 2026-04-23 | 0.0126 | +0.914% | +0.655% |

### d4_mcw20_l20_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2121 | +1.640% | +4.129% |
| 2026-04-20 | 0.1334 | +4.273% | +0.109% |
| 2026-04-21 | 0.0350 | +5.355% | -0.802% |
| 2026-04-22 | 0.0364 | +2.748% | -0.403% |
| 2026-04-23 | 0.0130 | +1.295% | +0.655% |

### d5_mcw10_l5_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2787 | +1.892% | +4.129% |
| 2026-04-20 | 0.0773 | +1.921% | +0.109% |
| 2026-04-21 | 0.0214 | +2.878% | -0.802% |
| 2026-04-22 | -0.0057 | +2.429% | -0.403% |
| 2026-04-23 | 0.0294 | +0.233% | +0.655% |

### d5_mcw10_l10_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2888 | +3.520% | +4.129% |
| 2026-04-20 | 0.1220 | +3.991% | +0.109% |
| 2026-04-21 | 0.0317 | +2.345% | -0.802% |
| 2026-04-22 | 0.0182 | +3.727% | -0.403% |
| 2026-04-23 | 0.0434 | -0.025% | +0.655% |

### d5_mcw20_l10_lr005

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2886 | +2.271% | +4.129% |
| 2026-04-20 | 0.1194 | +2.311% | +0.109% |
| 2026-04-21 | 0.0363 | +2.442% | -0.802% |
| 2026-04-22 | 0.0118 | +2.488% | -0.403% |
| 2026-04-23 | 0.0396 | -0.981% | +0.655% |

### d4_mcw10_l5_lr003

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2763 | +2.443% | +4.129% |
| 2026-04-20 | 0.1022 | +3.119% | +0.109% |
| 2026-04-21 | 0.0730 | +2.754% | -0.802% |
| 2026-04-22 | 0.0326 | +2.405% | -0.403% |
| 2026-04-23 | 0.0454 | +0.230% | +0.655% |

### d4_mcw20_l10_lr003

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2613 | +2.412% | +4.129% |
| 2026-04-20 | 0.0863 | +3.485% | +0.109% |
| 2026-04-21 | 0.0722 | +2.690% | -0.802% |
| 2026-04-22 | 0.0216 | +2.883% | -0.403% |
| 2026-04-23 | 0.0416 | +1.216% | +0.655% |

### d3_mcw20_l10_lr003

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2626 | +2.672% | +4.129% |
| 2026-04-20 | 0.1337 | +2.688% | +0.109% |
| 2026-04-21 | 0.0537 | +1.591% | -0.802% |
| 2026-04-22 | -0.0136 | +1.649% | -0.403% |
| 2026-04-23 | 0.0359 | -1.616% | +0.655% |

### d5_mcw20_l10_lr003

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2911 | +2.848% | +4.129% |
| 2026-04-20 | 0.1169 | +3.206% | +0.109% |
| 2026-04-21 | 0.1002 | +2.903% | -0.802% |
| 2026-04-22 | -0.0104 | +2.845% | -0.403% |
| 2026-04-23 | 0.0461 | -2.080% | +0.655% |

### d4_mcw20_l10_lr005_sub07

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2518 | +2.415% | +4.129% |
| 2026-04-20 | 0.0851 | +5.003% | +0.109% |
| 2026-04-21 | 0.1281 | +2.638% | -0.802% |
| 2026-04-22 | 0.0096 | +3.152% | -0.403% |
| 2026-04-23 | 0.0331 | +2.642% | +0.655% |

### d3_mcw20_l10_lr005_sub07

| anchor | rank IC | excess 5d | benchmark 5d |
| --- | ---: | ---: | ---: |
| 2026-04-15 | 0.2584 | +1.921% | +4.129% |
| 2026-04-20 | 0.0914 | +1.542% | +0.109% |
| 2026-04-21 | 0.0641 | +1.757% | -0.802% |
| 2026-04-22 | -0.0177 | +0.364% | -0.403% |
| 2026-04-23 | 0.0465 | +2.369% | +0.655% |
