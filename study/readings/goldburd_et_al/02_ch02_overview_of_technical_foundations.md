---
paper: goldburd_et_al
chapter: 2
title: "2. Overview of Technical Foundations"
topics: [exponential_family_distributions, link_function, dispersion_parameter, variance_function, tweedie_distribution, logistic_regression, overdispersion, multicollinearity]
key_formulas: [glm_linear_predictor, exponential_family_variance, tweedie_compound_poisson_gamma, logit_link_function]
---
> **TL;DR**
> - g(μᵢ) = β₀ + β₁x₁ + … + βₚxₚ; log link → multiplicative structure; exponentiated coefficients are rating factors
> - Variance = φV(μ): Normal V=1, Poisson V=μ, Gamma V=μ², Inv. Gaussian V=μ³, Tweedie V=μᵖ; φ is constant across all risks
> - Tweedie with p ∈ (1,2) models pure premium as a compound Poisson-gamma; typical p ≈ 1.5–1.8
> - Categorical base level choice affects significance statistics; choose a populous level to maximize confidence in comparisons
> - Offsets fix known factors (e.g., deductible, territory) with coefficient = 1; must be on linear predictor scale (log for log-link)
> - VIF > 10 signals multicollinearity; aliased (perfectly correlated) predictors cause non-convergence

# 2. Overview of Technical Foundations

**Generalized linear models** (GLMs) are a means of modeling the relationship between a variable whose outcome we wish to predict and one or more explanatory variables.

The predicted variable is called the **target variable** and is denoted  $y$ . In property/casualty insurance ratemaking applications, the target variable is typically one of the following:

- Claim frequency (i.e., claims per exposure)
- Claim severity (i.e., dollars of loss per claim or occurrence)
- Pure premium (i.e., dollars of loss per exposure)
- Loss ratio (i.e., dollars of loss per dollar of premium)

For quantitative target variables such as those above, the GLM will produce an estimate of the *expected value* of the outcome.

For other applications, the target variable may be the occurrence or non-occurrence of a certain event. Examples include:

- Whether or not a policyholder will renew their policy.
- Whether a submitted claim contains fraud.

For such variables, a GLM can be applied to estimate the *probability* that the event will occur.

The explanatory variables, or **predictors**, are denoted  $x_1 \dots x_p$ , where  $p$  is the number of predictors in the model. Potential predictors are typically any policy terms or policyholder characteristics that an insurer may wish to include in a rating plan. Some examples are:

- Type of vehicle, age, or marital status for personal auto insurance.
- Construction type, building age, or amount of insurance (AOI) for homeowners insurance.

## 2.1. The Components of the GLM

In a GLM, the outcome of the target variable is assumed to be driven by both a *systematic* component as well as a *random* component.

The **systematic component** refers to that portion of the variation in the outcomes that is related to the values of the predictors. For example, we may believe that driver age influences the expected claim frequency for a personal auto policy. If driver age

is included as a predictor in a frequency model, that effect is part of the systematic component.

The **random component** is the portion of the outcome driven by causes *other than* the predictors in our model. This includes the “pure randomness”—that is, the part driven by circumstances unpredictable even in theory—as well as that which may be predictable with additional variables that are not in our model. As an example of this last point, consider the effect of driver age, which we describe above as being part of the systematic component—if driver age is in the model. If driver age is *not* included in our model (either due to lack of data or for any other reason), then, from our perspective, its effect forms part of the random component.

In a general sense, our goal in modeling with GLMs is to “explain” as much of the variability in the outcome as we can using our predictors. In other words, we aim to shift as much of the variability as possible away from the random component and into the systematic component.

GLMs make explicit assumptions about both the random component and the systematic component. We will examine each in turn, beginning with the random component.

### 2.1.1. The Random Component: The Exponential Family

In a GLM,  $y$ —the target variable—is modeled as a random variable that follows a probability distribution. That distribution is assumed to be a member of the **exponential family** of distributions.

The exponential family is a class of distributions that have certain properties that are useful in fitting GLMs. It includes many well-known distributions, such as the normal, Poisson, gamma and binomial distributions. (It also includes a less widely known distribution—the Tweedie distribution—that is very useful in modeling insurance data; more on that later.) Selection and specification of the distribution is an important part of the model building process.

The randomness of the outcome of any particular risk (denoted  $y_i$ ) may be formally expressed as follows:

$$y_i \sim \text{Exponential}(\mu_i, \phi) \quad (1)$$

Note that “*Exponential*” above does not refer to a specific distribution; rather, it is a placeholder for any member of the exponential family. The terms inside the parentheses refer to a common trait shared by all the distributions of the family: each member takes two parameters,  $\mu$  and  $\phi$ , where  $\mu$  is the mean of the distribution.  $\phi$ , the **dispersion** parameter, is related to the variance (but is not the variance!) and is discussed later in this chapter.

The parameter  $\mu$  is of special interest: as the mean of the distribution, it represents the expected value of the outcome. The estimate of this parameter is said to be the “prediction” generated by the model—that is, the model’s ultimate output.

If no information about each record other than the outcome were available, the best estimate of  $\mu$  would be the same for each record—that is, the average of historical outcomes. However, GLMs allow us to use predictor variables to produce a better estimate, unique to each risk, based on the statistical relationships between the predictors and the target values in the historical data. Note the subscript  $i$  applied to  $\mu$  in Equation 1 above, which denotes that the  $\mu$  parameter in the distribution is record-specific. The subscript-less parameter  $\phi$ , on the other hand, is assumed to be the same for all records.

### 2.1.2. The Systematic Component

GLMs model the relationship between  $\mu_i$  (the model prediction) and the predictors as follows:

$$g(\mu_i) = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip}. \quad (2)$$

Equation 2 states that some specified *transformation* of  $\mu_i$  (denoted  $g(\mu_i)$ ) is equal to the **intercept** (denoted  $\beta_0$ ) plus a linear combination of the predictors and the **coefficients**, which are denoted  $\beta_1 \dots \beta_p$ . The values for the intercept ( $\beta_0$ ) and the coefficients ( $\beta_1 \dots \beta_p$ ) are estimated by GLM software. The transformation of  $\mu_i$  represented by the function  $g(\cdot)$  on the left-hand side of Equation 2 is called the **link function** and is specified by the user.

The right-hand side of Equation 2 is called the **linear predictor**; when calculated, it yields the value  $g(\mu_i)$ —that is, the model prediction transformed by our specified link function. Of course, the value  $g(\mu_i)$  per se is of little interest; our primary interest lies in the value of  $\mu_i$  itself. As such, after calculating the linear predictor, the model prediction is derived by applying the *inverse* of the function represented by  $g(\cdot)$  to the result.

The link function  $g(\cdot)$  serves to provide flexibility in relating the model prediction to the predictors: rather than requiring the mean of the target variable to be directly equal to the linear predictor, GLMs allow for a transformed value of the mean to be equal to it. However, the prediction must ultimately be driven by a linear combination of the predictors (hence the “linear” in “generalized linear model.”)

In a general sense, the flexibility afforded by the ability to use a link function is a good thing because it gives us more options in specifying a model, thereby providing greater opportunity to construct a model that best reflects reality. However, when using GLMs to produce insurance rating plans, an added benefit is obtained when the link function is specified to be the natural log function (i.e.,  $g(x) = \ln(x)$ ): a GLM with that specification (called a **log link** GLM) has the property of producing a multiplicative rating structure.

Here’s why: when a log link is specified, Equation 2 becomes

$$\ln \mu_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip}.$$

To derive  $\mu_i$ , the inverse of the natural log function, or the natural exponential function, is applied to both sides of the equation:

$$\mu_i = \exp(\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip}) = e^{\beta_0} \times e^{\beta_1 x_{i1}} \times \cdots \times e^{\beta_p x_{ip}}.$$

As demonstrated, the use of a log link results in the linear predictor—which begins as a series of additive terms—transforming into a series of multiplicative factors when deriving the model prediction.

Multiplicative models are the most common type of rating structure used for pricing insurance, due to a number of advantages they have over other structures. To name a few:

- They are simple and practical to implement.
- Having additive terms in a model can result in negative premiums, which doesn't make sense. With a multiplicative plan you guarantee positive premium without having to implement clunky patches like minimum premium rules.
- A multiplicative model has more intuitive appeal. It doesn't make much sense to say that having a violation should increase your auto premium by \$500, regardless of whether your base premium is \$1,000 or \$10,000. Rather it makes more sense to say that the surcharge for having a violation is 10%.

For these and other reasons, log link models, which produce multiplicative structures, are usually the most natural model for insurance risk.

### 2.1.3. An Example

Suppose we construct a GLM to predict the severity of auto claims using driver age and marital status as predictors. The data we use contains 972 rows, with each row corresponding to a single claim. For each claim, the loss amount is recorded, along with several policyholder characteristics, among which are our predictors: driver age (in years, and denoted  $x_1$  in our example) and marital status (coded as 0 = unmarried, 1 = married, and denoted  $x_2$ ). We aim to produce a multiplicative rating algorithm, so a log link is used. We believe that the loss amount generated by a claim, after accounting for the effect of age and marital status, is random and follows a gamma distribution.

For this setup, our model inputs are:

- The data
- The model specifications:
  - *Target variable:* loss amount
  - *Predictors:* driver age ( $x_1$ ) and marital status ( $x_2$ )
  - *Link function:* log
  - *Distribution:* gamma

The above are entered into the GLM fitting software. The outputs of the model fitting process are: estimates for the intercept, the two coefficients (for age and marital status), and the dispersion parameter ( $\phi$ ).

Suppose the software returns the following:

| <i>Parameter</i>                              | <i>coefficient</i> |
|-----------------------------------------------|--------------------|
| Intercept ( $\beta_0$ ):                      | 5.8                |
| Coefficient for driver age ( $\beta_1$ ):     | 0.1                |
| Coefficient for marital status ( $\beta_2$ ): | -0.15              |
| Dispersion parameter ( $\phi$ ):              | 0.3                |

We then wish to use this information to predict average claim severity for a 25-year-old married driver. We use Equation 2, plugging in the following values:  $\beta_0 = 5.8$ ,  $\beta_1 = 0.1$ ,  $\beta_2 = -0.15$ ,  $x_1 = 25$ , and  $x_2 = 1$ . We solve for  $\mu_i$ , which represents average claim severity for this driver as indicated by the model. Per Equation 2,

$$g(\mu_i) = \ln \mu_i = 5.8 + (0.1)25 + (-0.15)1 = 8.15 \rightarrow \mu_i = \mathbf{3,463.38}$$

Thus, the model predicts the loss amount for a claim from this class of driver to follow a gamma distribution with parameters  $\mu = 3,463.38$  and  $\phi = 0.3$ . The value 3,463.38 is the mean, or the expected severity for this driver; that figure may then be multiplied by an estimate of frequency to derive an expected pure premium which would underlie the rate charged for that class of driver.

Equivalently, the model prediction can be represented as a series of multiplicative rating factors by exponentiating both sides of the equation above:

$$\begin{aligned}\mu_i &= \exp[5.8 + (0.1)25 + (-0.15)1] = e^{5.8} \times e^{0.1(25)} \times e^{-0.15(1)} \\ &= 330.30 \times 12.182 \times 0.861 = \mathbf{3,464.42}\end{aligned}$$

which is similar to the result above. (The difference is due to rounding.)

The advantage of this last formulation is that it can be easily translated as a simple rating algorithm: begin with a “base” average severity of \$330.30, and apply the factors applicable to driver age 25 and married drivers (12.182 and 0.861, respectively), to arrive at the expected severity for this particular class of driver: \$3,464.

We might also use this model to predict mean severity for a 35-year-old unmarried driver; that prediction is  $\exp[5.8 + (0.1)35 + (-0.15)0] = 10,938$ , meaning the loss amount follows a gamma distribution with parameters  $\mu = 10,938$  and  $\phi = 0.3$ . Note that the  $\phi$  parameter is the same as for the first driver in our example, since  $\phi$  is constant for all risks in a GLM.

In this simple example, the specifications of the model—the distribution, the target variable and predictors to include—are given. In the real world, such decisions are often not straightforward. They are continually refined over many iterations of the model building process, and require a delicate balance of art and science.<sup>1</sup> The tools and concepts

<sup>1</sup> As for the link function, it is usually the case that the desirability of a multiplicative rating plan trumps all other considerations, so the log link is almost always used. One notable exception is where the target variable is binary (i.e., occurrence or non-occurrence of an event), for which a special link function must be used, as discussed later in this chapter.

**Table 1. The Exponential Family Variance Functions**

| Distribution                   | Variance Function [ $V(\mu)$ ] | Variance [ $\phi V(\mu)$ ] |
|--------------------------------|--------------------------------|----------------------------|
| normal                         | 1                              | $\phi$                     |
| Poisson                        | $\mu$                          | $\phi\mu$                  |
| gamma                          | $\mu^2$                        | $\phi\mu^2$                |
| inverse Gaussian               | $\mu^3$                        | $\phi\mu^3$                |
| negative binomial <sup>2</sup> | $\mu(1+\kappa\mu)$             | $\phi\mu(1+\kappa\mu)$     |
| binomial                       | $\mu(1-\mu)$                   | $\phi\mu(1-\mu)$           |
| Tweedie                        | $\mu^p$                        | $\phi\mu^p$                |

that help guide proper model specification and selection for the purpose of building an optimal rating plan are the primary focus of this monograph.

## 2.2. Exponential Family Variance

The particulars of the exponential family of distributions are complex, and most are not important from the viewpoint of the practitioner and will not be covered in this monograph. [For a fuller treatment, see Clark and Thayer (2004).] However, it is necessary to understand the first two central moments of this family of distributions and how they relate to the parameters.

**Mean.** As noted above, the mean of every exponential family distribution is  $\mu$ .

**Variance.** The variance is of the following form:

$$Var[y] = \phi V(\mu) \quad (3)$$

That is, the variance is equal to  $\phi$  (the dispersion parameter) times some function of  $\mu$ , denoted  $V(\mu)$ . The function  $V(\mu)$  is called the **variance function**, and its actual definition depends on the specific distribution being used. Table 1 shows the variance functions for several of the exponential family distributions.

As shown in Table 1, for the normal distribution, the function  $V(\mu)$  is a constant, and so the variance does not depend on  $\mu$ . For all other distributions, however,  $V(\mu)$  is a function of  $\mu$ , and in most cases it is an increasing function. This is a desirable property in modeling insurance data, as we expect that higher-risk insureds (in GLM-speak, insureds with higher values of  $\mu$ ) would also have higher variance. Recall that a constraint of GLMs that we need to live with is that the  $\phi$  parameter must be a

<sup>2</sup> Note that for the negative binomial distribution, the dispersion parameter  $\phi$  is restricted to be 1. As such, although this table shows expressions for both the variance function and the variance (for the sake of completeness), they are in fact equivalent.

constant value for all risks. Thanks to the variance function of the exponential family, however, this doesn't mean the *variance* must be constant for all risks; our expectation of increasing variance with increasing risk can still be reflected in a GLM.

To illustrate this last point, recall our previous example, where we predicted the average severities for two drivers using the same model, with the predictions being \$3,464 and \$10,938. In both cases, the  $\phi$  parameter was held constant at 0.3. Following Equation 3 and the gamma entry for  $V(\mu)$  in Table 1, we can calculate the variance in loss amount for the first driver as  $0.3 \times 3,464^2 = 3.6 \times 10^6$ , while the second driver has a variance of  $0.3 \times 10,938^2 = 35.9 \times 10^6$ . Thus the higher-risk driver has a higher variance than the lower-risk driver (an intuitive assumption) despite the restriction of constant  $\phi$ .

The third column in Table 1 reminds the reader that the variance function is *not* the variance. To get the actual variance, one must multiply the variance function by the estimated  $\phi$ , which in effect serves to scale the variance for all risks by some constant amount.

## 2.3. Variable Significance

For each predictor specified in the model, the GLM software will return an estimate of its coefficient. However, it is important to recognize that those estimates are just that—estimates, and are themselves the result of a random process, since they were derived from data with random outcomes. If a different set of data were used, with all the same underlying characteristics but with different outcomes, the resulting estimated coefficients would be different.

An important question for each predictor then becomes: is the estimate of the coefficient reasonably close to the “true” coefficient? And, perhaps more importantly: does the predictor have *any* effect on the outcome at all? Or, is it the case that the predictor has no effect—that is, the “true” coefficient is zero, and the (non-zero) coefficient returned by the model-fitting procedure is merely the result of pure chance?

Standard GLM software provides several statistics for each coefficient to help answer those questions, among which are the *standard error*, *p-value*, and *confidence interval*.

### 2.3.1. Standard Error

As described above, the estimated coefficient is the result of a random process. The **standard error** is the estimated standard deviation of that random process. For example, a standard error of 0.15 assigned to a coefficient estimate may be thought of as follows: if this process—collecting a dataset of this size (with the same underlying characteristics but different outcomes) and putting it through the GLM software with the same specifications—were replicated many times, the standard deviation of the resulting estimates of the coefficient for this predictor would be approximately 0.15.

A small standard deviation indicates that the estimated coefficient is expected to be close to the “true” coefficient, giving us more confidence in the estimate. On the other hand, a large standard deviation tells us that a wide range of estimates could be achieved through randomness, making it less likely that the estimate we got is close to the true value.

Generally, larger datasets will produce estimates with smaller standard errors than smaller datasets. This is intuitive, as more data allows us to “see” patterns more clearly.

The standard error is also related to the estimated value of  $\phi$ : the larger the estimate of  $\phi$ , the larger the standard errors will be. This is because a larger  $\phi$  implies more variance in the randomness of the outcomes, which creates more “noise” to obscure the “signal,” resulting in larger standard errors.

### 2.3.2. *p*-value

A statistic closely related to the standard error (and indeed derived from the standard error) is the ***p*-value**. For a given coefficient estimate, the *p*-value is an estimate of the probability of a value of that magnitude (or higher) arising by pure chance.

For example, suppose a certain variable in our model yields a coefficient of 1.5 with a *p*-value of 0.0012. This indicates that, if this variable’s true coefficient is zero, the probability of getting a coefficient of 1.5 or higher purely by chance is 0.0012.<sup>3</sup> In this case, it may be reasonable to conclude: since the odds of such a result arising by pure chance is small, it is therefore likely that the result reflects a real underlying effect—that is, the true coefficient is not zero. Such a variable is said to be **significant**.

On the other hand, if the *p*-value is, say, 0.52, it means that this variable—even if it has no effect—is much more likely to yield a coefficient of 1.5 or higher by chance; as such, we have no evidence from the model output that it has any effect at all. Note that this is not to say that we *have* evidence that it has *no* effect—it may be that the effect is actually there, but we would need a larger dataset to “see” it through our GLM.

Tests of significance are usually framed in terms of the **null hypothesis**—that is, the hypothesis that the true value of the variable in question is zero. For a *p*-value sufficiently small, we can reject the null hypothesis—that is, accept that the variable has a non-zero effect on the expected outcome. A common statistical rule of thumb is to reject the null hypothesis where the *p*-value is 0.05 or lower. However, while this value may seem small, note that it allows for a 1-in-20 chance of a variable being accepted as significant when it is not. Since in a typical insurance modeling project we are testing many variables, this threshold may be too high to protect against the possibility of spurious effects making it into the model.

### 2.3.3. Confidence Interval

As noted above, the *p*-value is used to guide our decision to accept or reject the hypothesis that the true coefficient is zero; if the *p*-value is sufficiently small, we reject it.

---

<sup>3</sup> It is perhaps worth clarifying here what is meant by “the probability of getting a coefficient of 1.5 or higher.” Certainly, there is no randomness in the GLM fitting process; for any given set of data and model specifications, the GLM will produce the same result every time it is run, and so the probability of getting the coefficient of 1.5 with *this* data is 100%. However, recall that the estimates produced are random because they are derived from a dataset with random outcomes. Thus, the interpretation of the *p*-value may be stated as: *if* the true coefficient is zero—that is, the variable has no correlation with the outcome—there is a 0.0012 probability of the random outcomes in the data being realized in such a way that if the resultant dataset is entered into a GLM the estimated coefficient for this variable would be 1.5 or higher.

However, a hypothesis of zero is just one of many hypotheses that could conceivably be formulated and tested; we could just as easily hypothesize any other value and test against it, and the  $p$ -value would be inversely related to the degree to which the estimated coefficient differs from our hypothesized coefficient. It is then natural to ask: what *range* of values, if hypothesized, would *not* be rejected at our chosen  $p$ -value threshold? This range is called the **confidence interval**, and can be thought of as a reasonable range of estimates for the coefficient.

Confidence intervals are typically described by the complement of the  $p$ -value threshold used to compute them, expressed as a percentage. E.g., the confidence interval based on a  $p$ -value threshold of 0.05 is called the 95% confidence interval. SAS and other GLM software typically return the 95% confidence interval by default but provide the option to return a confidence interval for any chosen  $p$ -value threshold.

As an example: suppose, for a particular predictor, the GLM software returns a coefficient of 0.48, with a  $p$ -value of 0.00056 and a 95% confidence interval of [0.17, 0.79]. In this case, the low  $p$ -value indicates that the null hypothesis can be rejected. However, all values in the range 0.17 to 0.79 are sufficiently close to 0.48 such that, if set as initial hypotheses, the data would produce  $p$ -values of 0.05 or higher. Assuming that we are comfortable with a threshold of  $p = 0.05$  for accept/reject decisions, hypotheses of values in that range would not be rejected, and so that range could be deemed to be a reasonable range of estimates.

## 2.4. Types of Predictor Variables

Predictor variables that go into a GLM are classified as being either *categorical* or *continuous*, and each of those types of variable is given a different treatment.

A **continuous variable** is a numeric variable that represents a measurement on a continuous scale. Examples include age, amount of insurance (in dollars), and population density.

A **categorical variable** is a variable that takes on one of two or more possible values, thereby assigning each risk to a “category.” A categorical variable may be numeric or non-numeric. Examples are: vehicle primary use (one of either “commute” or “pleasure”); vehicle type (one of “sedan,” “SUV,” “truck,” or “van”); or territory (a value from 1 to 8, representing the territory number). The distinct values that a categorical value may take on are called **levels**.

### 2.4.1. Treatment of Continuous Variables

The treatment of continuous variables in a GLM is straightforward: each continuous variable is input into the GLM as-is, and the GLM outputs a single coefficient for it. This results in the linear predictor holding a direct linear relationship with the value of the predictor: for each unit increase in the predictor, the linear predictor rises by the value of the coefficient (or declines, in the case of a negative coefficient). If a log link was used, this in turn results in the predicted value increasing or decreasing by some constant percentage for each unit increase in the predictor.

**Logging Continuous Variables.** When a log link is used, it is often appropriate to take the natural logs of continuous predictors before including them in the model, rather than placing them in the model in their original forms. This allows the scale of the predictors to match the scale of the entity they are linearly predicting, which in the case of a log link is the log of the mean of the outcome.

When a logged continuous predictor is placed in a log link model, the resulting coefficient becomes a *power transform* of the original variable. To see this mathematically, consider the simple case of a model with only an intercept term and a single continuous predictor  $x$ . Applying a log link, and logging predictor  $x$ , Equation 2 becomes:

$$\ln \mu = \beta_0 + \beta_1 \ln x$$

To derive  $\mu$ , we exponentiate both sides:

$$\mu = e^{\beta_0} \times e^{\beta_1 \ln x} = e^{\beta_0} \times x^{\beta_1}$$

As demonstrated, when deriving the prediction, the coefficient  $\beta_1$  becomes an exponent applied to the original variable  $x$ . To make this example more concrete, suppose  $x$  represents amount of insurance (AOI) in thousands of dollars; we log AOI and place it into a log link model, and the resulting coefficient is 0.62. We can use this information to derive a relativity factor for any AOI relative to a “base” AOI by raising the AOI to a power of 0.62 and dividing that by the base AOI raised to that same power. If our base AOI is \$100,000, the indicated relativity for \$200,000 of AOI is  $200^{0.62}/100^{0.62} = 1.54$ —in other words, a property with \$200,000 of AOI has an expected outcome 54% higher than that of a property with \$100,000 of AOI.

Including continuous predictors in their logged form allows a log link GLM flexibility in fitting the appropriate response curve. Some examples of the indicated response curves for different positive values of the coefficient are shown in the left panel of Figure 1. If the variable holds a direct linear relationship with the response, the estimated coefficient will

**Figure 1.** Indicated Response Curve for Logged Continuous Variable (*left*) and Unlogged Continuous Variable (*right*)

![Figure 1 consists of two side-by-side line graphs. The left graph shows response curves for a logged continuous variable with x-axis values from 1000 to 5000 and y-axis values from 1 to 5. It contains three lines: a solid line for beta = 1.0, a dashed line for beta = 0.6, and a dotted line for beta = 1.2. The right graph shows response curves for an unlogged continuous variable with the same axes. It contains three lines: a solid line for beta = 0.0005, a dashed line for beta = 0.0003, and a dotted line for beta = 0.0065. In both graphs, the curves start at (1000, 1) and increase as x increases, with higher beta values resulting in steeper curves.](f0cab3794e09131ff0a91cabe163ca16_img.jpg)

Figure 1 consists of two side-by-side line graphs. The left graph shows response curves for a logged continuous variable with x-axis values from 1000 to 5000 and y-axis values from 1 to 5. It contains three lines: a solid line for beta = 1.0, a dashed line for beta = 0.6, and a dotted line for beta = 1.2. The right graph shows response curves for an unlogged continuous variable with the same axes. It contains three lines: a solid line for beta = 0.0005, a dashed line for beta = 0.0003, and a dotted line for beta = 0.0065. In both graphs, the curves start at (1000, 1) and increase as x increases, with higher beta values resulting in steeper curves.

be near 1.0 (solid line). A coefficient between 0 and 1 (such as the 0.6 coefficient illustrated by the dashed line) would indicate that the mean response increases with the value of the predictor, but at a decreasing rate; this shape is often appropriate for predictors in insurance models. A coefficient greater than 1—such as 1.2, the dotted line—will yield a curve that increases at a mildly increasing rate. (Negative coefficients would yield response curves that decrease at a decreasing rate.)

On the other hand, if the variable  $x$  is not logged, the response curve for any positive coefficient will always have the same basic shape: exponential growth, that is, increasing at an increasing rate. The right panel of Figure 1 illustrates the kinds of fits that might be produced for variables similar to those in the left panel if the variable  $x$  were not logged. As can be seen, a direct linear relationship (the gray line) is no longer an option. Only an exponential growth curve can be achieved; the magnitude of the growth varies with the coefficient. To be sure, there may be some instances where such a shape may be warranted; for example, if  $x$  is a temporal variable (such as year) meant to pick up trend effects, it may be desirable for  $x$  to yield an exponential growth relationship with the response, as trend is often modeled as an exponential function. In general, though, rather than viewing logging as a *transformation* of a continuous variable, it is often useful to consider the logged form of a variable the “natural” state of a predictor in a log link model, with the original (unlogged) variable viewed as a “transformation” that should only be used in certain specific cases.

Note that this suggestion is not due to any statistical law, but rather it is a rule of thumb specific to the context of insurance modeling, and is based on our *a priori* expectation as to the relationship between losses and the continuous predictors typically found in insurance models. For some variables, logging may not be feasible or practical. For example, variables that contain negative or zero values cannot be logged without a prior transformation. Also, for “artificial” continuous variables (such as credit scores) we may not have any *a priori* expectation as to whether the natural form or the logged form would better capture the loss response.

Also note that when including a logged continuous variable in a log link model, the underlying assumption is that the logged variable yields a linear relationship with the logged mean of the outcome. Certainly, there are many instances of predictors for which such will not be the case. An example is the effect of driver age on expected auto pure premium, which is typically at its highest for teen drivers and declines as drivers mature into their twenties and thirties, but rises again as the drivers enter their senior years. Regardless of whether the original variable has been logged or not, it is crucial to test the assumption of linearity and make adjustments where appropriate. Techniques for detecting and handling such non-linear effects will be discussed in Chapter 5.

### 2.4.2. Treatment of Categorical Variables

When a categorical variable is used in a GLM the treatment is a bit more involved. One of the levels is designated as the **base level**. Behind the scenes, the GLM software replaces the column in the input dataset containing the categorical variable with a series of indicator columns, one for each level of that variable *other than* the base level. Each of those columns takes on the values 0 or 1, with 1 indicating membership of

**Table 2. Input Data to the GLM**

| freq | vtype | ... other predictors ... |
|------|-------|--------------------------|
| 0    | SUV   | ...                      |
| 0    | truck | ...                      |
| 1    | sedan | ...                      |
| 0    | truck | ...                      |
| 0    | van   | ...                      |
| ...  | ...   | ...                      |

that level. Those columns are treated as separate predictors, and each receives its own coefficient in the output. This resulting dataset is called the **design matrix**.

To illustrate: suppose, in an auto frequency model, we wish to include the categorical variable “vehicle type,” which can be either “sedan,” “SUV,” “truck” or “van.” We designate “sedan” as the base level.

Table 2 shows the target variable and vehicle type columns for the first five rows of our dataset. The vehicle type variable is named “vtype” in the data.

Prior to fitting the GLM, the software will transform the data to create indicator variables for each level of vtype other than “sedan,” our base level. Table 3 shows the resulting design matrix.

Record 1, which is of vehicle type “SUV,” has a 1 in the vtype:SUV column and zeros for all other columns relating to vehicle type. Similarly, record 2 has a 1 in the vtype:truck column and zeros in all the others. There is no column corresponding to vehicle type “sedan”; record 3’s membership in that level is indicated by all three vehicle type columns being zero. Each of the newly-created vehicle type columns is treated as a separate predictor in Equation 2.

For a risk of any non-base level, when the values for the indicators columns are linearly combined with their respective coefficients in Equation 2, the coefficients

**Table 3. Design Matrix**

| <i>predictor:</i> | freq | vtype:SUV | vtype:truck | vtype:van | ... other predictors ... |
|-------------------|------|-----------|-------------|-----------|--------------------------|
| <i>symbol:</i>    | $y$  | $x_1$     | $x_2$       | $x_3$     | $x_4 \dots x_p$          |
|                   | 0    | 1         | 0           | 0         | ...                      |
|                   | 0    | 0         | 1           | 0         | ...                      |
|                   | 1    | 0         | 0           | 0         | ...                      |
|                   | 0    | 0         | 1           | 0         | ...                      |
|                   | 0    | 0         | 0           | 1         | ...                      |
|                   | ...  | ...       | ...         | ...       | ...                      |

relating to all other levels are multiplied by zero and drop out, while the coefficient relating to the level to which it belongs is multiplied by one and remains. For a risk of the base level, *all* the coefficients drop out. As such, the coefficient for each non-base level indicates the effect of being a member of that level *relative to* the base level.

Continuing with our example, suppose the GLM returns the estimates shown in Table 4 for the three non-base vehicle types.

To use this output to derive the linear predictor for an SUV, we plug the coefficients of Table 4 and the  $x$  predictors of Table 3 into Equation 2:

$$\begin{aligned} g(\mu) &= \beta_0 + 1.23 \times 1 + 0.57 \times 0 + (-0.30) \times 0 + \beta_4 x_4 + \cdots + \beta_p x_p \\ &= \beta_0 + 1.23 + \beta_4 x_4 + \cdots + \beta_p x_p \end{aligned}$$

As seen, all coefficients related to vehicle type for types other than “SUV” drop out of the equation, and only the coefficient for SUVs (1.23) remains. Since for a risk of vehicle type “sedan” *all* the vehicle type coefficients would drop out, the positive coefficient applied to SUVs indicates that their claim frequency is greater than that of sedans. Similarly, the negative coefficient attached to “van” indicates that claims are less frequent for vans than for sedans.

If a log link was used, a factor table for vehicle type can be constructed from this output by exponentiating each of the above coefficients. For the base level (sedan in this example) the factor is 1.000, since the effect of this vehicle type on the linear predictor is zero (and  $e^0 = 1$ ). An SUV would get a rating factor of  $e^{1.23} = 3.421$ , indicating that the expected frequency for SUVs are 242% greater than that of sedans. The rating factor for a van would be  $e^{-0.30} = 0.741$ , indicating an expected frequency that is 25.9% lower than that of sedans.

We now turn our attention to the significance statistics for this model (that is, the rightmost two columns of Table 4). These statistics help us assess our confidence in the values the parameters being non-zero. In the context of this model—where the parameters relate each level of vehicle type to the base level—a parameter of zero would mean that the level has the same mean frequency as the base level. It follows that the significance of the parameter measures the confidence that the level is significantly *different* from the base level.

The low  $p$ -value assigned to the vtype:SUV parameter indicates that the frequency for SUVs is significantly higher than that of sedans. For vans, on the other hand, the high  $p$ -value tells us that there is not enough evidence in the data to conclude that the frequency for vans is indeed lower than that of sedans.

**Table 4. GLM Parameter Estimates for Vehicle Type**

| Parameter                 | Coefficient | Std. Error | $p$ -Value |
|---------------------------|-------------|------------|------------|
| vtype:SUV ( $\beta_1$ )   | 1.23        | 0.149      | <0.0001    |
| vtype:truck ( $\beta_2$ ) | 0.57        | 0.175      | 0.0011     |
| vtype:van ( $\beta_3$ )   | -0.30       | 0.436      | 0.4871     |

**Figure 2.** Graphical representation of the parameter estimates for vehicle type, with “sedan” as the base level (*left panel*) and with “van” as the base level (*right panel*). The filled squares show the GLM estimates, and the error bars around them indicate the 95% confidence intervals around those estimates. The vertical gray bars at the bottom are proportional to the volume of data for each vehicle type.

![Figure 2: Two side-by-side plots showing GLM estimates for vehicle type. The left panel has 'sedan' as the base level, and the right panel has 'van' as the base level. Both plots show estimates for sedan, SUV, truck, and van. Filled squares represent the GLM estimates, and vertical error bars represent the 95% confidence intervals. At the bottom of each plot, vertical gray bars represent the volume of data for each vehicle type. In the left panel, the 'van' estimate is negative and its error bar crosses the zero line. In the right panel, the 'van' estimate is zero, and the 'sedan' estimate is negative.](5500ab73cf84ccc0055eecf28889b4db_img.jpg)

Figure 2: Two side-by-side plots showing GLM estimates for vehicle type. The left panel has 'sedan' as the base level, and the right panel has 'van' as the base level. Both plots show estimates for sedan, SUV, truck, and van. Filled squares represent the GLM estimates, and vertical error bars represent the 95% confidence intervals. At the bottom of each plot, vertical gray bars represent the volume of data for each vehicle type. In the left panel, the 'van' estimate is negative and its error bar crosses the zero line. In the right panel, the 'van' estimate is zero, and the 'sedan' estimate is negative.

A graphical representation of the estimates of Table 4 can be seen in the left panel of Figure 2. The filled squares show the GLM estimates, and the error bars around them indicate the 95% confidence intervals around those estimates. The vertical gray bars at the bottom are proportional to the volume of data for each vehicle type. We can see that “van,” the level with the least amount of data, has the widest error bar. In general, for categorical variables, sparser levels tend to have wider standard errors, indicating less confidence in their parameter estimates, since those estimates are based on less data. The “van” error bar also crosses the zero line, indicating that this estimate is not significant at the 95% confidence level.

### 2.4.3. Choose Your Base Level Wisely!

In the above example, we’ve set the base level for vehicle type to be “sedan.” Table 5 shows what the output would be had we used “van” as the base level instead.

This model is equivalent to that of Table 4 in that both would produce the same predictions. To be sure, the coefficients are different, but that is only because they are relating the levels to a different base. To see this, subtract the coefficient for “sedan”

**Table 5. Parameter Estimates After Setting “van” as the Base Level**

| Parameter                 | Coefficient | Std. Error | p-Value |
|---------------------------|-------------|------------|---------|
| vtype:sedan ( $\beta_1$ ) | 0.30        | 0.436      | 0.4871  |
| vtype:SUV ( $\beta_2$ )   | 1.53        | 0.425      | 0.0003  |
| vtype:truck ( $\beta_3$ ) | 0.88        | 0.434      | 0.0440  |

from that of any of the other levels (using 0 for “van”), and compare the result to the corresponding coefficient on Table 4.

What *has* changed, though, are the significance statistics. Whereas for the prior model the “SUV” and “truck” estimates were highly significant, after running this model the  $p$ -values for both have increased, indicating less confidence in their estimates. The parameters are plotted in the right panel of Figure 2. We can see that the error bars have widened compared to the prior model.

To understand why, recall that the significance statistics for categorical variable parameters measure the confidence in any level being *different* from the base level. As such, to be confident about that relationship, we need confidence about both sides of it—the mean response of the parameter in question, as well as that of the base level. In this case, our base level has sparse data, which does not allow the model to get a good read on its mean frequency, and so we can’t be certain about the relativity of any other level to it either.

As such, when using categorical variables, it is important to set the base level to be one with populous data—and not simply take the default base assigned by the software—so that our measures of significance will be most accurate.

## 2.5. Weights

Frequently, the dataset going into a GLM will include rows that represent the averages of the outcomes of groups of similar risks rather than the outcomes of individual risks. For example, in a claim severity dataset, one row might represent the average loss amount for several claims, all with the same values for all the predictor variables. Or, perhaps, a row in a pure premium dataset might represent the average pure premium for several exposures with the same characteristics (perhaps belonging to the same insured).

In such instances, it is intuitive that rows that represent a greater number of risks should carry more weight in the estimation of the model coefficients, as their outcome values are based on more data. GLMs accommodate that by allowing the user to include a **weight** variable, which specifies the weight given to each record in the estimation process.

The weight variable, usually denoted  $\omega$ , formally works its way into the math of GLMs as a modification to the assumed variance. Recall that the exponential family variance is of the form  $Var[y] = \phi V(\mu)$ . When a weight variable is specified, the assumed variance for record  $i$  becomes

$$Var[y_i] = \frac{\phi V(\mu_i)}{\omega_i},$$

that is, the “regular” exponential family variance divided by the weight. The variance therefore holds an *inverse relation* to the weight.

When the weight variable is set to be the number of records that an aggregated row represents, this specification of variance neatly fits with our expectations of the variance for such aggregated records. Recall that a basic property of variances is that

for a random variable  $X$ ,  $Var[(\sum X_i)/n] = \frac{1}{n} Var[X]$ ; in other words, the variance of the average of  $n$  independent and identically distributed random variables is equal to  $1/n$  times the variance of one such random variable. As such, a row representing the average loss amount of two claims would be expected to have half the variance of a single-claim row, and so on. Setting the weight to be the number of claims allows the GLM to reflect that expectation.

## 2.6. Offsets

When modeling for insurance rating plans, it is often the case that the scope of the project is not to update the entire plan at once; rather, some elements will be changed while others remain as-is. Some common examples:

- Rating algorithms typically begin with a base loss cost that varies by region or class, which is derived outside of the GLM-based analysis and may even be separately filed. The scope of the GLM project may be to update the rating factors only while the relative base loss costs remain static.
- When updating deductible factors, it is frequently desirable to calculate them using traditional loss elimination-based techniques, while the GLM is used for factors other than deductible. (Section 9.1 discusses this in more detail.)

In such instances, the “fixed” variable (base loss cost or deductible in the above examples) would not be assigned an estimated coefficient by the GLM. However, since it will be part of the rating plan the GLM is intended to produce, the GLM must be made aware of its existence so that the estimated coefficients for the other variables are optimal in its presence. GLMs provide the facility to do so through the use of an **offset**.

An offset is formally defined as a predictor whose coefficient is constrained to be 1. Mathematically, it is an added term to Equation 2:

$$g(\mu_i) = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + \text{offset}$$

When including an offset in a model, it is crucial that it be on the same “scale” as the linear predictor. In the case of a log link model, this requires the offset variable to be logged prior to inclusion in the model.

As an example, suppose the rating plan we intend to produce using a log-link GLM will include a factor for deductible, for which the base deductible level is \$500, with the other options being \$1,000 and \$2,500. The deductible factors, having been separately estimated using non-GLM methods, are 0.95 for the \$1,000 deductible and 0.90 for the \$2,500 deductible. (The \$500 deductible, being the base level, is assigned a factor of 1.00.) As we do not wish to alter these factors—but would like to ensure that the other factors estimated by the GLM are optimized for a rating plan that includes them—we include the deductible factors in the GLM as an offset.

To do so, we create a new variable, set to be  $\ln(1.00) = 0$  for those records with the base deductible of \$500,  $\ln(0.95) = -0.0513$  for those records with \$1,000 deductibles, and  $\ln(0.90) = -0.1054$  for records with \$2,500 deductibles. That variable is set as the offset in the GLM specification.<sup>4</sup>

Multiple offsets can be included by simply adding them together (after first transforming them to the linear predictor scale). So, supposing we wish to offset a log-link model for both the territorial base loss cost and the deductible, a record for a risk in a territory with a base loss cost of \$265 having a deductible factor of 0.90 would have its offset variable set to be  $\ln(265) + \ln(0.90) = 5.5797 + (-0.1054) = 5.4744$ .

**Exposure Offsets.** Offsets are also used when modeling a target variable that is expected to vary directly with time on risk or some other measure of exposure. An example would be where the target variable is the number of claims per policy for an auto book of business where the term lengths of the policies vary; all else equal, a policy covering two car years is expected to have twice the claims as a one-year policy. This expectation can be reflected in a log-link GLM by including the (logged) number of exposures—car years in this example—as an offset.

Note that this approach is distinct from modeling claims *frequency*, i.e., where the target variable is the number of claims divided by the number of exposures, which is the more common practice. In a frequency model, the number of exposures should be included as a weight, but not as an offset. In fact: a claim count model that includes exposure as an offset is *exactly equivalent* to a frequency model that includes exposure as a weight (but not as an offset)—that is, they will yield the same predictions, relativity factors and standard errors.<sup>5</sup>

To gain an intuition for this relationship, recall that an offset is an adjustment to the *mean*, while the weight is an adjustment to the *variance*. For a claim *count* model, additional exposures on a record carry the expectation of a greater number of claims, and so an offset is required. While the variance of the claim count is also expected to increase with increasing exposure—due to the exponential family's inherent expectation of greater mean implying greater variance—this is naturally handled by the GLM's assumed mean/variance relationship, and so no adjustment to variance (i.e., no weight variable) is necessary. For a claim *frequency* model, on the other hand, additional exposure carries the expectation of reduced variance (due to the larger volume of exposures yielding greater stability in the average frequency), but no change to the expected mean, and therefore a weight—but no offset—is needed.<sup>6</sup>

<sup>4</sup> This example is for a log-link GLM. For an example of the use of an offset in a logistic model, see CAS Exam 8, Fall 2018 Question 7. (Logistic regression is discussed later in this chapter.)

<sup>5</sup> Note that while this equivalence holds true for the Poisson (or overdispersed Poisson) distribution, it does not work for the negative binomial distribution since the two approaches may yield different estimates of the negative binomial parameter  $\kappa$ . (These distributions are discussed in the next section.)

<sup>6</sup> See Yan et al [2009] for a more detailed discussion of this equivalence and its derivation.

The following table summarizes this equivalence.

|                 | Claim Count                    | Frequency                                              |
|-----------------|--------------------------------|--------------------------------------------------------|
| Target Variable | # of claims                    | $\frac{\# \text{ of claims}}{\# \text{ of exposures}}$ |
| Distribution    | Poisson                        | Poisson                                                |
| Link            | log                            | log                                                    |
| Weight          | None                           | # of exposures                                         |
| Offset          | $\ln(\# \text{ of exposures})$ | None                                                   |

## 2.7. An Inventory of Distributions

The following sections describe several of the exponential family distributions available for use in a GLM, with a focus on the types of target variables typically modeled when developing rating plans: severity, frequency, pure premium and loss ratio.

### 2.7.1. Distributions for Severity

When modeling the severity of claims or occurrences, two commonly used distributions are the *gamma* and *inverse Gaussian* distributions.

**Gamma.** The gamma distribution is right-skewed, with a sharp peak and a long tail to the right, and it has a lower bound at zero. As these characteristics tend to be exhibited by empirical distributions of claim severity, the gamma is a natural fit (and indeed the most widely used distribution) for modeling severity in a GLM. The gamma variance function is  $V(\mu) = \mu^2$ , meaning that the assumed variance of the severity for any claim in a gamma model is proportional to an exponential function of its mean.

Figure 3 shows several examples of the gamma probability density function (pdf) curves for varying values of  $\mu$  and  $\phi$ . The two black lines illustrate gamma with  $\phi = 1$ , with means of 1 and 5. The two gray lines show gamma curves with those same means

**Figure 3.** The Gamma Distribution

![Figure 3: The Gamma Distribution. A line graph showing four probability density function (pdf) curves for the gamma distribution. The x-axis is labeled 'x' and ranges from 0 to 10. The y-axis is labeled 'density' and ranges from 0.0 to 1.0. The legend indicates four curves: 1. Solid black line: mu = 1, phi = 1. This curve starts at a density of 1.0 at x=0 and decays rapidly. 2. Dashed black line: mu = 5, phi = 1. This curve starts at a density of approximately 0.2 at x=0 and decays more slowly. 3. Solid gray line: mu = 1, phi = 0.25. This curve starts at 0, peaks at approximately 0.9 at x=1, and then decays. 4. Dashed gray line: mu = 5, phi = 0.25. This curve starts at 0, peaks at approximately 0.2 at x=5, and then decays. The solid lines (phi = 0.25) are more peaked than the dashed lines (phi = 1).](f3c5e85b70f94b9c3c521f594d69539f_img.jpg)

Figure 3: The Gamma Distribution. A line graph showing four probability density function (pdf) curves for the gamma distribution. The x-axis is labeled 'x' and ranges from 0 to 10. The y-axis is labeled 'density' and ranges from 0.0 to 1.0. The legend indicates four curves: 1. Solid black line: mu = 1, phi = 1. This curve starts at a density of 1.0 at x=0 and decays rapidly. 2. Dashed black line: mu = 5, phi = 1. This curve starts at a density of approximately 0.2 at x=0 and decays more slowly. 3. Solid gray line: mu = 1, phi = 0.25. This curve starts at 0, peaks at approximately 0.9 at x=1, and then decays. 4. Dashed gray line: mu = 5, phi = 0.25. This curve starts at 0, peaks at approximately 0.2 at x=5, and then decays. The solid lines (phi = 0.25) are more peaked than the dashed lines (phi = 1).

**Figure 4.** The Inverse Gaussian Distribution  
(as compared with the gamma distribution)

![Figure 4: A line graph comparing the density functions of the gamma and inverse Gaussian distributions. The x-axis is labeled 'x' and ranges from 0 to 10. The y-axis is labeled 'density' and ranges from 0.0 to 1.0. There are four curves: 1) A dashed black line representing the gamma distribution with mu = 1 and phi = 1, which peaks at x=1 with a density of 1.0. 2) A solid black line representing the inverse Gaussian distribution with mu = 1 and phi = 1, which also peaks at x=1 but with a density slightly above 1.0. 3) A dashed gray line representing the gamma distribution with mu = 5 and phi = 0.25, which is broader and flatter, peaking around x=3.5 with a density of approximately 0.2. 4) A solid gray line representing the inverse Gaussian distribution with mu = 5 and phi = 0.05, which is narrower and taller than the dashed gray line, peaking around x=3.5 with a density of approximately 0.25. The legend in the top right corner identifies these four curves.](7119b28e39fa3784606bf8b8f44e4f9d_img.jpg)

Figure 4: A line graph comparing the density functions of the gamma and inverse Gaussian distributions. The x-axis is labeled 'x' and ranges from 0 to 10. The y-axis is labeled 'density' and ranges from 0.0 to 1.0. There are four curves: 1) A dashed black line representing the gamma distribution with mu = 1 and phi = 1, which peaks at x=1 with a density of 1.0. 2) A solid black line representing the inverse Gaussian distribution with mu = 1 and phi = 1, which also peaks at x=1 but with a density slightly above 1.0. 3) A dashed gray line representing the gamma distribution with mu = 5 and phi = 0.25, which is broader and flatter, peaking around x=3.5 with a density of approximately 0.2. 4) A solid gray line representing the inverse Gaussian distribution with mu = 5 and phi = 0.05, which is narrower and taller than the dashed gray line, peaking around x=3.5 with a density of approximately 0.25. The legend in the top right corner identifies these four curves.

but with a lower value of  $\phi$ . As you would expect, the gray lines indicate lower variance than their corresponding black lines. However, also note that the value of  $\phi$  does not tell the full story of the variance. Comparing the two gray lines, it is clear that gamma with  $\mu = 5$  (dashed line) has a much wider variance than gamma with  $\mu = 1$  (solid line), despite their having the same value of  $\phi$ . This, of course, is due to the variance function  $V(\mu) = \mu^2$ , which assigns higher variance to claims with higher expected means, and is a desirable characteristic when modeling severity in a GLM. We would expect claims with higher average severity to also exhibit higher variance in severity, and this property allows us to reflect that assumption in a GLM even though the dispersion parameter  $\phi$  must be held constant for all claims.

**Inverse Gaussian.** The inverse Gaussian distribution, like the gamma distribution, is right-skewed with a lower bound at zero, which makes it another good choice for modeling severity. Compared to the gamma, it has a sharper peak and a wider tail, and is therefore appropriate for situations where the skewness of the severity curve is expected to be more extreme. (Later in this text we will discuss formal tests that can be applied to the data to assess the appropriateness of the various distributions.)

The variance function for the inverse Gaussian distribution is  $V(\mu) = \mu^3$ ; like the gamma, the inverse Gaussian variance scales exponentially with the mean, but at a faster rate.

Figure 4 shows two examples of the inverse Gaussian distribution (the two solid lines) each compared to a gamma distribution with the same mean and variance (the dotted lines). As can be seen, the shapes of the inverse Gaussian distributions have sharper peaks and are more highly skewed than their gamma counterparts.<sup>7</sup>

<sup>7</sup> For the two  $\mu = 5$  curves (the gray lines) in Figure 4, a gamma distribution with  $\phi = 0.25$  is compared to an inverse Gaussian distribution with  $\phi = 0.05$ . This is so that the variance of the gamma curve ( $\phi\mu^2 = 0.25 \times 5^2 = 6.25$ ) is equal to that of the inverse Gaussian curve ( $\phi\mu^3 = 0.05 \times 5^3 = 6.25$ ). The intent is to demonstrate the difference in the curves that would be yielded by the two distributions *for the same data*; typically, the  $\phi$  parameter under the inverse Gaussian distribution will be much lower than under the gamma distribution to compensate for the much larger values of  $V(\mu)$  in keeping the overall assumed variance roughly constant.

### 2.7.2. Distributions for Frequency

When modeling claim frequency (e.g., expected claim count per unit of exposure or per dollar of premium), the most commonly used distribution is the *Poisson* distribution. Another available choice is the *negative binomial* distribution. Both are explained in the following sections.

**Poisson.** The Poisson distribution models the count of events occurring within a fixed time interval, and is widely used in actuarial science as a distribution for claim counts. Although the Poisson is typically a discrete distribution (defined only for integral values) its implementation in a GLM allows it to take on fractional values as well. This feature is useful when modeling claim frequency, where claim count is divided by a value such as exposure or premium, resulting in a non-integral target variable. (In such instances it is usually appropriate to set the GLM weight to be the denominator of frequency.)

The variance function for a Poisson distribution is  $V(\mu) = \mu$ , meaning that the variance increases *linearly* with the mean. In fact, for a “true” Poisson distribution, the variance *equals* the mean; stated in terms of the exponential family parameters, this would mean that  $\phi = 1$  and so it drops out of the variance formula, leaving  $\text{Var}[y] = \mu$ . However, claim frequency is most often found to have variance that is greater than the mean, a phenomenon called **overdispersion**.

Overdispersion arises mainly because in addition to the natural variance arising from the Poisson process, there is another source of variance: the variation in risk level among the policyholders themselves. In statistical terms: in addition to the Poisson variance, there is variance in the Poisson mean ( $\mu$ ) among risks. To be sure, determining the appropriate mean, and thereby separating the good risks from bad risks, is precisely the purpose of our modeling exercise. However, our model will not be perfect; there will always be some variation in risk level among policyholders not explained by our model’s predictors, and so the data will exhibit overdispersion.

One way to deal with this scenario is to use the **overdispersed Poisson** (ODP) distribution in place of the “true” Poisson. The overdispersed Poisson is similar to the Poisson distribution, with the main difference being the  $\phi$  parameter: ODP allows it to take on any positive value rather than being restricted to 1 as is the case with the true Poisson.

When modeling claims frequency with the Poisson distribution, it is recommended that the overdispersed Poisson be used; otherwise, the variance will likely be understated, thereby distorting the model diagnostic measures such as standard error and  $p$ -value. (Note that the Poisson and ODP distributions will always produce the same estimates of coefficients, and therefore the same predictions; it is only the model diagnostics that will be affected.)

**Negative Binomial.** Another way of dealing with the overdispersion in the Poisson distribution resulting from random variation in the Poisson mean among risks is to treat the Poisson mean for any given risk as a random variable itself. Doing so, we would need another probability distribution to model the Poisson mean; a good

choice for that might be the gamma distribution. Such a setup would be stated mathematically as follows:

$$y \sim \text{Poisson}(\mu = \theta), \quad \theta \sim \text{gamma}(\dots). \quad (4)$$

In words, the outcome ( $y$ ) is Poisson-distributed with a mean of  $\theta$ , where  $\theta$  is itself random and gamma-distributed. This combination results in  $y$  following a **negative binomial** distribution.

For the negative binomial distribution, the standard exponential family dispersion parameter,  $\phi$ , is restricted to be 1. However, this distribution includes a third parameter,  $\kappa$ , called the **overdispersion parameter**, which is related to the variance of the gamma distribution of Equation 4.

The negative binomial variance function is

$$V(\mu) = \mu(1 + \kappa\mu)$$

and so the  $\kappa$  parameter serves to “inflate” the variance over and above the mean, which would be the variance implied by the Poisson distribution. Indeed, as  $\kappa$  approaches zero, the negative binomial distribution approaches Poisson. (Note that for the negative binomial distribution,  $\phi$ , restricted to be 1, drops out of the variance formula and thus the variance function  $V(\mu)$  is the full expression of the variance.)

### 2.7.3. A Distribution for Pure Premium: the Tweedie Distribution

Modeling pure premium (or loss ratio) at the policy level has traditionally been challenging. To see why, consider the properties these measures exhibit, which would need to be approximated by the probability distribution used to describe them: they are most often zero, as most policies incur no loss; where they do incur a loss, the distribution of losses tends to be highly skewed. As such, the pdf would need to have most of its mass at zero, and the remaining mass skewed to the right. Fortunately, a rather remarkable distribution that can capture these properties does exist: the **Tweedie** distribution.

In addition to the standard exponential family parameters  $\mu$  and  $\phi$ , the Tweedie distribution introduces a third parameter,  $p$ , called the **power** parameter.  $p$  can take on any real number except those in the interval 0 to 1 (non-inclusive: 0 and 1 themselves are valid values). The variance function for Tweedie is  $V(\mu) = \mu^p$ .

One rather interesting characteristic of the Tweedie distribution is that several of the other exponential family distributions are in fact special cases of Tweedie, dependent on the value of  $p$ :

- A Tweedie with  $p = 0$  is a normal distribution.
- A Tweedie with  $p = 1$  is a Poisson distribution.
- A Tweedie with  $p = 2$  is a gamma distribution.
- A Tweedie with  $p = 3$  is an inverse Gaussian distribution.

Going further, thanks to the Tweedie distribution, our choices in modeling claim severity are not restricted to the moderately-skewed gamma distribution and

the extreme skewness of the inverse Gaussian. The Tweedie provides a *continuum* of distributions between those two by simply setting the value of  $p$  to be between 2 (gamma) and 3 (inverse Gaussian).

However, the area of the  $p$  parameter space we are most interested in is between 1 and 2. At the two ends of that range are Poisson, which is a good distribution for modeling frequency, and gamma, which is good for modeling severity. Between 1 and 2, Tweedie becomes a neat combination of Poisson and gamma, which is great for modeling pure premium or loss ratio—that is, the combined effects of frequency and severity. (For the remainder of this text, references to the Tweedie distribution refer to the specific case of a Tweedie where  $p$  is in the range  $[1,2]$ .)

**A Poisson Sum of Gammas.** The Tweedie distribution models a “compound Poisson-gamma process.” Where events (such as claims) occur following a Poisson process, and each event generates a random loss amount that follows a gamma distribution, the total loss amount for all events follows the Tweedie distribution. In this way the Tweedie distribution may be thought of as a “Poisson-distributed sum of gamma distributions.”

In fact, the Tweedie parameters ( $\mu$ ,  $\phi$  and  $p$ ) bear a direct relationship to those of the underlying Poisson and gamma distributions; we will examine that more closely here.

Poisson has a single parameter, typically denoted  $\lambda$ , which is both the mean and the variance. (In prior sections we’ve referred to the Poisson mean by the symbol  $\mu$ , following the Poisson’s exponential family form. For this section, we’ll use the “traditional” parameterizations of the underlying distributions, saving the symbol  $\mu$  for the Tweedie mean.)

The gamma distribution takes two parameters: the shape and scale parameters, usually denoted  $\alpha$  and  $\theta$ , respectively. The mean is

$$E[y] = \alpha \cdot \theta, \quad (5)$$

and the coefficient of variation is

$$CV = 1/\sqrt{\alpha}. \quad (6)$$

The Tweedie mean can be related to those parameters as follows:

$$E[y] = \mu = \lambda \cdot \alpha \cdot \theta. \quad (7)$$

Notice that this is the product of the Poisson mean ( $\lambda$ ) and the gamma mean ( $\alpha \cdot \theta$ ), as we would expect—pure premium equals expected frequency times expected severity.

The power parameter ( $p$ ) is

$$p = \frac{\alpha + 2}{\alpha + 1}. \quad (8)$$

As seen in Equation 8, the power parameter is purely a function of the gamma parameter  $\alpha$ . Since  $\alpha$  is itself a function of the gamma coefficient of variation (as can be seen by rearranging Equation 6 above), it follows that the  $p$  parameter is a function

of the gamma CV. Specifically, as the gamma CV approaches zero,  $p$  approaches 1; as the gamma CV gets arbitrarily large,  $p$  approaches 2. Values of  $p$  used in insurance modeling typically range between 1.5 and 1.8.

The left panel of Figure 5 shows an example of a Tweedie density function where  $p = 1.02$ . A value of  $p$  so close to 1 implies very little variance in the gamma (or severity) component, and so the randomness of the outcome is mainly driven by the random count of events (or, the frequency component). As such, the shape of the distribution resembles a Poisson distribution, with spikes at discrete points, but with a small amount of variation around each point. Also note that the distribution features a point mass at 0, which allows for the (likely) possibility of no claims.

The right panel of Figure 5 illustrates a Tweedie pdf for the more realistic case of  $p = 1.67$ . In this example, the gamma variation is considerably larger and therefore the discrete Poisson points are no longer visible. However, the distribution still assigns a significant probability to an outcome of 0.

The formula for the Tweedie dispersion parameter ( $\phi$ ) is

$$\phi = \frac{\lambda^{1-p} \cdot (\alpha\theta)^{2-p}}{2-p}. \quad (9)$$

Through equations 7, 8, and 9, the Tweedie parameters can be derived from any combination of the Poisson parameter ( $\lambda$ ) and gamma parameters ( $\alpha$  and  $\theta$ )—and vice versa, with some algebraic manipulation.

In a Tweedie GLM, the  $\mu$  parameter varies by record, controlled by the linear predictor, while the  $\phi$  and  $p$  parameters are set to be constant for all records. One important implication of this is that a Tweedie GLM contains the implicit assumption that frequency and severity “move in the same direction”—that is, where a predictor drives an increase in the target variable (pure premium or loss ratio), that increase is made up of an increase in both its frequency and severity components. (To see this, try the following exercise: begin with any set of  $\mu$ ,  $\phi$  and  $p$ , and solve for  $\lambda$ ,  $\alpha$  and  $\theta$ ;

**Figure 5.** The Tweedie Distribution, with  $p = 1.02$  (*left*) and  $p = 1.67$  (*right*)

![Figure 5 consists of two side-by-side plots showing Tweedie distributions. The left plot is for p = 1.02, showing a distribution with a point mass at 0 and several distinct peaks at discrete intervals, resembling a Poisson distribution. The right plot is for p = 1.67, showing a distribution that is smooth and decays rapidly from a point mass at 0. Both plots have 'Total Loss Amount' on the x-axis (ranging from 0 to 100) and density on the y-axis (ranging from 0.00 to 0.12).](3788d43ff8c1f359e46e9373a533432f_img.jpg)

Figure 5 consists of two side-by-side plots showing Tweedie distributions. The left plot is for p = 1.02, showing a distribution with a point mass at 0 and several distinct peaks at discrete intervals, resembling a Poisson distribution. The right plot is for p = 1.67, showing a distribution that is smooth and decays rapidly from a point mass at 0. Both plots have 'Total Loss Amount' on the x-axis (ranging from 0 to 100) and density on the y-axis (ranging from 0.00 to 0.12).

then, try increasing  $\mu$  while holding  $\phi$  and  $p$  constant. Both  $\lambda$  and the product  $\alpha\theta$  will move upward.) This assumption doesn't always hold true, as often times variables in a model may have a positive effect on frequency while negatively affecting severity, or vice versa. However, Tweedie GLMs can be quite robust against such violations of its assumptions and still produce very strong models.

**Determination of the  $p$  parameter.** There are several ways the Tweedie  $p$  parameter may be determined:

- Some model-fitting software packages provide the functionality to estimate  $p$  as part of the model-fitting process. (Note that using this option may increase the computation time considerably, particularly for larger datasets.)
- Several candidate values of  $p$  can be considered and tested with the goal of optimizing a statistical measure such as log-likelihood (discussed in Chapter 6) or using cross-validation (discussed in Chapter 4).
- Alternatively, many modelers simply judgmentally select some value that makes sense (common choices being 1.6, 1.67 or 1.7). This may be the most practical in many scenarios, as the fine-tuning of  $p$  is unlikely to have a very material effect on the model estimates.

## 2.8. Logistic Regression

For some models, the target variable we wish to predict is not a numeric value, but rather the occurrence or non-occurrence of an event. Such variables are called *dichotomous* or *binary* variables. Examples are:

- Whether or not a policyholder will renew their policy.
- Whether a newly-opened claim will wind up exceeding some specified loss amount threshold.
- Whether a potential subrogation opportunity for a claim will be realized.

Such a model would be built based on a dataset of historical records of similar scenarios for which the outcome is currently known. The target variable,  $y_i$ , takes on the value of either 0 or 1, where 1 indicates that the event in question did occur, and 0 indicates that it did not.

**Distribution.** To model such a scenario in a GLM, the distribution of the target variables is set to be the binomial distribution. The mean of the binomial distribution—that is, the prediction generated by the model—is the *probability* that the event will occur.

**Link Function.** When modeling a dichotomous variable using the binomial distribution, a special type of link function must be used. Why not just use the log link? That's because a basic property of GLMs is that the linear predictor—that is, the right-hand side of Equation 2—is unbounded, and can take on any value in the range  $[-\infty, +\infty]$ . The mean of the binomial distribution, on the other hand, being a measure of probability, must be in the range  $[0, 1]$ . As such, we will need a link function that can map a  $[0, 1]$ -ranged value to be unbounded.

**Figure 6.** The Logit Function (*left*) and Its Inverse, the Logistic Function (*right*)

![Figure 6 consists of two side-by-side plots. The left plot shows the logit function, with the y-axis labeled 'logit' ranging from -6 to 6 and the x-axis labeled 'μ' ranging from 0.0 to 1.0. The curve is S-shaped, increasing from negative infinity at μ=0 to positive infinity at μ=1. The right plot shows the logistic function, with the y-axis labeled 'μ (probability)' ranging from 0.0 to 1.0 and the x-axis labeled 'linear predictor' ranging from -6 to 6. The curve is an S-shaped curve that passes through (0, 0.5), representing the probability of occurrence given a linear predictor.](fe655d77258397f7242c2df72b965b56_img.jpg)

Figure 6 consists of two side-by-side plots. The left plot shows the logit function, with the y-axis labeled 'logit' ranging from -6 to 6 and the x-axis labeled 'μ' ranging from 0.0 to 1.0. The curve is S-shaped, increasing from negative infinity at μ=0 to positive infinity at μ=1. The right plot shows the logistic function, with the y-axis labeled 'μ (probability)' ranging from 0.0 to 1.0 and the x-axis labeled 'linear predictor' ranging from -6 to 6. The curve is an S-shaped curve that passes through (0, 0.5), representing the probability of occurrence given a linear predictor.

There are several link function that are available for this purpose, but the most common is the **logit** link function,<sup>8</sup> defined as follows:

$$g(\mu) = \ln \frac{\mu}{1 - \mu}. \quad (10)$$

The left panel of Figure 6 shows a graph of the logit function. As can be seen, the logit approaches  $-\infty$  as  $\mu$  approaches zero, and becomes arbitrarily large as  $\mu$  approaches 1.

The right-hand side of Figure 6 shows the inverse of the logit function, called the **logistic** function, defined as  $1/(1 + e^{-x})$ . In a GLM, this function translates the value of the linear predictor onto the prediction of probability. A large negative linear predictor would indicate a low probability of occurrence, and a large positive linear predictor would indicate a high probability; a linear predictor of zero would indicate that the probability is 50%.

The full specification of a logistic regression model can be summarized as follows:

$$y_i \sim \text{binomial}(\mu_i) \quad (11)$$

$$\ln \frac{\mu_i}{1 - \mu_i} = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip}. \quad (12)$$

**Interpreting Results of a Logistic Model.** The logit function of Equation 10 can be interpreted as the log of the *odds*, where the odds is defined as the ratio of the probability of occurrence to the probability of non-occurrence, or  $\frac{\mu}{1 - \mu}$ . The odds is an alternate means of describing probability, which, unlike probability—which must lie in the region  $[0, 1]$ —is unbounded in the positive direction. (Think of a near-certain event, which might be said to have “million-to-one” odds.)

<sup>8</sup> Others are the *probit* link and *complementary log-log* link, not covered in this text.

Exponentiating both sides of Equation 12, the logistic GLM equation becomes a multiplicative series of terms that produces the odds of occurrence. This leads to a natural interpretation of the coefficients of the GLM (after exponentiating) as describing the effect of the predictor variables on the odds. For example, a coefficient of 0.24 estimated for continuous predictor  $x$  indicates that a unit increase in  $x$  increases the odds by  $e^{0.24} - 1 = 27\%$ . A coefficient of 0.24 estimated for a given level of a categorical variable indicates that the odds for that level is 27% higher than that of the base level.

## 2.9. Correlation Among Predictors, Multicollinearity and Aliasing

Frequently, the predictors going into a GLM will exhibit correlation among them. Where such correlation is moderate, the GLM can handle that just fine. In fact, determining accurate estimates of relativities in the presence of correlated rating variables is a primary strength of GLMs versus univariate analyses; unlike univariate methods, the GLM will be able to sort out each variable's unique effect on the outcome, as distinct from the effect of any other variable that may correlate with it, thereby ensuring that no information is double-counted.

As such, before embarking on a GLM modeling project, it is important to understand the correlation structure among the predictors. This will aid in interpreting the GLM output—particularly in understanding significant deviations between the GLM indications versus what would be indicated by a series of univariate analyses of individual predictors.

Where the correlation between any two predictors is very large, however, the GLM may run into trouble. The high correlation means that much of the same information is entering the model twice. The GLM—forced not to double-count—will need to apportion the response effect between the two variables, and how precisely best to do so becomes a source of great uncertainty. As such, coefficients may behave erratically; it is not uncommon to see extremely high or low coefficients result in such scenarios. Furthermore, the standard errors associated with those coefficients will be large, and small perturbations in the data may swing the coefficient estimates wildly. Such a model is said to be *unstable*.

Such instability in a model should be avoided. As such it is important to look out for instances of high correlation prior to modeling, by examining two-way correlation tables. Where high correlation is detected, means of dealing with this include the following.

- For any group of correlated predictors, remove all but one from the model. While this is certainly the simplest approach, a potential downside is that there may be some unique information, distinct from the common information, contained in individual predictors that will not be considered in our modeling process.
- Pre-process the data using dimensionality-reduction techniques such as *principal components analysis* (PCA) or *factor analysis*. These methods create multiple new

variables from correlated groups of predictors. Those new variables exhibit little or no correlation between them—thereby making them much more useful in a GLM—and they may be representative of the different components of underlying information making up the original variables. The details of such techniques are beyond the scope of this paper.

**Multicollinearity.** Simple correlation between pairs of predictors are easy enough to detect using a correlation matrix. A more subtle potential problem may exist where two or more predictors in a model may be strongly predictive of a third, a situation known as **multicollinearity**. The same instability problems as above may result, since the information contained in the third variable is also present in the model in the form of the *combination* of the other two variables. However, the variable may not be highly correlated with either of the other two predictors *individually*, and so this effect will not show up in a correlation matrix, making it more difficult to detect.

A useful statistic for detecting multicollinearity is the **variance inflation factor** (VIF), which can be output by most statistical packages. The VIF for any predictor is a measure of how much the (squared) standard error for the predictor is increased due to the presence of collinearity with other predictors. It is determined for each predictor by running a linear model setting the predictor as the target and using all the *other* predictors as inputs, and measuring the predictive power of that model.

A common statistical rule of thumb is that a VIF greater than 10 is considered high. However, where large VIFs are indicated, it is important to look deeper into the collinearity structure in order to make an informed decision about how best to handle it in the model.

**Aliasing.** Where two predictors are *perfectly* correlated, they are said to be **aliased**, and the GLM will not have a unique solution. Most GLM fitting software will detect that and automatically drop one of those predictors from the model. Where they are *nearly* perfectly correlated, on the other hand, the software may not catch it and try to run the model anyway. Due to the extreme correlation, the model will be highly unstable; the fitting procedure may fail to converge, and even if the model run is successful the estimated coefficients will be nonsensical. Such problems can be avoided by looking out for and properly handling correlations among predictors, as discussed above.

## 2.10. Limitations of GLMs

This section discusses two important limitations inherent in GLMs that one should bear in mind when using them to construct rating plans.

**1. GLMs Assign Full Credibility to the Data.** The estimates produced by the GLM are fit under the assumption that the data are fully credible for every parameter. For any categorical variable in the model, the estimate of the coefficient for each level is the one which fits the training data best, with no consideration given to the thinness of the data on which it is based.

To gain an intuition for what this means in a practical sense, consider the following simple example. Suppose we run a GLM to estimate auto severity, and the GLM includes only one predictor: territory, a categorical variable with five levels, coded A through E. Volume of data varies greatly by territory, and the smallest territory, E, has only 8 claims.

After running this model, the prediction for each risk will simply be the overall average severity for its territory.

That's right. For a GLM with a single categorical variable as its only predictor, it actually makes no difference which distribution or link function is chosen, just so long as the GLM fitting process is able to converge. The answers will always be the same, and they will be the one-way averages of the target variable by levels of the categorical variable. (Of course, we would not need a GLM for this; we could get to the same place with a simple Excel worksheet.)

Now, continuing with our example, the indicated relativity for territory E, like the rest, will be based simply on the average severity for its 8 claims. As actuaries, if we had been using the one-way analysis to derive relativities, we would surely not select the raw indication for a territory with such little credibility with no modification; we would apply a credibility procedure, and, in absence of any additional information about the territory, probably select something closer to the statewide average. It stands to reason that for the GLM we should not just take the indicated relativity either.

To be sure, in such a scenario, the standard error for the territory E coefficient would be large, and its  $p$ -value high. In this way, the GLM *warns* you that the estimate is not fully credible—but does nothing about it.

Where multiple predictors or continuous variables are involved, the estimates are based on a more complicated procedure which could not be easily performed in Excel, and the answers would vary based on the chosen link function and distribution. However, the approach to deriving the estimates would similarly be one that gives full weight to the data at each level of each categorical variable.

Incorporating credibility into the GLM framework is generally beyond the scope of this monograph. However, Chapter 10 briefly discusses two extensions to the GLM that allow for credibility-like estimation methods: *generalized linear mixed models* (GLMMs) and *elastic net* GLMs.

**2. GLMs Assume the Randomness of Outcomes is Uncorrelated.** Another important assumption built into GLMs is that the random component of the outcome of the target variable is uncorrelated among the records in the training set. Note the qualification “random component” in that sentence—that’s not the same thing as saying the outcomes are uncorrelated. If our auto severity model contains driver age and territory as predictors, we expect that drivers of similar ages or in the same territory would have similar outcomes, and thus be correlated in that way. After all, identifying and capturing such correlations is precisely the point of our modeling exercise. However, the assumption is that the *random* component of the outcome—which, from our vantage point, means the portion of the outcome driven by causes not in our model—are independent.

This assumption may be violated if there exist groups of records that are likely to have similar outcomes, perhaps due to some latent variable not captured by our model. The following are examples of where this may arise in insurance models:

- Frequently, the dataset going into an insurance GLM will comprise several years of policy data. Thus, there will be many instances where distinct records will actually be multiple renewals of the same policy. Those records are likely to have correlated outcomes; after all, a policyholder who is a bad driver in year 1 will likely still be a bad driver in years 2, 3 and 4.
- When modeling a line that includes a wind peril, policyholders in the same area will likely have similar outcomes, as the losses tend to be driven by storms that affect multiple insureds in the area at once.

Where the correlation is small, this is usually nothing to worry about; GLMs are quite robust against minor violations of their assumptions. However, it is important to be wary of instances of large correlation. Since the parameter estimates and significance statistics of a GLM are all derived “as if” all the random outcomes were independent, large instances of groups of correlated outcomes would cause the GLM to give undue weight to those events—essentially, picking up too much random noise—and produce sub-optimal predictions and over-optimistic measures of statistical significance.

There are several extensions to the GLM that allow one to account for such correlation in the data. One such method is the generalized linear mixed model (GLMM), briefly discussed in Section 10.1. Another is generalized estimating equations (GEE), not covered in this text.

