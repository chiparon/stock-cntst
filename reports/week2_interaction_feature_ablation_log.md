# Feature Ablation Log

- Generated at: 2026-05-06 23:53:41
- As-of date: 2026-04-30
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-04-15, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Best By Feature Set

| feature set | groups | n_features | best experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| momentum_shape | momentum_shape | 20 | concentrated_top30 | 30 | 0.0882 | +2.808% | +0.797% | 1.00 |
| momentum_vol_interaction | momentum_shape,momentum_volatility_interaction | 26 | concentrated_top30 | 30 | 0.0877 | +1.854% | +0.473% | 1.00 |
| momentum_liq_interaction | momentum_shape,momentum_liquidity_interaction | 26 | concentrated_top30 | 30 | 0.0764 | +1.529% | +0.427% | 1.00 |
| momentum_vol_liq_interaction | momentum_shape,momentum_volatility_interaction,momentum_liquidity_interaction | 32 | slow_learning_top50 | 50 | 0.0946 | +1.264% | +0.137% | 1.00 |

## Full Results

### momentum_shape

- Groups: `momentum_shape`
- Feature count: 20

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0882 | +2.808% | +0.797% | 1.00 |
| baseline_top50 | 50 | 0.0853 | +1.205% | -0.132% | 0.80 |
| faster_learning_top50 | 50 | 0.0861 | +1.071% | +0.152% | 1.00 |
| slow_learning_top50 | 50 | 0.1059 | +0.914% | -0.798% | 0.80 |
| subsampled_top80 | 80 | 0.0912 | +0.902% | -0.337% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0945 | +0.786% | -0.433% | 0.80 |
| deep_regularized_top80 | 80 | 0.1088 | +0.678% | -0.987% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0685 | +0.633% | -0.411% | 0.60 |

### momentum_vol_interaction

- Groups: `momentum_shape,momentum_volatility_interaction`
- Feature count: 26

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0877 | +1.854% | +0.473% | 1.00 |
| shallow_regularized_top50 | 50 | 0.0983 | +1.346% | -0.145% | 0.80 |
| slow_learning_top50 | 50 | 0.0937 | +1.298% | -0.148% | 0.80 |
| faster_learning_top50 | 50 | 0.0720 | +1.096% | +0.185% | 1.00 |
| deep_regularized_top80 | 80 | 0.1012 | +1.056% | -0.542% | 0.80 |
| baseline_top50 | 50 | 0.0888 | +0.943% | -0.316% | 0.60 |
| subsampled_top80 | 80 | 0.0860 | +0.708% | -0.033% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0817 | +0.705% | -0.637% | 0.80 |

### momentum_liq_interaction

- Groups: `momentum_shape,momentum_liquidity_interaction`
- Feature count: 26

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0764 | +1.529% | +0.427% | 1.00 |
| baseline_top50 | 50 | 0.0883 | +1.494% | +0.560% | 1.00 |
| slow_learning_top50 | 50 | 0.0963 | +1.324% | -0.276% | 0.80 |
| faster_learning_top50 | 50 | 0.0699 | +1.106% | -0.041% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0922 | +1.005% | +0.079% | 1.00 |
| deep_regularized_top80 | 80 | 0.0890 | +0.903% | -0.304% | 0.80 |
| subsampled_top80 | 80 | 0.0938 | +0.673% | -0.066% | 0.60 |
| broad_portfolio_top100 | 100 | 0.0905 | +0.663% | +0.042% | 1.00 |

### momentum_vol_liq_interaction

- Groups: `momentum_shape,momentum_volatility_interaction,momentum_liquidity_interaction`
- Feature count: 32

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| slow_learning_top50 | 50 | 0.0946 | +1.264% | +0.137% | 1.00 |
| shallow_regularized_top50 | 50 | 0.1076 | +1.249% | +0.863% | 1.00 |
| concentrated_top30 | 30 | 0.0911 | +1.233% | -0.596% | 0.80 |
| baseline_top50 | 50 | 0.0770 | +1.178% | -0.377% | 0.80 |
| faster_learning_top50 | 50 | 0.0731 | +1.110% | -0.006% | 0.80 |
| subsampled_top80 | 80 | 0.0958 | +0.840% | +0.130% | 1.00 |
| broad_portfolio_top100 | 100 | 0.0991 | +0.752% | +0.172% | 1.00 |
| deep_regularized_top80 | 80 | 0.0886 | +0.678% | -0.299% | 0.80 |
