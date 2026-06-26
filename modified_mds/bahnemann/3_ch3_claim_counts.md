---
paper: bahnemann
chapter: 3
title: 3. Claim Counts
topics: [poisson_distribution, negative_binomial_distribution, parameter_uncertainty, claim_contagion, mixed_poisson_distribution, polya_model, portfolio_claims]
key_formulas: [poisson_probability_function, negative_binomial_probability_function, mixed_poisson_variance, polya_distribution, contagion_parameter_formula]
---

> **TL;DR**
> - **Poisson**: f(n)=λⁿe^{−λ}/n!; mean=var=λ; derived as binomial limit (mp=λ, m→∞); if sample mean≠sample variance, Poisson is inadequate — use NB
> - **Mixed Poisson (parameter uncertainty)**: E[N]=E[λ], Var[N]=E[λ]+Var[λ]; mixing Poisson with gamma(α, ν/α) for λ yields the **Negative Binomial** with mean ν and Var[N]=ν+ν²/α
> - **Negative Binomial** also arises from the **Pólya contagion model** as m→∞; contagion parameter γ=1/α; Var[N]=E[N]+γ(E[N])²; both interpretations yield the same distribution
> - Method-of-moments for NB: v̂=sample mean; α̂=(v̂²)/(sample var − v̂); NB reduces to Poisson as α→∞
> - **Portfolio**: sum of independent Poisson(λᵢ) is Poisson(Σλᵢ); sum of i.i.d. NB(α,ν) is NB(mα, mν)

# 3. Claim Counts

This chapter is devoted to probability models associated with the number of claims generated either by a single policy or by a portfolio of policies in property/casualty insurance. We study first some aspects of the basic claim process by means of a simplified example and then turn to the standard claim-count models. Our main emphasis is on the two most important parametric families, the Poisson and negative binomial distributions, with special attention paid to the modeling of both parameter uncertainty and claim contagion.

## 3.1. An Elementary Claim Process

The incidence of insurance claims is most usefully modeled as a random process, continuous throughout a fixed time interval. For a single policy this period is the length of time the policy remains in force—the policy term, typically one year. The basic random process must be endowed with a probability structure rich enough to support the essential random variables. The most important such time-dependent random variable—the claim count—is the principal focus of this chapter. Values of the claim-count variable, which we denote by  $N$ , are just the numbers of insured events occurring during the policy term that give rise to claims against the policy.

Begin by considering a simple discrete model of a claim process, based on the following pair of assumptions about claims arising from a single policy:

- B<sub>1</sub>** During a short time interval the probability of a single claim occurring is a fixed number  $p$  ( $0 \leq p \leq 1$ ) and the probability of two or more claims occurring is zero.
- B<sub>2</sub>** The numbers of claims occurring in disjoint short time intervals, each with the probability structure described in **B<sub>1</sub>**, are independent random variables.

In other words, the number of claims occurring during a single short interval is a Bernoulli random variable—it takes on the value 1 with probability  $p$  and the value 0 with probability  $1 - p$ .

Now let  $N_m$  denote the total number of claims occurring in  $m$  adjacent, but non-overlapping intervals for each of which assumptions **B<sub>1</sub>** and **B<sub>2</sub>** both hold. It is evident that  $N_m$  is the sum of  $m$  independent Bernoulli random variables, and so it has a binomial distribution with parameters  $(m, p)$  and probability function

$$\Pr\{N_m = n\} = {}_m C_n p^n (1 - p)^{m-n}, \quad n = 0, 1, 2, \dots, m. \quad (3.1)$$

The mean and variance of  $N_m$  are  $mp$  and  $mp(1 - p)$ , respectively.

**Example 3.1.** The probability that an individual policyholder makes a claim in any single day is 0.003. Assuming that at most one claim per day is possible and that claims on successive days are independent, the binomial distribution (3.1) with  $p = 0.003$  applies to any time period comprised of  $m$  successive days.

For example, during a 30-day period the respective probabilities of no claims and a single claim are

$$\Pr\{N_{30} = 0\} = {}_{30}C_0(0.003)^0(0.997)^{30} = 0.9138,$$

$$\Pr\{N_{30} = 1\} = {}_{30}C_1(0.003)^1(0.997)^{29} = 0.0825.$$

As a result, the probability of two or more claims is  $1 - 0.9138 - 0.0825 = 0.0037$ . The expected number of claims for the 30-day period is  $mp = (30)(0.003) = 0.0900$ .

Probabilities of claims occurring during a full year can be computed in a similar way. For example, the probability of two claims in a 365-day year is

$$\Pr\{N_{365} = 2\} = {}_{365}C_2(0.003)^2(0.997)^{363} = 0.2009,$$

and the expected number of claims for the year is  $(365)(0.003) = 1.0950$ . ■

Example 3.1 indicates how to apply the binomial model to a policy term of reasonable length—one year, for example. In that example, this was accomplished by partitioning the policy term into disjoint short time intervals, during each of which at most one claim is possible, thereby dividing the period into discrete units with separate but identical probability structures. However, such a discrete-time approach is conceptually at variance with the intuitive view that a claim process should be a *continuous* one. It seems desirable, therefore, to find a continuous-time model for the process.

Passage from a discrete model to a continuous one always requires some type of limit procedure. To accomplish this in the case of the binomial model, first partition the policy period into  $m$  short subintervals of equal length, each with a Bernoulli probability structure specified by  $\mathbf{B}_1$ , for which  $p$  is the probability of a single claim. The total number of claims in all these subintervals then has the binomial probability function (3.1) with parameters  $(m, p)$ .

Next, we allow the number of subintervals to become infinite in such a way that *the expected number of claims for the total policy period remains unchanged*. That is, as  $m \rightarrow \infty$  parameters  $m$  and  $p$  must always satisfy  $mp = \lambda$  for some positive constant  $\lambda$ . This implies that the probability  $p$  of a claim in each subinterval approaches zero as the number of subintervals becomes arbitrarily large—or equivalently, as the subinterval length becomes arbitrarily small. Then, for each nonnegative integer  $n$ , the probability of obtaining  $n$  claims is

$$\begin{aligned}\Pr\{n \text{ claims}\} &= \lim_{\substack{m \rightarrow \infty \\ mp = \lambda}} {}_mC_n p^n (1-p)^{m-n} \\ &= \lim_{m \rightarrow \infty} \frac{m(m-1) \dots (m-n+1)}{n!} \left(\frac{\lambda}{m}\right)^n \left(1 - \frac{\lambda}{m}\right)^{m-n}\end{aligned}$$

$$\begin{aligned}
&= \lim_{m \rightarrow \infty} \frac{m}{m} \cdot \frac{m-1}{m} \cdots \frac{m-n+1}{m} \cdot \frac{\lambda^n}{n!} \cdot \left(1 - \frac{\lambda}{m}\right)^{-n} \left(1 - \frac{\lambda}{m}\right)^m \\
&= \frac{\lambda^n e^{-\lambda}}{n!}.
\end{aligned} \tag{3.2}$$

The final step is a consequence of a familiar limit theorem from elementary calculus:  $\lim_{m \rightarrow \infty} (1 + x/m)^m = e^x$ .

Formula (3.2) expressing  $\lambda^n e^{-\lambda}/n!$  as the limit of binomial probabilities was first derived by Siméon-Denis Poisson (1781–1840), French mathematician and mathematical physicist extraordinaire.<sup>28</sup> The resulting probability distribution with probabilities given by (3.2) subsequently came to be known as a **Poisson distribution**.

Poisson distributions have been applied to a diverse range of random events occurring throughout some time interval (or, alternatively, some type of spatial configuration). The number of alpha particles emitted from a radioactive source during a fixed time period, the number of defective products in a lot of manufactured items, the number of calls arriving at a telephone switchboard during an hour, the number of cells visible under a microscope in a certain region, the number of hurricanes striking the North American Atlantic coast in a single year—all have been successfully modeled as Poisson processes.

Because of results like (3.2) the Poisson distribution has also come to play a prominent role in modeling claim processes in property/casualty insurance. In the next section, we derive this probability distribution directly from a set of general assumptions.

## 3.2. Poisson Claim Processes

Experience has shown that the claim process in property/casualty insurance is often a **Poisson process**. This means that claims occur over time in accordance with the following set of assumptions, sometimes referred to as the **Poisson postulates**. In statements  $\{\mathbf{A}_1, \mathbf{A}_2, \mathbf{A}_3, \mathbf{A}_4, \mathbf{A}_5\}$ ,  $P_n(t)$  is the probability that  $n$  claims occur during a time interval of length  $t$ ,  $0 \leq t < \infty$ .

- $\mathbf{A}_1$  The numbers of claims<sup>29</sup> occurring in disjoint time intervals are independent random variables.
- $\mathbf{A}_2$  The probability structure is time-invariant—that is, for all  $a \geq 0$  the probability of  $n$  claims occurring in the interval between  $a$  and  $a + t$  equals  $P_n(t)$ . Thus, the distribution of the number of claims occurring during an interval depends on the length of the interval but not on the endpoints.

<sup>28</sup> Poisson's derivation appeared in his 1837 treatise on probability, *Recherchés sur la probabilité des jugements en matière criminelle et en matière civile* [Research on the probability of criminal and civil verdicts]. Poisson published more than 300 papers on mathematics, including the fields of analysis and probability, and on a wide range of topics in physics. His memorable adage, "Life is good for only two things, discovering mathematics and teaching mathematics," is undoubtedly best appreciated by other mathematicians.

<sup>29</sup> In this special formulation of the Poisson postulates the underlying random event is the occurrence of an insurance claim during a specified time interval. However, as indicated above, the general Poisson process can be applied to a variety of random events occurring in time or space.

- A<sub>3</sub>** The probability of a single claim occurring in a short interval of length  $h$ ,  $h > 0$ , is approximately proportional to  $h$ :

$$P_1(h) = \lambda h + o(h) \text{ for some positive constant } \lambda.^{30}$$

Parameter  $\lambda$  is the **time density** of the incidence of claims—the average number of claims per unit of time.

- A<sub>4</sub>** The probability of more than one claim occurring in a short interval of length  $h$  is approximately zero:  $\sum_{n=2}^{\infty} P_n(h) = o(h)$ .
- A<sub>5</sub>** In an interval of length  $t = 0$ ,  $P_0(0) = 1$  and  $P_n(0) = 0$  for  $n > 0$ .

Although these assumptions are often satisfied in practice, there are situations involving the incidence of insurance claims in which one or more of them fails to hold in a significant way. For example, **A<sub>2</sub>** and **A<sub>3</sub>** imply that the density  $\lambda$  of claims per unit time remains constant over time, an assumption usually valid in the short run but which might fail in the long run. The assumption of independence in **A<sub>1</sub>** fails whenever the occurrence of a claim alters the probability of later claims. This phenomenon of claim contagion will be explored later, in Section 3.4. Finally, **A<sub>4</sub>** is incompatible with the occurrence of multiple simultaneous claims, as is the case when two or more individuals are injured in the same accident. Such a violation of postulate **A<sub>4</sub>** can be avoided by always defining “claim” to refer to a single insured event, without regard to the number of claimants involved.

A general formula for the Poisson probability function  $P_n(t)$  can be derived directly from postulates **{A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>, A<sub>4</sub>, A<sub>5</sub>}**. First, observe that **A<sub>3</sub>** and **A<sub>4</sub>** together imply that the probability  $P_0(h)$  of zero claims in a short interval of positive length  $h$  is given by

$$P_0(h) = 1 - \sum_{n=1}^{\infty} P_n(h) = 1 - \lambda h + o(h).$$

Moreover, the independence and time-invariance properties **A<sub>1</sub>** and **A<sub>2</sub>** imply that the probability of zero claims in the interval  $(0, t + h)$  can be expressed as

$$P_0(t + h) = P_0(t)P_0(h).$$

Extending this last equation to the case of  $n$  claims, where  $n \geq 1$ , we obtain

$$P_n(t + h) = P_n(t)P_0(h) + P_{n-1}(t)P_1(h) + \cdots + P_0(t)P_n(h), \quad (3.3)$$

verification of which is requested in Problem 3.5. Finally, combining the last three equations with postulate **A<sub>4</sub>** produces

$$P_0(t + h) = P_0(t)(1 - \lambda h + o(h)),$$

$$P_n(t + h) = P_n(t)(1 - \lambda h + o(h)) + P_{n-1}(t)(\lambda h + o(h)) + \sum_{i=2}^n P_{n-i}(t)o(h), \quad n \geq 1.$$

<sup>30</sup> The expression  $o(h)$ , pronounced “little *oh* of  $h$ ,” denotes a function of  $h$  that approaches 0 faster than  $h$ , so that  $A = o(h)$  means  $\lim_{h \rightarrow 0} A/h = 0$ . If  $A = o(h)$  and  $B = o(h)$ , then  $A + B = o(h)$  also.

These equations can now be used to obtain appropriate expressions for the derivative, with respect to  $t$ , of probability function  $P_n(t)$ .

The case  $n = 0$  yields the differential equation

$$\frac{d}{dt}P_0(t) = \lim_{h \rightarrow 0} \frac{P_0(t+h) - P_0(t)}{h} = \lim_{h \rightarrow 0} \frac{P_0(t)(-\lambda h + o(h))}{h} = -\lambda P_0(t).$$

The initial condition  $P_0(0) = 1$  supplied by **A<sub>5</sub>** gives rise to the unique solution  $P_0(t) = e^{-\lambda t}$ . Similarly, the derivative in the case  $n \geq 1$  is

$$\begin{aligned} \frac{d}{dt}P_n(t) &= \lim_{h \rightarrow 0} \frac{P_n(t+h) - P_n(t)}{h} \\ &= \lim_{h \rightarrow 0} \frac{P_n(t)(-\lambda h + o(h)) + P_{n-1}(t)(\lambda h + o(h)) + o(h)}{h} \\ &= -\lambda P_n(t) + \lambda P_{n-1}(t). \end{aligned}$$

When  $n = 1$  the solution of this differential equation is  $P_1(t) = \lambda t e^{-\lambda t}$ . Continuing inductively for  $n = 2, 3, 4, \dots$  yields the general Poisson probability function

$$P_n(t) = \frac{(\lambda t)^n e^{-\lambda t}}{n!}, \quad n = 0, 1, 2, \dots \quad (3.4)$$

**Example 3.2.** The claim process for a certain liability policy is Poisson, and claims occur at a constant rate of 0.04 per year. If the policy term is one year, then formula (3.4) with  $t = 1$  and  $\lambda = 0.04$  applies. The probabilities for zero, one, and two claims against the policy are, respectively,

$$P_0(1) = e^{-0.04} = 0.9608,$$

$$P_1(1) = (0.04)e^{-0.04} = 0.0384,$$

$$P_2(1) = \frac{(0.04)^2 e^{-0.04}}{2!} = 0.0008.$$

On the other hand, to obtain probabilities for claims arising during an 18-month period put  $t = 1.5$  and  $\lambda = 0.04$  into the same formula. Thus

$$P_0(1.5) = e^{-0.06} = 0.9418,$$

$$P_1(1.5) = (0.06)e^{-0.06} = 0.0565,$$

$$P_2(1.5) = \frac{(0.06)^2 e^{-0.06}}{2!} = 0.0017. \blacksquare$$

In property/casualty insurance applications the claim-count random variable of greatest interest is the number of claims occurring during a fixed time period, usually

a single policy term. It is appropriate then to take the basic time unit in the Poisson process to be the length of this fixed period and adjust the parameter  $\lambda$  to represent the claim density during the selected period. We denote the resulting random variable by  $N$  and use the customary  $f(n)$  to denote the associated probability mass function, which has the simplified form

$$f(n) = \frac{\lambda^n e^{-\lambda}}{n!}, \quad n = 0, 1, 2, \dots \quad (3.5)$$

The moment-generating function  $M(t)$  for claim-count  $N$  with distribution (3.5) exists for all real  $t$ :

$$M(t) = E[e^{tN}] = \sum_{n=0}^{\infty} e^{tn} \frac{\lambda^n e^{-\lambda}}{n!} = e^{-\lambda} \sum_{n=0}^{\infty} \frac{(\lambda e^t)^n}{n!} = \exp(\lambda e^t - \lambda). \quad (3.6)$$

This function has derivatives of all orders, and so all moments of  $N$  can be obtained from the successive derivatives of  $M(t)$  evaluated at  $t = 0$ :

$$E[N] = M'(0) = \lambda e^t M(t) \Big|_{t=0} = \lambda,$$

$$E[N^2] = M''(0) = (\lambda e^t + \lambda^2 e^{2t}) M(t) \Big|_{t=0} = \lambda + \lambda^2,$$

$$E[N^3] = M'''(0) = (\lambda e^t + 3\lambda^2 e^{2t} + \lambda^3 e^{3t}) M(t) \Big|_{t=0} = \lambda + 3\lambda^2 + \lambda^3.$$

It is not surprising, given the role that  $\lambda$  plays in the Poisson postulates, that  $E[N] = \lambda$ . In addition, the variance and skewness are

$$\text{Var}[N] = E[N^2] - (E[N])^2 = \lambda + \lambda^2 - \lambda^2 = \lambda, \quad (3.7)$$

$$\text{Sk}[N] = \frac{E[(N - E[N])^3]}{(\text{Var}[N])^{3/2}} = \frac{\lambda}{\lambda^{3/2}} = \frac{1}{\sqrt{\lambda}}. \quad (3.8)$$

Poisson random variables have a distinctive property that serves to characterize this distributional family—the mean and variance are equal, each identical to the distribution parameter  $\lambda$ .

The next example illustrates one way to fit a Poisson distribution to a set of claim data.

**Example 3.3.** During a single policy period of one year a certain portfolio of 1,000 identical insurance policies generated 150 claims. These data have been summarized in the table by the number of claims per policy per year. We wish to find a Poisson distribution for the claim-count variable  $N$  for an individual policy selected from the portfolio.

| # Claims | # Policies |
|----------|------------|
| 0        | 868        |
| 1        | 118        |
| 2        | 11         |
| 3        | 2          |
| 4        | 1          |
| ≥5       | 0          |
| Total    | 1,000      |

**Table 3.1. Claim-Count Distributions [Example 3.3]**

| # Claims $n$ | $\Pr\{N = n\}$ |                              |
|--------------|----------------|------------------------------|
|              | Sample         | Poisson ( $\lambda = 0.15$ ) |
| 0            | 0.8680         | 0.8607                       |
| 1            | 0.1180         | 0.1291                       |
| 2            | 0.0110         | 0.0097                       |
| 3            | 0.0020         | 0.0005                       |
| 4            | 0.0010         | 0.0000                       |
| $\geq 5$     | 0.0000         | 0.0000                       |
| Mean         | 0.1500         | 0.1500                       |
| Variance     | 0.1735         | 0.1500                       |

To do so, one can interpret these data as observations for a sample of size 1,000 drawn from a population of policies with identical Poisson claim-count distributions and unknown Poisson parameter  $\lambda$ . The method-of-moments estimate of parameter  $\lambda$  is just the sample average:  $\hat{\lambda} = 150/1,000 = 0.15$  claims per policy per year. It is also the case that  $\hat{\lambda}$  is a maximum-likelihood estimator of the parameter—see Problem 3.7.

In addition, the distribution based on  $\hat{\lambda}$  can be interpreted as a parametric distribution fit to the empirical distribution of the portfolio data. Table 3.1 compares the sample distribution to that implied by the Poisson formula  $f(n) = (0.15)^n e^{-0.15}/n!$ .

Visual inspection of the tabulated values shows that the Poisson probabilities are close to the sample values. However, one can test the goodness of fit in a more formal way, as with the Pearson chi-square test. First compute the Pearson statistic relative to the three cells containing policies with 0, 1, and 2 or more claims, respectively—grouping in this way avoids creating cells with frequencies that are too small. Here  $n_k$  denotes the observed policy frequency in the  $k^{\text{th}}$  cell. The expected cell frequency  $\phi_k(\hat{\lambda})$  predicted by the Poisson ( $\hat{\lambda}$ ) distribution is  $\phi_k(\hat{\lambda}) = 1,000\hat{p}_k$ , where  $\hat{p}_k$  is the Poisson ( $\hat{\lambda}$ ) probability of being in the  $k^{\text{th}}$  cell. Then

$$\chi^2 = \sum_{k=1}^3 \frac{(n_k - \phi_k(\hat{\lambda}))^2}{\phi_k(\hat{\lambda})} = \frac{(868 - 860.7)^2}{860.7} + \frac{(118 - 129.1)^2}{129.1} + \frac{(14 - 10.2)^2}{10.2} = 2.43.$$

The  $\chi^2$  statistic is approximately chi-square distributed, with degrees of freedom

$$d.f. = \# \text{ cells} - \# \text{ estimated parameters} - 1 = 3 - 1 - 1 = 1.$$

The 95<sup>th</sup> percentile of the chi-square distribution with  $d.f. = 1$  is  $\chi_{0.95}^2(1) = 3.84$ . Because  $\chi^2 = 2.43 < \chi_{0.95}^2(1)$ , we conclude at the 5% significance level that the Poisson distribution is an acceptable model for these data. ■

## 3.3. Parameter Uncertainty

It is sometimes the case that an insurance claim process is not strictly Poisson because the density parameter  $\lambda$  fails to be uniform throughout a population or is itself subject to some type of random fluctuation. For example, in a portfolio of insurance policies for which the random variable  $N$  is Poisson-distributed, the expected number of claims—the Poisson parameter  $\lambda$ —might vary from one insured to another. What is the distribution of  $N$  for a policy selected at random from such a population? Or consider the situation in which the distribution of the number of wind-damage claims depends on a parameter  $\lambda$  that varies with random changes in some key weather variables. How should one model the distribution of  $N$  in such a case?

Answers to questions like these can be obtained by means of a mixture of Poisson distributions, in which the parameter  $\lambda$  is itself taken to be a random variable. The resulting variable  $N$  having such a mixed distribution is called a model of **parameter uncertainty**.

To model parameter uncertainty in the Poisson case, begin by assuming that a given population of policies has a finite number  $m$  of parameter states  $\{S_i\}$ , where  $1 \leq i \leq m$ . In each state  $S_i$  the claim process is Poisson with claim density  $\alpha_i$  and  $\Pr\{\text{being in state } S_i\} = p_i$ , where  $p_1 + p_2 + \cdots + p_m = 1$ . Now let  $\lambda$  denote a random variable with the set of values  $\{\alpha_i\}$  and the associated discrete probability distribution, for which  $E[\lambda] = \sum_{i=1}^m \alpha_i p_i$ . In this context, variable  $\lambda$  is called the **mixing parameter** for the distribution of  $N$ .

For example, consider a portfolio of policies comprised of  $m$  disjoint subgroups, where the claim-count distribution in the  $i^{\text{th}}$  subgroup is Poisson with mean  $\alpha_i$ . The probability  $p_i$  of obtaining a single policy from the  $i^{\text{th}}$  subgroup in a random selection from this mixed portfolio is just the fraction of the total number of portfolio policies that belong to the  $i^{\text{th}}$  subgroup. The probability function of the claim-count variable  $N$  for such a randomly selected policy is then specified for each  $n = 0, 1, 2, \dots$  by the conditional probability formula

$$f_N(n) = \sum_{i=1}^m \Pr\{N = n | \lambda = \alpha_i\} \cdot \Pr\{\lambda = \alpha_i\} = \frac{1}{n!} \sum_{i=1}^m \alpha_i^n e^{-\alpha_i} p_i. \quad (3.9)$$

The expected value of this mixed distribution turns out to be, quite reasonably, the probability-weighted average of the  $\{\alpha_i\}$ , that is,  $E[\lambda]$ :

$$E[N] = \sum_{n=0}^{\infty} n \sum_{i=1}^m \Pr\{n | \lambda = \alpha_i\} p_i = \sum_{i=1}^m p_i \sum_{n=0}^{\infty} n \Pr\{n | \lambda = \alpha_i\} = \sum_{i=1}^m p_i \alpha_i = E[\lambda]. \quad (3.10)$$

The second moment is obtained in a similar way:

$$E[N^2] = \sum_{n=0}^{\infty} n^2 \sum_{i=1}^m \Pr\{n | \lambda = \alpha_i\} p_i = \sum_{i=1}^m p_i \sum_{n=0}^{\infty} n^2 \Pr\{n | \lambda = \alpha_i\} = \sum_{i=1}^m (\alpha_i + \alpha_i^2) p_i.$$

As a result, one can express  $Var[N]$  in terms of the mean and variance of  $\lambda$ :

$$Var[N] = E[\lambda] + \sum_{i=1}^m \alpha_i^2 p_i - (E[\lambda])^2 = E[\lambda] + Var[\lambda]. \quad (3.11)$$

It is evident from (3.10) and (3.11) that when  $N$  has a mixed Poisson distribution,  $Var[N] = E[N]$  if, and only if,  $Var[\lambda] = 0$  (in which case the variable  $\lambda$  is constant). Therefore, a mixture of distinct Poisson distributions—for which  $Var[\lambda] > 0$ —cannot itself be a Poisson distribution.

**Example 3.4.** A portfolio of 100 insurance policies for which the claim counts are Poisson-distributed produces an overall average of 0.51 claims per policy per year. However, this portfolio consists of four policy subgroups, representing four parameter states, with expected claim counts ranging from 0.10 to 1.40, as shown in the table. Also tabulated are the numbers of policies in each subgroup. Consequently, the distribution of  $N$  for a policy selected at random from this portfolio has a mixed Poisson distribution with probabilities

| State | Density $\alpha_i$ | # Policies |
|-------|--------------------|------------|
| $S_1$ | 0.10               | 20         |
| $S_2$ | 0.35               | 40         |
| $S_3$ | 0.70               | 30         |
| $S_4$ | 1.40               | 10         |
| Total | 0.51               | 100        |

$$f_N(n) = \frac{(0.10)^n e^{-0.10} (0.2) + (0.35)^n e^{-0.35} (0.4) + (0.70)^n e^{-0.70} (0.3) + (1.40)^n e^{-1.40} (0.1)}{n!}$$

As expected,  $E[N] = 0.51$ , and the variance exceeds the mean:  $Var[N] = 0.6439 > E[N]$ . Probabilities for  $N$  are shown in Table 3.2, where they are compared with those of the single Poisson distribution for which  $\lambda = 0.51$ .

**Table 3.2. Claim-Count Distributions [Example 3.4]**

| # Claims $n$ | $Pr\{N = n\}$ |                              |
|--------------|---------------|------------------------------|
|              | Mixed Poisson | Poisson ( $\lambda = 0.51$ ) |
| 0            | 0.6365        | 0.6005                       |
| 1            | 0.2556        | 0.3063                       |
| 2            | 0.0788        | 0.0781                       |
| 3            | 0.0218        | 0.0133                       |
| 4            | 0.0056        | 0.0017                       |
| 5            | 0.0013        | 0.0002                       |
| 6            | 0.0003        | 0.0000                       |
| $\geq 7$     | 0.0001        | 0.0000                       |
| Mean         | 0.5100        | 0.5100                       |
| Variance     | 0.6439        | 0.5100                       |

This example effectively illustrates how mixing several distinct Poisson distributions serves to increase the dispersion of the claim-count distribution over what would be expected in the case of a single Poisson distribution. ■

The discrete conditional probability formula (3.9) is readily generalized to the case in which the variable  $\lambda$  has a *continuous* density function  $f_\lambda(u)$  on the interval  $0 < u < \infty$  for which  $\int_0^\infty f_\lambda(u) du = 1$ . Thus, the continuous analog of (3.9) for claim counts  $n = 0, 1, 2, \dots$  is given by the integral formula

$$f_N(n) = \int_0^\infty \Pr\{N = n | \lambda = u\} f_\lambda(u) du = \frac{1}{n!} \int_0^\infty u^n e^{-u} f_\lambda(u) du. \quad (3.12)$$

Formulas (3.10) and (3.11) for the mean and variance of  $N$  also hold in the continuous case. For example, in the following continuous analog of (3.10) integration over the semi-infinite interval  $0 < u < \infty$  replaces summation over the finite set of parameter values  $\{\alpha_j\}$ :

$$E[N] = \sum_{n=0}^\infty n \int_0^\infty \frac{u^n e^{-u}}{n!} f_\lambda(u) du = \int_0^\infty \left( \sum_{n=0}^\infty n \frac{u^n e^{-u}}{n!} \right) f_\lambda(u) du = \int_0^\infty u f_\lambda(u) du = E[\lambda]. \quad (3.13)$$

As before, the second moment is  $E[N^2] = E[\lambda] + E[\lambda^2]$ , so that

$$\text{Var}[N] = E[\lambda] + \text{Var}[\lambda] = E[N] + \text{Var}[\lambda]. \quad (3.14)$$

Moreover,

$$Sk[N] = \frac{E[\lambda] + 3\text{Var}[\lambda] + E[(\lambda - E[\lambda])^3]}{(E[\lambda] + \text{Var}[\lambda])^{3/2}}. \quad (3.15)$$

**Example 3.5.** Parameter  $\lambda$  for a mixed Poisson distribution has an exponential density function:  $f_\lambda(u) = 4e^{-4u}$ ,  $0 < u < \infty$ . Consequently,  $E[\lambda] = 0.25$  and  $\text{Var}[\lambda] = 0.0625$ . The claim-count probabilities for the mixed distribution follow from (3.12):

$$f_N(n) = \frac{4}{n!} \int_0^\infty u^n e^{-5u} du = \frac{4}{n!} \Gamma(n+1) 5^{-(n+1)} = (0.8)(0.2)^n, \quad n = 0, 1, 2, \dots$$

This distribution is an instance of the *geometric distribution*—see Problem 3.21. Table 3.3 displays probabilities for the distribution, again compared to those of the related, but less-dispersed single Poisson distribution. ■

<sup>31</sup> By using the Riemann–Stieltjes integral, formulas (3.9) and (3.12) can both be expressed by the single integral formula  $f_N(n) = (1/n!) \int_0^\infty u^n e^{-u} dF_{\lambda(u)}$ , where the function  $F_\lambda(u)$  is the cumulative distribution function for the variable mixing parameter  $\lambda$ .

**Table 3.3. Claim-Count Distributions [Example 3.5]**

| # Claims $n$ | $\Pr\{N = n\}$ |                              |
|--------------|----------------|------------------------------|
|              | Mixed Poisson  | Poisson ( $\lambda = 0.25$ ) |
| 0            | 0.8000         | 0.7788                       |
| 1            | 0.1600         | 0.1947                       |
| 2            | 0.0320         | 0.0243                       |
| 3            | 0.0064         | 0.0020                       |
| 4            | 0.0013         | 0.0001                       |
| 5            | 0.0003         | 0.0000                       |
| $\geq 6$     | 0.0001         | 0.0000                       |
| Mean         | 0.2500         | 0.2500                       |
| Variance     | 0.3125         | 0.2500                       |

The mixed Poisson distribution provides a powerful alternative to the single Poisson distribution in modeling insurance claim data. However, the mixed distribution approach does require that one must have some a priori knowledge of the distribution of the variable parameter  $\lambda$ . In cases where claim data can reasonably be partitioned into a finite number of homogenous subgroups, as in Example 3.4, there is usually no difficulty in constructing the mixed distribution. On the other hand, if one is presented with a sample of claim data for which the mean and variance are quite different, then finding an appropriate parametric distribution in the absence of additional information about the population is more challenging. A common solution to this problem, which involves a special family of distributions for the variable  $\lambda$ , is the topic of the next section.

## 3.4. Negative Binomial Distributions

It is often the case that claim-count data yield a sample distribution with markedly different mean and variance and that very little is known about the actual population distribution. Nevertheless, the actuary can be faced with the problem of fitting a parametric distribution to such data in order to model the claim-count probabilities of a policy selected at random from the underlying population.

In situations like this it has proven useful to suppose that the population has a mixed Poisson distribution and, in the absence of any other information, to *assume* a particular distribution for the variable parameter  $\lambda$ . Gamma distributions are almost always used for this purpose because of the useful analytic form of the resulting mixed distribution.

We start by assuming that the mixing parameter  $\lambda$  has a gamma distribution with positive parameters  $\alpha$  and  $\beta = v/\alpha$  and the resulting density function

$$f_{\lambda}(u) = \frac{(\alpha/v)^{\alpha}}{\Gamma(\alpha)} u^{\alpha-1} e^{-(\alpha/v)u}, \quad 0 < u < \infty. \quad (3.16)$$

This special choice of  $\alpha$  and  $\beta$  is contrived to yield convenient forms for the means and variances of  $\lambda$  and  $N$ . In particular,  $E[\lambda] = v$  and  $Var[\lambda] = v^2/\alpha$ . The probability function for  $N$  is then obtained by substituting (3.16) into formula (3.12) for each  $n = 0, 1, 2, \dots$ :

$$\begin{aligned}
 f_N(n) &= \int_0^\infty \frac{u^n e^{-u}}{n!} \cdot \frac{(\alpha/v)^\alpha}{\Gamma(\alpha)} u^{\alpha-1} e^{-(\alpha/v)u} du \\
 &= \frac{(\alpha/v)^\alpha}{n! \Gamma(\alpha)} \int_0^\infty u^{\alpha+n-1} e^{-\left(\frac{v+\alpha}{v}\right)u} du \\
 &= \frac{(\alpha/v)^\alpha}{n! \Gamma(\alpha)} \Gamma(\alpha+n) \left(\frac{v+\alpha}{v}\right)^{-(\alpha+n)} \\
 &= \frac{\Gamma(\alpha+n)}{n! \Gamma(\alpha)} \left(\frac{\alpha}{v+\alpha}\right)^\alpha \left(\frac{v}{v+\alpha}\right)^n.
 \end{aligned} \tag{3.17}$$

The mean, variance, and skewness of  $N$  are thus given by formulas (3.13), (3.14), and (3.15):

$$\begin{aligned}
 E[N] &= v, \\
 Var[N] &= v + \frac{v^2}{\alpha}, \\
 Sk[N] &= \frac{\alpha^3 v + 3\alpha^2 v^2 + 2\alpha v^3}{(\alpha^2 v + \alpha v^2)^{3/2}}.
 \end{aligned} \tag{3.18}$$

The mixed probability distribution defined by (3.17) is a member of the **negative binomial** distribution family. Such a distribution has a probability function, with parameters  $r$  and  $q$ , of the general form

$$f(n) = \binom{r+n-1}{n} q^r (1-q)^n \quad (r > 0, 0 < q < 1), \quad n = 0, 1, 2, \dots \tag{3.19}$$

The leading coefficient in this function is an instance of the **general binomial coefficient**, defined for all real  $x$  and  $n = 0, 1, 2, 3, \dots$  by

$$\binom{x}{n} = \frac{\Gamma(x+1)}{n! \Gamma(x-n+1)} = \begin{cases} 1 & \text{if } n = 0 \\ \frac{x(x-1)(x-2)\cdots(x-n+1)}{n!} & \text{if } n > 0. \end{cases} \tag{3.20}$$

Putting  $r = \alpha$  and  $q = \alpha/(v + \alpha)$  into (3.19) and then applying (3.20) shows that probability function (3.17) does indeed belong to the negative binomial family.

The general binomial coefficient first arose in connection with Isaac Newton's *binomial series*, a convergent series expansion valid for all real  $s$ :

$$(1+x)^s = \sum_{n=0}^{\infty} \binom{s}{n} x^n, \quad -1 < x < 1. \quad (3.21)$$

When the exponent  $s$  is a positive integer  $m$ ,  $\binom{s}{n} = \binom{m}{n}$  is identical to the standard binomial coefficient  ${}_m C_n$  of combinatorial analysis:

$$\binom{m}{n} = {}_m C_n = \begin{cases} 0 & \text{if } n > m \\ \frac{m!}{n!(m-n)!} & \text{if } 0 \leq n \leq m. \end{cases}$$

Moreover, whenever  $s = m$  series (3.21) reduces to the familiar finite sum of the elementary Binomial Theorem.

The negative binomial distribution is so called because the probabilities in (3.19) are fixed multiples of terms from a convergent binomial series with negative exponent. This becomes evident after using the identity

$$\binom{r+n-1}{n} = (-1)^n \binom{-r}{n}, \quad r > 0 \quad (3.22)$$

to restate probability function (3.19) as

$$f(n) = \binom{-r}{n} q^r (q-1)^n. \quad (3.23)$$

Verification of  $\sum_{n=0}^{\infty} f(n) = 1$  follows immediately from (3.21) with  $x = q-1$  and negative exponent  $s = -r$ :

$$\sum_{n=0}^{\infty} f(n) = q^r \sum_{n=0}^{\infty} \binom{-r}{n} (q-1)^n = q^r (1+q-1)^{-r} = 1.$$

The negative binomial moment-generating function is obtained in a similar way:

$$M(t) = \sum_{n=0}^{\infty} e^{tn} \binom{-r}{n} q^r (q-1)^n = q^r (1+(q-1)e^t)^{-r}, \quad -\infty < t < -\log(1-q). \quad (3.24)$$

Returning to the mixed distribution (3.17), one can see that for a given mean  $\nu$  the size of  $Var[N]$  relative to  $E[N]$  is determined by parameter  $\alpha$ . The larger the value of  $\alpha$ , the more nearly equal are  $Var[N]$  and  $E[N]$  and conversely. One can therefore interpret  $1/\alpha$  as a measure of parameter uncertainty—of how significantly the mixed distribution deviates from a single Poisson.

Not surprisingly, the Poisson distribution is a limiting case—that is, for fixed mean  $v$  the negative binomial distribution (3.17) tends to a Poisson distribution as  $\alpha \rightarrow \infty$ . This can be easily demonstrated using the moment-generating function. The generating function of distribution (3.17) is

$$M(t) = \left(1 - \frac{v}{\alpha}(e^t - 1)\right)^{-\alpha}, \quad -\infty < t < \log((v + \alpha)/v),$$

obtained by substituting  $r = \alpha$  and  $q = \alpha/(v + \alpha)$  into (3.24). Passing to the limit as  $\alpha \rightarrow \infty$  while holding  $v$  constant yields

$$\lim_{\alpha \rightarrow \infty} M(t) = \lim_{\alpha \rightarrow \infty} \left(1 - \frac{v}{\alpha}(e^t - 1)\right)^{-\alpha} = \exp(v(e^t - 1)), \quad (3.25)$$

the moment-generating function of a Poisson random variable with mean  $v$ . The conclusion follows from the uniqueness property of the generating function.

One of the earliest uses of the negative binomial as a mixed Poisson distribution was in modeling the concept of *accident proneness*. The number of accidents incurred by individual members of a population group was assumed to be Poisson-distributed, but with different parameters—the more “accident-prone” members having larger Poisson parameters and those less so having smaller expected values. In the realm of property/casualty insurance, actuaries began to apply the negative binomial distribution to automobile liability in the 1950s and 1960s.<sup>32</sup> Since then, the distribution has enjoyed a wide range of applicability.

**Example 3.6.** Claim-count data from a sample of 5,000 automobile liability policies are displayed in the table. Here the mean 0.1238 and variance 0.130074 are unequal. This inequality suggests that the policies were possibly drawn not from a homogeneous population of Poisson-distributed policies but from a mix of policies with different Poisson distributions.

| # Claims | # Policies |
|----------|------------|
| 0        | 4,429      |
| 1        | 528        |
| 2        | 39         |
| 3        | 3          |
| 4        | 1          |
| ≥5       | 0          |
| Total    | 5,000      |

To obtain the distribution of claim counts for a single policy selected at random from this population, we shall assume a negative binomial distribution of the form (3.17) and search for appropriate parameter estimates  $(\hat{\alpha}, \hat{v})$ . Derivation of maximum-likelihood parameter estimates for the negative binomial distribution involves some difficult, but not insurmountable, complexities,<sup>33</sup> whereas the method-of-moments estimates are easily calculated. Opting

<sup>32</sup> For an example of such early applications of the negative binomial distribution in auto insurance see Hewitt [6].

<sup>33</sup> For example, refer to Simon [21]. In most cases the maximum-likelihood equations are solvable only by iteration, but Simon observes that the method “will usually produce answers very similar to the method-of-moments” estimates.

**Table 3.4. Negative Binomial Distribution [Example 3.6]**

| # Claims $n$ | Pr{ $n$ claims} |                   |
|--------------|-----------------|-------------------|
|              | Sample          | Negative binomial |
| 0            | 0.8858          | 0.8862            |
| 1            | 0.1056          | 0.1044            |
| 2            | 0.0078          | 0.0087            |
| 3            | 0.0006          | 0.0006            |
| 4            | 0.0002          | 0.0000            |
| $\geq 5$     | 0.0000          | 0.0000            |

for the latter approach, we set  $\hat{v} = 0.1238$  and then solve the variance formula  $Var = \hat{v} + \hat{v}^2/\hat{\alpha} = 0.130074$  for  $\hat{\alpha}$ :

$$\hat{\alpha} = \frac{(0.1238)^2}{0.130074 - 0.1238} = 2.44285.$$

Probabilities calculated from the resulting mass function

$$f(n) = \frac{\Gamma(2.44285 + n)}{n! \Gamma(2.44285)} (0.951766)(0.048234)^n, \quad n = 0, 1, 2, \dots,$$

are displayed in Table 3.4. The chi-square statistic based on the four cells corresponding to 0, 1, 2, and 3 or more claims is  $\chi^2 = 0.7753$ . The degrees-of-freedom parameter is  $d.f. = 4 - 2 - 1 = 1$ , so the rejection limit for a test at the 5% significance level is  $\chi_{0.95}^2(1) = 3.84$ . Because  $\chi^2 < 3.84$ , one can conclude that the negative binomial distribution is an acceptable model.

Recall that a negative binomial distribution can be interpreted as a mixture of Poisson distributions with a variable gamma-distributed mixing parameter  $\lambda$ . In this case an *implied* gamma density function for the variable mixing parameter  $\lambda$  can be obtained by putting  $\hat{\alpha}$  and  $\hat{v}$  into formula (3.16):

$$f_{\lambda}(u) = (1141.264) u^{1.44285} e^{-19.7322u}, \quad 0 < u < \infty.$$

Here  $E[\lambda] = 0.1238 = v$  and  $Var[\lambda] = 0.006274$ . A graph of this density function  $y = f_{\lambda}(u)$  is shown in Figure 3.1. ■

## 3.5. Claim Contagion

One of the assumptions of the Poisson claim-count process, that of independence of successive claims, is not always satisfied. This happens whenever the occurrence of a claim changes the probability of subsequent claims. For example, a successful products

**Figure 3.1. Implied Gamma Density Function for Mixing Parameter  $\lambda$  [Example 3.6]**

![Figure 3.1: A graph of the implied Gamma Density Function y = f_lambda(u). The horizontal axis is labeled u and has tick marks at 0.0, v, 0.2, and 0.4. The vertical axis is labeled y and has tick marks from 0 to 6. The curve starts at the origin (0,0), rises to a peak of approximately 6.2 at u ≈ 0.1, and then gradually declines, passing through the point (v, 4.5) where a vertical dashed line is drawn. The curve approaches the u-axis as u increases beyond 0.4.](e5a2c617a7a3399d1d266c93c62073b1_img.jpg)

Figure 3.1: A graph of the implied Gamma Density Function y = f\_lambda(u). The horizontal axis is labeled u and has tick marks at 0.0, v, 0.2, and 0.4. The vertical axis is labeled y and has tick marks from 0 to 6. The curve starts at the origin (0,0), rises to a peak of approximately 6.2 at u ≈ 0.1, and then gradually declines, passing through the point (v, 4.5) where a vertical dashed line is drawn. The curve approaches the u-axis as u increases beyond 0.4.

liability claim against a manufacturer often increases the likelihood that similar claims will be brought in the future—a classic example of *claim contagion*. A standard approach to modeling such a contagion process is based on an urn model proposed by the Hungarian mathematician George Pólya (1887–1985). Pólya models have since been used to model a variety of contamination processes, including the spread of contagious diseases.<sup>34</sup>

In the Pólya model, an urn initially contains  $w$  white balls and  $b$  black balls. A trial consists of drawing one ball at random, noting its color, and then replacing it together with  $c$  additional balls of the same color. Obtaining a white ball on the first trial therefore increases the probability of selecting a white ball on the next trial. The probability function for the number  $W_m$  of white balls obtained in  $m$  trials, is derived by conventional combinatorial methods:

$$\Pr\{W_m = n\} = P_n(w, b, c; m) = {}_m C_n \frac{\prod_{i=0}^{n-1} (w + ic) \prod_{i=0}^{m-n-1} (b + ic)}{\prod_{i=0}^{m-1} (w + b + ic)}, \quad n = 0, 1, \dots, m. \quad (3.26)$$

A distribution with probabilities  $P_n(w, b, c; m)$  is known as a *Pólya distribution*.<sup>35</sup> The ratio  $\gamma = c/w$  is customarily called the *degree of contagion*. When there is no contagion—that is, when  $c = \gamma = 0$ —the Pólya distribution is identical to the simpler binomial distribution for which the probability of drawing a white ball remains constant throughout successive trials.

<sup>34</sup> Pólya's original contamination model first appeared in a 1923 paper by Pólya and F. Eggenberger "Über die Statistik der vergetteter Vorgänge," *Zeitschrift für Angewandte Mathematik und Mechanik*, III, 279–289]. The present formulation is based on that presented by William Feller in his classic probability textbook: Feller [4], pp. 118–121, 142–143. Urn models have been used to model probability distributions ever since they were introduced by Swiss mathematician Jacob Bernoulli to describe the two-outcome experiment underlying the random variable now known as a Bernoulli variable.

<sup>35</sup> Although history and logic dictate that (3.26) should be called the Pólya distribution, some authors apply that name instead to the associated negative binomial distribution (3.27).

To derive the moments of the distribution for  $W_m$ , let  $p$  denote the probability of drawing a white ball in the first Pólya trial:  $p = w/(w + b)$ . Then

$$\begin{aligned} E[W_m] &= \sum_{n=0}^m nP_n(w, b, c; m) = \frac{mw}{w+b} \sum_{n=1}^m P_{n-1}(w+c, b, c; m-1) \\ &= mp \sum_{k=0}^{m-1} P_k(w+c, b, c; m-1) \\ &= mp. \end{aligned}$$

Similar reasoning yields

$$E[W_m^2] = mp + m(m-1) \frac{w+c}{w+b+c} p = mp + m(m-1) p^2 \frac{1+\gamma}{1+p\gamma},$$

so that

$$\text{Var}[W_m] = mp \left( 1 + (m-1) \frac{1+\gamma}{1+p\gamma} p - mp \right).$$

It is instructive to compare these formulas to the respective mean  $mp$  and variance  $mp(1-p)$  of the related binomial distribution. Clearly, the two distributions have identical means, each equal to  $mp$ . The Pólya distribution, as one would reasonably expect, has the larger variance:  $\text{Var}[W_m] \geq mp(1-p)$ .

**Example 3.7.** Pólya trials are conducted with an urn that initially contains  $w = 10$  white balls and  $b = 5$  black balls. Corresponding to  $c = 2$ , the degree of contagion is  $\gamma = 2/10$ . The initial probability is therefore  $p = E[W_1] = 10/15$ . Various probabilities for drawing white balls in the first three trials are given by

$$\Pr\{\text{white on 1st trial}\} = \frac{10}{15} = 0.6667,$$

$$\Pr\{\text{white on 2nd trial} | \text{white on 1st trial}\} = \frac{12}{17} = 0.7059,$$

$$\Pr\{\text{white on 2nd trial} | \text{black on 1st trial}\} = \frac{10}{17} = 0.5882,$$

$$\Pr\{\text{white on 2nd trial}\} = \frac{12}{17} \cdot \frac{10}{15} + \frac{10}{17} \cdot \frac{5}{15} = 0.6667,$$

$$\Pr\{\text{white on 3rd trial} | \text{white on 1st \& 2nd trials}\} = \frac{14}{19} = 0.7368,$$

$$\Pr\{\text{white on 3rd trial} | \text{black on 1st \& 2nd trials}\} = \frac{10}{19} = 0.5263.$$

**Table 3.5. Pólya and Binomial Probabilities [Example 3.7]**

| # White Balls $n$ | Pr{ $n$ white balls in 6 trials} |                      |
|-------------------|----------------------------------|----------------------|
|                   | Pólya ( $c = 2$ )                | Binomial ( $c = 0$ ) |
| 0                 | 0.0115                           | 0.0014               |
| 1                 | 0.0462                           | 0.0165               |
| 2                 | 0.1066                           | 0.0823               |
| 3                 | 0.1809                           | 0.2195               |
| 4                 | 0.2412                           | 0.3292               |
| 5                 | 0.2481                           | 0.2634               |
| 6                 | 0.1654                           | 0.0878               |
| Mean              | 4.0000                           | 4.0000               |
| Variance          | 2.1176                           | 1.3333               |

The probabilities  $P_n(10,5,2;6)$  for obtaining  $n$  white balls in six successive Pólya trials are shown in Table 3.5 and compared with those for the related binomial distribution, for which  $c = 0$ . The expected count for each distribution is  $mp = 4$ , but the Pólya distribution with positive contagion has the larger variance, a fact clearly evident in Figure 3.2. ■

To interpret the Pólya urn model as a claim process, identify the draw of a white ball in a Pólya trial with the occurrence of a claim. However, contagion in the urn model occurs at discrete times, after each draw from the urn. Modeling a time-continuous claim process, this time with contagion, again requires some type of limit process.

We proceed as in Section 3.1, where a Poisson distribution arose as the limit of a sequence of binomial distributions. Again, partition the basic time period—the policy

**Figure 3.2. Pólya and Binomial Distributions [Example 3.7]**![Bar chart comparing Pólya and Binomial distributions. The x-axis represents the number of white balls (n) from 0 to 6. The y-axis represents probability from 0.0 to 0.3. Black bars represent the Pólya distribution, and light gray bars represent the Binomial distribution. The Pólya distribution has a higher peak at n=4 and a higher probability at n=0 and n=6 compared to the Binomial distribution.](a7e667227af01b0bd7f81d42ebae5c07_img.jpg)

| n | Pólya  | Binomial |
|---|--------|----------|
| 0 | 0.0115 | 0.0014   |
| 1 | 0.0462 | 0.0165   |
| 2 | 0.1066 | 0.0823   |
| 3 | 0.1809 | 0.2195   |
| 4 | 0.2412 | 0.3292   |
| 5 | 0.2481 | 0.2634   |
| 6 | 0.1654 | 0.0878   |

Bar chart comparing Pólya and Binomial distributions. The x-axis represents the number of white balls (n) from 0 to 6. The y-axis represents probability from 0.0 to 0.3. Black bars represent the Pólya distribution, and light gray bars represent the Binomial distribution. The Pólya distribution has a higher peak at n=4 and a higher probability at n=0 and n=6 compared to the Binomial distribution.

term—into  $m$  subintervals of equal length and perform one Pólya trial per subinterval. Then let  $m \rightarrow \infty$  in such a way that the expected number of white balls (that is, claims) in the time period remains constant:  $mp = v > 0$ . Passage to the limit is carried out in such a way that the degree of contagion  $\gamma$  remains constant, as well. As before, the probability structure in each subinterval changes with  $m$  so that  $p \rightarrow 0$  as  $m \rightarrow \infty$ . Whenever  $\gamma > 0$  the limit of the Pólya probability function (3.26) is

$$\lim_{\substack{m \rightarrow \infty \\ mp=v}} P_n(w, b, c; m) = \binom{1/\gamma + n - 1}{n} \left( \frac{1}{1 + \gamma v} \right)^{1/\gamma} \left( \frac{\gamma v}{1 + \gamma v} \right)^n, \quad n = 0, 1, 2, \dots \quad (3.27)$$

Comparison to formula (3.19), after setting  $r = 1/\gamma$  and  $q = 1/(1 + \gamma v)$ , reveals the limiting distribution to be negative binomial with mean  $v$  and variance  $v + \gamma v^2$ .

Thus we have observed that two distinct situations—claim contagion in this section and parameter uncertainty with a gamma-distributed  $\lambda$  discussed in Section 3.4—give rise to the same distribution family for the claim-count variable  $N$ . In fact, the negative binomial distribution in (3.27), with mean  $v$  and contagion parameter  $\gamma$ , is identical to the negative binomial distribution (3.17) with mean  $v$  and uncertainty parameter  $\alpha = 1/\gamma$ . It is not surprising, then, that the negative binomial distribution remains the principal alternative to the Poisson for modeling the distribution of property/casualty claim counts.

We conclude this section with an outline of the proof of limit formula (3.27) in which the negative binomial is obtained as the limiting case of the Pólya distribution for a contagion model.

**Proof of (3.27):** Start by expressing the Pólya probability function in terms of the general binomial coefficients, where  $\gamma = c/w$  and  $p = w/(w + b)$ :

$$P_n(w, b, c; m) = \binom{\frac{1}{\gamma} + n - 1}{n} \binom{\frac{1-p}{\gamma p} + m - n - 1}{m - n} \bigg/ \binom{\frac{1}{\gamma p} + m - 1}{m}.$$

An application of the identity in Problem 3.27(b) yields

$$P_n(w, b, c; m) = \binom{\frac{1}{\gamma} + n - 1}{n} \cdot \underbrace{\frac{\binom{\frac{1-p}{\gamma p} + m - n - 1}{m - n}}{\binom{\frac{1}{\gamma p} + m - n - 1}{m - n}}}_A \cdot \underbrace{\frac{\prod_{i=1}^n \left(1 - \frac{i-1}{m}\right)}{\prod_{i=1}^n \left(\frac{1}{\gamma p m} + \frac{m-i}{m}\right)}}_B. \quad (3.28)$$

To complete the proof, we evaluate the limits of quotients  $A$  and  $B$  in turn.

First, apply to quotient  $A$  in equation (3.28) formula (3.20) defining the general binomial coefficient as a ratio of gamma function expressions. This yields

$$A = \frac{\binom{\frac{1-p}{\gamma p} + m - n - 1}{m - n}}{\binom{\frac{1}{\gamma p} + m - n - 1}{m - n}} = \frac{\Gamma\left(\frac{1-p}{\gamma p} + m - n\right)}{\Gamma\left(\frac{1}{\gamma p} + m - n\right)} \cdot \frac{\Gamma\left(\frac{1}{\gamma p}\right)}{\Gamma\left(\frac{1-p}{\gamma p}\right)}.$$

The limit of  $A$  is based on the asymptotic relation  $\Gamma(x) \sim \sqrt{2\pi} e^{-x} x^{x-1/2}$ .<sup>36</sup> Applying this to the gamma functions in the last equation, substituting  $Q = \gamma pm - \gamma pn$ , and observing that factors involving  $\sqrt{2\pi} e^{-x}$  cancel, one obtains

$$\begin{aligned} A &\sim \frac{\left(\frac{1-p + \gamma pm - \gamma pn}{\gamma p}\right)^{\frac{1+\gamma pm - \gamma pn}{\gamma p} - \frac{1}{2}}}{\left(\frac{1 + \gamma pm - \gamma pn}{\gamma p}\right)^{\frac{1+\gamma pm - \gamma pn}{\gamma p} - \frac{1}{2}}} \cdot \frac{\left(\frac{1}{\gamma p}\right)^{\frac{1}{\gamma p} - \frac{1}{2}}}{\left(\frac{1-p}{\gamma p}\right)^{\frac{1}{\gamma p} - \frac{1}{2}}} \\ &= \left(\frac{1-p+Q}{1+Q}\right)^{\frac{1+Q}{\gamma p}} (1-p)^{-1/(\gamma p)} \left(\frac{1-p}{1-p+Q}\right)^{1/\gamma} \sqrt{\frac{(1-p)(1+Q)}{1-p+Q}}. \end{aligned}$$

An application of the limit formulas

$$\lim_{\substack{m \rightarrow \infty \\ mp = v}} Q = \gamma v \quad \text{and} \quad \lim_{\delta \rightarrow 0} (1 + \delta x)^{1/\delta} = e^x$$

yields the desired limit:

$$\lim_{\substack{m \rightarrow \infty \\ mp = v}} A = e^{-1/\gamma} \cdot e^{1/\gamma} \cdot \left(\frac{1}{\gamma v + 1}\right)^{1/\gamma} \cdot 1 = \left(\frac{1}{\gamma v + 1}\right)^{1/\gamma}.$$

For quotient  $B$  in equation (3.28) we have

$$\lim_{\substack{m \rightarrow \infty \\ mp = v}} B = \lim_{\substack{m \rightarrow \infty \\ mp = v}} \frac{\left(1 - \frac{0}{m}\right) \left(1 - \frac{1}{m}\right) \cdots \left(1 - \frac{n-1}{m}\right)}{\left(\frac{1}{\gamma pm} + \frac{m-1}{m}\right) \left(\frac{1}{\gamma pm} + \frac{m-2}{m}\right) \cdots \left(\frac{1}{\gamma pm} + \frac{m-n}{m}\right)}$$

<sup>36</sup> This relation is a generalization of Stirling's approximation formula:  $n! \sim \sqrt{2\pi n} (n/e)^n$ ,  $n$  a positive integer; see Feller [4], pp. 52–54, 66.  $f(x) \sim g(x)$  means that  $\lim_{x \rightarrow \infty} f(x)/g(x) = 1$ . Therefore,  $f(x) \sim g(x)$  and  $\lim_{x \rightarrow \infty} g(x) = L$  together imply that  $\lim_{x \rightarrow \infty} f(x) = L$ .

$$\begin{aligned}
 &= \frac{1}{\left(\frac{1}{\gamma v} + 1\right)^n} \\
 &= \left(\frac{\gamma v}{1 + \gamma v}\right)^n.
 \end{aligned}$$

This completes the proof. ■

## 3.6. Portfolio Claims

Up to now our focus has been on modeling the claim process for a single policy. However, it is also important to find probability models that describe the aggregate behavior of entire portfolios of similar policies. In a variety of situations it is possible to infer the distribution of the portfolio claim count from those of the individual component policies.

For example, if the claim process for each policy in a portfolio of policies is Poisson, what can be said about the distribution of  $N$ , the total number of *portfolio* claims that occur during a policy period? The answer lies in the reproductive property of Poisson variables—that is, the sum of mutually independent Poisson random variables is also Poisson-distributed. This fact follows from an argument based on the moment-generating function.

Let  $N = N_1 + N_2 + \cdots + N_m$  be the sum of  $m$  independent Poisson random variables. If  $E[N_i] = \lambda_i$ , where  $1 \leq i \leq m$ , then

$$\begin{aligned}
 M_N(t) &= E\left[\exp\left(t \sum_{i=1}^m N_i\right)\right] = \prod_{i=1}^m E\left[e^{tN_i}\right] = \prod_{i=1}^m \exp(\lambda_i e^t - \lambda_i) \\
 &= \exp\left(\left(\sum_{i=1}^m \lambda_i\right)(e^t - 1)\right),
 \end{aligned}$$

the moment-generating function for a Poisson variable with parameter  $\sum_{i=1}^m \lambda_i$ . The uniqueness property of the generating function implies that  $N$  must be Poisson-distributed with mean  $\sum_{i=1}^m \lambda_i$ .

In the special case that each policy in a portfolio of  $m$  policies has the same Poisson distribution with expected value  $\lambda$ , it is evident that the portfolio claim-count variable  $N$  has a Poisson distribution with parameter  $m\lambda$ .

One can similarly show by means of the moment-generating function that the sum  $N = N_1 + N_2 + \cdots + N_m$  of mutually independent negative binomial variables, identically distributed as in (3.17) with parameters  $(\alpha, v)$ , has a negative binomial distribution with parameters  $(m\alpha, mv)$ :

$$\begin{aligned}
 M_N(t) &= \prod_{i=1}^m E\left[e^{tN_i}\right] = \left(\left(1 - \frac{v}{\alpha}(e^t - 1)\right)^{-\alpha}\right)^m \\
 &= \left(1 - \frac{1}{m\alpha}mv(e^t - 1)\right)^{-m\alpha}.
 \end{aligned}$$

On the other hand, the sum  $N$  does not necessarily have a negative binomial distribution when the  $\{N_i\}$  have different  $\alpha$  and  $\nu$  parameters. Consequently, the sum of independent claim-count random variables, each with a contagion structure as described in Section 3.5, is not always itself a negative binomial contagion model. Nevertheless, it is often desirable to be able to treat such a distribution as if it *were* such a model. One can do this by defining the contagion parameter  $\gamma$  for an arbitrary claim-count variable  $N$  in a way that is consistent with the negative binomial case, namely,

$$\gamma = \frac{\text{Var}[N] - E[N]}{(E[N])^2}, \quad (3.29)$$

obtained by rearranging the negative binomial formula

$$\text{Var}[N] = E[N] + \gamma(E[N])^2.$$

Formula (3.29) implies that the contagion parameter for a Poisson random variable is  $\gamma = 0$ , as one would reasonably expect.

**Example 3.8.** Consider a group of 100 identical policies, each with a Poisson claim process and an expected annual claim count of 0.035 per policy. What is the probability that these policies in aggregate generate five or more claims during a single year?

The portfolio claim-count variable  $N$  is the sum of identically distributed Poisson variables. Under the reasonable assumption that the claim processes associated with these policies are independent, the reproductive property of the Poisson process implies that  $N$  also has a Poisson distribution, with parameter  $\lambda = (100)(0.035) = 3.50$ . Therefore,

$$\Pr\{N \geq 5\} = 1 - e^{-3.50} \left( 1 + 3.50 + \frac{1}{2}(3.50)^2 + \frac{1}{6}(3.50)^3 + \frac{1}{24}(3.50)^4 \right) = 0.2746. \blacksquare$$

**Example 3.9.** A portfolio contains 20 independent, identically-distributed policies subject to claim contagion. Each policy has an expected claim count of  $\nu = 0.150$  per year and contagion parameter  $\gamma = 0.400$ . Thus the distribution of the portfolio claim count  $N$  is negative binomial, with

$$E[N] = (20)(0.150) = 3.000,$$

$$\text{Var}[N] = (20)(0.150) + (0.400)(20)(0.150)^2 = 3.180.$$

Formula (3.29) implies a portfolio contagion parameter of

$$\gamma = \frac{3.180 - 3.000}{(3.000)^2} = 0.020. \blacksquare$$

## 3.7. Problems

- 3.1** Random variable  $N$  has a binomial  $(m, p)$  distribution.
- (a) Use  $M_N(t)$  to derive the mean, variance, and skewness for  $N$ .
- (b) Evaluate  $\lim_{\substack{m \rightarrow \infty \\ mp = \lambda}} M_N(t)$ , where  $\lambda > 0$ . What conclusion can be drawn?
- 3.2** Verify that the Poisson probability function (3.4) satisfies  $\sum_{n=0}^{\infty} P_n(t) = 1$ .
- 3.3** Assume that claim-count variable  $N$  has probability function  $f(n) = \lambda^n e^{-\lambda} / n!$ . What are the values of  $\lambda$  and  $\Pr\{N \leq 3\}$  in each case?
- (a)  $E[N] = 3.20$ .      (b)  $Var[N] = 2.50$ .
- (c)  $Sk[N] = 0.40$ .      (d)  $f(1) = f(2)$ .
- (e)  $E[e^{tN}] = e^{4e^t} / e^4$ .      (f)  $f(0) = 0.80$ .
- 3.4** The policy claim count for a liability line of insurance is Poisson-distributed with constant density of 0.10 claims per policy per year. Compute the probability that a single policy has exactly two claims when the policy term is:
- (a) 6 months.      (b) 15 months.      (c) 24 months.
- 3.5** Use mathematical induction to verify equation (3.3) for the decomposition of  $P_n(t+h)$  in the derivation of the Poisson probability function.
- 3.6** Prove that the Poisson probability function  $f(n) = \lambda^n e^{-\lambda} / n!$  has a maximum value at  $n = \llbracket \lambda \rrbracket$ , where  $\llbracket x \rrbracket$  denotes the greatest integer function. [Hint: show that  $f$  satisfies the recursion relation  $f(n) = (\lambda/n) f(n-1)$  for  $n = 1, 2, 3, \dots$ ]
- 3.7** Let  $\langle n_i \rangle$  be a set of observations for a random sample of claim counts  $\langle N_1, N_2, \dots, N_m \rangle$  drawn from a Poisson-distributed population with unknown parameter  $\lambda$ . Prove that the sample mean  $M_1 = \frac{1}{m} \sum_{i=1}^m n_i$  is a maximum-likelihood estimator for  $\lambda$ .
- 3.8** Show that the cumulative distribution function  $F(n)$  for a Poisson ( $\lambda$ ) random variable can be expressed at each nonnegative integer  $n$  by

$$F(n) = \sum_{k=0}^n \frac{\lambda^k e^{-\lambda}}{k!} = 1 - \frac{\Gamma(\lambda, n+1)}{n!}.$$

- 3.9** The distribution of policy-year claims in a portfolio of 6,000 identical policies is summarized in the table.
- (a) Fit a Poisson model to these data to obtain a probability function for the claim-count variable  $N$  for a single policy selected at random from this population.
- (b) Check the goodness of fit of the resulting distribution with a chi-square test.

| # Claims | # Policies |
|----------|------------|
| 0        | 5,220      |
| 1        | 722        |
| 2        | 52         |
| 3        | 4          |
| 4        | 2          |
| $\geq 5$ | 0          |
| Total    | 6,000      |

- 3.10** Derive these formulas for the moments of a random variable  $N$  with a mixed-Poisson distribution directly from probability function (3.12), thus verifying (3.14) and (3.15).  
 (a)  $E[N^2] = E[\lambda] + E[\lambda^2]$ .      (b)  $E[N^3] = E[\lambda] + 3E[\lambda^2] + E[\lambda^3]$ .  
 (c)  $E[(N - E[N])^3] = E[\lambda] + 3\text{Var}[\lambda] + E[(\lambda - E[\lambda])^3]$ .
- 3.11** Assume that  $N$  has a mixed-Poisson distribution for which the mixing parameter  $\lambda$  has a gamma distribution with  $(\alpha, \beta) = (2, 1)$ . Compute:  
 (a)  $E[N]$ .      (b)  $\text{Var}[N]$ .      (c)  $\Pr\{N \leq 3\}$ .
- 3.12**  $N$  is the claim-count variable for a policy selected at random from a population characterized by a mixture of Poisson distributions for which  $\lambda$  has a gamma distribution with  $E[\lambda] = 0.100$  and  $\text{Var}[\lambda] = 0.005$ . Compute  $f_N(n)$  for  $n = 0, 1, 2, 3$ .
- 3.13** Random variable  $N_1$  is Poisson-distributed with  $\lambda = 0.75$ , variable  $N_2$  has a mixed-Poisson distribution with  $\Pr\{\lambda = 0.6\} = 0.75$  and  $\Pr\{\lambda = 1.2\} = 0.25$ , and variable  $N_3$  has a mixed distribution for which  $f_\lambda(u) = \frac{4}{3}e^{-(4/3)u}$ .  
 (a) Show that  $E[N_1] = E[N_2] = E[N_3]$ .  
 (b) Compute  $\text{Var}[N_1]$ ,  $\text{Var}[N_2]$ , and  $\text{Var}[N_3]$ .  
 (c) Compute  $f_{N_i}(n)$  for  $i = 1, 2, 3$  and  $n = 0, 1, 2, 3, 4, 5$ .
- 3.14** To the data of Example 3.6 fit a mixed Poisson distribution of the form

$$f(n) = \frac{1}{n!} (\omega_1 \lambda_1^n e^{-\lambda_1} + \omega_2 \lambda_2^n e^{-\lambda_2}), \quad \omega_1 + \omega_2 = 1.$$

- (a) Compute method-of-moments parameter estimates  $\hat{\lambda}_1, \hat{\lambda}_2, \hat{\omega}_1, \hat{\omega}_2$ .  
 (b) Compare the fit of the resulting distribution to that of the negative binomial distribution obtained in Example 3.6.

- 3.15** The table displays the incidence of claims from a portfolio of 10,000 annual policies. Fit a reasonable distribution model to these data. What assumptions must one make? Test the goodness of fit of the fitted distribution.

| # Claims | # Policies |
|----------|------------|
| 0        | 8,956      |
| 1        | 907        |
| 2        | 120        |
| 3        | 15         |
| 4        | 2          |
| $\geq 5$ | 0          |
| Total    | 10,000     |

- 3.16** Prove identity (3.22) for the general binomial coefficient.

- 3.17** Prove this identity:  $\prod_{i=1}^{n-1} (x+i) = \Gamma(x+n)/\Gamma(x)$ ,  $n = 2, 3, 4, \dots$

- 3.18** Derive these formulas for the mean and variance of a random variable  $N$  with the general negative binomial probability function (3.19).

(a)  $E[N] = r(1-q)/q$ .      (b)  $\text{Var}[N] = r(1-q)/q^2$ .

- 3.19** Show that the negative binomial probability function (3.19) satisfies a recursion relation of the following form: there exist numbers  $a > 0$  and  $b > 0$  such that

$$f(n) = \frac{na + b}{n} f(n-1), \quad n = 1, 2, 3, \dots$$

- 3.20** Explain how the negative binomial probability function (3.19), whenever parameter  $r$  has a positive integer value, can be interpreted as  $\Pr\{M = n\}$ , where  $M$  is the number of failures occurring before the  $r^{\text{th}}$  success in a sequence of independent Bernoulli trials for which  $q$  is the probability of success in a single trial. The negative binomial distribution for which parameter  $r$  is a positive integer is sometimes called the **Pascal distribution**, after French mathematician and philosopher Blaise Pascal (1623–1662).<sup>37</sup>

- 3.21** A random variable  $N$  with probability mass function

$$f(n) = p(1-p)^n, \quad 0 < p < 1, \quad n = 0, 1, 2, \dots$$

has a **geometric distribution** with parameter  $p$ .

- (a) Show that the geometric distribution is a special case of the Pascal distribution.  
 (b) Compute  $E[N]$  and  $Var[N]$  in terms of  $p$ .

- 3.22** A claim-count variable  $N$  is obtained as a mixture of geometric variables. Derive a formula for the probability function  $f_N(n)$  under each of the following assumptions about the distribution of the variable parameter  $p$ .

- (a)  $p$  is uniformly distributed on the interval  $0 < u < 1$ .  
 (b)  $p$  is distributed on the interval  $0.10 < u < 1$  with  $f_p(u) = 1/(u \log 10)$ .

- 3.23** (a) Verify that the moment-generating function  $M_\lambda(t)$  for the mixing parameter  $\lambda$  with the gamma probability density function (3.16) is

$$M_\lambda(t) = ((\alpha - vt)/\alpha)^{-\alpha}.$$

- (b) Show that the moment-generating function  $M_N(t)$  for the mixed distribution (3.17) satisfies the equation  $M_N(t) = M_\lambda(e^t - 1)$ , where  $M_\lambda(t)$  is the generating function of part (a).  
 (c) Prove that the relation  $M_N(t) = M_\lambda(e^t - 1)$  holds for an arbitrary (not just gamma) distribution for the variable parameter  $\lambda$ .

<sup>37</sup> Pascal and fellow French mathematician Pierre de Fermat (1601–1665) are credited with establishing the mathematical foundations of probability. In a remarkable correspondence during the summer of 1654 they solved a celebrated problem from the realm of gambling: how should the stakes in a game of chance be divided between two equally skilled players when the game is interrupted? Pascal's easily generalized solution made use of the array of binomial coefficients that has since become known as Pascal's Triangle.

- 3.24** Let  $\langle n_1, n_2, \dots, n_m \rangle$  be observations of a random sample of size  $m$  drawn from a population with a negative binomial distribution (3.17) with unknown parameters  $(\alpha, \nu)$ . Find formulas for the method-of-moments parameter estimates  $(\hat{\alpha}, \hat{\nu})$ .
- 3.25** For the Pólya distribution of Example 3.7, compute:
- (a)  $\Pr\{\text{white on 3rd trial} \mid \text{white on 1st \& black on 2nd trial}\}$ .
  - (b)  $\Pr\{\text{white on 3rd trial} \mid \text{black on 1st \& white on 2nd trial}\}$ .
  - (c)  $\Pr\{\text{white on 3rd trial}\}$ .
- 3.26** The number  $W_m$  of white balls drawn from an urn in  $m$  Pólya trials has probability function  $P_n(100, 25, 5; m)$ ,  $n = 0, 1, 2, \dots, m$ .
- (a) What is the degree of contagion?
  - (b) Compute these probabilities:  
 $\Pr\{\text{white on 1st trial}\}$ ,  
 $\Pr\{\text{white on 2nd trial} \mid \text{white on 1st trial}\}$ ,  
 $\Pr\{\text{white on 2nd trial} \mid \text{black on 1st trial}\}$ ,  
 $\Pr\{\text{white on 2nd trial}\}$ .
  - (c) Compute the probabilities  $P_n(100, 25, 5; 4)$  for  $n = 0, 1, 2, 3, 4$ .
  - (d) What is the limiting distribution of  $W_m$  as  $m \rightarrow \infty$  such that  $mp = 3.2$  and the degree of contagion remain constant?
- 3.27** (a) Demonstrate that the Pólya probability function (3.26) can be expressed in terms of the general binomial coefficients as

$$P_n(w, b, c; m) = \binom{\frac{1}{\gamma} + n - 1}{n} \binom{\frac{1-p}{\gamma p} + m - n - 1}{m-n} \bigg/ \binom{\frac{1}{\gamma p} + m - 1}{m},$$

where  $p = w/(w + b)$  and  $\gamma = c/w$ .

- (b) Show that the denominator in part (a) can be written as

$$\binom{\frac{1}{\gamma p} + m - 1}{m} = \binom{\frac{1}{\gamma p} + m - n - 1}{m-n} \prod_{i=1}^n \left( \frac{1}{\gamma p m} + \frac{m-i}{m} \right) \bigg/ \prod_{i=1}^n \left( 1 - \frac{i-1}{m} \right).$$

- 3.28**  $N$  has a negative binomial distribution with mean 1.00 and contagion parameter  $\gamma = 0.20$ . Compute the probabilities of  $N = 0, 1, 2, 3, 4, 5$  claims.
- 3.29** (a) Three independent claim-count variables  $(N_1, N_2, N_3)$  have respective means  $(10, 25, 5)$  and contagion parameters  $(0.35, 0.20, 0)$ . Compute the contagion parameter for  $N = N_1 + N_2 + N_3$ .
- (b) Let  $N$  be the sum of  $m$  independent claim-count random variables with means  $\{\nu_i\}$  and contagion parameters  $\{\gamma_i\}$ . Prove that the contagion parameter for  $N$  is

$$\gamma = \sum_{i=1}^m \gamma_i \nu_i^2 / \left( \sum_{i=1}^m \nu_i \right)^2.$$

- 3.30** A policyholder owns a fleet of 20 insured automobiles. The claim process for each vehicle is Poisson-distributed with claim density of 0.30 per year. Assuming that the individual claim processes are independent, find the probability of incurring at least six auto claims in a single year.
- 3.31** The claim-count variable for a portfolio of 8,000 policies is Poisson-distributed with an expected value of 650 claims. Assuming also that the claim-count variable for each policy has the same Poisson distribution, compute the expected number of policyholders that produce at least one claim.
- 3.32** In a portfolio of  $m$  identical policies, the claim count for every policy has the same negative binomial distribution with contagion parameter  $\gamma$ . If  $\gamma_m$  is the contagion parameter of the portfolio distribution, find  $\lim_{m \rightarrow \infty} \gamma_m$ . What does this imply about the nature of the portfolio distribution for large  $m$ ?
- 3.33** The random time of occurrence—or *waiting time*—for successive claims in a claim process is occasionally of interest. In the case that the process is Poisson, the distribution of the random variable  $T_n$ , the occurrence time of the  $n^{\text{th}}$  claim, has a particularly simple form.

Note that  $T_n \leq t$  is identical to the event that at least  $n$  claims occur in the time interval  $[0, t]$ . Thus, when the claim process is Poisson with parameter  $\lambda = \# \text{ claims per unit time}$ , probability formula (3.4) implies that the distribution function for  $T_n$  is

$$F_n(t) = \Pr\{T_n \leq t\} = \begin{cases} 0 & \text{if } -\infty < t < 0 \\ \sum_{k=n}^{\infty} \frac{(\lambda t)^k e^{-\lambda t}}{k!} & \text{if } 0 \leq t < \infty. \end{cases}$$

- (a) Show that  $T_n$  has the gamma probability density function

$$f_n(t) = \frac{\lambda^n}{(n-1)!} t^{n-1} e^{-\lambda t}.$$

- (b) Obtain  $E[T_n]$  and  $Var[T_n]$  in terms of  $n$  and  $\lambda$ .
- (c) Let  $\hat{T}_n$  denote the time between successive claims:

$$\hat{T}_n = \begin{cases} T_1 & \text{if } n = 1 \\ T_n - T_{n-1} & \text{if } n \geq 2. \end{cases}$$

Show that variables  $\hat{T}_n$  are independent and that each has an exponential distribution with parameter  $\beta = 1/\lambda$ .

- 3.34** The claim-count variable for a property policy with a two-year term has a Poisson distribution with 0.215 claims per year.
- (a) What is the expected time until the occurrence of the first claim?
  - (b) What is the probability that the first claim will occur within the first year? . . . the second year?
  - (c) What is the probability that the second claim will occur within the first year? . . . the second year?
- 3.35** For a certain claim process the claim-count variable  $N$  has a Poisson distribution with parameter  $\lambda$ , and the probability that any given claim is fraudulent is  $p$ . Find the distribution of  $N^* = \# \text{ fraudulent claims}$ . [Hint: for  $n = 1, 2, 3, \dots$

$$\begin{aligned}
 f_{N^*}(n) &= \sum_{k=n}^{\infty} \Pr\{n \text{ fraudulent claims} | N = k\} \cdot f_N(k) \\
 &= \sum_{k=n}^{\infty} \binom{k}{n} p^n (1-p)^{k-n} f_N(k). ]
 \end{aligned}$$

