---
tia_section: C3
tia_topic: mahler
title: Practice Problem 3
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 3
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [mahler/]
source_workbook: tia_excel/section-c/C_3_Mahler_practice_solutions.xlsx
source_sheet: Practice Problem 3
---

# Practice Problem 3

## Question

You are given the following information for a homeowners insurer:

- The exposure and claim experience for this insurer for the last 4 years is:

| Year | Earned Exposures | Closed Claim Counts |
| --- | --- | --- |
| 2,015 | 50,000 | 2,512 |
| 2,016 | 55,000 | 2,834 |
| 2,017 | 60,000 | 2,654 |
| 2,018 | 65,000 | 3,322 |
| Total | 230,000 | 11,322 |

- You are given the following chi-square table with α = 0.10:

| Degrees of Freedom | Critical Value α = 0.10 |
| --- | --- |
| 1 | 2.706 |
| 2 | 4.605 |
| 3 | 6.251 |
| 4 | 7.779 |
| 5 | 9.236 |
| 6 | 10.645 |

Use the chi-square test with α = 0.10 to test whether claim frequency has shifted over time for the insurer's book for business.

## Solution

First we need to calculate the expected frequency using the 4 year total.

**Expected Freq:** 0.049226 — `=E13/D13`

| Expected Claim Counts | Chi-squared |
| --- | --- |
| 2,461.304348 | 1.044182 |
| 2,707.434783 | 5.91658 |
| 2,953.565217 | 30.383389 |
| 3,199.695652 | 4.67493 |

<details><summary>Formulas</summary>

- `J9` = `=D9*L$5`
- `M9` = `=(E9-J9)^2/J9`
- `J10` = `=D10*L$5`
- `M10` = `=(E10-J10)^2/J10`
- `J11` = `=D11*L$5`
- `M11` = `=(E11-J11)^2/J11`
- `J12` = `=D12*L$5`
- `M12` = `=(E12-J12)^2/J12`

</details>

**Total:** 42.01908 — `=SUM(M9:M12)`

Compare to chi-squared table value with 3 degrees of freedom.

Since 42.019 > 6.251, conclude that risk parameters have shifted over time.

Note: in this example, the large chi-square value was mostly driven by a single year having unexpectedly low claim counts. This demonstrates that the chi-square value will be high simply due to large differences between actual and expected.
