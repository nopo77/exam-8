---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2001 Exam 9 - Q31 revised
source: past_exam
exam_year: 2001
exam_sitting: null
exam_number: 9
question_number: 31
practice_number: null
revised: true
points: 2.0
parts: [a, b]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2001 Exam 9 - Q31 revised
---

# 2001 Exam 9 - Q31 revised

**Points:** 2

## Question

Using the information below, answer the following questions. Show all work.

| B | C |
| --- | --- |
| $400,000 | Standard Premium |
| 1.10 | Loss Conversion Factor |
| 1.05 | Tax Multiplier |
| 0.50 | Expected Loss Ratio |
| 0.37 | Basic Premium Factor |
| 1.00 | Entry Ratio at Maximum Premium |

Table of Insurance Charges

| Expected Loss Group | Expected Loss Range | Expenses and Profit Excluding Taxes | Insurance Charge at 1.00 Entry Ratio |
| --- | --- | --- | --- |
| 39 | $210,469 - $227,507 | 0.184 | 0.39 |
| 40 | $194,842 - $210,468 | 0.200 | 0.40 |
| 41 | $180,486 - $194,841 | 0.215 | 0.41 |

### Part a (1.00 pts)

Calculate the savings at the minimum.

### Part b (1.00 pts)

Calculate the minimum premium factor assuming the plan has no explicit minimum premium selected.

## Solution

### Part a

Here we want to find Psi(r_H). Normally we calculate that as part of I, which is then used to get the basic premium. Since we are given the basic premium factor, we can work backwards to get Psi(r_H). This assumes the plan is balanced (though we don't need to state that).

B/P = e/P - ( c - 1 )E[A]/P + cI/P

Our only choice to get e/P is to look it up in the table given. Obviously based on the value it is an expense ratio, not expense dollars.

Since we aren't given a State Hazard Group factor here, we can just ignore it.

E[A] — $200,000 — `=B9*B6` — -> ELG 40 from lookup table above

| J | K |
| --- | --- |
| e/P | 0.200 |
| Phi(r_G) | 0.40 |

<details><summary>Formulas</summary>

- `K13` = `=D16`
- `K14` = `=E16`

</details>

**Solve for I:** $80,000 — `=(B10-K13+(B7-1)*B9)*(B6/B7)`

I = (φ(r_G) - ψ(r_H))E[A]

**Solve for Psi(r_H):** 0.00 — `=K14-K16/K11`

### Part b

With no explicit minimum premium selected, the minimum premium occurs when there are no losses, so H = BT.

**H/P:** 0.3885 — `=B10*B8`
