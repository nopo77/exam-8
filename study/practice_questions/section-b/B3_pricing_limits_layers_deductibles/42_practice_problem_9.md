---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 9 - Bahnemann Problem 6.8
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 9
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
source_sheet: Practice Problem 9
---

# Practice Problem 9 - Bahnemann Problem 6.8

## Question

### Part a

Assume that the distribution of the unlimited indemnity claim size X for a portfolio of policies has the following distribution:

| B | C |
| --- | --- |
| 3 | α for Shifted Pareto distribution |
| 6,000 | β for Shifted Pareto distribution |

For the Shifted Pareto distribution, you are given that:

![question image](images/img_3a192b949dd4.png)

Pareto severity with parameters $\alpha, \beta$:

$$E[X; l] = \frac{\beta}{\alpha-1}\left(1 - \left(\frac{\beta}{l+\beta}\right)^{\alpha-1}\right) \qquad F(x) = 1 - \left(\frac{\beta}{x+\beta}\right)^{\alpha}$$

**Assume that ALAE as a percentage of indemnity is:** 20%

Risk loads use the standard deviation method with:

| B | C |
| --- | --- |
| 0.500 | k' for standard deviation risk load |
| 0.100 | delta for standard deviation risk load |

Complete the missing values in the following table including ILFs with and without risk loads.

| Limit l | E[X;l] | ALAE | Risk load (l) | I(l) w/o RL | I(l) w/ RL | Weight | E[X^2;l] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1,000 | 796 | 159 | 446.666118 | 1.000 | 1.000 | 10% | 734,694 |
| 2,000 | - | - | - | - | - | 5% | 2,250,000 |
| 3,000 | - | - | - | - | - | 15% | 4,000,000 |
| 4,000 | - | - | - | - | - | 15% | 5,760,000 |
| 5,000 | - | - | - | - | - | 25% | 7,438,017 |
| 7,500 | - | - | - | - | - | 10% | 11,111,111 |
| 10,000 | - | - | - | - | - | 20% | 14,062,500 |

### Part b

Calculate the overall premium effect of using the risk-loaded factors in place of the unloaded factors.

## Solution

### Part a

| Limit l | E[X;l] | ALAE | Risk load | I(l) w/o RL | I(l) w/ RL |
| --- | --- | --- | --- | --- | --- |
| 1,000 | 796 | 159 | 447 | 1.000 | 1.000 |
| 2,000 | 1,312 | 262 | 778 | 1.649 | 1.679 |
| 3,000 | 1,667 | 333 | 1,034 | 2.094 | 2.165 |
| 4,000 | 1,920 | 384 | 1,238 | 2.412 | 2.527 |
| 5,000 | 2,107 | 421 | 1,404 | 2.648 | 2.806 |
| 7,500 | 2,407 | 481 | 1,710 | 3.025 | 3.280 |
| 10,000 | 2,578 | 516 | 1,919 | 3.239 | 3.576 |

<details><summary>Formulas</summary>

- `M4` = `=($B$9/($B$8-1))*(1-($B$9/(L4+$B$9))^($B$8-1))`
- `N4` = `=M4*$E$20`
- `O4` = `=B$24*SQRT(I30+B$25*M4^2)`
- `P4` = `=(M4+N4)/(M$4+N$4)`
- `Q4` = `=SUM(M4:O4)/SUM($M$4:$O$4)`
- `M5` = `=($B$9/($B$8-1))*(1-($B$9/(L5+$B$9))^($B$8-1))`
- `N5` = `=M5*$E$20`
- `O5` = `=B$24*SQRT(I31+B$25*M5^2)`
- `P5` = `=(M5+N5)/(M$4+N$4)`
- `Q5` = `=SUM(M5:O5)/SUM($M$4:$O$4)`
- `M6` = `=($B$9/($B$8-1))*(1-($B$9/(L6+$B$9))^($B$8-1))`
- `N6` = `=M6*$E$20`
- `O6` = `=B$24*SQRT(I32+B$25*M6^2)`
- `P6` = `=(M6+N6)/(M$4+N$4)`
- `Q6` = `=SUM(M6:O6)/SUM($M$4:$O$4)`
- `M7` = `=($B$9/($B$8-1))*(1-($B$9/(L7+$B$9))^($B$8-1))`
- `N7` = `=M7*$E$20`
- `O7` = `=B$24*SQRT(I33+B$25*M7^2)`
- `P7` = `=(M7+N7)/(M$4+N$4)`
- `Q7` = `=SUM(M7:O7)/SUM($M$4:$O$4)`
- `M8` = `=($B$9/($B$8-1))*(1-($B$9/(L8+$B$9))^($B$8-1))`
- `N8` = `=M8*$E$20`
- `O8` = `=B$24*SQRT(I34+B$25*M8^2)`
- `P8` = `=(M8+N8)/(M$4+N$4)`
- `Q8` = `=SUM(M8:O8)/SUM($M$4:$O$4)`
- `M9` = `=($B$9/($B$8-1))*(1-($B$9/(L9+$B$9))^($B$8-1))`
- `N9` = `=M9*$E$20`
- `O9` = `=B$24*SQRT(I35+B$25*M9^2)`
- `P9` = `=(M9+N9)/(M$4+N$4)`
- `Q9` = `=SUM(M9:O9)/SUM($M$4:$O$4)`
- `M10` = `=($B$9/($B$8-1))*(1-($B$9/(L10+$B$9))^($B$8-1))`
- `N10` = `=M10*$E$20`
- `O10` = `=B$24*SQRT(I36+B$25*M10^2)`
- `P10` = `=(M10+N10)/(M$4+N$4)`
- `Q10` = `=SUM(M10:O10)/SUM($M$4:$O$4)`

</details>

### Part b

| L | N |
| --- | --- |
| Avg ILF without RL | 2.471 |
| Avg ILF with RL | 2.632 |

<details><summary>Formulas</summary>

- `N12` = `=SUMPRODUCT(P4:P10,H30:H36)`
- `N13` = `=SUMPRODUCT(Q4:Q10,H30:H36)`

</details>

**% Change:** 6.5% — `=N13/N12-1`
