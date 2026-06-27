---
paper: bahnemann
chapter: 4
title: 4. Aggregate Claims
topics: [aggregate_loss_distribution, compound_distribution, moment_matching, normal_power_approximation, wilson_hilferty_approximation, panjer_recursion, fourier_approximation]
key_formulas: [aggregate_mean_variance_skewness, panjer_recursion_formula, normal_power_transformation, wilson_hilferty_transformation, heckman_meyers_algorithm]
---

> **TL;DR**
> - S = ΣXᵢ (compound distribution); **E[S]=E[N]E[X]**; **Var[S]=E[N]Var[X]+Var[N](E[X])²**; for Poisson: Var[S]=λE[X²]; MGF: M_S(t)=M_N(log M_X(t))
> - **Normal approximation** (match μ, σ) is poor when skewness κ is large; **shifted gamma** matches all three moments; **normal power** (good when κ<2) and **Wilson–Hilferty** both outperform normal for skewed S
> - **Normal power**: T_NP = √(6/κ·(S−μ)/σ + 9/κ²+1) − 3/κ ≈ Z; **Wilson–Hilferty**: T_WH = 3(2/κ)^{2/3}·((S−μ)/σ+2/κ)^{1/3} − 6/κ + κ/6 ≈ Z; WH generally more accurate
> - **Panjer recursion**: for Poisson (a=0, b=λ) or NB claim count with discrete claim sizes: f_S(m)=(1/(1−ag(0)))·Σ_{k=1}^m (a+bk/m)g(k)f_S(m−k); f_S(0) from MGF
> - **Heckman–Meyers**: piecewise-linear F_X → tractable characteristic function → Fourier inversion (4.44); highly accurate for long-tail probabilities; requires numerical integration

# 4. Aggregate Claims

The probability distribution of the total claim amount  $S$  for a claim process is called an **aggregate loss** (or **aggregate claim**) **distribution**. Because  $S$  depends on two independent random variables—the number of claims  $N$  and the claim size  $X$ —the distribution of  $S$  is a **compound distribution**, that is, an appropriate combination of the claim-count and claim-size distributions. In this chapter we describe how the aggregate distribution and its properties are derived from the component distributions of  $N$  and  $X$  and then discuss some practical methods for evaluating and approximating the distribution.

## 4.1. A Discrete Example

Before providing a general definition of the aggregate distribution in the next section, we illustrate the basic ideas with a simple discrete model in Example 4.1.

**Example 4.1.** Assume first that  $n = 0, 1, 2$  are the only possible numbers of claims and that there exist just three potential claim sizes:  $\{100, 200, 300\}$ . Associated probability functions for  $N$  and  $X$  are shown in the following tables.

| Claim Count $N$                     |          | Claim Size $X$                      |          |
|-------------------------------------|----------|-------------------------------------|----------|
| # Claims $n$                        | $f_N(n)$ | Size $x$                            | $f_X(x)$ |
| 0                                   | 0.60     | 100                                 | 0.40     |
| 1                                   | 0.30     | 200                                 | 0.50     |
| 2                                   | 0.10     | 300                                 | 0.10     |
| $E[N] = 0.50, \text{Var}[N] = 0.45$ |          | $E[X] = 170, \text{Var}[X] = 4,100$ |          |

Thus, there are seven distinct total loss amounts:  $\{0, 100, 200, 300, 400, 500, 600\}$ . Probabilities for these values of  $S$  are defined by

$$f_S(s) = \Pr\{S = s\} = \sum_{n=0}^2 \Pr\{S = s | N = n\} \cdot f_N(n). \quad (4.1)$$

Conditional probabilities  $\Pr\{S = s|N = n\}$  in this formula are displayed here for each  $n$  value and all possible  $s$  values.

|                      | $n = 0$ | $n = 1$ | $n = 2$   |           |           |
|----------------------|---------|---------|-----------|-----------|-----------|
| Amount $s$           | 0       | 100     | 100 + 100 | 100 + 200 | 100 + 300 |
|                      |         | 200     | 200 + 100 | 200 + 200 | 200 + 300 |
|                      |         | 300     | 300 + 100 | 300 + 200 | 300 + 300 |
| $\Pr\{S = s N = n\}$ | 1.00    | 0.40    | 0.16      | 0.20      | 0.04      |
|                      |         | 0.50    | 0.20      | 0.25      | 0.05      |
|                      |         | 0.10    | 0.04      | 0.05      | 0.01      |

Inserting these tabulated probabilities into formula (4.1) yields values of the aggregate probability function. For example,

$$\begin{aligned}
 f_S(300) &= \Pr\{S = 300|N = 0\} f_N(0) + \Pr\{S = 300|N = 1\} f_N(1) \\
 &\quad + \Pr\{S = 300|N = 2\} f_N(2) \\
 &= (0)(0.60) + (0.10)(0.30) + (0.20 + 0.20)(0.10) \\
 &= 0.0700.
 \end{aligned}$$

Other probabilities are obtained in a similar way and then assembled to form the distribution of  $S$ , shown in the table. Figure 4.1 displays a histogram of the discrete probability mass function  $f_S$ .

The expected loss amount for such a policy is  $E[S] = 85$ . In the next section, we shall see that it is not merely coincidental that  $E[S] = (0.50)(170) = E[N]E[X]$ . The premium charge for such a policy would therefore be \$85 plus a loading for the expense of doing business and a provision for profit and risk. ■

| Aggregate Loss $S$                  |          |          |
|-------------------------------------|----------|----------|
| Amount $s$                          | $f_S(s)$ | $F_S(s)$ |
| 0                                   | 0.6000   | 0.6000   |
| 100                                 | 0.1200   | 0.7200   |
| 200                                 | 0.1660   | 0.8860   |
| 300                                 | 0.0700   | 0.9560   |
| 400                                 | 0.0330   | 0.9890   |
| 500                                 | 0.0100   | 0.9990   |
| 600                                 | 0.0010   | 1.0000   |
| $E[S] = 85, \text{Var}[S] = 15,055$ |          |          |

## 4.2. Aggregate Distribution Properties

Example 4.1 shows how values for the aggregate random variable  $S$  can be generated in two steps: (i) select a number of claims  $N = n$  and then (ii) choose  $n$  claim-size values for  $X$ . The sum of these  $n$  numbers is a single value for  $S$ . Assuming that the sizes of successive claims are mutually independent and also independent of the number of claims, one can define the aggregate random variable by

$$S = \begin{cases} 0 & \text{if } N = 0 \\ X_1 + X_2 + \cdots + X_N & \text{if } N > 0, \end{cases}$$

**Figure 4.1. Aggregate Probability Mass Function [Example 4.1]**

![A bar chart showing the aggregate probability mass function f(s) for s from 0 to 600. The y-axis represents f(s) and ranges from 0.0 to 0.6. The x-axis represents s and ranges from 0 to 600. The bars show a distribution that starts at s=0 with a height of approximately 0.6, then drops to about 0.15 at s=100, rises to about 0.18 at s=200, and then gradually decreases to near zero by s=600.](69a2adeb3e48dbd7e9e1af814a9fbb03_img.jpg)

| s   | f(s) |
|-----|------|
| 0   | 0.60 |
| 100 | 0.15 |
| 200 | 0.18 |
| 300 | 0.10 |
| 400 | 0.05 |
| 500 | 0.02 |
| 600 | 0.01 |

A bar chart showing the aggregate probability mass function f(s) for s from 0 to 600. The y-axis represents f(s) and ranges from 0.0 to 0.6. The x-axis represents s and ranges from 0 to 600. The bars show a distribution that starts at s=0 with a height of approximately 0.6, then drops to about 0.15 at s=100, rises to about 0.18 at s=200, and then gradually decreases to near zero by s=600.

where  $X_1, X_2, \dots, X_N$  are independent random variables, all identical to  $X$ . This two-step generation of the aggregate variable  $S$  suggests how to construct the probability distribution for  $S$  from the component claim-count and claim-size distributions. In the discussion that follows,  $f_N(n)$  denotes  $\Pr\{N=n\}$ , and  $F(x)$  is the cumulative distribution function for  $X$ .

For every positive integer  $n$  define  $Y_n = \sum_{k=1}^n X_k$  as the sum of  $n$  independent random variables, each identical to  $X$ . (For later convenience, define  $Y_0 = 0$ .) The distribution function of  $Y_n$  is the convolution of  $n$  replicates of  $F(x)$ :

$$F_n^*(y) = \Pr\{Y_n \leq y\} = \underbrace{(F * F * \cdots * F)}_{n\text{-fold convolution}}(y), \quad n = 1, 2, 3, \dots, -\infty < y < \infty.$$

The convolution of two functions is obtained by a standard integral formula, employed in the following recursive definition of the sequence  $\langle F_n^*(y) \rangle$ :<sup>38</sup>

$$F_0^*(y) = \begin{cases} 0 & \text{if } y < 0 \\ 1 & \text{if } y \geq 0 \end{cases} \quad \text{and}$$

$$F_n^*(y) = (F_{n-1}^* * F)(y) = \int_{-\infty}^{\infty} F_{n-1}^*(y-u) dF(u), \quad n = 1, 2, 3, \dots \quad (4.2)$$

Finally, the aggregate variable  $S$  has the compound distribution function

$$F_S(s) = \sum_{n=0}^{\infty} f_N(n) \Pr\{Y_n \leq s | N=n\} = \sum_{n=0}^{\infty} f_N(n) F_n^*(s), \quad 0 \leq s < \infty. \quad (4.3)$$

<sup>38</sup> Development of the convolution integral formula  $(F_1 * F_2)(x) = \int_{-\infty}^{\infty} F_2(x-u) dF_1(u)$  for the distribution function of the sum of two independent random variables can be found in most textbooks of mathematical probability; see also Problem 4.2. In practice, it is usually easier to derive the distribution of the sum  $Y_n$  from the moment-generating or characteristic functions of the random variables involved than it is to perform the sequence of integrations indicated in (4.2).

The  $m^{\text{th}}$  moments of  $S$  ( $m = 1, 2, 3, \dots$ ) are related to the corresponding moments of the  $\{Y_n\}$  variables by the equation

$$\begin{aligned} E[S^m] &= \int_0^\infty s^m dF_S(s) \\ &= \int_0^\infty s^m \sum_{n=0}^\infty f_N(n) dF_n^*(s) = \sum_{n=0}^\infty f_N(n) \int_0^\infty s^m dF_n^*(s) \\ &= \sum_{n=0}^\infty f_N(n) E[Y_n^m], \end{aligned} \quad (4.4)$$

provided the  $E[Y_n^m]$  exist. Formulas for the first three moments of  $Y_n$ , displayed below, follow from the independence of the  $\{X_k\}$  variables. Derivation of these formulas also depends on the fact that the second and third moments of a sum of independent random variables are the respective sums of the second and third moments of the summands.

$$\begin{aligned} E[Y_n] &= nE[X], \\ E[Y_n^2] &= E[(Y_n - E[Y_n])^2] + (E[Y_n])^2 \\ &= nE[(X - E[X])^2] + (nE[X])^2 \\ &= n\text{Var}[X] + n^2(E[X])^2, \\ E[Y_n^3] &= E[(Y_n - E[Y_n])^3] + 3E[Y_n]E[Y_n^2] - 2(E[Y_n])^3 \\ &= nE[(X - E[X])^3] + 3n^2E[X]\text{Var}[X] + n^3(E[X])^3. \end{aligned}$$

Combining these results with equation (4.4) yields

$$E[S] = \sum_{n=1}^\infty f_N(n)(nE[X]) = \left( \sum_{n=0}^\infty nf_N(n) \right) E[X] = E[N]E[X], \quad (4.5)$$

$$\begin{aligned} E[S^2] &= \sum_{n=1}^\infty f_N(n)(n\text{Var}[X] + n^2(E[X])^2) \\ &= E[N]\text{Var}[X] + E[N^2](E[X])^2, \end{aligned} \quad (4.6)$$

$$\begin{aligned} E[S^3] &= \sum_{n=1}^\infty f_N(n)(nE[(X - E[X])^3] + 3n^2E[X]\text{Var}[X] + n^3(E[X])^3) \\ &= E[N]E[(X - E[X])^3] + 3E[N^2]E[X]\text{Var}[X] \\ &\quad + E[N^3](E[X])^3. \end{aligned} \quad (4.7)$$

Therefore,

$$\begin{aligned} \text{Var}[S] &= E[N]\text{Var}[X] + \text{Var}[N](E[X])^2, \\ \text{Sk}[S] &= \frac{E[N]E[(X - E[X])^3] + 3\text{Var}[N]E[X]\text{Var}[X]}{(\text{Var}[S])^{3/2}} \\ &\quad + \frac{E[(N - E[N])^3](E[X])^3}{(\text{Var}[S])^{3/2}}. \end{aligned} \quad (4.8)$$

If  $N$  is distributed with mean  $E[N] = \lambda$  and contagion parameter  $\gamma$  so that  $\text{Var}[N] = \lambda + \gamma\lambda^2$ , then formulas (4.5) and (4.8) become

$$\begin{aligned} E[S] &= \lambda E[X], \\ \text{Var}[S] &= \lambda E[X^2] + \gamma\lambda^2 (E[X])^2, \\ \text{Sk}[S] &= \frac{\lambda E[X^3] + 3\gamma\lambda^2 E[X]E[X^2] + 2\gamma^2\lambda^3 (E[X])^3}{(\lambda E[X^2] + \gamma\lambda^2 (E[X])^2)^{3/2}}. \end{aligned} \quad (4.9)$$

In the special case that  $N$  has a Poisson distribution, these formulas reduce to

$$\begin{aligned} E[S] &= \lambda E[X], \\ \text{Var}[S] &= \lambda E[X^2], \\ \text{Sk}[S] &= \frac{E[X^3]}{\sqrt{\lambda} (E[X^2])^{3/2}}. \end{aligned} \quad (4.10)$$

Derivations of (4.5)–(4.7) above, based on the fundamental equation (4.4) relating the moments of  $S$  to those of the sequence  $\langle Y_n \rangle$ , are completely straightforward. However, as with any random variable, these formulas can also be derived from the moment-generating function of  $S$  whenever that function exists.

To construct  $M_S(t)$ , start with the moment-generating function of variable  $Y_n$ . For each fixed  $n$ ,  $Y_n = \sum_{k=1}^n X_k$  is the sum of independent identical random variables, and therefore

$$M_{Y_n}(t) = E\left[\exp\left(t \sum_{k=1}^n X_k\right)\right] = \prod_{k=1}^n E[\exp(tX_k)] = (M_X(t))^n,$$

where  $M_X(t)$  is the generating function for the common claim-size variable  $X$ . Accordingly,  $M_S(t)$  is given by the series

$$M_S(t) = E[\exp(tY_N)] = \sum_{n=0}^{\infty} f_N(n) M_{Y_n}(t) = \sum_{n=0}^{\infty} f_N(n) (M_X(t))^n.$$

But this last formula can be interpreted as an expected value with respect to the distribution of  $N$ :

$$M_S(t) = \sum_{n=0}^{\infty} f_N(n)(M_X(t))^n = \sum_{n=0}^{\infty} f_N(n) \exp(n \log M_X(t)) = E_N[\exp(n \log M_X(t))].$$

Thus, in terms of the generating function  $M_N$  for  $N$ :

$$M_S(t) = M_N(\log M_X(t)). \quad (4.11)$$

As usual,  $E[S]$  is now obtainable from (4.11) by differentiation:

$$E[S] = M'_S(0) = M'_N(\log M_X(t)) \frac{M'_X(t)}{M_X(t)} \bigg|_{t=0} = M'_N(0) \frac{M'_X(0)}{M_X(0)} = E[N]E[X].$$

Similar derivations of formulas (4.6) and (4.7) are requested in Problem 4.5.

**Example 4.2.** Assume that the claim-count random variable  $N$  has a Poisson ( $\lambda$ ) distribution:

$$f_N(n) = \frac{\lambda^n e^{-\lambda}}{n!}, \quad n = 0, 1, 2, 3, \dots$$

Moreover, suppose that claim size  $X$  is gamma ( $\alpha$ ,  $\beta$ ) distributed:

$$F(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ \frac{\Gamma(x/\beta, \alpha)}{\Gamma(\alpha)} & \text{if } 0 \leq x < \infty. \end{cases}$$

Accordingly, the moment-generating function for  $X$  is  $M_X(t) = (1 - \beta t)^{-\alpha}$ , and the generating function for the sum of  $n$  independent such gamma variables is the  $n^{\text{th}}$  power of  $M_X(t)$ :

$$(M_X(t))^n = ((1 - \beta t)^{-\alpha})^n = (1 - \beta t)^{-n\alpha}, \quad -\infty < t < 1/\beta.$$

However, this is the generating function of a gamma variable with parameters  $(n\alpha, \beta)$ , so the  $n$ -fold convolution of identical gamma-distributed variables also has a gamma distribution:

$$F_n^*(y) = \begin{cases} 0 & \text{if } -\infty < y < 0 \\ \frac{\Gamma(y/\beta, n\alpha)}{\Gamma(n\alpha)} & \text{if } 0 \leq y < \infty, \quad n = 1, 2, 3, \dots \end{cases}$$

Note that deriving this convolution formula from the moment-generating function is considerably less onerous than carrying out the successive integrations indicated in formula (4.2). The distribution function for this combination of  $N$  and  $X$  can therefore be expressed in closed analytic form:

$$F_S(s) = \begin{cases} 0 & \text{if } -\infty < s < 0 \\ \sum_{n=0}^{\infty} \frac{\lambda^n e^{-\lambda}}{n!} \cdot \frac{\Gamma(s/\beta, n\alpha)}{\Gamma(n\alpha)} & \text{if } 0 \leq s < \infty. \end{cases} \quad (4.12)$$

In the particular instance that  $\lambda = 2.5$  and  $(\alpha, \beta) = (3, 400)$ , the Poisson formulas (4.10) imply that

$$E[S] = \lambda \alpha \beta = (2.5)(3)(400) = 3,000,$$

$$Var[S] = \lambda \alpha (\alpha + 1) \beta^2 = (2.5)(3)(4)(400)^2 = 4,800,000,$$

$$Sk[S] = \frac{\alpha + 2}{\sqrt{\lambda \alpha (\alpha + 1)}} = \frac{5}{\sqrt{30}} = 0.9129.$$

Values for the cumulative distribution function  $F(s)$  in this special case are displayed in Table 4.1. The distribution has a discrete lump of probability of size  $f_N(0) = e^{-2.5} = 0.0821$  at  $s = 0$ , but at all other  $s$  values  $F(s)$  is continuous. A graph of the corresponding probability density function is shown in Figure 4.2. ■

**Table 4.1. Aggregate Distribution  
[Example 4.2]**

| Amount $s$ | $F(s)$ |
|------------|--------|
| 0          | 0.0821 |
| 500        | 0.1096 |
| 1,000      | 0.1867 |
| 2,000      | 0.3755 |
| 3,000      | 0.5613 |
| 4,000      | 0.7152 |
| 5,000      | 0.8273 |
| 6,000      | 0.9013 |
| 7,000      | 0.9465 |
| 8,000      | 0.9723 |
| 9,000      | 0.9863 |
| 10,000     | 0.9934 |

**Figure 4.2. Aggregate Density Function**  
**[Example 4.2]**

![Figure 4.2: Aggregate Density Function. A graph showing the density function f(s) versus s. The x-axis (s) ranges from 0 to 9,000 with major ticks at 0, 3,000, 6,000, and 9,000. The y-axis (f(s)) ranges from 0.00000 to 0.00020 with major ticks at 0.00000, 0.00005, 0.00010, 0.00015, and 0.00020. The curve starts at (0,0), rises to a peak of approximately 0.00019 at s ≈ 1,500, and then gradually declines, passing through a point marked 'Mean' at s = 3,000 with a density of approximately 0.00017. The curve approaches zero as s increases towards 9,000.](111c2953ce033bb5d26aaa0b071e8a7f_img.jpg)

Figure 4.2: Aggregate Density Function. A graph showing the density function f(s) versus s. The x-axis (s) ranges from 0 to 9,000 with major ticks at 0, 3,000, 6,000, and 9,000. The y-axis (f(s)) ranges from 0.00000 to 0.00020 with major ticks at 0.00000, 0.00005, 0.00010, 0.00015, and 0.00020. The curve starts at (0,0), rises to a peak of approximately 0.00019 at s ≈ 1,500, and then gradually declines, passing through a point marked 'Mean' at s = 3,000 with a density of approximately 0.00017. The curve approaches zero as s increases towards 9,000.

In Example 4.2 we observed that the convolution of a gamma cumulative distribution function with itself is also gamma, a fact which led to an easy-to-calculate exact formula for the aggregate distribution function of that example. However, this desirable *reproductive property*—the distribution of a sum of identical independent random variables having the same distribution type as the components—is shared by just a few families of distributions (notably the normal distributions, which are not generally useful as claim-size distributions). In fact, sums of the ubiquitous lognormal and Pareto distributions belong neither to their respective families nor to any other familiar parametric distribution family. As a consequence, actuaries have since the mid-1900s sought to develop various procedures for calculating values of an aggregate distribution. Among these are several approximations using easily calculable parametric distributions, algorithms featuring recursive formulas, Fourier-transform-based methods, and Monte Carlo simulation. The remainder of this chapter is devoted to some of the most important of these techniques.

## 4.3. Approximation by Matching Moments

In this section we discuss a traditional technique of approximation, the method of *matching moments*, similar to the method-of-moments for fitting a distribution model to sample data. This approach is based on the not-unreasonable assumption that two distributions with identical moments of order  $m$ , where usually  $1 \leq m \leq 3$ , are sufficiently similar that one distribution can be used to approximate the other.<sup>39</sup>

The method consists of two steps:

- (i) Calculate from the moments of the claim-count and claim-size distributions the required mean  $\mu = E[S]$ , variance  $\sigma^2 = Var[S]$ , and skewness  $\kappa = Sk[S]$  according to formulas (4.5) and (4.8).
- (ii) Select from a convenient parametric family of continuous distributions the particular member with matching respective first, second, and third moments.

<sup>39</sup> Although the method of matching moments usually gives reasonable results, the assumption on which it is based—that distributions with identical lowest moments are indeed comparable—could fail to hold. It is possible for distributions with identical first-, second-, and third-order moments to be significantly different. For a discussion of this “moment problem” see Pentikäinen [19] and the references cited there. However, Pentikäinen suggests that acceptable approximations are usually obtained by the method of matching moments when the variable  $X$  is restricted to a finite interval, as in the case that claim size is limited by policy conditions.

The cumulative distribution function of this selected parametric distribution could then serve as an approximation to  $F_S$ .

### Normal Approximation

There are several reasons for considering a normal approximation to an aggregate-loss distribution. The variables  $Y_n$  defined in Section 4.2 are the sums of independent, identically distributed claim-size random variables. Thus, when  $n$  is large, the Central Limit Theorem implies that  $Y_n$  is approximately normally distributed. In addition, whenever the claim count is Poisson-distributed with mean  $\lambda$  (but not when  $N$  has a positive contagion parameter—see Problem 4.8), the Poisson formulas (4.10) imply that  $Sk[S]$  is small for large values of  $\lambda$ . In fact, in the Poisson case, one can observe that  $\lim_{\lambda \rightarrow \infty} Sk[S] = 0$ , so that the distribution of  $S$  is asymptotically symmetric.

In such a case—when  $N$  is Poisson-distributed and  $\lambda$  is large—it is useful to try the approximation  $S \approx Y = \sigma Z + \mu$ , where  $Z$  is the standard normal variable. This is equivalent to asserting that the standardized variable

$$T(S) = \frac{S - \mu}{\sigma} \quad (4.13)$$

is approximately standard normal. The **normal approximation**  $S \approx Y = \sigma Z + \mu$  (or equivalently,  $T(S) \approx Z$ ), yields

$$\begin{aligned} F_S(s) &= \Pr\{S \leq s\} = \Pr\{T(S) \leq T(s)\} \\ &\approx \Pr\{Z \leq T(s)\} = \Phi(T(s)) = \Phi((s - \mu)/\sigma), \quad 0 \leq s < \infty. \end{aligned} \quad (4.14)$$

Because  $E[Y] = E[S] = \mu$  and  $Var[Y] = Var[S] = \sigma^2$ , the normal approximation (4.14) certainly involves matching the first two, but not necessarily the third, moments of the distributions. Of course, the skewness of the symmetric variable  $Y = \sigma Z + \mu$  is zero, whereas  $Sk[S]$  is usually positive. Because of this, the normal approximation generally underestimates the probabilities of large claims. Moreover, it could assign significant probability to negative values of  $s$  and thereby fail to model acceptably the short tail of the aggregate distribution (for instance, refer to Example 4.3). Obviously, the normal approximation is useful only in those cases where  $S$  is nearly symmetric. In other situations one must look elsewhere for a satisfactory approximation.

### Gamma Approximation

When  $S$  is notably skewed, one way to improve on the normal approximation is to match moments with a known skewed distribution. The versatile family of gamma distributions often provides a reasonable starting point.

For example, consider a gamma-distributed variable  $G$  with parameters  $(\alpha, \beta)$ . The required mean  $\mu$  and variance  $\sigma^2$  then determine  $\alpha$  and  $\beta$ :

$$\begin{cases} \mu = \alpha\beta \\ \sigma^2 = \alpha\beta^2 \end{cases} \quad \text{implies} \quad \begin{cases} \alpha = \mu^2/\sigma^2 \\ \beta = \sigma^2/\mu. \end{cases}$$

With these parameters the distribution of  $G$  has the specified mean and variance, and it is also skewed, with  $Sk[G] = 2\sigma/\mu > 0$ . However, the utility of the gamma approximation  $S \approx G$  depends on how close  $2\sigma/\mu$  is to the desired skewness  $\kappa$ .

For a better approximation—one that matches all three parameters  $\mu$ ,  $\sigma$ , and  $\kappa$ —start again with a gamma variable  $G$ , except this time solve for the gamma parameters in terms of  $\sigma$  and  $\kappa$ :

$$\begin{cases} \sigma^2 = \alpha\beta^2 \\ \kappa = 2/\sqrt{\alpha} \end{cases} \text{ implies } \begin{cases} \alpha = 4/\kappa^2 \\ \beta = \frac{1}{2}\sigma\kappa. \end{cases} \quad (4.15)$$

As before, the distribution of  $G$  is now completely determined, but with  $E[G] = \alpha\beta = 2\sigma/\kappa$ . In order to match the required aggregate mean  $\mu$  we introduce the shifted variable  $Y = G + \mu - 2\sigma/\kappa$ , a random variable with all three specified properties:

$$E[Y] = E[G] + \mu - 2\sigma/\kappa = \mu,$$

$$Var[Y] = Var[G] = \sigma^2,$$

$$Sk[Y] = Sk[G] = \kappa.$$

The distribution function of the resulting *shifted gamma approximation*  $S \approx Y$  is

$$\begin{aligned} F_S(s) &\approx F_Y(s) = F_G(s - \mu + 2\sigma/\kappa) \\ &= \Gamma((s - \mu)/\beta + \alpha; \alpha)/\Gamma(\alpha), \quad \mu - 2\sigma/\kappa \leq s < \infty, \end{aligned} \quad (4.16)$$

where gamma parameters  $\alpha$  and  $\beta$  are given by (4.15). Depending on the sign and magnitude of the quantity  $\mu - 2\sigma/\kappa$ , the shift of the origin sometimes adversely affects the modeling of the short tail of the distribution, as in the case of the normal approximation (again, refer to Example 4.3).

### Normalizing Transformations

The normal approximation to  $S$  can also be improved by finding a refinement of the standardizing transformation (4.13) that allows for a better match of the third moments. Specifically, one could look for a transform  $T(S)$  with not only the properties  $E[T(S)] = 0$  and  $Var[T(S)] = 1$  as in (4.13), but with the additional property that the transformed variable be symmetric, or nearly so:  $Sk[T(S)] \approx 0$ . If such a “symmetrizing” function  $T$  could be found, then the assumption  $T(S) \approx Z$  is more likely to provide a satisfactory approximation to  $S$ . Such a transformation must necessarily be more complex than that of standardizing transformation (4.13). In particular, it cannot be *linear*, because the skewness property of a random variable is invariant under such a transformation (refer to Problem 2.26). Two such normalizing functions, described in this section, have been used extensively—the normal power and the Wilson–Hilferty transformations.

For a random variable  $S$  with mean  $\mu$ , variance  $\sigma^2$ , and skewness  $\kappa$  the **normal power transformation** is defined by

$$T_{NP}(S) = \sqrt{\frac{6}{\kappa} \cdot \frac{S - \mu}{\sigma} + \frac{9}{\kappa^2} + 1} - \frac{3}{\kappa}. \quad (4.17)$$

It was proposed in 1969 by Finnish authors Lauri Kauppi and Pertti Ojantakanen, who were seeking an approximation to the Poisson case of an aggregate distribution.<sup>40</sup> Kauppi and Ojantakanen observed that for large values of  $S$  the standardized aggregate variable  $(S - \mu)/\sigma$  could be approximated by a certain quadratic polynomial  $Q$  in the standard normal variable  $Z$ :

$$Q(Z) = \frac{\kappa}{6}(Z^2 - 1) + Z \approx \frac{S - \mu}{\sigma}. \quad (4.18)$$

This approximation formula is based on the so-called Edgeworth series expansion of a distribution function.<sup>41</sup> Solving the approximate equation (4.18) for  $Z$  yields formula (4.17) and the approximation

$$Z \approx T_{NP}(S) = Q^{-1}((S - \mu)/\sigma) = \sqrt{\frac{6}{\kappa} \cdot \frac{S - \mu}{\sigma} + \frac{9}{\kappa^2} + 1} - \frac{3}{\kappa}. \quad (4.19)$$

Thus, the **normal power approximation** to  $F_S$  is

$$F_S(s) \approx \Phi(T_{NP}(s)). \quad (4.20)$$

Formula (4.20) is generally applicable to the long tail of the distribution, the main region of interest in most applications.  $T_{NP}$  is somewhat less successful in modeling the short tail, but a refinement of  $T_{NP}(s)$  for smaller values of  $s$  exists.<sup>42</sup> The Normal Power approach can generally be relied upon to give acceptable results whenever  $S$  is moderately skewed, say when  $\kappa < 2$ .

Another classic approach to this problem is based on the work of Harvard statisticians Edwin B. Wilson and Margaret M. Hilferty. In 1931 Wilson and Hilferty developed a transformation of the chi-square variable  $X = \chi^2(m)$  with  $m$  degrees of freedom that yielded, approximately, the standard normal variable  $Z$ :

$$W(X) = \frac{\sqrt[3]{\frac{1}{m}X - \left(1 - \frac{2}{9m}\right)}}{\sqrt{\frac{2}{9m}}} \approx Z. \quad (4.21)$$

<sup>40</sup> Kauppi and Ojantakanen [10].

<sup>41</sup> A detailed derivation of the normal power approximation from the Edgeworth expansion can be found in Beard, Pentikäinen, and Pesonen [3], pp. 107–110, 355–356.

<sup>42</sup> *Ibid.*, pp. 116–117.

This transformation gave rise to a remarkably accurate approximation to the cumulative distribution function of the chi-square random variable:

$$F_{\chi^2(m)}(x) \approx \Phi(W(x)), \quad (4.22)$$

illustrated in Table 4.2. Since its initial appearance the Wilson–Hilferty transformation has been successfully generalized to other random variables—including, as we shall see, moderately skewed aggregate-loss variables.

To generalize (4.21) in this way, recall that  $\chi^2(m)$  is gamma-distributed, with parameters  $\alpha = (1/2)m$  and  $\beta = 2$ . Thus,  $E[\chi^2(m)] = m$  and  $\text{Var}[\chi^2(m)] = 2m$ . Thus, for the scaled variable  $Y = (1/m)\chi^2(m)$  we have  $E[Y] = 1$  and  $\text{Var}[Y] = 2/m$ . Setting  $v = \sqrt{\text{Var}[Y]}$ , one can express transformation  $W$  in (4.21) as

$$W(Y) = \frac{3}{v}(Y^{1/3} - 1) + \frac{v}{3}. \quad (4.23)$$

It is a simple matter now to apply (4.23) to an arbitrary gamma random variable  $G$  with parameters  $(\alpha, \beta)$ . In this case, set  $Y = G/(\alpha\beta)$ , for which  $v = 1/\sqrt{\alpha}$ . Consequently,

$$W(Y) = 3\sqrt{\alpha}(Y^{1/3} - 1) + \frac{1}{3\sqrt{\alpha}},$$

or in terms of the variable  $G$ ,

$$W(G) = 3\sqrt[3]{\alpha} \left( \frac{G - \alpha\beta}{\sqrt{\alpha}\beta} + \sqrt{\alpha} \right)^{1/3} - 3\sqrt{\alpha} + \frac{1}{3\sqrt{\alpha}}. \quad (4.24)$$

**Table 4.2. Wilson-Hilferty Approximation to  $\chi^2(10)$**

| $x$ | $F_{\chi^2(10)}(x)$ | $\Phi(W(x))$ | Relative Error |
|-----|---------------------|--------------|----------------|
| 3   | 0.0186              | 0.0193       | +3.76%         |
| 6   | 0.1847              | 0.1837       | −0.54%         |
| 9   | 0.4679              | 0.4672       | −0.15%         |
| 12  | 0.7149              | 0.7155       | +0.08%         |
| 15  | 0.8679              | 0.8686       | +0.08%         |
| 18  | 0.9450              | 0.9453       | +0.03%         |
| 21  | 0.9789              | 0.9789       | +0.00%         |
| 24  | 0.9924              | 0.9923       | −0.01%         |
| 27  | 0.9974              | 0.9973       | −0.01%         |
| 30  | 0.9991              | 0.9991       | 0.00%          |

Replacing  $G$  with  $S$  and substituting  $\alpha\beta = E[G] = \mu$ ,  $\alpha\beta^2 = \text{Var}[G] = \sigma^2$ ,  $2/\sqrt{\alpha} = Sk[G] = \kappa$  into (4.24) leads to a transformation of the aggregate variable  $S$ :

$$T_{WH}(S) = 3 \left( \frac{2}{\kappa} \right)^{2/3} \left( \frac{S - \mu}{\sigma} + \frac{2}{\kappa} \right)^{1/3} - \frac{6}{\kappa} + \frac{\kappa}{6}. \quad (4.25)$$

As in (4.22), we obtain the **Wilson–Hilferty approximation** to distribution function  $F_S(s)$ :

$$F_S(s) \approx \Phi(T_{WH}(s)), \quad 0 \leq s < \infty. \quad (4.26)$$

Because this approximation has been so successfully applied to gamma random variables, which in turn have provided acceptable approximations to a wide range of aggregate distributions, it is not surprising that the Wilson–Hilferty formula has proved to be useful in approximating aggregate distributions, as well.

In fact, all three approaches that take into consideration the skewness of  $S$ —the shifted gamma, the normal power, and the Wilson–Hilferty schemes—provide acceptable approximations to the aggregate-loss variable  $S$  whenever the skewness is not too large.

**Example 4.3.** The result of applying the normal (4.14), shifted gamma (4.16), normal power (4.20), and Wilson–Hilferty (4.26) approximations to the moderately skewed distribution of Example 4.2 are displayed in Table 4.3. The normal approximation clearly fails to yield a reasonable result, whereas the other three methods generate quite acceptable approximations to the long tail of the distribution.

Application of these same approximations to the Poisson/gamma distribution (4.12) for which  $\lambda = 10$ ,  $\alpha = 0.05$ , and  $\beta = 6,000$  yields the outcomes shown in Table 4.4.

**Table 4.3. Approximations to  $F_S(s)$ :  $\mu = 3,000$ ,  $\sigma = 2,191$ ,  $\kappa = 0.9129$  [Example 4.3]**

| Amount $s$ | $F(s)$ | Normal | Relative Error | Normal Power | Relative Error | Shifted Gamma | Relative Error | Wilson-Hilferty | Relative Error |
|------------|--------|--------|----------------|--------------|----------------|---------------|----------------|-----------------|----------------|
| 0          | 0.0821 | 0.0855 | +4.14%         | 0.0534       | −34.96%        | 0.0459        | −44.09%        | 0.0464          | −43.48%        |
| 1,000      | 0.1867 | 0.1807 | −3.21%         | 0.1900       | +1.77%         | 0.1775        | −4.93%         | 0.1765          | −5.46%         |
| 2,000      | 0.3755 | 0.3240 | −13.72%        | 0.3745       | −0.27%         | 0.3680        | −2.00%         | 0.3668          | −2.32%         |
| 3,000      | 0.5613 | 0.5000 | −10.92%        | 0.5591       | −0.39%         | 0.5607        | −0.11%         | 0.5605          | −0.14%         |
| 4,000      | 0.7152 | 0.6760 | −5.48%         | 0.7125       | −0.38%         | 0.7185        | +0.46%         | 0.7191          | +0.55%         |
| 5,000      | 0.8273 | 0.8193 | −0.97%         | 0.8245       | −0.34%         | 0.8310        | +0.45%         | 0.8318          | +0.54%         |
| 6,000      | 0.9013 | 0.9145 | +1.46%         | 0.8987       | −0.29%         | 0.9038        | +0.28%         | 0.9044          | +0.34%         |
| 7,000      | 0.9465 | 0.9661 | +2.07%         | 0.9443       | −0.23%         | 0.9475        | +0.11%         | 0.9478          | +0.14%         |
| 8,000      | 0.9723 | 0.9888 | +1.70%         | 0.9707       | −0.16%         | 0.9724        | +0.01%         | 0.9724          | +0.01%         |
| 10,000     | 0.9934 | 0.9993 | +0.59%         | 0.9927       | −0.07%         | 0.9930        | −0.04%         | 0.9929          | −0.05%         |

**Table 4.4. Approximations to  $F_S(s)$ :  $\mu = 3,000$ ,  $\sigma = 4,347$ ,  $\kappa = 2.8293$  [Example 4.3]**

| Amount $s$ | $F(s)$  | Normal | Relative Error | Normal Power | Relative Error | Shifted Gamma | Relative Error | Wilson-Hilferty | Relative Error |
|------------|---------|--------|----------------|--------------|----------------|---------------|----------------|-----------------|----------------|
| 0          | 0.00005 | 0.2451 | —              | 0.4023       | —              | 0.1228        | —              | 0.1494          | —              |
| 2,000      | 0.5922  | 0.4090 | −30.94%        | 0.5866       | −0.95%         | 0.5886        | −0.61%         | 0.5835          | −1.47%         |
| 4,000      | 0.7513  | 0.5910 | −21.34%        | 0.7108       | −5.39%         | 0.7504        | −0.12%         | 0.7519          | +0.08%         |
| 6,000      | 0.8401  | 0.7549 | −10.14%        | 0.7978       | −5.04%         | 0.8402        | −0.01%         | 0.8443          | +0.50%         |
| 8,000      | 0.8946  | 0.8750 | −2.19%         | 0.8590       | −3.98%         | 0.8949        | +0.03%         | 0.8992          | +0.51%         |
| 10,000     | 0.9294  | 0.9463 | +1.82%         | 0.9020       | −2.95%         | 0.9298        | +0.04%         | 0.9333          | +0.42%         |
| 12,000     | 0.9522  | 0.9808 | +3.00%         | 0.9322       | −2.10%         | 0.9525        | +0.03%         | 0.9552          | +0.32%         |
| 14,000     | 0.9674  | 0.9943 | +2.78%         | 0.9532       | −1.47%         | 0.9676        | +0.02%         | 0.9694          | +0.21%         |
| 16,000     | 0.9777  | 0.9986 | +2.14%         | 0.9678       | −1.01%         | 0.9778        | +0.01%         | 0.9789          | +0.12%         |
| 18,000     | 0.9846  | 0.9997 | +1.53%         | 0.9779       | −0.68%         | 0.9847        | +0.01%         | 0.9853          | +0.07%         |

This second distribution is considerably more skewed than that in Table 4.3, with  $\mu = 3,000$ ,  $\sigma = 4,347$ , and  $\kappa = 2.8293$ . Again, as expected, the normal approximation is unsuitable. The shifted gamma and Wilson–Hilferty methods, however, produce generally satisfactory results, at least to the long tail, while the normal power approximation is less accurate. ■

## 4.4. Recursion

In contrast to the method of matching moments, in which the approximating distribution for the aggregate-loss random variable is selected from a family of continuous distributions, the next technique under consideration involves a discrete approximating distribution. Values of this distribution are calculated by means of a recursion formula for the aggregate probability function.

The recursion approach has been studied since the mid-1960s, when the Poisson case was first described by R. M. Adelson. It was later extended to other cases by such authors as H. H. Panjer.<sup>43</sup> We present in this section a basic formulation of the recursion method, which rests on a pair of assumptions, one for each of the variables  $N$  and  $X$ .

Suppose first that the claim count  $N$  has a distribution for which the probability function  $f_N(n)$  satisfies, for some constants  $a$  and  $b$ , a recursion relation on  $n$ :

$$f_N(n) = \frac{na + b}{n} f_N(n-1), \quad n = 1, 2, 3, \dots \quad (4.27)$$

<sup>43</sup> Panjer [17].

Whenever  $N$  is Poisson-distributed with  $E[N] = \lambda$ , it is easy to show that probabilities  $f_N(n)$  satisfy (4.27) with  $a = 0$  and  $b = \lambda$ . This relation also holds in the negative binomial case—refer to Problem 3.19.

In addition, assume that claim-size variable  $X$  has a *discrete* structure, with only a finite number of equally spaced values  $x_k$ :

$$\{x_k\} = \{kh : k = 0, 1, 2, \dots, \hat{m}\}, \quad \text{where } h > 0 \text{ is the constant } \textit{step length}. \quad (4.28)$$

We denote the probability mass function for  $X$  by

$$g(k) = \Pr\{X = x_k\} = f_X(x_k),$$

for which, as usual,  $g(k) \geq 0$  and  $\sum_{k=0}^{\infty} g(k) = \sum_{k=0}^{\hat{m}} g(k) = 1$ . It is convenient to select  $\hat{m}$  so that  $\hat{m} = \max\{k : g(k) > 0\}$ .

Again, let  $Y_n = \sum_{i=1}^n X_i$  be the sum of  $n$  ( $n \geq 1$ ) independent random variables, each identical to  $X$ . Because the component variables  $\{X_i\}$  can have only values that are multiples of  $h$ , this is true for each  $Y_n$  and for the aggregate loss variable  $S$ , as well. Probabilities for  $Y_n$  are denoted by

$$g_n(m) = \Pr\{Y_n = mh\}, \quad m = 0, 1, 2, 3, \dots,$$

where, by convention,  $g_0(0) = 1$  and  $g_0(m) = 0$  when  $m \geq 1$ . Thus, the probability function  $f_S(m)$  for  $S$  has the form

$$f_S(m) = \Pr\{S = mh\} = \sum_{n=0}^{\infty} f_N(n) g_n(m), \quad m = 0, 1, 2, 3, \dots \quad (4.29)$$

Because of the independence of the  $\{X_i\}$  it is easy to verify that the convolution probabilities  $g_n(m)$  can be expressed recursively for positive  $n$  by

$$g_n(m) = \sum_{k=0}^m g(k) g_{n-1}(m-k), \quad m = 0, 1, 2, 3, \dots \quad (4.30)$$

In addition, observe that  $g_n(0) = g^n(0)$  for each positive  $n$ , so that

$$f_S(0) = \sum_{n=0}^{\infty} f_N(n) g^n(0) = \begin{cases} f_N(0) & \text{if } g(0) = 0 \\ M_N(\log g(0)) & \text{if } g(0) > 0. \end{cases} \quad (4.31)$$

Finally, applying (4.27) to formula (4.29), we obtain

$$f_S(m) = \sum_{n=1}^{\infty} \left(a + \frac{b}{n}\right) f_N(n-1) g_n(m), \quad m = 1, 2, 3, \dots \quad (4.32)$$

Having established these preliminary results, we can now state and prove the main theorem about  $f_S(m)$ :

The probability function for the aggregate-loss variable with a claim-count distribution satisfying (4.27) and a claim-size variable having the discrete structure (4.28) satisfies a recursion relation on the integer variable  $m$ :

$$f_S(m) = \frac{1}{1 - ag(0)} \sum_{k=1}^m \left( a + \frac{b}{m} k \right) g(k) f_S(m-k), \quad m = 1, 2, 3, \dots, \quad (4.33)$$

and  $f_S(0)$  is given by (4.31).

**Proof:** Verification of formula (4.33) rests on an ingenious argument about conditional probabilities and expectations for the random variables involved in the sums  $\{Y_n\}$  to create an alternative expression for  $g_n(m)$ .

Begin by considering the following conditional probability formula for  $X_n$ . Variables  $X_n$  and  $X_1 + X_2 + \dots + X_{n-1}$  are independent, so for each  $k$  and for each positive  $m$  for which  $g_n(m) \neq 0$

$$\Pr\{X_n = kh | Y_n = mh\} = \frac{g(k)g_{n-1}(m-k)}{g_n(m)}.$$

Subject to the condition  $Y_n = mh$ , the expected value of  $X_n$  is therefore

$$E[X_n | Y_n = mh] = h \sum_{k=1}^m \frac{k g(k) g_{n-1}(m-k)}{g_n(m)}. \quad (4.34)$$

It is obvious that

$$\sum_{i=1}^n E[X_i | Y_n = mh] = E[Y_n | Y_n = mh] = mh. \quad (4.35)$$

However, the random variables  $\{X_i\}$  are identical and independent, and they play symmetric roles in the definition of  $Y_n$ . This means that the expected values  $E[X_i | Y_n = mh]$  must be identical, so that the sum in equation (4.35) must also equal  $nE[X_n | Y_n = mh]$ . Consequently,  $E[X_n | Y_n = mh] = (m/n)h$ . Substituting this value into equation (4.34) yields the alternate formula

$$g_n(m) = \frac{n}{m} \sum_{k=1}^m k g(k) g_{n-1}(m-k). \quad (4.36)$$

But  $g(k)g_{n-1}(m-k) = 0$  whenever  $g_n(m) = 0$ , so (4.36) is valid for *all* values of  $m$ .

To conclude, apply (4.30) and (4.36) to formula (4.32) and obtain

$$\begin{aligned} f_S(m) &= \sum_{n=1}^{\infty} a f_N(n-1) g_n(m) + \sum_{n=1}^{\infty} \frac{b}{n} f_N(n-1) g_n(m) \\ &= \sum_{n=1}^{\infty} a f_N(n-1) \sum_{k=0}^m g(k) g_{n-1}(m-k) + \sum_{n=1}^{\infty} \frac{b}{n} f_N(n-1) \cdot \frac{n}{m} \sum_{k=1}^m k g(k) g_{n-1}(m-k) \end{aligned}$$

$$\begin{aligned}
&= ag(0) \sum_{n=1}^{\infty} f_N(n-1) g_{n-1}(m) + \sum_{k=1}^m \left(a + \frac{b}{m}k\right) g(k) \sum_{n=1}^{\infty} f_N(n-1) g_{n-1}(m-k) \\
&= ag(0) f_S(m) + \sum_{k=1}^m \left(a + \frac{b}{m}k\right) g(k) f_S(m-k).
\end{aligned}$$

Solving this equation for  $f_S(m)$  yields (4.33), as required. ■

**Example 4.4.** Claim-count random variable  $N$  is Poisson-distributed with mean  $\lambda = 1.75$ . Variable  $X$  has a discrete structure of the form (4.28), with  $h = 1,000$ ,  $\hat{m} = 5$ , and the tabulated probabilities  $g(k)$ .

Applying formula (4.33) in succession yields the probability function for the aggregate variable  $S$ :

$$f_S(0) = e^{-1.75} = 0.1738,$$

$$f_S(1) = \frac{1.75}{1}(1)(0.20)(0.1738) = 0.0608,$$

$$f_S(2) = \frac{1.75}{2}[(1)(0.20)(0.0608) + (2)(0.40)(0.1738)] = 0.1323,$$

$$\begin{aligned}
f_S(3) &= \frac{1.75}{3}[(1)(0.20)(0.1323) + (2)(0.40)(0.0608) + (3)(0.20)(0.1738)] \\
&= 0.1046,
\end{aligned}$$

$$\begin{aligned}
f_S(4) &= \frac{1.75}{4}[(1)(0.20)(0.1046) + (2)(0.40)(0.1323) + (3)(0.20)(0.0608) \\
&\quad + (4)(0.15)(0.1738)] = 0.1170,
\end{aligned}$$

....

The cumulative probability function  $F$  is a step function:

$$F_S(s) = \sum_{k=0}^{\lfloor s/b \rfloor} f_S(k).$$

Values of the derived discrete distribution functions for  $S$  are displayed in Table 4.5. ■

In order to use formula (4.33) to approximate the distribution of an aggregate-loss variable  $S$  for which the claim-size variable  $X$  is continuous, or continuous almost everywhere, one must first approximate  $X$  with a discrete variable of the form (4.28) by selecting parameters  $h$  and  $\hat{m}$  and defining probabilities  $g(k)$ .

| $k$      | $x_k$     | $g(k)$ |
|----------|-----------|--------|
| 1        | 1,000     | 0.20   |
| 2        | 2,000     | 0.40   |
| 3        | 3,000     | 0.20   |
| 4        | 4,000     | 0.15   |
| 5        | 5,000     | 0.05   |
| $\geq 6$ | 1,000 $k$ | 0.00   |

**Table 4.5. Aggregate Distribution [Example 4.4]**

| Amount $s$ | $f_s(s)$ | $F_s(s)$ |
|------------|----------|----------|
| 0          | 0.1738   | 0.1738   |
| 1,000      | 0.0608   | 0.2346   |
| 2,000      | 0.1323   | 0.3669   |
| 3,000      | 0.1046   | 0.4715   |
| 4,000      | 0.1170   | 0.5886   |
| 5,000      | 0.0932   | 0.6818   |
| 6,000      | 0.0786   | 0.7604   |
| 7,000      | 0.0641   | 0.8245   |
| 8,000      | 0.0499   | 0.8744   |
| 9,000      | 0.0377   | 0.9121   |
| 10,000     | 0.0274   | 0.9395   |
| 12,000     | 0.0138   | 0.9729   |
| 14,000     | 0.0063   | 0.9886   |
| 16,000     | 0.0027   | 0.9955   |

In general, greater accuracy is achieved by choosing  $h$  small and  $\hat{m}$  large. However, there does exist a tradeoff. The recursive nature of the method requires the calculation of all preceding values  $\{f_s(1), f_s(2), \dots, f_s(m-1)\}$  before  $f_s(m)$  can be evaluated, necessitating a large number of arithmetic operations in most applications. Calculation time can be adversely affected if  $\hat{m}$  becomes too large.

Whenever  $X$  is censored—say, by a policy limit  $l$ —one should select  $h$  and  $\hat{m}$  so that  $\hat{m}h = l$ . On the other hand, if  $X$  is unlimited, then  $\hat{m}h$  must be large enough to guarantee that  $1 - F_X(\hat{m}h)$  is small, as in Example 4.5.

Probabilities  $g(k)$  can be defined in variety of ways. In general, one is faced with the problem of starting with a continuous probability distribution defined by  $F_X$  for *intervals* of  $X$  values and redistributing the total probability mass to a finite set of *point* values. One simple technique, often referred to as the **midpoint method**, is to treat the lattice points  $\{kh\}$  as the midpoints of certain intervals and then assign probabilities as follows:

$$\begin{aligned}
 g(0) &= F_X\left(\frac{1}{2}h\right), \\
 g(k) &= F_X\left(\left(k + \frac{1}{2}\right)h\right) - F_X\left(\left(k - \frac{1}{2}\right)h\right), \quad k = 1, 2, \dots, \hat{m} - 1, \\
 g(\hat{m}) &= 1 - F_X\left(\left(\hat{m} - \frac{1}{2}\right)h\right).
 \end{aligned}
 \tag{4.37}$$

One difficulty with the midpoint method is that when  $h$  is large and  $\hat{m}$  is small the discrete distribution may fail to have the same moments as the continuous distribution for  $X$ . This can often be improved by a careful selection of  $h$  and  $\hat{m}$ .

**Example 4.5.** Return again to the aggregate-loss variable of Example 4.2, in which  $N$  is Poisson with  $E[N] = 2.5$  and  $X$  is gamma-distributed with  $(\alpha, \beta) = (3, 400)$ , so that  $E[X] = 1,200$  and  $Var[X] = 480,000$ .

Now approximate the distribution function using recursion model (4.33), with the midpoint method for assigning claim-size probabilities and two choices for parameters  $h$  and  $\hat{m}$ : (A)  $(h, \hat{m}) = (100, 60)$  and (B)  $(h, \hat{m}) = (20, 300)$ . Note that  $\hat{m}h = 6,000$  in both cases, and that  $F_X(6,000) = 0.99996$ . Both sets of parameters return good approximations to  $E[X]$  and  $Var[X]$ : (1,199.98; 480,642) for option (A) and (1,199.88; 479,846) for (B). Nevertheless, the two options do yield materially different approximations to  $F_S(s)$ , as shown in Table 4.6. ■

## 4.5. Fourier Approximation

We have already observed that the moment-generating function of a random variable is a Laplace transform of its probability density function  $f$ . In an analogous way, the **characteristic function**  $\varphi$  of a random variable is defined as a Fourier transform of the density function:

$$\varphi(t) = E[e^{itX}] = \int_{-\infty}^{\infty} e^{itx} f(x) dx \quad \text{for all real } t \ (i = \sqrt{-1}). \tag{4.38}$$

**Table 4.6. Aggregate Distribution, Discrete Approximations [Example 4.5]**

| Amount $s$ | $F_S(s)$ | Approx (A)<br>$h = 100$ | Relative Error | Approx (B)<br>$h = 20$ | Relative Error |
|------------|----------|-------------------------|----------------|------------------------|----------------|
| 0          | 0.0821   | 0.0821                  | 0.00%          | 0.0821                 | 0.00%          |
| 500        | 0.1096   | 0.1158                  | +5.66%         | 0.1108                 | +1.09%         |
| 1,000      | 0.1867   | 0.1956                  | +4.77%         | 0.1885                 | +0.96%         |
| 2,000      | 0.3755   | 0.3852                  | +2.58%         | 0.3775                 | +0.53%         |
| 3,000      | 0.5613   | 0.5699                  | +1.53%         | 0.5630                 | +0.30%         |
| 4,000      | 0.7152   | 0.7218                  | +0.92%         | 0.7165                 | +0.18%         |
| 5,000      | 0.8273   | 0.8318                  | +0.54%         | 0.8282                 | +0.11%         |
| 6,000      | 0.9013   | 0.9042                  | +0.32%         | 0.9019                 | +0.07%         |
| 7,000      | 0.9465   | 0.9482                  | +0.18%         | 0.9469                 | +0.04%         |
| 8,000      | 0.9723   | 0.9733                  | +0.10%         | 0.9725                 | +0.02%         |
| 9,000      | 0.9863   | 0.9868                  | +0.05%         | 0.9864                 | +0.01%         |
| 10,000     | 0.9934   | 0.9937                  | +0.03%         | 0.9935                 | +0.01%         |

Whereas the moment-generating function of a random variable could fail to exist, the expected value in (4.38) exists for every random variable. Moreover, to every characteristic function there corresponds a unique probability distribution, thus establishing a one-to-one correspondence between the set of probability distributions and the set of characteristic functions.

There exists a variety of formulas that invert formula (4.38) and allow recovery of the density function  $f$ —or equivalently, the distribution function  $F$ —from  $\varphi(t)$ . Particularly useful in this section is the inversion formula

$$\frac{F(x+) + F(x-)}{2} = \frac{1}{2} - \frac{1}{\pi} \int_0^{\infty} \frac{\Im(e^{-itx} \varphi(t))}{t} dt, \quad (4.39)$$

where  $F(x+)$  and  $F(x-)$  are the respective right- and left-hand limits of  $F$  at  $x$ .<sup>44</sup>

The correspondence between distributions and characteristic functions has been exploited by several authors—notably in the early 1980s by Philip Heckman and Glenn Meyers<sup>45</sup>—to develop methods for approximating an aggregate distribution function. These methods generally involve setting up the approximating function in a such a way that an appropriate inversion formula becomes easy to evaluate. The general approach to using characteristic functions as the basis of an approximation is outlined in this section, with particular attention paid to the Heckman–Meyers approach.

The characteristic function of an aggregate variable  $S$  is defined in a manner analogous to that of the moment-generating function  $M_S(t)$ . For each positive integer  $n$  the characteristic function of  $Y_n = \sum_{k=1}^n X_k$  is given by the product

$$\varphi_{Y_n}(t) = E\left[\exp\left(it \sum_{k=1}^n X_k\right)\right] = \prod_{k=1}^n E[\exp(it X_k)] = (\varphi_X(t))^n,$$

where  $\varphi_X(t)$  is that of the common claim-size distribution. Thus,  $\varphi_S(t)$  is given by the series

$$\varphi_S(t) = E[\exp(itY_N)] = \sum_{n=0}^{\infty} f_N(n) \varphi_{Y_n}(t) = \sum_{n=0}^{\infty} f_N(n) (\varphi_X(t))^n. \quad (4.40)$$

Finally,  $\varphi_S(t)$  can be expressed in terms of  $M_N(t)$ , as in (4.11):

$$\varphi_S(t) = M_N(\log \varphi_X(t)). \quad (4.41)$$

In the case that  $N$  has a Poisson ( $\lambda$ ) distribution, this equation becomes

$$\varphi_S(t) = \exp(\lambda \varphi_X(t) - \lambda). \quad (4.42)$$

<sup>44</sup>  $\Im(a + ib)$  denotes the imaginary part of the complex number  $a + ib$ :  $\Im(a + ib) = b$  and  $|a + ib| = \sqrt{a^2 + b^2}$ . Also,  $e^{i\theta}$  can be expressed as a complex number of the form  $a + ib$  by means of Euler's Formula:  $e^{i\theta} = \cos\theta + i \sin\theta$ . Note that if  $F$  is continuous at  $x$ , then  $(1/2)(F(x+) + F(x-)) = F(x)$ . For a derivation of inversion formula (4.39) consult, for example, Parzen [18], pp. 400–413.

<sup>45</sup> Heckman and Meyers [5].

On the other hand, if  $N$  has a negative binomial distribution with mean  $\lambda$  and contagion parameter  $\gamma$  ( $\gamma \neq 0$ ), then

$$\varphi_S(t) = (1 + \lambda\gamma - \lambda\gamma\varphi_X(t))^{-1/\gamma}. \quad (4.43)$$

**Example 4.6.** The characteristic function for the gamma  $(\alpha, \beta)$  random variable is  $\varphi(t) = (1 - i\beta t)^{-\alpha}$ . Therefore, the aggregate variable  $S$  with a Poisson-distributed claim count with mean  $\lambda$  and a gamma  $(\alpha, \beta)$  claim-size distribution has characteristic function  $\varphi_S(t) = \exp(\lambda(1 - i\beta t)^{-\alpha} - \lambda)$ . ■

The Heckman–Meyers algorithm begins with the definition of a piecewise-linear approximation to the cumulative distribution function  $F_X(x)$  for claim-size variable  $X$ . As we shall soon discover, this approach gives rise to a computationally tractable characteristic function for  $S$ . We start by assuming that  $F_X(x)$  is continuous on an interval  $0 < x < l$ . The Heckman–Meyers algorithm accordingly assumes that  $X$  is censored at  $l$ . If one must use an uncensored variable, choose  $l$  large enough so that  $1 - F_X(l)$  is negligibly small. After partitioning the closed interval  $[0, l]$  into  $m$  subintervals

$$0 = c_0 < c_1 < \cdots < c_{m-1} < c_m = l,$$

we approximate  $F_X(x)$  by a piecewise-linear function  $\hat{F}_X(x)$  with nodes at the points<sup>46</sup>

$$(c_k, F_X(c_k)), \quad k = 0, 1, 2, \dots, m.$$

That is, the graph of  $y = \hat{F}_X(x)$  on  $[0, l]$  is a continuous polygonal curve connecting the endpoints  $(0, F_X(0))$  and  $(l, F_X(l))$ . The associated probability density function  $\hat{f}_X(x)$  is a step function—that is,  $\hat{f}_X(x)$  is piecewise constant on  $[0, l]$ , with the sequence of constants defined by

$$\delta_k = \frac{F_X(c_k) - F_X(c_{k-1})}{c_k - c_{k-1}}, \quad k = 1, 2, \dots, m.$$

Consequently, the characteristic function associated with the approximating distribution function  $\hat{F}_X(x)$  is

$$\begin{aligned} \hat{\varphi}_X(t) &= \sum_{k=1}^m \int_{c_{k-1}}^{c_k} \delta_k e^{itx} dx + (1 - F_X(c_m)) e^{ic_m t} \\ &= \sum_{k=1}^m \int_{c_{k-1}}^{c_k} \delta_k (\cos tx + i \sin tx) dx + (1 - F_X(c_m)) e^{ic_m t} \end{aligned}$$

<sup>46</sup> To improve the approximation to  $F_X(x)$  it is advantageous to use a nonregular partition, with partition points closer together nearer  $x = 0$ , where the graph of  $y = F(x)$  is steeper, and farther apart nearer  $x = l$ , where the graph is flatter. For example, the formula  $c_k = \exp(\log(l)k/m)$  for  $1 \leq k \leq m$  often works well—see Example 4.7.

$$\begin{aligned}
&= \frac{1}{t} \sum_{k=1}^m \delta_k (\sin c_k t - \sin c_{k-1} t) + (1 - F_X(c_m)) \cos c_m t \\
&\quad + \frac{i}{t} \sum_{k=1}^m \delta_k (\cos c_{k-1} t - \cos c_k t) + i(1 - F_X(c_m)) \sin c_m t \\
&= A(t) + iB(t),
\end{aligned}$$

where  $A(t)$  and  $B(t)$  denote the real and imaginary parts of  $\hat{\phi}_X(t)$ , respectively. Note that a discrete lump of probability of size  $1 - F_X(l)$  has been incorporated at the upper limit  $l = c_m$ .

We can now use formulas (4.42) and (4.43) to develop the characteristic function for the approximating aggregate distribution. In the Poisson case

$$\hat{\phi}_S(t) = \exp(\lambda A(t) + i\lambda B(t) - \lambda) = R(t)e^{i\theta(t)},$$

where  $R(t) = e^{\lambda A(t) - \lambda}$  and  $\theta(t) = \lambda B(t)$ . In the negative binomial case the function is

$$\hat{\phi}_S(t) = (1 + \lambda\gamma - \lambda\gamma(A(t) + iB(t)))^{-1/\gamma} = R(t)e^{i\theta(t)},$$

with

$$\begin{aligned}
R(t) &= \sqrt{\left(|1 + \lambda\gamma - \lambda\gamma A(t)|^2 + |\lambda\gamma B(t)|^2\right)^{-1/\gamma}} \text{ and} \\
\theta(t) &= -\frac{1}{\gamma} \arctan\left(\frac{\lambda\gamma B(t)}{1 + \lambda\gamma - \lambda\gamma A(t)}\right).
\end{aligned}$$

The cumulative distribution function of  $S$  is recoverable from  $\hat{\phi}_S(t)$  by means of inversion formula (4.39):

$$\begin{aligned}
F_S(s) &\approx \hat{F}_S(s) = \frac{1}{2} - \frac{1}{\pi} \int_0^\infty \frac{\Im(e^{-its} \hat{\phi}_S(t))}{t} dt \\
&= \frac{1}{2} - \frac{1}{\pi} \int_0^\infty \frac{\Im(e^{-its} R(t) e^{i\theta(t)})}{t} dt \\
&= \frac{1}{2} + \frac{1}{\pi} \int_0^\infty \frac{R(t)}{t} \sin(st - \theta(t)) dt,
\end{aligned} \tag{4.44}$$

whenever  $F_S(s)$  is continuous at  $s$ . In their paper [5], Heckman and Meyers use numerical integration to evaluate formula (4.44) at the required values of  $s$ .

**Example 4.7.** An application of the Heckman–Meyers algorithm to the aggregate distribution of Example 4.2 yields the results shown in Table 4.7.<sup>47</sup> Here the

<sup>47</sup> These results were obtained from an implementation of the Heckman–Meyers algorithm in a Microsoft Excel workbook created by the author.

**Table 4.7. Heckman–Meyers Approximation [Example 4.7]**

| Amount $s$ | $F(s)$ | $\hat{F}(s)$ | Relative Error |
|------------|--------|--------------|----------------|
| 0          | 0.0821 | 0.0412       | −49.82%        |
| 500        | 0.1096 | 0.1094       | −0.15%         |
| 1,000      | 0.1867 | 0.1869       | +0.10%         |
| 2,000      | 0.3755 | 0.3757       | +0.06%         |
| 3,000      | 0.5613 | 0.5614       | +0.01%         |
| 4,000      | 0.7152 | 0.7151       | −0.01%         |
| 5,000      | 0.8273 | 0.8271       | −0.02%         |
| 6,000      | 0.9013 | 0.9011       | −0.02%         |
| 7,000      | 0.9465 | 0.9463       | −0.02%         |
| 8,000      | 0.9723 | 0.9722       | −0.01%         |
| 9,000      | 0.9863 | 0.9862       | −0.01%         |
| 10,000     | 0.9934 | 0.9934       | 0.00%          |

basic claim-size interval of definition is taken as  $[0; 20,000]$ , with partition points  $c_k = \exp(\log(20,000)k/256)$ ,  $k = 1, 2, \dots, 256$ . This choice of partition improves the accuracy of the approximation by placing the points closer together at the left end of the interval and farther apart at the right end, where the distribution is flatter. The approximation is highly accurate, except at the single point  $s = 0$ . At this exceptional point there is a discrete lump of probability, the probability of  $N = 0$  claims. Such points of discrete probability give rise to jump discontinuities in the function  $F_S(s)$ , as discussed in the next section. ■

## 4.6. Discontinuities

When a generally continuous claim-size distribution has a nonzero probability amount at a positive singular point  $\xi$ , the corresponding aggregate distribution function has a jump discontinuity at all multiples of  $\xi$ . This phenomenon is always present when the continuous claim-size variable  $X$  is censored at a limit value  $l$ . The distribution of the modified variable has a discrete lump of probability in the amount of  $1 - F_X(l)$  at  $x = l$  and an aggregate distribution function based on the modified distribution would then have jump discontinuities at all positive integer multiples of  $l$ .

The size of the jump discontinuity in the aggregate distribution at  $s = kl$ , the  $k^{\text{th}}$  multiple of the claim limit  $l$ , is given by

$$f_N(k) \cdot (1 - F_X(l))^k, \quad k = 1, 2, 3, \dots \quad (4.45)$$

In situations where  $E[N]$  is fairly large, the probability  $f_N(k)$ —and therefore the size of the discontinuity at  $k$ —is comfortably small. When this occurs the error of

approximation by a continuous function is negligible. On the other hand, when the expected number of claims is small, then the techniques discussed in Sections 4.3 and 4.5 can fail to provide a reasonable approximation at or near such a point of discontinuity. The next example illustrates this situation.

**Example 4.8.** Consider a gamma-distributed claim-size variable  $X$  with  $(\alpha, \beta) = (2.5, 500)$ . The unlimited mean is 1,250, but the distribution limited at  $l = 2,000$  has a mean of 1,147. The limited distribution has a single discrete amount of probability of size 0.1562 at  $l = 2,000$ .

Compounding this claim-size variable with a Poisson claim-count variable with mean  $\lambda = 1.308$  yields an aggregate random variable  $S$  with mean 1,500 =  $(1.308)(1,147)$ . The aggregate distribution function  $F_S$  will then have a jump discontinuity at  $s = 2,000$ , the size of which is given by (4.45) with  $k = 1$ :

$$(1.308)(e^{-1.308})(0.1562) = 0.0552.$$

Approximating the aggregate distribution function by the shifted gamma approximation (4.16) yields the continuous function shown in the graph of Figure 4.3 as the dashed curve. This approximation has considerable error throughout a fairly broad interval about the discontinuity at  $s = 2,000$ .

By way of contrast, the Fourier approximation (4.44) based on the Heckman-Meyers algorithm does a better job of approximating the function near the singular point, but as a continuous function it also has difficulty at the point itself. This approximation is shown in Figure 4.3 as the solid curve. Note that the graph of the Heckman-Meyers function passes through the midpoint of the jump at  $s = 2,000$ . ■

## 4.7. Simulation

Methods for calculating or approximating aggregate loss distributions discussed in the previous sections all involve deterministic models—that is, numbers associated with the approximating distribution are all calculable from definite algorithms and functional

**Figure 4.3. Approximations to  $F(s)$  at a Point of Discontinuity [Example 4.8]**

![Figure 4.3: A graph showing the cumulative distribution function F(s) versus s. The x-axis ranges from 1,900 to 2,100, and the y-axis ranges from 0.63 to 0.73. Three curves are plotted: 'Aggregate Dist' (solid line with a jump at s=2,000), 'Shifted Gamma Approx' (dashed line, continuous), and 'Fourier Approx' (solid line, continuous). The 'Aggregate Dist' curve has a jump at s=2,000, with a solid dot at the top of the jump and an open circle at the bottom. The 'Shifted Gamma Approx' is a straight dashed line. The 'Fourier Approx' is a smooth solid line that passes through the midpoint of the jump at s=2,000.](901925328a30b5a1dd351710f03a2e50_img.jpg)

The graph displays the cumulative distribution function  $F(s)$  against  $s$ . The x-axis is labeled  $s$  and ranges from 1,900 to 2,100. The y-axis is labeled  $F(s)$  and ranges from 0.63 to 0.73. Three curves are shown:

- Aggregate Dist:** A solid line representing the true distribution. It is continuous until  $s = 2,000$ , where it has a jump discontinuity. At  $s = 2,000$ , there is an open circle at the bottom of the jump and a solid dot at the top.
- Shifted Gamma Approx:** A dashed line representing a continuous approximation. It follows a slightly upward-sloping linear path across the discontinuity.
- Fourier Approx:** A solid line representing a continuous approximation based on the Heckman-Meyers algorithm. It is smooth and passes through the midpoint of the jump at  $s = 2,000$ .

A legend at the bottom identifies the curves: "Aggregate Dist" (solid line), "Shifted Gamma Approx" (dashed line), and "Fourier Approx" (solid line).

Figure 4.3: A graph showing the cumulative distribution function F(s) versus s. The x-axis ranges from 1,900 to 2,100, and the y-axis ranges from 0.63 to 0.73. Three curves are plotted: 'Aggregate Dist' (solid line with a jump at s=2,000), 'Shifted Gamma Approx' (dashed line, continuous), and 'Fourier Approx' (solid line, continuous). The 'Aggregate Dist' curve has a jump at s=2,000, with a solid dot at the top of the jump and an open circle at the bottom. The 'Shifted Gamma Approx' is a straight dashed line. The 'Fourier Approx' is a smooth solid line that passes through the midpoint of the jump at s=2,000.

formulas. In this section we turn to another classic approach to the problem—the method of distribution *simulation*, often called *Monte Carlo simulation* in reference to its stochastic basis.

The simulation technique is conceptually simple and straightforward: first (i) generate a large random sample of selections from the parametric distribution in question, and then (ii) create the discrete distribution for this sample, a distribution which can be a useful approximation to the original parametric distribution. In the case of stochastic simulation, however, there is no empirical population of data from which to select a random sample. The sample points must be generated, either from a table of random numbers or by means of a computer random number generator. Such computer software packages—more accurately characterized as pseudo random number generators—typically generate numbers uniformly distributed between 0 and 1.

At the heart of the simulation method lies the following theorem, used to transform a number  $u$  randomly selected from a uniform distribution on the interval  $0 < u < 1$  to a random value of a variable with a specified distribution. Thus, if  $F$  is the distribution function of random variable  $Y$  and  $u$  is a number randomly generated from the interval  $0 < u < 1$ , then  $\tilde{F}^{-1}(u)$ —where  $\tilde{F}^{-1}$  is the generalized inverse function defined at (4.46)—is a randomly generated value of variable  $Y$ .

*Assume that  $F(y) = \Pr\{Y \leq y\}$  is the cumulative distribution function for random variable  $Y$ . The generalized inverse function  $\tilde{F}^{-1}$  is defined for each  $u$  in the open interval  $(0, 1)$  by*

$$\tilde{F}^{-1}(u) = \min\{\xi : u \leq F(\xi)\}. \quad (4.46)$$

*If random variable  $U$  is uniformly distributed on the interval  $(0, 1)$ , then random variable  $\tilde{F}^{-1}(U)$  is identical to  $Y$ :  $\tilde{F}^{-1}(U) = Y$ .*

**Proof:** Observe first that  $\tilde{F}^{-1}$  has the following properties:

$$u \leq F(\tilde{F}^{-1}(u)) \text{ for all } u \text{ in } (0, 1), \quad (4.47)$$

$$\tilde{F}^{-1}(F(y)) \leq y \text{ for all real } y, \quad (4.48)$$

$$\tilde{F}^{-1}(u) \text{ is a nondecreasing function of } u, \quad (4.49)$$

(refer to Problem 4.19). The theorem will be established if we can show that for all real  $y$

$$\{u : \tilde{F}^{-1}(u) \leq y\} = \{u : u \leq F(y)\}. \quad (4.50)$$

Then, if random variable  $U$  is uniformly distributed on  $(0, 1)$ , equation (4.50) implies that

$$\Pr\{F^{-1}(U) \leq y\} = \Pr\{U \leq F(y)\} = F(y), \quad -\infty < y < \infty.$$

As a result, random variables  $\tilde{F}^{-1}(U)$  and  $Y$  have the same cumulative distribution function  $F(y)$ , and so they must be identical:  $\tilde{F}^{-1}(U) = Y$ .

To prove equation (4.50), assume that  $y$  is a fixed real number. First select  $u$  in  $(0, 1)$  so that  $\tilde{F}^{-1}(u) \leq y$ . Because of (4.47) and the fact that  $F$  is a nondecreasing function

$$u \leq F(\tilde{F}^{-1}(u)) \leq F(y). \quad (4.51)$$

Conversely, suppose that  $u \leq F(y)$ . Properties (4.48) and 4.49) imply that

$$\tilde{F}^{-1}(u) \leq \tilde{F}^{-1}(F(y)) \leq y. \quad (4.52)$$

Combining (4.51) and (4.52) yields the desired result. ■

**Example 4.9.** Suppose that  $X$  has the claim-size distribution of Example 4.1, with cumulative distribution function

$$F(x) = \begin{cases} 0 & \text{if } -\infty < x < 100 \\ 0.40 & \text{if } 100 \leq x < 200 \\ 0.90 & \text{if } 200 \leq x < 300 \\ 1.00 & \text{if } 300 \leq x < \infty. \end{cases}$$

(a) The inverse (4.46) is therefore given by

$$\tilde{F}^{-1}(u) = \begin{cases} 100 & \text{if } 0 < u \leq 0.40 \\ 200 & \text{if } 0.40 < u \leq 0.90 \\ 300 & \text{if } 0.90 < u < 1.00. \end{cases} \quad (4.53)$$

If  $U$  is uniformly distributed on the interval  $(0, 1)$ , then  $\tilde{F}^{-1}(U)$  takes on three possible values—100, 200, 300—with probabilities

$$\Pr\{\tilde{F}^{-1}(U) = 100\} = 0.40 - 0 = 0.40,$$

$$\Pr\{\tilde{F}^{-1}(U) = 200\} = 0.90 - 0.40 = 0.50,$$

$$\Pr\{\tilde{F}^{-1}(U) = 300\} = 1.00 - 0.90 = 0.10.$$

This verifies, of course, that random variables  $\tilde{F}^{-1}(U)$  and  $X$  are identical.

(b) Suppose now that three trials of the random generation process are performed, generating random numbers  $u_1 = 0.4547$ ,  $u_2 = 0.9236$ , and  $u_3 = 0.2573$ . The corresponding random values of  $X$  are obtained from formula (4.53):  $x_1 = \tilde{F}^{-1}(u_1) = 200$ ,  $x_2 = \tilde{F}^{-1}(u_2) = 300$ , and  $x_3 = \tilde{F}^{-1}(u_3) = 100$ . ■

The next three examples illustrate methods for generating random values of commonly encountered claim-size and claim-count random variables.

**Example 4.10.** (a) Variable  $X_1$  is exponentially distributed, with  $F_1(x) = 1 - e^{-x/\beta}$  for  $0 < x < \infty$ . Because  $F_1$  is strictly increasing for positive  $x$ , the function is invertible

**Table 4.8. Random Values for Claim-Size Distributions [Example. 4.10(d)]**

| Trial | Uniform<br>$u$ | Exponential<br>$x_1$ | Pareto<br>$x_2$ | Std Normal<br>$z$ | Lognormal<br>$x_3$ |
|-------|----------------|----------------------|-----------------|-------------------|--------------------|
| (1)   | 0.1854         | 410                  | 216             | -0.8950           | 18                 |
| (2)   | 0.3038         | 724                  | 397             | -0.5135           | 44                 |
| (3)   | 0.5498         | 1,596                | 981             | 0.1252            | 189                |
| (4)   | 0.7953         | 3,172                | 2,420           | 0.8249            | 947                |
| (5)   | 0.9774         | 7,580                | 11,304          | 2.0028            | 14,221             |

there in the ordinary sense, and the inverse defined in (4.46) is identical to the conventional inverse function:

$$x = F_1^{-1}(u) = -\beta \log(1 - u), \quad 0 < u < 1.$$

Alternatively, because  $1 - U$  is also distributed uniformly on the interval  $(0, 1)$ , one can generate a random value for  $x$  by the equation  $x = -\beta \log u$ ,  $0 < u < 1$ .

(b) Similarly, when random variable  $X_2$  has a shifted Pareto distribution with distribution function  $F_2(x) = 1 - (\beta/(x + \beta))^\alpha$  for  $0 < x < \infty$ , the inverse function is given by

$$x = F_2^{-1}(u) = \beta \left( (1 - u)^{-1/\alpha} - 1 \right), \quad 0 < u < 1.$$

(c) Random variable  $X_3$  has a lognormal distribution with parameters  $(\mu, \sigma)$ . Thus, if  $z$  is a randomly generated value of the standard normal distribution,<sup>48</sup> then  $x = \exp(\mu + \sigma z)$  is a random value for  $X_3$ .

(d) Five values of  $u$  were randomly generated from the uniform distribution on the interval  $(0, 1)$ . Corresponding random values for  $X_1$  when  $\beta = 2,000$ , for  $X_2$  when  $(\alpha, \beta) = (2; 2,000)$ , for standard normal  $Z$ , and for  $X_3$  when  $(\mu, \sigma) = (4.956, 2.3)$  are displayed in Table 4.8. ■

**Example 4.11.** (a) Variable  $X$  has a gamma distribution with probability density function

$$f(x) = \frac{1}{\beta^n \Gamma(n)} x^{n-1} e^{-x/\beta} \quad (n = 1, 2, 3, \dots, \beta > 0), \quad 0 < x < \infty.$$

The reproductive property of the gamma distribution implies that  $X$  has the same distribution as the sum of  $n$  independent random variables  $X_b$ , each with the exponential distribution with parameter  $\beta$  (refer to Section 2.3). Thus, to generate a random value

<sup>48</sup> Users of Microsoft Excel find the composite of two worksheet functions `NORM.S.INV(RAND)` convenient for generating random values of the standard normal variable  $Z$ . Refer to Appendix A.1 and also to Problem 4.26.

for  $X$ , generate values for each of the identical random variables  $X_i$ —the sum of these values is a random value for  $X$ :

$$x = x_1 + x_2 + \cdots + x_n.$$

(b) Variable  $X$  has a gamma distribution with  $(\alpha, \beta) = (3, 400)$ . Three random values are generated from the uniform distribution on  $(0, 1)$ : 0.5349, 0.8762, 0.2009 (three different random values of the uniform distribution are required because the  $X_i$  must be independent). Thus, we have a random value for  $X$ :

$$\begin{aligned} x &= -(400)\log(1 - 0.5349) - (400)\log(1 - 0.8762) - (400)\log(1 - 0.2009) \\ &= 1,232. \end{aligned}$$

**Example 4.12.** (a) Variable  $N$  has a Poisson distribution with mean  $\lambda = \# \text{ claims per unit time}$ :

$$f_N(n) = \frac{\lambda^n e^{-\lambda}}{n!}, \quad n = 0, 1, 2, \dots$$

The random variable  $\hat{T}_n$ , where  $\hat{T}_1 = \text{occurrence time of the first claim}$  and  $\hat{T}_n = \text{time between the occurrence of the } (n-1)^{\text{st}} \text{ and the } n^{\text{th}} \text{ claim } (n > 1)$ , has an exponential distribution with parameter  $\beta = 1/\lambda$  [refer to Problem 3.33(c)]. Thus, the event that  $N = n$  in a unit of time is equivalent to

$$\sum_{i=1}^n \hat{T}_i \leq 1 < \sum_{i=1}^{n+1} \hat{T}_i. \quad (4.54)$$

If  $\{u_i\}$  are values of the random variable  $U$ , uniformly distributed on the interval  $(0, 1)$ , then by the result of Example 4.10(a) above, we have corresponding values of  $\hat{T}_i$ :  $t_i = -(1/\lambda)\log u_i$ . As a result, inequality (4.54) is satisfied whenever

$$\sum_{i=1}^n -(1/\lambda)\log u_i \leq 1 < \sum_{i=1}^{n+1} -(1/\lambda)\log u_i.$$

After multiplying by  $-1$  and applying the exponential function, we obtain the equivalent inequality

$$\prod_{i=1}^n u_i \geq e^{-\lambda} > \prod_{i=1}^{n+1} u_i. \quad (4.55)$$

Inequality (4.55) can now be used to generate a random value for  $N$  in the following way, a method easily programmed for computer implementation:

- (i) Assume that  $\langle u_i \rangle$ ,  $i = 1, 2, 3, \dots$ , is a sequence of random values generated from the uniform distribution on the interval  $(0, 1)$ .
- (ii) If  $u_1 < e^{-\lambda}$ , then stop and set  $n = 0$ .

- (iii) Otherwise, if  $u_1 u_2 < e^{-\lambda}$ , then stop and set  $n = 1$ .
- (iv) Otherwise, if  $u_1 u_2 u_3 < e^{-\lambda}$ , then stop and set  $n = 2$ .
- (v) Otherwise, if  $u_1 u_2 u_3 u_4 < e^{-\lambda}$ , then stop and set  $n = 3$ .
- ...

Continue in this way until (4.55) is satisfied by  $i = m$ :

$$\prod_{i=1}^{m+1} u_i < e^{-\lambda} \leq \prod_{i=1}^m u_i;$$

then stop and set  $n = m$ .

(b) Variable  $N$  has a Poisson distribution with mean  $E[N] = \lambda = 1.500$ . Successive products of numbers randomly generated from the uniform distribution on the interval  $(0, 1)$  are compared to  $e^{-1.500} = 0.2231$  according to the procedure developed in part (a) above. Corresponding random values of  $N$  are then calculated, and the results of four such trials are displayed in Table 4.9. ■

The next two examples illustrate how Monte Carlo simulation methods can be used to generate random values of a compound aggregate loss random variable. To generate a single such value, one must first generate a random value for the claim-count variable  $N$ , say  $N = n$ , and then generate  $n$  values for the claim-size variable  $X$ . The sum of these claim-size amounts is a random value for the aggregate loss variable  $S$ .

**Example 4.13.** (a) For the aggregate variable  $S$  the claim-count  $N$  is Poisson-distributed with mean  $\lambda = 1.500$ . Claim-size  $X$  has a lognormal distribution with parameters  $(\mu, \sigma) = (4.956, 2.300)$ . Therefore,  $S$  has mean

$$E[S] = E[N]E[X] = (1.500) \exp\left(4.956 + \frac{1}{2}(2.300)^2\right) = 3,000.$$

For each random value  $n$  obtained for  $N$  we generate  $n$  random values for  $X$ , the sum of which is a random value for  $S$ . Table 4.10 displays the results of this procedure based on the four values for  $n$  generated in Example 4.12(b).

(b) One distinct advantage that Monte Carlo simulation has over other methods of approximating an aggregate loss distribution is the fact that it is easy to model various

**Table 4.9. Random Values for Poisson Distribution [Example 4.12(b)]**

| Trial | $u_1$  | $u_2$  | $u_3$  | $u_4$  | $\prod u_i$ | $e^{-1.500}$ | $n$ |
|-------|--------|--------|--------|--------|-------------|--------------|-----|
| (1)   | 0.6791 | 0.7543 | 0.2391 |        | 0.1225      | 0.2231       | 2   |
| (2)   | 0.1047 |        |        |        | 0.1047      | 0.2231       | 0   |
| (3)   | 0.7591 | 0.4746 | 0.7205 | 0.3256 | 0.0845      | 0.2231       | 3   |
| (4)   | 0.5029 | 0.2874 |        |        | 0.1445      | 0.2231       | 1   |

**Table 4.10. Random Values for Aggregate-Loss Distribution [Example 4.13]**

| Trial | $n$ | Example 4.13(a) |         |       |       | Example 4.13(b) |             |
|-------|-----|-----------------|---------|-------|-------|-----------------|-------------|
|       |     | $u$             | $z$     | $x$   | $s$   | $\tilde{x}$     | $\tilde{s}$ |
| (1)   | 2   | 0.2871          | −0.5619 | 39    | —     | 39              | —           |
|       |     | 0.8945          | 1.2508  | 2,522 | 2,561 | 1,000           | 1,039       |
| (2)   | 0   | —               | —       | —     | 0     | —               | 0           |
| (3)   | 3   | 0.7387          | 0.6393  | 618   | —     | 618             | —           |
|       |     | 0.3766          | −0.3144 | 69    | —     | 69              | —           |
|       |     | 0.9411          | 1.5641  | 5,185 | 5,872 | 1,000           | 1,687       |
| (4)   | 1   | 0.6982          | 0.5192  | 469   | 469   | 469             | 469         |

policy conditions imposed on the size of claims—including complex deductible and/or limit restrictions. As an example, consider the imposition of a \$1,000 policy limit on the size of claims in the claim process described in part (a) above. The results are shown in Table 4.10, where the limit has been imposed on each random claim size as it is generated, yielding the modified random values  $\tilde{x}$  and the associated modified aggregate loss amounts  $\tilde{s}$ . ■

**Example 4.14.** Return now to the aggregate distribution of Example 4.2, for which  $N$  has a Poisson distribution with  $\lambda = 2.5$  and  $X$  is gamma-distributed with parameters  $(\alpha, \beta) = (3, 400)$ . We generate 10,000 values of  $N$ —and for each of these a corresponding aggregate loss amount, thus creating a randomly generated sample of size 10,000. The resulting sample cumulative distribution function is an approximation to the aggregate distribution function  $F(s)$ . For example, 5,599 sample points have aggregate loss amounts less than or equal 3,000, so that

$$F_{10K}(3,000) = \frac{5,599}{10,000} = 0.5599 \approx F_S(3,000).$$

This compares favorably with the actual value of  $F(3,000) = 0.5613$ . Values of the cumulative distribution  $F_{10K}(s)$  based on the generated sample are shown in Table 4.11 along with the exact values of  $F(s)$ . ■

**Example 4.15.** Consider the aggregate random variable  $S$  for which the claim count  $N$  is Poisson-distributed with  $\lambda = 3$  and claim size  $X$  has a lognormal distribution with  $(\mu, \sigma) = (6, 1.5)$ . Moreover, claim size is limited by a policy limit of 1,000. As before, a sample of 10,000 random trials is generated, and the resulting aggregate distribution function created. A graph of  $y = F_{10K}(s)$  is displayed in Figure 4.4, in which the discontinuity at multiples of the 1,000 limit is clearly evident. ■

**Table 4.11. Approximation by Monte Carlo Simulation [Example 4.14]**

| Amount $s$ | $F(s)$ | $F_{10K}(s)$ | Relative Error |
|------------|--------|--------------|----------------|
| 0          | 0.0821 | 0.0832       | +1.34%         |
| 500        | 0.1096 | 0.1084       | -1.09%         |
| 1,000      | 0.1867 | 0.1874       | +0.37%         |
| 2,000      | 0.3755 | 0.3796       | +1.09%         |
| 3,000      | 0.5613 | 0.5599       | -0.25%         |
| 4,000      | 0.7152 | 0.7130       | -0.31%         |
| 5,000      | 0.8273 | 0.8342       | +0.83%         |
| 6,000      | 0.9013 | 0.9042       | +0.32%         |
| 7,000      | 0.9465 | 0.9468       | +0.03%         |
| 8,000      | 0.9723 | 0.9719       | -0.04%         |
| 9,000      | 0.9863 | 0.9865       | +0.02%         |
| 10,000     | 0.9934 | 0.9935       | +0.01%         |

**Figure 4.4. Cumulative Distribution Function  
 $y = F_{10K}(s)$  [Example 4.15]**![A line graph showing the cumulative distribution function y = F_{10K}(s) against the amount s. The x-axis (s) ranges from 0 to 8,000 with major ticks every 2,000. The y-axis (y) ranges from 0.0 to 1.0 with major ticks every 0.2. The curve starts at (0, 0.0832) and increases, passing through points approximately at (1,000, 0.1874), (2,000, 0.3796), (3,000, 0.5599), (4,000, 0.7130), (5,000, 0.8342), (6,000, 0.9042), (7,000, 0.9468), (8,000, 0.9719), and (9,000, 0.9865). The curve levels off towards y=1.0 as s increases.](677895e18a11676be0d822ac49108de3_img.jpg)

A line graph showing the cumulative distribution function y = F\_{10K}(s) against the amount s. The x-axis (s) ranges from 0 to 8,000 with major ticks every 2,000. The y-axis (y) ranges from 0.0 to 1.0 with major ticks every 0.2. The curve starts at (0, 0.0832) and increases, passing through points approximately at (1,000, 0.1874), (2,000, 0.3796), (3,000, 0.5599), (4,000, 0.7130), (5,000, 0.8342), (6,000, 0.9042), (7,000, 0.9468), (8,000, 0.9719), and (9,000, 0.9865). The curve levels off towards y=1.0 as s increases.

## 4.8. Problems

- 4.1** Construct the discrete aggregate loss distribution based on these distributions for  $N$  and  $X$ .

| Claim Count $N$ |          | Claim Size $X$ |          |
|-----------------|----------|----------------|----------|
| Count $n$       | $f_N(n)$ | Size $x$       | $f_X(x)$ |
| 0               | 0.20     | 500            | 0.10     |
| 1               | 0.40     | 1,000          | 0.40     |
| 2               | 0.25     | 1,500          | 0.30     |
| 3               | 0.15     | 2,000          | 0.20     |

- 4.2** Assume that  $Y = X_1 + X_2$ , where  $X_1$  and  $X_2$  are continuous, independent (not necessarily claim-size) random variables.

(a)  $X_1$  and  $X_2$  have respective probability density functions  $f_1$  and  $f_2$ . Prove that

$$f_Y(y) = \int_{-\infty}^{\infty} f_1(y-x) f_2(x) dx.$$

(b) Assume now that  $X_1$  and  $X_2$  are identically distributed claim-size random variables, with common distribution function  $F$  and  $F(x) = 0$  for  $x < 0$ . Show that  $F_Y$  can be expressed as

$$F_Y(y) = \begin{cases} 0 & \text{if } y < 0 \\ \int_0^y F(y-x) dF(x) & \text{if } y \geq 0. \end{cases}$$

- 4.3** Verify that the recursion formula (4.2) yields  $F_1^*(y) = F(y)$  for all  $y$ .
- 4.4** In each of the following cases construct a formula for  $F_S(s)$  in terms of  $f_N(n) = \Pr\{N=n\}$  and  $F_X(x)$ , the c.d.f. for  $X$ .
- (a)  $f_N(n) = 0$  for  $n > 1$ .      (b)  $f_N(n) = 0$  for  $n > 2$ .
- 4.5** Derive formulas (4.6) and (4.7) for  $E[S^2]$  and  $E[S^3]$  from the compound moment-generating function (4.11).
- 4.6**  $N$  is Poisson-distributed with mean  $\lambda$ , and  $X$  has an exponential ( $\beta$ ) distribution. Derive explicit formulas for the aggregate distribution functions  $f_S(s)$  and  $F_S(s)$ .

- 4.7**  $N$  is Poisson-distributed with mean  $\lambda = 8$ , and  $X$  has a gamma distribution with  $\alpha = 0.2000$  and  $\beta = 3,750$ . Calculate the indicated values for  $F_S(s)$ .

| Amount $s$ | $F_S(s)$ |
|------------|----------|
| 0          | _____    |
| 3,000      | _____    |
| 6,000      | _____    |
| 9,000      | _____    |
| 12,000     | _____    |
| 15,000     | _____    |
| 18,000     | _____    |
| 21,000     | _____    |
| 24,000     | _____    |
| 27,000     | _____    |

- 4.8**  $\lambda$  and  $\gamma$  are the claim-count mean and contagion parameter, respectively, for an aggregate loss variable  $S$ . Prove that for fixed  $\gamma$ :

$$(a) \lim_{\lambda \rightarrow \infty} CV[S] = \sqrt{\gamma}. \quad (b) \lim_{\lambda \rightarrow \infty} Sk[S] = 2\sqrt{\gamma}.$$

- 4.9** Verify the normal power inversion formula (4.19):

$$Q^{-1}((S - \mu)/\sigma) = T_{NP}(S),$$

where  $T_{NP}(S)$  is given by (4.17).

- 4.10** Provide detailed derivations of the Wilson–Hilferty transformation formulas (4.24) and (4.25).
- 4.11** Derive from the Wilson–Hilferty chi-square approximation (4.22) a formula for  $\chi_{0.95}^2(m)$ , the 95<sup>th</sup> percentile of the chi-square distribution with  $m$  degrees of freedom.
- 4.12** Use the formula obtained in Problem 4.11 to estimate the chi-square percentiles in the following table.

| d.f. $m$ | $\chi_{0.95}^2(m)$ | Wilson–Hilferty | Relative Error |
|----------|--------------------|-----------------|----------------|
| 5        | 11.070             | _____           | _____%         |
| 10       | 18.307             | _____           | _____%         |
| 15       | 24.996             | _____           | _____%         |
| 20       | 31.410             | _____           | _____%         |
| 25       | 37.652             | _____           | _____%         |
| 30       | 43.773             | _____           | _____%         |

**4.13** Tabulate the following approximations to the Poisson/gamma distribution function of Problem 4.7.

| Amount $s$ | $F_S(s)$ | Normal | Relative Error | Normal Power | Relative Error | Shifted Gamma | Relative Error | Wilson-Hilferty | Relative Error |
|------------|----------|--------|----------------|--------------|----------------|---------------|----------------|-----------------|----------------|
| 0          | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 3,000      | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 6,000      | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 9,000      | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 12,000     | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 15,000     | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 18,000     | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 21,000     | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 24,000     | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |
| 27,000     | _____    | _____  | _____ %        | _____        | _____ %        | _____         | _____ %        | _____           | _____ %        |

**4.14**  $\lambda$  and  $\gamma$  are, respectively, the claim-count mean and contagion parameter for an aggregate loss variable  $S$ . Verify the following special cases of formula (4.31) for  $f(0)$ .

(a) If  $N$  is Poisson-distributed, then  $f_S(0) = e^{\lambda g(0) - \lambda}$ .

(b) If  $N$  has a negative binomial distribution, for which  $\gamma \neq 0$ , then

$$f_S(0) = (1 + \gamma\lambda - \gamma\lambda g(0))^{-1/\gamma}.$$

**4.15** Show that recursion formula (4.33) can be expressed in the following form, where  $\hat{m}$  is defined by (4.28):

$$f_S(m) = \frac{1}{1 - ag(0)} \sum_{k=1}^{\min\{m, \hat{m}\}} \left(a + \frac{b}{m}k\right) g(k) f_S(m-k), \quad m = 1, 2, 3, \dots$$

**4.16** Use the recursion method of Section 4.4 to calculate the cumulative distribution function of the aggregate random variable for which claim size  $X$  has the discrete distribution of Example 4.1 and  $N$  has a Poisson distribution with  $\lambda = 1.35$ .

**4.17** Verify that the midpoint formulas of (4.37) actually define a discrete probability function.

**4.18** Random variable  $U$  is uniformly distributed on the interval  $(0, 1)$ .

(a) Show that the characteristic function of  $U$  is  $\varphi_U(t) = (e^{it} - 1)/(it)$ .

(b) Use formula (4.39) to recover  $F_U(x)$  from  $\varphi_U(t)$ .

- 4.19** Let  $F$  be the cumulative distribution function for random variable  $Y$ . Prove these statements about the inverse function  $\tilde{F}^{-1}$  defined by (4.46).
- (a)  $\tilde{F}^{-1}$  exists for all variables  $Y$ .
  - (b)  $\tilde{F}^{-1}(u)$  is a nondecreasing function of  $u$ .
  - (c)  $u \leq F(\tilde{F}^{-1}(u))$  for all  $u$  in  $(0, 1)$ .
  - (d)  $\tilde{F}^{-1}(F(y)) \leq y$  for all real  $y$ .
  - (e) Show by example that it is possible for the inequalities in (c) and (d) to be *strictly less than*.
  - (f) If  $F$  is strictly increasing, then  $\tilde{F}^{-1}$  is the usual inverse of function  $F$ .
- 4.20**  $F$  is a strictly increasing cumulative distribution function for continuous random variable  $X$ . Prove: random variable  $F(X)$  is uniformly distributed on the unit interval  $(0, 1)$ .
- 4.21** Calculate the inverse function  $\tilde{F}^{-1}(u)$  in the case that  $F(x)$  is a Weibull distribution function (2.61).
- 4.22** Consider the following sequence of random selections from the uniform distribution on the interval  $(0, 1)$ :

$\langle 0.4695, 0.2871, 0.7527, 0.9106, 0.5538, 0.1189, 0.8853 \rangle$ .

Calculate the random value for  $N$  with a Poisson distribution ( $\lambda = 3$ ) that is implied by the sequence.

- 4.23** Five random values of  $U$ , uniformly distributed on the interval  $(1,0)$ , are shown in the table. Calculate corresponding random values for  $X_1$  (exponential with  $\beta = 2,000$ ), for  $X_2$  (Pareto with  $(\alpha, \beta) = (2.5; 3,000)$ ), for  $X_3$  (lognormal with  $(\mu, \sigma) = (5.181, 2.2)$ ), and for  $X_4$  (Weibull with  $(\beta, \delta) = (1,000; 0.5)$ ).

| Trial | Uniform<br>$u$ | Exponential<br>$x_1$ | Pareto<br>$x_2$ | Lognormal<br>$x_3$ | Weibull<br>$x_4$ |
|-------|----------------|----------------------|-----------------|--------------------|------------------|
| (1)   | 0.2097         | _____                | _____           | _____              | _____            |
| (2)   | 0.3562         | _____                | _____           | _____              | _____            |
| (3)   | 0.6970         | _____                | _____           | _____              | _____            |
| (4)   | 0.8245         | _____                | _____           | _____              | _____            |
| (5)   | 0.9882         | _____                | _____           | _____              | _____            |

- 4.24 (a)** Random variable  $N$  has a geometric distribution, with

$$f(n) = p(1-p)^n \quad (0 < p < 1), \quad n = 0, 1, 2, \dots$$

Show that random values of  $N$  can be generated by the formula

$$n = \lceil (\log(1-u)) / (\log(1-p)) - 1 \rceil,$$

where  $\llbracket x \rrbracket$  denotes the greatest integer function. [*Hint: the cumulative distribution function at positive integer  $n$  is*

$$F_N(n) = 1 - (1 - p)^{n+1}.$$

- (b) Use moment-generating functions to show that the sum of  $m$  identical independent random variables, each distributed with a geometric distribution with parameter  $p$  has the special negative binomial distribution with probability density function

$$f(n) = \binom{m+n-1}{n} p^m (1-p)^n \quad (m = 1, 2, 3, \dots, 0 < p < 1), \quad n = 0, 1, 2, \dots$$

- (c) Describe a method for generating random values of a random variable with the negative binomial distribution defined in part (b).
- 4.25** (a) Random variables  $\langle U_n \rangle$  ( $n = 1, 2, \dots, 12$ ) are independent and uniformly distributed on the interval  $(0, 1)$ . Show that the distribution of  $X = \sum_{n=1}^{12} U_n - 6$  is approximately standard normal.
- (b) Use the result of part (a) to devise a method of generating random values from a normal distribution with parameters  $(\mu, \sigma)$ .
- (c) Use the result of part (b) to devise a method of generating random values from a lognormal distribution with parameters  $(\mu, \sigma)$ .

