---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 2
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 2
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
source_sheet: Practice Problem 2
---

# Practice Problem 2

## Question

State the 3 conditions for incorporating credibility into a GLM, and discuss how lasso credibility satisfies these 3 conditions.

## Solution

Conditions:

1. We can't just maximize log-likelihood to get coefficients (what GLMs do which give full credibility).

2. Estimates should be between traditional GLM estimates and complements of credibility,

depending on volume and volatility of modeling data.

3. "Credibility-weighting" must be part of model fitting to consider correlations between variables.

How lasso credibility satisfies these conditions:

1. The model will minimize the combination of negative log-likelihood and the lasso penalty.

2. The lasso penalty will shrink coefficients towards the complements of credibility.

3. Lasso estimates are "credibility-weighted" during model fitting through the penalty term.
