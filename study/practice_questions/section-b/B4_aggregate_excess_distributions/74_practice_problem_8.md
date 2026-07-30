---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 8 - Fisher Chapter 3 Q7
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 8
revised: false
points: null
parts: [a, b, c, d, e]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 8
---

# Practice Problem 8 - Fisher Chapter 3 Q7

## Question

Eight identical risks incur the following actual aggregate loss ratios, respectively:

| B | C |
| --- | --- |
| 20% | Risk 1 loss ratio |
| 40% | Risk 2 loss ratio |
| 40% | Risk 3 loss ratio |
| 60% | Risk 4 loss ratio |
| 80% | Risk 5 loss ratio |
| 80% | Risk 6 loss ratio |
| 120% | Risk 7 loss ratio |
| 200% | Risk 8 loss ratio |

Assume that the expected loss ratio for those risks is the observed average loss ratio.

### Part a

Construct a Table M showing the insurance charge for entry ratios from 0 to 3.0 in increments of 0.5.

### Part b

Calculate the Insurance Charge at a 70% loss ratio.

### Part c

Calculate the Insurance Savings at a 70% loss ratio.

### Part d

Calculate the Insurance Charge at a 110% loss ratio.

### Part e

Calculate the Insurance Savings at a 110% loss ratio.

## Solution

### Part a

Even though the question asks for increments of 0.5, we should also include rows with entry ratios in our data.

**E[A]/P:** 80% — `=AVERAGE(B6:B13)`

|   |   | Table M |   |   |   | Not needed for solution: |
| --- | --- | --- | --- | --- | --- | --- |
| Risk | r | r | # above | % above | Charge | Savings |
| 1 | 0.25 | 0.00 | 8 | 1 | 1.00 | 0.00 |
| 2 | 0.50 | 0.25 | 7 | 0.875 | 0.75 | 0.00 |
| 3 | 0.50 | 0.50 | 5 | 0.625 | 0.53 | 0.03 |
| 4 | 0.75 | 0.75 | 4 | 0.5 | 0.38 | 0.12 |
| 5 | 1.00 | 1.00 | 2 | 0.25 | 0.25 | 0.25 |
| 6 | 1.00 | 1.50 | 1 | 0.125 | 0.12 | 0.62 |
| 7 | 1.50 | 2.00 | 1 | 0.125 | 0.06 | 1.06 |
| 8 | 2.50 | 2.50 | 0 | 0 | 0.00 | 1.50 |
|  |  | 3.00 | 0 | 0 | 0.00 | 2.00 |

<details><summary>Formulas</summary>

- `I9` = `=B6/J$5`
- `M9` = `=COUNTIF($I$9:$I$16,">"&L9)`
- `N9` = `=M9/8`
- `O9` = `=O10+(L10-L9)*N9`
- `Q9` = `=O9+L9-1`
- `I10` = `=B7/J$5`
- `M10` = `=COUNTIF($I$9:$I$16,">"&L10)`
- `N10` = `=M10/8`
- `O10` = `=O11+(L11-L10)*N10`
- `Q10` = `=O10+L10-1`
- `I11` = `=B8/J$5`
- `M11` = `=COUNTIF($I$9:$I$16,">"&L11)`
- `N11` = `=M11/8`
- `O11` = `=O12+(L12-L11)*N11`
- `Q11` = `=O11+L11-1`
- `I12` = `=B9/J$5`
- `M12` = `=COUNTIF($I$9:$I$16,">"&L12)`
- `N12` = `=M12/8`
- `O12` = `=O13+(L13-L12)*N12`
- `Q12` = `=O12+L12-1`
- `I13` = `=B10/J$5`
- `M13` = `=COUNTIF($I$9:$I$16,">"&L13)`
- `N13` = `=M13/8`
- `O13` = `=O14+(L14-L13)*N13`
- `Q13` = `=O13+L13-1`
- `I14` = `=B11/J$5`
- `M14` = `=COUNTIF($I$9:$I$16,">"&L14)`
- `N14` = `=M14/8`
- `O14` = `=O15+(L15-L14)*N14`
- `Q14` = `=O14+L14-1`
- `I15` = `=B12/J$5`
- `M15` = `=COUNTIF($I$9:$I$16,">"&L15)`
- `N15` = `=M15/8`
- `O15` = `=O16+(L16-L15)*N15`
- `Q15` = `=O15+L15-1`
- `I16` = `=B13/J$5`
- `M16` = `=COUNTIF($I$9:$I$16,">"&L16)`
- `N16` = `=M16/8`
- `O16` = `=O17+(L17-L16)*N16`
- `Q16` = `=O16+L16-1`
- `M17` = `=COUNTIF($I$9:$I$16,">"&L17)`
- `N17` = `=M17/8`
- `Q17` = `=O17+L17-1`

</details>

### Part b

**r at 70% LR:** 0.875 — `=0.7/J5`

Charge — 0.3125 — `=FORECAST(K19,O12:O13,L12:L13)` — using linear interpolation from Table M

### Part c

**Savings:** 0.1875 — `=M21+K19-1`

### Part d

**r at 110% LR:** 1.375 — `=1.1/J5`

Charge — 0.1562 — `=FORECAST(K25,O13:O14,L13:L14)` — using linear interpolation from Table M

### Part e

**Savings:** 0.5312 — `=M27+K25-1`
