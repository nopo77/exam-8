---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 7 - Bahnemann Problem 6.4
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 7
revised: false
points: null
parts: [a, b]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: Practice Problem 7
---

# Practice Problem 7 - Bahnemann Problem 6.4

## Question

The average claim frequency for a portfolio of policies is given below:

0.000800 — φ, average claim frequency

If the claim-count distribution is Poisson, compute the probability that an individual annual policy selected from this portfolio will give rise to more than a single claim when the number of exposures units per policy is:

### Part a

1,000

### Part b

2,000

## Solution

Exposures — Lambda — Pr(N>1)

### Part a

1,000 — `=C12` — 0.8 — `=B17*$B$6` — 0.191 — `=1-POISSON.DIST(1,C17,TRUE)`

### Part b

2,000 — `=C13` — 1.6 — `=B18*$B$6` — 0.475 — `=1-POISSON.DIST(1,C18,TRUE)`
