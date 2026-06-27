---
paper: holmes_&_casotto
chapter: D
title: Sparsity: A Convex Optimization Perspective
topics: [sparsity, subgradient, soft_thresholding, lasso_optimality_conditions, convex_optimization]
key_formulas: [lasso_optimality_conditions, subgradient_definition, lasso_soft_thresholding_solution]
---

> **TL;DR**
> - GLM optimality: Σ(μᵢ − yᵢ) = 0 for each variable level — predictions match observed averages perfectly, regardless of exposure (full credibility).
> - Lasso optimality: |Σ(μᵢ − yᵢ)| ≤ λ when β̂ⱼ = 0 — coefficient set to zero whenever gradient signal falls below threshold λ.
> - Sparsity arises because |β| is non-differentiable at 0; the subgradient ∂|β|₀ = [−1, 1] allows the optimality condition 0 ∈ ∂f(β̂) to hold at β = 0 for a range of data values.
> - Soft-thresholding solution: β̂ = (ȳ − λ/n) if ȳ > λ/n; (ȳ + λ/n) if ȳ < −λ/n; else 0 — lasso shrinks by a fixed amount and zeroes small signals.
> - Ridge shrinks proportionally: β̂_Ridge = [n/(n+λ)]·ȳ; lasso is more aggressive for small signals (sets to zero) but less aggressive for large signals (fixed shrinkage vs. proportional).

# Appendix D. Sparsity: A Convex Optimization Perspective

The monograph details the intimate connections between penalized regression, with lasso in particular, and credibility, Bayesian statistics, and machine learning. There is one last connection, for the more mathematically inclined reader—that with convex optimization.

Lasso regression is known for its ability to achieve sparse solutions, where some of its estimated coefficients will be exactly equal to zero. The mathematical reasons for why sparsity happens are, however, either not discussed at all or hidden in very technical explanations that require a certain level of familiarity with advanced convex optimization concepts. That does not need to be the case—and this section is an attempt to show that **sparsity is achieved because lasso fits the signal up to a threshold**.

Let's start to evaluate how, in a multivariate setting, the GLM estimates adapt to the data by examining the gradient of the GLM formula.

The gradient of a GLM (with canonical link) can be seen as the difference, for each level of a variable, of the total observations and the total estimates included in the GLM model (Ohlsson and Johansson 2010):

$$\nabla NLL(y, X, \beta)_j = \frac{\partial NLL(y, X, \beta)}{\partial \beta_j} = \sum_{i=1}^n (\mu_i - y_i) x_{ij},$$

where  $\mu_i = \text{Link}^{-1}(X_i \beta)$  is the prediction for a given  $\beta$ . At the GLM solution  $\hat{\beta}$ , the gradient is null. In particular, we have

$$\sum_{i \in J} (\mu_i - y_i) = 0. \quad (\text{D.1})$$

This is consistent with the results already described in Section A.1: GLMs give 100% credibility to the data, and average predictions will coincide with the average of the observations for each level  $j$  included in the model (regardless of the number of exposures).

If we want to leave some room for the complement of credibility and shrink the estimates), we could consider adding some “slack,” so that the model can match the data only up to a certain threshold. For example  $|\sum_{i \in J} (y_i - \mu_i)| \leq \varepsilon$  for a certain value  $\varepsilon$ . This is exactly how the lasso guarantees optimality.

The following sections will prove that the optimality condition for

$$\hat{\beta} = \operatorname{argmin}_{\beta} \operatorname{NLL}(y, X, \beta) + \lambda \sum_{j=1}^p |\beta_j|$$

is equivalent to (where  $\mu_i = X_i\beta$ )

$$\begin{cases} \left| \sum_{i \in J} (\mu_i - y_i) \right| \leq \lambda & \leftrightarrow \hat{\beta}_j = 0 \\ \sum_{i \in J} (\mu_i - y_i) = \lambda \operatorname{sign}(\hat{\beta}_i) & \leftrightarrow \hat{\beta}_j > 0 \\ \sum_{i \in J} (\mu_i - y_i) = -\lambda \operatorname{sign}(\hat{\beta}_i) & \leftrightarrow \hat{\beta}_j \leq 0. \end{cases} \quad (\text{D.2})$$

Any final estimate of the lasso, regardless of fitting procedure, will satisfy the above optimality condition system (Equation D.2). We can clearly see the slack discussed above when matching observed and predicted averages: a coefficient will be deemed nonrelevant (and thus set to zero) if its contribution to the likelihood via the gradient falls below the threshold  $\lambda$ ; when the effect is instead considered relevant the coefficient will moved to capture it but just until the error tolerance threshold  $\lambda$  is hit, rather than going all the way like it would on a GLM.

The next sections provide a smooth learning curve to understand the origin of Equation D.2. First, by considering a simple example, we show how sparsity naturally arises from the nondifferentiability of the absolute value  $|\beta|$  contained in the lasso penalty. Then, we introduce the least amount of concepts from convex optimization necessary to provide the optimality guarantees for the lasso problem.

## D.1. Simplified Proof of the Lasso Problem

Consider the simplest possible lasso regression expressed as

$$\hat{\beta} = \operatorname{argmin}_{\beta} \frac{1}{2}(y - \beta)^2 + \lambda |\beta|, \quad (\text{D.3})$$

where we have a one-dimensional parameter  $\beta$  aiming to approximate a single observation  $y$ .

Computing the solution by setting the gradient to zero is not possible as the absolute value is nondifferentiable at zero. Instead, one can write the function as a piecewise parabolic function:

$$\frac{1}{2}(y - \beta)^2 + \lambda |\beta| = \begin{cases} \frac{1}{2}(y - \beta)^2 + \lambda \beta & \text{if } \beta \geq 0 \\ \frac{1}{2}(y - \beta)^2 - \lambda \beta & \text{if } \beta < 0. \end{cases} \quad (\text{D.4})$$

For every value of  $y$  and  $\lambda$ , this function is convex, meaning that there is one and only one global minimum. Figure D.1 highlights all the possible cases, depending on the value of  $y$ . It is clear that the optimum  $\hat{\beta}$  of the piecewise function lies either at the global minimum of the parabola or at  $\beta = 0$ , where the two parabolas intersect.

We can then deduce that if the minimum of the function lies in the right interval  $\beta > 0$ , then the optimum will be  $\hat{\beta} = y - \lambda$  (which is the global minimum of  $\frac{1}{2}(y - \beta)^2 + \lambda\beta$ ).

Equivalently, if it lies on the left part of the parabola ( $\beta < 0$ ), then the optimum will be  $\hat{\beta} = y + \lambda$ . Combining the inequalities, we prove that the optimum of Equation D.3 is

$$\hat{\beta} = \begin{cases} y - \lambda & \text{if } y > \lambda \\ y + \lambda & \text{if } y < -\lambda \\ 0 & \text{otherwise} \end{cases} \quad (\text{D.5})$$

Figure D.1 shows the plot of the optimum  $\hat{\beta}$  as a function of the value of  $y$ .

**Figure D.1.** The left graph represents the plot of three different lasso formulas (Equation D.4) with different fixed values of  $y$  and  $\lambda = 1$ . The right side represents  $\beta \rightarrow 1/2(3 - \beta)^2 + |\beta|$ , the left side is  $\beta \rightarrow 1/2(-3.8 - \beta)^2 + |\beta|$ , and discontinuity is  $\beta \rightarrow 1/2(-3.8 - \beta)^2 + |\beta|$ . The dots represent the optimum  $\hat{\beta}$  for each function. The right graph represents the evolution of the optimum  $\hat{\beta}$  as a function of the values  $y$ . The colored points represent the couples  $(y, \hat{\beta})$  of the three functions of the left-side graph. The function is also called soft-thresholding in the literature.

![Figure D.1: Two plots illustrating the Lasso regression function and its solution. The left plot, titled 'Univariate lasso function', shows three parabolic curves representing different Lasso functions with fixed y and lambda=1. The right plot, titled 'Solution of lasso', shows the evolution of the estimated coefficient beta-hat as a function of the target y, which is a soft-thresholding function.](6cfc5fab7fa377eebe58c4e17c91db04_img.jpg)

The figure consists of two side-by-side plots. The left plot, titled "Univariate lasso function", shows the loss value on the y-axis (ranging from 0 to 25) against the coefficient  $\beta$  on the x-axis (ranging from -2 to 2). Three parabolic curves are shown: a blue curve labeled "Right side", an orange curve labeled "Left side", and a green curve labeled "Discontinuity". The minimum of the blue curve is at  $\beta = 2$ , the minimum of the orange curve is at  $\beta = -3.8$ , and the minimum of the green curve is at  $\beta = 0$ . Colored dots mark these minima. The right plot, titled "Solution of lasso", shows the estimated coefficient  $\hat{\beta}$  on the y-axis (ranging from -4 to 4) against the target  $y$  on the x-axis (ranging from -4 to 4). The plot shows a blue line that is zero for  $y$  between -1 and 1, and increases linearly with a slope of 1 for  $y > 1$  and decreases linearly with a slope of -1 for  $y < -1$ . Colored dots mark the points  $(-3.8, -2.8)$ ,  $(0, 0)$ , and  $(2, 1)$ .

Figure D.1: Two plots illustrating the Lasso regression function and its solution. The left plot, titled 'Univariate lasso function', shows three parabolic curves representing different Lasso functions with fixed y and lambda=1. The right plot, titled 'Solution of lasso', shows the evolution of the estimated coefficient beta-hat as a function of the target y, which is a soft-thresholding function.

The example highlights how the discontinuity in the lasso penalty  $|\beta|$  achieves a sparse solution. The lasso estimate will be exactly equal to zero in correspondence of values of  $y$  smaller than  $\lambda$  in absolute value and will be equal to the value of  $y$  shrunk by a constant of size  $\lambda$  otherwise. It is thanks to its nondifferentiable nature that the lasso problem allows us to obtain sparse solutions.

We now review how to demonstrate the lasso solution in a general way using simple tools from convex optimization.

## D.2. General Proof of the Lasso Problem

When required to find a minimum of a function analytically, the practitioner would naturally compute the gradient of that function and find the parameter  $\beta$  that solves the equality of the gradient to zero.

In the case of the lasso problem, we saw how this is not possible due to the non-differentiability of the penalty at  $\beta = 0$ . As a matter of fact, it is still possible to compute a minimum of the lasso regression by setting the gradient to zero: we just need to generalize the definition of the gradient.

The gradient is defined as the slope of the tangent to the graph of a function. In the case of a discontinuity, there may be multiple slopes that are tangent to the graph of the function. The gradient loses its uniqueness property, and it is hence said that the function is “not differentiable.”

A generalization of the gradient, the subgradient, is defined as the *set* of possible slopes that are tangent to a graph. Formally, given a convex function  $f \in \mathbb{R}^p$ , the subgradient is

$$\partial f(\beta_0) = \left\{ u \in \mathbb{R}^p \mid f(\beta) - f(\beta_0) \geq u(\beta - \beta_0) \right\}.$$

In the case of the absolute value function, since the subgradient is equal to the gradient when the function is differentiable, for all values strictly different than zero the gradient will be equal to the sign function, that is, 1 for all positive values and  $-1$  for all negative values. In the discontinuity point at 0, it will take all possible values between  $-1$  and 1.

$$\partial|\beta| = \begin{cases} -1 & \text{if } \beta < 0 \\ (-1, 1] & \text{if } \beta = 0 \\ 1 & \text{if } \beta > 0 \end{cases} \quad (\text{D.6})$$

Generalizing the gradient to the subgradient allows us to compute the minimum for the lasso. It is established that if  $f$  is differentiable and convex, then

$$\hat{\beta} = \underset{\beta}{\operatorname{argmin}} f(\beta) \Leftrightarrow 0 = \nabla f(\hat{\beta}). \quad (\text{D.7})$$

**Figure D.2.** The graph on the left illustrates the subgradient for a piecewise function. In blue, we see the subgradient at value 2. As the function is differentiable, there exists only one subgradient, and it is equal to the gradient. Since the function at 0 is not differentiable, there is more than one tangent line to the graph. The subgradient is drawn in red. The graph on the right represents some possible tangent lines for the lasso function  $\beta \rightarrow |\beta|$ . Thus, we have a visual intuition of why  $\partial|\beta|_{\beta=0} = [-1, 1]$ .

![Figure D.2: Two graphs illustrating subgradients. The left graph, titled 'Subgradient example', shows a piecewise linear function with a kink at (0,0). A blue dashed line represents the unique subgradient at x=2, which is also the gradient. Multiple red dashed lines represent different subgradients at the non-differentiable point x=0. The right graph, titled 'Lasso subgradients at 0', shows the V-shaped function f(β) = |β|. Numerous blue dashed lines of different slopes pass through the origin (0,0), illustrating that any line passing through the origin stays below the V-shaped function, thus representing a subgradient at β=0.](a45bada58cb83d0191ed06b2b229d99c_img.jpg)

Figure D.2: Two graphs illustrating subgradients. The left graph, titled 'Subgradient example', shows a piecewise linear function with a kink at (0,0). A blue dashed line represents the unique subgradient at x=2, which is also the gradient. Multiple red dashed lines represent different subgradients at the non-differentiable point x=0. The right graph, titled 'Lasso subgradients at 0', shows the V-shaped function f(β) = |β|. Numerous blue dashed lines of different slopes pass through the origin (0,0), illustrating that any line passing through the origin stays below the V-shaped function, thus representing a subgradient at β=0.

If  $f$  is not differentiable (but still convex), then the optimality condition becomes

$$\hat{\beta} = \underset{\beta}{\operatorname{argmin}} f(\beta) \Leftrightarrow 0 \in \partial f(\hat{\beta}) \quad (\text{D.8})$$

by the subgradient optimality condition (see Boyd and Vandenberghe 2004). Since the subgradient of a sum is the sum of the subgradients and the subgradient of a differentiable function is the gradient, in the case of the (simplified) lasso regression we can write the optimality condition above as

$$\hat{\beta} = \underset{\beta}{\operatorname{argmin}} \frac{1}{2}(y - \beta)^2 + \lambda|\beta| \Leftrightarrow 0 \in (\hat{\beta} - y) + \lambda\partial|\hat{\beta}|,$$

where  $(\hat{\beta} - y)$  is the derivative of  $\frac{1}{2}(y - \beta)^2$ .

Since the subgradient of  $\beta \rightarrow |\beta|$  is given by Equation D.6, we can prove the optimality of Equation D.5: if the optimum is  $\hat{\beta} = 0$ , then there exists a number  $|u| \leq 1$  such that  $0 = -y + \lambda u$ . This happens only when  $|y| \leq \lambda$ . For the other cases ( $\hat{\beta} > 0$ ,  $\hat{\beta} < 0$ )

the lasso penalty is differentiable and by standard arguments one can verify the optimality of Equation D.5.

The subgradient definition provides the optimality conditions of the lasso regression in all its generality, both in a multivariate setting and using a generic negative log-likelihood. It provides as well the tools to understand the optimality conditions from Equation D.2. To see this, consider the general lasso problem

$$\hat{\beta} = \underset{\beta}{\operatorname{argmin}} \operatorname{NLL}(y, X, \beta) + \lambda \sum_{j=1}^p |\beta_j|.$$

To compute the optimal solution, first the **sub**gradient of the negative log-likelihood is required:

$$\frac{\partial}{\partial \beta_j} [\operatorname{NLL}(y, X, \beta) + \lambda \sum_{j=1}^p |\beta_j|] = \nabla \operatorname{NLL}(y, X, \beta)_j + \lambda \partial |\beta_j|.$$

At optimum  $\hat{\beta}$  zero must belong to the subgradient, which means that depending on the sign of  $\hat{\beta}_j$  we have that

$$\begin{cases} |\nabla \operatorname{NLL}(y, X, \beta)_j| < \lambda & \Leftrightarrow \hat{\beta}_j = 0 \\ \nabla \operatorname{NLL}(y, X, \beta)_j = -\lambda & \Leftrightarrow \hat{\beta}_j > 0 \\ \nabla \operatorname{NLL}(y, X, \beta)_j = \lambda & \Leftrightarrow \hat{\beta}_j < 0, \end{cases}$$

which proves Equation D.5. The results of this section combined provide as well all required tools to prove the optimal solution formula.

