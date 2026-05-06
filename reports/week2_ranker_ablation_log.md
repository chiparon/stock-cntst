# Week 2 XGBRanker Ablation

- Generated at: 2026-05-06 22:49:19
- Context: week1 submission is closed; this is week2 XGBoost-only research.
- As-of date: 2026-04-30
- Feature groups: momentum_shape
- Portfolio: top_k=30, weight_rule=score_positive
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-04-15, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23
- Ranker label variants: rank_decile, top20_binary, rank_ventile

## Summary

| model | label variant | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | --- | ---: | ---: | ---: | ---: |
| regressor_current | raw_return | 0.0882 | +3.580% | +0.818% | 1.00 |
| xgb_ranker | top20_binary | 0.0642 | +2.743% | -1.490% | 0.80 |
| xgb_ranker | rank_ventile | 0.0149 | +0.677% | -1.475% | 0.60 |
| xgb_ranker | rank_decile | -0.0221 | -1.020% | -3.533% | 0.20 |

## Interpretation Rules

- Treat `regressor_current` as the control. Ranker is accepted only if it improves mean excess without weakening worst-window excess.
- Rank IC is diagnostic; the primary selector remains 5-trading-day excess return versus CSI500.
- Keep feature groups and portfolio fixed until the objective comparison is settled.

## Details

| anchor | model | label variant | rank IC | excess 5d | portfolio 5d | benchmark 5d |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 2026-04-15 | regressor_current | raw_return | 0.2942 | +3.578% | +7.707% | +4.129% |
| 2026-04-15 | xgb_ranker | rank_decile | -0.1569 | -3.533% | +0.595% | +4.129% |
| 2026-04-15 | xgb_ranker | rank_ventile | 0.0152 | -0.054% | +4.075% | +4.129% |
| 2026-04-15 | xgb_ranker | top20_binary | 0.3338 | +4.122% | +8.250% | +4.129% |
| 2026-04-20 | regressor_current | raw_return | 0.0810 | +4.775% | +4.883% | +0.109% |
| 2026-04-20 | xgb_ranker | rank_decile | -0.0609 | -0.148% | -0.039% | +0.109% |
| 2026-04-20 | xgb_ranker | rank_ventile | 0.0274 | +1.730% | +1.839% | +0.109% |
| 2026-04-20 | xgb_ranker | top20_binary | 0.0453 | +4.032% | +4.141% | +0.109% |
| 2026-04-21 | regressor_current | raw_return | 0.0322 | +5.629% | +4.827% | -0.802% |
| 2026-04-21 | xgb_ranker | rank_decile | 0.0275 | -1.830% | -2.633% | -0.802% |
| 2026-04-21 | xgb_ranker | rank_ventile | 0.0045 | +0.809% | +0.006% | -0.802% |
| 2026-04-21 | xgb_ranker | top20_binary | 0.0008 | +3.385% | +2.583% | -0.802% |
| 2026-04-22 | regressor_current | raw_return | 0.0330 | +3.099% | +2.696% | -0.403% |
| 2026-04-22 | xgb_ranker | rank_decile | 0.1123 | +2.606% | +2.203% | -0.403% |
| 2026-04-22 | xgb_ranker | rank_ventile | 0.0989 | +2.373% | +1.970% | -0.403% |
| 2026-04-22 | xgb_ranker | top20_binary | -0.0528 | +3.667% | +3.264% | -0.403% |
| 2026-04-23 | regressor_current | raw_return | 0.0004 | +0.818% | +1.473% | +0.655% |
| 2026-04-23 | xgb_ranker | rank_decile | -0.0327 | -2.196% | -1.541% | +0.655% |
| 2026-04-23 | xgb_ranker | rank_ventile | -0.0714 | -1.475% | -0.820% | +0.655% |
| 2026-04-23 | xgb_ranker | top20_binary | -0.0059 | -1.490% | -0.836% | +0.655% |