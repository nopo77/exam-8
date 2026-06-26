---
paper: bahnemann
chapter: 5
title: 5. Excess Claims
topics: [excess_loss_variable, mean_excess_loss_function, truncation_and_shifting, increased_limits_factors, excess_layer_pricing]
key_formulas: [excess_loss_distribution, mean_excess_loss_function, excess_variable_moments, increased_limits_factor, excess_layer_expected_payment]
---

> **TL;DR**
> - **Excess variable** Y=max(0, X−a); F_Y(y)=F_X(y+a); E[Y]=E[X]−E[X;a]; note Y includes claims paying 0 (X≤a)
> - **Truncated-and-shifted variable** X_a = X−a | X>a; **E[X_a] = (E[X]−E[X;a])/(1−F_X(a))** — this is the mean excess loss (MEL) function e(a)
> - MEL behavior identifies tail type: **increasing MEL → heavy tail (Pareto)**; **constant MEL → exponential**; **decreasing MEL → light tail**
> - **Excess layer** (a, a+l]: expected payment per occurrence = E[X;a+l]−E[X;a]; multiply by 1/(1−F_X(a)) to get expected payment per excess claim
> - **Increased limits factor** ILF(l) = E[X;l]/E[X;b] (b = basic limit); use limited expected value formulas for Pareto/lognormal to price higher limits

# 5. Excess Claims

We investigate in this chapter claim processes in which all claims are restricted to those larger in size than some fixed positive amount—that is, to claims that penetrate an excess layer of insurance. Distributions of such excess losses are critical to the quantification of such common policy provisions as deductibles and to the pricing of successive layers of coverage lying above a first-dollar, or primary, layer of insurance.

## 5.1. Excess Claim Size

Consider first an unlimited claim-size random variable  $X$  and a nonnegative constant  $a$ . The random variable  $Y$  defined by

$$Y = \begin{cases} 0 & \text{if } 0 \leq X \leq a \\ X - a & \text{if } a < X < \infty \end{cases}$$

represents the size of claims modified by a policy condition that imposes an underlying limit amount  $a$ . Here the insurer pays nothing if the claim size is  $a$  or less, and the sizes of all other claims are reduced by  $a$ . In this situation  $a$  could represent an amount retained by the insured, as in the case of a policy with a deductible, or for an umbrella or excess policy it might be the limit of an underlying primary policy.

The distribution function of variable  $Y$  is readily obtained from that of  $X$ :

$$F_Y(y) = \Pr\{Y \leq y\} = \begin{cases} 0 & \text{if } -\infty < y < 0 \\ F_X(y + a) & \text{if } 0 \leq y < \infty. \end{cases}$$

If  $E[X]$  exists, then so does  $E[Y]$ . Moreover,

$$\begin{aligned} E[Y] &= \int_0^\infty y dF_X(y + a) \\ &= \int_a^\infty (u - a) dF_X(u) \\ &= \int_0^\infty u dF_X(u) - \int_0^a u dF_X(u) - a \int_a^\infty dF_X(u) \\ &= E[X] - E[X; a]. \end{aligned} \tag{5.1}$$

Clearly,  $E[Y] \leq E[X]$  whenever both expected values exist.

For random variable  $Y$  the probability that the insurer pays nothing,

$$F_Y(0) = \Pr\{Y = 0\} = \Pr\{X \leq a\} = F_X(a),$$

is usually a positive number. However, insurers do not always see, nor are they usually interested in, claims for which  $Y = 0$ . It is therefore more useful, from an insurer's standpoint, to work with a related variable  $X_a$ , defined only for  $X > a$ :

$$X_a = X - a, \quad a < X < \infty. \quad (5.2)$$

$X_a$  represents the **excess of  $X$  over the limit  $a$** , for which claims of size  $a$  or smaller are ignored and all others are reduced by the amount  $a$ . Thus modified, variable  $X$  is said to be **truncated from below and shifted by  $a$** . Variable  $X_a$  has a distribution function obtained conditionally from that of  $X$ —and in this case  $F_{X_a}(0) = 0$ :

$$F_{X_a}(x) = \Pr\{X - a \leq x | X > a\} = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ \frac{F_X(x+a) - F_X(a)}{1 - F_X(a)} & \text{if } 0 \leq x < \infty. \end{cases} \quad (5.3)$$

Whenever  $E[X]$  exists the expected value of  $X_a$  is

$$E[X_a] = \frac{\int_0^\infty x dF_X(x+a)}{1 - F_X(a)} = \frac{E[X] - E[X; a]}{1 - F_X(a)}. \quad (5.4)$$

[Compare this formula with that of (5.1).] Moreover, if all three moments  $E[X]$ ,  $E[X^2]$ , and  $E[X^3]$  exist, then the second and third moments of  $X_a$  are, respectively,

$$E[X_a^2] = \frac{E[X^2] - E[X^2; a] - 2a(E[X] - E[X; a])}{1 - F_X(a)}, \quad (5.5)$$

$$\begin{aligned} E[X_a^3] &= \frac{E[X^3] - E[X^3; a] - 3a(E[X^2] - E[X^2; a])}{1 - F_X(a)} \\ &\quad + \frac{3a^2(E[X] - E[X; a])}{1 - F_X(a)}. \end{aligned} \quad (5.6)$$

The limited expected value of the excess random variable  $X_a$  is an obvious combination of limited severities of the unlimited claim-size variable  $X$ :

$$\begin{aligned} E[X_a; l] &= \frac{\int_0^l x dF_X(x+a)}{1 - F_X(a)} + l \left( 1 - \frac{F_X(l+a) - F_X(a)}{1 - F_X(a)} \right) \\ &= \frac{\int_a^{a+l} (u-a) dF_X(u)}{1 - F_X(a)} + l \left( \frac{1 - F_X(a+l)}{1 - F_X(a)} \right) \end{aligned}$$

$$\begin{aligned}
&= \frac{E[X; a+l] - E[X; a] - (a+l)(1 - F_X(a+l)) + a(1 - F_X(a))}{1 - F_X(a)} \\
&\quad + \frac{l(1 - F_X(a+l)) - a(F_X(a+l) - F_X(a))}{1 - F_X(a)} \\
&= \frac{E[X; a+l] - E[X; a]}{1 - F_X(a)}. \tag{5.7}
\end{aligned}$$

**Example 5.1.** Claim-size random variable  $X$  has an exponential distribution with mean  $\beta$ :

$$F_X(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 - e^{-x/\beta} & \text{if } 0 \leq x < \infty. \end{cases}$$

For the exponential distribution family it is evident that the excess c.d.f. is independent of the size of limit  $a$ :

$$F_{X_a}(x) = \frac{(1 - e^{-(x+a)/\beta}) - (1 - e^{-a/\beta})}{e^{-a/\beta}} = 1 - e^{-x/\beta}, \quad 0 \leq x < \infty.$$

As a consequence, the excess claim size  $X_a$  and unlimited claim size  $X$  have the *same* distribution. This means that the existence of a deductible or underlying coverage does not affect the distribution of claim size. In particular,  $E[X_a] = E[X] = \beta$  for every limit  $a$ . ■

**Example 5.2.** Claim-size variable  $X$  has a Pareto distribution with probability density function

$$f_X(x) = \frac{\alpha\beta^\alpha}{(x+\beta)^{\alpha+1}}, \quad 0 < x < \infty.$$

Accordingly, the density function for  $X_d$  is

$$f_{X_d}(x) = \frac{f_X(x+d)}{1 - F_X(d)} = \frac{\alpha\beta^\alpha}{(x+d+\beta)^{\alpha+1}} \bigg/ \left( \frac{\beta}{d+\beta} \right)^\alpha = \frac{\alpha(d+\beta)^\alpha}{(x+d+\beta)^{\alpha+1}}, \quad 0 < x < \infty.$$

Hence,  $X_d$  is also Pareto-distributed, with parameters  $(\alpha, d+\beta)$ . The mean  $E[X_d]$  exists whenever  $\alpha > 1$ , and it is an increasing linear function of the lower limit  $d$ :

$$E[X_d] = \frac{d+\beta}{\alpha-1}. \quad \blacksquare$$

**Example 5.3.** The table below displays grouped claim-size data derived from a sample of 300 claims from an unlimited population with an unknown distribution.

| Size Group    | # Claims |
|---------------|----------|
| 0–5,000       | 139      |
| 5,001–10,000  | 68       |
| 10,001–15,000 | 32       |
| 15,001–20,000 | 15       |
| 20,001–25,000 | 11       |
| 25,001–30,000 | 8        |
| 30,001–35,000 | 5        |
| 35,001–40,000 | 4        |
| 40,001–45,000 | 3        |
| 45,001–48,500 | 15       |
| Total         | 300      |

Before the data were tabulated these claims were censored by a \$50,000 policy limit and then subjected to a \$1,500 straight deductible. Using the minimum chi-square approach, we wish to find a lognormal distribution function  $F_{\mu,\sigma}(x)$  for the population of the unlimited—non-truncated and non-censored—claims.

We begin by defining ten cells with boundaries  $c_k = 5,000k$  ( $k = 0, 1, \dots, 9$ ) and  $c_{10} = \infty$ . The observed cell frequencies are just the tabulated group claim frequencies  $n_k$ . In particular, note that  $n_{10} = 15$ .

The expected cell frequencies  $\phi_k(\mu, \sigma)$  are expressed in terms of the (as yet unknown) unlimited and unmodified population lognormal c.d.f.  $F_{\mu,\sigma}(x)$ . The probability  $P_k(\mu, \sigma)$  of a claim being less than or equal  $c_k$  is

$$P_k(\mu, \sigma) = \begin{cases} \frac{F_{\mu,\sigma}(c_k + 1,500) - F_{\mu,\sigma}(1,500)}{1 - F_{\mu,\sigma}(1,500)} & \text{if } k = 0, 1, 2, \dots, 9 \\ 1 & \text{if } k = 10. \end{cases}$$

Therefore

$$\phi_k(\mu, \sigma) = (300)(P_k(\mu, \sigma) - P_{k-1}(\mu, \sigma)).$$

Minimizing the chi-square statistic

$$\chi^2(\mu, \sigma) = \sum_{k=1}^{10} \frac{(n_k - \phi_k(\mu, \sigma))^2}{\phi_k(\mu, \sigma)}$$

as a function of  $\mu$  and  $\sigma$  yields a minimum value of  $\chi^2(\hat{\mu}, \hat{\sigma}) = 1.6610$  corresponding to the parameter estimates  $(\hat{\mu}, \hat{\sigma}) = (8.67593, 1.18109)$ .

Because sample data were truncated by the 1,500 deductible, the number of claims entirely eliminated by the deductible is unknown. However, one can estimate this number by means of  $F_{\hat{\mu}, \hat{\sigma}}(1,500) = 0.1243$ :

$$\# \text{ population claims } \leq 1,500 \approx \frac{300}{1 - 0.1243} (0.1243) = (343)(0.1243) = 43. \blacksquare$$

## 5.2. Excess Severity

The expectation  $E[X_a]$  obtained in (5.4), with respect to the unlimited random variable  $X$ , is called the **mean excess claim size at  $a$**  or **excess severity at  $a$** .<sup>49</sup> As with the limited expected value, we can express the mean excess claim size, when it exists,

<sup>49</sup> Illogically in the context of loss distributions,  $E[X_a]$  is also known as the **mean residual life at  $a$** . The term, however, makes sense when the random variable  $X$  is a failure-time variable encountered in reliability theory. The expression apparently found its way into actuarial usage because many distributions used by actuaries have also played prominent roles in reliability theory.

**Figure 5.1. Characteristic Excess Severity Function Graphs<sup>50</sup>**

![Figure 5.1: Characteristic Excess Severity Function Graphs. A graph showing five curves representing different probability distributions: Pareto (solid line, increasing linearly), Weibull (dotted line, increasing with a decreasing slope), lognormal (dashed line, increasing with a decreasing slope), gamma (dash-dot line, decreasing toward a horizontal asymptote), and exponential (dashed line, constant). The x-axis is labeled 'x' and the y-axis is labeled 'y'.](57be5d3e7441ceb413b18b0cb9ec0d60_img.jpg)

Figure 5.1: Characteristic Excess Severity Function Graphs. A graph showing five curves representing different probability distributions: Pareto (solid line, increasing linearly), Weibull (dotted line, increasing with a decreasing slope), lognormal (dashed line, increasing with a decreasing slope), gamma (dash-dot line, decreasing toward a horizontal asymptote), and exponential (dashed line, constant). The x-axis is labeled 'x' and the y-axis is labeled 'y'.

as a function of the associated limit  $x$ . In this context  $E[X_x]$  is commonly denoted by  $e(x)$ —or by  $e_X(x)$  when dependence on the random variable  $X$  must be indicated:

$$e_X(x) = \frac{E[X] - E[X; x]}{1 - F_X(x)}, \quad 0 < x < \infty. \quad (5.8)$$

The behavior of  $e(x)$  for large values of  $x$  is characteristic for all distributions in a given parametric family and tends to differ from one such family to another. For example, when  $X$  is exponentially distributed,  $e(x)$  is a constant function of  $x$ , as shown in Example 5.1. Example 5.2 indicates that for Pareto-distributed  $X$  with  $\alpha > 1$ ,  $e(x)$  is an increasing linear function of  $x$ . In the case of the lognormal family,  $e(x)$  increases without bound as  $x \rightarrow \infty$ , whereas for gamma-distributed  $X$  the function decreases toward a horizontal asymptote as  $x \rightarrow \infty$ . The Weibull  $e(x)$  function behaves like  $ax^b$  for some  $a$  and  $b$  and large values of  $x$ . Typical shapes for the graph of  $y = e(x)$  are shown in Figure 5.1. Refer to Problem 5.26 for hints on verifying these results.

The asymptotic behavior of  $y = e(x)$  is occasionally useful when it comes to fitting a parametric distribution to a set of sample data. The shape of the graph of the sample excess severity function  $e_n(x)$  may suggest an appropriate family of distributions. If this graph is approximately linear with positive slope, then a Pareto distribution could be used. If it is nearly constant for large  $x$ , a gamma or exponential model would be indicated. Otherwise, if the graph lies between these extremes, then a lognormal or Weibull distribution could be used.

<sup>50</sup> Figure 5.1 is suggested by a similar display in Hogg and Klugman [8], p. 109.

There is, however, a practical restriction in the use of this asymptotic test. The characteristic behavior of  $y = e(x)$  becomes apparent only for large  $x$ , the region for which sample data is typically the most sparse. It is therefore essential that the claim data contain enough large claims so that  $e_n(x)$  can be reliably calculated for sufficiently large values of  $x$ .

**Example 5.4.** The table displays grouped sample claim data for  $n = 1,000$  policies.

| Size Group   | # Claims | Total Loss | Severity |
|--------------|----------|------------|----------|
| 0–100        | 100      | 6,000      | 60       |
| 101–500      | 300      | 95,000     | 317      |
| 501–1,000    | 240      | 145,000    | 604      |
| 1,001–2,000  | 185      | 260,000    | 1,405    |
| 2,001–4,000  | 140      | 450,000    | 3,214    |
| 4,001–5,000  | 15       | 66,000     | 4,400    |
| 5,001–10,000 | 20       | 150,000    | 7,500    |
| Total        | 1,000    | 1,172,000  | 1,172    |

To investigate the behavior of the sample excess severity function for large  $x$ , begin by calculating values for the relevant sample statistics at the right-hand endpoints of the group intervals. For example, values of  $F_n(2,000)$ ,  $E_n[\hat{X}; 2,000]$ , and  $e_n(2,000)$  for the discrete sample variable  $\hat{X}$  are, respectively,

$$\begin{aligned}
 F_{1000}(2,000) &= \frac{100 + 300 + 240 + 185}{1,000} = 0.8250, \\
 E_{1000}[\hat{X}; 2,000] &= \frac{6,000 + 95,000 + 145,000 + 260,000}{1,000} \\
 &\quad + \frac{(140 + 15 + 20)(2,000)}{1,000} = 856, \\
 e_{1000}(2,000) &= \frac{1,172 - 856}{1 - 0.8250} = 1,806.
 \end{aligned}$$

The complete set of end-point values is shown in Table 5.1.

The tabulated values of  $e_n(x)$  along with a least-squares regression line are displayed graphically in Figure 5.2. It is evident that the sample values are very nearly aligned—the coefficient of determination for the linear regression is  $R^2 = 0.9823$ . A Pareto model is obviously indicated. To fit such a distribution, observe that the regression function  $0.257335x + 1,208.50$  can be equated with the Pareto  $e(x)$  and the resulting equation solved for parameters  $\alpha$  and  $\beta$ :

$$0.257335x + 1,208.50 = (x + \beta)/(\alpha - 1).$$

**Table 5.1. Sample and Pareto Excess Severity Functions [Example 5.4]**

| Size $x$ | Sample Distribution ( $n = 1,000$ ) |                   |          | Pareto Distribution |           |        |
|----------|-------------------------------------|-------------------|----------|---------------------|-----------|--------|
|          | $F_n(x)$                            | $E_n[\hat{X}; x]$ | $e_n(x)$ | $F(x)$              | $E[X; x]$ | $e(x)$ |
| 0        | 0.0000                              | 0                 | 1,172    | 0.0000              | 0         | 1,208  |
| 100      | 0.1000                              | 96                | 1,196    | 0.0978              | 95        | 1,234  |
| 500      | 0.4000                              | 401               | 1,285    | 0.3900              | 393       | 1,337  |
| 1,000    | 0.6400                              | 606               | 1,572    | 0.6106              | 638       | 1,466  |
| 2,000    | 0.8250                              | 856               | 1,806    | 0.8233              | 904       | 1,723  |
| 4,000    | 0.9650                              | 1,096             | 2,171    | 0.9507              | 1,098     | 2,238  |
| 5,000    | 0.9800                              | 1,122             | 2,500    | 0.9711              | 1,136     | 2,495  |
| 10,000   | 1.0000                              | 1,172             | —        | 0.9962              | 1,194     | 3,782  |

Thus,  $(\alpha, \beta) = (4.88599; 4,696.22)$ . Corresponding end-point values for this Pareto distribution are shown in Table 5.1 for comparison.

The technique of estimating Pareto parameters from the slope and intercept of the regression line seems to work well in this example, but it should be used with some caution. The slope of the regression line is sensitive to the size of the largest claims, and the calculated distribution parameters could be significantly affected by changes in just a few of these numbers. ■

**Example 5.5.** Figure 5.3 shows the graph of the sample excess severities for the data of Examples 2.6 and 2.7. Superimposed on this graph are the corresponding graphs of  $y = e(x)$  for the fitted gamma and lognormal distributions obtained in those examples. The graph of the gamma model reasonably approximates that of the sample function, but the lognormal function diverges significantly from the sample values for  $x > 1,500$ . This suggests that of the two probability distributions obtained in Chapter 2 the gamma might provide the better fit. ■

**Figure 5.2. Sample Excess Severities with Regression Line [Example 5.4]**![Scatter plot showing sample excess severities with a regression line. The x-axis is labeled 'x' and ranges from 0 to 5,000. The y-axis is labeled 'y' and ranges from 0 to 2,000. Five data points are plotted at approximately (0, 1208), (100, 1234), (500, 1337), (1000, 1466), and (2000, 1723). A regression line is drawn through the points with the equation y = 0.257335x + 1,208.50 and R^2 = 0.9823.](603a09e191b18f16af128d27a6c038bd_img.jpg)

Scatter plot showing sample excess severities with a regression line. The x-axis is labeled 'x' and ranges from 0 to 5,000. The y-axis is labeled 'y' and ranges from 0 to 2,000. Five data points are plotted at approximately (0, 1208), (100, 1234), (500, 1337), (1000, 1466), and (2000, 1723). A regression line is drawn through the points with the equation y = 0.257335x + 1,208.50 and R^2 = 0.9823.

**Figure 5.3. Excess Severity Functions [Example 5.5]**![Figure 5.3: Excess Severity Functions. A line graph showing three curves: Sample (solid line with dots), Gamma (dashed line), and Lognormal (dotted line). The x-axis represents the claim amount x, ranging from 0 to 7,000. The y-axis represents the severity y, ranging from 0 to 1,000. The Sample curve starts at approximately (1000, 850) and decreases to about (3500, 420). The Gamma curve starts at approximately (1000, 850) and decreases more slowly, reaching about (7000, 480). The Lognormal curve starts at approximately (1000, 850) and increases, reaching about (7000, 900).](ecaf55d564250830bf6c4165f2feeacc_img.jpg)

| x     | Sample (y) | Gamma (y) | Lognormal (y) |
|-------|------------|-----------|---------------|
| 1,000 | 850        | 850       | 850           |
| 2,000 | 650        | 700       | 700           |
| 3,000 | 450        | 550       | 750           |
| 4,000 | -          | 500       | 800           |
| 5,000 | -          | 480       | 850           |
| 6,000 | -          | 470       | 880           |
| 7,000 | -          | 480       | 900           |

Figure 5.3: Excess Severity Functions. A line graph showing three curves: Sample (solid line with dots), Gamma (dashed line), and Lognormal (dotted line). The x-axis represents the claim amount x, ranging from 0 to 7,000. The y-axis represents the severity y, ranging from 0 to 1,000. The Sample curve starts at approximately (1000, 850) and decreases to about (3500, 420). The Gamma curve starts at approximately (1000, 850) and decreases more slowly, reaching about (7000, 480). The Lognormal curve starts at approximately (1000, 850) and increases, reaching about (7000, 900).

## 5.3. Layers of Coverage

In many situations an insurance policy may impose both an upper limit and a lower limit on the claims subject to the policy. How these are applied depends on the specific policy conditions—for example, on whether the lower limit represents a deductible or whether it is the limit of underlying coverage, as in the case of an umbrella or excess liability policy. We shall be primarily concerned with the latter case in this section and leave the main discussion of the deductible case to the next chapter.

If the excess variable  $X_a$  is subject to an upper limit  $l$  (as in the case of an excess policy written over underlying coverage), then the claim amount paid by the insurer is the unrestricted amount  $x$  first decreased by  $a$  and then limited by  $l$ . Such claims are said to belong to the **layer of coverage** defined by  $a$  and  $l$ . Limit  $a$  is called an **underlying limit** or **attachment point**, whereas  $l$  is the **layer limit** or the **width** of the layer. An unlimited claim of size  $x$  is said to **penetrate** the layer whenever  $x > a$ .

If  $a > 0$  the layer is called an **excess layer**, whereas in the trivial case  $a = 0$  claims in the layer are referred to as **first-dollar** or **ground-up** claims. The layer defined by  $a$  and  $l$  is sometimes denoted by the “interval” notation  $(a, a + l]$ —although a **layer** of coverage is conceptually different from an **interval** of claims. This distinction is explored in Problems 5.14 and 5.15.

In the case of a straight deductible, however, the deductible limit is generally applied *after* the policy limit. In this situation, the layer width is the policy limit reduced by the deductible size,  $l - a$ , so that the insured layer is  $(a, l]$ . Deductibles are explored in detail in Section 6.5.

Example 5.6 illustrates, in the context of a policy limit and deductible, how upper and lower policy limits serve to partition claims into a sequence of layers.

**Example 5.6.** An insurance policy with a \$3,000 limit and \$100 straight deductible defines a three-layer structure: (i) the deductible layer between 0 and 100, (ii) the insured layer of width 2,900 between 100 and 3,000, and (iii) an uninsured layer excess of 3,000. Note that the deductible effectively reduces the policy limit from 3,000 to 2,900.

Suppose that the occurrence of insured events during the policy period gives rise to four claims—of sizes 50, 600, 1,800, and 4,000—for a total of 6,450. Three claims penetrate the insured layer, and one of these is limited by the policy limit. The table shows how they are distributed among the three layers.

| Layer               | Claim 1  | Claim 2    | Claim 3      | Claim 4      | Total        |
|---------------------|----------|------------|--------------|--------------|--------------|
| [0; 100]            | 50       | 100        | 100          | 100          | 350          |
| <b>(100; 3,000]</b> | <b>0</b> | <b>500</b> | <b>1,700</b> | <b>2,900</b> | <b>5,100</b> |
| (3,000; $\infty$ )  | 0        | 0          | 0            | 1,000        | 1,000        |
| Total               | 50       | 600        | 1,800        | 4,000        | 6,450        |

Here the insurer pays 5,100 in the insured layer, whereas the policyholder retains 1,350 of the total claim amount—350 within the deductible layer plus 1,000 in the uninsured layer above 3,000. ■

The random variable for claim size  $X_{a,l}$  in the layer  $(a, a + l]$  is defined on the interval  $a < X < \infty$  by the equation

$$X_{a,l} = \begin{cases} X - a & \text{if } a < X \leq a + l \\ l & \text{if } a + l < X < \infty. \end{cases} \quad (5.9)$$

Accordingly, the cumulative distribution function of variable  $X_{a,l}$  is

$$F_{X_{a,l}}(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ \frac{F_X(x+a) - F_X(a)}{1 - F_X(a)} & \text{if } 0 \leq x < l \\ 1 & \text{if } l \leq x < \infty. \end{cases} \quad (5.10)$$

It is easy to verify that the moments of the layer distribution are just the limited moments of the excess variable  $X_a$ :

$$E[X_{a,l}] = E[X_a; l] = \frac{E[X; a+l] - E[X; a]}{1 - F_X(a)}, \quad (5.11)$$

$$E[X_{a,l}^2] = E[X_a^2; l] = \frac{E[X^2; a+l] - E[X^2; a] - 2a(E[X; a+l] - E[X; a])}{1 - F_X(a)}, \quad (5.12)$$

$$E[X_{a,l}^3] = E[X_a^3; l] = \frac{E[X^3; a+l] - E[X^3; a] - 3a(E[X^2; a+l] - E[X^2; a])}{1 - F_X(a)} + \frac{3a^2(E[X; a+l] - E[X; a])}{1 - F_X(a)}. \quad (5.13)$$

**Example 5.7.** Random variable  $X$  has a Pareto distribution with parameters  $(\alpha, \beta) = (2; 3,000)$ . What is the average claim size in the layer 4,000 excess of the limit 5,000?

We first calculate the limited severities at the attachment point 5,000 and at  $a + l = 9,000$ . At  $a = 5,000$

$$E[X; 5,000] = \frac{\beta}{\alpha - 1} \left( 1 - \left( \frac{\beta}{5,000 + \beta} \right)^{\alpha - 1} \right) = (3,000) \left( 1 - \frac{3,000}{8,000} \right) = 1,875.$$

A similar calculation yields  $E[X; 9,000] = 2,250$ . Therefore, the layer mean is

$$\frac{E[X; 9,000] - E[X; 5,000]}{1 - F_X(5,000)} = \frac{2,250 - 1,875}{1 - 0.8594} = 2,667. \blacksquare$$

Limits imposed on the size of claims serve to decrease the variability of a claim process. To compare the dispersion of different distributions in a meaningful way, one can use the **coefficient of variation**. For variable  $X$  the coefficient of variation  $CV[X]$  is defined as the ratio of the standard deviation to the mean:

$$CV[X] = \frac{\sqrt{\text{Var}[X]}}{E[X]} = \frac{SD[X]}{E[X]}. \quad (5.14)$$

Because the coefficient of variation is a dimension-less ratio, calculating  $CV$ s for random variables with different means can provide a basis for an apt comparison. In addition,  $CV[X]$  has the useful property of remaining invariant whenever  $X$  is subjected to the linear transformation  $L_c(X) = cX$ , where  $c > 0$  (refer to Problem 2.31):  $CV[cX] = CV[X]$ .

**Example 5.8.** A claim-size variable  $X$  has a lognormal distribution with parameters  $(\mu, \sigma) = (5.9809, 1.800)$ . Probabilities and first and second limited moments at limits 3,000 and 8,000 for this distribution are displayed in the table.

The coefficient of variation of the unlimited variable  $X$  is

| Limit $l$ | $F_X(l)$ | $E[X; l]$ | $E[X^2; l]$ |
|-----------|----------|-----------|-------------|
| 3,000     | 0.869761 | 891       | 1,853,050   |
| 8,000     | 0.952557 | 1,276     | 5,774,970   |
| $\infty$  | 1.000000 | 2,000     | 102,134,385 |

$$CV[X] = \frac{\sqrt{102,134,385 - (2,000)^2}}{2,000} = 4.9531.$$

Not surprisingly, the distribution of  $X_{3K}$  has a smaller CV:

$$E[X_{3K}] = \frac{2,000 - 891}{1 - 0.869761} = 8,515,$$

$$CV[X_{3K}] = \frac{\sqrt{\frac{102,134,385 - 1,853,050 - 2(3,000)(2,000 - 891)}{1 - 0.869761} - (8,515)^2}}{8,515}$$

$$= 2.9858.$$

Restricting claims to the layer between 3,000 and 8,000 by imposing on  $X_{3K}$  an upper limit of 5,000 further reduces the coefficient of variation of the claim-size variable:  $CV[X_{3K}; 5,000] = 0.6452$ . ■

## 5.4. Excess Claim Counts

We now investigate the distribution characteristics of the random variable  $N_a$ , the number of claims excess of an underlying limit  $a$ . Because the very definition of an excess claim depends upon the size of the claim, distributions of excess claim counts involve not only the distribution of the ground-up claim count  $N$ , but also that of the unlimited claim size  $X$ .

If the distribution of  $X$  remains unchanged over time, then the probability of an excess claim also remains constant. Whenever this is true, the distribution of the excess claim count  $N_a$  is related in a simple way to the distribution of the number  $N$  of unrestricted, ground-up claims.

Let  $F_X(x)$  be the cumulative distribution function for the claim-size variable  $X$ . The probability that a claim exceeds  $a$  is  $p = 1 - F_X(a)$ , and the probability of obtaining  $n$  such claims is given by the conditional probability formula (5.15) below. This distribution function for  $N_a$  is derived from the fact that the number  $n$  of excess claims, given the occurrence of  $k$  ground-up claims ( $n \leq k$ ), has a binomial distribution with parameters  $(k, p)$ . The resulting formula is valid for every distribution of the ground-up claim-count variable  $N$ :

$$\begin{aligned} f_{N_a}(n) &= \sum_{k=n}^{\infty} \Pr\{n \text{ excess claims} | N = k\} \cdot \Pr\{N = k\} \\ &= \sum_{k=n}^{\infty} \binom{k}{n} p^n (1-p)^{k-n} f_N(k), \quad n = 0, 1, 2, \dots \end{aligned} \quad (5.15)$$

It is easy to show that  $E[N_a] = pE[N]$ :

$$\begin{aligned} E[N_a] &= \sum_{n=0}^{\infty} n \sum_{k=n}^{\infty} \binom{k}{n} p^n (1-p)^{k-n} f_N(k) \\ &= \sum_{n=0}^{\infty} f_N(k) \sum_{n=0}^k n \binom{k}{n} p^n (1-p)^{k-n} \end{aligned}$$

$$\begin{aligned}
&= \sum_{k=0}^{\infty} f_N(k)(kp) \\
&= pE[N].
\end{aligned}
\tag{5.16}$$

In a similar way one can obtain a formula for the second moment:

$$E[N_a^2] = p^2 E[N^2] + p(1-p)E[N], \tag{5.17}$$

so that

$$Var[N_a] = p^2 Var[N] + p(1-p)E[N]. \tag{5.18}$$

If  $N$  is known to have a specific parametric distribution, one can often determine the exact distribution of  $N_a$ . For example, if  $N$  has a Poisson ( $\lambda$ ) distribution, then (5.15) becomes

$$\begin{aligned}
f_{N_a}(n) &= \sum_{k=n}^{\infty} \binom{k}{n} p^n (1-p)^{k-n} \frac{\lambda^k e^{-\lambda}}{k!} \\
&= \frac{p^n \lambda^n e^{-\lambda}}{n!} \sum_{k=n}^{\infty} \frac{\lambda^{k-n}}{(k-n)!} (1-p)^{k-n} \\
&= \frac{(p\lambda)^n e^{-\lambda}}{n!} \sum_{i=0}^{\infty} \frac{(\lambda - p\lambda)^i}{i!} \\
&= \frac{(p\lambda)^n e^{-p\lambda}}{n!}.
\end{aligned}$$

This means that  $N_a$  is also Poisson-distributed, with parameter  $\lambda_a = p\lambda$ .

It is likewise true that if  $N$  has a negative binomial distribution of the form (3.17) with parameters  $(\alpha, v)$ , then  $N_a$  has a negative binomial distribution as well, but with parameters  $(\alpha, pv)$ . A proof is requested in Problem 5.17.

**Example 5.9.** The number of claims for a ground-up claim process is Poisson-distributed with  $\lambda = 15$ . Moreover, the unlimited claim-size variable  $X$  has the lognormal distribution of Example 5.8.

Consequently, the number of claims that penetrate a policy layer with attachment point 3,000 also has a Poisson distribution. The expected layer claim count is

$$E[N_{3K}] = \lambda(1 - F_X(3,000)) = (15)(0.130239) = 1.9536. \blacksquare$$

## 5.5. Inflation Effects

In Chapter 2 we saw that the effect of a uniform inflationary trend factor applied to an unlimited claim-size variable is moderated by the presence of a policy limit. In particular, claims subjected to a positive rate of inflation  $r$  and limited by an upper

limit increase at a rate less than  $r$ . In this section we continue that previous discussion and explore the effects of uniform inflationary pressure on claims excess of a fixed lower limit.

Suppose that the inflation factor  $\tau = 1 + r$  is applied to the ground-up claim size  $X$  with c.d.f.  $F_X(x)$ . Then the average claim sizes excess of the limit  $a$  before and after trending are, respectively,

$$E[X_a] = \frac{E[X] - E[X; a]}{1 - F_X(a)} \quad \text{and} \quad E[\tau X_a] = \frac{\tau E[X] - \tau E[X; a/\tau]}{1 - F_X(a/\tau)}.$$

Consequently, the effective trend factor  $\tilde{\tau}$  for the excess claim size  $X_a$  is

$$\tilde{\tau} = \frac{E[\tau X_a]}{E[X_a]} = \tau \cdot \frac{E[X] - E[X; a/\tau]}{E[X] - E[X; a]} \cdot \frac{1 - F_X(a)}{1 - F_X(a/\tau)}. \quad (5.19)$$

Formula (5.19) for  $X_a$  can be easily generalized to the layer claim-size variable  $X_{a,b}$ , as requested in Problem 5.19.

**Example 5.10.** Claim-size random variable  $X$  is Pareto-distributed with parameters  $(\alpha, \beta) = (2; 3,000)$  and is subject to a uniform annual inflation rate of  $r = 10\%$ . What is the annual trend rate for claims excess of 5,000?

The average excess claim size before trending is

$$e_X(5,000) = \frac{5,000 + 3,000}{2 - 1} = 8,000,$$

whereas the average trended claim size is

$$e_{1.10X}(5,000) = (1.10) \frac{5,000/1.10 + 3,000}{2 - 1} = 8,300.$$

Therefore, the effective excess trend rate is  $\tilde{r} = 8,300/8,000 - 1 = 3.75\%$ .

Similarly, the average trended claim size in the layer  $(5,000; 9,000]$  is

$$\frac{(1.10)E[X; 9,000/1.10] - (1.10)E[X; 5,000/1.10]}{1 - F_X(5,000/1.10)} = \frac{2,415 - 1,988}{1 - 0.841922} = 2,701.$$

The non-trended severity in this layer was found in Example 5.7 to be 2,667, so the rate of change for the layer claims is  $\tilde{r} = 2,701/2,667 - 1 = 1.27\%$ , yet another illustration of the damping effect of an upper limit. ■

Having just examined what happens to the *size* of excess claims when the unrestricted claim size is subject to inflation, we turn now to a related question: How does such an inflationary trend affect the *number* of excess claims? One would reasonably expect that, all other things being equal, a positive rate of inflation applied to the claim size

should increase the number of claims excess of a fixed limit  $a$ —after trending, all claims are larger, so there ought to be more of them that exceed the limit.

In fact, if  $E[N]$  is the expected number of ground-up claims and  $\tau_X$  is the claim-size trend factor, then the expected numbers of excess claims before and after trending are, respectively,  $(1 - F_X(a))E[N]$  and  $(1 - F_X(a/\tau_X))E[N]$ . The effective trend factor  $\tilde{\tau}_N$  for the excess claim count *due solely to the effect of inflation on the claim size*  $X$  is therefore given by

$$\tilde{\tau}_N = \frac{1 - F_X(a/\tau_X)}{1 - F_X(a)}. \quad (5.20)$$

To verify that a positive inflation rate applied to the unlimited claim size generally increases the excess claim count, observe that  $\tau_X > 1$  implies that  $a/\tau_X < a$ , and so  $F_X(a/\tau_X) \leq F_X(a)$ . Application of this last inequality to (5.20) yields  $\tilde{\tau}_N \geq 1$ , as expected. A similar argument shows that  $\tilde{\tau}_N \leq 1$  whenever  $\tau_X < 1$ .

**Example 5.11.** As in the previous example, claim-size variable  $X$  has a Pareto distribution with  $(\alpha, \beta) = (2; 3,000)$ . The effective annual trend factor for the number of claims excess of 5,000 due to 10% inflation in the claim size  $X$  is

$$\tilde{\tau}_N = \frac{1 - F_X(5,000/1.10)}{1 - F_X(5,000)} = \frac{1 - 0.841922}{1 - 0.859375} = 1.1241. \blacksquare$$

The 12.41% increase in the number of excess claims in the last example turned out to be larger than the basic claim-size inflation rate. But this is not always the case. Problem 5.21 shows that the rate of change in the number of excess claims can be either larger or smaller than the claim-size inflation rate.

Nevertheless, it *is* possible to generalize about the change in the total aggregate excess loss due to an inflationary trend applied to the unrestricted size of loss. The expected aggregate loss amount  $S$  for claims excess of limit  $a$  is

$$\begin{aligned} E[S] &= E[N_a]E[X_a] \\ &= (1 - F_X(a))E[N] \cdot \frac{E[X] - E[X; a]}{1 - F_X(a)} \\ &= E[N](E[X] - E[X; a]). \end{aligned}$$

Combining equations (5.19) and (5.20) yields the effective trend factor for the aggregate variable  $S$ :

$$\tilde{\tau}_S = \tau_X \frac{E[X] - E[X; a/\tau_X]}{E[X] - E[X; a]}. \quad (5.21)$$

As before,  $\tau_X > 1$  implies that  $a/\tau_X < a$  and  $E[X; a/\tau_X] \leq E[X; a]$ . Consequently, the quotient expression in (5.21) cannot be less than 1, and so  $\tilde{\tau}_S \geq \tau_X$ . Similarly,  $\tilde{\tau}_S \leq \tau_X$  whenever

$\tau_X < 1$ . As we have just demonstrated, the existence of a fixed underlying limit magnifies, or leverages, the effect of the basic uniform claim-size trend on the aggregate excess loss.

**Example 5.12.** As before in Examples 5.10 and 5.11, claim-size  $X$  has a Pareto distribution with  $(\alpha, \beta) = (2; 3,000)$  and is subject to a uniform annual inflation rate of 10%. In addition, the ground-up claim count is increasing at an annual rate of 5%. What is the annual change in the total aggregate loss generated by claims excess of 5,000? How much of this change is due solely to claim-size inflation?

Example 5.11 showed that the claim count increases at a rate of 12.41% due to the increase in  $X$ , so the total increase in the claim count is

$$r_N = (1.05)(1.1241) - 1 = 18.03\%.$$

Since the excess claim size increases at a rate of 3.75%, as shown in Example 5.10, the total aggregate loss increases at the annual rate of

$$r_S = (1.1803)(1.0375) - 1 = 22.46\%.$$

Thus,  $1.2246/1.05 - 1 = 16.6\%$  is the annual rate of increase due only to the claim-size inflation. This result, of course, can also be obtained directly from equation (5.21):

$$\tilde{r}_S = (1.10) \frac{3,000 - 1,807}{3,000 - 1,875} - 1 = 16.6\%. \blacksquare$$

## 5.6. Aggregate Layer Claims

The aggregate-loss random variable  $S$  for claims in the excess layer  $(a, a + l]$  is defined just as in Section 4.2, but with the modified variables  $N_a$  and  $X_{a,l}$  as components. Formulas for the mean, variance, and skewness of  $S$ , in terms of the ground-up claim count  $N$  and unlimited claim size  $X$ , are obtained by applying equations (5.11), (5.12), (5.13), (5.16), and (5.18) to the formulas of (4.9).

For example, if the distribution of  $N$  has mean  $E[N] = \lambda$  and contagion parameter  $\gamma$  so that  $Var[N] = \lambda + \gamma\lambda^2$ , then the layer mean, variance, and skewness can be obtained from the formulas

$$E[S] = \lambda(E[X; a + l] - E[X; a]), \quad (5.22)$$

$$Var[S] = \lambda(E[X^2; a + l] - E[X^2; a]) - 2aE[S] + \gamma(E[S])^2, \quad (5.23)$$

$$\begin{aligned} Sk[S] \cdot (Var[S])^{3/2} &= \lambda(E[X^3; a + l] - E[X^3; a]) - 3aVar[S] \\ &\quad - 3a^2E[S] + 3\gamma E[S]Var[S] - \gamma^2(E[S])^3. \end{aligned} \quad (5.24)$$

**Example 5.13.** The components of a ground-up claim process are as described in Examples 5.8 and 5.9—that is,  $N$  has a Poisson distribution with mean  $\lambda = 15$ , and the claim-size variable  $X$  is lognormally distributed with parameters  $(\mu, \sigma) = (5.9809,$

1.8000). What are the distribution characteristics for random variable  $S$  for claims in the layer 5,000 excess of 3,000?

Formula (5.22) yields the mean

$$E[S] = (15)(1,276 - 891) = 5,775,$$

and the variance and skewness are calculated from (5.23) and (5.24):

$$\text{Var}[S] = (15)(5,774,970 - 1,853,050) - (6,000)(5,775) = 24,178,800,$$

$$\begin{aligned} \text{Sk}[S] &= \frac{(15)(37,049,701,689 - 4,790,705,259)}{(24,178,800)^{3/2}} \\ &\quad - \frac{(9,000)(24,178,800) - (3)(3,000)^2(5,775)}{(24,178,800)^{3/2}} = 0.92816. \end{aligned}$$

Because the expected layer claim count  $\lambda_{3K} = 1.9536$  is small, one should expect the cumulative distribution function for  $S$  to have significant discontinuities at the smaller multiples of the layer limit 5,000. This is clearly evident in Figure 5.4, which displays the graph of  $y = F_S(x)$  as well as that of the continuous shifted gamma approximation to the function. ■

The distribution of Example 5.13 exhibits some properties typical of the distributions of aggregate loss in an excess layer. It is often the case, especially for small portfolios of policies or even for large single policies, that the expected layer claim count is small. As we have seen, this leads to jump discontinuities of substantial size at the lower end of the distribution, thus complicating the task of approximating the distribution with one of the continuous approximation models. Nevertheless, these methods can still return reasonable results for the long tail of the distribution, usually the most important region for applications of the aggregate distribution.

**Figure 5.4. Layer Aggregate Loss Distribution Function [Example 5.13]**

![Figure 5.4: Layer Aggregate Loss Distribution Function. The graph plots the cumulative distribution function y = F_S(x) against the loss amount x. The x-axis ranges from 0 to 25,000 with major ticks every 5,000. The y-axis ranges from 0.0 to 1.0 with major ticks every 0.2. A solid black line represents the 'Aggregate distribution function', which shows a series of jump discontinuities at x = 0, 5,000, 10,000, 15,000, and 20,000. A smooth grey line represents the 'Gamma approximation', which follows the general curve of the aggregate function but is continuous. A horizontal dashed line is drawn at y = 1.0.](e079c2e45b12c1af124ac4e7f8554700_img.jpg)

Figure 5.4: Layer Aggregate Loss Distribution Function. The graph plots the cumulative distribution function y = F\_S(x) against the loss amount x. The x-axis ranges from 0 to 25,000 with major ticks every 5,000. The y-axis ranges from 0.0 to 1.0 with major ticks every 0.2. A solid black line represents the 'Aggregate distribution function', which shows a series of jump discontinuities at x = 0, 5,000, 10,000, 15,000, and 20,000. A smooth grey line represents the 'Gamma approximation', which follows the general curve of the aggregate function but is continuous. A horizontal dashed line is drawn at y = 1.0.

## 5.7. Problems

**5.1** The claim-size random variable  $X$  for a claim process has an exponential distribution with mean 1,000. The expected number of claims for the ground-up claim process is 20. However, policy conditions limit claims to the layer between 1,000 and 3,000.

- (a) Compute the mean and variance of the layer claim size.
- (b) Compute the expected number of layer claims.
- (c) How do the policy conditions alter the coefficient of variation of the claim-size variable?
- (d) If a uniform inflation rate of 10% *per annum* is applied to  $X$ , what is the annual percentage increase in the layer claim size? . . . the layer claim count? . . . the total layer aggregate loss?

**5.2** Compute  $e_X(3,000)$  for the following distributions of  $X$ . Note that the unlimited severity for each distribution is the same:  $E[X] = 2,000$ .

- (a) uniform on  $[0; 4,000]$ .
- (b) gamma,  $(\alpha, \beta) = (2; 1,000)$ .
- (c) exponential,  $\beta = 2,000$ .
- (d) shifted Pareto,  $(\alpha, \beta) = (3; 4,000)$ .
- (e) lognormal,  $(\mu, \sigma) = (5.9809, 1.8000)$ .

**5.3** Verify formulas (5.5) and (5.6) for the second and third moments of  $X_a$ .

**5.4** Verify formulas (5.11), (5.12), and (5.13) for the moments of  $X_{a,l}$ .

**5.5** Prove:  $E[X_{a,l}] = e_X(a) - e_X(a+l) \frac{1 - F_X(a+l)}{1 - F_X(a)}$ .

**5.6** Claim-size variable  $X$  has the mixed cumulative distribution function  $F(x) = \sum_{k=1}^m \omega_k F_k(x)$ , where  $\{F_k\}$  are the component distribution functions and the weights  $\{\omega_k\}$  satisfy  $\omega_k > 0$  and  $\sum_{k=1}^m \omega_k = 1$ . Show that

$$e_X(x) = \frac{\sum_{k=1}^m \omega_k e_k(x)(1 - F_k(x))}{1 - \sum_{k=1}^m \omega_k F_k(x)}, \quad 0 < x < \infty.$$

**5.7** Compute  $\Pr\{X_d > x\}$ , where  $0 < d < x$ , and the distribution of  $X$  is:

- (a) exponential ( $\beta$ ).
- (b) shifted Pareto ( $\alpha, \beta$ ).

**5.8** Prove: If  $E[X]$  exists, then  $E[X] = E[X; x] + e(x)(1 - F(x))$  for all  $x > 0$ .

**5.9** (a) Show that the excess severity function  $e_X(x)$  can be expressed by the integral formula

$$e_X(x) = \int_x^\infty (u - x) dF_X(u) / \int_x^\infty dF_X(u), \quad 0 < x < \infty.$$

- (b) The unlimited claim-size observations  $\langle x_1, x_2, \dots, x_n \rangle$  from a random sample of size  $n$  are grouped into a sequence of intervals of the form  $(c_{k-1}, c_k]$ , where

$n_k = \# \text{ claims in the } k^{\text{th}} \text{ interval}$ ,  $\sum_k n_k = n$ , and  $\bar{x}_k = \text{mean claim size in the } k^{\text{th}} \text{ interval}$ . Show that the sample excess severity function  $e_n(c_k)$  is

$$e_n(c_k) = \frac{\sum_{i>k} n_i (\bar{x}_i - c_k)}{\sum_{i>k} n_i}.$$

- 5.10** For the lognormal claim-size random variable  $X$  of Example 5.8 calculate:  
 (a)  $CV[X; 3,000]$  and  $CV[X; 8,000]$ . Compare these numbers to  $CV[X]$ .  
 (b)  $Sk[X]$ ,  $Sk[X; 3,000]$ , and  $Sk[X; 8,000]$ .
- 5.11** Calculate  $CV[X]$  in terms of the distribution parameters when the distribution of  $X$  is:  
 (a) exponential ( $\beta$ ). (b) gamma ( $\alpha, \beta$ ).  
 (c) lognormal ( $\mu, \sigma$ ). (d) shifted Pareto ( $\alpha, \beta$ ) with  $\alpha > 2$ .  
 (e) uniform on the interval  $[0, a]$ ,  $a > 0$ .
- 5.12** Assume that the policy of Example 5.6 has a ground-up claim process with  $E[N] = 5$  and that the claim-size variable  $X$  is Pareto-distributed with  $(\alpha, \beta) = (3; 5,000)$ . For each layer  $L$  defined in that example compute:  
 (a) probability  $P_L$  that a claim penetrates the layer  $L$ .  
 (b) expected number of layer claims  $E[N_L]$ .  
 (c) expected layer claim size  $E[X_L]$ .  
 (d) expected aggregate layer loss  $E[S_L]$ .

| Layer $L$         | $P_L$  | $E[N_L]$ | $E[X_L]$ | $E[S_L]$ |
|-------------------|--------|----------|----------|----------|
| $[0; 100]$        | _____  | _____    | _____    | _____    |
| $(100; 3,000]$    | _____  | _____    | _____    | _____    |
| $(3,000; \infty)$ | _____  | _____    | _____    | _____    |
| $[0; \infty)$     | 1.0000 | 5.0000   | 2,500.00 | 12,500   |

- 5.13** Assume that  $E[X]$  exists and that the partition

$$0 = b_0 < b_1 < b_2 < \cdots < b_{m-1} < b_m = \infty$$

defines a sequence of  $m$  contiguous layers. Prove: if  $\mu_k$  is the mean claim size for the  $k^{\text{th}}$  layer  $(b_{k-1}, b_k]$  and  $p_k = \Pr\{X > b_{k-1}\}$ , then  $E[X] = \sum_{k=1}^m p_k \mu_k$ .

- 5.14** Let  $X$  denote an unlimited claim-size variable with distribution function  $F$ , and assume that  $0 \leq a < b$ . The claim *interval* between  $a$  and  $b$  is just the set of claims of size  $X$  such that  $a < X \leq b$ .  
 (a) Explain how the claim *interval* between  $a$  and  $b$  differs from the *layer* defined by  $a$  and  $b$ .  
 (b) If  $\lambda$  is the mean number of ground-up claims, what is the expected number of claims in the interval  $a < X \leq b$ ?  
 (c) Prove that the average claim size in the interval  $a < X \leq b$  is

$$E[X | a < X \leq b] = \frac{E[X; b] - E[X; a] - b(1 - F(b)) + a(1 - F(a))}{F(b) - F(a)}.$$

- 5.15** For the grouped data of Example 5.4 the indicated groups can be used to define either a sequence of claim *intervals* or a sequence of *layers* of coverage. Calculate the average claim size for each interval and each layer.

| Interval/Layer  | Interval Mean | Layer Mean |
|-----------------|---------------|------------|
| (0; 100]        | _____         | _____      |
| (100; 500]      | _____         | _____      |
| (500; 1,000]    | _____         | _____      |
| (1,000; 2,000]  | _____         | _____      |
| (2,000; 4,000]  | _____         | _____      |
| (4,000; 5,000]  | _____         | _____      |
| (5,000; 10,000] | _____         | _____      |

- 5.16** Verify formula (5.17) for the second moment of the excess claim-count random variable  $N_a$ .
- 5.17** Prove that whenever the ground-up claim count  $N$  has a negative binomial distribution of the form (3.17) with parameters  $(\alpha, \nu)$ , then the distribution of the claim count  $N_a$  excess of an underlying limit  $a$  is also negative binomial, with parameters  $(\alpha, p\nu)$ , where  $X$  is the claim-size variable and  $p = 1 - F_X(a)$ .
- 5.18** The ground-up claim count  $N$  has mean  $\lambda$  and contagion parameter  $\gamma$ . Prove that for the excess claim count  $N_a$ , the contagion parameter is unchanged:  $\gamma_a = \gamma$ .
- 5.19** Derive a generalization of formula (5.19) for the effective trend factor  $\tilde{\tau}$  associated with the layer claim size  $X_{a,l}$ .
- 5.20** Show that the leveraging effect on the aggregate excess loss disappears whenever the underlying limit  $a$  is also trended at the same rate as the claim-size variable  $X$ .
- 5.21** Claim-size random variable  $X$  is lognormally distributed with  $(\mu, \sigma) = (5.9809, 1.8000)$  and is subject to an inflation rate of 10% *per annum*. Calculate the corresponding effective inflation rate on the excess claim count for each of the following underlying limits, thus demonstrating that the induced claim-count rate of change can be either more or less than the basic claim-size inflation rate.  
**(a)**  $a = 3,000$ . **(b)**  $a = 8,000$ .
- 5.22** Variable  $X$  has a lognormal distribution as in Problem 5.21 and is also subject to a 10% inflation rate. Calculate the effective inflation rate on the excess aggregate loss for each of the following excess layers. What can be said about the effective layer inflation rate as compared to the basic rate of inflation?  
**(a)**  $(a, a + l] = (3,000; 5,000]$ . **(b)**  $(a, a + l] = (3,000; 8,000]$ .

**5.23** As in Example 5.3, the table summarizes grouped claim-size data from a sample of 1,000 claims. These claims are excess of a 500 straight deductible and have been censored by a policy limit of 100,000.

| Size Group     | # Claims |
|----------------|----------|
| 0–1,000        | 236      |
| 1,001–2,000    | 161      |
| 2,001–3,000    | 107      |
| 3,001–5,000    | 135      |
| 5,001–10,000   | 159      |
| 10,001–15,000  | 71       |
| 15,001–25,000  | 62       |
| 25,001–50,000  | 43       |
| 50,001–75,000  | 11       |
| 75,001–100,000 | 15       |
| Total          | 1,000    |

(a) Use the minimum chi-square method to obtain estimates of lognormal parameters for the ground-up population claim-size distribution.

(b) Estimate the number of claims eliminated by the policy deductible.

**5.24** Assume that  $X$  is a continuous claim-size random variable for which  $E[X]$  exists as a finite number. Derive this integral formula for  $e_X(x)$ :

$$e_X(x) = \frac{\int_x^\infty (1 - F_X(u)) du}{1 - F_X(x)}.$$

**5.25** Establish the following asymptotic properties of the mean excess claim size function  $e_X(x)$ . In each case it is useful to express  $e_X(x)$  by the integral formula of Problem 5.24.

(a) If  $X$  has the gamma density function

$$f(x) = \frac{1}{\Gamma(\alpha)\beta^\alpha} x^{\alpha-1} e^{-x/\beta},$$

then  $e_X(x) \approx x/(x/\beta + \alpha - 1)$  for large  $x$  so that  $\lim_{x \rightarrow \infty} e_X(x) = \beta$ . [Hint: Apply l'Hôpital's Rule.]

(b) If  $X$  has a Weibull density function

$$f(x) = \frac{\alpha}{\beta^\alpha} x^{\alpha-1} \exp(-(x/\beta)^\alpha), \quad 0 < x < \infty,$$

then  $e_X(x) \approx \beta^\alpha/(\alpha x^{\alpha-1})$  for large  $x$ . [Hint: use l'Hôpital's Rule to show that

$$\lim_{x \rightarrow \infty} \frac{e_X(x)}{\beta^\alpha/(\alpha x^{\alpha-1})} = 1.]$$

