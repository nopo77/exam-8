---
tia_section: C2
tia_topic: iso_experience_rating
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
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-c/C_2_ISO_experience_rating_practice_solutions.xlsx
source_sheet: Practice Problem 1
---

# Practice Problem 1

## Question

Given the following information for a commercial general liability insured:

- All historical policies were effective January 1 to December 31.

60% — Company Expected Loss Ratio

| Policy Year | Policy Type | Per-Occurrence Limit | Annual Aggregate Limit |
| --- | --- | --- | --- |
| 2,010 | First year claims-made | $150,000 | $500,000 |
| 2,011 | Second year claims-made | $100,000 | $250,000 |
| 2,012 | Occurrence | $100,000 | $250,000 |

- The historical exposures for this policy are:

| Year | Location | Class | Exposures |
| --- | --- | --- | --- |
| 2,012 | 1 | 1,111 | 200,000 |
| 2,012 | 1 | 2,222 | 500,000 |
| 2,012 | 2 | 1,111 | 700,000 |
| 2,011 | 1 | 1,111 | 400,000 |
| 2,011 | 1 | 2,222 | 500,000 |
| 2,011 | 2 | 1,111 | 1,100,000 |
| 2,010 | 1 | 1,111 | 700,000 |
| 2,010 | 1 | 2,222 | 900,000 |
| 2,010 | 2 | 1,111 | 2,200,000 |

- The current basic limit company rates per exposure are:

| Policy Type | Subline | Basic Limits Rate |
| --- | --- | --- |
| Occurrence | Premises/Operations | $4.50 |
| Occurrence | Products/Completed Ops | $7.50 |
| First year claims-made | Premises/Operations | $0.90 |
| First year claims-made | Products/Completed Ops | $1.50 |
| Second year claims-made | Premises/Operations | $1.80 |
| Second year claims-made | Products/Completed Ops | $3.00 |
| Third and later year claims-made | Premises/Operations | $4.00 |
| Third and later year claims-made | Products/Completed Ops | $6.50 |

- Increased Limit Factors applying to all coverages on this policy are:

Aggregate Limit

| C | D | E | F |
| --- | --- | --- | --- |
| Occurrence Limit | $200,000 | $250,000 | $500,000 |
| $100,000 | 1.00 | 1.20 | 1.30 |
| $150,000 | 1.08 | 1.25 | 1.37 |

Calculate the company subject loss cost to be used for experience rating a policy effective January 1, 2014.

## Solution

The ILFs used for each subline and year should be based on the BASIC per occurrence limit of $100,000 and ACTUAL policy annual aggregate limits:

For 2012, this is $100,000 occurrence and $250,000 aggregate. ILF = 1.20. For 2011, this is $100,000 occurrence and $250,000 aggregate. ILF = 1.20. For 2010, this is $100,000 occurrence and $500,000 aggregate. ILF = 1.30.

Exposures should be summed across all classes and locations for each year. Basic limits rates are applied based on historical policy type: 2012 was occurrence, 2011 was a 2nd year claims-made, and 2010 was a 1st year claims-made. Use the Detrend factors for Rule 5C, since there was a large change in exposures and we are using the Historical Exposures at Present Company Rates method. Note that the Policy Adjustment Factors from Tables 13B and 13C are NOT applied in this method.

Sum exposures by year. Rate based on historical policy type. ILF based on historical agg limit.

| Year | Subline | Total Exposures | Rate | ILF | ELR | Detrend | CSLC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2,012 | Prem/Ops | 1,400,000 | $4.50 | 1.20 | 60% | 0.949 | $4,304,664 |
|  | Products | 1,400,000 | $7.50 | 1.20 | 60% | 0.914 | $6,909,840 |
| 2,011 | Prem/Ops | 2,000,000 | $1.80 | 1.20 | 60% | 0.919 | $2,382,048 |
|  | Products | 2,000,000 | $3.00 | 1.20 | 60% | 0.869 | $3,754,080 |
| 2,010 | Prem/Ops | 3,800,000 | $0.90 | 1.30 | 60% | 0.887 | $2,366,161 |
|  | Products | 3,800,000 | $1.50 | 1.30 | 60% | 0.821 | $3,650,166 |
| Total |  |  |  |  |  |  | $23,366,959 |

<details><summary>Formulas</summary>

- `K18` = `=SUM(E18:E20)`
- `L18` = `=E31`
- `M18` = `=E44`
- `N18` = `=B$8`
- `P18` = `=PRODUCT(K18:O18)`
- `K19` = `=K18`
- `L19` = `=E32`
- `M19` = `=M18`
- `N19` = `=B$8`
- `P19` = `=PRODUCT(K19:O19)`
- `K20` = `=SUM(E21:E23)`
- `L20` = `=E35`
- `M20` = `=M19`
- `N20` = `=B$8`
- `P20` = `=PRODUCT(K20:O20)`
- `K21` = `=K20`
- `L21` = `=E36`
- `M21` = `=M20`
- `N21` = `=B$8`
- `P21` = `=PRODUCT(K21:O21)`
- `K22` = `=SUM(E24:E26)`
- `L22` = `=E33`
- `M22` = `=F44`
- `N22` = `=B$8`
- `P22` = `=PRODUCT(K22:O22)`
- `K23` = `=K22`
- `L23` = `=E34`
- `M23` = `=M22`
- `N23` = `=B$8`
- `P23` = `=PRODUCT(K23:O23)`
- `P24` = `=SUM(P18:P23)`

</details>
