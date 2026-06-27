---
paper: holmes_&_casotto
chapter: 3
title: Penalized Regression
topics: [penalized_regression, lasso, ridge_regression, elastic_net, penalty_parameter, sparsity, variable_selection, cross_validation]
key_formulas: [penalized_regression_formula, ridge_penalty, lasso_penalty, elastic_net_penalty, ridge_solution, lasso_soft_thresholding]
---

> **TL;DR**
> - Penalized regression: β̂ = argmin[NLL(y,X,β) + λ·Penalty(β)]; λ = 0 recovers a standard GLM; large λ shrinks all coefficients toward zero.
> - Ridge (L2): penalty = ½Σβⱼ²; shrinks all coefficients proportionally toward zero but never exactly to zero; handles correlated variables well.
> - Lasso (L1): penalty = Σ|βⱼ|; sets low-signal coefficients exactly to zero — achieves sparsity and performs automatic variable selection.
> - Elastic net blends ridge and lasso via hyperparameter α; lasso is recommended for most actuarial applications due to sparsity, interpretability, and responsiveness.
> - λ is selected by k-fold cross-validation (maximize Gini/deviance on holdout folds); actuarial judgment may favor a marginally higher λ than the cross-validation optimum for stability and conservatism.

# 3. Penalized Regression

We introduce penalized regression first via the general penalization formula so that we can then focus on the three most popular penalization methods: lasso, ridge, and elastic net. After highlighting the differences with and similarities to unpenalized GLMs, we describe guidelines to use when selecting and analyzing the result of a penalized model. Finally, we explain the rationale behind using the **lasso** penalty for actuarial analysis owing to its unique ability to create a **sparse** and parsimonious model.

## 3.1. Types of Penalized Regression

In Section 1.6, we saw that GLM estimates always attribute 100% credibility to the data, regardless of the underlying exposure. The reason lies in maximizing the likelihood formula, which targets the goodness of the fit alone as described in Section A.1.

Penalized regression slightly modifies the likelihood formula by adding a **penalty** term to the GLM optimization, thereby adding a credibility component to the cost function that the unpenalized GLM was missing. Penalized regression **jointly** optimizes the trade-off between

- goodness of fit (likelihood) and
- prior assumptions on the shape of the coefficients (penalty).

When we design the penalty, we can design it to favor models with desirable properties, such as a low number of parameters. This effectively adds a credibility component to the cost function and regularizes the likelihood.

The following is the general formula for penalized regression:<sup>3</sup>

$$\begin{aligned}\hat{\beta} &= \operatorname{argmin}_{\beta} -\operatorname{LogLikelihood}(y, X, \beta) + \lambda \operatorname{Penalty}(\beta) \\ &= \operatorname{argmin}_{\beta} \operatorname{NLL}(y, X, \beta) + \lambda \operatorname{Penalty}(\beta).\end{aligned}\tag{3.1}$$

In the formula,  $\lambda \geq 0$  is a positive number, referred to as the **penalty parameter**. The penalty parameter  $\lambda$  plays the role of a dial that assigns more or less importance

---

<sup>3</sup> Different formulations of the penalized regression can be found in the literature and in open-source solvers. For example, often the negative log-likelihood (NLL) is normalized by the number of observations  $n$ . In all cases, the formulas are equivalent after a reparameterization of the parameter (for example  $\lambda \rightarrow \frac{\lambda}{n}$ ).

to the goodness of fit of the model in the training database or to the prior structure of the coefficients.

Penalized regression is a well-established technique in machine learning with a massive amount of accompanying research and literature. This section gives only a very basic introduction to the topic, and we refer readers to Hastie, Tibshirani, and Friedman (2009) and van Wieringen (2015) for a more in-depth (and mathematically dense) treatment of the subject. Wüthrich and Merz's (2023) book and the final chapter of Goldburd et al. (2016) discuss penalized regression from an actuarial perspective.

There are three main, established types of penalties:

- The **ridge** penalty is given by the sum of squares (or l2 squared norm) of  $\beta$ , that is,

$$\text{Ridge}(\beta) = \frac{1}{2} \sum_{j=1}^p \beta_j^2 = \frac{1}{2} \|\beta\|_2^2.$$

- The **lasso** penalty is given by the sum of the absolute values (or l1 norm) of  $\beta$ , that is,

$$\text{Lasso}(\beta) = \sum_{j=1}^p |\beta_j| = \|\beta\|_1.$$

- The **elastic net** penalty is a blend of both the ridge and the lasso penalties, linearly combined via a user-defined parameter  $0 < \alpha < 1$ :

$$\text{Elastic Net}_\alpha(\beta) = \frac{1-\alpha}{2} \sum_j \beta_j^2 + \alpha \sum_j |\beta_j|.$$

Penalized regression techniques such as the lasso and the ridge are at their core very similar to GLMs in their mathematical specification (Goldburd et al. 2016) in that they preserve the same underlying structure:

- The estimated parameter is related to a **linear combination** of the explanatory variables by a **link function** (Section 1.2).
- Observations are assumed to follow a **distribution** around the estimated parameter (Section 1.3).
- The **table-based output** (Section 1.5) and the variable parametrizations are preserved.

The primary difference is given by the choice of the penalty (lasso or ridge) and the value of the penalty parameter  $\lambda$ . Those choices will determine the difference between the estimates of the parameters  $\beta$  of a penalized model and those of the unpenalized GLM.

### 3.1.1. Role of Penalty Parameter $\lambda$

The parameter lambda  $\lambda \geq 0$  is of fundamental importance in the penalized regression framework.

When  $\lambda = 0$ , the penalty term is removed and the resulting **model is an unpenalized GLM**. In this case, the coefficients can be quite noisy as they fully react to the data. When  $\lambda$  is sufficiently large, the penalty term in Equation 3.1 gains increasingly more

importance. Since the aforementioned penalties are designed to regularize or shrink the coefficients toward zero, a large penalty term leads to a solution whose coefficients will be either zero or a negligibly small number depending on the type of penalization.

For a fixed parameter  $\lambda$ , as the  $\beta$  coefficients move away from zero, the value of the penalty term increases.

In these scenarios, the exact behavior of the coefficients is decided by the type of penalization, as we'll detail in the next sections.

The penalty parameter is sensitive to the parameterization of the feature matrix  $X$ : for a given value of  $\lambda$ , the result will differ if the same quantity is, for example, expressed as miles or in kilometers. For this reason (among others), it is best practice to automatically standardize the features<sup>4</sup> before solving Equation 3.1.

Most statistical software supporting penalized regression, both proprietary and open source (glmnet in R or scikit-learn in Python), provide ways to automate the different steps in the computation: automatically standardize the coefficients, fit the penalized model, and return the unstandardized coefficients.

### 3.1.2. Ridge Regression

The formula for ridge regression adds the ridge penalty term to the GLM likelihood optimization:

$$\hat{\beta}_{\text{Ridge}} = \underset{\beta}{\operatorname{argmin}} \operatorname{NLL}(y, X, \beta) + \lambda \left( \frac{1}{2} \sum_i \beta_i^2 \right).$$

The formulation of the ridge penalty can be traced back to Hoerl (1962). The wide adoption of ridge regression is a consequence of its ability to provide stable estimates with highly correlated variables. GLMs are known to become unstable in the presence of highly correlated variables due to aliasing (see Section C.2). The ridge penalty term provides protection against the coefficients “blowing up” as they might in a GLM.

Figure 3.1 shows the differences in the GLM output coefficients between various ridge models with a varying  $\lambda$ .

We observe that the greater the penalty, the more the coefficient tends to be shrunk toward zero, compared with its unpenalized GLM counterpart ( $\lambda = 0$ ). Furthermore, the amount of shrinkage depends on the underlying amount of exposure: the lower the exposure, the higher the magnitude of the shrinkage as the penalty changes. This property matches the behavior of Bühlmann's credibility method. In Appendix A we prove that under some underlying hypotheses, ridge is a multivariate transposition of the Bühlmann credibility, where Bühlmann's  $K$  has a one-to-one correspondence with ridge's  $\lambda$  parameter.

We can get a more holistic representation of the relationship between the penalty and the models' parameters by visualizing the **coefficient path**. Figure 3.2 shows the

<sup>4</sup> Standardization involves rescaling the features (or columns) of the data set  $X$  so that they have a mean of 0 and a standard deviation of 1.

**Figure 3.1.** Comparison of an unpenalized GLM and a GLM with various, increasing levels of ridge penalty. Simple GLM corresponds to the fit with  $\lambda = 0$ .

![Figure 3.1: A dual-axis plot showing coefficients and exposure for categorical variable levels A through K. The left y-axis represents the Coefficient (ranging from -0.2 to 0.3), and the right y-axis represents Exposure (ranging from 0 to 160k). The x-axis lists categorical variable levels A, B, C, D, E, F, G, H, I, J, and K. The plot includes five data series: Exposure (blue bars), Simple GLM (yellow line with circles), Small penalty (brown line with circles), Medium penalty (dark blue line with circles), and Large penalty (purple line with circles). The Simple GLM and Small penalty lines show the highest coefficients, while the Large penalty line shows the lowest, closest to zero. The Exposure bars are highest for levels A and G, and lowest for levels F and I.](391ab9e5616ba6311161af4d7a93422b_img.jpg)

Figure 3.1: A dual-axis plot showing coefficients and exposure for categorical variable levels A through K. The left y-axis represents the Coefficient (ranging from -0.2 to 0.3), and the right y-axis represents Exposure (ranging from 0 to 160k). The x-axis lists categorical variable levels A, B, C, D, E, F, G, H, I, J, and K. The plot includes five data series: Exposure (blue bars), Simple GLM (yellow line with circles), Small penalty (brown line with circles), Medium penalty (dark blue line with circles), and Large penalty (purple line with circles). The Simple GLM and Small penalty lines show the highest coefficients, while the Large penalty line shows the lowest, closest to zero. The Exposure bars are highest for levels A and G, and lowest for levels F and I.

**Figure 3.2.** Coefficient path plot of Figure 3.1, obtained by computing solution for a wide range of penalty parameters. Dotted lines represent the values of  $\lambda$  penalty used to represent Figure 3.1. At very high values of the penalty (on the right), the coefficients are heavily shrunk and close to zero. Conversely, for very low values of the penalty, on the left, the coefficients are materially equal to the unpenalized GLM estimates.

![Figure 3.2: A ridge coefficient path plot showing the relationship between ln λ (x-axis, ranging from -8 to 1) and Coefficients (y-axis, ranging from -0.2 to 0.3). The plot shows multiple colored lines representing different coefficients, all of which converge to zero as ln λ increases (moving from left to right). Vertical dashed lines indicate the values of λ used in Figure 3.1: Small penalty (at ln λ ≈ -5.5), Medium penalty (at ln λ ≈ -3.5), and Large penalty (at ln λ ≈ -1.5). The lines are labeled 'Small penalty', 'Medium penalty', and 'Large penalty' at their respective vertical positions.](939b79420df0cf962959ccef56f3371f_img.jpg)

Ridge coefficient path

Figure 3.2: A ridge coefficient path plot showing the relationship between ln λ (x-axis, ranging from -8 to 1) and Coefficients (y-axis, ranging from -0.2 to 0.3). The plot shows multiple colored lines representing different coefficients, all of which converge to zero as ln λ increases (moving from left to right). Vertical dashed lines indicate the values of λ used in Figure 3.1: Small penalty (at ln λ ≈ -5.5), Medium penalty (at ln λ ≈ -3.5), and Large penalty (at ln λ ≈ -1.5). The lines are labeled 'Small penalty', 'Medium penalty', and 'Large penalty' at their respective vertical positions.

movement of standardized coefficients with varying  $\lambda$  for ridge regression. A high penalty term will shrink all coefficients to a negligibly small value but will not reduce them directly to zero. As the penalty term decreases, all standardized coefficients increase gradually.

### 3.1.3. Lasso

The formula for the **lasso** regression adds the lasso penalty term to the GLM likelihood optimization:

$$\hat{\beta}_{\text{Lasso}} = \underset{\beta}{\operatorname{argmin}} \operatorname{NLL}(y, X, \beta) + \lambda \left( \sum_j |\beta_j| \right).$$

Introduced by Tibshirani (1996), the lasso achieves **sparsity**—i.e., the ability to set coefficients that are nonsignificant exactly to zero—as part of the fitting procedure. This means that lasso can automate both variable and factor selection and estimation. The sparsity property of the lasso is at the root of its wide success in various applications.

Figure 3.3 compares an unpenalized GLM with lasso GLMs using increasing levels of  $\lambda$ . Similar to ridge, the lasso's parameters tend to be shrunk toward zero. Furthermore, the lower the exposure, the higher the amount of shrinkage. The main difference is that for certain values of the parameter  $\beta_{\text{Lasso}}$ , the parameters  $\beta_j$  are set to zero, causing the rating plan coefficient to shrink to 1.0 after the application of the log link ( $\exp(0) = 1$ ).

The lasso's ability to set coefficients to zero and thereby perform **variable selection** is shown through the coefficient path (Figure 3.4).

**Figure 3.3. Comparison of an Unpenalized GLM and a GLM with Various, Increasing Levels of Lasso Penalty**

![Figure 3.3: Comparison of an Unpenalized GLM and a GLM with Various, Increasing Levels of Lasso Penalty. The chart shows Coefficient (left y-axis, -0.2 to 0.3) and Exposure (right y-axis, 0 to 160k) for categorical variable levels A through K. The legend includes Exposure (blue bars), Simple GLM (yellow line with circles), Small penalty (brown line with circles), Medium penalty (dark blue line with circles), and Large penalty (purple line with circles). The Simple GLM shows the highest coefficients, while the Large penalty shows the lowest, closest to zero. The Exposure bars are highest for A and G, and lowest for F.](aa1b948a76d8a599c76b5033f5db9e2b_img.jpg)

| Categorical variable levels | Exposure (k) | Simple GLM | Small penalty | Medium penalty | Large penalty |
|-----------------------------|--------------|------------|---------------|----------------|---------------|
| A                           | ~85k         | 0.0        | 0.0           | 0.0            | 0.0           |
| B                           | ~15k         | ~0.12      | ~0.05         | 0.0            | 0.0           |
| C                           | ~15k         | ~0.32      | ~0.24         | ~0.15          | 0.0           |
| D                           | ~55k         | ~0.0       | ~0.0          | ~0.0           | ~0.0          |
| E                           | ~15k         | ~0.12      | ~0.05         | 0.0            | 0.0           |
| F                           | ~5k          | ~0.0       | ~0.0          | ~0.0           | ~0.0          |
| G                           | ~85k         | 0.0        | 0.0           | 0.0            | 0.0           |
| H                           | ~25k         | ~0.19      | ~0.14         | ~0.10          | ~0.02         |
| I                           | ~15k         | ~0.10      | ~0.04         | 0.0            | 0.0           |
| J                           | ~15k         | ~0.12      | ~0.08         | ~0.06          | 0.0           |
| K                           | ~15k         | ~0.13      | ~0.08         | ~0.02          | 0.0           |

Figure 3.3: Comparison of an Unpenalized GLM and a GLM with Various, Increasing Levels of Lasso Penalty. The chart shows Coefficient (left y-axis, -0.2 to 0.3) and Exposure (right y-axis, 0 to 160k) for categorical variable levels A through K. The legend includes Exposure (blue bars), Simple GLM (yellow line with circles), Small penalty (brown line with circles), Medium penalty (dark blue line with circles), and Large penalty (purple line with circles). The Simple GLM shows the highest coefficients, while the Large penalty shows the lowest, closest to zero. The Exposure bars are highest for A and G, and lowest for F.

**Figure 3.4.** Coefficient path plot of Figure 3.3, obtained by computing solutions for a wide range of penalty parameters. Dotted lines represent the values of  $\lambda$  penalty used to represent Figure 3.1. Coefficients are completely removed from the model using lasso penalization with a sufficiently large penalty term.

![Lasso coefficient path plot showing coefficients versus ln λ. The plot features several colored lines representing different variables. As ln λ increases (moving left), the penalty increases, and coefficients shrink towards zero. Three vertical dashed red lines mark 'Small penalty', 'Medium penalty', and 'Large penalty'. The 'Large penalty' line is at ln λ ≈ -6.5, where all coefficients are zero. The 'Medium penalty' line is at ln λ ≈ -7.3, and the 'Small penalty' line is at ln λ ≈ -8.1.](20727e57890be6da5692a02d13c0a8ec_img.jpg)

Lasso coefficient path

The figure is a line plot titled 'Lasso coefficient path'. The y-axis is labeled 'Coefficients' and ranges from -0.2 to 0.3. The x-axis is labeled 'ln λ' and ranges from -10 to -6. There are approximately 10 colored lines representing different variables. Most lines start at non-zero values for low ln λ (high penalty) and decrease towards zero as ln λ increases. Three vertical dashed red lines are drawn at ln λ ≈ -8.1 (labeled 'Small penalty'), ln λ ≈ -7.3 (labeled 'Medium penalty'), and ln λ ≈ -6.5 (labeled 'Large penalty'). At the 'Large penalty' line, all coefficients are zero. As the penalty decreases (moving right), more coefficients become non-zero.

Lasso coefficient path plot showing coefficients versus ln λ. The plot features several colored lines representing different variables. As ln λ increases (moving left), the penalty increases, and coefficients shrink towards zero. Three vertical dashed red lines mark 'Small penalty', 'Medium penalty', and 'Large penalty'. The 'Large penalty' line is at ln λ ≈ -6.5, where all coefficients are zero. The 'Medium penalty' line is at ln λ ≈ -7.3, and the 'Small penalty' line is at ln λ ≈ -8.1.

In lasso penalization, a sufficiently high penalty term will set all coefficients exactly to zero. As the penalty decreases, coefficients will overcome the penalty and are introduced into the model at different times.

The interested reader can investigate the ability of lasso to achieve sparsity:

- Section A.3 shows how sparsity arises from a Bayesian perspective (priors).
- Appendix D illustrates an **optimization** perspective. In particular, it explains with simple arguments why introducing the absolute value function  $|\beta|$ , which is non-differentiable, leads to sparsity and variable selection.

#### Elastic Net

In the presence of strong collinearities among the variables  $X$ , the lasso and ridge may behave differently:

- Ridge will include all collinear variables and attribute a similar parameter  $\beta_j$  to each one of them.
- Lasso will likely select one of the correlated variables and set the others to zero.

Depending on the use case, a modeler could benefit from including both the ridge and lasso penalties in the same model. The flexibility of the penalized framework allows one to combine both penalties. This approach is known as **elastic net**, whose penalty is a convex combination of both the lasso and ridge penalties:

$$\hat{\beta}_{\text{Elastic Net}, \alpha} = \operatorname{argmin}_{\beta} \text{NLL}(y, X, \beta) + \lambda \left( \frac{1-\alpha}{2} \sum_j \beta_j^2 + \alpha \sum_j |\beta_j| \right).$$

Figure 3.5 compares an unpenalized GLM with GLMs that incorporate various levels of elastic net penalty. Figure 3.6 shows the coefficient path for the elastic net, showcasing its ability to combine both the ridge regression and lasso behavior.

The elastic net requires the modeler to define an additional hyperparameter  $\alpha$  on top of the parameter  $\lambda$ . In general, the choice of the parameter  $\alpha$  depends on the nature of the data, and the methodology to compute this parameter is outside of the scope of the monograph.

**Figure 3.5. Comparison of an Unpenalized GLM and One with Various Increasing Levels of Elastic Net Penalty**

![Figure 3.5: A dual-axis plot comparing an unpenalized GLM (Simple GLM) with GLMs incorporating various levels of elastic net penalty (Small, Medium, Large) across categorical variable levels A through K. The left y-axis shows the Coefficient (ranging from -0.2 to 0.3), and the right y-axis shows Exposure (ranging from 0 to 160k). The Simple GLM is represented by a yellow line with diamond markers, showing the highest coefficients. The Small penalty is represented by a brown line with circle markers, the Medium penalty by a dark blue line with circle markers, and the Large penalty by a purple line with circle markers. The exposure is shown as light blue bars at the bottom of the plot.](99938fa8d7d80af041634eba601e418b_img.jpg)

Figure 3.5: A dual-axis plot comparing an unpenalized GLM (Simple GLM) with GLMs incorporating various levels of elastic net penalty (Small, Medium, Large) across categorical variable levels A through K. The left y-axis shows the Coefficient (ranging from -0.2 to 0.3), and the right y-axis shows Exposure (ranging from 0 to 160k). The Simple GLM is represented by a yellow line with diamond markers, showing the highest coefficients. The Small penalty is represented by a brown line with circle markers, the Medium penalty by a dark blue line with circle markers, and the Large penalty by a purple line with circle markers. The exposure is shown as light blue bars at the bottom of the plot.

**Figure 3.6. Coefficient path plot of Figure 3.5, obtained by computing solutions for a wide range of penalty parameters. The elastic net coefficient path is a blend of both the lasso and ridge coefficient paths, allowing for both variable selection and shrinkage of the coefficients.**

Elastic net coefficient path

![Figure 3.6: A line plot showing the Elastic net coefficient path for various levels of penalty parameters. The x-axis represents the natural logarithm of the penalty parameter λ (ln λ), ranging from -6 to -1. The y-axis represents the Coefficients, ranging from -0.2 to 0.3. The plot shows several curves for different variables, with vertical dashed lines indicating the levels of Small penalty (around ln λ = -4.5), Medium penalty (around ln λ = -3.2), and Large penalty (around ln λ = -2.2). As the penalty increases (ln λ decreases), the coefficients shrink towards zero, and some variables are completely selected (coefficient becomes zero).](98ff4ec9e120afa420dbe08b0d8d77b6_img.jpg)

Figure 3.6: A line plot showing the Elastic net coefficient path for various levels of penalty parameters. The x-axis represents the natural logarithm of the penalty parameter λ (ln λ), ranging from -6 to -1. The y-axis represents the Coefficients, ranging from -0.2 to 0.3. The plot shows several curves for different variables, with vertical dashed lines indicating the levels of Small penalty (around ln λ = -4.5), Medium penalty (around ln λ = -3.2), and Large penalty (around ln λ = -2.2). As the penalty increases (ln λ decreases), the coefficients shrink towards zero, and some variables are completely selected (coefficient becomes zero).

## 3.2. Lasso is Recommended for Actuarial Applications

A sparse statistical model is one having only a small number of nonzero parameters or weights. It represents a classic case of “less is more”: a sparse model can be much easier to estimate and interpret than a dense model. In this age of big data, the number of features measured on a person or object can be large, and might be larger than the number of observations. The sparsity assumption allows us to tackle such problems and extract useful and reproducible patterns from big datasets.

—Hastie, Tibshirani, and Wainwright (2015),  
*Statistical Learning with Sparsity*

As shown in Figure 3.4, for certain values of the parameter  $\lambda$ , some coefficients are shrunk exactly equal to zero. Since the solution of a lasso can set some of the coefficients exactly to zero, lasso is a natively sparse model.

On the other hand, the ridge penalty, as shown in Figure 3.2, does not have the ability to set coefficients directly to zero—hence it is not a natively sparse model. We won’t detail all the purely statistical benefits of sparsity here as literature already exists on the subject, such as Hastie, Tibshirani, and Wainwright (2015).

In addition to statistical benefits, sparsity is valued for its actuarial benefits:

- A sparse actuarial pricing model will be more stable over time than a dense model. Avoiding constant changes in pricing characteristics is valued by insurers, regulators, and customers.
- A sparse actuarial pricing model will be simpler than a dense model. Interpretability is valued by internal stakeholders as well as regulators and policyholders.
- A sparse modeling technique automatically sets a statistical materiality standard. This clarifies the boundary between actuarial and statistical judgment during modeling and during model review.

Additionally, lasso penalization exhibits a desirable responsiveness to significant coefficients. Factor curves can be concave in lasso penalization as shown in Figure 3.4, and this allows a lasso model to be more immediately responsive to signal than ridge or elastic net. Once a variable has passed the threshold of materiality, its coefficient may grow quickly. Ridge penalization instead reacts slowly as all coefficient paths grow slowly at first and only quickly increase as the penalty term gets quite low.

We therefore recommend the use of lasso penalization for most actuarial applications. As we will see later, lasso penalization is ideal for the application of penalized regression as a credibility procedure.

## 3.3. Selecting the Penalty Parameter

The preceding sections emphasized the penalized regression framework’s ability to incorporate credibility within a GLM through the introduction of both a penalty structure (ridge or lasso) and a penalty parameter  $\lambda$ . This penalty parameter clearly plays a critical role in determining the final estimates of the model, as we saw previously in Figure 3.1 and Figure 3.3.

While this section focuses on describing the standard methodologies selecting the penalty parameter in a penalized regression, it is important to note that the final decision on the penalty parameter should not be based solely on data-driven considerations. Actuarial judgment is also crucial and may be reflected in the choice of a slightly higher penalty parameter. This way, the final estimates can give more weight to the complement of credibility or a prior assumption.

Since the incorporation of actuarial judgment in the estimates can be better described under a more practical use case, we refer to Chapter 6 as a supplement to the methodology outlined here.

A “correct” value of the penalty parameter  $\lambda$  cannot be found via an explicit, analytical formula. This differs from other parameters used in actuarial methods, and the reason can be traced to the multivariate nature of the penalized regression.<sup>5</sup>

The lack of standard formulas is not in itself a limitation, as it allows a practitioner to approach the selection of the penalty parameter from a different, and in a sense, more practical perspective.

One of the desired behaviors of a model estimate is to generalize well to unseen data, and hence it is appropriate to choose statistical quality of fit (as measured by deviance or Gini) as the criteria to select the most appropriate penalty parameter. The standard procedure for choosing the penalty parameter consists of computing the generalization performance of a range of penalty values, and then selecting the value that has the best generalized predictive power.

The generalization performance is usually approximated via cross-validation (Hastie, Tibshirani, and Friedman 2009), which is a general procedure that allows us to “simulate” the behavior of a model with previously unseen data.

Figure 3.7 illustrates the procedure by which to evaluate, select, and validate the choice of a penalty parameter. We start by dividing the data into two sets: the modeling set and the validation set. The modeling set is used to build the model, and the validation set is used to assess the final model’s performance.

We perform cross-validation on the training set, which involves dividing it into four (or any number of) folds and using each fold in turn as the test set while the rest is used for training. For each trained cross-validation model, we calculate performance metrics such as deviance, Gini, and pseudo- $R^2$  on the corresponding testing fold. These metrics are then combined to estimate the penalty parameter’s performance on unseen data. Most solvers incorporate cross-validation routines, returning the penalty parameter value with the best average metric across all folds.

---

<sup>5</sup> This differs from standard credibility procedures, which do require the preliminary computation of some data-driven quantity of interest—for example, the  $K$  parameter in Bühlmann credibility (Table 2.1). This quantity is estimated via standard formulas (Bühlmann and Gisler 2005), which in particular require the estimates of average and variances for each of the individual classes. This implies that the quality of the estimator of  $K$  decreases as the number of individual classes are considered. When considering a multivariate model, as in penalized regression, the amount of observations sharing the exact same characteristics increases so significantly that these explicit formulas cannot be applied.

**Figure 3.7. The Recommended Setup for 4-Fold Cross-Validation is a 20%/20%/20%/20% Split for Training and Reserving the Remaining 20% as a True Holdout Set**

|                      | K-Fold<br>Model 1 | K-Fold<br>Model 2 | K-Fold<br>Model 3 | K-Fold<br>Model 4 | Validation<br>Model |
|----------------------|-------------------|-------------------|-------------------|-------------------|---------------------|
| modeling - quarter 1 | TRAIN             | TRAIN             | TRAIN             | TEST              | TRAIN               |
| modeling - quarter 2 | TRAIN             | TRAIN             | TEST              | TRAIN             | TRAIN               |
| modeling - quarter 3 | TRAIN             | TEST              | TRAIN             | TRAIN             | TRAIN               |
| modeling - quarter 4 | TEST              | TRAIN             | TRAIN             | TRAIN             | TRAIN               |
| Validation           |                   |                   |                   |                   | TEST                |

When selecting an optimal cross-validation penalty parameter, it is crucial to examine the overall results of the cross-validation process. Figure 3.8 demonstrates the evolution of cross-validation outcomes as the penalty parameter increases. Each red point signifies the mean error for a given penalty, while the error bars indicate the metric's variation within each score. Notably, even though the optimal penalty parameter  $\lambda_{opt}$  is identified, penalties within a (log) distance between  $-1$  and  $1$  exhibit comparably similar results when accounting for score variation.

**Figure 3.8. The model performance as measured by Gini increases as lambda increases up to a point, and then begins to decrease. Error bars represent the range of Gini calculated in cross-validation.**

![Figure 3.8: A line graph showing the Gini index (Y-axis, ranging from 0.27 to 0.32) versus the Penalty parameter: ln(λ/λ_opt.) (X-axis, ranging from -2 to 4). The Gini index starts at approximately 0.312 for ln(λ/λ_opt.) = -2, remains relatively stable until ln(λ/λ_opt.) = 0, and then decreases steadily to approximately 0.272 at ln(λ/λ_opt.) = 4. A blue circle highlights the peak of the curve at ln(λ/λ_opt.) = 0, Gini index ≈ 0.315. Red error bars are shown for each data point.](bac21fd48fcd7f025c723590e07d1823_img.jpg)

| Penalty parameter: $\ln(\lambda/\lambda_{opt.})$ | Gini index (approx.) |
|--------------------------------------------------|----------------------|
| -2.0                                             | 0.312                |
| -1.5                                             | 0.313                |
| -1.0                                             | 0.314                |
| -0.5                                             | 0.315                |
| 0.0                                              | 0.315                |
| 0.5                                              | 0.314                |
| 1.0                                              | 0.312                |
| 1.5                                              | 0.308                |
| 2.0                                              | 0.304                |
| 2.5                                              | 0.298                |
| 3.0                                              | 0.292                |
| 3.5                                              | 0.282                |
| 4.0                                              | 0.272                |

Figure 3.8: A line graph showing the Gini index (Y-axis, ranging from 0.27 to 0.32) versus the Penalty parameter: ln(λ/λ\_opt.) (X-axis, ranging from -2 to 4). The Gini index starts at approximately 0.312 for ln(λ/λ\_opt.) = -2, remains relatively stable until ln(λ/λ\_opt.) = 0, and then decreases steadily to approximately 0.272 at ln(λ/λ\_opt.) = 4. A blue circle highlights the peak of the curve at ln(λ/λ\_opt.) = 0, Gini index ≈ 0.315. Red error bars are shown for each data point.

Given these observations, the cross-validation procedure should not unilaterally dictate the penalty parameter selection. Instead, it provides **a range of viable penalties** that actuaries can scrutinize by analyzing the model's coefficient values, among other factors such as overall reasonability of the model and other actuarial considerations. In this way, although the cross-validation process assists in informing the penalty parameter choice, the final value should always be assessed for actuarial appropriateness. One frequent application of actuarial judgment is to select a marginally higher penalty value, leading to estimates closer to the selected complement of credibility.

After selecting the final penalty parameter value and finalizing input variables, the modeler should validate the model on the holdout validation set, which has not been used during the cross-validation routine, as seen in the “Validation model” column of Figure 3.7. When comparing a proposed model to a current model, double lift charts built on the full k-fold training set will not be helpful as an overfit model will seem to outperform a properly fit model. A true holdout set allows candidate models to be compared fairly on data neither model has seen before.

## 3.4. Lasso and Variable Transformations

There are various ways to include a variable in a GLM model. The GLM monograph by Goldburd et al. (2016) splits the nature of predictor variables into two groups: **categorical** and **continuous**.

We analyze the impact of the lasso penalty for each of these variable types and additionally provide a specific discussion of **ordinal** and **control** variables.

### 3.4.1. Categorical Variables

A categorical variable takes on one of two or more possible values, thereby assigning each risk to a “category.” Each of these values (levels) is modeled independently—i.e., it has a dedicated coefficient  $\beta_j$ . In a GLM (penalized or unpenalized), a categorical variable is represented by collections of  $\beta_j$ , each representing the impact of each category with respect to an arbitrary fixed level, called the “base level.” Including or excluding a specific coefficient  $\beta_j$  determines whether such a level is deemed significant by the modeler.

In Figure 3.9, we repurpose Figure 3.3 to illustrate the impact of the penalty on categorical variables.

Depending on the strength of the penalty, the lasso sets some coefficients to zero, thus providing an adaptive grouping of those less significant levels with the base. For the other selected levels, the value of the coefficient provides a “credibility-weighted” deviation from the base level. It is worth noting that unlike in a GLM, the predictions from penalized regression will change if a different base level is selected. In a GLM, the predictions will be the same but the confidence intervals and  $p$ -values will be different. Readers are encouraged to see how much this choice matters in the case study (Chapter 7) by changing the selected base level for various categorical variables.

**Figure 3.9. Comparison of an Unpenalized GLM and a GLM with Various, Increasing Levels of Lasso Penalty**

![Figure 3.9: A dual-axis chart comparing an Unpenalized GLM and a GLM with various levels of Lasso Penalty across 11 categorical variable levels (A-K). The left y-axis shows the Coefficient (ranging from -0.2 to 0.3), and the right y-axis shows Exposure (ranging from 0 to 160k). The x-axis is labeled 'Categorical variable levels'. The chart includes five data series: Exposure (blue bars), Simple GLM (yellow line with circles), Small penalty (brown line with circles), Medium penalty (dark blue line with circles), and Large penalty (purple line with circles). The Simple GLM shows the largest coefficients, while the Large penalty shows the smallest, closest to zero.](03498c9b76f980b32f2dfbb7c2e539d2_img.jpg)

| Categorical variable levels | Exposure (k) | Simple GLM | Small penalty | Medium penalty | Large penalty |
|-----------------------------|--------------|------------|---------------|----------------|---------------|
| A                           | 80           | 0.0        | 0.0           | 0.0            | 0.0           |
| B                           | 10           | 0.12       | 0.05          | 0.0            | 0.0           |
| C                           | 10           | 0.32       | 0.25          | 0.15           | 0.0           |
| D                           | 50           | -0.1       | -0.08         | -0.08          | -0.03         |
| E                           | 10           | 0.12       | 0.05          | 0.0            | 0.0           |
| F                           | 5            | -0.2       | -0.12         | -0.12          | 0.0           |
| G                           | 80           | 0.0        | 0.0           | 0.0            | 0.0           |
| H                           | 20           | 0.18       | 0.15          | 0.1            | 0.02          |
| I                           | 10           | 0.1        | 0.05          | 0.0            | 0.0           |
| J                           | 15           | 0.12       | 0.12          | 0.07           | 0.0           |
| K                           | 10           | 0.12       | 0.08          | 0.02           | 0.0           |

Figure 3.9: A dual-axis chart comparing an Unpenalized GLM and a GLM with various levels of Lasso Penalty across 11 categorical variable levels (A-K). The left y-axis shows the Coefficient (ranging from -0.2 to 0.3), and the right y-axis shows Exposure (ranging from 0 to 160k). The x-axis is labeled 'Categorical variable levels'. The chart includes five data series: Exposure (blue bars), Simple GLM (yellow line with circles), Small penalty (brown line with circles), Medium penalty (dark blue line with circles), and Large penalty (purple line with circles). The Simple GLM shows the largest coefficients, while the Large penalty shows the smallest, closest to zero.

### 3.4.2. Continuous Variables

A continuous variable is a numeric variable that represents a measurement on a continuous scale. In a GLM, continuous variables can be represented by one or multiple coefficients  $\beta$  according to the nature of the variables and the modeling decisions.

We start by evaluating the impact of the lasso penalty for a **linear** representation of a continuous variable: a single coefficient  $\beta$  is associated to a variable via the relationship  $\beta x$ . The  $\beta$  value represents the **slope** of the linear impact of the variable in the model. Since the lasso penalty either shrinks or sets to zero the coefficient, the impact of the penalty will correspond in the movement of a slope toward zero or removal of the variable depending on the strength of the effect as seen in Figure 3.10.

Whereas categorical variables identify a **change in level**, continuous variables identify a **change in slope**. Continuous variables may be appropriate for lasso penalization, but we will see that continuous variables are quite difficult to use in lasso credibility (defined in Chapter 5).

To make matters more challenging, in practical applications, the linear representation may be overly simplistic due to the nonlinearities naturally arising in insurance data. Examples could be either age of home or age of driver. Those variables may be represented by multiple coefficients  $\beta_j$ , each mapped to the parameter of some non-linear curves. One such example is a third-degree polynomial encoding, where for a given variable  $x$  three coefficients  $\beta_1, \beta_2, \beta_3$  will represent respectively a linear, a parabolic, and a cubic function. Under such a representation (or **feature engineering**) the interpretation of each individual coefficient is less intuitive: the modeler can determine the

**Figure 3.10. Lasso Fit for Various Penalty Values  $\lambda$  for a Continuous Variable**![Figure 3.10: A dual-axis plot showing the Lasso fit for various penalty values λ for a continuous variable. The x-axis is labeled 'Area' with values 0, 1, 2, 3, 4, 5. The left y-axis is 'Relativity' (1 to 2). The right y-axis is 'Exposure' (0 to 80k). The plot shows five series: 'Exposure' (light blue bars), 'Simple GLM' (yellow line with circles), 'Small penalty' (brown line with circles), 'Medium penalty' (dark blue line with circles), and 'Large penalty' (purple line with circles). All lines start at (0, 1) and increase as Area increases. The 'Simple GLM' line is the steepest, followed by 'Small penalty', 'Medium penalty', and 'Large penalty'. The 'Exposure' bars show a peak at Area 2 and a sharp drop at Area 5.](fe655d77258397f7242c2df72b965b56_img.jpg)

| Area | Exposure (k) | Simple GLM (Relativity) | Small penalty (Relativity) | Medium penalty (Relativity) | Large penalty (Relativity) |
|------|--------------|-------------------------|----------------------------|-----------------------------|----------------------------|
| 0    | ~1.6         | 1.0                     | 1.0                        | 1.0                         | 1.0                        |
| 1    | ~1.4         | ~1.15                   | ~1.1                       | ~1.05                       | ~1.02                      |
| 2    | ~2.1         | ~1.35                   | ~1.25                      | ~1.15                       | ~1.1                       |
| 3    | ~1.75        | ~1.55                   | ~1.45                      | ~1.25                       | ~1.15                      |
| 4    | ~1.6         | ~1.75                   | ~1.65                      | ~1.35                       | ~1.2                       |
| 5    | ~0.1         | ~2.05                   | ~1.85                      | ~1.45                       | ~1.3                       |

Figure 3.10: A dual-axis plot showing the Lasso fit for various penalty values λ for a continuous variable. The x-axis is labeled 'Area' with values 0, 1, 2, 3, 4, 5. The left y-axis is 'Relativity' (1 to 2). The right y-axis is 'Exposure' (0 to 80k). The plot shows five series: 'Exposure' (light blue bars), 'Simple GLM' (yellow line with circles), 'Small penalty' (brown line with circles), 'Medium penalty' (dark blue line with circles), and 'Large penalty' (purple line with circles). All lines start at (0, 1) and increase as Area increases. The 'Simple GLM' line is the steepest, followed by 'Small penalty', 'Medium penalty', and 'Large penalty'. The 'Exposure' bars show a peak at Area 2 and a sharp drop at Area 5.

appropriateness of the factor only by plotting the joint effect of the coefficient to the variable as illustrated in Figure 3.11.

Since the direct interpretation of each individual coefficient to the model is not clear, for such feature engineering sparsity is less necessary. Furthermore, polynomial feature transformations give rise to correlated predictors ( $x$ ,  $x^2$ ,  $x^3$ ). One caution when using lasso for variable selection is that the presence of many highly correlated predictors will produce suboptimal results due to the staggered entrance of such predictors (Hastie, Tibshirani, and Friedman 2009). Using lasso to determine the optimal combination of feature transformation is not recommended.

The modeler wishing to extensively combine polynomial terms or implement other complex feature transformations such as linear or cubic splines may find it beneficial to include some ridge penalty via the elastic net penalized regression. On the other hand, the lasso penalty allows us to model nonlinearities in a much more efficient manner than unpenalized GLMs via the **ordinal treatment**.

### 3.4.3. Ordinal Variables

An ordinal treatment of a variable relies not on the numeric values of the variable but instead on stepwise indicators. Under such a treatment, when a coefficient is zero, it results in the grouping of two consecutive levels. Such a representation is extremely powerful and allows the lasso penalty to automatically detect nonlinear effects.

The idea of blending an ordinal treatment with lasso penalized regression was originally proposed by Tibshirani et al. (2005) in their fused lasso paper. From that paper, several variations of the lasso penalty have been explored and discovered in various fields. In the actuarial field, this methodology is explored from two different perspectives.

**Figure 3.11. Lasso fit for various penalty values  $\lambda$  for a third-degree polynomial fit  $\beta_1x + \beta_2x^2 + \beta_3x^3$  on a continuous variable. The top of the illustration represents the cumulated effect of the polynomial curve with different degrees of penalization, which results in an overall shrinkage of the curve. The bottom of the illustration provides the plot of the change of the individual polynomial function  $\beta_i x^i$  to the varying degrees of penalty.**

![Figure 3.11: Cubic polynomial fit and various amounts of L1 penalty. The figure consists of four plots. The top plot, titled 'Cubic polynomial fit', shows the response versus input for a cubic polynomial fit with different levels of L1 penalty: 'No penalty' (yellow), 'Small penalty' (brown), 'Medium penalty' (dark blue), and 'Large penalty' (purple). The bottom row contains three plots showing the individual contributions of the linear, quadratic, and cubic terms to the response, each with the same four penalty levels. The 'Linear term contribution' plot shows a negative linear relationship. The 'Quadratic term contribution' plot shows a positive quadratic relationship. The 'Cubic term contribution' plot shows a positive cubic relationship. As the penalty increases, the coefficients of all terms shrink towards zero, resulting in a flatter overall fit.](65a73373b57df71e5c2ce1ce0eb7b65d_img.jpg)

Cubic polynomial fit and various amounts of  $L_1$  penalty

The figure illustrates the effect of varying the  $L_1$  penalty ( $\lambda$ ) on a cubic polynomial fit. The top plot shows the overall response versus input, with the fit becoming increasingly smooth and less biased as the penalty increases. The bottom row shows the individual contributions of the linear, quadratic, and cubic terms, demonstrating how each coefficient is shrunk towards zero as the penalty increases.

Figure 3.11: Cubic polynomial fit and various amounts of L1 penalty. The figure consists of four plots. The top plot, titled 'Cubic polynomial fit', shows the response versus input for a cubic polynomial fit with different levels of L1 penalty: 'No penalty' (yellow), 'Small penalty' (brown), 'Medium penalty' (dark blue), and 'Large penalty' (purple). The bottom row contains three plots showing the individual contributions of the linear, quadratic, and cubic terms to the response, each with the same four penalty levels. The 'Linear term contribution' plot shows a negative linear relationship. The 'Quadratic term contribution' plot shows a positive quadratic relationship. The 'Cubic term contribution' plot shows a positive cubic relationship. As the penalty increases, the coefficients of all terms shrink towards zero, resulting in a flatter overall fit.

In the accurate GLM (AGLM) method of Fujita et al. (2020), variables are transformed and encoded through step or binary transformations. In the derivative lasso of Casotto and Holmes (2023), the difference between these consecutive numeric levels is penalized directly. The results in both cases coincide.

Figure 3.12 represents the resulting effects of varying levels of lasso penalty for ordinal variables.

Ordinal variables also help in the selection of an actuarially sound penalty term. We can start with the statistically optimal penalty term and then increase it slightly until any unintuitive behaviors are penalized out of the model. In Figure 3.12, suspicious

**Figure 3.12. Lasso Fit for Various Penalty Values  $\lambda$  for an Ordinal Variable**![Figure 3.12: Lasso Fit for Various Penalty Values λ for an Ordinal Variable. The chart shows Relative (left y-axis, 0.4 to 1.2) and Exposure (right y-axis, 0 to 30k) versus VehAge (x-axis, 0 to 30). The Exposure is represented by blue bars. Three lines represent different penalty values: Small Penalty (yellow), Medium Penalty (dark blue), and Large Penalty (light blue). The Small Penalty line shows significant fluctuations, peaking around VehAge 7 and then dropping sharply after VehAge 17. The Medium Penalty line is relatively flat until VehAge 13, then drops sharply. The Large Penalty line is flat at 1.0 until VehAge 13, then drops to approximately 0.9.](e714d8aca168c4854edebc4a4f2e9bd1_img.jpg)

| VehAge | Exposure (k) | Small Penalty (Relative) | Medium Penalty (Relative) | Large Penalty (Relative) |
|--------|--------------|--------------------------|---------------------------|--------------------------|
| 0      | 15           | 0.98                     | 0.98                      | 1.02                     |
| 1      | 28           | 0.98                     | 1.00                      | 1.02                     |
| 2      | 25           | 1.05                     | 1.02                      | 1.02                     |
| 3      | 22           | 0.98                     | 1.02                      | 1.02                     |
| 4      | 20           | 1.02                     | 1.02                      | 1.02                     |
| 5      | 18           | 1.02                     | 1.02                      | 1.02                     |
| 6      | 16           | 1.02                     | 1.02                      | 1.02                     |
| 7      | 14           | 1.18                     | 1.02                      | 1.02                     |
| 8      | 12           | 1.08                     | 1.02                      | 1.02                     |
| 9      | 11           | 1.10                     | 1.02                      | 1.02                     |
| 10     | 10           | 1.02                     | 1.02                      | 1.02                     |
| 11     | 9            | 1.02                     | 1.02                      | 1.02                     |
| 12     | 8            | 1.02                     | 1.02                      | 1.02                     |
| 13     | 7            | 0.95                     | 0.95                      | 0.95                     |
| 14     | 6            | 0.95                     | 0.95                      | 0.95                     |
| 15     | 5            | 0.90                     | 0.90                      | 0.90                     |
| 16     | 4            | 0.85                     | 0.85                      | 0.90                     |
| 17     | 3            | 0.85                     | 0.85                      | 0.90                     |
| 18     | 2            | 0.70                     | 0.70                      | 0.90                     |
| 19     | 1.5          | 0.68                     | 0.68                      | 0.90                     |
| 20     | 1            | 0.65                     | 0.68                      | 0.90                     |
| 21     | 0.8          | 0.62                     | 0.68                      | 0.90                     |
| 22     | 0.6          | 0.62                     | 0.68                      | 0.90                     |
| 23     | 0.5          | 0.62                     | 0.68                      | 0.90                     |
| 24     | 0.4          | 0.62                     | 0.68                      | 0.90                     |
| 25     | 0.3          | 0.62                     | 0.68                      | 0.90                     |
| 26     | 0.2          | 0.62                     | 0.68                      | 0.90                     |
| 27     | 0.1          | 0.42                     | 0.62                      | 0.90                     |
| 28     | 0.1          | 0.42                     | 0.60                      | 0.90                     |
| 29     | 0.1          | 0.42                     | 0.58                      | 0.90                     |
| 30     | 0.1          | 0.42                     | 0.58                      | 0.90                     |

Figure 3.12: Lasso Fit for Various Penalty Values λ for an Ordinal Variable. The chart shows Relative (left y-axis, 0.4 to 1.2) and Exposure (right y-axis, 0 to 30k) versus VehAge (x-axis, 0 to 30). The Exposure is represented by blue bars. Three lines represent different penalty values: Small Penalty (yellow), Medium Penalty (dark blue), and Large Penalty (light blue). The Small Penalty line shows significant fluctuations, peaking around VehAge 7 and then dropping sharply after VehAge 17. The Medium Penalty line is relatively flat until VehAge 13, then drops sharply. The Large Penalty line is flat at 1.0 until VehAge 13, then drops to approximately 0.9.

reversals present in the small penalty scenario are subsequently canceled in the medium- and large-penalty scenarios. The medium penalty can be considered both statistically and actuarially appropriate.

### 3.4.4. Control Variables

Control variables like “year” and “state” are often used in loss models to account for (control for) the signal from such variables so that they do not flow into other risk characteristics. In GLMs, such variables are often left in the model regardless of significance. In lasso regression, it may happen that some levels of these control variables will be removed from the model by penalization.

Whether or not to apply a penalty term to such special factors is a modeling and actuarial decision, and both options can be motivated by different arguments. In most cases, allowing control variables to be fitted and penalized with other variables is appropriate. By fitting them at the same time, the model has the opportunity to allocate signal appropriately between control variables and potentially correlated predictor variables. Additionally, if a control variable is removed from a model through penalization, it is unlikely that the limited signal will have a material effect on correlated predictors due to the same penalization.

If a modeler wants to ensure that a control variable soaks up all the signal that it possibly can (at the risk of taking signal away from predictor variables), it may be appropriate to apply a stepwise modeling approach. A modeler could first fit the control variables and optionally a few key predictors with a low or absent penalty term. Then, they can offset the coefficients for those control variables when fitting their desired model with an appropriate penalty term. Using the stepwise approach, the modeler is deciding to give less of a penalty to their control variables.

## 3.5. Lasso for Variable Selection

One can also use lasso penalization for variable selection because of its ability to set coefficients directly to zero while maintaining a material coefficient for other variables. A modeler can start with a  $\lambda$  that is sufficiently high to remove all variables from the model. Then, the modeler can gradually decrease the penalty until variables begin to enter the model. In our earlier example (Figure 3.4), this method may be appropriate for variable selection. This approach is not possible with ridge, as the descent of all coefficients is much more uniform, and coefficients are never set directly to zero.

One caution when using lasso for variable selection is that the presence of many highly correlated predictors will produce suboptimal results due to the staggered entrance of these highly correlated predictors. Such a highly correlated collection may arise when including a wide variety of transformations of the same variable in a model (e.g.,  $x \rightarrow x^2, x^3, \log(x), \dots$ ) as seen in Section 3.4.3. Using lasso to determine the optimal combination of feature transformation is not recommended. Instead, some amount of variable pruning is necessary, and we recommend actuarially selecting between highly correlated predictor variables before using lasso for variable selection.

