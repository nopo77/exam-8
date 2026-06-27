---
paper: holmes_&_casotto
chapter: A
title: Bayesian Interpretation of Credibility
topics: [bayesian_statistics, maximum_a_posteriori, ridge_bühlmann_equivalence, prior_distributions, full_credibility_assumption, laplace_prior]
key_formulas: [map_estimation_formula, bühlmann_estimate, ridge_solution, lasso_solution, posterior_distribution]
---

> **TL;DR**
> - Proof: GLM likelihood maximization forces β̂ⱼ = ȳⱼ (observed segment average) for every segment, regardless of exposure n — formal proof of the full credibility assumption.
> - Bayesian framework: penalized regression = MAP estimation; Penalty(β) = −log(p_prior(β)) — each penalty type corresponds to a specific prior distribution on β.
> - Ridge (L2) ↔ Normal prior N(0, τ²) on β; λ = σ²/τ² = Bühlmann k; under Gaussian assumptions, ridge regression and Bühlmann credibility produce identical estimates.
> - Lasso (L1) ↔ Laplace prior on β; the Laplace distribution has a sharper peak at zero than the normal, explaining why lasso sets small coefficients exactly to zero.
> - Bühlmann credibility is a special case of Bayesian estimation using conjugate distributions (Jewell 1974); penalized regression is the multivariate MAP generalization.

# Appendix A. Bayesian Interpretation of Credibility

In this appendix, we explain why a GLM offers full credibility and how penalized regression mathematically aligns with Bühlmann credibility. After illustrating their differences, we delve into penalized regression's relationships with Bayesian statistics.

## A.1. Why GLMs Give 100% Credibility to the Data

The statement “GLMs grant 100% credibility to the data” is a recurring theme in this monograph. To support it, we show that for all canonical link GLMs, predicted averages invariably match observed segment averages. The proof's essence lies in the computation of the GLM's parameter  $\beta$ , which minimizes the data's negative log-likelihood.

Setting the derivative (or gradient) to zero during likelihood maximization results in estimates where predicted averages coincide with observed segment averages, **independent of the underlying exposure**.

To introduce some mathematical notation, we start by considering an actuarial use case that consists of building estimates of loss costs for companies in a workers' compensation insurance rating plan. The modeler has access to a data set of historical loss experience, where each row represents the total loss observation for a specific company in a fixed 1-year period. Additionally, the class code describing the industry type is available for each company. There are several class codes and for most of them the number of observations is limited. An example of such a database is shown in Figure A.1.

The database contains  $n$  observations. The information on the companies is encoded in the matrix  $X$ , which provides the binary representation of the  $p$  class codes in the database. The coordinate  $x_{ij}$  of the matrix  $X$  will be 1 if company  $i$  belongs to class  $j$ , and 0 otherwise.  $X_i$  will denote the row vector of matrix  $X$  of size  $p$ . In general, index  $i$  will be used to represent a line in the matrix/database, and  $i$  takes values from 1 to  $n$ . The index  $j$  will be used to represent columns of the matrix, and  $j$  takes values from 1 to  $p$ .

$Y$  represents the vector of the observed losses, meaning that  $Y_i$  will represent the observed loss for company  $i$ . The grand average is given by  $\bar{Y} = \frac{1}{n} \sum_{i=1}^n Y_i$ .  $y$  represents the differences of the observed losses from the grand average  $\bar{Y}$ , that is,  $y_i = Y_i - \bar{Y}$  (so  $y$  is centered on zero).

**Figure A.1.** The purple line represents the behavior of the observed average loss deviation  $\bar{y}_j$  by class code  $j$  on synthetic data. The blue bars represent the total number of observations  $n_j$  by class code  $j$ .

![Figure A.1: A dual-axis plot showing Exposure (blue bars) and Observed average loss deviation (purple line) across class codes 0 to 7. The left y-axis represents Exposure (0 to 800) and the right y-axis represents Observed (0 to 4000).](a0ca2e895d28cff7c1bbb8e7bad3b0a1_img.jpg)

| Class Code ( $j$ ) | Exposure ( $n_j$ ) | Observed Average Loss Deviation ( $\bar{y}_j$ ) |
|--------------------|--------------------|-------------------------------------------------|
| 0                  | 150                | 3800                                            |
| 1                  | 780                | 1800                                            |
| 2                  | 180                | 2300                                            |
| 3                  | 370                | 3200                                            |
| 4                  | 400                | 2500                                            |
| 5                  | 450                | 1500                                            |
| 6                  | 180                | 100                                             |
| 7                  | 680                | 2600                                            |

Figure A.1: A dual-axis plot showing Exposure (blue bars) and Observed average loss deviation (purple line) across class codes 0 to 7. The left y-axis represents Exposure (0 to 800) and the right y-axis represents Observed (0 to 4000).

$n_j$  denotes the number of observations belonging to class  $j$ . The set  $J$  represents the set of rows  $i$  belonging to class  $j$ , that is,  $i$  such that  $x_{ij} = 1$ . This implies that the cardinality of  $J$  is  $n_j$ . The constant  $\bar{y}_j$  represents the observed average loss deviation by class code  $j$ , that is  $\frac{1}{n_j} \sum_{i \in J} y_i$ .

For this example, we'll fit a sample GLM with the following items as defined in Section 1.1:

- The distribution is a normal distribution with constant variance  $\sigma^2$ .
- The link is the identity (canonical link).
- The target is the vector  $y$  representing the differences of the observed losses  $Y$  from the grand average  $\bar{Y}$ .

The GLM coefficients  $\beta$  are estimated by maximizing the log-likelihood, or, equivalently, by minimizing the *negative* log-likelihood (NLL):

$$\begin{aligned} \hat{\beta} &= \operatorname{argmax}_{\beta} \operatorname{Loglikelihood}(y, X, \beta) \\ &= \operatorname{argmin}_{\beta} NLL(y, X, \beta), \end{aligned}$$

which in the case of a Gaussian distribution with an identity link becomes

$$\hat{\beta} = \operatorname{argmin}_{\beta} \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - X_i \beta)^2.$$

Since  $\sigma$  is constant, it doesn't affect the optimization problem, and we can ignore it. We can proceed to compute the gradient only of the summation, by differentiating with respect to each coefficient. This solution can then be found by setting the gradient to zero. The gradient can be simplified by application of the chain rule of the derivative:

$$\frac{\partial}{\partial \beta_j} \left[ \sum_{i=1}^n (y_i - X_i \beta)^2 \right] = \sum_{i=1}^n (X_i \beta - y_i) x_{ij}$$

We can further simplify the formula since the summand is not null only for  $i \in J$  since  $x_{ij} = 0$ . Otherwise

$$\sum_{i=1}^n (X_i \beta - y_i) x_{ij} = \sum_{i \in J} (X_i \beta - y_i)$$

Since for all  $i \in J$ ,  $X_i \beta = \beta_j$ ; the  $n_j \bar{y}_j$  term is by the definition of the average  $\bar{y}_j = \sum_{i \in J} y_i / n_j$ , the first addend  $n_j \beta_j$  appears and we obtain

$$\sum_{i \in J} (X_i \beta - y_i) = n_j \beta_j - \sum_{i \in J} y_i = n_j \beta_j - n_j \bar{y}_j$$

Setting the gradient to zero implies that

$$0 = n_j \beta_j - n_j \bar{y}_j \leftrightarrow \beta_j = \bar{y}_j.$$

This proves that the coefficients  $\beta_j$  maximizing the log-likelihood are exactly matching the average  $\bar{y}_j$  of each class.

**Figure A.2.** The green line compares the GLM estimates  $\hat{\beta}_j$  with the data as represented in Figure A.1. The observed (purple line) coincides with the GLM estimates (green line).

![Figure A.2: A dual-axis chart showing Exposure (blue bars) and GLM estimates (green line) across categories 0 to 7. The left y-axis represents Exposure (0 to 800), and the right y-axis represents Exposure (0 to 4000). The x-axis represents categories 0 to 7. The blue bars represent the observed exposure for each category. The green line represents the GLM estimates, which are calculated as the average of the observed exposure for each category. The purple line represents the observed exposure, which coincides with the GLM estimates.](d176e833609ef451e07edca3e58436b0_img.jpg)

| Category | Observed Exposure (Bar) | GLM Estimates (Line) |
|----------|-------------------------|----------------------|
| 0        | 150                     | 150                  |
| 1        | 780                     | 780                  |
| 2        | 180                     | 180                  |
| 3        | 380                     | 380                  |
| 4        | 410                     | 410                  |
| 5        | 460                     | 460                  |
| 6        | 180                     | 180                  |
| 7        | 3800                    | 3800                 |

Figure A.2: A dual-axis chart showing Exposure (blue bars) and GLM estimates (green line) across categories 0 to 7. The left y-axis represents Exposure (0 to 800), and the right y-axis represents Exposure (0 to 4000). The x-axis represents categories 0 to 7. The blue bars represent the observed exposure for each category. The green line represents the GLM estimates, which are calculated as the average of the observed exposure for each category. The purple line represents the observed exposure, which coincides with the GLM estimates.

This simple proof highlights two important features of generalized linear modeling:

- When modeling a single class in a binary encoding, a GLM will output the average of the observations for such a class. This is true as well for all distributions when the canonical link is used, and it can be proven equivalently by changing  $X_i\beta$  with  $\mu_i = g^{-1}(X_i\beta)$  as in Ohlsson and Johansson (2010).
- The formula applies as well on multivariate settings. Whenever a discrete variable is added in a binary format, the coefficients will be estimated so that the average of the predictions  $X_i\beta$  on every level  $j$  will match the average of the observations, **regardless of the underlying exposure.**

In this sense, **any fitting procedure** that computes estimates by maximizing the likelihood of the data (or minimizing the deviance) **alone**, *effectively assumes that the underlying data sets are 100% credible, no matter their size.*

## A.2. Credibility: A Bayesian Interpretation

Maximizing likelihood doesn't inherently blend credibility into both the model's factors and estimates. To address that, we must reconsider how a model interprets and estimates data.

Using the maximum likelihood formula to compute GLMs is characteristic of the "frequentist" statistical approach. We propose complementing this with a "Bayesian" perspective. "The Bayesian and classical versions have a lot in common, but they have a philosophical difference in that in classical statistics parameters are constants, but for Bayesians they have distributions" (Venter n.d., x).

Before modeling with GLM, two assumptions are essential. First, a probabilistic description of the observed response must be established, defining the data-generating distribution. Second, a link function should be selected to depict the relationship between the linear predictor (comprising parameters and covariates) and the target.

Once those are set, the parameters are estimated by maximizing the likelihood over the data. Such a maximization will try to replicate the observed data as closely as possible, giving 100% credibility to the data.

From a statistical perspective, this happens because the frequentist approach to modeling assumes that there exists a fixed set of true coefficients: the observed values of the target are assumed to have been generated assuming these fixed coefficients and the hypothesis assumed above. Our best guess is thus the set of coefficients maximizing the probability of observing the actual values of the target, motivating a maximum likelihood approach.

In a Bayesian perspective, on top of the standard hypothesis done over the observations, a distributional assumption is made on the coefficients of the model themselves (called **the prior distribution**). This assumption describes our a priori knowledge of and uncertainty over the values of the coefficients (hence the name), which are now random variables, and allows for the inclusion of some additional structure on the coefficients' estimates.

Bühlmann credibility can be considered from both a Bayesian and a frequentist point of view (Tse 2009).

The Bayesian equivalence has been proved by Jewell (1974): for all data-generating distributions used in GLMs, one can find an appropriate prior distribution such that the resulting Bayesian estimation coincides with the estimator obtained via Bühlmann credibility.

Jewell's result shows that for a given statistical hypothesis on the target, there exists a certain prior distribution for the coefficient  $\beta$  (called **conjugate**) that will return the Bühlmann estimator.

Jewell's result allows us to put Bühlmann credibility into the much more generic framework of Bayesian statistics. Under the Bayesian perspective, the connection with penalized regression will be evident.

To see how that connection works in practice, it is helpful to apply Jewell's result to the workers' compensation use case. The goal is to show that a Bayesian model with proper priors returns the exact same estimates as the Bühlmann credibility formula.

As a reminder, the Bühlmann credibility estimator is given by

$$\hat{\beta}_j = \frac{n_j}{n_j + k} \bar{y}_j,$$

where  $k = \frac{\sigma^2}{\tau^2}$  is the ratio between the within-class variance and the between-class variance (see Table 2.1).

The initial assumption in the workers' compensation use case was that the loss deviations  $y$  are normally distributed around the estimations, that is,  $y_i \sim N(X_i\beta, \sigma^2)$ . The conjugate of the normal distribution with known variance is the normal distribution itself. For this reason we'll suppose that a priori  $\beta$  itself follows a normal distribution with constant variance  $\tau^2$  and mean zero:  $\beta \sim N(0, \tau^2)$ .

The choice of the normal **a priori** on  $\beta \sim N(0, \tau^2)$  can be motivated as well by pragmatic considerations: deviations of class code losses from the grand average should be centered around zero. Furthermore, large deviations from the grand average should be

**Table A.1. Pairings of statistical assumptions with their corresponding conjugate distribution for commonly used GLMs. Gamma ( $\alpha$ ) refers to a gamma distribution with known parameter  $\alpha$ .**

| Statistical Assumption        | Conjugate Distribution       |
|-------------------------------|------------------------------|
| $y \sim \text{Gaussian}$      | $\beta \sim \text{Gaussian}$ |
| $y \sim \text{Poisson}$       | $\beta \sim \text{Gamma}$    |
| $y \sim \text{Gamma}(\alpha)$ | $\beta \sim \text{Gamma}$    |
| $y \sim \text{Binomial}$      | $\beta \sim \text{Beta}$     |

considered a priori as less likely than minor deviations. In this sense, **the priors allow us to formalize commonsense intuitions in a robust mathematical framework.**

To define a Bayesian estimator for this model, it is necessary to derive the so-called *posterior* distribution, which updates through the likelihood (through the data) our *a priori* belief about the unknown parameter (the  $\beta$  should not deviate too much from zero, the mean). This update (by Bayes' theorem) takes the form of

$$p_{\text{posterior}}(\beta | y, X) = \frac{1}{K} \times p(y | \hat{y}(X, \beta)) \times p_{\text{prior}}(\beta),$$

where  $K$  is a constant that doesn't depend on  $\beta$ .

Under these specific assumptions of normality (see Section A.5 for more information), the solution can be computed via the maximum a posteriori formula:

$$\begin{aligned} \hat{\beta} &= \operatorname{argmax}_{\beta} p(y | \hat{y}(X)) \times p_{\text{prior}}(\beta) \\ &= \operatorname{argmin}_{\beta} \text{NLL}(y, X, \beta) - \log(p_{\text{prior}}(\beta)). \end{aligned}$$

The first summand is, for the workers' compensation use case, given by the same formula optimized by a GLM, that is,

$$\text{NLL}(y, X, \beta) = \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - X_i \beta)^2.$$

The second summand, since  $\beta \sim N(0, \tau^2)$ , is equal to

$$-\log(p_{\text{prior}}(\beta)) = \frac{1}{2\tau^2} \sum_{j=1}^p \beta_j^2 + C,$$

where  $C$  is a constant that does not depend on  $\beta$ , and can be removed from the optimization problem, which becomes

$$\begin{aligned} \hat{\beta} &= \operatorname{argmin}_{\beta} \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - X_i \beta)^2 + \frac{1}{2\tau^2} \sum_{j=1}^p \beta_j^2 \\ &= \operatorname{argmin}_{\beta} \frac{1}{2} \sum_{i=1}^n (y_i - X_i \beta)^2 + \frac{\sigma^2}{2\tau^2} \sum_{j=1}^p \beta_j^2. \end{aligned} \tag{A.1}$$

Formula in Equation A.1 shows as well that the Bayesian estimates' optimization formula is equal to that of ridge regression with  $\lambda = \frac{\sigma^2}{\tau^2}$ . Furthermore, by the Jewell theorem, we already know that the optimal solution is equal to the Bühlmann estimates, with  $k = \frac{\sigma^2}{\tau^2}$ .

## A.3. Penalized Regression: A Bayesian Interpretation

The equivalence of ridge estimates to this specific use case isn't accidental. As Miller (2015) demonstrated, every penalized regression can be framed as a Bayesian model, rooted in the maximum a posteriori (MAP) formula:

$$\begin{aligned}\hat{\beta} &= \operatorname{argmax}_{\beta} p(y | \hat{y}(X)) \times p_{\text{prior}}(\beta) \\ &= \operatorname{argmin}_{\beta} \text{NLL}(y, X, \beta) - \log(p_{\text{prior}}(\beta)).\end{aligned}\quad (\text{A.2})$$

There is a one-to-one correspondence between prior distribution (prior assumption on the coefficients)  $p_{\text{prior}}$  and penalties:

$$\text{Penalty}(\beta) = -\log(p_{\text{prior}}(\beta)). \quad (\text{A.3})$$

We just showed how the ridge penalty corresponds to a normal prior on the coefficients with  $\lambda = \frac{\sigma^2}{\tau^2}$ . Furthermore, under the hypothesis of the workers' compensation use case, **ridge regression and Bühlmann credibility are equivalent** with  $k = \lambda$ .

In the case of the lasso, the associated prior is the Laplace distribution.

For context, the Laplace random variable with mean  $\mu = 0$  and scale  $\gamma$  has the distribution

$$f_{\text{Laplace}(0, \gamma)}(x) = \frac{1}{2\gamma} \exp\left(-\frac{|x|}{\gamma}\right).$$

Figure A.3 compares the Gaussian and Laplace distribution.

Replacing Equation A.3 with the prior assumption that  $\beta \sim \text{Laplace}(0, \gamma)$ , then

$$-\log(p_{\text{prior}}(\beta)) = \frac{1}{\gamma} |\beta_j| + C,$$

where  $C$  is a constant independent on  $\beta$ , which is ignored when computing a MAP estimator. The formula is equal to the lasso penalty with  $\lambda = 1/\gamma$ .

The formulas highlight a strong connection between Bayesian and penalized regression modeling:

1. Bayesian modeling offers a general framework with which to model the uncertainty of the estimation  $\beta$  when the number of observations is limited. This uncertainty translates into a choice of a **prior** hypothesis on the coefficients  $\beta$ , i.e, a certain distribution that the coefficients  $\beta$  are assumed to follow.

**Figure A.3. Comparison of Densities of Both the Normal/Ridge Prior and the Laplace/Lasso Prior**

![Figure A.3: Prior distributions of Penalized Regression. The plot shows two probability density functions centered at 0. The x-axis ranges from -3 to 3, and the y-axis ranges from 0.0 to 0.5. The green curve, labeled 'Normal / Ridge', is a smooth bell-shaped curve peaking at approximately 0.4. The blue curve, labeled 'Laplace / Lasso', is a sharper V-shaped curve peaking at 0.5. The Laplace distribution has a higher peak and thinner tails than the Normal distribution.](f2306ba11f0b23027f8e52d2c69ea95f_img.jpg)

Figure A.3: Prior distributions of Penalized Regression. The plot shows two probability density functions centered at 0. The x-axis ranges from -3 to 3, and the y-axis ranges from 0.0 to 0.5. The green curve, labeled 'Normal / Ridge', is a smooth bell-shaped curve peaking at approximately 0.4. The blue curve, labeled 'Laplace / Lasso', is a sharper V-shaped curve peaking at 0.5. The Laplace distribution has a higher peak and thinner tails than the Normal distribution.

2. The estimator of the Bayesian model can be found by maximizing the posteriori log-likelihood  $p_{\text{posterior}}(\beta | y, X)$ . When taking the logarithm, its structure decomposes naturally into two terms: the log-likelihood (equal to the GLM formula) and the log-probability of the prior (which acts as a penalty).
3. Bühlmann credibility is an instance of a specific Bayesian model where the error distribution and the prior are conjugates (Table A.1). The choice of conjugate distributions allows us to compute the estimates in an explicit form. Explicit formulas were required due to the lack of computational tools, which are now available to everyone. Overcoming this bottleneck allows us today to both choose a range of more appropriate priors and to easily adapt the credibility framework to a multivariate setting via penalized regression.

## A.4. Practical Comparison

Ridge and lasso, viewed as credibility methodologies, can benefit from a comparison with other credibility methods. We consider two comparison scenarios:

1. Increasing underlying exposures and fixed observed average
2. Increasing underlying average and fixed exposures

### A.4.1. Comparison with Increasing Exposures (Fixed Observed Average)

A meaningful comparison can be given by showing how the credibility estimates evolve as the underlying amount of exposures increases. Figure A.4 displays the evolution

**Figure A.4.** Plot of the estimates  $\hat{\beta}$  with  $\bar{y} = 5$  and the number of observations varying. Parameters for each model were as follows: classical credibility  $N_{full} = 1,082$ , Bühlmann  $k = 1,600$ , ridge  $\lambda_{Ridge} = 1/k$ , lasso  $\lambda_{Lasso} = 4,000$ . The formulas used to compute the estimates for the use case can be found in the relative section in the paper. The parameters were chosen arbitrarily to best display the differences of trend. Depending on the parameters, the curve would more or less be similar.

![Figure A.4: Credibility estimate variation. A line graph showing the estimated coefficient β̂ versus the number of observations. The y-axis is labeled 'Estimated coefficient β̂' and has a dashed line at ȳ. The x-axis is labeled 'Number of observations' and ranges from 0 to 14,000. Four curves are shown: Buhlmann - Ridge (blue), Lasso (orange), Classic (green), and GLM (dashed black). The Classic curve rises sharply from the origin and reaches ȳ at approximately 1,000 observations. The Lasso curve starts at zero, remains at zero until about 1,000 observations, then rises and approaches ȳ. The Buhlmann - Ridge curve rises more gradually from the origin and approaches ȳ. The GLM curve is a horizontal dashed line at ȳ.](58084970bdd0e711a061181d8e1ea328_img.jpg)

Figure A.4: Credibility estimate variation. A line graph showing the estimated coefficient β̂ versus the number of observations. The y-axis is labeled 'Estimated coefficient β̂' and has a dashed line at ȳ. The x-axis is labeled 'Number of observations' and ranges from 0 to 14,000. Four curves are shown: Buhlmann - Ridge (blue), Lasso (orange), Classic (green), and GLM (dashed black). The Classic curve rises sharply from the origin and reaches ȳ at approximately 1,000 observations. The Lasso curve starts at zero, remains at zero until about 1,000 observations, then rises and approaches ȳ. The Buhlmann - Ridge curve rises more gradually from the origin and approaches ȳ. The GLM curve is a horizontal dashed line at ȳ.

of the estimates of an effect with an increasing number of observations (e.g., an increasing number of observations for a specific class code of workers' compensation risks) when the average  $\bar{y}$  for such effect is kept fixed.

The behavior of the lasso is different from the others, as it exhibits a minimum amount of observations (here  $\lambda_{Lasso}/\bar{y}$ ) for which the recorded experience does not influence the estimates  $\hat{\beta}$  and the predictions are equal to the complement of credibility. This can be seen as equivalent to considering a specific level of significance to include a variable in a GLM. The choice of including or excluding a specific level in a GLM may be based upon the result of a statistic ( $p$ -value) that will depend, among others, on the number of observations. If the statistic is below a certain threshold (e.g., 5% for  $p$ -values), then the factor will be included in the modeling, giving an underlying 100% credibility. The lasso regression leads to similar results, but it allows interpolation between 0 and full credibility instead of a binary split (a yes-or-no decision).

When the number of observations is above the lasso's threshold, experience gains weight onto the final estimate much faster than in the ridge/Bühlmann estimates.

The visualization in Figure A.4 shows, in a univariate example, how the signal is interpolated from the complement of credibility to the observed data by credibility

and penalized regression. It also shows how both frameworks can be derived from a Bayesian prior hypothesis on the coefficients' distribution, demonstrating how the penalized regression approach extends GLMs by integrating credibility in a multi-variate context.

### A.4.2. Comparison with an Increasing Observed Average (Fixed Exposure)

We now focus on comparing the estimates of GLM, ridge, and lasso when the number of observations are fixed but the observed average effect  $\bar{y}$  changes. This toy example is helpful as it provides a sense of how these methodologies “learn” from the observed data.

First, we need to compute the estimates of each of the methodologies, i.e., the values of  $\beta_j$  as a function of  $\bar{y}_j$ .

#### GLM Solution

Because a **GLM** gives 100% credibility to the data,

$$\beta_{\text{GLM},j} = \bar{y}_j.$$

#### Ridge Solution

To compute the **ridge** estimate, we need to solve for  $\hat{\beta}$ :

$$\hat{\beta}_{\text{Ridge}} = \underset{\beta}{\operatorname{argmin}} \frac{1}{2} \sum_{i=1}^n (y_i - X\beta)^2 + \frac{\lambda}{2} \sum_{j=1}^p \beta_j^2.$$

This solution can be found by means of computing the gradient and setting it to zero, similarly to the GLM. The solution is given by the vector that sets the gradient to zero, that is,

$$\hat{\beta}_{\text{Ridge},j} = \frac{n_j}{n_j + \lambda} \bar{y}_j.$$

The addition of the penalty term effectively “shrinks” the observed estimates  $\bar{y}_j$  by a number that is dependent on the number of observations of the segment in question.

#### Lasso Solution

The same procedure should be applied to the **lasso**, which solves the formula

$$\hat{\beta}_{\text{Lasso}} = \underset{\beta}{\operatorname{argmin}} \frac{1}{2} \sum_{i=1}^n (y_i - X\beta)^2 + \lambda \sum_{j=1}^p |\beta_j|.$$

We prove in Section D.1 that

$$\hat{\beta}_{\text{Lasso},j} = \begin{cases} \bar{y}_j - \frac{\lambda}{n_j} & \text{if } \bar{y}_j > \frac{\lambda}{n_j} \\ \bar{y}_j + \frac{\lambda}{n_j} & \text{if } \bar{y}_j < -\frac{\lambda}{n_j} \\ 0 & \text{otherwise.} \end{cases}$$

Whenever the quantity  $n_j \bar{y}_j = \bar{y}_i < \lambda$ , the coefficient for the class  $j$  will be set equal to zero, hence assigning no credibility to the data if the quantity of signal is not relevant enough. Appendix D explores in depth the modeling consequences of the structure of the lasso solution.

### A.4.3. Final Comparison

Figure A.5 displays how the different estimates  $\beta_j$  differ in the workers' compensation use case for fixed  $\lambda$ ,  $n_j$ .

**Figure A.5.** Plot of the correspondence between observed value  $\bar{y}_j$  with estimates  $\hat{\beta}_j$  for GLM and penalized regression. For GLMs, the dashed line represents the identity function. For the ridge, the relationship is linear, by a factor of  $\frac{n_j}{n_j + \lambda}$ . For the lasso, the relationship is piecewise linear.

![A line graph comparing three regression models: Ridge, Lasso, and GLM. The x-axis is 'Observed value y_j' ranging from -3 to 3. The y-axis is 'Estimated coefficient beta_j' ranging from -3 to 3. The GLM (dashed black line) is the identity function y=x. The Ridge (solid blue line) is a linear function with a slope less than 1, passing through the origin. The Lasso (solid orange line) is piecewise linear, staying at zero for |y_j| <= 1 and following the identity function for |y_j| > 1.](da82c28f91abb7e03beec3535b711ab7_img.jpg)

Comparison of  $\hat{\beta}$  estimates

| Observed value $\bar{y}_j$ | Ridge $\hat{\beta}_j$ | Lasso $\hat{\beta}_j$ | GLM $\hat{\beta}_j$ |
|----------------------------|-----------------------|-----------------------|---------------------|
| -3                         | -1.5                  | -2.5                  | -3                  |
| -2                         | -1                    | -1                    | -2                  |
| -1                         | -0.5                  | 0                     | -1                  |
| 0                          | 0                     | 0                     | 0                   |
| 1                          | 0.5                   | 0                     | 1                   |
| 2                          | 1                     | 1                     | 2                   |
| 3                          | 1.5                   | 2.5                   | 3                   |

A line graph comparing three regression models: Ridge, Lasso, and GLM. The x-axis is 'Observed value y\_j' ranging from -3 to 3. The y-axis is 'Estimated coefficient beta\_j' ranging from -3 to 3. The GLM (dashed black line) is the identity function y=x. The Ridge (solid blue line) is a linear function with a slope less than 1, passing through the origin. The Lasso (solid orange line) is piecewise linear, staying at zero for |y\_j| <= 1 and following the identity function for |y\_j| > 1.

Compared to the GLM estimates ( $\hat{\beta}_j = \bar{y}_j$ ), the lasso reduces the coefficient by a factor  $\lambda/n_j$  accordingly to the sign of  $\bar{y}_j$ . If the value of  $\bar{y}_j$  is lower than such a threshold, then such value is set to zero.

Compared to the ridge estimates ( $\hat{\beta}_j = \frac{n_j}{n_j + \lambda} \bar{y}_j$ ), the lasso shrinks high values of the observed  $\bar{y}_j$  to a lesser degree (since lasso penalty grows linearly with the coefficients, and ridge quadratically), but does the opposite for small values of the observed (setting them to exactly zero).

## A.5. Degrees of “Bayesian-ness”

We showed that Bühlmann credibility and ridge regression coincide when we do compute the Bayesian estimates via the maximum a posteriori, or MAP, formula. The MAP formula is not the only way to compute the estimates of Bayesian models—there are various other ways to do it.

As mentioned earlier, Bayesian statistics treats parameters as distributions themselves (the “posterior” distribution), and in general, penalized regression provides as prediction the mode of such estimators. Another typical estimator could be the posterior mean, and it can be proven to coincide with the mode in the case of the Bühlmann Gaussian example mentioned in the previous sections.

Ideally, we would be interested in computing the whole posterior distribution of the parameters  $\beta$ , but outside of a limited number of convenient combinations of likelihoods and relative conjugate priors, the posterior distribution might not be known analytically. Inference can quickly become intricate when delving into details. For instance, while we set prior distributions for the parameter  $\beta$ , those priors (like the normal distribution) depend on additional parameters, such as the standard deviation  $\sigma$ . In Bayesian statistics, these metaparameters might have their own prior assumptions. To maintain practicality, various approximations are available to modelers based on desired complexity. As Murphy (2012) illustrated, a hierarchy can be constructed where the more integrals executed, the “more Bayesian” the approach becomes (Table A.2).

The hierarchy serves as a guide through various actuarial methodologies that incorporate Bayesian statistics to varying extents. GLMs are based on the maximum likelihood method, while penalized regressions are MAP estimates of Bayesian models.

**Table A.2. From Murphy (2012)**

| Method                  | Definition                                                                                                                               |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Maximum likelihood      | $\hat{\theta} = \operatorname{argmax}_{\theta} p(D \theta)$                                                                              |
| MAP estimation          | $\hat{\theta} = \operatorname{argmax}_{\theta} p(D \theta)p(\theta \eta)$                                                                |
| ML-II (empirical Bayes) | $\hat{\eta} = \operatorname{argmax}_{\eta} \int p(D \theta)p(\theta \eta)d\theta = \operatorname{argmax}_{\eta} p(D \eta)$               |
| MAP-II                  | $\hat{\eta} = \operatorname{argmax}_{\eta} \int p(D \theta)p(\theta \eta)p(\eta)d\theta = \operatorname{argmax}_{\eta} p(D \eta)p(\eta)$ |
| Full Bayes              | $p(\theta, \eta D) \propto p(D \theta)p(\theta \eta)p(\eta)$                                                                             |

Generalized linear mixed models, which are examples of empirical Bayes estimates, were popularized in the actuarial realm by Klinker (2011). In practice, GLMMs share many similarities with ridge penalized regression. Both use Gaussian priors  $\beta \sim \mathcal{N}(0, \sigma^2)$  and yield shrunk parameter estimates for  $\beta$ . Full Bayes models, on the other hand, necessitate specialized coding languages or Bayesian tools like Stan.

It's worth noting that the sparsity lasso introduces applies to maximum posterior estimates and doesn't necessarily extend to entire distributions.

Concluding this section on Bayesian interpretation, it's essential to recognize that there is no single best approach. Each method has its merits depending on the use case. While more Bayesian models might excel in certain scenarios, our monograph's purpose is to introduce sophistication to address practical challenges within our statistical methodology.

GLMs, widely accepted and comprehended within the actuarial community, have set a foundation. Penalized regressions, however, emerge as a natural progression from GLMs. They not only introduce a touch of Bayesian thinking, such as prior assumptions and the complement of credibility, but also bridge the gap between traditional statistical methods and machine learning techniques. This intersection with Bayesian statistics offers a pragmatic balance, especially considering that penalized regressions require tuning just a single parameter.

In the authors' view, this blend of simplicity and sophistication makes penalized regression an invaluable tool, serving as a practical introduction to more advanced Bayesian concepts within the standard approach.

