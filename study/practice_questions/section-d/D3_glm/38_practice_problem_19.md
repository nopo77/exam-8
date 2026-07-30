---
tia_section: D3
tia_topic: glm
title: Practice Problem 19
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 19
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
source_sheet: Practice Problem 19
---

# Practice Problem 19

## Question

Briefly describe 3 options for measuring model stability.

## Solution

- The influence of an individual record on the model can be measured using the Cook's distance,

which can be calculated by most GLM software. Records with the highest Cook's distance should be given additional scrutiny as to whether they should be included in the dataset or not.

- Cross-validation can be used to assess model stability by comparing in-sample parameter

estimates across different model runs.

- Bootstrapping can be used to create new datasets with the same number of records by

randomly sampling with replacement from the original dataset. The model can then be refit on many different datasets and we can get statistics like the mean and variance for each parameter estimate.
