---
tia_section: D3
tia_topic: glm
title: Practice Problem 5
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 5
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [goldburd_et_al/]
source_workbook: tia_excel/section-d/D_3_GLM_practice_solutions.xlsx
source_sheet: Practice Problem 5
---

# Practice Problem 5

## Question

You are trying to combine Poisson frequency and Gamma severity distributions into a single Tweedie pure premium distribution. For a particular observation, the distributions have the following parameters:

| B | C |
| --- | --- |
| 0.02 | Poisson λ |
| 0.55 | Gamma α |
| 8,000 | Gamma θ |

### Part a

Calculate the mean and variance of the Tweedie distribution for this observation.

### Part b

Discuss how the shape of the Tweedie distribution changes as power parameter of the Tweedie distribution moves between 1 and 2.

## Solution

### Part a

**Mean:** 88 — `=PRODUCT(B8:B10)`

Tweedie Variance = phi*mu^p

**p:** 1.645 — `=(B9+2)/(B9+1)`

**phi:** 690.11 — `=(B8^(1-C24)*(B9*B10)^(2-C24))/(2-C24)`

**Variance:** 1,091,200 — `=C26*C20^C24`

### Part b

When p moves closer to 1, the Tweedie becomes more like Poisson, and it will have spikes at discrete points with some variance around each spike. As p moves closer to 2, the Tweedie becomes more like Gamma, and it will look like a smoother curve with no apparent spikes (other than at 0).
