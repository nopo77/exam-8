---
paper: holmes_&_casotto
chapter: 1
title: A Review of GLMs
topics: [glm_structure, link_functions, full_credibility_assumption, p_values, linear_predictor, offset]
key_formulas: [glm_likelihood_optimization, linear_predictor_equation]
---

> **TL;DR**
> - A GLM has three components: target distribution (exponential family), linear predictor η = Xβ, and monotonic link function g such that μ = g⁻¹(η).
> - Log link creates a multiplicative model: prediction = exp(β₀) × exp(β₁X₁) × … — ideal for rating tables where factors multiply.
> - The offset adds a fixed term to the linear predictor (e.g., prior relativities, deductibles) without estimating a coefficient; both offset and predictor variable must be included in lasso credibility.
> - GLM likelihood maximization forces β̂ⱼ = observed segment average regardless of exposure — this is the full credibility assumption (proven by setting the gradient of the log-likelihood to zero).
> - P-values provide only a binary include/exclude decision; they cannot assign partial credibility and are inappropriate after penalization is applied.

# 1. A Review of GLMs

Generalized linear models (GLMs) are a means of modeling the relationship between a variable whose outcome we wish to predict and one or more explanatory variables.

—Goldburd et al. (2016),  
*Generalized Linear Models for Insurance Rating*

In this chapter, we review the basics of GLMs to provide the minimum background necessary to introduce penalized regression and lasso credibility. First, we explore the linearity of GLMs. That foundation will help us demonstrate how to incorporate a complement of credibility into the GLM framework. Then, we describe the link function and give an example of how link functions allow a modeler to easily use a GLM's output as a multiplicative rating table. We revisit this example later in the paper to show how to implement the output of a lasso credibility model as an adjustment to an existing set of rating tables. Finally, we discuss the full credibility assumption of GLMs and how it allows for the use of  $p$ -values to evaluate coefficients. This prepares us for a discussion on how penalized regression does not assume full credibility, and therefore  $p$ -values are not appropriate in penalized regression and should be replaced by another type of model evaluation.

## 1.1. Definitions and Terminology

We begin with a short introduction to GLMs. For a comprehensive introduction, we refer the reader to Goldburd et al. (2016).

A GLM consists of three elements:<sup>2</sup>

1. A target variable  $Y$ , a random variable following a probability distribution from the exponential family, which is in turn defined by a selected variance function and dispersion parameter.
2. A linear predictor  $\eta = X\beta$ , where  $X$  is the design matrix and  $\beta$  is the coefficient vector.
3. A monotonic link function  $g$  such that  $E(Y) = \mu = g^{-1}(\eta)$ .

These elements have established connections to common insurance concepts.

$Y$  represents the random variable that models the risk and  $y_i$  represents the actual observed risk for row  $i$ . Depending on the nature of the risk, one makes different statistical

---

<sup>2</sup> The GLM definition is taken from Casualty Actuarial and Statistical (C) Task Force (2020) with some minor changes.

assumptions. For example, the actuary may model accident frequency via the Poisson probability distribution and accident severity via a gamma distribution.

The matrix  $X$  is such that its rows  $X_i$  contain the information about each record and any covariate relevant for predicting the considered risk. Typically,  $X_i$  represents a unit of risk specified by the modeler for each row  $i$ . For example, one exposure may represent a year of observation or a single policy. The columns of the matrix provide a numerical representation of the available information on the risk covariates. The values of the coefficients  $\beta$  define how the covariates are linearly combined to estimate the risk. Using  $X_i$  and  $\beta$ , we can represent the linear combination of the covariates as  $\eta_i = X_i\beta$ .

Finally,  $\mu_i$  represents the expected risk estimate for each row  $i$ . The linear combination of the features  $X_i\beta$  are related to the expected risk via the link function  $\mu_i = g^{-1}(X_i\beta)$ . In this notation, the intercept  $\beta_0$  is implicit. The specific choice of the link function depends on the target probability distribution chosen during modeling. For example, for Poisson and gamma distributions, the preferred link function is the logarithm, which gives a multiplicative model.

The process of building (or fitting) a GLM requires the specification of the target variable  $Y$  and its statistical assumptions together with the covariates  $X$ . The output of the fitting procedure is a set of coefficients  $\beta$  that maximizes the likelihood of observing  $Y$  with expected mean  $\mu_i$  and the assumed target distribution given the data  $X$ . This process of fitting coefficients based on the observed likelihood is at the core of why “GLMs effectively assume that the underlying datasets are 100% credible, no matter their size.” We now explore these elements a bit more deeply.

## 1.2. The Linear Predictor

GLMs are called generalized *linear* models because the relationship between the predictor variables  $X$  and the expected risk  $\mu_i$  is determined by the **linear** predictor  $\eta$ . The formula for this relationship is

$$\eta = \beta_0 + \beta_1 X_1 \dots \beta_n X_n = \beta_0 + X\beta. \quad (1.1)$$

For a change in each individual characteristic  $X_i$  (holding all other  $X$  constant), there is a linear change in the value of  $\eta$ . For instance, for each integer increase in  $X_1$ , the linear predictor  $\eta$  increases by the value of  $\beta_1$ . This is not to say that the prediction is always linear with respect to the underlying risk characteristic. For example, when using the predictor “age of vehicle squared,” the relationship will be linear with respect to “age of vehicle squared,” and therefore quadratic with respect to the risk characteristic “age of vehicle.” It is quite common to include multiple polynomial terms (linear, squared, cubed) in a model for a single risk characteristic. The creation of these variable transformations, often referred to as **feature engineering**, is an essential part of fitting a GLM. The creation and inclusion of polynomial terms is an example of feature engineering for a continuous variable. To encode categorical variables, one can introduce

dummy variables that take the values of either 1 or 0 to represent the presence or absence of a certain predictor value. This is referred to as one-hot encoding in the machine learning literature.

## 1.3. Distributions and Link Functions

The link function is the relationship between the linear predictor  $\eta$  in Equation 1.1 and the predicted value  $\mu$ . If we use no link function, then we are using  $\eta$  to directly predict  $\mu$ . By using the log link function, we can predict the log of  $\mu$  instead:

$$\ln(\mu) = \beta_0 + \beta_1 X_1 \dots \beta_n X_n,$$

or equivalently

$$\begin{aligned} \mu &= \exp(\beta_0 + \beta_1 X_1 \dots \beta_n X_n) \\ &= \exp(\beta_0) \times \exp(\beta_1 X_1) \times \dots \times \exp(\beta_n X_n). \end{aligned}$$

By using this link function, the modeled components are now combined multiplicatively to create a predicted expected value. This is ideal for actuarial pricing, as many rating plans are a combination of multiplicative rating tables. Additionally, the link function allows for the use of different error distributions.

Since the linear predictor  $\eta$  can potentially take any value, the correct choice of the link function is key in GLM modeling. The inverse of the link function determines the expected mean  $\mu$ —hence the link must be chosen such that  $\eta$  is mapped to the correct range of values. For example, for the gamma and Poisson distributions, the expected mean must be positive. Hence the log link is appropriate for those distributions as the inverse of the log link is the exponential function, which is always positive. To note another example, the mean of a binomial (logistic) variable must be between 0 and 1, and hence the logit is one of the appropriate link functions for the Bernoulli distribution, as its inverse, the logistic function, maps all values in the range from 0 to 1.

Table 1.1 shows some commonly used distributions and link functions for actuarial models. Other link functions may be used for some of these distributions, but the ones listed are the most common in actuarial applications (Goldburd et al. 2016).

**Table 1.1. Commonly Used Distributions in Actuarial Modeling**

| Model Type                        | Distribution               | Link  | Inverse Link |
|-----------------------------------|----------------------------|-------|--------------|
| Frequency                         | Poisson, negative binomial | Log   | Exp          |
| Severity                          | Gamma, inverse Gaussian    | Log   | Exp          |
| Pure premium                      | Tweedie                    | Log   | Exp          |
| Propensity, retention, conversion | Bernoulli                  | Logit | Logistic     |

## 1.4. The Offset

When building a model, we may want to consider the effect of risk characteristics without coming up with a prediction for them. Deductibles, for example, are best priced through a loss elimination ratio analysis rather than a GLM (Goldburd et al. 2016). Instead of modeling or ignoring these risk characteristics, they can be included as an **offset** in our GLM. The offset term is an additional item in our linear equation. Consider a GLM with a logarithmic link. The formula for the offset is given by

$$\ln(\mu) = \beta_0 + \beta_1 X_1 \dots \beta_n X_n + \text{offset}.$$

Assuming we are offsetting a deductible characteristic, the offset would be a column in our data set representing the coefficient for the surcharge or discount at the record's deductible level. A GLM will then directly include this coefficient in its prediction of  $\mu$  when fitting the optimal values of  $\beta$ . Multiple risk characteristics—e.g., deductible factors, increased limit factors, territory relativities, etc.—can be included in a single offset term.

## 1.5. Table-Based Output: An Example

Let's create a two-variable pricing model for home insurance as an example. We will use a Tweedie distribution and a log link to model pure premium directly. The first variable is the presence of a fire extinguisher, encoded as 1 without a fire extinguisher or 0 with a fire extinguisher. This 1 or 0 value would be represented by  $X_1$ . The second variable will be age of home, encoded as the integers 0–10. The appropriate integer per record would be represented as  $X_2$ :

$$\hat{\mu} = \exp(\beta_0) \times \exp(\beta_1 X_1) \times \exp(\beta_2 X_2).$$

Let's assume that our model fit these convenient values:

$$\beta_0 = \log_e(100) \approx 4.605$$

$$\beta_1 = \log_e(1.2) \approx 0.182$$

$$\beta_2 = \log_e(1.01) \approx 0.01$$

The predicted pure premium would then be calculated as follows:

$$\begin{aligned} \text{Pure premium} &= \exp(\beta_0) \times \exp(\beta_1 X_1) \times \exp(\beta_2 X_2) \\ &= \exp(4.6057) \times \exp(0.182 \times X_1) \times \exp(0.01 \times X_2) \\ &= 100 \times 1.2^{X_1} \times 1.01^{X_2}. \end{aligned}$$

We can represent this model in the following rating tables:  
 Base rate:  $\exp(4.6057) = 100$ .

| Fire Extinguishers | Factor                         |
|--------------------|--------------------------------|
| No                 | $\exp(0.182 \times 1) = 1.200$ |
| Yes                | $\exp(0.182 \times 0) = 1.000$ |

| Age of Home | Factor                         |
|-------------|--------------------------------|
| 0           | $\exp(0.01 \times 0) = 1.000$  |
| 1           | $\exp(0.01 \times 1) = 1.010$  |
| 2           | $\exp(0.01 \times 2) = 1.020$  |
| 3           | $\exp(0.01 \times 3) = 1.030$  |
| 4           | $\exp(0.01 \times 4) = 1.041$  |
| 5           | $\exp(0.01 \times 5) = 1.051$  |
| 6           | $\exp(0.01 \times 6) = 1.062$  |
| 7           | $\exp(0.01 \times 7) = 1.072$  |
| 8           | $\exp(0.01 \times 8) = 1.083$  |
| 9           | $\exp(0.01 \times 9) = 1.094$  |
| 10          | $\exp(0.01 \times 10) = 1.105$ |

This easy translation from beta coefficients to rating tables is one of the many reasons that GLMs have been used in actuarial pricing for quite some time.

## 1.6. Likelihood Optimization: Full Credibility Assumption

The full credibility assumption of GLMs is related to the optimization process used when fitting the model's  $\beta$  parameters. The procedure for computing the GLM parameters  $\beta$  is via the maximization of the log-likelihood (or equivalently, minimization of the negative of the log-likelihood) of observing  $y_i$  under the assumption that they follow the chosen error distribution with mean being  $\mu_i$ .

$$\begin{aligned}\hat{\beta}_{\text{GLM}} &= \operatorname{argmax}_{\beta} \operatorname{LogLikelihood}(y, X, \beta) \\ &= \operatorname{argmin}_{\beta} -\operatorname{LogLikelihood}(y, X, \beta).\end{aligned}\tag{1.2}$$

The maximization of likelihood alone will always treat the data as fully credible, and will not consider volatility in the estimates of  $\beta_p$  or the significance of the improvement each  $\beta_p$  might add to the overall model. In short, **GLM estimates are unstable on segments with low exposures.**

Section A.1 provides a motivation and proof for this statement. The implications of this behavior can be shown using our two-variable example model.

Assume that the likelihood maximization process determines that a surcharge of 20% is the “most likely” estimate of the true surcharge. The implications of this result may vary wildly depending on the data. We examine three scenarios where a single-variable GLM would output such a surcharge as the “most likely” estimate.

### Scenario 1: Credible and sound estimate

| Category                  | Exposures | Average Loss |
|---------------------------|-----------|--------------|
| With fire extinguisher    | 1,000,000 | 100          |
| Without fire extinguisher | 1,000,000 | 120          |

In this scenario, a  $\beta$  representing a 20% surcharge will be output as the most likely value of the surcharge. The estimate assigns full credibility to both categories in the data. An actuary would likely be confident in implementing this surcharge.

### Scenario 2: Midway estimate

| Category                  | Exposures | Average Loss |
|---------------------------|-----------|--------------|
| With fire extinguisher    | 1,000,000 | 100          |
| Without fire extinguisher | 5,000     | 120          |

In this scenario, a  $\beta$  representing a 20% surcharge will be output as the most likely value of the surcharge. The estimate assigns full credibility to both categories in the data. An actuary may believe that there is some signal to the true surcharge but may not be fully confident in the point estimate.

### Scenario 3: Noncredible estimate

| Category                  | Exposures | Average Loss |
|---------------------------|-----------|--------------|
| With fire extinguisher    | 1,000,000 | 100          |
| Without fire extinguisher | 10        | 120          |

In the third scenario, a  $\beta$  representing a 20% surcharge will be output as the most likely value of the true surcharge. The estimate, again, assigns full credibility to both categories in the data. But whereas a 20% surcharge is the “most likely” result given our limited data, we would not be fully confident in the estimate.

In a univariate analysis, an actuary might use a credibility procedure to determine the appropriate surcharge. However, in a multivariate setting, the question remains open because unpenalized GLMs do not incorporate credibility.

Although the modeler has no control over the **estimate** of the model, it is still possible to decide whether a factor needs to be included at all in the model.

That evaluation is binary due to the structure of a GLM: should we include this variable at full credibility, or should we exclude it entirely? The most common method of answering this question is the evaluation of  $p$ -values.

### 1.6.1. P-Values

In statistical hypothesis testing,  $p$ -values are a commonly used tool to accept or reject a null hypothesis against an alternative hypothesis. The aim of statistical hypothesis testing is to decide whether the data provides sufficient evidence against the null hypothesis, in which case this hypothesis is rejected in favor of the alternative hypothesis.  $P$ -values control the error of rejecting the null hypothesis when the null hypothesis is true and the experiment is repeated an infinite number of times. In GLM modeling we can apply this principle and use  $p$ -values to decide whether a given coefficient is significant. The null hypothesis being tested is then that a given coefficient's true value is zero or more extreme, i.e., the coefficient is not significant. Thus, the  **$p$ -value** of a coefficient represents the probability that a coefficient result at least as extreme as the estimate could have happened assuming that the null hypothesis (often assuming one parameter  $\beta_j$  is 0 or more extreme) is true.

When a coefficient's  $p$ -value is below 0.05, this means that there is less than a 5% chance that the observed results could have happened if the true value of the coefficient was zero and the experiment was repeated on different data an infinite number of times. In other words, the probability that the coefficient is due purely to randomness in the data is less than 5%.

A  $p$ -value of 0.05 is commonly used as a threshold for coefficient significance. When a coefficient's  $p$ -value is equal to or greater than the selected threshold, the coefficient is deemed **insignificant** and we cannot reject the null hypothesis that the true coefficient is zero. In this case, the coefficient is usually removed from a model. When a coefficient's  $p$ -value is less than 0.05, we reject the null hypothesis that the coefficient is zero and the coefficient is considered **significant**. When a coefficient is significant, it is included in the model and given full credibility.

$P$ -values and significance testing have several limitations:

1. Significance testing is a binary test that answers only the question "Is this coefficient likely not zero or more extreme?"
2. Although GLM output provides tools such as confidence intervals to evaluate coefficient stability, it does not provide statistical guidance on how to make corresponding adjustments. For example, when using a  $p$ -value threshold of 0.05, how should an actuary treat a coefficient with a  $p$ -value of 0.047? How much should an actuary trust the coefficient of a variable accepted by the actuarial and regulatory community as a predictor of loss that has a reasonable value and a  $p$ -value of 0.06? Such decisions are purely judgmental.
3. The traditional 0.05 level of significance is arbitrary. Numerous authors say that it is not an appropriate threshold for many studies (Wasserstein and Lazar 2016). Other scholars suggest that significance testing should be removed altogether.

4. Significance testing is iterative due to its post hoc application. The addition or removal of coefficients may affect the significance of other coefficients.
5. Nonbinary adjustments for questionable  $p$ -values must be made after modeling. *These actuarial selections are frequently made on a univariate basis and are therefore often suboptimal and contrary to the multivariate nature of a GLM's structure.*

Additional misconceptions and limitations are detailed in Greenland et al. (2016). Despite these downsides,  $p$ -values are widely used to evaluate GLM coefficients because they are a convenient and simple metric with which to perform significance testing. However, as we will later see,  $p$ -value significance testing is inappropriate (and in some cases not even possible) when using penalized regression. Penalized regression's ability to evaluate and adjust coefficients during the modeling process eliminates the need for post hoc significance testing.

### 1.6.2. Lack of Credibility in GLM Estimates

A consequence of the lack of credibility considerations during the fitting process is that a modeler must perform **post hoc** procedures on the coefficients of a model if one or more of the coefficients are unreasonable.

There are two kinds of post hoc analyses:

1. An analysis informing a subsequent model iteration
2. An analysis informing selections from final modeled coefficients

When the first post hoc analysis is incorporated back into the model, it must be a binary application. Either the coefficient should be included and receive full credibility or it should be excluded and receive no credibility—GLMs do not have another option. As described earlier,  $p$ -value significance testing is one appropriate methodology to arrive at this binary recommendation.

A common post hoc analysis that informs selections from final modeled coefficients is the credibility procedure. Unfortunately, such a credibility procedure must necessarily be done on a variable-by-variable basis as we are examining and adjusting one coefficient at a time. As we pointed out before, these adjustments may result in a suboptimal final model as they do not reflect the multivariate structure of the GLM.

To summarize, a coefficient can either (a) be assigned partial credibility during a post hoc univariate analysis or (b) receive full credibility or be removed during the multivariate fitting process. As we will see, penalization solves this dilemma by allowing a coefficient to be assigned partial credibility in a multivariate fitting procedure.

