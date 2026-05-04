# Feature Ablation Log

- Generated at: 2026-05-04 17:14:02
- As-of date: 2026-04-30
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-04-15, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Best By Feature Set

| feature set | groups | n_features | best experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| momentum_shape | momentum_shape | 20 | concentrated_top30 | 30 | 0.0882 | +2.808% | +0.797% | 1.00 |
| mom_ret3_trend_60_20 | mom_ret3,mom_trend_60_20 | 18 | concentrated_top30 | 30 | 0.0977 | +1.992% | +0.672% | 1.00 |
| rank_liquidity | rank_all,liquidity_log | 33 | concentrated_top30 | 30 | 0.1097 | +1.989% | +0.528% | 1.00 |
| liquidity_log | liquidity_log | 18 | concentrated_top30 | 30 | 0.0693 | +1.878% | -0.385% | 0.80 |
| rank_momentum | rank_all,momentum_shape | 34 | concentrated_top30 | 30 | 0.1155 | +1.838% | +0.837% | 1.00 |
| mom_trend_pair | mom_trend_20_5,mom_trend_60_20 | 18 | concentrated_top30 | 30 | 0.1051 | +1.645% | +0.618% | 1.00 |
| rank_vol | rank_all,vol_regime | 35 | concentrated_top30 | 30 | 0.0842 | +1.589% | +0.388% | 1.00 |
| mom_trend_60_20 | mom_trend_60_20 | 16 | concentrated_top30 | 30 | 0.0993 | +1.436% | +0.357% | 1.00 |
| rank_vol_liquidity | rank_all,vol_regime,liquidity_log | 37 | concentrated_top30 | 30 | 0.0871 | +1.397% | +0.173% | 1.00 |
| baseline | baseline | 14 | slow_learning_top50 | 50 | 0.0816 | +1.362% | +0.457% | 1.00 |
| rank_all | rank_all | 31 | concentrated_top30 | 30 | 0.0856 | +1.360% | -0.176% | 0.80 |
| rank_vol_liquidity_momentum | rank_all,vol_regime,liquidity_log,momentum_shape | 40 | concentrated_top30 | 30 | 0.1009 | +1.174% | -0.820% | 0.80 |
| mom_ret3_trend_20_5 | mom_ret3,mom_trend_20_5 | 18 | deep_regularized_top80 | 80 | 0.0868 | +1.048% | -0.403% | 0.80 |
| vol_regime | vol_regime | 22 | broad_portfolio_top100 | 100 | 0.0911 | +1.018% | +0.333% | 1.00 |
| mom_ret3 | mom_ret3 | 16 | broad_portfolio_top100 | 100 | 0.0824 | +0.723% | +0.273% | 1.00 |
| mom_trend_20_5 | mom_trend_20_5 | 16 | broad_portfolio_top100 | 100 | 0.0763 | +0.696% | +0.309% | 1.00 |

## Full Results

### baseline

- Groups: `baseline`
- Feature count: 14

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| slow_learning_top50 | 50 | 0.0816 | +1.362% | +0.457% | 1.00 |
| baseline_top50 | 50 | 0.1000 | +1.303% | -0.255% | 0.80 |
| faster_learning_top50 | 50 | 0.0806 | +1.180% | -0.076% | 0.80 |
| concentrated_top30 | 30 | 0.0749 | +0.926% | -1.201% | 0.80 |
| deep_regularized_top80 | 80 | 0.0863 | +0.856% | -0.977% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0694 | +0.778% | -0.285% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0607 | +0.590% | -0.827% | 0.80 |
| subsampled_top80 | 80 | 0.0518 | +0.013% | -0.615% | 0.40 |

### rank_all

- Groups: `rank_all`
- Feature count: 31

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0856 | +1.360% | -0.176% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0895 | +1.199% | +0.193% | 1.00 |
| slow_learning_top50 | 50 | 0.0919 | +1.085% | +0.114% | 1.00 |
| baseline_top50 | 50 | 0.0950 | +1.036% | -0.533% | 0.80 |
| faster_learning_top50 | 50 | 0.0797 | +0.932% | +0.482% | 1.00 |
| deep_regularized_top80 | 80 | 0.0822 | +0.898% | -0.262% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0956 | +0.714% | -0.159% | 0.80 |
| subsampled_top80 | 80 | 0.0699 | +0.644% | -1.089% | 0.80 |

### vol_regime

- Groups: `vol_regime`
- Feature count: 22

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| broad_portfolio_top100 | 100 | 0.0911 | +1.018% | +0.333% | 1.00 |
| deep_regularized_top80 | 80 | 0.0872 | +0.998% | +0.371% | 1.00 |
| baseline_top50 | 50 | 0.0773 | +0.990% | -0.049% | 0.80 |
| slow_learning_top50 | 50 | 0.0761 | +0.791% | -0.105% | 0.80 |
| faster_learning_top50 | 50 | 0.0778 | +0.728% | -0.797% | 0.60 |
| subsampled_top80 | 80 | 0.0752 | +0.600% | -0.628% | 0.60 |
| shallow_regularized_top50 | 50 | 0.0608 | +0.500% | -0.305% | 0.60 |
| concentrated_top30 | 30 | 0.0792 | +0.412% | -0.600% | 0.40 |

### liquidity_log

- Groups: `liquidity_log`
- Feature count: 18

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0693 | +1.878% | -0.385% | 0.80 |
| faster_learning_top50 | 50 | 0.0833 | +1.616% | +0.044% | 1.00 |
| baseline_top50 | 50 | 0.0790 | +1.453% | +0.314% | 1.00 |
| slow_learning_top50 | 50 | 0.0830 | +1.434% | -0.010% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0827 | +1.316% | -0.093% | 0.80 |
| deep_regularized_top80 | 80 | 0.0821 | +1.035% | -0.101% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0866 | +0.829% | -0.239% | 0.80 |
| subsampled_top80 | 80 | 0.0634 | +0.800% | +0.117% | 1.00 |

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

### mom_ret3

- Groups: `mom_ret3`
- Feature count: 16

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| broad_portfolio_top100 | 100 | 0.0824 | +0.723% | +0.273% | 1.00 |
| concentrated_top30 | 30 | 0.0688 | +0.721% | -0.955% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0738 | +0.713% | -0.393% | 0.80 |
| deep_regularized_top80 | 80 | 0.0500 | +0.686% | -0.645% | 0.80 |
| slow_learning_top50 | 50 | 0.0673 | +0.458% | -0.712% | 0.60 |
| baseline_top50 | 50 | 0.0391 | +0.298% | -0.673% | 0.60 |
| subsampled_top80 | 80 | 0.0734 | +0.262% | -0.589% | 0.40 |
| faster_learning_top50 | 50 | 0.0233 | -0.347% | -1.491% | 0.40 |

### mom_trend_20_5

- Groups: `mom_trend_20_5`
- Feature count: 16

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| broad_portfolio_top100 | 100 | 0.0763 | +0.696% | +0.309% | 1.00 |
| deep_regularized_top80 | 80 | 0.0646 | +0.688% | -0.946% | 0.80 |
| baseline_top50 | 50 | 0.0608 | +0.562% | -0.570% | 0.60 |
| concentrated_top30 | 30 | 0.0767 | +0.519% | -1.326% | 0.60 |
| subsampled_top80 | 80 | 0.0728 | +0.456% | -0.628% | 0.80 |
| slow_learning_top50 | 50 | 0.0713 | +0.342% | -1.468% | 0.60 |
| faster_learning_top50 | 50 | 0.0583 | +0.261% | -0.562% | 0.40 |
| shallow_regularized_top50 | 50 | 0.0716 | +0.161% | -1.490% | 0.60 |

### mom_trend_60_20

- Groups: `mom_trend_60_20`
- Feature count: 16

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0993 | +1.436% | +0.357% | 1.00 |
| faster_learning_top50 | 50 | 0.1033 | +1.147% | -1.114% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0924 | +1.137% | +0.065% | 1.00 |
| baseline_top50 | 50 | 0.0919 | +0.943% | -0.313% | 0.80 |
| slow_learning_top50 | 50 | 0.0814 | +0.941% | +0.147% | 1.00 |
| deep_regularized_top80 | 80 | 0.0908 | +0.820% | -0.489% | 0.80 |
| subsampled_top80 | 80 | 0.0937 | +0.735% | -0.704% | 0.80 |
| broad_portfolio_top100 | 100 | 0.1066 | +0.676% | -0.422% | 0.60 |

### mom_ret3_trend_20_5

- Groups: `mom_ret3,mom_trend_20_5`
- Feature count: 18

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| deep_regularized_top80 | 80 | 0.0868 | +1.048% | -0.403% | 0.80 |
| slow_learning_top50 | 50 | 0.0782 | +0.801% | -0.440% | 0.60 |
| broad_portfolio_top100 | 100 | 0.0808 | +0.758% | -0.498% | 0.80 |
| baseline_top50 | 50 | 0.0782 | +0.718% | -0.127% | 0.80 |
| subsampled_top80 | 80 | 0.0693 | +0.297% | -0.554% | 0.60 |
| faster_learning_top50 | 50 | 0.0608 | -0.186% | -2.219% | 0.40 |
| shallow_regularized_top50 | 50 | 0.0588 | -0.245% | -2.146% | 0.40 |
| concentrated_top30 | 30 | 0.0648 | -0.299% | -2.505% | 0.60 |

### mom_ret3_trend_60_20

- Groups: `mom_ret3,mom_trend_60_20`
- Feature count: 18

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0977 | +1.992% | +0.672% | 1.00 |
| baseline_top50 | 50 | 0.0988 | +1.123% | +0.409% | 1.00 |
| faster_learning_top50 | 50 | 0.0928 | +0.888% | +0.400% | 1.00 |
| deep_regularized_top80 | 80 | 0.0935 | +0.882% | -0.344% | 0.80 |
| slow_learning_top50 | 50 | 0.0969 | +0.872% | -0.144% | 0.80 |
| subsampled_top80 | 80 | 0.0871 | +0.842% | -0.337% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0998 | +0.817% | -0.294% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0826 | +0.463% | -0.423% | 0.40 |

### mom_trend_pair

- Groups: `mom_trend_20_5,mom_trend_60_20`
- Feature count: 18

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.1051 | +1.645% | +0.618% | 1.00 |
| shallow_regularized_top50 | 50 | 0.0948 | +1.125% | -0.727% | 0.80 |
| faster_learning_top50 | 50 | 0.0874 | +0.976% | -0.725% | 0.80 |
| subsampled_top80 | 80 | 0.1096 | +0.913% | -0.190% | 0.80 |
| baseline_top50 | 50 | 0.1021 | +0.885% | -0.299% | 0.80 |
| deep_regularized_top80 | 80 | 0.0866 | +0.812% | -0.471% | 0.80 |
| slow_learning_top50 | 50 | 0.0843 | +0.805% | -0.237% | 0.60 |
| broad_portfolio_top100 | 100 | 0.0964 | +0.570% | -0.573% | 0.80 |

### rank_vol

- Groups: `rank_all,vol_regime`
- Feature count: 35

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0842 | +1.589% | +0.388% | 1.00 |
| slow_learning_top50 | 50 | 0.0808 | +1.451% | -0.083% | 0.80 |
| faster_learning_top50 | 50 | 0.0803 | +1.344% | -0.446% | 0.80 |
| baseline_top50 | 50 | 0.0805 | +1.152% | -0.424% | 0.80 |
| deep_regularized_top80 | 80 | 0.0704 | +0.961% | -0.614% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0834 | +0.950% | -0.074% | 0.80 |
| subsampled_top80 | 80 | 0.1047 | +0.940% | -0.351% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0833 | +0.745% | -0.353% | 0.80 |

### rank_liquidity

- Groups: `rank_all,liquidity_log`
- Feature count: 33

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.1097 | +1.989% | +0.528% | 1.00 |
| slow_learning_top50 | 50 | 0.1053 | +1.443% | +0.064% | 1.00 |
| shallow_regularized_top50 | 50 | 0.1033 | +1.276% | -0.489% | 0.80 |
| baseline_top50 | 50 | 0.0897 | +1.176% | -1.006% | 0.80 |
| deep_regularized_top80 | 80 | 0.0928 | +1.032% | -0.314% | 0.80 |
| faster_learning_top50 | 50 | 0.0949 | +0.971% | -0.907% | 0.80 |
| subsampled_top80 | 80 | 0.0988 | +0.915% | -0.760% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0996 | +0.870% | -0.522% | 0.80 |

### rank_momentum

- Groups: `rank_all,momentum_shape`
- Feature count: 34

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.1155 | +1.838% | +0.837% | 1.00 |
| slow_learning_top50 | 50 | 0.0813 | +1.380% | +0.487% | 1.00 |
| faster_learning_top50 | 50 | 0.1027 | +1.125% | +0.406% | 1.00 |
| broad_portfolio_top100 | 100 | 0.1106 | +0.925% | +0.040% | 1.00 |
| shallow_regularized_top50 | 50 | 0.1060 | +0.890% | -0.955% | 0.80 |
| deep_regularized_top80 | 80 | 0.1045 | +0.860% | -0.474% | 0.80 |
| baseline_top50 | 50 | 0.0950 | +0.771% | +0.012% | 1.00 |
| subsampled_top80 | 80 | 0.0989 | +0.527% | -0.298% | 0.40 |

### rank_vol_liquidity

- Groups: `rank_all,vol_regime,liquidity_log`
- Feature count: 37

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0871 | +1.397% | +0.173% | 1.00 |
| shallow_regularized_top50 | 50 | 0.0971 | +1.361% | -0.692% | 0.80 |
| slow_learning_top50 | 50 | 0.0963 | +1.240% | -0.545% | 0.80 |
| subsampled_top80 | 80 | 0.1043 | +1.123% | -0.081% | 0.80 |
| baseline_top50 | 50 | 0.0819 | +1.076% | -0.821% | 0.80 |
| deep_regularized_top80 | 80 | 0.0932 | +1.043% | -0.769% | 0.80 |
| faster_learning_top50 | 50 | 0.0697 | +1.027% | +0.671% | 1.00 |
| broad_portfolio_top100 | 100 | 0.0991 | +0.789% | +0.016% | 1.00 |

### rank_vol_liquidity_momentum

- Groups: `rank_all,vol_regime,liquidity_log,momentum_shape`
- Feature count: 40

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.1009 | +1.174% | -0.820% | 0.80 |
| deep_regularized_top80 | 80 | 0.0959 | +1.035% | -0.696% | 0.80 |
| faster_learning_top50 | 50 | 0.1019 | +0.974% | -0.656% | 0.60 |
| shallow_regularized_top50 | 50 | 0.1137 | +0.964% | -0.440% | 0.80 |
| subsampled_top80 | 80 | 0.0995 | +0.955% | -0.763% | 0.80 |
| baseline_top50 | 50 | 0.0849 | +0.873% | -0.455% | 0.80 |
| slow_learning_top50 | 50 | 0.0774 | +0.817% | -0.765% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0933 | +0.726% | -0.240% | 0.80 |
