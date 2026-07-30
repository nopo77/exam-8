---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2005 Exam 9 - Q35 revised
source: past_exam
exam_year: 2005
exam_sitting: null
exam_number: 9
question_number: 35
practice_number: null
revised: true
points: 2.5
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2005 Exam 9 - Q35 revised
---

# 2005 Exam 9 - Q35 revised

**Points:** 2.5

## Question

Given the following information:

| Size of loss | Number of Claims |
| --- | --- |
| $500 | 1 |
| $1,000 | 62 |
| $5,000 | 114 |
| $8,000 | 120 |
| $10,000 | Y |
| $15,000 | 38 |
| $20,000 | 15 |

40% — Loss elimination ratio for a $5,000 deductible disappearing at $15,000

Determine the value of Y.

## Solution

(1,052,500 + 2,500Y) / (2,462,500 + 10,000Y) = 40%

Solve for Y:

$985,000 — `=K14*B15` — 4000Y — 1,052,500 + 2,500Y = 985,000 + 4,000Y

1,500 — `=4000-2500` — $67,500 — `=L14-B22` — 67,500 = 1,500Y

**Y:** 45 — `=C24/B24`

You could have instead used the FORECAST function to get the deductibles between d and D:

| Claim size | Effective Deductible |
| --- | --- |
| 5,000 | 5,000 |
| 15,000 | 0 |

| B | C |
| --- | --- |
| $8,000 | 3,500 |
| $10,000 | 2,500 |

<details><summary>Formulas</summary>

- `B33` = `=B10`
- `C33` = `=FORECAST(B33,$C$30:$C$31,$B$30:$B$31)`
- `B34` = `=B11`
- `C34` = `=FORECAST(B34,$C$30:$C$31,$B$30:$B$31)`

</details>

| Ded amount | Total Loss | Loss Eliminated |
| --- | --- | --- |
| $500 | $500 | $500 |
| $1,000 | $62,000 | $62,000 |
| $5,000 | $570,000 | $570,000 |
| $3,500 | $960,000 | $420,000 |
| $2,500 | 10000Y | 2500Y |
| $0 | $570,000 | $0 |
| $0 | $300,000 | $0 |
| Total excl Y row | $2,462,500 | $1,052,500 |

<details><summary>Formulas</summary>

- `J7` = `=B7`
- `K7` = `=C7*B7`
- `L7` = `=C7*J7`
- `J8` = `=B8`
- `K8` = `=C8*B8`
- `L8` = `=C8*J8`
- `J9` = `=B9`
- `K9` = `=C9*B9`
- `L9` = `=C9*J9`
- `J10` = `=5000/(15000-5000)*(15000-B10)`
- `K10` = `=C10*B10`
- `L10` = `=C10*J10`
- `J11` = `=5000/(15000-5000)*(15000-B11)`
- `K12` = `=C12*B12`
- `L12` = `=C12*J12`
- `K13` = `=C13*B13`
- `L13` = `=C13*J13`
- `K14` = `=SUM(K12:K13,K7:K10)`
- `L14` = `=SUM(L7:L10,L12:L13)`

</details>
