---
tia_section: C1
tia_topic: experience_rating
title: Practice Problem 2
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 2
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/01_ch01_experience_rating.md]
source_workbook: tia_excel/section-c/C_1_Experience_rating_practice_solutions.xlsx
source_sheet: Practice Problem 2
---

# Practice Problem 2

## Question

An actuary is considering various credibility functions to use in Experience Rating a policy. The actuary has come down to 4 options. The following table shows the resulting calculated credibility for each of the options for various loss sizes (E).

Based on the results from the table, what is the best option to use to calculate the credibility? Explain why your selected option is better than each of the other methods.

Credibility

| E | Option 1 | Option 2 | Option 3 | Option 4 |
| --- | --- | --- | --- | --- |
| 100 | 72% | 30% | 85% | 55% |
| 200 | 83% | 69% | 80% | 60% |
| 300 | 93% | 75% | 76% | 66% |
| 400 | 102% | 80% | 73% | 73% |
| 500 | 110% | 83% | 71% | 81% |

## Solution

The 3 criteria for credibility are:

i. 0 <= Z <= 1

ii. d/dE (Z) >= 0

iii. d/dE (Z/E) <0

Option 4 is the best since it satisfies all 3 criteria.

Option 1: Credibility cannot exceed 100%. Option 2: The change in Z/E divided by the change in E is positive from E=100 to E=200. Option 3: Credibility cannot decrease as E increases.

| Z/E |   |   |   | Chg (Z/E) / Chg E |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Option 1 | Option 2 | Option 3 | Option 4 | Option 1 | Option 2 | Option 3 | Option 4 |
| 0.0072 | 0.0030 | 0.0085 | 0.0055 |  |  |  |  |
| 0.0042 | 0.0034 | 0.0040 | 0.0030 | -0.000030 | 0.000004 | -0.000045 | -0.000025 |
| 0.0031 | 0.0025 | 0.0025 | 0.0022 | -0.000010 | -0.000009 | -0.000015 | -0.000008 |
| 0.0026 | 0.0020 | 0.0018 | 0.0018 | -0.000006 | -0.000005 | -0.000007 | -0.000004 |
| 0.0022 | 0.0017 | 0.0014 | 0.0016 | -0.000004 | -0.000003 | -0.000004 | -0.000002 |

<details><summary>Formulas</summary>

- `J13` = `=D13/$C13`
- `K13` = `=E13/$C13`
- `L13` = `=F13/$C13`
- `M13` = `=G13/$C13`
- `J14` = `=D14/$C14`
- `K14` = `=E14/$C14`
- `L14` = `=F14/$C14`
- `M14` = `=G14/$C14`
- `O14` = `=(J14-J13)/($C14-$C13)`
- `P14` = `=(K14-K13)/($C14-$C13)`
- `Q14` = `=(L14-L13)/($C14-$C13)`
- `R14` = `=(M14-M13)/($C14-$C13)`
- `J15` = `=D15/$C15`
- `K15` = `=E15/$C15`
- `L15` = `=F15/$C15`
- `M15` = `=G15/$C15`
- `O15` = `=(J15-J14)/($C15-$C14)`
- `P15` = `=(K15-K14)/($C15-$C14)`
- `Q15` = `=(L15-L14)/($C15-$C14)`
- `R15` = `=(M15-M14)/($C15-$C14)`
- `J16` = `=D16/$C16`
- `K16` = `=E16/$C16`
- `L16` = `=F16/$C16`
- `M16` = `=G16/$C16`
- `O16` = `=(J16-J15)/($C16-$C15)`
- `P16` = `=(K16-K15)/($C16-$C15)`
- `Q16` = `=(L16-L15)/($C16-$C15)`
- `R16` = `=(M16-M15)/($C16-$C15)`
- `J17` = `=D17/$C17`
- `K17` = `=E17/$C17`
- `L17` = `=F17/$C17`
- `M17` = `=G17/$C17`
- `O17` = `=(J17-J16)/($C17-$C16)`
- `P17` = `=(K17-K16)/($C17-$C16)`
- `Q17` = `=(L17-L16)/($C17-$C16)`
- `R17` = `=(M17-M16)/($C17-$C16)`

</details>
