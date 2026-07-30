---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 11
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 11
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
source_sheet: Practice Problem 11
---

# Practice Problem 11

## Question

### Part a

Fully explain the bias-variance trade-off in the context of predictive models.

### Part b

Discuss how the bias-variance trade-off is evaluated using traditional Generalized Linear Models.

### Part c

Discuss how penalized regression models help optimize the bias-variance trade-off.

## Solution

### Part a

In predictive modeling, the goal is to minimize the error between a model's estimates and the true values being estimated. This error can be broken down into two main components: bias and variance.

Bias is the error between a model's predictions and the true, real-world relationships. A model with high bias is too simple and doesn't sufficiently capture the underlying patterns, a condition known as underfitting.

Variance is the error that results from using a limited sample of data rather than the entire true population. A model with high variance is too sensitive to the random noise in the training data and doesn't generalize well to new data, a condition known as overfitting.

The "trade-off" comes from the fact that it is impossible to reduce both bias and variance at the same time. Adding complexity to a model (like including more variables) tends to decrease bias but, in turn, increases variance. The goal of a modeler is to find the optimal balance between the two that minimizes the overall error.

### Part b

In a traditional GLM, the bias-variance trade-off is managed by adding or removing variables and then evaluating the results using various statistics after the model has been fit. The most common metrics used for this evaluation are AIC and BIC. These metrics work by "penalizing" a model's goodness of fit based on its complexity. When comparing two models, such as one with an additional variable and one without, the model with the lower AIC or BIC is considered to have the more optimal bias-variance trade-off.

### Part c

Penalized regression uses coefficient shrinkage to optimize the trade-off. The shrinkage process introduces bias by pulling the coefficients away from their pure data-driven estimates and toward a chosen complement (0 in regular penalized regression). This is done to achieve a more-than-offsetting reduction in model variance, which makes the model less sensitive to noise in the training data and more stable. The trade-off is optimized during the model fitting process itself, typically using cross-validation to find the optimal penalty parameter, which controls the amount of shrinkage. This procedure finds the trade-off that best generalizes to unseen data, removing the need for post-hoc metrics like AIC or BIC.
