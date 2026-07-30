---
tia_section: D3
tia_topic: glm
title: Practice Problem 2
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 2
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
source_sheet: Practice Problem 2
---

# Practice Problem 2

## Question

Suppose you are the analyst creating a Generalized Linear Model for a rating plan, and you want to include the deductible relativities that you have estimated from a separate analysis into your pure premium model. Below are the estimated deductible relativities and the deductibles for several observations from the modeling dataset.

| Deductible | Relativity |
| --- | --- |
| $250 | 1.25 |
| $500 | 1.00 |
| $1,000 | 0.92 |
| $2,500 | 0.78 |

| B | C |
| --- | --- |
| $500 | Deductible for observations 1 and 4 |
| $1,000 | Deductible for observation 2 |
| $250 | Deductible for observation 3 |

- The model has a log link function.

Calculate the appropriate offset term for each of the 4 observations.

## Solution

| Observation | Offset |
| --- | --- |
| 1 | 0 |
| 2 | -0.083 |
| 3 | 0.223 |
| 4 | 0 |

<details><summary>Formulas</summary>

- `C24` = `=LN(C11)`
- `C25` = `=LN(C12)`
- `C26` = `=LN(C10)`
- `C27` = `=LN(C11)`

</details>
