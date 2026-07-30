---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 2 - Fisher Chapter 3 Q1
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 2
revised: false
points: null
parts: [a, b, c]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 2
---

# Practice Problem 2 - Fisher Chapter 3 Q1

## Question

A policy has the following coverage profile:

| B | C |
| --- | --- |
| $10,000 | Per-occurrence deductible |
| $25,000 | Aggregate deductible limit |
| $1,000,000 | Per-occurrence policy limit |

Over the course of the policy, the insured incurs the following losses, in chronological sequence:

| B | C |
| --- | --- |
| $3,000 | 1st loss |
| $8,000 | 2nd loss |
| $14,000 | 3rd loss |
| $12,000 | 4th loss |
| $18,000 | 5th loss |

Determine (i) the total insurance policy coverage, and (ii) the amount for which the insured is responsible after the insurance coverage, for each of the following:

### Part a

After the first three claims have been incurred

### Part b

After the first four claims have been incurred

### Part c

After all five claims have been incurred

## Solution

The policy occurrence limit doesn't come into relevance here since all the claims are small, so I'll ignore it in the formulas below. If it did matter, it would cap the insurer's payment on any individual claim.

Claim — Insurer pays — Insured responsibility — Agg deductible remaining

$25,000 — `=B7`

| I | J | K | L |
| --- | --- | --- | --- |
| 1 | $0 | $3,000 | $22,000 |
| 2 | $0 | $8,000 | $14,000 |
| 3 | $4,000 | $10,000 | $4,000 |

<details><summary>Formulas</summary>

- `J7` = `=B13-K7`
- `K7` = `=MIN(B$6,B13,L6)`
- `L7` = `=L6-K7`
- `J8` = `=B14-K8`
- `K8` = `=MIN(B$6,B14,L7)`
- `L8` = `=L7-K8`
- `J9` = `=B15-K9`
- `K9` = `=MIN(B$6,B15,L8)`
- `L9` = `=L8-K9`

</details>

### Part a

Cumulative — $4,000 — `=SUM(J7:J9)` — $21,000 — `=SUM(K7:K9)`

4 — $8,000 — `=B16-K12` — $4,000 — `=MIN(B$6,B16,L9)` — $0 — `=L9-K12`

### Part b

Cumulative — $12,000 — `=J12+J10` — $25,000 — `=K12+K10`

5 — $18,000 — `=B17-K15` — $0 — `=MIN(B$6,B17,L12)` — $0 — `=L12-K15`

### Part c

Cumulative — $30,000 — `=J15+J13` — $25,000 — `=K15+K13`
