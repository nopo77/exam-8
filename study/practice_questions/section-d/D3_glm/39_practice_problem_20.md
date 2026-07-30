---
tia_section: D3
tia_topic: glm
title: Practice Problem 20
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 20
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
source_sheet: Practice Problem 20
---

# Practice Problem 20

## Question

You are given the following confusion matrix for a logistic model with a discrimination threshold of 28%:

Predicted

| Actual | Yes |   | No |   | Total |
| --- | --- | --- | --- | --- | --- |
| Yes | True positives: | 40 | False negatives: | 180 | 220 |
| No | False positives: | 50 | True negatives: | 1,185 | 1,235 |
| Total |  | 90 |  | 1,365 | 1,455 |

### Part a

Calculate the specificity and sensitivity from the above data.

### Part b

Discuss the impact on the specificity and sensitivity of increasing the discrimination threshold to 40%.

## Solution

### Part a

| B | C |
| --- | --- |
| Sensitivity | 18.2% |
| Specificity | 96.0% |

<details><summary>Formulas</summary>

- `C20` = `=D9/G9`
- `C21` = `=F10/G10`

</details>

### Part b

Increasing the discrimination threshold will result in fewer true positives and more true negatives. Since these are the numerators of sensitivity and specificity respectively, these will cause the sensitivity of the model to decrease and the specificity of the model to increase.
