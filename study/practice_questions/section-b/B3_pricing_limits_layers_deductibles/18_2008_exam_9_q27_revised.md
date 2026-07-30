---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2008 Exam 9 - Q27 revised
source: past_exam
exam_year: 2008
exam_sitting: null
exam_number: 9
question_number: 27
practice_number: null
revised: true
points: 2.25
parts: [a, b, c]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2008 Exam 9 - Q27 revised
---

# 2008 Exam 9 - Q27 revised

**Points:** 2.25

## Question

The following increased limit factors (ILFs) are used to price a general liability policy:

| Limit | ILF |
| --- | --- |
| $100,000 | 0.800 |
| $250,000 | 1.000 |
| $500,000 | 1.375 |
| $1,000,000 | 1.750 |

### Part a (0.75 pts)

Demonstrate that there is exactly one ILF that violates the consistency test.

### Part b (1.00 pts)

Calculate the range of possible values that the inconsistent ILF found in part (a) above may take so that all the factors in the table pass the consistency test.

### Part c (0.50 pts)

Discuss one reason why a set of ILFs may fail the consistency test yet still generate actuarially reasonable prices.

## Solution

### Part a

I'(l)

0.0000013 — `=(C8-C7)/(B8-B7)`

0.0000015 — `=(C9-C8)/(B9-B8)` — Test fails at $500k since I''(l)>0

0.0000008 — `=(C10-C9)/(B10-B9)`

### Part b

| J | K |
| --- | --- |
| x >= 1 | 500k ILF should be greater than 250k ILF |
| x <= 1.75 | 500k ILF should be less than 1M ILF |

(x - 1)/(500k-250k) <= 0.0000013

**x <=:** 1.33 — `=J8*(B9-B8)+C8`

(x - 1)/(500k-250k) >= (1.75-x)/(1M-500k)

| J | K |
| --- | --- |
| $250,000 | $500,000 |
| $437,500 | $500,000 |

<details><summary>Formulas</summary>

- `J19` = `=B9-B8`
- `K19` = `=B10-B9`
- `J20` = `=J19*C10`
- `K20` = `=K19*C8`

</details>

**x >=:** 1.25 — `=(J20+K20)/(J19+K19)`

So 1.25 <= I(500k) <= 1.33

### Part c

It would be very difficult to justify ILFs failing the I'(l) >= 0 criterion, so I'll focus on the 2nd criterion.

If insureds with higher loss potential were more inclined to buy higher limits, or jury verdicts were larger for larger limits, then ILFs could fail I''(l) <= 0 and still be reasonable.

Optional I''(l) rescaled

0.01 — `=(J9-J8)/(B9-B8)*10000000000`

-0.02 — `=(J10-J9)/(B10-B9)*10000000000`
