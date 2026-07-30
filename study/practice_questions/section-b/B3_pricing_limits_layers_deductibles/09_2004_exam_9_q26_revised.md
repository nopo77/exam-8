---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2004 Exam 9 - Q26 revised
source: past_exam
exam_year: 2004
exam_sitting: null
exam_number: 9
question_number: 26
practice_number: null
revised: true
points: 3.0
parts: [a, b, c]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: review
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2004 Exam 9 - Q26 revised
---

# 2004 Exam 9 - Q26 revised

**Points:** 3

## Question

Given the following pure premium information about a block of auto policies:

| Attachment Point | Excess Losses as a Percent of Total | Excess Losses per Exposure Unit |
| --- | --- | --- |
| $0 | 100% | $5,000 |
| $25,000 | 75% | $3,750 |
| $100,000 | 50% | $2,500 |
| $500,000 | 35% | $1,750 |
| $1,000,000 | 10% | $500 |

### Part a (0.50 pts)

Calculate the pure premium for coverage from $500,000 to $1,000,000. Show all work.

### Part b (1.50 pts)

Given that $25,000 is the basic limit for a policy, calculate the four increased limits factors for the policy limits of $25,000, $100,000, $500,000, and $1,000,000. Show all work.

### Part c (1.00 pts)

Do the increased limits factors calculated in part (b) above pass the consistency test? Explain why or why not.

$25,000

$100,000

$500,000

$1,000,000

## Solution

### Part a

**pure prem:** $1,250 — `=D10-D11`

### Part c

### Part b

| Limit | pure prem | ILF | I'(l) | Optional: I''(l) rescaled |
| --- | --- | --- | --- | --- |
|  | $1,250 | 1.00 |  |  |
|  | $2,500 | 2.00 | 0.0000133 |  |
|  | $3,250 | 2.60 | 0.0000015 | -0.30 |
|  | $4,500 | 3.60 | 0.0000020 | 0.01 |

<details><summary>Formulas</summary>

- `D27` = `=$D$7-D8`
- `E27` = `=D27/$D$27`
- `D28` = `=$D$7-D9`
- `E28` = `=D28/$D$27`
- `G28` = `=(E28-E27)/(B28-B27)`
- `D29` = `=$D$7-D10`
- `E29` = `=D29/$D$27`
- `G29` = `=(E29-E28)/(B29-B28)`
- `I29` = `=(G29-G28)/(B29-B28)*10000000000`
- `D30` = `=$D$7-D11`
- `E30` = `=D30/$D$27`
- `G30` = `=(E30-E29)/(B30-B29)`
- `I30` = `=(G30-G29)/(B30-B29)*10000000000`

</details>

The ILFs do not pass the consistency test since the marginal rate increases from 500k to 1M.
