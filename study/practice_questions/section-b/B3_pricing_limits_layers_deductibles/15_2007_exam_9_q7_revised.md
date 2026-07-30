---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2007 Exam 9 - Q7 revised
source: past_exam
exam_year: 2007
exam_sitting: null
exam_number: 9
question_number: 7
practice_number: null
revised: true
points: 2.0
parts: []
good_problem: true
has_images: true
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2007 Exam 9 - Q7 revised
---

# 2007 Exam 9 - Q7 revised

**Points:** 2

## Question

A collection of general liability policies has the following properties:

| B | C |
| --- | --- |
| 11.1% | Annual severity trend that impacts each loss uniformly |
| $4,000 | 2007 expected value pure premium for a $1,000,000 excess of $500,000 contract |
| $250,000 | 2007 basic limit |

- The 2006 increased limits table, where I(K) represents the ILF at limit K, is given by:

| K | I(K) |
| --- | --- |
| 225,000 | 0.94 |
| 250,000 | 1.00 |
| 450,000 | 1.40 |
| 500,000 | 1.48 |
| 900,000 | 1.90 |
| 1,000,000 | 1.96 |
| 1,350,000 | 2.15 |
| 1,500,000 | 2.18 |

Calculate the 2007 basic limits pure premium for this collection of policies.

## Solution

Solution 1: Calculate 2007 basic limit PP as 2007 PP for 1M xs 500k layer / (2007 ILF for 1.5M - 2007 ILF for 500k)

| l | l/tau | I_2006(l/tau) | I_2007(l) |
| --- | --- | --- | --- |
| $250,000 | $225,023 | 0.94 |  |
| $500,000 | $450,045 | 1.40 | 1.489 |
| $1,500,000 | $1,350,135 | 2.15 | 2.287 |

<details><summary>Formulas</summary>

- `J6` = `=B8`
- `K6` = `=J6/(1+$B$6)`
- `L6` = `=C13`
- `K7` = `=J7/(1+$B$6)`
- `L7` = `=C15`
- `M7` = `=L7/L6`
- `J8` = `=J7+1000000`
- `K8` = `=J8/(1+$B$6)`
- `L8` = `=C19`
- `M8` = `=L8/L6`

</details>

**2007 basic limit PP:** $5,013.33 — `=B7/(M8-M7)`

Solution 2: Calculate 2007 basic limit PP as 2006 basic limit PP * inflation for basic PP

![solution image](images/img_1ee2b80bc15b.png)

**tau_S for 1M xs 500k:** 1.190 — `=(1+B6)*(C19-C15)/(C20-C16)`

**2006 PP for 1M xs 500k:** $3,360.34 — `=B7/N20`

**2006 basic limit PP:** $4,800.48 — `=N22/(C20-C16)`

**basic limit inflation = tau_S for 250k xs 0:** 1.044 — `=(1+B6)*(C13/C14)`

**2007 basic limit PP:** $5,013.33 — `=N24*N26`
