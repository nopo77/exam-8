---
tia_section: B2
tia_topic: excess_distributions
title: Practice Problem 3 - Bahnemann Problem 5.12
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 3
revised: false
points: null
parts: []
good_problem: true
has_images: true
has_examiner_report: false
layout: side_by_side
split_confidence: review
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 3
---

# Practice Problem 3 - Bahnemann Problem 5.12

## Question

Assume that a policy has the following characteristics:

5 — E[N], expected claim counts

Claim-size X has a shifted Pareto distribution with the following:

| B | C |
| --- | --- |
| 3 | α for Shifted Pareto distribution |
| 5,000 | β for Shifted Pareto distribution |

![question image](images/img_3a192b949dd4.png)

Pareto severity with parameters $\alpha, \beta$:

$$E[X; l] = \frac{\beta}{\alpha-1}\left(1 - \left(\frac{\beta}{l+\beta}\right)^{\alpha-1}\right) \qquad F(x) = 1 - \left(\frac{\beta}{x+\beta}\right)^{\alpha}$$

For each layer L defined below compute:

(a) probability PL that a claim penetrates the layer L.

(b) expected number of layer claims E[N_L].

(c) expected layer claim size E[X_L].

(d) expected aggregate layer loss E[S_L].

| Layer L | PL | E[N_L] | E[X_L] | E[S_L] |
| --- | --- | --- | --- | --- |
| [0, 100] | - | - | - | - |
| (100; 3,000) | - | - | - | - |
| (3,000; ∞) | - | - | - | - |
| [0; ∞) | 1.0000 | 5.0000 | 2,500.00 | 12,500 |

Layer L — PL — E[N_L] — E[X_L] — E[S_L]

[0, 100] (100; 3,000) (3,000; ∞)

[0; ∞) — 1.0000 — 5.0000 — 2,500.00 — 12,500

## Solution

|   | (a) | (b) | (c) | (d) |   |
| --- | --- | --- | --- | --- | --- |
| Bottom of layer L |  |  |  |  | E[X;L] |
| 0 | 1 | 5 | 97.08 | 485.390235 | 0 |
| 100 | 0.9423 | 4.712 | 1513.66 | 7,131.797265 | 97.078047 |
| 3,000 | 0.2441 | 1.221 | 4000.00 | 4,882.8125 | 1,523.4375 |

<details><summary>Formulas</summary>

- `C37` = `=($B$11/(A37+$B$11))^$B$10`
- `D37` = `=$B$6*C37`
- `E37` = `=(H38-H37)/C37`
- `F37` = `=E37*D37`
- `H37` = `=($B$11/($B$10-1))*(1-($B$11/(A37+$B$11))^($B$10-1))`
- `C38` = `=($B$11/(A38+$B$11))^$B$10`
- `D38` = `=$B$6*C38`
- `E38` = `=(H39-H38)/C38`
- `F38` = `=E38*D38`
- `H38` = `=($B$11/($B$10-1))*(1-($B$11/(A38+$B$11))^($B$10-1))`
- `C39` = `=($B$11/(A39+$B$11))^$B$10`
- `D39` = `=$B$6*C39`
- `E39` = `=(H40-H39)/C39`
- `F39` = `=E39*D39`
- `H39` = `=($B$11/($B$10-1))*(1-($B$11/(A39+$B$11))^($B$10-1))`

</details>

2,500 — `=$B$11/($B$10-1)`
