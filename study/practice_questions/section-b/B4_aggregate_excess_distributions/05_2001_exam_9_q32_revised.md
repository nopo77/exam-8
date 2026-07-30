---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2001 Exam 9 - Q32 revised
source: past_exam
exam_year: 2001
exam_sitting: null
exam_number: 9
question_number: 32
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
source_sheet: 2001 Exam 9 - Q32 revised
---

# 2001 Exam 9 - Q32 revised

**Points:** 3

## Question

Answer the following.

### Part a (1.50 pts)

You are the risk manager for a large company that buys a retrospectively rated Workers Compensation policy. This policy was rated using an expected loss ratio of 60%. Your boss asks you to determine how the final retrospectively rated premium for this policy will compare to the guaranteed cost premium if the loss ratio at the final evaluation is equal to 60%.

Briefly describe how the final retrospectively rated premium and the guaranteed cost premium will compare. Assume the maximum premium factor corresponds to a loss ratio higher than 60%, and the minimum premium factor corresponds to a loss ratio lower than 60%.

### Part b (1.50 pts)

Your boss is suspicious of the complicated trial-and-error procedure used by the insurer to calculate an insurance charge for your company's policy. Briefly explain why such an iterative procedure is used.

## Solution

### Part a

Guaranteed cost premium = (e + E[A])T

For this question, actual losses = L = expected losses = E[A] As usual on these older problems based on the NCCI plan, we'll assume the plan is balanced.

Retro premium = R = (B + cL)T = (B + cE[A])T B = e - (c - 1)E[A] + cI R = (e - (c - 1)E[A] + cI + cE[A])T R = (e + E[A] + cI)T R - GCP = (e + E[A] + cI)T - (e + E[A])T = cIT

Thus, the difference between the guaranteed cost premium and the retro premium will be driven by the net insurance charge I, which will depend on the selected maximum and minimum premium. If the max and min are selected to result in a zero net charge, then the retro premium will equal the guaranteed cost premium. If the max and min are selected such that there is a positive net charge, the retro premium will be higher than the guaranteed cost premium.

### Part b

This is in reference to the Table M search process.

The iterative procedure is needed because the insured selects H (minimum premium) and G (maximum premium), instead of r_G and r_H . Since H and G depend on B, which in turn, depends on H and G, an iterative procedure is needed.
