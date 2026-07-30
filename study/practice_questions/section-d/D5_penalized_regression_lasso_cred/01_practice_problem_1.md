---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 1
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 1
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
source_sheet: Practice Problem 1
---

# Practice Problem 1

## Question

An insurance company has developed a Generalized Linear Model (GLM) to predict annual claim counts for a new line of business in the state of Utah.

Given:

- The model uses a Poisson distribution with a log link function.
- The model includes an offset term to account for the natural log of exposures.
- The GLM was fitted using maximum likelihood optimization.
- The fitted model parameters are as follows:

| Variable | Coefficient | p-Value |
| --- | --- | --- |
| Intercept | -2.500 | < 0.001 |
| Policy_Type_B | 0.470 | 0.025 |
| Policy_Type_C | 0.693 | 0.080 |
| Insured_Exp_Factor | -0.050 | < 0.001 |

Additional Information:

- The base level for Policy_Type is "A".
- The Policy_Type_C segment is a new pilot program with very limited data (20 exposures),

while all other segments have thousands of exposures.

- The Insured_Exp_Factor is a continuous variable representing the insured's years of experience.
- The Insured_Exp_Factor variable is not logged.
- There is some exposure correlation between the Policy Type and Insured Experience variables.

### Part a

Calculate the predicted claim counts for a policy with the following characteristics:

| Policy Type | C |
| --- | --- |
| Insured's Experience (Years) | 2 |
| Exposures | 0.5 |

### Part b

A junior analyst notices that the p-value of 0.080 for the Policy_Type_C variable is not statistically significant at the 5% level. Instead of removing the variable from the model, the analyst suggests credibility-weighting the relativity based on the model estimate of 0.693 with the countrywide relative average claim frequency for policy type C compared to policy type A.

Discuss a problem with that suggestion, and suggest an alternative approach to obtaining a policy type C estimated relativity that overcomes that problem.

## Solution

### Part a

**linear predictor:** -2.600 — `=C13+C15+C16*C30+LN(C31)`

**Predicted claim counts:** 0.074 — `=EXP(L2)`

### Part b

Solution 1 : the intended answer (that you should have thought of given this problem is in the lasso credibility section)

Problem: the credibility-weighting will be on a univariate basis, and will thus lose some of the multivariate benefit of using the GLM (especially since we know there is correlation between insured experience and policy type).

Alternative approach: we could build a GLM on the insurer's countrywide data, and then build a lasso credibility model for Utah with the countrywide estimates as the complements of credibility (including for policy type C). This would give an estimate for policy type C that effectively credibility-weights the state estimate with the countrywide estimate while still accounting for multivariate effects (i.e., the correlation with insured experience).

Solution 2: view the statistical significance itself as the problem (not an ideal answer, but probably acceptable)

Problem: the policy type C estimate from the GLM is totally unreliable due to the high p-value and low exposures.

Alternative approach: use the relativity from another source, such as a large neighboring state or countrywide, or even competitor or industry data since those relativities should be based on enough exposures to be be statistically reliable.
