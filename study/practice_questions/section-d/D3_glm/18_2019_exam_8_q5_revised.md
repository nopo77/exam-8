---
tia_section: D3
tia_topic: glm
title: 2019 Exam 8 - Q5 revised
source: past_exam
exam_year: 2019
exam_sitting: null
exam_number: 8
question_number: 5
practice_number: null
revised: true
points: 1.25
parts: [a, b, d]
good_problem: true
has_images: true
has_examiner_report: true
layout: vertical
split_confidence: clean
readings: [goldburd_et_al/]
source_workbook: tia_excel/section-d/D_3_GLM_practice_solutions.xlsx
source_sheet: 2019 Exam 8 - Q5 revised
---

# 2019 Exam 8 - Q5 revised

**Points:** 1.25

## Question

The following confusion matrix shows the result from a claim fraud model with a discrimination threshold of 25%:

Predicted

| Actual | Yes | No |
| --- | --- | --- |
| Yes | 72 | 162 |
| No | 63 | 1,203 |

### Part a (0.50 pts)

Identify a link function that can be used for a generalized linear model that has a binary target variable and briefly explain why this link function is appropriate.

### Part b (0.50 pts)

Calculate the sensitivity and specificity from the above data.

### Part d (0.25 pts)

Briefly describe how the severity of claims will impact the selection of the model threshold.

## Solution

### Part a

The logit link function is best to use as its inverse (the logistic function) transforms the linear predictor to a [0,1] range that is appropriate for a binary target variable.

### Part b

| B | C |
| --- | --- |
| Sensitivity | 30.8% |
| Specificity | 95.0% |

<details><summary>Formulas</summary>

- `C26` = `=D9/(D9+E9)`
- `C27` = `=E10/(D10+E10)`

</details>

### Part d

With higher severity of fraud, it will be cost effective to spend more on investigating fraud, which means choosing a lower discrimination threshold to catch more potential fraud.

## Examiner Report

Examiner report solutions and comments:

![examiner image](images/img_fe1f188edae0.png)

![examiner image](images/img_3c66dcd1cf57.png)

![examiner image](images/img_260dc92ee0ce.png)

![examiner image](images/img_47e1c2983a7a.png)
