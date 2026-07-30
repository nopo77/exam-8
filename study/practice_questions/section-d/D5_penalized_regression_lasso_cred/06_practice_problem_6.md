---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 6
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 6
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
source_sheet: Practice Problem 6
---

# Practice Problem 6

## Question

Discuss the drawbacks of using non-sparse models for actuarial ratemaking.

## Solution

If a model isn't sparse, then it will be easier for new variables to appear or drop out of the predictor variable list between model refreshes/runs. If as a result, the list of rating variables used in ratemaking changes frequently, this will cause more cost for the insurer's IT department to implement the changes, it will create more scrutiny with regulators in reviewing the changing variables, and it will have more disruptive rate impacts on insured's premiums. Furthermore, this could result in models that are more difficult to interpret, and for which the variable selection decision is based on judgment (e.g., using an arbitrary p-value threshold) instead of a statistical framework.
