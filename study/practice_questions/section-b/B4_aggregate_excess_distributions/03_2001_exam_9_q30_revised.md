---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2001 Exam 9 - Q30 revised
source: past_exam
exam_year: 2001
exam_sitting: null
exam_number: 9
question_number: 30
practice_number: null
revised: true
points: 1.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2001 Exam 9 - Q30 revised
---

# 2001 Exam 9 - Q30 revised

**Points:** 1

## Question

Describe the steps to construct a Table M.

## Solution

Really, there are 4 main steps to include here for 0.25 points each:

1. Calculate entry ratios = actual loss / expected loss for each aggregate loss amount in the data and at 0.

2. Calculate the % of risks above each entry ratio.

3. Set Charge(r) = 0 for the largest value of r.

4. Calculate Charge(r_i) = Charge(r_(i+1)) + (r_(i+1) - r_i)(% risks above r_i).
