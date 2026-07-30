---
tia_section: B2
tia_topic: excess_distributions
title: Practice Problem 5 - Bahnemann Problem 5.21
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 5
revised: false
points: null
parts: [a, b]
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: Practice Problem 5
---

# Practice Problem 5 - Bahnemann Problem 5.21

## Question

Given the following information:

Claim-size random variable X is lognormally distributed as follows:

| B | C |
| --- | --- |
| 5.9809 | μ for lognormal distribution |
| 1.80 | σ for lognormal distribution |

The claim size variable X is subject to an inflation rate of 10% per annum.

The cumulative distribution values for the lognormal distribution can be obtained using the LOGNORM.DIST spreadsheet function: F(x) = LOGNORM.DIST(x, μ, σ, TRUE)

Calculate the corresponding effective inflation rate on the excess claim counts for each of the following underlying limits:

### Part a

Underlying limit a = 3000

### Part b

Underlying limit a = 8000

## Solution

Tau_N = (1 - F_X(a/tau)) / (1 - F_X(a))

Excess count inflation rate

a — a/tau — F(a) — F(a/tau) — Tau_N - 1

### Part a

3,000 — 2,727.27 — `=B29/1.1` — 0.87 — `=LOGNORM.DIST(B29,$B$8,$B$9,TRUE)` — 0.86 — `=LOGNORM.DIST(C29,$B$8,$B$9,TRUE)` — 8.9% — `=(1-E29)/(1-D29)-1`

### Part b

8,000 — 7,272.73 — `=B30/1.1` — 0.95 — `=LOGNORM.DIST(B30,$B$8,$B$9,TRUE)` — 0.95 — `=LOGNORM.DIST(C30,$B$8,$B$9,TRUE)` — 11.5% — `=(1-E30)/(1-D30)-1`
