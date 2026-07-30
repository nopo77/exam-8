---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2001 Exam 9 - Q11 revised
source: past_exam
exam_year: 2001
exam_sitting: null
exam_number: 9
question_number: 11
practice_number: null
revised: true
points: 1.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2001 Exam 9 - Q11 revised
---

# 2001 Exam 9 - Q11 revised

**Points:** 1

## Question

Based on the consistency test for Increased Limit Factors, at what limits are the increased limits factors in the the following table inconsistent?

| Limit | Increased Limits Factor |
| --- | --- |
| $25,000 | 1.00 |
| $50,000 | 1.20 |
| $100,000 | 1.40 |
| $250,000 | 1.75 |
| $500,000 | 2.10 |
| $1,000,000 | 2.90 |
| $2,000,000 | 4.00 |

## Solution

It would be sufficient to compute I'(l) and look for increases, but you could also compute I''(l) and look for positive values.

I'(l)

0.0000080 — `=(C9-C8)/(B9-B8)`

0.0000040 — `=(C10-C9)/(B10-B9)`

0.0000023 — `=(C11-C10)/(B11-B10)`

0.0000014 — `=(C12-C11)/(B12-B11)`

0.0000016 — `=(C13-C12)/(B13-B12)`

0.0000011 — `=(C14-C13)/(B14-B13)`

Test fails at $1M limit since I''(L) > 0.

Optional: I''(l) (scaled up to be readable)

-8.00 — `=(J10-J9)/(B10-B9)*100000000000`

-1.11 — `=(J11-J10)/(B11-B10)*100000000000`

-0.37 — `=(J12-J11)/(B12-B11)*100000000000`

0.04 — `=(J13-J12)/(B13-B12)*100000000000`

-0.05 — `=(J14-J13)/(B14-B13)*100000000000`
