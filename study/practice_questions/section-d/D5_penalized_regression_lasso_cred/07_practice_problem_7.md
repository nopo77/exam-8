---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 7
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 7
revised: false
points: null
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [holmes_&_casotto/]
source_workbook: tia_excel/section-d/D_5_Penalized_Regression_Lasso_Cred_practice_solutions.xlsx
source_sheet: Practice Problem 7
---

# Practice Problem 7

## Question

Explain how cross-validation can be used to help select an optimal penalty parameter for penalized regression models.

## Solution

Since there is no formula to calculate the optimal penalty parameter in penalized models, a good process is to test different values of the parameter and see which value results in the best predictive power. To do this using cross-validation, you can perform the following steps:

1. Split the data into modeling data and validation data.

2. Split the modeling data into k folds.

3. For each fold, train a model using other k - 1 folds, and test model using this kth fold.

4. For each test fold, calculate performance metrics like deviance, Gini index, and pseudo-R^2.

5. Choose the penalty parameter with the best average metrics across all folds, incorporating judgment as appropriate.
