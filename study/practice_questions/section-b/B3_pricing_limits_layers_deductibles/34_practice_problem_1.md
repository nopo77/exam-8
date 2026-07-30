---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 1
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 1
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
source_sheet: Practice Problem 1
---

# Practice Problem 1

## Question

Given the following information:

Ground-up claim severity is uniformly distributed on [a,b] as follows:

| B | C |
| --- | --- |
| $0 | a for uniform severity distribution |
| $5,000 | b for uniform severity distribution |
| $1,000 | Basic per-claim limit |
| $500 | Average ALAE regardless of limit |

Limits/deductibles do not apply to ALAE.

### Part a

$250 — Calculate the loss elimination ratio for a $250 straight deductible.

### Part b

$250 — Calculate the loss elimination ratio for a $250 franchise deductible.

### Part c

Given the following additional information:

10% — Inflation trend for ground-up claim severity

Estimate the impact of the trend net of a $250 straight deductible and capped by the basic per-claim limit.

## Solution

### Part a

| K | M |
| --- | --- |
| F(250) | 0.05 |
| F(1000) | 0.2 |

<details><summary>Formulas</summary>

- `M2` = `=B16/B9`
- `M3` = `=B10/B9`

</details>

| K | M |
| --- | --- |
| E[X;250] | $243.75 |
| E[X;1000] | $900 |

<details><summary>Formulas</summary>

- `M5` = `=M2*B16/2+(1-M2)*B16`
- `M6` = `=M3*B10/2+(1-M3)*B10`

</details>

**LER:** 0.192 — `=(M5+M2*B11)/(M6+B11)`

### Part b

Here we can use the numbers from part (a).

**LER:** 0.022 — `=(M5-B19*(1-M2)+M2*B11)/(M6+B11)`

### Part c

I'll assume the question is talking about the impact of inflation on aggregate losses in the layer, since that is what is typically asked for on the exam.

| l | F(l) | E[X;l] |
| --- | --- | --- |
| $227.27 | 0.045 | $222.11 |
| $909.09 | 0.182 | $826.45 |

<details><summary>Formulas</summary>

- `K18` = `=B16/(1+$B$24)`
- `L18` = `=K18/$B$9`
- `M18` = `=L18*K18/2+(1-L18)*K18`
- `K19` = `=B10/(1+$B$24)`
- `L19` = `=K19/$B$9`
- `M19` = `=L19*K19/2+(1-L19)*K19`

</details>

**Tau_S - 1:** 5.2% — `=(1+B24)*(M19-M18+(1-L18)*B11)/(M6-M5+(1-M2)*B11) - 1`
