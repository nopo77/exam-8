---
paper: holmes_&_casotto
chapter: 4
title: The Bias–Variance Trade-Off
topics: [bias_variance_tradeoff, overfitting, underfitting, shrinkage, credibility_interpretation, aic_bic]
key_formulas: [mse_decomposition, aic_formula, bic_formula, credibility_weighted_coefficient]
---

> **TL;DR**
> - MSE = Bias² + Variance; reducing one increases the other — the optimal model minimizes the sum (generalization error), not either component alone.
> - High variance → overfit (model reacts to noise in training data); high bias → underfit (model excludes relevant variables, introducing fixed error).
> - GLMs evaluate the bias–variance trade-off post hoc via AIC/BIC and make binary variable inclusion decisions (in at full credibility, or out entirely).
> - Penalized regression optimizes the trade-off during fitting: shrinkage biases coefficients toward zero, reducing variance without full variable removal.
> - A penalized coefficient equals Z × β_GLM + (1−Z) × 0 — making penalization equivalent to partial credibility with a null (zero) complement.
> - Ridge ≡ Bühlmann credibility in a special Gaussian case (proven in Appendix A); cross-validation identifies the λ that best generalizes to unseen data.

# 4. The Bias–Variance Trade-Off

## 4.1. Introducing the Bias–Variance Trade-Off

We have explained what penalized regression is, but we have yet to demonstrate how it improves upon an unpenalized GLM. The core of this argument is intuitively supported by our cross-validation lambda grid search (Figure 3.8). At the leftmost point, the performance of a GLM is displayed. As we increase the penalty, the performance increases up to a maximum, and then decreases. This is not by chance, nor is it a cherry-picked example from the data. Both in practice and theory, this happens consistently: a model with (the right amount of) penalization will outperform a standard GLM. This fact is determined by what is known as the **bias–variance** trade-off.

The bias–variance trade-off is a very generic and general concept in machine learning. Bias here must not be confused with “biased” model in the context of protected classes as described in Mosley and Wenman (2022). It may be helpful to also remember that mean squared error (MSE) decomposes directly to bias and variance:  $\text{MSE} = \text{Bias}^2 + \text{Variance}$ . When the bias–variance trade-off is improved, the MSE decreases.

We introduce the concept of the bias–variance trade-off from the perspective of a GLM, and demonstrate how variable selection is often performed to maximize this trade-off. The trade-off may be viewed analogously as **underfitting versus overfitting**:

- A model with **high bias** is often described as **underfit**.
- A model with **high variance** is often described as **overfit**.

We then show how **penalized regression reduces variance through coefficient shrinkage** rather than manual coefficient removal. Finally, we draw connections between the bias–variance trade-off and both penalized regression and credibility. These connections will help lay the groundwork for the treatment of penalized regression as an actuarially sound credibility procedure.

## 4.2. Defining the Bias–Variance Trade-Off

Statistical theory shows that the error of **any** model on unseen data is the sum of two kinds of errors: the **bias** and the **variance** as described in Figure 4.1.

- **Bias** represents the error between the model we are building and the “real” model. Assuming we have access to infinite data, the bias will measure how the structure of the model we are building will replicate the “real” underlying model.

**Figure 4.1.** In a hypothetical scenario where we have access to an almost infinite amount of data, we would favor a very complex model such as the one on the right with plenty of variables (low bias). However, in a realistic scenario with limited data points, such a model will poorly generalize due to the instability of the parameters (high variance). Conversely, if we were to choose a too simplistic model, we could obtain a very stable model having low variance but very high bias. In practice we would always favor a right trade-off between bias and variance.

![Figure 4.1: A graph illustrating the bias-variance trade-off. The y-axis is labeled 'Error' and the x-axis is labeled 'Model Complexity'. Three curves are shown: 'Variance' (blue), 'Bias' (orange), and 'Generalization Error' (green). The 'Variance' curve starts low and increases as model complexity increases. The 'Bias' curve starts high and decreases as model complexity increases. The 'Generalization Error' curve is U-shaped, representing the sum of bias and variance. The graph is divided into three regions: 'Underfit' (low complexity, high bias), 'Optimal Value' (middle complexity, balanced), and 'Overfit' (high complexity, high variance). Below the graph, three target diagrams illustrate the concepts: the first shows a tight cluster of points far from the center (High Bias, Low variance); the second shows a tight cluster of points in the center (Low Bias, Low variance); and the third shows a wide, scattered cluster of points in the center (Low Bias, High variance).](1316cc5a3c69067473f110271212db3b_img.jpg)

Figure 4.1: A graph illustrating the bias-variance trade-off. The y-axis is labeled 'Error' and the x-axis is labeled 'Model Complexity'. Three curves are shown: 'Variance' (blue), 'Bias' (orange), and 'Generalization Error' (green). The 'Variance' curve starts low and increases as model complexity increases. The 'Bias' curve starts high and decreases as model complexity increases. The 'Generalization Error' curve is U-shaped, representing the sum of bias and variance. The graph is divided into three regions: 'Underfit' (low complexity, high bias), 'Optimal Value' (middle complexity, balanced), and 'Overfit' (high complexity, high variance). Below the graph, three target diagrams illustrate the concepts: the first shows a tight cluster of points far from the center (High Bias, Low variance); the second shows a tight cluster of points in the center (Low Bias, Low variance); and the third shows a wide, scattered cluster of points in the center (Low Bias, High variance).

- **Variance** represents the error of building the model on the specific data set that we used to fit the model versus other, richer data sets. This component becomes more important the smaller the data set and the “noisier” the effect. Unfortunately, small noisy data is quite common when dealing with insurance data.

Minimizing the generalization error is desirable when building models, and ideally one will look to minimize both the bias and variance error components **simultaneously**. Unfortunately, the bias–variance trade-off highlights a harsh truth: minimizing one of either model bias or variance will irremediably increase the other. Finding the model with the minimal error requires finding the **optimal bias–variance trade-off**.

## 4.3. Bias–Variance Trade-Off: A GLM Perspective

As a reminder, **variance** represents the error of building the model on a specific data set used to fit the model versus other, richer data sets. Imagine you are building a two-variable model on your own imperfect modeling data set. If you magically had twice the amount of data, the modeled coefficients would be more accurate and the predictions would have less error. Double it again, and this improvement continues. The error being reduced due to modeling on a richer data set is **error introduced by variance**.

Unfortunately, we cannot magically double our data. Some modeled coefficients may be unreliable, and a typical solution is to remove those coefficients from the model. You may decide to remove one variable and now you are left with a one-variable model. No matter how much data is added to this one-variable GLM, the coefficient for our removed variable is fixed at 0 and its error will never increase or decrease. The error between 0 and the coefficient’s true value is the **error introduced by bias**.

Did we make the right decision? That depends. If we leave the variable in our model, how much error in our predicted estimates is introduced by variance? If we remove the variable, how much error is introduced by the bias of setting this coefficient directly to zero? Before describing how the trade-off can be maximized through penalization, let’s explore an example of the trade-off in an unpenalized GLM.

Let’s think back to our homeowners example GLM in Section 1.6. In the second scenario, the fire extinguisher variable certainly has an impact on the target we are modeling. However, the amount of underlying exposures is so limited that the resulting GLM estimate will have a high variance.

In Table 4.1, model 1 is our original model and model 2 is a new model fitted without the fire extinguisher indicator.

**Table 4.1. Sample GLM Results for Models Fit with and without the Fire Extinguisher Variable**

| Model Output                                 | Model 1            | Model 2            |
|----------------------------------------------|--------------------|--------------------|
| exp(Intercept)                               | 100                | 105                |
| exp( $\beta_{\text{no fire extinguisher}}$ ) | 1.2                | NA                 |
| exp( $\beta_{\text{age of home}}$ )          | 1.01               | 1.01               |
| Average overall prediction                   | 110                | 110                |
| NA = not applicable.                         |                    |                    |
| Risk Description                             | Model 1 Prediction | Model 2 Prediction |
| No extinguisher, home age 0                  | 120                | 105                |
| With extinguisher, home age 0                | 100                | 105                |

By removing the fire extinguisher variable, we have certainly reduced the variance of our model. Remember that the **variance** represents the error of building the model on the specific data set we used to fit the model versus a different or more robust data set. When we remove this variable, the factor for not having a fire extinguisher will be the same on any data set that we use: 1.0. Certainly we will not see an increased or decreased error from the fire extinguisher variable on a different data set. Now, the question is whether the removal of this variable and corresponding reduction in variance introduces too much **bias** into our model. Are we potentially moving too far away from the “real” model by removing this variable?

If we include too many variables in our model, it will have a high variance and be **overfit**. To take an extreme example, imagine that only a single policy does not have a fire extinguisher. The extreme resulting relativity would be quite overfit to the training data and would perform poorly on the holdout data. It is intuitive that adding more and more information on policies without fire extinguishers would decrease the error of this model.

If we do not include enough variables in our model, it will be biased and **underfit**. Underfit models are excluding relevant information that could make for a more accurate prediction. If we remove the fire extinguisher variable, we may be excluding relevant information. The decision about whether to include a variable is made through an evaluation of the bias–variance trade-off.

## 4.4. Evaluating the Bias–Variance Trade-Off

We evaluate the bias–variance trade-off in a GLM after model fitting using various statistics. The traditional metrics are the Akaike information criterion (AIC) and the Bayesian information criterion (BIC):

$$\text{AIC}(\beta) = 2\text{NLL}(\beta) + 2\{\# \text{ of degrees of freedom}\}.$$

$$\text{BIC}(\beta) = 2\text{NLL}(\beta) + \log(n_{\text{obs}})\{\# \text{ of degrees of freedom}\}.$$

Both metrics are “penalized” measures of fit, as they are both the sum of two terms:

- The “likelihood” term, expressing the quality of fit within the training set
- The “degrees of freedom” term, which expresses the **complexity** of the model in terms of number of parameters

Both the AIC and the BIC are metrics that penalize the goodness of fit based on the number of coefficients in the model. There is a hurdle in the measure of fit that each coefficient must overcome to be included in the model.

If our fire extinguisher variable overcame this improvement and model 1 had a better AIC than model 2, model 1 would be superior and model 2 would be considered **biased** and **underfit**. If model 2 had a better AIC, this is a sign that the additional variable is not adding sufficient power and model 1 may have too much **variance** and be **overfit**.

**It is impossible to improve both bias and variance simultaneously.** When building a traditional GLM, the tools available to the modeler to maximize the bias–variance trade-off are the addition and removal of variables. A modeler must make use of post hoc penalized measures of fit like the AIC and the BIC to determine the bias–variance trade-off of a variable in a GLM.

**Conversely, it is possible to find the bias–variance trade-off that best generalizes on unseen data.** In fact, we demonstrated this optimization process earlier by the selection of a lambda penalty parameter through cross-validation. Rather than using a post hoc penalized goodness-of-fit statistic to evaluate the bias–variance trade-off of variable inclusion and exclusion, lasso penalized regression uses shrinkage to apply an optimal bias to coefficients during the fitting process. If the coefficient that maximizes this trade-off is zero, lasso penalization will remove the coefficient from the model completely. The use of penalization within the model fitting process removes the need for post hoc penalized metrics.

Section C.3 further develops how the generalization error can be measured. In particular, it shows how cross-validation can be seen as a better alternative to AIC and BIC, and further details the connections between AIC and BIC and penalized regression.

In more traditional actuarial analysis, this bias–variance trade-off is often addressed through credibility procedures.

## 4.5. Bias–Variance Trade-Off and Credibility

Let's think conceptually about the bias–variance trade-off and credibility using the fire extinguisher variable from our earlier example model. In the example, our data was showing an indicated factor of 1.2. If our data is thin, we might combine this with a selected complement of credibility of 1.1 using classical or Bühlmann credibility:

$$\text{Credibility-weighted factor} = 1.2 \times Z + 1.1 \times (1 - Z).$$

By weighing these together, the resulting estimate between 1.2 and 1.1 will have less variance than 1.2 alone if we have selected a stable, reasonably uncorrelated complement.

However, we are now introducing a bias to our models. Our selected complement of credibility is not based on the data, and therefore imposes a potential source of error outside of the data. The  $Z$  used in credibility is calculated to maximize the bias–variance trade-off by reducing the variance of a partially credible estimate through the introduction of an informed bias to the estimate.

The shrinkage introduced by penalized regression similarly introduces a bias to reduce the variance of estimated predictive values. The difference between this example and traditional penalized regression is that when using credibility, we are biasing our estimate toward a selected complement instead of a null coefficient. We now explore how penalized regression acts as a credibility procedure through this introduction of bias. This introduction lays the foundation for our later discussion on the implementation of lasso credibility.

## 4.6. Penalized Regression and Credibility

Let's again return to our fire extinguisher-only model. A GLM that has been fitted using only the fire extinguisher variable will produce a coefficient corresponding exactly to the pure premium relativity of the two categories in the data. Owing to the full credibility assumption of GLMs, the coefficient will correspond exactly to this relativity no matter how few exposures are in the "No" category. This is the unpenalized graph in Figure 4.2.

Now, we are going to apply a lasso penalty to our model. By introducing a sufficiently large penalty term, our output coefficient for "No" will shrink all the way to

**Figure 4.2. The experienced (purple) and the indicated relativity (yellow) are shown across different values of penalization  $\lambda$  for the fire extinguisher variable. The experienced and indicated relativities completely overlap without penalization.**

![Four charts showing the relationship between Fire Extinguisher status and Relativity/Exposure across different levels of penalization: UNPENALIZED, SMALL PENALIZATION, LARGE PENALIZATION, and FULLY PENALIZED.](3a310163273edcf70c19269a06d0cdf2_img.jpg)

The figure consists of four subplots arranged in a 2x2 grid, each showing the relationship between Fire Extinguisher status (Yes/No) and Relativity (left y-axis, 1 to 1.25) and Exposure (right y-axis, 0 to 1200). The x-axis for all plots is 'Fire Extinguisher' with categories 'Yes' and 'No'. The y-axis for the left column is 'Relativity' and for the right column is 'Exposure'.

- UNPENALIZED:** The 'Yes' bar is at Relativity 1.2 and the 'No' bar is at Relativity 1.0. The purple line (experienced relativity) and yellow line (indicated relativity) both start at (Yes, 1.0) and end at (No, 1.2), showing a positive slope.
- SMALL PENALIZATION:** The 'Yes' bar is at Relativity 1.2 and the 'No' bar is at Relativity 1.0. The purple line starts at (Yes, 1.0) and ends at (No, 1.2). The yellow line starts at (Yes, 1.0) and ends at (No, 1.1), showing a shallower positive slope.
- LARGE PENALIZATION:** The 'Yes' bar is at Relativity 1.2 and the 'No' bar is at Relativity 1.0. The purple line starts at (Yes, 1.0) and ends at (No, 1.2). The yellow line starts at (Yes, 1.0) and ends at (No, 1.05), showing a very shallow positive slope.
- FULLY PENALIZED:** The 'Yes' bar is at Relativity 1.2 and the 'No' bar is at Relativity 1.0. The purple line starts at (Yes, 1.0) and ends at (No, 1.2). The yellow line is horizontal at Relativity 1.0 for both 'Yes' and 'No' categories.

Four charts showing the relationship between Fire Extinguisher status and Relativity/Exposure across different levels of penalization: UNPENALIZED, SMALL PENALIZATION, LARGE PENALIZATION, and FULLY PENALIZED.

zero and be removed from the model. This extreme application of bias is effectively assigning no credibility to the data. This is represented by the fully penalized graph in Figure 4.2.

When  $\lambda$  is between these two extreme values, the coefficient will be somewhere between the GLM estimate and zero.

The bias that penalization introduces can be restated in the traditional credibility equation. We can represent every predicted value of  $\beta_i$  using a credibility value of  $0 < Z < 1$  by weighing a fully credible GLM estimate  $\beta_{GLM}$  with the noncredible coefficient estimate of 0. Note that  $Z$  is arbitrary and cannot be directly calculated from the selected penalty parameter:

$$\beta_i = \beta_{GLM} \times (Z) + 0 \times (1 - Z).$$

This similarity is not a coincidence. In Section A.2, we prove that **Bühlmann credibility and ridge penalization are in fact equivalent in a special case**. The mathematical relationship between penalization and credibility has been explored in Miller (2015) and Casotto, Banterle, and Beraud-Sudreau (2020), and we include a detailed explanation of the relationship between penalized regression and Bayesian statistics in Appendix A. Additionally, Appendix B contains a robust defense of penalized regression as an actuarial credibility procedure through the lens of ASOP 25. Rather than simply being “credibility-like,” we suggest that penalized regression, when used properly, can be applied as an actuarially sound credibility procedure in the form of **lasso credibility**.

## 4.7. Conclusion: Benefits of Lasso Penalization

Penalized regression applies a penalty term to the size of coefficients during the maximization of likelihood. The penalty value  $\lambda$  adjusts coefficients for their credibility and volatility. Selecting the penalization factor allows one to find the optimal generalization error of the bias–variance trade-off. Therefore, it is not necessary to perform post hoc significance testing to ensure that all coefficients are valid. To the extent that a variable is not beneficial to the fitting process, it is given partial credibility and shrunk toward zero **during** the fitting process. Lasso penalization will fully remove noncredible coefficients from the model **during** the fitting process.

This evaluation of coefficients during the fitting process directly addresses the issues with  $p$ -value significance testing discussed in Section 1.6.1. Lasso penalization

- answers the question “Is this coefficient credibly not zero, and how much can we trust this coefficient?” as opposed to just “Is this coefficient likely not zero or more extreme?”;
- provides a sound estimate of how much a coefficient or effect can be trusted—rather than a post hoc univariate adjustment for  $p$ -values close to 0.05, penalized regression automatically shrinks such coefficients by optimizing the bias–variance trade-off in a multivariate analysis (estimates are developed **jointly** considering correlations, and not on a one-by-one basis, as in GLM or  $p$ -values);

- does not use an arbitrary threshold of significance (e.g., 5%) but instead removes coefficients that do not overcome the penalty parameter (this penalty parameter is tuned and adjusted for each model individually based on sound procedures);
- does not require the post hoc removal of variables and refitting, as it will automatically remove noncredible variables during the fitting process; and
- does not require the post hoc adjustment of variables based on significance testing, as those variables are adjusted on a **multivariate basis** during the fitting process based on their credibility.

Penalized regression takes the null hypothesis in  $p$ -value significance testing and instead uses a version of this hypothesis as the complement in a credibility procedure. **Whereas variable evaluation in GLMs is a binary, often univariate, post hoc process, variable evaluation in penalized regression is a continuous, multivariate process that occurs during model fitting.**

Now that we have introduced penalized regression as a credibility procedure using a significance test's null hypothesis as a complement, we are ready to change this complement to something more actuarially appropriate through **lasso credibility**.

