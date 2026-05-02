# Stage 1 Experiment Log

- Generated at: 2026-05-02 22:03:50
- Python: 3.12.13
- Packages: pandas 3.0.2, numpy 1.26.4, pyarrow 24.0.0, xgboost 3.2.0, sklearn 1.8.0, scipy 1.17.1
- Data: prices rows 159,277, stocks 499, dates 2025-01-02 to 2026-04-30, constituents 499
- Git status: M data/constituents.csv
 M data/index.parquet
 M data/prices.parquet
 M features.py
?? reports/
?? stage1_xgboost_sweep.py
- Command: `python stage1_xgboost_sweep.py --prices E:\Eproject\ml-competition-sp26\data\prices.parquet --constituents E:\Eproject\ml-competition-sp26\data\constituents.csv --out-dir submissions --report reports/stage1_experiment_log.md`

## Method

- Factors: reused the official technical factors in `features.py`, including recent returns, volatility, volume z-score, turnover average, moving-average distance, RSI, and cross-sectional ranks.
- Model: XGBoost regressor trained from scratch to predict 5-trading-day forward return.
- Split: time-based train/validation split from the baseline, with a 5-trading-day embargo before the last 10 validation trading days.
- Training rows: 119,363; validation rows: 4,989; train end: 2026-04-01; validation start: 2026-04-10; prediction date: 2026-04-30.
- Portfolio: top-K predicted names with rank-based long-only weights, max weight 10%, fully invested.

## Results

| Experiment | top_k | validation rank IC | valid | output | params |
| --- | ---: | ---: | --- | --- | --- |
| shallow_regularized_top50 | 50 | 0.1314 | yes | `submissions\stage1_shallow_regularized_top50.csv` | n_estimators=500, max_depth=3, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=5.0 |
| subsampled_top80 | 80 | 0.1179 | yes | `submissions\stage1_subsampled_top80.csv` | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.7, colsample_bytree=0.7, min_child_weight=10, reg_lambda=5.0 |
| slow_learning_top50 | 50 | 0.1169 | yes | `submissions\stage1_slow_learning_top50.csv` | n_estimators=800, max_depth=4, learning_rate=0.03, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=5.0 |
| deep_regularized_top80 | 80 | 0.1158 | yes | `submissions\stage1_deep_regularized_top80.csv` | n_estimators=500, max_depth=5, learning_rate=0.03, subsample=0.8, colsample_bytree=0.8, min_child_weight=20, reg_lambda=10.0 |
| concentrated_top30 | 30 | 0.1087 | yes | `submissions\stage1_concentrated_top30.csv` | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=5.0 |
| baseline_top50 | 50 | 0.1045 | yes | `submissions\stage1_baseline_top50.csv` | n_estimators=400, max_depth=5, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=1.0 |
| broad_portfolio_top100 | 100 | 0.1031 | yes | `submissions\stage1_broad_portfolio_top100.csv` | n_estimators=500, max_depth=4, learning_rate=0.05, subsample=0.9, colsample_bytree=0.9, min_child_weight=10, reg_lambda=5.0 |
| faster_learning_top50 | 50 | 0.0999 | yes | `submissions\stage1_faster_learning_top50.csv` | n_estimators=300, max_depth=4, learning_rate=0.08, subsample=0.8, colsample_bytree=0.8, min_child_weight=10, reg_lambda=1.0 |

## Stage Conclusion

- Selected submission: `submissions\stage1_shallow_regularized_top50.csv` copied to `submissions/week1.csv`.
- Best validation rank IC: 0.1314 from `shallow_regularized_top50`.
- Historical sanity check: a baseline portfolio generated as of 2026-04-23 and scored over 2026-04-24 to 2026-04-30 returned -1.310% versus CSI500 +0.655%, for -1.965% excess return. This is only a local sanity check, not the official live evaluation.
- The first-stage choice favors a reproducible XGBoost variant over adding new model families, reducing leakage and integration risk before the May 4 deadline.
- LLM assistance was used for planning and coding support. The portfolio scores and weights are produced by locally trained XGBoost models, not by LLM stock selection.

## Reproduction

```powershell
.\.conda\python.exe -m pip install -r requirements.txt
.\.conda\python.exe stage1_xgboost_sweep.py
.\.conda\python.exe validate_submission.py submissions/week1.csv
```
