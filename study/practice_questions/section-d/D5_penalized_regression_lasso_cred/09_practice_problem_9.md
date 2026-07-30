---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 9
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 9
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [holmes_&_casotto/]
source_workbook: tia_excel/section-d/D_5_Penalized_Regression_Lasso_Cred_practice_solutions.xlsx
source_sheet: Practice Problem 9
---

# Practice Problem 9

## Question

An actuary is building a pure premium lasso regression model for a homeowners insurance book of business. The model has the following parameters/variables:

- An intercept term for the model
- A categorical variable for the insured's territory of residence, with 20 levels.
- A 3rd degree polynomial for home age (age, age^2, age^3).
- A categorical variable for the construction type of the home, with 3 levels.
- An ordinal variable for the rating of the insured's local fire department, with 10 levels.
- An offset term that includes deductible relativities determined using a loss elimination analysis.

When fine-tuning the penalty parameter for the model, the actuary notices jumps in the Gini index at certain values of the penalty parameter.

### Part a

Discuss why the jumps could be occurring.

### Part b

Give 3 options for dealing with the issue causing the jumps.

## Solution

### Part a

The polynomial terms for the home age variable will be highly correlated with each other, so the lasso penalty is likely to remove some of these terms as the penalty parameter is increased. When a term is removed, it is likely to cause the jumps being observed.

### Part b

3 options:

1. Don't apply the lasso penalty to the home age variable and instead use judgment to decide which terms to include in the model.

2. Use a ridge penalty for the home age variable (which can't remove terms from the model like lasso).

3. Transform the home age variable into an ordinal variable.
