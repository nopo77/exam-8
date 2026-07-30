---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 2
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 2
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: Practice Problem 2
---

# Practice Problem 2

## Question

Given the following information:

2 — Parameter for Poisson claim count distribution

Ground-up claim size distribution:

| Claim-size | Probability |
| --- | --- |
| $500 | 50% |
| $1,000 | 50% |

### Part a

For this part:

| B | C |
| --- | --- |
| $750 | Per-claim limit |
| $500 | Basic per-claim limit |

Calculate the increased limit factor for a $750 per-claim limit given that the basic per-claim limit is $500.

### Part b

For this part:

| B | C |
| --- | --- |
| $750 | Per-claim limit |
| $2,000 | Aggregate limit |
| $500 | Basic per-claim limit |

Calculate the increased limit factor for a $750 per-claim limit and a $2,000 aggregate limit given that the basic per-claim limit is $500.

## Solution

### Part a

| K | L |
| --- | --- |
| E[X;500] | $500 |
| E[X;750] | $625 |

<details><summary>Formulas</summary>

- `L2` = `=B11*(C11+C12)`
- `L3` = `=B11*C11+750*C12`

</details>

**I(750):** 1.25 — `=L3/L2`

### Part b

For this part we need to construct an aggregate loss distribution in order to calculate the expected loss limited by both the per-claim and aggregate limits. Note that we want to use the limited claim size distribution due to the $750 per-claim limit, so for this part our limited claim size distribution is just $500 or $750 with equal probability. We can use Panjer's recursive algorithm to get the aggregate loss distribution as I show below, or we can obtain it by considering the possible combinations of loss events.

| K | L |
| --- | --- |
| a | 0 |
| b | 2 |
| h | 250 |
| f(500) | 50% |
| f(750) | 50% |

<details><summary>Formulas</summary>

- `L14` = `=B6`
- `L16` = `=C11`
- `L17` = `=C12`

</details>

Alternative way to get distribution:

| m | S | f(s) |   | Events that lead to this S value | Probability |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.135 |  | no claims occur | 0.135 |
| 1 | 250 | 0 | since f_x(250)=0 | impossible | 0.000 |
| 2 | 500 | 0.135 |  | 1 claim occurs equal to 500 | 0.135 |
| 3 | 750 | 0.135 |  | 1 1000 claim occurs, limited to 750 | 0.135 |
| 4 | 1,000 | 0.068 |  | 2 claims occur, both equal to 500 | 0.068 |
| 5 | 1,250 | 0.135 |  | 1 claim of 500 & 1 claim of 1000 limited to 750, in either order | 0.135 |
| 6 | 1,500 | 0.090 |  | 2 claims of 1000 each limited to 750 or 3 claims of 500 | 0.090 |
| 7 | 1,750 | 0.068 |  | 1 1000 claim occurs, limited to 750, and 2 claims of 500, in any order | 0.068 |
| 2000 or greater | 2,000 | 0.233 |  | Remainder of probability | 0.233 |

<details><summary>Formulas</summary>

- `K20` = `=J20*$L$15`
- `L20` = `=EXP(-B6)`
- `P20` = `=POISSON.DIST(0,B6,FALSE)`
- `J21` = `=J20+1`
- `K21` = `=J21*$L$15`
- `J22` = `=J21+1`
- `K22` = `=J22*$L$15`
- `L22` = `=$L$14/J22*2*$L$16*$L$20`
- `P22` = `=POISSON.DIST(1,B6,FALSE)*C11`
- `J23` = `=J22+1`
- `K23` = `=J23*$L$15`
- `L23` = `=$L$14/J23*3*$L$17*$L$20`
- `P23` = `=POISSON.DIST(1,B6,FALSE)*C12`
- `J24` = `=J23+1`
- `K24` = `=J24*$L$15`
- `L24` = `=$L$14/J24*2*$L$16*$L$22`
- `P24` = `=POISSON.DIST(2,B6,FALSE)*C11^2`
- `J25` = `=J24+1`
- `K25` = `=J25*$L$15`
- `L25` = `=$L$14/J25*2*$L$16*$L$23+$L$14/J25*3*$L$17*$L$22`
- `P25` = `=POISSON.DIST(2,B6,FALSE)*C11*C12*2`
- `J26` = `=J25+1`
- `K26` = `=J26*$L$15`
- `L26` = `=$L$14/J26*2*$L$16*$L$24+$L$14/J26*3*$L$17*$L$23`
- `P26` = `=POISSON.DIST(2,B6,FALSE)*C12^2 + POISSON.DIST(3,B6,FALSE)*C11^3`
- `J27` = `=J26+1`
- `K27` = `=J27*$L$15`
- `L27` = `=$L$14/J27*2*$L$16*$L$25+$L$14/J27*3*$L$17*$L$24`
- `P27` = `=POISSON.DIST(3,B6,FALSE)*(C12*C11^2)*3`
- `L28` = `=1-SUM(L20:L27)`
- `P28` = `=1-SUM(P20:P27)`

</details>

**E[S_750;2000]:** 1,125.959629 — `=SUMPRODUCT(K20:K28,L20:L28)`

**E[S_500]:** $1,000 — `=L2*B6`

**I(750,2000):** 1.126 — `=L30/L32`

It makes sense that this ILF is lower than the ILF in part (a), which was I(750,∞).
