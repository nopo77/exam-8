---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2010 Exam 9 - Q24 revised
source: past_exam
exam_year: 2010
exam_sitting: null
exam_number: 9
question_number: 24
practice_number: null
revised: true
points: 3.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2010 Exam 9 - Q24 revised
---

# 2010 Exam 9 - Q24 revised

**Points:** 3

## Question

An insurance company is considering a large dollar deductible policy with the following underlying parameters:

| Deductible Amount | Excess Ratio |   | Policy Value |
| --- | --- | --- | --- |
| $25,000 | 0.500 | Expected Ground-Up Loss | $500,000 |
| $50,000 | 0.350 | Deductible | $100,000 |
| $100,000 | 0.200 | Aggregate Limit | $1,000,000 |
| $250,000 | 0.125 |  |  |

Limited Table M Charges

Deductible Amount

| B | C | D | E | F |
| --- | --- | --- | --- | --- |
| Entry Ratio | 25,000 | 50,000 | 100,000 | 250,000 |
| 2.0 | 0.067 | 0.073 | 0.08 | 0.088 |
| 2.1 | 0.053 | 0.058 | 0.065 | 0.072 |
| 2.2 | 0.039 | 0.044 | 0.05 | 0.057 |
| 2.3 | 0.03 | 0.034 | 0.04 | 0.046 |
| 2.4 | 0.021 | 0.025 | 0.03 | 0.036 |
| 2.5 | 0.017 | 0.02 | 0.025 | 0.03 |
| 2.6 | 0.013 | 0.016 | 0.02 | 0.025 |
| 2.7 | 0.011 | 0.014 | 0.017 | 0.022 |
| 2.8 | 0.01 | 0.012 | 0.015 | 0.019 |
| 2.9 | 0.009 | 0.011 | 0.014 | 0.017 |
| 3.0 | 0.008 | 0.01 | 0.013 | 0.016 |

Due to bad data, the company's actuary incorrectly uses the expected ground-up loss below to determine the insurance charge:

$462,500 — Incorrectly used expected ground-up loss

Calculate the percentage by which the insurance charge (dollars) will be inadequate.

## Solution

**XS ratio:** 0.200 — `=C10`

Using correct Expected Ground-Up Loss:

| J | L |
| --- | --- |
| E[A_D] | $400,000 |
| r*_G | 2.5 |

<details><summary>Formulas</summary>

- `L8` = `=F8*(1-K5)`
- `L9` = `=F10/L8`

</details>

Charge: — 0.025 — `=E21` — $10,000 — `=L11*L8`

Using incorrect Expected Ground-Up Loss:

| J | L |
| --- | --- |
| E[A_D] | $370,000 |
| r*_G | 2.70 |

<details><summary>Formulas</summary>

- `L14` = `=(1-K5)*B30`
- `L15` = `=F10/L14`

</details>

Charge: — 0.017 — `=E23` — $6,290 — `=L17*L14`

The inadequacy should be relative to the correct charge.

**Inadequacy:** 37.1% — `=(M11-M17)/M11`
