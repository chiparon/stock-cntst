# Week 2 Final Submission Decision

- Generated at: 2026-05-10
- Submission 2 deadline: 2026-05-10 23:59
- Evaluation window: 2026-05-11 to 2026-05-15
- Final data refresh attempted through 2026-05-10.
- Latest available trading data remains 2026-05-08 because 2026-05-09 and 2026-05-10 are weekend dates.

## Final Sweep

The final sweep keeps the model fixed and only adjusts portfolio construction:

- Model: `current_d4_mcw10_l5_lr005`
- Feature group: `momentum_shape`
- Top names: 30
- Weighting: score-positive weights with volatility adjustment
- Volatility adjustment: divide raw score weights by `vol_20d ** vol_power`

Three gates were rerun:

| Gate | Report | Anchor rule |
| --- | --- | --- |
| 5x80 | `reports/week2_final_overlay_sweep_5x80.md` | top 5 dates from recent 80 eligible dates |
| 8x120 | `reports/week2_final_overlay_sweep_8x120.md` | top 8 dates from recent 120 eligible dates |
| recent40 | `reports/week2_final_overlay_sweep_recent40.md` | top 5 dates from recent 40 eligible dates |

## Key Readout

All metrics are 5-trading-day excess returns.

The original final sweep selected `p1.40`. A follow-up primary-only
concentration test then extended `score_power` to `2.60` and `3.00` while
keeping the model, feature set, top-30 names, 10% cap, and volatility adjustment
unchanged.

| candidate | 5x80 avg | 5x80 min | 8x120 avg | 8x120 min | recent40 avg | recent40 min |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `primary_voladj_v1_k30_cap100_p1.10` | +1.291% | -3.235% | +0.516% | -3.235% | +3.780% | +2.136% |
| `primary_voladj_v1_k30_cap100_p1.25` | +1.361% | -3.269% | +0.559% | -3.269% | +3.919% | +2.289% |
| `primary_voladj_v1_k30_cap100_p1.40` | +1.411% | -3.282% | +0.589% | -3.282% | +4.023% | +2.432% |
| `primary_voladj_v1_k30_cap100_p2.60` | +1.565% | -3.184% | +0.685% | -3.184% | +4.510% | +3.486% |
| `primary_voladj_v1_k30_cap100_p3.00` | +1.585% | -3.149% | +0.698% | -3.149% | +4.549% | +3.372% |
| `primary_k30_cap100_p1.40` | +1.094% | -5.048% | +0.377% | -5.048% | +4.333% | +3.121% |
| `robust_only_k30_cap100_p1` | +1.279% | -1.536% | +0.085% | -3.927% | +3.397% | +2.388% |

## Decision

Use `submissions/week2_final_primary_voladj_v1_k30_p26.csv` as the final leading candidate.

Rationale:

- It improves average excess return versus the earlier `p1.40` final candidate in all three gates.
- It improves the worst-window excess in both broad gates and has the best recent40 minimum among the tested vol-adjusted concentration variants.
- Its win rate is unchanged versus `p1.40` in the broad gates and remains 1.00 in recent40.
- It keeps the same 30 selected names as `p1.40`; the change is only a controlled weight-intensity adjustment.
- `p3.00` has slightly higher broad-gate average, but `p2.60` is less extreme and has better recent40 minimum, making it the cleaner final risk/reward choice.

Keep `submissions/week2_final_primary_voladj_v1_k30_p14.csv` as the conservative backup if the final preference shifts toward lower concentration.

## Generated Files

The final selected file passed `scripts/validate_submission.py`:

| file | role |
| --- | --- |
| `submissions/week2_final_primary_voladj_v1_k30_p26.csv` | final leading candidate |
| `submissions/week2_final_primary_voladj_v1_k30_p14.csv` | conservative backup |

