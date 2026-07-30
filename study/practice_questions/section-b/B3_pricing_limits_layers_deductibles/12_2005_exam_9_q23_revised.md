---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2005 Exam 9 - Q23 revised
source: past_exam
exam_year: 2005
exam_sitting: null
exam_number: 9
question_number: 23
practice_number: null
revised: true
points: 3.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2005 Exam 9 - Q23 revised
---

# 2005 Exam 9 - Q23 revised

**Points:** 3

## Question

An insurance company has determined that its general liability claims are accurately modeled by a Poisson frequency distribution, and a lognormal severity distribution having the following limited first and second moments:

Limited Severity

| Per Occurrence Limit | 1st Moment | 2nd Moment |
| --- | --- | --- |
| $100,000 | $19,433 | 1,284,000,000 |
| $500,000 | $32,923 | 7,962,000,000 |
| $1,000,000 | $38,064 | 15,310,000,000 |
| $2,000,000 | $42,244 | 27,200,000,000 |
| $5,000,000 | $46,109 | 51,590,000,000 |
| $10,000,000 | $47,901 | 76,740,000,000 |

Assume:

- Only process risk needs to be reflected in the increased limit factors.

| B | C |
| --- | --- |
| 0.10 | Mean of Poisson frequency distribution |
| 5% | The appropriate risk load for policies having a $100,000 per occurrence limit is equal to 5% of |

the expected pure premium.

$100,000 — Basic occurrence limit

Calculate the risk-adjusted increased limit factor for a policy having a $5,000,000 per occurrence limit.

## Solution

The process risk is the same type of risk we are quantifying with the risk loads discussed in the lessons (as opposed to parameter risk). Since this question doesn't specify, we can use either a variance or standard deviation approach here.

Solution 1: Variance approach

| K | M |
| --- | --- |
| PP for 100k | $1,943.30 |
| Risk load for 100k | $97.17 |

<details><summary>Formulas</summary>

- `M7` = `=B21*C10`
- `M8` = `=M7*B22`

</details>

The general variance formula for a risk load is ρ(l) = k(E[X^2;l] + δ(E[X;l])^2) Since frequency is Poisson, δ=0, and we just have ρ(l) = kE[X^2;l]

**k:** 0.000000076 — `=M8/D10`

**I_r(5M):** 2.561 — `=(C14+M13*D14)/(C10+M13*D10)`

Solution 2: Standard deviation approach

| K | M |
| --- | --- |
| PP for 100k | $1,943.30 |
| Risk load for 100k | $97.17 |

<details><summary>Formulas</summary>

- `M19` = `=B21*C10`
- `M20` = `=M19*B22`

</details>

The general standard deviation formula for a risk load is ρ(l) = k'*sqrt(E[X^2;l] + δ(E[X;l])^2) Since frequency is Poisson, δ=0, and we just have ρ(l) = k' * sqrt(E[X^2;l])

**k':** 0.002711611 — `=M20/SQRT(D10)`

**I_r(5M):** 2.392 — `=(C14+M25*SQRT(D14))/(C10+M25*SQRT(D10))`
