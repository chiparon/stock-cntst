# Portfolio Overlay Sweep

- Generated at: 2026-05-10 19:30:48
- As-of date: 2026-05-08
- Feature groups: momentum_shape
- Primary spec: current_d4_mcw10_l5_lr005
- Robust spec: d4_mcw20_l10_lr005_sub07
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.9512
- Selected anchors: 2026-01-09, 2026-01-12, 2026-01-23, 2026-04-21, 2026-04-22

## Summary

| candidate | family | avg excess 5d | max excess 5d | min excess 5d | win 5d | avg portfolio 5d | avg names | avg max weight | params |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| primary_voladj_v1_k30_cap100_p1.4 | primary_vol_adjust | +1.411% | +5.656% | -3.282% | 0.80 | +1.189% | 30.0 | 8.84% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap100_p1.4 | primary_vol_adjust | +1.362% | +5.842% | -3.588% | 0.60 | +1.141% | 30.0 | 8.78% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k30_cap100_p1.25 | primary_vol_adjust | +1.361% | +5.420% | -3.269% | 0.80 | +1.139% | 30.0 | 8.84% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap100_p1.25 | primary_vol_adjust | +1.305% | +5.595% | -3.604% | 0.60 | +1.083% | 30.0 | 8.75% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k30_cap100_p1.1 | primary_vol_adjust | +1.291% | +5.187% | -3.235% | 0.80 | +1.070% | 30.0 | 8.84% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| robust_only_k30_cap100_p1 | robust_baseline | +1.279% | +3.152% | -1.536% | 0.80 | +1.057% | 30.0 | 9.35% | model=robust, top_k=30, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap100_p1.4 | primary_vol_adjust | +1.273% | +6.025% | -4.083% | 0.60 | +1.052% | 30.0 | 8.52% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k35_cap100_p1.4 | primary_vol_adjust | +1.245% | +5.671% | -3.336% | 0.60 | +1.024% | 35.0 | 8.72% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap100_p1 | primary_vol_adjust | +1.230% | +5.036% | -3.195% | 0.80 | +1.008% | 30.0 | 8.84% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap100_p1.1 | primary_vol_adjust | +1.226% | +5.349% | -3.608% | 0.60 | +1.005% | 30.0 | 8.71% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k30_cap100_p1.25 | primary_vol_adjust | +1.215% | +5.767% | -4.097% | 0.60 | +0.993% | 30.0 | 8.50% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap100_p1.4 | primary_vol_adjust | +1.189% | +5.846% | -3.683% | 0.60 | +0.967% | 35.0 | 8.62% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap100_p1 | primary_vol_adjust | +1.157% | +5.188% | -3.601% | 0.60 | +0.935% | 30.0 | 8.68% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k35_cap100_p1.25 | primary_vol_adjust | +1.149% | +5.421% | -3.323% | 0.60 | +0.927% | 35.0 | 8.72% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap100_p1.1 | primary_vol_adjust | +1.136% | +5.508% | -4.099% | 0.60 | +0.914% | 30.0 | 8.46% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap100_p1.4 | primary_vol_adjust | +1.123% | +5.641% | -3.381% | 0.60 | +0.901% | 40.0 | 8.63% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap100_p1.4 | primary_vol_adjust | +1.107% | +6.019% | -4.147% | 0.60 | +0.885% | 35.0 | 8.38% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap100_p1.4 | primary_score_power | +1.094% | +6.380% | -5.048% | 0.60 | +0.873% | 30.0 | 8.04% | model=primary, top_k=30, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k35_cap100_p1.25 | primary_vol_adjust | +1.085% | +5.585% | -3.702% | 0.60 | +0.863% | 35.0 | 8.58% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap100_p1.4 | primary_vol_adjust | +1.084% | +5.816% | -3.694% | 0.60 | +0.862% | 40.0 | 8.55% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.75 |
| blend_primary50_robust50 | primary_robust_blend | +1.079% | +4.134% | -3.290% | 0.80 | +0.857% | 50.0 | 6.99% | primary_share=0.50, max_weight=0.100 |
| primary_voladj_v1_k30_cap085_p1.4 | primary_vol_adjust | +1.075% | +5.368% | -3.797% | 0.80 | +0.854% | 30.0 | 7.64% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap100_p1 | primary_vol_adjust | +1.065% | +5.338% | -4.089% | 0.60 | +0.844% | 30.0 | 8.43% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap085_p1.25 | primary_vol_adjust | +1.062% | +5.263% | -3.727% | 0.80 | +0.840% | 30.0 | 7.64% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap100_p1.1 | primary_vol_adjust | +1.056% | +5.174% | -3.289% | 0.60 | +0.834% | 35.0 | 8.72% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap085_p1.4 | primary_vol_adjust | +1.051% | +5.475% | -3.895% | 0.60 | +0.830% | 30.0 | 7.60% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap085_p1.25 | primary_vol_adjust | +1.047% | +5.435% | -3.849% | 0.60 | +0.825% | 30.0 | 7.60% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap100_p1.25 | primary_vol_adjust | +1.035% | +5.379% | -3.356% | 0.60 | +0.813% | 40.0 | 8.63% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap100_p1.25 | primary_score_power | +1.033% | +6.101% | -5.059% | 0.60 | +0.811% | 30.0 | 8.02% | model=primary, top_k=30, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k30_cap085_p1.1 | primary_vol_adjust | +1.030% | +5.037% | -3.616% | 0.80 | +0.809% | 30.0 | 7.64% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k40_cap100_p1.4 | primary_vol_adjust | +1.013% | +5.988% | -4.154% | 0.60 | +0.792% | 40.0 | 8.31% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap085_p1 | primary_vol_adjust | +1.011% | +4.883% | -3.523% | 0.80 | +0.790% | 30.0 | 7.64% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap100_p1.25 | primary_vol_adjust | +1.002% | +5.747% | -4.163% | 0.60 | +0.780% | 35.0 | 8.35% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k30_cap085_p1.1 | primary_vol_adjust | +1.002% | +5.202% | -3.800% | 0.60 | +0.780% | 30.0 | 7.60% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| blend_primary70_robust30 | primary_robust_blend | +0.999% | +4.732% | -3.991% | 0.80 | +0.777% | 50.0 | 7.35% | primary_share=0.70, max_weight=0.100 |
| primary_voladj_v1_k35_cap100_p1 | primary_vol_adjust | +0.998% | +5.013% | -3.253% | 0.60 | +0.777% | 35.0 | 8.72% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k30_cap085_p1.4 | primary_vol_adjust | +0.996% | +5.589% | -4.147% | 0.60 | +0.775% | 30.0 | 7.55% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k40_cap100_p1.25 | primary_vol_adjust | +0.986% | +5.542% | -3.707% | 0.60 | +0.764% | 40.0 | 8.51% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k30_cap085_p1.25 | primary_vol_adjust | +0.983% | +5.539% | -4.136% | 0.60 | +0.762% | 30.0 | 7.55% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap100_p1.1 | primary_vol_adjust | +0.981% | +5.325% | -3.711% | 0.60 | +0.759% | 35.0 | 8.53% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap085_p1 | primary_vol_adjust | +0.970% | +5.038% | -3.761% | 0.60 | +0.749% | 30.0 | 7.60% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| blend_primary80_robust20 | primary_robust_blend | +0.959% | +5.031% | -4.342% | 0.60 | +0.737% | 50.0 | 7.55% | primary_share=0.80, max_weight=0.100 |
| primary_voladj_v1_k40_cap100_p1.1 | primary_vol_adjust | +0.955% | +5.116% | -3.305% | 0.60 | +0.734% | 40.0 | 8.63% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap100_p1.1 | primary_score_power | +0.952% | +5.818% | -5.057% | 0.60 | +0.730% | 30.0 | 8.00% | model=primary, top_k=30, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap085_p1.1 | primary_vol_adjust | +0.947% | +5.364% | -4.105% | 0.60 | +0.725% | 30.0 | 7.55% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap100_p1.4 | primary_score_power | +0.940% | +6.355% | -5.048% | 0.60 | +0.718% | 35.0 | 7.94% | model=primary, top_k=35, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap085_p1.4 | primary_vol_adjust | +0.919% | +5.394% | -3.809% | 0.60 | +0.697% | 35.0 | 7.52% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap100_p1 | primary_vol_adjust | +0.915% | +5.154% | -3.709% | 0.60 | +0.693% | 35.0 | 8.49% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap100_p1.25 | primary_vol_adjust | +0.913% | +5.703% | -4.164% | 0.60 | +0.692% | 40.0 | 8.27% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap085_p1 | primary_vol_adjust | +0.909% | +5.190% | -4.089% | 0.60 | +0.688% | 30.0 | 7.53% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap100_p1 | primary_vol_adjust | +0.903% | +4.944% | -3.250% | 0.60 | +0.681% | 40.0 | 8.63% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap085_p1.25 | primary_vol_adjust | +0.902% | +5.266% | -3.731% | 0.60 | +0.681% | 35.0 | 7.52% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap100_p1.1 | primary_vol_adjust | +0.897% | +5.475% | -4.168% | 0.60 | +0.675% | 35.0 | 8.31% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap085_p1.4 | primary_vol_adjust | +0.896% | +5.501% | -3.909% | 0.60 | +0.675% | 35.0 | 7.49% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k40_cap100_p1.1 | primary_vol_adjust | +0.893% | +5.266% | -3.708% | 0.60 | +0.671% | 40.0 | 8.45% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap085_p1.25 | primary_vol_adjust | +0.883% | +5.433% | -3.875% | 0.60 | +0.662% | 35.0 | 7.49% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap100_p1 | primary_score_power | +0.879% | +5.629% | -5.043% | 0.60 | +0.657% | 30.0 | 7.97% | model=primary, top_k=30, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap100_p1.4 | primary_score_power | +0.872% | +6.323% | -5.037% | 0.60 | +0.650% | 40.0 | 7.87% | model=primary, top_k=40, max_weight=0.100, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k40_cap085_p1.4 | primary_vol_adjust | +0.864% | +5.387% | -3.802% | 0.60 | +0.643% | 40.0 | 7.43% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap085_p1.1 | primary_vol_adjust | +0.853% | +5.024% | -3.622% | 0.60 | +0.631% | 35.0 | 7.52% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k40_cap085_p1.4 | primary_vol_adjust | +0.847% | +5.493% | -3.926% | 0.60 | +0.625% | 40.0 | 7.40% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k35_cap085_p1.4 | primary_vol_adjust | +0.838% | +5.607% | -4.175% | 0.60 | +0.617% | 35.0 | 7.45% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap100_p1.25 | primary_score_power | +0.833% | +6.063% | -5.060% | 0.60 | +0.611% | 35.0 | 7.92% | model=primary, top_k=35, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k35_cap100_p1 | primary_vol_adjust | +0.829% | +5.294% | -4.162% | 0.60 | +0.608% | 35.0 | 8.27% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k40_cap100_p1 | primary_vol_adjust | +0.829% | +5.084% | -3.698% | 0.60 | +0.608% | 40.0 | 8.40% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap085_p1.25 | primary_vol_adjust | +0.825% | +5.225% | -3.708% | 0.60 | +0.603% | 40.0 | 7.43% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap085_p1.25 | primary_vol_adjust | +0.825% | +5.557% | -4.163% | 0.60 | +0.603% | 35.0 | 7.45% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k35_cap085_p1.1 | primary_vol_adjust | +0.819% | +5.178% | -3.841% | 0.60 | +0.597% | 35.0 | 7.49% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap100_p1.1 | primary_vol_adjust | +0.818% | +5.414% | -4.160% | 0.60 | +0.597% | 40.0 | 8.22% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k40_cap085_p1.25 | primary_vol_adjust | +0.809% | +5.390% | -3.896% | 0.60 | +0.588% | 40.0 | 7.40% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap085_p1.4 | primary_score_power | +0.802% | +5.817% | -5.048% | 0.60 | +0.581% | 30.0 | 7.14% | model=primary, top_k=30, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap085_p1 | primary_vol_adjust | +0.802% | +4.860% | -3.532% | 0.60 | +0.581% | 35.0 | 7.52% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k40_cap085_p1.4 | primary_vol_adjust | +0.799% | +5.600% | -4.192% | 0.60 | +0.577% | 40.0 | 7.37% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap085_p1.25 | primary_score_power | +0.782% | +5.747% | -5.059% | 0.60 | +0.560% | 30.0 | 7.12% | model=primary, top_k=30, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap085_p1.25 | primary_vol_adjust | +0.772% | +5.546% | -4.169% | 0.60 | +0.551% | 40.0 | 7.37% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_k40_cap100_p1.25 | primary_score_power | +0.769% | +6.017% | -5.042% | 0.60 | +0.547% | 40.0 | 7.84% | model=primary, top_k=40, max_weight=0.100, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap085_p1.1 | primary_score_power | +0.762% | +5.679% | -5.057% | 0.60 | +0.541% | 30.0 | 7.10% | model=primary, top_k=30, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k30_cap075_p1.1 | primary_vol_adjust | +0.762% | +4.911% | -4.242% | 0.80 | +0.540% | 30.0 | 6.84% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap085_p1.1 | primary_vol_adjust | +0.760% | +5.330% | -4.168% | 0.60 | +0.539% | 35.0 | 7.41% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap075_p1 | primary_vol_adjust | +0.758% | +4.777% | -4.088% | 0.80 | +0.536% | 30.0 | 6.84% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k30_cap075_p1.4 | primary_vol_adjust | +0.758% | +5.086% | -4.521% | 0.80 | +0.536% | 30.0 | 6.84% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k40_cap085_p1.1 | primary_vol_adjust | +0.756% | +4.965% | -3.586% | 0.60 | +0.535% | 40.0 | 7.43% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k35_cap085_p1 | primary_vol_adjust | +0.756% | +5.004% | -3.801% | 0.60 | +0.535% | 35.0 | 7.49% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap100_p1 | primary_vol_adjust | +0.754% | +5.222% | -4.145% | 0.60 | +0.532% | 40.0 | 8.18% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k30_cap075_p1.25 | primary_vol_adjust | +0.752% | +4.996% | -4.422% | 0.80 | +0.531% | 30.0 | 6.84% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k30_cap075_p1 | primary_vol_adjust | +0.748% | +4.927% | -4.164% | 0.60 | +0.526% | 30.0 | 6.80% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap075_p1.4 | primary_vol_adjust | +0.741% | +5.164% | -4.548% | 0.60 | +0.520% | 30.0 | 6.80% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap075_p1.1 | primary_vol_adjust | +0.739% | +4.972% | -4.288% | 0.60 | +0.518% | 30.0 | 6.80% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k30_cap075_p1.25 | primary_vol_adjust | +0.737% | +5.066% | -4.439% | 0.60 | +0.515% | 30.0 | 6.80% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k30_cap075_p1.4 | primary_vol_adjust | +0.728% | +5.241% | -4.549% | 0.60 | +0.507% | 30.0 | 6.75% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_k35_cap100_p1.1 | primary_score_power | +0.724% | +5.766% | -5.058% | 0.60 | +0.503% | 35.0 | 7.89% | model=primary, top_k=35, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap085_p1.1 | primary_vol_adjust | +0.724% | +5.117% | -3.845% | 0.60 | +0.502% | 40.0 | 7.40% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap085_p1 | primary_score_power | +0.721% | +5.487% | -5.043% | 0.60 | +0.499% | 30.0 | 7.07% | model=primary, top_k=30, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k30_cap075_p1 | primary_vol_adjust | +0.718% | +5.035% | -4.286% | 0.60 | +0.497% | 30.0 | 6.75% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap075_p1.25 | primary_vol_adjust | +0.717% | +5.135% | -4.468% | 0.60 | +0.496% | 30.0 | 6.75% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k30_cap075_p1.1 | primary_vol_adjust | +0.713% | +5.062% | -4.373% | 0.60 | +0.492% | 30.0 | 6.75% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap085_p1 | primary_vol_adjust | +0.711% | +4.790% | -3.512% | 0.60 | +0.489% | 40.0 | 7.43% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap100_p0.75 | primary_score_power | +0.707% | +5.163% | -4.941% | 0.60 | +0.485% | 30.0 | 7.89% | model=primary, top_k=30, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k35_cap085_p1 | primary_vol_adjust | +0.689% | +5.146% | -4.162% | 0.60 | +0.468% | 35.0 | 7.37% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap085_p1.1 | primary_vol_adjust | +0.677% | +5.268% | -4.160% | 0.60 | +0.456% | 40.0 | 7.32% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k40_cap085_p1 | primary_vol_adjust | +0.672% | +4.932% | -3.790% | 0.60 | +0.451% | 40.0 | 7.40% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_k40_cap100_p1.1 | primary_score_power | +0.669% | +5.704% | -5.030% | 0.60 | +0.447% | 40.0 | 7.80% | model=primary, top_k=40, max_weight=0.100, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap100_p1 | primary_score_power | +0.655% | +5.567% | -5.045% | 0.60 | +0.434% | 35.0 | 7.86% | model=primary, top_k=35, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap085_p1.4 | primary_score_power | +0.648% | +5.821% | -5.048% | 0.60 | +0.426% | 35.0 | 7.04% | model=primary, top_k=35, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap085_p1.4 | primary_score_power | +0.636% | +5.814% | -5.037% | 0.60 | +0.414% | 40.0 | 6.97% | model=primary, top_k=40, max_weight=0.085, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap085_p1.25 | primary_score_power | +0.626% | +5.751% | -5.060% | 0.60 | +0.405% | 35.0 | 7.02% | model=primary, top_k=35, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap085_p1 | primary_vol_adjust | +0.616% | +5.073% | -4.145% | 0.60 | +0.394% | 40.0 | 7.28% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_k40_cap085_p1.25 | primary_score_power | +0.604% | +5.741% | -5.042% | 0.60 | +0.383% | 40.0 | 6.94% | model=primary, top_k=40, max_weight=0.085, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap075_p1.1 | primary_vol_adjust | +0.604% | +4.907% | -4.196% | 0.60 | +0.382% | 35.0 | 6.72% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_k40_cap100_p1 | primary_score_power | +0.602% | +5.493% | -5.007% | 0.60 | +0.380% | 40.0 | 7.77% | model=primary, top_k=40, max_weight=0.100, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap075_p1 | primary_vol_adjust | +0.599% | +4.753% | -4.033% | 0.60 | +0.378% | 35.0 | 6.72% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap075_p1.4 | primary_score_power | +0.599% | +5.399% | -5.048% | 0.60 | +0.377% | 30.0 | 6.54% | model=primary, top_k=30, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v1_k35_cap075_p1.25 | primary_vol_adjust | +0.592% | +4.997% | -4.387% | 0.60 | +0.371% | 35.0 | 6.72% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v1_k35_cap075_p1.4 | primary_vol_adjust | +0.591% | +5.093% | -4.526% | 0.60 | +0.370% | 35.0 | 6.72% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_k35_cap085_p1.1 | primary_score_power | +0.588% | +5.626% | -5.058% | 0.60 | +0.367% | 35.0 | 6.99% | model=primary, top_k=35, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k35_cap075_p1.1 | primary_vol_adjust | +0.586% | +4.991% | -4.250% | 0.60 | +0.364% | 35.0 | 6.69% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap075_p1 | primary_vol_adjust | +0.583% | +4.898% | -4.140% | 0.60 | +0.362% | 35.0 | 6.69% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.75_k35_cap075_p1.4 | primary_vol_adjust | +0.581% | +5.166% | -4.526% | 0.60 | +0.359% | 35.0 | 6.69% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_k30_cap075_p1.25 | primary_score_power | +0.577% | +5.326% | -5.059% | 0.60 | +0.356% | 30.0 | 6.52% | model=primary, top_k=30, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap085_p0.75 | primary_score_power | +0.577% | +5.013% | -4.941% | 0.60 | +0.356% | 30.0 | 6.99% | model=primary, top_k=30, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k35_cap075_p1.25 | primary_vol_adjust | +0.577% | +5.063% | -4.408% | 0.60 | +0.355% | 35.0 | 6.69% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k35_cap075_p1.4 | primary_vol_adjust | +0.568% | +5.239% | -4.530% | 0.60 | +0.346% | 35.0 | 6.65% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k35_cap075_p1 | primary_vol_adjust | +0.559% | +5.041% | -4.275% | 0.60 | +0.337% | 35.0 | 6.65% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap075_p1.1 | primary_vol_adjust | +0.558% | +4.850% | -4.087% | 0.40 | +0.337% | 40.0 | 6.63% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.5_k35_cap075_p1.1 | primary_vol_adjust | +0.557% | +5.081% | -4.354% | 0.60 | +0.335% | 35.0 | 6.65% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap075_p1.1 | primary_score_power | +0.556% | +5.256% | -5.057% | 0.60 | +0.335% | 30.0 | 6.50% | model=primary, top_k=30, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k35_cap075_p1.25 | primary_vol_adjust | +0.553% | +5.129% | -4.459% | 0.60 | +0.332% | 35.0 | 6.65% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k40_cap075_p1.1 | primary_vol_adjust | +0.551% | +4.977% | -4.190% | 0.40 | +0.330% | 40.0 | 6.60% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap075_p1.25 | primary_vol_adjust | +0.551% | +4.970% | -4.310% | 0.40 | +0.330% | 40.0 | 6.63% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=1.00 |
| primary_k30_cap075_p1 | primary_score_power | +0.544% | +5.212% | -5.043% | 0.60 | +0.323% | 30.0 | 6.47% | model=primary, top_k=30, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.75_k40_cap075_p1.25 | primary_vol_adjust | +0.543% | +5.036% | -4.345% | 0.40 | +0.322% | 40.0 | 6.60% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v1_k40_cap075_p1.4 | primary_vol_adjust | +0.541% | +5.072% | -4.474% | 0.40 | +0.320% | 40.0 | 6.63% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=1.00 |
| primary_voladj_v0.75_k40_cap075_p1.4 | primary_vol_adjust | +0.539% | +5.146% | -4.484% | 0.40 | +0.318% | 40.0 | 6.60% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.75 |
| primary_voladj_v0.5_k40_cap075_p1.1 | primary_vol_adjust | +0.532% | +5.067% | -4.310% | 0.40 | +0.310% | 40.0 | 6.57% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.5_k40_cap075_p1.4 | primary_vol_adjust | +0.532% | +5.219% | -4.513% | 0.40 | +0.310% | 40.0 | 6.57% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v1_k40_cap075_p1 | primary_vol_adjust | +0.529% | +4.686% | -3.933% | 0.40 | +0.308% | 40.0 | 6.63% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=1.00 |
| primary_k40_cap085_p1.1 | primary_score_power | +0.529% | +5.562% | -5.030% | 0.60 | +0.308% | 40.0 | 6.90% | model=primary, top_k=40, max_weight=0.085, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap075_p1.25 | primary_vol_adjust | +0.527% | +5.117% | -4.426% | 0.40 | +0.305% | 40.0 | 6.57% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=True, vol_power=0.50 |
| primary_voladj_v0.75_k40_cap075_p1 | primary_vol_adjust | +0.522% | +4.829% | -4.054% | 0.40 | +0.301% | 40.0 | 6.60% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.75 |
| primary_k35_cap085_p1 | primary_score_power | +0.515% | +5.424% | -5.045% | 0.60 | +0.293% | 35.0 | 6.96% | model=primary, top_k=35, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_voladj_v0.5_k40_cap075_p1 | primary_vol_adjust | +0.498% | +4.971% | -4.247% | 0.40 | +0.277% | 40.0 | 6.57% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=True, vol_power=0.50 |
| primary_k30_cap075_p0.75 | primary_score_power | +0.483% | +4.913% | -4.941% | 0.60 | +0.262% | 30.0 | 6.39% | model=primary, top_k=30, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap100_p0.75 | primary_score_power | +0.483% | +5.078% | -4.947% | 0.60 | +0.261% | 35.0 | 7.76% | model=primary, top_k=35, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap085_p1 | primary_score_power | +0.465% | +5.348% | -5.007% | 0.60 | +0.243% | 40.0 | 6.87% | model=primary, top_k=40, max_weight=0.085, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1.4 | primary_score_power | +0.437% | +5.403% | -5.048% | 0.60 | +0.215% | 35.0 | 6.44% | model=primary, top_k=35, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1.4 | primary_score_power | +0.424% | +5.396% | -5.037% | 0.40 | +0.202% | 40.0 | 6.37% | model=primary, top_k=40, max_weight=0.075, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1.25 | primary_score_power | +0.414% | +5.330% | -5.060% | 0.60 | +0.193% | 35.0 | 6.42% | model=primary, top_k=35, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1.25 | primary_score_power | +0.406% | +5.319% | -5.042% | 0.40 | +0.184% | 40.0 | 6.34% | model=primary, top_k=40, max_weight=0.075, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1.1 | primary_score_power | +0.394% | +5.261% | -5.058% | 0.60 | +0.172% | 35.0 | 6.39% | model=primary, top_k=35, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap100_p0.75 | primary_score_power | +0.392% | +4.974% | -4.874% | 0.60 | +0.171% | 40.0 | 7.66% | model=primary, top_k=40, max_weight=0.100, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1.1 | primary_score_power | +0.388% | +5.247% | -5.030% | 0.40 | +0.167% | 40.0 | 6.30% | model=primary, top_k=40, max_weight=0.075, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p1 | primary_score_power | +0.382% | +5.218% | -5.045% | 0.60 | +0.161% | 35.0 | 6.36% | model=primary, top_k=35, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p1 | primary_score_power | +0.359% | +5.202% | -5.007% | 0.40 | +0.137% | 40.0 | 6.27% | model=primary, top_k=40, max_weight=0.075, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap085_p0.75 | primary_score_power | +0.346% | +4.926% | -4.947% | 0.60 | +0.125% | 35.0 | 6.86% | model=primary, top_k=35, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap085_p0.75 | primary_score_power | +0.317% | +4.820% | -4.874% | 0.60 | +0.096% | 40.0 | 6.76% | model=primary, top_k=40, max_weight=0.085, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap075_p0.75 | primary_score_power | +0.252% | +4.825% | -4.947% | 0.60 | +0.030% | 35.0 | 6.26% | model=primary, top_k=35, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap075_p0.75 | primary_score_power | +0.224% | +4.718% | -4.874% | 0.40 | +0.003% | 40.0 | 6.16% | model=primary, top_k=40, max_weight=0.075, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p0.75 | primary_score_power | +0.205% | +4.475% | -4.969% | 0.60 | -0.017% | 30.0 | 5.47% | model=primary, top_k=30, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1.4 | primary_score_power | +0.203% | +4.464% | -5.441% | 0.60 | -0.018% | 30.0 | 5.47% | model=primary, top_k=30, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1.25 | primary_score_power | +0.173% | +4.448% | -5.441% | 0.60 | -0.048% | 30.0 | 5.47% | model=primary, top_k=30, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1 | primary_score_power | +0.166% | +4.443% | -5.249% | 0.60 | -0.055% | 30.0 | 5.47% | model=primary, top_k=30, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k30_cap060_p1.1 | primary_score_power | +0.163% | +4.441% | -5.344% | 0.60 | -0.058% | 30.0 | 5.47% | model=primary, top_k=30, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p0.75 | primary_score_power | +0.057% | +4.465% | -4.874% | 0.40 | -0.165% | 40.0 | 5.26% | model=primary, top_k=40, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p0.75 | primary_score_power | +0.043% | +4.488% | -4.947% | 0.40 | -0.178% | 35.0 | 5.36% | model=primary, top_k=35, max_weight=0.060, power=0.75, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1 | primary_score_power | +0.038% | +4.530% | -5.117% | 0.40 | -0.183% | 40.0 | 5.30% | model=primary, top_k=40, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1 | primary_score_power | +0.013% | +4.502% | -5.202% | 0.40 | -0.208% | 35.0 | 5.37% | model=primary, top_k=35, max_weight=0.060, power=1.00, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.1 | primary_score_power | +0.010% | +4.490% | -5.219% | 0.40 | -0.211% | 40.0 | 5.30% | model=primary, top_k=40, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1.1 | primary_score_power | -0.005% | +4.477% | -5.298% | 0.40 | -0.226% | 35.0 | 5.37% | model=primary, top_k=35, max_weight=0.060, power=1.10, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.25 | primary_score_power | -0.017% | +4.485% | -5.357% | 0.40 | -0.238% | 40.0 | 5.30% | model=primary, top_k=40, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1.25 | primary_score_power | -0.021% | +4.478% | -5.422% | 0.40 | -0.243% | 35.0 | 5.37% | model=primary, top_k=35, max_weight=0.060, power=1.25, vol_adjust=False, vol_power=0.00 |
| primary_k35_cap060_p1.4 | primary_score_power | -0.024% | +4.488% | -5.484% | 0.40 | -0.246% | 35.0 | 5.37% | model=primary, top_k=35, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |
| primary_k40_cap060_p1.4 | primary_score_power | -0.036% | +4.494% | -5.471% | 0.40 | -0.257% | 40.0 | 5.30% | model=primary, top_k=40, max_weight=0.060, power=1.40, vol_adjust=False, vol_power=0.00 |

## Details

| anchor | candidate | excess 5d | portfolio 5d | benchmark 5d | names | max weight | primary IC | robust IC |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
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