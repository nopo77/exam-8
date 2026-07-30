---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2007 Exam 9 - Q10 revised
source: past_exam
exam_year: 2007
exam_sitting: null
exam_number: 9
question_number: 10
practice_number: null
revised: true
points: 2.0
parts: [a, b, c]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2007 Exam 9 - Q10 revised
---

# 2007 Exam 9 - Q10 revised

**Points:** 2

## Question

### Part a (1.00 pts)

The following increased limits factors are used to price general liability policies.

| Limit | ILF |
| --- | --- |
| $100,000 | 1.00 |
| $300,000 | 1.75 |
| $500,000 | 2.55 |
| $1,000,000 | 2.65 |

Demonstrate whether these increased limits factors pass the consistency test.

### Part b (0.50 pts)

Discuss one reason why it is desirable for a set of increased limits factors to pass this consistency test.

### Part c (0.50 pts)

Discuss one reason that a set of increased limits factors may fail this consistency test yet still generate actuarially reasonable prices.

## Solution

### Part a

I'(l) — Optional I''(l) rescaled

0.0000038 — `=(C10-C9)/(B10-B9)`

| J | K | L |
| --- | --- | --- |
| 0.0000040 | 0.12 | The test fails at a limit of $500,000, since I''(l) > 0. |
| 0.0000002 | -0.76 |  |

<details><summary>Formulas</summary>

- `J11` = `=(C11-C10)/(B11-B10)`
- `K11` = `=(J11-J10)/(B11-B10)*100000000000`
- `J12` = `=(C12-C11)/(B12-B11)`
- `K12` = `=(J12-J11)/(B12-B11)*100000000000`

</details>

### Part b

I'll show one way to word this, but discussing other things like adverse selection could be fine as well.

If the test fails the I'(l) >= 0 criterion, an insured would pay less for more coverage, which wouldn't make any sense. If the test fails the I''(l) <= 0 criterion, it implies negative probabilities in the claim size distribution (i.e., f(x) < 0 for some values of x), which doesn't make sense.

### Part c

It would be very difficult to justify ILFs failing the I'(l) >= 0 criterion, so I'll focus on the 2nd criterion.

If insureds with higher loss potential were more inclined to buy higher limits, or jury verdicts were larger for larger limits, then ILFs could fail I''(l) <= 0 and still be reasonable.
