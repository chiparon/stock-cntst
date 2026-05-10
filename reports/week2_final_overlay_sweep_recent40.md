# Portfolio Overlay Sweep

- Generated at: 2026-05-10 19:34:17
- As-of date: 2026-05-08
- Feature groups: momentum_shape
- Primary spec: current_d4_mcw10_l5_lr005
- Robust spec: d4_mcw20_l10_lr005_sub07
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.9512
- Selected anchors: 2026-04-14, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-24

## Summary

| candidate | family | avg excess 5d | max excess 5d | min excess 5d | win 5d | avg portfolio 5d | avg names | avg max weight | params |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| primary_k30_cap100_p1.4 | primary_score_power | +4.333% | +6.380% | +3.121% | 1.00 | +5.389% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap100_p1.4 | primary_score_power | +4.261% | +6.355% | +3.012% | 1.00 | +5.317% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap100_p1.25 | primary_score_power | +4.211% | +6.101% | +2.953% | 1.00 | +5.267% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap100_p1.4 | primary_vol_adjust | +4.177% | +6.025% | +2.775% | 1.00 | +5.233% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k40_cap100_p1.4 | primary_score_power | +4.116% | +6.323% | +2.833% | 1.00 | +5.172% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k30_cap100_p1.4 | primary_vol_adjust | +4.098% | +5.842% | +2.603% | 1.00 | +5.154% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k35_cap100_p1.4 | primary_vol_adjust | +4.097% | +6.019% | +2.665% | 1.00 | +5.153% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap100_p1.25 | primary_score_power | +4.079% | +6.063% | +2.847% | 1.00 | +5.135% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap100_p1.25 | primary_vol_adjust | +4.068% | +5.767% | +2.619% | 1.00 | +5.124% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap100_p1.1 | primary_score_power | +4.062% | +5.818% | +2.769% | 1.00 | +5.118% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k30_cap100_p1.4 | primary_vol_adjust | +4.023% | +5.656% | +2.432% | 1.00 | +5.079% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap100_p1.4 | primary_vol_adjust | +4.014% | +5.846% | +2.492% | 1.00 | +5.070% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap100_p1.25 | primary_vol_adjust | +3.994% | +5.595% | +2.454% | 1.00 | +5.050% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap100_p1.4 | primary_vol_adjust | +3.957% | +5.988% | +2.493% | 1.00 | +5.013% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k40_cap100_p1.25 | primary_score_power | +3.949% | +6.017% | +2.672% | 1.00 | +5.005% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap100_p1 | primary_score_power | +3.936% | +5.629% | +2.639% | 1.00 | +4.992% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap100_p1.4 | primary_vol_adjust | +3.934% | +5.671% | +2.320% | 1.00 | +4.990% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap100_p1.25 | primary_vol_adjust | +3.932% | +5.747% | +2.515% | 1.00 | +4.988% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap100_p1.1 | primary_vol_adjust | +3.924% | +5.508% | +2.451% | 1.00 | +4.980% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap100_p1.25 | primary_vol_adjust | +3.919% | +5.420% | +2.289% | 1.00 | +4.974% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap085_p1.4 | primary_score_power | +3.918% | +5.817% | +2.777% | 1.00 | +4.974% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap100_p1.1 | primary_score_power | +3.900% | +5.766% | +2.672% | 1.00 | +4.956% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap100_p1.4 | primary_vol_adjust | +3.876% | +5.816% | +2.323% | 1.00 | +4.932% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap100_p1.25 | primary_vol_adjust | +3.855% | +5.585% | +2.349% | 1.00 | +4.911% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_k35_cap085_p1.4 | primary_score_power | +3.853% | +5.821% | +2.697% | 1.00 | +4.909% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k30_cap100_p1.1 | primary_vol_adjust | +3.853% | +5.349% | +2.293% | 1.00 | +4.909% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap085_p1.25 | primary_score_power | +3.835% | +5.747% | +2.637% | 1.00 | +4.891% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| blend_primary80_robust20 | primary_robust_blend | +3.828% | +5.031% | +2.589% | 1.00 | +4.884% | 39.0 | 9.86% | primary_share=0.80, max_weight=0.100 |
| primary_voladj_v0.5_k30_cap085_p1.4 | primary_vol_adjust | +3.805% | +5.589% | +2.528% | 1.00 | +4.861% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap100_p1 | primary_vol_adjust | +3.804% | +5.338% | +2.331% | 1.00 | +4.860% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap100_p1.25 | primary_vol_adjust | +3.800% | +5.703% | +2.348% | 1.00 | +4.856% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap100_p1.4 | primary_vol_adjust | +3.794% | +5.641% | +2.154% | 1.00 | +4.850% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap100_p1.1 | primary_vol_adjust | +3.780% | +5.187% | +2.136% | 1.00 | +4.836% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_k40_cap100_p1.1 | primary_score_power | +3.779% | +5.704% | +2.504% | 1.00 | +4.835% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap100_p1 | primary_score_power | +3.778% | +5.567% | +2.550% | 1.00 | +4.834% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap100_p1.25 | primary_vol_adjust | +3.778% | +5.421% | +2.184% | 1.00 | +4.834% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| blend_primary70_robust30 | primary_robust_blend | +3.774% | +4.843% | +2.563% | 1.00 | +4.830% | 39.0 | 9.79% | primary_share=0.70, max_weight=0.100 |
| primary_k40_cap085_p1.4 | primary_score_power | +3.774% | +5.814% | +2.515% | 1.00 | +4.830% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap085_p1.25 | primary_score_power | +3.761% | +5.751% | +2.530% | 1.00 | +4.817% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k35_cap100_p1.1 | primary_vol_adjust | +3.761% | +5.475% | +2.356% | 1.00 | +4.816% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k30_cap085_p1.4 | primary_vol_adjust | +3.748% | +5.475% | +2.406% | 1.00 | +4.804% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap085_p1.1 | primary_score_power | +3.739% | +5.679% | +2.450% | 1.00 | +4.795% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k30_cap100_p1 | primary_vol_adjust | +3.735% | +5.188% | +2.179% | 1.00 | +4.791% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap100_p1.25 | primary_vol_adjust | +3.723% | +5.542% | +2.187% | 1.00 | +4.779% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k35_cap085_p1.4 | primary_vol_adjust | +3.722% | +5.607% | +2.369% | 1.00 | +4.778% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap085_p1.25 | primary_vol_adjust | +3.709% | +5.539% | +2.298% | 1.00 | +4.765% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap085_p1.4 | primary_vol_adjust | +3.691% | +5.368% | +2.284% | 1.00 | +4.747% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap100_p1.1 | primary_vol_adjust | +3.688% | +5.325% | +2.199% | 1.00 | +4.744% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_k40_cap085_p1.25 | primary_score_power | +3.674% | +5.741% | +2.351% | 1.00 | +4.730% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| blend_primary50_robust50 | primary_robust_blend | +3.666% | +4.889% | +2.513% | 1.00 | +4.722% | 39.0 | 9.66% | primary_share=0.50, max_weight=0.100 |
| primary_voladj_v1_k30_cap100_p1 | primary_vol_adjust | +3.665% | +5.036% | +2.028% | 1.00 | +4.721% | 30.0 | 10.00% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap085_p1.4 | primary_vol_adjust | +3.664% | +5.501% | +2.246% | 1.00 | +4.720% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap085_p1.25 | primary_vol_adjust | +3.654% | +5.435% | +2.175% | 1.00 | +4.710% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_k40_cap100_p1 | primary_score_power | +3.647% | +5.493% | +2.390% | 1.00 | +4.703% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap085_p1.1 | primary_score_power | +3.645% | +5.626% | +2.351% | 1.00 | +4.701% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k40_cap100_p1.25 | primary_vol_adjust | +3.645% | +5.379% | +2.026% | 1.00 | +4.701% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap100_p1 | primary_vol_adjust | +3.642% | +5.294% | +2.247% | 1.00 | +4.698% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap085_p1 | primary_score_power | +3.640% | +5.487% | +2.317% | 1.00 | +4.696% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap085_p1.4 | primary_vol_adjust | +3.637% | +5.600% | +2.170% | 1.00 | +4.693% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap100_p1.1 | primary_vol_adjust | +3.637% | +5.414% | +2.198% | 1.00 | +4.693% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k35_cap085_p1.25 | primary_vol_adjust | +3.633% | +5.557% | +2.192% | 1.00 | +4.688% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap100_p1.1 | primary_vol_adjust | +3.614% | +5.174% | +2.043% | 1.00 | +4.670% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap085_p1.4 | primary_vol_adjust | +3.605% | +5.394% | +2.124% | 1.00 | +4.661% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap085_p1.1 | primary_vol_adjust | +3.595% | +5.364% | +2.126% | 1.00 | +4.651% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap085_p1.25 | primary_vol_adjust | +3.586% | +5.263% | +2.056% | 1.00 | +4.642% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap075_p1.4 | primary_score_power | +3.578% | +5.399% | +2.509% | 1.00 | +4.633% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k35_cap100_p1 | primary_vol_adjust | +3.572% | +5.154% | +2.096% | 1.00 | +4.628% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap085_p1.4 | primary_vol_adjust | +3.568% | +5.493% | +1.999% | 1.00 | +4.624% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap100_p1.1 | primary_vol_adjust | +3.564% | +5.266% | +2.046% | 1.00 | +4.619% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap085_p1.25 | primary_vol_adjust | +3.562% | +5.433% | +2.023% | 1.00 | +4.618% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap085_p1.25 | primary_vol_adjust | +3.536% | +5.546% | +2.022% | 1.00 | +4.592% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k30_cap085_p1.1 | primary_vol_adjust | +3.523% | +5.202% | +1.966% | 1.00 | +4.579% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap075_p1.25 | primary_score_power | +3.514% | +5.326% | +2.393% | 1.00 | +4.570% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1.4 | primary_score_power | +3.513% | +5.403% | +2.388% | 1.00 | +4.569% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap085_p1.1 | primary_score_power | +3.510% | +5.562% | +2.181% | 1.00 | +4.566% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap085_p1 | primary_vol_adjust | +3.509% | +5.190% | +2.005% | 1.00 | +4.565% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap085_p1.4 | primary_vol_adjust | +3.509% | +5.387% | +1.879% | 1.00 | +4.565% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap075_p1.4 | primary_vol_adjust | +3.509% | +5.241% | +2.407% | 1.00 | +4.565% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap085_p1 | primary_score_power | +3.507% | +5.424% | +2.227% | 1.00 | +4.563% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap100_p0.75 | primary_score_power | +3.503% | +5.163% | +2.263% | 1.00 | +4.559% | 30.0 | 9.98% | model=primary, top_k=30, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap100_p1 | primary_vol_adjust | +3.500% | +5.222% | +2.092% | 1.00 | +4.556% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap100_p1 | primary_vol_adjust | +3.500% | +5.013% | +1.946% | 1.00 | +4.556% | 35.0 | 10.00% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap085_p1.1 | primary_vol_adjust | +3.494% | +5.330% | +2.030% | 1.00 | +4.550% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap085_p1.25 | primary_vol_adjust | +3.492% | +5.266% | +1.903% | 1.00 | +4.548% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k40_cap100_p1.1 | primary_vol_adjust | +3.489% | +5.116% | +1.894% | 1.00 | +4.545% | 40.0 | 10.00% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap075_p1.4 | primary_vol_adjust | +3.475% | +5.164% | +2.326% | 1.00 | +4.531% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k30_cap085_p1.1 | primary_vol_adjust | +3.456% | +5.037% | +1.818% | 1.00 | +4.511% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_k40_cap075_p1.4 | primary_score_power | +3.454% | +5.396% | +2.265% | 1.00 | +4.510% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap085_p1.25 | primary_vol_adjust | +3.454% | +5.390% | +1.858% | 1.00 | +4.510% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap075_p1.1 | primary_score_power | +3.444% | +5.256% | +2.216% | 1.00 | +4.500% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k30_cap085_p1 | primary_vol_adjust | +3.442% | +5.038% | +1.850% | 1.00 | +4.498% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_k35_cap075_p1.25 | primary_score_power | +3.440% | +5.330% | +2.277% | 1.00 | +4.496% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k30_cap075_p1.4 | primary_vol_adjust | +3.440% | +5.086% | +2.240% | 1.00 | +4.496% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap075_p1.25 | primary_vol_adjust | +3.438% | +5.135% | +2.223% | 1.00 | +4.494% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k35_cap075_p1.4 | primary_vol_adjust | +3.436% | +5.239% | +2.286% | 1.00 | +4.492% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap085_p1.1 | primary_vol_adjust | +3.418% | +5.178% | +1.871% | 1.00 | +4.474% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap100_p1 | primary_vol_adjust | +3.403% | +5.084% | +1.834% | 1.00 | +4.459% | 40.0 | 9.89% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap075_p1.25 | primary_vol_adjust | +3.400% | +5.066% | +2.105% | 1.00 | +4.456% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap075_p1.4 | primary_vol_adjust | +3.398% | +5.166% | +2.184% | 1.00 | +4.454% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| robust_only_k30_cap100_p1 | robust_baseline | +3.397% | +5.003% | +2.388% | 1.00 | +4.453% | 30.0 | 10.00% | model=robust, top_k=30, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1.25 | primary_score_power | +3.392% | +5.319% | +2.138% | 1.00 | +4.448% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap085_p1 | primary_score_power | +3.391% | +5.348% | +2.064% | 1.00 | +4.447% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap075_p1 | primary_score_power | +3.376% | +5.212% | +2.103% | 1.00 | +4.432% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k30_cap085_p1 | primary_vol_adjust | +3.372% | +4.883% | +1.697% | 1.00 | +4.428% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k40_cap085_p1.25 | primary_vol_adjust | +3.372% | +5.225% | +1.694% | 1.00 | +4.428% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap085_p1 | primary_vol_adjust | +3.370% | +5.146% | +1.919% | 1.00 | +4.426% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap075_p1.1 | primary_score_power | +3.366% | +5.261% | +2.138% | 1.00 | +4.422% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap085_p1.1 | primary_vol_adjust | +3.366% | +5.268% | +1.870% | 1.00 | +4.422% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap075_p1.4 | primary_vol_adjust | +3.363% | +5.219% | +2.046% | 1.00 | +4.419% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap075_p1.25 | primary_vol_adjust | +3.361% | +4.996% | +1.985% | 1.00 | +4.417% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap075_p1.4 | primary_vol_adjust | +3.355% | +5.093% | +2.061% | 1.00 | +4.411% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap075_p1.25 | primary_vol_adjust | +3.349% | +5.129% | +2.069% | 1.00 | +4.405% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap085_p1.1 | primary_vol_adjust | +3.343% | +5.024% | +1.712% | 1.00 | +4.399% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap075_p1.1 | primary_vol_adjust | +3.340% | +5.062% | +1.975% | 1.00 | +4.396% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap085_p0.75 | primary_score_power | +3.331% | +5.013% | +1.958% | 1.00 | +4.387% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap075_p1.4 | primary_vol_adjust | +3.317% | +5.146% | +1.923% | 1.00 | +4.373% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap075_p1.25 | primary_vol_adjust | +3.306% | +5.063% | +1.947% | 1.00 | +4.362% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap100_p1 | primary_vol_adjust | +3.303% | +4.944% | +1.578% | 1.00 | +4.359% | 40.0 | 9.80% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap085_p1 | primary_vol_adjust | +3.299% | +5.004% | +1.765% | 1.00 | +4.355% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_k40_cap075_p1.1 | primary_score_power | +3.295% | +5.247% | +1.965% | 1.00 | +4.351% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1 | primary_score_power | +3.295% | +5.218% | +2.012% | 1.00 | +4.351% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap085_p1.1 | primary_vol_adjust | +3.291% | +5.117% | +1.715% | 1.00 | +4.347% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap075_p1.1 | primary_vol_adjust | +3.289% | +4.972% | +1.856% | 1.00 | +4.344% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_k35_cap100_p0.75 | primary_score_power | +3.270% | +5.078% | +2.046% | 1.00 | +4.326% | 35.0 | 9.78% | model=primary, top_k=35, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap075_p1 | primary_vol_adjust | +3.264% | +5.035% | +1.801% | 1.00 | +4.320% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap075_p1.25 | primary_vol_adjust | +3.263% | +5.117% | +1.820% | 1.00 | +4.319% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap075_p1.4 | primary_vol_adjust | +3.262% | +5.072% | +1.800% | 1.00 | +4.318% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap075_p1.25 | primary_vol_adjust | +3.255% | +4.997% | +1.825% | 1.00 | +4.311% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k40_cap085_p1 | primary_vol_adjust | +3.254% | +5.073% | +1.767% | 1.00 | +4.310% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k35_cap075_p1.1 | primary_vol_adjust | +3.246% | +5.081% | +1.827% | 1.00 | +4.302% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap075_p1.1 | primary_vol_adjust | +3.244% | +4.911% | +1.738% | 1.00 | +4.300% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap085_p1 | primary_vol_adjust | +3.226% | +4.860% | +1.613% | 1.00 | +4.282% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k40_cap085_p1.1 | primary_vol_adjust | +3.216% | +4.965% | +1.561% | 1.00 | +4.272% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap075_p1 | primary_vol_adjust | +3.210% | +4.927% | +1.685% | 1.00 | +4.266% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap075_p1.25 | primary_vol_adjust | +3.210% | +5.036% | +1.701% | 1.00 | +4.266% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_k40_cap075_p1 | primary_score_power | +3.203% | +5.202% | +1.847% | 1.00 | +4.259% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k35_cap075_p1.1 | primary_vol_adjust | +3.192% | +4.991% | +1.709% | 1.00 | +4.248% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap085_p1 | primary_vol_adjust | +3.182% | +4.932% | +1.619% | 1.00 | +4.238% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k35_cap075_p1 | primary_vol_adjust | +3.176% | +5.041% | +1.700% | 1.00 | +4.232% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap075_p1.1 | primary_vol_adjust | +3.170% | +5.067% | +1.651% | 1.00 | +4.226% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap085_p0.75 | primary_score_power | +3.167% | +4.926% | +1.905% | 1.00 | +4.223% | 35.0 | 8.50% | model=primary, top_k=35, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k40_cap075_p1.25 | primary_vol_adjust | +3.159% | +4.970% | +1.583% | 1.00 | +4.215% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap075_p1 | primary_vol_adjust | +3.147% | +4.777% | +1.570% | 1.00 | +4.203% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap075_p0.75 | primary_score_power | +3.143% | +4.913% | +1.739% | 1.00 | +4.199% | 30.0 | 7.50% | model=primary, top_k=30, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap075_p1.1 | primary_vol_adjust | +3.140% | +4.907% | +1.592% | 1.00 | +4.195% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k40_cap085_p1 | primary_vol_adjust | +3.109% | +4.790% | +1.471% | 1.00 | +4.165% | 40.0 | 8.50% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap075_p1 | primary_vol_adjust | +3.105% | +4.898% | +1.548% | 1.00 | +4.161% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap075_p1.1 | primary_vol_adjust | +3.102% | +4.977% | +1.494% | 1.00 | +4.158% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap075_p1 | primary_vol_adjust | +3.067% | +4.971% | +1.546% | 1.00 | +4.123% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap075_p1 | primary_vol_adjust | +3.041% | +4.753% | +1.434% | 1.00 | +4.097% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k40_cap075_p1.1 | primary_vol_adjust | +3.032% | +4.850% | +1.363% | 1.00 | +4.088% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_k40_cap085_p0.75 | primary_score_power | +3.004% | +4.820% | +1.700% | 1.00 | +4.060% | 40.0 | 8.43% | model=primary, top_k=40, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap075_p1 | primary_vol_adjust | +2.995% | +4.829% | +1.397% | 1.00 | +4.051% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap060_p1.4 | primary_score_power | +2.991% | +4.464% | +1.753% | 1.00 | +4.047% | 30.0 | 6.00% | model=primary, top_k=30, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p0.75 | primary_score_power | +2.986% | +4.825% | +1.686% | 1.00 | +4.042% | 35.0 | 7.50% | model=primary, top_k=35, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap100_p0.75 | primary_score_power | +2.980% | +4.974% | +1.700% | 1.00 | +4.036% | 40.0 | 9.35% | model=primary, top_k=40, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1.25 | primary_score_power | +2.927% | +4.448% | +1.732% | 1.00 | +3.983% | 30.0 | 6.00% | model=primary, top_k=30, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k40_cap075_p1 | primary_vol_adjust | +2.922% | +4.686% | +1.248% | 1.00 | +3.978% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_k35_cap060_p1.4 | primary_score_power | +2.895% | +4.488% | +1.786% | 1.00 | +3.951% | 35.0 | 6.00% | model=primary, top_k=35, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p0.75 | primary_score_power | +2.895% | +4.718% | +1.552% | 1.00 | +3.951% | 40.0 | 7.50% | model=primary, top_k=40, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.4 | primary_score_power | +2.866% | +4.494% | +1.785% | 1.00 | +3.922% | 40.0 | 6.00% | model=primary, top_k=40, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1.1 | primary_score_power | +2.864% | +4.441% | +1.691% | 1.00 | +3.920% | 30.0 | 6.00% | model=primary, top_k=30, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1.25 | primary_score_power | +2.854% | +4.478% | +1.761% | 1.00 | +3.910% | 35.0 | 6.00% | model=primary, top_k=35, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.25 | primary_score_power | +2.826% | +4.485% | +1.720% | 1.00 | +3.882% | 40.0 | 6.00% | model=primary, top_k=40, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1 | primary_score_power | +2.820% | +4.443% | +1.640% | 1.00 | +3.876% | 30.0 | 6.00% | model=primary, top_k=30, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1.1 | primary_score_power | +2.804% | +4.477% | +1.698% | 1.00 | +3.860% | 35.0 | 6.00% | model=primary, top_k=35, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.1 | primary_score_power | +2.783% | +4.490% | +1.618% | 1.00 | +3.839% | 40.0 | 6.00% | model=primary, top_k=40, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1 | primary_score_power | +2.771% | +4.502% | +1.650% | 1.00 | +3.827% | 35.0 | 6.00% | model=primary, top_k=35, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1 | primary_score_power | +2.752% | +4.530% | +1.497% | 1.00 | +3.808% | 40.0 | 6.00% | model=primary, top_k=40, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p0.75 | primary_score_power | +2.710% | +4.475% | +1.392% | 1.00 | +3.766% | 30.0 | 6.00% | model=primary, top_k=30, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p0.75 | primary_score_power | +2.644% | +4.488% | +1.358% | 1.00 | +3.700% | 35.0 | 6.00% | model=primary, top_k=35, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p0.75 | primary_score_power | +2.601% | +4.465% | +1.221% | 1.00 | +3.657% | 40.0 | 6.00% | model=primary, top_k=40, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |

## Details

| anchor | candidate | excess 5d | portfolio 5d | benchmark 5d | names | max weight | primary IC | robust IC |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-04-14 | blend_primary50_robust50 | +3.671% | +5.918% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | blend_primary70_robust30 | +3.617% | +5.864% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | blend_primary80_robust20 | +3.590% | +5.837% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap060_p0.75 | +2.550% | +4.798% | +2.247% | 30 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap060_p1 | +2.653% | +4.900% | +2.247% | 30 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap060_p1.1 | +2.685% | +4.932% | +2.247% | 30 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap060_p1.25 | +2.732% | +4.979% | +2.247% | 30 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap060_p1.4 | +2.784% | +5.031% | +2.247% | 30 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap075_p0.75 | +2.915% | +5.162% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap075_p1 | +3.061% | +5.308% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap075_p1.1 | +3.115% | +5.362% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap075_p1.25 | +3.172% | +5.419% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap075_p1.4 | +3.212% | +5.459% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap085_p0.75 | +3.068% | +5.316% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap085_p1 | +3.289% | +5.536% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap085_p1.1 | +3.337% | +5.584% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap085_p1.25 | +3.403% | +5.650% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap085_p1.4 | +3.463% | +5.710% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap100_p0.75 | +3.223% | +5.470% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap100_p1 | +3.537% | +5.784% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap100_p1.1 | +3.625% | +5.872% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap100_p1.25 | +3.744% | +5.991% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k30_cap100_p1.4 | +3.783% | +6.030% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap060_p0.75 | +2.536% | +4.784% | +2.247% | 35 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap060_p1 | +2.633% | +4.880% | +2.247% | 35 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap060_p1.1 | +2.661% | +4.908% | +2.247% | 35 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap060_p1.25 | +2.702% | +4.949% | +2.247% | 35 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap060_p1.4 | +2.734% | +4.981% | +2.247% | 35 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap075_p0.75 | +2.832% | +5.080% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap075_p1 | +3.007% | +5.254% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap075_p1.1 | +3.050% | +5.297% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap075_p1.25 | +3.113% | +5.360% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap075_p1.4 | +3.176% | +5.423% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap085_p0.75 | +2.960% | +5.207% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap085_p1 | +3.208% | +5.455% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap085_p1.1 | +3.286% | +5.534% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap085_p1.25 | +3.337% | +5.584% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap085_p1.4 | +3.391% | +5.638% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap100_p0.75 | +3.057% | +5.304% | +2.247% | 35 | 9.76% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap100_p1 | +3.430% | +5.678% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap100_p1.1 | +3.511% | +5.758% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap100_p1.25 | +3.628% | +5.875% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k35_cap100_p1.4 | +3.734% | +5.981% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap060_p0.75 | +2.299% | +4.546% | +2.247% | 40 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap060_p1 | +2.458% | +4.705% | +2.247% | 40 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap060_p1.1 | +2.519% | +4.766% | +2.247% | 40 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap060_p1.25 | +2.563% | +4.810% | +2.247% | 40 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap060_p1.4 | +2.612% | +4.859% | +2.247% | 40 | 6.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap075_p0.75 | +2.523% | +4.770% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap075_p1 | +2.807% | +5.054% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap075_p1.1 | +2.880% | +5.127% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap075_p1.25 | +2.954% | +5.201% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap075_p1.4 | +3.024% | +5.272% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap085_p0.75 | +2.603% | +4.851% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap085_p1 | +2.965% | +5.212% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap085_p1.1 | +3.060% | +5.307% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap085_p1.25 | +3.198% | +5.445% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap085_p1.4 | +3.256% | +5.503% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap100_p0.75 | +2.611% | +4.858% | +2.247% | 40 | 8.59% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap100_p1 | +3.137% | +5.385% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap100_p1.1 | +3.292% | +5.539% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap100_p1.25 | +3.421% | +5.668% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_k40_cap100_p1.4 | +3.545% | +5.792% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap075_p1 | +3.055% | +5.302% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap075_p1.1 | +3.107% | +5.354% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap075_p1.25 | +3.165% | +5.412% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap075_p1.4 | +3.208% | +5.455% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap085_p1 | +3.284% | +5.531% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap085_p1.1 | +3.332% | +5.579% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap085_p1.25 | +3.398% | +5.646% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap085_p1.4 | +3.459% | +5.706% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap100_p1 | +3.506% | +5.754% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap100_p1.1 | +3.593% | +5.840% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap100_p1.25 | +3.716% | +5.963% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k30_cap100_p1.4 | +3.779% | +6.026% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap075_p1 | +2.986% | +5.233% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap075_p1.1 | +3.030% | +5.277% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap075_p1.25 | +3.095% | +5.342% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap075_p1.4 | +3.158% | +5.405% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap085_p1 | +3.161% | +5.409% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap085_p1.1 | +3.248% | +5.495% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap085_p1.25 | +3.321% | +5.568% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap085_p1.4 | +3.377% | +5.624% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap100_p1 | +3.378% | +5.625% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap100_p1.1 | +3.468% | +5.715% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap100_p1.25 | +3.585% | +5.833% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k35_cap100_p1.4 | +3.698% | +5.945% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap075_p1 | +2.740% | +4.987% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap075_p1.1 | +2.841% | +5.088% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap075_p1.25 | +2.922% | +5.169% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap075_p1.4 | +2.995% | +5.242% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap085_p1 | +2.901% | +5.148% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap085_p1.1 | +2.997% | +5.245% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap085_p1.25 | +3.137% | +5.385% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap085_p1.4 | +3.228% | +5.475% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap100_p1 | +3.075% | +5.322% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap100_p1.1 | +3.218% | +5.465% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap100_p1.25 | +3.364% | +5.611% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.5_k40_cap100_p1.4 | +3.489% | +5.736% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap075_p1 | +3.051% | +5.298% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap075_p1.1 | +3.102% | +5.349% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap075_p1.25 | +3.169% | +5.417% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap075_p1.4 | +3.205% | +5.452% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap085_p1 | +3.270% | +5.518% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap085_p1.1 | +3.327% | +5.574% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap085_p1.25 | +3.394% | +5.641% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap085_p1.4 | +3.454% | +5.701% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap100_p1 | +3.489% | +5.736% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap100_p1.1 | +3.575% | +5.822% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap100_p1.25 | +3.697% | +5.944% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k30_cap100_p1.4 | +3.775% | +6.022% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap075_p1 | +2.973% | +5.220% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap075_p1.1 | +3.018% | +5.265% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap075_p1.25 | +3.084% | +5.331% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap075_p1.4 | +3.160% | +5.407% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap085_p1 | +3.136% | +5.383% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap085_p1.1 | +3.222% | +5.469% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap085_p1.25 | +3.310% | +5.557% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap085_p1.4 | +3.368% | +5.615% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap100_p1 | +3.346% | +5.593% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap100_p1.1 | +3.444% | +5.691% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap100_p1.25 | +3.562% | +5.809% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k35_cap100_p1.4 | +3.674% | +5.921% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap075_p1 | +2.704% | +4.951% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap075_p1.1 | +2.806% | +5.053% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap075_p1.25 | +2.903% | +5.150% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap075_p1.4 | +2.977% | +5.224% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap085_p1 | +2.861% | +5.108% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap085_p1.1 | +2.964% | +5.211% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap085_p1.25 | +3.105% | +5.352% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap085_p1.4 | +3.212% | +5.459% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap100_p1 | +3.041% | +5.288% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap100_p1.1 | +3.178% | +5.426% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap100_p1.25 | +3.333% | +5.580% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v0.75_k40_cap100_p1.4 | +3.459% | +5.706% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap075_p1 | +3.044% | +5.292% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap075_p1.1 | +3.102% | +5.349% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap075_p1.25 | +3.190% | +5.437% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap075_p1.4 | +3.202% | +5.449% | +2.247% | 30 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap085_p1 | +3.251% | +5.498% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap085_p1.1 | +3.321% | +5.568% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap085_p1.25 | +3.387% | +5.635% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap085_p1.4 | +3.448% | +5.695% | +2.247% | 30 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap100_p1 | +3.470% | +5.718% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap100_p1.1 | +3.556% | +5.803% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap100_p1.25 | +3.676% | +5.923% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k30_cap100_p1.4 | +3.770% | +6.017% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap075_p1 | +2.959% | +5.206% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap075_p1.1 | +3.005% | +5.252% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap075_p1.25 | +3.073% | +5.320% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap075_p1.4 | +3.159% | +5.407% | +2.247% | 35 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap085_p1 | +3.109% | +5.356% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap085_p1.1 | +3.195% | +5.442% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap085_p1.25 | +3.299% | +5.546% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap085_p1.4 | +3.356% | +5.603% | +2.247% | 35 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap100_p1 | +3.313% | +5.560% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap100_p1.1 | +3.412% | +5.659% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap100_p1.25 | +3.536% | +5.783% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k35_cap100_p1.4 | +3.648% | +5.895% | +2.247% | 35 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap075_p1 | +2.667% | +4.914% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap075_p1.1 | +2.769% | +5.016% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap075_p1.25 | +2.883% | +5.130% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap075_p1.4 | +2.958% | +5.206% | +2.247% | 40 | 7.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap085_p1 | +2.818% | +5.065% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap085_p1.1 | +2.929% | +5.176% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap085_p1.25 | +3.070% | +5.317% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap085_p1.4 | +3.195% | +5.442% | +2.247% | 40 | 8.50% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap100_p1 | +3.005% | +5.252% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap100_p1.1 | +3.137% | +5.384% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap100_p1.25 | +3.300% | +5.547% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | primary_voladj_v1_k40_cap100_p1.4 | +3.427% | +5.674% | +2.247% | 40 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-14 | robust_only_k30_cap100_p1 | +3.805% | +6.052% | +2.247% | 30 | 10.00% | 0.1109 | 0.1245 |
| 2026-04-20 | blend_primary50_robust50 | +4.889% | +4.998% | +0.109% | 38 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | blend_primary70_robust30 | +4.843% | +4.952% | +0.109% | 38 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | blend_primary80_robust20 | +4.820% | +4.929% | +0.109% | 38 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap060_p0.75 | +3.402% | +3.510% | +0.109% | 30 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap060_p1 | +3.514% | +3.622% | +0.109% | 30 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap060_p1.1 | +3.573% | +3.681% | +0.109% | 30 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap060_p1.25 | +3.652% | +3.761% | +0.109% | 30 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap060_p1.4 | +3.747% | +3.856% | +0.109% | 30 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap075_p0.75 | +3.838% | +3.947% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap075_p1 | +4.085% | +4.194% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap075_p1.1 | +4.183% | +4.292% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap075_p1.25 | +4.194% | +4.302% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap075_p1.4 | +4.192% | +4.301% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap085_p0.75 | +4.167% | +4.276% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap085_p1 | +4.312% | +4.421% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap085_p1.1 | +4.402% | +4.511% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap085_p1.25 | +4.532% | +4.640% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap085_p1.4 | +4.654% | +4.763% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap100_p0.75 | +4.261% | +4.370% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap100_p1 | +4.775% | +4.883% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap100_p1.1 | +4.807% | +4.916% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap100_p1.25 | +4.844% | +4.952% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k30_cap100_p1.4 | +4.950% | +5.059% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap060_p0.75 | +3.218% | +3.327% | +0.109% | 35 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap060_p1 | +3.364% | +3.473% | +0.109% | 35 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap060_p1.1 | +3.442% | +3.551% | +0.109% | 35 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap060_p1.25 | +3.547% | +3.656% | +0.109% | 35 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap060_p1.4 | +3.653% | +3.762% | +0.109% | 35 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap075_p0.75 | +3.649% | +3.758% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap075_p1 | +3.938% | +4.047% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap075_p1.1 | +4.058% | +4.167% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap075_p1.25 | +4.123% | +4.232% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap075_p1.4 | +4.138% | +4.247% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap085_p0.75 | +3.989% | +4.098% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap085_p1 | +4.177% | +4.286% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap085_p1.1 | +4.287% | +4.396% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap085_p1.25 | +4.442% | +4.551% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap085_p1.4 | +4.586% | +4.695% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap100_p0.75 | +3.968% | +4.077% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap100_p1 | +4.668% | +4.777% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap100_p1.1 | +4.718% | +4.827% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap100_p1.25 | +4.774% | +4.883% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k35_cap100_p1.4 | +4.891% | +5.000% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap060_p0.75 | +3.285% | +3.394% | +0.109% | 40 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap060_p1 | +3.455% | +3.564% | +0.109% | 40 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap060_p1.1 | +3.468% | +3.577% | +0.109% | 40 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap060_p1.25 | +3.531% | +3.640% | +0.109% | 40 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap060_p1.4 | +3.601% | +3.710% | +0.109% | 40 | 6.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap075_p0.75 | +3.756% | +3.865% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap075_p1 | +3.913% | +4.022% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap075_p1.1 | +4.008% | +4.117% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap075_p1.25 | +4.148% | +4.257% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap075_p1.4 | +4.177% | +4.286% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap085_p0.75 | +3.870% | +3.978% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap085_p1 | +4.207% | +4.316% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap085_p1.1 | +4.245% | +4.354% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap085_p1.25 | +4.370% | +4.479% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap085_p1.4 | +4.497% | +4.605% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap100_p0.75 | +3.760% | +3.868% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap100_p1 | +4.697% | +4.806% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap100_p1.1 | +4.731% | +4.840% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap100_p1.25 | +4.772% | +4.881% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_k40_cap100_p1.4 | +4.813% | +4.922% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap075_p1 | +3.927% | +4.036% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap075_p1.1 | +4.018% | +4.127% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap075_p1.25 | +4.088% | +4.197% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap075_p1.4 | +4.082% | +4.191% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap085_p1 | +4.196% | +4.305% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap085_p1.1 | +4.251% | +4.359% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap085_p1.25 | +4.370% | +4.479% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap085_p1.4 | +4.483% | +4.592% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap100_p1 | +4.687% | +4.796% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap100_p1.1 | +4.720% | +4.829% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap100_p1.25 | +4.756% | +4.865% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k30_cap100_p1.4 | +4.801% | +4.910% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap075_p1 | +3.787% | +3.896% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap075_p1.1 | +3.898% | +4.007% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap075_p1.25 | +4.021% | +4.130% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap075_p1.4 | +4.030% | +4.139% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap085_p1 | +4.078% | +4.187% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap085_p1.1 | +4.140% | +4.249% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap085_p1.25 | +4.283% | +4.392% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap085_p1.4 | +4.417% | +4.526% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap100_p1 | +4.579% | +4.688% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap100_p1.1 | +4.629% | +4.738% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap100_p1.25 | +4.686% | +4.795% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k35_cap100_p1.4 | +4.744% | +4.853% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap075_p1 | +3.778% | +3.887% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap075_p1.1 | +3.856% | +3.965% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap075_p1.25 | +3.983% | +4.092% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap075_p1.4 | +4.074% | +4.183% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap085_p1 | +4.111% | +4.219% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap085_p1.1 | +4.146% | +4.255% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap085_p1.25 | +4.219% | +4.328% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap085_p1.4 | +4.333% | +4.442% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap100_p1 | +4.545% | +4.654% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap100_p1.1 | +4.641% | +4.750% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap100_p1.25 | +4.681% | +4.790% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.5_k40_cap100_p1.4 | +4.708% | +4.817% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap075_p1 | +3.849% | +3.958% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap075_p1.1 | +3.937% | +4.045% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap075_p1.25 | +4.037% | +4.146% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap075_p1.4 | +4.029% | +4.138% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap085_p1 | +4.146% | +4.255% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap085_p1.1 | +4.182% | +4.291% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap085_p1.25 | +4.290% | +4.399% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap085_p1.4 | +4.398% | +4.507% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap100_p1 | +4.642% | +4.751% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap100_p1.1 | +4.674% | +4.783% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap100_p1.25 | +4.711% | +4.820% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k30_cap100_p1.4 | +4.734% | +4.843% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap075_p1 | +3.712% | +3.821% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap075_p1.1 | +3.819% | +3.928% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap075_p1.25 | +3.969% | +4.078% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap075_p1.4 | +3.978% | +4.087% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap085_p1 | +4.028% | +4.137% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap085_p1.1 | +4.082% | +4.191% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap085_p1.25 | +4.205% | +4.314% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap085_p1.4 | +4.333% | +4.442% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap100_p1 | +4.534% | +4.643% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap100_p1.1 | +4.583% | +4.692% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap100_p1.25 | +4.640% | +4.749% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k35_cap100_p1.4 | +4.679% | +4.788% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap075_p1 | +3.726% | +3.835% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap075_p1.1 | +3.782% | +3.891% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap075_p1.25 | +3.902% | +4.011% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap075_p1.4 | +4.020% | +4.128% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap085_p1 | +4.062% | +4.171% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap085_p1.1 | +4.096% | +4.205% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap085_p1.25 | +4.144% | +4.253% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap085_p1.4 | +4.252% | +4.361% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap100_p1 | +4.468% | +4.577% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap100_p1.1 | +4.596% | +4.705% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap100_p1.25 | +4.634% | +4.743% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v0.75_k40_cap100_p1.4 | +4.661% | +4.770% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap075_p1 | +3.772% | +3.881% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap075_p1.1 | +3.856% | +3.964% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap075_p1.25 | +3.974% | +4.083% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap075_p1.4 | +3.977% | +4.086% | +0.109% | 30 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap085_p1 | +4.096% | +4.204% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap085_p1.1 | +4.132% | +4.241% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap085_p1.25 | +4.210% | +4.319% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap085_p1.4 | +4.314% | +4.423% | +0.109% | 30 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap100_p1 | +4.595% | +4.704% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap100_p1.1 | +4.628% | +4.737% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap100_p1.25 | +4.665% | +4.774% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k30_cap100_p1.4 | +4.689% | +4.798% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap075_p1 | +3.639% | +3.747% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap075_p1.1 | +3.741% | +3.850% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap075_p1.25 | +3.884% | +3.993% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap075_p1.4 | +3.927% | +4.036% | +0.109% | 35 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap085_p1 | +3.978% | +4.087% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap085_p1.1 | +4.031% | +4.140% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap085_p1.25 | +4.128% | +4.236% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap085_p1.4 | +4.250% | +4.359% | +0.109% | 35 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap100_p1 | +4.489% | +4.598% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap100_p1.1 | +4.537% | +4.646% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap100_p1.25 | +4.594% | +4.703% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k35_cap100_p1.4 | +4.633% | +4.742% | +0.109% | 35 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap075_p1 | +3.674% | +3.783% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap075_p1.1 | +3.709% | +3.818% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap075_p1.25 | +3.821% | +3.930% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap075_p1.4 | +3.933% | +4.041% | +0.109% | 40 | 7.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap085_p1 | +4.012% | +4.121% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap085_p1.1 | +4.045% | +4.154% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap085_p1.25 | +4.085% | +4.194% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap085_p1.4 | +4.172% | +4.281% | +0.109% | 40 | 8.50% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap100_p1 | +4.386% | +4.495% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap100_p1.1 | +4.550% | +4.659% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap100_p1.25 | +4.586% | +4.695% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | primary_voladj_v1_k40_cap100_p1.4 | +4.613% | +4.722% | +0.109% | 40 | 10.00% | 0.0810 | 0.0851 |
| 2026-04-20 | robust_only_k30_cap100_p1 | +5.003% | +5.112% | +0.109% | 30 | 10.00% | 0.0810 | 0.0851 |
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
| 2026-04-24 | blend_primary50_robust50 | +2.513% | +6.642% | +4.129% | 36 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | blend_primary70_robust30 | +2.563% | +6.693% | +4.129% | 36 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | blend_primary80_robust20 | +2.589% | +6.718% | +4.129% | 36 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap060_p0.75 | +1.392% | +5.521% | +4.129% | 30 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap060_p1 | +1.640% | +5.769% | +4.129% | 30 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap060_p1.1 | +1.691% | +5.820% | +4.129% | 30 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap060_p1.25 | +1.732% | +5.861% | +4.129% | 30 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap060_p1.4 | +1.753% | +5.882% | +4.129% | 30 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap075_p0.75 | +1.739% | +5.869% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap075_p1 | +2.103% | +6.232% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap075_p1.1 | +2.216% | +6.345% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap075_p1.25 | +2.393% | +6.522% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap075_p1.4 | +2.575% | +6.704% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap085_p0.75 | +1.958% | +6.087% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap085_p1 | +2.317% | +6.447% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap085_p1.1 | +2.450% | +6.579% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap085_p1.25 | +2.637% | +6.766% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap085_p1.4 | +2.777% | +6.906% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap100_p0.75 | +2.263% | +6.392% | +4.129% | 30 | 9.90% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap100_p1 | +2.639% | +6.768% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap100_p1.1 | +2.769% | +6.898% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap100_p1.25 | +2.953% | +7.082% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k30_cap100_p1.4 | +3.121% | +7.250% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap060_p0.75 | +1.358% | +5.487% | +4.129% | 35 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap060_p1 | +1.650% | +5.779% | +4.129% | 35 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap060_p1.1 | +1.698% | +5.827% | +4.129% | 35 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap060_p1.25 | +1.761% | +5.890% | +4.129% | 35 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap060_p1.4 | +1.786% | +5.915% | +4.129% | 35 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap075_p0.75 | +1.686% | +5.815% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap075_p1 | +2.012% | +6.141% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap075_p1.1 | +2.138% | +6.267% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap075_p1.25 | +2.277% | +6.406% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap075_p1.4 | +2.461% | +6.590% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap085_p0.75 | +1.905% | +6.034% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap085_p1 | +2.227% | +6.357% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap085_p1.1 | +2.351% | +6.481% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap085_p1.25 | +2.530% | +6.659% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap085_p1.4 | +2.697% | +6.826% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap100_p0.75 | +2.046% | +6.175% | +4.129% | 35 | 9.15% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap100_p1 | +2.550% | +6.679% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap100_p1.1 | +2.672% | +6.801% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap100_p1.25 | +2.847% | +6.977% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k35_cap100_p1.4 | +3.012% | +7.141% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap060_p0.75 | +1.221% | +5.351% | +4.129% | 40 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap060_p1 | +1.497% | +5.626% | +4.129% | 40 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap060_p1.1 | +1.618% | +5.747% | +4.129% | 40 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap060_p1.25 | +1.720% | +5.850% | +4.129% | 40 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap060_p1.4 | +1.785% | +5.914% | +4.129% | 40 | 6.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap075_p0.75 | +1.552% | +5.681% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap075_p1 | +1.847% | +5.976% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap075_p1.1 | +1.965% | +6.094% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap075_p1.25 | +2.138% | +6.267% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap075_p1.4 | +2.265% | +6.394% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap085_p0.75 | +1.700% | +5.829% | +4.129% | 40 | 8.17% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap085_p1 | +2.064% | +6.193% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap085_p1.1 | +2.181% | +6.310% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap085_p1.25 | +2.351% | +6.481% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap085_p1.4 | +2.515% | +6.645% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap100_p0.75 | +1.700% | +5.829% | +4.129% | 40 | 8.17% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap100_p1 | +2.390% | +6.519% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap100_p1.1 | +2.504% | +6.633% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap100_p1.25 | +2.672% | +6.801% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_k40_cap100_p1.4 | +2.833% | +6.963% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap075_p1 | +1.801% | +5.930% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap075_p1.1 | +1.975% | +6.104% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap075_p1.25 | +2.223% | +6.352% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap075_p1.4 | +2.407% | +6.536% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap085_p1 | +2.005% | +6.134% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap085_p1.1 | +2.126% | +6.255% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap085_p1.25 | +2.298% | +6.427% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap085_p1.4 | +2.528% | +6.658% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap100_p1 | +2.331% | +6.461% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap100_p1.1 | +2.451% | +6.580% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap100_p1.25 | +2.619% | +6.748% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k30_cap100_p1.4 | +2.775% | +6.904% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap075_p1 | +1.700% | +5.829% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap075_p1.1 | +1.827% | +5.956% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap075_p1.25 | +2.069% | +6.198% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap075_p1.4 | +2.286% | +6.415% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap085_p1 | +1.919% | +6.048% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap085_p1.1 | +2.030% | +6.159% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap085_p1.25 | +2.192% | +6.321% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap085_p1.4 | +2.369% | +6.498% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap100_p1 | +2.247% | +6.376% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap100_p1.1 | +2.356% | +6.485% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap100_p1.25 | +2.515% | +6.644% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k35_cap100_p1.4 | +2.665% | +6.794% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap075_p1 | +1.546% | +5.676% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap075_p1.1 | +1.651% | +5.780% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap075_p1.25 | +1.820% | +5.949% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap075_p1.4 | +2.046% | +6.175% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap085_p1 | +1.767% | +5.896% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap085_p1.1 | +1.870% | +5.999% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap085_p1.25 | +2.022% | +6.151% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap085_p1.4 | +2.170% | +6.299% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap100_p1 | +2.092% | +6.221% | +4.129% | 40 | 9.98% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap100_p1.1 | +2.198% | +6.328% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap100_p1.25 | +2.348% | +6.477% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.5_k40_cap100_p1.4 | +2.493% | +6.622% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap075_p1 | +1.685% | +5.814% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap075_p1.1 | +1.856% | +5.985% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap075_p1.25 | +2.105% | +6.234% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap075_p1.4 | +2.326% | +6.455% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap085_p1 | +1.850% | +5.979% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap085_p1.1 | +1.966% | +6.095% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap085_p1.25 | +2.175% | +6.304% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap085_p1.4 | +2.406% | +6.535% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap100_p1 | +2.179% | +6.308% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap100_p1.1 | +2.293% | +6.422% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap100_p1.25 | +2.454% | +6.583% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k30_cap100_p1.4 | +2.603% | +6.732% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap075_p1 | +1.548% | +5.677% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap075_p1.1 | +1.709% | +5.838% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap075_p1.25 | +1.947% | +6.076% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap075_p1.4 | +2.184% | +6.313% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap085_p1 | +1.765% | +5.895% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap085_p1.1 | +1.871% | +6.000% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap085_p1.25 | +2.023% | +6.152% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap085_p1.4 | +2.246% | +6.375% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap100_p1 | +2.096% | +6.225% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap100_p1.1 | +2.199% | +6.328% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap100_p1.25 | +2.349% | +6.478% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k35_cap100_p1.4 | +2.492% | +6.621% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap075_p1 | +1.397% | +5.526% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap075_p1.1 | +1.494% | +5.623% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap075_p1.25 | +1.701% | +5.830% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap075_p1.4 | +1.923% | +6.052% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap085_p1 | +1.619% | +5.748% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap085_p1.1 | +1.715% | +5.844% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap085_p1.25 | +1.858% | +5.987% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap085_p1.4 | +1.999% | +6.128% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap100_p1 | +1.834% | +5.963% | +4.129% | 40 | 9.47% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap100_p1.1 | +2.046% | +6.175% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap100_p1.25 | +2.187% | +6.316% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v0.75_k40_cap100_p1.4 | +2.323% | +6.453% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap075_p1 | +1.570% | +5.699% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap075_p1.1 | +1.738% | +5.867% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap075_p1.25 | +1.985% | +6.114% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap075_p1.4 | +2.240% | +6.369% | +4.129% | 30 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap085_p1 | +1.697% | +5.826% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap085_p1.1 | +1.818% | +5.947% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap085_p1.25 | +2.056% | +6.185% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap085_p1.4 | +2.284% | +6.413% | +4.129% | 30 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap100_p1 | +2.028% | +6.157% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap100_p1.1 | +2.136% | +6.265% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap100_p1.25 | +2.289% | +6.419% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k30_cap100_p1.4 | +2.432% | +6.561% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap075_p1 | +1.434% | +5.564% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap075_p1.1 | +1.592% | +5.721% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap075_p1.25 | +1.825% | +5.954% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap075_p1.4 | +2.061% | +6.190% | +4.129% | 35 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap085_p1 | +1.613% | +5.742% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap085_p1.1 | +1.712% | +5.841% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap085_p1.25 | +1.903% | +6.032% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap085_p1.4 | +2.124% | +6.253% | +4.129% | 35 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap100_p1 | +1.946% | +6.075% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap100_p1.1 | +2.043% | +6.172% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap100_p1.25 | +2.184% | +6.314% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k35_cap100_p1.4 | +2.320% | +6.449% | +4.129% | 35 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap075_p1 | +1.248% | +5.377% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap075_p1.1 | +1.363% | +5.492% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap075_p1.25 | +1.583% | +5.712% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap075_p1.4 | +1.800% | +5.929% | +4.129% | 40 | 7.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap085_p1 | +1.471% | +5.600% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap085_p1.1 | +1.561% | +5.690% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap085_p1.25 | +1.694% | +5.823% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap085_p1.4 | +1.879% | +6.008% | +4.129% | 40 | 8.50% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap100_p1 | +1.578% | +5.707% | +4.129% | 40 | 8.98% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap100_p1.1 | +1.894% | +6.024% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap100_p1.25 | +2.026% | +6.155% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | primary_voladj_v1_k40_cap100_p1.4 | +2.154% | +6.283% | +4.129% | 40 | 10.00% | 0.0905 | 0.0957 |
| 2026-04-24 | robust_only_k30_cap100_p1 | +2.388% | +6.517% | +4.129% | 30 | 10.00% | 0.0905 | 0.0957 |