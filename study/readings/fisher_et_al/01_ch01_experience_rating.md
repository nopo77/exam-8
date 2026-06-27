---
paper: fisher_et_al
chapter: 1
title: "Chapter 1: Experience Rating"
topics: [experience_rating, experience_modification_factor, bühlmann_credibility, split_loss_plan, schedule_rating, quintile_test, process_variance, variance_of_hypothetical_means]
key_formulas: [bühlmann_credibility_Z, experience_modification_factor_formula, split_plan_mod_formula, ncci_weighting_ballast_formula, efficiency_test_statistic]
---

> **TL;DR**
> - Experience rating is prospective, not punitive: the e-mod M = (A+K)/(E+K) adjusts manual premium to reflect expected future loss potential, not to recoup past losses; a debit mod ≠ a "bad" risk
> - Bühlmann credibility determines Z = E/(E+K) where K = EPV/VHM; larger risks receive higher Z and thus greater weight on their own experience vs. the class average
> - Split loss plans (e.g. NCCI WC) separately credibility-weight primary losses (frequency proxy) and excess losses (severity proxy); NCCI uses weighting factor w and ballast B instead of Z_p/Z_e directly
> - Quintile test: ranked by mod, manual LRs should increase across quintiles (plan identifies differences); standard LRs should show no trend (plan correctly adjusts for differences); the efficiency test statistic Var(standard LR)/Var(manual LR) quantifies this—lower is better
> - Schedule credits/debits must not double-count effects already captured by the experience mod; apply schedule credit only when a favorable characteristic postdates or is not yet reflected in the experience period

## Chapter 1: Experience Rating

By Rebecca Pettingell

### 1. Introduction/Definition

Experience Rating is the use of an insured's past loss experience to determine rates for a future exposure period. The compilation of rules, definitions, formulas, etc., needed to calculate such a rate is referred to as the experience rating plan.

It is generally in the form of a multiplicative factor applied to manual rates, such that:

Standard Premium = E-mod \* Manual Premium.

An experience rating modification factor, or e-mod, greater than 1.0 implies the insured's experience is worse than average for its class. This is called a debit mod. A factor of less than 1.0 implies the insured's experience is better than average for its class. This is called a credit mod.

*Note: a risk with a debit mod should not be viewed as a "bad" risk, nor should a risk with a credit mod be viewed as a "good" or "better" risk. The mod merely indicates the risk's expected loss relative to other risks in its class.*

There is a misconception that experience rating is an attempt to "charge back" or make up for the past loss experience of an insured. This is incorrect! What experience rating does is determine how much an insured's past loss experience is predictive of its future loss potential and incorporate that prediction into a prospective rate which is better tailored to that risk's loss potential.

### 2. Advantages of Experience Rating

There are several advantages to using experience rating. It allows us to account for differences between risks within a class. It also allows us to account for differences due to variables that are difficult, impractical, or impossible to quantify via rating variables. Experience rating is a further refinement of classification rating since an individual risk's rate can be further tailored to its loss potential beyond the use of the class and rating variables that make up an insurer's manual rates.

### 3. Differences within Class

Experience rating is particularly useful when insureds don't fit neatly into a rating class. This could happen if a risk has unique operations, or if the classification system is not sophisticated. The fewer number of rating classes or the broader the range of rating classes in a classification system, the more useful experience rating will be because it allows us to pick up differences within a rating class. Another way to think about this is experience rating allows us to account for the variance of the hypothetical means of the risks within a rating class.

Let's consider two different companies that are very similar in size and operations. Both would be in the same rating class because their operations are so similar. In one company, management is very safety conscious. They require all employees to complete regular safety courses and frequently inspect their premises for safety hazards. If there are any accidents or safety incidents, they conduct a thorough review to determine what went wrong and how another incident could be avoided in the future. In the second company, management thinks that safety is just common sense and spending time discussing safety is a waste of time and money.

If we used strictly manual rating criteria, these two companies would likely be rated the same or very similarly. However, it is pretty clear that the first company will likely have fewer claims and better loss experience. The application of an experience rating plan would likely pick up the

differences between these two companies and allow an insurance company to charge each of these insureds a rate that is more closely tailored to their loss potential.

### **4. Objectives/Goals**

Experience rating accomplishes several objectives. First and foremost, it leads to greater risk equity. By charging a rate that is more commensurate with an insured risk's expected losses, we have increased fairness.

Second, experience rating creates an increased incentive for safety. By attaching a financial consequence to loss experience, there is an additional incentive to prevent or minimize losses on top of the incentives that already exist.

Also, experience rating enhances market competition. The same arguments that are made about classification rating systems enhancing market competition can also be made about experience rating. Since experience rating allows an insurer to charge a rate that is more in line with a risk's loss potential, the insurer will view more risks as being desirable to write. For example, imagine a risk that consistently has higher loss experience than other risks in its class. If an insurer has no mechanism to charge this risk a higher rate, it will not want to write this risk. However, by using experience rating the insurer can charge a premium that is more reflective of the risk's future loss potential.

### **5. Equity**

When thinking about experience rating, it is natural to ask "Is it really equitable to base an insured's future rates on its past experience? Isn't this just a way to charge back an insured for poor loss experience?" Gary Venter answers this question very elegantly. In his article "Experience Rating—Equity and Predictive Accuracy," he states "to the extent that the loss experience is indicative of true differences from the classification average, it appears equitable to charge for it." The experience mod is intended to be a prospective measure of loss potential for the future exposure period. It is not intended to be a penalty or reward for past experience or to recoup past losses.

### **6. Credibility**

Arguably the most important consideration in designing an experience rating plan is credibility—specifically how much credibility should be given to the individual insured's experience in the determination of the premium adjustment.

You can think of experience rating as a way of treating each risk as its own rating class. Just as an insurer might credibility weight the experience of a small rating class with the experience of the larger group it is a part of (e.g., the general liability experience of a small state might be credibility weighted with the country-wide indication), the experience of a single insured can be credibility weighted with that of other risks in its rating class.

First, let's review some basic credibility concepts. Then, we will explore those concepts in an individual risk rating and experience rating context, discussing specific credibility provisions and how they are incorporated into the determination of a risk's premium.

#### 6.1 Credibility Review<sup>1</sup>

In determining a rate or premium (or, what is ultimately equivalent, the modification factor applied to the old rate or the manual rate), the amount of weight given to the insured's own experience represents the level of credibility ascribed to that experience. The complement of credibility is applied to the expected loss experience represented by the manual rate.

Over the years, a number of mathematical approaches to determining credibility have been explored—in particular:

- Classical credibility—also known as “limited fluctuation” credibility, since the volume of expected losses (or expected number of claims, or number of exposures) necessary for a risk's loss experience to be given full credibility is based upon the potential fluctuation of results from expected levels.
- Bühlmann credibility—also known as “greatest accuracy” or “least squares” credibility, as it involves the analysis of the variance associated with the stochastic situation being evaluated.
- Bayesian credibility, which updates prior hypotheses in light of emerging experience. Under certain circumstances, the Bühlmann and Bayesian credibility approaches give the same result.

Regardless of the particular approach used, there are certain characteristics that a credibility factor  $Z$  (which represents the level of credibility associated with a risk's observed loss experience) is expected to have:

- $Z$  is a value between 0 and 1:  $0 \leq Z \leq 1$ .
- $Z$  does not decrease as the size of the risk (the level of expected losses, or  $E$ ) increases:  
$$dZ/dE \geq 0.$$
- As the size of a risk increases (i.e., as  $E$  increases), the ratio of  $Z$  to  $E$  decreases:  $\frac{d}{dE} \left( \frac{Z}{E} \right) < 0$ .  
This amounts to the charge for a loss of any given size decreasing as the size of the risk increases.

For purposes of experience rating, a Bühlmann credibility framework is used. The basic formula for credibility in this context is:

$$Z = \frac{E}{E + K}$$

where  $K$  is a constant for a particular situation. More specifically, in accordance with Bühlmann credibility,

$$K = \frac{\text{Expected Value of the Process Variance}}{\text{Variance of the Hypothetical Means}}.$$

Basically, the difference between a risk's actual loss experience and its expected loss experience can be divided into two categories. First, there is the variation that is purely random and results from the loss process being inherently stochastic, i.e., the process variance. Second, there is variation from the expected experience that is due to a risk being innately different from other risks within its class, i.e., the variance of the hypothetical means. We do not want to penalize or

---

<sup>1</sup> There are some excellent sources of information and explanation about credibility in the actuarial literature—e.g., Philbrick, 1981, “An examination of Credibility Concepts,” *Proceedings of the Casualty Actuarial Society (PCAS)*, 68:195-219, and Mahler and Dean, 2001, “Chapter 8: Credibility,” in *Foundations of Casualty Actuarial Science*, fourth edition, pp. 485-659.

reward a risk for experience that is truly random, but we do want the risk to take ownership of experience that is due to the risk's inherent differences. The weighting factor given to a risk's experience,  $Z$ , represents the portion of experience that is due to a risk's inherent differences. From this basic credibility framework emerges a set of formulas by which rates and premiums can be determined, either directly or as an adjustment to current rate levels, in light of the risk's own recent loss experience. While there are a number of specific formulas tailored to particular experience rating approaches, the general idea is reflected in a basic version of a rate modification factor. Letting  $M$  be the experience modification factor (or "mod"):

$$M = \frac{ZA + (1 - Z)E}{E} = \dots = \frac{A + K}{E + K}$$

where the last expression can be derived algebraically from the previous one.

### 7. Credibility Issues in Experience Rating

Two common elements of experience rating plans that relate to the issue of credibility as applied in experience rating are:

- 1) MSL—The Maximum Single Loss is the amount at which individual large losses are capped when they are included in the calculation of a risk's experience,  $A$ . This prevents a single random event from exerting too much influence on the calculation of the mod.
- 2) Min and Max Adjustment—The calculated modification factor is often subject to a minimum and maximum value. These function as a final measure to ensure that the experience rating adjustment is not too extreme.

These two elements, along with the basic credibility framework and the credibility factor itself,  $Z$ , will vary with the size of the risk. The loss experience of larger risks will receive greater credibility than the loss experience of smaller risks. In practice, the size of a risk could be measured using manual premium, expected loss, expected number of claims, or an exposure base (such as sales receipts for GL or power units for commercial auto).

### 8. Split Loss Plans

Another potential feature of an experience rating plan is to separate the individual claims of a risk's loss experience into different layers. This plan is known as a split loss plan.

For example, let's suppose we have an experience rating plan which uses a single loss split at \$5,000 and a risk has the following loss experience:

| Claim # | Incurred Loss Amount |
|---------|----------------------|
| 001     | \$1,150              |
| 002     | \$5,000              |
| 003     | \$3,000              |
| 004     | \$500                |
| 005     | \$50,000             |
| 006     | \$2,000              |
| 007     | \$10,000             |
| 008     | \$6,000              |
| 009     | \$350                |
| 010     | \$12,025             |
| 011     | \$4,500              |

Now let's look at the losses after we split them into layers of \$0 – \$5,000 and \$5,000+.

| <b>Claim #</b> | <b>Incurred Loss Amount</b> | <b>Primary Loss Amount</b> | <b>Excess Loss Amount</b> |
|----------------|-----------------------------|----------------------------|---------------------------|
| 001            | \$1,150                     | \$1,150                    | \$0                       |
| 002            | \$5,000                     | \$5,000                    | \$0                       |
| 003            | \$3,000                     | \$3,000                    | \$0                       |
| 004            | \$500                       | \$500                      | \$0                       |
| 005            | \$50,000                    | \$5,000                    | \$45,000                  |
| 006            | \$2,000                     | \$2,000                    | \$0                       |
| 007            | \$10,000                    | \$5,000                    | \$5,000                   |
| 008            | \$6,000                     | \$5,000                    | \$1,000                   |
| 009            | \$350                       | \$350                      | \$0                       |
| 010            | \$12,025                    | \$5,000                    | \$7,025                   |
| 011            | \$4,500                     | \$4,500                    | \$0                       |
| Total          | \$94,525                    | \$36,500                   | \$58,025                  |

Now instead of comparing just the total loss experience of this risk to an expected amount, we will compare the primary and excess components independently.

Split rating plans—which ordinarily give much more weight to the small portion of losses than to the large portion—can also be thought of as a linear approximation to assigning credibility to the log of the loss amount. Many real loss distributions are skewed with extremely heavy tails. The most predictive estimate might be obtained by normalizing the distribution in some way, such as taking a logarithm of it. But that could lead to messy and complex rating algorithms. The split rating plan is a compromise between simplicity and precision.

One can view these primary and excess components of loss as representing the frequency and severity of the experience, respectively. If the limit for the primary portion of the loss is relatively low, when the actual primary losses exceed the expected primary losses it must mean there have been a higher number of losses than expected. Since the primary losses are truncated from above, a higher than expected outcome cannot be due to a single or small number of very large losses.

The excess component of the loss experience represents severity. It would be difficult for a large number of smaller losses to cause the excess portion of the loss experience to greatly exceed expectation unless the severity of the losses was higher than expected.

The NCCI WC Experience Rating Plan is an example of a split loss plan. The split plan has been found to produce empirically better results for the WC plan than a total or limited loss plan, perhaps because WC loss distributions are very heavy tailed<sup>2</sup>. This can also be thought of as separating the claim count uncertainty (the parameter risk, mostly driven by lots of small Med-only and TT claims) and the severity uncertainty (the process risk, driven by relatively few but influential Major PP, PT, and Fatal claims).

---

<sup>2</sup> See Gillam, W.R., "Parameterizing the Workers' Compensation Experience Rating Plan," PCAS LXXIX, 1992, pp21-56 and Meyers, G., "An Analysis of Experience Rating", PCAS LXXII 1985, pp278-317 for this result and discussions for and against using a split rating plan, and some practical and statistical considerations in choosing an experience rating plan structure.

With respect to credibility, a split plan necessitates a credibility-weighted modification factor ( $M$ ) formula that is adjusted to reflect the two tiers of losses, primary and excess. Using the same underlying framework as described in the prior section, a split plan formula for the mod factor is:

$$M = [Z_p A_p + (1 - Z_p) E_p + Z_e A_e + (1 - Z_e) E_e] \div E$$

where  $A$ ,  $E$ , and  $Z$  are defined as before, and the subscripts  $p$  and  $e$  refer to “primary” and “excess,” respectively. This formula can then be algebraically manipulated to yield:

$$M = 1 + Z_p \frac{(A_p - E_p)}{E} + Z_e \frac{(A_e - E_e)}{E}.$$

This is the framework for determining the modification factor in the context of credibility factors. The NCCI uses a mathematically equivalent formula, but describes the components in terms of “weighting” and “ballast”:

$$M = \frac{A_p + (1 - w)E_e + B + wA_e}{E_p + (1 - w)E_e + B + wE_e} = \frac{A_p + (1 - w)E_e + B + wA_e}{E + B}$$

where  $w$  is the excess loss weighting factor,  $B$  is the ballast value, and other terms are as defined earlier.

### 9. Schedule Rating

Schedule rating is a series of credits and debits that can be used to modify a risk’s rates to reflect the risk’s individual characteristics. Rates can be modified either upward (increased) or downward (decreased), depending on the expected impact on the risk’s loss experience.

A schedule rating plan for commercial general liability coverage might look something like this:

| Risk Characteristic | Description                                  | Range of Modifications: |    |       |
|---------------------|----------------------------------------------|-------------------------|----|-------|
|                     |                                              | Credit                  |    | Debit |
| Location            | Exposure inside the premises                 | 5%                      | to | 5%    |
|                     | Exposure outside the premises                | 5%                      | to | 5%    |
| Premises            | Condition and care of premises               | 10%                     | to | 10%   |
| Equipment           | Type, condition, and care of equipment       | 10%                     | to | 10%   |
| Classification      | Peculiarities of classification              | 10%                     | to | 10%   |
| Employees           | Selection, training, supervision, experience | 6%                      | to | 6%    |
| Cooperation         | Medical facilities                           | 2%                      | to | 2%    |
|                     | Safety Program                               | 2%                      | to | 2%    |

Under this plan, a risk that had a particularly good safety program might receive up to a 2% credit to its manual rates. However, a risk that has a much more inexperienced than average workforce could receive a debit of up to 6% to reflect the fact that inexperienced employees are correlated with worse than average loss experience.

One must be careful to prevent overlap when both schedule rating and experience rating will be applied to a policy. If a risk has made a recent change that will likely impact its loss experience, then it is appropriate to use a schedule credit (or debit). For example, suppose a risk has recently hired a full time safety manager who will oversee operations and be responsible for enforcing appropriate safety measures. This would be expected to have a favorable effect on loss experience and it would be appropriate to apply a schedule credit to reflect this expectation of improved loss experience. Contrast this to another risk who has always had a full-time safety manager on its staff. The effect of the safety manager on this second risk’s experience will already be reflected in its loss experience since the safety manager was there during the experience period. If one applied a schedule credit for having a safety manager to this second risk, the effect of the safety manager would be double-counted—first by the schedule credit and

second by the experience mod. However, if the risk is too small to have fully credible experience, it might be appropriate to give some schedule credit for the safety manager—but less than for the first risk, since the impact of the safety manager is partially credited by the experience mod for the second risk, but not at all for the first.

### 10. Evaluating and Comparing Plans

The following definitions will be helpful for this section:

- Manual Premium—the manual premium refers to the premium calculated based on the criteria in the rating manual. In its simplest form, this is the exposure multiplied by the rates found in the rating manual. This is effectively the premium for a risk before the application of experience rating.
- Standard Premium—this is the premium after the application of the experience rating mod. This is sometimes also referred to as the modified premium, in reference to the fact that it includes the impact of the experience rating modification factor.

In the following discussions of Standard Premium and Standard Loss Ratios in this chapter, we ignore the schedule mod.

An effective experience rating plan should do two things. It should identify risk differences among otherwise similar risks, and it should adjust for them. There is a simple qualitative test that can be used to evaluate a plan based on these criteria, sometimes referred to as the Quintile Test, because it relies on observing the impact of the e-mod among quintiles of the set of risks subject to the plan<sup>3</sup>.

The procedure is as follows:

- Rank order risks by the size of their mod and then collapse into five groups.
- Calculate the manual loss ratio and the standard (modified) loss ratio for each group.
- Observe any trends in the manual or standard loss ratios across the groups.

Consider the following sample of insurance risks which have been experience rated. They have already been ordered from lowest to highest mod.

| Risk | Manual<br>Premium | Loss  | Mod  |
|------|-------------------|-------|------|
| (1)  | (2)               | (3)   | (4)  |
| A    | 950               | 475   | 0.52 |
| B    | 1,075             | 645   | 0.59 |
| C    | 1,225             | 858   | 0.70 |
| D    | 1,100             | 880   | 0.81 |
| E    | 1,175             | 999   | 0.83 |
| F    | 1,050             | 945   | 0.91 |
| G    | 1,000             | 950   | 0.96 |
| H    | 925               | 925   | 0.99 |
| I    | 1,025             | 1,040 | 1.05 |

<sup>3</sup> Paul Dorweiler discussed a slightly more general version of this test as applied to New York Workmen's Compensation in his presidential address to the Casualty Actuarial Society at its twentieth anniversary, "A Survey of Risk Credibility in Experience Rating," *PCAS* XXI, 1934.

|   |       |       |      |
|---|-------|-------|------|
| J | 995   | 1,055 | 1.06 |
| K | 1,150 | 1,254 | 1.08 |
| L | 1,200 | 1,300 | 1.11 |
| M | 900   | 1,040 | 1.14 |
| N | 875   | 1,030 | 1.18 |
| O | 1,125 | 1,450 | 1.22 |

These fifteen risks would collapse into the following five groups:

| Risk Group<br>(5) | Manual Premium<br>(6) | Loss<br>(7) | Avg. Mod<br>(8) | Manual Loss Ratio<br>(9)=(7)/(6) | Standard Loss Ratio<br>(10)=(7)/[(6)*(8)] |
|-------------------|-----------------------|-------------|-----------------|----------------------------------|-------------------------------------------|
| A-B-C             | 3,250                 | 1,978       | 0.61            | 0.61                             | 1.00                                      |
| D-E-F             | 3,325                 | 2,824       | 0.85            | 0.85                             | 1.00                                      |
| G-H-I             | 2,950                 | 2,915       | 1.00            | 0.99                             | 0.99                                      |
| J-K-L             | 3,345                 | 3,608       | 1.08            | 1.08                             | 1.00                                      |
| M-N-O             | 2,900                 | 3,520       | 1.18            | 1.21                             | 1.03                                      |

Column (6) is equal to the sum of the manual premium in column (2) for all the risks in the group; (7) is the sum of the loss in column (3) for all risks in the group; the average mod (8) is equal to the premium weighted average of the mods for each risk in the group.

The first thing we want to check is whether this experience rating plan correctly identifies differences in risks. To do this, we compare the manual loss ratios for the groups. In this plan, there is a distinct and upward trend in the manual loss ratio as the average modification factor increases. Risks with the lowest manual loss ratio received the lowest mods (i.e., they received the most credit) and the risks with the highest manual loss ratio received the highest mods. One would reasonably conclude that this plan does indeed identify differences in risks.

The second thing to check for is whether the plan reasonably adjusts for differences in the risks. To do this, we compare the standard loss ratios for the groups. Notice that the standard loss ratios are much less dispersed than the manual loss ratios and that there is no discernable trend in the standard loss ratios. It would be reasonable to conclude that this plan does indeed account for the differences in the risks.

Now let's look at this same set of risks, but use a different experience rating plan. In this example, the loss and premium experience for each risk is the same as in the previous example, but the mod for each risk is different.

| Risk<br>(1) | Manual Premium<br>(2) | Loss<br>(3) | Mod<br>(4) |
|-------------|-----------------------|-------------|------------|
| A           | 950                   | 475         | 0.49       |
| B           | 1,075                 | 645         | 0.57       |
| C           | 1,225                 | 858         | 0.67       |
| D           | 1,100                 | 880         | 0.78       |
| E           | 1,175                 | 999         | 0.83       |
| F           | 1,050                 | 945         | 0.89       |
| G           | 1,000                 | 950         | 0.95       |
| H           | 925                   | 925         | 1.01       |

|   |       |       |      |
|---|-------|-------|------|
| I | 1,025 | 1,040 | 1.04 |
| J | 995   | 1,055 | 1.09 |
| K | 1,150 | 1,254 | 1.10 |
| L | 1,200 | 1,300 | 1.14 |
| M | 900   | 1,040 | 1.23 |
| N | 875   | 1,030 | 1.24 |
| O | 1,125 | 1,450 | 1.34 |

Grouping the risks and calculating the manual and standard loss ratios by group as we did above will give us:

| Risk Group<br>(5) | Manual Premium<br>(6) | Loss<br>(7) | Avg. Mod<br>(8) | Manual Loss Ratio<br>(9)=(7)/(6) | Standard Loss Ratio<br>(10)=(7)/[(6)*(8)] |
|-------------------|-----------------------|-------------|-----------------|----------------------------------|-------------------------------------------|
| A-B-C             | 3,250                 | 1,978       | 0.59            | 0.61                             | 1.04                                      |
| D-E-F             | 3,325                 | 2,824       | 0.83            | 0.85                             | 1.02                                      |
| G-H-I             | 2,950                 | 2,915       | 1.00            | 0.99                             | 0.99                                      |
| J-K-L             | 3,345                 | 3,608       | 1.11            | 1.08                             | 0.97                                      |
| M-N-O             | 2,900                 | 3,520       | 1.28            | 1.21                             | 0.95                                      |

Notice that there is a downward trend in the standard loss ratios by group as the average mods increase. The risks with the best loss experience in the past now actually have higher loss ratios than the risks with the worst past loss experience in the group. This indicates that the experience rating plan is giving too much credibility to the risks' actual experience. The risks with the lowest mods are getting credit for better than average experience more than the experience is predictive of their future loss experience. The result is that their premium is reduced so much that their loss ratios are now higher than average. Likewise, the risks with the highest past loss experience are getting penalized too much under this plan. The result is that they now have lower loss ratios than the rest of the risks in the group.

This scenario is undesirable. Recall from earlier that the objectives of an experience rating plan include increasing equity and enhancing market competition. This second rating plan does not enhance equity because the risks with the highest mods are paying more premium than is equitable. This plan also does not enhance market competition. This plan generates a scenario where risks with higher past loss experience will generate a lower loss ratio and therefore higher profits. These risks will be more desirable for the insurer to write than risks with better past loss experience. This is contrary to the desire to enhance market competition by making ALL risks equal in terms of profit potential and therefore equally desirable to write.

Analogous to the previous example would be a scenario where there was an upward trend (higher standard loss ratios for groups with higher mods). This would indicate that the plan does not give enough credibility to actual experience. Risks with better than average past loss experience would not get enough credit and would continue to have lower than average loss ratios. Meanwhile, risks with higher than average past loss experience would continue to produce higher loss ratios even after the experience rating plan is applied. A good experience rating plan will have no discernable trend in the modified loss ratios.

We can also quantify the efficiency of an experience rating plan by comparing its results across the quintiles. Similar to above, we rank risks by their mod and combine them into five groups. We then calculate the manual and standard loss ratios for each group. For each plan, calculate the efficiency test statistic as the ratio of the variance of the standard loss ratio to the variance of the manual loss ratio<sup>4</sup>. The plan with the lower variance ratio is "better"—it does a better job at adjusting premium; i.e., it makes "risks of differing experience more equally desirable".

---

<sup>4</sup> This test statistic was first described by Robbin Gillam as a "quintiles test" in "Worker' Compensation Experience Rating: What Every Actuary should know", *PCAS LXXIX*, 1992, pp. 215-239.

Let's use the Efficiency Test to compare the experience rating plans in the last two examples. For clarity, we'll refer to the experience rating plan in the first example as Plan A and the second as Plan B.

| Risk Group                | Manual Loss  | Plan A<br>Standard | Plan B<br>Standard |
|---------------------------|--------------|--------------------|--------------------|
| (1)                       | Ratio<br>(2) | Loss Ratio<br>(3)  | Loss Ratio<br>(4)  |
| A-B-C                     | 0.61         | 1.00               | 1.04               |
| D-E-F                     | 0.85         | 1.00               | 1.02               |
| G-H-I                     | 0.99         | 0.99               | 0.99               |
| J-K-L                     | 1.08         | 1.00               | 0.97               |
| M-N-O                     | 1.21         | 1.03               | 0.95               |
| Sample Variance           | 0.0536       | 0.0002             | 0.0013             |
| Efficiency Test Statistic |              | 0.0039             | 0.0237             |

The test statistic for Plan A is lower than for Plan B. As expected, the result of the Efficiency Test is that Plan A is a better experience rating plan.

### Questions

1. What are the objectives of experience rating?
2. Explain how experience rating increases equity.
3. Consider two insurance companies writing an identical line of business. Company A has developed a very sophisticated classification plan for rating risks which incorporates many different risk characteristics to assign a risk into one of several dozen classes. Company B has a much simpler rating plan which considers fewer risk characteristics and has only half a dozen rating classes. Which company would benefit more from using experience rating?
4. Explain how the use of experience rating can help an insurance company avoid adverse selection.
5. Discuss the concepts of process variance and the variance of the hypothetical means (VHM) and how they relate to experience rating.
6. Suppose you are pricing a risk (which will be experience rated). This particular risk has a significantly better safety program than most other risks. Would it be appropriate to apply a schedule credit to reflect lower than average loss potential due to this superior safety program?

### Acknowledgments

This chapter would not have been possible without significant contributions by Rick Gorvett. I would also like to thank Ginda Fisher, Lawrence McTaggart, and Jill Petker for their support, advice, and assistance.



