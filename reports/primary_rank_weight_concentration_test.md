# Primary Rank Weight Concentration Test

- Generated at: 2026-05-10 21:59:45
- As-of date: 2026-05-08
- Primary model: `current_d4_mcw10_l5_lr005`
- Feature groups: `momentum_shape`
- Test shape: top 30, max weight 10%, primary model only
- Question: whether high-ranked/high-score names should receive much larger weights than lower-ranked names.

## Existing Code Behavior

- `src/csi500_ml/portfolio.py` has a `rank` rule where raw rank weights are `top_k, ..., 1` before the 10% cap.
- The week1 candidate used `score_positive`: shift scores positive, add `0.1 * score_std`, then cap/redistribute.
- The week2 final overlay uses `score_positive_raw(...).pow(score_power)` plus optional volatility adjustment. Increasing `score_power` strengthens the high-rank weighting.
- The 10% single-name cap limits how far the top ranks can dominate, so stronger `score_power` mostly reallocates weight inside ranks 3-30 after the top names hit cap.

## Anchor Gates

| gate | AUC | selected anchors |
| --- | ---: | --- |
| 5x80 | 0.9512 | 2026-01-09, 2026-01-12, 2026-01-23, 2026-04-21, 2026-04-22 |
| 8x120 | 0.9512 | 2026-01-08, 2026-01-09, 2026-01-12, 2026-01-15, 2026-01-23, 2026-01-26, 2026-04-21, 2026-04-22 |
| recent40 | 0.9512 | 2026-04-14, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-24 |

## Combined Broad-Gate Readout

Broad-gate average is the mean of the 5x80 and 8x120 summary averages. Current final is `primary_voladj_v1_p1.4_current`.

| candidate | broad avg excess | broad worst min | broad win | recent40 avg | recent40 min |
| --- | ---: | ---: | ---: | ---: | ---: |
| primary_voladj_v1_p3 | +1.142% | -3.149% | 0.78 | +4.549% | +3.372% |
| primary_voladj_v1_p2.6 | +1.125% | -3.184% | 0.78 | +4.510% | +3.486% |
| primary_voladj_v1_p2.2 | +1.099% | -3.225% | 0.78 | +4.433% | +3.374% |
| primary_voladj_v1_p1.8 | +1.081% | -3.266% | 0.78 | +4.277% | +2.919% |
| primary_voladj_v1_p1.4_current **current** | +1.000% | -3.282% | 0.78 | +4.023% | +2.432% |
| primary_voladj_v1_p1 | +0.854% | -3.195% | 0.78 | +3.665% | +2.028% |
| primary_plain_p3 | +0.837% | -4.802% | 0.61 | +4.690% | +3.155% |
| primary_plain_p2.6 | +0.830% | -4.854% | 0.61 | +4.674% | +3.283% |
| primary_plain_p2.2 | +0.813% | -4.917% | 0.61 | +4.630% | +3.380% |
| primary_plain_p1.8 | +0.785% | -4.987% | 0.61 | +4.530% | +3.434% |
| primary_plain_p1.4 | +0.736% | -5.048% | 0.61 | +4.333% | +3.121% |
| primary_plain_p1 | +0.561% | -5.043% | 0.61 | +3.936% | +2.639% |

## Per-Gate Summary

| gate | candidate | avg excess | max excess | min excess | win | top5 weight | top10 weight | effective names | rank1/rank30 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5x80 | primary_voladj_v1_p3 | +1.585% | +6.592% | -3.149% | 0.80 | 41.95% | 70.21% | 17.0 | 3655.3 |
| 5x80 | primary_voladj_v1_p2.6 | +1.565% | +6.412% | -3.184% | 0.80 | 41.80% | 69.25% | 17.2 | 1115.0 |
| 5x80 | primary_voladj_v1_p2.2 | +1.533% | +6.215% | -3.225% | 0.80 | 41.62% | 68.14% | 17.5 | 349.9 |
| 5x80 | primary_voladj_v1_p1.8 | +1.510% | +6.110% | -3.266% | 0.80 | 41.23% | 66.76% | 17.8 | 115.4 |
| 5x80 | primary_voladj_v1_p1.4_current **current** | +1.411% | +5.656% | -3.282% | 0.80 | 40.45% | 64.87% | 18.2 | 41.5 |
| 5x80 | primary_voladj_v1_p1 | +1.230% | +5.036% | -3.195% | 0.80 | 38.74% | 61.59% | 19.3 | 17.0 |
| 5x80 | primary_plain_p3 | +1.219% | +7.036% | -4.802% | 0.60 | 39.01% | 66.37% | 17.4 | 2227.7 |
| 5x80 | primary_plain_p2.6 | +1.211% | +6.918% | -4.854% | 0.60 | 38.70% | 65.33% | 17.7 | 683.8 |
| 5x80 | primary_plain_p2.2 | +1.190% | +6.780% | -4.917% | 0.60 | 38.34% | 64.11% | 18.0 | 217.1 |
| 5x80 | primary_plain_p1.8 | +1.155% | +6.619% | -4.987% | 0.60 | 37.92% | 62.65% | 18.3 | 73.0 |
| 5x80 | primary_plain_p1.4 | +1.094% | +6.380% | -5.048% | 0.60 | 37.30% | 60.81% | 18.8 | 27.0 |
| 5x80 | primary_plain_p1 | +0.879% | +5.629% | -5.043% | 0.60 | 35.64% | 57.67% | 19.8 | 11.2 |
| 8x120 | primary_voladj_v1_p3 | +0.698% | +6.592% | -3.149% | 0.75 | 35.47% | 61.24% | 20.2 | 3654.0 |
| 8x120 | primary_voladj_v1_p2.6 | +0.685% | +6.412% | -3.184% | 0.75 | 35.38% | 60.64% | 20.3 | 1080.0 |
| 8x120 | primary_voladj_v1_p2.2 | +0.665% | +6.215% | -3.225% | 0.75 | 35.27% | 59.94% | 20.5 | 326.3 |
| 8x120 | primary_voladj_v1_p1.8 | +0.651% | +6.110% | -3.266% | 0.75 | 35.02% | 59.07% | 20.6 | 102.8 |
| 8x120 | primary_voladj_v1_p1.4_current **current** | +0.589% | +5.656% | -3.282% | 0.75 | 34.52% | 57.87% | 21.0 | 35.1 |
| 8x120 | primary_voladj_v1_p1 | +0.478% | +5.036% | -3.195% | 0.75 | 33.40% | 55.72% | 21.7 | 13.8 |
| 8x120 | primary_plain_p3 | +0.454% | +7.036% | -4.802% | 0.62 | 31.98% | 55.82% | 20.8 | 3174.5 |
| 8x120 | primary_plain_p2.6 | +0.449% | +6.918% | -4.854% | 0.62 | 31.79% | 55.17% | 21.0 | 925.6 |
| 8x120 | primary_plain_p2.2 | +0.436% | +6.780% | -4.917% | 0.62 | 31.57% | 54.41% | 21.2 | 275.2 |
| 8x120 | primary_plain_p1.8 | +0.414% | +6.619% | -4.987% | 0.62 | 31.30% | 53.49% | 21.4 | 85.0 |
| 8x120 | primary_plain_p1.4 | +0.377% | +6.380% | -5.048% | 0.62 | 30.91% | 52.33% | 21.7 | 28.3 |
| 8x120 | primary_plain_p1 | +0.243% | +5.629% | -5.043% | 0.62 | 29.85% | 50.32% | 22.4 | 10.6 |
| recent40 | primary_plain_p3 | +4.690% | +7.036% | +3.155% | 1.00 | 49.82% | 85.73% | 12.2 | 2537.3 |
| recent40 | primary_plain_p2.6 | +4.674% | +6.918% | +3.283% | 1.00 | 49.58% | 83.88% | 12.7 | 932.0 |
| recent40 | primary_plain_p2.2 | +4.630% | +6.780% | +3.380% | 1.00 | 49.08% | 81.51% | 13.2 | 347.2 |
| recent40 | primary_voladj_v1_p3 | +4.549% | +6.592% | +3.372% | 1.00 | 49.72% | 85.18% | 12.4 | 2880.5 |
| recent40 | primary_plain_p1.8 | +4.530% | +6.619% | +3.434% | 1.00 | 48.25% | 78.33% | 14.0 | 132.0 |
| recent40 | primary_voladj_v1_p2.6 | +4.510% | +6.412% | +3.486% | 1.00 | 49.63% | 83.45% | 12.8 | 1062.8 |
| recent40 | primary_voladj_v1_p2.2 | +4.433% | +6.215% | +3.374% | 1.00 | 49.23% | 81.03% | 13.3 | 388.7 |
| recent40 | primary_plain_p1.4 | +4.333% | +6.380% | +3.121% | 1.00 | 46.95% | 74.16% | 15.1 | 52.6 |
| recent40 | primary_voladj_v1_p1.8 | +4.277% | +6.110% | +2.919% | 1.00 | 48.29% | 77.68% | 14.1 | 144.8 |
| recent40 | primary_voladj_v1_p1.4_current **current** | +4.023% | +5.656% | +2.432% | 1.00 | 46.92% | 73.46% | 15.2 | 57.5 |
| recent40 | primary_plain_p1 | +3.936% | +5.629% | +2.639% | 1.00 | 43.54% | 67.88% | 17.1 | 21.9 |
| recent40 | primary_voladj_v1_p1 | +3.665% | +5.036% | +2.028% | 1.00 | 43.26% | 67.04% | 17.3 | 23.9 |

## Current-vs-Stronger Takeaway

- 5x80: current primary_voladj_v1_p1.4_current = avg +1.411%, min -3.282%; best tested = `primary_voladj_v1_p3` avg +1.585%, min -3.149%.
- 8x120: current primary_voladj_v1_p1.4_current = avg +0.589%, min -3.282%; best tested = `primary_voladj_v1_p3` avg +0.698%, min -3.149%.
- recent40: current primary_voladj_v1_p1.4_current = avg +4.023%, min +2.432%; best tested = `primary_plain_p3` avg +4.690%, min +3.155%.

Interpretation: stronger concentration is already present via `score_power`. In this test, pushing beyond the current vol-adjusted `p1.4` gives a small but consistent lift in the broad gates and a clearer lift in recent40. The tradeoff is concentration: effective names fall from about 15.2 to 12.4 in recent40 when moving from `p1.4` to `p3.0`, and rank1/rank30 becomes extremely large because the low-ranked tail gets tiny weights. If we strengthen the final rule, `primary_voladj_v1_p2.6` is the cleaner compromise: it is nearly tied with `p3.0` on broad-gate average, has the best recent40 minimum among vol-adjusted variants, and is slightly less extreme.
