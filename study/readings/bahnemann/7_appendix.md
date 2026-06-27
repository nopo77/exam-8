---
paper: bahnemann
chapter: null
title: Appendix
topics: [distribution_approximation, normal_distribution_approximation, gamma_distribution_approximation, lognormal_distribution_approximation, monte_carlo_simulation]
key_formulas: [normal_cdf_rational_approximation, inverse_normal_approximation, gamma_cdf_via_incomplete_gamma, lognormal_excel_functions]
---

> **TL;DR**
> - **Normal CDF** Φ(z) has no closed form; approximated by rational function (A.1) with error < 1.5×10⁻⁷; Excel: NORM.S.DIST(z, TRUE) and NORM.DIST(y, μ, σ, TRUE)
> - **Inverse normal** Φ⁻¹(u) approximated by rational function (A.4); used in Monte Carlo simulation via inversion method (set U~Uniform, return Φ⁻¹(U))
> - **Gamma CDF** = Γ(x/β, α)/Γ(α) via incomplete gamma function; no closed form — use chi-square tables (γ=2, α=n/2 case) or Excel GAMMA.DIST
> - **Lognormal** CDF = Φ((log x − μ)/σ); Excel: LOGNORM.DIST(x, μ, σ, TRUE); inverse: LOGNORM.INV — critical for computing limited moments in exam problems
> - These approximations underpin the numerical methods in Chapters 4–6; in exam settings use Excel functions or provided tables rather than deriving from scratch

# Appendix

## A.1. Distribution Approximation

### *Normal Distributions*

The cumulative distribution function of the standard normal random variable  $Z$  is defined by the integral

$$\Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z \exp\left(-\frac{1}{2}u^2\right) du, \quad -\infty < z < \infty.$$

This integral cannot be evaluated by the elementary method involving an antiderivative of the integrand. Consequently, mathematicians have developed approximation formulas involving easily calculated expressions. One such formula, based on a rational function, is cited by Abramowitz and Stegun:<sup>56</sup>

$$\Phi(z) \approx \begin{cases} Q(-z) & \text{if } -\infty < z < 0 \\ 1 - Q(z) & \text{if } 0 \leq z < \infty, \end{cases} \quad (\text{A.1})$$

where

$$Q(z) = \frac{1}{2} \left( 1 + \sum_{k=1}^6 a_k z^k \right)^{-16}$$

and

$$\begin{cases} a_1 = 0.0498673470 & a_2 = 0.0211410061 & a_3 = 0.0032776263 \\ a_4 = 0.0000380036 & a_5 = 0.0000488906 & a_6 = 0.0000053830. \end{cases}$$

The error in approximation (A.1) is bounded by  $1.50 \times 10^{-7}$ .

For users of Microsoft Excel, the built-in worksheet function NORM.S.DIST provides an approximation with precision similar to that of (A.1):

---

<sup>56</sup> Abramowitz and Stegun [1], p. 932. Formula (A.1) is one of several approximations to  $\Phi$  included in this standard reference work.

$$\text{NORM.S.DIST}(z, \text{TRUE}) \approx \Phi(z), \quad -\infty < z < \infty$$

$$\text{NORM.S.DIST}(z, \text{FALSE}) \approx \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{1}{2}z^2\right). \quad (\text{A.2})$$

In addition, Excel provides the related worksheet function NORM.DIST, which returns values of the distribution functions for the normal random variable  $Y = \sigma Z + \mu$  with parameters  $\mu$  and  $\sigma$  ( $\mu > 0$ ,  $\sigma > 0$ ):

$$\text{NORM.DIST}(y, \mu, \sigma, \text{TRUE}) \approx F_Y(y) = \Phi((y - \mu)/\sigma), \quad -\infty < z < \infty,$$

$$\text{NORM.DIST}(y, \mu, \sigma, \text{FALSE}) \approx f_Y(y) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{1}{2}(y - \mu)^2/\sigma^2\right). \quad (\text{A.3})$$

For the purpose of Monte Carlo simulation it is also useful to have available an approximation to the inverse function  $\Phi^{-1}(u)$ . Abramowitz and Stegun offer the following rational function (as usual,  $\log x$  denotes the natural logarithm function):<sup>57</sup>

$$\Phi^{-1}(u) \approx x - \frac{b_0x + b_1x + b_2x^2}{1 + c_1x + c_2x^2 + c_3x^3}, \quad (\text{A.4})$$

where

$$x = \begin{cases} \sqrt{-2 \log u} & \text{if } 0 < u \leq 0.5 \\ \sqrt{-2 \log(1 - u)} & \text{if } 0.5 < u < 1 \end{cases}$$

and

$$\begin{cases} b_0 = 2.515517 & b_1 = 0.802853 & b_2 = 0.010328 \\ c_1 = 1.432788 & c_2 = 0.189269 & c_3 = 0.001308. \end{cases}$$

The error in (A.4) is bounded by  $4.50 \times 10^{-4}$ . Excel also provides the useful worksheet function

$$\text{NORM.S.INV}(u) \approx \Phi^{-1}(u), \quad 0 < u < 1. \quad (\text{A.5})$$

### Gamma Distributions

The gamma function, defined by the convergent improper integral

$$\Gamma(x) = \int_0^\infty u^{x-1} e^{-u} du, \quad 0 < x < \infty,$$

<sup>57</sup> *Ibid.*, p. 933.

can be approximated on the interval  $1 \leq x \leq 2$  by the polynomial

$$\Gamma(x) \approx 1 + \sum_{k=1}^8 d_k (x-1)^k, \quad 1 \leq x \leq 2, \quad (\text{A.6})$$

where

$$\begin{cases} d_1 = -0.577191652 & d_2 = 0.988205891 & d_3 = -0.897056937 \\ d_4 = 0.918206857 & d_5 = -0.756704078 & d_6 = 0.482199394 \\ d_7 = -0.193527818 & d_8 = 0.035868343. \end{cases}$$

This approximation, of course, can be extended to all positive  $x$  by use of the recursive formula  $\Gamma(x) = (x-1)\Gamma(x-1)$ . Error in (A.6) is bounded by  $3 \times 10^{-7}$ .<sup>58</sup> In Microsoft Excel,  $\Gamma(x)$  can be calculated by using the composition of two worksheet functions:  $\text{EXP}(\text{GAMMALN}(x)) \approx \Gamma(x)$  for  $x > 0$ .

In Section 2.3 we showed that the gamma cumulative distribution function (2.16) can be expressed by the formula

$$F(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ \frac{\Gamma(x/\beta, \alpha)}{\Gamma(\alpha)} & \text{if } 0 \leq x < \infty \quad (\alpha > 0, \beta > 0), \end{cases} \quad (\text{A.7})$$

where  $\Gamma(x, \alpha)$  is the incomplete gamma function:

$$\Gamma(x, \alpha) = \int_0^x u^{\alpha-1} e^{-u} du \quad (\alpha > 0), \quad 0 \leq x < \infty. \quad (\text{A.8})$$

The incomplete gamma function (A.8) has a power series expansion:

$$\Gamma(x, \alpha) = x^\alpha e^{-x} \Gamma(\alpha) \sum_{k=0}^{\infty} \frac{x^k}{\Gamma(\alpha + k + 1)} = x^\alpha e^{-x} \frac{\Gamma(\alpha)}{\Gamma(\alpha + 1)} \left( 1 + \sum_{k=1}^{\infty} \frac{x^k}{(\alpha + 1) \dots (\alpha + k)} \right),$$

so that the gamma distribution function (A.7) has a corresponding power series representation

$$F(x) = \frac{(x/\beta)^\alpha e^{-x/\beta}}{\Gamma(\alpha + 1)} \left( 1 + \sum_{k=1}^{\infty} \frac{(x/\beta)^k}{(\alpha + 1) \dots (\alpha + k)} \right). \quad (\text{A.9})$$

An approximation to the gamma distribution function (A.7) can thus be obtained by using an appropriate partial sum of the series (A.9).

<sup>58</sup> *Ibid.*, p. 257.

Again, for users of Microsoft Excel, the worksheet function GAMMA.DIST provides an approximation to both the probability density and the cumulative distribution functions:

$$\begin{aligned}\text{GAMMA.DIST}(x, \alpha, \beta, \text{FALSE}) &\approx f(x) = \frac{1}{\beta^\alpha \Gamma(\alpha)} x^{\alpha-1} e^{-x/\beta}, \quad 0 \leq x < \infty, \\ \text{GAMMA.DIST}(x, \alpha, \beta, \text{TRUE}) &\approx F(x) = \int_0^x f(x) dx.\end{aligned}\quad (\text{A.10})$$

In addition, the worksheet function GAMMA.INV returns an approximation to the inverse cumulative distribution function:

$$\text{GAMMA.INV}(u, \alpha, \beta) \approx F^{-1}(u), \quad 0 \leq u < 1. \quad (\text{A.11})$$

### Lognormal Distributions

For the lognormal distribution function Microsoft Excel provides two worksheet functions. LOGNORM.DIST approximates the lognormal density and cumulative distribution functions with parameters  $\mu$  and  $\sigma$  ( $\mu > 0$ ,  $\sigma > 0$ ):

$$\begin{aligned}\text{LOGNORM.DIST}(x, \mu, \sigma, \text{TRUE}) &\approx F(x) = \Phi((\log x - \mu)/\sigma), \quad 0 < x < \infty, \\ \text{LOGNORM.DIST}(x, \mu, \sigma, \text{FALSE}) &\approx \frac{1}{\sigma\sqrt{2\pi}x} \exp\left(-\frac{1}{2}(\log x - \mu)^2/\sigma^2\right).\end{aligned}\quad (\text{A.12})$$

LOGNORM.INV provides values of the inverse c.d.f.:

$$\text{LOGNORM.INV}(u, \mu, \sigma) \approx F^{-1}(u), \quad 0 \leq u < 1. \quad (\text{A.13})$$

### Weibull Distributions

As in the case of the previously mentioned distributions, the single Excel worksheet function WEIBULL.DIST provides an approximation to both the probability density and the cumulative distribution functions of the Weibull distribution with parameters  $\beta$  and  $\delta$  ( $\beta > 0$ ,  $\delta > 0$ ):

$$\begin{aligned}\text{WEIBULL.DIST}(x, \delta, \beta, \text{TRUE}) &\approx F(x) = 1 - \exp\left(-(x/\beta)^\delta\right), \quad 0 \leq x < \infty, \\ \text{WEIBULL.DIST}(x, \delta, \beta, \text{FALSE}) &\approx f(x) = \frac{\delta}{\beta^\delta} x^{\delta-1} \exp\left(-(x/\beta)^\delta\right).\end{aligned}\quad (\text{A.14})$$

## A.2. Answers to Selected Problems

- 1.1 (b) *Hint:*  $(E^c \cup F^c)^c = E \cap F$   
 (c)  $S = \{\emptyset, \{a\}, \{d\}, \{a, d\}, \{b, c\}, \{a, b, c\}, \{b, c, d\}, \Omega\}.$

- 1.2 (a)  $P(E) + P(E^c) = P(E \cup E^c) = P(\Omega) = 1$ .  
 (e)  $P(F) = P(F \cap E) + P(F \cap E^c) = P(E) + P(F \cap E^c) \geq P(E)$ .
- 1.3 (a)  $\lim_{n \rightarrow \infty} P(E_n) = \lim_{n \rightarrow \infty} P(\bigcup_{k=1}^n E_k) = P(\bigcup_n E_n)$ .
- 1.4 (a) 0.1429. (b) 0.2857. (c) 0.8571.
- 1.5 (b)  $P(E \cup F) = P(E) + P(F) - P(E)P(F) = P(E)P(F^c) + P(F) = P(E)P(F^c) + 1 - P(F^c) = 1 - P(E^c)P(F^c)$ .
- 1.7 (a) 0.2500. (b) 0.1875. (c) 0.8125. (d) 3.8125. (e) 1.7773.
- 1.10 (b)  $(1-p)/p$ . (c)  $E[N] = 1/(1-p)$ ,  $Var[N] = p/(1-p)^2$ .
- 1.11 (a) 0.7500. (b) 0. (c) 0.8484. (d) 0.0597.  
 (e) 0.5000. (f) 1.7500.
- 1.12 (b)  $\Pr\{X = x\} = 0$  implies  $\Pr\{X < x\} = \Pr\{X \leq x\} = F(x)$  for all  $x$ .
- 1.13 (a) 2/3. (b) 4. (c) 1. (d) 15.
- 1.14 (a) 1.5. (b) 3. (c)  $0.125 + 0.375e^t + 0.375e^{2t} + 0.125e^{3t}$ .
- 1.15 (a)  $\frac{1}{2}(\alpha + \beta)$ . (b)  $\frac{1}{3}(\alpha^2 + \alpha\beta + \beta^2)$ . (c)  $(e^{\beta t} - e^{\alpha t})/((\beta - \alpha)t)$ .
- 1.16 (b)  $E[X] = 180$ ,  $Var[X] = 35,600$ .
- 1.17  $E[X] = \frac{1}{2}(\alpha + \beta)$ ,  $Var[X] = \frac{1}{12}(\beta - \alpha)^2$ .
- 1.18  $E[X_a] = 75.00$ ,  $Var[X_a] = 9,375$ .
- 1.19  $E[Y] = \mu$ ,  $Var[Y] = \sigma^2$ .
- 1.20 (b)  $\exp(\mu t + \frac{1}{2}\sigma^2 t^2)$ .
- 1.21 (a)  $pe^t/[1 - (1-p)e^t]$ ,  $t < \log(1-p)$ . (b)  $1/p$ . (c)  $(1-p)/p^2$ .  
 (d)  $p/[1 - (1-p)^2]$ .
- 1.23  $\hat{\beta} = M_1$ .
- 2.1 (a) 1,500. (b) 750,000. (c) 0.1250. (d) 1,375.
- 2.2 (a) 875. (b) does not exist. (c) 0.2500. (d) 687.50.
- 2.3  $(200)(1 - e^{-y/250})$ .
- 2.4  $E[\hat{X}] = 1,532$ ;  $E[\hat{X}; 1,000] = 892$ ,  $E[\hat{X}; 1,500] = 1,203$ .
- 2.6  $M_1 \approx \frac{1}{n} \sum_{k=1}^m n_k a_k$ .

$$2.7 \quad E[X; x] \leq \int_0^x u \, dF(u) + x < \infty.$$

$$2.9 \quad (a) \quad \frac{d}{dx} [\int_0^x u f(u) du + x(1 - F(x))] = 1 - F(x). \quad (b) \quad \text{Use } E[X; 0] = 0 \text{ with (a).}$$

$$2.10 \quad (b) \quad \text{Set } v = u^2. \quad (c) \quad \text{Set } v = \log(1/u).$$

$$2.11 \quad (b) \quad \text{Integration by parts.} \quad (d) \quad \text{Apply (2.18) inductively to } \Gamma(x+1)/\Gamma(x) = x.$$

$$2.13 \quad \alpha = 1, \beta = E[X].$$

$$2.14 \quad \Pr\{X > a + b \mid X > a\} = \Pr\{X > b\}.$$

$$2.15 \quad (a) \quad \omega\beta_1 + (1 - \omega)\beta_2. \quad (b) \quad \omega\beta_1^2 + (1 - \omega)\beta_2^2 + \omega(1 - \omega)(\beta_1 - \beta_2)^2.$$

$$2.16 \quad \text{Excel Solver yields } (\hat{\alpha}, \hat{\beta}) = (4.7432, 337.31).^{59}$$

$$2.17 \quad (b) \quad 556. \quad (d) \quad 0.1461. \quad (e) \quad 0.2108. \quad (f) \quad 1,023. \quad (g) \quad 9,689.$$

$$2.18 \quad (b) \quad (\hat{\mu}, \hat{\sigma}) = (7.235292, 0.477366).$$

$$2.19 \quad (b) \quad 1,040. \quad (d) \quad 0.1866. \quad (e) \quad 0.3254. \quad (f) \quad 1,347. \quad (g) \quad 6,500.$$

$$2.20 \quad \text{Var}[X] = \frac{\alpha}{\alpha - 2} (E[X])^2 > (E[X])^2.$$

$$2.21 \quad \beta(\log(x + \beta) - \log \beta).$$

$$2.24 \quad (a) \quad \beta \log 2. \quad (b) \quad e^{\mu}. \quad (c) \quad \beta(2^{1/\alpha} - 1).$$

$$2.25 \quad (a) \quad 1,282. \quad (b) \quad 1,315. \quad (c) \quad 1,428.$$

$$2.26 \quad \text{Hint: } E[(L(X) - E[L(X)])^3] = a^3 E[(X - E[X])^3], \text{Var}[L(X)] = a^2 \text{Var}[X].$$

$$2.27 \quad L(X) = \beta(X/\gamma - 1).$$

$$2.28 \quad (a) \quad \text{exponential (2).} \quad (b) \quad \text{shifted Pareto } (\alpha, \beta). \quad (c) \quad \text{Burr } (\alpha, \beta, \delta). \\ (d) \quad \text{Weibull } (\beta, \delta). \quad (e) \quad \text{exponential } (1/\alpha).$$

$$2.29 \quad (a) \quad \beta^{m/\delta} \Gamma(\alpha - m/\delta) \Gamma(1 + m/\delta) / \Gamma(\alpha), \alpha\delta > m.$$

$$2.30 \quad (a) \quad F_Y(y) = \begin{cases} 0 & \text{if } -\infty < y \leq 1 \\ \frac{\Gamma((\log y)/\beta, \alpha)}{\Gamma(\alpha)} & \text{if } 1 < y < \infty. \end{cases} \quad (b) \quad E[Y^m] = (1 - m\beta)^{-\alpha}.$$

$$2.31 \quad CV[\tau X] = \sqrt{\text{Var}[\tau X]} / E[\tau X] = (|\tau|/\tau) CV[X] = CV[X].$$

<sup>59</sup> Results obtained by an iterative algorithm applied by the Excel Solver may vary slightly, depending on how the problem is set up in the worksheet and the process is initiated.

- 2.32  $\tilde{\tau} = \tau E[X; \tau//\tau]/E[X; l] = \tau$ .
- 2.33 (a) Weibull  $(a\beta^{b+1}, 1/(b+1))$ . (b) Burr  $(\alpha, \alpha\beta^{b+1}, 1/(b+1))$ .  
 (c) Weibull  $(a\beta^{b+1}, \delta/(b+1))$ . (d) Burr  $(\alpha, \alpha\beta^{b+1}, \delta/(b+1))$ .
- 2.34 (a) 0.6321. (b)  $\Gamma(\alpha, \alpha)/\Gamma(\alpha)$ . (c)  $\Phi(\sigma/2)$ . (d)  $1 - (1 - 1/\alpha)^\alpha$ .
- 2.37 (a) none. (b)  $\beta$ . (c) none. (d)  $\beta$ . (e)  $\beta$ . (f) none.
- 2.38  $f_{c\theta}(x) = (1/c) f_\theta(x/c) = (1/c\theta) f_1(x/c\theta)$ .
- 2.39 (a) Excel Solver yields  $(\hat{\mu}, \hat{\sigma}) = (9.778102, 1.444776)$ .  
 (c)  $\chi^2 = 5.89 < \chi_{0.95}^2(5) = 11.1$ .
- 2.40 Excel Solver yields  $(\hat{\mu}, \hat{\sigma}) = (9.701968, 1.535797)$ .
- 2.41 (a)  $F_Y(y) = \begin{cases} F_X(y)/F_X(l) & \text{if } -\infty < y < l \\ 1 & \text{if } l \leq y < \infty. \end{cases}$
- 2.42 (a)  $F_Y(y) = \begin{cases} 0 & \text{if } -\infty < y \leq a \\ \frac{F_X(y) - F_X(a)}{1 - F_X(a)} & \text{if } a \leq y < \infty. \end{cases}$
- 2.43 (a) Excel Solver yields  $(\hat{\mu}, \hat{\sigma}) = (9.495111, 1.084180)$ .  
 (b)  $M_1 = 14,840, E[Y] = 14,930$ .
- 3.1 (a)  $M'_N(0) = mp, M''_N(0) = mp + m(m-1)p^2$ .  
 (b)  $\lim_{\substack{m \rightarrow \infty \\ mp=\lambda}} M_N(t) = \lim_{m \rightarrow \infty} \left(1 + \frac{\lambda}{m}(e^t - 1)\right)^m = \exp(\lambda(e^t - 1))$ .
- 3.3 (b) 2.50, 0.7576. (c) 6.25, 0.1303. (d) 2.00, 0.8571.  
 (e) 4.00, 0.4335.
- 3.4 (a) 0.0012. (b) 0.0069. (c) 0.0164.
- 3.7  $\frac{d}{d\lambda} \log L(\lambda) = -m + \sum_{i=1}^m n_i/\lambda$ .
- 3.8 Integrate  $\int_{\lambda}^{\infty} t^n e^{-t} dt/n!$  by parts  $n$  times.
- 3.10 (a)  $E[N^2] = \sum_{n=0}^{\infty} n^2 \int_0^{\infty} \frac{u^n e^{-u}}{n!} f_{\lambda}(u) du = \int_0^{\infty} \left( \sum_{n=0}^{\infty} n^2 \frac{u^n e^{-u}}{n!} \right) f_{\lambda}(u) du$   
 $= \int_0^{\infty} (u + u^2) f_{\lambda}(u) du = E[\lambda] + E[\lambda^2]$ .
- 3.11 (a) 2. (b) 4. (c) 0.8125.
- 3.12 0.9070, 0.0864, 0.0062, 0.0004.

**3.13 (b)** 0.7500, 0.8175, 1.3125.

| (c) $n \backslash i$ | (1)    | (2)    | (3)    |
|----------------------|--------|--------|--------|
| 0                    | 0.4724 | 0.4869 | 0.5714 |
| 1                    | 0.3543 | 0.3373 | 0.2449 |
| 2                    | 0.1329 | 0.1283 | 0.1050 |
| 3                    | 0.0332 | 0.0365 | 0.0450 |
| 4                    | 0.0062 | 0.0087 | 0.0193 |
| 5                    | 0.0009 | 0.0018 | 0.0083 |

**3.14 (a)** Excel Solver yields  $\hat{\lambda}_1 = 0.114493$ ,  $\hat{\lambda}_2 = 0.797855$ ,  $\hat{p}_1 = 0.986380$ .

**3.15** Method-of-moments estimates are  $(\hat{\alpha}, \hat{v}) = (0.685714, 0.120000)$ . Using 4 cells  $\{0, 1, 2, \geq 3 \text{ claims}\}$ ,  $\chi^2 = 0.3288 < 3.8415 = \chi_{0.95}^2(1)$ .

$$\mathbf{3.16} \quad \binom{-r}{n} = \frac{-r(-r-1)(-r-2) \cdots (-r-n+1)}{n!} = (-1)^n \frac{(r+n-1) \cdots (r+2)(r+1)r}{n!}.$$

**3.19**  $a = 1 - q$ ,  $b = (r - 1)(1 - q)$ .

**3.21 (a)** Set  $r = 1$ ,  $q = p$  in (3.19).      **(b)**  $E[N] = (1 - p)/p$ ,  $Var[N] = (1 - p)/p^2$ .

**3.22 (a)**  $f_N(n) = 1/((n + 1)(n + 2))$ .      **(b)**  $f_N(n) = (0.9)^{n+1}/((n + 1)\log 10)$ .

**3.23 (a)** Substitute  $\beta = v/\alpha$  into (2.26).

**3.24**  $\hat{\alpha} = M_1^2/(M_2 - M_1^2 - M_1)$ ,  $\hat{v} = M_1$ .

**3.25 (a)** 0.6316.      **(b)** 0.6316.      **(c)** 0.6667.

**3.26 (a)**  $\gamma = 0.05$ .      **(b)** 0.8000, 0.8077, 0.7692, 0.8000.  
**(c)** 0.0034, 0.0342, 0.1538, 0.3761, 0.4325.

**3.27** *Hint:* Divide numerator and denominator of (3.26) by  $c^m$ . Observe that

$$(w + ic)/c = \frac{1}{\gamma} + i, (r + ic)/c = \frac{1 - p}{\gamma p} + i, (w + r + ic)/c = \frac{1}{\gamma p} + i.$$

**3.28** 0.4019, 0.3349, 0.1674, 0.0651, 0.0217, 0.0065.

**3.29 (a)**  $\gamma = 0.1000$ .

**3.30** 0.5543.

**3.31** 624.

**3.32**  $\lim_{m \rightarrow \infty} \gamma_m = 0$ .

$$\mathbf{3.33} \quad \text{(a)} \quad \frac{d}{dt} F_n(t) = \sum_{k=n}^{\infty} \left( \frac{\lambda(\lambda t)^{k-1} e^{-\lambda t}}{(k-1)!} - \frac{\lambda(\lambda t)^k e^{-\lambda t}}{k!} \right) = \frac{\lambda^n t^{n-1} e^{-\lambda t}}{(n-1)!}.$$

**(b)**  $E[T_n] = n/\lambda$ ,  $Var[T_n] = n/\lambda^2$ .

**3.34 (a)** 4.651 years.      **(b)** 0.1935, 0.1560.      **(c)** 0.0201, 0.0497.

**3.35**  $N^*$  is Poisson-distributed with parameter  $p\lambda$ .

| 4.1 | Amount $s$ | $F_S(s)$ | Amount $s$ | $F_S(s)$ |
|-----|------------|----------|------------|----------|
|     | 0          | 0.2000   |            |          |
|     | 500        | 0.2400   | 3,500      | 0.9047   |
|     | 1,000      | 0.4025   | 4,000      | 0.9507   |
|     | 1,500      | 0.5427   | 4,500      | 0.9781   |
|     | 2,000      | 0.6795   | 5,000      | 0.9934   |
|     | 2,500      | 0.7580   | 5,500      | 0.9988   |
|     | 3,000      | 0.8418   | 6,000      | 1.0000   |

4.4 (a)  $F_S(s) = f_N(0) + f_N(1)F_X(s)$ .

(b)  $F_S(s) = f_N(0) + f_N(1)F_X(s) + f_N(2)(F_X * F_X)(s)$ .

4.6  $f_S(s) = e^{-\lambda-s/\beta} \sum_{n=1}^{\infty} \frac{\lambda^n s^n}{\beta^n n!(n-1)!}$ ,  $F_S(s) = e^{-\lambda-s/\beta} \sum_{n=0}^{\infty} \frac{\lambda^n}{n!} \cdot \sum_{k=n}^{\infty} \frac{s^k}{\beta^k k!}$ ,  $s > 0$ .

4.7 See Problem 4.13 solution.

4.11  $\chi_{0.95}^2(m) \approx m \left( \sqrt{2/(9m)} \left( \Phi^{-1}(0.95) - \sqrt{2/(9m)} \right) + 1 \right)^3$ .

| 4.12 | d.f. $m$ | $\chi_{0.95}^2(m)$ | W-H    | Rel Error |
|------|----------|--------------------|--------|-----------|
|      | 5        | 11.070             | 11.044 | -0.24%    |
|      | 10       | 18.307             | 18.292 | -0.08%    |
|      | 15       | 24.996             | 24.985 | -0.04%    |
|      | 20       | 31.410             | 31.402 | -0.03%    |
|      | 25       | 37.652             | 37.645 | -0.02%    |
|      | 30       | 43.773             | 43.767 | -0.01%    |

### 4.13

| Amount $s$ | $F_S(s)$ | Normal | Relative Error | Normal Power | Relative Error | Shifted Gamma | Relative Error | Wilson-Hilferty | Relative Error |
|------------|----------|--------|----------------|--------------|----------------|---------------|----------------|-----------------|----------------|
| 0          | 0.0003   | 0.1241 | —              | 0.0756       | —              | 0.0263        | —              | 0.0312          | —              |
| 3,000      | 0.3420   | 0.2819 | -17.57%        | 0.3654       | +6.84%         | 0.3362        | -1.70%         | 0.3322          | -2.87%         |
| 6,000      | 0.6070   | 0.5000 | -17.63%        | 0.5981       | -1.47%         | 0.6054        | -0.26%         | 0.6043          | -0.44%         |
| 9,000      | 0.7774   | 0.7181 | -7.63%         | 0.7608       | -2.14%         | 0.7782        | +0.10%         | 0.7797          | +0.30%         |
| 12,000     | 0.8782   | 0.8759 | -0.26%         | 0.8642       | -1.59%         | 0.8793        | +0.13%         | 0.8810          | +0.32%         |
| 15,000     | 0.9349   | 0.9584 | +2.51%         | 0.9257       | -0.98%         | 0.9356        | +0.07%         | 0.9367          | +0.19%         |
| 18,000     | 0.9658   | 0.9895 | +2.45%         | 0.9605       | -0.55%         | 0.9661        | +0.03%         | 0.9666          | +0.08%         |
| 21,000     | 0.9823   | 0.9981 | +1.61%         | 0.9796       | -0.27%         | 0.9824        | +0.01%         | 0.9824          | +0.01%         |
| 24,000     | 0.9910   | 0.9997 | +0.88%         | 0.9896       | -0.14%         | 0.9909        | -0.01%         | 0.9908          | -0.02%         |
| 27,000     | 0.9954   | 1.0000 | +0.46%         | 0.9948       | -0.06%         | 0.9953        | -0.01%         | 0.9952          | -0.02%         |

**4.15** All terms in the sum (4.33) for which  $k > \hat{m}$  are zero.

**4.16**

| Amount $s$ | $F_s(s)$ |
|------------|----------|
| 0          | 0.2592   |
| 500        | 0.2942   |
| 1,000      | 0.4366   |
| 1,500      | 0.5606   |
| 2,000      | 0.6838   |
| 3,000      | 0.8306   |
| 4,000      | 0.9223   |
| 5,000      | 0.9670   |
| 6,000      | 0.9872   |

**4.17**  $g(0) + \sum_{k=1}^{\hat{m}-1} g(k) + g(\hat{m}) =$   
 $F_X(\frac{1}{2}h) - [F_X(\frac{1}{2}h) + F_X((\hat{m} - \frac{1}{2})h)] + 1 - F_X((\hat{m} - \frac{1}{2})h) = 1.$

**4.20** If  $Y = F_X(X)$ , then  $F_Y(y) = \Pr\{F_X(X) \leq y\} = \Pr\{X \leq F_X^{-1}(y)\} = y$  for  $0 < y < 1$ .

**4.21**  $\tilde{F}^{-1}(u) = \beta(-\log(1 - u))^{1/\delta}, 0 < u < 1.$

**4.22**  $n = 5.$

**4.23**

| Trial | Uniform<br>$u$ | Exponential<br>$x_1$ | Pareto<br>$x_2$ | Lognormal<br>$x_3$ | Weibull<br>$x_4$ |
|-------|----------------|----------------------|-----------------|--------------------|------------------|
| (1)   | 0.2097         | 471                  | 296             | 30                 | 55               |
| (2)   | 0.3562         | 881                  | 578             | 79                 | 194              |
| (3)   | 0.6970         | 2,388                | 1,837           | 553                | 1,426            |
| (4)   | 0.8245         | 3,480                | 3,017           | 1,384              | 3,028            |
| (5)   | 0.9882         | 8,879                | 14,716          | 25,871             | 19,711           |

**4.25** (a) Because  $E\{U_n\} = \frac{1}{2}$  and  $Var[U_n] = \frac{1}{12}$ ,  $E[X] = 0$  and  $Var[X] = 1$ . The Central Limit Theorem implies that  $X$  is approximately normal.

**5.1** (a) 865; 440,343. (b) 7.4. (d) 6.6%, 9.5%, 16.7%.

**5.2** (a) 500. (b) 1,250. (c) 2,000. (d) 3,500. (e) 8,518.

**5.7** (a)  $e^{-x/\beta}$ . (b)  $((d + \beta)/(x + d + \beta))^\alpha$ .

**5.9** (a)  $e_X(x) = \frac{\int_0^\infty u dF(u) - \left(\int_0^x u dF(u) + x \int_x^\infty dF(u)\right)}{1 - \int_0^x dF(u)} = \frac{\int_x^\infty (u - x) dF(u)}{\int_x^\infty dF(u)}.$

**5.10** (a) 1.1551, 1.5959. (b) 136.38, 1.1487, 2.2616.

5.11 (a) 1. (b)  $\frac{1}{\alpha}\sqrt{\alpha}$ . (c)  $\sqrt{\exp(\sigma^2) - 1}$ .  
 (d)  $\sqrt{\alpha/(\alpha - 2)}$ . (e)  $\frac{1}{3}\sqrt{3}$ .

5.12

| Layer $L$         | $P_L$  | $E[N_L]$ | $E[X_L]$ | $E[S_L]$ |
|-------------------|--------|----------|----------|----------|
| [0, 100]          | 1.0000 | 5.0000   | 97.08    | 485      |
| (100, 3000]       | 0.9423 | 4.7116   | 1,513.66 | 7,132    |
| (3000, $\infty$ ) | 0.2441 | 1.2207   | 4,000.00 | 4,883    |

5.13 *Hint:*  $\mu_1 = E[X; b_1]$ ,  $\mu_k = (E[X; b_k] - E[X; b_{k-1}])/p_k$ ,  $1 < k < m$ .

5.14 (b)  $\lambda(F(b) - F(a))$ . (c)  $E[X | a < X \leq b] = \int_a^b x dF(x) / \int_a^b dF(x)$ .

5.15 Interval means: 60; 317; 604; 1,405; 3,214; 4,400; 7,500.  
 Layer means: 96; 339; 342; 694; 1,371; 743; 2,500.

5.16 
$$E[N_a^2] = \sum_{n=0}^{\infty} n^2 \sum_{k=n}^{\infty} \binom{k}{n} p^n (1-p)^{k-n} \Pr\{N=k\}$$

$$= \sum_{k=0}^{\infty} \Pr\{N=k\} \sum_{n=0}^k n^2 \binom{k}{n} p^n (1-p)^{k-n}$$

$$= \sum_{k=0}^{\infty} \Pr\{N=k\} (k^2 p^2 + kp - kp^2) = E[N^2] p^2 + E[N] p - E[N] p^2.$$

5.18 
$$\gamma_a = \frac{\text{Var}[N_a] - E[N_a]}{(E[N_a])^2} = \frac{p^2 \text{Var}[N] + p(1-p)\lambda - p\lambda}{p^2 \lambda^2} = \frac{\text{Var}[N] - \lambda}{\lambda^2} = \gamma.$$

5.20 
$$\tilde{\tau}_s = \tau_x \frac{E[X] - E[X; (\tau_x a)/\tau_x]}{E[X] - E[X; a]} = \tau_x.$$

5.21 (a) 8.9%. (b) 11.5%.

5.22 (a) 9.5%. (b) 10.2%.

5.23 (a)  $(\hat{\mu}, \hat{\sigma}) = (7.960294, 1.428801)$ . (b) 125.

5.24  $E[X] - E[X; x] = \int_0^{\infty} (1 - F(u)) du - \int_0^x (1 - F(u)) du.$

6.1 (a) 4.50. (b) 1.875. (c) 11,250. (d) 1.3333. (e) 6.00.  
 (f) 15,000.

6.2 (a) 6.1905. (b) 3.8690. (c) 0.0003888. (d) 0.8166.  
 (e) 8,125. (f) 0.3750.

6.3 (a) 6.1905. (b) 3.8333. (c) 0.0003853. (d) 0.8090.  
 (e) 8,050.

**6.4** (a) 0.1912. (b) 0.4751.

**6.5**

| Limit $l$ | $E[X; l]$ | ALAE [a] | $l(l)$ [a] | ALAE [b] | $l(l)$ [b] |
|-----------|-----------|----------|------------|----------|------------|
| 100,000   | 9,178     | 2,500    | 1.0000     | 2,295    | 1.0000     |
| 250,000   | 12,548    | 2,500    | 1.2885     | 3,137    | 1.3671     |
| 500,000   | 15,180    | 2,500    | 1.5139     | 3,795    | 1.6539     |
| 1,000,000 | 17,702    | 2,500    | 1.7299     | 4,426    | 1.9288     |
| 2,000,000 | 19,968    | 2,500    | 1.9240     | 4,992    | 2.1756     |
| 5,000,000 | 22,404    | 2,500    | 2.1325     | 5,601    | 2.4410     |

**6.7** ILFs: 1.0000, 1.5317, 1.6488, 1.7122, 1.8427, 1.9038, 1.9405, 1.9655.

**6.8** (a)

| Limit $l$ | $E[X; l]$ | ALAE | $\rho(l)$ | $l(l)$ w/o RL | $l(l)$ w/ RL |
|-----------|-----------|------|-----------|---------------|--------------|
| 1,000     | 796       | 159  | 447       | 1.0000        | 1.0000       |
| 2,000     | 1,313     | 263  | 778       | 1.6490        | 1.6787       |
| 3,000     | 1,667     | 333  | 1,034     | 2.0940        | 2.1645       |
| 4,000     | 1,920     | 384  | 1,238     | 2.4123        | 2.5267       |
| 5,000     | 2,107     | 421  | 1,404     | 2.6478        | 2.8055       |
| 7,500     | 2,407     | 481  | 1,710     | 3.0247        | 3.2805       |
| 10,000    | 2,578     | 516  | 1,919     | 3.2392        | 3.5759       |

**6.9**  $1 + \delta = \text{Var}[N]/E[N] = (E[N] + \gamma(E[N])^2)/E[N] = 1 + \gamma E[N]$ .

**6.10**

| Limit $l$ | $E[X; l]$ | $\rho(l)$ | $l(l)$ | Layer Factor |
|-----------|-----------|-----------|--------|--------------|
| 4,000K    | 4,223     | 3,374     | 2.1014 | 0.3556       |
| 5,000K    | 4,459     | 4,429     | 2.4585 | 0.3571       |
| 6,000K    | 4,660     | 5,533     | 2.8194 | 0.3609       |
| 7,000K    | 4,836     | 6,678     | 3.1849 | 0.3655       |
| 8,000K    | 4,994     | 7,859     | 3.5553 | 0.3705       |
| 9,000K    | 5,137     | 9,074     | 3.9309 | 0.3755       |
| 10,000K   | 5,268     | 10,319    | 4.3114 | 0.3806       |

**6.11** (a) 0.0209. (b) 0.0142. (c) 0.0112. (d) 0.0093. (e) 0.0081.

**6.12** (a) \$40,447. (b) \$844.

**6.13** (a) 62,200; 0.2635. (b) 80,200; 0.0503.

**6.14** (a) 50,900; 0.3973. (b) 68,900; 0.1841.

| 6.16 | (a) |         |        |           | (b) |         |        |           |
|------|-----|---------|--------|-----------|-----|---------|--------|-----------|
|      |     | Ded $d$ | $C(d)$ | Pure Prem |     | Ded $d$ | $C(d)$ | Pure Prem |
|      |     | 1,000   | 0.0959 | 4.247     |     | 1,000   | 0.0411 | 4.505     |
|      |     | 2,000   | 0.1501 | 3.993     |     | 2,000   | 0.0647 | 4.394     |
|      |     | 3,000   | 0.1926 | 3.973     |     | 3,000   | 0.0848 | 4.300     |
|      |     | 4,000   | 0.2283 | 3.625     |     | 4,000   | 0.1028 | 4.215     |
|      |     | 5,000   | 0.2596 | 3.478     |     | 5,000   | 0.1193 | 4.137     |
|      |     | 10,000  | 0.3783 | 2.921     |     | 10,000  | 0.1884 | 3.813     |

| 6.17 | (a) |         |        |           |          |
|------|-----|---------|--------|-----------|----------|
|      |     | Ded $d$ | $C(d)$ | Frequency | Severity |
|      |     | 0       | 0.0000 | 0.005000  | 3,028    |
|      |     | 250     | 0.0855 | 0.004643  | 2,982    |
|      |     | 500     | 0.1648 | 0.004319  | 2,928    |
|      |     | 750     | 0.2385 | 0.004025  | 2,864    |
|      |     | 1,000   | 0.3071 | 0.003757  | 2,792    |

  

| (b) |         |        |           |          |
|-----|---------|--------|-----------|----------|
|     | Ded $d$ | $C(d)$ | Frequency | Severity |
|     | 250     | 0.0088 | 0.004643  | 3,232    |
|     | 500     | 0.0221 | 0.004319  | 3,428    |
|     | 750     | 0.0391 | 0.004025  | 3,614    |
|     | 1,000   | 0.0590 | 0.003757  | 3,792    |

| 6.21 | (a) |       |          |           | (b) |       |          |           |
|------|-----|-------|----------|-----------|-----|-------|----------|-----------|
|      |     | Ded   | # Claims | % BL Prem |     | Ded   | # Claims | % BL Prem |
|      |     | 1,000 | 242      | 7.4%      |     | 1,000 | 234      | 7.1%      |
|      |     | 2,000 | 299      | 12.5%     |     | 2,000 | 292      | 12.0%     |
|      |     | 3,000 | 331      | 16.6%     |     | 3,000 | 324      | 16.1%     |
|      |     | 4,000 | 353      | 20.2%     |     | 4,000 | 346      | 19.5%     |
|      |     | 5,000 | 368      | 23.3%     |     | 5,000 | 362      | 22.6%     |

## A.3. References

- [1] Abramowitz, Milton, and Irene Stegun, eds. *Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables*. New York: Dover Publications, 1972 (reprint of a work originally published by the National Bureau of Standards, United States Department of Commerce, 1964).
- [2] Apostol, Tom M. *Mathematical Analysis*, 2nd ed. Reading MA: Addison-Wesley, 1974.
- [3] Beard, R. E., T. Pentikäinen, and E. Pesonen. *Risk Theory: The Stochastic Basis of Insurance*, 3rd ed. London: Chapman and Hall, 1984.

- [4] Feller, William. *An Introduction to Probability Theory and Its Applications*, Vol. I, 3rd ed. New York: John Wiley & Sons, Inc., 1968.
- [5] Heckman, Philip E., and Glenn G. Meyers. "The calculation of aggregate loss distributions from claim severity and claim count distributions," *Proceedings of the Casualty Actuarial Society*, LXX (1983), 22–61. Additional exhibits and FORTRAN code are in *PCAS*, LXXI (1984), 49–66.
- [6] Hewitt, Charles C., Jr. "The negative binomial applied to the Canadian merit rating plan for individual automobile risks," *Proceedings of the Casualty Actuarial Society*, XLVII (1960), 55–65.
- [7] Hogg, Robert V., and Allen T. Craig. *Introduction to Mathematical Statistics*, 4th ed. New York: Macmillan Publishing Co., Inc., 1978.
- [8] Hogg, Robert V., and Stuart A. Klugman. *Loss Distributions*. New York: John Wiley & Sons, Inc., 1984.
- [9] Insurance Services Office. *Report of the Increased Limits Subcommittee: A Review of Increased Limits Ratemaking*. New York: Insurance Services Office, Inc., 1980.
- [10] Kauppi, Laurie, and Pertti Ojantakanen. "Approximations of the generalized Poisson function," *ASTIN Bulletin*, V (1969), 213–226.
- [11] Keatinge, Clive. "Modeling losses with the mixed exponential distribution," *Proceedings of the Casualty Actuarial Society*, LXXXVI (1999), 654–698.
- [12] Klugman, Stuart A., and A. Rahulji Parsa. "Minimum distance estimation of loss distributions," *Proceedings of the Casualty Actuarial Society*, LXXX (1993), 250–270.
- [13] Lindgren, B.W. *Statistical Theory*, 2nd ed. New York: The Macmillan Company, 1968.
- [14] McCord, James R., III, and Richard M. Moroney, Jr. *Introduction to Probability Theory*. New York: The Macmillan Company, 1964.
- [15] Meyers, Glenn. *The competitive market equilibrium risk load formula for increased limits ratemaking*. New York: Insurance Services Office, Inc., 1991.
- [16] Miccolis, Robert S. "On the theory of increased limits and excess of loss pricing," *Proceedings of the Casualty Actuarial Society*, LXIV (1977), 27–59.
- [17] Panjer, H.H. "Recursive evaluation of a family of compound distributions," *ASTIN Bulletin*, XII (1981), 21–26.
- [18] Parzen, Emanuel. *Modern Probability Theory and Its Applications*. New York: John Wiley & Sons, Inc., 1960.
- [19] Pentikäinen, T. "Approximative evaluation of the distribution function of aggregate claims," *ASTIN Bulletin*, XVII (1987), 15–39.
- [20] Rosenberg, Sheldon, and Aaron Halpert. "Adjusting size of loss distributions for trend," *Inflation Implications for Property-Casualty Insurance: Casualty Actuarial Society 1981 Discussion Paper Program*, 458–494.
- [21] Simon, Leroy J. "Fitting negative binomial distributions by the method of maximum likelihood," *Proceedings of the Casualty Actuarial Society*, XLVIII (1961), 45–53.
- [22] Weibull, E.H.W. "A statistical distribution function of wide applicability," *Journal of Applied Mechanics*, XVIII (1951), 293–297.

