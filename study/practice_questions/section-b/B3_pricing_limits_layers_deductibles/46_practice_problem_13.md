---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: Practice Problem 13
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 13
revised: false
points: 2.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: Practice Problem 13
---

# Practice Problem 13

**Points:** 2

## Question

| Limit | Increased Limit Factor |
| --- | --- |
| $90,703 | 0.85 |
| $95,238 | 0.93 |
| $100,000 | 1.00 |
| $105,000 | 1.07 |
| $110,250 | 1.14 |
| $226,757 | 2.50 |
| $238,095 | 2.63 |
| $250,000 | 2.75 |
| $262,500 | 2.86 |
| $275,625 | 2.97 |
| $453,515 | 4.20 |
| $476,190 | 4.33 |
| $500,000 | 4.45 |
| $525,000 | 4.53 |
| $551,250 | 4.58 |

Prove that if a set of Increased Limits Factors passes the consistency test prior to inflation, that it will pass the test after inflation. Assume that the inflation rate is always positive and that ILFs are for loss only.

## Solution

0.25 points for stating the consistency test requires I''(k)<=0 0.25 points for deriving correct formula for I1(k) using pre-inflation terms 0.25 points for obtaining expressions for each of I1'(k) and I1''(k) (0.5 points total) 0.75 points for correctly demonstrating that I1'(k)>=0 and I1''(k)<=0

Since the consistency test is passed prior to inflation, we have I'(k) >= 0 and I''(k) <= 0. This means S(k) = 1 - F(k), f(k), and E[X;b] will never be negative, based on the relations below:

I(k) = E[X;k] / E[X;b]

I'(k) = S(k) / E[X;b] >= 0

I''(k) = -f(k) / E[X;b] <= 0

After inflation, we have:

I1(k) = E[X1;k] / E[X1;b] = aE[X;k/a] / aE[X;b/a] = E[X;k/a] / E[X;b/a]

Taking derivatives, we get:

I1'(k) = S(k/a) / aE[X;b/a]

I1''(k) = -f(k/a) / a^2*E[X;b/a]

a will always be positive since the inflation factor is always positive.

Since S(k), f(k), and E[X;b] are never negative for any values of k and b, we have that S(k/a), f(k/a), and E[X;b/a] will also never be negative.

This implies that I1'(k) >= 0 and I1''(k) <= 0. Thus, the consistency test will continue to be passed after inflation.
