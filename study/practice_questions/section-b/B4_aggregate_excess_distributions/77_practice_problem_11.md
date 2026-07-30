---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 11 - Fisher Chapter 3 Q10
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 11
revised: false
points: null
parts: [a, b, c, d]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 11
---

# Practice Problem 11 - Fisher Chapter 3 Q10

## Question

Assume the following information for a retrospectively rated insured:

| B | C |
| --- | --- |
| $30,000 | Basic premium |
| $10,000 | Excess loss premium |
| 1.1 | Loss conversion factor |
| 1.05 | Tax multiplier |
| $100,000 | Accident limit |
| $250,000 | Maximum premium |

### Part a

If the insured has small losses in a year totaling to:

$150,000 — Total of small losses in a year

What is the retro premium for the insured?

### Part b

If the insured has small losses in a year totaling to:

$200,000 — Total of small losses in a year

What is the retro premium for the insured?

### Part c

If the insured has 1 large loss in a year totaling to:

$150,000 — Amount of large loss

What is the retro premium for the insured?

### Part d

If the insured has both small and large losses in a year totaling to:

| B | C |
| --- | --- |
| $100,000 | Total of small losses in a year |
| $150,000 | Amount of large loss |

What is the retro premium for the insured?

## Solution

In all parts of this problem, I'll assume the retro formula used is:

R = (B + cL_D + excess loss premium)T In other words, since the excess loss premium is given separately from the basic premium, I'll assume it is not included as part of the basic premium. This is how the NCCI retro plan works.

### Part a

**R:** $215,250 — `=MIN(B11,(B6+B7+B8*B16)*B9)`

### Part b

R — $250,000 — `=MIN(B11,(B6+B7+B8*B23)*B9)` — capped by the max premium

### Part c

R — $157,500 — `=MIN(B11,(B6+B7+B8*MIN(B30,B10))*B9)` — cap the large loss by the accident limit

### Part d

R — $250,000 — `=MIN(B11,(B6+B7+B8*(B37+MIN(B38,B10)))*B9)` — cap the large loss by the accident limit, capped by the max premium

The last case is an example of the "overlap" between the effects of the maximum premium and the accident limit. In some years, even though there are large accidents, the accident limit will not provide any additional benefit to the insured beyond that provided by the maximum premium. In other words, for large accidents the accident limit and the maximum premium overlap.
