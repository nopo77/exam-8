---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 9
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 9
revised: false
points: 1.5
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [chalk_et_al/]
source_workbook: tia_excel/section-d/D_6_From_GLMs_practice_solutions.xlsx
source_sheet: Practice Problem 9
---

# Practice Problem 9

**Points:** 1.5

## Question

Match the penalized-regression technique on the left with the single best description on the right.

## Solution

> Relaxed LASSO

> A two-stage procedure: use a penalized fit purely to SELECT features (discarding its coefficient values), then refit the chosen features with little or no shrinkage.

> Fused LASSO

> Penalizes the differences between coefficients of ADJACENT ordinal levels, so neighboring levels are pushed toward equal values.

> Hard-thresholding

> Can zero out small coefficients but leaves the surviving coefficients at their unshrunk magnitudes, producing a less stable model.

> Adaptive LASSO

> A single fit that assigns each feature its own penalty weight, derived from a first-pass model, so important features are penalized less and weak ones more.

> Soft-thresholding

> Can zero out small coefficients AND shrinks the surviving coefficients toward zero with a single global penalty.

> Elastic net (α ≈ 0.95)

> Mixes the lasso and ridge penalties, keeping lasso-style selection while improving stability when features are highly correlated.

> Grouped LASSO

> Penalizes the group norm of a categorical variable's level dummies, forcing all levels of that variable in or out together.
