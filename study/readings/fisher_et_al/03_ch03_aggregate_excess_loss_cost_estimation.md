---
paper: fisher_et_al
chapter: 3
title: "Chapter 3: Aggregate Excess Loss Cost Estimation"
topics: [table_m, insurance_charge, insurance_savings, entry_ratio, lee_diagrams, table_l, expected_loss_group, per_occurrence_limits]
key_formulas: [table_m_charge_phi, table_m_savings_psi, phi_psi_relationship, balance_equations_3_4_and_3_5, basic_premium_formula_3_3, table_l_charge_formula]
---

> **TL;DR**
> - Entry ratio r = A/E; Table M charge φ(r) = E[max(A/E − r, 0)] (expected aggregate excess ratio); savings ψ(r) = E[max(r − A/E, 0)]; fundamental relation: ψ(r) = φ(r) + r − 1
> - Lee diagrams place loss size on the y-axis and cumulative probability on the x-axis; area under the curve = E{X}; horizontal slicing (∫S(x)dx per layer) is often simpler than vertical slicing for expected loss in a layer
> - Table M is constructed empirically by grouping similar-sized risks (expected loss group or expected claim count group), computing entry ratios, and averaging excess per risk (vertical) or accumulating layer survival probabilities (horizontal); larger policies have lower φ(r) for the same r
> - Table M_D uses per-occurrence-limited losses before aggregating; Table L charge φ*_D(r) = per-occurrence excess ratio k plus aggregate excess of limited losses, all relative to unlimited expected loss
> - Balance equations: φ(r_H) − φ(r_G) = (e+E−H)/(cE) and r_G − r_H = (G−H)/(cE); used with B = e − (c−1)E + cI to derive all retro plan parameters from specified min/max premiums

# Chapter 3: Aggregate Excess Loss Cost Estimation

By Ginda Kaplan Fisher

### 1. Overview

#### 1.1. *Who Pays, and How Much?*

A critical part of modeling the cost of an insurance contract is determining who pays, and how much. When an insurance policy includes risk sharing at an aggregate level, it can be quite challenging to model these aggregate losses and to determine the coverage responsibilities among the parties to an insurance contract—e.g., the policyholder and/or the insurer. How to do so will depend upon the specific nature and parameters of the contract. Estimating the cost of various slices of the aggregate losses is important in estimating insurance costs when:

- A retrospectively rated policy (or “retro”) is considered, as retrospectively rated policies have a maximum ratable loss (max). The impact of aggregate losses on the policy premium are limited by the max.
- A retrospectively rated policy has a minimum ratable loss (min).
- A deductible policy has an aggregate limit.
- A policy is written over a self-insured retention, limiting the customer’s aggregate losses.
- A (re)insurance policy has an aggregate limit on the total it will pay out, but the data (or mathematical functions used to estimate the data) used to price the policy is not subject to that limit.

Americans are probably most familiar with aggregate loss costs in health insurance. It is common for US health insurance policies to have a deductible and/or co-payment, but an annual limit on “out of pocket” costs. That is, there is an aggregate limit on the deductible plus co-payment (where a co-payment is really just another type of deductible—so the two combined are the total deductible for the policy).

For example, a policy might pay 80% of medical costs incurred after you pay a \$2000 annual deductible. (That is, a 20% co-payment.) But your out-of-pocket medical costs will be capped at \$10,000. So if you get very ill, the costs you are charged and the insurance payments might look like this:

Exhibit 3.1. Illustrative medical costs

| Date | Gross Medical Cost Incurred | Payment toward Annual Deductible | Insured's Co-Payment | Insurance Payment | Insured's Cost for this month | Insured's cost so far this year |
|------|-----------------------------|----------------------------------|----------------------|-------------------|-------------------------------|---------------------------------|
| Jan  | \$1,000                     | \$1,000                          | 0                    | 0                 | \$1,000                       | \$1,000                         |
| Feb  | \$5,000                     | \$1,000                          | \$800                | \$3,200           | \$1,800                       | \$2,800                         |
| Mar  | \$20,000                    | 0                                | \$4,000              | \$16,000          | \$4,000                       | \$6,800                         |
| Apr  | \$20,000                    | 0                                | \$3,200              | \$16,800          | \$3,200                       | \$10,000                        |
| May  | \$10,000                    | 0                                | 0                    | \$10,000          | 0                             | \$10,000                        |
| Jun  | \$4,000                     | 0                                | 0                    | \$4,000           | 0                             | \$10,000                        |

Here, you finished paying the \$2000 flat deductible partway through February, and then paid 20% of the medical expenses incurred until you paid the out-of-pocket cap of \$10,000 partway through April. In this example, you recovered in June and stopped incurring medical payments that year.

A commercial liability policy might have a per-claim deductible of \$100K and an aggregate limit on the deductible of \$500K. In the insurance industry, this type of policy is often referred to as a “large deductible policy” or a “large dollar deductible policy,” in order to distinguish it from, for example, a Homeowners’ policy with a \$500 deductible. For simplicity, hereafter it will just be referred to as a deductible policy. A similar example for this policy might look like this:

Exhibit 3.2. Illustrative general liability costs

| Date | Dollars of loss on claims that are each less than \$100K | Number of claims over \$100K | Dollars of loss on claims over \$100K | Deductible | Insurance payment | Insured's cost so far this year |
|------|----------------------------------------------------------|------------------------------|---------------------------------------|------------|-------------------|---------------------------------|
| Q1   | \$132,500                                                | 0                            | 0                                     | \$132,500  | 0                 | \$132,500                       |
| Q2   | \$93,000                                                 | 2                            | \$350,000                             | \$293,000  | \$150,000         | \$425,500                       |
| Q3   | \$105,000                                                | 0                            | 0                                     | \$74,500   | \$30,500          | \$500,000                       |
| Q4   | \$122,500                                                | 1                            | \$150,000                             | 0          | \$272,500         | \$500,000                       |

In this case, the insured pays all the losses on claims less than \$100K, and pays the first \$100K of each large claim, until the aggregate limit of the deductible is reached in Q3. After that, the insurance company pays the rest of the losses incurred under the policy. Of course, in typical years, the insured would not incur enough large claims to exhaust the aggregate limit.

The out-of-pocket maximum or aggregate limit on the deductible is a benefit to the insured (and a cost to the insurer). In general, the same mathematical tools can be used to estimate any “slice” of aggregate loss, whether a cost or a savings to the insurer. It is important to pay attention to which party benefits from any particular aggregate limit. When confused, it is often helpful to imagine a specific situation and ask, “how much does the insured pay before the insurer is responsible? How

much does the insurer pay before hitting its policy limits? How much is the insured responsible for above the policy limits?

This chapter focuses on retrospectively rated and deductible plans. It is clearer to develop the math of aggregate loss cost limitations in the context of a simple retrospective policy that has no per-occurrence loss limits. This allows us to delay introducing the complications of also needing to consider the impact of any per-occurrence limitations, so much of the chapter will be written from that perspective. Then this chapter will go on to explain how to incorporate per-occurrence limitations. Keep in mind that the tools described in this chapter can work for all the situations above.

This approach is consistent with the historical development of the math around aggregate insurance losses. Many of the early papers on aggregate excess loss costs were written from the perspective of US workers' compensation policies. Retrospective rating was introduced for workers' compensation a couple decades after the coverage was invented, as a way to more fairly charge premium to safer and less safe employers.<sup>14</sup> Workers' compensation policies have no policy limit on the insurer's liability (except for the limitations imposed by the human lifespan) and some retrospectively-rated policies have no per-claim loss limitation on ratable losses used in calculating the retrospective premium.

But the reader should be aware that deductible policies are far more important and widespread than retrospective policies today. For that reason, deductibles will be discussed alongside retros when the topic is relevant to policies with per-occurrence loss limitations.

For simplicity of language, this chapter will often refer to unlimited losses. This is a natural way to describe workers' compensation losses, because there is no limit to the insurer's liability under the policy. And most of this material was originally developed in the context of US worker's compensation, so this language is consistent with most of the literature. However, all the math works the same if you substitute "losses to policy limit" for "unlimited losses" when you are working with other coverages. In real life, the actuary must be careful to keep track of whether the word "limit" refers to a policy limit, a deductible limit, or some other limit.

From the point of view of the policyholder, a deductible with an aggregate limit looks the same as a retro with a loss limit (with respect to ultimate losses retained). For example, the insured who buys a large deductible policy with a deductible of \$250,000 and an aggregate deductible limit of \$500,000 is in essentially the same position as an insured who purchases a retro with a maximum that translates to \$500,000 of loss, and a per loss limit of \$250,000 (ignoring the fact that there might be some differences in the treatment of expenses). The language is a little different—what we call the per-claim (or per-occurrence) deductible on a large deductible policy corresponds to the loss limitation

---

<sup>14</sup> The first retrospective rating plan for Workmen's Compensation, as it was then called, was approved by Massachusetts in 1936, as described by Sydney Pinney in "Retrospective Rating Plan for Workmen's Compensation Risks," *PCAS* XXIV.

on a retro; what we call an aggregate limit on a deductible corresponds to the maximum on a retro—but the general structures are the same. In particular, the risk transfer is the same.<sup>15</sup>

The reader should be aware that the timing and accounting for the monies that flow between insurer and insured are different for different types of policies, even if the risk transfer is essentially the same. For example, in a retro plan, risk-sensitive future cash flows are typically premium, and typically they only happen once a year. Those cash flows are losses in a deductible plan, and the deductible losses may be billed and paid monthly. There are also plans with loss-sensitive dividends, which are an expense to the insurer (not premium or loss) and are usually calculated annually. But while the timing of cash flows and other aspects of the plans might differ, the expected ultimate loss, which is the subject of this chapter, is the same. Loss sensitive dividend plans and self-insured retention plans can have similar loss provisions, as discussed in chapter 2.

This chapter focuses mostly on aggregate limits of primary losses, because insurers typically have more information about those losses, and thus more methods of estimating them. But similar methods can be used to price policy limits when the actuary lacks a history of relevant data but has a reasonable idea of the underlying frequency and severity distributions.

#### *1.2. Some definitions and notation to describe aggregate losses*

It is important to remember that losses are random processes, and a particular outcome (for example, the losses that a risk incurs during a policy year) is unlikely to match the expected value.

First, consider a retrospectively rated policy with no per-claim limit. This is common on smaller policies, where the maximum ratable loss might easily be breached by one large claim.

The following notation and definitions are used throughout this chapter:

**N:** the random variable representing the number of claims that a risk incurs during the relevant period (usually the life of a policy).

The expected claim frequency is the expected number of claims divided by the exposures or premium of the risk. We might also consider the frequency of large or small claims.<sup>16</sup>

---

<sup>15</sup> Or nearly the same. There might be some differences due to the timing of the payments, and what sort of security is required.

<sup>16</sup> A policy might be written per-claim, or per-occurrence, but for simplicity, this chapter will refer to the insured event as a claim, and use the terms “claim” and “occurrence” interchangeably. In real life, there might be sub-limits per claim, as well as limits per-occurrence, or other differences between a claim and an occurrence. The same general methods can be used to estimate expected losses under such policies, but working out the details is beyond the scope of this chapter. Similarly, a loss sensitive rating plan might contemplate loss or loss + ALAE. The two would have different expected loss distributions. But investigating the expected difference is beyond the scope of this study note.

**X**: random variable representing a claim incurring to a risk.

The expected severity is  $E\{X\}$ , the expected value of a single claim, should it occur.

**A**: random variable representing the actual total aggregate loss incurring to a risk.<sup>17</sup>

**E** =  $E\{A\}$ : expected loss.

Note that  $E\{A\} = E\{N\} * E\{X\}$

**Entry ratio:  $r = \frac{A}{E}$** : the ratio of actual to expected losses (or, equivalently, the ratio of the actual policy loss ratio to the expected loss ratio)

For example, a policy was written on a commercial auto fleet. The underwriter expected total losses on the policy to be \$200,000. At the end of the year, actual losses on the policy were estimated to have been \$189,000. In this case, the entry ratio  $r = 189K/200K = 0.945$ .

If the premium for that policy was \$250,000, the expected loss ratio would have been 80.0% (\$200K/\$250K). The actual loss ratio would have been 75.6% (\$189K/\$250K). The entry ratio calculated from loss ratios is  $75.6\%/80.0\% = 0.945$ . The two methods of determining the entry ratio are equivalent: the loss ratio calculation is simply the loss calculation with both numerator and denominator divided by the premium.

The entry ratio, **r**, is also a random variable. Although policies of different sizes tend to have different distributions of **r**, similarly sized policies of the same type of coverage (e.g., commercial auto policies in the Midwest covering fleets of private passenger vehicles, with expected losses of a few million dollars) will behave similarly, and it is customary to estimate expected aggregate excess losses in terms of their entry ratio. When aggregate charges were published in tabular form, in printed books, the charges were calculated separately for various expected loss groups (ELGs) that were similar enough to group together for analysis, and the actuary “entered the table” at the appropriate entry ratio. Empirical studies of aggregate charges are still done by grouping similar policies in this way.

The approximate size of a policy has a large influence on how its aggregate excess losses will behave. This is mostly because the variance of the loss distribution is very sensitive to the expected number of claims. Historically, policies were grouped by their expected losses (into expected loss groups) as a proxy for the expected number of claims. Policies can also be grouped directly by their expected number of claims (into expected claim count groups.) The rationale for grouping policies by size (either expected loss or expected number of claims) is discussed later in this chapter, in section 6.

---

<sup>17</sup> Note that some textbooks use S to designate this amount.

**$\phi(r)$ : Table M charge<sup>18</sup>** = the ratio of a risk's average amount of loss in excess of  $r$  times its expected loss, divided by the total expected loss, or the expected percent of losses excess of  $rE$ .

$\phi(r)$  is also known as the **Aggregate Excess Loss Factor, Aggregate Excess Ratio, Excess Pure Premium Ratio, or Insurance Charge**. (Note that this chapter will use "insurance charge" to refer to an amount, not a ratio, but the phrase is used both ways in the literature.)

**Table M:** a collection of related aggregate excess loss factors (and related savings, defined below). When there is a per-occurrence limit, "Table M" will refer to those factors calculated ignoring the impact of that limit. See **Table M<sub>D</sub>** below.

**Insurance Charge:**  $\phi(r)$  times the expected loss, **E**.

This value, the expected aggregate excess loss, is often called the insurance charge because on a retrospectively rated policy, this is the portion of the retrospective premium that is fixed and pays for losses.<sup>19</sup> (The other premium components are variable or pay for expenses.)

For example, consider an insurer with a book of 5 similar policies, each with an expected loss of \$100K. In a typical year, the actual losses on those policies are \$80K; \$90K; \$100K; \$110K; and \$120K. The average loss for the book is, as expected, \$100K per policy.

(This is not a realistic example, it was chosen to be symmetric and with small variation for illustrative purposes only.)

At  $r=1$ , the aggregate excess ratio,  $\phi(1)$ , is the portion of each loss above 100K, divided by the expected loss:

$$(0+0+0+10K+20K)/(100K+100K+100K+100K+100K) = 0.06.$$

At  $r = 0.6$ , the aggregate excess ratio,  $\phi(0.6)$ , is the portion of each loss above 60K ( $60K = 0.6 * \text{expected loss}$ ):

$$(20K+30K+40K+50K+60K)/(500K) = 0.40.$$

At  $r = 1.2$ , the aggregate excess ratio,  $\phi(1.2)$ , is the portion of each loss above 120K, or zero.

**$\psi(r)$ : Table M Savings** = the expected amount by which the risk's actual aggregate loss falls short of  $r$  times the expected loss, divided by the expected loss, (so, an expected percent, not an expected amount.) Or,

---

<sup>18</sup> Historically, the National Council of Compensation Insurers (NCCI) published aggregate excess loss factors and aggregate minimum loss factors for use with retrospectively rated US workers' compensation in a large table. Those factors were referred to collectively as "Table M." For example, see *The 1965 Table M*, by LeRoy Simon, *PCAS LII*, 1965. The terminology has passed into common usage and will be used throughout this paper.

<sup>19</sup> If a retro policy also has a per claim loss-limit, the charge for that is sometimes considered part of the insurance charge, and sometimes considered a separate charge. The terminology is not entirely consistent across the industry, and the actuary should be careful to understand what is being measured or estimated.

$\psi(\mathbf{r}) = \text{the expected value of } \max [r - \frac{A}{E}, 0],$

An empirical estimate over several similar risks could be calculated as:

$$\psi(\mathbf{r}) = \sum_{i=1}^N \max [r - \frac{A_i}{E_i}, 0] / N$$

$\psi(\mathbf{r})$  is also known as the insurance savings or aggregate minimum loss factor. (As with the phrase “insurance charge”, note that this chapter will use “insurance savings” to refer to an amount, not a ratio, but the phrase is used both ways in the literature.)

Retrospectively rated policies often have a minimum ratable loss as well as a maximum ratable loss. This is the minimum aggregate loss that factors into the retrospective premium calculation. Just as the maximum aggregate loss that the insured will pay for generates an insurance charge, the minimum ratable loss the insured will pay for even if it incurs no claims over the policy period generates an insurance savings that offsets the insurance charge (or is subtracted from the charge to generate a net insurance charge. The ratio of the net insurance charge to the expected loss is called the Net Table M charge, or the net aggregate loss factor).

Continuing the simple example as above, a book of 5 similar policies, each with an expected loss of \$100K, and a typical loss distribution of \$80K, \$90K, \$100K, \$110K, and \$120K:

At  $r=1$ , the insurance savings,  $\psi(1)$ , is the portion that each loss falls short of 100K, divided by the expected loss:

$$(20K+10K+0+0+0)/(100K+100K+100K+100K+100K) = 0.06.$$

At  $r = 0.6$ , the insurance savings,  $\psi(0.6)$ , is the portion that each loss falls short of 60K (0.6 \* expected loss):

$$(0+0+0+0+0)/(500K) = \text{zero}.$$

At  $r = 1.2$ , the insurance savings,  $\psi(1.2)$ , is the portion that each loss falls short of 120K:

$$(40K + 30K + 20K + 10K + 0)/(500K) = 0.20.$$

**Charges and Savings:** More precisely, let

$Y = \mathbf{A}/\mathbf{E}$ , actual loss in units of expected loss (i.e., the entry ratio)

$F(Y)$  = the cumulative distribution function of  $Y$ .

Then

$$\phi(r) = \int_r^{\infty} (y - r) dF(y)$$

and

$$\psi(r) = \int_0^r (r - y) dF(y)$$

By definition, both  $\phi(r)$  and  $\psi(r)$  are non-negative for every  $r$ .

While the expected loss to the risk is  $\mathbf{E}$ , there is often a great deal of variance in the distribution of  $\mathbf{A}$ , the actual loss. For example, if 100 similar risks each have the same expected loss,  $\mathbf{E}$ , we would expect some of them to actually have more loss, and others less than expected. Thus, in general, we expect both  $\phi(r)$  and  $\psi(r)$  to be positive numbers for most non-negative values of  $r$ .<sup>20</sup>

**$\mathbf{A}_D$ :** The actual policy loss, with each claim or occurrence limited to  $D$ .<sup>21</sup>

---

<sup>20</sup> Note that in unusual cases where all risks always have losses close to what is expected, the charges and savings are zero for many values of  $r$ , such as in the overly simple example of five policies, above.

<sup>21</sup> It was pointed out to the author that Bahnemann uses the same notation to refer to excess rather than primary losses. This is unfortunate for candidates studying both for CAS exam 8, but actuaries should always be aware of what notation means in context.

Many policies have per-occurrence limits as well as aggregate limits. If a retrospective policy has a per-occurrence limit, the actuary might estimate the expected excess loss separately, and then look at the function of limited losses.

**Expected Primary Losses:**  $E\{A_D\}$ , the expected value of the losses limited by the per-occurrence limit.

**k:** the excess ratio for the per-occurrence limit. That is,  $k = \frac{E - E\{A_D\}}{E}$

**Table M<sub>D</sub>:** A table of related aggregate excess loss factors and related savings developed using data in which the individual losses have been limited by a per-occurrence limit prior to being aggregated into policy outcomes for use in developing those charges and savings.

For example, M<sub>\$100,000</sub> has had a per-occurrence limit of \$100,000 applied.

Limited Table M factors are developed exactly the same as unlimited Table M factors, except we use the distribution of limited (primary) losses.

**r** =  $A_D / E\{A_D\}$ , the entry ratio of the limited distribution, the actual policy loss on the policy in units of expected primary loss; and

**F<sub>D</sub>(r)** = the cumulative distribution function of **r**, the limited losses whose unlimited cumulative distribution function was given by **F**.

Note that the limited Table M charge (or savings) in this case will be the ratio of a risk's average amount of limited loss in excess of (entry ratio) **r** times its expected limited loss, divided by the total expected limited loss.

**Table L:** It is also possible to calculate the total amount of loss that will be covered by the policy (per-occurrence excess plus aggregate excess) directly, as a single factor to expected loss. That amount is known as the Table L charge, for the California Table L.<sup>22</sup> It will be described in more detail in section 5.1.

Note that when considering Table L calculations, the entry ratio (**r**) is defined as the actual limited aggregate losses divided by the expected unlimited aggregate losses.

**ϕ<sub>D</sub><sup>\*</sup>(r):** the Table L charge at entry ratio **r** and per-occurrence limit **D** for aggregate and per-occurrence loss. This is defined as the average difference between a risk's actual unlimited loss and its actual limited loss, plus the risk's limited loss in excess of **rE**.

The Table L insurance charge at entry ratio  $r \geq 0$  is defined as:

$$\phi_D^*(r) = \int_r^\infty (y - r) dF^*(y) + k$$

---

<sup>22</sup> Skurnick, D., "The California Table L," *PCAS LXI*, 1974, pp. 117-140.

$\psi_D^*(r)$ : the Table L savings at entry ratio  $r$  and per-occurrence limit  $D$ ,  $\psi_D^*(r)$ , is defined as the average amount by which the risk's actual limited loss falls short of  $r$  times the expected unlimited loss.

$$\psi_D^*(r) = \int_0^r (r - y) dF^*(y)$$

Note that the Table L charge and savings are both expressed as ratios to expected unlimited loss.

As mentioned above, the claims covered by a deductible policy with an aggregate deductible limit are the same as the claims covered by a retrospectively rated policy with the same per-claim limit and maximum ratable loss entering the retrospective rating formula.

The amount of premium will be different, however. For a retrospective policy, the insurer pays all of the losses and the insured pays premium. The premium will be comparable to that of a fully insured policy, although the actual amount of premium to be paid to the insurer is uncertain until all the claims have settled. In contrast, for a deductible policy the insurer is reimbursed for losses below the deductible (subject to limit of the aggregate deductible amount) and the insured's premium is a fixed amount much smaller than that for a fully insured policy. For a deductible policy, the pure premium is the sum of the expected per-occurrence excess loss and the expected aggregate excess loss, and the total premium is the pure premium grossed up for the risk charge and other expenses. In the case of a deductible policy, the uncertainty is in the amount and timing of the loss reimbursements that the insured will have to pay to the insurer.

In Section 2 of this chapter we will try to give a better intuitive understanding of these entities by drawing pictures of them. This will be accompanied by descriptions of some important relevant calculations.

#### Questions

1. A policy has a \$10,000 per-occurrence deductible, a \$25,000 aggregate deductible limit, and a per-occurrence policy limit of \$1M. Over the course of the policy, the insured incurs the following losses, in chronological sequence:

\$3,000   \$8,000   \$14,000   \$12,000   \$18,000

Determine (i) the total insurance policy coverage, and (ii) the amount for which the insured is responsible after the insurance coverage, for each of the following:

- (a) After the first three claims have been incurred
- (b) After the first four claims have been incurred
- (c) After all five claims have been incurred

2. Medium Manufacturing Company (MMC) buys a General Liability policy with a large deductible. The policy has a \$250K per-claim deductible, covers claims up to \$1M per claim (from the first dollar, so the insured amount is actually \$1M less \$250K, or \$750K xs \$250K<sup>23</sup>) with an aggregate limit on the policy of \$5M and an aggregate limit on the deductible of \$1M. During the policy period, MMC has the following claims:

- 25 small claims that collectively cost \$500K
- 1 claim for \$100K
- 1 claim for \$300K
- 1 claim for \$2M

- (a) What is the total loss sustained by MMC prior to any consideration of insurance?
- (b) What is MMC's total loss responsibility under the per-claim deductible (but before consideration of the aggregate limit of the deductible)?
- (c) How much of MMC's deductible losses are above the aggregate limit on the deductible?
- (d) How much is over the per-claim policy limit?
- (e) How much loss would be paid by the insurer prior to consideration of the policy's aggregate limit?
- (f) How much loss is over the policy's aggregate limit?
- (g) How much in total will the insurance company need to pay for MMC's liability?

3. Let A, the total aggregate loss random variable, have a continuous uniform distribution from 0 to 100. Let E, the expected aggregate losses, be the mean of the uniform distribution, or 50. Find the Table M Insurance Charge associated with

---

<sup>23</sup> This is often denoted just "\$750K x \$250K", or even "750x250" in practice.

- (a)  $A = 40$
- (b)  $A = 50$
- (c)  $A = 60$

4. Let aggregate loss random variable  $A$  be an exponential distribution with a mean of 10. Find the Table M (Insurance) Savings associated with

- (a)  $A = 5$
- (b)  $A = 10$
- (c)  $A = 15$

### 2. Visualizing Aggregate Excess Losses

The mathematics of per-occurrence excess and aggregate excess loss coverage can often be challenging, so it can be helpful to think about the questions graphically. Section 2 of this chapter is adapted from a paper by Yoong-Sin Lee.<sup>24</sup> This paper is so widely used in the casualty actuarial field that the graphs he described are often referred to as “Lee diagrams.”

While formulas are good for calculations, graphs often provide insight into the structure of a problem, and help with developing intuition. Many problems are hard to understand until you draw a picture. Per-occurrence excess and aggregate excess loss calculations can be unintuitive, and it’s often helpful to draw a picture specifying which layers will be paid by which party before commencing with the calculations. A good graphical presentation can not only provide insight into the abstract relations, it can also make the mathematical procedure much easier to follow compared with algebraic manipulations. For those who always prefer algebra, it will serve at least as a very useful supplement to the algebraic treatment.

Note that a key feature of Lee diagrams is that “size” (severity, or aggregate loss, or entry ratio) is on the vertical axis, and the horizontal axis represents the cumulative claim count or cumulative % of loss distribution. In that sense, Lee diagrams are slightly different from what many actuaries are used to seeing with respect to probability functions.

#### 2.1. *Lee Diagrams of Severity Distributions*

To develop the idea of what Lee diagrams look like, consider the case of per-occurrence deductibles and limits.

To start with, consider a large number of losses, of ordered sizes  $x_1, x_2, \dots, x_k$ , occurring  $n_1, n_2, \dots, n_k$  times, respectively, with  $n = n_1 + \dots + n_k$ .

We might, for example, look at the distribution of those losses. In Exhibit 3.3, we show the incremental and cumulative loss distribution of a set of losses, with size of loss on the X-axis.

---

<sup>24</sup> Lee, Yoong-Sin, “The Mathematics of Excess of Loss Coverages and Retrospective Rating—A Graphical Approach,” *PCAS* LXXV, 1988.

Exhibit 3.3. Size-of-loss on the X-axis  
Incremental and Cumulative loss distributions

![Two histograms showing incremental and cumulative loss distributions.](892c6816711b2d83080366cf799d2c62_img.jpg)

The figure consists of two side-by-side histograms. The left histogram shows the 'Number of Claims' on the y-axis (ranging from 0 to 16) against the 'Size of Loss' on the x-axis (ranging from 1 to 20). The right histogram shows the 'Cumulative Claim Count' on the y-axis (ranging from 0 to 16) against the 'Size of Loss' on the x-axis (ranging from 1 to 20).

| Size of Loss | Number of Claims | Cumulative Claim Count |
|--------------|------------------|------------------------|
| 1            | 1                | 1                      |
| 2            | 1                | 2                      |
| 3            | 1                | 3                      |
| 4            | 2                | 5                      |
| 5            | 2                | 7                      |
| 6            | 4                | 11                     |
| 7            | 1                | 12                     |
| 8            | 1                | 13                     |
| 9            | 1                | 14                     |
| 10           | 1                | 15                     |
| 11           | 1                | 16                     |
| 12           | 1                | 17                     |
| 13           | 1                | 18                     |
| 14           | 1                | 19                     |
| 15           | 1                | 20                     |
| 16           | 1                | 21                     |
| 17           | 1                | 22                     |
| 18           | 1                | 23                     |
| 19           | 1                | 24                     |
| 20           | 1                | 25                     |

Two histograms showing incremental and cumulative loss distributions.

In Exhibit 3.4 we represent these same losses by means of a cumulative frequency curve, in which the y-axis represents the loss size, and the x-axis represents the cumulative number of losses,  $c_i = n_1 + \dots + n_i, i \leq k$ . This is how Lee diagrams are constructed.

Exhibit 3.4. A Cumulative Frequency Curve—Size-of-loss on the Y-axis

![A cumulative frequency curve (Lee diagram) showing size of loss on the Y-axis and cumulative claim count on the X-axis.](7a427d3f02cc89bd23f77068e257e90f_img.jpg)

The graph shows a step function representing the cumulative frequency curve. The y-axis is labeled 'Size of Loss' and ranges from 0 to 20. The x-axis is labeled 'Cumulative Claim Count' and ranges from 0 to 16. A shaded vertical strip is highlighted between cumulative claim counts 4 and 5, with a height of 4. The area of this strip is labeled  $n_i x_i$ . The total cumulative claim count is labeled  $n$ .

| Cumulative Claim Count | Size of Loss |
|------------------------|--------------|
| 0                      | 0            |
| 1                      | 1            |
| 2                      | 2            |
| 3                      | 3            |
| 4                      | 4            |
| 5                      | 5            |
| 6                      | 6            |
| 7                      | 7            |
| 8                      | 8            |
| 9                      | 9            |
| 10                     | 10           |
| 11                     | 11           |
| 12                     | 12           |
| 13                     | 13           |
| 14                     | 14           |
| 15                     | 15           |
| 16                     | 16           |

A cumulative frequency curve (Lee diagram) showing size of loss on the Y-axis and cumulative claim count on the X-axis.

The curve is a step function (with argument along the vertical axis) which has a jump of  $n_i$  at the point  $x_i$ . Consider the shaded vertical strip in the graph. It has an area equal to  $n_i x_i$ . Summing all such vertical strips we have

$$\text{Total amount of loss} = n_1 x_1 + \dots + n_k x_k.$$

We may therefore interpret the area of the vertical strip corresponding to  $x_i$  as the amount of loss of size  $x_i$ , and the total enclosed area below the cumulative frequency curve as the total amount of loss.

In fact, we have a new way of viewing the cumulative frequency function curve. This curve can be constructed by arranging the losses in ascending order of magnitude, and laying them from left to right with each loss occupying a unit horizontal length.

Now let  $X$  be a random variable representing the amount of loss incurred by a risk. Define the cumulative distribution function (cdf)  $F(x)$  as

$$F(x) = \Pr(X \leq x).$$

Exhibit 3.5 shows the graph of a continuous cdf. Consider the vertical strip in the graph, with area  $xdF(x)$ . If we sum up all these strips, we will obtain the expected value of  $X$  (where  $E\{X\}$  represents the expected value of a random variable  $X$ ),

$$E\{X\} = \int_0^\infty x dF(x),$$

which is represented by the enclosed area below the cdf curve (the shaded area in the graph). We may interpret the expected loss as composed of losses of different sizes, and the strip  $xdF(x)$  as the contribution from losses of size between  $x$  and  $x+dx$ .

Exhibit 3.5. CDF Curve and Expectation

![A graph illustrating the relationship between the Size of Loss (Y-axis) and the Cumulative Distribution Function F(x) (X-axis). The curve starts at the origin (0,0) and increases monotonically, ending at (1,1). A vertical strip is shown at a point x_i on the X-axis, with its height labeled x_i dF(x). The area under the curve is shaded with diagonal lines, representing the total expected loss. The X-axis is labeled F(x) and ranges from 0 to 1. The Y-axis is labeled 'Size of Loss'.](468ad549a121ee06a5aa05e6915b7c39_img.jpg)

A graph illustrating the relationship between the Size of Loss (Y-axis) and the Cumulative Distribution Function F(x) (X-axis). The curve starts at the origin (0,0) and increases monotonically, ending at (1,1). A vertical strip is shown at a point x\_i on the X-axis, with its height labeled x\_i dF(x). The area under the curve is shaded with diagonal lines, representing the total expected loss. The X-axis is labeled F(x) and ranges from 0 to 1. The Y-axis is labeled 'Size of Loss'.

We can readily modify this diagram to visualize limits and deductibles:

##### *Limits:*

Consider a coverage which pays for losses up to a limit  $L$  only. Exhibit 3.6(a) shows that a loss of size not more than  $L$ , such as  $S_1$ , is paid in full, while a loss of size  $S_2$  which is greater than  $L$ , is paid only an amount  $L$ . By summing up vertical strips as before, except that strips with length greater than  $L$  are limited to length  $L$ , we obtain the expected payment per loss under such a coverage as the shaded area in Exhibit 3.6(a).

##### *Deductibles:*

Likewise, a coverage which pays for losses subject to a flat deductible  $D$  and up to limit  $L$  has expected payment per loss represented by the shaded area in Exhibit 3.6(b).

Exhibit 3.6. Expected Loss with (a) Limit and (b) Deductible

![Two graphs, (a) and (b), illustrating expected loss with a limit and a deductible.](b9f1f5c5167e357277b530940312d9ed_img.jpg)

The figure consists of two side-by-side graphs, labeled (a) and (b). Both graphs have a vertical axis labeled 'Size of Loss' and a horizontal axis with tick marks at 0,  $S_1$ ,  $S_2$ , and 1. A curve starts at the origin (0,0) and increases monotonically, concave down, ending at (1,1). In graph (a), a horizontal dashed line is drawn at height  $L$  on the vertical axis. The area under the curve from  $x=0$  to  $x=1$  is shaded with diagonal lines. A vertical line is drawn at  $x=S_1$ , which is to the left of the  $L$  line, and another vertical line is drawn at  $x=S_2$ , which is to the right of the  $L$  line. In graph (b), a horizontal dashed line is drawn at height  $D$  on the vertical axis. The area under the curve from  $x=0$  to  $x=1$  is shaded with diagonal lines. A horizontal dashed line is also drawn at height  $L$  on the vertical axis, which is above the  $D$  line.

Two graphs, (a) and (b), illustrating expected loss with a limit and a deductible.

We have shown the integral along the x-axis, but as with any other measurement of area, one could just as well integrate in horizontal slices along the y-axis. One method is often easier than the other in actual practice, depending on what data is available and what curves are used to estimate the underlying process.

A vertical strip has area  $x dF(x)$ , and we define

$$S(x) = 1 - F(x).$$

So a horizontal strip has area  $S(x) dx$ , as shown in Exhibit 3.7(a).

Exhibit 3.7. Size and Layer Views of Losses

![Exhibit 3.7. Size and Layer Views of Losses. Two graphs, (a) and (b), illustrating the size and layer views of losses. Graph (a) shows a curve starting at (0,0) and ending at (1,1). A vertical strip of width dx at position F(x) has area x dF(x). A horizontal strip of height dx at position x has area S(x) dx. Graph (b) shows the same curve with a shaded region between x=a and x=b, representing the expected loss in that layer.](7bbc8cb3417e534d01e969cbc5f3d891_img.jpg)

Graph (a) shows a curve starting at (0,0) and ending at (1,1). A vertical strip of width  $dx$  at position  $F(x)$  has area  $x dF(x)$ . A horizontal strip of height  $dx$  at position  $x$  has area  $S(x) dx$ . Graph (b) shows the same curve with a shaded region between  $x=a$  and  $x=b$ , representing the expected loss in that layer.

Exhibit 3.7. Size and Layer Views of Losses. Two graphs, (a) and (b), illustrating the size and layer views of losses. Graph (a) shows a curve starting at (0,0) and ending at (1,1). A vertical strip of width dx at position F(x) has area x dF(x). A horizontal strip of height dx at position x has area S(x) dx. Graph (b) shows the same curve with a shaded region between x=a and x=b, representing the expected loss in that layer.

Summing up the vertical strips and the horizontal strips separately must give us the same area, so we have

$$\int_0^\infty x dF(x) = \int_0^\infty S(x) dx = E\{X\}$$

This result can also be derived algebraically via integration by parts.

The two modes of summation correspond, in fact, to two views of the losses. The vertical strips group losses by size, whereas the horizontal strips group the loss amounts by layer. We may therefore call them the size method and the layer method. It is often more convenient to evaluate the expected loss in a layer by layer fashion, i.e., summing horizontal strips, than by the size method, i.e., summing vertical strips. For example, consider the layer of loss between  $a$  and  $b$  in Exhibit 3.7(b). The expected loss in this layer is represented by the shaded area. The layer method of summation gives simply

$$\int_a^b S(x) dx.$$

To express this integral by the size method is more difficult. However, some reflection, with the help of Exhibit 3.7(b), yields the following expression for the integral:

$$\int_a^b x dF(x) + bS(b) - aS(a).$$

Again, the equality of the two expressions can be established via integration by parts.

The more complicated expression derived from the size method is the form commonly found in the literature. Although the integral associated with the layer method is simple in form,  $S(x)$  is a function that is generally more difficult to integrate. This disadvantage vanishes, however, when the distribution is given numerically, as, for example, when actual experience is used. The retrospective rating Table M and Table L have been constructed by the layer method, as described in subsequent sections of this chapter; see also Simon<sup>25</sup> and Skurnick.<sup>26</sup>

#### 2.2. Lee Diagrams of Aggregate Loss Distributions

Lee diagrams are a very effective way to visualize aggregate policy provisions. They can be used — looking at an individual policy — to keep track of who owes what when, and also to visualize the outcome of a large group of similar policies, to aid in calculating expected aggregate excess losses.

In practice, when pricing aggregate policy provisions, the actuary needs actual numbers, and those are commonly pre-calculated, or estimated with an accessible set of formulas. This study note will show how such factors can be calculated. It will start by considering the simple case, where there is no per-occurrence loss limitation. It will later consider the more general cases where a policy might have both per-occurrence and aggregate loss limitations, looking at limited Tables M and Table L.

The mathematical basis of Table M is a distribution of entry ratios and its underlying distribution of aggregate losses. Recall from Section 1.2 that  $r$  is the entry ratio (actual loss divided by expected loss).

$$\text{Insurance Charge at } r = X = \phi(r) = \int_r^\infty (y - r)f(y)dy$$

$$\text{Insurance Savings at } r = S = \psi(r) = \int_0^r (r - y)f(y)dy$$

$$S = X + r - 1 \text{ or } \psi(r) = \phi(r) + r - 1$$

(To be derived subsequently).

In estimating the expected aggregate excess loss, we need to consider the distribution of outcomes of the total claims on a policy. As with severity distributions, it can be helpful to visualize the data to gain an intuitive understanding of how the elements relate to each other. We can draw a picture, remembering that we are graphing the probability distribution of aggregate losses (which can be thought of as multiple simulations of a single policy).

<sup>25</sup> LeRoy J. Simon, “1965 Table M,” *PCAS* LII, 1965, p. 1.

<sup>26</sup> David Skurnick, “The California Table L,” *PCAS* LXI, 1974, p. 117.

Exhibit 3.8. Functions in Retrospective Rating

![A graph showing the cumulative distribution function F(y) against the entry ratio y. The y-axis is labeled 'Entry Ratio' and has a point 'r'. The x-axis is labeled 'F(y)' and has points '0' and '1'. A curve starts at (0,0) and ends at (1,1). A horizontal dashed line at y=r intersects the curve. The area under the curve to the left of this line is labeled ψ(r). The area to the right is labeled 1-φ(r). The area above the curve and below the line y=r is labeled φ(r).](851d99765a6fe09d94a024c53bd9fe40_img.jpg)

A graph showing the cumulative distribution function F(y) against the entry ratio y. The y-axis is labeled 'Entry Ratio' and has a point 'r'. The x-axis is labeled 'F(y)' and has points '0' and '1'. A curve starts at (0,0) and ends at (1,1). A horizontal dashed line at y=r intersects the curve. The area under the curve to the left of this line is labeled ψ(r). The area to the right is labeled 1-φ(r). The area above the curve and below the line y=r is labeled φ(r).

In Exhibit 3.8 the cdf  $F(y)$  is graphed against the entry ratio  $y$ . The functions  $\phi(r)$  and  $\psi(r)$  are represented by the areas indicated in the graph. A number of mathematical properties are now clearly demonstrated.

- (1) By definition, the bounded area below the  $F(y)$  curve is equal to 1. Hence  $\phi(0) = 1$ .
- (2)  $\phi(r)$  is a decreasing function of  $r$ , and  $\phi(r) \rightarrow 0$  as  $r \rightarrow \infty$ .
- (3)  $\psi(r)$  is an increasing function of  $r$ ; its value is unbounded as  $r \rightarrow \infty$ .
- (4) Consider a small strip at  $y=r$  in the graph. This shows that an increment  $dr$  from  $r$  will yield a decrease  $S(r)dr$  in  $\phi(r)$ . Hence

$$\phi'(r) = (d/dr) \phi(r) = -S(r).$$

Using the fact that  $S'(x) = -f(x)$ , a second differentiation yields

$$\phi''(r) = f(r),$$

where  $f(r)$  is the density function of the entry ratio.<sup>27</sup> Similarly, we may deduce from Exhibit 3.8 that

$$\psi'(r) = (d/dr) \psi(r) = F(r)$$

and

$$\psi''(r) = f(r).$$

- (5) Consider the area of the rectangle on the interval from 0 to  $r$  in Exhibit 3.8. This gives the relation

$$r = [1 - \phi(r)] + \psi(r)$$

or

$$\psi(r) = \phi(r) + r - 1; \quad (\text{Formula 3.1})$$

this is a fundamental relation connecting  $\psi(r)$  and  $\phi(r)$ .

In general, consider a policy that has both a minimum ratable loss and a maximum ratable loss. Let  $L$  be the aggregate loss subject to a minimum of  $r_1E$  and a maximum of  $r_2E$ . So:

<sup>27</sup> Nels M. Valerius, "Risk Distributions Underlying Insurance Charges in the Retrospective Rating Plan," *PCAS* XXIX, 1942, p. 96.

$$L = \begin{cases} r_1 E & \text{if } A \leq r_1 E \\ A & \text{if } r_1 E \leq A \leq r_2 E \\ r_2 E & \text{if } r_2 E \leq A \end{cases}$$

If the actual loss is less than  $r_1 E$ ,  $L$  equals  $r_1 E$ , the minimum loss. If the actual loss falls between  $r_1 E$  and  $r_2 E$ ,  $L$  will be the actual loss. If the actual loss exceeds  $r_2 E$ , the maximum loss,  $L$  will be  $r_2 E$ .

Then a result more general than Formula 3.1 can also be obtained quite easily from examining Exhibit 3.9.

Exhibit 3.9. Expectation of Insured Loss (L) in Retrospective Rating

![A graph showing the relationship between Entry Ratio (y-axis) and F(y) (x-axis). The y-axis has labels 0, r1, and r2. The x-axis has labels 0 and 1. A curve starts at (0,0) and increases. A horizontal dashed line at r1 intersects the curve, and the area under the curve from 0 to this point is shaded and labeled ψ(r1). Another horizontal dashed line at r2 intersects the curve, and the area under the curve from 0 to this point is shaded and labeled φ(r2). The area between the two shaded regions is also shaded.](9fe11419dec507724d0362eb31c7b217_img.jpg)

A graph showing the relationship between Entry Ratio (y-axis) and F(y) (x-axis). The y-axis has labels 0, r1, and r2. The x-axis has labels 0 and 1. A curve starts at (0,0) and increases. A horizontal dashed line at r1 intersects the curve, and the area under the curve from 0 to this point is shaded and labeled ψ(r1). Another horizontal dashed line at r2 intersects the curve, and the area under the curve from 0 to this point is shaded and labeled φ(r2). The area between the two shaded regions is also shaded.

The shaded area in Figure 3.9 represents the quantity  $E\{L\}/E$  and we have

$$E\{L\}/E = \psi(r_1) + \phi(r_2) = 1,$$

or

$$E\{L\}/E = 1 + \psi(r_1) - \phi(r_2). \quad (\text{Formula 3.2})$$

See Skurnick.<sup>28</sup>

Lee diagrams can also be used to motivate the derivation of key formulas used in Retrospective Rating.

(Note that for ease of exposition, we ignore the tax factor in this chapter. Real premium calculations, would, of course, include a component for taxes.<sup>29</sup>)

Recall from Chapter 2 that in a Retrospective Rating Plan, the retrospective premium  $R$  is given by

$$R = B + cA,$$

where  $B$  is the basic premium and  $c$  is the loss conversion factor (LCF), and where  $B$  is alternatively represented by

$$B = bP,$$

with  $P$  as the standard premium (before any applicable expense gradation) and  $b$  as the basic premium ratio.

For this section, we will assume the policy is subject to a maximum premium  $G$  and a minimum premium  $H$ .

Let  $L_G$  be actual loss that will produce the maximum premium:

$$G = B + cL_G$$

and let

<sup>28</sup> David Skurnick, "The California Table L," *PCAS LXI*, 1974, p. 117.

<sup>29</sup> The otherwise calculated retrospective premium would be multiplied by  $T$ , which is called the tax multiplier. Chapter 2 shows this more complete version of the formula.

$$r_G = L_G/E.$$

Similarly, define  $L_H$  to be

$$H = B + cL_H,$$

$$r_H = L_H/E.$$

Further, let

$$L = \begin{cases} L_H & \text{if } A \leq L_H \\ A & \text{if } L_H \leq A \leq L_G \\ L_G & \text{if } L_G \leq A \end{cases}$$

So if the actual loss is less than  $L_H$ ,  $L$  equals  $L_H$ , the minimum ratable loss. If the actual loss falls between  $L_H$  and  $L_G$ ,  $L$  will be the actual loss. If the actual loss exceeds  $L_G$ , the maximum ratable loss,  $L$  will be  $L_G$ .

Then the retrospective premium can be represented by

$$R = B + cL.$$

If we identify  $r_H$  and  $r_G$  with  $r_1$  and  $r_2$ , respectively, then Exhibit 3.10 shows the quantity  $E\{L\}/E$  as the area of the shaded region OFDCBA.

Exhibit 3.10. Retrospective Rating Premium

![A graph titled 'Exhibit 3.10. Retrospective Rating Premium'. The vertical axis is labeled 'Entry Ratio' and has points 0, r_H, and r_G. The horizontal axis is labeled 'y' and has points 0 and F. A curve starts at the origin (0,0) and increases, passing through point B on the r_H line and point C on the r_G line. The area under the curve is divided into two shaded regions: a lower region with diagonal hatching from bottom-left to top-right, and an upper region with cross-hatching. Point A is on the r_H line at x=0. Point D is on the r_G line at x=F. Point E is on the r_H line at x=F. The lower shaded region is bounded by the y-axis, the r_H line, the curve, and the vertical line at x=F. The upper shaded region is bounded by the curve, the r_G line, and the vertical line at x=F.](78fcfedad60b6dd255b4cc3c69d02c62_img.jpg)

A graph titled 'Exhibit 3.10. Retrospective Rating Premium'. The vertical axis is labeled 'Entry Ratio' and has points 0, r\_H, and r\_G. The horizontal axis is labeled 'y' and has points 0 and F. A curve starts at the origin (0,0) and increases, passing through point B on the r\_H line and point C on the r\_G line. The area under the curve is divided into two shaded regions: a lower region with diagonal hatching from bottom-left to top-right, and an upper region with cross-hatching. Point A is on the r\_H line at x=0. Point D is on the r\_G line at x=F. Point E is on the r\_H line at x=F. The lower shaded region is bounded by the y-axis, the r\_H line, the curve, and the vertical line at x=F. The upper shaded region is bounded by the curve, the r\_G line, and the vertical line at x=F.

It then follows that

$$\begin{aligned} E\{L\} &= E - \phi(r_G) E + \psi(r_H) E \\ &= E - I, \end{aligned}$$

where

$$I = [\phi(r_G) - \psi(r_H)]E$$

is called the net insurance charge of Table M. If the plan is to cover the expected costs of the policy, the expected retrospective premium must be equal to the sum of the total expenses,  $e$ , and the expected loss,  $E$ :

$$E\{R\} = e + E.$$

On the other hand, it also follows from the above that

$$E\{R\} = B + c(E - I).$$

Equating these two quantities we obtain the basic premium in terms of the expense, expected loss, and the net insurance charge:

$$B + c(E - I) = e + E$$

or

$$B = e - (c - 1)E + cI. \quad (\text{Formula 3.3})$$

A formula relating the charge difference to the minimum premium, expected loss and expense provision has been used to facilitate the determination of retrospective rating values from specified maximum and minimum premiums. This formula can be derived with the help of Figure 3.11 below.

Consider the equation

$$R = B + cL$$

Taking the expectation of both sides, recalling that  $E\{R\} = e + E$ , and representing the expectation  $E\{L\}/E$  by the shaded area of Exhibit 3.11 (areas U and V combined, equivalent to OFDCBA in Exhibit 3.10)

Exhibit 3.11. Retrospective Rating Premium

![A graph titled 'Exhibit 3.11. Retrospective Rating Premium'. The vertical axis is labeled 'Entry Ratio' and has points 0, r_H, and r_G. The horizontal axis is labeled 'y' and has points 0 and F. A curve starts at point B on the r_H line and rises to point C on the r_G line. A horizontal line at r_H is labeled A at the y-axis and E at point F. A horizontal line at r_G is labeled D at point F. The area under the curve from B to C is shaded and labeled U. The area under the r_H line from 0 to F is shaded and labeled V.](55086c71bc8ee4c0abc7160d26a8092c_img.jpg)

A graph titled 'Exhibit 3.11. Retrospective Rating Premium'. The vertical axis is labeled 'Entry Ratio' and has points 0, r\_H, and r\_G. The horizontal axis is labeled 'y' and has points 0 and F. A curve starts at point B on the r\_H line and rises to point C on the r\_G line. A horizontal line at r\_H is labeled A at the y-axis and E at point F. A horizontal line at r\_G is labeled D at point F. The area under the curve from B to C is shaded and labeled U. The area under the r\_H line from 0 to F is shaded and labeled V.

we have

$$e + E = B + cE[U+V].$$

On the other hand, we have for the minimum premium H:

$$\begin{aligned} H &= B + cEr_H \\ &= B + cE [V]. \end{aligned}$$

Taking the difference on both sides of the two equations above we have

$$\begin{aligned} (e + E) - H &= cE[U] \\ &= cE [\phi(r_H) - \phi(r_G)]. \end{aligned}$$

Or

$$\phi(r_H) - \phi(r_G) = \frac{(e + E) - H}{cE} \quad (\text{Formula 3.4})$$

We can also derive a formula relating the entry ratios themselves to the major plan parameters.

The losses at the minimum premium are  $r_H E$ . So

$$H = cr_H E + B.$$

Similarly, the losses at the maximum premium are  $r_G E$ . So

$$G = cr_G E + B.$$

Subtracting these two equations you find

$$G - H = cE(r_G - r_H)$$

or

$$r_G - r_H = \frac{G - H}{cE} \quad (\text{Formula 3.5})$$

Formulas 3.4 and 3.5 can be used to determine the rating values given the maximum and minimum premiums. They are commonly referred to as the balance equations for aggregate losses.

One may interpret the difference in charge,  $\phi(r_H) - \phi(r_G)$ , as indicated by area U in Exhibit 3.11, to be the difference between the expected retrospective premium and the minimum premium, apart from conversion factor  $cE$ .



#### Questions

5. Label each of the three areas, A, B, and C in the Lee diagram below in terms of the Insurance Charge and the Insurance Savings.

![Lee diagram for question 5 showing a curve from (0,0) to (1,1) with a horizontal dashed line at entry ratio r.](a7d6560ff54237234261b647f30ec25c_img.jpg)

A Lee diagram with a vertical axis labeled 'y' and 'Entry Ratio' and a horizontal axis labeled 'F(y)' and '1'. A curve starts at the origin (0,0) and ends at (1,1). A horizontal dashed line is drawn at an entry ratio of  $r$ . The area between the curve and the horizontal line is labeled 'A'. The area between the horizontal line and the x-axis is labeled 'C'. The area between the curve and the y-axis is labeled 'B'.

Lee diagram for question 5 showing a curve from (0,0) to (1,1) with a horizontal dashed line at entry ratio r.

6. For the Lee diagram below, identify the areas associated with

- (a) Insurance Charge at R
- (b) Insurance Charge at S
- (c) Insurance Savings at R
- (d) Insurance Savings at S

![Lee diagram for question 6 showing a curve from (0,0) to (1,1) with horizontal dashed lines at entry ratios R and S, and vertical dashed lines at F(y) values.](e2b57ed20df1cf724e0188b64870fe05_img.jpg)

A Lee diagram with a vertical axis labeled 'y' and 'Entry Ratio' and a horizontal axis labeled 'F(y)' and '1'. A curve starts at the origin (0,0) and ends at (1,1). Two horizontal dashed lines are drawn at entry ratios  $R$  and  $S$ , where  $R > S$ . Two vertical dashed lines are drawn at  $F(y)$  values. The areas are labeled as follows: 'A' is the area above the curve and below the line  $R$ ; 'B' is the area between the curve and the line  $R$  to the left of the first vertical dashed line; 'C' is the area between the curve and the line  $R$  between the two vertical dashed lines; 'D' is the area between the curve and the line  $R$  to the right of the second vertical dashed line; 'E' is the area above the curve and below the line  $R$  to the right of the second vertical dashed line; 'F' is the area between the curve and the line  $S$  to the left of the first vertical dashed line; 'G' is the area between the curve and the line  $S$  to the left of the first vertical dashed line; 'H' is the area between the curve and the line  $S$  between the two vertical dashed lines; 'I' is the area between the curve and the line  $S$  to the right of the second vertical dashed line.

Lee diagram for question 6 showing a curve from (0,0) to (1,1) with horizontal dashed lines at entry ratios R and S, and vertical dashed lines at F(y) values.

### 3. Estimating Aggregate Loss Costs Using Table M

#### 3.1. How Table M is Used

To summarize: Table M contains insurance charges and savings by entry ratio and by size of policy, possibly by limit, and other key considerations.<sup>30</sup> The entry ratio is defined as the aggregate losses divided by the expected aggregate losses (unlimited, or limited in the case of a limited Table M). Because different sized policies will have very different aggregate loss distributions, they must be grouped by approximate size, usually determined either by expected loss or expected number of claims<sup>31</sup> to estimate an appropriate insurance charge. The mathematical basis of Table M is a distribution of entry ratios and its underlying distribution of aggregate losses.

$$\text{Insurance Charge at } r = X = \phi(r) = \int_r^{\infty} (y - r)f(y)dy$$

$$\text{Insurance Savings at } r = S = \psi(r) = \int_0^r (r - y)f(y)dy$$

$$S = X + r - 1 \text{ or } \psi(r) = \phi(r) + r - 1$$

For example, we might consider a workers' compensation insurance policy with expected aggregate losses of \$200,000. It is a loss-sensitive policy, with a limit of \$80,000 to the losses the insured is responsible for. That is, the maximum the insured will pay is the first \$80,000 of aggregate losses, and the insurer will pay the rest. The entry ratio for the aggregate limit is 0.4 (= \$80,000/\$200,000). Assume that in this example the Table M for this sized insured has a corresponding insurance charge of 0.72 for an entry ratio of 0.4. Then the loss cost of the aggregate deductible policy is \$144,000 (= \$200,000 \* 0.72), the expected losses to be owed by the insurer.

---

<sup>30</sup> Other key considerations include product being priced, types of losses covered, the jurisdiction where the policy is in force, etc. The size of the policy is highlighted because it has an enormous impact on the insurance charges and savings, as discussed later in this chapter.

<sup>31</sup> Grouping policies either by expected total loss (expected loss group) or expected number of claims (expected claim count group) serves the purpose of bucketing risks whose aggregate loss distributions have a similar variance component due to claim frequency. Grouping explicitly by expected number of claims has the advantage of getting at that aspect of the risk more directly, and is less subject to inflation. But the expected loss is a core element of any pricing exercise, and may be more readily available.

#### 3.2. *Empirical Construction of Table M*<sup>32</sup>

While Table M can now be stored electronically, often as a function (or set of functions) of the plan parameters, rather than as a giant look-up table, the starting point for developing those functions are empirical methods. It is instructive to understand how this is done.

In order to construct Table M empirically, the first step is to obtain data on the annual aggregate losses for many insureds. The data needs to be split into groups of insureds which are expected to have similar distribution of aggregate losses. A separate analysis should be done for each of these groups.

Ideally, this means the insureds have a similar frequency-of-loss distribution and have similar patterns of claim severity. In practice, actuaries usually group insureds that are similar in size and are subject to similar risks. (E.g., workers' compensation risks engaged in moderately hazardous activities with between 35 and 40 expected claims.)

For each group, we need actual aggregate losses for the year, or the actual aggregate loss ratios, or some other measure that will allow us to compare a group's aggregate loss experience with that of the average risk of the group.<sup>33</sup> Typically, we use the average of the actual aggregate losses as the expected loss for the group. Note that if we use some other estimate of expected, the empirically calculated  $\phi(0)$  will not equal 1.

The final published table of insurance charges is then organized by the groups examined (risk size and other key characteristics) as well as the entry ratio.

A representative sample of the data is shown in Exhibit 3.12, focusing on a single group.

---

<sup>32</sup> Section 3.2 is adapted from a study note by J. Eric Brosius, "Table M Construction," 2002, published by the Casualty Actuarial Society as part of the Syllabus of Exams.

<sup>33</sup> Developing those losses to ultimate without dampening the underlying variance is a complex problem which is beyond the scope of this study note, but which the practitioner should be aware of. A common solution is the use of a stochastic development procedure.

Exhibit 3.12.  
Experience for a Group of Risks with Approximately 500 Expected Claims (N)

| Risk | Actual Aggregate Loss |
|------|-----------------------|
| 1    | 1,000,000             |
| 2    | 2,500,000             |
| 3    | 3,000,000             |
| 4    | 3,500,000             |
| 5    | 4,000,000             |
| 6    | 4,000,000             |
| 7    | 4,500,000             |
| 8    | 5,000,000             |
| 9    | 7,500,000             |
| 10   | 15,000,000            |

The second step is to compute entry ratios. As defined previously, the entry ratio is the ratio of the actual aggregate losses to the expected aggregate losses. In the example above, the empirical average aggregate loss per policy is \$5M. So the entry ratios can be found as in Exhibit 3.13.

Exhibit 3.13.

Entry Ratios for a Group of Risks with  $N \sim 500$ ,  
and observed average aggregate loss of \$5,000,000

| Risk | Actual Aggregate Loss | Entry Ratio (r) |
|------|-----------------------|-----------------|
| 1    | 1,000,000             | 0.2             |
| 2    | 2,500,000             | 0.5             |
| 3    | 3,000,000             | 0.6             |
| 4    | 3,500,000             | 0.7             |
| 5    | 4,000,000             | 0.8             |
| 6    | 4,000,000             | 0.8             |
| 7    | 4,500,000             | 0.9             |
| 8    | 5,000,000             | 1.0             |
| 9    | 7,500,000             | 1.5             |
| 10   | 15,000,000            | 3.0             |

Then we will start to find the insurance charges in Table M. There are two methods for calculating the insurance charges: vertical slicing method and horizontal slicing method. The former is from the viewpoint of per risk, while the latter is from the viewpoint of per layer. It can be helpful to construct a Lee diagram of the data at this point.

Exhibit 3.14. Raw Data

![Bar chart showing Entry Ratio vs Percent for raw data. The y-axis is Entry Ratio (0.00 to 3.00) and the x-axis is Percent (0% to 100%). The bars show a step-like increase in entry ratio as the percent increases.](21529f776ea22c5048fc2d9e8e274b5c_img.jpg)

| Percent   | Entry Ratio |
|-----------|-------------|
| 0.0 - 0.2 | 0.2         |
| 0.2 - 0.4 | 0.5         |
| 0.4 - 0.6 | 0.6         |
| 0.6 - 0.8 | 0.7         |
| 0.8 - 1.0 | 0.8         |
| 1.0 - 1.2 | 0.8         |
| 1.2 - 1.4 | 0.9         |
| 1.4 - 1.6 | 1.0         |
| 1.6 - 1.8 | 1.5         |
| 1.8 - 2.0 | 3.0         |

Bar chart showing Entry Ratio vs Percent for raw data. The y-axis is Entry Ratio (0.00 to 3.00) and the x-axis is Percent (0% to 100%). The bars show a step-like increase in entry ratio as the percent increases.

##### (I) Vertical Slicing Method

We will explain the vertical slicing method first. In the example above, we will calculate the insurance charge of the entry ratio at 1.2, or  $\phi(1.2)$ .

Exhibit 3.15. Aggregate Excess at an Entry Ratio of 1.2

![Bar chart showing Aggregate Excess at an Entry Ratio of 1.2. The y-axis is Entry Ratio (0.00 to 3.00) and the x-axis is Percent (0% to 100%). A horizontal dashed line at r=1.2 is shown. The area above the line is shaded, with values 0.3 and 1.8 labeled.](67408c41c75d983c13a9bd3d66953f3c_img.jpg)

| Percent   | Entry Ratio | Excess (r=1.2) |
|-----------|-------------|----------------|
| 0.0 - 0.2 | 0.2         | 0.0            |
| 0.2 - 0.4 | 0.5         | 0.0            |
| 0.4 - 0.6 | 0.6         | 0.0            |
| 0.6 - 0.8 | 0.7         | 0.0            |
| 0.8 - 1.0 | 0.8         | 0.0            |
| 1.0 - 1.2 | 0.8         | 0.0            |
| 1.2 - 1.4 | 0.9         | 0.1            |
| 1.4 - 1.6 | 1.0         | 0.2            |
| 1.6 - 1.8 | 1.5         | 0.3            |
| 1.8 - 2.0 | 3.0         | 1.8            |

Bar chart showing Aggregate Excess at an Entry Ratio of 1.2. The y-axis is Entry Ratio (0.00 to 3.00) and the x-axis is Percent (0% to 100%). A horizontal dashed line at r=1.2 is shown. The area above the line is shaded, with values 0.3 and 1.8 labeled.

Exhibit 3.16. Calculation with vertical slices

| Risk | Actual Aggregate Loss | Entry Ratio ( r ) | Excess of r=1.2 |
|------|-----------------------|-------------------|-----------------|
| 1    | 1,000,000             | 0.2               | 0               |
| 2    | 2,500,000             | 0.5               | 0               |
| 3    | 3,000,000             | 0.6               | 0               |
| 4    | 3,500,000             | 0.7               | 0               |
| 5    | 4,000,000             | 0.8               | 0               |

|    |            |     |     |
|----|------------|-----|-----|
| 6  | 4,000,000  | 0.8 | 0   |
| 7  | 4,500,000  | 0.9 | 0   |
| 8  | 5,000,000  | 1   | 0   |
| 9  | 7,500,000  | 1.5 | 0.3 |
| 10 | 15,000,000 | 3   | 1.8 |

Then the average value of the excess column is the insurance charge of the entry ratio at 1.2. That is,  $\phi(1.2)=(0.3+1.8)/10=0.21$ . We can find the insurance charges for all the other entry ratios, using the same procedure. A Table M with an equal height of 0.1 can be constructed as below.

Exhibit 3.17. Table M: For  $N \sim 500$

| $r$ | $\phi(r)$ |
|-----|-----------|
| 0   | 1         |
| 0.1 | 0.9       |
| 0.2 | 0.8       |
| 0.3 | 0.71      |
| 0.4 | 0.62      |
| 0.5 | 0.53      |
| 0.6 | 0.45      |
| 0.7 | 0.38      |
| 0.8 | 0.32      |
| 0.9 | 0.28      |
| 1.0 | 0.25      |
| 1.1 | 0.23      |
| 1.2 | 0.21      |
| 1.3 | 0.19      |
| 1.4 | 0.17      |
| 1.5 | 0.15      |
| 1.6 | 0.14      |
| 1.7 | 0.13      |
| 1.8 | 0.12      |
| 1.9 | 0.11      |
| 2.0 | 0.1       |
| 2.1 | 0.09      |
| 2.2 | 0.08      |
| 2.3 | 0.07      |
| 2.4 | 0.06      |
| 2.5 | 0.05      |
| 2.6 | 0.04      |
| 2.7 | 0.03      |
| 2.8 | 0.02      |
| 2.9 | 0.01      |
| 3.0 | 0         |

It can be seen that it takes lots of work to calculate the insurance charges for all the entry ratios if the vertical slicing method is used, although it is easy to understand and explain.

##### (II) Horizontal Slicing Method

Now, we will introduce the other method of constructing Table M, the horizontal slicing method. In comparison with the former method, the latter method is much easier to calculate insurance charges for multiple entry ratios although to some extent it is less intuitive and harder to explain. This is exactly comparable to slicing a distribution horizontally (instead of vertically) on a Lee diagram, as shown in Exhibit 3.18

Exhibit 3.18. Horizontal Slices

![A horizontal bar chart titled 'Exhibit 3.18. Horizontal Slices'. The vertical axis is labeled 'Entry Ratio' and ranges from 0.00 to 3.00 in increments of 0.50. The horizontal axis is labeled 'Percent' and ranges from 0% to 100%. The chart displays 10 horizontal bars of increasing height from bottom to top. The bottom bar is at an entry ratio of 0.20 and extends to approximately 10% on the x-axis. Each subsequent bar is 0.10 units higher on the y-axis and extends further to the right. The top bar is at an entry ratio of 3.00 and extends to 100% on the x-axis.](9e4179ffe4701bec67534299c4935049_img.jpg)

| Entry Ratio | Percent |
|-------------|---------|
| 0.20        | 10%     |
| 0.30        | 20%     |
| 0.40        | 30%     |
| 0.50        | 40%     |
| 0.60        | 50%     |
| 0.70        | 60%     |
| 0.80        | 70%     |
| 0.90        | 80%     |
| 1.00        | 90%     |
| 3.00        | 100%    |

A horizontal bar chart titled 'Exhibit 3.18. Horizontal Slices'. The vertical axis is labeled 'Entry Ratio' and ranges from 0.00 to 3.00 in increments of 0.50. The horizontal axis is labeled 'Percent' and ranges from 0% to 100%. The chart displays 10 horizontal bars of increasing height from bottom to top. The bottom bar is at an entry ratio of 0.20 and extends to approximately 10% on the x-axis. Each subsequent bar is 0.10 units higher on the y-axis and extends further to the right. The top bar is at an entry ratio of 3.00 and extends to 100% on the x-axis.

The procedure of the horizontal slicing method of calculating Table M charges is shown in Exhibit 3.19. Starting from the entry ratio ( $r$ ) column, we find the number of risks in the group with the corresponding entry ratio as shown in the “# Risks” column. Then the “# Risks over  $r$ ” shows the number of risks which have entry ratios exceeding a given entry ratio. The “% Risks over  $r$ ” column converts the number in the “# Risks over  $r$ ” into a percentage basis by dividing by the total number of risks (here it is 10). The “Difference in  $r$ ” column shows the difference between the entry value in this row and the entry value in the next row. Finally, the last column in the table is the insurance charge. The last column begins from the bottom row which is 0 and then works up; the value in each row is equal to the value in the row beneath plus the product of the “% Risks over  $r$ ” and the “Difference in  $r$ ” in that row.

Exhibit 3.19. Calculation with horizontal slices

| r   | # Risks | # Risks<br>over r | % Risks<br>over r | Difference in r | $\phi(r)$            |
|-----|---------|-------------------|-------------------|-----------------|----------------------|
| 0   | 0       | 10                | 100%              | 0.2             | 1                    |
| 0.2 | 1       | 9                 | 90%               | $0.3=0.5-0.2$   | 0.8                  |
| 0.5 | 1       | 8                 | 80%               | $0.1=0.6-0.5$   | 0.53                 |
| 0.6 | 1       | 7                 | 70%               | 0.1             | 0.45                 |
| 0.7 | 1       | 6                 | 60%               | 0.1             | 0.38                 |
| 0.8 | 2       | 4                 | 40%               | 0.1             | 0.32                 |
| 0.9 | 1       | 3                 | 30%               | 0.1             | 0.28                 |
| 1.0 | 1       | 2                 | 20%               | 0.5             | $0.25=0.15+20\%*0.5$ |
| 1.5 | 1       | 1                 | 10%               | 1.5             | $0.15=0+10\%*1.5$    |
| 3.0 | 1       | 0                 | 0%                | 0               | 0                    |

Using the horizontal slicing method, we can construct a Table M with an equal height of 0.1, as shown previously in Exhibit 3.17. The results of the vertical and horizontal slicing methods are the same so long as we calculate horizontal slices at all the data points, because we use the same data. When a real Table M is constructed, the entry ratios are usually chosen so as to have intervals of 0.01 between rows.<sup>34</sup>

<sup>34</sup> If the entry ratios of the data points (the aggregate loss seen on a policy divided by the expected aggregate loss) falls between the “slices” chosen, we would not actually be adding the area of rectangles, and unless adjustments are made, the calculated charges will be slightly off. This is rarely a serious problem in real-life analyses, where many slices are used and there are enough observations that simple adjustments, such as adding the area of trapezoids instead of rectangles, and linearly interpolating between observed entry ratios, will yield adequate accuracy, but it can make a significant difference in the sort of simplified examples that might come up when studying this material. See question 7 for an example of this effect.

Finally, we can also calculate the insurance savings for each entry ratio by using the formula  $\psi(r) = \phi(r) + r - 1$ . If the observed data does not match all entry ratios we want in our table, we can interpolate. Exhibit 3.20 was developed by linearly interpolating the values in Exhibit 3.19. For example, the charge at 0.3 is gotten by linearly interpolating between the charges at 0.2 and 0.5 of 0.8 and 0.53 respectively:

$$(2/3)(0.8) + (1/3)(0.53) = 0.71.$$

Thus, the Table M with an equal height of 0.1 can be constructed as shown in Exhibit 3.20.

Exhibit 3.20. Table M: For  $N \sim 500$

| r   | $\phi(r)$ | $\psi(r)$ |
|-----|-----------|-----------|
| 0   | 1         | 0         |
| 0.1 | 0.9       | 0         |
| 0.2 | 0.8       | 0         |
| 0.3 | 0.71      | 0.01      |
| 0.4 | 0.62      | 0.02      |
| 0.5 | 0.53      | 0.03      |
| 0.6 | 0.45      | 0.05      |
| 0.7 | 0.38      | 0.08      |
| 0.8 | 0.32      | 0.12      |
| 0.9 | 0.28      | 0.18      |
| 1.0 | 0.25      | 0.25      |
| 1.1 | 0.23      | 0.33      |
| 1.2 | 0.21      | 0.41      |
| 1.3 | 0.19      | 0.49      |
| 1.4 | 0.17      | 0.57      |
| 1.5 | 0.15      | 0.65      |
| 1.6 | 0.14      | 0.74      |
| 1.7 | 0.13      | 0.83      |
| 1.8 | 0.12      | 0.92      |
| 1.9 | 0.11      | 1.01      |
| 2.0 | 0.1       | 1.1       |
| 2.1 | 0.09      | 1.19      |
| 2.2 | 0.08      | 1.28      |
| 2.3 | 0.07      | 1.37      |
| 2.4 | 0.06      | 1.46      |
| 2.5 | 0.05      | 1.55      |
| 2.6 | 0.04      | 1.64      |
| 2.7 | 0.03      | 1.73      |
| 2.8 | 0.02      | 1.82      |
| 2.9 | 0.01      | 1.91      |
| 3.0 | 0         | 2         |

#### 3.3. *Calculating Table M from a parameterized aggregate loss distribution*

In many cases, the aggregate loss distribution can be modeled by parameterized functions which are amenable to manipulation. In a very simple example, one might assume that the number of claims can be modeled by a Poisson distribution and the severity of resulting claims can be modeled by a Pareto distribution. Or the aggregate loss distribution might be directly approximated using a lognormal distribution.

This might be done for a reinsurance contract, where there is not a statistically credible body of similar policies that can be used to construct an empirical aggregate loss density function. The actuary might, however, have evidence that similar policies tend to have loss frequency and severity distributions of certain general types, and might have nothing better on which to base their prices than the results of fitting the available claim data to those types of distributions. When data is thin, pricing actuaries should be careful to test the sensitivity of their loss cost estimates to a variety of assumptions. Even with an abundance of data, parameterized functions make it easy to develop a large number of consistent insurance charges.

Once the underlying frequency and severity distributions have been selected, the aggregate loss distribution can be simulated or, in many cases, calculated using a variety of closed-form methods. In either case, the resulting aggregate loss distribution can be used to generate Table M charges according to the horizontal slicing method described above. Chapter 4 of the CAS monograph “Distributions for Actuaries” by David Bahnemann discusses these methods, and those calculations are beyond the scope of this study note.<sup>35</sup>

In practice, a hybrid of empirical data and models is often used. For example, in order to accumulate enough data to have reasonably credible groups, we might not be able to split the data into buckets small enough to provide accurate charges across the whole range of the data. So the data might be split into a modest number of large groups, whose aggregate loss distribution can be fitted to parameterized distributions. In doing this, it is best to look at each policy’s aggregate loss as a ratio to its expected loss, so as not to introduce extra variation due to the different expectations of loss. Once an empirical distribution is found, parameterized curves can be fit to it. Then the parameters can be interpolated to generate aggregate loss distributions for smaller, more homogeneous groups. The details of these procedures are beyond the scope of this study note, but the actuary should be aware that issues of loss development,<sup>36</sup> trend, and the heterogeneous nature of the underlying exposures all need to be considered.

#### Questions

7. Eight identical risks incur the following actual aggregate loss ratios, respectively:  
20% 40% 40% 60% 80% 80% 120% 200%

Assume that the expected loss ratio for those risks is the observed average loss ratio.

- (a) Construct a Table M showing the insurance charge for entry ratios from 0 to 3.0 in increments of 0.5.

---

<sup>35</sup> Two methods that have been used to create aggregate distributions from underlying frequency and severity distributions are the recursive method, described by Harry Panjer, “Recursive Evaluation of a Family of Compound Distributions,” *Astin Bulletin*, Vol. 12, No. 1, 1981, pp. 22-26 and the Heckman-Meyers method, described by Philip E. Heckman and Glenn G. Meyers in “The Calculation of Aggregate Loss Distributions from Claim Severity and Claim Count Distributions,” *PCAS* LXX, 1983.

See also D. Bahnemann, “Distributions for Actuaries,” CAS Monograph # 2, Chapter 4.

<sup>36</sup> Some discussion of these topics can be found in H. C. Mahler, Discussion of “Retrospective Rating: 1997 Excess Loss Factors,” *PCAS* LXXXV, 1998, pp. 316-344.

- (b) Calculate the Insurance Charge at a 70% loss ratio.
- (c) Calculate the Insurance Savings at a 70% loss ratio.
- (d) Calculate the Insurance Charge at a 110% loss ratio.
- (e) Calculate the Insurance Savings at a 110% loss ratio.

8. What are some advantages and disadvantages of using parameterized distributions to develop Tables M?

### 4. Estimating Limited Aggregate Excess Loss Costs<sup>37</sup>

#### 4.1. Introduction of Limited Aggregate Deductible Policies

The original Table M was developed for retrospectively rated workers' compensation policies, and for historical reasons it was originally calculated based on aggregate losses with no per-claim limit.

But we often want to price aggregate insurance charges on limited losses. For example, a large dollar deductible workers' compensation policy might have a per-occurrence limit to ratable losses (or deductible) of \$100,000 for each loss occurring to it. When the amount of a claim<sup>38</sup> is less than \$100,000, the insured is responsible for the amount of the claim. If the amount of a claim exceeds the per-occurrence limit of \$100,000, the insured will only be responsible for the first \$100,000 of the loss.

However, if the insured also wanted to limit its total liability, it may also have negotiated an aggregate deductible limit of \$250,000, so the insured would never have to pay more than \$250,000 in losses occurring on this policy, regardless of actual experience. The policy could reach that limit if there are more than two claims larger than \$100,000, or if there are lots of small claims, or some combination of the two. In this situation, the actuary needs to calculate the limited aggregate excess charge.

In pricing the loss portion of a deductible policy with an aggregate deductible limit, or a retrospectively rated policy with a per-occurrence limit, the actuary can either price for the excess losses and the aggregate deductible losses simultaneously (as is done in the California Table L, discussed in section 5) or can charge separately for losses in excess of the deductible and for the deductible losses in excess of the aggregate limit. We will first consider calculating the two charges separately—directly calculating a Table M appropriate to aggregate limited losses, which produces charges suitable to add to per-occurrence excess loss charges. We will then consider other methods of pricing such policies in section 5.

The following text will use the notation "limited Table M," or "Table M<sub>D</sub>" where D is the limit or deductible amount to refer to a table of charges for the aggregate of limited losses.

#### 4.2. Considerations for Table M<sub>D</sub>

Often it is expedient to calculate the charges for the per-occurrence excess and the aggregate excess separately. The actuary might have enough data to update the estimate for the per-occurrence excess more frequently than the aggregate excess charge, or might have reasons to rely on different data sources for the two calculations. Both ISO and the NCCI take this approach for policies with a per-loss limitation on their retro plans, including an excess loss premium factor in addition to the Table M charge.

Throughout this section, we assume that the per-occurrence excess charge is known, and has been calculated based on losses not subject to an aggregate limit. So as not to double-count losses that might be subject to either the per-occurrence or the aggregate limit, the limited aggregate excess loss charge must be developed or estimated based on the distribution of limited losses, that is, losses to which the per-occurrence limit has already been applied.

---

<sup>37</sup> Section 4 is adapted from a study note by Ginda Kaplan Fisher, "Pricing Aggregates on Deductible Policies," 2002, published by the Casualty Actuarial Society as part of the Syllabus of Exams.

<sup>38</sup> This chapter assumes that a single insured occurrence will generate at most one claim, which would be subject to the per-occurrence limit. In real insured events, an occurrence can generate multiple claims which might apply to one or more insurance policies and interact with the limits of those policies in complicated ways. However, those details are beyond the scope of this study note.

For example, consider a policy which has a per-occurrence limit of \$100,000 and an aggregate deductible limit of \$250,000. Four claims occur:

\$50,000

\$50,000

\$50,000

\$300,000

After the first three claims, the insured is responsible for paying \$150,000. Then the \$300,000 claim occurs. The insured is only responsible for the first \$100,000 of loss on that claim. But is the other \$200,000 excess of the aggregate limit, or of the per-occurrence limit? This is an example of the overlap of the per-occurrence limit (deductible) and aggregate limit. It is customary to apply the per-occurrence limit first, so those \$200,000 are considered excess of the per-occurrence limit, and should be contemplated in the per-occurrence excess charge.

If the actuary calculated Table M charges without limiting the aggregate losses for the effect of the \$100,000 deductible, those \$200,000 would increase the Table M charge, and there would be an overlap between the Table M charge and the per-occurrence excess charge, leading to inappropriate Table M charges. Simply limiting the aggregate losses for the effect of the \$100,000 deductible before using any of the methods above to estimate Table M removes this problem.<sup>39</sup>

Actuaries can determine limited aggregate excess charges through the same methods used for any other aggregate excess loss: they can gather a large body of policy data which is expected to be similar to that for the policies being priced and build an empirical table or they can use information about the expected distribution of losses to model the charges.

The shape of the distribution of limited (or primary) losses is different from the shape of the distribution of the same losses when not subject to a limit<sup>40</sup>, as the severity distribution can be quite different—nevertheless, it is just another loss distribution. In particular, all the same relationships used in constructing Table M charges apply to calculating limited loss insurance charges, as described above.

Because the size of the deductible has an impact on the shape of the aggregate loss distribution, a separate table  $M_D$  must be calculated for a wide range of deductibles, spanning the range of deductibles offered. Fortunately, this does not require masses of data at every deductible or loss limit. If the unlimited losses are known (as is often the case with both retrospectively rated and large deductible plans) the same losses can be used to calculate Table M charges at any limit simply by limiting each loss before adding it to the aggregate used. The actuary should be careful to limit individual occurrences prior to aggregating the losses of each policy.

In general, the lower the deductible (or the smaller the per-occurrence limit), the less variance there is in the severity distribution and thus the less variance there is in the resulting limited aggregate loss. This is because loss distributions tend to be positively skewed, with many small losses and few large losses. Therefore much of the variance of the severity distribution is driven by the extreme (high) losses, and after the application of the per-occurrence limit, the variance of severity is reduced. (Limiting the losses does not change the frequency distribution.) The reduction in variance of limited aggregate losses reduces the probability of unusually large

---

<sup>39</sup> Note that adjusting the excess charges to remove aggregate losses would be a much more complicated process, and would mean that excess charges would depend on the size of the policy, and not just the severity distribution of the losses.

<sup>40</sup> Or when subject to a much higher policy limit.

limited aggregate losses in a given year. Therefore, lower deductibles usually lead to lower insurance charges for entry ratios greater than 1.

#### *4.3. Construction of Table $M_D$*

When working with a limited Table M, it is important to remember to use limited losses consistently. The expected losses used in calculating the entry ratio must be the expected deductible (or limited) losses, and not the total expected ground-up losses on the policy.

For example, an insured has a per-occurrence deductible of \$250,000 and its expected limited aggregate losses are \$800,000. The aggregate deductible limit is \$1,000,000. First, we need to compute the appropriate entry ratio,  $r$ :

$$1.25 = r = \$1,000,000 / \$800,000$$

Assume that the insurance charge for an entry ratio of 1.25 in Table  $M_D$  with a per-occurrence limit of \$250,000 is 0.18. Then the loss cost of the aggregate deductible limit is \$144,000 ( $=\$800,000 * 0.18$ ).

The methods of constructing a Limited Table M or Table  $M_D$  are the same as those of constructing a standard Table M, except that the data of aggregate losses are required to be the limited aggregate losses rather than the unlimited aggregate losses. Therefore, in Table  $M_D$  the entry ratio ( $r$ ) is defined as the actual limited aggregate losses divided by the expected limited aggregate losses.

For example, an insured risk has a per-occurrence limit (deductible) of 100,000 and it has five claims in a year. The five claims are shown in Exhibit 3.21.

Exhibit 3.21. Experience for a Group of Risks with a Per-Occurrence Limit of \$100,000

| Claim No. | Unlimited Amount | Limited Amount |
|-----------|------------------|----------------|
| 1         | 60,000           | 60,000         |
| 2         | 70,000           | 70,000         |
| 3         | 90,000           | 90,000         |
| 4         | 110,000          | 100,000        |
| 5         | 120,000          | 100,000        |
| Total     | 450,000          | 420,000        |

In this case, the unlimited aggregate losses of \$450,000, the sum of all the five claims, can be used to construct a standard Table M. In order to construct a Limited Table M, however, we should use the sum of the limited aggregate losses, \$420,000.

All the same methods that are used to construct unlimited Tables M (vertical or horizontal slicing of empirical data, manipulating parameterized loss distributions) can be used to construct a Table  $M_D$ . A Limited Table M has three dimensions: the expected size of the policy, the entry ratio, and the per-occurrence loss limit, D. Alternately, one can think of Table  $M_D$  as a set of tables, one for each deductible or per-occurrence loss limit.

##### **Examples of using Tables $M_D$ to price the insurance charge of an insurance policy with a deductible and an aggregate:**

Expected total losses = \$700,000

Deductible = \$250,000

Expected Primary Losses<sup>41</sup> = \$500,000

Expected number of claims = 60

Entry Ratio = 2.0 (which means the aggregate limit is  $2.0 \times \$500,000 = \$1,000,000$ )

Table  $M_D$  for policies around \$500K in size is shown in Exhibit 3.22.<sup>42</sup>

Exhibit 3.22. Sample Table  $M_D$

| Insurance Charge Factor | Deductible |      |      |
|-------------------------|------------|------|------|
|                         | 100K       | 250K | 500K |
| Entry Ratio             |            |      |      |
| 1.0                     | .240       | .250 | .260 |
| 1.5                     | .100       | .110 | .120 |
| 2.0                     | .030       | .040 | .050 |
| 2.5                     | .018       | .022 | .030 |

The factor at 250K for an entry ratio of 2.0 is 0.040, for an insurance charge of  $0.040 \times \$500,000 = \$20,000$ .

The total expected loss cost for this policy would be \$220,000 (\$20,000 plus the difference between \$700,000 and \$500,000).

Now consider the situation if the policy had been written with a deductible of \$150,000.

Expected total losses = \$700,000

Deductible = \$150,000

Expected Primary Losses = \$400,000

Entry Ratio = 2.5 (which means the aggregate limit is  $2.5 \times \$400,000 = \$1,000,000$ )

Note that the Expected Primary Losses are less because the deductible is now \$150,000 rather than \$250,000.

Using the table in Exhibit 3.22 again,

Interpolating<sup>43</sup> between the factor for an entry ratio of 2.5 at 100K (0.018) and at 250K (0.022) gives an insurance charge factor of .019, for an insurance charge of  $0.019 \times \$400,000 = \$7,733$ .

The total expected loss cost for this policy would be \$307,733 (\$7,733 plus the difference between \$700,000 and \$400,000).

#### Questions

9. For the Lee diagram below, identify the areas associated with
  - (a) Table  $M_D$  Charge at R
  - (b) Table  $M_D$  Savings at S
  - (c) Per-occurrence excess charge at D

<sup>41</sup>  $E\{A_{250,000}\}$

<sup>42</sup> A real Table  $M_D$  would have many more entry ratios than this simplified example.

<sup>43</sup> Because the differences are small, any reasonable interpolation will do. I have used a linear interpolation for simplicity.

![A graph showing the relationship between Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has two horizontal dashed lines: 'R = Max ER' and 'S = Min ER'. The x-axis is labeled 'F(y)' and has values '0' and '1'. Two curves, F(y) and F_D(y), start at the origin (0,0) and end at (1,1). F(y) is the upper curve and F_D(y) is the lower curve. The area between the curves is divided into regions labeled with letters: A, B, C, D, E, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z. The regions are defined by vertical dashed lines and the horizontal lines R and S.](36f6f5bc2a35070ad6dc4312a93bcbe3_img.jpg)

A graph showing the relationship between Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has two horizontal dashed lines: 'R = Max ER' and 'S = Min ER'. The x-axis is labeled 'F(y)' and has values '0' and '1'. Two curves, F(y) and F\_D(y), start at the origin (0,0) and end at (1,1). F(y) is the upper curve and F\_D(y) is the lower curve. The area between the curves is divided into regions labeled with letters: A, B, C, D, E, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z. The regions are defined by vertical dashed lines and the horizontal lines R and S.

For questions 10 and 11,<sup>44</sup> please refer to chapter 2 for the retrospective premium formula, including the tax multiplier.

10. Let us assume a retrospectively rated insured had a basic premium of \$30,000, an excess loss premium of \$10,000, a loss conversion factor of 1.1, a tax multiplier of 1.05, an accident limit of \$100,000, and a maximum premium of \$250,000. Refer to chapter 2 for the retrospective premium formula including the tax factor.

- If the insured has small losses totaling to \$150,000 in year, what is the retro premium?
- If the insured has small losses totaling to \$200,000 in year, what is the retro premium?
- If the insured has one large loss of \$150,000 in year, what is the retro premium?
- If the insured has one large loss of \$150,000 in year plus \$100,000 in small losses, what is the retro premium?

11. Let us assume a retrospectively rated insured had a basic premium of \$300,000, an excess loss premium of \$100,000, a loss conversion factor of 1.1, a tax multiplier of 1.05, an accident limit of \$100,000, and a minimum premium of \$650,000. Refer to chapter 2 for the retrospective rating formula, including the tax factor.

- If the insured has small losses totaling to \$150,000 in year, what is the retro premium?
- If the insured has one large loss of \$150,000 in year, what is the retro premium?

12. You price a retrospective policy with an expected loss of \$150,000 and aggregate limit of \$300,000, and find that the insurance charge is \$15,000.

The customer requests that you also add a per-occurrence loss limitation of \$100,000 to the losses subject to the retrospective calculation. You determine that if there were no aggregate limit, the cost of the per-occurrence limit would be \$50,000

Would the combined charge for the per-occurrence limit and the aggregate limit be more, less, or the same as the sum of the two charges, \$65,000? Why?

13. You are given the following table of insurance charges, by per-occurrence deductible:

<sup>44</sup> Questions 10 and 11 were adapted with permission from material written by Howard Mahler.

| <u>r</u> | <u>\$100,000 deductible</u> | <u>\$200,000 deductible</u> |
|----------|-----------------------------|-----------------------------|
| 1.0      | 0.20                        | 0.22                        |
| 1.5      | 0.10                        | 0.12                        |
| 2.0      | 0.04                        | 0.05                        |
| 2.5      | 0.02                        | 0.03                        |

The expected unlimited losses are \$40,000.

The expected primary losses at a per-occurrence limit of \$100,000 are \$20,000.

The expected primary losses at a per-occurrence limit of \$200,000 are \$30,000.

(a) A policy has a \$100,000 per-occurrence deductible and a \$40,000 aggregate deductible limit. Find the cost of the \$40,000 aggregate deductible limit.

(b) Find the cost of the \$40,000 aggregate deductible limit if the policy had a \$200,000 per-occurrence deductible. (Use linear interpolation in the table, if necessary.)

(c) Which policy will the insurer charge more for? Why?

### **5. Other Methods of Combining Per-Occurrence and Aggregate Excess Loss Cost<sup>45</sup>**

#### *5.1. Estimating Per-Occurrence and Aggregate Combined Excess Loss Cost Using Table L*

Consider the case of an insured with a per-occurrence limit of \$50,000 for each loss occurring to it, and an aggregate limit of \$250,000. For example, if the policy had the following claims:

\$20,000

\$30,000

\$45,000

\$55,000

\$100,000

\$120,000

The insured would be responsible for the first \$50,000 of each claim, or

$$\$20K + \$30K + \$45K + 3 \times (\$50K) = \$245K .$$

If one more claim of \$10,000 were incurred, the insured would only be responsible for an additional \$5,000, because the aggregate limit on the limited loss would have been reached.

##### *a. Table L and its Implication*

Table L is a method to estimate a per-occurrence and aggregate combined excess policy simultaneously, in a single table. Like Table M<sub>D</sub>, that table has three dimensions: the expected size of the policy, the entry ratio, and the per-occurrence loss limit. Alternately, one can think of Table L as set of tables, with one per each per-occurrence limit.

It is defined as follows: Assume that a formula for limiting or adjusting individual occurrences is given. The entry ratio (r) at any actual loss incurred by the risk is defined as the actual limited

<sup>45</sup> Section 5 is adapted from David Skurnick, "The California Table L," *PCAS* LXI, 1974; Yoong-Sin Lee, "The Mathematics of Excess of Loss Coverages and Retrospective Rating—A Graphical Approach," *PCAS* LXXV, 1988; and a study note by Ginda Kaplan Fisher, "Pricing Aggregates on Deductible Policies", 2002, published by the Casualty Actuarial Society as part of the Syllabus of Exams.

aggregate losses divided by the expected unlimited aggregate losses. The Table L charge at entry ratio  $r$ ,  $\phi_D^*(r)$ , is defined as the average difference between a risk's actual unlimited loss and its actual loss limited to  $D$ , plus the risk's limited loss in excess of  $r$  times the risk's expected unlimited loss. The Table L savings at entry ratio  $r$ ,  $\psi_D^*(r)$ , is defined as the average amount by which the risk's actual limited loss falls short of  $r$  times the expected unlimited loss. The Table L charge and savings are both expressed as ratios to expected unlimited loss<sup>46</sup>.

This differs from Table M in that Table L looks at how much loss, on average, will be limited by the combination of the per-occurrence limit and the aggregate excess limit.

Recall that  $F_D(Y)$  = the cumulative distribution function of  $Y$ , the limited losses whose unlimited cumulative distribution function was given by  $F$ . Then the Table L insurance charge at entry ratio  $r \geq 0$  is defined as a formula:

$$\phi_D^*(r) = \int_r^\infty (y - r) dF_D(y) + k \quad (\text{Formula 3.6})$$

and

$$\psi_D^*(r) = \int_0^r (r - y) dF_D(y) \quad (\text{Formula 3.7})$$

where  $k$  is the excess ratio for the per-occurrence limit. That is,

$$k = \frac{E - E\{A_D\}}{E}, \quad (\text{Formula 3.8})$$

where  $E$  is the total expected loss, and  $E\{A_D\}$  is the expected loss after application of the per-occurrence limit.

Note that if there is no loss limit, "k" will be zero,  $F_D(y) = F(y)$ , and the above formulas reduce to the Table M formulas.

Both the per-occurrence limit and the aggregate limit remove losses from the portion the insured owes (whether the ratable losses in a retro policy or the deductible losses in a deductible policy). If estimated separately, without considering both, the effects of the per-occurrence and aggregate limits overlap, as discussed in section 4. It is important not to double-count any losses excluded by these provisions. The formula for the Table L charge avoids this by using the limited distribution,  $F_D$ , in the integral.

We can see that the second part,  $k$ , of the  $\phi_D^*(r)$  equation stands for the loss cost of the per-occurrence excess portion and the first part is the additional effect of the aggregate limit beyond that of the occurrence limit.

---

<sup>46</sup> Or policy limit loss, as mentioned in section 1.1, page 40.

Exhibit 3.23. Lee Diagram of Table L charge and savings

![A graph showing the relationship between the size of loss and the probability of loss. The vertical axis is labeled 'Size of Loss (on the policy)' and has a point 'r'. The horizontal axis is labeled 'Probability of Loss (on the policy)' and has points '0' and '1'. Two curves originate from (0,0): an upper curve labeled 'F(y)' and a lower curve labeled 'F_D(y)'. A horizontal dashed line at 'r' intersects both curves. The area under 'F(y)' is divided into regions V (top), T (middle), and W (bottom, above r). The area under 'F_D(y)' is divided into regions S (top, above r) and U (bottom, below r). The area between the curves above 'r' is labeled 'X'. The area between the curves below 'r' is labeled 'T'.](e82430d9040f65fe7abed1d9cd028bd6_img.jpg)

A graph showing the relationship between the size of loss and the probability of loss. The vertical axis is labeled 'Size of Loss (on the policy)' and has a point 'r'. The horizontal axis is labeled 'Probability of Loss (on the policy)' and has points '0' and '1'. Two curves originate from (0,0): an upper curve labeled 'F(y)' and a lower curve labeled 'F\_D(y)'. A horizontal dashed line at 'r' intersects both curves. The area under 'F(y)' is divided into regions V (top), T (middle), and W (bottom, above r). The area under 'F\_D(y)' is divided into regions S (top, above r) and U (bottom, below r). The area between the curves above 'r' is labeled 'X'. The area between the curves below 'r' is labeled 'T'.

In Exhibit 3.23, the upper curve is  $F$ , the lower curve is  $F_D$ , and  $r$  corresponds to aggregate limit. As with Table M,  $r = (\text{aggregate limit}) / (\text{expected unlimited losses})$ . The area under the upper curve ( $T+U+W+X$ ) represents the unlimited loss distribution. It has area = 1, since all entities are defined in terms of the expected unlimited loss.

The area between the curves ( $T+W$ ) represents the distribution of loss above the per-occurrence limit, and together they have area  $k$ .

The area under the lower curve ( $U+X$ ) represents the distribution subject to the per-occurrence limit, or  $1-k$ .

Area  $X$  represents the distribution of loss after application of the per-occurrence limit that is above the aggregate limit.

The Table M charge at entry ratio  $r$  (ignoring the per-occurrence limitation) is  $W+X$ .

The Table L charge at entry ratio  $r$ ,  $\phi_D^*(r)$ , is  $T+W+X$ .

The Table M savings at entry ratio  $r$  (ignoring the per-occurrence limitation) is  $S$ .

The Table L savings at entry ratio  $r$ ,  $\psi_D^*(r)$ , is  $S+T$ .

Also,  $r = S + T + U$  and  $1 = \text{the area under } F(y) = T + U + W + X$ .

So  $\phi_D^*(r) + r - 1 = (T + W + X) + (S + T + U) - (T + U + W + X) = T + S = \psi_D^*(r)$ .

And (reading the above from right to left) the relationship between the insurance charge and the insurance saving in Table L is similar to that for Table M:

$$\psi_D^*(r) = \phi_D^*(r) + r - 1 . \quad (\text{Formula 3.9})$$

##### *b. Construction of Table L*

Here we will show an illustration of a Table L construction from empirical data.

To construct Table L, we need to obtain data on both the unlimited aggregate losses and the limited aggregate losses for each of the risks.

Exhibit 3.24. Experience for a Group of Risks with a Per-Occurrence Limit of \$50,000

| Risk | Actual Unlimited<br>Aggregate Loss | Actual Limited<br>Aggregate Loss |
|------|------------------------------------|----------------------------------|
| 1    | 20,000                             | 20,000                           |
| 2    | 50,000                             | 50,000                           |
| 3    | 60,000                             | 60,000                           |
| 4    | 70,000                             | 70,000                           |

|         |         |         |
|---------|---------|---------|
| 5       | 80,000  | 80,000  |
| 6       | 80,000  | 80,000  |
| 7       | 90,000  | 90,000  |
| 8       | 100,000 | 100,000 |
| 9       | 150,000 | 120,000 |
| 10      | 300,000 | 250,000 |
| Average | 100,000 | 92,000  |

First, we compute the excess ratio (k) for the per-occurrence limit:

$$k = 0.08 = (\$100,000 - \$92,000) / \$100,000.$$

Next we compute the entry ratios. As stated previously, the entry ratio is the ratio of the actual limited aggregate losses to the expected unlimited aggregate losses. In this illustration, the expected unlimited aggregate losses of the group are \$100,000. So the entry ratios, shown in Exhibit 3.25, are:

Exhibit 3.25. Entry Ratios for a Group of Risks with a Per Occurrence Limit of \$50,000

| Risk | Actual Unlimited<br>Aggregate Loss | Actual Limited<br>Aggregate Loss | Entry<br>Ratio<br>(r) |
|------|------------------------------------|----------------------------------|-----------------------|
| 1    | 20,000                             | 20,000                           | 0.2                   |
| 2    | 50,000                             | 50,000                           | 0.5                   |
| 3    | 60,000                             | 60,000                           | 0.6                   |
| 4    | 70,000                             | 70,000                           | 0.7                   |
| 5    | 80,000                             | 80,000                           | 0.8                   |
| 6    | 80,000                             | 80,000                           | 0.8                   |
| 7    | 90,000                             | 90,000                           | 0.9                   |
| 8    | 100,000                            | 100,000                          | 1                     |
| 9    | 150,000                            | 120,000                          | 1.2                   |
| 10   | 300,000                            | 250,000                          | 2.5                   |

Then construct the Table L using the horizontal slicing method. The procedure is similar to the one we used to construct a Table M, and is shown in Exhibit 3.26. Note that the average r is  $0.92 = 1-k$ .

Exhibit 3.26. Calculation of Table L

| r   | #<br>Risks | # Risks over r | % Risks over<br>r | Difference in<br>r | $\phi_D^*(r)-k$      | $\phi_D^*(r)$ |
|-----|------------|----------------|-------------------|--------------------|----------------------|---------------|
| 0   | 0          | 10             | 100%              | 0.2                | 0.92                 | 1             |
| 0.2 | 1          | 9              | 90%               | 0.3                | 0.72                 | 0.8           |
| 0.5 | 1          | 8              | 80%               | 0.1                | 0.45                 | 0.53          |
| 0.6 | 1          | 7              | 70%               | 0.1                | 0.37                 | 0.45          |
| 0.7 | 1          | 6              | 60%               | 0.1                | 0.3                  | 0.38          |
| 0.8 | 2          | 4              | 40%               | 0.1                | 0.24                 | 0.32          |
| 0.9 | 1          | 3              | 30%               | 0.1                | 0.2                  | 0.28          |
| 1   | 1          | 2              | 20%               | 0.2                | $0.17=0.13+20\%*0.2$ | 0.25          |
| 1.2 | 1          | 1              | 10%               | 1.3                | $0.13=0+10\%*1.3$    | 0.21          |
| 2.5 | 1          | 0              | 0%                | 0                  | 0                    | 0.08          |

Starting from the entry ratio (r) column, we find the number of risks in the group with the corresponding entry ratio as shown in the “# Risks” column. Then the “# Risks over r” shows the number of risks which have entry ratios exceeding a given entry ratio. The “% Risks over r” column converts the number in the “# Risks over r” into a percentage basis by dividing by the total number of risks (here it is 10). The “Difference in r” column shows the difference between the entry value in this row and the entry value in the next row.

Then, the “ $\phi_D^*(r)-k$ ” column is calculated similarly to  $\phi(r)$  for an unlimited Table M. We begin from the bottom row with 0, as there are no expected losses greater than the largest entry ratio. Then we work up; the value in each row is equal to the value in the row beneath plus the product of the “% Risks over r” and the “Difference in r” in that row. Finally, the last column “ $\phi_D^*(r)$ ” is the “ $\phi_D^*(r)-k$ ” column plus the excess ratio (k) for the per-occurrence limit. Recall that k was calculated as 0.08 in the first step.

Note that if there is no loss limit, “k” will be zero, and this formula is the same as the formula for the Table M charge.

Finally, we can also calculate the insurance savings for each entry ratio by using the formula  $\psi_D^*(r) = \phi_D^*(r) + r - 1$ . Thus, the Table L can be constructed as shown in Exhibit 3.27.

Exhibit 3.27. Table L

| $r$ | $\phi_D^*(r)$ | $\psi_D^*(r)$ |
|-----|---------------|---------------|
| 0   | 1             | 0             |
| 0.2 | 0.8           | 0             |
| 0.5 | 0.53          | 0.03          |
| 0.6 | 0.45          | 0.05          |
| 0.7 | 0.38          | 0.08          |
| 0.8 | 0.32          | 0.12          |
| 0.9 | 0.28          | 0.18          |
| 1   | 0.25          | 0.25          |
| 1.2 | 0.21          | 0.41          |
| 2.5 | 0.08          | 1.58          |

Note that as with calculating Table M<sub>D</sub>, we do not need to have a large body of data at every per-occurrence loss limit in order to calculate Table L from empirical data. If the unlimited data is known at the claim level, we can create “as if” data at any per-occurrence loss limit. (When working with losses from coverages that might have varying policy limits, such as commercial auto insurance, it might be necessary to estimate “unlimited” claims/occurrences above lower per-occurrence policy limits if data from many policy limits is to be combined.)

As with Tables M, Tables L can also be calculated from simulated data (or other methods) if we have a parameterized loss distribution. But to calculate the Table L charge from simulated data, we need to separately simulate the number of claims and the severity of each claim, so that the per-claim loss limit can be appropriately applied. More detail is needed than the (unlimited) aggregate distribution, even if the excess ratio k is known.

#### 5.2. The ICRL Method

In some cases, it might be expedient to use an existing table of insurance charges, and apply reasonable modifications to it so it reflects the impact of limiting the losses. When tables were large printed documents, this was a very appealing option, even when there was adequate data or a robust enough model to explicitly calculate aggregate loss charges for a variety of deductible limits. Now, electronic or formulaic Tables M are generally available for both limited and unlimited policy losses, in which case, this sort of adjustment is not needed. However, until 2019, the NCCI published only unlimited Table M, and used an adjustment of this type in its workers' compensation rating manual: the Insurance Charge Reflecting Loss Limitation (ICRL) procedure.<sup>47</sup> This procedure uses an unlimited Table M, and adjusts it to approximate Table M<sub>D</sub>. The ICRL method is presented here as an example of the sort of estimate an actuary can make when perfect data isn't available. Note that the 1998 NCCI Table M was published by Expected Loss Group (ELG) rather than by expected number of claims, and a State/Hazard Group adjustment was used to account for the different severities (and thus a different implied expected number of claims) within an ELG depending on the state and hazard group of the risk. As mentioned above, Table M<sub>D</sub> must be indexed by three variables: the expected size of the policy<sup>48</sup>, the deductible, and the entry ratio. In effect, the ICRL procedure can be used to map the three indices of M<sub>D</sub> into the two used by the (unlimited) Table M, and can be thought of as a mapping of Table M<sub>D</sub> onto Table M. Both the entry ratio and the size category (ELG) are modified to account for the deductible.

The Loss Group Adjustment Factor used in the ICRL procedure is

$$\frac{1+0.8*k}{1-k} \quad \text{(Formula 3.10)}$$

where k is the fraction of losses expected to be above the per-claim limit or deductible amount.<sup>49</sup> For example, a workers' compensation insured has a per-occurrence limit of \$250,000 and its expected limited aggregate losses are \$490,000. In addition, its expected unlimited aggregate losses are \$650,000. An aggregate deductible policy covers the insured and the aggregate deductible limit is \$750,000.

We also know that this risk has a State/Hazard Group relativity of 0.9.

First, we compute the entry ratio:  $1.53 = \$750,000/\$490,000$ .

Then we compute the ICRL adjustment

$$\frac{1 + 0.8 * (\$650,000 - \$490,000)/\$650,000}{1 - (\$650,000 - \$490,000)/\$650,000} = 1.588$$

In an unlimited Table M, as excerpted below, the expected unlimited aggregate losses of \$650,000 would correspond to Expected Loss Group 31. But in this case, we adjust the expected loss by the SHG and ICRL adjustment to yield

$$\$650,000 \times 0.9 \times 1.588 = \$929,000.$$

So we will use an Expected Loss Group 29 to enter Table M.

---

<sup>47</sup> The ICRL procedure was originally described by Ira Robbin in "Overlap Revisited—The 'Insurance Charge Reflecting Loss Limitation' Procedure," *Pricing, Casualty Actuarial Society Discussion Paper Program*, 1990, Volume 2.

<sup>48</sup> ICRL used expected limited loss for this, consistent with grouping policies by expected unlimited loss for the unlimited Table M

<sup>49</sup> This excess ratio, k, was referred to as "ER" in the pre-2019 NCCI retrospective rating manual.

Exhibit 3.28. Table of Expected Loss Group<sup>50</sup>

| Expected Loss Group | Range of Values     |
|---------------------|---------------------|
| 31                  | 630,000-720,000     |
| 30                  | 720,001-830,000     |
| 29                  | 830,001-990,000     |
| 28                  | 990,001-1,180,000   |
| 27                  | 1,180,001-1,415,000 |
| 26                  | 1,415,001-1,744,000 |

Looking this up in the excerpt of Table M below gives us a Table M charge of 0.1583, which indicates a dollar charge of  $0.1583 \times \$490,000$  or \$77,567. This is the additional charge for the aggregate limit. The charge for the per-occurrence limit is  $\$650,000 - \$490,000 = \$160,000$ . So the total expected loss cost for this policy is  $\$160,000 + \$77,567 = \$237,567$ .

Exhibit 3.29. Table of Insurance Charges

| Entry Ratio | Expected Loss Group |        |               |        |        |        |
|-------------|---------------------|--------|---------------|--------|--------|--------|
|             | 31                  | 30     | 29            | 28     | 27     | 26     |
| 0.75        | 0.4150              | 0.4069 | 0.3989        | 0.3911 | 0.3833 | 0.3755 |
| 0.81        | 0.3864              | 0.3777 | 0.369         | 0.3605 | 0.3521 | 0.3436 |
| 1.07        | 0.2867              | 0.2764 | 0.2661        | 0.2557 | 0.2453 | 0.2349 |
| 1.15        | 0.2628              | 0.2522 | 0.2417        | 0.231  | 0.2203 | 0.2096 |
| 1.53        | 0.1797              | 0.169  | <b>0.1583</b> | 0.1476 | 0.1369 | 0.1261 |

#### Questions

14. Draw a Lee diagram illustrating a policy that has:

- A continuous uniform unlimited loss distribution from 0 to 500
- A continuous uniform limited loss distribution from 0 to 400
- An entry ratio of 1.5 times the expected unlimited loss

a) Label:

$\phi_D^*(1.5)$ , the Table L charge at the entry ratio

$\psi_D^*(1.5)$ , the Table L savings at the entry ratio

b) Calculate the value of

$\phi_D^*(1.5)$ , the Table L charge at the entry ratio

$\psi_D^*(1.5)$ , the Table L savings at the entry ratio

15. For the Lee diagram below, identify the areas associated with

<sup>50</sup> The Table of Expected Loss Groups changed over time, with inflation. This example is just illustrative.

- (a) Table L Charge at R
- (b) Table L Savings at S

![A graph showing two curves, F(y) and F_D(y), on a coordinate system with 'Entry Ratio y' on the vertical axis and 'F(y)' on the horizontal axis. The horizontal axis is marked from 0 to 1. The vertical axis has two horizontal dashed lines labeled 'R = Max ER' and 'S = Min ER'. The area between the curves and the axes is divided into regions labeled with letters: A, B, C, D, E, G, H, I, J, K, L, M, N, O, P, Q, T, U, V, W, X, Z. The curve F(y) is the upper curve, and F_D(y) is the lower curve. The region between the curves is divided into regions H, I, J, K, L, M, N, O, P, Q, T, U, V, W, X, Z. The region above F(y) is divided into regions A, B, C, D, E, G. The region below F_D(y) is divided into regions V, W, X, Z. The region between F(y) and F_D(y) is divided into regions H, I, J, K, L, M, N, O, P, Q, T, U, V, W, X, Z.](52c2f593b127e110ac6fb67e135f1ad3_img.jpg)

A graph showing two curves, F(y) and F\_D(y), on a coordinate system with 'Entry Ratio y' on the vertical axis and 'F(y)' on the horizontal axis. The horizontal axis is marked from 0 to 1. The vertical axis has two horizontal dashed lines labeled 'R = Max ER' and 'S = Min ER'. The area between the curves and the axes is divided into regions labeled with letters: A, B, C, D, E, G, H, I, J, K, L, M, N, O, P, Q, T, U, V, W, X, Z. The curve F(y) is the upper curve, and F\_D(y) is the lower curve. The region between the curves is divided into regions H, I, J, K, L, M, N, O, P, Q, T, U, V, W, X, Z. The region above F(y) is divided into regions A, B, C, D, E, G. The region below F\_D(y) is divided into regions V, W, X, Z. The region between F(y) and F\_D(y) is divided into regions H, I, J, K, L, M, N, O, P, Q, T, U, V, W, X, Z.

16. What are some advantages to using ICRL as compared to a limited Table M?

What are some disadvantages?

17.<sup>51</sup> A large dollar deductible workers' compensation policy requires the insured to reimburse the insurer for each occurrence up to \$250,000, subject to an aggregate reimbursement of \$1,200,000. The following attributes also apply to this policy:

Standard Premium: \$1,000,000

Hazard Group Relativity: 0.900

Expected Unlimited Loss Ratio: 75%

K (Excess Ratio): 20%

Table MD: Limited Insurance Charges with D = 250,000

| Entry Ratio      | 1.0   | 1.5   | 2.0   | 2.5   |
|------------------|-------|-------|-------|-------|
| Insurance Charge | 0.250 | 0.110 | 0.040 | 0.022 |

Table of Expected Loss Ranges

| Expected Loss Group | Expected Losses       |
|---------------------|-----------------------|
| 31                  | 630,000 – 720,000     |
| 30                  | 720,001 – 830,000     |
| 29                  | 830,001 – 990,000     |
| 28                  | 990,001 – 1,180,000   |
| 27                  | 1,180,001 – 1,415,000 |

Table M: Unlimited Insurance Charges

| Entry Ratio | Expected Loss Group |       |       |       |       |
|-------------|---------------------|-------|-------|-------|-------|
|             | 31                  | 30    | 29    | 28    | 27    |
| 0.5         | 0.415               | 0.407 | 0.399 | 0.391 | 0.383 |
| 1.0         | 0.386               | 0.378 | 0.369 | 0.361 | 0.352 |
| 1.5         | 0.287               | 0.276 | 0.266 | 0.256 | 0.245 |
| 2.0         | 0.263               | 0.252 | 0.242 | 0.231 | 0.220 |

- Use a limited Table M approach to calculate the Insurance Charge.
- Use the ICRL procedure to calculate the total expected loss cost for this policy.

18. What was the purpose of the state/hazard group relativity? What implicit assumption is made when using a state/hazard group relativity?

<sup>51</sup> Exercise 17 was adapted with permission from material written by Howard Mahler.

### 6. Understanding Aggregate Loss Distributions

To get an intuitive feel for how the distribution of deductible losses should behave, it is helpful to consider the extreme cases.

Consider first some extreme plan designs: A deductible policy with an infinite deductible but an aggregate limit on the deductible behaves like a retrospectively rated policy with a maximum, but no per-loss limitation and a minimum equal to basic times tax. Alternatively, a retrospectively rated policy with a per-loss loss limitation but an infinite maximum behaves exactly like a deductible policy with no aggregate limit.

Remember that a distribution of aggregate losses is information about the range of outcomes of many similar insurance policies. We will largely be concerned with the distribution of entry ratios, which are scaled with respect to expected aggregate losses. The shape of the distribution of entry ratios is largely driven by the variance of the underlying aggregate distribution. So it can be helpful to visualize some extreme outcomes, or extreme underlying severity distributions.

First, what would the aggregate loss distribution look like if every policy's losses were exactly equal to the expected losses? For example, every policy had exactly \$100 of loss.

Exhibit 3.30. Twenty-five policies that all incur exactly their expected loss  
(Only 25 shown so they can be seen)

![A bar chart showing 25 policies, each with a loss of exactly $100. The y-axis represents loss amount from 0 to 120. The x-axis represents policy numbers from 1 to 25. Each bar is shaded with diagonal lines, representing the 'Observation'. A horizontal line at y=100 represents the 'Average'.](9acfc25b29c0ce9239e2fac2350c527e_img.jpg)

The figure is a bar chart with 25 bars, each representing a policy. The y-axis is labeled from 0 to 120 in increments of 20. The x-axis is labeled with policy numbers 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, and 25. Each bar is shaded with diagonal lines, representing the 'Observation'. A horizontal line at y=100 represents the 'Average'.

A bar chart showing 25 policies, each with a loss of exactly \$100. The y-axis represents loss amount from 0 to 120. The x-axis represents policy numbers from 1 to 25. Each bar is shaded with diagonal lines, representing the 'Observation'. A horizontal line at y=100 represents the 'Average'.

The smallest outcome equals the expected loss of \$100 equals the largest outcome.

At an entry ratio  $r = 0.8$ , the charge would be the part of the shaded area above the line  $y = (0.8 * E) = 80$  divided by the total shaded area.

$$\phi(0.8) = (100-80)*25/(100*25) = 0.2.$$

At an entry ratio  $r = 1.2$ , the charge would be the part of the shaded area above the line  $y = (1.2 * E) = 120$  divided by the total shaded area. It can be seen there is no shaded area above 120, so

$$\phi(1.2) = 0$$

In fact, The Table M charge at any entry ratio  $r$  greater than or equal to 1 would be zero and the Table M charge for any entry ratio less than one would be  $1-r$ .

Next consider the other extreme. What if a policy rarely had any losses, but if it had a loss, that loss would be enormous. For example, you might have a policy with a  $1/10,000$  chance of having any claims at all, but if it did have a claim, the claim was \$1,000,000. This policy also has an expected loss of \$100, but it has a very high variance. In this case, the Table M charge at an entry ratio of 1 would be nearly 1 ( $999,900/1,000,000$  to be precise) because that one time in 10,000 when there is a loss, 999,900 of it will be in excess of the aggregate limit, and the other 9999 times when there is no loss the aggregate limit is irrelevant.

###### Exhibit 3.31.

Twenty-five policies, only one of which incurs any loss, with the same overall expected value as the policies pictured in Exhibit 3.30. (only 25 in this example, so they can be seen)

![A bar chart showing the distribution of losses for 25 policies. The y-axis represents loss amount from 0 to 2500. The x-axis represents policy numbers from 1 to 25. Policy 25 has a loss of 2500, while policies 1-24 have a loss of 0. A legend indicates that the shaded bar represents 'Observation' and the dots represent 'Average'.](e0740204d7aa33697c8f2d59c4cca51b_img.jpg)

| Policy Number | Observation (Loss) | Average (Loss) |
|---------------|--------------------|----------------|
| 1             | 0                  | 100            |
| 3             | 0                  | 100            |
| 5             | 0                  | 100            |
| 7             | 0                  | 100            |
| 9             | 0                  | 100            |
| 11            | 0                  | 100            |
| 13            | 0                  | 100            |
| 15            | 0                  | 100            |
| 17            | 0                  | 100            |
| 19            | 0                  | 100            |
| 21            | 0                  | 100            |
| 23            | 0                  | 100            |
| 25            | 2500               | 100            |

A bar chart showing the distribution of losses for 25 policies. The y-axis represents loss amount from 0 to 2500. The x-axis represents policy numbers from 1 to 25. Policy 25 has a loss of 2500, while policies 1-24 have a loss of 0. A legend indicates that the shaded bar represents 'Observation' and the dots represent 'Average'.

These extremely simple examples were chosen so the values are obvious and easy to calculate, but the same principles apply to real policies. Very small policies can be similar to the second extreme, because on very small policies the likelihood of even one claim is small, so most of the expected value of the aggregate loss is in the “tail,”<sup>52</sup> or unusually high outcomes (the rare cases when a loss occurs). In contrast, very large commercial policies are more like the first extreme.

<sup>52</sup> Mathematically, this is the right-hand tail of the distribution, but as most aggregate distributions that actuaries encounter are only defined between zero and infinity, the right hand tail is often referred to simply as “the tail.”

They are expected to have a large number of claims, each of which is relatively small as compared to the total expected loss for the policy.

All other things being equal, the higher the expected number of claims, the lower the variance on the distribution of entry ratios, and the smaller the Table M charge is for entry ratios above 1. The possibility of extremely severe individual claims also increases the variance of the distribution of entry ratios.

For many types of insurance policies, the losses are driven by injuries to human beings. Some policies will tend to have more severe injuries than other policies (for example, a policy covering large trucks may have higher average liability severity than a policy covering private passenger vehicles, and a policy covering injuries to foundry workers will tend to have more severe claims than one covering injury to office workers.) But the difference in variance due to size of policy usually overwhelms those differences. That is, most of the difference in variance of aggregate loss among policies (and thus difference in Table M charge) is driven by the variance in the claim frequency.

But the variation of the severity distribution matters, too. For example, consider two policies, each of which has an expected frequency of 1 claim and no variance in the frequency—these imaginary policies will always have exactly 1 claim. Each claim on the first policy is equally likely to be \$1000 or \$5000. So the expected loss for the policy is \$3000. Each claim on the second policy has a 60% chance of costing \$500, a 30% chance of costing \$5000, and a 10% chance of costing \$12,000. This policy also has an expected aggregate loss of \$3000. Exhibit 3.32 compares the aggregate loss distributions of ten policies like the first, and ten like the second.

Exhibit 3.32. Comparing two policies with the same frequency and expected loss, but with different severity distributions

![Two bar charts comparing ten observations of Policy 1 and Policy 2. Both policies have an expected loss of 3,000. Policy 1 has a severity distribution where 5 observations are at 1,000 and 5 are at 5,000. Policy 2 has a severity distribution where 6 observations are at 1,000, 3 are at 9,000, and 1 is at 12,000. Both charts show a dotted line for the average at 3,000.](9946fd1a3f090031a13901d2d60d3da3_img.jpg)

| Policy   | Observation | Severity (Loss) |
|----------|-------------|-----------------|
| Policy 1 | 1           | 1,000           |
|          | 2           | 1,000           |
|          | 3           | 1,000           |
|          | 4           | 1,000           |
|          | 5           | 1,000           |
|          | 6           | 5,000           |
|          | 7           | 5,000           |
|          | 8           | 5,000           |
|          | 9           | 5,000           |
|          | 10          | 5,000           |
| Policy 2 | 1           | 1,000           |
|          | 2           | 1,000           |
|          | 3           | 1,000           |
|          | 4           | 1,000           |
|          | 5           | 1,000           |
|          | 6           | 1,000           |
|          | 7           | 9,000           |
|          | 8           | 9,000           |
|          | 9           | 9,000           |
|          | 10          | 12,000          |

Two bar charts comparing ten observations of Policy 1 and Policy 2. Both policies have an expected loss of 3,000. Policy 1 has a severity distribution where 5 observations are at 1,000 and 5 are at 5,000. Policy 2 has a severity distribution where 6 observations are at 1,000, 3 are at 9,000, and 1 is at 12,000. Both charts show a dotted line for the average at 3,000.

In this example, The charge at entry ratio of 1 is  $0.33 = (2000 \cdot 5) / (1000 \cdot 5 + 5000 \cdot 5)$  for policy 1 and  $0.5 = (2000 \cdot 3 + 9000) / (1000 \cdot 6 + 5000 \cdot 3 + 12,000)$  for policy 2.

For example, workers' compensation covers the same types of injuries to people all across the US. But some industries have a higher proportion of serious claims, and others have a higher proportion of minor claims. For instance, workers in metal foundries are subject to serious burns, whereas office workers are more likely to develop repetitive stress disorders. Because of this, the NCCI assigns workers' compensation job classes into seven Hazard Groups, A-G. Job classes in Hazard Group A have the smallest probability of serious injury leading to unusually high-severity claims, and those in Hazard Group G have the largest probability of a serious injury. Another driver of severity is location. The cost of the same injury may vary from place to place—medical care may be more expensive in one state than another. Also between the different states in the United States, workers' compensation laws vary significantly in the benefits they provide to injured workers for lost wages, and the courts may be more or less inclined to award very large liability verdicts.

In US workers' compensation, the NCCI reflects these differences by considering the state and hazard group of each risk when parametrizing the expected severity distribution used to generate aggregate loss factors. Similarly, when using the NCCI's new countrywide Table of Aggregate Loss Factors (Table M), the expected number of claims for a risk having a given expected loss will vary based on the average severity of its losses, which can be estimated by looking up the severity relativity of the appropriate state and hazard group mix of the policy. This can adjust the expected number of claims to reflect fewer (more) expected claims when a risk has a higher (lower) expected severity, so as to increase (decrease) the assumed variability of the risk. In general, for a given expected loss size, we treat a risk expected to have more severe individual claims as if it is smaller (and thus more variable) than a risk with the same expected loss due to a larger number of (on average) less severe claims.

To summarize, Table M shows different columns of aggregate loss factors for different expected claim count groups due to the impact of the size of a risk on the claim count distribution; all other things being equal, a larger insured has a tighter distribution of the ratio of observed claim

frequency over expected claim frequency than does a smaller insured. But severity distributions can vary as well, even within an insurance coverage.

If the severity distribution differs in scale, while having the same shape—in other words, the mean is different but the coefficient of variation and the skewness are approximately the same—simply adjusting the expected number of claims should yield reasonably accurate Table M charges (aggregate loss factors). However, if the difference is more extreme, we may need to also adjust the severity distribution, potentially needing to calculate a different Table M. Note that General Liability policies (especially products policies) and excess-of-loss reinsurance policies are more likely to differ significantly from other groups of policies due to their severity distribution.

Adjustments treating the differences as if they are driven mostly by scale have been used to adapt a table of expected aggregate charges developed from one coverage to be used for another coverage. For instance, some US insurers have used severity adjustment factors analogous to State/Hazard Group relativity factors in order to adapt a workers' compensation Table M to be used to estimate aggregate loss costs for Commercial Auto or General Liability. As always, care should be used when extrapolating that the resulting charges are reasonable. But sometimes there is not enough data to come up with a better estimate.

### Questions

19. When all else is equal, if the variance of the loss distribution is larger, will the Table M charge be larger or smaller than with a smaller variance?

20. An actuary calculates the insurance charges on an aggregate deductible for a general liability policy for house painters. All the losses in the historical data used in the analysis resulted from inadequate and/or sloppy paint jobs, which were relatively inexpensive to fix. Later, it is discovered that some paint contained a toxic substance and those painters are liable for very expensive remediation of the painted properties.

The new claims are 10% as common as the historical claims. For every 10 claims that would have been expected before, there are now 11, one of which is cleaning up toxic paint.

Had this been known, the expected cost of a policy would have been twice the cost the actuary used.

- (a) At an entry ratio of 2.00, with no per-occurrence loss limit, explain whether the insurance charge would increase, decrease, or stay the same.
- (b) Explain how a per-occurrence limit would affect the change in the insurance charge for the aggregate deductible.

### Acknowledgments

I would like to thank the many people who helped with everything from brainstorming the overall shape of this chapter to proofreading it. Jill Petker, Fran Sarrel, and Lawrence McTaggart helped with overall support and suggestions. X. Sherwin Li helped incorporate prior study notes and articles into this format and also helped review a draft. Dylan Lei and Matthew Iseler provided helpful and insightful feedback on a draft. Rick Gorvett provided some sample questions and pedagogic guidance. Teresa Lam, Jill Petker, Kirk Bitu, and Tom Daley helped me understand the changes to the NCCI retro rating plan. Nedzad Arnautovic, Elena Blagojevic, Brian Choi, Melanie Dufour, Joe Harkman, Alex Leitheiser, Colin Rizzio, Josh Taub, and Matt Veibell, all helpfully submitted errata and suggestions to the earlier editions of this chapter. And I would especially like to thank Howard Mahler who reviewed multiple drafts of this chapter and found any number of typos and inelegant or confusing sections, suggested numerous clarifications and examples, and generously allowed me to use some of the exercises published in his study guide.

## **Index of equivalent terms**

There are a great many names for many of the entities described in Chapter 3. As a convenience to the reader, I have tried to collect some of them here.

Table M Charge

Insurance Charge

Aggregate Excess Loss Factor

Aggregate Excess Ratio

Table M Saving

Insurance Saving

Aggregate Minimum Loss Factor

Net Insurance Charge

Net Aggregate Loss Factor

Net Table M Charge

Table M

Table of Insurance Charges

Table of Aggregate Loss Factors

Excess Loss Factor

