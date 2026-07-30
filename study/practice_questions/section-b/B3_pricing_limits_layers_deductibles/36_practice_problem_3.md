---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 3
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 3
revised: false
points: null
parts: [a, b, c]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: Practice Problem 3
---

# Practice Problem 3

## Question

Suppose ground-up claim severity is uniformly distributed on [a,b] as follows:

| B | C |
| --- | --- |
| $0 | a for uniform distribution |
| $10,000 | b for uniform distribution |

### Part a

Given the following:

| B | C |
| --- | --- |
| $1,000 | Basic limit |
| $5,000 | Increased limit |
| 20% | ALAE as a % of Loss |

Assume that limits do not apply to ALAE.

Calculate the increased limit factor for a limit of $5,000.

### Part b

Given the following:

| B | C |
| --- | --- |
| $1,000 | Basic limit |
| $5,000 | Increased limit |
| $1,000 | Average ALAE regardless of limit |

Assume that limits do not apply to ALAE.

Calculate the increased limit factor for a limit of $5,000.

### Part c

You are additionally given:

| B | C |
| --- | --- |
| 1.8 | Loss Cost Multiplier (LCM) |
| 2 | Parameter for Poisson distribution for ground-up claim counts |
| $1,000 | Bottom of layer |
| $5,000 | Top of layer |
| $1,000 | Average ALAE regardless of limit |

Assume that limits do not apply to ALAE.

Calculate the premium for the layer between $1,000 and $5,000.

## Solution

### Part a

| l | F(l) | E[X;l] | w/ALAE |
| --- | --- | --- | --- |
| $1,000 | 0.1 | $950 | $1,140 |
| $5,000 | 0.5 | $3,750 | $4,500 |

<details><summary>Formulas</summary>

- `J3` = `=B12`
- `K3` = `=J3/$B$7`
- `L3` = `=K3*J3/2+(1-K3)*J3`
- `M3` = `=L3*(1+$B$14)`
- `J4` = `=B13`
- `K4` = `=J4/$B$7`
- `L4` = `=K4*J4/2+(1-K4)*J4`
- `M4` = `=L4*(1+$B$14)`

</details>

**I(5k):** 3.947 — `=M4/M3`

### Part b

**I(5k):** 2.436 — `=(L4+B25)/(L3+B25)`

### Part c

The text discusses 2 ways to solve this, though 1 is technically wrong.

Solution 1: Using the layer formula (inaccurate when ALAE additive)

**P basic:** $7,020 — `=B34*B35*(L3+B38)`

**P for layer:** $10,080 — `=M14*(M8-1)`

Solution 2: Using the technically correct formula for additive ALAE (that assumes a portion is eliminated for claims below the layer)

**P for layer:** $13,320 — `=B34*B35*(L4-L3+(1-K3)*B38)`

Note this is quite different from the other solution, since the other solution effectively omits ALAE (and the loading applied to it using the LCM).
