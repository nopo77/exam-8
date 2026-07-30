---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 14
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 14
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [holmes_&_casotto/]
source_workbook: tia_excel/section-d/D_5_Penalized_Regression_Lasso_Cred_practice_solutions.xlsx
source_sheet: Practice Problem 14
---

# Practice Problem 14

## Question

An actuary is reviewing a newly developed Lasso Credibility model for commercial auto insurance.

- The model includes categorical variables for Driver_Experience (Levels: Low, Medium, High)

and Business_Class (Levels: Local Radius, Long Haul).

- The complement of credibility for Driver_Experience is derived from a very stable, multi-year

internal study of the company's entire book of business.

- The complement of credibility for Business_Class is taken from an external industry-wide rating manual.
- The actuary knows that these two variables are correlated; drivers with "Low" experience are much

more likely to be in the "Local Radius" business class than in "Long Haul."

After fitting the model, the actuary reviews the relativity plots and notices that the indicated relativities for both Driver_Experience and Business_Class are almost identical to their respective complements.

Discuss whether this will potentially lead to problematic estimated relativities. Explain.

## Solution

The complements of credibility for these 2 variables come from different sources, and as such, the complements do not take into account the correlation between the 2 variables. Since the model is estimating relativities that are very close to the complements, the model predictions will not fully account for the correlation between these variables. As a result, the model will likely under or over estimate the risks for these segments.
