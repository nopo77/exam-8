---
paper: goldburd_et_al
chapter: 10
title: "10. Variations on the Generalized Linear Model"
topics: [glmm, elastic_net, gam, mars, dglm, credibility_shrinkage, random_effects, non_linearity]
key_formulas: [glmm_random_effects_equation, elastic_net_penalty_function, dglm_dispersion_equation]
---
> **TL;DR**
> - GLMM: designates sparse categorical variable coefficients as random effects → shrinkage toward grand mean; analogous to Bühlmann-Straub credibility
> - DGLM: models per-record dispersion φᵢ in addition to μᵢ; useful when class-level volatility varies; approximated by alternating GLM iterations
> - GAM: replaces linear predictor terms with arbitrary smooth functions; captures non-linearity natively; effects must be assessed graphically, not from coefficients
> - MARS: automatically fits hinge functions with optimal cut points; performs variable selection and searches for interactions; output can be replicated in a standard GLM
> - Elastic net: minimizes deviance + λ(α∑|β| + (1−α)/2∑β²); λ tuned via CV; shrinkage, variable selection, and robustness to correlated predictors

# 10. Variations on the Generalized Linear Model

As we have seen in the preceding sections, the GLM is a flexible, robust and highly interpretable model that can accommodate many different types of target variables and covariate relationships. However, it does have a number of shortcomings, most notably:

- Predictions must be based on a linear function of the predictors. Certainly, there are workarounds to handle non-linearity (such as polynomials or hinge functions) but those must be explicitly specified by the modeler.
- GLMs exhibit instability in the face of thin data or highly correlated predictors.
- Full credibility is given to the data for each coefficient, with no regard to the thinness on which it is based.
- GLMs assume the random component of the outcome is uncorrelated among risks.
- The exponential family parameter  $\phi$  must be held constant across risks.

Many of the more advanced predictive modeling techniques used by data scientists in other disciplines, such as *neural nets*, *random forests* or *gradient boosting machines*, do not have these flaws, and are therefore able to produce stronger models that yield more accurate predictions. However, using those methods would entail a huge loss of interpretability, which, for many actuarial applications, is as great a necessity as predictive accuracy, if not greater.

Fortunately, a number of extensions to GLMs have been developed that address some of the limitations noted above. We *briefly* discuss some of them in this section. As each of the models presented here is either based on the GLM framework or something very similar, using them sacrifices little or no loss in interpretability, while potentially yielding increased flexibility, robustness and accuracy.

We caution that the discussions below are meant to be brief overviews of these models, and are intended to introduce the reader to them and motivate further learning. Each has many nuances and complexities not covered here, and the reader is urged to refer to other statistical texts that cover these methods in greater detail prior to attempting to use them in a real business scenario.

## 10.1. Generalized Linear Mixed Models (GLMMs)

In a standard GLM, the randomness of the outcome is considered to be the only source of randomness in the model; the coefficients themselves are assumed to be fixed values. To be sure, from *our* perspective, where the coefficients are unknown

and will need to be estimated from random data, the estimates of those parameters are random. (This is the randomness that statistics such as the standard error are meant to describe.) However, the underlying model assumes that *some* fixed set of values exist that always describe the relationship between the predictors and the expected value of the target variable. To see this, take a look back at Equation 2: the equals sign indicates a deterministic relationship involving fixed values; the only tilde (denoting randomness) appears in Equation 1.

The practical effect of this is that in seeking to maximize likelihood, the fitting procedure “moves” the coefficients as close to the data as possible, even for those where the data is thin. In other words, it gives the data full credibility, since we have not supplied it with any information to signal that the coefficients should behave otherwise.

A useful extension to the GLM is the **generalized linear mixed model**, or GLMM, which allows for some of the coefficients to be modeled as random variables themselves. In this context, predictors with coefficients modeled as random variables are called **random effects**; parameters modeled as having fixed values are called **fixed effects**. In practice, random effects would be estimated for categorical variables with many levels that lack the credibility for their coefficients to be estimated fully from their own data.

To illustrate, we present a simple example of an auto severity model with three predictors: driver age (a continuous variable), marital status (coded as 0 = unmarried, 1 = married) and territory, a categorical variable with 15 levels. Driver age and marital status will be designated as fixed effects in our model; territory, with many of its levels sparse and lacking credibility, will be designated as a random effect.

We denote driver age as  $x_1$  and marital status as  $x_2$ . The territory variable is transformed to 15 dummy-coded (0/1) variables of a design matrix, where 1 indicates membership in that territory.<sup>22</sup> Rather than denote those 15 predictors as  $x_3 \dots x_{17}$ , we will use a new symbol—namely,  $z$ —to distinguish random effects from fixed effects, and so the territory variables are denoted  $z_1 \dots z_{15}$ . The coefficients for the fixed effects are denoted  $\beta_1, \beta_2$ , and the coefficients for the random effects are denoted  $\gamma_1 \dots \gamma_{15}$ .

A typical setup for this model might be as follows:

$$g(\mu_i) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \gamma_1 z_1 + \dots + \gamma_{15} z_{15} \quad (19)$$

$$y \sim \text{gamma}(\mu_i, \phi) \quad (20)$$

$$\gamma \sim \text{normal}(\nu, \sigma) \quad (21)$$

Equations 19 and 20 are the familiar fixed and random components of a regular GLM. Equation 21 introduces a probability distribution for the fifteen  $\gamma$  parameters, which are taken to be independent and identically distributed random variables in this model. (The normal distribution is used here for illustrative purposes; depending on the implementation, a different distribution may be used.)

<sup>22</sup> For random effects we do not designate a base level, and so all 15 levels get a column in the design matrix.

In maximizing likelihood for this setup, we now have *two* probability distributions to simultaneously consider: the distribution of outcomes  $y$  of Equation 20, and the distribution of random coefficients  $\gamma$  of Equation 21. Moving any of the  $\gamma$  coefficients close to the data raises the likelihood of  $y$ , while moving it away from the mean of the other  $\gamma$ s lowers the likelihood of  $\gamma$ . In being forced to balance those two opposing forces, the model will produce territory relativities that are somewhere between the full-credibility estimates of a GLM and the grand mean for territory. The less data available for a territory, the closer its estimate will be to the mean. This effect is referred to as **shrinkage**.

Figure 27 shows an example of the estimates produced by a GLMM compared with those estimated by a standard GLM. The dotted line shows the grand mean log relativity across all territories. For territories where the data is the sparsest—and the standard errors the widest—the GLMM estimates move farther from the GLM indications and closer toward the mean.

In practice, GLMMs are estimated as a two-step process. First, estimates of all the “fixed” parameters underlying the model are produced. For the fixed effects, this stage would produce actual estimates of the coefficient; for the random effects, on the other hand, this stage produces estimates related to the probability distribution that their coefficients follow. The second stage produces estimates for all levels of categorical variables that were specified as random effects. These estimates use a Bayesian procedure that factors in the estimated randomness of the parameter as estimated by the first step as well as the volume of data available at each level.

In our example, the initial fitting procedure produces estimates for the following parameters: the intercept,  $\beta_0$ ; the coefficients for the fixed effects,  $\beta_1$  and  $\beta_2$ ; the

**Figure 27.** A comparison of GLM and GLMM estimates. The filled squares show the GLM estimates, and the error bars indicate the 95% confidence intervals around those estimates. The unfilled squares show the GLMM estimates. The vertical bars are proportional to the volume of data within each territory.

![Figure 27: A comparison of GLM and GLMM estimates. The plot shows estimates for 10 territories. The y-axis is 'Estimate' ranging from -1.5 to 1.5. The x-axis is 'Territory' from 1 to 10. A horizontal dotted line at approximately -0.4 represents the 'grand mean'. For each territory, there are two data points: a GLM estimate (filled square) and a GLMM estimate (unfilled square). Error bars representing 95% confidence intervals are shown for the GLM estimates. The GLMM estimates are generally closer to the grand mean than the GLM estimates, especially for territories with smaller data volumes (indicated by shorter vertical bars).](30c3f67945e143cf60f6cd55a56525fe_img.jpg)

| Territory | GLM estimate | GLMM estimate |
|-----------|--------------|---------------|
| 1         | 0.2          | -0.2          |
| 2         | -0.2         | -0.2          |
| 3         | -0.8         | -0.2          |
| 4         | 0.2          | -0.2          |
| 5         | -0.6         | -0.6          |
| 6         | 0.2          | -0.2          |
| 7         | -0.6         | -0.6          |
| 8         | -0.4         | -0.4          |
| 9         | -0.6         | -0.6          |
| 10        | -0.2         | -0.2          |

Figure 27: A comparison of GLM and GLMM estimates. The plot shows estimates for 10 territories. The y-axis is 'Estimate' ranging from -1.5 to 1.5. The x-axis is 'Territory' from 1 to 10. A horizontal dotted line at approximately -0.4 represents the 'grand mean'. For each territory, there are two data points: a GLM estimate (filled square) and a GLMM estimate (unfilled square). Error bars representing 95% confidence intervals are shown for the GLM estimates. The GLMM estimates are generally closer to the grand mean than the GLM estimates, especially for territories with smaller data volumes (indicated by shorter vertical bars).

dispersion parameter,  $\phi$ ; and the parameters related to the *distribution* of the  $\gamma$  coefficients—namely,  $\nu$  and  $\sigma$ . Note that at this stage, the  $\gamma$  coefficients themselves have not been estimated; we’ve only estimated their distribution.

A second stage will produce the estimates of the  $\gamma$  coefficients. Rather than basing the estimate for each territory entirely on its own data—as a regular GLM would do—the GLMM estimates will incorporate several pieces of information: the observed severity within the territory; the estimated distribution of the  $\gamma$  parameters; and the estimated variance of  $y$ . Generally, estimates for more dense levels will be closer to those indicated by the data, while estimates for more sparse levels are driven closer to the overall mean.

If any of this seems eerily similar to Bühlmann-Straub credibility, that’s because it is. In fact, the variance of the  $\gamma$  distribution—denoted  $\sigma$  above—is analogous to the familiar credibility concept of “between-variance” among the theoretical means; residual variance in the model—represented by  $\phi$ —corresponds to the “within-variance.” The estimated  $\gamma$  for each territory will in effect be a blend between the grand mean severity among territories ( $\nu$ ) and the territory’s own observed severity, with the weighting determined based on the expected “within-variance” given the volume of data in the territory, relative to the “between-variance.” Thus, the GLMM is a useful means of introducing classical credibility concepts into a GLM for multi-level categorical variables.<sup>23</sup>

**Correlation Among Random Outcomes.** In addition to allowing for credibility, the GLMM is also a means of inducing correlation into a model. Consider the case where a multi-year dataset may contain multiple renewals of the same policy. If we are concerned that the correlation among policy records is large enough so as to distort the GLM results, we may wish to include policy ID as a random effect in a GLMM. In this instance, although the GLMM will produce an estimate for each policy ID, those are probably not of interest to us.

## 10.2. GLMs with Dispersion Modeling (DGLMs)

Recall that a constraint built into GLMs is that the dispersion parameter of the exponential family ( $\phi$ ) must be held constant for all records. An extension to the GLM that loosens up this restriction is a GLM with a **dispersion modeling** component, which allows for each record to have a unique  $\phi$  as well as  $\mu$ , controlled by a linear combination of coefficients and predictors. Those predictors may be the same as those that predict the  $\mu$  parameter, or they may be different. This type of model is sometimes called a **double-generalized linear model** (or **DGLM**).<sup>24</sup>

The mathematical specification of a DGLM is as follows:

$$y_i \sim \text{Exponential}(\mu_i, \phi_i) \quad (22)$$

$$g(\mu_i) = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} \quad (23)$$

<sup>23</sup> See Klinker (2011a) for a more detailed discussion on the relationship between classical credibility and GLMMs.

<sup>24</sup> Smyth and Jørgensen (2002).

$$g_d(\phi_i) = \gamma_0 + \gamma_1 z_{i1} + \gamma_2 z_{i2} + \cdots + \gamma_n z_{ip} \quad (24)$$

Equation 22 is similar to Equation 1, with a subtle difference: the  $\phi$  parameter now has a subscript  $i$  attached to it, indicating that it may vary by record. Equation 23 is identical to Equation 2.

The chief innovation of the DGLM is Equation 24, which specifies the relationship between the dispersion parameter and the predictors  $z_1 \dots z_p$ , which may or may not be the same as the  $\mu$  predictors,  $x_1 \dots x_p$ . Coefficients for  $z_1 \dots z_p$ —denoted here as  $\gamma_1 \dots \gamma_p$ —are estimated by the model. The linear combination of those predictors and coefficients equals the dispersion parameter transformed by a link function, denoted here as  $g_d(\cdot)$ . The subscript  $d$  is added to distinguish it from the link function applied to  $\mu$  in Equation 23, since those two need not be the same; in practice, though, it is common to use a log link for both.

**Implementation.** DGLMs are implemented in the “dglm” package available for both the R and S-Plus statistical languages. However, where the distribution is a member of the Tweedie family (that is, either the normal, Poisson, gamma, inverse Gaussian or Tweedie distribution), the DGLM parameters can be closely approximated using any GLM estimation software with the following iterative procedure:<sup>25</sup>

1. Begin by assigning a value of 1 to all  $\phi_i$ .
2. Run a GLM to estimate the  $\beta$  coefficients as usual, but with one modification: the weight variable should be the inverse of the dispersion parameter for each record—that is,  $1/\phi_i$ . If we wish to use a weight in the model, we must divide it by  $\phi$  (i.e., set the weight variable to  $\omega_i/\phi_i$ ).
3. Using the predictions generated by the model estimated in step 2, calculate the *unit deviance* for each record. The unit deviance is defined as:

$$d_i = 2\phi_i [\ln f(y_i | \mu_i = y_i) - \ln f(y_i | \mu_i = \hat{\mu}_i)]$$

Note that this formula is the record’s contribution to the total unscaled deviance described in Section 6.1.2.<sup>26</sup>

4. Run a GLM specified as follows:
  - The target variable is the unit deviance calculated in step 3.
  - The distribution is gamma.
  - As predictors, use whatever variables we believe may affect dispersion. These are the  $z$  variables of Equation 24, which may or may not be the same as the main GLM predictors.

<sup>25</sup> Smyth and Jørgensen (2002).

<sup>26</sup> For the Tweedie distribution, that formula works out to be the following:

$$d_i = 2\omega_i \left( y_i \frac{y_i^{1-p} - \mu_i^{1-p}}{1-p} - \frac{y_i^{2-p} - \mu_i^{2-p}}{2-p} \right)$$

where  $\omega$  denotes the weight variable.

5. Set the dispersion parameters  $\phi_i$  to be the predictions generated by the model of step 4.
6. Repeat steps 2 through 5 until the model converges (that is, the model parameters cease to change significantly between iterations).

**Where to Use It.** In a general sense, using a DGLM rather than a GLM may produce better predictions of the mean, particularly in cases where certain classes of business are inherently more volatile than others. Allowing the dispersion parameter to “float” will in turn allow the model to give less weight to the historical outcomes of the volatile business, and more weight to the stable business whose data is more informative—thereby ignoring more noise and picking up more signal.

The following are particular scenarios where using a DGLM rather than a GLM may provide additional benefit:

- For some actuarial applications, the full distribution of the outcome variable, rather than just the mean, is desired. In such scenarios, a GLM with constant dispersion may be too simplistic to adequately describe the distribution. The DGLM, on the other hand, models two distributional parameters for each risk and thereby has greater flexibility to fit the distributional curves.
- GLMs that use the Tweedie distribution to model pure premium or loss ratio, by keeping the dispersion parameter constant, contain the implicit assumption that all predictors have the same directional effect on frequency and severity. (See Section 2.7.3 for further discussion on this.) The DGLM, on the other hand, by allowing the dispersion parameter to vary, provides the flexibility for the model to mold itself to the frequency and severity effects observed in the data.

## 10.3. Generalized Additive Models (GAMs)

As noted in the introduction to this chapter, a hallmark assumption of the GLM is linearity in the predictors. While non-linear effects can be accommodated by adding various transformations of the predictors into the linear equation, those are workarounds that must be specified manually.

The **generalized additive model** (GAM) is a GLM-like model that handles non-linearity natively. The mathematical specification of a GAM is as follows:

$$y_i \sim \text{Exponential}(\mu_i, \phi) \quad (25)$$

$$g(\mu_i) = \beta_0 + f_1(x_{i1}) + f_2(x_{i2}) + \cdots + f_p(x_{ip}) \quad (26)$$

Equation 25 is identical to equation 1. GAMs, like GLMs, assume the random component of the outcome to follow an exponential family distribution.

Equation 26 is similar to equation 2, but with an important twist: the addends making up the linear predictor are no longer linear functions of the predictors—rather, they are

any arbitrary functions of the predictors. Those functions, denoted  $f_1(\cdot) \dots f_n(\cdot)$  specify the effects of the predictors on the (transformed) mean response as smooth curves. The shapes of these curves are estimated by the GAM software.

Note that the “additive” of “generalized additive model” refers to the fact that the linear predictor is a series of additive terms (though free from the constraint of linearity). As with a GLM, we can specify a log link, which would turn the model multiplicative.

Unlike in a GLM, where the effect of a variable on the response can be easily determined by examining its coefficient, for a GAM we are provided no such convenient numeric description of the effect. As such, predictor effects must be assessed graphically. Figure 28 shows examples of such graphs, using the example severity model discussed back in Section 5.4. For this illustration, two continuous variables—building age and amount of insurance, both logged—are included in a log link GAM, and their estimated smooth functions are graphed in the left and right panels, respectively.

For building age, the GAM estimated a clearly non-linear function, with mean severity first rising, reaching a peak at around building age  $e^{2.8} = 16$  years, then declining. (Compare this to Figures 10 and 11.) For amount of insurance, on the other hand, although the GAM was free to fit any arbitrary function, the one it estimated is nearly linear (albeit with some curvature), indicating that a linear fit would probably suffice for this variable.

The GAM allows us to choose from among several different methods for estimating the smooth functions; we will not delve into those details here. Each of those methods allows us to specify parameters that control the degree of smoothness for each function. Those parameters must be fine-tuned carefully, as allowing for too-flexible a function runs the risk of overfitting.

**Implementation.** GAMs are available through the R packages “gam” or “mgcv,” or through PROC GAM in SAS.

**Figure 28.** Graphical Display of GAM Smoother Functions for Log of Building Age (*left panel*) and Log of Amount of Insurance (*right panel*)

![Figure 28: Graphical Display of GAM Smoother Functions. The figure consists of two side-by-side line graphs. The left graph shows the smooth function for log(building age), with the x-axis labeled 'log(building age)' ranging from 1.5 to 3.5 and the y-axis labeled 'smooth function' ranging from 1.5 to 4.0. The curve starts at approximately (1.5, 1.8), rises to a peak of about 3.5 at x=2.8, and then declines to about 2.8 at x=3.5. The right graph shows the smooth function for log(aoi), with the x-axis labeled 'log(aoi)' ranging from 10 to 18 and the y-axis labeled 'smooth function' ranging from 4 to 9. The curve starts at approximately (10, 4.2) and rises in a nearly straight line to about (18, 9.0).](3309ddcf0507a77ef8c0984c100f80ec_img.jpg)

Figure 28: Graphical Display of GAM Smoother Functions. The figure consists of two side-by-side line graphs. The left graph shows the smooth function for log(building age), with the x-axis labeled 'log(building age)' ranging from 1.5 to 3.5 and the y-axis labeled 'smooth function' ranging from 1.5 to 4.0. The curve starts at approximately (1.5, 1.8), rises to a peak of about 3.5 at x=2.8, and then declines to about 2.8 at x=3.5. The right graph shows the smooth function for log(aoi), with the x-axis labeled 'log(aoi)' ranging from 10 to 18 and the y-axis labeled 'smooth function' ranging from 4 to 9. The curve starts at approximately (10, 4.2) and rises in a nearly straight line to about (18, 9.0).

## 10.4. MARS Models

Another GLM variant that is great at handling non-linearities is **multivariate adaptive regression splines**, or MARS. Rather than fit smooth functions for the predictors, as does the GAM discussed in the preceding section, MARS models operate by incorporating piecewise linear functions, or *hinge functions*, into a regular GLM. These hinge functions are the same as those discussed in Section 5.4.4. However, in that section we manually created the functions and determined cut points by eyeballing partial residual plots; MARS models create the functions and optimize the cut points automatically.

To illustrate, we continue with our example severity model of the previous section. This time, we will use a MARS model to capture potential non-linearity in the building age and amount of insurance variables. Table 14 shows the portion of the resulting coefficient table relating to those two variables.

In the output below, the function  $h(\cdot)$  refers to the “hinge function” discussed in Section 5.4.4. For example, “ $h(\log(\text{AoC})-1.94591)$ ” is defined as  $\max(\log(\text{AoC})-1.94591, 0)$ .

Looking at the three hinge functions for building age, notice that this handling of that variable is fairly similar to the piecewise linear functions we set up in Section 5.4.4, which had cut points at 2.75 and 3.5. The MARS model also found another cut point at 1.95. MARS did not include the unaltered  $\log(\text{AoC})$  term in this model, meaning that the response curve for  $\log(\text{AoC})$  below 1.95 is flat. (In a practical sense, that means this model would not differentiate between buildings of ages 1 to 7 years.)

Figure 29 graphs the response curves indicated by this model for those two variables. The  $\times$ ’s mark the locations of the cut points. Compare those to the curves indicated by the GAM output of the previous section.

As with GAMs, MARS has tuning parameters to control the flexibility of the fit. A more flexible model will create more cut points, allowing for finer segmentation. Of course, with that additional flexibility comes the risk of chasing noise.

**Table 14. Partial Output of MARS Coefficient Table**

| Parameter             | Estimate | Std. Error | <i>p</i> -Value |
|-----------------------|----------|------------|-----------------|
| ...                   | ...      | ...        | ...             |
| ‘h(log(AoC)–1.94591)’ | 1.8977   | 0.1976     | <0.0001         |
| ‘h(log(AoC)–2.70805)’ | –2.9557  | 0.2598     | <0.0001         |
| ‘h(log(AoC)–3.46574)’ | 1.2980   | 0.3457     | 0.0002          |
| ‘h(log(AOI)–9.39124)’ | 0.3949   | 0.0359     | <0.0001         |
| ‘h(log(AOI)–13.2124)’ | 0.0611   | 0.0657     | 0.3526          |
| ‘h(log(AOI)–15.7578)’ | 0.7151   | 0.2263     | 0.0016          |
| ...                   | ...      | ...        | ...             |

**Figure 29.** Graphical display of MARS indicated relativities for log of building age (*left panel*) and log of amount of insurance (*right panel*). The x's mark the locations of the cut points.

![Figure 29: Two line graphs showing MARS indicated relativities. The left panel shows log relativity vs log(building age) with a peak at x=2.7. The right panel shows log relativity vs log(aoi) with a steady increase.](3ae8c7e35a46d9336931efdd39c3760c_img.jpg)

The figure consists of two side-by-side line graphs. Both graphs have 'log relativity' on the y-axis and a log-transformed variable on the x-axis. 'x' marks indicate the locations of cut points where the slope of the line changes.

**Left Panel:** The x-axis is labeled 'log(building age)' with tick marks at 1.5, 2.5, and 3.5. The y-axis has tick marks at 0.0, 0.5, and 1.0. The line starts at (1.5, 0.0), rises to a peak at (2.7, 1.2), then falls to (3.5, 0.6), and finally rises slightly to (4.0, 0.8).

**Right Panel:** The x-axis is labeled 'log(aoi)' with tick marks at 10, 12, 14, 16, and 18. The y-axis has tick marks from 0 to 6 in increments of 1. The line starts at (10, 0), rises to (13, 1.5), then to (16, 2.8), and finally to (18, 5.5).

Figure 29: Two line graphs showing MARS indicated relativities. The left panel shows log relativity vs log(building age) with a peak at x=2.7. The right panel shows log relativity vs log(aoi) with a steady increase.

In addition to its natural ability to handle non-linearities, MARS has a number of additional highly useful features, including:

- It performs its own variable selection. Unlike a GLM—which will generate a coefficient for each predictor input by the user—MARS will keep only those that are significant. (Tuning parameters are available to control how many variables are retained.)
- It can also search for significant interactions. It is quite flexible in this regard; in addition to the 2-way interactions discussed in Section 5.6, it can search for 3-way (or higher degree) interactions, as well as interactions among the piecewise linear functions.

Even where we require our final model to be in the form of a standard GLM, MARS may still be a very valuable tool in the model refinement process: we can run a MARS model on the data, examine its output—hinge functions it created, interactions it discovered, and so on—and copy whichever terms we like into our GLM. Consider the output shown in Table 14; it is very easy to simply replicate those same hinge functions in our GLM, and get the same benefit of the non-linear fit.

Used in this way, MARS may uncover non-linear transformations or interactions we may not have thought to try. Great care needs to be taken, though, as such a “deep search” through the data can easily turn up spurious effects.

**Implementation.** MARS is available as commercial software from Salford Systems. Implementations of the same procedure (not called *MARS*, due to Salford Systems’ trademark on the name) are available through the “earth” package in R and PROC ADAPTIVEREG in SAS (beginning with SAS/STAT version 13.1).

## 10.5. Elastic Net GLMs

When modeling in situations where there are a large number of potential predictor variables, overfitting can be a real concern for GLMs. GLMs make full use of all the

predictors fed into them to fit the training data as best as possible—that is, it will find coefficients for all predictors such that the deviance of the training set is minimized. Including too many predictors will cause the model to pick up random noise in the training data, yielding a model that may perform poorly on unseen data. In such a scenario, variable selection—choosing the right variables to include in the model while omitting the others—can be quite challenging.

**Elastic net** GLMs provide a powerful means of protecting against overfitting even in the presence of many predictors. Elastic nets GLMs are, at the core, identical to GLMs in their mathematical specification. The chief difference is in the method by which the coefficients are fit. Rather than aggressively minimizing deviance on the training set—as a regular GLM would—elastic nets enable you to constrain the fit, by minimizing a function that is deviance subject to a penalty term for the size and magnitude of the coefficients. This penalty term can be fine-tuned to allow you to find the right balance where the model fits the training data well—but at the same time, the coefficients of the model are not too large.

The function minimized by elastic nets is as follows:<sup>27</sup>

$$\text{Deviance} + \lambda \left( \alpha \sum |\beta| + (1 - \alpha) \frac{1}{2} \sum \beta^2 \right) \quad (27)$$

The first additive term of the above expression is just the GLM deviance; if this were a regular GLM, we'd be minimizing just that. The elastic net adds the part following the plus sign, called the *penalty term*. Let's examine that closely.

Inside the parentheses is a weighted average of the sum of the absolute values of the coefficients and the halved sum of squared coefficients, with the weights determined by  $\alpha$ , a parameter between 0 and 1 that we control. This use of a weighted average is primarily due to the fact that this model is a generalization of two earlier variations on this same concept: the **lasso** model, which uses absolute value of coefficients, and **ridge** model, which uses squared coefficients. The important thing to recognize, though, is that the terms inside the parentheses yield an increasing function of the *magnitude* of the coefficients, or the degree by which the coefficients deviate from zero. Thus, a greater penalty is applied for larger coefficients.<sup>28</sup>

The more important tuning parameter in Equation 27 is the  $\lambda$  that sits outside the parentheses. This allows us to control the severity of the penalty that gets applied. The practical effect of raising  $\lambda$  is that it forces coefficients to shrink closer to zero, to compensate for the increased penalty, in minimizing Equation 27. Under certain

<sup>27</sup> In Equation 27, the vector of coefficients represented by  $\beta$  does not include  $\beta_0$ , the intercept term, which does not contribute to the penalty.

<sup>28</sup> In elastic net models, all predictor variables are automatically centered and scaled prior to running the model. This way, the resulting  $\beta$  coefficients are on similar scales, and so the magnitude of deviation from zero means roughly the same thing for all variables, regardless of the scales of the original variables. Note, however, that most implementations of elastic nets will return the coefficients on the scales of the original variables, so this standardization that happens behind the scenes poses no obstacle to implementation of the resulting model.

**Figure 30.** An Illustration of the Effect of Varying  $\lambda$  on Elastic Net Coefficients

![Figure 30: A line graph showing the effect of varying the penalty parameter lambda on the coefficients of five predictors (Var A, Var B, Var C, Var D, Var E). The y-axis is labeled 'Coefficients' and ranges from -0.05 to 0.15. The x-axis is labeled 'decreasing lambda ->' and points to the right. Five curves are shown: Var A (solid black), Var B (dashed black), Var C (dotted black), Var D (solid grey), and Var E (dashed grey). All curves start at zero for high lambda and increase as lambda decreases. Var E increases most rapidly, followed by Var B, Var C, Var A, and Var D. Var D is the only curve that decreases below zero as lambda decreases.](dbc7dd1650a1d26458600aac48198df6_img.jpg)

Figure 30: A line graph showing the effect of varying the penalty parameter lambda on the coefficients of five predictors (Var A, Var B, Var C, Var D, Var E). The y-axis is labeled 'Coefficients' and ranges from -0.05 to 0.15. The x-axis is labeled 'decreasing lambda ->' and points to the right. Five curves are shown: Var A (solid black), Var B (dashed black), Var C (dotted black), Var D (solid grey), and Var E (dashed grey). All curves start at zero for high lambda and increase as lambda decreases. Var E increases most rapidly, followed by Var B, Var C, Var A, and Var D. Var D is the only curve that decreases below zero as lambda decreases.

conditions, some less-important predictors will be assigned coefficients of zero (effectively removing them from the model entirely).

In Figure 30 we illustrate this effect for a simple model that has five predictors, which we name A through E. Each predictor is represented by a different curve. For each, the value that the coefficient assigns to the predictor is plotted on the  $y$ -axis for different values of  $\lambda$ , with  $\lambda$  *decreasing* from left to right along the  $x$ -axis.

At the far left of the graph—where  $\lambda$  is at its highest—the penalty for coefficient size is severe, and so no variables make it in with a non-zero coefficient. As we move rightward, dialing down  $\lambda$  and thereby easing up on the penalty, Variable E—clearly the most significant variable here—enters our model and grows in influence as  $\lambda$  declines. Moving farther to the right, more variables make their way in and their coefficients grow—eventually converging toward the maximum likelihood estimates that a regular GLM would give them.

In practice, the  $\lambda$  parameter is usually fine-tuned through cross validation. Doing so produces a model that is likely to perform better on unseen data than would a regular GLM. After all, a GLM is just a special case of the elastic net (where  $\lambda = 0$ ) and so the fine-tuning procedure has the flexibility to produce a standard GLM if in fact it is the best model. Usually, though, the model can be improved by setting a non-zero penalty.

As we have seen, a non-zero penalty causes the model parameters to exhibit the shrinkage effect that is characteristic of actuarial credibility models as well as GLMMs discussed above. In fact, it has been shown that elastic nets bear direct relationships to many classical credibility models.<sup>29</sup> Thus, as with GLMMs discussed above, elastic nets provide a convenient means of incorporating familiar credibility concepts into the GLM framework.

<sup>29</sup> See Miller (2015) for further discussion on this equivalence and its derivation.

Elastic nets also have the advantage of being able to perform automatic variable selection, as variables that are not important enough to justify their inclusion in the model under the penalty constraint will be removed.

Furthermore, elastic nets perform much better than GLMs in the face of highly correlated predictors. The penalty term provides protection against the coefficients “blowing up” as they might in a GLM. Rather, one or two variables of a group of correlated predictors will typically be selected, and they will be assigned moderate coefficients.

The main disadvantage of elastic nets is that they are much more computationally complex than standard GLMs. The computational resources and time needed to fit elastic nets and optimize  $\lambda$  may make elastic nets impractical for large datasets.

**Implementation.** Elastic nets are implemented in the “glmnet” package in R.<sup>30</sup> It is also available in SAS (beginning with SAS/STAT version 13.1) using PROC GLMSELECT.

---

<sup>30</sup> As of this writing, the glmnet package does not support the gamma or Tweedie distributions. Fortunately, the “HDTweedie” package provides an implementation of glmnet for the Tweedie distribution; the gamma distribution is accessible through this package by setting the Tweedie  $p$  parameter to be 2.

