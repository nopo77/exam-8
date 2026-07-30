---
tia_section: C1
tia_topic: experience_rating
title: 2000 Exam 9 - Q40 revised
source: past_exam
exam_year: 2000
exam_sitting: null
exam_number: 9
question_number: 40
practice_number: null
revised: true
points: 3.0
parts: [a, b, c]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/01_ch01_experience_rating.md]
source_workbook: tia_excel/section-c/C_1_Experience_rating_practice_solutions.xlsx
source_sheet: 2000 Exam 9 - Q40 revised
---

# 2000 Exam 9 - Q40 revised

**Points:** 3

## Question

There are three criteria for an effective credibility function in experience rating.

### Part a (1.00 pts)

Briefly describe in words the three criteria.

### Part b (1.00 pts)

Show the three criteria in formulas. Define all notation used.

### Part c (1.00 pts)

For each of the three criteria, determine whether or not the following credibility function satisfies that criterion. If it does not, briefly explain why.

| Expected Losses Between | Credibility |
| --- | --- |
| $0 - $5,000 | 0% |
| $5,001 - $50,000 | 50% |
| $50,001 or more | 100% |

## Solution

### Part a

i. The credibility should be between zero and one (inclusive).

ii. The credibility should not decrease as risk size increases.

iii. As the risk size increases, the percentage charge for a loss of a given size decreases.

### Part b

i. 0 <= Z <= 1 — Z is credibility, E is expected losses for the risk

ii. d/dE (Z) >= 0

iii. d/dE (Z/E) <0

### Part c

i. The credibility is always between 0 and 1 (satisfied).

ii. The credibility increases with size (satisfied).

iii. The credibility does not always have d/dE (Z/E) < 0 (does not satisfy). For example:

| E | Z | Z/E | Chg(Z/E) / Chg(E) |   |
| --- | --- | --- | --- | --- |
| 50,000 | 50% | 0.000010 |  |  |
| 50,001 | 100% | 0.000020 | 0.000010 | <-- not less than 0 |

<details><summary>Formulas</summary>

- `J15` = `=C18`
- `K15` = `=J15/I15`
- `J16` = `=C19`
- `K16` = `=J16/I16`
- `L16` = `=(K16-K15)/(I16-I15)`

</details>
