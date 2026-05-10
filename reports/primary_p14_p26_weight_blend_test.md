# Primary p1.4 / p2.6 Weight Blend Test

- Generated at: 2026-05-10 22:23:10
- As-of date: 2026-05-08
- Primary model: `current_d4_mcw10_l5_lr005`
- Feature groups: `momentum_shape`
- Blend rule: `weights = (1 - alpha) * p1.4_weights + alpha * p2.6_weights`, then cap/renormalize.
- `alpha=0` is current p1.4 final; `alpha=1` is aggressive p2.6.

## Combined Readout

| candidate | p2.6 alpha | broad avg excess | broad worst min | broad win | broad top10 | broad effective names | recent40 avg | recent40 min | recent40 top10 | recent40 effective names |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| p14_p26_blend_a1.00 | 1.00 | +1.125% | -3.184% | 0.78 | 64.94% | 18.8 | +4.510% | +3.486% | 83.45% | 12.8 |
| p14_p26_blend_a0.75 | 0.75 | +1.094% | -3.209% | 0.78 | 64.05% | 19.0 | +4.389% | +3.403% | 80.95% | 13.4 |
| p14_p26_blend_a0.50 | 0.50 | +1.063% | -3.233% | 0.78 | 63.16% | 19.2 | +4.267% | +3.080% | 78.45% | 14.0 |
| p14_p26_blend_a0.25 | 0.25 | +1.031% | -3.258% | 0.78 | 62.26% | 19.4 | +4.145% | +2.756% | 75.96% | 14.6 |
| p14_p26_blend_a0.00 | 0.00 | +1.000% | -3.282% | 0.78 | 61.37% | 19.6 | +4.023% | +2.432% | 73.46% | 15.2 |

## Per-Gate Summary

| gate | candidate | avg excess | max excess | min excess | win | top5 | top10 | effective names | rank1/rank30 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5x80 | p14_p26_blend_a1.00 | +1.565% | +6.412% | -3.184% | 0.80 | 41.80% | 69.25% | 17.2 | 1115.0 |
| 5x80 | p14_p26_blend_a0.75 | +1.526% | +6.223% | -3.209% | 0.80 | 41.46% | 68.15% | 17.5 | 136.8 |
| 5x80 | p14_p26_blend_a0.50 | +1.488% | +6.034% | -3.233% | 0.80 | 41.11% | 67.06% | 17.8 | 76.4 |
| 5x80 | p14_p26_blend_a0.25 | +1.449% | +5.845% | -3.258% | 0.80 | 40.77% | 65.97% | 18.0 | 53.5 |
| 5x80 | p14_p26_blend_a0.00 | +1.411% | +5.656% | -3.282% | 0.80 | 40.45% | 64.87% | 18.2 | 41.5 |
| 8x120 | p14_p26_blend_a1.00 | +0.685% | +6.412% | -3.184% | 0.75 | 35.38% | 60.64% | 20.3 | 1080.0 |
| 8x120 | p14_p26_blend_a0.75 | +0.661% | +6.223% | -3.209% | 0.75 | 35.16% | 59.95% | 20.5 | 117.8 |
| 8x120 | p14_p26_blend_a0.50 | +0.637% | +6.034% | -3.233% | 0.75 | 34.94% | 59.25% | 20.6 | 64.9 |
| 8x120 | p14_p26_blend_a0.25 | +0.613% | +5.845% | -3.258% | 0.75 | 34.72% | 58.56% | 20.8 | 45.4 |
| 8x120 | p14_p26_blend_a0.00 | +0.589% | +5.656% | -3.282% | 0.75 | 34.52% | 57.87% | 21.0 | 35.1 |
| recent40 | p14_p26_blend_a1.00 | +4.510% | +6.412% | +3.486% | 1.00 | 49.63% | 83.45% | 12.8 | 1062.8 |
| recent40 | p14_p26_blend_a0.75 | +4.389% | +6.223% | +3.403% | 1.00 | 48.93% | 80.95% | 13.4 | 189.3 |
| recent40 | p14_p26_blend_a0.50 | +4.267% | +6.034% | +3.080% | 1.00 | 48.23% | 78.45% | 14.0 | 107.0 |
| recent40 | p14_p26_blend_a0.25 | +4.145% | +5.845% | +2.756% | 1.00 | 47.56% | 75.96% | 14.6 | 74.8 |
| recent40 | p14_p26_blend_a0.00 | +4.023% | +5.656% | +2.432% | 1.00 | 46.92% | 73.46% | 15.2 | 57.5 |

## Takeaway

- Best broad-gate average in this blend sweep is `p14_p26_blend_a1.00` with broad avg +1.125% and broad worst min -3.184%.
- The blend path is monotonic in these gates: adding more p2.6 weight improves average and worst-window metrics, but also increases concentration.
- A 50/50 blend is a moderate compromise; alpha 0.75 captures most of p2.6 uplift while staying less concentrated than alpha 1.0.