

![Yellow circle graphic](2dfa6ac3edfe874f68aa0cbccaa42322_img.jpg)

A solid yellow circle, likely a decorative element or part of a logo.

Yellow circle graphic

# INDIVIDUAL RISK RATING

Study Note, October 31, 2019

Ginda Kaplan Fisher  
Lawrence McTaggart  
Jill Petker  
Rebecca Pettingell

![CAS logo](5fb340ad68b0c71df0b56698b137e35b_img.jpg)

The logo for the Casualty Actuarial Society (CAS). It features the letters 'CAS' in white, stylized font, set against a blue circular background. A small yellow dot is positioned below the 'A'.

CAS logo

**Expertise. Insight.  
Solutions.**

© Casualty Actuarial Society, 2019

# Individual Risk Rating Study Note

Ginda Kaplan Fisher, Lawrence McTaggart, Jill Petker, and Rebecca Pettingell



## Contents

|                                                                                                  |    |
|--------------------------------------------------------------------------------------------------|----|
| Foreword.....                                                                                    | 1  |
| Chapter 1: Experience Rating .....                                                               | 3  |
| 1. Introduction/Definition .....                                                                 | 3  |
| 2. Advantages of Experience Rating .....                                                         | 3  |
| 3. Differences within Class .....                                                                | 3  |
| 4. Objectives/Goals .....                                                                        | 4  |
| 5. Equity .....                                                                                  | 4  |
| 6. Credibility .....                                                                             | 5  |
| 7. Credibility Issues in Experience Rating.....                                                  | 7  |
| 8. Split Loss Plans .....                                                                        | 7  |
| 9. Schedule Rating .....                                                                         | 9  |
| 10. Evaluating and Comparing Plans.....                                                          | 10 |
| Acknowledgments.....                                                                             | 15 |
| Chapter 2: Risk Sharing Through Retrospective Rating and Other Loss Sensitive Rating Plans ..... | 17 |
| 1. Risk Sharing: Risk Retention and Risk Transfer .....                                          | 17 |
| 2. What is Retrospective Rating?.....                                                            | 18 |
| 3. The Retrospective Rating Formula .....                                                        | 19 |
| 4. Regulatory Approval and the Large Risk Alternative Rating Option (LRARO) .....                | 22 |
| 5. Other Loss Sensitive Plans.....                                                               | 23 |
| 6. Other Variations on Loss Sensitive Plans .....                                                | 25 |
| 7. Credit Risk .....                                                                             | 26 |
| 8. Setting Retention Levels .....                                                                | 27 |
| 9. Capital and Profit Provisions .....                                                           | 27 |
| 10. The Dissolution of Loss Sensitive Rating Plans for Long-Tailed Lines .....                   | 28 |
| Acknowledgments.....                                                                             | 31 |
| Appendix to Chapter 2: Examples of Expected Cash Flow.....                                       | 32 |
| Chapter 3: Aggregate Excess Loss Cost Estimation.....                                            | 35 |
| 1. Overview .....                                                                                | 35 |
| 2. Visualizing Aggregate Excess Losses .....                                                     | 45 |

|                                                                                           |           |
|-------------------------------------------------------------------------------------------|-----------|
| 3. Estimating Aggregate Loss Costs Using Table M.....                                     | 59        |
| 4. Estimating Limited Aggregate Excess Loss Costs.....                                    | 70        |
| 5. Other Methods of Combining Per-Occurrence and Aggregate Excess Loss Cost.....          | 77        |
| 6. Understanding Aggregate Loss Distributions.....                                        | 87        |
| Acknowledgments.....                                                                      | 92        |
| <b>Chapter 4: Concluding Remarks .....</b>                                                | <b>93</b> |
| 1. General Observations .....                                                             | 93        |
| 2. Sensitivity of Table M charges to the Accuracy of the Loss Pick or Rate Adequacy ..... | 94        |
| 3. Consistency of Assumptions.....                                                        | 96        |
| Acknowledgments.....                                                                      | 96        |
| Solutions to Chapter Questions.....                                                       | 97        |
| References .....                                                                          | 109       |

## Foreword

By Lawrence McTaggart

This study note introduces concepts and methods employed when supporting Excess, Deductible and Individual Risk pricing. The authors intend to provide a better experience for candidates by consolidating insights from several foundational papers, providing examples beyond U.S.-based workers' compensation practice, and introducing a few fresh insights.

Chapter 1 provides a summary of experience rating. An experience rating plan prospectively adjusts manual premium based on a policyholder's past experience. The more an individual risk's past experience differs from what is expected of risks in the rating manual classification, the greater the experience modification to the individual risk's manual premium.

Chapter 2 provides an overview of various loss sensitive rating plans. As insureds grow in size their appetite for risk grows. Loss sensitive rating plans allow insureds to retain a portion of their actual loss experience, fulfilling their desire to share in the risk, or reward, of their actual loss experience. Insureds and insurers negotiate the terms of loss sensitive policies, and an actuary will be asked to provide pricing for many different combinations of per-occurrence and aggregate retentions.

Chapter 3 introduces aggregate excess loss estimation. Estimates of aggregate excess loss contemplate both the severity of claims and the number of claims. The expected number of claims for a policy is, in part, a function of the size of the risk. Thus aggregate excess loss estimation considers risk size. Claim severity is a function, in part, of retentions and limits. Visualizing how a loss sensitive plan's insured retentions and insurer limits for both per-occurrence and aggregate boundaries is an important first step when pricing individual loss sensitive rating plans.

Chapter 4 concludes the study note with cautions associated with pricing excess and aggregate loss. Understanding a few of the ways bias can creep into an estimate begins to build the ability to discern estimates that may be biased, and defend estimates that are perceived by others to be biased.

The Excel-based Case Study applies the methods from the readings to a single set of fictional claims data. The Case Study is intended to provide greater clarity and understanding. In practice, or on the exam, the combinations of loss sensitive contract retentions, limits and aggregates is practically unlimited.

The authors hope this study note will help casualty actuaries world-wide understand and master these concepts.



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



# Chapter 2: Risk Sharing Through Retrospective Rating and Other Loss-Sensitive Rating Plans

By Jill Petker

### 1. Risk Sharing: Risk Retention and Risk Transfer

Retrospective rating and other loss-sensitive rating plans allow risk sharing between the insured and the insurer. This chapter will look at how risk sharing is achieved through retrospective rating, large deductibles, self-insurance arrangements, and other loss-sensitive rating plans. This risk-sharing contrasts with guaranteed-cost policies, where the insured's premium is fixed up front and the insured does not share in their own risk, except perhaps through a small deductible. We start with retrospective rating because it is a direct contrast to the experience rating that you already learned about through the Basic Ratemaking syllabus and in Chapter 1 of this study note. In current practice, however, large deductible plans are more common than retrospective rating. When sharing risk, the insured's risk tolerance and financial capacity are typically better suited to their retaining the risk associated with the more predictable primary losses while transferring the risk associated with the more volatile and uncertain per-occurrence excess losses to the insurer. However, even the primary layer of loss can be volatile (driven by frequency or even severity within the primary layer). Therefore, the primary risk that the insured retains is often limited in aggregate to a specified amount. The risk of having primary losses in excess of the insured's aggregate retention is transferred to the insurer.

The advantages to the insured of risk sharing through loss-sensitive rating plans include:

- An incentive for loss control, which affects their direct costs as well as indirect costs, such as lost productivity for Workers Compensation
- The immediate reflection of good loss experience, without the lag and credibility-weighting that come with experience rating
- Cash flow benefits from paid loss retrospective rating plans, large deductible plans, and self-insurance, all of which are described further below
- A possible reduction in premium-based taxes and assessments (under large deductible plans in particular)

The disadvantages to the insured include:

- Uncertain costs, compared to a fixed premium under guaranteed-cost plans
- The loss of the immediate tax deductibility of full guaranteed-cost premium
- The immediate reflection of bad loss experience
- Impact on future financial statements
- Ongoing administrative costs, e.g., paying bills long into the future
- The need to post security as collateral against credit risk (discussed further below)
- Added complexity, compared to guaranteed-cost plans

The advantages to the insurer include:

- The insured's incentive for loss control, which is stronger than the incentive provided by experience rating alone

- Ability to write some risks which the insurer would not find acceptable to write on a guaranteed-cost basis
- Less capital required to write policies under which the insured shares in their risk. (See section on capital and profit provisions below.)

The disadvantages to the insurer include:

- Higher administrative costs
- Credit risk (discussed below)
- A reduction in cash flow to the extent that insureds pay for their retained losses over time, as opposed to paying premium to cover all of their expected losses during the policy period, as under guaranteed-cost plans
- Insureds' tendency to second-guess claims handling and ALAE costs
- Insureds' tendency to question the size of profit provisions since they are taking on a share of the risk. (Again, see section on capital and profit provisions below.)

### 2. What is Retrospective Rating?

You have learned about how experience rating uses an insured's loss experience from historical policy periods to adjust their premium for the upcoming policy period. In contrast, retrospective rating uses an insured's loss experience from a policy period to adjust the premium for that same policy period. Adjustments to the policy premium are made "retrospectively" upon review of actual loss experience.

Risk sharing under a retrospective rating plan follows the format outlined in the section above, in that it is generally a primary layer of loss that is used to retrospectively adjust the policy premium. However, to protect the insured from volatility, the primary losses that influence the retrospectively rated premium will generally be subject to a maximum "ratable" loss amount. That maximum ratable loss amount may either be established directly, or it may correspond to a maximum premium amount. In addition, the primary losses that influence the retrospectively rated premium may be subject to a minimum ratable loss amount, which again may either be established directly or may correspond to a minimum premium amount.

### 3. The Retrospective Rating Formula

Premium under a retrospective rating plan is calculated as **Premium = (B + cL) × T**, where **B** is the basic premium amount, **c** is the loss conversion factor, **L** is the loss amount that will be used in the calculation, and **T** is the tax multiplier. Each of these components is discussed further below.<sup>5</sup>

**B** is called the **basic premium amount**. It reflects fixed charges (i.e., those that won't vary with actual losses), such as:

---

<sup>5</sup> If you are practicing in the US, you may find it helpful to review both NCCI's and ISO's retrospective rating plan manuals for detailed requirements and options specific to their lines of business. Examples of specifics related to those retrospective rating plans are included in the footnotes below. This chapter is intended to be a general discussion not specific to either the NCCI's or ISO's specific retrospective rating plans.

- Expenses for which the charge will be a fixed amount. Typical fixed expenses include underwriting expenses and commission (if commission is a fixed amount or a percentage of guaranteed-cost premium).
- Expected per-occurrence excess losses, if losses influencing the premium are subject to a per-occurrence loss limit. Estimating an appropriate charge for per-occurrence excess losses is often done by applying an expected ratio of excess/total losses to the total loss estimate for the policy. The estimation of expected ratios of excess/total losses is discussed in the CAS monograph *Distributions for Actuaries*. Sometimes you will see the per-occurrence excess loss component as a separate provision.<sup>6</sup> In that case, it may be called an excess loss premium. This excess loss premium generally includes a provision for the loss adjustment expenses associated with the per-occurrence excess losses (see more on this below).
- Expected aggregate excess losses, if losses influencing the premium are subject to a maximum ratable loss amount or if the retrospectively rated premium is subject to a maximum premium amount. This is often referred to as the **insurance charge**. Estimating an appropriate charge for aggregate excess losses will be discussed in Chapter 3. This component of the basic premium also generally includes a provision for the loss adjustment expenses associated with the aggregate excess losses.
- A credit if losses influencing the premium are subject to a minimum ratable loss amount or if the retrospectively rated premium is subject to a minimum premium amount. This amount is often referred to as the (insurance) **savings**. The combination of the savings and the insurance charge described above is often referred to as the **net insurance charge**. Estimating the savings will be discussed in Chapter 3.
- The underwriting profit provision, which will be discussed further below.

**c** is called the **loss conversion factor**. It covers expenses for which the charge is going to vary with actual losses. Typically the loss conversion factor would include loss adjustment expenses, and may also include loss-based assessments. If desired, expenses can be shifted back and forth between the basic premium and the loss conversion factor. However, it may not be prudent to charge for expenses that don't vary with losses through the loss conversion factor. If losses are lower than expected, those expenses will not be fully recouped.

To reflect the ability to shift expenses back and forth between the basic premium and the loss conversion factor, the following formula is often used to calculate the expense portion of the basic premium (as a percentage of the guaranteed-cost premium):  $e - (c-1) \times E$ , where:

- **e** is the expense ratio underlying the guaranteed-cost premium. This expense ratio reflects the premium discount (recognizing that expenses are a lower percentage of premium for large accounts) but excludes premium-based taxes and assessments. It includes loss adjustment expenses.
- **c** is the selected loss conversion factor.

---

<sup>6</sup> Under NCCI's and ISO's retrospective rating plans, the charge for per-occurrence excess losses is a separate component in the formula. So the formula for retrospective premium becomes: Premium = (Basic Premium + Excess Loss Premium +  $c \times$  Ratable Loss)  $\times$  T

- **E** is the expected loss ratio underlying the guaranteed-cost premium.

You can see that as **c** increases, the expense portion of the basic decreases, and vice versa. **L** represents the losses that will be used to calculate the retrospective premium. These losses are often called “**ratable**” losses because they are used to calculate the retrospectively rated premium amount. Options related to these losses include:

- They may or may not include Allocated Loss Adjustment Expense (ALAE).<sup>7</sup> When the ratable losses include ALAE:
  - The loss adjustment expenses that would be typically covered through the loss conversion factor **c** would be just Unallocated Loss Adjustment Expense (ULAE).
  - Similarly, the expense ratio **e** would include ULAE but not ALAE.
  - The expected loss ratio **E** mentioned above would be an expected loss-and-ALAE ratio.

When the ratable losses exclude ALAE:

- The loss adjustment expenses that would be typically covered through the loss conversion factor **c** would be both ALAE and ULAE.
  - Similarly, the expense ratio **e** would include both ALAE and ULAE.
  - The expected loss ratio **E** mentioned above would be an expected loss-only ratio.
- They may or may not be subject to a per-occurrence loss limit. If they are, as mentioned above, the charge for the expected losses above the per-occurrence loss limit may be included in the basic premium amount or may be kept separate from the basic premium.<sup>8,9</sup>
  - Note that **E** in the formula above (for the expense amount to be included as fixed in the basic premium) represents total losses – limited to the policy limit if there is one, but not limited otherwise. As such, the loss conversion factor **c** is intended to be applied to total losses. Therefore, the charge for expected losses above the per-occurrence loss limit needs to have the loss conversion factor **c** applied to it.
- They may or may not be subject to an aggregate loss limit. If they are, as mentioned above, the charge for the expected (limited per occurrence, if applicable) losses above the aggregate loss limit is generally included in the basic premium amount.<sup>10</sup> This charge needs to have the loss conversion factor **c** applied to it for the same reason described above. Aggregate loss limits are often set in one of these two ways:
  - As a multiple of the expected losses that will be subject to the aggregate limit (i.e., either full losses or losses limited by the per-occurrence loss limit mentioned above). For example, if the per-occurrence loss limit is \$250,000 and the expected limited

---

<sup>7</sup> Under ISO’s retrospective rating plan, losses for commercial auto liability, general liability, and hospital professional liability must include ALAE. See their retrospective rating plan manual for details.

<sup>8</sup> A per-occurrence loss limit is required under ISO’s retrospective rating plan but is optional under NCCI’s plan. See their retrospective rating plan manuals for details.

<sup>9</sup> Under ISO’s retrospective rating plan, ALAE is included on an unlimited basis for commercial auto liability, general liability, and hospital professional liability. However, there is an optional cross-lines accident limitation that does limit ALAE. See their retrospective rating plan manual for details.

<sup>10</sup> Under both NCCI’s and ISO’s retrospective rating plan, a maximum premium amount is required. See their retrospective rating plan manuals for details.

losses are \$300,000, then the aggregate loss limit might be set at twice the expected limited losses, or \$600,000. If the selected multiple is 2.5, then the aggregate loss limit would be \$750,000.

- So that the maximum premium under the retrospective rating plan will be a multiple of the guaranteed-cost premium. For example, if the guaranteed-cost premium is \$1,000,000 and the selected multiple is 1.25, then the aggregate loss limit would be set such that the maximum retrospectively rated premium would be \$1,250,000. This method requires an iterative pricing approach, since backing into the implied maximum ratable loss increases the basic premium amount by adding a charge for the expected losses above that maximum ratable loss amount, in turn reducing the implied maximum ratable loss that will produce the selected maximum premium. Reducing the maximum ratable loss amount will then increase the insurance charge, thereby further reducing the implied maximum ratable loss. A few rounds of iteration should stabilize the maximum ratable loss amount.

Notice that under the second approach, the aggregate loss limit will automatically increase or decrease if exposures increase or decrease, since the exposure change will be reflected in the guaranteed-cost premium after the premium (exposure) audit. Under the first approach, the aggregate loss limit can also be made to increase or decrease with exposures if the limit is first calculated based on expected limited losses but then translated to a rate per exposure.

- They may or may not be subject to a minimum ratable loss amount. If they are, as mentioned above, the basic premium amount generally includes a credit. Note that even if there is no minimum ratable loss amount, there is still a minimum premium amount that will be charged – you can see from the retrospective rating formula that the minimum premium will be equal to the basic premium times the tax multiplier.
- They may be paid or incurred. If the premium is calculated based on paid losses, the plan is called a paid loss retrospective rating plan. If the premium is calculated based on incurred losses, the plan is called an incurred loss retrospective rating plan. Paid loss retrospective rating plans are often converted to an incurred loss basis at a pre-determined point in time (e.g., after five years).

There must be either a per-occurrence loss limit or an aggregate loss limit (or both) for there to be risk transfer to the insurer.

- If there is a per-occurrence loss limit but not an aggregate loss limit, and the coverage is Workers Compensation or Auto Liability (coverages with no aggregate policy limit), the insured is technically retaining an unlimited amount of loss exposure.
- If there is an aggregate loss limit but no per-occurrence loss limit, and if the aggregate loss limit is relatively low, then the aggregate loss limit can be used up by a few (and sometimes just one) large losses. This could eliminate the insured's loss control incentive before the policy is expired. If there is no per-occurrence loss limit and the aggregate loss limit is relatively high, the retrospective premium can be very unstable (driven by the volatility of large losses).

Note that total expected loss amount equals the sum of these components: the expected per-occurrence excess losses, the expected aggregate excess losses (net of any savings related to minimum ratable losses), and the expected ratable losses. Were it not for the increased incentive for loss control under loss-sensitive rating plans, the total expected loss amount under a retrospective rating plan would equal the total expected loss amount under a guaranteed-cost plan. It is a requirement under some retrospective rating plans filed in the US that the expected premium under a retrospective rating plan also equal the expected premium under a guaranteed-cost plan. However, this requirement (often called “the balance principle”) does not make sense given the difference in risk transfer and the resulting difference in capital needed to support a retrospective rating plan vs a guaranteed-cost plan. See the section on Capital and Profit Provisions below.

For incurred loss retrospective rating plans, losses are typically first evaluated as of 6 months after the policy expiration (i.e. 18 months of development), and then annually thereafter. Since losses at 18 months are typically much lower than their ultimate level, the insured would typically receive a partial return of premium at that first evaluation. Then, as losses develop upwards at later evaluations, the insured would typically pay additional premium amounts. These additional premium amounts create credit risk for the insurer. See the section on Credit Risk below for a further discussion of credit risk and the ways in which insurers can mitigate that risk.

For paid loss retrospective rating plans, losses are typically evaluated monthly, beginning with the first month of the policy period. Therefore, the retrospectively rated premium amount increases as paid losses develop upwards. This creates credit risk for the insurer, which again, is discussed below.

T is called the **tax multiplier**. It is calculated as  $1/(1 - \text{tax rate})$ , where the tax rate may include residual market and other premium-based assessments. If commission is a percentage of the net premium (i.e., net of retrospective rating adjustments), then commission would be included with the tax rate, and not in the basic premium amount.

### **4. Regulatory Approval and the Large Risk Alternative Rating Option (LRARO)**

In the US, the pricing methodology and parameters for retrospective rating plans generally must be filed and approved by state regulators.<sup>11</sup> Those plan parameters include the expected loss ratio to be applied to guaranteed-cost premium in order to estimate the total expected losses, the expense ratio, per-occurrence excess losses as a ratio to total losses, the table of insurance charges that will be discussed further in Chapter 3, and the tax multiplier.

However, there is a Large Risk Alternative Rating Option under both ISO’s and NCCI’s retrospective rating plans in most states that allows large insureds to be retrospectively rated “as mutually agreed upon by carrier with insured.” “Large” is generally defined in terms of standard premium individually or in any combination with WC, GL, Auto, Crime, and a few other lines of business. A key assumption underlying LRARO is that large risks are knowledgeable and sophisticated enough to negotiate with insurers their retrospective rating parameters. Although LRARO allows for pricing flexibility, pricing still must comply with regulatory principles and not be inadequate, excessive, or unfairly discriminatory.

In addition to allowing flexibility in pricing, LRARO also allows flexibility in structure.

Examples include:

---

<sup>11</sup> Outside of the US, there is much less rate regulation for commercial insurance. Wherever you are practicing, be sure to understand and follow the rate regulation in place for that jurisdiction.

- NCCI's standard retrospective rating plan for WC only includes incurred loss retrospective rating plans. A paid loss basis requires the use of LRARO. Here, LRARO's pricing flexibility is important so that the insurer can reflect in its pricing the loss of investment income under a paid loss basis relative to an incurred loss basis.
- Maximum and minimum ratable loss amounts can be set directly, rather than indirectly through maximum and minimum premium amounts.
- The basic premium factor and/or the maximum and minimum ratable loss amounts can be based on exposures instead of standard premium, if that is deemed to be more appropriate or convenient.

### 5. Other Loss-Sensitive Plans

Other loss-sensitive plan types include the following:

- Large Deductibles: In the US, large deductibles for casualty lines of business are generally considered to be those at or above \$100,000 per occurrence.
  - Because insurers wish to direct the handling of casualty claims from the start (and insureds are not typically set up to adjust and pay claims) insurers pay all claims up front and bill the insured for deductible reimbursements up to the per-occurrence deductible amount.
  - Like a retrospective rating plan, the losses that are subject to deductible reimbursement may or may not include ALAE.
  - Unlike a retrospective rating plan, however, the losses that are subject to deductible reimbursement must be subject to a per-occurrence loss limit (i.e., the deductible).
  - Like a retrospective rating plan, the insured's deductible reimbursements may or may not be capped at an aggregate deductible limit.
  - Unlike a retrospective rating plan, however, there is no analog to the minimum ratable loss amount. That is, there is no minimum deductible reimbursement.
  - Notice that the risk transfer under a large deductible is the same as the risk transfer under a retrospective rating plan that has a per-occurrence loss limit and a maximum ratable loss amount but does not have a minimum ratable loss amount. Per-occurrence and aggregate excess loss risk are transferred to the insurer.
  - Under a large deductible plan, the premium is generally fixed. However, the insured's cost (premium plus loss reimbursements under the deductible) is not fixed. A large deductible plan is considered to be a loss-sensitive plan because the insured's total cost for the policy period varies based on actual loss experience.
  - The premium for a large deductible must cover the same components that a retrospective rating plan's premium covers, with one exception: The premium does not cover the expected cost of losses below both the per-occurrence deductible and aggregate deductible limit.
  - Net premium (i.e., premium net of the deductible credit) still must cover the expected per-occurrence excess losses, expected aggregate excess losses (if

applicable), expenses, and an underwriting profit provision. Relative to the premium for a retrospectively rated policy:

- The charge for expected excess losses is the same.
- The provisions for most expenses are the same, except:
  - The provisions for premium tax and some premium-based assessments (if based on net-of-deductible premium) are lower because the deductible reimbursements are not premium and therefore are not subject to those taxes and assessments.
  - The provision for commission may be lower if commission is a percentage of net premium. (Alternatively, commission may be a percentage of guaranteed-cost premium, a flat allowance, or zero if a fee for service is paid directly by the insured to the agent or broker. Note that these same alternatives are available for retrospective rating plans as well.)
  - Because of these exceptions, the insured's expected cost is generally lower under a large deductible plan.

See question 9, the appendix, and the companion case study for examples of how to calculate the net premium under a large deductible plan.

- Note that as the deductible becomes large, the expected (excess) loss component of the premium can become very small relative to the expense and underwriting profit provisions. Thus the premium for a high deductible can appear to be surprisingly large. However, the expenses do not go away and the risk load applicable to the excess losses can be quite large due to the significant amount of both parameter risk and process variance.
- Self-Insured Retentions: Self-insured retentions (SIRs) are similar to large deductibles, but differ in these important ways:
  - In the US, self-insurance for Workers Compensation and Auto Liability requires regulatory approval, because they are both legally required coverages.
  - The insured is responsible for adjusting and paying claims or making arrangements for someone else to do those tasks. They may self-administer the claims or hire a third-party claims administrator. Many insurers have affiliated third-party claims administrators, so the insured may find it convenient to purchase claims-handling services from the same insurer from whom they buy excess loss coverage (per-occurrence and/or aggregate). However, some insureds value the control that choosing the party responsible for claims handling gives them. Insurers reimburse the insured for loss amounts in excess of the self-insured retention.
  - Because the insurer is not handling claims up front, it is not incurring ALAE for claims that stay within the self-insured retention. Therefore, the retention generally applies to pure loss only, and ALAE is generally shared pro-rata for claims that exceed the retention.

- In addition, because the insurer is not handling claims up front, only a minimal amount of ULAE is included in the premium for excess-over-SIR coverage. Therefore there is an even greater expense savings due to having a lower base for premium taxes and some premium-based assessments.
- Because the insurer is not responsible for claims until after they have been paid by the insured, the insurer does not take on credit risk for the loss-sensitive feature. See below for more on credit risk.
- The policy limit for excess-over-SIR coverage is generally not eroded by the self-insured retention. This contrasts with the limit for large deductible coverage, which generally is eroded by losses within the deductible. For example, excess-over-SIR coverage with a \$1m limit over a \$250k per-occurrence retention would cover the layer of losses between \$250k and \$1,250k. However, a large deductible policy with a \$1m limit and a \$250k deductible transfers the layer of losses between \$250k and \$1m, essentially only providing \$750k of coverage. Note that when excess-over-SIR coverage is provided for Workers Compensation, a policy limit can be applied (as opposed to the usual statutory limits, which is essentially unlimited).
- Dividend Plans: Some dividend plans have loss-sensitive features that act similar to incurred loss retrospective rating plans, but with two important distinctions:
  - If the insured's losses are lower than expected, the money that is returned to the insured is not considered a premium credit for accounting purposes. Instead, it is considered to be an expense paid by the insurer. As such, there is no savings in premium-based taxes and assessments.
  - If the insured's losses are higher than expected, no additional money is collected from the insured. In this way, loss-sensitive dividend plans are not balanced in terms of the expected "ratable" losses.

Like incurred loss retrospective rating plans, losses under loss-sensitive dividend plans are often evaluated six months after the policy expires and then annually thereafter. If reported losses develop upwards (the most likely scenario), the indicated dividend will decrease. Dividend amounts already paid at earlier evaluations may need to be partially recouped from the customer. Thus loss-sensitive dividend plans also create credit risk for the insurer, which is discussed below.

Dividend payments generally are not contractually guaranteed and generally require approval from the insurer's board of directors.

### 6. Other Variations on Loss-Sensitive Plans

- Clash Coverage: When an insured has exposures covered by more than one loss-sensitive plan, they may wish to limit their exposure to a single occurrence that impacts their retentions across multiple lines of business. Often referred to as a Clash Deductible or Clash Aggregate, the coverage defines a single dollar amount for the sum of retained loss payments from an occurrence that impacts multiple lines of business. For example, an insured may have large deductible policies for Workers Compensation and Auto Liability

with deductibles of \$250k and \$100k, respectively. They may purchase clash coverage so that if an at-fault auto accident injures both their employee and a third party, their total retention will be only \$300k instead of \$350k. This coverage is difficult to price and may require the use of simulations with assumptions around frequencies, severities, and correlations between lines of business.

- Basket Aggregate Coverage: When an insured has exposures covered by more than one loss-sensitive plan, a Basket Aggregate (sometimes called Account Aggregate) policy can provide a total aggregate limit on all reimbursable or ratable losses from the underlying plans. Typically, the underlying plans are written with no aggregate deductible limits or maximum ratable loss amounts. A separate GL policy reimburses the insured for losses in excess of a specified maximum aggregate retention for the insured, up to a specified policy limit.
- Multi-Year Plans: Retrospective rating plans, large deductible plans, and basket aggregates are sometimes written as multi-year plans. Three years is a typical term. One goal is to stabilize costs by lengthening the experience period. The thought here is that good and bad years offset each other and reduce the insurance charge. However, loss trends for the longer policy period must be built into the charges for both per-occurrence and aggregate excess exposure. In addition, contract wording should allow for rate adjustment when exposures change significantly during the policy period. Also, credit risk increases as the insurer must evaluate the potential for the financial condition of the insured to deteriorate over a longer time horizon. Multi-year plans tend to become popular during soft markets as insureds attempt to lock in favorable rates.
- Captives: Captives are insurance companies formed to serve the insurance needs of their parent companies. They offer another avenue for risk sharing, although the risk sharing mechanism here is often reinsurance. That is, insurers will often write policies to provide coverage and then cede losses (usually primary, and usually limited to an aggregate amount) to the captive.

### 7. Credit Risk

Retrospective rating, large deductible, and loss-sensitive dividend plans subject insurers to credit risk. Insurers are depending on the customer to be willing and able to pay additional premium amounts, loss reimbursements, or returns of dividend amounts in the future. This is particularly true for paid loss retrospective rating plans and large deductible plans, but it is also true of incurred loss retrospective rating plans and loss-sensitive dividend plans at early maturities. Note that credit risk increases for long-tailed lines and for higher loss limits or deductibles. This is because the timeframe for collectible amounts grows longer, so the insurer is at greater risk of the insured becoming unable or unwilling to continue to pay those amounts during that timeframe.

There are several approaches available to insurers to protect themselves from this credit risk:

1. Security: The insurer can hold collateral against the amounts that are expected to be paid by the insured in the future. This approach can be used for either retrospective rating plans or

large deductible plans. For insureds with a weaker financial position, insurers may want to hold collateral to an amount higher in the range of loss outcomes.

2. **Loss Development Factors:** The insurer can apply loss development factors to the losses used in the retrospective premium or dividend formula. This is typically not done for paid loss retrospective rating plans, as those plans are typically intended to mimic the cash flows of a large deductible plan (see the appendix for examples of expected cash flows under an incurred retrospective rating plan vs. a large deductible plan). The loss development factors are generally established up front when the retrospective rating plan is written.<sup>12</sup> This option is not available for large deductible plans.
3. **Holdbacks:** The insurer and the insured can agree up front to defer all or a portion of retrospective premium adjustments and/or dividend payments until a specified maturity.<sup>13</sup> Again, this is typically not done for paid loss retrospective rating plans.

### **8. Setting Retention Levels**

There are several considerations that should be taken into account when setting retentions levels for an insured:

- Per-occurrence retentions should generally be set so that the insured keeps the more predictable “working layer” of losses, which is the layer in which there is a relatively high rate of frequency. The insurer should take on the more volatile loss exposure above that level, where there is less frequency but where the claims can become quite large.
- The retentions should be within the insured’s risk tolerance. Insureds who are more risk averse or who want more stability in their insurance-related costs will not feel comfortable taking on high retentions.
- The retentions should reflect the insured’s financial capacity. When credit risk is an issue, the insurer may wish to set lower retentions in order to reduce credit risk.
- The retentions should increase with loss trend. If they do not, over time the effectiveness of the retentions will erode. This is particularly an issue for per-occurrence retentions, which are established as fixed dollar amounts. With inflation, more and more claims will exceed a fixed dollar amount. This is less of an issue for aggregate retentions, if they are set as a multiple of the expected primary losses or to produce a multiple of the guaranteed-cost premium.

### **9. Capital and Profit Provisions**

With the exception of dividend plans, the risk transferred from the insured to the insurer under a loss-sensitive plan is lower than the risk transferred under a guaranteed-cost plan. This is

---

<sup>12</sup> Under both NCCI’s and ISO’s retrospective rating plans, the provision for IBNR is accomplished through factors that get applied to standard premium and then get multiplied by the loss conversion factor and the tax multiplier, for the first three adjustments (NCCI) or the first four adjustments (ISO). See their retrospective rating plan manuals for details.

<sup>13</sup> Holdbacks are not part of the NCCI’s or ISO’s filed retrospective rating plan manuals. They require the use of LRARO where those filed plans apply.

because the insured is retaining the risk for their own primary losses, up to an aggregate limit. Therefore, the capital required to support these plans is lower than the capital required to support a guaranteed-cost plan. Note, though, that the capital is not reduced in proportion to the loss sharing. As mentioned above, the customer is sharing in their less risky primary losses, and their risk is often capped. The insurer takes on the riskier per-occurrence and aggregate excess losses. Therefore the capital reduction is significantly less than the reduction in the expected loss dollars transferred to the insured. As a result, the profit provision (in dollars) is reduced, but is increased as a percentage of insured loss.

### **10. The Dissolution of Loss-Sensitive Rating Plans for Long-Tailed Lines**

Retrospective rating adjustments and large deductible reimbursements typically continue until both parties agree to close the plan. (Sometimes there is a predetermined limit on the number of annual premium adjustments for an incurred retrospective rating plan.) An insured might want to close the plan in order to free up their balance sheet from the liabilities under the plan. This is often a desire if the insured is putting itself up for sale. Or they may want to eliminate the need to post collateral, thereby freeing up credit lines and/or saving costs associated with posting the collateral. An insurer might want to close the plan in order to eliminate the administrative costs associated with billing additional premium or loss reimbursement amounts. Or, if the insured is going through a bankruptcy or reorganization, it may be in the interests of both parties to close the plan. However, unless the insured and insurer are at least somewhat in agreement about the amount of future development on the losses under the plan, or unless the terms of closing the plan are predetermined at the time of sale, it is unlikely that an agreement on the cost of closing the plan will be reached.

Retrospective rating plans are generally closed through what is called a retrospective rating plan **closeout**. This closeout is generally achieved by applying final loss development factors to the losses in order to determine the final premium amount. As mentioned above, sometimes the terms of a future closeout are predetermined when the plan is initially written.

Large deductible plans may be closed through either a large deductible **buyout** or a **loss portfolio transfer**. A buyout is an agreement between the insurer and insured where, for a fee, the insurer assumes the liabilities related to the deductible layer of loss. These liabilities may include loss-based assessments associated with those losses. A loss portfolio transfer is a separate policy under which the insured's remaining loss obligations are ceded to an insurer or reinsurer.

Self-insured retentions are closed through loss portfolio transfers.

### Questions

1. Why is there no credit risk related to self-insured retentions?
2. Given a tax rate of 5%, calculate the tax multiplier.
3. Given a tax multiplier of 1.05, calculate the tax rate.
4. Why is the tax multiplier minus 1 higher than the tax rate?
5. Given the following, calculate the amount of expenses (as a percentage of guaranteed-cost premium) that will be collected through the basic premium, as a percentage of the guaranteed-cost premium:
  - The loss conversion factor is 1.10.
  - The expected loss ratio is 0.70.
  - The expense ratio (excluding premium-based taxes and assessments) is 0.20.
6. Given the following, calculate the loss conversion factor:
  - The expense ratio (excluding premium-based taxes and assessments) is 0.25.
  - The expected loss ratio is 0.65.
  - The amount of expenses to be collected through the basic premium, as a percentage of the guaranteed-cost premium, is 0.15.
7. Given the following, calculate the retrospectively rated premium amount:
  1. The basic premium amount is \$150,000.
  2. The loss conversion factor is 1.10.
  3. The tax multiplier is 1.031.
  4. The per-occurrence loss limit is \$100,000.
  5. The maximum ratable loss amount is \$500,000.
  6. There are 15 claims on the policy. Ten of those claims are under \$10,000 and total \$25,000. The other 5 claims have values of:
    - \$15,000
    - \$25,000
    - \$50,000
    - \$100,000
    - \$1,000,000
8. How does the basic premium as a percentage of guaranteed-cost premium change as:
  - The loss conversion factor increases?
  - The loss limit increases?
  - The maximum premium or maximum ratable loss increases?
  - The minimum premium or minimum ratable loss increases?
  - The account size increases?

9. Given the following cost components, calculate the premium for a large deductible plan.
- Fixed expenses are \$35,000. This includes a flat dollar commission for the broker.
  - The underwriting profit provision is \$5,000.
  - Loss-based expenses are 10% of losses.
  - The premium tax rate is 3%.
  - Expected losses are \$300,000.
  - Expected losses limited to \$250,000 per-occurrence are \$270,000.
  - Expected losses limited to \$250,000 per-occurrence and to \$500,000 in aggregate are \$260,000.
10. In what way is a loss-sensitive dividend plan unbalanced?
11. Under what conditions is the risk transfer the same for a retrospective rating plan and a large deductible plan?

### **Acknowledgments**

I would like to thank the following people for their review and suggestions for improvement: Ginda Fisher, Howard Mahler, Kalev Maricq, Lawrence McTaggart, Fran Sarrel, Phillip Schiavone, Josh Taub, Matt Veibell, Amy Waldhauer, and Wade Warriner.

I would also like to thank the following people for answering questions related to content: Matt Hayden, Sandra Kipust, Diana O'Brien, Nancy Treitel-Moore, Jean Ruggieri, Diana Trent, Shane Vadbunker, and Chris Wallace.

## Appendix: Examples of Expected Cash Flow

Examples ignore processing lags and assume no aggregate excess loss exposure.

| Pricing Assumptions |                                           |           |                                                      |
|---------------------|-------------------------------------------|-----------|------------------------------------------------------|
| 1                   | Initial Premium                           | 1,100,000 |                                                      |
| 2                   | Expected Primary Loss & ALAE              | 600,000   |                                                      |
| 3                   | Expected Excess Loss & ALAE               | 300,000   |                                                      |
| 4                   | Commission                                | 55,000    |                                                      |
| 5                   | General Expense                           | 15,000    |                                                      |
| 6                   | Underwriting Profit Provision             | 5,000     |                                                      |
| 7                   | ULAE                                      | 10.0%     |                                                      |
| 8                   | Tax Rate                                  | 3.0%      |                                                      |
|                     |                                           |           |                                                      |
|                     | <b>Incurred Retrospective Rating Plan</b> |           |                                                      |
| 9                   | Basic Premium                             | 405,000   | = (3) x (10) + (4) + (5) + (6)                       |
| 10                  | Loss Conversion Factor                    | 1.100     | = 1 + (7)                                            |
| 11                  | Tax Multiplier                            | 1.031     | = 1.0 / (1.0 - (8))                                  |
|                     |                                           |           |                                                      |
|                     | <b>Large Deductible Plan</b>              |           |                                                      |
| 12                  | Premium                                   | 479,381   | = {(3) + (4) + (5) + (6) + (7) * [(2) + (3)]} x (11) |

| Payment Patterns |                 |                              |                          |                         |                        |            |                 |       |
|------------------|-----------------|------------------------------|--------------------------|-------------------------|------------------------|------------|-----------------|-------|
| Time             | Initial Premium | Primary Incurred Loss & ALAE | Primary Paid Loss & ALAE | Excess Paid Loss & ALAE | Total Paid Loss & ALAE | Commission | General Expense | ULAE  |
| 0.00             | 1.000           |                              |                          |                         |                        | 1.000      | 0.250           |       |
| 0.25             |                 | 0.107                        | 0.021                    | 0.001                   | 0.014                  |            | 0.438           | 0.073 |
| 0.50             |                 | 0.263                        | 0.072                    | 0.005                   | 0.050                  |            | 0.625           | 0.162 |
| 0.75             |                 | 0.454                        | 0.145                    | 0.020                   | 0.103                  |            | 0.813           | 0.265 |
| 1.00             |                 | 0.655                        | 0.234                    | 0.050                   | 0.173                  |            | 1.000           | 0.380 |
| 1.50             |                 | 0.773                        | 0.409                    | 0.150                   | 0.323                  |            |                 | 0.492 |
| 2.50             |                 | 0.879                        | 0.635                    | 0.350                   | 0.540                  |            |                 | 0.655 |
| 3.50             |                 | 0.939                        | 0.798                    | 0.600                   | 0.732                  |            |                 | 0.799 |
| 4.50             |                 | 0.974                        | 0.904                    | 0.800                   | 0.869                  |            |                 | 0.902 |
| 5.50             |                 | 0.989                        | 0.956                    | 0.900                   | 0.937                  |            |                 | 0.953 |
| 6.50             |                 | 0.997                        | 0.977                    | 0.950                   | 0.968                  |            |                 | 0.976 |
| 7.50             |                 | 1.000                        | 1.000                    | 1.000                   | 1.000                  |            |                 | 1.000 |

| Policyholder Cash Flows            |                              |                                |                                   |                       |
|------------------------------------|------------------------------|--------------------------------|-----------------------------------|-----------------------|
|                                    |                              |                                |                                   |                       |
| Incurred Retrospective Rating Plan |                              |                                |                                   |                       |
| Time                               | Primary Incurred Loss & ALAE | Premium <sup>1</sup>           | Cumulative Cash Flow              | Incremental Cash Flow |
|                                    |                              |                                |                                   |                       |
| 0.00                               | -                            | 1,100,000                      | (1,100,000)                       | (1,100,000)           |
| 0.25                               | 64,200                       | 1,100,000                      | (1,100,000)                       | -                     |
| 0.50                               | 157,800                      | 1,100,000                      | (1,100,000)                       | -                     |
| 0.75                               | 272,400                      | 1,100,000                      | (1,100,000)                       | -                     |
| 1.00                               | 393,000                      | 1,100,000                      | (1,100,000)                       | -                     |
| 1.50                               | 463,800                      | 943,485                        | (943,485)                         | 156,515               |
| 2.50                               | 527,400                      | 1,015,608                      | (1,015,608)                       | (72,124)              |
| 3.50                               | 563,400                      | 1,056,433                      | (1,056,433)                       | (40,825)              |
| 4.50                               | 584,400                      | 1,080,247                      | (1,080,247)                       | (23,814)              |
| 5.50                               | 593,400                      | 1,090,454                      | (1,090,454)                       | (10,206)              |
| 6.50                               | 598,200                      | 1,095,897                      | (1,095,897)                       | (5,443)               |
| 7.50                               | 600,000                      | 1,097,938                      | (1,097,938)                       | (2,041)               |
|                                    |                              |                                |                                   |                       |
|                                    |                              |                                |                                   |                       |
| Large Deductible Plan              |                              |                                |                                   |                       |
| Time                               | Premium                      | Deductible Loss Reimbursements | Cumulative Cash Flow <sup>2</sup> | Incremental Cash Flow |
|                                    |                              |                                |                                   |                       |
| 0.00                               | 479,381                      | -                              | (479,381)                         | (479,381)             |
| 0.25                               | 479,381                      | 12,600                         | (491,981)                         | (12,600)              |
| 0.50                               | 479,381                      | 43,200                         | (522,581)                         | (30,600)              |
| 0.75                               | 479,381                      | 87,000                         | (566,381)                         | (43,800)              |
| 1.00                               | 479,381                      | 140,400                        | (619,781)                         | (53,400)              |
| 1.50                               | 479,381                      | 245,400                        | (724,781)                         | (105,000)             |
| 2.50                               | 479,381                      | 381,000                        | (860,381)                         | (135,600)             |
| 3.50                               | 479,381                      | 478,800                        | (958,181)                         | (97,800)              |
| 4.50                               | 479,381                      | 542,400                        | (1,021,781)                       | (63,600)              |
| 5.50                               | 479,381                      | 573,600                        | (1,052,981)                       | (31,200)              |
| 6.50                               | 479,381                      | 586,200                        | (1,065,581)                       | (12,600)              |
| 7.50                               | 479,381                      | 600,000                        | (1,079,381)                       | (13,800)              |

<sup>1</sup> Premium under the Incurred Retrospective Rating Plan begins as the Initial premium of \$1,100,000. Starting at 18 months (time 1.5), the retrospective rating formula applies. Here, the policyholder gets a partial return of premium at 18 months, but then pays additional premium amounts at 30, 42, 54, 66, 78, and 90 months. These additional premium amounts create credit risk for the insurer.

<sup>2</sup> Cash flow for the policyholder includes both premium payments and deductible loss reimbursements.

| Insurer Cash flows                 |           |                                           |                           |            |             |                    |        |                                      |                          |
|------------------------------------|-----------|-------------------------------------------|---------------------------|------------|-------------|--------------------|--------|--------------------------------------|--------------------------|
|                                    |           |                                           |                           |            |             |                    |        |                                      |                          |
| Incurred Retrospective Rating Plan |           |                                           |                           |            |             |                    |        |                                      |                          |
| Time                               | Premium   |                                           | Total Paid<br>Loss & ALAE | Commission | Premium Tax | General<br>Expense | ULAE   | Cumulative<br>Cash Flow <sup>3</sup> | Incremental<br>Cash Flow |
| 0.00                               | 1,100,000 |                                           | -                         | 55,000     | 33,000      | 3,750              | -      | 1,008,250                            | 1,008,250                |
| 0.25                               | 1,100,000 |                                           | 12,900                    | 55,000     | 33,000      | 6,570              | 6,570  | 985,960                              | (22,290)                 |
| 0.50                               | 1,100,000 |                                           | 44,700                    | 55,000     | 33,000      | 9,375              | 14,580 | 943,345                              | (42,615)                 |
| 0.75                               | 1,100,000 |                                           | 93,000                    | 55,000     | 33,000      | 12,195             | 23,850 | 882,955                              | (60,390)                 |
| 1.00                               | 1,100,000 |                                           | 155,400                   | 55,000     | 33,000      | 15,000             | 34,200 | 807,400                              | (75,555)                 |
| 1.50                               | 943,485   |                                           | 290,400                   | 55,000     | 28,305      | 15,000             | 44,280 | 510,500                              | (296,900)                |
| 2.50                               | 1,015,608 |                                           | 486,000                   | 55,000     | 30,468      | 15,000             | 58,950 | 370,190                              | (140,310)                |
| 3.50                               | 1,056,433 |                                           | 658,800                   | 55,000     | 31,693      | 15,000             | 71,910 | 224,030                              | (146,160)                |
| 4.50                               | 1,080,247 |                                           | 782,400                   | 55,000     | 32,407      | 15,000             | 81,180 | 114,260                              | (109,770)                |
| 5.50                               | 1,090,454 |                                           | 843,600                   | 55,000     | 32,714      | 15,000             | 85,770 | 58,370                               | (55,890)                 |
| 6.50                               | 1,095,897 |                                           | 871,200                   | 55,000     | 32,877      | 15,000             | 87,840 | 33,980                               | (24,390)                 |
| 7.50                               | 1,097,938 |                                           | 900,000                   | 55,000     | 32,938      | 15,000             | 90,000 | 5,000                                | (28,980)                 |
|                                    |           |                                           |                           |            |             |                    |        |                                      |                          |
|                                    |           |                                           |                           |            |             |                    |        |                                      |                          |
| Large Deductible Plan              |           |                                           |                           |            |             |                    |        |                                      |                          |
| Time                               | Premium   | Deductible<br>Loss<br>Reimburse-<br>ments | Total Paid<br>Loss & ALAE | Commission | Premium Tax | General<br>Expense | ULAE   | Cumulative<br>Cash Flow <sup>4</sup> | Incremental<br>Cash Flow |
| 0.00                               | 479,381   | -                                         | -                         | 55,000     | 14,381      | 3,750              | -      | 406,250                              | 406,250                  |
| 0.25                               | 479,381   | 12,600                                    | 12,900                    | 55,000     | 14,381      | 6,570              | 6,570  | 396,560                              | (9,690)                  |
| 0.50                               | 479,381   | 43,200                                    | 44,700                    | 55,000     | 14,381      | 9,375              | 14,580 | 384,545                              | (12,015)                 |
| 0.75                               | 479,381   | 87,000                                    | 93,000                    | 55,000     | 14,381      | 12,195             | 23,850 | 367,955                              | (16,590)                 |
| 1.00                               | 479,381   | 140,400                                   | 155,400                   | 55,000     | 14,381      | 15,000             | 34,200 | 345,800                              | (22,155)                 |
| 1.50                               | 479,381   | 245,400                                   | 290,400                   | 55,000     | 14,381      | 15,000             | 44,280 | 305,720                              | (40,080)                 |
| 2.50                               | 479,381   | 381,000                                   | 486,000                   | 55,000     | 14,381      | 15,000             | 58,950 | 231,050                              | (74,670)                 |
| 3.50                               | 479,381   | 478,800                                   | 658,800                   | 55,000     | 14,381      | 15,000             | 71,910 | 143,090                              | (87,960)                 |
| 4.50                               | 479,381   | 542,400                                   | 782,400                   | 55,000     | 14,381      | 15,000             | 81,180 | 73,820                               | (69,270)                 |
| 5.50                               | 479,381   | 573,600                                   | 843,600                   | 55,000     | 14,381      | 15,000             | 85,770 | 39,230                               | (34,590)                 |
| 6.50                               | 479,381   | 586,200                                   | 871,200                   | 55,000     | 14,381      | 15,000             | 87,840 | 22,160                               | (17,070)                 |
| 7.50                               | 479,381   | 600,000                                   | 900,000                   | 55,000     | 14,381      | 15,000             | 90,000 | 5,000                                | (17,160)                 |

<sup>3</sup> Insurer cash flows under the Incurred Retrospective Rating Plan equals the premium collected less losses and expenses paid.

<sup>4</sup> Insurer cash flows under the Large Deductible Plan equals the premium and deductible loss reimbursements collected less losses and expenses paid.



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

## Chapter 4: Concluding Remarks

By Ginda Kaplan Fisher

### 1. General Observations

In general, the premium for an insurance policy should pay for the expected costs, including the cost of capital supporting the policy. When retrospectively rated policies were developed, it was considered desirable that the expected premium to be paid by the insured would be the same, regardless of the retrospective policy provisions. (Obviously, the *actual* premium could vary, if actual losses were more or less than expected.) This was called a Balanced Plan.

Since then, large deductible policies and other policies that remove a significant fraction of the costs from “premium” have been developed. Also, as discussed in Chapter 2, the risk load and expected expenses to be paid may be significantly different with different policy provisions. There are still some highly regulated types of insurance where the expected premium must remain the same, but for most policy types, it is not necessary or desirable to balance the premium. It is still important that the pure premium or expected losses be balanced, however. It is worth noting that there can be a great deal of uncertainty or risk in both the aggregate and per-occurrence excess loss. Especially when very high layers are insured, it is common for the risk charge to be greater than the loss cost for some portions of the coverage. Sometimes, the actual expected loss is so much less than the value of the risk that neither party cares much about the actual loss cost.

This study note focuses on loss cost, so it deals with those cases where the loss cost is significant *enough* to be worth estimating, and Chapter 3 provides tools for the actuary to estimate the cost of the aggregate excess loss. However, if the actuary uses these methods and comes up with some insignificant loss charge, it is usually appropriate to charge something for the coverage. The same is true for high layers of per-occurrence loss. Remember that if the customer wants to buy protection for some layer of risk, it is worth something to the insured. Maybe the insured knows something they aren’t sharing. Even if the actuary is very comfortable with the total or primary loss pick,<sup>53</sup> the risk load and the expected expense of maintaining a loss-sensitive provision should be carefully evaluated.

Questions:

1. Would you expect a fair premium for a retrospective plan with a high aggregate loss limit to be more or less than the fair premium for a guaranteed cost plan covering the same risk?
2. Why should you generally recommend charging a non-negligible premium for high layers of aggregate or per-occurrence loss even though you estimated the loss cost for those layers to be negligible?

---

<sup>53</sup> A common name for the actuary’s best estimate of  $E$  or  $E(A_D)$ . In some cases, rather than estimate the total expected loss, the actuary will use the more stable limited loss data to select a limited expected loss, the “primary loss pick” and estimate the other loss components from that.

### 2. Sensitivity of Table M charges to the Accuracy of the Loss Pick or Rate Adequacy

Also, whenever an actuary is pricing a loss sensitive plan (e.g., a deductible or retrospective policy) with an aggregate limit/maximum, the actuary should be aware of the leverage that the primary loss pick has on the insurance charge. This section has been adapted from a prior CAS study note<sup>54</sup>

It is tempting to think that this loss pick isn't very important, because the insured is responsible for those losses. This may be true if the entry ratio is very high and the deductible relatively low, as most of the insured losses will be in the per-occurrence excess portion, not the aggregate excess portion.<sup>55</sup> However, if the primary entry ratio is relatively low, or the deductible is very high, a significant portion of the expected insured losses will come from the aggregate. The loss pick might be inadequate on a large account because the underwriter has been optimistic, or on a small account because the state has demanded inadequate filed rates. In any case, as every actuary knows, it is hard to predict the level of future expected losses. An excessive loss pick will also lead to an inappropriate insurance charge.

The following example was priced using the Countrywide Table of Aggregate Loss Factors found in NCCI's Circular CIF-2017-32 "Countrywide—Announcement of Item R-1414—Revisions to Retrospective Rating Plan Manual Appendix B and All Related Rules and Endorsements"

Assume the actuary and underwriter expected there to be \$500K total loss on a policy, and priced the policy accordingly. The underwriter sold an aggregate loss limit with an intended entry ratio of 2, or \$1M. But in fact, the true expected loss is \$550,000. Assume the error in estimation is due to frequency. What happens to the Table M charge?

The actuary determined this account would have about 42 claims, and so fit Expected Claim Group 41. The aggregate excess loss factor for an unlimited loss ( $k=0$ ) in Expected Claim Group 41, at an entry ratio of 2 is 0.2108. So the Table M charge the actuary calculates is  $\$500,000 \times 0.2108 = \$105,400$ .

But the true expected loss is \$550,000. So the actual entry ratio at which aggregate losses will be capped is  $\$1M/\$550K = 1.82$

The true expected number of claims is closer to 46, pushing the account into the slightly cheaper expected claim group 40. Even so, the aggregate excess loss factor in Expected Claim Group 40, at an entry ratio of 1.82 is 0.2228. And the true expected Table M charge is  $\$550,000 \times 0.2228 = \$122,540$ . The aggregate limit has been underpriced by more than 16%.

---

<sup>54</sup> Ginda Kaplan Fisher, "Pricing Aggregates on Deductible Policies," 2002, published by the Casualty Actuarial Society as part of the Syllabus of Exams.

<sup>55</sup> Of course, if the excess portion is priced as a fraction of the primary loss pick, then the primary loss pick is important in pricing this component, too.

Exhibits 4.1 through 4.5 show an example of the impact on the insurance charge of an inadequate or excessive loss.<sup>56</sup>

In this example, the NCCI countrywide subtable 6 Table M charges were used, that is, this example represents a retrospective policy with a loss limitation of about 12%. However, the same effect would occur on any other insurance charge priced in a similar way (using Table MD, ICRL, etc.) Notice that the dollar error in insurance charges is greatest for large policies at low entry ratios, but the largest (absolute value) observed percent error in insurance charge is for a large policy at entry ratio 2. The percent error in the total expected losses for a deductible policy would also depend on the expected deductible losses. In any case, it is easy to see that adequate (primary) loss estimates are important to the profitability of a book of loss-sensitive policies.

Exhibit 4.1. If rates/loss picks are correct; Tables of % and \$ Charge<sup>57</sup>

|                          |           |                      |                                         |                                     | At Entry Ratio |      |      |      |      |
|--------------------------|-----------|----------------------|-----------------------------------------|-------------------------------------|----------------|------|------|------|------|
| true<br>expected<br>loss | Loss Pick | expected<br>severity | true<br>expected<br>number of<br>claims | Expected<br>Claim<br>Count<br>group | 1              | 1.2  | 1.7  | 2    | 3    |
| 3,000,000                | 3,000,000 | 12,000               | 250.0                                   | 29                                  | 0.25           | 0.18 | 0.07 | 0.04 | 0.01 |
| 1,000,000                | 1,000,000 | 12,000               | 83.3                                    | 36                                  | 0.32           | 0.25 | 0.13 | 0.09 | 0.02 |
| 500,000                  | 500,000   | 12,000               | 41.7                                    | 41                                  | 0.37           | 0.31 | 0.18 | 0.13 | 0.04 |
| 100,000                  | 100,000   | 12,000               | 8.3                                     | 57                                  | 0.54           | 0.49 | 0.39 | 0.34 | 0.23 |

| true<br>expected<br>loss | Loss Pick | expected<br>severity | true expected<br>number of<br>claims | Expected<br>Claim Count<br>group | 1       | 1.2     | 1.7     | 2       | 3      |
|--------------------------|-----------|----------------------|--------------------------------------|----------------------------------|---------|---------|---------|---------|--------|
| 3,000,000                | 3,000,000 | 12,000               | 250.0                                | 29                               | 762,600 | 543,900 | 220,500 | 124,500 | 16,500 |
| 1,000,000                | 1,000,000 | 12,000               | 83.3                                 | 36                               | 319,400 | 247,900 | 128,400 | 85,300  | 20,700 |
| 500,000                  | 500,000   | 12,000               | 41.7                                 | 41                               | 186,300 | 152,750 | 91,600  | 66,550  | 22,400 |
| 100,000                  | 100,000   | 12,000               | 8.3                                  | 57                               | 54,440  | 49,310  | 39,170  | 34,440  | 23,240 |

<sup>56</sup> Using an inappropriate aggregate loss distribution can also produce significant pricing problems.

<sup>57</sup> \$Charge based on true “expected loss.”

If rates or loss picks are 10% inadequate, charges may be more than **20% inadequate**:

Exhibit 4.2. If rates are 10% inadequate; Table of % and \$Charge<sup>58</sup>

|                          |              |                      |                                         |                                     | Entry Ratio |      |      |      |      |
|--------------------------|--------------|----------------------|-----------------------------------------|-------------------------------------|-------------|------|------|------|------|
| true<br>expected<br>loss | Loss<br>Pick | expected<br>severity | True<br>expected<br>number<br>of claims | Expected<br>Claim<br>Count<br>group | 1           | 1.2  | 1.7  | 2    | 3    |
| 3,300,000                | 3,000,000    | 12,000               | 275.0                                   | 28                                  | 0.29        | 0.21 | 0.09 | 0.05 | 0.01 |
| 1,100,000                | 1,000,000    | 12,000               | 91.7                                    | 35                                  | 0.35        | 0.27 | 0.15 | 0.10 | 0.03 |
| 550,000                  | 500,000      | 12,000               | 45.8                                    | 40                                  | 0.40        | 0.33 | 0.20 | 0.15 | 0.05 |
| 110,000                  | 100,000      | 12,000               | 9.2                                     | 56                                  | 0.56        | 0.51 | 0.41 | 0.36 | 0.24 |

| true<br>expected<br>loss | Loss Pick | expected<br>severity | true<br>expected<br>number<br>of claims | Expected<br>Claim<br>Count<br>group | 1       | 1.2     | 1.7     | 2       | 3      |
|--------------------------|-----------|----------------------|-----------------------------------------|-------------------------------------|---------|---------|---------|---------|--------|
| 3,300,000                | 3,000,000 | 12,000               | 275.0                                   | 28                                  | 945,120 | 694,320 | 297,330 | 175,230 | 26,070 |
| 1,100,000                | 1,000,000 | 12,000               | 91.7                                    | 35                                  | 382,030 | 302,170 | 161,810 | 110,550 | 28,930 |
| 550,000                  | 500,000   | 12,000               | 45.8                                    | 40                                  | 218,460 | 181,280 | 110,935 | 82,225  | 29,150 |
| 110,000                  | 100,000   | 12,000               | 9.2                                     | 56                                  | 61,589  | 56,012  | 44,649  | 39,413  | 26,774 |

%error with 10% inadequate loss pick

| % Error at Sold or intended Entry Ratio |     |     |     |     |
|-----------------------------------------|-----|-----|-----|-----|
| 1                                       | 1.2 | 1.7 | 2   | 3   |
| 24%                                     | 28% | 35% | 41% | 58% |
| 20%                                     | 22% | 26% | 30% | 40% |
| 17%                                     | 19% | 21% | 24% | 30% |
| 13%                                     | 14% | 14% | 14% | 15% |

<sup>58</sup> \$Charge based on true “expected loss.”

If rates or loss picks are 10% excessive, charges may be more than **25% excessive**:

Exhibit 4.3. If rates are 10% Excessive; Table of % and \$Charge<sup>59</sup>

|                          |           |                              |                                         |                                     | Entry Ratio |      |      |      |      |
|--------------------------|-----------|------------------------------|-----------------------------------------|-------------------------------------|-------------|------|------|------|------|
| true<br>expected<br>loss | Loss Pick | expect<br>ed<br>severit<br>y | True<br>expected<br>number<br>of claims | Expected<br>Claim<br>Count<br>group | 1           | 1.2  | 1.7  | 2    | 3    |
| 2,727,273                | 3,000,000 | 12,000                       | 227.3                                   | 29                                  | 0.22        | 0.15 | 0.05 | 0.03 | 0.00 |
| 909,091                  | 1,000,000 | 12,000                       | 75.8                                    | 36                                  | 0.28        | 0.21 | 0.10 | 0.06 | 0.01 |
| 454,545                  | 500,000   | 12,000                       | 37.9                                    | 42                                  | 0.35        | 0.28 | 0.17 | 0.12 | 0.04 |
| 90,909                   | 100,000   | 12,000                       | 7.6                                     | 58                                  | 0.53        | 0.48 | 0.38 | 0.33 | 0.22 |

| true<br>expected<br>loss | Loss Pick | expecte<br>d<br>severity | true<br>expected<br>number<br>of claims | Expected<br>Claim<br>Count<br>group | 1       | 1.2     | 1.7     | 2      | 3      |
|--------------------------|-----------|--------------------------|-----------------------------------------|-------------------------------------|---------|---------|---------|--------|--------|
| 2,727,273                | 3,000,000 | 12,000                   | 227.3                                   | 29                                  | 586,636 | 400,909 | 145,364 | 76,364 | 7,909  |
| 909,091                  | 1,000,000 | 12,000                   | 75.8                                    | 36                                  | 256,000 | 193,000 | 2,727   | 58,818 | 12,182 |
| 454,545                  | 500,000   | 12,000                   | 37.9                                    | 42                                  | 158,500 | 128,682 | 75,227  | 53,682 | 17,091 |
| 90,909                   | 100,000   | 12,000                   | 7.6                                     | 58                                  | 48,100  | 43,436  | 34,309  | 30,082 | 20,173 |

%error with 10% excessive loss pick

| % Error at Sold or intended Entry Ratio |      |      |      |      |
|-----------------------------------------|------|------|------|------|
| 1                                       | 1.2  | 1.7  | 2    | 3    |
| -23%                                    | -26% | -34% | -39% | -52% |
| -20%                                    | -22% | -28% | -31% | -41% |
| -15%                                    | -16% | -18% | -19% | -24% |
| -12%                                    | -12% | -12% | -13% | -13% |

<sup>59</sup> \$Charge based on true “expected loss.”

Questions:

3. Given a large deductible WC policy with the following features:

- \$2M expected total loss
- Expected average severity of \$10,000 per claim
- The insured retains 86% of expected loss under the per-occurrence deductible (14% is expected to be excess of the deductible)
- There is a limit on the aggregate deductible retained by the insured of \$3M

a.) What is the insurance charge for the aggregate limit?

If the account is larger than the pricing actuary realized, and the expected total losses should have been \$2.5M, what should the insurance charge have been?

### 3. Consistency of Assumptions

The actuary should also be cautious of mismatched assumptions. Using different methods to calculate the per-occurrence excess charges and aggregate excess charges can sometimes lead to disjointed results. For instance, a company might have developed estimates of per-occurrence excess losses independently of the method used to develop its estimate of aggregate excess losses. Perhaps the company has estimated its own per-occurrence excess loss factors, but is relying on a rating bureau for aggregate excess loss factors. When this happens, a plan might come up with different pricing depending on how it is described. For instance, if the per-occurrence limit on a retrospectively rated plan is greater than or equal to the aggregate limit, the actuary's pricing model ought to recommend the same loss cost whether or not the per-occurrence limit is mentioned. But if the estimated charges were developed independently, that might not happen.

Mismatches in assumptions can creep into calculations in all sorts of places, including systematic errors. For instance, an actuary might look at a rating bureau's "pure premium" for a slice of the risk. But sometimes rating bureau pure-premium is "loaded" with various non-loss items, such as provisions for loss based assessments and LAE. If unadjusted rating bureau excess factors are multiplied by a loss estimate that doesn't include those components (and thus is smaller), excess losses can be underestimated, sometimes substantially so<sup>60</sup>.

The actuary should be careful to monitor pricing assumptions for consistency and reasonability. When designing a pricing model, the actuary should compare the sum of the predicted primary, per-occurrence excess, and aggregate excess losses for various types of policies that might be written on various types of accounts, and ensure that the sums of the parts compare reasonably with the predicted total losses for those accounts. If not, an investigation of the assumptions used in estimating the per-occurrence excess and aggregate excess losses is in order.

---

<sup>60</sup> Whenever using factors from somewhere else, an actuary should ideally be familiar with the assumptions behind the calculation of those factors.

## **Acknowledgments**

I would like to thank Jill Petker and Paul Ivanovskis for bringing many of these issues to my attention, and encouraging me to include them in the scope of a study note.

## Solutions to Chapter Questions

## Chapter 1 Answers

1. The objectives of experience rating are to:
  - a. Increase equity
  - b. Incentive for safety
  - c. Enhance market competition
2. Experience rating adjusts a risk's rate to be more in line with that risk's expected loss experience. Risks whose expected loss experience is lower than average will pay less premium, and risks whose expected loss experience is higher will pay more premium.
3. Company B—since Company B has fewer rating classes, there will probably be more variation in risks within each rating class. The use of experience rating will allow the company to further tailor each risk's premium with its loss potential.
4. Without experience rating, a company would charge better than average and worse than average risks the same rate. Better than average risks might be able to find a lower rate with another company that recognizes the risk's lower loss potential. If enough of the better than average risks do this, the company will be left with only the worse than average risks.
5. In a group of risks, some of the difference in experience is due to underlying differences in the loss potential of the different risks. This is the variance of the hypothetical means. Some of the difference in experience among the risks is purely random, i.e., the process variance. Experience rating attempts to identify and adjust for the VHM, while at the same time not penalizing risks for differences in experience that are purely random.
6. Probably not. If the safety program in question does in fact reduce this risk's loss potential, this will be reflected in the risk's past experience and will be picked up by the experience rating. Using a schedule credit would double-count the expected benefit of the safety program. However, if the safety program is new (i.e., it was implemented during or after the experience period used by the experience rating program) then there is some expected benefit that would not be reflected in the past experience.

### Chapter 2 Answers

1. There is no credit risk related to self-insured retentions because the insurer does not pay the retained losses up front, and therefore does not need to seek reimbursement from the self-insured.
2.  $1.053 = 1 / (1 - 0.05)$
3.  $0.048 = 1 - 1/1.05$
4. The tax multiplier needs to account for the fact that premium tax is part of premium and therefore is itself taxed.
5.  $13\% = 0.20 - (1.10 - 1) \times 0.70$ . That is, 13% of the guaranteed-cost premium will be collected as a fixed expense through the basic premium amount.
6.  $1.15 = 1 + (0.25 - 0.15) / 0.65$
7. Total losses, limited to the per-occurrence loss limit, are  $315,000 = 25,000 + 15,000 + 25,000 + 50,000 + 2 \times 100,000$ . This is below the maximum ratable loss amount.  
The retrospective premium is  $\$511,892 = (150,000 + 1.1 \times 315,000) \times 1.031$
8. As the loss conversion factor increases, expenses are shifted out of the basic premium, and the basic premium decreases.

As the loss limit increases, the charge for per-occurrence excess exposure decreases, and the basic premium decreases.

As the maximum premium or maximum ratable loss amount increases, the charge for aggregate excess exposure decreases, and the basic premium decreases.

As the minimum premium or minimum ratable loss amount increases, the net charge for aggregate excess exposure (i.e., the net insurance charge) decreases, and the basic premium decreases.

As the account size increases, there are two effects. The amount of premium discount increases, reducing the percentage expense provision in the basic premium. In addition, larger accounts have more stable loss experience, so the charge for aggregate excess exposure decreases. (The latter impact may become clearer after reading chapter 3.) For both of these reasons, the basic premium decreases.

9. The premium is calculated as:

|               |                                                  |
|---------------|--------------------------------------------------|
| 35,000        | fixed expense                                    |
| 30,000        | loss-based expense = $300,000 \times 10\%$       |
| 5,000         | underwriting profit                              |
| 30,000        | per-occurrence excess = $300,000 - 270,000$      |
| <u>10,000</u> | aggregate excess = $270,000 - 260,000$           |
| 110,000       | subtotal                                         |
| 113,402       | including premium tax = $110,000 \times (1/.97)$ |

10. A loss-sensitive dividend plan is unbalanced because if loss experience is better than expected, the insured receives a dividend, but if loss experience is worse than expected, the insured does not incur any additional costs.

11. The risk transfer is the same for a retrospective rating plan and a large deductible plan when:
  - a. The loss limit for the retrospective rating plan equals the per-occurrence deductible.
  - b. The maximum ratable loss amount for the retrospective rating plan equals the aggregate deductible limit.
  - c. There is no minimum ratable loss amount for the retrospective rating plan.

### Chapter 3 Answers

1.

| Problem | Claim # | Claim \$000 | Occ.-Ltd. Agg. Sum | Occ. Excess | Agg. Excess | Total Insurance | Insured Payment |
|---------|---------|-------------|--------------------|-------------|-------------|-----------------|-----------------|
| (a)     | 1       | 3           | 3                  | 0           | 0           | 0               | 3               |
|         | 2       | 8           | 11                 | 0           | 0           | 0               | 8               |
|         | 3       | 14          | 21                 | 4           | 0           | 4               | 10              |
| (b)     | 4       | 12          | 31                 | 2           | 6           | 8               | 4               |
| (c)     | 5       | 18          | 41                 | 8           | 10          | 18              | 0               |

(a) Insurer =  $0+0+4 = 4$ ; Insured =  $3+8+10 = 21$

(b) Insurer =  $4+8 = 12$ ; Insured =  $21+4 = 25$

(c) Insurer =  $12+18 = 30$ ; Insured =  $25+0 = 25$

2.

(a)  $\$500K + \$100K + \$300K + \$2,000K = \$2,900K$

(b)  $\$500K + \$100K + \$250K + \$250K = \$1.1M$

(c)  $\$1.1M - \$1.0M = \$100K$

(d) Only the \$2M claim breaches the per-claim policy limit, so **\$1M**

(e) Prior to application of the policy's aggregate limit, the policy would cover

- \$0 on the small claims
- \$0 on the \$100K claim
- \$50K on the \$300K claim
- \$750K on the \$2M claim
- \$100K for the aggregate on the deductible

For a total of **\$900K**.

(f) **Zero** ( $900K < 5M$ )

(g) **\$900K**

3.

The Table M insurance charge associated with a given outcome is the ratio of the area bounded by  $F(A)$  and that outcome to the total area under  $F(A)$ . The total area under the curve  $F(A) = 100 * 1/2 = 50$ .

![A graph of a linear function F(A) on a coordinate system. The horizontal axis is labeled F(A) and ranges from 0 to 1. The vertical axis is labeled A and ranges from 0 to 100. A solid line starts at the origin (0,0) and goes up to (1,100). Three horizontal dashed lines are drawn at A=40, A=50, and A=60. These lines intersect the solid line at F(A) values of 0.4, 0.5, and 0.6 respectively. The area under the solid line is a triangle with base 1 and height 100, with a total area of 50.](3ae8c7e35a46d9336931efdd39c3760c_img.jpg)

A graph of a linear function F(A) on a coordinate system. The horizontal axis is labeled F(A) and ranges from 0 to 1. The vertical axis is labeled A and ranges from 0 to 100. A solid line starts at the origin (0,0) and goes up to (1,100). Three horizontal dashed lines are drawn at A=40, A=50, and A=60. These lines intersect the solid line at F(A) values of 0.4, 0.5, and 0.6 respectively. The area under the solid line is a triangle with base 1 and height 100, with a total area of 50.

a) The area above the line  $A = 40$  and below  $F(A)$  has area  $= 60 * 0.6 * 1/2 = 18$

$$18/50 = 0.36$$

b) The area above the line  $A = 50$  and below  $F(A)$  has area  $= 50 * 0.5 * 1/2 = 12.5$

$$12.5/50 = 0.25$$

c) The area above the line  $A = 60$  and below  $F(A)$  has area  $= 40 * 0.4 * 1/2 = 8$   
 $8/50 = 0.16$

Calculus:

First we normalize the Lee diagram so that the area under the curve (the distribution of the probability of aggregate loss) adds to 1. Then

$$\text{Let } Y = A/E \sim \text{Uniform}(0,2)$$

$$\text{Then } f(y) = 0.50$$

$$(a) \quad r = 40/50 = 0.80 \quad \phi(0.80) = \int_{0.8}^2 0.50(y - 0.80)dy = \mathbf{0.36}$$

$$(b) \quad r = 50/50 = 1 \quad \phi(1) = \int_1^2 0.50(y - 1)dy = \mathbf{0.25}$$

$$(c) \quad r = 60/50 = 1.20 \quad \phi(1.20) = \int_{1.2}^2 0.50(y - 1.20)dy = \mathbf{0.16}$$

4.

$$E = 10 \quad Y = A/E \sim \text{Expon}(\text{mean} = 1) \quad f(y) = e^{-y}$$

$$\psi(r) = \int_0^r (r - y)e^{-y}dy$$

$$(a) \quad r = 5/10 = 0.50 \quad \psi(0.50) = \mathbf{0.1065}$$

$$(b) \quad r = 10/10 = 1 \quad \psi(1) = \mathbf{0.3679}$$

$$(c) \quad r = 15/10 = 1.5 \quad \psi(1.5) = \mathbf{0.7231}$$

5.

![A graph showing the relationship between the Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has a tick mark at 'r'. The x-axis is labeled 'F(y)' and has tick marks at '0' and '1'. A curve starts at the origin (0,0) and increases monotonically, passing through the point (F(r), r). The area under the curve is divided into two regions: the area to the left of the curve is labeled ψ(r), and the area to the right of the curve is labeled φ(r). The area between the horizontal line at y=r and the curve is labeled r-ψ(r) or 1-φ(r).](4c86e4dfdc04db280a2a1ab345358130_img.jpg)

A graph showing the relationship between the Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has a tick mark at 'r'. The x-axis is labeled 'F(y)' and has tick marks at '0' and '1'. A curve starts at the origin (0,0) and increases monotonically, passing through the point (F(r), r). The area under the curve is divided into two regions: the area to the left of the curve is labeled ψ(r), and the area to the right of the curve is labeled φ(r). The area between the horizontal line at y=r and the curve is labeled r-ψ(r) or 1-φ(r).

6.

- (a)  $\Phi(R) = A$
- (b)  $\Phi(S) = A + D + E$
- (c)  $\psi(R) = B + C + F$
- (d)  $\psi(S) = F$

7.

- (a) Step 1: Expected loss ratio = Average Loss Ratio =  
 $(20\%+40\%+40\%+60\%+80\%+80\%+120\%+200\%)/8 = 80\%$   
 So for each risk,  $r = \text{loss ratio}/0.8$

To solve this precisely, we need to look at every slice at which there is at least one data point, plus all the other points we want factors for:

| r   | # Risks<br>from<br>prior to | # Risks<br>Above | % Risks<br>Above | Difference<br>in r | $\Phi(r)$       | $\psi(r) = \Phi(r)+r-1$ |
|-----|-----------------------------|------------------|------------------|--------------------|-----------------|-------------------------|
| 0   | 0                           | 8                | 1.000            | 0.25               | 1.00            | 0                       |
| .25 | 1                           | 7                | 0.875            | 0.25               | .75             | 0                       |
| .50 | 2                           | 5                | 0.625            | 0.25               | .53125          | .03125                  |
| .75 | 1                           | 4                | 0.500            | 0.25               | .25+.5*.25=.375 | .375+.75-1=.125         |
| 1.0 | 2                           | 2                | 0.250            | 0.50               | .125+.25*.5=.25 | 0.25+1-1=.25            |
| 1.5 | 1                           | 1                | 0.125            | 0.50               | .125+.125*1=.25 | 0.125+1.5-1=0.625       |
| 2.0 | 0                           | 1                | 0.125            | 0.50               | 0+.125*.5=.0625 | .0625+2-1=1.0625        |
| 2.5 | 1                           | 0                | 0.000            | 0.50               | 0               | 0+2.5-1=1.5             |
| 3.0 | 0                           | 0                | 0.000            | 0                  | 0               | 0+3-1=2                 |

|       |   |  |  |  |  |  |
|-------|---|--|--|--|--|--|
| Total | 8 |  |  |  |  |  |
|-------|---|--|--|--|--|--|

This can then be summarized as:

| r     | $\Phi(r)$             | $\psi(r) = \Phi(r)+r-1$ |
|-------|-----------------------|-------------------------|
| 0     | 1.00                  | 0                       |
| .50   | .53125                | .03125                  |
| 1.0   | .25                   | .25                     |
| 1.5   | $0.0625+.125*.5=.125$ | $0.125+1.5-1=0.625$     |
| 2.0   | $0+.125*.5=.0625$     | $0.0625+2-1=1.0625$     |
| 2.5   | 0                     | $0+2.5-1=1.5$           |
| 3.0   | 0                     | $0+3-1=2$               |
| Total |                       |                         |

Note what happens if we just look at intervals of 0.5

| r     | Risks from prior to | # Risks Above | % Risks Above | fference in r | $\Phi(r)$             | $\psi(r) = \Phi(r)+r-1$ |
|-------|---------------------|---------------|---------------|---------------|-----------------------|-------------------------|
| 0     | 0                   | 8             | 1.000         | 0.5           | 1.0625                | .0625                   |
| .50   | 3                   | 5             | 0.625         | 0.5           | .5625                 | .0625                   |
| 1.0   | 3                   | 2             | 0.250         | 0.5           | .25                   | .25                     |
| 1.5   | 1                   | 1             | 0.125         | 0.5           | $0.0625+.125*.5=.125$ | $0.125+1.5-1=0.625$     |
| 2.0   | 0                   | 1             | 0.125         | 0.5           | $0+.125*.5=.0625$     | $0.0625+2-1=1.0625$     |
| 2.5   | 1                   | 0             | 0.000         | 0.5           | 0                     | $0+2.5-1=1.5$           |
| 3.0   | 0                   | 0             | 0.000         | 0             | 0                     | $0+3-1=2$               |
| Total | 8                   |               |               |               |                       |                         |

All looks well until we get to  $r = 0.5$ . Then we end up with 0.5625 for the charge, rather than 0.53125. The calculated charge is too large by 0.03125. The error grows at  $r=0$  to 0.0625. This is because when we “integrate” under the curve, we are assuming each piece we are adding is a rectangle. But if we look at the Lee diagram of the outcomes:

![A bar chart titled 'Entry Ratio = r' vs 'Claim Number (ranked by size)'. The x-axis shows claim numbers 1 through 8. The y-axis shows the entry ratio from 0 to 3. The bars represent the cumulative distribution function. The first bar (claim 1) has a height of 0.5. The second bar (claim 2) has a height of 0.5. The third bar (claim 3) has a height of 0.5. The fourth bar (claim 4) has a height of 1.0. The fifth bar (claim 5) has a height of 1.0. The sixth bar (claim 6) has a height of 1.0. The seventh bar (claim 7) has a height of 1.5. The eighth bar (claim 8) has a height of 2.5. A blue shaded area is shown above the first three bars, with arrows pointing to it from the text 'Extra pieces in the boxes, but above the area representing the outcomes.'](ba99363c7d61d24290635b47b71e41c2_img.jpg)

Entry Ratio = r

Extra pieces in the boxes, but above the area representing the outcomes.

Claim Number (ranked by size)

A bar chart titled 'Entry Ratio = r' vs 'Claim Number (ranked by size)'. The x-axis shows claim numbers 1 through 8. The y-axis shows the entry ratio from 0 to 3. The bars represent the cumulative distribution function. The first bar (claim 1) has a height of 0.5. The second bar (claim 2) has a height of 0.5. The third bar (claim 3) has a height of 0.5. The fourth bar (claim 4) has a height of 1.0. The fifth bar (claim 5) has a height of 1.0. The sixth bar (claim 6) has a height of 1.0. The seventh bar (claim 7) has a height of 1.5. The eighth bar (claim 8) has a height of 2.5. A blue shaded area is shown above the first three bars, with arrows pointing to it from the text 'Extra pieces in the boxes, but above the area representing the outcomes.'

We can see that there are two extra pieces in the boxes, but above the area representing the outcomes. Each has area =  $0.25 \times (1/8) = 0.03125$ . That is the source of the extra in the calculation. This is an example of the problem described in footnote 30 on page 66.

(b) 70% L/R  $\rightarrow r=0.875$

It helps to look again at the Lee diagram to understand the situation

![A bar chart titled 'Entry Ratio = r' vs 'Claim Number (ranked by size)'. The y-axis ranges from 0 to 3 with increments of 0.5. The x-axis shows claim numbers 1 through 8. The bars have heights: 0.25, 0.5, 0.5, 0.75, 1.0, 1.0, 1.5, and 2.5. A horizontal line is drawn at r = 0.875, intersecting the bars for claim numbers 5, 6, 7, and 8.](fe8840a79cf6b30f8b2284064f3d2a36_img.jpg)

| Claim Number (ranked by size) | Entry Ratio = r |
|-------------------------------|-----------------|
| 1                             | 0.25            |
| 2                             | 0.5             |
| 3                             | 0.5             |
| 4                             | 0.75            |
| 5                             | 1.0             |
| 6                             | 1.0             |
| 7                             | 1.5             |
| 8                             | 2.5             |

A bar chart titled 'Entry Ratio = r' vs 'Claim Number (ranked by size)'. The y-axis ranges from 0 to 3 with increments of 0.5. The x-axis shows claim numbers 1 through 8. The bars have heights: 0.25, 0.5, 0.5, 0.75, 1.0, 1.0, 1.5, and 2.5. A horizontal line is drawn at r = 0.875, intersecting the bars for claim numbers 5, 6, 7, and 8.

There are a few ways to approach this problem. First, we will solve it precisely, using the horizontal method:

The width of the distribution between 1.0 and 0.875 is 0.5, four of the 8 claims. So the additional insurance charge is 0.5 times the height of the additional band, or  $(1-0.875) \times 0.5 = 0.0625$ . so

$$\Phi(0.875) = \Phi(1.0) + 0.0625 = 0.25 + 0.0625 = \mathbf{0.3125}$$

We could also have interpolated. Had we estimated  $\Phi(0.875)$  with a linear interpolation, we would have gotten:

$$(\Phi(0.5) \times (1-0.875) + \Phi(1.0) \times (0.875 - 0.5)) / (1.0 - 0.5) = (0.53125 \times 0.125 + 0.25 \times 0.375) / (0.5) = \mathbf{0.3203}$$

Note that the interpolation does not give the exact answer, but is reasonably close.

Since we are interested in the insurance charge at a single point, we might also use the vertical method.

| Risk    | Actual<br>Agg. L/R | Entry<br>Ratio | Excess of<br>$r = 70/80 = 0.875$ | Excess of<br>$r = 110/80 = 1.375$ |
|---------|--------------------|----------------|----------------------------------|-----------------------------------|
| 1       | 20%                | 0.25           | 0                                | 0                                 |
| 2       | 40                 | 0.50           | 0                                | 0                                 |
| 3       | 40                 | 0.50           | 0                                | 0                                 |
| 4       | 60                 | 0.75           | 0                                | 0                                 |
| 5       | 80                 | 1.00           | 0.125                            | 0                                 |
| 6       | 80                 | 1.00           | 0.125                            | 0                                 |
| 7       | 120                | 1.50           | 0.625                            | 0.125                             |
| 8       | 200                | 2.50           | 1.625                            | 1.125                             |
| Total:  |                    |                | <b>2.500</b>                     | <b>1.250</b>                      |
| Average |                    |                | <b>0.3125</b>                    | <b>0.15625</b>                    |

- (c)  $\psi(0.875) = 0.3125 + 0.875 - 1 = \mathbf{0.1875}$
- (d) 110% L/R  $\rightarrow r=1.375$ .  $\Phi(1.375) = \mathbf{0.15625}$  (work done in section b)
- (e)  $\psi(1.375) = 0.15625 + 1.375 - 1 = \mathbf{0.53125}$

### 8. Using Parameterized distributions to develop Tables M

#### Advantages:

1. When you don't have a statistically credible group of policies to base your pricing on, but you have an idea of what shape the distribution of outcomes is likely to approximate, you can fit curves to what data you have.
2. When data is thin, and you have large gaps between empirical entry ratios, you don't have to rely on linear interpolation.
3. Even with large body of data, fitting distributions to frequency and severity can help develop charges that are consistent with the excess charges.

#### Disadvantages:

1. If the assumptions underlying the selected distribution aren't close enough to reality, you can generate plausible, internally consistent, precise, but misleading charges.
2. It might be more computationally complex to build a model than to use empirical data for the desired degree of precision.

### 9.

- (a)  $M_D$  Charge at R = **G**
- (b)  $M_D$  Savings at S = **Q+T+U**
- (c) Per-Occ XS Charge at D = **A+D+E+J+L+N+T+U**

### 10.

- (a)  $\{40,000 + (1.1)(150,000)\} (1.05) = 215,250$ .

*Comment: The insured benefited from neither the maximum premium nor the accident limit.*

- (b)  $\{40,000 + (1.1)(200,000)\} (1.05) = 273,000$ . Limited to the maximum of \$250,000.

*Comment: The insured benefited from the maximum premium.*

- (c)  $\{40,000 + (1.1)(100,000)\} (1.05) = 157,500$ .

*Comment: The insured benefited from the accident limit.*

- (d)  $\{40,000 + (1.1)(200,000)\} (1.05) = 273,000$ . Limited to the maximum of \$250,000.

*Comment: The accident limit decreased the losses entering the calculation, but the insured ended up paying the maximum premium anyway.*

*The last case is an example of the “overlap” between the effects of the maximum premium and the accident limit. In some years, even though there are large accidents, the accident limit will not provide any additional benefit to the insured beyond that provided by the maximum premium. In other words, for large accidents the accident limit and the maximum premium overlap*

11.

- (a)  $\{400,000 + (1.1)(150,000)\}(1.05) = 593,250$ . The insured pays the minimum premium, \$650,000.

- (b)  $\{400,000 + (1.1)(100,000)\}(1.05) = 535,500$ . The insured pays the minimum premium, \$650,000.

*The last case is an example of the “underlap” between the effects of the minimum premium and the accident limit. In some years, even though there are large accidents, the accident limit will not provide any benefit to the insured due to the minimum premium. This has a relatively small overall impact.*

12.

$$E=150,000$$

$$\text{Agg Limit} = 300,000$$

$$R = 300 / 150 = 2.0$$

$$\Phi(2.0) \times 150,000 = 15,000$$

$$\Phi(2.0) = 0.10$$

With only Per-Occurrence Deductible:

$$k * E = 50,000 \rightarrow k = 50,000 / 150,000 = 0.333$$

Note that the Aggregate Limit of 300,000 is three times the expected limited loss of 100,000, so the entry ratio,  $r$ , of the limited loss distribution is  $300,000 / 100,000 = 3$ .

![A graph showing the relationship between Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has a horizontal dashed line at y=1. The x-axis is labeled 'F(y)' and ranges from 0 to 1. Two curves originate from (0,0): the upper curve is labeled F(y) and the lower curve is labeled F_{100K}(y). The area between the curves is divided into regions A, B, and C. Region A is the area under F(y) and above the dashed line. Region B is the area between the two curves above the dashed line. Region C is the area under F_{100K}(y) and above the dashed line. Region D is the area under F_{100K}(y) and below the dashed line. Labels include: 'R = 2 unlimited' and 'R = 3 limited' on the y-axis; 'K_{100K} = A+B = 0.33' in region A; 'phi(2) = B+C = 0.1' near the top of the F(y) curve; and 'phi_{100K}(3) = C >= 0' near the top of the F_{100K}(y) curve.](0f4879d336bad8b1801dee947a7dc617_img.jpg)

A graph showing the relationship between Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has a horizontal dashed line at y=1. The x-axis is labeled 'F(y)' and ranges from 0 to 1. Two curves originate from (0,0): the upper curve is labeled F(y) and the lower curve is labeled F\_{100K}(y). The area between the curves is divided into regions A, B, and C. Region A is the area under F(y) and above the dashed line. Region B is the area between the two curves above the dashed line. Region C is the area under F\_{100K}(y) and above the dashed line. Region D is the area under F\_{100K}(y) and below the dashed line. Labels include: 'R = 2 unlimited' and 'R = 3 limited' on the y-axis; 'K\_{100K} = A+B = 0.33' in region A; 'phi(2) = B+C = 0.1' near the top of the F(y) curve; and 'phi\_{100K}(3) = C >= 0' near the top of the F\_{100K}(y) curve.

Together, the combined charge would be  $0.333+0.10 = 0.433$ , or  $0.433 \times 150,000 = 65,000$ . However, the combined charge is very unlikely to be equal to 65,000. It will generally be less than 65,000 because there is overlap between the two charges, as shown by region B in the graph.

13.

- a) The expected primary losses = 20,000.  
Entry ratio =  $40,000/20,000=2.0$   
The aggregate excess loss factor is 0.04, so the insurance charge =  $0.04 \times 20,000=800$ .  
(Which would be in addition to the \$20,000 charge for the per-occurrence deductible, for a total expected loss cost within the policy of \$20,800.)
- b) The expected primary losses = 30,000.  
Entry ratio =  $40,000/30,000=1.333$ .  
Interpolate the aggregate excess loss factors on the table to get  
 $(1/3)*0.22 + (2/3)*.12 = 0.1533 =$  the aggregate excess loss factor.  
So the insurance charge is  $0.1533 \times 30,000 = 4600$   
(which would be in addition to the \$10,000 charge for the per-occurrence deductible, for a total expected loss cost within the policy of \$14,600.)
- c) The insurer will charge more for (a) because even though the aggregate insurance charge is less than (b), the insured has a much smaller per-occurrence deductible which transfers more expected losses to the insurer.

14.

![A graph showing the relationship between the entry ratio r and the normalized area of loss. The vertical axis is labeled 'r = Entry Ratio to unlimited loss' and has tick marks at 1.5, 1.6, and 2. The horizontal axis is labeled 'F(r)' and has tick marks at 0 and 1. Two lines originate from the origin (0,0). The upper line passes through the point (1, 2). The lower line passes through the point (1, 1.6). A horizontal dashed line is drawn at r = 1.5. This line intersects the upper line at a point labeled 'B' and the lower line at a point labeled 'E'. The area between the two lines from F(r)=0 to F(r)=1 is divided into three regions: 'A' is the area below the lower line; 'B' is the area between the two lines from F(r)=0 to the point where the dashed line intersects the upper line; 'C' is the area below the lower line from the point where the dashed line intersects the lower line to F(r)=1. The area between the two lines from the point where the dashed line intersects the lower line to F(r)=1 is labeled 'D'. The area between the lower line and the dashed line from the point where the dashed line intersects the lower line to F(r)=1 is labeled 'E'.](f72d881958a5863f9fea850513142c46_img.jpg)

A graph showing the relationship between the entry ratio r and the normalized area of loss. The vertical axis is labeled 'r = Entry Ratio to unlimited loss' and has tick marks at 1.5, 1.6, and 2. The horizontal axis is labeled 'F(r)' and has tick marks at 0 and 1. Two lines originate from the origin (0,0). The upper line passes through the point (1, 2). The lower line passes through the point (1, 1.6). A horizontal dashed line is drawn at r = 1.5. This line intersects the upper line at a point labeled 'B' and the lower line at a point labeled 'E'. The area between the two lines from F(r)=0 to F(r)=1 is divided into three regions: 'A' is the area below the lower line; 'B' is the area between the two lines from F(r)=0 to the point where the dashed line intersects the upper line; 'C' is the area below the lower line from the point where the dashed line intersects the lower line to F(r)=1. The area between the two lines from the point where the dashed line intersects the lower line to F(r)=1 is labeled 'D'. The area between the lower line and the dashed line from the point where the dashed line intersects the lower line to F(r)=1 is labeled 'E'.

a)  $\Phi_D^*(1.5) = B + D + E$   
 $\psi_D^*(1.5) = A + B$

- b) The normalized area of the total loss (the area of the large triangle,  $B+C+D+E$ ) is 1. The area of the limited loss is  $400/500$  times the total, or 0.8. It is also the area of the small triangle,  $C + E$ .  
 So the area of  $B + D$  is 0.2.

The area of  $E$  is the  $\frac{1}{2}$  the height times the length. The height is  $1.6 - 1.5 = 0.1$ .

$E$  is the same shape as  $C+E$ , which has height 1.6 and length 1. So the length of  $E$  must be  $(0.1/1.6) = 0.0625$ .

So the area of  $E$  is  $0.1 * 0.0625 / 2 = 0.003125$ .

So  $\Phi_D^*(1.5) = B + D + E = 0.2 + 0.003125 = 0.203125$

And

$\psi_D^*(1.5) = \Phi_D^*(1.5) + r - 1 = 0.203125 + 1.5 - 1 = 0.703125$ .

15.

- a)  $T+U+J+L+N+D+E+A+G$   
 b)  $Q+U+T$

16.

#### Advantages:

- When large tables were awkward (either as a vast pile of paper or a computer file that was difficult to store) ICRL allowed a single unlimited Table M to be used to generate reasonable charges that would otherwise have required a large number of Tables M<sub>D</sub>.
- The ICRL procedure is an expedient way of approximating Table M<sub>D</sub> when a suitable Table M<sub>D</sub> is unavailable. For example, this method can be used to adjust a Table M developed based on one book of business to a similar book for which there isn't adequate data to develop its own Tables M.

#### Disadvantages:

- It is only an approximation to Table M<sub>D</sub> and may introduce additional error in the estimate of the charge for the aggregate limit.

17.

- a) Expected Unlimited Losses = 1,000,000 x 0.75 = 750,000  
Expected Limited Losses = 750,000 x (1 - 0.2) = 600,000  
 $r = 1,200,000 / 600,000 = 2.0 \rightarrow \text{Ins Charge} = 0.04 \times 600,000 = 24,000$
- b) Loss Group Adjustment Ftr =  $\frac{1+0.8(0.2)}{1-0.2} = 1.45$

Losses used in group selection = 750,000 x 0.90 x 1.45 = 978,750  $\rightarrow$  ELG 29  
 $r = 1,200,000 / 600,000 = 2.0$   
Insurance Charge Factor = 0.242  
Total Expected Loss Cost = 0.2(750,000) + 0.242(600,000) = 295,200

18.

The State/Hazard Group Relativity makes an adjustment to reflect for differences in claim size by class of business and geographic location. For a given expected loss size, it treats a risk expected to have more severe individual claims as if it is smaller (and thus more variable) than a risk with the same expected loss resulting from a larger number of less severe claims.

The implicit assumption with using the State/Hazard Group Relativity is that the actual severity distribution has a similar shape as that which is used to determine the insurance charges, and differs mostly due to scale. If the difference is extreme, the severity distribution may need to be adjusted, potentially requiring a different Table M

19.

The Table M charge will be larger when the variance of the loss distribution is larger, all else being equal – see Exhibit 3.32.

20.

a) The insurance charge would increase. The toxic paint claims have a low frequency and a very high severity compared to the historical claims. This means they greatly increase the variance of the severity, which increases the variance of the aggregate losses. In particular, with the original assumptions, an insured would have had to experience twice the expected claims frequency to breach the aggregate, but with the revised understanding of the liability, a single large claim would be almost enough to do so. This will result in a much larger insurance charge at an entry ratio of 2.0.

b) A per-occurrence limit, assuming it is high enough to be above the historical losses, but substantially limits the toxic paint claims, would shift losses from the aggregate limit charge to the per-occurrence charge. Therefore, the charge for the aggregate deductible would decrease.

### Chapter 4 Answers

1. The fair premium should be lower, as the insured is responsible for a significant fraction of the risk.
2. Because you need to price for the risk involved and the expenses of monitoring the claims experience. The risk includes the risk that the insured knows more about the liability than you do. The expenses may include annual or monthly reports to the insured whether or not any losses breach the insurable threshold.
3. Given a large deductible WC policy with the following features:
  - \$2M expected total loss
  - Expected average severity of \$10,000 per claim
  - The insured retains 86% of expected loss under the per-occurrence deductible (14% is expected to be excess of the deductible)
  - There is a limit on the aggregate deductible retained by the insured of \$3M

b.) What is the insurance charge for the aggregate limit?

If the account is larger than the pricing actuary realized, and the expected total losses should have been \$2.5M, what should the insurance charge have been?

## References

- Bahnemann, D. "Distributions for Actuaries," CAS Monograph # 2.
- Brosius, J. Eric., "Table M Construction," CAS Study Note, 2002.
- Couret, Jose and Gillam, William R., "Retrospective Rating: 1997 Excess Loss Factors," *PCAS* LXXXIV, 1997.
- Fisher, Ginda Kaplan, "Pricing Aggregates on Deductible Policies," CAS Study Note, May 2002.
- Gillam, W. R., "Workers' Compensation Experience Rating: What Every Actuary Should Know," *PCAS* LXXIX, 1992.
- Gillam, W. R. and Snader, R.H., "Fundamentals of Individual Risk Rating," National Council on Compensation Insurance (Study Note), 1992
- Heckman, Philip E. and Meyers, Glenn G., "The Calculation of Aggregate Loss Distributions from Claim Severity and Claim Count Distributions," *PCAS* LXX, 1983.
- Insurance Services Office, Inc., *Commercial General Liability Experience and Schedule Rating Plan*, 2006. (or any other year)
- Lee, Yoong-Sin, "The Mathematics of Excess of Loss Coverages and Retrospective Rating—A Graphical Approach," *PCAS* LXXV, 1988.
- Mahler, Howard C., Discussion of "Retrospective Rating: 1997 Excess Loss Factors," *PCAS* LXXXV, 1998, Including Errata.
- Miccolis, R. S., "On the Theory of Increased Limits and Excess of Loss Pricing," *PCAS* LXIV, 1977. Including discussion of paper: Rosenberg, S., *PCAS* LXIV, 1977, pp. 60-73.
- National Council on Compensation Insurance, *Experience Rating Plan Manual for Workers Compensation and Employers Liability Insurance*.
- National Council on Compensation Insurance, *Retrospective Rating Plan Manual for Workers Compensation and Employers Liability Insurance*.
- National Council on Compensation Insurance, Circular CIF-2017-32 *Countrywide Announcement of Items R-1414 Revisions to Retrospective Rating Plan Manual Appendix B and all Related Rules and Endorsements*, 2017.
- Panjer, Harry "Recursive Evaluation of a Family of Compound Distributions," *Astin Bulletin*, Vol. 12, No. 1, 1981, pp. 22-26
- Robertson, J.P., "NCCI's 2007 Hazard Group Mapping," *Variance*, Vol. 3, Issue 2, 2009, Casualty Actuarial Society, pp. 194-213.

- Robbin, Ira, "Overlap Revisited—The 'Insurance Charge Reflecting Loss Limitation' Procedure," *Pricing*, Casualty Actuarial Society *Discussion Paper Program*, 1990, Volume 2.
- Skurnick, D., "The California Table L," *PCAS* LXI, 1974, pp. 117-140. Including discussion of this paper: Gillam, W.R., *PCAS* LXXX, 1993, pp. 353-365.
- Teng, M. T. S., "Pricing Workers' Compensation Large Deductible and Excess Insurance," *Casualty Actuarial Society Forum*, Winter 1994, pp. 413-437.
- Venter, G.G., "Experience Rating—Equity and Predictive Accuracy," *NCCI Digest*, April 1987, Volume II, Issue I, pp. 27-35.