# Feature Ablation Log

- Generated at: 2026-05-06 23:55:19
- As-of date: 2026-04-30
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-02-02, 2026-04-15, 2026-04-16, 2026-04-17, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Best By Feature Set

| feature set | groups | n_features | best experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| momentum_shape | momentum_shape | 20 | concentrated_top30 | 30 | 0.0903 | +2.509% | -0.116% | 0.88 |
| momentum_vol_liq_interaction | momentum_shape,momentum_volatility_interaction,momentum_liquidity_interaction | 32 | shallow_regularized_top50 | 50 | 0.1079 | +1.309% | -0.030% | 0.88 |

## Full Results

### momentum_shape

- Groups: `momentum_shape`
- Feature count: 20

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0903 | +2.509% | -0.116% | 0.88 |
| baseline_top50 | 50 | 0.0870 | +1.169% | -0.132% | 0.88 |
| slow_learning_top50 | 50 | 0.1032 | +1.143% | -0.798% | 0.75 |
| faster_learning_top50 | 50 | 0.0919 | +1.070% | +0.023% | 1.00 |
| shallow_regularized_top50 | 50 | 0.0913 | +0.966% | -0.433% | 0.88 |
| subsampled_top80 | 80 | 0.0879 | +0.927% | -0.337% | 0.88 |
| broad_portfolio_top100 | 100 | 0.0788 | +0.747% | -0.411% | 0.75 |
| deep_regularized_top80 | 80 | 0.0975 | +0.733% | -0.987% | 0.75 |

### momentum_vol_liq_interaction

- Groups: `momentum_shape,momentum_volatility_interaction,momentum_liquidity_interaction`
- Feature count: 32

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| shallow_regularized_top50 | 50 | 0.1079 | +1.309% | -0.030% | 0.88 |
| concentrated_top30 | 30 | 0.0966 | +1.072% | -1.071% | 0.75 |
| slow_learning_top50 | 50 | 0.0952 | +1.053% | -0.501% | 0.88 |
| baseline_top50 | 50 | 0.0835 | +1.014% | -0.672% | 0.75 |
| faster_learning_top50 | 50 | 0.0820 | +1.008% | -0.189% | 0.75 |
| subsampled_top80 | 80 | 0.0847 | +1.001% | +0.130% | 1.00 |
| broad_portfolio_top100 | 100 | 0.0980 | +0.763% | -0.047% | 0.88 |
| deep_regularized_top80 | 80 | 0.0897 | +0.756% | -0.350% | 0.75 |
