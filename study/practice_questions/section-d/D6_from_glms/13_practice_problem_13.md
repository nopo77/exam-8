---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 13
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 13
revised: false
points: 2.0
parts: [a, b, c]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [chalk_et_al/]
source_workbook: tia_excel/section-d/D_6_From_GLMs_practice_solutions.xlsx
source_sheet: Practice Problem 13
---

# Practice Problem 13

**Points:** 2

## Question

An actuary is building a Poisson GLM with a log link function for pet-insurance claim frequency. Dog breed, a high cardinality categorical variable, will be incorporated using target encoding. Cross-validation has selected λ = 5. The training data is summarized below.

5 — Penalty parameter λ

| Dog Breed | Exposures | Claim Counts |
| --- | --- | --- |
| Labrador | 100 | 10 |
| Bulldog | 50 | 9 |
| Poodle | 25 | 2 |
| Dachshund | 16 | 1 |
| Mastiff | 8 | 2 |
| Chihuahua | 1 | 0 |
| Total | 200 | 24 |

### Part a (1.25 pts)

Calculate the multiplicative target-encoded value x'_k for each dog breed.

### Part b (0.50 pts)

Suppose that instead of using the global mean for target encoding, a GLM is first built without the dog breed variable, and those predictions are used for target encoding the dog breed variable.

0.15 — The average predicted claim frequency for Bulldogs from the GLM without dog breed

Calculate the multiplicative target-encoded value x'_k for Bulldogs using this approach. Assume the penalty parameter remains λ = 5.

### Part c (0.25 pts)

Briefly discuss the advantage of using the approach in part (b) compared to using the global mean for target encoding.

## Solution

### Part a

| Breed | Avg freq | AvE | Z_k | x'_k |
| --- | --- | --- | --- | --- |
| Labrador | 0.10 | 0.83 | 0.95 | 0.84 |
| Bulldog | 0.18 | 1.50 | 0.91 | 1.45 |
| Poodle | 0.08 | 0.67 | 0.83 | 0.72 |
| Dachshund | 0.06 | 0.52 | 0.76 | 0.63 |
| Mastiff | 0.25 | 2.08 | 0.62 | 1.67 |
| Chihuahua | 0.00 | 0.00 | 0.17 | 0.83 |
| Total | 0.12 |  |  |  |

<details><summary>Formulas</summary>

- `K3` = `=B11`
- `L3` = `=D11/C11`
- `M3` = `=L3/L$9`
- `N3` = `=C11/(C11+B$8)`
- `O3` = `=N3*M3+(1-N3)*1`
- `K4` = `=B12`
- `L4` = `=D12/C12`
- `M4` = `=L4/L$9`
- `N4` = `=C12/(C12+B$8)`
- `O4` = `=N4*M4+(1-N4)*1`
- `K5` = `=B13`
- `L5` = `=D13/C13`
- `M5` = `=L5/L$9`
- `N5` = `=C13/(C13+B$8)`
- `O5` = `=N5*M5+(1-N5)*1`
- `K6` = `=B14`
- `L6` = `=D14/C14`
- `M6` = `=L6/L$9`
- `N6` = `=C14/(C14+B$8)`
- `O6` = `=N6*M6+(1-N6)*1`
- `K7` = `=B15`
- `L7` = `=D15/C15`
- `M7` = `=L7/L$9`
- `N7` = `=C15/(C15+B$8)`
- `O7` = `=N7*M7+(1-N7)*1`
- `K8` = `=B16`
- `L8` = `=D16/C16`
- `M8` = `=L8/L$9`
- `N8` = `=C16/(C16+B$8)`
- `O8` = `=N8*M8+(1-N8)*1`
- `K9` = `=B17`
- `L9` = `=D17/C17`

</details>

### Part b

| K | M |
| --- | --- |
| New Bulldog AvE | 1.20 |
| New Bulldog x'_k | 1.18 |

<details><summary>Formulas</summary>

- `M11` = `=L4/B26`
- `M12` = `=N4*M11+(1-N4)*1`

</details>

### Part c

By using the initial GLM predictions, the encoding only captures the dog breed signal not already accounted for by the other features in the GLM.

You could also say this could help bring any outlier HCCV AvE levels more in line with the more common HCCV levels if correlated variables partially account for the unique aspects of those levels. e.g., the helicopter examples in the source paper aircraft model
