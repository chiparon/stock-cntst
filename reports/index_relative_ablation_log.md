# Feature Ablation Log

- Generated at: 2026-05-05 21:29:56
- As-of date: 2026-04-30
- Holding window: 5 trading days
- Anchor selection feature groups: baseline
- Adversarial validation AUC: 0.8906
- Selected anchors: 2026-04-15, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23

## Best By Feature Set

| feature set | groups | n_features | best experiment | top_k | mean IC | mean excess 5d | min excess 5d | win 5d |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| momentum_shape | momentum_shape | 20 | concentrated_top30 | 30 | 0.0882 | +2.808% | +0.797% | 1.00 |
| momentum_index | momentum_shape,index_relative | 29 | concentrated_top30 | 30 | 0.0585 | +1.540% | +0.594% | 1.00 |
| index_relative | index_relative | 23 | concentrated_top30 | 30 | 0.0460 | +1.217% | -0.187% | 0.80 |
| rank_liquidity_index | rank_all,liquidity_log,index_relative | 42 | concentrated_top30 | 30 | -0.0011 | +0.154% | -2.474% | 0.60 |

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
