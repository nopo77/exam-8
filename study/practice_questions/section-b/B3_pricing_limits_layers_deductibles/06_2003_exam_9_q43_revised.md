---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2003 Exam 9 - Q43 revised
source: past_exam
exam_year: 2003
exam_sitting: null
exam_number: 9
question_number: 43
practice_number: null
revised: true
points: 2.0
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2003 Exam 9 - Q43 revised
---

# 2003 Exam 9 - Q43 revised

**Points:** 2

## Question

You believe the standard deviation of pure premiums is an appropriate measure of risk. You are given the following pure premium distribution:

| Amount of Loss | Probability of Loss |
| --- | --- |
| $0 | 90% |
| $1,000 | 9% |
| $10,000 | 1% |

| B | C |
| --- | --- |
| 10% | Percent of standard deviation selected as the appropriate risk load |
| $2,000 | Basic aggregate limit |
| $5,000 | Aggregate limit on policy being priced |

There are no expenses. What is the increased limit factor with risk load for a $5,000 aggregate policy limit?

## Solution

Note that the table gives a pure premium distribution, not a severity distribution, which is evident given the 90% chance of no losses. So the $1k and $10k in the table represent the total losses from all claims. Furthermore, the limits we are discussing here are aggregate limits, not per-claim limits, so we aren't using the per-claim risk load formulas from the lessons. Instead, since the question says there are no expenses, the premium for a policy will just consist of the expected loss cost plus the risk load:

Prem_L = E[S;L] + 10% × Stdev[S;L]

| Limit L | E[S;L] | E[S^2;L] | Stdev[S;L] | Prem for limit L | Risk-loaded ILF for L |
| --- | --- | --- | --- | --- | --- |
| $2,000 | $110 | $130,000 | 343.37 | $144.34 |  |
| $5,000 | $140 | $340,000 | 566.04 | $196.60 | 1.362 |

<details><summary>Formulas</summary>

- `C28` = `=SUMPRODUCT($D$8:$D$10,J8:J10)`
- `D28` = `=SUMPRODUCT($D$8:$D$10,K8:K10)`
- `E28` = `=SQRT(D28-C28^2)`
- `F28` = `=C28+$B$12*E28`
- `C29` = `=SUMPRODUCT($D$8:$D$10,L8:L10)`
- `D29` = `=SUMPRODUCT($D$8:$D$10,M8:M10)`
- `E29` = `=SQRT(D29-C29^2)`
- `F29` = `=C29+$B$12*E29`
- `G29` = `=F29/F28`

</details>

| cap at 2k | square | cap at 5k | square |
| --- | --- | --- | --- |
| $0 | $0 | $0 | $0 |
| $1,000 | $1,000,000 | $1,000 | $1,000,000 |
| $2,000 | $4,000,000 | $5,000 | $25,000,000 |

<details><summary>Formulas</summary>

- `J8` = `=MIN(C8,$B$13)`
- `K8` = `=J8^2`
- `L8` = `=MIN(C8,$B$14)`
- `M8` = `=L8^2`
- `J9` = `=MIN(C9,$B$13)`
- `K9` = `=J9^2`
- `L9` = `=MIN(C9,$B$14)`
- `M9` = `=L9^2`
- `J10` = `=MIN(C10,$B$13)`
- `K10` = `=J10^2`
- `L10` = `=MIN(C10,$B$14)`
- `M10` = `=L10^2`

</details>
