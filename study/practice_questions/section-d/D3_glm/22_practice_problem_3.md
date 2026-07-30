---
tia_section: D3
tia_topic: glm
title: Practice Problem 3
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 3
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
source_sheet: Practice Problem 3
---

# Practice Problem 3

## Question

### Part a

State 3 advantages of using a log link function when building a pure premium model for use in creating a rating plan.

### Part b

You are given the output from a pure premium GLM below:

| Parameter | β |
| --- | --- |
| Intercept | 5.8036 |

Location

**Rural:** -0.2107

Risk Class

| B | C |
| --- | --- |
| B | -0.0834 |
| C | 0.2469 |

- The Location variable has values of Urban and Rural.
- The Risk Class variable has values of A, B, C, and D.
- Risk Class D was combined with Risk Class A in the model due to low exposures.
- The GLM has a log link function.
- The error distribution selected is Tweedie.
- Pure premium in the GLM includes loss and ALAE.
- All ULAE, UW expenses, and profit are variable to premium.

Based on the above, calculate each of the relativities for each variable in the rating plan.

## Solution

### Part a

A log link allows for a multiplicative rating plan, which has the following advantages:

- Simple and practical to implement.
- It guarantees positive premiums.
- Impact of risk characteristics is more intuitive.

### Part b

| B | C |
| --- | --- |
| Urban Rel | 1 |
| Rural Rel | 0.81 |

<details><summary>Formulas</summary>

- `C38` = `=EXP(C15)`

</details>

| B | C |
| --- | --- |
| Risk Class A Rel | 1 |
| Risk Class B Rel | 0.92 |
| Risk Class C Rel | 1.28 |
| Risk Class D Rel | 1 |

<details><summary>Formulas</summary>

- `C41` = `=EXP(C18)`
- `C42` = `=EXP(C19)`

</details>
