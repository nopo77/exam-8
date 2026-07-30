---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2011 Exam 8 - Q17 revised
source: past_exam
exam_year: 2011
exam_sitting: null
exam_number: 8
question_number: 17
practice_number: null
revised: true
points: 3.0
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2011 Exam 8 - Q17 revised
---

# 2011 Exam 8 - Q17 revised

**Points:** 3

## Question

Let X represent the size of loss of a given claim. Assume the following average severities for varying claim size intervals:

| Size of Loss Interval | Average Size of Loss |
| --- | --- |
| X <= $500 | $250 |
| $500 < X <= $1,000 | $750 |
| X > $1,000 | $2,000 |

The following information is also available:

| B | C |
| --- | --- |
| 500 | Total number of claims in study |
| $650 | Overall average claim size |
| 0.50 | Loss elimination ratio for a $500 straight deductible |

$1,000 — Calculate the loss elimination ratio for a straight deductible of $1,000.

## Solution

Solution 1: Step by step logic

LER at 1000 ded = [($250 * # claims below $500) + ($750 * # claims between $500 and $1000) + ($1000 * # claims above $1000)] / Total Losses

We will need to figure out the number of claims in each size interval, which we can do with the information given. First, we can figure out the number of claims below $500 given the LER, since a $500 deductible will eliminate claims below $500 in full and will eliminate $500 off of claims above $500. Next, we can use this information to determine the number of claims between $500 and $1,000 since we also know the overall average claim size. Finally, we can solve for the desired LER.

**Total Losses:** $325,000 — `=B14*B15`

LER at 500 ded = [($250 * # claims below $500) + ($500 * # claims above $500)] / Total Losses = 0.50

Let the number of claims under $500 be A

LER at 500 ded = [$250 * A + $500 * (500-A)] / Total Losses = 0.50

| I | K |
| --- | --- |
| Loss eliminated by 500 ded | $162,500 |
| A | 350 |

<details><summary>Formulas</summary>

- `K20` = `=K12*B16`
- `K21` = `=(K20-B14*500)/(C8-500)`

</details>

Let the number of claims between $500 and $1,000 be B.

Total Losses = ($250 * 350) + ($750 * B) + [$2000 * (500-350-B)] = $325,000

$750 * B - $2000 * B = $325,000 - ($250 * 350) - [$2000 * (500-350)]

**B:** 50 — `=(K12-C8*K21-C10*(B14-K21))/(C9-C10)`

**# claims above 1000:** 100 — `=B14-K21-K29`

**LER at $1000:** 69.2% — `=(C8*K21+C9*K29+B18*K31)/K12`

Solution 2: Set up system of equations and solve using Excel matrix functions

Here we can set up 3 equations to solve for the 3 unknown claim counts in each size interval.

Let A be # claims below $500 — Total Losses

Let B be # claims between $500 and $1000

Let C be # claims above $1000 — Loss eliminated by 500 ded

| I | L |
| --- | --- |
| A + B + C = 500 | <-- total claim counts |
| 250A + 750B + 2000C = 325,000 | <-- total losses |
| 250A + 500B + 500C = 162,500 | <-- loss eliminated by 500 deductible |

| Left-side matrix from equations above |   |   | Right-side result array from equations above |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 500 |
| $250 | $750 | $2,000 | $325,000 |
| 250 | $500 | $500 | $162,500 |

<details><summary>Formulas</summary>

- `I49` = `=C8`
- `J49` = `=C9`
- `K49` = `=C10`
- `M49` = `=P39`
- `M50` = `=P41`

</details>

Inverse Matrix:

| I | J | K |
| --- | --- | --- |
| 2 | -0 | -0.004 |
| -1.2 | -0.0008 | 0.0056 |
| 0.2 | 0.0008 | -0.0016 |

<details><summary>Formulas</summary>

- `I53` = `={MINVERSE(I48:K50)}`

</details>

| I | J | L |
| --- | --- | --- |
| A | 350 | Multiply inverse matrix by result array to get variable array |
| B | 50 |  |
| C | 100 |  |

<details><summary>Formulas</summary>

- `J57` = `={MMULT(ANCHORARRAY(I53),M48:M50)}`

</details>

**LER at $1000:** 69.2% — `=(SUMPRODUCT(J57:J58,C8:C9)+J59*B18)/P39`

$325,000 — `=B15*B14`

$162,500 — `=P39*B16`
