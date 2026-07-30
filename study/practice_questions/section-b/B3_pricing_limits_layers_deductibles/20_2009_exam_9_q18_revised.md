---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2009 Exam 9 - Q18 revised
source: past_exam
exam_year: 2009
exam_sitting: null
exam_number: 9
question_number: 18
practice_number: null
revised: true
points: 2.0
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2009 Exam 9 - Q18 revised
---

# 2009 Exam 9 - Q18 revised

**Points:** 2

## Question

The following information is available for general liability insurance:

| Policy Limit (l) | Average Severity of Limited Losses E[X;l] | Second Moment of the Limited Severity Dist. E[X^2;l] |
| --- | --- | --- |
| $500,000 | $83,333 | 100,000,000,000 |
| $1,000,000 | $142,857 | 400,000,000,000 |
| $1,500,000 | $166,667 | 1,200,000,000,000 |
| $2,000,000 | $200,000 | 2,500,000,000,000 |
| $2,500,000 | $227,273 | 3,400,000,000,000 |
| $3,000,000 | $250,000 | 5,000,000,000,000 |

| B | C |
| --- | --- |
| $500,000 | Basic Limit |
| 0 | k for Risk Loading Proportional to Variance |
| 2 | Expected Number of Claims |

The number of claims follows a Poisson distribution.

Calculate the difference between the risk-adjusted increased limit factor and the unadjusted increased limit factor for a policy with a limit of $2,000,000.

## Solution

**I(2M):** 2.400 — `=C10/C7`

**I_r(2M):** 2.981 — `=(C10+B15*D10)/(C7+B15*D7)`

**Difference:** 0.581 — `=C26-C24`
