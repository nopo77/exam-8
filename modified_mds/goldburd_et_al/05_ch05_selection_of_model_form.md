---
paper: goldburd_et_al
chapter: 5
title: "5. Selection of Model Form"
topics: [frequency_severity_modeling, variable_selection, variable_transformation, non_linearity, hinge_functions, polynomial_terms, binning, interactions]
key_formulas: [partial_residual_formula, hinge_function_definition]
---
> **TL;DR**
> - Frequency/severity preferred over pure premium: isolates effects, avoids Tweedie's same-direction assumption, detects opposing effects on each component
> - Partial residual rᵢ = (yᵢ − μᵢ)/μᵢ + βⱼxᵢⱼ; plotting against xⱼ reveals non-linearity in continuous predictors
> - Three non-linearity remedies: binning (flexible but no continuity guarantee), polynomial terms (smooth but erratic at edges), hinge functions max(0, x − k) (interpretable slope changes)
> - Categorical grouping: start with many levels, iteratively combine neighbors with similar coefficients; balance parsimony vs. predictive power
> - Interactions (cat×cat, cat×cont, cont×cont) require p-value testing; center continuous variables at base value for interpretable coefficients

# 5. Selection of Model Form

Selecting the form of a predictive model is an iterative process, and is often more of an art than a science. As preliminary models are built and refined into final models, the model form is likely to evolve based on an analysis of the results.

In a generalized linear modeling framework, important decisions on the model form include:

- Choosing the target and predictor variables.
- Choosing a distribution for the target variable.
- Making decisions on the best form for the predictor variables, including whether to make them continuous or categorical, whether to apply transformations to the variables, and how best to group variables.

## 5.1. Choosing the Target Variable

Based on the scope of the modeling project, there may be several options for the target variable. When modeling a rating plan, for example, the target variable might be pure premium, claim frequency, or claim severity. If the goal of the project is instead to identify deficiencies in the existing rating plan, loss ratio may be a more appropriate target variable. Or when evaluating a set of underwriting restrictions, the probability of a large loss may be a good option.

The decision of which target variable to choose generally comes down to data availability and the preferences of the modeler. There is usually not one right answer, and it may be beneficial to try several options to see which one produces the best model.

### 5.1.1. Frequency/Severity versus Pure Premium

Where the ultimate goal of a model is to predict pure premium, there are two approaches we can use to get there.

1. Build two separate models: one with claims frequency—that is, count of claims per exposure—as the target, and another targeting claim severity, i.e., dollars of loss per claim. The individual models are then combined to form a pure premium model. Assuming log links were used for both, this combination of the two models is achieved by simply multiplying their corresponding relativity factors together.
2. Build a single model targeting pure premium, i.e., dollars of loss per exposure, using the Tweedie distribution.

This choice may be dictated by data constraints—for example, the data necessary to build separate models for claim frequency and severity may not be available. Furthermore, as the former approach requires building two models rather than one, time constraints may factor in as well, especially if a large number of pure premium models must be produced (e.g., when separately modeling multiple segments of the business or different perils).

However, where possible, the frequency/severity approach confers a number of advantages over pure premium modeling, some of which are as follows:

- Modeling frequency and severity separately often provides much more insight than a pure premium model, as it allows us to see the extent to which the various effects are frequency-driven versus severity-driven—information that may prove valuable in the model refinement process. Furthermore, some interesting effects may get “lost” when viewed on a pure premium basis due to *counteracting* effects on its components; for example, a variable that has a strong negative effect on frequency but an equally strong positive effect on severity would show up as a zero effect (and an insignificant variable!) in a pure premium model, and therefore go completely unnoticed. In such a case, while we may choose to deem the total effect of the variable a “wash” and not include it in our rating plan, that knowledge of the underlying effects may be useful in other business decisions.
- Each of frequency and severity is more stable—that is, it exhibits less random variance—than pure premium. Therefore, separating out those two sources of variance from the pure premium data effectively “cuts through the noise,” enabling us to see effects in the data that we otherwise would not. For example, consider a variable that has a positive effect on frequency and no effect on severity, thereby having a positive total effect on pure premium. While this variable may show up as significant in a frequency model, when testing it in a pure premium model the high variance in severity may overwhelm the effect, rendering the variable insignificant. Thus, a predictive variable may be missed, leading to underfitting.
- Pure premium modeling can also lead to overfitting. Continuing with the above example of a variable that affects frequency only, if that variable *does* wind up included in our pure premium model, the model is forced to fit its coefficient to both the frequency and severity effects observed in the training data. To the extent the severity effect is spurious, that parameter is overfit.
- The distribution used to model pure premium—the Tweedie distribution—contains the implicit assumption that frequency and severity “move in the same direction”—that is, where a predictor drives an increase in the target variable (pure premium or loss ratio), that increase is made up of an increase in both its frequency and severity components. (See Section 2.7.3 for a detailed discussion on this.) Modeling frequency and severity separately frees us from this restriction.

### 5.1.2. Policies with Multiple Coverages and Perils

Where the line of business we are modeling includes several types of coverage, it is usually a good idea to separate out the data pertaining to each coverage and model them

separately. For example, when modeling for a Businessowners package policy that includes building, business personal property and liability coverage, each of those items should be separately modeled. We may also consider subdividing the data further and modeling each peril (or group of perils) individually; for example, for our Businessowners building model, we may wish to create separate models for fire and lightning, wind and hail, and all other.

Even if the final rating plan must be structured on an “all perils combined” basis, there may be benefit to modeling the perils separately, as that will allow us to tailor the models to the unique characteristics of each peril. We can always combine the models at the end. A simple method for combining separate by-peril models to form a combined all-peril model is as follows:

1. Use the by-peril models to generate predictions of expected loss due to each peril for some set of exposure data.
2. Add the peril predictions together to form an all-peril loss cost for each record.
3. Run a model on that data, using the all-peril loss cost calculated in Step 2 as the target, and the union of all the individual model predictors as the predictors.

The coefficients for the resulting model will yield the all-peril relativities implied by the underlying by-peril models for the mix of business in the data. Note that since the target data fed into this new model is extremely stable, this procedure doesn’t require a whole lot of data. Rather, the focus should be on getting the mix of business right. The data used for this procedure should reflect the expected mix going forward, and so using only the most recent year may be ideal.

### 5.1.3. Transforming the Target Variable

In some modeling contexts, it may also be necessary or beneficial to transform the target variable in some way prior to modeling. Some considerations include:

- For pure premium, loss ratio or severity models, the presence of a few very large losses can have undue influence on the model results. In such cases, *capping* losses at a selected large loss threshold may yield a more robust and stable model. The cap point should be set high enough so that the target variable still captures the systematic variation in severity among risks, but not too high such that random large losses create excessive noise. (In Section 6.4 we discuss a formal statistical measure of a record’s influence on the model results called *Cook’s distance*. This statistic can also be used to alert the practitioner to instances where capping the target variable may be warranted.)
- In addition to the effect of individual large losses, it is also important to look out for catastrophic events that would cause a large number of losses at once, which can skew both frequency and severity effects. If possible, losses related to such events should be removed from the data entirely—thereby limiting the scope of the model to predicting *non-catastrophic* loss only—and a catastrophe model should separately be used to estimate the effect of catastrophes on the rating variables. If that is not an option, the effect of catastrophic losses should be tempered, either by adjusting

the value of the target variable downward or by decreasing the weight, so that these events should not unduly influence the parameter estimates.

- Where the data includes risks that are not at full loss maturity such that significant further loss development is to be expected (such recent accident year exposures for long-tailed lines), it may be necessary to *develop* the losses prior to modeling. Care should be taken so that the development factors applied match the type of entity being modeled. For example, for a severity model, the development factor should reflect only expected future development on *known claims*; for a pure premium or loss ratio model, the development factor should include the effect of pure IBNR claims as well.
- Where premium is used as the denominator of a ratio target variable (such as loss ratio), it may be necessary to on-level the premium.
- Where multi-year data is used, losses and/or exposures may need to be trended.

Note that for the latter three items on that list, as an alternative to applying those transformations, a temporal variable such as year can be included in the model. This variable would pick up any effects on the target related to time—such as trend, loss development and rate changes, for which the target has not been specifically adjusted—all at once. This is usually sufficient for most purposes, since the individual effects of development, trend, etc. are usually not of interest in models built for the purpose of rating. Rather, we wish to *control* for these effects so that they do not influence the parameter estimates of the rating variables, and the temporal variable does just that. Furthermore, the “control variable” approach also has the advantage in that the assumed temporal effects will be more “in tune” with the data the model is being estimated on.

On the other hand, there may be situations where adjusting the target using factors derived from other sources may be more appropriate. For example, where loss development factors are available that have been estimated from a wider, more credible body of data—perhaps incorporating industry data sources—those may provide a truer measure of development. Also, as there may already be established factors that have been assumed in other actuarial analyses of this same line of business (such as rate change analyses or reserve reviews) it may be preferable to use those in our rating factor model as well, so that all reviews of this line will be in sync. When doing so, however, it may be a good idea to try including the temporal variable even after the target has been adjusted; any significant temporal effects would then suggest a deficiency in the assumed factors, which can then be investigated.

## 5.2. Choosing the Distribution

Once the target variable is selected, the modeler must select a distribution for the target variable. This list of options is narrowed significantly based on the selected target variable. If modeling claim frequency, the distribution is likely to be either Poisson, negative binomial, or binomial (in the case of a logistic model). If modeling claim severity, common choices for the distribution are gamma and inverse Gaussian. The decision on which distribution to select may be based on an analysis of the deviance residuals, which is described in Section 6.3. It’s important to realize, though, that the distribution

is very unlikely to fit the data perfectly. The goal is simply to find the distribution that fits the data most closely out of the set of possible options.

## 5.3. Variable Selection

For some modeling projects, the objective may be to simply update the relativity factors to be used in an *existing* rating plan. That is, the structure of the pricing formula will remain as-is, and only the numerical factors will change to reflect what is indicated by the most recent data. For such instances, **variable selection**—that is, choosing which variables to include in the model—is not an issue, as the choice of variables has been fixed at the outset.

Frequently, though, a rating plan update provides the company an opportunity to revisit the rating structure. Are there additional variables—not currently rated on, but available in the data—that may provide useful information about the target variable, thereby allowing us to more finely segment risks? Or, perhaps, a rating plan is being formulated for a line of business for the first time, and no prior model exists. In such cases, the choice of which variables to include becomes an important concern in the modeling process.

Certainly, a major criteria is variable significance—that is, we would like to be confident that the effect of the variable indicated by the GLM is the result of a true relationship between that predictor and the target, and not due to noise in the data. To that end, we are guided by the  $p$ -value, as described in Section 2.3.2. However, it is important to bear in mind a crucial limitation of the  $p$ -value: it says nothing about the probability of a coefficient being non-zero; it merely informs us of the probability of an estimated coefficient of that magnitude arising *if* the “true” coefficient *is* zero. In assessing our confidence in the indicated factor, the  $p$ -value should be viewed as one piece of information, which we combine with intuition and knowledge of the business to arrive at a decision on whether to include the variable. As such, there is no “magic number”  $p$ -value below which a variable should automatically be deemed significant.

In addition to statistical significance, other considerations for variable selection include:

- Will it be cost-effective to collect the value of this variable when writing new and renewal business?
- Does inclusion of this variable in a rating plan conform to actuarial standards of practice and regulatory requirements?
- Can the electronic quotation system be easily modified to handle the inclusion of this variable in the rating formula?

In practice, many different areas of the business may need to weigh in on the practicality and acceptability of any given variable in the final rating structure.

For more complex modeling projects—particularly where external data is attached to the insurer’s own data to expand the predictive power—there may be hundreds or thousands of potential predictors to choose from, and variable selection becomes much more challenging. For such scenarios, a number of automated variable selection algorithms

exist that may aid in the process. (They may also add lots of spurious effects to the model if not used with appropriate care!) Those methods are beyond the scope of this paper.

## 5.4. Transformation of Variables

For any variable that is a potential predictor in our model, deciding whether or not to include it is not the end of the story. In many cases the variable will need to be transformed in some way such that the resulting model is a better fit to the data. Continuous and categorical variables each have considerations that would require transformation.

When including a continuous variable in a log-link model—logged, as discussed in Section 2.4.1—the model assumes a linear relationship between the log of the variable and the log of the mean of the target variable. However, this relationship doesn’t always hold; some variables have a more complex relationship with the target variable that cannot be described by a straight line. For such instances, it is necessary to transform the variable in some way so that it can adequately model the effect.

To illustrate the ways a non-linear effect can be handled in a GLM, we will use the example of a multi-peril Businessowners building severity model that includes the building age (or age of construction) as one of its predictors. Building age is expressed in years, with a value of 1 signifying a new building.

Suppose, in this instance, the GLM returned a coefficient of  $-0.314$  for log of building age. In log terms, this means that according to our model, each unit increase in the log of building age results in a 0.314 decline in the log of expected severity. We can also interpret this in “real terms”: the expected severity for any building age relative to a new building is the age raised to  $-0.314$ . However, this is the best log-linear fit. But is a linear fit the best way to model the relationship?

The next section presents a useful graphical diagnostic that will allow us to find out.

### 5.4.1. Detecting Non-Linearity with Partial Residual Plots

The set of **partial residuals** for any predictor  $x_j$  in a model is defined as follows:

$$r_i = (y_i - \mu_i) g'(\mu_i) + \beta_j x_{ij}, \quad (13)$$

where  $g'(\mu_i)$  is the first derivative of the link function. For a log link model, Equation 13 simplifies as follows:

$$r_i = \frac{y_i - \mu_i}{\mu_i} + \beta_j x_{ij}. \quad (14)$$

In Equation 14, the residual is calculated by subtracting the model prediction from the actual value, and then adjusted to bring it to a similar scale as the linear predictor (by dividing by  $\mu_i$ )<sup>9</sup>. Then,  $\beta_j x_{ij}$ —that is, the part of the linear predictor that  $x_j$  is responsible for—is added back to the result. Thus, the partial residual may be thought

---

<sup>9</sup> Note that this is the “working residual” discussed in Section 6.3.2.

**Figure 8.** Partial Residual Plot of Age of Construction Variable

![Partial Residual Plot of Age of Construction Variable. The plot shows Partial Residual on the y-axis (ranging from -1.5 to 0.0) versus x=log(age of construction) on the x-axis (ranging from 1.5 to 4.0). A scatter of points is shown with a linear fit line labeled 'fit line (y = -0.314x)'. The points show a non-linear, U-shaped pattern, indicating that the linear model is not a good fit for the data.](4c547ec1af44f8fcdc8b1d67662ac30a_img.jpg)

Partial Residual Plot of Age of Construction Variable. The plot shows Partial Residual on the y-axis (ranging from -1.5 to 0.0) versus x=log(age of construction) on the x-axis (ranging from 1.5 to 4.0). A scatter of points is shown with a linear fit line labeled 'fit line (y = -0.314x)'. The points show a non-linear, U-shaped pattern, indicating that the linear model is not a good fit for the data.

of as the actual value with all components of the model prediction *other than* the part driven by  $x_j$  subtracted out. (Hence the “partial” in “partial residual.”) The variance in the partial residuals therefore contains the variance unexplained by our model in addition to the portion of the variance our model intends to explain with  $\beta_j x_j$ . We can then plot them against the model’s estimate of  $\beta_j x_j$  to see how well it did.

Figure 8 shows the partial residual plot for our example building age variable.<sup>10</sup> The model’s linear estimate of the building age effect, or  $-0.314x$ , is superimposed over the plot. While the line may be the best *linear* fit to the points, it is certainly not the best fit, as the points are missing the line in a systematic way. The model is clearly over-predicting for risks where log building age is 2.5 (in real terms, building age 12) and lower. It under-predicts between 2.5 and 3.25, and once again over-predicts for older buildings. It is clear we will need something more flexible than a straight line to properly fit this data.

We present three ways such non-linearities can be accommodated within a GLM:

- binning the variable
- adding polynomial terms
- using piecewise linear functions.

Each of these approaches is discussed in the following sections.

### 5.4.2. Binning Continuous Predictors

One possible fix for non-linearity in a continuous variable is not to model it as continuous at all; rather, a new categorical variable is created where levels are defined as intervals over the range of the original variable. The model then treats it as it would any categorical variable; a coefficient is estimated for each interval, which applies to all risks falling within it.

<sup>10</sup> Note that despite this model having been built on around 50,000 records, the plot shows only 100 points. As 50,000 points would make for a very messy (and uninformative) scatterplot, the data has been *binned* prior to plotting. We discuss binning plotted residuals in Section 6.3.2. When binning partial residuals, the working weights, as described in that section, should be used.

**Figure 9.** Coefficient Estimates for the Bucketed Age of Construction Variable (*left*) and a Graphical Representation (*right*)

| Variable   | Estimate | Std. Err. |
|------------|----------|-----------|
| ...        | ...      | ...       |
| AoC: 11–14 | 0.622    | 0.117     |
| AoC: 15–17 | 0.745    | 0.121     |
| AoC: 18–20 | 0.561    | 0.124     |
| AoC: 21–23 | 0.589    | 0.122     |
| AoC: 24–26 | 0.344    | 0.128     |
| AoC: 27–29 | 0.037    | 0.139     |
| AoC: 30–33 | –0.079   | 0.141     |
| AoC: 34–39 | –0.064   | 0.142     |
| AoC: 39+   | –0.139   | 0.147     |
| ...        | ...      | ...       |
| ...        | ...      | ...       |

![A graphical representation of the coefficient estimates for the bucketed age of construction variable. The plot shows the estimate for each age bin on the y-axis (ranging from -0.4 to 1.0) against the age of construction on the x-axis (ranging from 1-10 to 39+). The estimates show a general upward trend from 1-10 to 15-17, peaking at 15-17, and then generally declining, with a slight increase for the 21-23 bin compared to the 18-20 bin. The 1-10 bin is the base level at 0.0.](98ea5e21d919b389f3ce8b17ef4e65f6_img.jpg)

| Age of Construction | Estimate |
|---------------------|----------|
| 1-10                | 0.000    |
| 11-14               | 0.622    |
| 15-17               | 0.745    |
| 18-20               | 0.561    |
| 21-23               | 0.589    |
| 24-26               | 0.344    |
| 27-29               | 0.037    |
| 30-33               | -0.079   |
| 34-39               | -0.064   |
| 39+                 | -0.139   |

A graphical representation of the coefficient estimates for the bucketed age of construction variable. The plot shows the estimate for each age bin on the y-axis (ranging from -0.4 to 1.0) against the age of construction on the x-axis (ranging from 1-10 to 39+). The estimates show a general upward trend from 1-10 to 15-17, peaking at 15-17, and then generally declining, with a slight increase for the 21-23 bin compared to the 18-20 bin. The 1-10 bin is the base level at 0.0.

Figure 9 shows the results of running age of construction through our model as a categorical variable. For this example, ten bins were created. Interval boundaries were designed such that the bins contain roughly equal number of records, and building ages 1 through 10 was designated as the base level.

As the graphical plot of the coefficients shows, the model picked up a shape similar to that seen in the points of the partial residual plot. Average severity rises for buildings older than ten years, reaching a peak at the 15-to-17 year range, then gradually declining.

Binning a continuous variable frees the model from needing to constrain its assumed relationship with the target variable to any particular shape, as each level is allowed to float freely.

There are, however, some drawbacks to this approach.

In a general sense, binning a continuous variable, and therefore giving it a large number of parameters in our model, may violate the goal of parsimony, or keeping the model simple; as a rule, we shouldn't be giving the model more degrees of freedom than is necessary to adequately fit the data. The next paragraphs describe two more specific downsides to binning versus modeling a variable continuously.

**Continuity in the Estimates is Not Guaranteed.** Allowing each interval to move freely may not always be a good thing. The ordinal property of the levels of the binned variable have no meaning in the GLM; there is no way to force the GLM to have the estimates behave in any continuous fashion, and each estimate is derived independently of the others. Therefore, there is a risk that some estimates will be inconsistent with others due to random noise.

This pitfall is illustrated in the results shown in Figure 9. The building age effect on severity seems to be declining past 17 years. However, the 21–23 year factor is slightly higher than the 18–20 year factor. We have no reason to believe this break in the pattern is real, and it is most likely due to volatility in the data.

This issue may present an even bigger problem if the predictor variable is replacement cost of the building. The expectation is that, as the replacement cost increases, so does the expected loss cost for the policy. By including replacement cost in the model as a continuous variable (perhaps with some transformation applied), we can better ensure a monotonic relationship between replacement cost and predicted loss cost, which is a desirable outcome. If replacement cost is instead binned, there may be reversals in the variable coefficients due to volatility in the data. For example, buildings with a replacement cost of \$300,000 may have a lower predicted loss cost than buildings with a \$250,000 replacement cost, even though this result doesn't make sense.

In our building age example, note that the problem can be remedied somewhat by combining those two levels to a single level representing ages 18 through 23. Alternatively, we can manually smooth out the pattern when selecting factors.

**Variation within Intervals is Ignored.** Since each bin is assigned a single estimate, the model ignores any variation in severity that may exist *within* the bins. In our building age example, all buildings with ages between 1 and 10 years are assumed to have the same severity, which may not be the case. Of course, we could refine the interval boundaries to split that bin into two or more smaller ones. Doing so, however, would thin out the data, reducing the credibility of the estimates, thereby making them more susceptible to noise. Modeling building age as a continuous variable with a transformation (as discussed in the next sections) allows each building age to have a unique factor with no loss of credibility.

### 5.4.3. Adding Polynomial Terms

Another means of accommodating non-linearity in a linear model is to include the square, cube, or higher-order polynomials of the variable in the model in addition to the original variable. In such a model, the original variable and the polynomial terms are all treated as separate predictors, and a separate coefficient is estimated for each. This enables the model to fit curves to the data; the more polynomial terms that are provided, the more flexible the fit that can be achieved.

The left panel of Figure 10 shows the results of adding the square of the logged building age—in addition to log building age itself—to our model. In this example, the model estimated a coefficient of 4.749 for log building age (denoted here as  $x$ ) and a coefficient of  $-0.866$  for log building age squared (denoted as  $x^2$ ). The graph shows the partial residuals with the curve formed by both building age terms superimposed.<sup>11</sup> Clearly this is a better fit to the data than the straight line shown in Figure 8.

In the right panel of Figure 10, a third term—the log building age cubed—was added. The additional freedom provided by this term allows the model to attenuate the downward slope on the right-hand side of the curve. This perhaps yields a better fit, as the points seem to indicate that the declining severity as building age increases does taper off toward the higher end of the scale.

<sup>11</sup> For this graph (as well as Figure 11) we extended the definition of partial residuals given in Equation 14 to include all terms related to the variable being evaluated (i.e., the  $\beta_j x_{ij}$ 's for all polynomial terms are added back to the working residual rather than the single  $\beta_j x_{ij}$  term).

**Figure 10.** Partial Residual Plot of Age of Construction Variable using Two Polynomial Terms (*left*) and Three Polynomial Terms (*right*)

![Figure 10: Two side-by-side partial residual plots. The left plot shows a quadratic fit with equation y = 4.749x - 0.866x^2. The right plot shows a cubic fit with equation y = 12.683x - 3.697x^2 + 0.329x^3. Both plots have 'Partial Residual' on the y-axis and 'x=log(age of construction)' on the x-axis.](c3a537b0b6eced7fb3f46a5d4c19b62e_img.jpg)

Figure 10 consists of two side-by-side partial residual plots. The left plot shows a quadratic fit with the equation  $y = 4.749x - 0.866x^2$ . The right plot shows a cubic fit with the equation  $y = 12.683x - 3.697x^2 + 0.329x^3$ . Both plots have 'Partial Residual' on the y-axis and 'x=log(age of construction)' on the x-axis.

Figure 10: Two side-by-side partial residual plots. The left plot shows a quadratic fit with equation y = 4.749x - 0.866x^2. The right plot shows a cubic fit with equation y = 12.683x - 3.697x^2 + 0.329x^3. Both plots have 'Partial Residual' on the y-axis and 'x=log(age of construction)' on the x-axis.

One potential downside to using polynomials is the loss of interpretability. From the coefficients alone it is often very difficult to discern the shape of the curve; to understand the model's indicated relationship of the predictor to the target variable it may be necessary to graph the polynomial function.

Another drawback is that polynomial functions have a tendency to behave erratically at the edges of the data, particularly for higher-order polynomials. For example, Figure 11 shows the partial residual plot that would result if we were to use *five* polynomial terms in our age of construction example. In this model, the fitted

**Figure 11.** Partial Residual Plot of Age of Construction Variable using Five Polynomial Terms

![Figure 11: A partial residual plot showing a highly complex, wiggly fit line for five polynomial terms. The y-axis is 'Partial Residual' and the x-axis is 'x=log(age of construction)'. The fit line is labeled 'fit line'.](03b9c04a0552e519e849210b8e2bf596_img.jpg)

Figure 11 is a partial residual plot showing a highly complex, wiggly fit line for five polynomial terms. The y-axis is 'Partial Residual' and the x-axis is 'x=log(age of construction)'. The fit line is labeled 'fit line'.

Figure 11: A partial residual plot showing a highly complex, wiggly fit line for five polynomial terms. The y-axis is 'Partial Residual' and the x-axis is 'x=log(age of construction)'. The fit line is labeled 'fit line'.

curve veers sharply upward near the upper bound of the data, and would most likely generate unreasonably high predictions for ages of construction higher than typical.

### 5.4.4. Using Piecewise Linear Functions

A third method for handling non-linear effects is to “break” the line at one or more points over the range of the variable, and allow the slope of the line to change at each break point.

Looking back at the partial residual plot in Figure 8, it is apparent that severity rises and reaches a peak at around age 2.75 (in log terms) and then declines. Thus, while a single straight line does not fit this pattern, a broken line—with a rising slope up to 2.75 and then declining—will likely do the job.

We can insert a break in the line at that point by defining a new variable as  $\max(0, \ln(AoC) - 2.75)$ , and adding it to the model. This new variable, called a *hinge function*, has a value of 0 for buildings with log age 2.75 or lower, and rises linearly thereafter, and so it will allow the GLM to capture the change in slope for older buildings versus newer ones.

Running the model with the addition of the hinge function breaking the line at 2.75 yields the partial output shown in Table 6.

For  $\log(AoC)$  2.75 and lower, the hinge function variable has a value of zero, and only the basic  $\log(AoC)$  function varies; as such, the slope of the log-log response is 1.225. For  $\log(AoC)$  above 2.75, on the other hand, both variables are in play. Thus, to calculate the log-log slope for older buildings, we must add the two coefficients together, yielding a slope of  $1.225 + (-2.269) = -1.044$ . Thus, the log-log response is a positive slope for newer buildings and a negative slope for older buildings.

The left panel of Figure 12 shows the partial residual plot of  $\log(AoC)$  under this model, with the broken line indicated by the model superimposed. This clearly does a much better job at fitting the points than the straight line of Figure 8.

As the points seem to indicate that the downward slope tapers off at the far right of the graph, we may try to improve the fit further by adding another break at  $\log(AoC) = 3.6$ . The resulting model output is shown in Table 7, and the right panel of Figure 12 graphs the partial residual plot.

The positive coefficient estimated for the second hinge function indicates that the slope of the line to the right of  $\log(AoC) = 3.6$  is higher than slope to the left of it. As the graphed fit line shows, this has the effect of nearly straightening out the steep

**Table 6. Model Output After Adding a Hinge Function for a Break Point at  $\log(AoC) = 2.75$**

| Variable                    | Estimate | Std. Error | p-Value |
|-----------------------------|----------|------------|---------|
| ...                         | ...      | ...        | ...     |
| $\log(AoC)$                 | 1.225    | 0.163      | <0.0001 |
| $\max(0, \log(AoC) - 2.75)$ | -2.269   | 0.201      | <0.0001 |
| ...                         | ...      | ...        | ...     |

**Figure 12.** Partial Residual Plot of Age of Construction Variable using a Break at 2.75 (*left*) and Breaks at Both 2.75 and 3.6 (*right*)

![Figure 12: Two partial residual plots for the Age of Construction variable. The left plot shows a single break at 2.75, with a piecewise linear fit line that has a positive slope before 2.75 and a negative slope after 2.75. The right plot shows two breaks at 2.75 and 3.6, with a piecewise linear fit line that has a positive slope before 2.75, a negative slope between 2.75 and 3.6, and a horizontal slope after 3.6. Both plots have 'Partial Residual' on the y-axis (ranging from 1.5 to 4.0) and 'x=log(age of construction)' on the x-axis (ranging from 1.5 to 4.0).](839caaa69e77dd042dd8910e8d294d01_img.jpg)

Figure 12: Two partial residual plots for the Age of Construction variable. The left plot shows a single break at 2.75, with a piecewise linear fit line that has a positive slope before 2.75 and a negative slope after 2.75. The right plot shows two breaks at 2.75 and 3.6, with a piecewise linear fit line that has a positive slope before 2.75, a negative slope between 2.75 and 3.6, and a horizontal slope after 3.6. Both plots have 'Partial Residual' on the y-axis (ranging from 1.5 to 4.0) and 'x=log(age of construction)' on the x-axis (ranging from 1.5 to 4.0).

downward slope. The  $p$ -value of 0.0082 indicates that the evidence for a change in slope following the 3.6 point is strong, but not as strong as for a change following the 2.75 point. However, this may simply be due to that estimate being based on a relatively small subset of the data. As this leveling-off effect comports with our intuition, we may decide to keep the third hinge function term in the model.

The use of hinge functions allows one to fit a very wide range of non-linear patterns. Furthermore, the coefficients provided by the model can be easily interpreted as describing the change in slope at the break points; and, as we have seen, the significance statistics (such as  $p$ -value) indicate the degree of evidence of said change in slope.

One major drawback of this approach is that the break points must be selected by the user. Generally, break points are initially “guesstimated” by visual inspection of the partial residual plot, and they may be further refined by adjusting them to improve some measure of model fit (such as deviance, which is discussed in the next section). However, the GLM provides no mechanism for estimating them automatically. (In Chapter 10 we briefly discuss a useful model called *MARS*, a variant of the GLM, which, among other things, fits non-linear curves using hinge functions—and does it in an automated fashion with no need for tweaking by the user.)

**Table 7.** Adding an Additional Break Point at  $\log(\text{AoC}) = 3.6$

| Variable                           | Estimate | Std. Error | $p$ -Value |
|------------------------------------|----------|------------|------------|
| ...                                | ...      | ...        | ...        |
| $\log(\text{AoC})$                 | 1.289    | 0.159      | <0.0001    |
| $\max(0, \log(\text{AoC}) - 2.75)$ | -2.472   | 0.217      | <0.0001    |
| $\max(0, \log(\text{AoC}) - 3.60)$ | 1.170    | 0.443      | 0.0082     |
| ...                                | ...      | ...        | ...        |

Another potential downside is that while the fitted response curve is continuous, its first derivative is not—in other words, the fit line does not exhibit the “smooth” quality we would expect, but rather abruptly changes direction at our selected breakpoints.

### 5.4.5. Natural Cubic Splines

A more advanced method for handling non-linear effects—one that combines the concepts of polynomial functions and piecewise functions with breakpoints as discussed in the prior two sections—is the **natural cubic spline**. This is more mathematically complex than the prior two approaches, and we will not delve into the details here; the interested reader can refer to Hastie, Tibshirani & Friedman (Section 5.2.1 of 2nd Ed.) or Harrell (Section 2.4.4). We describe here some of its characteristics:

- The first and second derivatives of the fitted curve function are continuous—which in a practical sense means that the curve will appear fully “smooth” with no visible breaks in the pattern.
- The fits at the edges of the data (i.e., before the first selected breakpoint and after the last) are restricted to be linear, which curtails the potential for the kind of erratic edge behavior exhibited by regular polynomial functions.
- The use of breakpoints makes it more suitable than regular polynomial functions for modeling more complex effect responses, such as those with multiple rises and falls.

As with polynomial functions, natural cubic splines do not lend themselves to easy interpretation based on the model coefficients alone, but rather require graphical plotting to understand the modeled effect.

## 5.5. Grouping Categorical Variables

Some categorical predictor variables are binary or can only take on a small number of values. Others, though, can take on a large number of possible values, and for these variables it is generally necessary to group them prior to inclusion in the model. Consider, for example, driver age. If ungrouped, this variable is likely to consume too many degrees of freedom, which can lead to nonsensical results and the inability of the model to converge. In deciding how to group such variables, one strategy is to start with many levels and then begin grouping based on model coefficients and significance. For example, we may start with 30 buckets, then compare the coefficients for neighboring buckets. If one bucket is, say, drivers between the ages of 26 and 27, and another is drivers between 28 and 29, and the coefficients for these two levels are similar, we can create a new bucket for drivers between 26 and 29. This is generally an iterative process and requires balancing the competing priorities of predictive power, parsimony, and avoiding overfitting to the data.

## 5.6. Interactions

Thus far, we have focused on optimizing the selection and transformation of variables for our model under the assumption that each variable has an individual effect on the target variable. However, we may also wish to consider the hypothesis that two or more variables may have a *combined* effect on the target over and above their

individual effects. Stated differently, the effect of one predictor may depend on the level of another predictor, and vice-versa. Such a relationship is called an **interaction**.

An example of an interaction is illustrated in Figure 13. In this example we have two categorical variables: variable 1 has two levels, A and B, with A being the base level; variable 2 has levels X (the base) and Y.

The table in the left panel shows the mean response for each combination of levels with no interaction. For variable 1, the multiplicative factor for level B (relative to base level A) is 2.0, regardless of the level of variable 2. Similarly, the variable 2 relativity of level Y is 1.5, regardless of the level of variable 1. Simple enough.

The right panel shows an example of where an interaction is present. Where variable 2 is X, the relativity for level B is 2.0, as before; however, where variable 2 is Y, the level B relativity is 2.2. Or, we can state this effect in terms of variable 2: the relativity for level Y is either 1.50 or 1.65, depending on the level of variable 1.

Another way of describing the situation in the right panel of Figure 13 is as follows: for each of the two variables, there are **main effects**, where the relativity of level B is 2.0 and the relativity of level Y is 1.5; plus, there is an additional **interaction effect** of being both of level Y and level B—with a multiplicative factor of 1.1. This is the setup typically used in GLMs, and it allows us to use the GLM significance statistics to test the interaction effects distinctly from the main effects in order to determine whether the inclusion of an interaction significantly improves the model.

The above example illustrates the interaction of two categorical variables. It is also possible to interact two continuous variables, or a continuous variable with a categorical variable. In the following sections, we further explore the categorical/categorical interaction in a GLM, as well as the other two interaction types.

### 5.6.1. Interacting Two Categorical Variables

We present here a more concrete example to illustrate the handling of a categorical/categorical interaction in a GLM.

Suppose, for a commercial building claims frequency model, which uses a Poisson distribution and a log link, we include two categorical predictors: occupancy class, coded 1 through 4, with 1 being the base class; and sprinklered status, which can be either “no” or “yes,” the latter indicating the presence of a sprinkler system in the building, with no sprinkler being the base case.

**Figure 13.** An Example of a Mean Response for Each Level of Two Categorical Variables Without an Interaction (*left panel*) and With an Interaction (*right panel*)

| Without Interaction |   |            |    | With Interaction |   |            |    |
|---------------------|---|------------|----|------------------|---|------------|----|
|                     |   | Variable 1 |    |                  |   | Variable 1 |    |
|                     |   | A          | B  |                  |   | A          | B  |
| Variable 2          | X | 10         | 20 | Variable 2       | X | 10         | 20 |
|                     | Y | 15         | 30 |                  | Y | 15         | 33 |

**Table 8. Model with the Main Effects of Occupancy Class and Sprinklered Status**

|                 | Estimate | Std. Error | p-Value |
|-----------------|----------|------------|---------|
| (Intercept)     | −10.8679 | 0.0184     | <0.0001 |
| occupancy:2     | 0.2117   | 0.0264     | <0.0001 |
| occupancy:3     | 0.4581   | 0.0262     | <0.0001 |
| occupancy:4     | 0.0910   | 0.0245     | 0.0005  |
| sprinklered:Yes | −0.3046  | 0.0372     | <0.0001 |

Running the model with the main effects only yields the output shown in Table 8. The coefficient of  $-0.3046$  indicated for “sprinklered:yes” indicates a sprinklered discount of 26.3% (as  $e^{-0.3046}-1 = -0.263$ ).

We then wish to test whether the sprinklered discount should vary by occupancy class. To do this, we add the interaction of those two variables in the model, in addition to the main effects. Behind the scenes, the model fitting software adds additional columns to the design matrix: a column for each combination of non-base levels for the two variables. Each of those columns is valued 1 where a risk has that combination of levels, and is 0 otherwise. These new columns are treated as distinct predictors in Equation 2, and so the coefficient estimated for each of those new predictors will indicate the added effect—above the main effects—of a risk having that combination of levels. In our example, this results in three additional predictors being added to our model: the combination of “sprinklered:yes” with each of occupancies 2, 3, and 4.

Running this model results in the output shown in Table 9. In this context, the coefficient of  $-0.2895$  for the main effect “sprinklered:yes” indicates a discount of 25.1% *for occupancy class 1*. The three interaction effects yield the effect of having a sprinkler for the remaining three occupancy groups *relative* to the sprinklered effect for group 1.

**Table 9. The Model with the Addition of the Interaction Term**

|                              | Estimate | Std. Error | p-Value |
|------------------------------|----------|------------|---------|
| (Intercept)                  | −10.8690 | 0.0189     | <0.0001 |
| occupancy:2                  | 0.2303   | 0.0253     | <0.0001 |
| occupancy:3                  | 0.4588   | 0.0271     | <0.0001 |
| occupancy:4                  | 0.0701   | 0.0273     | 0.0102  |
| sprinklered:Yes              | −0.2895  | 0.0729     | 0.0001  |
| occupancy:2, sprinklered:Yes | −0.2847  | 0.1014     | 0.0050  |
| occupancy:3, sprinklered:Yes | −0.0244  | 0.1255     | 0.8455  |
| occupancy:4, sprinklered:Yes | 0.2622   | 0.0981     | 0.0076  |

Looking at the row for the first interaction term, the negative coefficient indicates that occupancy class 2 should receive a steeper sprinklered discount than class 1; specifically, its indicated sprinklered factor is  $e^{-0.2895-0.2847}=0.563$ , or a 43.7% discount. The low  $p$ -value of 0.005 associated with that estimate indicates that the sprinklered factor for this class is indeed significantly different from that of class 1.

The interaction of occupancy class 3 with sprinklered shows a negative coefficient as well. However, it has a high  $p$ -value, indicating that the difference in sprinklered factors is not significant. Based on this, we may wish to simplify our model by combining class 3 with the base class for the purpose of this interaction.

The interaction term for occupancy class 4 has a significant positive coefficient of nearly equal magnitude to the negative coefficient of the main sprinklered effect. This result suggests that perhaps occupancy class 4 should not receive a sprinklered discount at all.

### 5.6.2. Interacting a Categorical Variable with a Continuous Variable

We extend the above example to add a continuous variable—amount of insurance (AOI)—to our frequency model. Following the practice discussed in Section 2.4.1, we will log AOI prior to inclusion in the model.

The main-effects model yields the estimates shown in Table 10. This model indicates a sprinklered factor of  $e^{-0.7167} = 0.488$ . The coefficient for log(AOI) indicates that the log of the mean frequency increases 0.416 for each unit increase in log(AOI)—or, equivalently, the frequency response to AOI (in real terms) is proportional to the power curve  $AOI^{0.4161}$ .

We now wish to test whether the AOI curve should be different for sprinklered versus non-sprinklered properties. To do so, we specify that we would like to add the interaction of sprinklered and log(AOI) to our model. The GLM fitting software adds a column to our design matrix that is the product of the indicator column for “sprinklered:Yes” and log(AOI). Thus, the resulting new predictor is 0 where sprinklered = No, and the log of AOI otherwise.

Running this GLM yields the output shown in Table 11. For this model, the coefficient for the log(AOI) main effect yields the AOI curve for risks of the base class

**Table 10. A Model with Occupancy Class, Sprinklered Status and AOI as Main Effects**

|                 | Estimate | Std. Error | $p$ -Value |
|-----------------|----------|------------|------------|
| (Intercept)     | −8.8431  | 0.1010     | <0.0001    |
| occupancy:2     | 0.2909   | 0.0248     | <0.0001    |
| occupancy:3     | 0.3521   | 0.0267     | <0.0001    |
| occupancy:4     | 0.0397   | 0.0266     | 0.1353     |
| sprinklered:Yes | −0.7167  | 0.0386     | <0.0001    |
| log(AOI)        | 0.4161   | 0.0075     | <0.0001    |

**Table 11. Adding the Interaction of AOI and Sprinklered Status**

|                           | Estimate | Std. Error | <i>p</i> -Value |
|---------------------------|----------|------------|-----------------|
| (Intercept)               | −8.9456  | 0.1044     | <0.0001         |
| occupancy:2               | 0.2919   | 0.0247     | <0.0001         |
| occupancy:3               | 0.3510   | 0.0266     | <0.0001         |
| occupancy:4               | 0.0370   | 0.0265     | 0.1622          |
| sprinklered:Yes           | 0.7447   | 0.3850     | 0.0531          |
| log(AOI)                  | 0.4239   | 0.0078     | <0.0001         |
| sprinklered:Yes, log(AOI) | −0.1032  | 0.0272     | 0.0001          |

of “sprinklered” (that is, risks for which sprinklered = “No”). The model also estimates a coefficient of  $-0.1032$  for the interaction term, which indicates that the rise of frequency in response to AOI is less steep for sprinklered properties than for non-sprinklered properties. The *p*-value indicates that this difference in curves is significant.

The positive coefficient estimated for “sprinklered:Yes” in this model may be a bit startling at first. Does this mean that a *premium* should now be charged for having a sprinkler?

Not quite. In interpreting the meaning of this, it is important to recognize that the model includes another variable that is non-zero for sprinklered properties—the interaction term, which captures the difference in the AOI *slope* between sprinklered and non-sprinklered risks. Thus, the main sprinklered effect may be thought of as an adjustment of the *intercept* of the AOI curve, or the indicated sprinklered relativity where  $\log(\text{AOI}) = 0$ .

Of course, where  $\log(\text{AOI})$  is zero, AOI is \$1—a highly unlikely value for AOI. The left panel of Figure 14 shows a graphical interpretation of this model’s indicated effects of AOI and sprinklered status. The *x*-axis is the log of AOI, and *y*-axis shows the (log) indicated relativity to the hypothetical case of a non-sprinklered property with an AOI of \$1. The two lines show the effect of AOI on log mean frequency: the slope of the “sprinklered” line is less steep than that of “non-sprinklered,” due to the negative coefficient of the interaction term.

The vertical gray stripe at the bottom left highlights what the main sprinklered effect coefficient refers to: it raises the sprinklered AOI curve at  $\log(\text{AOI}) = 0$ . However, as the AOI histogram overlaid on the graph shows,  $\log(\text{AOI}) = 0$  is way out of the range of the data, and so this “sprinklered surcharge” is just a theoretical construct, and no actual policy is likely to be charged such a premium.

An alternate way of specifying this model—one that leads to better interpretation—is to divide the AOI by the base AOI prior to logging and including it in the model. Supposing our chosen base AOI (which would receive a relativity of 1.00 in our rating plan) is \$200,000, we use  $\log(\text{AOI}/200,000)$  as the predictor in our model. The resulting estimates are shown in Table 12.

**Figure 14.** Illustration of the Effect of the Interaction of Sprinklered and Amount of Insurance (*left panel*) and the Same Model After Dividing AOI by Its Base Amount (*right panel*)

![Figure 14 consists of two panels. The left panel is a plot of log relativity (y-axis, 0 to 6) versus log(AOI) (x-axis, 0 to 15). It shows two lines: a solid line for 'Non-sprinklered' and a dashed line for 'Sprinklered'. The dashed line is below the solid line, indicating a lower relativity for sprinklered risks. A histogram of log(AOI) is shown in the bottom right corner. The right panel is a plot of log relativity (y-axis, -2 to 2) versus log(AOI/200,000) (x-axis, -4 to 4). It also shows two lines: a solid line for 'Non-sprinklered' and a dashed line for 'Sprinklered'. The dashed line is below the solid line. A horizontal dashed line at y=0 is labeled 'base rate', and a vertical dashed line at x=0 is labeled 'base AOI'. A gray vertical stripe is centered at x=0.](14294c70b5a0effb6bdaf09c46bbdc9f_img.jpg)

Figure 14 consists of two panels. The left panel is a plot of log relativity (y-axis, 0 to 6) versus log(AOI) (x-axis, 0 to 15). It shows two lines: a solid line for 'Non-sprinklered' and a dashed line for 'Sprinklered'. The dashed line is below the solid line, indicating a lower relativity for sprinklered risks. A histogram of log(AOI) is shown in the bottom right corner. The right panel is a plot of log relativity (y-axis, -2 to 2) versus log(AOI/200,000) (x-axis, -4 to 4). It also shows two lines: a solid line for 'Non-sprinklered' and a dashed line for 'Sprinklered'. The dashed line is below the solid line. A horizontal dashed line at y=0 is labeled 'base rate', and a vertical dashed line at x=0 is labeled 'base AOI'. A gray vertical stripe is centered at x=0.

This model is equivalent to the prior model; that is, they will both produce the same predictions. The sprinklered coefficient (now negative) still refers to the specific case where the value of the AOI predictor is zero—however, with the AOI predictor in this form it has a more natural interpretation: it is the (log) sprinklered relativity for a risk with the *base* AOI.

The right panel of Figure 13 illustrates the output of this model. (The  $x$ -axis in that panel spans only the values actually present in the data.) The gray stripe at center shows the main effect for sprinklered status, which is to lower the mean response at  $x = 0$  (the base AOI) by 0.5153 for sprinklered risks.

Note that in all this discussion, we described this interaction as “the slope of the AOI curve varying based on the sprinklered status.” Of course, it is just as valid to characterize it as “the sprinklered discount varying based on AOI.” Which way it is presented in the rating plan is a matter of preference.

**Table 12.** The Model of Table 11 with log AOI Centered at the Base AOI

|                                  | Estimate | Std. Error | $p$ -Value |
|----------------------------------|----------|------------|------------|
| (Intercept)                      | −3.7710  | 0.0201     | <0.0001    |
| occupancy:2                      | 0.2919   | 0.0247     | <0.0001    |
| occupancy:3                      | 0.3510   | 0.0266     | <0.0001    |
| occupancy:4                      | 0.0370   | 0.0265     | 0.1622     |
| sprinklered:Yes                  | −0.5153  | 0.0635     | <0.0001    |
| log(AOI/200000)                  | 0.4239   | 0.0078     | <0.0001    |
| sprinklered:Yes, log(AOI/200000) | −0.1032  | 0.0272     | 0.0001     |

As an aside, note that this last model form, with AOI centered at the base AOI, has an additional benefit: the intercept term (after exponentiating) yields the indicated frequency at the base case (i.e., when all variables are at their base levels). In general, for a GLM to have this property, all continuous variables need to be divided by their base values prior to being logged and included in the model.

### 5.6.3. Interacting Two Continuous Variables

To understand the third type of interaction—a continuous variable with another continuous variable—it is useful to visualize the combined effects of the variables on the log mean response as perspective plots, with the two variables shown along the  $x$ - and  $y$ -axes, and the relative log mean shown along the  $z$ -axis.

The left panel of Figure 15 graphs a scenario where two variables,  $x_1$  and  $x_2$ , are included in a model as main effects only, and the GLM indicates coefficients for them of 0.02 and 0.04, respectively. The response curve slopes for those two variables can be seen by following the front edge of the plane along the  $x$ - and  $y$ -axes; clearly,  $x_2$  has a steeper slope than  $x_1$ , which is due to its coefficient being larger. However, for any given value of  $x_2$ , the  $x_1$  curve, while in a different position vertically, has the same slope, and vice versa. As such, the effect of the two variables are independent of each other.

If we believe the slope for each variable should depend on the value of the other variable, we may include an interaction term. This term takes the form of the *product* of the two predictors. The right panel illustrates the case where the main effect coefficients are the same as before, but an added interaction term has a coefficient of 0.005. The slope of  $x_1$  where  $x_2 = 0$  (the front edge of the plane) is the same as in the left panel graph. However, moving inward, as  $x_2$  increases, we see the slope of  $x_1$  becomes more steep. Similarly, the slope of  $x_2$  steepens as  $x_1$  increases.

As with the earlier interaction types, the  $p$ -value estimated for the interaction term guides us in our determination of whether this effect is significant, or whether the variables should be left independent.

**Figure 15.** Perspective Plots of the Log Mean Response to Two Continuous Variables, both Without (*left*) and With (*right*) an Interaction Term

![Figure 15 consists of two 3D perspective plots side-by-side. Both plots have a vertical axis labeled 'log relativity' and two horizontal axes labeled 'x1' and 'x2'. The left plot shows a flat, rectangular grid representing a plane, indicating that the variables have independent main effects. The right plot shows a curved, saddle-shaped grid, indicating that the variables interact, as the slope of one variable changes depending on the value of the other.](6241b5db14cb0e67ec277832d1f1184c_img.jpg)

Figure 15 consists of two 3D perspective plots side-by-side. Both plots have a vertical axis labeled 'log relativity' and two horizontal axes labeled 'x1' and 'x2'. The left plot shows a flat, rectangular grid representing a plane, indicating that the variables have independent main effects. The right plot shows a curved, saddle-shaped grid, indicating that the variables interact, as the slope of one variable changes depending on the value of the other.

