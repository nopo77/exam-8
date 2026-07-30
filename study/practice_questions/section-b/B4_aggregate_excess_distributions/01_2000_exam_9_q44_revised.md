---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2000 Exam 9 - Q44 revised
source: past_exam
exam_year: 2000
exam_sitting: null
exam_number: 9
question_number: 44
practice_number: null
revised: true
points: 2.0
parts: [a, b]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2000 Exam 9 - Q44 revised
---

# 2000 Exam 9 - Q44 revised

**Points:** 2

## Question

An insured is deciding whether or not to be retrospectively rated. The insured is given the following information about a possible retrospectively rated program:

| B | C |
| --- | --- |
| $100,000 | Standard Premium |
| $20,000 | Basic Premium |
| $60,000 | Expected Losses |
| $1,950 | Converted Net Insurance Charge |
| 1.300 | Loss Conversion Factor |
| 2% | Taxes as a Percent of Premium |

### Part a (1.50 pts)

What premium will the insured pay if he decides not to be retrospectively rated? Show all work.

### Part b (0.50 pts)

At what level of incurred losses will the insured pay the same premium whether or not he decides to be retrospectively rated? Show all work.

## Solution

### Part a

If the insured is prospectively rated, he will pay the guaranteed cost premium. If the retro plan is balanced, this equals the expected retro premium. So either formula can be used to obtain the solution. Note that we are given the "converted" net insurance charge, which is cI.

I assume the retro plan is balanced, so GCP = E[R], and the insured will pay GCP if rated prospectively.

Solution 1: use E[R] = (B + cE[L])T = (B + c(E[A] - I))T = (B + cE[A] - cI)T

**E[R]:** $98,010 — `=(B8+B11*B9-B10)/(1-B12)`

Solution 2: use GCP = (e + E[A])T

B = e - (c - 1)E[A] + cI

**Solve for e:** $36,050 — `=B8-B10+(B11-1)*B9`

**GCP:** $98,010 — `=(K16+B9)/(1-B12)`

### Part b

Technically we can solve for ratable losses L here, not actual losses A. We don't know the ratable limits (or max/min premiums) that would be required to confirm whether L and A would be equal in this scenario.

R = (B + cL)T = 98,010

**Solve for L:** $58,500 — `=(L10*(1-B12)-B8)/B11`
