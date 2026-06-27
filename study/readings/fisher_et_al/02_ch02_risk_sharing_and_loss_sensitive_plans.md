---
paper: fisher_et_al
chapter: 2
title: "Chapter 2: Risk Sharing Through Retrospective Rating and Other Loss-Sensitive Rating Plans"
topics: [retrospective_rating, loss_sensitive_plans, large_deductibles, self_insured_retentions, credit_risk, basic_premium, loss_conversion_factor, tax_multiplier]
key_formulas: [retrospective_premium_formula, basic_premium_expense_formula, tax_multiplier_formula]
---

> **TL;DR**
> - Retro premium: P = (B + cL) × T; B covers fixed charges (per-occurrence excess, net insurance charge, fixed expenses, profit); c = loss conversion factor covers variable loss expenses (ALAE/ULAE); T = 1/(1 − tax rate)
> - Risk transfer under a retro equals that of a large deductible when: per-occurrence limit = per-occurrence deductible, max ratable loss = aggregate deductible limit, and there is no minimum ratable loss
> - SIRs carry no insurer credit risk because the insurer never advances retained losses; large deductibles and incurred retros both create credit risk, mitigated by security/collateral, loss development factors applied to ratable losses, or holdbacks deferring adjustments
> - Large deductible premiums are lower than equivalent retro premiums because deductible reimbursements are not "premium" and are therefore exempt from premium-based taxes and some assessments
> - Dissolution: retro plans closed via closeout (final LDFs applied to losses); large deductible plans via buyout or loss portfolio transfer; SIR plans via loss portfolio transfer only

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



