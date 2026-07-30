---
tia_section: B2
tia_topic: excess_distributions
title: Practice Problem 9
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 9
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 9
---

# Practice Problem 9

## Question

Given the following information:

- Ground-up claim counts follow a Poisson distribution.
- Ground-up claim severity follows an exponential distribution.

| B | C |
| --- | --- |
| 2 | Mean of ground-up claim count Poisson distribution |
| $1,000 | Mean of ground-up claim severity exponential distribution |
| $500 | Policy retention |

Calculate the mean and variance of claim counts excess of a $500 retention.

## Solution

Solution 1: Shortcut way by recognizing distribution of excess counts

Prob of claim above 500 — 0.607 — `=EXP(-B11/B10)` — Alternatively: — 0.607 — `=1-EXPON.DIST(B11,1/B10,TRUE)`

**E[N_a]  = Var[N_a] since Poisson, both =:** 1.213 — `=D18*B9`

Solution 2: Longer way doing the calculations

Prob of claim above 500 — 0.607 — `=EXP(-B11/B10)` — Alternatively: — 0.607 — `=1-EXPON.DIST(B11,1/B10,TRUE)`

**E[N_a]:** 1.213 — `=D24*B9`

**Var[N_a]:** 1.213 — `=D24^2*B9+D24*(1-D24)*B9`
