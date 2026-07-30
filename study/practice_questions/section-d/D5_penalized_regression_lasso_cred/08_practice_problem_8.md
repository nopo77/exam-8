---
tia_section: D5
tia_topic: penalized_regression_lasso_cred
title: Practice Problem 8
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 8
revised: false
points: null
parts: [a, b, c, d, e]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [holmes_&_casotto/]
source_workbook: tia_excel/section-d/D_5_Penalized_Regression_Lasso_Cred_practice_solutions.xlsx
source_sheet: Practice Problem 8
---

# Practice Problem 8

## Question

An actuary has fit a GLM to model personal auto pure premiums. The model uses a log link function. One of the variables in the model is Vehicle_Age_Group, which is treated as a categorical variable with "0-4 years" as the base level.

The output for the intercept and the Vehicle_Age_Group coefficients is as follows:

| Variable | Coefficient |
| --- | --- |
| Intercept | 6.20 |
| Vehicle_Age_Group: 5-9 years | -0.10 |
| Vehicle_Age_Group: 10-14 years | -0.18 |
| Vehicle_Age_Group: 15+ years | -0.25 |

The actuary wants to restructure the model by converting the Vehicle_Age_Group variable into an equivalent ordinal variable. The new ordinal structure will have a new intercept and three new coefficients for the following three stepwise indicator variables:

- Age_Step_5+: Is 1 if the vehicle age is 5 years or older, 0 otherwise.
- Age_Step_10+: Is 1 if the vehicle age is 10 years or older, 0 otherwise.
- Age_Step_15+: Is 1 if the vehicle age is 15 years or older, 0 otherwise.

### Part a

For the new ordinal model to be equivalent to the original categorical model (i.e., produce the exact same prediction for every age group), what are the required values for the new intercept and the new ordinal coefficients?

### Part b

If this variable was changed from categorical to ordinal for a penalized regression model, would the new model give the exact same predictions as before? Explain your answer.

### Part c

The vehicle age variable could be used as a categorical variable, an ordinal variable, or a continuous variable in a regular GLM. Discuss the pros and cons of each approach.

### Part d

Discuss how your answer to part (c) would change if you were using a ridge penalized regression model instead of a GLM.

### Part e

Discuss how your collective answers to parts (c) and (d) combined would change if you were using a lasso credibility model instead of a GLM or a ridge regression model.

## Solution

None of this is stated directly in the source text, but this is all within the realm of an exam question in my opinion.

### Part a

The presence of any other variables in the model is irrelevant to this answer. To get the same predictions, we want the value of the linear predictor to remain the same for each vehicle age group. We can calculate the existing values of the linear predictor, and set up equations for the new values using the new coefficients. Then we can solve those equations.

| Vehicle Age Group | Categorical Linear Predictor |
| --- | --- |
| 0-4 | 6.20 |
| 5-9 | 6.10 |
| 10-14 | 6.02 |
| 15+ | 5.95 |

<details><summary>Formulas</summary>

- `J10` = `=C10`
- `J11` = `=C$10+C11`
- `J12` = `=C$10+C12`
- `J13` = `=C$10+C13`

</details>

| I | J | K |
| --- | --- | --- |
| Ordinal Group | Coefficient | Ordinal Linear Predictor |
| 0-4 | c0 | c0 = 6.20 |
| 5+ | c1 | c0+c1 = 6.10 |
| 10+ | c2 | c0+c1+c2 = 6.02 |
| 15+ | c3 | c0+c1+c2+c3 = 5.95 |

| Variable |   | New Coefficient |
| --- | --- | --- |
| New Intercept | c0 | 6.20 |
| Age_Step_5+ | c1 | -0.10 |
| Age_Step_10+ | c2 | -0.08 |
| Age_Step_15+ | c3 | -0.07 |

<details><summary>Formulas</summary>

- `K22` = `=J10`
- `K23` = `=J11-K22`
- `K24` = `=J12-SUM(K22:K23)`
- `K25` = `=J13-SUM(K22:K24)`

</details>

### Part b

No, the predictions would be different. The lower ordinal groups (e.g., 5+) would have more observations than the corresponding categorical groups (e.g, 5-9), so those groups would receive less of a penalty compared to the categorical equivalent levels. This would mean the lower categorical groups would have their coefficients likely be closer to 0 compared to the corresponding ordinal groups. Also, the larger groupings for ordinal variables could potentially understate the differences between levels.

### Part c

Remember this part is only about a traditional GLM, so any references to credibility aren't really relevant here.

Categorical Pros: most flexible to fit non-linear patterns in the data, more consistent with a typical rating variable for vehicle age, easiest to interpret

Categorical Cons: ages must be grouped prior to modeling, grouping is judgmental, estimates don't consider ordering of ages so may be counterintuitive, if groups are too granular it can lead to unstable estimates/overfitting, may require lots of degrees of freedom if lots of levels

Continuous Pros: gives smooth predictions, can incorporate feature engineering for more flexibility, uses fewest degrees of freedom

Continuous Cons: forces the same pattern to fit all age levels, difficult to interpret without a graph (especially if transformations used), transformations are judgmental, polynomial terms (if used) can will have high correlations with each other which can cause problems, may not extrapolate well to tail levels with low exposures

Ordinal Pros: good balance between smooth estimates (like continuous variables) vs. flexibility for different patterns (like categorical variables), insignificant steps get grouped with adjacent levels instead of the base level, less need to group ages prior to modeling, balance between continuous and categorical for degrees of freedom used, no need for feature engineering

Poor answers for ordinal pros in this part would be that ordinal variables don't have to be numeric (since vehicle age is numeric), and how they can help us choose an optimal penalty parameter since there is no penalty in regular GLMs.

Ordinal Cons: less easy to interpret coefficients directly since not consistent with traditional rating plan levels.

### Part d

The changes would be:

1. Polynomial term correlation would be less of an issue for continuous variables since some of them may be highly penalized.

2. An additional ordinal pro would be that reviewing the estimate patterns could help select an optimal penalty parameter for the model.

3. An additional ordinal con would be that the penalty would have a greater influence on higher ages than lower ages since lower ages would have more observations.

### Part e

The changes would be:

1. Using a complement of credibility with categorical and ordinal levels would be more consistent with traditional credibility-weighting

since they use magnitudes (instead of slopes for continuous variables).

2. There would be less of a need to group categorical (and maybe ordinal) levels if the ungrouped levels have good complements of credibility.

3. An additional continuous con would be that the same credibility would apply to all levels of the variable, even though the exposures may vary significantly by level.
