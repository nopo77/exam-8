---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 5 - Fisher Chapter 3 Q4
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 5
revised: false
points: null
parts: [a, b, c]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 5
---

# Practice Problem 5 - Fisher Chapter 3 Q4

## Question

Let aggregate loss random variable A be an exponential distribution with a mean of:

10 — Mean of exponential distribution

Find the Table M (Insurance) Savings associated with:

### Part a

**L =:** 5

### Part b

**L =:** 10

### Part c

**L =:** 15

## Solution

| L | F(L) | E[A;L] | Table M Savings |
| --- | --- | --- | --- |
| 5 | 0.39 | 3.93 | 0.1065 |
| 10 | 0.63 | 6.32 | 0.3679 |
| 15 | 0.78 | 7.77 | 0.7231 |

<details><summary>Formulas</summary>

- `I4` = `=C11`
- `J4` = `=EXPON.DIST(I4,1/B$6,TRUE)`
- `K4` = `=B$6*J4`
- `L4` = `=(I4-K4)/B$6`
- `I5` = `=C14`
- `J5` = `=EXPON.DIST(I5,1/B$6,TRUE)`
- `K5` = `=B$6*J5`
- `L5` = `=(I5-K5)/B$6`
- `I6` = `=C17`
- `J6` = `=EXPON.DIST(I6,1/B$6,TRUE)`
- `K6` = `=B$6*J6`
- `L6` = `=(I6-K6)/B$6`

</details>
