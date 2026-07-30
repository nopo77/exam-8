---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 11 - Bahnemann Problem 6.13/6.14
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 11
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: Practice Problem 11
---

# Practice Problem 11 - Bahnemann Problem 6.13/6.14

## Question

The following set of twelve (unadjusted) losses are incurred on a policy:

| B | C | D | E |
| --- | --- | --- | --- |
| 1,000 | 2,200 | 5,200 | 12,500 |
| 1,550 | 2,500 | 9,000 | 15,000 |
| 1,700 | 3,000 | 11,000 | 19,800 |

The policy has the following characteristics:

| B | C |
| --- | --- |
| 20,000 | per-claim limit |
| 2,000 | deductible |

Compute the total amount paid by the insurer (exclusive of loss adjustment expense) and the empirical loss elimination ratio (for the limit and deductible combined) for this set of claims if the deductible is:

(a) a straight deductible.

(b) a franchise deductible.

(c) Repeat the calculations for (a) and (b) if the policy instead had:

12,000 — new per-claim limit

## Solution

### Part a

**Total Loss:** 84,450 — `=SUM(B6:E8)`

**Loss Eliminated:** 22,250 — `=SUM(B6:B8)+COUNT(C6:E8)*B13`

| B | D |
| --- | --- |
| Paid by Insurer | 62,200 |
| LER | 26.35% |

<details><summary>Formulas</summary>

- `D30` = `=$D$26-D28`
- `D31` = `=D28/$D$26`

</details>

### Part b

**Loss Eliminated:** 4,250 — `=SUM(B6:B8)`

| B | D |
| --- | --- |
| Paid by Insurer | 80,200 |
| LER | 5.03% |

<details><summary>Formulas</summary>

- `D35` = `=$D$26-D33`
- `D36` = `=D33/$D$26`

</details>

### Part c

Here we can use the losses eliminated in parts (a) and (b) and add the loss eliminated by the limit.

**Loss eliminated by limit:** 11,300 — `=SUM(E6:E8)-COUNT(E6:E8)*B23`

| B | D | E | F | G |
| --- | --- | --- | --- | --- |
| Straight ded | LER | 39.7% | Paid by Insurer | 50,900 |
| Franchise ded | LER | 18.4% | Paid by Insurer | 68,900 |

<details><summary>Formulas</summary>

- `E42` = `=(D28+D40)/D26`
- `G42` = `=$D$26-D28-D40`
- `E43` = `=(D33+D40)/D26`
- `G43` = `=$D$26-D33-D40`

</details>
