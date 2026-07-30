---
tia_section: B2
tia_topic: excess_distributions
title: Practice Problem 7 - Bahnemann Problem 5.23
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 7
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 7
---

# Practice Problem 7 - Bahnemann Problem 5.23

## Question

The table below summarizes grouped claim-size data from a sample of 1,000 claims. These claims are excess of a 500 straight deductible and have been censored by a policy limit of 100,000.

| Size Group Bottom | Size Group Top | # Claims |
| --- | --- | --- |
| 0 | 1,000 | 236 |
| 1,001 | 2,000 | 161 |
| 2,001 | 3,000 | 107 |
| 3,001 | 5,000 | 135 |
| 5,001 | 10,000 | 159 |
| 10,001 | 15,000 | 71 |
| 15,001 | 25,000 | 62 |
| 25,001 | 50,000 | 43 |
| 50,001 | 75,000 | 11 |
| 75,001 | 100,000 | 15 |
| Total |  | 1,000 |

| B | C |
| --- | --- |
| 500 | Straight deductible |
| 100,000 | Policy limit |

### Part a

Use the minimum chi-square method to obtain estimates of lognormal parameters for the ground-up population claim-size distribution. Use mu of 7.96 and test sigma values between 1.40 and 1.50 in 0.01 increments.

### Part b

Estimate the number of claims eliminated by the policy deductible.

## Solution

### Part a

| J | K | L | M | N |
| --- | --- | --- | --- | --- |
| mu | 7.96 | <--- given |  |  |
| sigma | 1.43 | <--- test to find optimal value of 1.43 |  |  |
|  |  |  | Expected | Chi-squared |
| GU top of layer | F(x) | CDF of X_a | Counts |  |
| 500 | 0.11 | 0.00 |  |  |
| 1,500 | 0.33 | 0.24 | 241.21 | 0.11 |
| 2,500 | 0.46 | 0.39 | 153.68 | 0.35 |
| 3,500 | 0.56 | 0.50 | 105.34 | 0.03 |
| 5,500 | 0.68 | 0.64 | 135.18 | 0.00 |
| 10,500 | 0.82 | 0.80 | 160.06 | 0.01 |
| 15,500 | 0.88 | 0.87 | 70.85 | 0.00 |
| 25,500 | 0.94 | 0.93 | 62.66 | 0.01 |
| 50,500 | 0.98 | 0.97 | 45.84 | 0.18 |
| 75,500 | 0.99 | 0.99 | 12.73 | 0.24 |
| infinity | 1 | 1.00 | 12.45 | 0.52 |

<details><summary>Formulas</summary>

- `J7` = `=B20`
- `K7` = `=LOGNORM.DIST(J7,K$3,K$4,TRUE)`
- `L7` = `=(K7-K$7)/(1-K$7)`
- `J8` = `=C8+B$20`
- `K8` = `=LOGNORM.DIST(J8,K$3,K$4,TRUE)`
- `L8` = `=(K8-K$7)/(1-K$7)`
- `M8` = `=D$18*(L8-L7)`
- `N8` = `=(D8-M8)^2/M8`
- `J9` = `=C9+B$20`
- `K9` = `=LOGNORM.DIST(J9,K$3,K$4,TRUE)`
- `L9` = `=(K9-K$7)/(1-K$7)`
- `M9` = `=D$18*(L9-L8)`
- `N9` = `=(D9-M9)^2/M9`
- `J10` = `=C10+B$20`
- `K10` = `=LOGNORM.DIST(J10,K$3,K$4,TRUE)`
- `L10` = `=(K10-K$7)/(1-K$7)`
- `M10` = `=D$18*(L10-L9)`
- `N10` = `=(D10-M10)^2/M10`
- `J11` = `=C11+B$20`
- `K11` = `=LOGNORM.DIST(J11,K$3,K$4,TRUE)`
- `L11` = `=(K11-K$7)/(1-K$7)`
- `M11` = `=D$18*(L11-L10)`
- `N11` = `=(D11-M11)^2/M11`
- `J12` = `=C12+B$20`
- `K12` = `=LOGNORM.DIST(J12,K$3,K$4,TRUE)`
- `L12` = `=(K12-K$7)/(1-K$7)`
- `M12` = `=D$18*(L12-L11)`
- `N12` = `=(D12-M12)^2/M12`
- `J13` = `=C13+B$20`
- `K13` = `=LOGNORM.DIST(J13,K$3,K$4,TRUE)`
- `L13` = `=(K13-K$7)/(1-K$7)`
- `M13` = `=D$18*(L13-L12)`
- `N13` = `=(D13-M13)^2/M13`
- `J14` = `=C14+B$20`
- `K14` = `=LOGNORM.DIST(J14,K$3,K$4,TRUE)`
- `L14` = `=(K14-K$7)/(1-K$7)`
- `M14` = `=D$18*(L14-L13)`
- `N14` = `=(D14-M14)^2/M14`
- `J15` = `=C15+B$20`
- `K15` = `=LOGNORM.DIST(J15,K$3,K$4,TRUE)`
- `L15` = `=(K15-K$7)/(1-K$7)`
- `M15` = `=D$18*(L15-L14)`
- `N15` = `=(D15-M15)^2/M15`
- `J16` = `=C16+B$20`
- `K16` = `=LOGNORM.DIST(J16,K$3,K$4,TRUE)`
- `L16` = `=(K16-K$7)/(1-K$7)`
- `M16` = `=D$18*(L16-L15)`
- `N16` = `=(D16-M16)^2/M16`
- `L17` = `=(K17-K$7)/(1-K$7)`
- `M17` = `=D$18*(L17-L16)`
- `N17` = `=(D17-M17)^2/M17`

</details>

Total — 1.44 — `=SUM(N8:N17)` — <--- minimize this

### Part b

| J | M |
| --- | --- |
| Expected GU counts | 1,125.02 |
| Expected counts below 500 ded | 125.02 |

<details><summary>Formulas</summary>

- `M21` = `=D18/(1-K7)`
- `M22` = `=M21*K7`

</details>

Test all possible sigma values to find lowest result

| Sigma | Chi-squared result |   |
| --- | --- | --- |
| 1.40 | 1.984752 |  |
| 1.41 | 1.665751 |  |
| 1.42 | 1.485644 |  |
| 1.43 | 1.43605 | <--- lowest value |
| 1.44 | 1.509233 |  |
| 1.45 | 1.698035 |  |
| 1.46 | 1.995832 |  |
| 1.47 | 2.396479 |  |
| 1.48 | 2.894277 |  |
| 1.49 | 3.483926 |  |
| 1.50 | 4.160 |  |

<details><summary>Formulas</summary>

- `R7` = `=R6+0.01`
- `R8` = `=R7+0.01`
- `R9` = `=R8+0.01`
- `R10` = `=R9+0.01`
- `R11` = `=R10+0.01`
- `R12` = `=R11+0.01`
- `R13` = `=R12+0.01`
- `R14` = `=R13+0.01`
- `R15` = `=R14+0.01`
- `R16` = `=R15+0.01`

</details>
