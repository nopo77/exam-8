---
tia_section: C4
tia_topic: bailey_simon
title: 2004 Exam 9 - Q2 revised
source: past_exam
exam_year: 2004
exam_sitting: null
exam_number: 9
question_number: 2
practice_number: null
revised: true
points: 1.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [bailey_&_simon.md]
source_workbook: tia_excel/section-c/C_4_Bailey_Simon_practice_solutions.xlsx
source_sheet: 2004 Exam 9 - Q2 revised
---

# 2004 Exam 9 - Q2 revised

**Points:** 1

## Question

Given the following information:

| Class | Number of Years Since Most Recent Accident | Earned Car Years | Earned Premium at Present B Rates | Number of Claims |
| --- | --- | --- | --- | --- |
| A | 3 or more | 10,000 | $1,000,000 | 1,000 |
| X | 2 | 7,000 | $770,000 | 1,155 |
| Y | 1 | 5,000 | $625,000 | 1,250 |
| B | 0 | 2,000 | $400,000 | 1,000 |
| Total |  | 24,000 | $2,795,000 | 4,405 |

Calculate the credibility of one or more accident-free years of experience.

## Solution

Note: the terminology here for "class" is different than in the source paper. In the source paper, all of the merit ratings have different factors, but can be contained within a single broader class.

**Mod:** 0.902 — `=SUM(F7:F9)/SUM(E7:E9)/(F11/E11)`

**Credibility:** 0.098 — `=1-C19`
