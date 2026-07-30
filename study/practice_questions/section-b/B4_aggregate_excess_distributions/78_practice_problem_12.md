---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 12 - Fisher Chapter 3 Q11
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 12
revised: false
points: null
parts: [a, b]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 12
---

# Practice Problem 12 - Fisher Chapter 3 Q11

## Question

Assume the following information for a retrospectively rated insured:

| B | C |
| --- | --- |
| $300,000 | Basic premium |
| $100,000 | Excess loss premium |
| 1.1 | Loss conversion factor |
| 1.05 | Tax multiplier |
| $100,000 | Accident limit |
| $650,000 | Minimum premium |

### Part a

If the insured has small losses in a year totaling to:

$150,000 — Total of small losses in a year

What is the retro premium for the insured?

### Part b

If the insured has 1 large loss in a year totaling to:

$150,000 — Amount of large loss

What is the retro premium for the insured?

## Solution

In all parts of this problem, I'll assume the retro formula used is:

R = (B + cL_D + excess loss premium)T In other words, since the excess loss premium is given separately from the basic premium, I'll assume it is not included as part of the basic premium. This is how the NCCI retro plan works.

### Part a

R — $650,000 — `=MAX(B11,(B6+B7+B8*B16)*B9)` — floored by the minimum premium

### Part b

R — $650,000 — `=MAX(B11,(B6+B7+B8*MIN(B23,B10))*B9)` — floored by the minimum premium

The last case is an example of the "underlap" between the effects of the minimum premium and the accident limit. In some years, even though there are large accidents, the accident limit will not provide any benefit to the insured due to the minimum premium. This has a relatively small overall impact.
