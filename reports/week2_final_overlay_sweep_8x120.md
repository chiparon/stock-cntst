# Portfolio Overlay Sweep

- Generated at: 2026-05-10 19:32:52
- As-of date: 2026-05-08
- Feature groups: momentum_shape
- Primary spec: current_d4_mcw10_l5_lr005
- Robust spec: d4_mcw20_l10_lr005_sub07
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.9512
- Selected anchors: 2026-01-08, 2026-01-09, 2026-01-12, 2026-01-15, 2026-01-23, 2026-01-26, 2026-04-21, 2026-04-22

## Summary

| candidate | family | avg excess 5d | max excess 5d | min excess 5d | win 5d | avg portfolio 5d | avg names | avg max weight | params |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| primary_voladj_v1_k35_cap100_p1.4 | primary_vol_adjust | +0.627% | +5.671% | -3.336% | 0.62 | +0.569% | 35.0 | 7.84% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap100_p1.4 | primary_vol_adjust | +0.589% | +5.656% | -3.282% | 0.75 | +0.531% | 30.0 | 7.98% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap100_p1.4 | primary_vol_adjust | +0.586% | +5.846% | -3.683% | 0.62 | +0.528% | 35.0 | 7.71% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k35_cap100_p1.25 | primary_vol_adjust | +0.568% | +5.421% | -3.323% | 0.62 | +0.510% | 35.0 | 7.83% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap100_p1.25 | primary_vol_adjust | +0.559% | +5.420% | -3.269% | 0.75 | +0.500% | 30.0 | 7.98% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap100_p1.4 | primary_vol_adjust | +0.556% | +5.842% | -3.588% | 0.62 | +0.498% | 30.0 | 7.88% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k35_cap100_p1.4 | primary_vol_adjust | +0.528% | +6.019% | -4.147% | 0.62 | +0.470% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap100_p1.25 | primary_vol_adjust | +0.522% | +5.585% | -3.702% | 0.62 | +0.464% | 35.0 | 7.68% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap100_p1.25 | primary_vol_adjust | +0.520% | +5.595% | -3.604% | 0.62 | +0.462% | 30.0 | 7.86% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k30_cap100_p1.1 | primary_vol_adjust | +0.516% | +5.187% | -3.235% | 0.75 | +0.458% | 30.0 | 7.97% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap100_p1.1 | primary_vol_adjust | +0.512% | +5.174% | -3.289% | 0.62 | +0.454% | 35.0 | 7.82% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k40_cap100_p1.4 | primary_vol_adjust | +0.502% | +5.641% | -3.381% | 0.62 | +0.444% | 40.0 | 7.71% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap100_p1.4 | primary_vol_adjust | +0.497% | +6.025% | -4.083% | 0.62 | +0.439% | 30.0 | 7.66% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap100_p1 | primary_vol_adjust | +0.478% | +5.013% | -3.253% | 0.62 | +0.420% | 35.0 | 7.81% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap100_p1 | primary_vol_adjust | +0.478% | +5.036% | -3.195% | 0.75 | +0.420% | 30.0 | 7.97% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k40_cap100_p1.4 | primary_vol_adjust | +0.473% | +5.816% | -3.694% | 0.62 | +0.415% | 40.0 | 7.61% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap100_p1.1 | primary_vol_adjust | +0.472% | +5.349% | -3.608% | 0.62 | +0.414% | 30.0 | 7.83% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k35_cap100_p1.25 | primary_vol_adjust | +0.463% | +5.747% | -4.163% | 0.62 | +0.405% | 35.0 | 7.48% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap100_p1.25 | primary_vol_adjust | +0.460% | +5.767% | -4.097% | 0.62 | +0.402% | 30.0 | 7.64% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap100_p1.1 | primary_vol_adjust | +0.459% | +5.325% | -3.711% | 0.62 | +0.401% | 35.0 | 7.65% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap100_p1.25 | primary_vol_adjust | +0.448% | +5.379% | -3.356% | 0.62 | +0.390% | 40.0 | 7.70% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap085_p1.4 | primary_vol_adjust | +0.431% | +5.394% | -3.809% | 0.62 | +0.373% | 35.0 | 6.90% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap100_p1 | primary_vol_adjust | +0.429% | +5.188% | -3.601% | 0.62 | +0.371% | 30.0 | 7.81% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap100_p1.4 | primary_vol_adjust | +0.423% | +5.988% | -4.154% | 0.62 | +0.365% | 40.0 | 7.40% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap085_p1.25 | primary_vol_adjust | +0.422% | +5.266% | -3.731% | 0.62 | +0.364% | 35.0 | 6.89% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap100_p1 | primary_vol_adjust | +0.420% | +5.154% | -3.709% | 0.62 | +0.362% | 35.0 | 7.61% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap100_p1.25 | primary_vol_adjust | +0.413% | +5.542% | -3.707% | 0.62 | +0.354% | 40.0 | 7.57% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k30_cap100_p1.1 | primary_vol_adjust | +0.412% | +5.508% | -4.099% | 0.62 | +0.353% | 30.0 | 7.61% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap085_p1.4 | primary_vol_adjust | +0.411% | +5.501% | -3.909% | 0.62 | +0.353% | 35.0 | 6.81% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_k35_cap100_p1.4 | primary_score_power | +0.408% | +6.355% | -5.048% | 0.62 | +0.349% | 35.0 | 7.11% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k35_cap085_p1.25 | primary_vol_adjust | +0.404% | +5.433% | -3.875% | 0.62 | +0.346% | 35.0 | 6.81% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap100_p1.1 | primary_vol_adjust | +0.400% | +5.116% | -3.305% | 0.62 | +0.342% | 40.0 | 7.69% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap100_p1.1 | primary_vol_adjust | +0.399% | +5.475% | -4.168% | 0.62 | +0.341% | 35.0 | 7.45% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap085_p1.1 | primary_vol_adjust | +0.393% | +5.024% | -3.622% | 0.62 | +0.335% | 35.0 | 6.89% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap085_p1.4 | primary_vol_adjust | +0.387% | +5.368% | -3.797% | 0.75 | +0.329% | 30.0 | 7.04% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap085_p1.25 | primary_vol_adjust | +0.379% | +5.263% | -3.727% | 0.75 | +0.321% | 30.0 | 7.04% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap100_p1.4 | primary_score_power | +0.377% | +6.380% | -5.048% | 0.62 | +0.319% | 30.0 | 7.24% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k30_cap085_p1.4 | primary_vol_adjust | +0.369% | +5.475% | -3.895% | 0.62 | +0.311% | 30.0 | 6.95% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap100_p1 | primary_vol_adjust | +0.369% | +4.944% | -3.250% | 0.62 | +0.311% | 40.0 | 7.68% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap085_p1.4 | primary_vol_adjust | +0.368% | +5.607% | -4.175% | 0.62 | +0.310% | 35.0 | 6.73% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap100_p1 | primary_vol_adjust | +0.368% | +5.338% | -4.089% | 0.62 | +0.310% | 30.0 | 7.59% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k30_cap085_p1.25 | primary_vol_adjust | +0.367% | +5.435% | -3.849% | 0.62 | +0.308% | 30.0 | 6.95% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap085_p1.1 | primary_vol_adjust | +0.366% | +5.178% | -3.841% | 0.62 | +0.308% | 35.0 | 6.80% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k35_cap085_p1 | primary_vol_adjust | +0.364% | +4.860% | -3.532% | 0.62 | +0.306% | 35.0 | 6.88% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k40_cap100_p1.25 | primary_vol_adjust | +0.362% | +5.703% | -4.164% | 0.62 | +0.304% | 40.0 | 7.37% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k35_cap085_p1.25 | primary_vol_adjust | +0.361% | +5.557% | -4.163% | 0.62 | +0.303% | 35.0 | 6.73% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap085_p1.1 | primary_vol_adjust | +0.360% | +5.037% | -3.616% | 0.75 | +0.302% | 30.0 | 7.04% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap100_p1 | primary_vol_adjust | +0.359% | +5.294% | -4.162% | 0.62 | +0.301% | 35.0 | 7.42% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k40_cap100_p1.1 | primary_vol_adjust | +0.356% | +5.266% | -3.708% | 0.62 | +0.298% | 40.0 | 7.53% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap085_p1.4 | primary_vol_adjust | +0.349% | +5.387% | -3.802% | 0.62 | +0.291% | 40.0 | 6.77% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap085_p1 | primary_vol_adjust | +0.349% | +4.883% | -3.523% | 0.75 | +0.291% | 30.0 | 7.03% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_k35_cap100_p1.25 | primary_score_power | +0.342% | +6.063% | -5.060% | 0.62 | +0.284% | 35.0 | 7.09% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k30_cap085_p1.1 | primary_vol_adjust | +0.339% | +5.202% | -3.800% | 0.62 | +0.281% | 30.0 | 6.95% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap100_p1.25 | primary_score_power | +0.339% | +6.101% | -5.059% | 0.62 | +0.280% | 30.0 | 7.22% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap085_p1.4 | primary_vol_adjust | +0.333% | +5.493% | -3.926% | 0.62 | +0.275% | 40.0 | 6.70% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k30_cap085_p1.4 | primary_vol_adjust | +0.331% | +5.589% | -4.147% | 0.62 | +0.273% | 30.0 | 6.86% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap085_p1 | primary_vol_adjust | +0.329% | +5.004% | -3.801% | 0.62 | +0.271% | 35.0 | 6.80% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap085_p1.25 | primary_vol_adjust | +0.325% | +5.225% | -3.708% | 0.62 | +0.267% | 40.0 | 6.77% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap085_p1.25 | primary_vol_adjust | +0.323% | +5.539% | -4.136% | 0.62 | +0.265% | 30.0 | 6.86% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k35_cap085_p1.1 | primary_vol_adjust | +0.322% | +5.330% | -4.168% | 0.62 | +0.264% | 35.0 | 6.70% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_k40_cap100_p1.4 | primary_score_power | +0.322% | +6.323% | -5.037% | 0.62 | +0.264% | 40.0 | 7.02% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k30_cap085_p1 | primary_vol_adjust | +0.320% | +5.038% | -3.761% | 0.62 | +0.262% | 30.0 | 6.94% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap100_p1 | primary_vol_adjust | +0.318% | +5.084% | -3.698% | 0.62 | +0.260% | 40.0 | 7.49% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap085_p1.25 | primary_vol_adjust | +0.311% | +5.390% | -3.896% | 0.62 | +0.252% | 40.0 | 6.69% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap100_p1.1 | primary_vol_adjust | +0.304% | +5.414% | -4.160% | 0.62 | +0.245% | 40.0 | 7.33% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap085_p1.1 | primary_vol_adjust | +0.301% | +5.364% | -4.105% | 0.62 | +0.243% | 30.0 | 6.86% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap085_p1.4 | primary_vol_adjust | +0.298% | +5.600% | -4.192% | 0.62 | +0.239% | 40.0 | 6.62% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap100_p1.1 | primary_score_power | +0.288% | +5.818% | -5.057% | 0.62 | +0.230% | 30.0 | 7.20% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k40_cap085_p1.1 | primary_vol_adjust | +0.284% | +4.965% | -3.586% | 0.62 | +0.226% | 40.0 | 6.75% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k40_cap085_p1.25 | primary_vol_adjust | +0.282% | +5.546% | -4.169% | 0.62 | +0.224% | 40.0 | 6.62% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k35_cap085_p1 | primary_vol_adjust | +0.280% | +5.146% | -4.162% | 0.62 | +0.222% | 35.0 | 6.67% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap085_p1 | primary_vol_adjust | +0.278% | +5.190% | -4.089% | 0.62 | +0.220% | 30.0 | 6.84% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap100_p1.1 | primary_score_power | +0.276% | +5.766% | -5.058% | 0.62 | +0.217% | 35.0 | 7.07% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap100_p1 | primary_vol_adjust | +0.265% | +5.222% | -4.145% | 0.62 | +0.207% | 40.0 | 7.30% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k40_cap085_p1.1 | primary_vol_adjust | +0.259% | +5.117% | -3.845% | 0.62 | +0.200% | 40.0 | 6.68% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_k40_cap100_p1.25 | primary_score_power | +0.258% | +6.017% | -5.042% | 0.62 | +0.200% | 40.0 | 7.00% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k40_cap085_p1 | primary_vol_adjust | +0.257% | +4.790% | -3.512% | 0.62 | +0.199% | 40.0 | 6.74% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap075_p1.1 | primary_vol_adjust | +0.243% | +4.907% | -4.196% | 0.62 | +0.185% | 35.0 | 6.26% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap100_p1 | primary_score_power | +0.243% | +5.629% | -5.043% | 0.62 | +0.185% | 30.0 | 7.19% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap075_p1 | primary_vol_adjust | +0.242% | +4.753% | -4.033% | 0.62 | +0.184% | 35.0 | 6.25% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap075_p1.25 | primary_vol_adjust | +0.234% | +4.997% | -4.387% | 0.62 | +0.176% | 35.0 | 6.27% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_k35_cap085_p1.4 | primary_score_power | +0.234% | +5.821% | -5.048% | 0.62 | +0.176% | 35.0 | 6.36% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap100_p1 | primary_score_power | +0.234% | +5.567% | -5.045% | 0.62 | +0.175% | 35.0 | 7.05% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap075_p1.4 | primary_vol_adjust | +0.232% | +5.093% | -4.526% | 0.62 | +0.173% | 35.0 | 6.27% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k40_cap085_p1 | primary_vol_adjust | +0.228% | +4.932% | -3.790% | 0.62 | +0.170% | 40.0 | 6.67% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap075_p1 | primary_vol_adjust | +0.226% | +4.898% | -4.140% | 0.62 | +0.168% | 35.0 | 6.17% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap075_p1.1 | primary_vol_adjust | +0.226% | +4.991% | -4.250% | 0.62 | +0.168% | 35.0 | 6.18% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap085_p1.1 | primary_vol_adjust | +0.224% | +5.268% | -4.160% | 0.62 | +0.166% | 40.0 | 6.58% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap085_p1.25 | primary_score_power | +0.221% | +5.751% | -5.060% | 0.62 | +0.163% | 35.0 | 6.34% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k35_cap075_p1.4 | primary_vol_adjust | +0.219% | +5.166% | -4.526% | 0.62 | +0.161% | 35.0 | 6.19% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap075_p1.25 | primary_vol_adjust | +0.218% | +5.063% | -4.408% | 0.62 | +0.160% | 35.0 | 6.19% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| blend_primary80_robust20 | primary_robust_blend | +0.211% | +5.031% | -4.342% | 0.38 | +0.153% | 51.6 | 6.58% | primary_share=0.80, max_weight=0.100 |
| primary_voladj_v0.5_k35_cap075_p1.4 | primary_vol_adjust | +0.205% | +5.239% | -4.530% | 0.62 | +0.146% | 35.0 | 6.11% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k35_cap075_p1 | primary_vol_adjust | +0.204% | +5.041% | -4.275% | 0.62 | +0.146% | 35.0 | 6.09% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap085_p1.4 | primary_score_power | +0.202% | +5.817% | -5.048% | 0.62 | +0.144% | 30.0 | 6.49% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k35_cap075_p1.1 | primary_vol_adjust | +0.201% | +5.081% | -4.354% | 0.62 | +0.143% | 35.0 | 6.10% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap085_p1.1 | primary_score_power | +0.199% | +5.626% | -5.058% | 0.62 | +0.141% | 35.0 | 6.32% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap100_p1.1 | primary_score_power | +0.197% | +5.704% | -5.030% | 0.62 | +0.139% | 40.0 | 6.97% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k30_cap075_p1.1 | primary_vol_adjust | +0.197% | +4.911% | -4.242% | 0.75 | +0.139% | 30.0 | 6.41% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap075_p1.25 | primary_vol_adjust | +0.197% | +5.129% | -4.459% | 0.62 | +0.138% | 35.0 | 6.10% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| blend_primary70_robust30 | primary_robust_blend | +0.196% | +4.732% | -3.991% | 0.50 | +0.137% | 51.6 | 6.28% | primary_share=0.70, max_weight=0.100 |
| primary_voladj_v1_k30_cap075_p1 | primary_vol_adjust | +0.195% | +4.777% | -4.088% | 0.75 | +0.137% | 30.0 | 6.41% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap075_p1.4 | primary_vol_adjust | +0.194% | +5.086% | -4.521% | 0.75 | +0.135% | 30.0 | 6.42% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap075_p1.25 | primary_vol_adjust | +0.191% | +4.996% | -4.422% | 0.75 | +0.132% | 30.0 | 6.42% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap085_p1.25 | primary_score_power | +0.189% | +5.747% | -5.059% | 0.62 | +0.131% | 30.0 | 6.47% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap085_p1 | primary_vol_adjust | +0.187% | +5.073% | -4.145% | 0.62 | +0.129% | 40.0 | 6.55% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k30_cap075_p1 | primary_vol_adjust | +0.186% | +4.927% | -4.164% | 0.62 | +0.128% | 30.0 | 6.32% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_k40_cap085_p1.4 | primary_score_power | +0.183% | +5.814% | -5.037% | 0.62 | +0.125% | 40.0 | 6.27% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k30_cap075_p1.4 | primary_vol_adjust | +0.180% | +5.164% | -4.548% | 0.62 | +0.122% | 30.0 | 6.33% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap075_p1.1 | primary_vol_adjust | +0.180% | +4.972% | -4.288% | 0.62 | +0.122% | 30.0 | 6.32% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap075_p1.25 | primary_vol_adjust | +0.178% | +5.066% | -4.439% | 0.62 | +0.120% | 30.0 | 6.33% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap085_p1.1 | primary_score_power | +0.178% | +5.679% | -5.057% | 0.62 | +0.119% | 30.0 | 6.45% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap075_p1.4 | primary_vol_adjust | +0.169% | +5.241% | -4.549% | 0.62 | +0.111% | 30.0 | 6.24% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap075_p1.1 | primary_vol_adjust | +0.166% | +4.850% | -4.087% | 0.50 | +0.108% | 40.0 | 6.13% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_k40_cap085_p1.25 | primary_score_power | +0.164% | +5.741% | -5.042% | 0.62 | +0.106% | 40.0 | 6.25% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap075_p1 | primary_vol_adjust | +0.164% | +5.035% | -4.286% | 0.62 | +0.106% | 30.0 | 6.23% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| blend_primary50_robust50 | primary_robust_blend | +0.164% | +4.134% | -3.290% | 0.50 | +0.106% | 51.6 | 5.97% | primary_share=0.50, max_weight=0.100 |
| primary_voladj_v0.5_k30_cap075_p1.25 | primary_vol_adjust | +0.162% | +5.135% | -4.468% | 0.62 | +0.104% | 30.0 | 6.24% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap075_p1.1 | primary_vol_adjust | +0.160% | +5.062% | -4.373% | 0.62 | +0.102% | 30.0 | 6.23% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap075_p1.25 | primary_vol_adjust | +0.160% | +4.970% | -4.310% | 0.50 | +0.102% | 40.0 | 6.14% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_k40_cap100_p1 | primary_score_power | +0.157% | +5.493% | -5.007% | 0.62 | +0.099% | 40.0 | 6.94% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap075_p1.1 | primary_vol_adjust | +0.157% | +4.977% | -4.190% | 0.50 | +0.098% | 40.0 | 6.06% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_k35_cap085_p1 | primary_score_power | +0.155% | +5.424% | -5.045% | 0.62 | +0.096% | 35.0 | 6.30% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k40_cap075_p1.4 | primary_vol_adjust | +0.153% | +5.072% | -4.474% | 0.50 | +0.094% | 40.0 | 6.15% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap085_p1 | primary_score_power | +0.152% | +5.487% | -5.043% | 0.62 | +0.094% | 30.0 | 6.44% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap075_p1.25 | primary_vol_adjust | +0.150% | +5.036% | -4.345% | 0.50 | +0.092% | 40.0 | 6.07% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap075_p1 | primary_vol_adjust | +0.149% | +4.686% | -3.933% | 0.50 | +0.091% | 40.0 | 6.12% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k40_cap075_p1.4 | primary_vol_adjust | +0.146% | +5.146% | -4.484% | 0.50 | +0.088% | 40.0 | 6.07% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap075_p1 | primary_vol_adjust | +0.140% | +4.829% | -4.054% | 0.50 | +0.082% | 40.0 | 6.05% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap075_p1.1 | primary_vol_adjust | +0.139% | +5.067% | -4.310% | 0.50 | +0.081% | 40.0 | 5.99% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap100_p0.75 | primary_score_power | +0.138% | +5.163% | -4.941% | 0.62 | +0.079% | 30.0 | 7.13% | model=primary, top_k=30, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap075_p1.4 | primary_vol_adjust | +0.136% | +5.219% | -4.513% | 0.50 | +0.078% | 40.0 | 6.00% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap075_p1.25 | primary_vol_adjust | +0.134% | +5.117% | -4.426% | 0.50 | +0.076% | 40.0 | 5.99% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap100_p0.75 | primary_score_power | +0.132% | +5.078% | -4.947% | 0.62 | +0.074% | 35.0 | 6.97% | model=primary, top_k=35, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap075_p1 | primary_vol_adjust | +0.119% | +4.971% | -4.247% | 0.50 | +0.061% | 40.0 | 5.98% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_k40_cap085_p1.1 | primary_score_power | +0.119% | +5.562% | -5.030% | 0.62 | +0.060% | 40.0 | 6.22% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1.4 | primary_score_power | +0.107% | +5.403% | -5.048% | 0.62 | +0.049% | 35.0 | 5.86% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1.25 | primary_score_power | +0.094% | +5.330% | -5.060% | 0.62 | +0.036% | 35.0 | 5.84% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| robust_only_k30_cap100_p1 | robust_baseline | +0.085% | +3.152% | -3.927% | 0.50 | +0.026% | 30.0 | 8.88% | model=robust, top_k=30, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1.1 | primary_score_power | +0.083% | +5.261% | -5.058% | 0.62 | +0.025% | 35.0 | 5.82% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap085_p1 | primary_score_power | +0.080% | +5.348% | -5.007% | 0.62 | +0.022% | 40.0 | 6.19% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap075_p1.4 | primary_score_power | +0.080% | +5.399% | -5.048% | 0.62 | +0.022% | 30.0 | 5.99% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1 | primary_score_power | +0.077% | +5.218% | -5.045% | 0.62 | +0.019% | 35.0 | 5.80% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap075_p1.25 | primary_score_power | +0.067% | +5.326% | -5.059% | 0.62 | +0.008% | 30.0 | 5.97% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap085_p0.75 | primary_score_power | +0.064% | +5.013% | -4.941% | 0.62 | +0.006% | 30.0 | 6.38% | model=primary, top_k=30, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1.4 | primary_score_power | +0.056% | +5.396% | -5.037% | 0.50 | -0.002% | 40.0 | 5.77% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap085_p0.75 | primary_score_power | +0.055% | +4.926% | -4.947% | 0.62 | -0.003% | 35.0 | 6.22% | model=primary, top_k=35, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap075_p1.1 | primary_score_power | +0.054% | +5.256% | -5.057% | 0.62 | -0.004% | 30.0 | 5.95% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap075_p1 | primary_score_power | +0.047% | +5.212% | -5.043% | 0.62 | -0.011% | 30.0 | 5.94% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1.25 | primary_score_power | +0.046% | +5.319% | -5.042% | 0.50 | -0.012% | 40.0 | 5.75% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1.1 | primary_score_power | +0.037% | +5.247% | -5.030% | 0.50 | -0.022% | 40.0 | 5.72% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap100_p0.75 | primary_score_power | +0.031% | +4.974% | -4.874% | 0.62 | -0.027% | 40.0 | 6.85% | model=primary, top_k=40, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1 | primary_score_power | +0.019% | +5.202% | -5.007% | 0.50 | -0.039% | 40.0 | 5.69% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap075_p0.75 | primary_score_power | +0.011% | +4.913% | -4.941% | 0.62 | -0.048% | 30.0 | 5.88% | model=primary, top_k=30, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p0.75 | primary_score_power | +0.002% | +4.825% | -4.947% | 0.62 | -0.057% | 35.0 | 5.72% | model=primary, top_k=35, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap085_p0.75 | primary_score_power | -0.007% | +4.820% | -4.874% | 0.62 | -0.065% | 40.0 | 6.10% | model=primary, top_k=40, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p0.75 | primary_score_power | -0.059% | +4.718% | -4.874% | 0.50 | -0.118% | 40.0 | 5.60% | model=primary, top_k=40, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p0.75 | primary_score_power | -0.120% | +4.488% | -4.947% | 0.50 | -0.178% | 35.0 | 4.97% | model=primary, top_k=35, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1 | primary_score_power | -0.145% | +4.502% | -5.202% | 0.50 | -0.203% | 35.0 | 5.00% | model=primary, top_k=35, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p0.75 | primary_score_power | -0.155% | +4.465% | -4.874% | 0.50 | -0.214% | 40.0 | 4.85% | model=primary, top_k=40, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p0.75 | primary_score_power | -0.155% | +4.475% | -4.969% | 0.62 | -0.214% | 30.0 | 5.11% | model=primary, top_k=30, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1.1 | primary_score_power | -0.157% | +4.477% | -5.298% | 0.50 | -0.216% | 35.0 | 5.00% | model=primary, top_k=35, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1.4 | primary_score_power | -0.159% | +4.464% | -5.441% | 0.62 | -0.218% | 30.0 | 5.12% | model=primary, top_k=30, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1.25 | primary_score_power | -0.169% | +4.478% | -5.422% | 0.50 | -0.228% | 35.0 | 5.00% | model=primary, top_k=35, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1.4 | primary_score_power | -0.172% | +4.488% | -5.484% | 0.50 | -0.231% | 35.0 | 5.00% | model=primary, top_k=35, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1 | primary_score_power | -0.172% | +4.530% | -5.117% | 0.50 | -0.231% | 40.0 | 4.90% | model=primary, top_k=40, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1.25 | primary_score_power | -0.178% | +4.448% | -5.441% | 0.62 | -0.236% | 30.0 | 5.12% | model=primary, top_k=30, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1 | primary_score_power | -0.181% | +4.443% | -5.249% | 0.62 | -0.240% | 30.0 | 5.12% | model=primary, top_k=30, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1.1 | primary_score_power | -0.184% | +4.441% | -5.344% | 0.62 | -0.242% | 30.0 | 5.12% | model=primary, top_k=30, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.1 | primary_score_power | -0.191% | +4.490% | -5.219% | 0.50 | -0.249% | 40.0 | 4.90% | model=primary, top_k=40, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.25 | primary_score_power | -0.209% | +4.485% | -5.357% | 0.50 | -0.267% | 40.0 | 4.91% | model=primary, top_k=40, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.4 | primary_score_power | -0.222% | +4.494% | -5.471% | 0.50 | -0.280% | 40.0 | 4.91% | model=primary, top_k=40, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |

## Details

| anchor | candidate | excess 5d | portfolio 5d | benchmark 5d | names | max weight | primary IC | robust IC |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-01-08 | blend_primary50_robust50 | -2.012% | +2.152% | +4.164% | 52 | 5.59% | 0.0795 | -0.0138 |
| 2026-01-08 | blend_primary70_robust30 | -2.265% | +1.899% | +4.164% | 52 | 7.35% | 0.0795 | -0.0138 |
| 2026-01-08 | blend_primary80_robust20 | -2.391% | +1.773% | +4.164% | 52 | 8.24% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap060_p0.75 | -2.479% | +1.685% | +4.164% | 30 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap060_p1 | -2.479% | +1.685% | +4.164% | 30 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap060_p1.1 | -2.479% | +1.685% | +4.164% | 30 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap060_p1.25 | -2.479% | +1.685% | +4.164% | 30 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap060_p1.4 | -2.479% | +1.685% | +4.164% | 30 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap075_p0.75 | -2.541% | +1.623% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap075_p1 | -2.541% | +1.623% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap075_p1.1 | -2.541% | +1.623% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap075_p1.25 | -2.541% | +1.623% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap075_p1.4 | -2.541% | +1.623% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap085_p0.75 | -2.582% | +1.582% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap085_p1 | -2.582% | +1.582% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap085_p1.1 | -2.582% | +1.582% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap085_p1.25 | -2.582% | +1.582% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap085_p1.4 | -2.582% | +1.582% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap100_p0.75 | -2.644% | +1.520% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap100_p1 | -2.644% | +1.520% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap100_p1.1 | -2.644% | +1.520% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap100_p1.25 | -2.644% | +1.520% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k30_cap100_p1.4 | -2.644% | +1.520% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap060_p0.75 | -2.111% | +2.053% | +4.164% | 35 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap060_p1 | -2.111% | +2.053% | +4.164% | 35 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap060_p1.1 | -2.111% | +2.053% | +4.164% | 35 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap060_p1.25 | -2.111% | +2.053% | +4.164% | 35 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap060_p1.4 | -2.111% | +2.053% | +4.164% | 35 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap075_p0.75 | -2.179% | +1.985% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap075_p1 | -2.179% | +1.985% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap075_p1.1 | -2.179% | +1.985% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap075_p1.25 | -2.179% | +1.985% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap075_p1.4 | -2.179% | +1.985% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap085_p0.75 | -2.224% | +1.940% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap085_p1 | -2.224% | +1.940% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap085_p1.1 | -2.224% | +1.940% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap085_p1.25 | -2.224% | +1.940% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap085_p1.4 | -2.224% | +1.940% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap100_p0.75 | -2.292% | +1.872% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap100_p1 | -2.292% | +1.872% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap100_p1.1 | -2.292% | +1.872% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap100_p1.25 | -2.292% | +1.872% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k35_cap100_p1.4 | -2.292% | +1.872% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap060_p0.75 | -1.997% | +2.167% | +4.164% | 40 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap060_p1 | -1.997% | +2.167% | +4.164% | 40 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap060_p1.1 | -1.997% | +2.167% | +4.164% | 40 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap060_p1.25 | -1.997% | +2.167% | +4.164% | 40 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap060_p1.4 | -1.997% | +2.167% | +4.164% | 40 | 6.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap075_p0.75 | -2.067% | +2.097% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap075_p1 | -2.067% | +2.097% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap075_p1.1 | -2.067% | +2.097% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap075_p1.25 | -2.067% | +2.097% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap075_p1.4 | -2.067% | +2.097% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap085_p0.75 | -2.113% | +2.051% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap085_p1 | -2.113% | +2.051% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap085_p1.1 | -2.113% | +2.051% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap085_p1.25 | -2.113% | +2.051% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap085_p1.4 | -2.113% | +2.051% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap100_p0.75 | -2.183% | +1.981% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap100_p1 | -2.183% | +1.981% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap100_p1.1 | -2.183% | +1.981% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap100_p1.25 | -2.183% | +1.981% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_k40_cap100_p1.4 | -2.183% | +1.981% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap075_p1 | -2.631% | +1.533% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap075_p1.1 | -2.631% | +1.533% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap075_p1.25 | -2.631% | +1.533% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap075_p1.4 | -2.631% | +1.533% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap085_p1 | -2.671% | +1.493% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap085_p1.1 | -2.671% | +1.493% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap085_p1.25 | -2.671% | +1.493% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap085_p1.4 | -2.671% | +1.493% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap100_p1 | -2.732% | +1.432% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap100_p1.1 | -2.732% | +1.432% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap100_p1.25 | -2.732% | +1.432% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k30_cap100_p1.4 | -2.732% | +1.432% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap075_p1 | -2.288% | +1.876% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap075_p1.1 | -2.288% | +1.876% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap075_p1.25 | -2.288% | +1.876% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap075_p1.4 | -2.288% | +1.876% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap085_p1 | -2.332% | +1.832% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap085_p1.1 | -2.332% | +1.832% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap085_p1.25 | -2.332% | +1.832% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap085_p1.4 | -2.332% | +1.832% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap100_p1 | -2.398% | +1.766% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap100_p1.1 | -2.398% | +1.766% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap100_p1.25 | -2.398% | +1.766% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k35_cap100_p1.4 | -2.398% | +1.766% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap075_p1 | -2.162% | +2.002% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap075_p1.1 | -2.162% | +2.002% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap075_p1.25 | -2.162% | +2.002% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap075_p1.4 | -2.162% | +2.002% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap085_p1 | -2.208% | +1.956% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap085_p1.1 | -2.208% | +1.956% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap085_p1.25 | -2.208% | +1.956% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap085_p1.4 | -2.208% | +1.956% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap100_p1 | -2.276% | +1.888% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap100_p1.1 | -2.276% | +1.888% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap100_p1.25 | -2.276% | +1.888% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.5_k40_cap100_p1.4 | -2.276% | +1.888% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap075_p1 | -2.676% | +1.488% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap075_p1.1 | -2.676% | +1.488% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap075_p1.25 | -2.676% | +1.488% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap075_p1.4 | -2.676% | +1.488% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap085_p1 | -2.715% | +1.449% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap085_p1.1 | -2.715% | +1.449% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap085_p1.25 | -2.715% | +1.449% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap085_p1.4 | -2.715% | +1.449% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap100_p1 | -2.775% | +1.389% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap100_p1.1 | -2.775% | +1.389% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap100_p1.25 | -2.775% | +1.389% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k30_cap100_p1.4 | -2.775% | +1.389% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap075_p1 | -2.343% | +1.821% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap075_p1.1 | -2.343% | +1.821% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap075_p1.25 | -2.343% | +1.821% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap075_p1.4 | -2.343% | +1.821% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap085_p1 | -2.387% | +1.777% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap085_p1.1 | -2.387% | +1.777% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap085_p1.25 | -2.387% | +1.777% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap085_p1.4 | -2.387% | +1.777% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap100_p1 | -2.452% | +1.712% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap100_p1.1 | -2.452% | +1.712% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap100_p1.25 | -2.452% | +1.712% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k35_cap100_p1.4 | -2.452% | +1.712% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap075_p1 | -2.211% | +1.953% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap075_p1.1 | -2.211% | +1.953% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap075_p1.25 | -2.211% | +1.953% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap075_p1.4 | -2.211% | +1.953% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap085_p1 | -2.256% | +1.908% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap085_p1.1 | -2.256% | +1.908% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap085_p1.25 | -2.256% | +1.908% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap085_p1.4 | -2.256% | +1.908% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap100_p1 | -2.323% | +1.841% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap100_p1.1 | -2.323% | +1.841% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap100_p1.25 | -2.323% | +1.841% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v0.75_k40_cap100_p1.4 | -2.323% | +1.841% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap075_p1 | -2.720% | +1.444% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap075_p1.1 | -2.720% | +1.444% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap075_p1.25 | -2.720% | +1.444% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap075_p1.4 | -2.720% | +1.444% | +4.164% | 30 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap085_p1 | -2.759% | +1.405% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap085_p1.1 | -2.759% | +1.405% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap085_p1.25 | -2.759% | +1.405% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap085_p1.4 | -2.759% | +1.405% | +4.164% | 30 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap100_p1 | -2.818% | +1.346% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap100_p1.1 | -2.818% | +1.346% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap100_p1.25 | -2.818% | +1.346% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k30_cap100_p1.4 | -2.818% | +1.346% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap075_p1 | -2.399% | +1.765% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap075_p1.1 | -2.399% | +1.765% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap075_p1.25 | -2.399% | +1.765% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap075_p1.4 | -2.399% | +1.765% | +4.164% | 35 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap085_p1 | -2.442% | +1.722% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap085_p1.1 | -2.442% | +1.722% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap085_p1.25 | -2.442% | +1.722% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap085_p1.4 | -2.442% | +1.722% | +4.164% | 35 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap100_p1 | -2.506% | +1.658% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap100_p1.1 | -2.506% | +1.658% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap100_p1.25 | -2.506% | +1.658% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k35_cap100_p1.4 | -2.506% | +1.658% | +4.164% | 35 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap075_p1 | -2.260% | +1.904% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap075_p1.1 | -2.260% | +1.904% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap075_p1.25 | -2.260% | +1.904% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap075_p1.4 | -2.260% | +1.904% | +4.164% | 40 | 7.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap085_p1 | -2.304% | +1.860% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap085_p1.1 | -2.304% | +1.860% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap085_p1.25 | -2.304% | +1.860% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap085_p1.4 | -2.304% | +1.860% | +4.164% | 40 | 8.50% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap100_p1 | -2.371% | +1.793% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap100_p1.1 | -2.371% | +1.793% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap100_p1.25 | -2.371% | +1.793% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | primary_voladj_v1_k40_cap100_p1.4 | -2.371% | +1.793% | +4.164% | 40 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-08 | robust_only_k30_cap100_p1 | -1.381% | +2.783% | +4.164% | 30 | 10.00% | 0.0795 | -0.0138 |
| 2026-01-09 | blend_primary50_robust50 | +0.992% | +3.177% | +2.184% | 57 | 5.00% | -0.0704 | -0.0240 |
| 2026-01-09 | blend_primary70_robust30 | +1.033% | +3.217% | +2.184% | 57 | 7.00% | -0.0704 | -0.0240 |
| 2026-01-09 | blend_primary80_robust20 | +1.053% | +3.237% | +2.184% | 57 | 8.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap060_p0.75 | +0.174% | +2.359% | +2.184% | 30 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap060_p1 | +0.174% | +2.359% | +2.184% | 30 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap060_p1.1 | +0.174% | +2.359% | +2.184% | 30 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap060_p1.25 | +0.174% | +2.359% | +2.184% | 30 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap060_p1.4 | +0.174% | +2.359% | +2.184% | 30 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap075_p0.75 | +0.519% | +2.703% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap075_p1 | +0.519% | +2.703% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap075_p1.1 | +0.519% | +2.703% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap075_p1.25 | +0.519% | +2.703% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap075_p1.4 | +0.519% | +2.703% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap085_p0.75 | +0.749% | +2.933% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap085_p1 | +0.749% | +2.933% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap085_p1.1 | +0.749% | +2.933% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap085_p1.25 | +0.749% | +2.933% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap085_p1.4 | +0.749% | +2.933% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap100_p0.75 | +1.094% | +3.278% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap100_p1 | +1.094% | +3.278% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap100_p1.1 | +1.094% | +3.278% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap100_p1.25 | +1.094% | +3.278% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k30_cap100_p1.4 | +1.094% | +3.278% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap060_p0.75 | -0.315% | +1.869% | +2.184% | 35 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap060_p1 | -0.315% | +1.869% | +2.184% | 35 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap060_p1.1 | -0.315% | +1.869% | +2.184% | 35 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap060_p1.25 | -0.315% | +1.869% | +2.184% | 35 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap060_p1.4 | -0.315% | +1.869% | +2.184% | 35 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap075_p0.75 | +0.068% | +2.253% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap075_p1 | +0.068% | +2.253% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap075_p1.1 | +0.068% | +2.253% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap075_p1.25 | +0.068% | +2.253% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap075_p1.4 | +0.068% | +2.253% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap085_p0.75 | +0.324% | +2.508% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap085_p1 | +0.324% | +2.508% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap085_p1.1 | +0.324% | +2.508% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap085_p1.25 | +0.324% | +2.508% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap085_p1.4 | +0.324% | +2.508% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap100_p0.75 | +0.707% | +2.892% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap100_p1 | +0.707% | +2.892% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap100_p1.1 | +0.707% | +2.892% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap100_p1.25 | +0.707% | +2.892% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k35_cap100_p1.4 | +0.707% | +2.892% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap060_p0.75 | -0.422% | +1.763% | +2.184% | 40 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap060_p1 | -0.422% | +1.763% | +2.184% | 40 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap060_p1.1 | -0.422% | +1.763% | +2.184% | 40 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap060_p1.25 | -0.422% | +1.763% | +2.184% | 40 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap060_p1.4 | -0.422% | +1.763% | +2.184% | 40 | 6.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap075_p0.75 | -0.030% | +2.154% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap075_p1 | -0.030% | +2.154% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap075_p1.1 | -0.030% | +2.154% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap075_p1.25 | -0.030% | +2.154% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap075_p1.4 | -0.030% | +2.154% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap085_p0.75 | +0.231% | +2.416% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap085_p1 | +0.231% | +2.416% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap085_p1.1 | +0.231% | +2.416% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap085_p1.25 | +0.231% | +2.416% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap085_p1.4 | +0.231% | +2.416% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap100_p0.75 | +0.623% | +2.807% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap100_p1 | +0.623% | +2.807% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap100_p1.1 | +0.623% | +2.807% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap100_p1.25 | +0.623% | +2.807% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_k40_cap100_p1.4 | +0.623% | +2.807% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap075_p1 | +0.484% | +2.668% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap075_p1.1 | +0.484% | +2.668% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap075_p1.25 | +0.484% | +2.668% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap075_p1.4 | +0.484% | +2.668% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap085_p1 | +0.716% | +2.900% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap085_p1.1 | +0.716% | +2.900% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap085_p1.25 | +0.716% | +2.900% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap085_p1.4 | +0.716% | +2.900% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap100_p1 | +1.063% | +3.248% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap100_p1.1 | +1.063% | +3.248% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap100_p1.25 | +1.063% | +3.248% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k30_cap100_p1.4 | +1.063% | +3.248% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap075_p1 | +0.079% | +2.264% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap075_p1.1 | +0.079% | +2.264% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap075_p1.25 | +0.079% | +2.264% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap075_p1.4 | +0.079% | +2.264% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap085_p1 | +0.334% | +2.519% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap085_p1.1 | +0.334% | +2.519% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap085_p1.25 | +0.334% | +2.519% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap085_p1.4 | +0.334% | +2.519% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap100_p1 | +0.717% | +2.901% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap100_p1.1 | +0.717% | +2.901% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap100_p1.25 | +0.717% | +2.901% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k35_cap100_p1.4 | +0.717% | +2.901% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap075_p1 | -0.048% | +2.136% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap075_p1.1 | -0.048% | +2.136% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap075_p1.25 | -0.048% | +2.136% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap075_p1.4 | -0.048% | +2.136% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap085_p1 | +0.214% | +2.398% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap085_p1.1 | +0.214% | +2.398% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap085_p1.25 | +0.214% | +2.398% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap085_p1.4 | +0.214% | +2.398% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap100_p1 | +0.607% | +2.792% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap100_p1.1 | +0.607% | +2.792% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap100_p1.25 | +0.607% | +2.792% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.5_k40_cap100_p1.4 | +0.607% | +2.792% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap075_p1 | +0.468% | +2.652% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap075_p1.1 | +0.468% | +2.652% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap075_p1.25 | +0.468% | +2.652% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap075_p1.4 | +0.468% | +2.652% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap085_p1 | +0.700% | +2.885% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap085_p1.1 | +0.700% | +2.885% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap085_p1.25 | +0.700% | +2.885% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap085_p1.4 | +0.700% | +2.885% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap100_p1 | +1.050% | +3.234% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap100_p1.1 | +1.050% | +3.234% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap100_p1.25 | +1.050% | +3.234% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k30_cap100_p1.4 | +1.050% | +3.234% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap075_p1 | +0.082% | +2.267% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap075_p1.1 | +0.082% | +2.267% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap075_p1.25 | +0.082% | +2.267% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap075_p1.4 | +0.082% | +2.267% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap085_p1 | +0.337% | +2.522% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap085_p1.1 | +0.337% | +2.522% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap085_p1.25 | +0.337% | +2.522% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap085_p1.4 | +0.337% | +2.522% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap100_p1 | +0.719% | +2.904% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap100_p1.1 | +0.719% | +2.904% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap100_p1.25 | +0.719% | +2.904% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k35_cap100_p1.4 | +0.719% | +2.904% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap075_p1 | -0.061% | +2.124% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap075_p1.1 | -0.061% | +2.124% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap075_p1.25 | -0.061% | +2.124% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap075_p1.4 | -0.061% | +2.124% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap085_p1 | +0.202% | +2.387% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap085_p1.1 | +0.202% | +2.387% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap085_p1.25 | +0.202% | +2.387% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap085_p1.4 | +0.202% | +2.387% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap100_p1 | +0.597% | +2.781% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap100_p1.1 | +0.597% | +2.781% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap100_p1.25 | +0.597% | +2.781% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v0.75_k40_cap100_p1.4 | +0.597% | +2.781% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap075_p1 | +0.452% | +2.636% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap075_p1.1 | +0.452% | +2.636% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap075_p1.25 | +0.452% | +2.636% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap075_p1.4 | +0.452% | +2.636% | +2.184% | 30 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap085_p1 | +0.686% | +2.870% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap085_p1.1 | +0.686% | +2.870% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap085_p1.25 | +0.686% | +2.870% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap085_p1.4 | +0.686% | +2.870% | +2.184% | 30 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap100_p1 | +1.036% | +3.221% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap100_p1.1 | +1.036% | +3.221% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap100_p1.25 | +1.036% | +3.221% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k30_cap100_p1.4 | +1.036% | +3.221% | +2.184% | 30 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap075_p1 | +0.084% | +2.268% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap075_p1.1 | +0.084% | +2.268% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap075_p1.25 | +0.084% | +2.268% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap075_p1.4 | +0.084% | +2.268% | +2.184% | 35 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap085_p1 | +0.339% | +2.523% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap085_p1.1 | +0.339% | +2.523% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap085_p1.25 | +0.339% | +2.523% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap085_p1.4 | +0.339% | +2.523% | +2.184% | 35 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap100_p1 | +0.721% | +2.905% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap100_p1.1 | +0.721% | +2.905% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap100_p1.25 | +0.721% | +2.905% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k35_cap100_p1.4 | +0.721% | +2.905% | +2.184% | 35 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap075_p1 | -0.075% | +2.110% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap075_p1.1 | -0.075% | +2.110% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap075_p1.25 | -0.075% | +2.110% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap075_p1.4 | -0.075% | +2.110% | +2.184% | 40 | 7.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap085_p1 | +0.189% | +2.374% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap085_p1.1 | +0.189% | +2.374% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap085_p1.25 | +0.189% | +2.374% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap085_p1.4 | +0.189% | +2.374% | +2.184% | 40 | 8.50% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap100_p1 | +0.585% | +2.769% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap100_p1.1 | +0.585% | +2.769% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap100_p1.25 | +0.585% | +2.769% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | primary_voladj_v1_k40_cap100_p1.4 | +0.585% | +2.769% | +2.184% | 40 | 10.00% | -0.0704 | -0.0240 |
| 2026-01-09 | robust_only_k30_cap100_p1 | +0.891% | +3.076% | +2.184% | 30 | 6.77% | -0.0704 | -0.0240 |
| 2026-01-12 | blend_primary50_robust50 | +0.431% | +0.902% | +0.471% | 55 | 6.67% | 0.0659 | 0.1065 |
| 2026-01-12 | blend_primary70_robust30 | +0.104% | +0.575% | +0.471% | 55 | 5.33% | 0.0659 | 0.1065 |
| 2026-01-12 | blend_primary80_robust20 | -0.059% | +0.412% | +0.471% | 55 | 4.67% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap060_p0.75 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap060_p1 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap060_p1.1 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap060_p1.25 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap060_p1.4 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap075_p0.75 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap075_p1 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap075_p1.1 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap075_p1.25 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap075_p1.4 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap085_p0.75 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap085_p1 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap085_p1.1 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap085_p1.25 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap085_p1.4 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap100_p0.75 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap100_p1 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap100_p1.1 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap100_p1.25 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k30_cap100_p1.4 | -0.386% | +0.085% | +0.471% | 30 | 3.33% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap060_p0.75 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap060_p1 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap060_p1.1 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap060_p1.25 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap060_p1.4 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap075_p0.75 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap075_p1 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap075_p1.1 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap075_p1.25 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap075_p1.4 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap085_p0.75 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap085_p1 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap085_p1.1 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap085_p1.25 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap085_p1.4 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap100_p0.75 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap100_p1 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap100_p1.1 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap100_p1.25 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k35_cap100_p1.4 | -0.628% | -0.157% | +0.471% | 35 | 2.86% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap060_p0.75 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap060_p1 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap060_p1.1 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap060_p1.25 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap060_p1.4 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap075_p0.75 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap075_p1 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap075_p1.1 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap075_p1.25 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap075_p1.4 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap085_p0.75 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap085_p1 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap085_p1.1 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap085_p1.25 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap085_p1.4 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap100_p0.75 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap100_p1 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap100_p1.1 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap100_p1.25 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_k40_cap100_p1.4 | -0.619% | -0.149% | +0.471% | 40 | 2.50% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap075_p1 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap075_p1.1 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap075_p1.25 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap075_p1.4 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap085_p1 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap085_p1.1 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap085_p1.25 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap085_p1.4 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap100_p1 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap100_p1.1 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap100_p1.25 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k30_cap100_p1.4 | -0.142% | +0.328% | +0.471% | 30 | 3.76% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap075_p1 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap075_p1.1 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap075_p1.25 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap075_p1.4 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap085_p1 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap085_p1.1 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap085_p1.25 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap085_p1.4 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap100_p1 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap100_p1.1 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap100_p1.25 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k35_cap100_p1.4 | -0.415% | +0.055% | +0.471% | 35 | 3.24% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap075_p1 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap075_p1.1 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap075_p1.25 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap075_p1.4 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap085_p1 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap085_p1.1 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap085_p1.25 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap085_p1.4 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap100_p1 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap100_p1.1 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap100_p1.25 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.5_k40_cap100_p1.4 | -0.483% | -0.013% | +0.471% | 40 | 2.83% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap075_p1 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap075_p1.1 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap075_p1.25 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap075_p1.4 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap085_p1 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap085_p1.1 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap085_p1.25 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap085_p1.4 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap100_p1 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap100_p1.1 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap100_p1.25 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k30_cap100_p1.4 | -0.030% | +0.440% | +0.471% | 30 | 3.98% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap075_p1 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap075_p1.1 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap075_p1.25 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap075_p1.4 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap085_p1 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap085_p1.1 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap085_p1.25 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap085_p1.4 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap100_p1 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap100_p1.1 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap100_p1.25 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k35_cap100_p1.4 | -0.319% | +0.152% | +0.471% | 35 | 3.43% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap075_p1 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap075_p1.1 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap075_p1.25 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap075_p1.4 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap085_p1 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap085_p1.1 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap085_p1.25 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap085_p1.4 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap100_p1 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap100_p1.1 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap100_p1.25 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v0.75_k40_cap100_p1.4 | -0.423% | +0.048% | +0.471% | 40 | 3.00% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap075_p1 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap075_p1.1 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap075_p1.25 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap075_p1.4 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap085_p1 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap085_p1.1 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap085_p1.25 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap085_p1.4 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap100_p1 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap100_p1.1 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap100_p1.25 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k30_cap100_p1.4 | +0.075% | +0.546% | +0.471% | 30 | 4.20% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap075_p1 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap075_p1.1 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap075_p1.25 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap075_p1.4 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap085_p1 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap085_p1.1 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap085_p1.25 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap085_p1.4 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap100_p1 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap100_p1.1 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap100_p1.25 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k35_cap100_p1.4 | -0.229% | +0.241% | +0.471% | 35 | 3.62% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap075_p1 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap075_p1.1 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap075_p1.25 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap075_p1.4 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap085_p1 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap085_p1.1 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap085_p1.25 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap085_p1.4 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap100_p1 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap100_p1.1 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap100_p1.25 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | primary_voladj_v1_k40_cap100_p1.4 | -0.367% | +0.104% | +0.471% | 40 | 3.17% | 0.0659 | 0.1065 |
| 2026-01-12 | robust_only_k30_cap100_p1 | +1.248% | +1.718% | +0.471% | 30 | 10.00% | 0.0659 | 0.1065 |
| 2026-01-15 | blend_primary50_robust50 | -1.905% | +0.093% | +1.998% | 53 | 2.24% | 0.0773 | -0.0726 |
| 2026-01-15 | blend_primary70_robust30 | -1.096% | +0.902% | +1.998% | 53 | 3.06% | 0.0773 | -0.0726 |
| 2026-01-15 | blend_primary80_robust20 | -0.692% | +1.306% | +1.998% | 53 | 3.47% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap060_p0.75 | +0.132% | +2.131% | +1.998% | 30 | 4.23% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap060_p1 | +0.117% | +2.115% | +1.998% | 30 | 4.29% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap060_p1.1 | +0.113% | +2.112% | +1.998% | 30 | 4.31% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap060_p1.25 | +0.110% | +2.108% | +1.998% | 30 | 4.32% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap060_p1.4 | +0.108% | +2.106% | +1.998% | 30 | 4.33% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap075_p0.75 | +0.132% | +2.131% | +1.998% | 30 | 4.23% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap075_p1 | +0.117% | +2.115% | +1.998% | 30 | 4.29% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap075_p1.1 | +0.113% | +2.112% | +1.998% | 30 | 4.31% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap075_p1.25 | +0.110% | +2.108% | +1.998% | 30 | 4.32% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap075_p1.4 | +0.108% | +2.106% | +1.998% | 30 | 4.33% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap085_p0.75 | +0.132% | +2.131% | +1.998% | 30 | 4.23% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap085_p1 | +0.117% | +2.115% | +1.998% | 30 | 4.29% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap085_p1.1 | +0.113% | +2.112% | +1.998% | 30 | 4.31% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap085_p1.25 | +0.110% | +2.108% | +1.998% | 30 | 4.32% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap085_p1.4 | +0.108% | +2.106% | +1.998% | 30 | 4.33% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap100_p0.75 | +0.132% | +2.131% | +1.998% | 30 | 4.23% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap100_p1 | +0.117% | +2.115% | +1.998% | 30 | 4.29% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap100_p1.1 | +0.113% | +2.112% | +1.998% | 30 | 4.31% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap100_p1.25 | +0.110% | +2.108% | +1.998% | 30 | 4.32% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k30_cap100_p1.4 | +0.108% | +2.106% | +1.998% | 30 | 4.33% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap060_p0.75 | +0.198% | +2.196% | +1.998% | 35 | 4.13% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap060_p1 | +0.148% | +2.147% | +1.998% | 35 | 4.25% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap060_p1.1 | +0.137% | +2.135% | +1.998% | 35 | 4.27% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap060_p1.25 | +0.125% | +2.123% | +1.998% | 35 | 4.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap060_p1.4 | +0.117% | +2.115% | +1.998% | 35 | 4.32% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap075_p0.75 | +0.198% | +2.196% | +1.998% | 35 | 4.13% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap075_p1 | +0.148% | +2.147% | +1.998% | 35 | 4.25% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap075_p1.1 | +0.137% | +2.135% | +1.998% | 35 | 4.27% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap075_p1.25 | +0.125% | +2.123% | +1.998% | 35 | 4.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap075_p1.4 | +0.117% | +2.115% | +1.998% | 35 | 4.32% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap085_p0.75 | +0.198% | +2.196% | +1.998% | 35 | 4.13% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap085_p1 | +0.148% | +2.147% | +1.998% | 35 | 4.25% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap085_p1.1 | +0.137% | +2.135% | +1.998% | 35 | 4.27% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap085_p1.25 | +0.125% | +2.123% | +1.998% | 35 | 4.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap085_p1.4 | +0.117% | +2.115% | +1.998% | 35 | 4.32% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap100_p0.75 | +0.198% | +2.196% | +1.998% | 35 | 4.13% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap100_p1 | +0.148% | +2.147% | +1.998% | 35 | 4.25% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap100_p1.1 | +0.137% | +2.135% | +1.998% | 35 | 4.27% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap100_p1.25 | +0.125% | +2.123% | +1.998% | 35 | 4.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k35_cap100_p1.4 | +0.117% | +2.115% | +1.998% | 35 | 4.32% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap060_p0.75 | +0.187% | +2.185% | +1.998% | 40 | 4.04% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap060_p1 | +0.144% | +2.142% | +1.998% | 40 | 4.20% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap060_p1.1 | +0.134% | +2.132% | +1.998% | 40 | 4.24% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap060_p1.25 | +0.123% | +2.121% | +1.998% | 40 | 4.28% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap060_p1.4 | +0.116% | +2.114% | +1.998% | 40 | 4.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap075_p0.75 | +0.187% | +2.185% | +1.998% | 40 | 4.04% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap075_p1 | +0.144% | +2.142% | +1.998% | 40 | 4.20% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap075_p1.1 | +0.134% | +2.132% | +1.998% | 40 | 4.24% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap075_p1.25 | +0.123% | +2.121% | +1.998% | 40 | 4.28% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap075_p1.4 | +0.116% | +2.114% | +1.998% | 40 | 4.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap085_p0.75 | +0.187% | +2.185% | +1.998% | 40 | 4.04% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap085_p1 | +0.144% | +2.142% | +1.998% | 40 | 4.20% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap085_p1.1 | +0.134% | +2.132% | +1.998% | 40 | 4.24% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap085_p1.25 | +0.123% | +2.121% | +1.998% | 40 | 4.28% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap085_p1.4 | +0.116% | +2.114% | +1.998% | 40 | 4.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap100_p0.75 | +0.187% | +2.185% | +1.998% | 40 | 4.04% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap100_p1 | +0.144% | +2.142% | +1.998% | 40 | 4.20% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap100_p1.1 | +0.134% | +2.132% | +1.998% | 40 | 4.24% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap100_p1.25 | +0.123% | +2.121% | +1.998% | 40 | 4.28% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_k40_cap100_p1.4 | +0.116% | +2.114% | +1.998% | 40 | 4.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap075_p1 | +0.219% | +2.218% | +1.998% | 30 | 4.85% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap075_p1.1 | +0.215% | +2.214% | +1.998% | 30 | 4.87% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap075_p1.25 | +0.211% | +2.209% | +1.998% | 30 | 4.89% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap075_p1.4 | +0.209% | +2.207% | +1.998% | 30 | 4.91% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap085_p1 | +0.219% | +2.218% | +1.998% | 30 | 4.85% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap085_p1.1 | +0.215% | +2.214% | +1.998% | 30 | 4.87% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap085_p1.25 | +0.211% | +2.209% | +1.998% | 30 | 4.89% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap085_p1.4 | +0.209% | +2.207% | +1.998% | 30 | 4.91% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap100_p1 | +0.219% | +2.218% | +1.998% | 30 | 4.85% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap100_p1.1 | +0.215% | +2.214% | +1.998% | 30 | 4.87% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap100_p1.25 | +0.211% | +2.209% | +1.998% | 30 | 4.89% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k30_cap100_p1.4 | +0.209% | +2.207% | +1.998% | 30 | 4.91% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap075_p1 | +0.253% | +2.251% | +1.998% | 35 | 4.77% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap075_p1.1 | +0.239% | +2.237% | +1.998% | 35 | 4.81% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap075_p1.25 | +0.224% | +2.223% | +1.998% | 35 | 4.85% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap075_p1.4 | +0.215% | +2.213% | +1.998% | 35 | 4.88% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap085_p1 | +0.253% | +2.251% | +1.998% | 35 | 4.77% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap085_p1.1 | +0.239% | +2.237% | +1.998% | 35 | 4.81% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap085_p1.25 | +0.224% | +2.223% | +1.998% | 35 | 4.85% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap085_p1.4 | +0.215% | +2.213% | +1.998% | 35 | 4.88% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap100_p1 | +0.253% | +2.251% | +1.998% | 35 | 4.77% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap100_p1.1 | +0.239% | +2.237% | +1.998% | 35 | 4.81% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap100_p1.25 | +0.224% | +2.223% | +1.998% | 35 | 4.85% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k35_cap100_p1.4 | +0.215% | +2.213% | +1.998% | 35 | 4.88% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap075_p1 | +0.238% | +2.236% | +1.998% | 40 | 4.68% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap075_p1.1 | +0.226% | +2.225% | +1.998% | 40 | 4.74% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap075_p1.25 | +0.215% | +2.213% | +1.998% | 40 | 4.80% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap075_p1.4 | +0.207% | +2.205% | +1.998% | 40 | 4.84% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap085_p1 | +0.238% | +2.236% | +1.998% | 40 | 4.68% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap085_p1.1 | +0.226% | +2.225% | +1.998% | 40 | 4.74% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap085_p1.25 | +0.215% | +2.213% | +1.998% | 40 | 4.80% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap085_p1.4 | +0.207% | +2.205% | +1.998% | 40 | 4.84% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap100_p1 | +0.238% | +2.236% | +1.998% | 40 | 4.68% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap100_p1.1 | +0.226% | +2.225% | +1.998% | 40 | 4.74% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap100_p1.25 | +0.215% | +2.213% | +1.998% | 40 | 4.80% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.5_k40_cap100_p1.4 | +0.207% | +2.205% | +1.998% | 40 | 4.84% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap075_p1 | +0.267% | +2.266% | +1.998% | 30 | 5.14% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap075_p1.1 | +0.263% | +2.261% | +1.998% | 30 | 5.16% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap075_p1.25 | +0.258% | +2.257% | +1.998% | 30 | 5.19% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap075_p1.4 | +0.256% | +2.254% | +1.998% | 30 | 5.21% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap085_p1 | +0.267% | +2.266% | +1.998% | 30 | 5.14% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap085_p1.1 | +0.263% | +2.261% | +1.998% | 30 | 5.16% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap085_p1.25 | +0.258% | +2.257% | +1.998% | 30 | 5.19% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap085_p1.4 | +0.256% | +2.254% | +1.998% | 30 | 5.21% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap100_p1 | +0.267% | +2.266% | +1.998% | 30 | 5.14% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap100_p1.1 | +0.263% | +2.261% | +1.998% | 30 | 5.16% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap100_p1.25 | +0.258% | +2.257% | +1.998% | 30 | 5.19% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k30_cap100_p1.4 | +0.256% | +2.254% | +1.998% | 30 | 5.21% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap075_p1 | +0.303% | +2.301% | +1.998% | 35 | 5.03% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap075_p1.1 | +0.288% | +2.286% | +1.998% | 35 | 5.08% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap075_p1.25 | +0.271% | +2.270% | +1.998% | 35 | 5.13% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap075_p1.4 | +0.261% | +2.259% | +1.998% | 35 | 5.17% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap085_p1 | +0.303% | +2.301% | +1.998% | 35 | 5.03% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap085_p1.1 | +0.288% | +2.286% | +1.998% | 35 | 5.08% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap085_p1.25 | +0.271% | +2.270% | +1.998% | 35 | 5.13% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap085_p1.4 | +0.261% | +2.259% | +1.998% | 35 | 5.17% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap100_p1 | +0.303% | +2.301% | +1.998% | 35 | 5.03% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap100_p1.1 | +0.288% | +2.286% | +1.998% | 35 | 5.08% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap100_p1.25 | +0.271% | +2.270% | +1.998% | 35 | 5.13% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k35_cap100_p1.4 | +0.261% | +2.259% | +1.998% | 35 | 5.17% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap075_p1 | +0.281% | +2.280% | +1.998% | 40 | 4.93% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap075_p1.1 | +0.270% | +2.268% | +1.998% | 40 | 5.00% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap075_p1.25 | +0.258% | +2.256% | +1.998% | 40 | 5.07% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap075_p1.4 | +0.250% | +2.248% | +1.998% | 40 | 5.12% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap085_p1 | +0.281% | +2.280% | +1.998% | 40 | 4.93% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap085_p1.1 | +0.270% | +2.268% | +1.998% | 40 | 5.00% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap085_p1.25 | +0.258% | +2.256% | +1.998% | 40 | 5.07% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap085_p1.4 | +0.250% | +2.248% | +1.998% | 40 | 5.12% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap100_p1 | +0.281% | +2.280% | +1.998% | 40 | 4.93% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap100_p1.1 | +0.270% | +2.268% | +1.998% | 40 | 5.00% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap100_p1.25 | +0.258% | +2.256% | +1.998% | 40 | 5.07% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v0.75_k40_cap100_p1.4 | +0.250% | +2.248% | +1.998% | 40 | 5.12% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap075_p1 | +0.313% | +2.311% | +1.998% | 30 | 5.43% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap075_p1.1 | +0.308% | +2.307% | +1.998% | 30 | 5.46% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap075_p1.25 | +0.304% | +2.302% | +1.998% | 30 | 5.49% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap075_p1.4 | +0.301% | +2.299% | +1.998% | 30 | 5.51% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap085_p1 | +0.313% | +2.311% | +1.998% | 30 | 5.43% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap085_p1.1 | +0.308% | +2.307% | +1.998% | 30 | 5.46% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap085_p1.25 | +0.304% | +2.302% | +1.998% | 30 | 5.49% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap085_p1.4 | +0.301% | +2.299% | +1.998% | 30 | 5.51% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap100_p1 | +0.313% | +2.311% | +1.998% | 30 | 5.43% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap100_p1.1 | +0.308% | +2.307% | +1.998% | 30 | 5.46% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap100_p1.25 | +0.304% | +2.302% | +1.998% | 30 | 5.49% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k30_cap100_p1.4 | +0.301% | +2.299% | +1.998% | 30 | 5.51% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap075_p1 | +0.351% | +2.349% | +1.998% | 35 | 5.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap075_p1.1 | +0.334% | +2.333% | +1.998% | 35 | 5.36% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap075_p1.25 | +0.317% | +2.315% | +1.998% | 35 | 5.42% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap075_p1.4 | +0.305% | +2.304% | +1.998% | 35 | 5.46% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap085_p1 | +0.351% | +2.349% | +1.998% | 35 | 5.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap085_p1.1 | +0.334% | +2.333% | +1.998% | 35 | 5.36% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap085_p1.25 | +0.317% | +2.315% | +1.998% | 35 | 5.42% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap085_p1.4 | +0.305% | +2.304% | +1.998% | 35 | 5.46% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap100_p1 | +0.351% | +2.349% | +1.998% | 35 | 5.30% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap100_p1.1 | +0.334% | +2.333% | +1.998% | 35 | 5.36% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap100_p1.25 | +0.317% | +2.315% | +1.998% | 35 | 5.42% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k35_cap100_p1.4 | +0.305% | +2.304% | +1.998% | 35 | 5.46% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap075_p1 | +0.323% | +2.321% | +1.998% | 40 | 5.16% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap075_p1.1 | +0.311% | +2.309% | +1.998% | 40 | 5.25% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap075_p1.25 | +0.299% | +2.297% | +1.998% | 40 | 5.34% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap075_p1.4 | +0.291% | +2.289% | +1.998% | 40 | 5.40% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap085_p1 | +0.323% | +2.321% | +1.998% | 40 | 5.16% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap085_p1.1 | +0.311% | +2.309% | +1.998% | 40 | 5.25% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap085_p1.25 | +0.299% | +2.297% | +1.998% | 40 | 5.34% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap085_p1.4 | +0.291% | +2.289% | +1.998% | 40 | 5.40% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap100_p1 | +0.323% | +2.321% | +1.998% | 40 | 5.16% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap100_p1.1 | +0.311% | +2.309% | +1.998% | 40 | 5.25% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap100_p1.25 | +0.299% | +2.297% | +1.998% | 40 | 5.34% | 0.0773 | -0.0726 |
| 2026-01-15 | primary_voladj_v1_k40_cap100_p1.4 | +0.291% | +2.289% | +1.998% | 40 | 5.40% | 0.0773 | -0.0726 |
| 2026-01-15 | robust_only_k30_cap100_p1 | -3.927% | -1.929% | +1.998% | 30 | 4.29% | 0.0773 | -0.0726 |
| 2026-01-23 | blend_primary50_robust50 | -3.290% | -5.847% | -2.557% | 57 | 5.00% | -0.2585 | -0.2114 |
| 2026-01-23 | blend_primary70_robust30 | -3.991% | -6.548% | -2.557% | 57 | 5.43% | -0.2585 | -0.2114 |
| 2026-01-23 | blend_primary80_robust20 | -4.342% | -6.899% | -2.557% | 57 | 5.79% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap060_p0.75 | -4.969% | -7.526% | -2.557% | 30 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap060_p1 | -5.249% | -7.806% | -2.557% | 30 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap060_p1.1 | -5.344% | -7.900% | -2.557% | 30 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap060_p1.25 | -5.441% | -7.998% | -2.557% | 30 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap060_p1.4 | -5.441% | -7.998% | -2.557% | 30 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap075_p0.75 | -4.941% | -7.498% | -2.557% | 30 | 6.12% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap075_p1 | -5.043% | -7.600% | -2.557% | 30 | 6.53% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap075_p1.1 | -5.057% | -7.614% | -2.557% | 30 | 6.64% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap075_p1.25 | -5.059% | -7.616% | -2.557% | 30 | 6.78% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap075_p1.4 | -5.048% | -7.605% | -2.557% | 30 | 6.89% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap085_p0.75 | -4.941% | -7.498% | -2.557% | 30 | 6.12% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap085_p1 | -5.043% | -7.600% | -2.557% | 30 | 6.53% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap085_p1.1 | -5.057% | -7.614% | -2.557% | 30 | 6.64% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap085_p1.25 | -5.059% | -7.616% | -2.557% | 30 | 6.78% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap085_p1.4 | -5.048% | -7.605% | -2.557% | 30 | 6.89% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap100_p0.75 | -4.941% | -7.498% | -2.557% | 30 | 6.12% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap100_p1 | -5.043% | -7.600% | -2.557% | 30 | 6.53% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap100_p1.1 | -5.057% | -7.614% | -2.557% | 30 | 6.64% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap100_p1.25 | -5.059% | -7.616% | -2.557% | 30 | 6.78% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k30_cap100_p1.4 | -5.048% | -7.605% | -2.557% | 30 | 6.89% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap060_p0.75 | -4.947% | -7.504% | -2.557% | 35 | 5.95% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap060_p1 | -5.202% | -7.759% | -2.557% | 35 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap060_p1.1 | -5.298% | -7.854% | -2.557% | 35 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap060_p1.25 | -5.422% | -7.979% | -2.557% | 35 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap060_p1.4 | -5.484% | -8.041% | -2.557% | 35 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap075_p0.75 | -4.947% | -7.504% | -2.557% | 35 | 5.95% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap075_p1 | -5.045% | -7.602% | -2.557% | 35 | 6.44% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap075_p1.1 | -5.058% | -7.615% | -2.557% | 35 | 6.57% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap075_p1.25 | -5.060% | -7.617% | -2.557% | 35 | 6.74% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap075_p1.4 | -5.048% | -7.605% | -2.557% | 35 | 6.86% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap085_p0.75 | -4.947% | -7.504% | -2.557% | 35 | 5.95% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap085_p1 | -5.045% | -7.602% | -2.557% | 35 | 6.44% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap085_p1.1 | -5.058% | -7.615% | -2.557% | 35 | 6.57% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap085_p1.25 | -5.060% | -7.617% | -2.557% | 35 | 6.74% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap085_p1.4 | -5.048% | -7.605% | -2.557% | 35 | 6.86% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap100_p0.75 | -4.947% | -7.504% | -2.557% | 35 | 5.95% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap100_p1 | -5.045% | -7.602% | -2.557% | 35 | 6.44% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap100_p1.1 | -5.058% | -7.615% | -2.557% | 35 | 6.57% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap100_p1.25 | -5.060% | -7.617% | -2.557% | 35 | 6.74% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k35_cap100_p1.4 | -5.048% | -7.605% | -2.557% | 35 | 6.86% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap060_p0.75 | -4.874% | -7.431% | -2.557% | 40 | 5.79% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap060_p1 | -5.117% | -7.674% | -2.557% | 40 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap060_p1.1 | -5.219% | -7.776% | -2.557% | 40 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap060_p1.25 | -5.357% | -7.914% | -2.557% | 40 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap060_p1.4 | -5.471% | -8.028% | -2.557% | 40 | 6.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap075_p0.75 | -4.874% | -7.431% | -2.557% | 40 | 5.79% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap075_p1 | -5.007% | -7.564% | -2.557% | 40 | 6.35% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap075_p1.1 | -5.030% | -7.587% | -2.557% | 40 | 6.51% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap075_p1.25 | -5.042% | -7.599% | -2.557% | 40 | 6.69% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap075_p1.4 | -5.037% | -7.594% | -2.557% | 40 | 6.83% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap085_p0.75 | -4.874% | -7.431% | -2.557% | 40 | 5.79% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap085_p1 | -5.007% | -7.564% | -2.557% | 40 | 6.35% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap085_p1.1 | -5.030% | -7.587% | -2.557% | 40 | 6.51% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap085_p1.25 | -5.042% | -7.599% | -2.557% | 40 | 6.69% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap085_p1.4 | -5.037% | -7.594% | -2.557% | 40 | 6.83% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap100_p0.75 | -4.874% | -7.431% | -2.557% | 40 | 5.79% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap100_p1 | -5.007% | -7.564% | -2.557% | 40 | 6.35% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap100_p1.1 | -5.030% | -7.587% | -2.557% | 40 | 6.51% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap100_p1.25 | -5.042% | -7.599% | -2.557% | 40 | 6.69% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_k40_cap100_p1.4 | -5.037% | -7.594% | -2.557% | 40 | 6.83% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap075_p1 | -4.286% | -6.843% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap075_p1.1 | -4.373% | -6.930% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap075_p1.25 | -4.468% | -7.025% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap075_p1.4 | -4.549% | -7.105% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap085_p1 | -4.089% | -6.646% | -2.557% | 30 | 8.37% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap085_p1.1 | -4.105% | -6.661% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap085_p1.25 | -4.136% | -6.693% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap085_p1.4 | -4.147% | -6.704% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap100_p1 | -4.089% | -6.646% | -2.557% | 30 | 8.37% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap100_p1.1 | -4.099% | -6.656% | -2.557% | 30 | 8.53% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap100_p1.25 | -4.097% | -6.654% | -2.557% | 30 | 8.71% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k30_cap100_p1.4 | -4.083% | -6.640% | -2.557% | 30 | 8.85% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap075_p1 | -4.275% | -6.832% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap075_p1.1 | -4.354% | -6.911% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap075_p1.25 | -4.459% | -7.016% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap075_p1.4 | -4.530% | -7.087% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap085_p1 | -4.162% | -6.719% | -2.557% | 35 | 8.10% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap085_p1.1 | -4.168% | -6.725% | -2.557% | 35 | 8.28% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap085_p1.25 | -4.163% | -6.720% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap085_p1.4 | -4.175% | -6.732% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap100_p1 | -4.162% | -6.719% | -2.557% | 35 | 8.10% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap100_p1.1 | -4.168% | -6.725% | -2.557% | 35 | 8.28% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap100_p1.25 | -4.163% | -6.720% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k35_cap100_p1.4 | -4.147% | -6.704% | -2.557% | 35 | 8.65% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap075_p1 | -4.247% | -6.804% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap075_p1.1 | -4.310% | -6.867% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap075_p1.25 | -4.426% | -6.983% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap075_p1.4 | -4.513% | -7.070% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap085_p1 | -4.145% | -6.702% | -2.557% | 40 | 8.06% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap085_p1.1 | -4.160% | -6.717% | -2.557% | 40 | 8.28% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap085_p1.25 | -4.169% | -6.726% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap085_p1.4 | -4.192% | -6.749% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap100_p1 | -4.145% | -6.702% | -2.557% | 40 | 8.06% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap100_p1.1 | -4.160% | -6.717% | -2.557% | 40 | 8.28% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap100_p1.25 | -4.164% | -6.721% | -2.557% | 40 | 8.53% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.5_k40_cap100_p1.4 | -4.154% | -6.711% | -2.557% | 40 | 8.71% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap075_p1 | -4.164% | -6.721% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap075_p1.1 | -4.288% | -6.845% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap075_p1.25 | -4.439% | -6.996% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap075_p1.4 | -4.548% | -7.105% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap085_p1 | -3.761% | -6.318% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap085_p1.1 | -3.800% | -6.357% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap085_p1.25 | -3.849% | -6.406% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap085_p1.4 | -3.895% | -6.452% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap100_p1 | -3.601% | -6.158% | -2.557% | 30 | 9.40% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap100_p1.1 | -3.608% | -6.165% | -2.557% | 30 | 9.58% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap100_p1.25 | -3.604% | -6.161% | -2.557% | 30 | 9.79% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k30_cap100_p1.4 | -3.588% | -6.145% | -2.557% | 30 | 9.94% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap075_p1 | -4.140% | -6.697% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap075_p1.1 | -4.250% | -6.807% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap075_p1.25 | -4.408% | -6.965% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap075_p1.4 | -4.526% | -7.083% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap085_p1 | -3.801% | -6.358% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap085_p1.1 | -3.841% | -6.398% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap085_p1.25 | -3.875% | -6.432% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap085_p1.4 | -3.909% | -6.466% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap100_p1 | -3.709% | -6.266% | -2.557% | 35 | 9.02% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap100_p1.1 | -3.711% | -6.268% | -2.557% | 35 | 9.23% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap100_p1.25 | -3.702% | -6.259% | -2.557% | 35 | 9.47% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k35_cap100_p1.4 | -3.683% | -6.240% | -2.557% | 35 | 9.65% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap075_p1 | -4.054% | -6.611% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap075_p1.1 | -4.190% | -6.747% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap075_p1.25 | -4.345% | -6.902% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap075_p1.4 | -4.484% | -7.041% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap085_p1 | -3.790% | -6.347% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap085_p1.1 | -3.845% | -6.402% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap085_p1.25 | -3.896% | -6.453% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap085_p1.4 | -3.926% | -6.482% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap100_p1 | -3.698% | -6.255% | -2.557% | 40 | 9.01% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap100_p1.1 | -3.708% | -6.265% | -2.557% | 40 | 9.27% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap100_p1.25 | -3.707% | -6.264% | -2.557% | 40 | 9.55% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v0.75_k40_cap100_p1.4 | -3.694% | -6.251% | -2.557% | 40 | 9.76% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap075_p1 | -4.088% | -6.645% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap075_p1.1 | -4.242% | -6.799% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap075_p1.25 | -4.422% | -6.978% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap075_p1.4 | -4.521% | -7.078% | -2.557% | 30 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap085_p1 | -3.523% | -6.080% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap085_p1.1 | -3.616% | -6.173% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap085_p1.25 | -3.727% | -6.284% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap085_p1.4 | -3.797% | -6.354% | -2.557% | 30 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap100_p1 | -3.195% | -5.752% | -2.557% | 30 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap100_p1.1 | -3.235% | -5.792% | -2.557% | 30 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap100_p1.25 | -3.269% | -5.826% | -2.557% | 30 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k30_cap100_p1.4 | -3.282% | -5.839% | -2.557% | 30 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap075_p1 | -4.033% | -6.590% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap075_p1.1 | -4.196% | -6.753% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap075_p1.25 | -4.387% | -6.944% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap075_p1.4 | -4.526% | -7.083% | -2.557% | 35 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap085_p1 | -3.532% | -6.089% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap085_p1.1 | -3.622% | -6.178% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap085_p1.25 | -3.731% | -6.288% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap085_p1.4 | -3.809% | -6.366% | -2.557% | 35 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap100_p1 | -3.253% | -5.810% | -2.557% | 35 | 9.98% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap100_p1.1 | -3.289% | -5.846% | -2.557% | 35 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap100_p1.25 | -3.323% | -5.880% | -2.557% | 35 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k35_cap100_p1.4 | -3.336% | -5.893% | -2.557% | 35 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap075_p1 | -3.933% | -6.490% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap075_p1.1 | -4.087% | -6.644% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap075_p1.25 | -4.310% | -6.867% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap075_p1.4 | -4.474% | -7.031% | -2.557% | 40 | 7.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap085_p1 | -3.512% | -6.069% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap085_p1.1 | -3.586% | -6.143% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap085_p1.25 | -3.708% | -6.265% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap085_p1.4 | -3.802% | -6.359% | -2.557% | 40 | 8.50% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap100_p1 | -3.250% | -5.807% | -2.557% | 40 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap100_p1.1 | -3.305% | -5.862% | -2.557% | 40 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap100_p1.25 | -3.356% | -5.913% | -2.557% | 40 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | primary_voladj_v1_k40_cap100_p1.4 | -3.381% | -5.937% | -2.557% | 40 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-23 | robust_only_k30_cap100_p1 | -1.536% | -4.093% | -2.557% | 30 | 10.00% | -0.2585 | -0.2114 |
| 2026-01-26 | blend_primary50_robust50 | -0.165% | -5.686% | -5.521% | 58 | 5.00% | -0.1969 | -0.1973 |
| 2026-01-26 | blend_primary70_robust30 | -0.068% | -5.589% | -5.521% | 58 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | blend_primary80_robust20 | -0.019% | -5.540% | -5.521% | 58 | 3.19% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap060_p0.75 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap060_p1 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap060_p1.1 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap060_p1.25 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap060_p1.4 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap075_p0.75 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap075_p1 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap075_p1.1 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap075_p1.25 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap075_p1.4 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap085_p0.75 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap085_p1 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap085_p1.1 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap085_p1.25 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap085_p1.4 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap100_p0.75 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap100_p1 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap100_p1.1 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap100_p1.25 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k30_cap100_p1.4 | +0.078% | -5.442% | -5.521% | 30 | 3.33% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap060_p0.75 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap060_p1 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap060_p1.1 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap060_p1.25 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap060_p1.4 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap075_p0.75 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap075_p1 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap075_p1.1 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap075_p1.25 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap075_p1.4 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap085_p0.75 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap085_p1 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap085_p1.1 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap085_p1.25 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap085_p1.4 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap100_p0.75 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap100_p1 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap100_p1.1 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap100_p1.25 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k35_cap100_p1.4 | +0.738% | -4.783% | -5.521% | 35 | 2.86% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap060_p0.75 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap060_p1 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap060_p1.1 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap060_p1.25 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap060_p1.4 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap075_p0.75 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap075_p1 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap075_p1.1 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap075_p1.25 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap075_p1.4 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap085_p0.75 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap085_p1 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap085_p1.1 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap085_p1.25 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap085_p1.4 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap100_p0.75 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap100_p1 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap100_p1.1 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap100_p1.25 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_k40_cap100_p1.4 | +0.284% | -5.237% | -5.521% | 40 | 2.50% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap075_p1 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap075_p1.1 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap075_p1.25 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap075_p1.4 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap085_p1 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap085_p1.1 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap085_p1.25 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap085_p1.4 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap100_p1 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap100_p1.1 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap100_p1.25 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k30_cap100_p1.4 | +0.132% | -5.389% | -5.521% | 30 | 3.74% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap075_p1 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap075_p1.1 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap075_p1.25 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap075_p1.4 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap085_p1 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap085_p1.1 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap085_p1.25 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap085_p1.4 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap100_p1 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap100_p1.1 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap100_p1.25 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k35_cap100_p1.4 | +0.871% | -4.650% | -5.521% | 35 | 3.23% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap075_p1 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap075_p1.1 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap075_p1.25 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap075_p1.4 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap085_p1 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap085_p1.1 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap085_p1.25 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap085_p1.4 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap100_p1 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap100_p1.1 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap100_p1.25 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.5_k40_cap100_p1.4 | +0.388% | -5.133% | -5.521% | 40 | 2.80% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap075_p1 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap075_p1.1 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap075_p1.25 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap075_p1.4 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap085_p1 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap085_p1.1 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap085_p1.25 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap085_p1.4 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap100_p1 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap100_p1.1 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap100_p1.25 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k30_cap100_p1.4 | +0.157% | -5.364% | -5.521% | 30 | 3.94% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap075_p1 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap075_p1.1 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap075_p1.25 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap075_p1.4 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap085_p1 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap085_p1.1 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap085_p1.25 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap085_p1.4 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap100_p1 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap100_p1.1 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap100_p1.25 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k35_cap100_p1.4 | +0.933% | -4.588% | -5.521% | 35 | 3.42% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap075_p1 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap075_p1.1 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap075_p1.25 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap075_p1.4 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap085_p1 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap085_p1.1 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap085_p1.25 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap085_p1.4 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap100_p1 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap100_p1.1 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap100_p1.25 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v0.75_k40_cap100_p1.4 | +0.438% | -5.083% | -5.521% | 40 | 2.95% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap075_p1 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap075_p1.1 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap075_p1.25 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap075_p1.4 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap085_p1 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap085_p1.1 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap085_p1.25 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap085_p1.4 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap100_p1 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap100_p1.1 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap100_p1.25 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k30_cap100_p1.4 | +0.180% | -5.341% | -5.521% | 30 | 4.14% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap075_p1 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap075_p1.1 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap075_p1.25 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap075_p1.4 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap085_p1 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap085_p1.1 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap085_p1.25 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap085_p1.4 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap100_p1 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap100_p1.1 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap100_p1.25 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k35_cap100_p1.4 | +0.992% | -4.529% | -5.521% | 35 | 3.60% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap075_p1 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap075_p1.1 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap075_p1.25 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap075_p1.4 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap085_p1 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap085_p1.1 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap085_p1.25 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap085_p1.4 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap100_p1 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap100_p1.1 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap100_p1.25 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | primary_voladj_v1_k40_cap100_p1.4 | +0.485% | -5.035% | -5.521% | 40 | 3.11% | -0.1969 | -0.1973 |
| 2026-01-26 | robust_only_k30_cap100_p1 | -0.408% | -5.929% | -5.521% | 30 | 10.00% | -0.1969 | -0.1973 |
| 2026-04-21 | blend_primary50_robust50 | +4.134% | +3.331% | -0.802% | 44 | 8.28% | 0.0322 | 0.1281 |
| 2026-04-21 | blend_primary70_robust30 | +4.732% | +3.929% | -0.802% | 44 | 8.97% | 0.0322 | 0.1281 |
| 2026-04-21 | blend_primary80_robust20 | +5.031% | +4.229% | -0.802% | 44 | 9.31% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap060_p0.75 | +4.475% | +3.673% | -0.802% | 30 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap060_p1 | +4.443% | +3.640% | -0.802% | 30 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap060_p1.1 | +4.441% | +3.639% | -0.802% | 30 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap060_p1.25 | +4.448% | +3.646% | -0.802% | 30 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap060_p1.4 | +4.464% | +3.662% | -0.802% | 30 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap075_p0.75 | +4.913% | +4.110% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap075_p1 | +5.212% | +4.409% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap075_p1.1 | +5.256% | +4.453% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap075_p1.25 | +5.326% | +4.523% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap075_p1.4 | +5.399% | +4.596% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap085_p0.75 | +5.013% | +4.210% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap085_p1 | +5.487% | +4.684% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap085_p1.1 | +5.679% | +4.876% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap085_p1.25 | +5.747% | +4.945% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap085_p1.4 | +5.817% | +5.015% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap100_p0.75 | +5.163% | +4.361% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap100_p1 | +5.629% | +4.827% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap100_p1.1 | +5.818% | +5.016% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap100_p1.25 | +6.101% | +5.298% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k30_cap100_p1.4 | +6.380% | +5.577% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap060_p0.75 | +4.488% | +3.685% | -0.802% | 35 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap060_p1 | +4.502% | +3.700% | -0.802% | 35 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap060_p1.1 | +4.477% | +3.675% | -0.802% | 35 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap060_p1.25 | +4.478% | +3.675% | -0.802% | 35 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap060_p1.4 | +4.488% | +3.686% | -0.802% | 35 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap075_p0.75 | +4.825% | +4.023% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap075_p1 | +5.218% | +4.416% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap075_p1.1 | +5.261% | +4.458% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap075_p1.25 | +5.330% | +4.528% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap075_p1.4 | +5.403% | +4.600% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap085_p0.75 | +4.926% | +4.124% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap085_p1 | +5.424% | +4.621% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap085_p1.1 | +5.626% | +4.823% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap085_p1.25 | +5.751% | +4.949% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap085_p1.4 | +5.821% | +5.019% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap100_p0.75 | +5.078% | +4.276% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap100_p1 | +5.567% | +4.765% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap100_p1.1 | +5.766% | +4.964% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap100_p1.25 | +6.063% | +5.260% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k35_cap100_p1.4 | +6.355% | +5.552% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap060_p0.75 | +4.465% | +3.662% | -0.802% | 40 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap060_p1 | +4.530% | +3.727% | -0.802% | 40 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap060_p1.1 | +4.490% | +3.687% | -0.802% | 40 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap060_p1.25 | +4.485% | +3.683% | -0.802% | 40 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap060_p1.4 | +4.494% | +3.692% | -0.802% | 40 | 6.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap075_p0.75 | +4.718% | +3.915% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap075_p1 | +5.202% | +4.399% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap075_p1.1 | +5.247% | +4.444% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap075_p1.25 | +5.319% | +4.517% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap075_p1.4 | +5.396% | +4.593% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap085_p0.75 | +4.820% | +4.018% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap085_p1 | +5.348% | +4.546% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap085_p1.1 | +5.562% | +4.760% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap085_p1.25 | +5.741% | +4.938% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap085_p1.4 | +5.814% | +5.011% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap100_p0.75 | +4.974% | +4.171% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap100_p1 | +5.493% | +4.691% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap100_p1.1 | +5.704% | +4.901% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap100_p1.25 | +6.017% | +5.214% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_k40_cap100_p1.4 | +6.323% | +5.521% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap075_p1 | +5.035% | +4.233% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap075_p1.1 | +5.062% | +4.260% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap075_p1.25 | +5.135% | +4.333% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap075_p1.4 | +5.241% | +4.438% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap085_p1 | +5.190% | +4.388% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap085_p1.1 | +5.364% | +4.561% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap085_p1.25 | +5.539% | +4.737% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap085_p1.4 | +5.589% | +4.787% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap100_p1 | +5.338% | +4.535% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap100_p1.1 | +5.508% | +4.706% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap100_p1.25 | +5.767% | +4.964% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k30_cap100_p1.4 | +6.025% | +5.223% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap075_p1 | +5.041% | +4.238% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap075_p1.1 | +5.081% | +4.279% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap075_p1.25 | +5.129% | +4.326% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap075_p1.4 | +5.239% | +4.436% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap085_p1 | +5.146% | +4.344% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap085_p1.1 | +5.330% | +4.527% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap085_p1.25 | +5.557% | +4.754% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap085_p1.4 | +5.607% | +4.805% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap100_p1 | +5.294% | +4.492% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap100_p1.1 | +5.475% | +4.672% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap100_p1.25 | +5.747% | +4.945% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k35_cap100_p1.4 | +6.019% | +5.216% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap075_p1 | +4.971% | +4.168% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap075_p1.1 | +5.067% | +4.264% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap075_p1.25 | +5.117% | +4.315% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap075_p1.4 | +5.219% | +4.417% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap085_p1 | +5.073% | +4.271% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap085_p1.1 | +5.268% | +4.466% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap085_p1.25 | +5.546% | +4.744% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap085_p1.4 | +5.600% | +4.798% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap100_p1 | +5.222% | +4.420% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap100_p1.1 | +5.414% | +4.612% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap100_p1.25 | +5.703% | +4.900% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.5_k40_cap100_p1.4 | +5.988% | +5.186% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap075_p1 | +4.927% | +4.125% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap075_p1.1 | +4.972% | +4.170% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap075_p1.25 | +5.066% | +4.263% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap075_p1.4 | +5.164% | +4.361% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap085_p1 | +5.038% | +4.235% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap085_p1.1 | +5.202% | +4.399% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap085_p1.25 | +5.435% | +4.632% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap085_p1.4 | +5.475% | +4.673% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap100_p1 | +5.188% | +4.385% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap100_p1.1 | +5.349% | +4.546% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap100_p1.25 | +5.595% | +4.792% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k30_cap100_p1.4 | +5.842% | +5.040% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap075_p1 | +4.898% | +4.095% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap075_p1.1 | +4.991% | +4.189% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap075_p1.25 | +5.063% | +4.261% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap075_p1.4 | +5.166% | +4.364% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap085_p1 | +5.004% | +4.202% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap085_p1.1 | +5.178% | +4.375% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap085_p1.25 | +5.433% | +4.630% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap085_p1.4 | +5.501% | +4.698% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap100_p1 | +5.154% | +4.352% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap100_p1.1 | +5.325% | +4.523% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap100_p1.25 | +5.585% | +4.783% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k35_cap100_p1.4 | +5.846% | +5.043% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap075_p1 | +4.829% | +4.027% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap075_p1.1 | +4.977% | +4.174% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap075_p1.25 | +5.036% | +4.234% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap075_p1.4 | +5.146% | +4.344% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap085_p1 | +4.932% | +4.130% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap085_p1.1 | +5.117% | +4.315% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap085_p1.25 | +5.390% | +4.588% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap085_p1.4 | +5.493% | +4.691% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap100_p1 | +5.084% | +4.281% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap100_p1.1 | +5.266% | +4.464% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap100_p1.25 | +5.542% | +4.739% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v0.75_k40_cap100_p1.4 | +5.816% | +5.013% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap075_p1 | +4.777% | +3.975% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap075_p1.1 | +4.911% | +4.109% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap075_p1.25 | +4.996% | +4.194% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap075_p1.4 | +5.086% | +4.284% | -0.802% | 30 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap085_p1 | +4.883% | +4.081% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap085_p1.1 | +5.037% | +4.235% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap085_p1.25 | +5.263% | +4.460% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap085_p1.4 | +5.368% | +4.565% | -0.802% | 30 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap100_p1 | +5.036% | +4.234% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap100_p1.1 | +5.187% | +4.385% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap100_p1.25 | +5.420% | +4.618% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k30_cap100_p1.4 | +5.656% | +4.854% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap075_p1 | +4.753% | +3.951% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap075_p1.1 | +4.907% | +4.104% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap075_p1.25 | +4.997% | +4.195% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap075_p1.4 | +5.093% | +4.290% | -0.802% | 35 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap085_p1 | +4.860% | +4.058% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap085_p1.1 | +5.024% | +4.222% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap085_p1.25 | +5.266% | +4.464% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap085_p1.4 | +5.394% | +4.592% | -0.802% | 35 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap100_p1 | +5.013% | +4.211% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap100_p1.1 | +5.174% | +4.372% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap100_p1.25 | +5.421% | +4.619% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k35_cap100_p1.4 | +5.671% | +4.868% | -0.802% | 35 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap075_p1 | +4.686% | +3.884% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap075_p1.1 | +4.850% | +4.048% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap075_p1.25 | +4.970% | +4.167% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap075_p1.4 | +5.072% | +4.270% | -0.802% | 40 | 7.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap085_p1 | +4.790% | +3.987% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap085_p1.1 | +4.965% | +4.163% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap085_p1.25 | +5.225% | +4.422% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap085_p1.4 | +5.387% | +4.584% | -0.802% | 40 | 8.50% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap100_p1 | +4.944% | +4.141% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap100_p1.1 | +5.116% | +4.314% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap100_p1.25 | +5.379% | +4.576% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | primary_voladj_v1_k40_cap100_p1.4 | +5.641% | +4.839% | -0.802% | 40 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-21 | robust_only_k30_cap100_p1 | +2.638% | +1.836% | -0.802% | 30 | 10.00% | 0.0322 | 0.1281 |
| 2026-04-22 | blend_primary50_robust50 | +3.126% | +2.723% | -0.403% | 37 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | blend_primary70_robust30 | +3.115% | +2.712% | -0.403% | 37 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | blend_primary80_robust20 | +3.110% | +2.707% | -0.403% | 37 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap060_p0.75 | +1.730% | +1.327% | -0.403% | 30 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap060_p1 | +1.850% | +1.447% | -0.403% | 30 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap060_p1.1 | +1.931% | +1.528% | -0.403% | 30 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap060_p1.25 | +2.071% | +1.668% | -0.403% | 30 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap060_p1.4 | +2.206% | +1.803% | -0.403% | 30 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap075_p0.75 | +2.311% | +1.907% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap075_p1 | +2.418% | +2.015% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap075_p1.1 | +2.450% | +2.047% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap075_p1.25 | +2.486% | +2.083% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap075_p1.4 | +2.509% | +2.106% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap085_p0.75 | +2.451% | +2.048% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap085_p1 | +2.797% | +2.394% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap085_p1.1 | +2.825% | +2.422% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap085_p1.25 | +2.858% | +2.454% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap085_p1.4 | +2.878% | +2.475% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap100_p0.75 | +2.604% | +2.201% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap100_p1 | +3.099% | +2.696% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap100_p1.1 | +3.289% | +2.886% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap100_p1.25 | +3.415% | +3.012% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k30_cap100_p1.4 | +3.432% | +3.029% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap060_p0.75 | +1.619% | +1.216% | -0.403% | 35 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap060_p1 | +1.709% | +1.306% | -0.403% | 35 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap060_p1.1 | +1.740% | +1.337% | -0.403% | 35 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap060_p1.25 | +1.781% | +1.378% | -0.403% | 35 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap060_p1.4 | +1.816% | +1.413% | -0.403% | 35 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap075_p0.75 | +1.939% | +1.536% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap075_p1 | +2.297% | +1.894% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap075_p1.1 | +2.324% | +1.921% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap075_p1.25 | +2.359% | +1.956% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap075_p1.4 | +2.388% | +1.985% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap085_p0.75 | +2.056% | +1.653% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap085_p1 | +2.499% | +2.096% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap085_p1.1 | +2.676% | +2.273% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap085_p1.25 | +2.745% | +2.342% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap085_p1.4 | +2.771% | +2.368% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap100_p0.75 | +2.202% | +1.799% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap100_p1 | +2.673% | +2.270% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap100_p1.1 | +2.834% | +2.431% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap100_p1.25 | +3.081% | +2.678% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k35_cap100_p1.4 | +3.312% | +2.909% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap060_p0.75 | +1.734% | +1.331% | -0.403% | 40 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap060_p1 | +1.819% | +1.416% | -0.403% | 40 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap060_p1.1 | +1.823% | +1.420% | -0.403% | 40 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap060_p1.25 | +1.830% | +1.427% | -0.403% | 40 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap060_p1.4 | +1.838% | +1.435% | -0.403% | 40 | 6.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap075_p0.75 | +1.926% | +1.523% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap075_p1 | +2.248% | +1.845% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap075_p1.1 | +2.374% | +1.971% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap075_p1.25 | +2.401% | +1.998% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap075_p1.4 | +2.408% | +2.005% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap085_p0.75 | +2.029% | +1.626% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap085_p1 | +2.372% | +1.969% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap085_p1.1 | +2.501% | +2.098% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap085_p1.25 | +2.709% | +2.306% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap085_p1.4 | +2.788% | +2.385% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap100_p0.75 | +1.858% | +1.455% | -0.403% | 40 | 9.99% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap100_p1 | +2.520% | +2.117% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap100_p1.1 | +2.666% | +2.263% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap100_p1.25 | +2.864% | +2.461% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_k40_cap100_p1.4 | +3.067% | +2.664% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap075_p1 | +2.501% | +2.098% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap075_p1.1 | +2.536% | +2.133% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap075_p1.25 | +2.578% | +2.175% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap075_p1.4 | +2.608% | +2.205% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap085_p1 | +2.871% | +2.468% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap085_p1.1 | +2.902% | +2.499% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap085_p1.25 | +2.940% | +2.537% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap085_p1.4 | +2.966% | +2.563% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap100_p1 | +3.156% | +2.753% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap100_p1.1 | +3.348% | +2.945% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap100_p1.25 | +3.482% | +3.079% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k30_cap100_p1.4 | +3.503% | +3.100% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap075_p1 | +2.364% | +1.961% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap075_p1.1 | +2.394% | +1.991% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap075_p1.25 | +2.433% | +2.030% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap075_p1.4 | +2.466% | +2.063% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap085_p1 | +2.544% | +2.141% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap085_p1.1 | +2.721% | +2.318% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap085_p1.25 | +2.810% | +2.407% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap085_p1.4 | +2.840% | +2.437% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap100_p1 | +2.713% | +2.310% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap100_p1.1 | +2.875% | +2.472% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap100_p1.25 | +3.124% | +2.721% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k35_cap100_p1.4 | +3.361% | +2.958% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap075_p1 | +2.299% | +1.896% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap075_p1.1 | +2.434% | +2.031% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap075_p1.25 | +2.474% | +2.071% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap075_p1.4 | +2.483% | +2.080% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap085_p1 | +2.419% | +2.016% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap085_p1.1 | +2.547% | +2.144% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap085_p1.25 | +2.755% | +2.352% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap085_p1.4 | +2.855% | +2.452% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap100_p1 | +2.568% | +2.165% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap100_p1.1 | +2.713% | +2.310% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap100_p1.25 | +2.905% | +2.502% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.5_k40_cap100_p1.4 | +3.108% | +2.705% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap075_p1 | +2.539% | +2.136% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap075_p1.1 | +2.576% | +2.172% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap075_p1.25 | +2.620% | +2.217% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap075_p1.4 | +2.653% | +2.250% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap085_p1 | +2.905% | +2.502% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap085_p1.1 | +2.937% | +2.534% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap085_p1.25 | +2.977% | +2.574% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap085_p1.4 | +3.006% | +2.603% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap100_p1 | +3.179% | +2.776% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap100_p1.1 | +3.372% | +2.969% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap100_p1.25 | +3.513% | +3.110% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k30_cap100_p1.4 | +3.536% | +3.133% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap075_p1 | +2.394% | +1.991% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap075_p1.1 | +2.425% | +2.022% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap075_p1.25 | +2.466% | +2.063% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap075_p1.4 | +2.501% | +2.098% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap085_p1 | +2.560% | +2.157% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap085_p1.1 | +2.738% | +2.335% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap085_p1.25 | +2.840% | +2.437% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap085_p1.4 | +2.871% | +2.468% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap100_p1 | +2.728% | +2.325% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap100_p1.1 | +2.890% | +2.487% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap100_p1.25 | +3.140% | +2.737% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k35_cap100_p1.4 | +3.381% | +2.978% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap075_p1 | +2.318% | +1.915% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap075_p1.1 | +2.454% | +2.050% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap075_p1.25 | +2.507% | +2.104% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap075_p1.4 | +2.517% | +2.114% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap085_p1 | +2.438% | +2.035% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap085_p1.1 | +2.565% | +2.162% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap085_p1.25 | +2.772% | +2.369% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap085_p1.4 | +2.885% | +2.482% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap100_p1 | +2.587% | +2.184% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap100_p1.1 | +2.731% | +2.328% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap100_p1.25 | +2.921% | +2.518% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v0.75_k40_cap100_p1.4 | +3.123% | +2.720% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap075_p1 | +2.573% | +2.170% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap075_p1.1 | +2.612% | +2.209% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap075_p1.25 | +2.660% | +2.257% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap075_p1.4 | +2.696% | +2.293% | -0.403% | 30 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap085_p1 | +2.936% | +2.532% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap085_p1.1 | +2.970% | +2.567% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap085_p1.25 | +3.013% | +2.610% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap085_p1.4 | +3.044% | +2.641% | -0.403% | 30 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap100_p1 | +3.197% | +2.794% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap100_p1.1 | +3.392% | +2.989% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap100_p1.25 | +3.541% | +3.138% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k30_cap100_p1.4 | +3.567% | +3.164% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap075_p1 | +2.421% | +2.018% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap075_p1.1 | +2.453% | +2.050% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap075_p1.25 | +2.496% | +2.093% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap075_p1.4 | +2.534% | +2.130% | -0.403% | 35 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap085_p1 | +2.572% | +2.169% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap085_p1.1 | +2.751% | +2.348% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap085_p1.25 | +2.867% | +2.464% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap085_p1.4 | +2.900% | +2.497% | -0.403% | 35 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap100_p1 | +2.739% | +2.336% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap100_p1.1 | +2.902% | +2.499% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap100_p1.25 | +3.153% | +2.750% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k35_cap100_p1.4 | +3.399% | +2.996% | -0.403% | 35 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap075_p1 | +2.334% | +1.931% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap075_p1.1 | +2.469% | +2.066% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap075_p1.25 | +2.538% | +2.135% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap075_p1.4 | +2.548% | +2.145% | -0.403% | 40 | 7.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap085_p1 | +2.453% | +2.050% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap085_p1.1 | +2.580% | +2.177% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap085_p1.25 | +2.785% | +2.382% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap085_p1.4 | +2.913% | +2.510% | -0.403% | 40 | 8.50% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap100_p1 | +2.603% | +2.200% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap100_p1.1 | +2.746% | +2.343% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap100_p1.25 | +2.933% | +2.530% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | primary_voladj_v1_k40_cap100_p1.4 | +3.135% | +2.732% | -0.403% | 40 | 10.00% | 0.0330 | 0.0096 |
| 2026-04-22 | robust_only_k30_cap100_p1 | +3.152% | +2.749% | -0.403% | 30 | 10.00% | 0.0330 | 0.0096 |