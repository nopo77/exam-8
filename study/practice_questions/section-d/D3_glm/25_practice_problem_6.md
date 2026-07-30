---
tia_section: D3
tia_topic: glm
title: Practice Problem 6
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 6
revised: false
points: null
parts: [a, b, c, d, e, f]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [goldburd_et_al/]
source_workbook: tia_excel/section-d/D_3_GLM_practice_solutions.xlsx
source_sheet: Practice Problem 6
---

# Practice Problem 6

## Question

A main benefit of GLMs over univariate analysis is being able to handle exposure correlation, however, GLMs also run into problems when predictor variables are very highly correlated.

### Part a

Briefly state what can happen in GLMs with highly correlated predictor variables.

### Part b

Suggest two options for dealing with highly correlated predictor variables. Give a downside of each approach.

### Part c

Define multicollinearity, and state why it is a problem in GLMs.

### Part d

Briefly state one way to detect multicollinearity in a model.

### Part e

Define aliasing.

### Part f

Briefly state how GLM software can be used to correct for aliasing in a GLM.

## Solution

### Part a

This can result in an unstable model with erratic coefficients that have high standard errors.

### Part b

i. Removing all highly correlated variables except one. This eliminates the high correlation in

the model, but it also potentially loses some unique information contained in the eliminated variables.

ii. Use dimensionality-reduction techniques such as principal components analysis or factor

analysis to create a new subset of variables from the correlated variables, and use this subset of variables in the GLM. The downside is the additional time required to do this extra analysis.

### Part c

Multicollinearity occurs when there is a near-perfect linear dependency among 3 or more predictor variables. For example, suppose x1 + x2 is nearly equal to x3 . When multicollinearity is present in a model, the model may become unstable with erratic coefficients, and it may not converge to a solution.

### Part d

Use the variance inflation factor (VIF) statistic, which is given for each predictor variable, and measures the impact on the squared standard error for that variable due to collinearity with other predictor variables by seeing how well other predictor variables can predict the variable in question.

### Part e

When there is a perfect linear dependency among predictor variables, those variables are aliased.

### Part f

Most GLM software will detect aliasing and automatically remove one of the problematic variables from the model.
