---
tia_section: B4
tia_topic: aggregate_excess_distributions
title: 2001 Exam 9 - Q34 revised
source: past_exam
exam_year: 2001
exam_sitting: null
exam_number: 9
question_number: 34
practice_number: null
revised: true
points: 3.0
parts: [a, b]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md, fisher_et_al/04_ch04_concluding_remarks.md]
source_workbook: tia_excel/section-b/B_4_Aggregate_excess_distributions_practice_solutions.xlsx
source_sheet: 2001 Exam 9 - Q34 revised
---

# 2001 Exam 9 - Q34 revised

**Points:** 3

## Question

Some retrospectively rated policies do not balance to guaranteed cost. Ignoring any difference in risk charges between prospectively rated and retrospectively rated policies and based on the information below, answer the following questions. Show all work.

Retrospective Premium = .24 × Standard Premium + Incurred Losses

| B | C |
| --- | --- |
| 110% | Expected Loss Ratio |
| 1.01 | Minimum Premium Factor |
| 1.56 | Maximum Premium Factor |

| Entry Ratio | Charge | Savings | Entry Ratio | Charge | Savings |
| --- | --- | --- | --- | --- | --- |
| 0.10 | 0.92 | 0.02 | 0.80 | 0.46 | 0.26 |
| 0.20 | 0.86 | 0.06 | 0.90 | 0.38 | 0.28 |
| 0.30 | 0.80 | 0.10 | 1.00 | 0.30 | 0.30 |
| 0.40 | 0.74 | 0.14 | 1.10 | 0.23 | 0.33 |
| 0.50 | 0.67 | 0.17 | 1.20 | 0.14 | 0.34 |
| 0.60 | 0.60 | 0.20 | 1.30 | 0.07 | 0.37 |
| 0.70 | 0.53 | 0.23 | 1.40 | 0.03 | 0.43 |

### Part a (2.00 pts)

What is the expected ultimate retrospective premium for risks that have $100,000 of Standard Premium?

### Part b (1.00 pts)

Assume that 24% of Standard Premium is needed for expenses including loss adjustment and taxes. Compute the necessary maximum premium factor (instead of 1.56) so that the expected ultimate premium will be adequate for these risks.

## Solution

### Part a

Here we want to solve for E[R], where R is given as R = 0.24P + A and H<=R<=G Since we need E[R], we have to use the equivalent formula R = 0.24P + L, which doesn't directly depend on H and G since we can't account for those otherwise within the expected value.

E[R] = 0.24P + E[L] E[L] = E[A] - I

**E[A]:** $110,000 — `=B10*100000`

I = (Phi(r_G) - Psi(r_H))E[A]

Clearly we have a table with charges and savings, but we need the entry ratios at the max/min. We can solve for this using the formulas for G and H.

G = 0.24P + L_G = 0.24P + (r_G)(E[A]) G/P = 0.24 + (r_G)(E[A]/P)

Solve for r_G — 1.2 — `=(B12-0.24)/B10` — Phi(r_G) — 0.14 — `=F19`

H/P = 0.24 + (r_H)(E[A]/P)

r_H — 0.7 — `=(B11-0.24)/B10` — Psi(r_H) — 0.23 — `=D21`

**I:** $-9,900 — `=(N19-N23)*L9`

**E[L]:** $119,900 — `=L9-L25`

**E[R]:** $143,900 — `=0.24*100000+L27`

### Part b

For adequacy, guaranteed cost premium = expected retro prem

**GCP:** $134,000 — `=(B10+0.24)*100000`

Set this equal to E[R]=0.24P+E[L] and use the E[L] and I formulas to solve for the new Phi(r_G).

| K | L |
| --- | --- |
| E[L] | $110,000 |
| I | $0 |

<details><summary>Formulas</summary>

- `L37` = `=L33-0.24*100000`
- `L38` = `=L37-L9`

</details>

**Phi(r_G):** 0.23 — `=L38/L9+N23`

Lookup in the table in the problem to find a charge of 0.23 occurs when:

**r_G:** 1.10 — `=E18`

G/P — 1.45 — `=0.24+L44*B10` — use G/P = 0.24 + (r_G)(E[A]/P) from above
