---
tia_section: B2
tia_topic: excess_distributions
title: Practice Problem 4 - Bahnemann Problem 5.15
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 4
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: review
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 4
---

# Practice Problem 4 - Bahnemann Problem 5.15

## Question

For the grouped data below, the indicated groups can be used to define either a sequence of claim intervals or a sequence of layers of coverage. Calculate the average claim size for each interval and each layer.

| Size Group (Interval) | # Claims in Size Group | Total Ground-up Loss for Claims in Size Group |
| --- | --- | --- |
| 0-100 | 100 | 6,000 |
| 101-500 | 300 | 95,000 |
| 501-1,000 | 240 | 145,000 |
| 1,001-2,000 | 185 | 260,000 |
| 2,001-4,000 | 140 | 450,000 |
| 4,001-5,000 | 15 | 66,000 |
| 5,001-10,000 | 20 | 150,000 |
| Total | 1,000 | 1,172,000 |

0-100 101-500 501-1,000 1,001-2,000 2,001-4,000 4,001-5,000 5,001-10,000

0-100 101-500 501-1,000 1,001-2,000 2,001-4,000 4,001-5,000 5,001-10,000

## Solution

Note that the average claim size in each interval is just the given losses divided by the given claim counts. The average claim size for an interval will of course be within that interval, since we are taking an average only from claims in that size group (e.g., for the interval 4,000-5,000, the average claim size will be between 4,000 and 5,000). When talking about layers though, we need to consider that claims larger than a given size can contribute the full amount to lower layers, and for claims in a given size interval, they only contribute to the layer the portion of their claim size that falls in the layer. The average claim size for a layer does not need to fall within the interval, but it will fall within the layer (e.g., for the layer 4,000-5,000, the maximum amount in that layer is 5,000-4,000 = 1,000, so the average claim size in the layer must be between 0 and 1,000).

Interval — Avg Size

60.0 — `=D9/C9`

316.7 — `=D10/C10`

604.2 — `=D11/C11`

1405.4 — `=D12/C12`

3214.3 — `=D13/C13`

4400.0 — `=D14/C14`

7500.0 — `=D15/C15`

Avg Size for Layers = Loss Dollars in Layer / # Claims contributing to Layer

|   | Layer | Avg Size |
| --- | --- | --- |
| 0 |  | 96 |
| 100 |  | 338.9 |
| 500 |  | 341.7 |
| 1,000 |  | 694.4 |
| 2,000 |  | 1371.4 |
| 4,000 |  | 742.9 |
| 5,000 |  | 2,500 |

<details><summary>Formulas</summary>

- `C40` = `=(D9-C9*A40+SUM(C10:$C$15)*(A41-A40))/SUM(C9:$C$15)`
- `C41` = `=(D10-C10*A41+SUM(C11:$C$15)*(A42-A41))/SUM(C10:$C$15)`
- `C42` = `=(D11-C11*A42+SUM(C12:$C$15)*(A43-A42))/SUM(C11:$C$15)`
- `C43` = `=(D12-C12*A43+SUM(C13:$C$15)*(A44-A43))/SUM(C12:$C$15)`
- `C44` = `=(D13-C13*A44+SUM(C14:$C$15)*(A45-A44))/SUM(C13:$C$15)`
- `C45` = `=(D14-C14*A45+SUM(C15:$C$15)*(A46-A45))/SUM(C14:$C$15)`
- `C46` = `=(D15- C15*A46)/C15`

</details>
