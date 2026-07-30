---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 12 - Bahnemann Problem 6.17
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 12
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: true
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: Practice Problem 12
---

# Practice Problem 12 - Bahnemann Problem 6.17

## Question

Assume that the distribution of the unlimited indemnity claim size X for a portfolio of policies has the following distribution:

| B | C |
| --- | --- |
| 3.000 | α for Shifted Pareto distribution |
| 10,000 | β for Shifted Pareto distribution |

For the Shifted Pareto distribution, you are given that:

![question image](images/img_3a192b949dd4.png)

Pareto severity with parameters $\alpha, \beta$:

$$E[X; l] = \frac{\beta}{\alpha-1}\left(1 - \left(\frac{\beta}{l+\beta}\right)^{\alpha-1}\right) \qquad F(x) = 1 - \left(\frac{\beta}{x+\beta}\right)^{\alpha}$$

Also, for this portfolio of policies:

| B | C |
| --- | --- |
| 0.005 | Unlimited claim frequency |
| 250 | Additive ALAE per claim |

A policy from this portfolio has a deductible of size d and the following basic limit:

5,000 — Basic limit

### Part a

Complete the missing values in the following table for values of a straight deductible d:

| Deductible d | C(d) | Policy Frequency | Policy Severity | Pure Premium |
| --- | --- | --- | --- | --- |
| 0 | - | - | - | - |
| 250 | - | - | - | - |
| 500 | - | - | - | - |
| 750 | - | - | - | - |
| 1,000 | - | - | - | - |

### Part b

Repeat part (a) assuming the deductible was a franchise deductible instead of a straight deductible.

## Solution

Includes ALAE

### Part a

| Deductible d | C(d) | Policy Frequency | Policy Severity | Pure Premium | E[X;d] | F(d) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.000 | 0.0050 | 3,027.78 | 15.14 | 0.00 | 0.00 |
| 250 | 0.085 | 0.0046 | 2,981.91 | 13.84 | 240.93 | 0.07 |
| 500 | 0.165 | 0.0043 | 2,927.50 | 12.64 | 464.85 | 0.14 |
| 750 | 0.238 | 0.0040 | 2,864.34 | 11.53 | 673.34 | 0.20 |
| 1,000 | 0.307 | 0.0038 | 2,792.22 | 10.49 | 867.77 | 0.25 |

<details><summary>Formulas</summary>

- `J4` = `=(N4+O4*B$22)/(N$10+B$22)`
- `K4` = `=B$21*(1-O4)`
- `L4` = `=(N$10-N4)/(1-O4)+B$22`
- `M4` = `=K4*L4`
- `N4` = `=(B$8/(B$7-1))*(1-(B$8/(I4+B$8))^(B$7-1))`
- `O4` = `=1-(B$8/(I4+B$8))^B$7`
- `J5` = `=(N5+O5*B$22)/(N$10+B$22)`
- `K5` = `=B$21*(1-O5)`
- `L5` = `=(N$10-N5)/(1-O5)+B$22`
- `M5` = `=K5*L5`
- `N5` = `=(B$8/(B$7-1))*(1-(B$8/(I5+B$8))^(B$7-1))`
- `O5` = `=1-(B$8/(I5+B$8))^B$7`
- `J6` = `=(N6+O6*B$22)/(N$10+B$22)`
- `K6` = `=B$21*(1-O6)`
- `L6` = `=(N$10-N6)/(1-O6)+B$22`
- `M6` = `=K6*L6`
- `N6` = `=(B$8/(B$7-1))*(1-(B$8/(I6+B$8))^(B$7-1))`
- `O6` = `=1-(B$8/(I6+B$8))^B$7`
- `J7` = `=(N7+O7*B$22)/(N$10+B$22)`
- `K7` = `=B$21*(1-O7)`
- `L7` = `=(N$10-N7)/(1-O7)+B$22`
- `M7` = `=K7*L7`
- `N7` = `=(B$8/(B$7-1))*(1-(B$8/(I7+B$8))^(B$7-1))`
- `O7` = `=1-(B$8/(I7+B$8))^B$7`
- `J8` = `=(N8+O8*B$22)/(N$10+B$22)`
- `K8` = `=B$21*(1-O8)`
- `L8` = `=(N$10-N8)/(1-O8)+B$22`
- `M8` = `=K8*L8`
- `N8` = `=(B$8/(B$7-1))*(1-(B$8/(I8+B$8))^(B$7-1))`
- `O8` = `=1-(B$8/(I8+B$8))^B$7`

</details>

basic lim: — 5,000 — 2,777.78 — `=(B$8/(B$7-1))*(1-(B$8/(I10+B$8))^(B$7-1))`

### Part b

| Deductible d | C(d) | Policy Frequency | Policy Severity | Pure Premium |
| --- | --- | --- | --- | --- |
| 0 | 0.000 | 0.0050 | 3,027.78 | 15.14 |
| 250 | 0.009 | 0.0046 | 3,231.91 | 15.01 |
| 500 | 0.022 | 0.0043 | 3,427.50 | 14.80 |
| 750 | 0.039 | 0.0040 | 3,614.34 | 14.55 |
| 1,000 | 0.059 | 0.0038 | 3,792.22 | 14.25 |

<details><summary>Formulas</summary>

- `J13` = `=(N4-I13*(1-O4)+O4*B$22)/(N$10+B$22)`
- `K13` = `=B$21*(1-O4)`
- `L13` = `=(N$10-N4)/(1-O4)+(I13+B$22)`
- `M13` = `=L13*K13`
- `J14` = `=(N5-I14*(1-O5)+O5*B$22)/(N$10+B$22)`
- `K14` = `=B$21*(1-O5)`
- `L14` = `=(N$10-N5)/(1-O5)+(I14+B$22)`
- `M14` = `=L14*K14`
- `J15` = `=(N6-I15*(1-O6)+O6*B$22)/(N$10+B$22)`
- `K15` = `=B$21*(1-O6)`
- `L15` = `=(N$10-N6)/(1-O6)+(I15+B$22)`
- `M15` = `=L15*K15`
- `J16` = `=(N7-I16*(1-O7)+O7*B$22)/(N$10+B$22)`
- `K16` = `=B$21*(1-O7)`
- `L16` = `=(N$10-N7)/(1-O7)+(I16+B$22)`
- `M16` = `=L16*K16`
- `J17` = `=(N8-I17*(1-O8)+O8*B$22)/(N$10+B$22)`
- `K17` = `=B$21*(1-O8)`
- `L17` = `=(N$10-N8)/(1-O8)+(I17+B$22)`
- `M17` = `=L17*K17`

</details>
