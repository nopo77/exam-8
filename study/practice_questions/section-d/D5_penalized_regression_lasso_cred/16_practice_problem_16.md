---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 16
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 16
revised: false
points: null
parts: [a, b, c]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [holmes_&_casotto/]
source_workbook: tia_excel/section-d/D_5_Penalized_Regression_Lasso_Cred_practice_solutions.xlsx
source_sheet: Practice Problem 16
---

# Practice Problem 16

## Question

An actuary is tasked with building a predictive model from a dataset with a large number of potential predictor variables. They compare two approaches: a best subset selection procedure and a Lasso regression model. After running both procedures, the two final models have selected the exact same set of 15 predictor variables.

### Part a

For the 15 predictor variables included in both models, how would you expect the magnitude of their coefficients in the Lasso model to compare to the magnitude of their coefficients in the best subset selection model? Explain your reasoning.

### Part b

A colleague argues that because both models selected the same set of variables, and best subset selection is considered the theoretical "gold standard," the best subset model must have better predictive performance on a holdout dataset. Critique this argument by explaining the key reason, related to the bias-variance trade-off, why the Lasso model might actually outperform the best subset model in practice.

### Part c

Aside from predictive performance, what is the primary practical reason that best subset selection is often not used for models with many potential predictor variables?

## Solution

### Part a

The coefficients in the Lasso model are expected to be smaller in magnitude (i.e., shrunk closer to zero) than the coefficients in the best subset selection model. A best subset selection model first identifies the optimal set of predictors and then fits a standard GLM using only those predictors. This means the coefficients are the full, maximum-likelihood estimates without any shrinkage. A Lasso model, by contrast, includes a penalty term that inherently shrinks the coefficients of all selected variables toward zero. Therefore, even for the same set of included variables, the Lasso coefficients will be less extreme than their best subset counterparts.

### Part b

The Lasso model can shrink the coefficients towards 0, which introduces a bias (toward 0) that reduces the variance. Because of this, the Lasso model will have lower model variance compared to the best subset model, and this can result in the Lasso model having an overall better balance of bias and variance and thus better predictive performance.

### Part c

Best subset selection problems are not numerically tractable, so they can't be solved efficiently with computers like lasso models.
