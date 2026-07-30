---
tia_section: D3
tia_topic: glm
title: Practice Problem 11
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 11
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [goldburd_et_al/]
source_workbook: tia_excel/section-d/D_3_GLM_practice_solutions.xlsx
source_sheet: Practice Problem 11
---

# Practice Problem 11

## Question

Briefly discuss how adding additional predictor variables in a model will impact the fit of a GLM on both the training dataset and on the testing dataset.

## Solution

Adding more variables to a model will always cause the model to fit the training dataset better since they provide more freedom for the model to fit that data. However, these additional variables only add predictive power to the model on other datasets (such as the testing dataset) up to a point, after which they are being fit to the noise in the training dataset in addition to the signal, and as such are less useful when applied to new datasets.
