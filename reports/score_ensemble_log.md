# Score Ensemble Log

- Generated at: 2026-05-05 21:31:52
- As-of date: 2026-04-30
- Portfolio: top_k=30, weight_rule=score_positive
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-04-15, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Summary

| ensemble | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: |
| primary_robust_70_30 | 0.0952 | +3.041% | +0.927% | 1.00 |
| primary_robust_equal | 0.1003 | +2.940% | +0.841% | 1.00 |
| primary_only | 0.0882 | +2.919% | +0.805% | 1.00 |
| primary_heavy_all | 0.0967 | +2.296% | +1.078% | 1.00 |
| all_equal | 0.1001 | +2.235% | +0.967% | 1.00 |
| primary_rankliq_70_30 | 0.0914 | +2.165% | +0.718% | 1.00 |

## Details

| anchor | ensemble | rank IC | excess 5d | benchmark 5d |
| --- | --- | ---: | ---: | ---: |
| 2026-04-15 | all_equal | 0.2466 | +2.057% | +4.129% |
| 2026-04-15 | primary_heavy_all | 0.2731 | +2.410% | +4.129% |
| 2026-04-15 | primary_only | 0.2942 | +3.696% | +4.129% |
| 2026-04-15 | primary_rankliq_70_30 | 0.2664 | +2.553% | +4.129% |
| 2026-04-15 | primary_robust_70_30 | 0.2891 | +3.369% | +4.129% |
| 2026-04-15 | primary_robust_equal | 0.2816 | +3.117% | +4.129% |
| 2026-04-20 | all_equal | 0.1074 | +3.370% | +0.109% |
| 2026-04-20 | primary_heavy_all | 0.1010 | +3.188% | +0.109% |
| 2026-04-20 | primary_only | 0.0810 | +3.179% | +0.109% |
| 2026-04-20 | primary_rankliq_70_30 | 0.1042 | +2.372% | +0.109% |
| 2026-04-20 | primary_robust_70_30 | 0.0857 | +4.554% | +0.109% |
| 2026-04-20 | primary_robust_equal | 0.0845 | +4.671% | +0.109% |
| 2026-04-21 | all_equal | 0.1077 | +1.796% | -0.802% |
| 2026-04-21 | primary_heavy_all | 0.0713 | +2.158% | -0.802% |
| 2026-04-21 | primary_only | 0.0322 | +4.707% | -0.802% |
| 2026-04-21 | primary_rankliq_70_30 | 0.0518 | +2.319% | -0.802% |
| 2026-04-21 | primary_robust_70_30 | 0.0612 | +3.551% | -0.802% |
| 2026-04-21 | primary_robust_equal | 0.0951 | +3.074% | -0.802% |
| 2026-04-22 | all_equal | 0.0285 | +2.986% | -0.403% |
| 2026-04-22 | primary_heavy_all | 0.0321 | +2.643% | -0.403% |
| 2026-04-22 | primary_only | 0.0330 | +2.209% | -0.403% |
| 2026-04-22 | primary_rankliq_70_30 | 0.0358 | +2.865% | -0.403% |
| 2026-04-22 | primary_robust_70_30 | 0.0296 | +2.803% | -0.403% |
| 2026-04-22 | primary_robust_equal | 0.0245 | +2.996% | -0.403% |
| 2026-04-23 | all_equal | 0.0101 | +0.967% | +0.655% |
| 2026-04-23 | primary_heavy_all | 0.0060 | +1.078% | +0.655% |
| 2026-04-23 | primary_only | 0.0004 | +0.805% | +0.655% |
| 2026-04-23 | primary_rankliq_70_30 | -0.0014 | +0.718% | +0.655% |
| 2026-04-23 | primary_robust_70_30 | 0.0102 | +0.927% | +0.655% |
| 2026-04-23 | primary_robust_equal | 0.0156 | +0.841% | +0.655% |