---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2006 Exam 9 - Q7 revised
source: past_exam
exam_year: 2006
exam_sitting: null
exam_number: 9
question_number: 7
practice_number: null
revised: true
points: 3.0
parts: [a, b]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2006 Exam 9 - Q7 revised
---

# 2006 Exam 9 - Q7 revised

**Points:** 3

## Question

Given the following information for 10 risks:

Individual Claims greater than $100,000

| Risk Number | Aggregate Loss | Claim 1 | Claim 2 | Claim 3 | Claim 4 |
| --- | --- | --- | --- | --- | --- |
| 1 | $350,000 |  |  |  |  |
| 2 | $550,000 |  |  |  |  |
| 3 | $650,000 |  |  |  |  |
| 4 | $750,000 | $200,000 |  |  |  |
| 5 | $900,000 | $125,000 |  |  |  |
| 6 | $950,000 | $250,000 |  |  |  |
| 7 | $1,150,000 | $200,000 | $225,000 |  |  |
| 8 | $1,200,000 | $700,000 |  |  |  |
| 9 | $1,500,000 | $350,000 | $850,000 |  |  |
| 10 | $2,000,000 | $125,000 | $200,000 | $400,000 | $950,000 |

Assume:

| B | C |
| --- | --- |
| $1,250,000 | Standard premium for each risk |
| 80% | Expected loss ratio for each risk |

- The table shows the ground-up value of claims.
- The aggregate loss column contains the total value of all claims (including the large claims

greater than $100,000) for each risk.

### Part a (1.50 pts)

Calculate the Loss Elimination Ratio (LER) with a $250,000 per claim limit.

### Part b (1.50 pts)

Calculate the Table L charge at an entry ratio of 1.05 with a per-claim limit of $250,000.

## Solution

### Part a

Remember that the numerator of a loss elimination ratio for a limit represents the amounts in excess of that limit.

| J | K | M | N |
| --- | --- | --- | --- |
| E[A] | $1,000,000 | k | 0.2 |
| E[A_D] | $800,000 |  |  |

<details><summary>Formulas</summary>

- `K4` = `=B21*B22`
- `N4` = `=1-K5/K4`
- `K5` = `=AVERAGE(J8:J17)`

</details>

| A_D | r for Table L |
| --- | --- |
| $350,000 | 0.35 |
| $550,000 | 0.55 |
| $650,000 | 0.65 |
| $750,000 | 0.75 |
| $900,000 | 0.9 |
| $950,000 | 0.95 |
| $1,150,000 | 1.15 |
| $750,000 | 0.75 |
| $800,000 | 0.8 |
| $1,150,000 | 1.15 |

<details><summary>Formulas</summary>

- `J8` = `=C8`
- `L8` = `=J8/K$4`
- `J9` = `=C9`
- `L9` = `=J9/K$4`
- `J10` = `=C10`
- `L10` = `=J10/K$4`
- `J11` = `=C11`
- `L11` = `=J11/K$4`
- `J12` = `=C12`
- `L12` = `=J12/K$4`
- `J13` = `=C13`
- `L13` = `=J13/K$4`
- `J14` = `=C14`
- `L14` = `=J14/K$4`
- `J15` = `=C15-(D15-250000)`
- `L15` = `=J15/K$4`
- `J16` = `=C16-(D16+E16)+250000*2`
- `L16` = `=J16/K$4`
- `J17` = `=C17-(F17+G17)+250000*2`
- `L17` = `=J17/K$4`

</details>

### Part b

Solution 1: Use vertical slices

**Table L charge:** 0.22 — `=N4+(L14-1.05)*(1/10)+(L17-1.05)*(1/10)`

Solution 2: Limiting Losses

| J | K | M | O |
| --- | --- | --- | --- |
| Risk Number | min(r,1.05) | E[r;1.05] | 0.78 |
| 1 | 0.35 |  |  |
| 2 | 0.55 | Table L Charge | 0.22 |
| 3 | 0.65 |  |  |
| 4 | 0.75 |  |  |
| 5 | 0.9 |  |  |
| 6 | 0.95 |  |  |
| 7 | 1.05 |  |  |
| 8 | 0.75 |  |  |
| 9 | 0.8 |  |  |
| 10 | 1.05 |  |  |

<details><summary>Formulas</summary>

- `O25` = `=AVERAGE(K26:K35)`
- `K26` = `=MIN(L8,1.05)`
- `K27` = `=MIN(L9,1.05)`
- `O27` = `=1-O25`
- `K28` = `=MIN(L10,1.05)`
- `K29` = `=MIN(L11,1.05)`
- `K30` = `=MIN(L12,1.05)`
- `K31` = `=MIN(L13,1.05)`
- `K32` = `=MIN(L14,1.05)`
- `K33` = `=MIN(L15,1.05)`
- `K34` = `=MIN(L16,1.05)`
- `K35` = `=MIN(L17,1.05)`

</details>

Solution 3: Build a Table L

|   | r | # above | % above | Table L Charge |   |
| --- | --- | --- | --- | --- | --- |
| 0.35 | 0 | 10 | 1 | 1 |  |
| 0.55 | 0.35 | 9 | 0.9 | 0.65 |  |
| 0.65 | 0.55 | 8 | 0.8 | 0.47 |  |
| 0.75 | 0.65 | 7 | 0.7 | 0.39 |  |
| 0.8 | 0.75 | 5 | 0.5 | 0.32 |  |
| 0.9 | 0.8 | 4 | 0.4 | 0.295 |  |
| 0.95 | 0.9 | 3 | 0.3 | 0.255 |  |
| 1.15 | 0.95 | 2 | 0.2 | 0.24 |  |
|  | 1.050 | 2 | 0.2 | 0.22 | <-- part (b) answer |
|  | 1.15 | 0 | 0 | 0.2 |  |

<details><summary>Formulas</summary>

- `H40` = `={SORT(UNIQUE(L8:L17))}`
- `K40` = `=COUNTIF($L$8:$L$17,">"&J40)`
- `L40` = `=K40/10`
- `M40` = `=M41+(J41-J40)*L40`
- `J41` = `=H40`
- `K41` = `=COUNTIF($L$8:$L$17,">"&J41)`
- `L41` = `=K41/10`
- `M41` = `=M42+(J42-J41)*L41`
- `J42` = `=H41`
- `K42` = `=COUNTIF($L$8:$L$17,">"&J42)`
- `L42` = `=K42/10`
- `M42` = `=M43+(J43-J42)*L42`
- `J43` = `=H42`
- `K43` = `=COUNTIF($L$8:$L$17,">"&J43)`
- `L43` = `=K43/10`
- `M43` = `=M44+(J44-J43)*L43`
- `J44` = `=H43`
- `K44` = `=COUNTIF($L$8:$L$17,">"&J44)`
- `L44` = `=K44/10`
- `M44` = `=M45+(J45-J44)*L44`
- `J45` = `=H44`
- `K45` = `=COUNTIF($L$8:$L$17,">"&J45)`
- `L45` = `=K45/10`
- `M45` = `=M46+(J46-J45)*L45`
- `J46` = `=H45`
- `K46` = `=COUNTIF($L$8:$L$17,">"&J46)`
- `L46` = `=K46/10`
- `M46` = `=M47+(J47-J46)*L46`
- `J47` = `=H46`
- `K47` = `=COUNTIF($L$8:$L$17,">"&J47)`
- `L47` = `=K47/10`
- `M47` = `=M48+(J48-J47)*L47`
- `K48` = `=COUNTIF($L$8:$L$17,">"&J48)`
- `L48` = `=K48/10`
- `M48` = `=M49+(J49-J48)*L48`
- `J49` = `=H47`
- `K49` = `=COUNTIF($L$8:$L$17,">"&J49)`
- `L49` = `=K49/10`
- `M49` = `=N4`

</details>
