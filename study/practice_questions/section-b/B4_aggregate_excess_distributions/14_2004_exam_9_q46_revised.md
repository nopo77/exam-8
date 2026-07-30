---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2004 Exam 9 - Q46 revised
source: past_exam
exam_year: 2004
exam_sitting: null
exam_number: 9
question_number: 46
practice_number: null
revised: true
points: 2.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2004 Exam 9 - Q46 revised
---

# 2004 Exam 9 - Q46 revised

**Points:** 2

## Question

A large deductible workers compensation policy provides for reimbursement of losses to the insurer up to $200,000 per accident and subject to an aggregate limit of $1,500,000. For this policy the following apply:

| B | C |
| --- | --- |
| $1,000,000 | Expected unlimited losses |
| $750,000 | Expected losses capped at $200,000 per accident limit |
| 1.10 | State and hazard group differential |

Given the following regular Table M:

Range of Rounded Entry Ratio

| Range of Rounded Expected Losses | 1.00 to 1.25 | 1.26 to 1.50 | 1.51 to 1.75 | 1.76 to 2.00 | 2.01 to 2.25 | 2.26 to 2.50 |
| --- | --- | --- | --- | --- | --- | --- |
| $900,000 and lower | 0.301 | 0.240 | 0.196 | 0.164 | 0.139 | 0.120 |
| $900,001 to $1,050,000 | 0.291 | 0.229 | 0.185 | 0.153 | 0.130 | 0.111 |
| $1,050,001 to $1,200,000 | 0.280 | 0.218 | 0.175 | 0.143 | 0.120 | 0.103 |
| $1,200,001 to $1,350,000 | 0.270 | 0.207 | 0.164 | 0.133 | 0.111 | 0.094 |
| $1,350,001 to $1,500,000 | 0.259 | 0.197 | 0.154 | 0.123 | 0.102 | 0.085 |
| $1,500,001 to $1,650,000 | 0.249 | 0.186 | 0.143 | 0.113 | 0.092 | 0.077 |
| $1,650,001 to $1,800,000 | 0.238 | 0.175 | 0.133 | 0.104 | 0.083 | 0.069 |
| $1,800,001 to $1,950,000 | 0.228 | 0.164 | 0.122 | 0.094 | 0.074 | 0.060 |
| $1,950,001 and higher | 0.217 | 0.153 | 0.112 | 0.084 | 0.065 | 0.052 |

Calculate the expected losses paid by the insurer under this policy. Show all work.

## Solution

For a large deductible policy with a Limited Table M, the expected losses on the policy are:

kE[A] + phi^LM(r*_L)*E[A_D] Since this is a regular Table M but we have an accident limit to consider, we need to use the ICRLL procedure.

**r*_G:** 2.00 — `=1500000/B9`

**k:** 0.25 — `=1-B9/B8`

**Adjusted Expected Loss:** $1,760,000 — `=B8*B10*(1+0.8*M8)/(1-M8)`

**Expected loss paid by insurer:** $328,000 — `=M8*B8+F22*B9`
