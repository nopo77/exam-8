---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 7
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 7
revised: false
points: 1.75
parts: [a, b, c, d]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [chalk_et_al/]
source_workbook: tia_excel/section-d/D_6_From_GLMs_practice_solutions.xlsx
source_sheet: Practice Problem 7
---

# Practice Problem 7

**Points:** 1.75

## Question

An actuary tunes the penalty of a homeowners water-damage frequency model by cross-validation. For each lambda on the grid, the table shows the mean validation pseudo-R-squared across folds, the standard error of that mean, and the number of features the fit retains.

| Lambda | Mean validation pseudo-R^2 | Standard error | Features retained |
| --- | --- | --- | --- |
| 0.5 | 0.0332 | 0.0009 | 46 |
| 1.0 | 0.0337 | 0.0008 | 38 |
| 2.0 | 0.0340 | 0.0004 | 27 |
| 4.0 | 0.0338 | 0.0005 | 19 |
| 8.0 | 0.0334 | 0.0006 | 12 |
| 16.0 | 0.0327 | 0.0006 | 8 |
| 32.0 | 0.0316 | 0.0005 | 5 |
| 64.0 | 0.0296 | 0.0005 | 3 |

### Part a (0.50 pts)

Identify the lambda that maximizes estimated validation performance, and calculate the one-standard-error threshold.

### Part b (0.50 pts)

Apply the one-standard-error rule to select a model. State the selected lambda and its feature count, and calculate the reduction in features relative to the maximum-performance model.

### Part c (0.25 pts)

Briefly explain the rationale for preferring the one-standard-error model despite its lower point estimate of performance.

### Part d (0.50 pts)

The chief actuary instead accepts any model within 2% of the maximum performance. Determine the model that rule selects, and state whether it simplifies more or less aggressively than the one-standard-error rule here.

## Solution

### Part a

Maximum mean performance One-standard-error threshold

### Part b

The rule selects the largest lambda (the simplest model) whose mean performance still meets the threshold.

Lambda = 4 is largest lambda with pseudo-R^2 >= 0.0336.

Features at the selection Features removed by the rule

### Part c

The two means differ by less than the noise in the estimates, so the data cannot distinguish the models on performance; given a statistical tie, the simpler model wins on stability, filing, and maintenance.

### Part d

Within-2% threshold

Lambda = 8 is largest lambda with pseudo-R^2 >= 0.0333.

That selects the 12-feature model, so the 2% rule simplifies more aggressively than the one-standard-error rule's 19 features in this table.

0.0340 — `=MAX($C$9:$C$16)` — at lambda = 2

0.0336 — `=N2-D11`

19 — `=E12`

8 — `=E11-N9`

0.0333 — `=0.98*MAX($C$9:$C$16)`
