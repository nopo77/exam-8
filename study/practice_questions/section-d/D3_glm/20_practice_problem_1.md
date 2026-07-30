---
tia_section: D3
tia_topic: glm
title: Practice Problem 1
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 1
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [goldburd_et_al/]
source_workbook: tia_excel/section-d/D_3_GLM_practice_solutions.xlsx
source_sheet: Practice Problem 1
---

# Practice Problem 1

## Question

Fully describe the 2 main components of a Generalized Linear Model.

## Solution

One component is the random component, which states that each y_i is assumed to be independent and to come from the exponential family of distributions with mean mu_i and variance Var(y_i) = (phi*V(mu_i)/omega_i). Phi is called the dispersion parameter and is a constant used to scale the variance. V(mu) is called the variance function and it describes the relationship between the variance and mean for a selected distribution type. Omega_i are known as weights and assign a weight to each observation i.

The other component is the systematic component, which is of the form g(mu) = Beta0 + Beta1 x1 + Beta2 x2 + ··· + Betap xp + offset. The right hand side is known as the linear predictor. The offset term is optional and allows you to manually specify the estimates for certain variables. The x's are the predictor variables. g(mu) is called the link function, and allows for transformations of the linear predictor. For rating plans, the log link function g(mu) = ln(mu) is typically used since it transforms the linear predictor into a multiplicative structure. Beta0 is called the intercept term, and the other beta's are called the coefficients of the model. These are what we want to estimate. Once we know the beta's, we can plug in known values for the x variables and calculate the predicted values of the y variables (i.e., mu).
