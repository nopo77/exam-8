---
paper: goldburd_et_al
chapter: 6
title: "6. Model Refinement"
topics: [log_likelihood, deviance, f_test, aic_bic, residual_analysis, working_residuals, cook_distance, model_stability]
key_formulas: [scaled_deviance, f_statistic, aic, bic, deviance_residual, working_residual_formula, working_weight_formula]
---
> **TL;DR**
> - Scaled deviance = 2(ℓ_sat − ℓ_model); GLM minimizes deviance = maximizes log-likelihood; saturated model has deviance = 0
> - F-test for nested models: F = (D_S − D_B) / (# added params × φ̂_B); compare to F(df_added, n − p_B) distribution; dispersion parameter is NOT counted in denominator df
> - AIC = −2ℓ + 2p; BIC = −2ℓ + p·ln(n); AIC preferred in practice — BIC often too conservative
> - Deviance residuals should be approximately normal and homoscedastic for correct distribution; Q-Q plots and histograms diagnose distribution choice
> - Binned working residuals (equal working-weight bins): E(brb) = 0 and Var(brb) = constant for well-fit model; reveal missed non-linearities
> - Cook's distance identifies influential records; bootstrapping gives empirical confidence intervals for coefficients

# 6. Model Refinement

## 6.1. Some Measures of Model Fit

GLM software provides a number of statistical measures of how well the model fits the training data, which are useful when comparing candidates for model specifications and assessing the predictive power of individual variables. The most important such measures are *log-likelihood* and *deviance*.

### 6.1.1. Log-Likelihood

For any given set of coefficients, a GLM implies a probabilistic mean for each record. That, along with the dispersion parameter and chosen distributional form, implies a full probability distribution. It is therefore possible to calculate, for any record, the probability (or probability density) that the GLM would assign to the actual outcome that has indeed occurred. Multiplying those values across *all* records produces the probability of all the historical outcomes occurring; this value is called the **likelihood**.

A GLM is fit by finding the set of parameters for which the likelihood is the highest. This is intuitive; absent other information, the best model is the one that assigns the highest probability to the historical outcomes. Since likelihood is usually an extremely small number, the log of likelihood, or **log-likelihood**, is usually used instead to make working with it more manageable.

Log-likelihood by itself can be difficult to interpret. It is therefore useful to relate the log-likelihood to its hypothetical upper and lower bounds achievable with the given data.

At the low end of the scale is the log-likelihood of the **null model**, or a hypothetical model with no predictors—only an intercept. Such a model would produce the same prediction for every record: the grand mean.

At the other extreme lies the **saturated model**, or a hypothetical model with an equal number of predictors as there are records in the dataset. For such a model, Equation 2 becomes a system of equations with  $n$  equations and  $n$  unknowns, and therefore a perfect solution is possible. This model would therefore perfectly “predict” every historical outcome. It would also be, most likely, useless; overfit to the extreme, it is essentially nothing more than a complicated way of restating the historical data. However, since predicting each record perfectly is the theoretical best a model can possibly do, it provides a useful upper bound to log-likelihood for this data.

While the null model yields the lowest possible log-likelihood, the saturated model yields the highest; the log-likelihood of your model will lie somewhere in between. This naturally leads to another useful measure of model fit: deviance.

### 6.1.2. Deviance

**Scaled deviance** for a GLM is defined as follows:

$$\text{scaled deviance} = 2 \times (\ell_{\text{saturated}} - \ell_{\text{model}}) \quad (15)$$

where  $\ell_{\text{saturated}}$  is the log-likelihood of the saturated model, and  $\ell_{\text{model}}$  is the log-likelihood of the model being evaluated. This may be more formally stated as follows (with scaled deviance denoted as  $D^*$ ):

$$D^* = 2 \times \sum_{i=1}^n \ln f(y_i | \mu_i = y_i) - \ln f(y_i | \mu_i = \mu_i) \quad (16)$$

The first term after the summation sign is the log of the probability of outcome  $y_i$  given that the model's predicted mean is  $y_i$ —the mean that would be predicted by the saturated model. The second term is the log probability assigned to the outcome  $y_i$  by the actual model. The difference between those two values can be thought of as the magnitude by which the model missed the “perfect” log-likelihood for that record. Summing across all records and multiplying the result by 2 yields the scaled deviance.

Multiplying the scaled deviance by the estimated dispersion parameter  $\phi$  yields the *unscaled deviance*.<sup>12</sup> The unscaled deviance has the additional property of being independent of the dispersion parameter and thereby being useful for comparing models with different estimates of dispersion.

However, irrespective of the type of deviance measure (i.e., scaled or unscaled), note that the fitted GLM coefficients are those that minimize deviance. Recall that the previous section stated that the GLM is fit by maximizing log-likelihood, and in fact those two statements are equivalent: maximizing log-likelihood is also minimizing deviance. It is easy to see that by examining Equation 15 above. The first term inside the parentheses,  $\ell_{\text{saturated}}$  is constant with respect to the model coefficients, as it is purely a function of the data and the selected distribution. Since the log-likelihood of our model is subtracted from it, the coefficients yielding the maximum log-likelihood also yield the minimum deviance.

The deviance for the saturated model is zero, while the deviance for the null model can be thought of as the total deviance inherent in the data. The deviance for your model will lie between those two extremes.

<sup>12</sup> See Anderson, et al. § 1.154-1.158 for a more formal and generalized definition of the unscaled deviance. Further note that there is some discrepancy in terminology among various GLM texts, as some (e.g., Dobson & Barnett [2008]) use the term “deviance” to refer to the measure presented here as “scaled deviance,” and use “scaled deviance” to refer to that measure multiplied by the estimated dispersion parameter (i.e., the “unscaled deviance” in this text). We have followed the terminology used in Anderson et al [2007] and McCullough and Nelder [1989].

### 6.1.3. Limitations on the Use of Log-Likelihood and Deviance

The next section discusses some statistical tests that can be used to compare the fits of different models using these measures. However, at the outset, it is important to note the following caveats:

Firstly, when comparing two models using log-likelihood or deviance, the comparison is valid only if the datasets used to fit the two models are exactly identical. To see why, recall that the total log-likelihood is calculated by summing the log-likelihoods of the individual records across the data; if the data used for one model has a different number of records than the other, the total will be different in a way that has nothing to do with model fit.

This, by the way, is something to look out for when adding variables to an existing model and then comparing the resulting model with the original. If the new variable has missing values for some records, the default behavior of most model fitting software is to toss out those records when fitting the model. In that case, the resulting measures of fit are no longer comparable, since the second model was fit with fewer records than the first.

For any comparisons of models that use deviance, in addition to the caveat above, it is also necessary that the assumed distribution must be identical as well. This restriction arises from deviance being based on the amount by which log-likelihood deviates from the “perfect” log-likelihood; changing any assumptions other than the coefficients would alter the value of the “perfect” log-likelihood as well the model log-likelihood, muddying the comparison.

## 6.2. Comparing Candidate Models

As described above, the process of building and refining a GLM is one that takes place over many iterations; frequent decisions need to be made along the way, such as: which predictors to include; the appropriate transformations, if any, to be applied to continuous variables; and the groupings of levels for categorical variables. This section presents several statistical tests, based on the measures of model fit just discussed, that can be used to compare successive model runs and guide our decision making.

### 6.2.1. Nested Models and the F-Test

Where a model uses a subset of the predictors of a larger model, the smaller model is said to be a **nested model** of the larger one. Comparisons of nested models frequently occur when considering whether to add or subtract predictors. We may have one model that includes the extra predictors being considered, and one that does not but includes all the other variables. We then wish to compare the model statistics to answer the question: is the larger model, with the added variables, better than the smaller one? In other words, do the added predictors enhance the predictive power of the model?

We can do that by comparing the deviance (subject to the caveats noted above). However, in doing so we must consider a basic fact: adding predictors to a model *always* reduces deviance, whether the predictor has any relation to the target variable

or not. This is because more predictors—which means more parameters available to fit—gives the model fitting process more freedom to fit the data, and so it *will* fit the data better. At the extreme end of that is the saturated model, where the model fitting process has enough freedom to produce a perfect fit—even if the predictors are purely random and have no predictive power at all; with  $n$  unknowns and  $n$  equations, a perfect fit is always mathematically possible.

Therefore the meaningful question when comparing deviances is: did the added predictors reduce the deviance *significantly more* than we would expect them to if they are *not* predictive? One way to answer that is through the ***F*-test**, wherein the ***F*-statistic** is calculated and compared against the ***F* distribution**.

The formula for the *F*-statistic is

$$F = \frac{D_S - D_B}{(\# \text{ of added parameters}) \times \hat{\phi}_B} \quad (17)$$

In Equation 17, the symbol “D” refers to the *unscaled* deviance, and the subscripts “S” and “B” refer to the “small” and “big” models, respectively. The numerator is the difference in the unscaled deviance between the two models—that is, the amount by which the unscaled deviance was reduced by the inclusion of the additional parameters. As described above, this value is positive, since deviance always goes down.

The  $\hat{\phi}_B$  in the denominator is the estimate of the dispersion parameter for the big model. As it happens, this is also a good estimate of the amount by which we can expect unscaled deviance to go down for each new parameter added to the model—simply by pure chance—if the parameter adds no predictive power. Multiplying this value by the number of added parameters gives us the total expected drop in deviance. For the added predictors to “carry their weight,” they must reduce deviance by significantly more than this amount. (If some of the added predictors are categorical, note that a categorical variable with  $m$  levels adds  $m - 1$  parameters—one for each level other than the base level.)

Thus, the ratio in Equation 17 has an expected value of 1. If it is significantly greater than 1, we may conclude that the added variables do indeed improve the model.

How much greater than 1 is significant? Statistical theory says that the *F*-statistic follows an *F* distribution, with a numerator degrees of freedom equal to the number of added parameters and a denominator degrees of freedom equal to  $n - p_B$ , or the number of records minus the number of parameters in the big model. Note, however, that we do not count the dispersion parameter as a parameter when calculating the denominator degrees of freedom for the  $F$ -test. If the percentile of the *F*-statistic on the *F* distribution is sufficiently high, we may conclude that the added parameters are indeed significant.

As an example, suppose the auto GLM we built on 972 rows of data with 4 parameters yields an unscaled deviance of 365.8 and an estimated dispersion parameter of 1.42. We wish to test the significance of an additional potential predictor: rating territory, a categorical variable with 5 levels.

We run the GLM with the inclusion of rating territory, thereby adding  $5 - 1 = 4$  parameters to the model. Suppose the unscaled deviance of the resulting model is 352.1, and its estimated dispersion parameter is 1.42.

Using this information and Equation 17, we calculate the  $F$ -statistic.

$$\frac{365.8 - 352.1}{4 \times 1.42} = 2.412$$

To assess the significance of this value, we compare it against an  $F$  distribution with 4 numerator degrees of freedom and  $972 - 7$  (3 original parameters not counting the dispersion parameter + 4 added parameters) = 965 denominator degrees of freedom. An  $F$  distribution with those parameters has 2.412 at its 95.2 percentile, indicating a 4.8% probability of a drop in deviance of this magnitude arising by pure chance. As such, rating territory is found to be significant at the 95% significance level.

### 6.2.2. Penalized Measures of Fit

The  $F$ -test of the prior section is only applicable to nested models. Frequently, though we would want to compare non-nested models—that is, models having different variables, where one does not contain a subset of the variables of the other. As described above, deviance alone can not be used, since adding parameters always reduces deviance, and so selecting on the basis of lowest deviance gives an unfair advantage to the model with more parameters, which can lead to over-fitting.

A practical way to avoid the problem of over-fitting is to use a *penalized measure of fit*. While deviance is strictly a measure of model goodness of fit on the training data, a penalized measure of fit also incorporates information about the model's complexity, and so becomes a measure of model quality. Using one of these measures, one can compare two models that have different numbers of parameters. The two most commonly used measures of deviance are **AIC** and **BIC**.

**AIC**, or the **Akaike Information Criterion**, is defined as follows:

$$AIC = -2 \times \log\text{-likelihood} + 2p \quad (18)$$

where  $p$  is the number of parameters in the model.\* As with deviance, a smaller AIC suggests a “better” model. The first term in the above equation declines as model fit on the training data improves; the second term, called the *penalty term*, serves to increase the AIC as a “penalty” for each added parameter. (The rationale for using twice the number of parameters as the penalty is grounded in information theory and out of the scope of this monograph.) Using this criterion, models that produce low measures of deviance but high AICs can be discarded.

Note that the first additive term of equation 18 is the same as the formula for scaled deviance in Equation 15 but without the  $\mathcal{U}_{saturated}$  term, which is constant with respect to the model predictions. As such, the AIC can also be thought of as a penalized measure of *deviance*, when using it to compare two models. (AIC has little meaning outside of the context of a comparison anyway.) As a matter of fact, some statistical packages occasionally take advantage of this equivalence and substitute deviance for  $-2 \times \log\text{-likelihood}$  where it would simplify the calculation.

**BIC**, or the **Bayesian Information Criterion**, is defined as  $-2 \times \log\text{-likelihood} + p \log(n)$ , where  $p$  is once again the number of parameters, and  $n$  is the number of data points that the model is fit on. As most insurance models are fit on very large datasets, the penalty for additional parameters imposed by BIC tends to be much larger than the penalty for additional parameters imposed by AIC.

Most statistical packages can produce either of these measures. In practical terms, the authors have found that AIC tends to produce more reasonable results. Relying too heavily on BIC may result in the exclusion of predictive variables from your model.

\*Note that for AIC and BIC, unlike for the  $F$ -test, some GLM implementations, including R's `glm()`, count the dispersion parameter as an additional parameter when it is estimated, whereas others do not.

## 6.3. Residual Analysis

One useful and important means of assessing how well the specified model fits the data is by visual inspection of the *residuals*, or measures of the deviations of the individual data points from their predicted values. For any given record, we can think of the residual as measuring the magnitude by which the model prediction “missed” the actual value. In our GLM, this is assumed to be the manifestation of the *random* component of the model—that is, the portion of the outcome driven by factors other than the predictors, which our model describes using Equation 1 and our assumed distribution. Therefore, it is natural to inspect these values to determine how well our model actually does at capturing this randomness.

The simplest kind of residual is the **raw residual** which is just the difference between actual and expected, or  $y_i - \mu_i$ . For GLMs, however, two measures of deviation of actual from predicted that are much more useful are the **deviance residual** and the **working residual**. These measures have many useful properties for assessing model fit, and are discussed in the following sections.

### 6.3.1. Deviance Residuals

The square of the deviance residual for any given record is defined as that record’s contribution to the unscaled deviance. The deviance residual takes the same sign as actual minus predicted. Look back at Equation 16 (on page 63); the deviance residual for any record  $i$  is the square root of: twice the term to the right of the summation sign multiplied by the scale parameter. We use the negative square root where actual ( $y_i$ ) is less than expected ( $\mu_i$ ), and the positive square root where  $y_i > \mu_i$ .

Intuitively, we can think of the deviance residual as the residual “adjusted for” the shape of the assumed GLM distribution, such that its distribution will be approximately normal if the assumed GLM distribution is correct.

In a well-fit model, we expect deviance residuals to have the following properties:

- **They follow no predictable pattern.** Remember, the residuals are meant to be the random, or unpredictable, part of the data. If we discover any way the residuals can be predicted, then we are leaving some predictive power on the table and we can probably improve our model to pick it up.
- **They are normally distributed, with constant variance.** The *raw* residuals are certainly not expected to follow a normal distribution (assuming we selected a distribution other than normal); furthermore, the variance of the raw residual of any

record would be dependent on its predicted mean, due to the variance property of Equation 3. However, as the deviance residuals have been adjusted for the shape of the underlying distribution, they are expected to be normal and with constant variance. (The latter property is called **homoscedasticity**.) Any significant deviations from normality or homoscedasticity may indicate that the selected distribution is incorrect.

Figure 16 shows examples of two ways we might assess the normality of deviance residuals for a model of claim severity built using the gamma distribution. The left panel shows a histogram of the deviance residuals, with the best normal curve fit super-imposed. If the random component of the outcome indeed follows a gamma distribution, we would expect the histogram and the normal curve to be closely aligned. In this case, however, the histogram appears right-skewed relative to the normal curve, which suggests that the data exhibits greater skewness than what would be captured by a gamma distribution.

Another means of comparing the deviance residual distribution to normal is the  $q$ - $q$  plot, shown on the right panel of Figure 16. In this plot, the theoretical normal quantile for each point is plotted on the  $x$ -axis, and the empirical (sample) quantile of the deviance residual is plotted on the  $y$ -axis. If the deviance residuals are indeed normal, the points should follow a straight line; a line passing through the 25 and 75 theoretical quantiles is shown for reference. We observe that at the edges of the distribution, the points lie above the line; in particular the right-most points deviate significantly upward, which means that there are many more high-valued deviance residuals than would be expected under a normal distribution. This indicates that the distribution of deviance residuals is more skewed than normal—and by extension, the data is more skewed than gamma—confirming what we observed in the histogram.

Based on these results, we may suppose that an inverse Gaussian distribution, which assumes greater skewness, may be more appropriate for this data than the gamma distribution. Figure 17 shows the diagnostic plots for the same model but with the

**Figure 16.** Graphical Comparisons of Deviance Residuals of a Gamma Model with the Normal Distribution

![Figure 16: Graphical Comparisons of Deviance Residuals of a Gamma Model with the Normal Distribution. The figure consists of two panels. The left panel is a histogram titled 'Histogram' showing the density of deviance residuals. The x-axis is labeled 'Deviance Residual' and ranges from -1 to 2. The y-axis is labeled 'Density' and ranges from 0.0 to 0.8. A normal distribution curve is superimposed on the histogram, which shows a right-skewed distribution. The right panel is a Normal Q-Q Plot titled 'Normal Q-Q Plot'. The x-axis is labeled 'Theoretical Quantiles' and ranges from -3 to 3. The y-axis is labeled 'Sample Quantiles' and ranges from -1 to 2. A diagonal line represents the expected normal distribution. The data points follow the line closely in the center but deviate upwards at the right tail, indicating right-skewness.](72f8f68566ae1c43d361dd4b990b5631_img.jpg)

Figure 16: Graphical Comparisons of Deviance Residuals of a Gamma Model with the Normal Distribution. The figure consists of two panels. The left panel is a histogram titled 'Histogram' showing the density of deviance residuals. The x-axis is labeled 'Deviance Residual' and ranges from -1 to 2. The y-axis is labeled 'Density' and ranges from 0.0 to 0.8. A normal distribution curve is superimposed on the histogram, which shows a right-skewed distribution. The right panel is a Normal Q-Q Plot titled 'Normal Q-Q Plot'. The x-axis is labeled 'Theoretical Quantiles' and ranges from -3 to 3. The y-axis is labeled 'Sample Quantiles' and ranges from -1 to 2. A diagonal line represents the expected normal distribution. The data points follow the line closely in the center but deviate upwards at the right tail, indicating right-skewness.

**Figure 17.** Graphical Comparisons of Deviance Residuals of the Inverse Gaussian Model with the Normal Distribution

![Figure 17: Graphical Comparisons of Deviance Residuals of the Inverse Gaussian Model with the Normal Distribution. The figure contains two plots: a Histogram and a Normal Q-Q Plot. The Histogram shows the density of deviance residuals, with a normal curve overlaid. The Normal Q-Q Plot shows sample quantiles against theoretical quantiles, with points closely following a diagonal line.](012117dcead1d581e96cafc55090be70_img.jpg)

The figure consists of two side-by-side plots. The left plot is a histogram titled 'Histogram' showing the density of deviance residuals. The x-axis is labeled 'Deviance Residual' and ranges from -0.020 to 0.010. The y-axis is labeled 'Density' and ranges from 0 to 100. A normal distribution curve is overlaid on the histogram bars. The right plot is a Normal Q-Q Plot titled 'Normal Q-Q Plot'. The x-axis is labeled 'Theoretical Quantiles' and ranges from -3 to 3. The y-axis is labeled 'Sample Quantiles' and ranges from -0.020 to 0.010. The data points are plotted as open circles and follow a solid diagonal line very closely, indicating a good fit to the normal distribution.

Figure 17: Graphical Comparisons of Deviance Residuals of the Inverse Gaussian Model with the Normal Distribution. The figure contains two plots: a Histogram and a Normal Q-Q Plot. The Histogram shows the density of deviance residuals, with a normal curve overlaid. The Normal Q-Q Plot shows sample quantiles against theoretical quantiles, with points closely following a diagonal line.

assumption of inverse Gaussian as the underlying distribution. For this model, the histogram more closely matches the normal curve and the  $q$ - $q$  plot better approximates the straight line, confirming that this model is indeed a better fit.

**Discrete Distributions.** For discrete distributions (such as Poisson or negative binomial) or distributions that otherwise have a point mass (such as Tweedie, which has a point mass at zero), the deviance residuals will likely *not* follow a normal distribution. This is because while the deviance residuals factor in the shape of the distribution, they do not adjust for the discreteness; the large numbers of records having the same target values cause the residuals to be clustered together in tight groups. This makes deviance residuals less useful for assessing the appropriateness of such distributions.

One possible solution is to use *randomized quantile residuals*, which have similar properties as deviance residuals, but add random jitter to the discrete points so that they wind up more smoothly spread over the distribution. Randomized quantile residuals are described in detail in Dunn and Smyth (1996).<sup>13</sup> Another possible solution is to use binned working residuals, as described in the next section.

Where discretely-distributed data is highly aggregated, such as for claims data where a single record may represent the average frequency for a large number of risks, the target variable will take on a larger number of distinct values, effectively “smoothing out” the resulting distribution. This causes the distribution to lose much of its discrete property and approach a continuous distribution, thereby making deviance residuals more useful for such data.

<sup>13</sup> In R, randomized quantile residuals are available via the `qresiduals()` function of the “statmod” package. Note, however, that for the Poisson distribution, randomized quantile residuals can only be calculated for the “true” Poisson distribution (with  $\phi = 1$ ) but not the overdispersed Poisson; this diminishes their usefulness for most insurance data where “true” Poisson is unlikely to yield a good fit.

### 6.3.2. Working Residuals

Another useful type of residual is called the **working residual**. Most implementations of GLM fit the model using the Iteratively Reweighted Least Squares (IRLS) algorithm, the details of which are beyond the scope of this monograph. Working residuals are quantities that are used by the IRLS algorithm during the fitting process. Careful analysis of the working residuals is an additional tool that can be used to assess the quality of model fit.

Working residuals are defined as follows:

$$wr_i = (y_i - \mu_i) \cdot g'(\mu_i)$$

For a log link model, this simplifies to:

$$wr_i = \frac{y_i - \mu_i}{\mu_i}$$

For a logistic model, the working residual formula simplifies to:

$$wr_i = \frac{y_i - \mu_i}{\mu_i \cdot (1 - \mu_i)}$$

The main advantage of working residuals is that they solve a key problem that arises when visually inspecting the residuals via graphical methods, such a scatterplot. Such graphical plots are a highly useful means of detecting misspecifications or other shortcomings of a model. As noted above in the discussion of deviance residuals, any predictable pattern observed in the residuals indicates that the model could (and should) be improved, and a graphical analysis is an effective means of looking out for such patterns. However, most insurance models have thousands or even millions of observations, and the quantity being modeled is usually highly skewed. It can be difficult to identify predictable patterns in the dense clouds of skewed individual residuals, even for models with gross errors in specification.

Therefore, for such models, it is critical to **bin** the residuals before analyzing them. That is, we group the residuals by similar values of the  $x$ -axis of our intended plot, and aggregate (by averaging) both the  $x$ -axis values and the residuals prior to plotting. Binning the residuals aggregates away the volume and skewness of individual residuals, and allows us to focus on the signal. The advantage of *working* residuals is that they can be aggregated in a way that preserves the common properties of residuals – that is, they are unbiased (i.e., have no predictable pattern in the mean) and homoscedastic (i.e., have no pattern in the variance) for a well-fit model.<sup>14</sup>

---

<sup>14</sup> See the Appendix for the mathematical derivation of these properties.

To accomplish this, the working residuals are aggregated into bins, where each bin has a (roughly) equal sum of **working weights**. Working weights are defined as:<sup>15</sup>

$$ww_i = \frac{\omega_i}{V(\mu_i) \cdot [g'(\mu_i)]^2}$$

For each bin, the **binned working residual** is calculated by taking the weighted average of the working residuals of the individual observations within the bin, weighted by the working weights. Mathematically, for bin  $b$ , binned residual  $br_b$  is defined as:

$$br_b = \frac{\sum_{i \in b} wr_i \cdot ww_i}{\sum_{i \in b} ww_i}$$

If, in the course of graphically analyzing the working residuals over the different dimensions of the data, we are able to find a way to sort the working residuals into bins such that binned residuals appear to be predictably biased or “fanning out”, then we have identified a shortcoming in the model specification. The following are several examples of binned working residual scatterplots that may be useful in revealing flaws in the model.

**Plotting Residuals over the Linear Predictor.** Plotting the residuals over the value of the linear predictor may reveal “miscalibrations” in the model—that is, areas of the prediction space where the model may be systematically under- or over-predicting. Figure 18 shows examples of such plots for two example models.

Both plots use binned working residuals; the underlying models have thousands of observations, but we have binned the working residuals into 100 bins prior to plotting. Thus, for example, the left-most point of each plot represents those observations with the lowest 1% of linear predictor values, and the  $x$ -axis and  $y$ -axis values for that point are the average linear predictor and average working residual for those observations, both averages weighted by the working weights as described above.

The left-hand plot of Figure 18 reveals no structural flaws in the model. The plot points form an uninformative cloud with no apparent pattern, as they should for a well-fit model.

The right-hand plot, on the other hand, shows signs of trouble. The residuals in the left region tend to be below the zero line, indicating that the model predictions for those

<sup>15</sup> The following table shows the simplification of this formula for several common model forms:

| Distribution | Link function | Working Weights                          |
|--------------|---------------|------------------------------------------|
| Poisson      | Log           | $\omega_i \cdot \mu_i$                   |
| Gamma        | Log           | $\omega_i$                               |
| Tweedie      | Log           | $\omega_i \cdot \mu_i^{2-p}$             |
| Binomial     | Logit         | $\omega_i \cdot \mu_i \cdot (1 - \mu_i)$ |

**Figure 18.** Plotting Residuals over Linear Predictor![Figure 18: Two side-by-side scatter plots comparing 'Good Model' and 'Not-so-Good Model' residuals against the Linear Predictor. The 'Good Model' plot shows a random distribution of residuals around zero, while the 'Not-so-Good Model' plot shows a clear non-linear pattern, with residuals being positive for low and high predictor values and negative for middle values.](7b692a27af8e1a2533b06dc024e9db5c_img.jpg)

The figure consists of two side-by-side scatter plots. The left plot is titled 'Good Model' and the right plot is titled 'Not-so-Good Model'. Both plots have 'Linear Predictor' on the x-axis (ranging from 2 to 7) and 'Binned Working Resid' on the y-axis. The y-axis for the 'Good Model' ranges from -0.02 to 0.03, while for the 'Not-so-Good Model' it ranges from -0.06 to 0.04. In the 'Good Model' plot, the residuals are scattered randomly around the zero line. In the 'Not-so-Good Model' plot, the residuals show a clear non-linear pattern: they are positive for low predictor values (around 2-3), negative for middle predictor values (around 4-5), and positive again for high predictor values (around 6-7).

Figure 18: Two side-by-side scatter plots comparing 'Good Model' and 'Not-so-Good Model' residuals against the Linear Predictor. The 'Good Model' plot shows a random distribution of residuals around zero, while the 'Not-so-Good Model' plot shows a clear non-linear pattern, with residuals being positive for low and high predictor values and negative for middle values.

observations are higher than they should be. The model then seems to under-predict part of the middle region, and then once again over-predict for the highest-predicted observations. This may be caused by a non-linear effect that may have been missed, and the issue may be made clearer with plots of residuals over the various predictors, as discussed below.

**Plotting Residuals over the Value of a Predictor Variable.** While it is good practice to check partial residual plots (discussed in section 5.4.1) during the modeling process to understand the effect of responses and adjust as necessary, plots of residuals over the various predictors in the model may also reveal non-linear effects that may have been missed or not properly adjusted for.

Figure 19 shows binned working residual plots over one of the predictor variables (labeled “Variable X”) for two example models.

The left-hand plot clearly reveals that Variable X has a non-linear relationship with the target variable that is not being adequately addressed. The right-hand shows the plot that results after this issue had been fixed with a hinge function.

**Plotting Residuals over the Weight.** A plot of residuals over the weight variable used in the model (or over a variable that could potentially be a good choice of weight in the model) may reveal information about the appropriateness of the model weight (or lack thereof). Figure 20 shows plots of residuals over the number of exposures.

The model that generated the left-hand plot of Figure 20 did not use exposure as a weight in the model. This shows a “fanning out” effect on the left side, which violates the expectation of homoscedasticity, i.e., no pattern in the variance. Specifically, the lower-exposure records show more variance, and the higher-exposure records show less variance. This might be expected if no weight is specified; observations based on

**Figure 19.** Plotting Residuals over the Value of a Predictor Variable![Figure 19: Two side-by-side residual plots. The left plot, titled 'No Hinge Function', shows 'Binned Working Resid' on the y-axis (ranging from -0.2 to 0.1) against 'Variable X' on the x-axis (ranging from 0 to 4). The residuals form a clear downward-sloping curve, indicating a non-linear relationship. The right plot, titled 'With Hinge Function', shows the same y-axis (ranging from -0.02 to 0.02) against 'Variable X' (ranging from 0 to 4). The residuals are scattered randomly around zero, indicating a good fit with the hinge function.](b3faf87063b80c8f67bb574a903ca7e0_img.jpg)

Figure 19: Two side-by-side residual plots. The left plot, titled 'No Hinge Function', shows 'Binned Working Resid' on the y-axis (ranging from -0.2 to 0.1) against 'Variable X' on the x-axis (ranging from 0 to 4). The residuals form a clear downward-sloping curve, indicating a non-linear relationship. The right plot, titled 'With Hinge Function', shows the same y-axis (ranging from -0.02 to 0.02) against 'Variable X' (ranging from 0 to 4). The residuals are scattered randomly around zero, indicating a good fit with the hinge function.

larger volume of exposure tend to be more stable (i.e., exhibit lower variance in the outcome) than lower-volume records, as discussed in Section 2.5.

The right-hand plot results after this issue is rectified by adding exposure as the weight in the model. In this model, the expectation of lower variance with higher exposure has already been assumed by the model, and so the residuals have this effect adjusted out, forming a homoscedastic cloud.

## 6.4. Assessing Model Stability

Model stability refers to the sensitivity of a model to changes in the modeling data. We assume that past experience will be a good predictor of future events, but small

**Figure 20.** Plotting Residuals over the Number of Exposures![Figure 20: Two side-by-side residual plots. The left plot, titled 'No Weight', shows 'Binned Working Resid' on the y-axis (ranging from -0.20 to 0.05) against 'Exposure' on the x-axis (ranging from 0 to 6000). The residuals show a clear downward trend as exposure increases, indicating a negative bias for higher exposure values. The right plot, titled 'Exposure as Weight', shows the same y-axis (ranging from -0.02 to 0.02) against 'Exposure' (ranging from 0 to 8000). The residuals are scattered randomly around zero, indicating a good fit with exposure as a weight.](52f2555df324f05c0e27978beb5accb8_img.jpg)

Figure 20: Two side-by-side residual plots. The left plot, titled 'No Weight', shows 'Binned Working Resid' on the y-axis (ranging from -0.20 to 0.05) against 'Exposure' on the x-axis (ranging from 0 to 6000). The residuals show a clear downward trend as exposure increases, indicating a negative bias for higher exposure values. The right plot, titled 'Exposure as Weight', shows the same y-axis (ranging from -0.02 to 0.02) against 'Exposure' (ranging from 0 to 8000). The residuals are scattered randomly around zero, indicating a good fit with exposure as a weight.

changes in the past that we've observed should not lead to large changes in the future we predict. The classic example of this occurring is an unusually large loss experienced by an insured in a class with few members. A model run on all of the data may tell us with a high degree of confidence that this class is very risky. But if we remove the large loss from the dataset, the model may tell us with the same degree of confidence that the class is very safe. The model is not very stable with respect to the indication for this class, and so we may not want to give full weight to its results.

In the example above, the large loss is a particularly influential record, in that its removal from the dataset causes a significant change to our modeled results. Influential records tend to be highly weighted outliers. Assessing the impact of influential records is a straightforward way to assess model stability. A common measure of the influence of a record in GLM input data, calculable by most statistical packages, is **Cook's distance**. Sorting records in descending order of Cook's distance will identify those that have the most influence on the model results—a higher Cook's distance indicates a higher level of influence. If rerunning the model without some of the most influential records in the dataset causes large changes in some of the parameter estimates, we may want to consider whether or not those records or the parameter estimates they affect should be given full weight.

Another way to assess model stability is via cross validation, as described in Section 4.3.4 above. In that section, we presented cross validation as a means of testing the out-of-sample model performance. However, looking at the *in-sample* parameter estimates across the different model runs can yield important information about the stability of the model as well. The model should produce similar results when run on separate subsets of the initial modeling dataset.

Still another way to assess model stability is via **bootstrapping**. In bootstrapping, the dataset is randomly sampled with replacement to create a new dataset with the same number of records as the initial dataset. By refitting the model on many bootstrapped versions of the initial dataset, we can get a sense of how stable each of the parameter estimates are. In fact, we can calculate empirical statistics for each of the parameter estimates—mean, variance, confidence intervals, and so on—via bootstrapping. Many modelers prefer bootstrapped confidence intervals to the estimated confidence intervals produced by statistical software in GLM output.

