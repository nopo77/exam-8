---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 11
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 11
revised: false
points: 2.75
parts: [a, b, c, d, e]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [chalk_et_al/]
source_workbook: tia_excel/section-d/D_6_From_GLMs_practice_solutions.xlsx
source_sheet: Practice Problem 11
---

# Practice Problem 11

**Points:** 2.75

## Question

A commercial property insurer rates annual claim frequency per location with a filed log-link GLM whose coefficients are shown; Frame construction and Office occupancy are the base levels.

A sprinkler credit is then estimated in a second stage: a log-link GLM fit with each location's log of stage-one predicted frequency as an offset, producing a coefficient of -0.30 for sprinklered locations (non-sprinklered base).

Two risks are quoted:

Risk 1 has 12 masonry restaurant locations, all sprinklered Risk 2 has 4 frame office locations, none sprinklered

Stage-one model parameters

| Parameter | Coefficient |
| --- | --- |
| Intercept | -3.20 |
| Construction: Masonry | -0.25 |
| Construction: Fire-resistive | -0.45 |
| Occupancy: Restaurant | 0.55 |
| Occupancy: Retail | 0.20 |

| B | C |
| --- | --- |
| -0.30 | Stage-two coefficient, sprinklered |
| 12 | Risk 1 locations (masonry restaurant, sprinklered) |
| 4 | Risk 2 locations (frame office, non-sprinklered) |
| $18,000 | Average severity per claim |
| 25% | Variable expenses (% of premium) |
| $600 | Fixed expenses per policy |

### Part a (0.50 pts)

Calculate the stage-one predicted claim frequency per location for each risk.

### Part b (0.50 pts)

Calculate the offset value each risk's locations carry into the second-stage fit.

### Part c (0.75 pts)

Calculate the expected annual claim count for each risk.

### Part d (0.50 pts)

Calculate the indicated premium for Risk 1.

### Part e (0.50 pts)

Briefly describe two situations in which fixing the first-stage model through an offset is preferable to refitting all variables jointly with the stage-two variable(s).

## Solution

### Part a

The systematic equation is: ln(mu) = -3.20 - 0.25*Masonry - 0.45*Fire-resistive + 0.55*Restaurant + 0.20*Retail Remember that mu here is per location.

| Risk | Predicted freq (mu) |   |
| --- | --- | --- |
| 1 | 0.0550 | masonry, restaurant |
| 2 | 0.0408 | frame (base level), office (base level) |

<details><summary>Formulas</summary>

- `L6` = `=EXP(C17+C18+C20)`
- `L7` = `=EXP(C17)`

</details>

### Part b

The offset must sit on the scale of the linear predictor, so it is the log of the stage-one prediction.

| Risk | Offset |
| --- | --- |
| 1 | -2.90 |
| 2 | -3.20 |

<details><summary>Formulas</summary>

- `L12` = `=LN(L6)`
- `L13` = `=LN(L7)`

</details>

### Part c

The systematic equation for the second-stage model is: ln(mu) = -0.30*Sprinklered + offset from stage-one

| Risk | Stage 2 (total) predicted freq |   | Expected Counts |
| --- | --- | --- | --- |
| 1 | 0.0408 | sprinklered | 0.4891 |
| 2 | 0.0408 | not sprinklered | 0.1630 |

<details><summary>Formulas</summary>

- `L18` = `=EXP(B23+L12)`
- `O18` = `=L18*B24`
- `L19` = `=EXP(L13)`
- `O19` = `=L19*B25`

</details>

### Part d

| K | O |
| --- | --- |
| Expected Pure Premium | $8,804.64 |
| Indicated Premium | $12,539.51 |

<details><summary>Formulas</summary>

- `O21` = `=O18*B26`
- `O22` = `=(O21+B28)/(1-B27)`

</details>

### Part e

Any two of:

- If the stage two variable was an enrichment feature obtained at quote time, if it ever failed to retrieve, we could

still have a reliable prediction from the first-stage model to fall back upon.

- We could use the current rating plan as stage-one and then use stage two to just evaluate incremental

changes from the current rating plan.

- If a GLM is insufficient to model the relationship (e.g., spatial smoothing), a specialized stage two model

can handle this on top of a traditional GLM in stage one.

- The stage one model could be a filed rating plan, while a stage two model can be used to evaluate

additional information that could be used in underwriting decisions before issuing the policy.
