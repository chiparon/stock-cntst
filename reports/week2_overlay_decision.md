# Week 2 Overlay Decision Note

- Generated at: 2026-05-08
- As-of date: 2026-05-08
- Data cache: updated through 2026-05-08
- Control model: `current_d4_mcw10_l5_lr005`
- Control features: `momentum_shape`
- Objective: improve portfolio construction without broad feature stacking.

## Validation Gates

Three gates were run with the updated 2026-05-08 as-of cross-section:

| Gate | Report | Anchor rule | Selected anchors |
| --- | --- | --- | --- |
| 5x80 | `reports/week2_portfolio_overlay_sweep.md` | top 5 dates from recent 80 eligible dates | 2026-01-09, 2026-01-12, 2026-01-23, 2026-04-21, 2026-04-22 |
| 8x120 | `reports/week2_portfolio_overlay_sweep_8x120.md` | top 8 dates from recent 120 eligible dates | 2026-01-08, 2026-01-09, 2026-01-12, 2026-01-15, 2026-01-23, 2026-01-26, 2026-04-21, 2026-04-22 |
| recent40 | `reports/week2_portfolio_overlay_sweep_recent40.md` | top 5 dates from recent 40 eligible dates | 2026-04-14, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-24 |

Adversarial validation AUC is 0.9512, which means the 2026-05-08 live cross-section is quite distinct from historical dates. The wider gates therefore include January 2026 anchors, while the recency-constrained gate stays in April.

## Key Candidates

All numbers below are 5-trading-day excess returns.

| candidate | 5x80 avg | 5x80 min | 8x120 avg | 8x120 min | recent40 avg | recent40 min |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `primary_k30_cap100_p1` | +0.879% | -5.043% | +0.243% | -5.043% | +3.936% | +2.639% |
| `primary_k30_cap100_p1.25` | +1.033% | -5.059% | +0.339% | -5.059% | +4.211% | +2.953% |
| `primary_voladj_k30_cap100_p1` | +1.230% | -3.195% | +0.478% | -3.195% | +3.665% | +2.028% |
| `primary_voladj_k30_cap100_p1.25` | +1.361% | -3.269% | +0.559% | -3.269% | +3.919% | +2.289% |
| `robust_only_k30_cap100_p1` | +1.279% | -1.536% | +0.085% | -3.927% | +3.397% | +2.388% |

## Readout

`primary_voladj_k30_cap100_p1.25` is the best cross-gate compromise:

- It is the best 5x80 candidate by average excess return.
- It is second-best in 8x120 by average excess return and keeps a higher win rate than the top 8x120 `k35` variant.
- It remains close to the recent40 winner, giving up about 0.29 percentage points of recent40 mean excess versus pure `p1.25` while reducing the deep negative windows in the wider gates.

Pure `primary_k30_cap100_p1.25` is attractive only if we fully trust the recent40 gate. It wins recent40, but its 5x80 and 8x120 worst windows are around -5.06%, so it is too fragile as the primary recommendation.

`robust_only_k30_cap100_p1` has the best 5x80 worst window, but it loses too much in 8x120 and changes the selected stock set more aggressively. Keep it as a fallback rather than the primary.

## Generated Submission Candidates

The following files were generated from 2026-05-08 data and passed `validate_submission.py`:

| file | purpose |
| --- | --- |
| `submissions/week2_primary_k30_cap100.csv` | updated primary baseline |
| `submissions/week2_primary_k30_cap100_p125.csv` | high-conviction primary weighting |
| `submissions/week2_primary_voladj_k30_cap100.csv` | volatility-adjusted primary, power 1.00 |
| `submissions/week2_primary_voladj_k30_cap100_p125.csv` | recommended cross-gate overlay |
| `submissions/week2_robust_k30_cap100.csv` | robust fallback |

Recommendation for the current checkpoint: use `submissions/week2_primary_voladj_k30_cap100_p125.csv` as the leading week-2 candidate, with `submissions/week2_robust_k30_cap100.csv` retained as a conservative fallback.

