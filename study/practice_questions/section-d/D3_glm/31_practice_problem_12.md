---
tia_section: D3
tia_topic: glm
title: Practice Problem 12
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 12
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
source_sheet: Practice Problem 12
---

# Practice Problem 12

## Question

### Part a

Briefly discuss why a separate dataset should be used for testing a GLM than the dataset used to train the GLM.

### Part b

Discuss 2 approaches that can be used to split individual records from a ratemaking dataset into a training dataset and a testing dataset. Include an advantage of one of those approaches.

## Solution

### Part a

Adding additional variables to a GLM will always result in a better fit on the training dataset. As such, to test the predictive power of the model, we need to use a separate testing dataset.

### Part b

Records can be split on a time basis or randomly. A time basis means that the records from a certain time period (e.g., certain accident years) would go in the training dataset and the remaining records would go in the testing dataset. The advantage of splitting using time is that the same weather events would be in both datasets if split randomly, which can result in over-optimistic validation results.
