---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 10
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 10
revised: false
points: null
parts: [a, b, c]
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [holmes_&_casotto/]
source_workbook: tia_excel/section-d/D_5_Penalized_Regression_Lasso_Cred_practice_solutions.xlsx
source_sheet: Practice Problem 10
---

# Practice Problem 10

## Question

### Part a

Discuss the purpose of control variables in models, and give 2 examples of control variables and why they might be used.

### Part b

Discuss the pros of allowing the penalty term in a lasso model to apply to control variables.

### Part c

Discuss an approach for ensuring that control variables remain in a lasso model other than just directly not applying the penalty term to those variables.

## Solution

### Part a

Control variables are used in models to control for overall expected effects we expect to see in the data that might be correlated with other predictor variables, even though we usually don't care about the estimates for control variables. Two common examples of control variables are year (to account for things like trend and development) and state (when building a countrywide model).

### Part b

Having a penalty for control variables is appropriate since the model can consistently allocate the signal between the control variables and any correlated predictor variables. And if a control variable is removed from the model due to a lasso penalty, then the impact of it was likely minimal anyways.

### Part c

Use a stepwise modeling approach:

1. Fit a model with control variables and maybe a few potentially correlated predictor variables with

low or no penalty.

2. Include the control variable coefficients from the above model in the offset term as part of your

regular model with the penalty term.
