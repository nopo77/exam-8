---
tia_section: B2
tia_topic: excess_distributions
title: Practice Problem 8
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 8
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
source_sheet: Practice Problem 8
---

# Practice Problem 8

## Question

You are given the following claims information from a book of business:

| Size Group | # Claims | Ground-up Loss |
| --- | --- | --- |
| 0 - 500 | 631 | $135,714 |
| 500 - 1,000 | 244 | $170,766 |
| 1,000 - 2,000 | 106 | $138,937 |
| 2,000 - 5,000 | 19 | $47,050 |
| Total | 1,000 | $492,467 |

### Part a

Calculate the excess severities for this book of business at the amounts below:

$0

$500

$1,000

$2,000

### Part b

Given the following additional information:

| B | C |
| --- | --- |
| 1.5 | Mean of ground-up claim count distribution |
| 0.4 | Claim contagion parameter |
| $121,439 | E[X2;500] |
| $273,701 | E[X2;1,000] |

Calculate the mean and variance of pure premiums in the layer 500 - 1,000.

## Solution

### Part a

Solution 1: Calculate expected limited loss, and use that to get expected excess loss

| x | F(x) | E[X;x] | Excess Sev |
| --- | --- | --- | --- |
| $0 | 0 | 0 | $492.47 |
| $500 | 0.631 | $320.21 | $466.81 |
| $1,000 | 0.875 | $431.48 | $487.90 |
| $2,000 | 0.981 | $483.42 | $476.32 |
| $5,000 | 1 | $492.47 |  |

<details><summary>Formulas</summary>

- `I6` = `=B16`
- `L6` = `=($K$10-K6)/(1-J6)`
- `I7` = `=B17`
- `J7` = `=SUM($C$7:C7)/$C$11`
- `K7` = `=(SUM($D$7:D7)+SUM(C8:$C$10)*I7)/$C$11`
- `L7` = `=($K$10-K7)/(1-J7)`
- `I8` = `=B18`
- `J8` = `=SUM($C$7:C8)/$C$11`
- `K8` = `=(SUM($D$7:D8)+SUM(C9:$C$10)*I8)/$C$11`
- `L8` = `=($K$10-K8)/(1-J8)`
- `I9` = `=B19`
- `J9` = `=SUM($C$7:C9)/$C$11`
- `K9` = `=(SUM($D$7:D9)+SUM(C10:$C$10)*I9)/$C$11`
- `L9` = `=($K$10-K9)/(1-J9)`
- `J10` = `=SUM($C$7:C10)/$C$11`
- `K10` = `=D11/C11`

</details>

Solution 2: Calculate ground-up loss for each size group and subtract off loss below the limit

| x | Excess Sev | Mathematically equivalent alternative version of this calculation that may feel more intuitive: |
| --- | --- | --- |
| $0 | $492.47 | $492.47 |
| $500 | $466.81 | $466.81 |
| $1,000 | $487.90 | $487.90 |
| $2,000 | $476.32 | $476.32 |

<details><summary>Formulas</summary>

- `I15` = `=B16`
- `J15` = `=SUM(D7:D$10)/SUM(C7:C$10)-I15`
- `N15` = `=(SUM(D7:D$10)-SUM(C7:C$10)*I15)/SUM(C7:C$10)`
- `I16` = `=B17`
- `J16` = `=SUM(D8:D$10)/SUM(C8:C$10)-I16`
- `N16` = `=(SUM(D8:D$10)-SUM(C8:C$10)*I16)/SUM(C8:C$10)`
- `I17` = `=B18`
- `J17` = `=SUM(D9:D$10)/SUM(C9:C$10)-I17`
- `N17` = `=(SUM(D9:D$10)-SUM(C9:C$10)*I17)/SUM(C9:C$10)`
- `I18` = `=B19`
- `J18` = `=SUM(D10:D$10)/SUM(C10:C$10)-I18`
- `N18` = `=(SUM(D10:D$10)-SUM(C10:C$10)*I18)/SUM(C10:C$10)`

</details>

### Part b

Solution 1: Based on solution 1 above

E[S] — $166.90 — `=B24*(K8-K7)` — For the mean, we use E[S] = E[N](E[X;a + l] - E[X;a])

Var[S] — $72,636.11 — `=B24*(B27-B26)-2*500*K23+B25*K23^2` — For the variance, we use Var[S] = E[N](E[X^2 ;a + l] - E [X^2;a]) - 2aE[S] + γ(E[S])^2.

Solution 2: Based on solution 2 above

| x | F(x) | E[N_a] | <-- E[N_a] = expected counts exceeding x |
| --- | --- | --- | --- |
| $500 | 0.631 | 0.5535 |  |
| $1,000 | 0.875 | 0.1875 |  |

<details><summary>Formulas</summary>

- `I30` = `=B17`
- `K30` = `=SUM($C$7:C7)/$C$11`
- `L30` = `=B$24*(1-K30)`
- `I31` = `=B18`
- `K31` = `=SUM($C$7:C8)/$C$11`
- `L31` = `=B$24*(1-K31)`

</details>

E[S] — $166.90 — `=L30*J16-L31*J17` — Expected losses exceeding 500 - expected losses exceeding 1000 = expected losses between 500 and 1000

Var[S] — $72,636.11 — `=B24*(B27-B26)-2*500*K33+B25*K33^2` — For the variance, we use Var[S] = E[N](E[X^2 ;a + l] - E [X^2;a]) - 2aE[S] + γ(E[S])^2.
