---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2007 Exam 9 - Q33 revised
source: past_exam
exam_year: 2007
exam_sitting: null
exam_number: 9
question_number: 33
practice_number: null
revised: true
points: 3.0
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2007 Exam 9 - Q33 revised
---

# 2007 Exam 9 - Q33 revised

**Points:** 3

## Question

A large dollar deductible workers compensation policy requires the insured to reimburse the insurer for each occurrence up to $250,000, subject to an aggregate reimbursement of $1,200,000. The following also apply to this policy:

| B | C |
| --- | --- |
| $1,000,000 | Standard Premium |
| 0.900 | Hazard Group Relativity |
| 75% | Expected Unlimited Loss Ratio |
| 20% | Excess Ratio |

Table MD : Limited Insurance Charges with D = 250,000

| B | C | D | E | F |
| --- | --- | --- | --- | --- |
| Entry Ratio | 1.0 | 1.5 | 2.0 | 2.5 |
| Insurance Charge | 0.250 | 0.110 | 0.040 | 0.022 |

Table of Expected Loss Ranges

| Expected Loss Group | Expected Losses |
| --- | --- |
| 31 | 630,000 - 720,000 |
| 30 | 720,001 - 830,000 |
| 29 | 830,001 - 990,000 |
| 28 | 990,001 - 1,180,000 |
| 27 | 1,180,001 - 1,415,000 |

Table M: Unlimited Insurance Charges

Expected Loss Group

| B | C | D | E | F | G |
| --- | --- | --- | --- | --- | --- |
| Entry Ratio | 31 | 30 | 29 | 28 | 27 |
| 0.5 | 0.415 | 0.407 | 0.399 | 0.391 | 0.383 |
| 1.0 | 0.386 | 0.378 | 0.369 | 0.361 | 0.352 |
| 1.5 | 0.287 | 0.276 | 0.266 | 0.256 | 0.245 |
| 2.0 | 0.263 | 0.252 | 0.242 | 0.231 | 0.220 |

### Part a (1.00 pts)

Use the Limited Table M approach to calculate the Insurance Charge in dollars.

### Part b (2.00 pts)

Use the ICRLL procedure to calculate the total expected loss cost for this policy.

## Solution

### Part a

| K | L |
| --- | --- |
| E[A] | $750,000 |
| E[A_D] | $600,000 |

<details><summary>Formulas</summary>

- `L2` = `=B10*B8`
- `L3` = `=(1-B11)*L2`

</details>

**r*_G:** 2.00 — `=1200000/L3`

| K | L |
| --- | --- |
| Charge(r*_G) | 0.040 |
| Charge in dollars | $24,000 |

<details><summary>Formulas</summary>

- `L7` = `=E15`
- `L8` = `=L7*L3`

</details>

### Part b

Adjusted Expected Loss — $978,750 — `=L2*B9*(1+0.8*B11)/(1-B11)` — --> Lookup ELG 29

**Charge(r*_G):** 0.242 — `=E31`

**Total loss cost:** $295,200 — `=(L2-L3)+L12*L3`
