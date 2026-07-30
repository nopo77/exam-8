---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 5
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 5
revised: false
points: 2.0
parts: [a, b, c, d]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [chalk_et_al/]
source_workbook: tia_excel/section-d/D_6_From_GLMs_practice_solutions.xlsx
source_sheet: Practice Problem 5
---

# Practice Problem 5

**Points:** 2

## Question

An actuary models the natural log of claim severity for a homeowners book by least squares, using five standardized predictors that are mutually uncorrelated in the modeling data; predicted severity is the exponentiated fitted value, so exp of a coefficient acts as a severity relativity per standard deviation of a feature. The unpenalized coefficients are shown. The actuary refits the model as a LASSO (the same least-squares loss with an L1 penalty) at a fixed lambda; at that lambda the fitted LASSO coefficient for the roof age score is 0.52.

| Variable | Unpenalized coefficient |
| --- | --- |
| Roof age score | 0.62 |
| Protection class score | -0.41 |
| Home age score | 0.15 |
| Lot size score | -0.08 |
| Owner tenure score | 0.03 |

0.52 — LASSO coefficient for the roof age score

### Part a (0.75 pts)

Determine the LASSO coefficients of the other four variables at this lambda.

### Part b (0.50 pts)

Determine the reduction amount at which the protection class score would just be eliminated, and the surviving coefficients at that point.

### Part c (0.25 pts)

Briefly explain why a ridge fit would retain all five variables at any lambda.

### Part d (0.50 pts)

Calculate the indicated severity relativity for a risk one standard deviation above average on home age, before and after the penalization in part (a), and the percentage change in that relativity.

## Solution

### Part a

With least-squares loss and standardized, mutually uncorrelated predictors, the penalized objective separates into one single-feature problem per coefficient, and each solves by soft thresholding: every surviving coefficient's absolute value falls by the same amount, and any coefficient smaller than that amount is removed. The roof age score reveals the reduction.

Reduction in absolute value

Protection class score Home age score Lot size score Owner tenure score

### Part b

Reduction eliminating protection class

At a reduction (lambda) of 0.41, all coefficients except roof age would be set to 0.

Roof age score at that reduction

### Part c

This could be said in different ways. This is just one (simple) way to say this.

Ridge doesn't have an absolute value in its penalty term, which is what allows LASSO to set coefficients to 0. So ridge coefficients get shrunk towards 0, but never fully set to 0.

### Part d

With the model fit on log severity, predicted severity is the exponentiated fitted value, so exp of the home age coefficient is its multiplicative effect per standard deviation since variables are standardized.

Relativity before penalization Relativity after penalization Change in the relativity

0.10 — `=ABS($C$15)-ABS($B$21)`

LASSO coefficient

-0.31 — `=SIGN($C16)*MAX(0,ABS($C16)-$O$6)`

0.05 — `=SIGN($C17)*MAX(0,ABS($C17)-$O$6)`

0.00 — `=SIGN($C18)*MAX(0,ABS($C18)-$O$6)`

0.00 — `=SIGN($C19)*MAX(0,ABS($C19)-$O$6)`

0.41 — `=ABS($C$16)`

0.21 — `=SIGN($C$15)*MAX(0,ABS($C$15)-$O$14)`

1.1618 — `=EXP($C$17)`

1.0513 — `=EXP($O$10)`

-9.52% — `=O29/O28-1`
