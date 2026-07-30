---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 15 - Fisher Chapter 3 Q14b
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 15
revised: false
points: null
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 15
---

# Practice Problem 15 - Fisher Chapter 3 Q14b

## Question

A policy has:

- A continuous uniform unlimited loss distribution from
- A continuous uniform limited loss distribution from
- An entry ratio of 1.5 times the expected unlimited loss

Calculate the value of

φ*_D(1.5), the Table L charge at the entry ratio ψ*_D(1.5), the Table L savings at the entry ratio

| F | G | H |
| --- | --- | --- |
| 0 | to | 500 |
| 0 | to | 400 |

## Solution

**E[A]:** 250 — `=AVERAGE(F6,H6)`

There are multiple ways to calculate this solution. Building a Table L will not be accurate since this is a continuous distribution. I'll show 1 approach.

Distributions in terms of entry ratios:

| B | D | E | F |
| --- | --- | --- | --- |
| Unlimited uniform on: | 0 | to | 2 |
| Limited uniform on: | 0 | to | 1.6 |

<details><summary>Formulas</summary>

- `D22` = `=F6/D$16`
- `F22` = `=H6/D$16`
- `D23` = `=F7/D$16`
- `F23` = `=H7/D$16`

</details>

The charge will be 1 - E[r_D;1.5] The savings will be 1.5 - E[r_D;1.5]

**E[r_D;1.5]:** 0.796875 — `=(1.5/F23)*AVERAGE(D23,1.5)+(1-1.5/F23)*1.5`

| B | D | F |
| --- | --- | --- |
| Table L charge at 1.5 | 0.203125 |  |
| Table L savings at 1.5 | 0.703125 | Alternatively: |

<details><summary>Formulas</summary>

- `D30` = `=1-D28`
- `D31` = `=1.5-D28`

</details>

0.703125 — `=D30+1.5-1`
