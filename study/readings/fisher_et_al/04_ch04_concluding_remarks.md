---
paper: fisher_et_al
chapter: 4
title: "Chapter 4: Concluding Remarks"
topics: [insurance_charge_sensitivity, loss_pick_adequacy, assumption_consistency, aggregate_excess_pricing, risk_load, loss_sensitive_plan_pricing]
key_formulas: []
---

> **TL;DR**
> - A 10% inadequate loss pick can cause >20% underpricing of the Table M insurance charge; the error compounds because both the expected claim count group (ELG) and the effective entry ratio shift simultaneously in the same direction
> - Loss pick leverage is greatest for large policies at low entry ratios; small policies and high entry ratios are relatively less sensitive to loss pick errors
> - Always charge a non-negligible premium for high aggregate or per-occurrence loss layers even when estimated loss cost is near zero—risk load and ongoing monitoring expenses remain significant, and the insured may have private information about exposure
> - Mismatched assumptions (e.g., bureau aggregate charges paired with proprietary per-occurrence charges using different LAE or loss definitions) can cause the sum of primary + per-occurrence excess + aggregate excess to diverge from total expected loss; validate all components sum to the total
> - The balanced plan concept (expected retro premium = guaranteed cost premium) is increasingly unnecessary for most lines; the essential check is that expected losses are properly balanced across all retro formula components

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

