---
tia_section: A2
tia_topic: loss_sensitive_rating_plans
title: Practice Problem 2
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 2
revised: false
points: null
parts: [a, b, c]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/02_ch02_risk_sharing_and_loss_sensitive_plans.md]
source_workbook: tia_excel/section-a/A_2_Loss_sensitive_rating_plans_practice_solutions.xlsx
source_sheet: Practice Problem 2
---

# Practice Problem 2

## Question

You are given the following information for a 1-year incurred retrospective rating plan effective January 1, 2016. Adjustments take place at 6 months after policy expiration and every 12 months thereafter.

| B | C |
| --- | --- |
| $120,000 | Basic Premium |
| 1.20 | Loss Conversion Factor |
| 3% | Tax Rate |
| $100,000 | Per-occurrence ratable limit |
| $400,000 | Aggregate ratable limit |
| $500,000 | Initial Premium |

Incurred as of

| B | C | D | E |
| --- | --- | --- | --- |
| Claim # | 2016-07-01 | 2017-07-01 | 2018-07-01 |
| 1 | 20,000 | 50,000 | 45,000 |
| 2 | 0 | 75,000 | 120,000 |
| 3 | 300,000 | 300,000 | 300,000 |
| 4 | 750,000 | 1,000,000 | 850,000 |
| 5 | 5,000 | 8,000 | 6,000 |
| 6 | 125,000 | 125,000 | 30,000 |

### Part a

Calculate the retrospective premium at the first adjustment.

### Part b

Calculate the retrospective premium at the second adjustment.

### Part c

Briefly mention the amount and direction of the cash flows to/from the insured at each of these adjustments.

## Solution

### Part a

Note that the first adjustment takes place at 18 months on 7/1/2017. The loss data as of 7/1/2016 is irrelevant. We need to cap individual losses first by the occurrence limit, and then possibly cap aggregate limited losses by the aggregate limit.

R = (B + cL)T

**R:** $618,557 — `=($B$8+$B$9*M23)/(1-$B$10)`

### Part b

Now we evaluate losses as of 7/1/2018.

**R:** $595,052 — `=($B$8+$B$9*N23)/(1-$B$10)`

### Part c

On 7/1/2017, the insured will pay additional premium of

On 7/1/2018, the insured will receive a refund in premium of

$118,557 — `=C39-B13`

$-23,505 — `=C43-C39`

|   | Ratable Loss at 7/1/17 | Ratable Loss at 7/1/18 |
| --- | --- | --- |
|  | 50,000 | 45,000 |
|  | 75,000 | 100,000 |
|  | 100,000 | 100,000 |
|  | 100,000 | 100,000 |
|  | 8,000 | 6,000 |
|  | 100,000 | 30,000 |
| Aggregate | 400,000 | 381,000 |

<details><summary>Formulas</summary>

- `M17` = `=MIN(D17,$B$11)`
- `N17` = `=MIN(E17,$B$11)`
- `M18` = `=MIN(D18,$B$11)`
- `N18` = `=MIN(E18,$B$11)`
- `M19` = `=MIN(D19,$B$11)`
- `N19` = `=MIN(E19,$B$11)`
- `M20` = `=MIN(D20,$B$11)`
- `N20` = `=MIN(E20,$B$11)`
- `M21` = `=MIN(D21,$B$11)`
- `N21` = `=MIN(E21,$B$11)`
- `M22` = `=MIN(D22,$B$11)`
- `N22` = `=MIN(E22,$B$11)`
- `M23` = `=MIN(SUM(M17:M22),$B$12)`
- `N23` = `=MIN(SUM(N17:N22),$B$12)`

</details>
