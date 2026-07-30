---
tia_section: C2
tia_topic: iso_experience_rating
title: 2003 Exam 9 - Q5 revised
source: past_exam
exam_year: 2003
exam_sitting: null
exam_number: 9
question_number: 5
practice_number: null
revised: true
points: 1.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-c/C_2_ISO_experience_rating_practice_solutions.xlsx
source_sheet: 2003 Exam 9 - Q5 revised
---

# 2003 Exam 9 - Q5 revised

**Points:** 1

## Question

An insured has the following products/completed operations losses:

| Policy Period | Total Limit Losses | Allocated Loss Adjustment Expense |
| --- | --- | --- |
| January 1, 2000 - December 31, 2000 | $10,000 | $0 |
|  | $17,500 | $2,000 |
|  | $150,000 | $150,000 |

| B | D | E |
| --- | --- | --- |
| January 1, 2001 - December 31, 2001 | $0 | $15,000 |
|  | $7,000 | $500 |
|  | $140,000 | $25,000 |

January 1, 2002 - December 31, 2002 — $150,000 — $125,000

| B | C |
| --- | --- |
| $160,000 | Maximum Single Loss |
| $100,000 | Basic Limit |

What is the total amount of actual losses that would be included in the calculation of the general liability experience modification for a policy effective January 1, 2004?

## Solution

We first need to cap losses at the basic limit, then cap basic limits losses + ALAE by the MSL.

| Basic Loss | Loss+ALAE Lim by MSL |
| --- | --- |
| $10,000 | $10,000 |
| $17,500 | $19,500 |
| $100,000 | $160,000 |

<details><summary>Formulas</summary>

- `I7` = `=MIN(D7,$B$18)`
- `K7` = `=MIN(I7+E7,$B$17)`
- `I8` = `=MIN(D8,$B$18)`
- `K8` = `=MIN(I8+E8,$B$17)`
- `I9` = `=MIN(D9,$B$18)`
- `K9` = `=MIN(I9+E9,$B$17)`

</details>

| I | K |
| --- | --- |
| $0 | $15,000 |
| $7,000 | $7,500 |
| $100,000 | $125,000 |

<details><summary>Formulas</summary>

- `I11` = `=MIN(D11,$B$18)`
- `K11` = `=MIN(I11+E11,$B$17)`
- `I12` = `=MIN(D12,$B$18)`
- `K12` = `=MIN(I12+E12,$B$17)`
- `I13` = `=MIN(D13,$B$18)`
- `K13` = `=MIN(I13+E13,$B$17)`

</details>

$100,000 — `=MIN(D15,$B$18)` — $160,000 — `=MIN(I15+E15,$B$17)`

**Total:** $497,000 — `=SUM(K7:K15)`
