---
paper: holmes_&_casotto
chapter: C
title: Miscellaneous
topics: [rebasing, near_aliasing, aic_bic, sparsity, best_subset_selection]
key_formulas: [aic_formula, bic_formula]
---

> **TL;DR**
> - Rebasing: adjust the intercept to change which category is the reference level post-modeling; predictions are unchanged but factor tables look different.
> - Near aliasing in GLMs causes coefficient instability when two variables nearly overlap; lasso penalization automatically handles this by penalizing the near-collinear pair.
> - AIC = 2·NLL + 2·(# parameters); BIC = 2·NLL + log(n)·(# parameters); both trade off training fit against model complexity as approximations to generalization error.
> - Lasso is the best convex (computationally tractable) approximation to the NP-hard "best subset selection" problem.
> - Lasso outperforms best subset selection in practice on typical insurance data due to lower variance from inherent coefficient shrinkage.

# Appendix C. Miscellaneous

## C.1. Rebasing Model Output

To make modeling output more interpretable and comparable, we often **rebase** the coefficients and factors by modifying the intercept, and we assume a log-link for this example. The term *coefficients* refers to the un-exponentiated betas produced by the model for a particular variable. The term *factors* refers to the exponentiated combination of coefficients with their corresponding  $X$  values. This post-modeling rebasing will have no effect on the scoring of the model as the rebasing factor may be incorporated into the intercept.

This is not to say that the selection of the base level during modeling is immaterial. The base level should still be selected to be the most statistically sound in penalized regression. For example, the optimal base level for a categorical variable should be the level with the highest level of exposure. After modeling, factors can be rebased to a selected base level for implementation and the base rate can be adjusted to achieve the desired rate level.

The tables below show an example of rebasing in a model using only one categorical variable with levels A, B, and C. The original base level is A, and we are rebasing to make level B the new base level.

| Category | Coefficient | Rebased Coefficient     | Factor          | Rebased Factor                  | Rebased Intercept         |
|----------|-------------|-------------------------|-----------------|---------------------------------|---------------------------|
| A        | 0           | $0 - (\beta_1)$         | 1.0             | $\exp(-\beta_1)$                | $\exp(\beta_0 + \beta_1)$ |
| B        | $\beta_1$   | $\beta_1 - \beta_1 = 0$ | $\exp(\beta_1)$ | $\exp(\beta_1 - \beta_1) = 1.0$ | $\exp(\beta_0 + \beta_1)$ |
| C        | $\beta_2$   | $(\beta_2 - \beta_1)$   | $\exp(\beta_2)$ | $\exp(\beta_2 - \beta_1)$       | $\exp(\beta_0 + \beta_1)$ |

| Category | Coefficient | Rebased Coefficient | Factor | Rebased Factor | Base Rate | Rebased Base Rate |
|----------|-------------|---------------------|--------|----------------|-----------|-------------------|
| A        | 0.0         | -.2                 | 1.0    | 0.819          | 100       | 122.1             |
| B        | .2          | 0                   | 1.221  | 1.0            | 100       | 122.1             |
| C        | .5          | .3                  | 1.549  | 1.340          | 100       | 122.1             |

The tables represent the mathematical transformations necessary to rebase the coefficient. In the model fit, category A was originally the base level, as highlighted by its 1.0 factor. In the rebased columns, such reference is changed to the factor B, which has a factor of 1.0 in the “Rebased Factor” column.

## C.2. Penalized Regression and Near Aliasing

Near aliasing can cause large instabilities in GLMs, but models using penalized regression do not exhibit such volatility. We can explain this through the lens of credibility. Take for example two indicator variables that overlap entirely except for a handful of characteristics. Those non-overlapping risks are implicitly being given full credibility by the GLM, as one indicator will increase drastically and the other will decrease until both segments are perfectly identified. This extremely high or low prediction for the small segment can greatly skew test statistics. When using lasso penalization, it is highly likely that one of the indicators will be highly penalized, and that the other will be included and will correctly account for the overlapping risks.

## C.3. Penalized Regression and the AIC

In the context of model selection in GLMs, the modeler may need to decide on one model between two alternatives. For example, such a comparison could be based on evaluating performances in a holdout, or testing, data set. Another way to compare models is not to use any testing set at all but instead use statistical theory to approximate the generalization power of a model using training data alone. This approach doesn't rely on new data sets to assess the generalization power of the model, avoiding the problems described above.

The Akaike information criterion, or AIC, is one of the most popular of such metrics, whose formula is

$$\text{AIC}(\beta) = 2\text{NLL}(\beta) + 2\{\# \text{ of degrees of freedom}\}.$$

Here, NLL represents the negative log-likelihood computed in the training data, and # of degrees of freedom represents the number of nonzero entries of the GLM coefficient  $\beta$ .

Given two different modeling alternatives, the modeler can compute the AIC for such models. Since the AIC formula “penalizes” the decrease of the NLL of the more complex model with the degrees of freedom (hence the complexity), the model with lower AIC should be preferred.

The curious reader may notice that the AIC formula looks similar to the penalized GLM Equation 3.1:

$$\hat{\beta} = \underset{\beta}{\text{argmin}} \text{NLL}(y, X, \beta) + \lambda \text{Penalty}(\beta).$$

Both formulas consider the trade-off between the goodness of fit (negative log-likelihood) and the complexity of the model (in the AIC, the number of degrees of freedom, in penalized regression, the penalty).

The connections between AIC and penalized GLM, with lasso in particular, are much more deep. First, we can define a penalized GLM version of the AIC, by just defining

$$\text{Penalty}(\boldsymbol{\beta}) = \# \text{ of degrees of freedom} = \# \text{ of nonzero entries of } \boldsymbol{\beta},$$

The solution of this problem is known as “best subset selection” problem. Many authors consider this the gold standard for building models: who would not compute the most performant GLM model given a “complexity” budget determined by the degrees of freedom? The model is not popular because it is proven to be numerically intractable. However, one can prove that the best “numerically tractable”<sup>10</sup> approximation to that problem is the lasso. The mathematically inclined reader can refer to Hastie, Tibshirani, and Tibshirani (2020) for a more in-depth discussion of this approximation result.

That paper also contains an unexpected result: lasso outperforms best subset selection in conditions characteristic of insurance data. This result may sound counter-intuitive, because from a theoretical perspective, best subset selection is superior to lasso. But this does not mean that it will perform better in practice for every (or even a typical) high-dimensional regression problem that we might want to solve. Best subset selection tends to have much higher variance than the lasso, because there is shrinkage inherent in the latter’s coefficient estimates. As a result, which estimator performs better in practice really depends on a lot of factors, such as the signal-to-noise ratio.

---

<sup>10</sup> A problem is considered numerically tractable if an optimization algorithm can provide its optimal solution in a reasonable time. This usually means that the problem is convex.

