---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2004 Exam 9 - Q19 revised
source: past_exam
exam_year: 2004
exam_sitting: null
exam_number: 9
question_number: 19
practice_number: null
revised: true
points: 1.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2004 Exam 9 - Q19 revised
---

# 2004 Exam 9 - Q19 revised

**Points:** 1

## Question

Given the following loss distribution:

| Size of Loss | Number of Claims | Total Loss Dollars |
| --- | --- | --- |
| $100 | 40 | $4,000 |
| $250 | 50 | $12,500 |
| $500 | 120 | $60,000 |
| $750 | 50 | $37,500 |
| $1,000 and higher | 60 | $86,000 |
| Total | 320 | $200,000 |

Calculate the loss elimination ratio of a $250 deductible disappearing at $750.

## Solution

**LER:** 0.1575 — `=J13/D12`

Not relevant for the question, but we can also calculate the excess claim counts and severity as:

| B | C | D |
| --- | --- | --- |
| Excess claim counts: | 230 | since claims of $250 and below are eliminated |
| Excess severity | $732.61 |  |

<details><summary>Formulas</summary>

- `C21` = `=SUM(C9:C11)`
- `C22` = `=(D12-J13)/C21`

</details>

| Deductible | Loss Eliminated |   |
| --- | --- | --- |
| $100 | $4,000 |  |
| $250 | $12,500 |  |
| $125 | $15,000 | since 500 is halfway between 250 and 750, the deductible goes halfway from 250 towards 0, so 125 |
| 0 | $0 |  |
| 0 | $0 |  |

<details><summary>Formulas</summary>

- `I7` = `=B7`
- `J7` = `=I7*C7`
- `I8` = `=B8`
- `J8` = `=I8*C8`
- `I9` = `=250/2`
- `J9` = `=I9*C9`
- `J10` = `=I10*C10`
- `J11` = `=I11*C11`

</details>

$31,500 — `=SUM(J7:J11)`
