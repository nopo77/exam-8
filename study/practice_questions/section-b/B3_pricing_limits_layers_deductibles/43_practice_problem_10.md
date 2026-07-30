---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 10 - Bahnemann Problem 6.10
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 10
revised: false
points: null
parts: []
good_problem: true
has_images: true
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: Practice Problem 10
---

# Practice Problem 10 - Bahnemann Problem 6.10

## Question

Assume that the distribution of the unlimited indemnity claim size X for a portfolio of policies has the following distribution:

| B | C |
| --- | --- |
| 0.780 | α for Shifted Pareto distribution |
| 100 | β for Shifted Pareto distribution |

For the Shifted Pareto distribution, you are given that:

![question image](images/img_3a192b949dd4.png)

Pareto severity with parameters $\alpha, \beta$:

$$E[X; l] = \frac{\beta}{\alpha-1}\left(1 - \left(\frac{\beta}{l+\beta}\right)^{\alpha-1}\right) \qquad F(x) = 1 - \left(\frac{\beta}{x+\beta}\right)^{\alpha}$$

ILFs do not include any Loss Adjustment Expenses.

Risk loads use the variance method with:

| B | C |
| --- | --- |
| 0.00000050 | k for variance risk load |
| 0 | delta for variance risk load |

Complete the missing values in the following table including risk-loaded ILFs, and calculate the layer factors for successive layers of 1,000,000 width and thereby demonstrate the inconsistency of this set of ILFs.

| Limit l | E[X;l] | Risk load (l) | I(l) w/ RL | Layer Factor | E[X^2;l] |
| --- | --- | --- | --- | --- | --- |
| 1,000,000 | 2,994 | 622 | 1.000 | n/a | 1,243,106,397 |
| 2,000,000 | 3,562 | 1,448 | 1.386 | 0.3858 | 2,896,303,012 |
| 3,000,000 | 3,936 | 2,375 | 1.746 | 0.3600 | 4,750,094,900 |
| 4,000,000 | - | - | - | - | 6,747,473,455 |
| 5,000,000 | - | - | - | - | 8,858,896,975 |
| 6,000,000 | - | - | - | - | 11,065,888,883 |
| 7,000,000 | - | - | - | - | 13,355,660,167 |
| 8,000,000 | - | - | - | - | 15,718,768,783 |
| 9,000,000 | - | - | - | - | 18,147,923,367 |
| 10,000,000 | - | - | - | - | 20,637,303,326 |

## Solution

| Limit l | E[X;l] | Risk load (l) | I(l) w/ RL | Layer Factor |
| --- | --- | --- | --- | --- |
| 1,000,000 | 2,994 | 622 | 1.000 | n/a |
| 2,000,000 | 3,562 | 1,448 | 1.386 | 0.3858 |
| 3,000,000 | 3,936 | 2,375 | 1.746 | 0.3600 |
| 4,000,000 | 4,223 | 3,374 | 2.101 | 0.3556 |
| 5,000,000 | 4,459 | 4,429 | 2.459 | 0.3571 |
| 6,000,000 | 4,660 | 5,533 | 2.819 | 0.3609 |
| 7,000,000 | 4,836 | 6,678 | 3.185 | 0.3655 |
| 8,000,000 | 4,994 | 7,859 | 3.555 | 0.3705 |
| 9,000,000 | 5,137 | 9,074 | 3.931 | 0.3755 |
| 10,000,000 | 5,268 | 10,319 | 4.311 | 0.3806 |

<details><summary>Formulas</summary>

- `K4` = `=($B$8/($B$7-1))*(1-($B$8/(J4+$B$8))^($B$7-1))`
- `L4` = `=B$23*(G31+B$24*K4^2)`
- `M4` = `=SUM(K4:L4)/SUM($K$4:$L$4)`
- `K5` = `=($B$8/($B$7-1))*(1-($B$8/(J5+$B$8))^($B$7-1))`
- `L5` = `=B$23*(G32+B$24*K5^2)`
- `M5` = `=SUM(K5:L5)/SUM($K$4:$L$4)`
- `N5` = `=M5-M4`
- `K6` = `=($B$8/($B$7-1))*(1-($B$8/(J6+$B$8))^($B$7-1))`
- `L6` = `=B$23*(G33+B$24*K6^2)`
- `M6` = `=SUM(K6:L6)/SUM($K$4:$L$4)`
- `N6` = `=M6-M5`
- `K7` = `=($B$8/($B$7-1))*(1-($B$8/(J7+$B$8))^($B$7-1))`
- `L7` = `=B$23*(G34+B$24*K7^2)`
- `M7` = `=SUM(K7:L7)/SUM($K$4:$L$4)`
- `N7` = `=M7-M6`
- `K8` = `=($B$8/($B$7-1))*(1-($B$8/(J8+$B$8))^($B$7-1))`
- `L8` = `=B$23*(G35+B$24*K8^2)`
- `M8` = `=SUM(K8:L8)/SUM($K$4:$L$4)`
- `N8` = `=M8-M7`
- `K9` = `=($B$8/($B$7-1))*(1-($B$8/(J9+$B$8))^($B$7-1))`
- `L9` = `=B$23*(G36+B$24*K9^2)`
- `M9` = `=SUM(K9:L9)/SUM($K$4:$L$4)`
- `N9` = `=M9-M8`
- `K10` = `=($B$8/($B$7-1))*(1-($B$8/(J10+$B$8))^($B$7-1))`
- `L10` = `=B$23*(G37+B$24*K10^2)`
- `M10` = `=SUM(K10:L10)/SUM($K$4:$L$4)`
- `N10` = `=M10-M9`
- `K11` = `=($B$8/($B$7-1))*(1-($B$8/(J11+$B$8))^($B$7-1))`
- `L11` = `=B$23*(G38+B$24*K11^2)`
- `M11` = `=SUM(K11:L11)/SUM($K$4:$L$4)`
- `N11` = `=M11-M10`
- `K12` = `=($B$8/($B$7-1))*(1-($B$8/(J12+$B$8))^($B$7-1))`
- `L12` = `=B$23*(G39+B$24*K12^2)`
- `M12` = `=SUM(K12:L12)/SUM($K$4:$L$4)`
- `N12` = `=M12-M11`
- `K13` = `=($B$8/($B$7-1))*(1-($B$8/(J13+$B$8))^($B$7-1))`
- `L13` = `=B$23*(G40+B$24*K13^2)`
- `M13` = `=SUM(K13:L13)/SUM($K$4:$L$4)`
- `N13` = `=M13-M12`

</details>

The layer factors in red above are increasing as the limit increases, which fails the consistency test, as the rate for successive layers of coverage of constant width should decrease.

You could also perform the consistency test by looking at I'(l) and I''(l):

I'(l) rescaled — I''(l) rescaled

0.386 — `=(M5-M4)/(J5-J4)*1000000`

| Q | R | S |
| --- | --- | --- |
| 0.360 | -0.257 |  |
| 0.356 | -0.044 |  |
| 0.357 | 0.015 | <--- these rows have values above I''(l)>0, but I''(l) should be <= 0 to pass the consistency test. |
| 0.361 | 0.037 |  |
| 0.365 | 0.046 |  |
| 0.370 | 0.050 |  |
| 0.376 | 0.051 |  |
| 0.381 | 0.050 |  |

<details><summary>Formulas</summary>

- `Q6` = `=(M6-M5)/(J6-J5)*1000000`
- `R6` = `=(Q6-Q5)/(J6-J5)*10000000`
- `Q7` = `=(M7-M6)/(J7-J6)*1000000`
- `R7` = `=(Q7-Q6)/(J7-J6)*10000000`
- `Q8` = `=(M8-M7)/(J8-J7)*1000000`
- `R8` = `=(Q8-Q7)/(J8-J7)*10000000`
- `Q9` = `=(M9-M8)/(J9-J8)*1000000`
- `R9` = `=(Q9-Q8)/(J9-J8)*10000000`
- `Q10` = `=(M10-M9)/(J10-J9)*1000000`
- `R10` = `=(Q10-Q9)/(J10-J9)*10000000`
- `Q11` = `=(M11-M10)/(J11-J10)*1000000`
- `R11` = `=(Q11-Q10)/(J11-J10)*10000000`
- `Q12` = `=(M12-M11)/(J12-J11)*1000000`
- `R12` = `=(Q12-Q11)/(J12-J11)*10000000`
- `Q13` = `=(M13-M12)/(J13-J12)*1000000`
- `R13` = `=(Q13-Q12)/(J13-J12)*10000000`

</details>
