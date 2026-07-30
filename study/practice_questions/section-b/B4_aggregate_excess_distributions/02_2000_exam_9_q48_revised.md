---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2000 Exam 9 - Q48 revised
source: past_exam
exam_year: 2000
exam_sitting: null
exam_number: 9
question_number: 48
practice_number: null
revised: true
points: 2.0
parts: [a, b, c, d]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2000 Exam 9 - Q48 revised
---

# 2000 Exam 9 - Q48 revised

**Points:** 2

## Question

Based on the data below, answer the following. Assume that all risks have equal standard premiums. Show all work.

| Number of Risks | Unlimited Loss Ratio |
| --- | --- |
| 1 | 10% |
| 4 | 30% |
| 2 | 40% |
| 4 | 50% |
| 1 | 60% |
| 3 | 70% |
| 1 | 80% |
| 2 | 100% |
| 2 | 120% |

| Number of Risks | Limited Loss Ratio |
| --- | --- |
| 1 | 10% |
| 4 | 30% |
| 4 | 40% |
| 3 | 50% |
| 2 | 60% |
| 1 | 70% |
| 2 | 80% |
| 2 | 90% |
| 1 | 100% |

### Part a (0.50 pts)

Calculate the unlimited expected loss ratio and the limited expected loss ratio.

### Part b (0.50 pts)

Calculate the excess ratio.

### Part c (1.50 pts)

Calculate the Table M charges at loss ratios from 0% to 120% using loss ratio increments of 10%.

### Part d (0.50 pts)

Calculate the Table M savings for an entry ratio of 0.50.

## Solution

### Part a

| I | K |
| --- | --- |
| E[A]/P | 60% |
| E[A_D]/P | 53.5% |

<details><summary>Formulas</summary>

- `K2` = `=SUMPRODUCT(C8:C16,D8:D16)/SUM(C8:C16)`
- `K3` = `=SUMPRODUCT(C19:C27,D19:D27)/SUM(C19:C27)`

</details>

### Part b

**k:** 10.8% — `=1-K3/K2`

### Part c

Note they technically asked for a regular Table M, not a Limited Table M, so parts (c) and (d) have nothing to do with the limited table or the LER.

**total # risks:** 20 — `=SUM(C8:C16)`

| Unlim LR | r | # above | % above | Charge |
| --- | --- | --- | --- | --- |
| 0% | 0.00 | 20 | 1 | 1.000 |
| 10.0% | 0.17 | 19 | 0.95 | 0.833 |
| 20.0% | 0.33 | 19 | 0.95 | 0.675 |
| 30.0% | 0.50 | 15 | 0.75 | 0.517 |
| 40.0% | 0.67 | 13 | 0.65 | 0.392 |
| 50.0% | 0.83 | 9 | 0.45 | 0.283 |
| 60.0% | 1.00 | 8 | 0.4 | 0.208 |
| 70.0% | 1.17 | 5 | 0.25 | 0.142 |
| 80.0% | 1.33 | 4 | 0.2 | 0.100 |
| 90.0% | 1.50 | 4 | 0.2 | 0.067 |
| 100.0% | 1.67 | 2 | 0.1 | 0.033 |
| 110.0% | 1.83 | 2 | 0.1 | 0.017 |
| 120.0% | 2.00 | 0 | 0 | 0 |

<details><summary>Formulas</summary>

- `J13` = `=I13/$K$2`
- `K13` = `=SUMIF($D$8:$D$16,">"&I13,$C$8:$C$16)`
- `L13` = `=K13/K$10`
- `M13` = `=M14+(J14-J13)*L13`
- `I14` = `=I13+0.1`
- `J14` = `=I14/$K$2`
- `K14` = `=SUMIF($D$8:$D$16,">"&I14,$C$8:$C$16)`
- `L14` = `=K14/K$10`
- `M14` = `=M15+(J15-J14)*L14`
- `I15` = `=I14+0.1`
- `J15` = `=I15/$K$2`
- `K15` = `=SUMIF($D$8:$D$16,">"&I15,$C$8:$C$16)`
- `L15` = `=K15/K$10`
- `M15` = `=M16+(J16-J15)*L15`
- `I16` = `=I15+0.1`
- `J16` = `=I16/$K$2`
- `K16` = `=SUMIF($D$8:$D$16,">"&I16,$C$8:$C$16)`
- `L16` = `=K16/K$10`
- `M16` = `=M17+(J17-J16)*L16`
- `I17` = `=I16+0.1`
- `J17` = `=I17/$K$2`
- `K17` = `=SUMIF($D$8:$D$16,">"&I17,$C$8:$C$16)`
- `L17` = `=K17/K$10`
- `M17` = `=M18+(J18-J17)*L17`
- `I18` = `=I17+0.1`
- `J18` = `=I18/$K$2`
- `K18` = `=SUMIF($D$8:$D$16,">"&I18,$C$8:$C$16)`
- `L18` = `=K18/K$10`
- `M18` = `=M19+(J19-J18)*L18`
- `I19` = `=I18+0.1`
- `J19` = `=I19/$K$2`
- `K19` = `=SUMIF($D$8:$D$16,">"&I19,$C$8:$C$16)`
- `L19` = `=K19/K$10`
- `M19` = `=M20+(J20-J19)*L19`
- `I20` = `=I19+0.1`
- `J20` = `=I20/$K$2`
- `K20` = `=SUMIF($D$8:$D$16,">"&I20,$C$8:$C$16)`
- `L20` = `=K20/K$10`
- `M20` = `=M21+(J21-J20)*L20`
- `I21` = `=I20+0.1`
- `J21` = `=I21/$K$2`
- `K21` = `=SUMIF($D$8:$D$16,">"&I21,$C$8:$C$16)`
- `L21` = `=K21/K$10`
- `M21` = `=M22+(J22-J21)*L21`
- `I22` = `=I21+0.1`
- `J22` = `=I22/$K$2`
- `K22` = `=SUMIF($D$8:$D$16,">"&I22,$C$8:$C$16)`
- `L22` = `=K22/K$10`
- `M22` = `=M23+(J23-J22)*L22`
- `I23` = `=I22+0.1`
- `J23` = `=I23/$K$2`
- `K23` = `=SUMIF($D$8:$D$16,">"&I23,$C$8:$C$16)`
- `L23` = `=K23/K$10`
- `M23` = `=M24+(J24-J23)*L23`
- `I24` = `=I23+0.1`
- `J24` = `=I24/$K$2`
- `K24` = `=SUMIF($D$8:$D$16,">"&I24,$C$8:$C$16)`
- `L24` = `=K24/K$10`
- `M24` = `=M25+(J25-J24)*L24`
- `I25` = `=I24+0.1`
- `J25` = `=I25/$K$2`
- `K25` = `=SUMIF($D$8:$D$16,">"&I25,$C$8:$C$16)`
- `L25` = `=K25/K$10`

</details>

### Part d

**Psi(0.5):** 0.017 — `=M16+J16-1`
