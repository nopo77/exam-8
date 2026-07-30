---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 1
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 1
revised: false
points: null
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: review
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 1
---

# Practice Problem 1

## Question

Given the following aggregate losses for a sample of 5 risks used to construct a Table M:

| Risk | Aggregate Loss |
| --- | --- |
| 1 | $25,000 |
| 2 | $50,000 |
| 3 | $75,000 |
| 4 | $100,000 |
| 5 | $125,000 |

$100,000 — True population expected aggregated losses per risk

Construct a Table M using this data.

Risk

1

2

3

4

5

Risk

1

2

3

4

5

## Solution

**E[A]:** $75,000 — `=AVERAGE(C7:C11)`

Since the sample average of $75,000 does not equal the expected loss of $100,000, we can either build our Table M using the $75,000 expected loss to calculate entry ratios, or we can calculate entry ratios using the $100,000 expected loss and then normalize the table by adjusting the entry ratio and charge columns. It will be much faster to just build the table using the sample average.

Using the sample average (fast way):

r

0.33 — `=C7/J$2`

0.67 — `=C8/J$2`

1.00 — `=C9/J$2`

1.33 — `=C10/J$2`

1.67 — `=C11/J$2`

| r | # above | % above | Charge |
| --- | --- | --- | --- |
| 0 | 5 | 1 | 1.00 |
| 0.33 | 4 | 0.8 | 0.67 |
| 0.67 | 3 | 0.6 | 0.40 |
| 1.00 | 2 | 0.4 | 0.20 |
| 1.33 | 1 | 0.2 | 0.07 |
| 1.67 | 0 | 0 | 0.00 |

<details><summary>Formulas</summary>

- `I19` = `=COUNTIF($I$12:$I$16,">"&H19)`
- `J19` = `=I19/5`
- `K19` = `=K20+(H20-H19)*J19`
- `H20` = `=I12`
- `I20` = `=COUNTIF($I$12:$I$16,">"&H20)`
- `J20` = `=I20/5`
- `K20` = `=K21+(H21-H20)*J20`
- `H21` = `=I13`
- `I21` = `=COUNTIF($I$12:$I$16,">"&H21)`
- `J21` = `=I21/5`
- `K21` = `=K22+(H22-H21)*J21`
- `H22` = `=I14`
- `I22` = `=COUNTIF($I$12:$I$16,">"&H22)`
- `J22` = `=I22/5`
- `K22` = `=K23+(H23-H22)*J22`
- `H23` = `=I15`
- `I23` = `=COUNTIF($I$12:$I$16,">"&H23)`
- `J23` = `=I23/5`
- `K23` = `=K24+(H24-H23)*J23`
- `H24` = `=I16`
- `I24` = `=COUNTIF($I$12:$I$16,">"&H24)`
- `J24` = `=I24/5`

</details>

Using the expected loss (long way, not recommended):

r

0.25 — `=C7/B$13`

0.50 — `=C8/B$13`

0.75 — `=C9/B$13`

1.00 — `=C10/B$13`

1.25 — `=C11/B$13`

| r | # above | % above | Charge |   |
| --- | --- | --- | --- | --- |
| 0 | 5 | 1 | 0.75 | <--- note this doesn't equal 1 |
| 0.25 | 4 | 0.8 | 0.5 |  |
| 0.50 | 3 | 0.6 | 0.3 |  |
| 0.75 | 2 | 0.4 | 0.15 |  |
| 1.00 | 1 | 0.2 | 0.05 |  |
| 1.25 | 0 | 0 | 0 |  |

<details><summary>Formulas</summary>

- `I36` = `=COUNTIF($I$29:$I$33,">"&H36)`
- `J36` = `=I36/5`
- `K36` = `=K37+(H37-H36)*J36`
- `H37` = `=I29`
- `I37` = `=COUNTIF($I$29:$I$33,">"&H37)`
- `J37` = `=I37/5`
- `K37` = `=K38+(H38-H37)*J37`
- `H38` = `=I30`
- `I38` = `=COUNTIF($I$29:$I$33,">"&H38)`
- `J38` = `=I38/5`
- `K38` = `=K39+(H39-H38)*J38`
- `H39` = `=I31`
- `I39` = `=COUNTIF($I$29:$I$33,">"&H39)`
- `J39` = `=I39/5`
- `K39` = `=K40+(H40-H39)*J39`
- `H40` = `=I32`
- `I40` = `=COUNTIF($I$29:$I$33,">"&H40)`
- `J40` = `=I40/5`
- `K40` = `=K41+(H41-H40)*J40`
- `H41` = `=I33`
- `I41` = `=COUNTIF($I$29:$I$33,">"&H41)`
- `J41` = `=I41/5`

</details>

Divide all entry ratios and φ(r) values by φ(0) = 0.75 to normalize:

| r | Charge |
| --- | --- |
| 0.00 | 1.00 |
| 0.33 | 0.67 |
| 0.67 | 0.40 |
| 1.00 | 0.20 |
| 1.33 | 0.07 |
| 1.67 | 0.00 |

<details><summary>Formulas</summary>

- `H46` = `=H36/$K$36`
- `I46` = `=K36/$K$36`
- `H47` = `=H37/$K$36`
- `I47` = `=K37/$K$36`
- `H48` = `=H38/$K$36`
- `I48` = `=K38/$K$36`
- `H49` = `=H39/$K$36`
- `I49` = `=K39/$K$36`
- `H50` = `=H40/$K$36`
- `I50` = `=K40/$K$36`
- `H51` = `=H41/$K$36`
- `I51` = `=K41/$K$36`

</details>
