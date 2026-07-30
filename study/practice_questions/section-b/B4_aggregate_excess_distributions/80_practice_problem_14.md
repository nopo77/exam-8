---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 14 - Fisher Chapter 3 Q13
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 14
revised: false
points: null
parts: [a, b, c]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 14
---

# Practice Problem 14 - Fisher Chapter 3 Q13

## Question

You are given the following table of insurance charges, by per-occurrence deductible:

| r | $100,000 deductible | $200,000 deductible |
| --- | --- | --- |
| 1.0 | 0.20 | 0.22 |
| 1.5 | 0.10 | 0.12 |
| 2.0 | 0.04 | 0.05 |
| 2.5 | 0.02 | 0.03 |

| B | C |
| --- | --- |
| $40,000 | Expected unlimited losses |
| $20,000 | Expected primary losses at a per-occurrence limit of $100,000 |
| $30,000 | Expected primary losses at a per-occurrence limit of $200,000 |

### Part a

A policy has a $100,000 per-occurrence deductible and a $40,000 aggregate deductible limit. Find the cost of the $40,000 aggregate deductible limit.

### Part b

Find the cost of the $40,000 aggregate deductible limit if the policy had a $200,000 per- occurrence deductible. (Use linear interpolation in the table, if necessary.)

### Part c

Which policy will the insurer charge more for? Why?

## Solution

### Part a

r* at 40k Limited Table M Charge

Insurance Charge

### Part b

r* at 40k

Limited Table M Charge

Insurance Charge

### Part c

The total policy expected losses would be the per-occurrence excess plus the aggregate excess.

Part (a) total expected loss in excess of deductibles Part (b) total expected loss in excess of deductibles

The insurer will charge more for the policy in part (a) because the larger per-occurrence excess losses in excess of $100k vs $200k (20k vs 10k) outweighs the lower insurance charge (800 vs 4600).

2.0 — `=40000/B14` — Divide by expected limited loss for Limited Table M

0.04 — `=C9`

$800 — `=K4*B14`

1.33 — `=40000/B15`

0.153 — `=FORECAST(K8,D7:D8,B7:B8)` — use linear interpolation

$4,600 — `=K10*B15`

$20,800 — `=K6+(B13-B14)`

$14,600 — `=K12+(B13-B15)`
