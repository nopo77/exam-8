---
paper: bahnemann
chapter: 6
title: 6. Limits and Deductibles
topics: [pure_premium, claim_frequency, claim_severity, policy_deductibles, loss_cost_multipliers, exposure_rating, aggregate_policy_limits]
key_formulas: [pure_premium_formula, rate_per_unit_exposure, loss_cost_multiplier, straight_deductible_factor, aggregate_limit_factor]
---

> **TL;DR**
> - **Pure premium** p=φ·E[Y] (frequency×severity); **rate per unit exposure** R=(p+f)/(1−v); policy premium P=mR where m = exposure units
> - **Straight deductible d**: insurer pays max(0, X−d); loss cost multiplier LCM=(E[X;l]−E[X;d])/E[X;b] adjusts base rate; also reduces claim frequency by factor (1−F_X(d))
> - **Franchise deductible d**: insurer pays full X when X>d (not X−d); higher indemnity per excess claim than straight deductible
> - **Per-occurrence limit l with deductible d**: expected indemnity = E[X;d+l]−E[X;d]; ILF from basic limit b to limit l is ratio of these expressions
> - **Aggregate limits** (stop-loss): apply compound distribution or recursion to determine expected aggregate excess payment above an aggregate retention

# 6. Limits and Deductibles

In this chapter we explore some common applications of the claim-count, claim-size, and aggregate-loss distributions in property/casualty insurance. In particular, we investigate the pricing of policies with various coverage limitations such as deductible options, and per-claim and aggregate limits with a variety of properties. We begin by reviewing some basic premium concepts and how they relate to distributional theory.

## 6.1. Premium Concepts

Every insurance policy has an associated loss process described jointly by a claim-count random variable  $N$  and a claim-size variable  $Y$ . In the following discussion  $Y$  represents the entire claim amount: the indemnity payment plus loss adjustment expense allocated to the claim, as limited by policy conditions. Allocated loss adjustment expenses (ALAE) are those incurred during the settlement process for an individual claim: attorneys' fees, investigation expense, expert witness fees, and the like. (Unallocated loss adjustment expenses, such as claim department overhead, are usually treated as general expenses and are not included in the policy aggregate loss.) The expected loss for the policy is then  $E[N]E[Y]$ , the mean of the policy aggregate loss distribution. Premium charged for such a policy is based on this expected loss, loaded for general expenses, underwriting profit, and a charge for risk.

The mean  $E[N]$  of the claim-count variable represents the expected number of claims per policy. In most situations, the expected claim count is seen to depend on an **exposure unit** associated with the policy coverage. The exposure unit is usually chosen to have certain desirable characteristics: (i) it should be a meaningful indicator of the policy's expected number of claims—the more exposure units covered by the policy the greater the expected number of claims, and (ii) one should be able to determine an expected number of claims—constant over at least a moderate period of time—associated with a single exposure unit.

For example, a single auto is the customary exposure unit for an auto liability policy with a term of one year. For such a policy the expected number of policy claims  $E[N]$  is obtained by multiplying the number of autos covered by the policy for a year, referred to as the number of **vehicle years**, and the expected number of claims per auto per year—that is, the number of claims per vehicle year. Other common measures of exposure include dollars of annual payroll for workers' compensation policies, the number of objects manufactured in a year or dollars of annual sales for product liability coverages, and building area measured in square feet for premises liability coverages.

The expected number of claims per unit exposure is called the **claim frequency**. If  $m$  denotes the number of exposure units and  $\phi$  the claim frequency, then obviously

$$m\phi = E[N]. \quad (6.1)$$

In addition, the **claim severity** is the average claim size  $E[Y]$  for the policy. The product of frequency and severity, denoted by  $p$ , is called the **pure premium**:

$$p = \text{pure premium} = (\text{frequency})(\text{severity}) = \phi E[Y]. \quad (6.2)$$

It is clear that the pure premium represents the *expected aggregate claim amount per unit of exposure*. Accordingly, exposure times pure premium yields the policy expected loss:

$$mp = m(\phi E[Y]) = E[N]E[Y]. \quad (6.3)$$

In the case that a policy involves more than a single line of business—each with its own exposure, frequency, and severity—then the policy expected loss is obtained by summing over all component coverages the corresponding products of exposure, frequency, and severity.

**Example 6.1.** For a certain general liability coverage the exposure unit is \$1,000 of annual sales, the claim frequency is 0.000825 claims per \$1,000 sales per year, and the claim severity is \$5,200.

An insured has \$650,000 of sales revenue per year. Consequently, the number exposure units for an annual policy is

$$m = \frac{\$650,000}{\$1,000} = 650,$$

the pure premium is  $p = (0.000825)(5,200) = 4.29$ , and the expected loss for the policy is  $mp = (650)(4.29) = 2,789$ . ■

To calculate the policy premium one must first load the pure premium amount with a provision for general expenses, underwriting profit, and risk. **General expenses** include acquisition expense—commission paid to agents and brokers—salaries and overhead, taxes and fees, and other costs of doing business. **Underwriting profit** is the expected excess of premium over paid losses and expenses. (In some lines of business the underwriting profit could be zero, or even negative, in anticipation of an offset from investment income.) The **risk charge** is extra premium collected by the insurer to cover such contingencies as (i) random fluctuations of losses about the expected values and (ii) uncertainty inherent in the selection of critical parameters used in modeling the underlying loss process. Insurer risk from the first source is called **process risk** and that from the second, **parameter risk**.

Provisions for expense, profit, and risk can be treated either as variable—loaded as a percent of the final premium amount—or as fixed—added as a dollar amount per unit of exposure to the pure premium. Agent and broker commission is generally a variable expense, whereas the overhead cost of issuing a policy could be loaded as a fixed expense.

If variable expenses, plus the load for profit and risk, constitute the fraction  $v$  of the total policy premium,<sup>51</sup> and fixed expenses are  $f$  dollars per unit exposure, then the modified pure premium

$$R = \frac{p + f}{1 - v} \quad (6.4)$$

is the **rate per unit exposure**. The number of exposure units  $m$  times the rate  $R$  yields the final policy premium  $P$ :

$$P = mR = \frac{m(p + f)}{1 - v} = \frac{E[N]E[Y] + mf}{1 - v}. \quad (6.5)$$

In the case that  $f = 0$ —that is, all expense amounts are assumed to be variable and expressed by the expense ratio  $v$ —the factor

$$\psi = \frac{1}{1 - v} \quad (6.6)$$

is called a **loss-cost multiplier**. Rate formula (6.4) then reduces to the simpler form  $R = \psi p$ , and the premium formula becomes

$$P = mR = m(\psi p) = \psi E[N]E[Y]. \quad (6.7)$$

In subsequent sections we shall generally assume that expenses are loaded by means of a loss-cost multiplier  $\psi$ , as in (6.7).

**Example 6.2.** A business owner wishes to buy annual insurance coverage for general liability and auto liability for a business operation that involves premises of 20,000 square feet and four automobiles. General and auto liability premiums are rated separately, as indicated below.

For the general liability coverage the insurer has determined a claim frequency of 0.004 per 1,000 square feet per year and a claim severity of 6,500. The general liability pure premium is therefore  $p = (0.004)(6,500) = 26.00$ . Variable expenses plus profit load amount to 30% of the premium; fixed expenses are 4.10 per exposure unit. Therefore, the general liability annual rate is

$$R_{GL} = \frac{26.00 + 4.10}{1 - 0.30} = 43.00 \text{ per 1,000 square feet.}$$

For the auto coverage the claim frequency is 0.052 per vehicle year, with a claim severity of 2,800 and fixed expense of 9.80 per vehicle year, and so the auto liability rate is

$$R_{AL} = \frac{(0.052)(2,800) + 9.80}{1 - 0.30} = 222.00 \text{ per vehicle year.}$$

---

<sup>51</sup> As we shall see in Section 6.3, the risk load is often calculated as an amount that varies with the policy limit, as well as one that varies with premium.

Annual liability premium  $P$  is obtained by multiplying the number of exposure units and the rate for each coverage and summing the results:

$$P = \frac{20,000}{1,000} R_{GL} + 4R_{AL} = (20)(43) + (4)(222) = \$1,748. \blacksquare$$

## 6.2. Increased Limit Factors

The premium for many property/casualty policies is calculated first for a basic per-claim policy limit, and then this basic-limit premium is multiplied by an appropriate **increased limit factor** (ILF) to determine the full policy premium. A set of increased limit factors—one for each of the available policy limit options—can be obtained from an empirical loss distribution based on loss data organized around the required policy per-claim limits, or it can be derived from an appropriate parametric size-of-loss distribution. Such an analytic distribution fit to empirical sample data is often useful for obtaining factors for those higher limits for which data are either sparse or nonexistent.

Let  $P_b$  denote the policy premium at the basic per-claim limit  $b$  and  $P_l$  the premium at a policy per-claim limit  $l$ . Then the increased limit factor  $I(l)$  is defined by

$$I(l) = \frac{P_l}{P_b}, \quad (6.8)$$

so that  $P_l = P_b \cdot I(l)$ . Note also that if the policy premium is based on formula (6.7), then  $p_l = p_b \cdot I(l)$ , where  $p_l$  is the pure premium associated with the limit  $l$ .

In the discussion that follows,  $E_l[Y]$  is the policy severity, including both indemnity payment and allocated loss adjustment expense, appropriately modified by the policy limit  $l$ . When expenses are loaded by means of a loss-cost multiplier  $\psi$ , ILF formula (6.8) becomes

$$I(l) = \frac{P_l}{P_b} = \frac{\psi E[N] E_l[Y]}{\psi E[N] E_b[Y]} = \frac{E_l[Y]}{E_b[Y]}. \quad (6.9)$$

The specific form of  $E_l[Y]$  depends on whether policy conditions stipulate that limit  $l$  applies to the full claim amount, including both indemnity and allocated loss adjustment expense portions of a claim, or whether it applies only to the indemnity payment.

Consider first the case that policy limit  $l$  applies to the total claim amount: indemnity loss plus loss adjustment expense. If  $X_i$  denotes the ground-up, unlimited total claim-size random variable, then the policy severity is  $E_l[Y] = E[X_i; l]$ . In these circumstances ILF formula (6.9) can be expressed as

$$I(l) = \frac{E[X_i; l]}{E[X_i; b]}. \quad (6.10)$$

On the other hand, suppose that the limit  $l$  applies only to the indemnity portion of the claim, as is usually the case. If random variable  $X$  denotes just the indemnity component of the claim, then one could write

$$E_l[Y] = E[X; l] + \epsilon, \quad (6.11)$$

where  $\epsilon$  is the average per-claim allocated loss adjustment expense, independent of the policy limit. In this case (6.9) has the form

$$I(l) = \frac{E[X; l] + \epsilon}{E[X; b] + \epsilon}. \quad (6.12)$$

Provision for loss adjustment expense in formula (6.11) is an overall average amount  $\epsilon$  added to every claim, regardless of size. Amount  $\epsilon$  can thus be interpreted as the mean of a loss adjustment expense random variable, but in (6.11) it is unnecessary to know exactly how that variable is distributed.

As an alternative to this approach, it is sometimes useful to assume that loss adjustment expense bears some functional relationship to the size of the indemnity payment. One simple scheme is to assume that loss adjustment expense is a fixed multiple  $u$  of the indemnity amount. This assumption can be approximately true provided that the indemnity payment is not too large. (An alternative, hybrid method of expense loading is described in Problem 6.6.) Again, assuming that the policy limit applies only to the indemnity portion of the claim, one can write

$$E_l[Y] = E[X; l] + uE[X; l] = E[X; l](1 + u). \quad (6.13)$$

Then ILF formula (6.9) becomes

$$I(l) = \frac{E[X; l](1 + u)}{E[X; b](1 + u)} = \frac{E[X; l]}{E[X; b]}. \quad (6.14)$$

The three approaches to loss adjustment expense incorporated into formulas (6.12), (6.13), and (6.14) can be combined into a single general formula for the policy severity:

$$E_l[Y] = (E[X; l] + \epsilon)(1 + u). \quad (6.15)$$

In case that limit  $l$  applies to indemnity loss plus loss adjustment expense, set  $X = X$ , and  $\epsilon = u = 0$  in (6.15). Otherwise, when the limit applies only to the indemnity payment, let variable  $X$  represent the indemnity-only portion of a claim and set either  $\epsilon = 0$  or  $u = 0$ , as desired.

The Insurance Services Office (ISO) increased limits methodology treats allocated loss adjustment expense additively like the constant  $\epsilon$  in formula (6.15) and loads unallocated adjustment expense multiplicatively like the factor  $1 + u$  in that formula.<sup>52</sup>

<sup>52</sup> For an extended discussion of the ISO method, refer to a current ISO Actuarial Service Circular for increased limits data and analysis for General and/or Commercial Auto Liability (Jersey City, NJ: Insurance Services Office, Inc.).

**Table 6.1. Increased Limit Factors [Example 6.3]**

| Limit /<br>(\$000) | $E[X; I]$ | $I(I)$<br>ALAE = 2,200 | $I(I)$<br>ALAE = 20% |
|--------------------|-----------|------------------------|----------------------|
| 100                | 8,896     | 1.0000                 | 1.0000               |
| 500                | 13,626    | 1.4263                 | 1.5317               |
| 750                | 14,668    | 1.5202                 | 1.6488               |
| 1,000              | 15,345    | 1.5812                 | 1.7249               |
| 2,000              | 16,738    | 1.7067                 | 1.8815               |
| 3,000              | 17,390    | 1.7655                 | 1.9548               |
| 4,000              | 17,782    | 1.8008                 | 1.9989               |
| 5,000              | 18,048    | 1.8248                 | 2.0288               |

**Example 6.3.** Indemnity losses for a portfolio of insurance policies have a lognormal claim-size distribution with parameters  $(\mu, \sigma) = (7.000, 2.400)$ . The policy per-claim limit applies only to the indemnity portion of a claim, and the average per-claim loss adjustment expense is 2,200. Claim frequency for these policies is  $\phi = 0.0005$  per exposure unit, and variable expenses equal 35% of premium.

A set of increased limits factors based on (6.15) with  $b = 100,000$ ,  $\varepsilon = 2,200$ , and  $u = 0$  is shown in the third column of Table 6.1. For example,

$$I(1,000K) = \frac{15,345 + 2,200}{8,896 + 2,200} = 1.5812.$$

For a policy with 400 exposure units, so that  $E[N] = (400)(0.0005) = 0.2000$ , the basic-limit premium is

$$P_{100K} = \frac{(0.2000)(8,896 + 2,200)}{1 - 0.35} = \$3,414.$$

The corresponding premium for a policy limit of 1,000,000 is therefore

$$P_{1,000K} = P_{100K} \cdot I(1,000K) = (3,414)(1.5812) = \$5,398.$$

Alternatively, if the loss adjustment expense is treated as 20% of the indemnity portion of the claim, then the resulting increased limit factors are displayed in the fourth column of Table 6.1. For example, in this case

$$I(1,000K) = \frac{(15,345)(1.20)}{(8,896)(1.20)} = 1.7249.$$

For the policy with 400 exposure units the basic-limit premium is

$$P_{100K} = \frac{(0.2000)(8,896)(1.20)}{1 - 0.35} = \$3,285,$$

and with a 1,000,000 limit,

$$P_{1,000K} = (3,285)(1.7249) = \$5,666. \blacksquare$$

### Excess Layer Pricing

Increased limit factors can also be applied to price an excess layer of coverage, defined by a policy limit  $l$  and attachment point  $a$  ( $l > 0$ ,  $a > 0$ ), as discussed in Section 5.3. If  $\phi$  and  $E_{a,l}[Y]$  denote, respectively, the ground-up claim frequency and the severity for the policy layer ( $a$ ,  $a + l$ ), then the layer pure premium is

$$p_{a,l} = \phi (1 - F_{X_t}(a)) E_{a,l}[Y],$$

where  $X_t$  is the total ground-up claim amount. In the case that  $X_t$  is subject to the layer limits we rearrange the pure premium formula as follows:

$$\begin{aligned} p_{a,l} &= \phi (1 - F_{X_t}(a)) \frac{E[X_t; a + l] - E[X_t; a]}{1 - F_{X_t}(a)} \\ &= \phi (E[X_t; a + l] - E[X_t; a]) \\ &= \phi E[X_t; b] \left( \frac{E[X_t; a + l]}{E[X_t; b]} - \frac{E[X_t; a]}{E[X_t; b]} \right). \end{aligned} \quad (6.16)$$

In this special case, a layer factor, applied to the basic-limit pure premium to calculate the pure premium for the excess layer, is just the difference of two ground-up increased limit factors of the form (6.9), namely,

$$p_{a,l} = p_b \cdot (I(a + l) - I(a)).$$

Since  $P_{a,l} = m(\psi p_{a,l}) = m(\psi p_b) (I(a + l) - I(a))$ , premium for the excess layer ( $a$ ,  $a + l$ ) can be calculated by using the **layer formula** for policy premium  $P$ :

$$P = P_b \cdot (I(a + l) - I(a)). \quad (6.17)$$

The simplicity of this basic formula makes it very easy to apply. Because of this, it is widely used in increased limits pricing, even in situations where it is not strictly appropriate. For example, suppose that the layer limits  $l$  and  $a$  apply only to the indemnity portion of a claim and ALAE is added as in formula (6.11). Then the excess-layer premium based on that model would be

$$\begin{aligned} P_{a,l} &= \psi E[N] (1 - F_X(a)) \left( \frac{E[X; a + l] - E[X; a]}{1 - F_X(a)} + \varepsilon \right) \\ &= \psi E[N] (E[X; a + l] - E[X; a] + (1 - F_X(a)) \varepsilon). \end{aligned} \quad (6.18)$$

On the other hand, the layer formula for  $P$  yields

$$\begin{aligned} P &= \psi E[N](E[X; b] + \varepsilon) \left( \frac{E[X; a + l] + \varepsilon}{E[X; b] + \varepsilon} - \frac{E[X; a] + \varepsilon}{E[X; b] + \varepsilon} \right) \\ &= \psi E[N](E[X; a + l] - E[X; a]). \end{aligned} \quad (6.19)$$

Notice that  $P = P_{a,l}$  and that the load for loss adjustment expense has dropped out of the premium calculation in (6.19) entirely. In the situation where such an excess policy is written over a primary policy providing first-dollar coverage for the primary layer  $[0, a]$ , this state of affairs is consistent with the assumption that allocated loss adjustment expense is paid in its entirety by the primary insurer.

On the other hand, if loss adjustment expense is loaded by means of the factor  $1 + u$ , then

$$P_{a,l} = \psi E[N](E[X; a + l] - E[X; a])(1 + u),$$

where the provision for ALAE in the excess premium is

$$ALAE = \psi E[N](E[X; a + l] - E[X; a]) u.$$

The layer formula for  $P$  yields the premium amount

$$\begin{aligned} P &= \psi E[N] E[X; b] (1 + u) \left( \frac{E[X; a + l]}{E[X; b]} - \frac{E[X; a]}{E[X; b]} \right) \\ &= \psi E[N](E[X; a + l] - E[X; a])(1 + u). \end{aligned} \quad (6.20)$$

In this case, for which the ALAE multiplier  $u$  is the same for both primary and excess policies, the basic layer formula preserves the loss adjustment expense loading exactly and  $P = P_{a,l}$ .

**Example 6.4.** We return to the portfolio of policies described in Example 6.3 and calculate the premium for successive excess layers of insurance for a policy with  $m = 400$ . We use the ILFs constructed in that example under the assumption that the average per-claim ALAE payment is  $\varepsilon = \$2,200$ .

The basic limit premium was calculated in the previous example to be \$3,414. Thus, premium  $P$  for the layer  $(1,000,000; 2,000,000]$  given by the layer formula (6.17) is

$$P = (3,414)(1.7067 - 1.5812) = (3,414)(0.1255) = \$428.$$

Similarly, for the layer  $(2,000,000; 3,000,000]$ , we obtain

$$P = (3,414)(1.7655 - 1.7067) = (3,414)(0.0588) = \$201.$$

Premium amounts for the successive million-dollar layers obtained from these layer factors applied to the basic-limit premium are displayed in Table 6.2. ■

**Table 6.2. Layer Premium [Example 6.4]**

| Layer (\$000)  | Layer Factor | Premium |
|----------------|--------------|---------|
| [0; 100]       | 1.0000       | 3,414   |
| [0; 1,000]     | 1.5812       | 5,398   |
| (1,000; 2,000] | 0.1255       | 428     |
| (2,000; 3,000] | 0.0588       | 201     |
| (3,000; 4,000] | 0.0353       | 121     |
| (4,000; 5,000] | 0.0240       | 82      |

### Consistency

The premiums calculated in Example 6.4 illustrate an important and desirable characteristic of excess layer pricing—premium amounts for successively higher layers of constant width decrease as the attachment point becomes larger. In that example, premium for the ground-up million-dollar layer is \$5,398, and for successively higher layers of one-million-dollar width the calculated premium steadily declines with increasing attachment point: \$428, \$201, \$121, \$82. As we shall see, this is a property common to all pricing methods based on expected losses and reasonable distributions for the claim-size random variables.

Consider a set of increased limit factors based on the general severity formula (6.15). If the claim-size variable  $X$  has a continuous probability density function  $f_X(x) = F'_X(x) > 0$ , then the ILF function  $I(x)$  is twice differentiable with respect to the limit  $x$  (refer to Problem 2.9). Specifically, for all  $x > 0$

$$I'(x) = \frac{(1+u)(1-F_X(x))}{E[X; b] + \varepsilon} \quad \text{and} \quad I''(x) = \frac{-(1+u)f_X(x)}{E[X; b] + \varepsilon} < 0.$$

A set of increased limit factors for which  $I''(x) < 0$  for all limits  $x$  is said to be **consistent**. Thus, every set of increased limit factors based on severity formula (6.15) for which the claim-size density function is positive and continuous is always consistent.

Consistent sets of increased limit factors share a common property: the premium  $P$  calculated from the layer formula (6.17) applied to successive excess layers of *constant width* is a decreasing function of the attachment point limit. It is easy to verify this assertion in the case that the claim-size variable has a continuous probability density function. Assume that in the formula

$$P = P_b \cdot (I(x+l) - I(x))$$

the attachment point  $x$  is variable, whereas the layer width  $l$  is a fixed constant. Then the rate of change of premium  $P$  with respect to  $x$  is

$$\frac{dP}{dx} = P_b \left( \frac{d}{dx} I(x+l) - \frac{d}{dx} I(x) \right).$$

Consistency means that  $I'(x)$  is a decreasing function of  $x$ , so that

$$\frac{d}{dx} I(x+l) < \frac{d}{dx} I(x) \quad \text{and hence} \quad \frac{dP}{dx} < 0.$$

Therefore, for each fixed  $l$ , premium  $P$  for the layer  $(x, x+l]$  decreases as the attachment point  $x$  increases.

## 6.3. Risk Load

Increased limit factors based on expected-value concepts have generally been thought to be inadequate for pricing insurance policies with high limits or attachment points unless they were loaded with a charge for insurer risk. With lower claim probabilities for such policies, loss behavior associated with excess policies is more volatile and less predictable than that of primary policies with lower limits. Insurer risk due to such variability is process risk, in contrast to the parameter risk derived from estimation errors in selecting the claim-count and claim-size distributions. Process risk has long been understood by actuaries as a function of the variance of the basic stochastic claim process for a portfolio of policies or line of property/casualty insurance business.

In most approaches to risk-loaded increased limit factors, the risk load  $\rho(l)$  is usually defined as an increasing function of the policy limit  $l$ , which is added to the expected total policy severity for the policy. The severity formula (6.15) is thus modified

$$E_l[Y] + \rho(l) = (E[X; l] + \epsilon) + \rho(l), \quad (6.21)$$

and the resulting risk-loaded increased limit factors are

$$I(l) = \frac{(E[X; l] + \epsilon) + \rho(l)}{(E[X; b] + \epsilon) + \rho(b)}. \quad (6.22)$$

The merits of different methods of quantifying process risk for increased limit factors have been debated since the mid-1970s. Robert Miccolis<sup>53</sup> suggested in 1977 that process risk load be added to the policy expected aggregate loss as a constant multiple of the variance of the policy aggregate indemnity-loss random variable  $S$ :

$$\begin{aligned} & E[N]E[X; l] + k \text{Var}[S] \\ &= E[N] \left( E[X; l] + k \frac{E[N] \text{Var}[X; l] + \text{Var}[N](E[X; l])^2}{E[N]} \right). \end{aligned}$$

The multiplier  $k$  in this formula is selected arbitrarily to produce the desired level of risk loading. The risk load function  $\rho(l)$  in formula (6.21) is thus given by

$$\rho(l) = k \frac{\text{Var}[S]}{E[N]} = k (E[X^2; l] + \delta(E[X; l])^2), \quad (6.23)$$

<sup>53</sup> Miccolis [16].

where  $\delta = \text{Var}[N]/E[N] - 1$ . Setting  $\delta = 0$ , of course, is consistent with the assumption that  $N$  has a Poisson distribution. Note also that when  $\delta = 0$  the risk load  $\rho(l)$  is independent of the claim-count random variable and dependent only upon the claim-size variable. Such a variance-based approach to process risk load was adopted by ISO in the early 1980s.<sup>54</sup>

By mid-decade, however, ISO changed to a method based on the standard deviation of the policy aggregate indemnity-loss distribution:

$$\begin{aligned}\rho(l) &= k \frac{\sqrt{\text{Var}[S]}}{E[N]} \\ &= \frac{k}{\sqrt{E[N]}} \sqrt{E[X^2; l] + \delta(E[X; l])^2} \\ &= k' \sqrt{E[X^2; l] + \delta(E[X; l])^2},\end{aligned}\tag{6.24}$$

where  $\delta$  is defined as in the variance formula (6.23). ISO actuaries cited several reasons for this change. Risk-loaded factors based on (6.23) and (6.24) with thick-tailed Pareto distributions for  $X$  were sometimes inconsistent (for example, refer to Problem 6.10). Moreover, it seemed preferable to express the risk load as a dollar amount rather than in terms of (dollars)<sup>2</sup>. In 1991 ISO introduced a new risk-loading method that includes a measure of parameter risk as well as process risk. But this new method returned to the earlier variance approach to process risk.<sup>55</sup>

**Example 6.5.** We turn again to the portfolio of policies described in Example 6.3. Indemnity losses are distributed lognormally with parameters  $(\mu, \sigma) = (7.000, 2.400)$ , and allocated loss adjustment expense is 20% of the indemnity payment. We generate a set of risk-loaded increased limit factors by using formula (6.22) with  $\varepsilon = 0$  and  $u = 20\%$ . The risk load  $\rho(l)$  is obtained by the standard deviation method (6.24) with  $k' = 0.0277$  and  $\delta = 0$ . Thus,

$$\begin{aligned}\rho(100,000) &= (0.0277)\sqrt{512,509,058} = 627, \\ \rho(1,000,000) &= (0.0277)\sqrt{5,283,276,848} = 2,013,\end{aligned}$$

so that

$$I(1,000,000) = \frac{(15,345)(1.20) + 2,013}{(8,896)(1.20) + 627} = 1.8074.$$

Two sets of increased limit factors—risk-loaded and non-risk-loaded—are displayed in Table 6.3. The average increased limit factor in each column is obtained by using the indicated portfolio weights for the given set of limits. The ratio of these two averages

<sup>54</sup> Insurance Services Office [9].

<sup>55</sup> This approach is based on the paper by Glenn Meyers [15].

**Table 6.3. Risk-Loaded Increased Limit Factors [Example 6.5]**

| Limit $l$<br>(\$000) | $E[X; l]$<br>$\times 1.20$ | Risk<br>Load<br>$\rho(l)$ | $I(l)$<br>w/o Risk<br>Load | $I(l)$<br>w/ Risk<br>Load | Limit<br>Weight |
|----------------------|----------------------------|---------------------------|----------------------------|---------------------------|-----------------|
| 100                  | 10,675                     | 627                       | 1.0000                     | 1.0000                    | 15%             |
| 500                  | 16,351                     | 1,473                     | 1.5317                     | 1.5770                    | 10%             |
| 1,000                | 18,414                     | 2,013                     | 1.7249                     | 1.8074                    | 30%             |
| 2,000                | 20,086                     | 2,663                     | 1.8815                     | 2.0128                    | 20%             |
| 3,000                | 20,868                     | 3,090                     | 1.9548                     | 2.1197                    | 10%             |
| 4,000                | 21,338                     | 3,410                     | 1.9989                     | 2.1897                    | 10%             |
| 5,000                | 21,658                     | 3,668                     | 2.0288                     | 2.2407                    | 5%              |
| Average              |                            |                           | 1.6938                     | 1.7955                    |                 |

indicates an increase of  $1.7955/1.6938 - 1 = 6.0\%$ . This means that using the risk-loaded factors on a portfolio with this distribution of policy limits would generate 6% more premium than would be obtained by using the unloaded factors. ■

Unfortunately, both the variance and standard deviation approaches to risk load are incompatible with the layer formula (6.17) for pricing an excess layer. For example, if the risk load  $\rho_{a,l}$  for the excess layer  $(a, a + l]$  is defined as a multiple of the variance of the aggregate indemnity-loss variable  $S$  for the layer, then  $\rho_{a,l} \neq \rho(a + l) - \rho(a)$ , where  $\rho(l)$  is defined by (6.23).

To show this in a special case, we first calculate the layer risk load. For simplicity, assume that  $N$  is the ground-up claim-count variable with  $\delta = 0$  and that  $X$  is the ground-up claim-size variable. Then

$$\begin{aligned}\rho_{a,l} &= \frac{k \text{Var}[S]}{E[N]} \\ &= k(E[X^2; a + l] - E[X^2; a] - 2a(E[X; a + l] - E[X; a])).\end{aligned}$$

But this means that

$$\rho_{a,l} = \rho(a + l) - \rho(a) - 2ka(E[X; a + l] - E[X; a]) < \rho(a + l) - \rho(a).$$

That is, the risk load ascribed to the layer  $(a, a + l]$  by the basic layer formula, namely  $\rho(a + l) - \rho(a)$ , is larger than the risk load based on the actual variance of the layer aggregate-loss random variable.

Overstatement of the risk load remains a technical problem when one uses the basic layer formula with risk-loaded ILFs to price excess layers of insurance. Ideally, one should first determine the layer premium by applying the basic formula with non-risk-loaded factors and then add on the risk load for the layer. Such an approach,

probably too cumbersome to be widely adopted, is more frequently used by reinsurers providing excess-of-loss coverage.

## 6.4. Aggregate Limits

It is often the case with liability lines of insurance that policies are written not only with a per-claim limit but also with an **aggregate limit** as well. Whereas the per-claim limit is the maximum the insurance company would pay on a single claim, an aggregate limit is the maximum amount that would be paid during the policy term for all claims combined.

The policy expected loss under the restrictions imposed by a per-claim limit  $l$  and an aggregate limit  $L$  (where  $L > l$ ) is just the expected value  $E[S_l; L]$ , where  $S_l$  is the aggregate-loss random variable based on a claim-count variable  $N$  and a claim-size variable  $X$  limited at  $l$ . Thus, the unlimited aggregate mean is

$$E[S_l] = E[N]E[X; l]. \quad (6.25)$$

It is often more efficient and accurate to calculate the expected aggregate loss eliminated by the limit  $L$ —namely  $E[S_l] - E[S_l; L]$ —and subtract this amount from the unlimited mean (6.25) than it is to calculate  $E[S_l; L]$  directly. For example, if the (unlimited) aggregate distribution function  $F_S(s)$  has been approximated by one of the deterministic models discussed in Chapter 4, then expected excess loss  $E[S_l] - E[S_l; L]$  can be obtained from the integral formula

$$\begin{aligned} E[S_l] - E[S_l; L] &= \int_0^\infty s dF_S(s) - \int_0^L s dF_S(s) - L(1 - F_S(L)) \\ &= \int_L^\infty (s - L) dF_S(s). \end{aligned} \quad (6.26)$$

In practice, the improper integral in (6.26) is most easily evaluated by numerical integration techniques. When a deterministic approximation is not practicable, then an approximation to  $E[S_l; L]$  could be obtained by stochastic simulation.

Thus, when  $N$  is the claim-count variable,  $X$  is the unlimited indemnity-only claim-size variable, and allocated loss adjustment expense is loaded multiplicatively by the factor  $1 + u$ , the increased limit factor from the basic limit  $b$  with no aggregate limit to a per-claim limit  $l$  combined with an aggregate limit  $L$  is given by

$$I(l, L) = \frac{\psi E[S_l; L](1 + u)}{\psi E[N]E[X; b](1 + u)} = \frac{E[S_l; L]}{E[N]E[X; b]}. \quad (6.27)$$

The next example illustrates the use of formula (6.27).

**Example 6.6.** For a portfolio of liability policies the unlimited indemnity claim size distributed lognormally with  $(\mu, \sigma) = (7.600, 2.400)$ . Claim count  $N$  is distributed so that  $E[N] = 1.20$  with contagion parameter  $\gamma = 0.100$ . Allocated loss adjustment expense is assumed to be 20% of the indemnity payment.

At the basic limit of 500,000 with no aggregate limit the expected policy indemnity loss is

$$E[S_{0.5M}] = E[N]E[X; 500,000] = (1.20)(21,743) = 26,092.$$

With a per-claim limit of 2,000,000 the expected loss is

$$E[S_{2M}] = E[N]E[X; 2,000,000] = (1.20)(28,338) = 34,006.$$

Consider now the case for which the per-claim limit of 2,000,000 is accompanied by an aggregate limit of 3,000,000. In addition to the mean 34,006, the aggregate-loss variable  $S_{2M}$  has  $SD[S_{2M}] = 151,311$  and  $Sk[S_{2M}] = 9.4728$ . A numerical integration of  $\int_{3M}^{\infty} (s - 3,000,000) d\tilde{F}(s)$ , where  $\tilde{F}(s)$  is the shifted gamma approximation to  $F_{S_{2M}}(s)$ , yielded

$$E[S_{2M}] - E[S_{2M}; 3,000,000] = 91.$$

Thus,

$$E[S_{2M}; 3,000,000] = 34,006 - 91 = 33,915.$$

The ILF for the 2,000,000/3,000,000 limit combination is therefore

$$I(2M, 3M) = \frac{33,915}{26,092} = 1.2998.$$

Compare this result with the factor for the 2,000,000 per-claim limit with no aggregate limit:

$$I(2M) = \frac{34,006}{26,092} = 1.3033.$$

The expected policy aggregate losses for several combinations of per-claim and aggregate limits for this portfolio, as well as the increased limit factors calculated from them, are shown in Table 6.4. ■

## 6.5. Deductibles

The deductible is a coverage modification often used to decrease the policy claim count by eliminating small claims less than the deductible amount. It also serves possibly to encourage the policyholder to take steps to prevent or limit the occurrence of claims. We discuss in this section the standard straight deductible, as well as the less common franchise and diminishing deductible options.

By reducing the amount paid by the insurer for some or all claims, deductible provisions also serve to lower the premium charged for a policy. Deductible premium credits are easily calculated with the help of the claim-size limited pure premium and the loss elimination ratio concepts. In many cases, where there are sufficient data available, deductible credits can be calculated empirically. In other cases, analytic models involving parametric distributions are useful.

**Table 6.4. Expected Aggregate Loss and ILFs with Aggregate Limits [Example 6.6]**

| Per-Claim Limit | Aggregate Limit (\$000) |        |        |        |        |           |
|-----------------|-------------------------|--------|--------|--------|--------|-----------|
|                 | 1,000                   | 2,000  | 3,000  | 4,000  | 5,000  | Unlimited |
| 500,000         | 26,050                  | 26,092 | 26,092 | 26,092 | 26,092 | 26,092    |
| 1,000,000       | 29,702                  | 30,306 | 30,333 | 30,335 | 30,335 | 30,335    |
| 2,000,000       | —                       | 33,524 | 33,915 | 33,988 | 34,002 | 34,006    |
| 3,000,000       | —                       | —      | 35,421 | 35,696 | 35,781 | 35,821    |
| 4,000,000       | —                       | —      | —      | 36,604 | 36,808 | 36,949    |
| 5,000,000       | —                       | —      | —      | —      | 37,428 | 37,733    |
| 500,000         | 0.9984                  | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000    |
| 1,000,000       | 1.1384                  | 1.1615 | 1.1625 | 1.1626 | 1.1626 | 1.1626    |
| 2,000,000       | —                       | 1.2848 | 1.2998 | 1.3026 | 1.3032 | 1.3033    |
| 3,000,000       | —                       | —      | 1.3575 | 1.3681 | 1.3713 | 1.3729    |
| 4,000,000       | —                       | —      | —      | 1.4029 | 1.4107 | 1.4161    |
| 5,000,000       | —                       | —      | —      | —      | 1.4345 | 1.4462    |

### Straight Deductible

The *straight deductible* is the most common deductible coverage modification. It eliminates, from the standpoint of the insurer, all claims less than or equal to the deductible amount  $d$ , and it reduces the size of larger claims by  $d$ . If  $X$  represents the unmodified, ground-up claim-size variable, excluding allocated loss adjustment expense, then application of a straight deductible of size  $d$  yields a modified random variable, truncated from below and shifted by  $d$ :

$$X_d = X - d, \quad d < X < \infty. \quad (6.28)$$

Clearly, claims net of such a deductible are excess over an underlying limit  $d$ , as discussed in Section 5.1.

For all deductible options discussed in this section we shall assume that allocated loss adjustment expense is not included in the deductible or policy limit and that the policy severity is modeled by the general formula (6.15) with ALAE parameters  $\varepsilon$  and  $u$ . Thus, the basic-limit pure premium before application of the deductible is

$$p_b = \varphi(E[X; b] + \varepsilon)(1 + u), \quad (6.29)$$

where  $b$  is the basic limit and  $\varphi$  the claim frequency.

In practice, the basic-limit pure premium (6.29) is modified to reflect the presence of a deductible by applying a *deductible credit factor*  $C(d)$ :

$$p_{d,b} = p_b \cdot (1 - C(d)), \quad 0 < d < b. \quad (6.30)$$

Of course, this implies that the deductible-modified policy premium is obtained in the same way:

$$P_{d,b} = P_b \cdot (1 - C(d)). \quad (6.31)$$

The deductible premium credit amount is therefore  $P_b C(d)$ . Note also that the existence of the deductible reduces the basic limit policy layer width to  $b - d$ .

A formula for the deductible credit factor  $C(d)$  is easily derived by starting with the modified basic-limit pure premium, calculated from first principles as the product of the policy frequency and severity:

$$\begin{aligned} p_{d,b} &= \varphi(1 - F_X(d)) \left( \frac{E[X; b] - E[X; d]}{1 - F_X(d)} + \varepsilon \right) (1 + u) \\ &= \varphi(E[X; b] - E[X; d] + (1 - F_X(d))\varepsilon)(1 + u). \end{aligned} \quad (6.32)$$

Equating the two expressions for  $p_{d,b}$  in (6.30) and (6.32), we solve for  $C(d)$ :

$$C(d) = \frac{\varphi(E[X; d] + F_X(d)\varepsilon)(1 + u)}{p_b} = \frac{E[X; d] + F_X(d)\varepsilon}{E[X; b] + \varepsilon}. \quad (6.33)$$

The expression in (6.33) is merely the ratio of the pure premium eliminated by the deductible to that of the unmodified policy layer  $[0, b]$ . Accordingly, the ratio is referred to as a **loss elimination ratio**. The loss elimination ratio concept is useful in quantifying the effects of a variety of coverage modifications mandated by policy conditions.

Formula (6.31) yields the basic-limit premium modified by the straight deductible  $d$ , but how should the premium for a higher limit  $l$  be so adjusted? Recall that  $P_l = P_b \cdot I(l)$ , where  $I(l)$  is the increased limit factor for limit  $l$  with respect to the basic limit  $b$ , and that the premium credit amount for the existence of the deductible is  $P_b \cdot C(d)$ . Therefore,

$$P_{d,l} = P_l - P_b C(d) = P_b \cdot (I(l) - C(d)). \quad (6.34)$$

**Example 6.7** As in Example 6.3, consider a portfolio of policies for which the ground-up indemnity claim size  $X$  has a lognormal distribution with parameters  $(\mu, \sigma) = (7.000, 2.400)$  and allocated loss adjustment expense is  $u = 20\%$  of the indemnity amount. The basic limit is  $b = 100,000$ . We calculate the credit factors, as well as the resulting frequency and severity, for six straight deductible options:  $\{1,000; 2,000; 3,000; 4,000; 5,000; 10,000\}$ . Results are tabulated in Table 6.5. For example, equation (6.33) with  $u = 20\%$  and  $\varepsilon = 0$  implies that

$$C(2,000) = \frac{E[X; d]}{E[X; b]} = \frac{1,111}{8,896} = 0.1249.$$

**Table 6.5. Straight Deductible Credit Factors [Example 6.7]**

| Ded $d$ | $E[X; d]$ | $F_X(d)$ | $C(d)$ | Frequency | Severity | Pure Prem |
|---------|-----------|----------|--------|-----------|----------|-----------|
| 0       | 0         | 0.0000   | 0.0000 | 0.000500  | 10,675   | 5.338     |
| 1,000   | 659       | 0.4847   | 0.0741 | 0.000258  | 19,182   | 4.942     |
| 2,000   | 1,111     | 0.5989   | 0.1249 | 0.000201  | 23,291   | 4.671     |
| 3,000   | 1,478     | 0.6625   | 0.1661 | 0.000169  | 26,375   | 4.451     |
| 4,000   | 1,793     | 0.7051   | 0.2016 | 0.000147  | 28,903   | 4.262     |
| 5,000   | 2,071     | 0.7364   | 0.2328 | 0.000132  | 31,070   | 4.095     |
| 10,000  | 3,144     | 0.8215   | 0.3534 | 0.000089  | 38,669   | 3.451     |

The ground-up claim frequency for this portfolio is  $\phi = 0.000500$ . Consequently, for a policy with deductible  $d = 2,000$  we have an deductible-adjusted frequency

$$\phi(1 - F_X(d)) = (0.000500)(1 - 0.5989) = 0.000201.$$

In addition, the modified severity is

$$\frac{E[X; b] - E[X; d]}{1 - F_X(d)}(1 + u) = \frac{8,896 - 1,111}{1 - 0.5989}(1.20) = 23,291,$$

yielding the pure premium  $p = (0.000201)(23,291) = 4.671$ .

In Example 6.3 we calculated the basic-limit premium for a policy with 400 exposure units to be \$3,285. Accordingly, premium for this policy with a limit of 1,000,000 and a 2,000 deductible is  $P = (3,285)(1.8074 - 0.1249) = \$5,527$ . ■

### Franchise Deductible

The *franchise deductible* was one of the first coverage modifications to arise. Marine underwriters from the earliest times used it with policies insuring cargo shipments. It is now utilized in some types of workers' compensation coverages. The franchise deductible eliminates all claims less than or equal to the deductible or "franchise" amount  $d$ , and claims in excess of  $d$  are paid in full. Consequently, application of a franchise deductible  $d$  to the unlimited, ground-up random variable  $X$  results in the truncated, but non-shifted variable

$$X_d = X, \quad d < X < \infty.$$

In this case, the deductible-modified basic-limit pure premium is

$$p_{b,d} = \phi(E[X; b] - E[X; d] + (1 - F_X(d))(d + \epsilon))(1 + u). \quad (6.35)$$

It is easy to show that the deductible credit factor for a franchise deductible of size  $d$  and basic limit pure premium given by (6.29) is

$$C(d) = \frac{E[X; d] - d(1 - F_X(d)) + F_X(d)\varepsilon}{E[X; b] + \varepsilon}. \tag{6.36}$$

**Example 6.8.** We recalculate the deductible credit factors of Example 6.7 in the case that  $d$  is a franchise deductible. For instance,

$$C(2,000) = \frac{E[X; d] - d(1 - F_X(d))}{E[X; b]} = \frac{1,111 - (2,000)(1 - 0.5989)}{8,896} = 0.0347.$$

Moreover, the resulting claim frequency and severity for a deductible of size 2,000 are, respectively,

$$\varphi = 0.000201 \quad \text{and} \quad \left( \frac{8,896 - 1,111}{1 - 0.5989} + 2,000 \right) (1.20) = 25,691.$$

The full set of results is displayed in Table 6.6. As one would expect, the premium credit for a franchise deductible is less than that for a straight deductible of equal size—the straight deductible eliminates a larger fraction of the pure premium than is eliminated by the corresponding franchise deductible. ■

### Diminishing Deductible

The *diminishing* (or *disappearing*) *deductible* is an alternative that incorporates features of both the straight and franchise deductibles. Such a policy modification eliminates all claims less than a positive deductible amount  $d$  and pays in full all claims in excess of a larger amount  $D$ ,  $D > d$ . Claims between  $d$  and  $D$  in size are paid net of a deductible amount that declines linearly from size  $d$  at  $X = d$  to 0 at  $X = D$ —that

**Table 6.6. Franchise Deductible Credit Factors [Example 6.8]**

| Ded $d$ | $E[X; d]$ | $F_X(d)$ | $C(d)$ | Frequency | Severity | Pure Prem |
|---------|-----------|----------|--------|-----------|----------|-----------|
| 0       | 0         | 0.0000   | 0.0000 | 0.000500  | 10,675   | 5.338     |
| 1,000   | 659       | 0.4847   | 0.0162 | 0.000258  | 20,382   | 5.251     |
| 2,000   | 1,111     | 0.5989   | 0.0347 | 0.000201  | 25,691   | 5.152     |
| 3,000   | 1,478     | 0.6625   | 0.0523 | 0.000169  | 29,975   | 5.058     |
| 4,000   | 1,793     | 0.7051   | 0.0690 | 0.000147  | 33,703   | 4.970     |
| 5,000   | 2,071     | 0.7364   | 0.0846 | 0.000132  | 37,070   | 4.886     |
| 10,000  | 3,144     | 0.8215   | 0.1528 | 0.000089  | 50,669   | 4.522     |

is, the deductible “disappears” at  $D$ . Thus, the deductible amount, as a function of the unrestricted claim value  $x$ , is

$$Ded(x) = \begin{cases} \frac{d}{D-d}(D-x) & \text{if } d \leq x \leq D \\ 0 & \text{if } D < x < \infty. \end{cases} \quad (6.37)$$

Like the franchise deductible, the diminishing deductible has the advantage of eliminating, from the standpoint of the insurer, numerous small claims while at the same time paying larger claims in full. However, the diminishing deductible can be more difficult to administer.

It is a straight-forward exercise to show that the deductible-modified random variable  $X_{d,D}$  is defined for  $X > d$  by

$$X_{d,D} = \begin{cases} \frac{D}{D-d}(X-d) & \text{if } d < X \leq D \\ X & \text{if } D < X < \infty. \end{cases} \quad (6.38)$$

The distribution function for variable  $X_{d,D}$  is therefore

$$F_{X_{d,D}}(x) = \begin{cases} 0 & \text{if } x \leq 0 \\ \frac{F_X\left(\frac{D-d}{D}x + d\right) - F_X(d)}{1 - F_X(d)} & \text{if } 0 \leq x \leq D \\ \frac{F_X(x) - F_X(d)}{1 - F_X(d)} & \text{if } D < x < \infty. \end{cases} \quad (6.39)$$

In the case that allocated loss adjustment expense is loaded multiplicatively (with  $\varepsilon = 0$  in (6.29)), the credit factor  $C(d, D)$  for the disappearing deductible defined by  $d$  and  $D$  is

$$\begin{aligned} C(d, D) = & \frac{1}{E[X; b]} \left[ E[X; D] - D(1 - F_X(D)) \right. \\ & - \frac{D}{D-d} (E[X; D] - E[X; d] - D(1 - F_X(D)) + d(1 - F_X(d))) \\ & \left. + \frac{dD}{D-d} (F_X(D) - F_X(d)) \right]. \end{aligned} \quad (6.40)$$

**Example 6.9.** We now calculate the deductible credit factors for the policies of Example 6.7 with a diminishing deductible for which  $D = d + 1,000$ . The factors are displayed in Table 6.7, compared with those obtained in Examples 6.7 and 6.8.

**Table 6.7. Deductible Credit Factors [Example 6.9]**

| Ded $d$ | Straight<br>$C(d)$ | Diminishing<br>$C(d,D)$ | Franchise<br>$C(d)$ |
|---------|--------------------|-------------------------|---------------------|
| 1,000   | 0.0741             | 0.0233                  | 0.0162              |
| 2,000   | 0.1249             | 0.0424                  | 0.0347              |
| 3,000   | 0.1661             | 0.0599                  | 0.0523              |
| 4,000   | 0.2016             | 0.0766                  | 0.0690              |
| 5,000   | 0.2328             | 0.0917                  | 0.0864              |

Note that for a given  $d$  the straight deductible eliminates the largest percent of the total policy loss, the franchise deductible the least percentage, and the diminishing deductible eliminating an amount between the two extremes. ■

### **Deductibles and Inflation**

Because the characteristics of claims net of a straight deductible are similar to those of excess claims, the deductible exerts a comparable leveraging effect on an inflationary trend, as discussed in Section 5.5.

Suppose, for example, that the pure premium for a policy with a fixed straight deductible of size  $d$  is subjected to a uniform trend factor  $\tau = 1 + r$ . Assuming first that claim-size variable  $X$  is unlimited from above by the policy conditions, we calculate the trended pure premium:

$$p_r = \varphi(1+r)(E[X] - E[X; d/\tau] + (1 - F_X(d/\tau))\varepsilon).$$

The effective trend factor is therefore

$$\tilde{\tau} = 1 + \tilde{r} = (1+r) \frac{E[X] - E[X; d/\tau] + (1 - F_X(d/\tau))\varepsilon}{E[X] - E[X; d] + (1 - F_X(d))\varepsilon}. \quad (6.41)$$

Both  $E[X; x]$  and  $F_X(x)$  are nondecreasing functions of  $x$ , so that

$$0 < r \leq \tilde{r} \quad \text{or} \quad \tilde{r} \leq r < 0. \quad (6.42)$$

Thus, in the absence of other policy limits, the straight deductible magnifies the effect of a uniform trend.

However, if policy claims are limited by an upper limit  $b$ , then

$$\tilde{\tau} = (1+r) \frac{E[X; b/\tau] - E[X; d/\tau] + (1 - F_X(d/\tau))\varepsilon}{E[X; b] - E[X; d] + (1 - F_X(d))\varepsilon}. \quad (6.43)$$

The damping effect of the upper limit in this case sometimes prevents inequalities (6.42) from holding for certain combinations of  $b$ ,  $d$ , and  $r$ . This phenomenon is illustrated in the next example.

**Example 6.10.** A policy has a straight deductible of  $d = 500$ . The ground-up claim-size variable  $X$  has a shifted Pareto distribution with  $(\alpha, \beta) = (2; 8,000)$ . Moreover,  $\phi = 0.25$  and  $\varepsilon = 50$ . If claims are unlimited by policy conditions, then the policy pure premium is

$$\begin{aligned} p_0 &= \phi (E[X] - E[X; d] + (1 - F_X(d))\varepsilon) \\ &= (0.25)(8,000 - 471 + (1 - 0.1142)(50)) \\ &= 1,893. \end{aligned}$$

However, if claims are subjected to a 5% uniform trend, then

$$\begin{aligned} p_{5\%} &= \phi ((1.05)E[X] - (1.05)E[X; d/1.05] + (1 - F_X(d/1.05))(1.05)\varepsilon) \\ &= (0.25)(8,400 - 472 + (1 - 0.1092)(52.5)) \\ &= 1,994. \end{aligned}$$

Thus, the effective trend rate is

$$\tilde{r} = \frac{p_{5\%}}{p_0} - 1 = \frac{1,994}{1,893} - 1 = 5.3\%,$$

greater than the nominal 5%.

On the other hand, if policy conditions limit claims to  $l = 5,000$ , replace  $E[X]$  in the above calculations with the limited severity  $E[X; 5,000] = 3,077$ . Then

$$\tilde{r} = \frac{p_{5\%}}{p_0} - 1 = \frac{677.3}{662.7} - 1 = 2.2\%. \quad (6.44)$$

Here the natural increase in the effective trend rate has been dampened by the presence of the policy limit. ■

## 6.6. Problems

- 6.1** For a certain liability coverage the claim frequency is  $\phi = 0.00075$  and the severity is  $E[Y] = 6,000$ . For these policies expenses are all variable with  $v = 25\%$ . For a policy for an insured with 2,500 exposure units, calculate:
- |                           |                                       |
|---------------------------|---------------------------------------|
| (a) pure premium $p$ .    | (b) expected # policy claims $E[N]$ . |
| (c) policy expected loss. | (d) loss-cost multiplier $\psi$ .   |
| (e) rate $R$ .            | (f) policy premium $P$ .              |
- 6.2** A product liability policy is issued for a premium of \$13,000. The insured's exposure amount is \$2,100,000 of product sales, and the exposure unit is \$1,000 of sales. For this line of business the severity at the policy limit is 9,950, and the policy has a loss-cost multiplier  $\psi = 1.60$ . Calculate:
- |                              |                                       |
|------------------------------|---------------------------------------|
| (a) rate $R$ .               | (b) pure premium $p$ .                |
| (c) claim frequency $\phi$ . | (d) expected # policy claims $E[N]$ . |
| (e) policy expected loss.    | (f) variable expense ratio $v$ .      |

- 6.3** For the policy of Problem 6.2 instead of treating all expenses as variable assume that there is fixed expense of \$0.50 per exposure unit and variable expense is 30% of premium. Calculate:
- (a) rate  $R$ . (b) pure premium  $p$ .  
 (c) claim frequency  $\phi$ . (d) expected # policy claims  $E[N]$ .  
 (e) policy expected loss.
- 6.4** The average claim frequency for a portfolio of policies is  $\phi = 0.000800$  per policy year. If the claim-count distribution is Poisson, compute the probability that an individual annual policy selected from this portfolio will give rise to more than a single claim when the number of exposure units is
- (a) 1,000. (b) 2,000.
- 6.5** Assume that the distribution of the unlimited indemnity claim size  $X$  for a portfolio of policies is lognormally distributed with  $(\mu, \sigma) = (6.800, 2.600)$ .
- (a) Complete the following table of increased limit factors based on formula (6.12) with an average per-claim ALAE = 2,500.

| Limit $l$ | $E[X; l]$ | ALAE  | $l(l)$ |
|-----------|-----------|-------|--------|
| 100,000   | 9,178     | 2,500 | 1.000  |
| 250,000   | _____     | _____ | _____  |
| 500,000   | _____     | _____ | _____  |
| 1,000,000 | _____     | _____ | _____  |
| 2,000,000 | _____     | _____ | _____  |
| 5,000,000 | _____     | _____ | _____  |

- (b) Alternatively, assume that ALAE is 25% of the indemnity payment. Complete the following table of increased limit factors based on formula (6.14).

| Limit $l$ | $E[X; l]$ | ALAE = 25% | $l(l)$ |
|-----------|-----------|------------|--------|
| 100,000   | 9,178     | 2,295      | 1.000  |
| 250,000   | _____     | _____      | _____  |
| 500,000   | _____     | _____      | _____  |
| 1,000,000 | _____     | _____      | _____  |
| 2,000,000 | _____     | _____      | _____  |
| 5,000,000 | _____     | _____      | _____  |

- 6.6** Consider the following alternative to the two methods of loading allocated loss adjustment expense in an ILF formula—the per-claim average amount  $\varepsilon$  of formula (6.12) and the fixed multiple  $u$  of the indemnity payment in formula (6.14). Here the ALAE for smaller claims is loaded as a percent of the indemnity payment, and for larger claims ALAE is fixed at a constant per-claim average.

Let  $X$  be the unlimited claim-size (indemnity only) random variable. Assume that the allocated loss adjustment expense is a fixed multiple  $r$  ( $r > 0$ ) of claim size  $X$  whenever  $X$  is not larger than the claim size  $c$  and that ALAE has the constant value  $rc$  when  $X > c$ . Thus the policy claim amount is

$$Y = \begin{cases} X + rX & \text{if } X \leq c \\ X + rc & \text{if } X > c. \end{cases}$$

Show that in this case the policy severity at limit  $l$  is

$$E_l[Y] = \begin{cases} E[X; l](1+r) & \text{if } l \leq c \\ E[X; l] + rE[X; c] & \text{if } l > c. \end{cases}$$

- 6.7** For the portfolio of policies of Example 6.3 construct an ILF table using the method of loading allocated loss adjustment expense described in Problem 6.6. Assume that  $r = 20\%$  and  $c = 750,000$ . Compare the results to those obtained in Example 6.3.

| Limit $l$<br>(\$000) | $l(l)$<br>$\varepsilon = 2,200$ | $l(l)$<br>$u = 20\%$ | $l(l)$<br>limited |
|----------------------|---------------------------------|----------------------|-------------------|
| 100                  | 1.0000                          | 1.0000               | 1.0000            |
| 500                  | 1.4263                          | 1.5317               | _____             |
| 750                  | 1.5202                          | 1.6488               | _____             |
| 1,000                | 1.5812                          | 1.7249               | _____             |
| 2,000                | 1.7067                          | 1.8815               | _____             |
| 3,000                | 1.7655                          | 1.9548               | _____             |
| 4,000                | 1.8008                          | 1.9989               | _____             |
| 5,000                | 1.8248                          | 2.0288               | _____             |

- 6.8** (a) Construct the following ILF table using the risk-loaded formula (6.22). Assume that the unlimited indemnity claim size  $X$  has a shifted Pareto distribution with  $(\alpha, \beta) = (3; 6,000)$  and that  $\varepsilon = 0$ ,  $u = 20\%$ . Use the standard deviation method of risk loading (6.24) with  $k' = 0.5000$  and  $\delta = 0.1000$ .

| Limit $l$ | $E[X; l]$ | ALAE  | $\rho(l)$ | $l(l)$<br>w/o RL | $l(l)$<br>w/ RL | Weight |
|-----------|-----------|-------|-----------|------------------|-----------------|--------|
| 1,000     | 796       | 159   | 447       | 1.0000           | 1.0000          | 10%    |
| 2,000     | _____     | _____ | _____     | _____            | _____           | 5%     |
| 3,000     | _____     | _____ | _____     | _____            | _____           | 15%    |
| 4,000     | _____     | _____ | _____     | _____            | _____           | 15%    |
| 5,000     | _____     | _____ | _____     | _____            | _____           | 25%    |
| 7,500     | _____     | _____ | _____     | _____            | _____           | 10%    |
| 10,000    | _____     | _____ | _____     | _____            | _____           | 20%    |

- (b) Calculate the overall premium effect of using the risk-loaded factors in place of the unloaded factors.
- 6.9** Show that the risk-load parameter  $\delta$  of formulas (6.23) and (6.24) can be expressed as  $\delta = \gamma E[N]$ , where  $\gamma$  denotes the contagion parameter for the claim-count variable  $N$ .
- 6.10** Construct the following table of increased limit factors using the risk-loaded formula (6.22). Assume that the unlimited indemnity claim size  $X$  has a shifted Pareto distribution with  $(\alpha, \beta) = (0.780, 100)$  and that  $\varepsilon = u = 0$ . Use the variance method (6.23) for calculating the risk-load function  $\rho(l)$  with  $k = 0.0000005$  and  $\delta = 0$ . Calculate the layer factors for successive layers of 1,000,000 width and thereby demonstrate the inconsistency of this set of ILFs.

| Limit $l$  | $E[X; l]$ | $\rho(l)$ | $l(l)$ | Layer Factor |
|------------|-----------|-----------|--------|--------------|
| 1,000,000  | 2,994     | 622       | 1.0000 | —            |
| 2,000,000  | 3,562     | 1,448     | 1.3858 | 0.3858       |
| 3,000,000  | 3,936     | 2,375     | 1.7458 | 0.3600       |
| 4,000,000  | _____     | _____     | _____  | _____        |
| 5,000,000  | _____     | _____     | _____  | _____        |
| 6,000,000  | _____     | _____     | _____  | _____        |
| 7,000,000  | _____     | _____     | _____  | _____        |
| 8,000,000  | _____     | _____     | _____  | _____        |
| 9,000,000  | _____     | _____     | _____  | _____        |
| 10,000,000 | _____     | _____     | _____  | _____        |

- 6.11** Consider a policy selected from the portfolio of Example 6.6 with per-claim limit  $l$ . Calculate the loss eliminated by the addition of an aggregate limit of size  $l$  and obtain the resulting loss elimination ratio when  $l$  equals:
- (a) 1,000,000.      (b) 2,000,000.      (c) 3,000,000.  
 (d) 4,000,000.      (e) 5,000,000.
- 6.12** (a) Assuming that variable expenses and profit load are 25% of premium, calculate the premium for a policy selected from the portfolio of Example 6.6 with a per-claim limit of 1,000,000 and no aggregate limit.  
 (b) What is the premium credit if the policy in part (a) is written with an aggregate limit of 1,000,000?
- 6.13** The following set of twelve (unadjusted) losses are incurred on a policy with a per-claim limit of  $l = 20,000$  and a deductible of size  $d = 2,000$ :

{1,000; 1,550; 1,700; 2,200; 2,500; 3,000;  
 5,200; 9,000; 11,000; 12,500; 15,000; 19,800}.

Compute the total amount paid by the insurer (exclusive of loss adjustment expense) and the empirical loss elimination ratio for this set of claims if the deductible is

- (a) a straight deductible.                      (b) a franchise deductible.

- 6.14** Repeat the calculations requested in Problem 6.13 if the policy in that problem has a per-claim limit of  $l = 12,000$ .
- 6.15** Derive formula (6.33) for the franchise deductible credit factor.
- 6.16** (a) Calculate the straight deductible factors and corresponding pure premiums for the portfolio of policies of Example 6.7, this time with ALAE parameters  $\varepsilon = 500$  and  $u = 0$ .  
(b) Calculate the franchise deductible factors and corresponding pure premiums for the portfolio of policies of Example 6.8 with ALAE parameters of part (a).
- 6.17** A policy has a basic limit  $b = 5,000$  and a deductible of size  $d$ . Assume that the underlying claim size variable  $X$  has a shifted Pareto distribution with  $(\alpha, \beta) = (3.00; 10,000)$ . Assume also that the unlimited claim frequency is  $\varphi = 0.005$  and  $\varepsilon = 250$ . Compute  $C(d)$ , the policy frequency and severity, and the pure premium for deductibles of sizes  $\{0; 250; 500; 750; 1,000\}$  in the case of  
(a) a straight deductible.                      (b) a franchise deductible.
- 6.18** Prove that on the interval  $0 < d < b$  the deductible credit factors (6.33) and (6.36)  
(a) are increasing functions of  $d$ .  
(b) satisfy the inequality  $0 < C(d) < 1$ .
- 6.19** Verify formulas (6.38), (6.39), and (6.40) for the diminishing deductible.
- 6.20** Verify inequalities (6.42) for a deductible-modified uniform trend rate.
- 6.21** A portfolio of policies described in Example 6.7 has a total expected ground-up claim count of 500.  
(a) For each of the indicated straight deductibles calculate (i) the total number of claims eliminated by the deductible and (ii) the percent of the total ground-up basic-limit loss eliminated by the deductible.

| Deductible | # Claims Eliminated | % BL Premium Eliminated |
|------------|---------------------|-------------------------|
| 1,000      | _____               | _____                   |
| 2,000      | _____               | _____                   |
| 3,000      | _____               | _____                   |
| 4,000      | _____               | _____                   |
| 5,000      | _____               | _____                   |

- (b) Assuming that the claim-size  $X$  is subjected to a 10% uniform trend, perform the same calculations requested in part (a).

| Deductible | # Claims<br>Eliminated | % BL Premium<br>Eliminated |
|------------|------------------------|----------------------------|
| 1,000      | _____                  | _____                      |
| 2,000      | _____                  | _____                      |
| 3,000      | _____                  | _____                      |
| 4,000      | _____                  | _____                      |
| 5,000      | _____                  | _____                      |

- 6.22** Verify the calculation of the pure premium amounts used in equation (6.44).

