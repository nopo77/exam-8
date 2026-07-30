---
tia_section: C1
tia_topic: experience_rating
title: 2011 Exam 8 - Q16 revised
source: past_exam
exam_year: 2011
exam_sitting: null
exam_number: 8
question_number: 16
practice_number: null
revised: true
points: 2.5
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/01_ch01_experience_rating.md]
source_workbook: tia_excel/section-c/C_1_Experience_rating_practice_solutions.xlsx
source_sheet: 2011 Exam 8 - Q16 revised
---

# 2011 Exam 8 - Q16 revised

**Points:** 2.5

## Question

Given the following information:

| Risks with Expected Loss Size (Quintile) | Actual Losses | Expected Losses | Plan A Modified Expected Loss |
| --- | --- | --- | --- |
| Stratum 1 | $187,000 | $190,000 | $182,000 |
| Stratum 2 | $195,000 | $195,000 | $187,000 |
| Stratum 3 | $201,000 | $200,000 | $195,000 |
| Stratum 4 | $227,000 | $205,000 | $210,000 |
| Stratum 5 | $238,000 | $210,000 | $255,000 |

### Part a (2.00 pts)

Calculate the efficiency test statistic for Plan A.

### Part b (0.50 pts)

Another experience rating plan, Plan B has a efficiency test statistic of 0.50. Explain whether Plan A or Plan B has assigned more appropriate credibility.

## Solution

### Part a

Here we'll use expected losses instead of manual premium, and modified expected losses instead of standard premium.

| Actual/Modified | Actual/Expected |
| --- | --- |
| 1.027 | 0.984 |
| 1.043 | 1.000 |
| 1.031 | 1.005 |
| 1.081 | 1.107 |
| 0.933 | 1.133 |

<details><summary>Formulas</summary>

- `I7` = `=C7/E7`
- `K7` = `=C7/D7`
- `I8` = `=C8/E8`
- `K8` = `=C8/D8`
- `I9` = `=C9/E9`
- `K9` = `=C9/D9`
- `I10` = `=C10/E10`
- `K10` = `=C10/D10`
- `I11` = `=C11/E11`
- `K11` = `=C11/D11`

</details>

var — 0.002968 — `=VAR.S(I7:I11)` — 0.00475 — `=VAR.S(K7:K11)`

**Eff stat:** 0.625 — `=I13/K13`

### Part b

Plan B has assigned more appropriately credibility because the test statistic is smaller. It has eliminated more of the variance after the application of the experience mod.
