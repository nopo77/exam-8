---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 4
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 4
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
source_sheet: Practice Problem 4
---

# Practice Problem 4

**Points:** 2

## Question

An actuary is building a personal auto claim frequency GLM on standardized predictors and compares four fits: (1) unpenalized, (2) ridge with lambda = 1.5, (3) LASSO with lambda = 0.8, and

(4) an elastic net with alpha = 0.4 and lambda = 2. Each model has an intercept term.

The fitted coefficients and the deviance statistics on the training and validation sets are shown; a coefficient of 0.00 means the variable was removed exactly.

Standardized coefficients

| Variable | Unpenalized | Ridge | LASSO | Elastic net |
| --- | --- | --- | --- | --- |
| Driver age | 0.42 | 0.30 | 0.34 | 0.32 |
| Vehicle age | -0.18 | -0.12 | 0.00 | -0.08 |
| Territory density | 0.35 | 0.26 | 0.27 | 0.25 |
| Prior claims | 0.28 | 0.21 | 0.19 | 0.20 |

| Fit | Training deviance | Validation deviance |
| --- | --- | --- |
| Unpenalized | 41,250 | 42,900 |
| Ridge | 41,830 | 42,410 |
| LASSO | 41,760 | 42,350 |
| Elastic net | 41,780 | 42,380 |

| B | C |
| --- | --- |
| 1.5 | Lambda for the ridge fit |
| 0.8 | Lambda for the LASSO fit |
| 2.0 | Lambda for the elastic net fit |
| 0.4 | Alpha for the elastic net fit |

### Part a (0.50 pts)

Calculate the penalty term of the ridge fit and the penalty term of the LASSO fit.

### Part b (0.50 pts)

Calculate the penalty term of the elastic net fit.

### Part c (0.50 pts)

Recommend which of the four fits to implement, and briefly justify using the deviance statistics.

### Part d (0.50 pts)

Briefly describe two advantages of the LASSO penalty over the ridge penalty when the model will be filed as a rating plan.

## Solution

### Part a

The ridge penalty is lambda (or lambda/2) times the sum of squared coefficients; the LASSO penalty is lambda times the sum of absolute coefficients. The intercept is excluded from both.

Ridge penalty LASSO penalty

Note: penalty conventions vary across texts. Some write the ridge penalty as lambda/2 times the sum of squares, others like monograph 16 just use lambda times the sum of squares.

### Part b

Here we need to use the elastic net coefficients. The alpha is the weight given to the LASSO penalty, with the complement given to the ridge penalty. Note that while elastic net is a combination of ridge and LASSO penalties, it estimates its own coefficients, so it would not be appropriate to use the ridge and LASSO coefficients used in part (a) for this part.

Elastic net penalty

### Part c

Lowest validation deviance Implement the LASSO fit, which has the lowest validation deviance.

Note the training deviance is irrelevant since performance on training data won't necessarily generalize well.

### Part d

Any two of:

- The LASSO can set coefficients exactly to zero, so the filed plan contains fewer variables and is simpler to explain, implement,

and support.

- Variable selection is automatic and built into the fit, rather than requiring a separate manual pruning step.
- Fewer rating variables means fewer data elements to collect, verify, and maintain in production.

0.3241 — `=B23*SUMSQ(D12:D15)` — OR — 0.1621 — `=B23/2*SUMSQ(D12:D15)`

0.6400 — `={B24*SUM(ABS(E12:E15))}`

0.9336 — `={B25*(B26*SUM(ABS(F12:F15))+(1-B26)*SUMSQ(F12:F15))}` — OR — 0.8068 — `={B25*(B26*SUM(ABS(F12:F15))+(1-B26)*SUMSQ(F12:F15)/2)}`

42,350 — `=MIN($D$18:$D$21)`
