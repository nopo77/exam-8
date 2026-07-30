---
tia_section: A2
tia_topic: loss_sensitive_rating_plans
title: 2002 Exam 9 - Q1 revised
source: past_exam
exam_year: 2002
exam_sitting: null
exam_number: 9
question_number: 1
practice_number: null
revised: true
points: 1.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/02_ch02_risk_sharing_and_loss_sensitive_plans.md]
source_workbook: tia_excel/section-a/A_2_Loss_sensitive_rating_plans_practice_solutions.xlsx
source_sheet: 2002 Exam 9 - Q1 revised
---

# 2002 Exam 9 - Q1 revised

**Points:** 1

## Question

Calculate the premium for a workers compensation large deductible policy using the following information.

| B | C |
| --- | --- |
| $5,000,000 | Standard Premium for the Full Coverage Policy |
| $3,500,000 | Expected Loss and ALAE for the Full Coverage Policy |
| 10% | ULAE as a % of Loss and ALAE |
| 20% | Excess Loss and ALAE as a % of Total Loss and ALAE |
| 3% | Loss Based Assessment Factor as a % of Total Loss and ALAE |
| 0.5% | Provision for Credit Risk as a % of Standard Premium |
| 8% | Overhead Expense Ratio as a % of Standard Premium |
| 6% | Variable Expense and Profit as a % of Net Premium |

## Solution

It appears that there is no aggregate limit on deductible losses since there is no insurance charge.

**Premium:** $1,680,851 — `=(B8*SUM(B9:B11)+B7*SUM(B12:B13))/(1-B14)`

The components are shown below, but you wouldn't need to show all these individually to get full credit:

| B | E |
| --- | --- |
| Expected Losses and ALAE on Policy | $700,000 |
| Expected ULAE on Policy | $350,000 |
| Loss Based Assessment Provision | $105,000 |
| Credit Risk Provision | $25,000 |
| Overhead Expense Provision | $400,000 |

<details><summary>Formulas</summary>

- `E23` = `=B10*B8`
- `E24` = `=B9*B8`
- `E25` = `=B11*B8`
- `E26` = `=B12*B7`
- `E27` = `=B13*B7`

</details>

**Premium:** $1,680,851 — `=SUM(E23:E27)/(1-B14)`
