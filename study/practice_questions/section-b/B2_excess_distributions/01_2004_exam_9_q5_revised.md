---
tia_section: B2
tia_topic: excess_distributions
title: 2004 Exam 9 - Q5 revised
source: past_exam
exam_year: 2004
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
split_confidence: review
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: 2004 Exam 9 - Q5 revised
---

# 2004 Exam 9 - Q5 revised

**Points:** 1

## Question

An insurance company purchases workers compensation excess of loss coverage of $500,000 excess of $500,000 per claim. Losses in the current year are as follows:

| Loss Number | Incurred Losses |
| --- | --- |
| 1 | $500,000 |
| 2 | $600,000 |
| 3 | $350,000 |
| 4 | $1,500,000 |
| 5 | $950,000 |

| B | C |
| --- | --- |
| $500,000 | Retention |
| $500,000 | Limit |
| 9% | Inflation rate for workers compensation claims |

Calculate the inflation rate for pure premiums in the $500,000 excess of $500,000 layer.

| Loss Number | Incurred Losses |
| --- | --- |
| 1 | $500,000 |
| 2 | $600,000 |
| 3 | $350,000 |
| 4 | $1,500,000 |
| 5 | $950,000 |

## Solution

Solution 2: Calculate limited expected values (more consistent with current syllabus)

Limit l

$458,715.60 — `=E23/(1+B16)` — $500,000 — `=B14` — $917,431.19 — `=G23/(1+B16)` — $1,000,000 — `=B14+B15`

Capped Loss

| D | E | F | G |
| --- | --- | --- | --- |
| $458,716 | $500,000 | $500,000 | $500,000 |
| $458,716 | $500,000 | $600,000 | $600,000 |
| $350,000 | $350,000 | $350,000 | $350,000 |
| $458,716 | $500,000 | $917,431 | $1,000,000 |
| $458,716 | $500,000 | $917,431 | $950,000 |

<details><summary>Formulas</summary>

- `D25` = `=MIN($C25,D$23)`
- `E25` = `=MIN($C25,E$23)`
- `F25` = `=MIN($C25,F$23)`
- `G25` = `=MIN($C25,G$23)`
- `D26` = `=MIN($C26,D$23)`
- `E26` = `=MIN($C26,E$23)`
- `F26` = `=MIN($C26,F$23)`
- `G26` = `=MIN($C26,G$23)`
- `D27` = `=MIN($C27,D$23)`
- `E27` = `=MIN($C27,E$23)`
- `F27` = `=MIN($C27,F$23)`
- `G27` = `=MIN($C27,G$23)`
- `D28` = `=MIN($C28,D$23)`
- `E28` = `=MIN($C28,E$23)`
- `F28` = `=MIN($C28,F$23)`
- `G28` = `=MIN($C28,G$23)`
- `D29` = `=MIN($C29,D$23)`
- `E29` = `=MIN($C29,E$23)`
- `F29` = `=MIN($C29,F$23)`
- `G29` = `=MIN($C29,G$23)`

</details>

E[X;l] — $436,972 — `=AVERAGE(D25:D29)` — $470,000 — `=AVERAGE(E25:E29)` — $656,972 — `=AVERAGE(F25:F29)` — $680,000 — `=AVERAGE(G25:G29)`

**Tau_S:** 1.142 — `=(1+B16)*(F31-D31)/(G31-E31)`

**Trend rate:** 14.2% — `=D33-1`

Solution 1: Calculate loss in layer before and after trend

| Loss in layer | Trended Loss | Trended Loss in Layer |
| --- | --- | --- |
| $0 | $545,000 | $45,000 |
| $100,000 | $654,000 | $154,000 |
| $0 | $381,500 | $0 |
| $500,000 | $1,635,000 | $500,000 |
| $450,000 | $1,035,500 | $500,000 |

<details><summary>Formulas</summary>

- `M8` = `=MAX(0,MIN(C8-$B$14,$B$15))`
- `N8` = `=C8*(1+$B$16)`
- `O8` = `=MAX(0,MIN(N8-$B$14,$B$15))`
- `M9` = `=MAX(0,MIN(C9-$B$14,$B$15))`
- `N9` = `=C9*(1+$B$16)`
- `O9` = `=MAX(0,MIN(N9-$B$14,$B$15))`
- `M10` = `=MAX(0,MIN(C10-$B$14,$B$15))`
- `N10` = `=C10*(1+$B$16)`
- `O10` = `=MAX(0,MIN(N10-$B$14,$B$15))`
- `M11` = `=MAX(0,MIN(C11-$B$14,$B$15))`
- `N11` = `=C11*(1+$B$16)`
- `O11` = `=MAX(0,MIN(N11-$B$14,$B$15))`
- `M12` = `=MAX(0,MIN(C12-$B$14,$B$15))`
- `N12` = `=C12*(1+$B$16)`
- `O12` = `=MAX(0,MIN(N12-$B$14,$B$15))`

</details>

$1,050,000 — `=SUM(M8:M12)` — $1,199,000 — `=SUM(O8:O12)`

**Trend in layer:** 14.2% — `=O14/M14-1`
