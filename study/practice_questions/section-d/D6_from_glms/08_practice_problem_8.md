---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 8
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 8
revised: false
points: 2.25
parts: [a, b, c, d]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [chalk_et_al/]
source_workbook: tia_excel/section-d/D_6_From_GLMs_practice_solutions.xlsx
source_sheet: Practice Problem 8
---

# Practice Problem 8

**Points:** 2.25

## Question

A commercial auto book is rated by class code, with about 400 codes, too many to fit as separate GLM levels. An actuary encodes each class as a shrunken claim frequency: the class's claim count plus m times the overall book frequency, divided by the class's car-years plus m. The encoded value then enters a log-link frequency GLM as ln of the class's encoded frequency divided by the overall frequency, with fitted intercept -2.8134 and fitted coefficient 0.85 on that feature. Data for four class codes is shown.

| Class code | Earned car-years | Claim count |
| --- | --- | --- |
| G41 | 5,000 | 390 |
| H72 | 1,200 | 54 |
| K18 | 150 | 15 |
| M09 | 40 | 1 |

| B | C |
| --- | --- |
| 0.0600 | Overall book frequency (claims per car-year) |
| 500 | Shrinkage parameter m (car-years) |
| -2.8134 | Fitted intercept |
| 0.85 | Fitted coefficient on the encoded feature |

### Part a (0.75 pts)

Calculate the encoded frequency for each of the four class codes.

### Part b (0.50 pts)

Calculate the GLM's predicted frequency for a class K18 risk.

### Part c (0.50 pts)

The fitted coefficient on the encoded feature is 0.85 rather than 1. Explain what a coefficient below 1 does to the encoded relativities, and briefly state why the fit chooses it.

### Part d (0.50 pts)

Describe how target leakage arises in this construction, and one modification that prevents it.

## Solution

### Part a

Each class's raw frequency is blended with the overall frequency, with m playing the role of car-years of prior weight. The formula used here is given in words in the setup of the question.

| Class | Encoded Freq |
| --- | --- |
| G41 | 0.0764 |
| H72 | 0.0494 |
| K18 | 0.0692 |
| M09 | 0.0574 |

<details><summary>Formulas</summary>

- `K6` = `='[1]Practice Problem 8'!B15`
- `L6` = `=(D15+$B$21*$B$20)/(C15+$B$21)`
- `K7` = `='[1]Practice Problem 8'!B16`
- `L7` = `=(D16+$B$21*$B$20)/(C16+$B$21)`
- `K8` = `='[1]Practice Problem 8'!B17`
- `L8` = `=(D17+$B$21*$B$20)/(C17+$B$21)`
- `K9` = `='[1]Practice Problem 8'!B18`
- `L9` = `=(D18+$B$21*$B$20)/(C18+$B$21)`

</details>

### Part b

Here we have to assume there are no other variables in the model since no information is given about them. The systematic equation is ln(y) = intercept + beta_te * ln(x'_k), so the predicted y = exp(intercept + beta_te * ln(x'_k)). You could also express this as: y = exp(intercept) * exp(beta_te * ln(x'_k)) = exp(intercept) * x'_k^beta_te

| K | O | Q | S |
| --- | --- | --- | --- |
| Encoded feature (x'_k) for K18: | 1.1538 |  |  |
| ln(x'_k) for K18: | 0.1431 |  |  |
| Predicted freq: | 0.0678 | alternate calc: | 0.0678 |

<details><summary>Formulas</summary>

- `O15` = `=L8/B20`
- `O16` = `=LN(O15)`
- `O17` = `=EXP(B22+B23*O16)`
- `S17` = `=EXP(B22)*O15^B23`

</details>

### Part c

A coefficient below 1 dampens every encoded relativity toward 1.

E.g., for K18: — from — 1.1538 — `=O15` — to — 1.1293 — `=O15^B23`

The fit chooses it because the encoded values are still noisy estimates of each class's true frequency, and trusting them at less than face value predicts better; the coefficient acts as a second, global layer of shrinkage on top of m.

### Part d

Each class's encoding is computed from the same claims the model is then trained and validated on, so the target has leaked into a predictor: a thin class that happened to have a bad year gets a high encoding, and the model appears to predict that class's experience when it is really reading it back, inflating apparent performance and biasing the chosen m toward too little shrinkage. The fix is out-of-fold encoding: compute each fold's encodings using only the other folds' data the row level), so no observation's own outcome enters the feature it is scored on.
