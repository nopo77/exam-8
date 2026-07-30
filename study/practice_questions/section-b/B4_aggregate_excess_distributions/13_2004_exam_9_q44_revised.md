---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2004 Exam 9 - Q44 revised
source: past_exam
exam_year: 2004
exam_sitting: null
exam_number: 9
question_number: 44
practice_number: null
revised: true
points: 3.0
parts: [a, b, c, d]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2004 Exam 9 - Q44 revised
---

# 2004 Exam 9 - Q44 revised

**Points:** 3

## Question

An actuary observes the following risks in a retrospective rating plan:

| Loss Ratio | Number of Risks |
| --- | --- |
| 10% | 4 |
| 30% | 6 |
| 60% | 5 |
| 80% | 3 |
| 120% | 2 |

All risks have a standard premium of $10,000.

Assume for parts (c) and (d) below:

- A per occurrence limit applying to all risks results in the loss ratio of 120% being changed to

90%, with no other changes to the loss ratios or number of risks in the table above.

- The loss elimination ratio is 0.06.

### Part a (1.50 pts)

Determine the Table M charge for an entry ratio of 1.4. Show all work.

### Part b (0.50 pts)

Determine the Table M savings for an entry ratio of 1.4. Show all work.

### Part c (0.50 pts)

Determine the Table L charge for an entry ratio of 1.4. Show all work.

### Part d (0.50 pts)

Determine the Table L savings for an entry ratio of 1.4. Show all work.

## Solution

| G | H |
| --- | --- |
| # risks | 20 |
| E[A]/P | 50% |

<details><summary>Formulas</summary>

- `H3` = `=SUM(C7:C11)`
- `H4` = `=SUMPRODUCT(B7:B11,C7:C11)/H3`

</details>

| r for Table M | r for Table L |
| --- | --- |
| 0.2 | 0.2 |
| 0.6 | 0.6 |
| 1.2 | 1.2 |
| 1.6 | 1.6 |
| 2.4 | 1.8 |

<details><summary>Formulas</summary>

- `G7` = `=B7/H$4`
- `H7` = `=G7`
- `G8` = `=B8/H$4`
- `H8` = `=G8`
- `G9` = `=B9/H$4`
- `H9` = `=G9`
- `G10` = `=B10/H$4`
- `H10` = `=G10`
- `G11` = `=B11/H$4`
- `H11` = `=0.9/H4`

</details>

From here, I'll show 2 approaches to this problem: (1) a quick way using vertical slices, and (2) building the full tables (not recommended since takes long).

Solution 1: Use vertical slices

### Part a

**Phi(1.4):** 0.13 — `=(G10-1.4)*(C10/H3)+(G11-1.4)*(C11/H3)`

### Part b

**Psi(1.4):** 0.53 — `=I17+1.4-1`

### Part c

**Table L charge:** 0.13 — `=0.06+(H10-1.4)*(C10/H3)+(H11-1.4)*(C11/H3)`

### Part d

**Table L savings:** 0.53 — `=I21+1.4-1`

Solution 2: Build full tables

| r | # above | % above | Table M Charge | Table M Savings |   |
| --- | --- | --- | --- | --- | --- |
| 0 | 20 | 1 | 1 | 0 |  |
| 0.2 | 16 | 0.8 | 0.8 | 0 |  |
| 0.6 | 10 | 0.5 | 0.48 | 0.08 |  |
| 1.2 | 5 | 0.25 | 0.18 | 0.38 |  |
| 1.40 | 5 | 0.25 | 0.13 | 0.53 | <-- (a) and (b) answers |
| 1.6 | 2 | 0.1 | 0.08 | 0.68 |  |
| 2.4 | 0 | 0 | 0 | 1.4 |  |

<details><summary>Formulas</summary>

- `I28` = `=SUMIF($G$7:$G$11,">"&H28,$C$7:$C$11)`
- `J28` = `=I28/H$3`
- `K28` = `=K29+(H29-H28)*J28`
- `L28` = `=K28+H28-1`
- `H29` = `=G7`
- `I29` = `=SUMIF($G$7:$G$11,">"&H29,$C$7:$C$11)`
- `J29` = `=I29/H$3`
- `K29` = `=K30+(H30-H29)*J29`
- `L29` = `=K29+H29-1`
- `H30` = `=G8`
- `I30` = `=SUMIF($G$7:$G$11,">"&H30,$C$7:$C$11)`
- `J30` = `=I30/H$3`
- `K30` = `=K31+(H31-H30)*J30`
- `L30` = `=K30+H30-1`
- `H31` = `=G9`
- `I31` = `=SUMIF($G$7:$G$11,">"&H31,$C$7:$C$11)`
- `J31` = `=I31/H$3`
- `K31` = `=K32+(H32-H31)*J31`
- `L31` = `=K31+H31-1`
- `I32` = `=SUMIF($G$7:$G$11,">"&H32,$C$7:$C$11)`
- `J32` = `=I32/H$3`
- `K32` = `=K33+(H33-H32)*J32`
- `L32` = `=K32+H32-1`
- `H33` = `=G10`
- `I33` = `=SUMIF($G$7:$G$11,">"&H33,$C$7:$C$11)`
- `J33` = `=I33/H$3`
- `K33` = `=K34+(H34-H33)*J33`
- `L33` = `=K33+H33-1`
- `H34` = `=G11`
- `I34` = `=SUMIF($G$7:$G$11,">"&H34,$C$7:$C$11)`
- `J34` = `=I34/H$3`
- `L34` = `=K34+H34-1`

</details>

| r | # above | % above | Table L Charge | Table L Savings |   |
| --- | --- | --- | --- | --- | --- |
| 0 | 20 | 1 | 1 | 0 |  |
| 0.2 | 16 | 0.8 | 0.8 | 0 |  |
| 0.6 | 10 | 0.5 | 0.48 | 0.08 |  |
| 1.2 | 5 | 0.25 | 0.18 | 0.38 |  |
| 1.40 | 5 | 0.25 | 0.13 | 0.53 | <-- (c) and (d) answers |
| 1.6 | 2 | 0.1 | 0.08 | 0.68 |  |
| 1.8 | 0 | 0 | 0.06 | 0.86 |  |

<details><summary>Formulas</summary>

- `I37` = `=SUMIF($H$7:$H$11,">"&H37,$C$7:$C$11)`
- `J37` = `=I37/H$3`
- `K37` = `=K38+(H38-H37)*J37`
- `L37` = `=K37+H37-1`
- `H38` = `=H7`
- `I38` = `=SUMIF($H$7:$H$11,">"&H38,$C$7:$C$11)`
- `J38` = `=I38/H$3`
- `K38` = `=K39+(H39-H38)*J38`
- `L38` = `=K38+H38-1`
- `H39` = `=H8`
- `I39` = `=SUMIF($H$7:$H$11,">"&H39,$C$7:$C$11)`
- `J39` = `=I39/H$3`
- `K39` = `=K40+(H40-H39)*J39`
- `L39` = `=K39+H39-1`
- `H40` = `=H9`
- `I40` = `=SUMIF($H$7:$H$11,">"&H40,$C$7:$C$11)`
- `J40` = `=I40/H$3`
- `K40` = `=K41+(H41-H40)*J40`
- `L40` = `=K40+H40-1`
- `I41` = `=SUMIF($H$7:$H$11,">"&H41,$C$7:$C$11)`
- `J41` = `=I41/H$3`
- `K41` = `=K42+(H42-H41)*J41`
- `L41` = `=K41+H41-1`
- `H42` = `=H10`
- `I42` = `=SUMIF($H$7:$H$11,">"&H42,$C$7:$C$11)`
- `J42` = `=I42/H$3`
- `K42` = `=K43+(H43-H42)*J42`
- `L42` = `=K42+H42-1`
- `H43` = `=H11`
- `I43` = `=SUMIF($H$7:$H$11,">"&H43,$C$7:$C$11)`
- `J43` = `=I43/H$3`
- `L43` = `=K43+H43-1`

</details>
