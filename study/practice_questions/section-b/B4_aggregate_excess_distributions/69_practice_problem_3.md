---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: Practice Problem 3 - Fisher Chapter 3 Q2
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 3
revised: false
points: null
parts: [a, b, c, d, e, f, g]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 3
---

# Practice Problem 3 - Fisher Chapter 3 Q2

## Question

Medium Manufacturing Company (MMC) buys a General Liability policy with a large deductible. The policy has a $250K per-claim deductible, covers claims up to $1M per claim (from the first dollar, so the insured amount is actually $1M less $250K, or $750K xs $250K) with an aggregate limit on the policy of $5M and an aggregate limit on the deductible of $1M.

| B | C |
| --- | --- |
| $250,000 | Per-claim deductible |
| $1,000,000 | Per-claim coverage limit |
| $1,000,000 | Aggregate limit on deductible |
| $5,000,000 | Aggregate policy limit |

During the policy period, MMC has the following claims:

| B | C |
| --- | --- |
| $500,000 | 25 small claims that collectively cost $500K |
| $100,000 | 1 claim for $100K |
| $300,000 | 1 claim for $300K |
| $2,000,000 | 1 claim for $2M |

### Part a

What is the total loss sustained by MMC prior to any consideration of insurance?

### Part b

What is MMC's total loss responsibility under the per-claim deductible (but before consideration of the aggregate limit of the deductible)?

### Part c

How much of MMC's deductible losses are above the aggregate limit on the deductible?

### Part d

How much of the total loss is over the per-claim policy limit?

### Part e

How much loss would be paid by the insurer prior to consideration of the policy's aggregate limit?

### Part f

How much loss is over the policy's aggregate limit?

### Part g

How much in total will the insurance company need to pay for MMC's liability?

## Solution

### Part a

Total GU loss:

### Part b

Loss under per-claim ded

### Part c

Ded loss above ded limit

### Part d

Loss above per-claim limit

### Part e

Insurer pays before agg pol limit

### Part f

None (900k < 5M)

### Part g

Total insurer pays

$2,900,000 — `=SUM(B16:B19)`

$1,100,000 — `=B16+MIN(B17,B9)+MIN(B18,B9)+MIN(B19,B9)`

$100,000 — `=L4-B11`

$1,000,000 — `=B19-B10`

$900,000 — `=(B18-B9)+(MIN(B19,B10)-B9)+L6`

$900,000 — `=L10`
