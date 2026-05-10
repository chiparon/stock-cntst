# Week 1 Realized Comparison

- Generated at: 2026-05-08
- Evaluation window: 2026-05-06 to 2026-05-08
- Data source: project `scripts/download_data.py --update --end 20260508`
- Cache after update: `data/prices.parquet` max date 2026-05-08; `data/index.parquet` max date 2026-05-08.
- Scoring convention: `scripts/score_submission.py`, using previous close before start as entry and close on end date as exit.

## Headline

`submissions/week1_candidate.csv` realized a +8.310% portfolio return over the 3-trading-day week 1 window. The CSI500 benchmark returned +4.128%, so the candidate's realized excess return was +4.182%.

Compared with `submissions/week1.csv`, the candidate was +1.332 percentage points higher in portfolio return and +1.332 percentage points higher in excess return. Note that `week1.csv` is the stage-1 selected week 1 file in the earlier report, while `week1_candidate.csv` was generated later as the primary candidate in the feature/portfolio ablation notes.

## Submission Comparison

| Submission | Names | Portfolio return | Benchmark return | Excess return |
| --- | ---: | ---: | ---: | ---: |
| `week1_candidate.csv` | 30 | +8.310% | +4.128% | +4.182% |
| `stage1_faster_learning_top50.csv` | 50 | +7.255% | +4.128% | +3.128% |
| `stage1_baseline_top50.csv` | 50 | +7.171% | +4.128% | +3.043% |
| `stage1_shallow_regularized_top50.csv` | 50 | +6.978% | +4.128% | +2.850% |
| `week1.csv` | 50 | +6.978% | +4.128% | +2.850% |
| `stage1_concentrated_top30.csv` | 30 | +6.893% | +4.128% | +2.765% |
| `stage1_subsampled_top80.csv` | 80 | +6.808% | +4.128% | +2.680% |
| `stage1_slow_learning_top50.csv` | 50 | +6.788% | +4.128% | +2.660% |
| `week1_baseline.csv` | 50 | +6.416% | +4.128% | +2.288% |
| `stage1_deep_regularized_top80.csv` | 80 | +6.215% | +4.128% | +2.087% |
| `sanity_20260415_20260421.csv` | 50 | +6.070% | +4.128% | +1.942% |
| `stage1_broad_portfolio_top100.csv` | 100 | +5.969% | +4.128% | +1.841% |
| `sanity_20260424_20260430.csv` | 50 | +4.072% | +4.128% | -0.056% |

No submitted holding needed a missing-price fallback during scoring.

## Candidate Attribution

Summary for `week1_candidate.csv`:

- Names: 30
- Weight sum: 1.00000000
- Positive contributors: 19
- Negative contributors: 11
- Gross positive contribution: +10.112%
- Gross negative contribution: -1.802%

Top contributors:

| Stock code | Weight | Realized return | Contribution |
| --- | ---: | ---: | ---: |
| `002281` | 10.00% | +25.256% | +2.526% |
| `000967` | 8.31% | +20.118% | +1.672% |
| `600498` | 5.36% | +22.108% | +1.186% |
| `600208` | 6.04% | +12.747% | +0.770% |
| `002624` | 4.13% | +15.385% | +0.636% |

Largest drags:

| Stock code | Weight | Realized return | Contribution |
| --- | ---: | ---: | ---: |
| `300390` | 10.00% | -6.380% | -0.638% |
| `688819` | 3.74% | -6.660% | -0.249% |
| `002756` | 2.59% | -8.700% | -0.225% |
| `000062` | 5.39% | -3.738% | -0.201% |
| `002294` | 2.94% | -6.609% | -0.194% |

## Candidate vs Stage-1 Week 1

- `week1_candidate.csv`: 30 names.
- `week1.csv`: 50 names.
- Overlap: 19 names.
- Candidate-only names: `000155`, `001389`, `002281`, `002756`, `003035`, `300390`, `300677`, `300757`, `600299`, `601016`, `688702`.
