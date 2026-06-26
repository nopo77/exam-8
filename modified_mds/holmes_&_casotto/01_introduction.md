---
paper: holmes_&_casotto
chapter: null
title: Introduction
topics: [glm_limitations, lasso_credibility, penalized_regression, complement_of_credibility, asop_25, p_values_vs_credibility]
key_formulas: []
---

> **TL;DR**
> - GLMs assume 100% credibility regardless of exposure, producing unstable coefficients for thin segments; penalized regression addresses this by adding a credibility component to the fitting process.
> - Lasso credibility reframes significance testing: p-values answer "is this non-zero?" whereas lasso asks "how much credibility should we give to this coefficient's deviation from the complement?"
> - An offset encodes the complement of credibility; penalization shrinks modeled deviations toward that complement rather than toward zero.
> - Using penalized regression as a credibility procedure brings ASOP 25 guidelines into scope; the penalty parameter λ serves as the credibility parameter.
> - Lasso credibility extends GLM modeling to smaller data sets and enables actuarially sound, multivariate partial credibility within the fitting process.

# Introduction

Predictive modeling has a number of operational applications in the insurance industry, and actuaries have access to a generous tool kit of modeling techniques to best address the various use cases. Among those modeling techniques, generalized linear models (GLMs) are a common choice for frequency, severity, and pure premium loss modeling.

The unpenalized GLM approach comes with one well-documented shortcoming: while minimum bias and univariate techniques can incorporate credibility in the calculation of indicated rating relativities, there has been no statistically straightforward, consistent way of incorporating actuarial credibility into a GLM. The Casualty Actuarial and Statistical (C) Task Force described this shortcoming as follows: “GLMs effectively assume that the underlying datasets are 100% credible, no matter their size. If some segments have little data, the resulting uncertainty would not be reflected in the GLM parameter estimates themselves (although it might be reflected in the standard errors, confidence intervals, etc.)” (2020, 4).

GLM output can warn a user of instability in a parameter estimate through a wide standard error, but it does not adjust the coefficient to take the large volatility into account. Instead, the practitioner may perform ad hoc adjustments to consider the lack of credibility or volatility in a specific segment. Post-modeling adjustments performed in this necessarily univariate manner may result in a suboptimal final rating plan.

Fortunately, this issue can be addressed by applying an enhanced version of a GLM: penalized regression. Penalized regression has similarities with credibility procedures as documented in Miller (2015) and Casotto, Banterle, and Beraud-Sudreau (2020). In this monograph we review GLMs and then introduce penalized regression and its connections to credibility. We describe the motivation for the technique as well as why lasso is our preferred penalization for actuarial analysis. Furthermore, we show how lasso penalization can be used as **lasso credibility** through a new use of the offset. We are not creating a new form of modeling from scratch, but rather combining existing tools to create an actuarially sound credibility procedure.

Using penalized regression for credibility has significant implications in actuarial analysis. With lasso credibility, the amount of data needed for predictive modeling is reduced. This means actuaries can use smaller data sets that might be insufficient for a stable GLM. Also, when we use lasso penalization as lasso credibility, the usage must now align with the guidelines of Actuarial Standard of Practice No. 25, *Credibility Procedures* (hereafter referred to as ASOP 25). We explain how the guidance in ASOP 25 applies to penalized regression as a credibility procedure.

This perspective shift to credibility should affect the way actuaries interpret and evaluate lasso credibility modeling results. For example, consider the question of whether one should include a specific factor, or variable, in a model. Modelers using a GLM may rely on a  $p$ -value analysis, which can provide a measure of whether the data is compatible with the absence of such a factor (the null hypothesis) (Wasserstein and Lazar 2016).

We show that whereas  $p$ -values answer the question of **significance**—*Is this significantly different than zero (or a more extreme value)?*—lasso penalized regression answers a question of **credibility**—*How much credibility, if any, should we give to this coefficient?* Lasso credibility answers a similar question—*How much credibility, if any, should we give to this coefficient's deviation from our complement?* By using lasso penalization or lasso credibility, an actuary can simultaneously evaluate the significance and magnitude of a coefficient, while an unpenalized GLM's  $p$ -values will evaluate only significance. Users of lasso credibility will need to let go of the idea of  $p$ -values and embrace a credibility interpretation of coefficients to correctly apply and evaluate the methodology. Furthermore, as we will see, the tuning of the penalty parameter (which acts as a credibility parameter) is both simpler and more robust than the examination of  $p$ -values.

The main body of the paper is written to provide a reader with the intuition behind penalized regression as a credibility procedure and practical guidance on how to implement lasso credibility. We provide a minimum necessary background for these approaches, reserving statistical proofs and rigorous defense of the concepts for a series of appendices. We hope that this structure allows the communication of these ideas to a broad audience without a lack of precision or loss of statistical rigor.

We supplement the guidance with a case study comparing lasso credibility, penalized regression, and traditional GLM models on data sets of varying size. The case study shows that lasso credibility can outperform both GLM and penalized regression when the model is informed by an adequate complement of credibility. This section has accompanying code on the CAS GitHub,<sup>1</sup> and we highly encourage readers to pull the code and run it alongside the case study. Additionally, we provide optional exercises to familiarize yourself with the behavior of lasso credibility in alternate scenarios.

---

<sup>1</sup> <https://github.com/casact/mg-credibility>

