# Primary p1.4 / p3.0 Weight Blend Test

- Generated at: 2026-05-10 22:54:51
- As-of date: 2026-05-08
- Primary model: `current_d4_mcw10_l5_lr005`
- Feature groups: `momentum_shape`
- Blend rule: `weights = (1 - alpha) * p1.4_weights + alpha * p3.0_weights`, then cap/renormalize.
- `alpha=0` is current p1.4 final; `alpha=1` is aggressive p3.0.

## Anchor Gates

| gate | AUC | selected anchors |
| --- | ---: | --- |
| 5x80 | 0.9512 | 2026-01-09, 2026-01-12, 2026-01-23, 2026-04-21, 2026-04-22 |
| 8x120 | 0.9512 | 2026-01-08, 2026-01-09, 2026-01-12, 2026-01-15, 2026-01-23, 2026-01-26, 2026-04-21, 2026-04-22 |
| recent40 | 0.9512 | 2026-04-14, 2026-04-20, 2026-04-21, 2026-04-22, 2026-04-24 |

## Combined Readout

| candidate | p3 alpha | broad avg excess | broad worst min | broad win | broad top10 | broad effective names | recent40 avg | recent40 min | recent40 top10 | recent40 effective names |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| p14_p30_blend_a1.00 | 1.00 | +1.142% | -3.149% | 0.78 | 65.72% | 18.6 | +4.549% | +3.372% | 85.18% | 12.4 |
| p14_p30_blend_a0.75 | 0.75 | +1.106% | -3.182% | 0.78 | 64.63% | 18.9 | +4.417% | +3.421% | 82.24% | 13.2 |
| p14_p30_blend_a0.50 | 0.50 | +1.071% | -3.215% | 0.78 | 63.55% | 19.1 | +4.286% | +3.199% | 79.32% | 13.9 |
| p14_p30_blend_a0.25 | 0.25 | +1.035% | -3.249% | 0.78 | 62.46% | 19.4 | +4.154% | +2.815% | 76.39% | 14.6 |
| p14_p30_blend_a0.00 | 0.00 | +1.000% | -3.282% | 0.78 | 61.37% | 19.6 | +4.023% | +2.432% | 73.46% | 15.2 |

## Per-Gate Summary

| gate | candidate | avg excess | max excess | min excess | win | top5 | top10 | effective names | rank1/rank30 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5x80 | p14_p30_blend_a1.00 | +1.585% | +6.592% | -3.149% | 0.80 | 41.95% | 70.21% | 17.0 | 3655.3 |
| 5x80 | p14_p30_blend_a0.75 | +1.542% | +6.358% | -3.182% | 0.80 | 41.57% | 68.87% | 17.3 | 148.2 |
| 5x80 | p14_p30_blend_a0.50 | +1.498% | +6.124% | -3.215% | 0.80 | 41.18% | 67.54% | 17.7 | 78.8 |
| 5x80 | p14_p30_blend_a0.25 | +1.454% | +5.890% | -3.249% | 0.80 | 40.80% | 66.21% | 18.0 | 54.1 |
| 5x80 | p14_p30_blend_a0.00 | +1.411% | +5.656% | -3.282% | 0.80 | 40.45% | 64.87% | 18.2 | 41.5 |
| 8x120 | p14_p30_blend_a1.00 | +0.698% | +6.592% | -3.149% | 0.75 | 35.47% | 61.24% | 20.2 | 3654.0 |
| 8x120 | p14_p30_blend_a0.75 | +0.671% | +6.358% | -3.182% | 0.75 | 35.23% | 60.39% | 20.4 | 126.4 |
| 8x120 | p14_p30_blend_a0.50 | +0.644% | +6.124% | -3.215% | 0.75 | 34.99% | 59.55% | 20.6 | 66.7 |
| 8x120 | p14_p30_blend_a0.25 | +0.617% | +5.890% | -3.249% | 0.75 | 34.74% | 58.71% | 20.8 | 45.8 |
| 8x120 | p14_p30_blend_a0.00 | +0.589% | +5.656% | -3.282% | 0.75 | 34.52% | 57.87% | 21.0 | 35.1 |
| recent40 | p14_p30_blend_a1.00 | +4.549% | +6.592% | +3.372% | 1.00 | 49.72% | 85.18% | 12.4 | 2880.5 |
| recent40 | p14_p30_blend_a0.75 | +4.417% | +6.358% | +3.421% | 1.00 | 49.01% | 82.24% | 13.2 | 209.1 |
| recent40 | p14_p30_blend_a0.50 | +4.286% | +6.124% | +3.199% | 1.00 | 48.30% | 79.32% | 13.9 | 111.1 |
| recent40 | p14_p30_blend_a0.25 | +4.154% | +5.890% | +2.815% | 1.00 | 47.60% | 76.39% | 14.6 | 75.8 |
| recent40 | p14_p30_blend_a0.00 | +4.023% | +5.656% | +2.432% | 1.00 | 46.92% | 73.46% | 15.2 | 57.5 |

## Takeaway

- Best broad-gate average in this blend sweep is `p14_p30_blend_a1.00` with broad avg +1.142% and broad worst min -3.149%.
- The p1.4 to p3.0 blend path is also monotonic on 5x80 and 8x120 in this test.
- Compared with p2.6, pure p3.0 slightly improves broad-gate average/worst-min but is a bit worse on recent40 minimum, so p3.0 is more aggressive rather than strictly dominant.