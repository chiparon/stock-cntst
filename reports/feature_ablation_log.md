# Feature Ablation Log

- Generated at: 2026-05-05 21:27:50
- As-of date: 2026-04-30
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-04-15, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Best By Feature Set

| feature set | groups | n_features | best experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| momentum_shape | momentum_shape | 20 | concentrated_top30 | 30 | 0.0882 | +2.808% | +0.797% | 1.00 |
| rank_liquidity | rank_all,liquidity_log | 36 | concentrated_top30 | 30 | 0.0788 | +2.184% | +0.598% | 1.00 |
| mom_ret3_trend_60_20 | mom_ret3,mom_trend_60_20 | 18 | concentrated_top30 | 30 | 0.0977 | +1.992% | +0.672% | 1.00 |
| liquidity_log | liquidity_log | 18 | concentrated_top30 | 30 | 0.0693 | +1.878% | -0.385% | 0.80 |
| rank_all | rank_all | 34 | concentrated_top30 | 30 | 0.0919 | +1.763% | +0.674% | 1.00 |
| rank_vol | rank_all,vol_regime | 38 | concentrated_top30 | 30 | 0.0863 | +1.728% | +0.722% | 1.00 |
| rank_momentum | rank_all,momentum_shape | 37 | concentrated_top30 | 30 | 0.1007 | +1.727% | +0.907% | 1.00 |
| mom_trend_pair | mom_trend_20_5,mom_trend_60_20 | 18 | concentrated_top30 | 30 | 0.1051 | +1.645% | +0.618% | 1.00 |
| momentum_index | momentum_shape,index_relative | 29 | concentrated_top30 | 30 | 0.0585 | +1.540% | +0.594% | 1.00 |
| rank_vol_liquidity | rank_all,vol_regime,liquidity_log | 40 | concentrated_top30 | 30 | 0.0980 | +1.439% | +0.073% | 1.00 |
| mom_trend_60_20 | mom_trend_60_20 | 16 | concentrated_top30 | 30 | 0.0993 | +1.436% | +0.357% | 1.00 |
| baseline | baseline | 14 | slow_learning_top50 | 50 | 0.0816 | +1.362% | +0.457% | 1.00 |
| rank_vol_liquidity_momentum | rank_all,vol_regime,liquidity_log,momentum_shape | 43 | concentrated_top30 | 30 | 0.0944 | +1.309% | -0.137% | 0.80 |
| index_relative | index_relative | 23 | concentrated_top30 | 30 | 0.0460 | +1.217% | -0.187% | 0.80 |
| mom_ret3_trend_20_5 | mom_ret3,mom_trend_20_5 | 18 | deep_regularized_top80 | 80 | 0.0868 | +1.048% | -0.403% | 0.80 |
| vol_regime | vol_regime | 22 | broad_portfolio_top100 | 100 | 0.0911 | +1.018% | +0.333% | 1.00 |
| mom_ret3 | mom_ret3 | 16 | broad_portfolio_top100 | 100 | 0.0824 | +0.723% | +0.273% | 1.00 |
| mom_trend_20_5 | mom_trend_20_5 | 16 | broad_portfolio_top100 | 100 | 0.0763 | +0.696% | +0.309% | 1.00 |
| rank_liquidity_index | rank_all,liquidity_log,index_relative | 42 | concentrated_top30 | 30 | -0.0011 | +0.154% | -2.474% | 0.60 |

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
- Feature count: 34

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0919 | +1.763% | +0.674% | 1.00 |
| baseline_top50 | 50 | 0.0879 | +1.513% | +0.987% | 1.00 |
| faster_learning_top50 | 50 | 0.0901 | +1.202% | -0.098% | 0.80 |
| slow_learning_top50 | 50 | 0.0821 | +1.200% | +0.268% | 1.00 |
| shallow_regularized_top50 | 50 | 0.0855 | +1.160% | +0.450% | 1.00 |
| subsampled_top80 | 80 | 0.1095 | +1.158% | +0.421% | 1.00 |
| deep_regularized_top80 | 80 | 0.1077 | +1.129% | +0.224% | 1.00 |
| broad_portfolio_top100 | 100 | 0.1015 | +0.857% | -0.099% | 0.80 |

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
- Feature count: 38

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0863 | +1.728% | +0.722% | 1.00 |
| faster_learning_top50 | 50 | 0.0856 | +1.719% | -0.059% | 0.80 |
| slow_learning_top50 | 50 | 0.0954 | +1.666% | +0.321% | 1.00 |
| baseline_top50 | 50 | 0.0885 | +1.176% | -0.832% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0861 | +1.002% | -0.856% | 0.80 |
| subsampled_top80 | 80 | 0.0765 | +0.930% | -0.479% | 0.80 |
| deep_regularized_top80 | 80 | 0.0954 | +0.857% | -0.952% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0863 | +0.819% | +0.022% | 1.00 |

### rank_liquidity

- Groups: `rank_all,liquidity_log`
- Feature count: 36

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0788 | +2.184% | +0.598% | 1.00 |
| faster_learning_top50 | 50 | 0.0985 | +1.260% | -0.283% | 0.80 |
| subsampled_top80 | 80 | 0.1124 | +1.203% | +0.009% | 1.00 |
| shallow_regularized_top50 | 50 | 0.0910 | +1.196% | +0.031% | 1.00 |
| slow_learning_top50 | 50 | 0.0979 | +1.162% | +0.109% | 1.00 |
| baseline_top50 | 50 | 0.0904 | +0.868% | -0.532% | 0.80 |
| broad_portfolio_top100 | 100 | 0.0916 | +0.800% | -0.459% | 0.80 |
| deep_regularized_top80 | 80 | 0.1027 | +0.705% | -0.541% | 0.80 |

### rank_momentum

- Groups: `rank_all,momentum_shape`
- Feature count: 37

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.1007 | +1.727% | +0.907% | 1.00 |
| slow_learning_top50 | 50 | 0.0906 | +1.035% | +0.314% | 1.00 |
| faster_learning_top50 | 50 | 0.0776 | +1.015% | -0.055% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0967 | +0.903% | -0.005% | 0.80 |
| deep_regularized_top80 | 80 | 0.0892 | +0.769% | +0.335% | 1.00 |
| baseline_top50 | 50 | 0.0841 | +0.689% | -0.506% | 0.60 |
| broad_portfolio_top100 | 100 | 0.1029 | +0.597% | -0.109% | 0.80 |
| subsampled_top80 | 80 | 0.0928 | +0.562% | -0.128% | 0.60 |

### index_relative

- Groups: `index_relative`
- Feature count: 23

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0460 | +1.217% | -0.187% | 0.80 |
| faster_learning_top50 | 50 | 0.0532 | +0.760% | -0.079% | 0.80 |
| subsampled_top80 | 80 | 0.0691 | +0.507% | -0.926% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0770 | +0.498% | -1.053% | 0.60 |
| broad_portfolio_top100 | 100 | 0.0554 | +0.247% | -0.746% | 0.40 |
| deep_regularized_top80 | 80 | 0.0410 | +0.241% | -1.375% | 0.80 |
| slow_learning_top50 | 50 | 0.0071 | -0.080% | -1.402% | 0.60 |
| baseline_top50 | 50 | 0.0227 | -0.287% | -2.336% | 0.60 |

### momentum_index

- Groups: `momentum_shape,index_relative`
- Feature count: 29

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0585 | +1.540% | +0.594% | 1.00 |
| faster_learning_top50 | 50 | 0.0576 | +0.622% | -1.387% | 0.60 |
| shallow_regularized_top50 | 50 | 0.0820 | +0.565% | -2.203% | 0.60 |
| baseline_top50 | 50 | 0.0268 | +0.376% | -2.186% | 0.80 |
| deep_regularized_top80 | 80 | 0.0301 | +0.369% | -0.965% | 0.60 |
| slow_learning_top50 | 50 | 0.0533 | +0.331% | -0.745% | 0.60 |
| broad_portfolio_top100 | 100 | 0.0561 | +0.063% | -0.915% | 0.60 |
| subsampled_top80 | 80 | 0.0232 | -0.648% | -2.681% | 0.40 |

### rank_liquidity_index

- Groups: `rank_all,liquidity_log,index_relative`
- Feature count: 42

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | -0.0011 | +0.154% | -2.474% | 0.60 |
| broad_portfolio_top100 | 100 | 0.0748 | +0.070% | -0.468% | 0.60 |
| deep_regularized_top80 | 80 | 0.0063 | -0.078% | -1.407% | 0.60 |
| faster_learning_top50 | 50 | 0.0038 | -0.136% | -1.089% | 0.60 |
| shallow_regularized_top50 | 50 | 0.0190 | -0.525% | -2.802% | 0.40 |
| subsampled_top80 | 80 | -0.0260 | -0.675% | -2.582% | 0.20 |
| slow_learning_top50 | 50 | 0.0041 | -0.677% | -2.802% | 0.40 |
| baseline_top50 | 50 | -0.0143 | -0.775% | -2.802% | 0.40 |

### rank_vol_liquidity

- Groups: `rank_all,vol_regime,liquidity_log`
- Feature count: 40

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0980 | +1.439% | +0.073% | 1.00 |
| baseline_top50 | 50 | 0.0833 | +1.104% | -0.298% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0866 | +1.072% | -0.157% | 0.80 |
| subsampled_top80 | 80 | 0.0883 | +0.915% | -0.745% | 0.80 |
| broad_portfolio_top100 | 100 | 0.1109 | +0.911% | -0.364% | 0.80 |
| slow_learning_top50 | 50 | 0.0844 | +0.891% | -1.299% | 0.80 |
| deep_regularized_top80 | 80 | 0.0832 | +0.884% | -0.056% | 0.80 |
| faster_learning_top50 | 50 | 0.0678 | +0.631% | -0.918% | 0.80 |

### rank_vol_liquidity_momentum

- Groups: `rank_all,vol_regime,liquidity_log,momentum_shape`
- Feature count: 43

| experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | ---: | ---: | ---: | ---: | ---: |
| concentrated_top30 | 30 | 0.0944 | +1.309% | -0.137% | 0.80 |
| slow_learning_top50 | 50 | 0.1005 | +1.133% | -0.884% | 0.80 |
| deep_regularized_top80 | 80 | 0.0897 | +0.893% | -0.618% | 0.80 |
| subsampled_top80 | 80 | 0.0778 | +0.880% | -0.445% | 0.80 |
| shallow_regularized_top50 | 50 | 0.0996 | +0.878% | -0.415% | 0.80 |
| faster_learning_top50 | 50 | 0.0983 | +0.810% | +0.100% | 1.00 |
| broad_portfolio_top100 | 100 | 0.0981 | +0.750% | -0.008% | 0.80 |
| baseline_top50 | 50 | 0.0939 | +0.453% | -0.774% | 0.80 |
