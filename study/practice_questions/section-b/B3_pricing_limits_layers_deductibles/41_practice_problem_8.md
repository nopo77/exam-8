---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 8 - Bahnemann Problem 6.5 revised
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 8
revised: false
points: null
parts: [a, b]
good_problem: false
has_images: true
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: Practice Problem 8
---

# Practice Problem 8 - Bahnemann Problem 6.5 revised

## Question

Assume that the distribution of the unlimited indemnity claim size X for a portfolio of policies has the following distribution:

| B | C |
| --- | --- |
| 2 | α for Shifted Pareto distribution |
| 24,000 | β for Shifted Pareto distribution |

For the Shifted Pareto distribution, you are given that:

![question image](images/img_3a192b949dd4.png)

Pareto severity with parameters $\alpha, \beta$:

$$E[X; l] = \frac{\beta}{\alpha-1}\left(1 - \left(\frac{\beta}{l+\beta}\right)^{\alpha-1}\right) \qquad F(x) = 1 - \left(\frac{\beta}{x+\beta}\right)^{\alpha}$$

### Part a

**Assume that the average ALAE per-claim is:** 2,500

Complete the following table of increased limit factors (including ALAE).

| Limit l | E[X;l] | ALAE | I(l) |
| --- | --- | --- | --- |
| 100,000 | 19,355 | 2,500 | 1.000 |
| 250,000 | - | - | - |
| 500,000 | - | - | - |
| 1,000,000 | - | - | - |
| 2,000,000 | - | - | - |
| 5,000,000 | - | - | - |

### Part b

**Alternatively, assume that ALAE as a percentage of indemnity is:** 25%

Complete the following table of increased limit factors (including ALAE).

| Limit l | E[X;l] | ALAE | I(l) |
| --- | --- | --- | --- |
| 100,000 | 19,355 | 4,839 | 1.000 |
| 250,000 | - | - | - |
| 500,000 | - | - | - |
| 1,000,000 | - | - | - |
| 2,000,000 | - | - | - |
| 5,000,000 | - | - | - |

## Solution

### Part a

| Limit l | E[X;l] | ALAE | I(l) |
| --- | --- | --- | --- |
| 100,000 | 19,355 | 2,500 | 1.000 |
| 250,000 | 21,898 | 2,500 | 1.116 |
| 500,000 | 22,901 | 2,500 | 1.162 |
| 1,000,000 | 23,438 | 2,500 | 1.187 |
| 2,000,000 | 23,715 | 2,500 | 1.200 |
| 5,000,000 | 23,885 | 2,500 | 1.207 |

<details><summary>Formulas</summary>

- `K4` = `=($B$8/($B$7-1))*(1-($B$8/(J4+$B$8))^($B$7-1))`
- `L4` = `=F$20`
- `M4` = `=(K4+L4)/(K$4+L$4)`
- `K5` = `=($B$8/($B$7-1))*(1-($B$8/(J5+$B$8))^($B$7-1))`
- `L5` = `=F$20`
- `M5` = `=(K5+L5)/(K$4+L$4)`
- `K6` = `=($B$8/($B$7-1))*(1-($B$8/(J6+$B$8))^($B$7-1))`
- `L6` = `=F$20`
- `M6` = `=(K6+L6)/(K$4+L$4)`
- `K7` = `=($B$8/($B$7-1))*(1-($B$8/(J7+$B$8))^($B$7-1))`
- `L7` = `=F$20`
- `M7` = `=(K7+L7)/(K$4+L$4)`
- `K8` = `=($B$8/($B$7-1))*(1-($B$8/(J8+$B$8))^($B$7-1))`
- `L8` = `=F$20`
- `M8` = `=(K8+L8)/(K$4+L$4)`
- `K9` = `=($B$8/($B$7-1))*(1-($B$8/(J9+$B$8))^($B$7-1))`
- `L9` = `=F$20`
- `M9` = `=(K9+L9)/(K$4+L$4)`

</details>

### Part b

| Limit l | E[X;l] | ALAE | I(l) | Note that ALAE will cancel out here when calculating ILFs, so this is the same as: |
| --- | --- | --- | --- | --- |
| 100,000 | 19,355 | 4,839 | 1.000 | 1.000 |
| 250,000 | 21,898 | 5,474 | 1.131 | 1.131 |
| 500,000 | 22,901 | 5,725 | 1.183 | 1.183 |
| 1,000,000 | 23,438 | 5,859 | 1.211 | 1.211 |
| 2,000,000 | 23,715 | 5,929 | 1.225 | 1.225 |
| 5,000,000 | 23,885 | 5,971 | 1.234 | 1.234 |

<details><summary>Formulas</summary>

- `K12` = `=($B$8/($B$7-1))*(1-($B$8/(J12+$B$8))^($B$7-1))`
- `L12` = `=K12*0.25`
- `M12` = `=(K12+L12)/(K$12+L$12)`
- `O12` = `=K12/K$12`
- `K13` = `=($B$8/($B$7-1))*(1-($B$8/(J13+$B$8))^($B$7-1))`
- `L13` = `=K13*0.25`
- `M13` = `=(K13+L13)/(K$12+L$12)`
- `O13` = `=K13/K$12`
- `K14` = `=($B$8/($B$7-1))*(1-($B$8/(J14+$B$8))^($B$7-1))`
- `L14` = `=K14*0.25`
- `M14` = `=(K14+L14)/(K$12+L$12)`
- `O14` = `=K14/K$12`
- `K15` = `=($B$8/($B$7-1))*(1-($B$8/(J15+$B$8))^($B$7-1))`
- `L15` = `=K15*0.25`
- `M15` = `=(K15+L15)/(K$12+L$12)`
- `O15` = `=K15/K$12`
- `K16` = `=($B$8/($B$7-1))*(1-($B$8/(J16+$B$8))^($B$7-1))`
- `L16` = `=K16*0.25`
- `M16` = `=(K16+L16)/(K$12+L$12)`
- `O16` = `=K16/K$12`
- `K17` = `=($B$8/($B$7-1))*(1-($B$8/(J17+$B$8))^($B$7-1))`
- `L17` = `=K17*0.25`
- `M17` = `=(K17+L17)/(K$12+L$12)`
- `O17` = `=K17/K$12`

</details>
