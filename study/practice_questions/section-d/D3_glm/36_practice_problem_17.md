---
tia_section: D3
tia_topic: glm
title: Practice Problem 17
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 17
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [goldburd_et_al/]
source_workbook: tia_excel/section-d/D_3_GLM_practice_solutions.xlsx
source_sheet: Practice Problem 17
---

# Practice Problem 17

## Question

You have constructed a GLM for private passenger auto severity. The model has two rating variables: territory (urban or rural) and gender (male or female). You are given the following information about this model:

| B | C |
| --- | --- |
| 12 | Number of observations in dataset |
| 15 | Estimated unscaled deviance |
| 1.25 | Estimated dispersion parameter |

Another model, which has the same variables as the prior model but with an additional binary variable for whether the driver is under the age of 18, was estimated on the same dataset. For this model:

| B | C |
| --- | --- |
| 9 | Estimated unscaled deviance |
| 1.25 | Estimated dispersion parameter |

Using the F table at α = 0.05 provided below, perform a null hypothesis test to decide which model is superior.

| B | C | D | E | F | G | H | I | J | K |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | df1 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| df2 = 1 | 161.45 | 199.50 | 215.71 | 224.58 | 230.16 | 233.99 | 236.77 | 238.88 | 240.54 |
| 2 | 18.51 | 19.00 | 19.16 | 19.25 | 19.29 | 19.33 | 19.35 | 19.37 | 19.38 |
| 3 | 10.13 | 9.55 | 9.28 | 9.12 | 9.01 | 8.94 | 8.89 | 8.85 | 8.81 |
| 4 | 7.71 | 6.94 | 6.59 | 6.39 | 6.26 | 6.16 | 6.09 | 6.04 | 6.00 |
| 5 | 6.61 | 5.79 | 5.41 | 5.19 | 5.05 | 4.95 | 4.88 | 4.82 | 4.77 |
| 6 | 5.99 | 5.14 | 4.76 | 4.53 | 4.39 | 4.28 | 4.21 | 4.15 | 4.10 |
| 7 | 5.59 | 4.74 | 4.35 | 4.12 | 3.97 | 3.87 | 3.79 | 3.73 | 3.68 |
| 8 | 5.32 | 4.46 | 4.07 | 3.84 | 3.69 | 3.58 | 3.50 | 3.44 | 3.39 |
| 9 | 5.12 | 4.26 | 3.86 | 3.63 | 3.48 | 3.37 | 3.29 | 3.23 | 3.18 |

## Solution

H0 : The F statistic is not significantly different from 1 (i.e., the small model is superior).

Reject the null hypothesis if the F-test statistic is greater than the relevant F table value.

The small model has 3 (non-dispersion) parameters: 1 for the intercept term, 1 for gender (either male or female), and 1 for territory (either urban or rural). The big model has a 4th parameter for whether the driver is over or under 18.

**F statistic:** 4.8 — `=(B9-B16)/(1*B17)`

df2 — 8 — `=B8-4` — 4 parameters in big model

**F_1,8:** 5.32 — `=C30`

Since 4.8 < 5.32, we do not reject the null hypothesis, and we conclude that the model with fewer parameters is superior.
