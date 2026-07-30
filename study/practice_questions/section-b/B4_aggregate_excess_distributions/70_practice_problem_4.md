---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 4 - Fisher Chapter 3 Q3
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 4
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
source_sheet: Practice Problem 4
---

# Practice Problem 4 - Fisher Chapter 3 Q3

## Question

Let A, the total aggregate loss random variable, have a continuous uniform distribution on the interval below:

| B | C |
| --- | --- |
| 0 | Bottom of interval |
| 100 | Top of interval |

Let E, the expected aggregate losses, be the mean of the uniform distribution, or

50 — `=AVERAGE(B7:B8)` — E (mean of distribution)

Find the Table M Insurance Charge associated with:

### Part a

**L =:** 40

### Part b

**L =:** 50

### Part c

**L =:** 60

## Solution

L — F(L) — E[A;L] — Table M Charge

### Part a

40 — `=C17` — 0.4 — `=I4/B$8` — 32 — `=J4*I4/2+(1-J4)*I4` — 0.36 — `=(B$12-K4)/B$12`

### Part b

50 — `=C20` — 0.5 — `=I5/B$8` — 37.5 — `=J5*I5/2+(1-J5)*I5` — 0.25 — `=(B$12-K5)/B$12`

### Part c

60 — `=C23` — 0.6 — `=I6/B$8` — 42 — `=J6*I6/2+(1-J6)*I6` — 0.16 — `=(B$12-K6)/B$12`
