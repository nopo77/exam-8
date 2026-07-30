---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 12
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 12
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
source_sheet: Practice Problem 12
---

# Practice Problem 12

## Question

An actuary is using a Lasso Credibility model with a log link function to model claim frequency for a homeowners book of business. The model has the following parameters/variables:

- An intercept term for the model
- A categorical variable for the presence of a central burglar alarm, with 2 levels (1 if yes, 0 otherwise).
- A categorical variable for the insured's territory of residence, with 20 levels.
- A categorical variable for the construction type of the home, with 3 levels.
- An ordinal variable for the rating of the insured's local fire department, with 10 levels.
- An offset term that includes deductible relativities determined using a loss elimination analysis.

Each variable above has a corresponding complement of credibility included in the offset term of the model.

You also have the following information for the central burglar alarm variable:

| B | C |
| --- | --- |
| 0.88 | Total predicted relativity (including complement) from the Lasso Credibility model |
| 0.95 | Complement of credibility relativity |

### Part a

Calculate the beta coefficient (excluding the complement) estimated by the model for the central burglar alarm variable.

### Part b

The traditional GLM estimate for the central burglar alarm coefficient is:

-0.22 — Traditional GLM coefficient estimate

Calculate the implied credibility given to the modeling data's GLM coefficient for the central burglar alarm variable.

### Part c

The coefficient for the central alarm variable in the Lasso Credibility model is Beta_j. Suppose that the complement of credibility coefficient for the alarm variable was set to -0.22 instead of being based on the complement relativity given above. Discuss how Beta_j would change as the number of observations in the data increases.

## Solution

### Part a

Total relativity = exp(Beta_j + Beta_complement) Total relativity = exp(Beta_j) * exp(Beta_complement) 0.88 = exp(Beta_j) * 0.95

**Beta_j:** -0.077 — `=LN(B17/B18)`

### Part b

Z*Beta_GLM + (1-Z)*Beta_Complement = Beta_j + Beta_Complement Z = (Beta_j + Beta_Complement - Beta_Complement) / (Beta_GLM - Beta_Complement) Z = (Beta_j) / (Beta_GLM - Beta_Complement)

| K | L |
| --- | --- |
| Beta_GLM | -0.22 |
| Beta_Complement | -0.051 |

<details><summary>Formulas</summary>

- `L12` = `=B27`
- `L13` = `=LN(B18)`

</details>

**Z:** 0.454 — `=L6/(L12-L13)`

### Part c

In this case, the GLM estimate (based on the data) perfectly matches the complement estimate. Since Beta_j represents the difference of the modeling data estimate from the complement, the model will set this to 0. This doesn't change as the number of observations increase (though it might smooth out any volatility in the data so the model is more confident about setting the coefficient to 0).
