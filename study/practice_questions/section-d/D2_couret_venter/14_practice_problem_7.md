---
tia_section: D2
tia_topic: couret_venter
title: Practice Problem 7
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 7
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: review
readings: [couret_&_venter/]
source_workbook: tia_excel/section-d/D_2_Couret_Venter_practice_solutions.xlsx
source_sheet: Practice Problem 7
---

# Practice Problem 7

## Question

You are given the following output of a multi-dimensional credibility procedure for Workers' Compensation Fatal claim count ratios to Temporary Total claim counts in Hazard Group A:

| Class | Sample Class Ratio | Predicted Class Ratio | Holdout Class Ratio |
| --- | --- | --- | --- |
| 1 | 0.006 | 0.008 | 0.006 |
| 2 | 0.002 | 0.004 | 0 |
| 3 | 0.002 | 0.002 | 0.002 |
| 4 | 0.006 | 0.007 | 0.004 |
| 5 | 0.018 | 0.013 | 0.008 |
| 6 | 0.012 | 0.010 | 0.004 |

- Hazard Group A only contains 6 classes.
- All classes have equal numbers of TT claim counts in the modeling data.
- Three methods of prediction will be evaluated:

i. Using raw class data

ii. Using hazard group data

iii. Using the multi-dimensional credibility procedure

### Part a

Perform a Sum of Squared Errors test at the class level to determine which method is optimal for the hazard group for Fatal claims.

### Part b

Group classes into 3 buckets and perform a Sum of Squared Errors test to determine which method is optimal for the hazard group for Fatal claims.

| Class | Sample Class Ratio | Predicted Class Ratio | Holdout Class Ratio |
| --- | --- | --- | --- |
| 3 | 0.002 | 0.002 | 0.002 |
| 2 | 0.002 | 0.004 | 0 |
| 4 | 0.006 | 0.007 | 0.004 |
| 1 | 0.006 | 0.008 | 0.006 |
| 6 | 0.012 | 0.010 | 0.004 |
| 5 | 0.018 | 0.013 | 0.008 |

## Solution

|   | raw | HG | cred |
| --- | --- | --- | --- |
|  | 0 | 0.000003 | 0.000004 |
|  | 0.000004 | 0.000059 | 0.000016 |
|  | 0 | 0.000032 | 0 |
|  | 0.000004 | 0.000013 | 0.000009 |
|  | 0.0001 | 0 | 0.000025 |
|  | 0.000064 | 0.000013 | 0.000036 |
| SSE | 0.000172 | 0.000121 | 0.00009 |

<details><summary>Formulas</summary>

- `I9` = `=(C9-E9)^2`
- `J9` = `=($C$35-E9)^2`
- `K9` = `=(D9-E9)^2`
- `I10` = `=(C10-E10)^2`
- `J10` = `=($C$35-E10)^2`
- `K10` = `=(D10-E10)^2`
- `I11` = `=(C11-E11)^2`
- `J11` = `=($C$35-E11)^2`
- `K11` = `=(D11-E11)^2`
- `I12` = `=(C12-E12)^2`
- `J12` = `=($C$35-E12)^2`
- `K12` = `=(D12-E12)^2`
- `I13` = `=(C13-E13)^2`
- `J13` = `=($C$35-E13)^2`
- `K13` = `=(D13-E13)^2`
- `I14` = `=(C14-E14)^2`
- `J14` = `=($C$35-E14)^2`
- `K14` = `=(D14-E14)^2`
- `I15` = `=SUM(I9:I14)`
- `J15` = `=SUM(J9:J14)`
- `K15` = `=SUM(K9:K14)`

</details>

### Part a

Since each class has the same number of TT claim counts, we can take straight averages (instead of weighted averages) to get the quintile level and hazard group level ratios.

**HG avg ratio:** 0.007667 — `=AVERAGE(C9:C14)`

SSE_cred — 0.00009 — `=K15` — is lowest

Since SSE for the credibility procedure is lowest, the credibility procedure is best.

### Part b

First we need to sort the data by the predicted column. Then we can group into buckets.

Next we can normalize the table by dividing each column by the column total.

| Classes | Avg Raw Ratio | Avg Pred Ratio | Avg Holdout Ratio | Raw | Pred | Holdout | SSE_raw | SSE_HG | SSE_pred |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3,2 | 0.002 | 0.003 | 0.001 | 0.261 | 0.409 | 0.250 | 0.00012 | 0.56250 | 0.02531 |
| 4,1 | 0.006 | 0.0075 | 0.005 | 0.783 | 1.023 | 1.250 | 0.21845 | 0.06250 | 0.05165 |
| 6,5 | 0.015 | 0.0115 | 0.006 | 1.957 | 1.568 | 1.500 | 0.20841 | 0.25000 | 0.00465 |
| HG | 0.007667 | 0.007333 | 0.004 | 1.000 | 1.000 | 1.000 | 0.42698 | 0.87500 | 0.08161 |

<details><summary>Formulas</summary>

- `C54` = `=AVERAGE(C44:C45)`
- `D54` = `=AVERAGE(D44:D45)`
- `E54` = `=AVERAGE(E44:E45)`
- `G54` = `=C54/C$57`
- `H54` = `=D54/D$57`
- `I54` = `=E54/E$57`
- `J54` = `=(G54-I54)^2`
- `K54` = `=(1-I54)^2`
- `L54` = `=(H54-I54)^2`
- `C55` = `=AVERAGE(C46:C47)`
- `D55` = `=AVERAGE(D46:D47)`
- `E55` = `=AVERAGE(E46:E47)`
- `G55` = `=C55/C$57`
- `H55` = `=D55/D$57`
- `I55` = `=E55/E$57`
- `J55` = `=(G55-I55)^2`
- `K55` = `=(1-I55)^2`
- `L55` = `=(H55-I55)^2`
- `C56` = `=AVERAGE(C48:C49)`
- `D56` = `=AVERAGE(D48:D49)`
- `E56` = `=AVERAGE(E48:E49)`
- `G56` = `=C56/C$57`
- `H56` = `=D56/D$57`
- `I56` = `=E56/E$57`
- `J56` = `=(G56-I56)^2`
- `K56` = `=(1-I56)^2`
- `L56` = `=(H56-I56)^2`
- `C57` = `=AVERAGE(C44:C49)`
- `D57` = `=AVERAGE(D44:D49)`
- `E57` = `=AVERAGE(E44:E49)`
- `G57` = `=C57/C$57`
- `H57` = `=D57/D$57`
- `I57` = `=E57/E$57`
- `J57` = `=SUM(J54:J56)`
- `K57` = `=SUM(K54:K56)`
- `L57` = `=SUM(L54:L56)`

</details>

Since SSE_cred is lowest, the credibility procedure is best.
