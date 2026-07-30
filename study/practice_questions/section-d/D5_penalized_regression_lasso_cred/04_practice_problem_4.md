---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 4
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 4
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
source_sheet: Practice Problem 4
---

# Practice Problem 4

## Question

Compare and contrast lasso, ridge, and elastic net models as applied to insurance ratemaking.

## Solution

All 3 models contain a penalty that generally shrink GLM coefficients towards 0. Ridge models have a more direct relationship to Buhlmann credibility, but cannot set coefficients to 0. Lasso and Elastic Nets can set coefficients to 0, resulting in more sparse models. This means the variable list will be more stable, reducing IT costs, regulator scrutiny, and customer rate impacts. Lasso allows coefficients to grow quickly once they are significant, unlike Ridge and Elastic Nets which have coefficients grow slower. Overall, Lasso models achieve sparsity and allow coefficients to grow quickly, which are both beneficial for ratemaking.
