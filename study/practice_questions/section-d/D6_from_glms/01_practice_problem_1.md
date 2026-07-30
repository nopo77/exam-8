---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 1
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 1
revised: false
points: 2.75
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [chalk_et_al/]
source_workbook: tia_excel/section-d/D_6_From_GLMs_practice_solutions.xlsx
source_sheet: Practice Problem 1
---

# Practice Problem 1

**Points:** 2.75

## Question

A LASSO frequency model is tuned over four penalties (0.01, 0.05, 0.10, 0.25) with 4-fold cross-validation. For each fold the table shows the validation null deviance and the model deviance at each penalty. A final holdout set, never touched during tuning, has null deviance 1,200 and model deviance 1,041 for the tuned model.

Model deviance at penalty value

| B | C | D | E | F | G |
| --- | --- | --- | --- | --- | --- |
| Fold | Null deviance | 0.01 | 0.05 | 0.10 | 0.25 |
| 1 | 800 | 688 | 684 | 685 | 694 |
| 2 | 950 | 830 | 818 | 820 | 833 |
| 3 | 700 | 596 | 601 | 600 | 608 |
| 4 | 1,050 | 908 | 897 | 901 | 916 |

| B | C |
| --- | --- |
| 1,200 | Holdout null deviance |
| 1,041 | Holdout model deviance |

### Part a (2.25 pts)

Recommend the penalty at which to deploy the model under the one-standard-error rule.

### Part b (0.50 pts)

Determine the performance figure that should be quoted for the deployed model, and quantify the error of quoting the tuning results instead.

## Solution

### Part a

Convert every fold and penalty to a pseudo-R2, average each penalty across folds, find the best, and set the acceptance threshold one standard error (of the best penalty's folds) below the best mean. The rule then keeps the simplest (largest)  penalty clearing the threshold.

Pseudo-R^2 at penalty

| K | L | M | N | O |
| --- | --- | --- | --- | --- |
| Fold | 0.01 | 0.05 | 0.10 | 0.25 |
| 1 | 0.1400 | 0.1450 | 0.1438 | 0.1325 |
| 2 | 0.1263 | 0.1389 | 0.1368 | 0.1232 |
| 3 | 0.1486 | 0.1414 | 0.1429 | 0.1314 |
| 4 | 0.1352 | 0.1457 | 0.1419 | 0.1276 |
| Average | 0.1375 | 0.1428 | 0.1413 | 0.1287 |

<details><summary>Formulas</summary>

- `L7` = `=D10`
- `M7` = `=E10`
- `N7` = `=F10`
- `O7` = `=G10`
- `K8` = `=B11`
- `L8` = `=1-D11/$C11`
- `M8` = `=1-E11/$C11`
- `N8` = `=1-F11/$C11`
- `O8` = `=1-G11/$C11`
- `K9` = `=B12`
- `L9` = `=1-D12/$C12`
- `M9` = `=1-E12/$C12`
- `N9` = `=1-F12/$C12`
- `O9` = `=1-G12/$C12`
- `K10` = `=B13`
- `L10` = `=1-D13/$C13`
- `M10` = `=1-E13/$C13`
- `N10` = `=1-F13/$C13`
- `O10` = `=1-G13/$C13`
- `K11` = `=B14`
- `L11` = `=1-D14/$C14`
- `M11` = `=1-E14/$C14`
- `N11` = `=1-F14/$C14`
- `O11` = `=1-G14/$C14`
- `L12` = `=AVERAGE(L8:L11)`
- `M12` = `=AVERAGE(M8:M11)`
- `N12` = `=AVERAGE(N8:N11)`
- `O12` = `=AVERAGE(O8:O11)`

</details>

Max (best)

| K | N | O |
| --- | --- | --- |
| SE | 0.0016 | Remember SE = STDEV / SQRT(# of folds). |
| 1 SE threshold | 0.1412 | Any penalty with a pseudo-R^2 of this or higher will still perform nearly as well. |

<details><summary>Formulas</summary>

- `N15` = `=STDEV($M$8:$M$11)/SQRT(COUNT(M8:M11))`
- `N16` = `=M12-N15`

</details>

Within 1 SE? — no — `=IF(L12>=$N$16,"yes","no")` — yes — `=IF(M12>=$N$16,"yes","no")` — yes — `=IF(N12>=$N$16,"yes","no")` — no — `=IF(O12>=$N$16,"yes","no")`

The best avg pseudo-R^2 is 0.1428 at a penalty of 0.05, and the 1 SE threshold is about 0.1412. A penalty of 0.10 also clears this threshold, and since a higher penalty results in a simpler model, select a penalty of 0.10 for the model.

### Part b

| K | N |
| --- | --- |
| Holdout pseudo-R^2 | 0.1325 |
| From cross-validation | 0.1413 |
| Error from quoting CV value | 0.0088 |

<details><summary>Formulas</summary>

- `N24` = `=1-B17/B16`
- `N25` = `=N12`
- `N26` = `=N25-N24`

</details>

Quote the holdout value of 0.1325. Quoting the CV result can be slightly over-optimistic, in this case by 0.0088.

While using cross-validation can help reduce generalization error, there can still be some over-optimism in its estimate of future performance. This can be due to distribution changes between the CV data and the (future) data used, or it can also be due to selection bias since we are choosing the "best" model based on the CV performance.
