---
paper: holmes_&_casotto
chapter: 2
title: A Brief Review of Credibility
topics: [classical_credibility, bühlmann_credibility, complement_of_credibility, credibility_factor]
key_formulas: [classical_credibility_z, bühlmann_credibility_z]
---

> **TL;DR**
> - Credibility formula: Estimate = Z × Observed Experience + (1 − Z) × Complement of Credibility, where 0 ≤ Z ≤ 1.
> - Classical credibility: Z = min(√(N / N_full), 1); reaches full credibility at N = N_full exposures (based on probability P and tolerance K).
> - Bühlmann credibility: Z = n / (n + k), where k = σ²_PV / τ²_HM (ratio of expected process variance to variance of hypothetical means).
> - Both types share the key property that Z increases with the number of observations and approaches 1 as n → ∞.
> - Multivariate credibility in GLMs requires three properties: no pure likelihood maximization, shrinkage toward a complement, and credibility weighting embedded in the fitting process — penalized regression satisfies all three.

# 2. A Brief Review of Credibility

Credibility, simply put, is the weighting together of different estimates to come up with a combined estimate.

—*Foundations of Casualty Actuarial Science*

In the context of ratemaking, credibility provides a framework with which to combine an estimate based on observed experience (observed losses, frequencies, or loss ratios), subject to volatility, with a more stable yet less individualized estimate—the complement of credibility. This combination aims to improve on both estimates to create better predictions of future values.

The estimates are blended together via the credibility factor, normally referred to as  $Z$ , a factor between 0 and 1 that will give more or less weight to the observed experienced or the complement of credibility:

$$\text{Estimate} = Z \times \text{Observed Experience} + (1 - Z) \times \text{Complement of Credibility.}$$

Two main types of credibility are found in the literature: **classical** and **Bühlmann**. Even if they differ in terms of the underlying hypothesis and formulation of the factor  $Z$  (see Table 2.1), they share the same basic credibility property: the credibility factor increases with the number of observations  $n$  (i.e., the exposure). In that sense, unlike simple GLMs, the credibility framework enables a user to incorporate information on the number of observations directly into the estimates.

## 2.1. Incorporation of Credibility into GLM Estimates

There are, of course, simplistic ways to adjust GLM estimates with these traditional credibility methodologies, but they all share the drawbacks highlighted in Klinker (2011): “Some actuaries have been known to apply an ad hoc credibility adjustment to coefficients output by a GLM. In some cases this even produces results similar to those arrived at by more statistically rigorous methods. If so, then what is so wrong with the ad hoc credibility adjustment of GLM output? . . . This gets back to the old issue that a sequence of steps, each optimal individually, may not be optimal in the aggregate” (1–2).

Table 2.1. Main Parameters of Classical and Bühlmann Credibility

| Classical Credibility                                                                                                                                                                                                | Bühlmann Credibility                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $Z = \min\left(\sqrt{\frac{N}{N_{full}}}, 1\right) \quad (2.1)$                                                                                                                                                      | $Z = \frac{n}{n+k} \quad (2.2)$                                                                                                                                                                                               |
| Additional parameters:<br>$N_{full} = N_{full}(K, P)$ — number observations to reach full credibility<br>$P$ — probability that the observations are within estimated risk<br>$K$ — tolerance to error, as % of risk | Additional parameters:<br>$k$ — ratio of $\sigma_{PV}^2/\tau_{HM}^2$ , with<br>$\sigma_{PV}^2$ — expected process variance (within class variance)<br>$\tau_{HM}^2$ — variance of hypothetical means (between class variance) |

Figure 2.1. Evolution of the credibility factor  $Z$  for a given estimate  $j$  as a function of the number of observations  $n$ . The  $Z$  for the classical credibility is computed using Equation 2.1 with  $N_{\text{full}} = 10,000$ . Bühlmann credibility uses  $k = 1,600$  in Equation 2.2.

![A line graph titled 'Credibility estimate variation' showing the evolution of the credibility factor Z as a function of the number of observations n. The x-axis is labeled 'Number of observations' and ranges from 0 to 14,000 with major ticks every 2,000. The y-axis is labeled 'Credibility factor Z' and ranges from 0.0 to 1.0 with major ticks every 0.2. Two curves are plotted: a green line for 'Classic' and a blue line for 'Bühlmann'. The green curve starts at (0,0) and rises to reach a horizontal dashed line at Z=1.0 when n=10,000. The blue curve also starts at (0,0) and rises more gradually, reaching approximately 0.9 at n=14,000. A legend in the bottom right corner identifies the curves.](c4c8cd9c58f395c25a2a2b217ca7c2fb_img.jpg)

Credibility estimate variation

| Number of observations (n) | Classic Credibility Factor (Z) | Bühlmann Credibility Factor (Z) |
|----------------------------|--------------------------------|---------------------------------|
| 0                          | 0.00                           | 0.00                            |
| 2,000                      | 0.40                           | 0.55                            |
| 4,000                      | 0.60                           | 0.70                            |
| 6,000                      | 0.75                           | 0.80                            |
| 8,000                      | 0.88                           | 0.85                            |
| 10,000                     | 1.00                           | 0.88                            |
| 12,000                     | 1.00                           | 0.90                            |
| 14,000                     | 1.00                           | 0.92                            |

A line graph titled 'Credibility estimate variation' showing the evolution of the credibility factor Z as a function of the number of observations n. The x-axis is labeled 'Number of observations' and ranges from 0 to 14,000 with major ticks every 2,000. The y-axis is labeled 'Credibility factor Z' and ranges from 0.0 to 1.0 with major ticks every 0.2. Two curves are plotted: a green line for 'Classic' and a blue line for 'Bühlmann'. The green curve starts at (0,0) and rises to reach a horizontal dashed line at Z=1.0 when n=10,000. The blue curve also starts at (0,0) and rises more gradually, reaching approximately 0.9 at n=14,000. A legend in the bottom right corner identifies the curves.

If the simplistic ways are insufficient, then how can we best incorporate credibility into model fitting? To obtain a statistically rigorous multivariate modeling technique that can incorporate credibility, at least three necessary properties must be satisfied:

1. The estimation of the parameters shall not rely on maximizing the log-likelihood (or variance) alone: any technique with this property will inevitably assign 100% credibility to the data.
2. Estimates will be shrunk toward the complement of credibility and the amount of shrinkage will depend on the number of observations.
3. To consider correlations, the “credibility weighting” of the coefficients must be a part of the fitting procedure, not a post-processing step on top of a GLM.

Penalized regression satisfies these three criteria when applied in a specific manner. Before we describe the application of penalized regression as credibility, we introduce penalized regression as a modeling technique and contrast it with a GLM.

