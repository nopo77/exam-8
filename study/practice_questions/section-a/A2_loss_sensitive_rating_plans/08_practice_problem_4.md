---
tia_section: A2
tia_topic: loss_sensitive_rating_plans
title: Practice Problem 4
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 4
revised: false
points: null
parts: [a, b, c, d]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/02_ch02_risk_sharing_and_loss_sensitive_plans.md]
source_workbook: tia_excel/section-a/A_2_Loss_sensitive_rating_plans_practice_solutions.xlsx
source_sheet: Practice Problem 4
---

# Practice Problem 4

## Question

You are given the following information for a large deductible plan with a $100,000 per-occurrence deductible and a $350,000 limit on deductible losses:

| B | C |
| --- | --- |
| $50,000 | Fixed Expenses |
| $5,000 | Underwriting Profit Provision |
| 10% | Loss-based Expenses (% of ground-up losses) |
| 3% | Premium Tax Rate |
| $300,000 | Expected Ground-up Losses |
| $220,000 | Expected Losses limited to $100,000 per-occurrence |
| $205,000 | Expected Losses limited to $100,000 per-occurrence and $350,000 in aggregate |

Actual loss experience after the policy is written:

| Claim | Ground-up Loss |
| --- | --- |
| 1 | 20,000 |
| 2 | 325,000 |
| 3 | 15,000 |
| 4 | 200,000 |

### Part a

Calculate the premium for the large deductible policy.

### Part b

Calculate the total amount the insured will need to reimburse the insurer.

### Part c

Briefly discuss why credit risk exists for a large deductible plan.

### Part d

For loss-sensitive plans in general, briefly discuss three ways an insurer can protect itself from credit risk.

## Solution

### Part a

Note that the premium covers excess losses in excess of both the occurrence deductible and the aggregate limit on deductible losses. We can calculate these 2 pieces separately by adding (300-220) and (220-205), or we can just subtract (300-205) directly.

**Premium:** $185,567 — `=(B7+B8+B9*B11+(B11-B13))/(1-B10)`

### Part b

The insured will reimburse the insurer for all amounts below the 100,000 deductible, up to a maximum reimbursement of 350,000.

**Reimbursement:** 235,000 — `=M22`

### Part c

Credit risk exists in case the insurer is unable to collect the deductible reimbursements from the insured due to the insured's financial condition.

### Part d

3 ways are:

i. Security: The insurer can hold collateral.

ii. LDFs: For retro and dividend plans, the insurer can apply loss development factors and use

ultimate losses instead of actual losses to date in the retro premium and dividend formulas.

iii. Holdbacks: Insurers can delay retro adjustments or dividend payments until later

maturities.

Limited Loss

20,000 — `=MIN(C18,100000)`

100,000 — `=MIN(C19,100000)`

15,000 — `=MIN(C20,100000)`

100,000 — `=MIN(C21,100000)`

**Agg:** 235,000 — `=MIN(SUM(M18:M21),350000)`
