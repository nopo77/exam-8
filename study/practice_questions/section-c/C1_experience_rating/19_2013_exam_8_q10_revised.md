---
tia_section: C1
tia_topic: experience_rating
title: 2013 Exam 8 - Q10 revised
source: past_exam
exam_year: 2013
exam_sitting: null
exam_number: 8
question_number: 10
practice_number: null
revised: true
points: 1.5
parts: [a, b]
good_problem: false
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [fisher_et_al/01_ch01_experience_rating.md]
source_workbook: tia_excel/section-c/C_1_Experience_rating_practice_solutions.xlsx
source_sheet: 2013 Exam 8 - Q10 revised
---

# 2013 Exam 8 - Q10 revised

**Points:** 1.5

## Question

An actuarial analyst has experience rated five groups of policies under the current rating plan and two alternatives, Plan A and Plan B. The results are as follows:

|   | Manual Loss Ratio |   |   | Standard Loss Ratio |   |   |
| --- | --- | --- | --- | --- | --- | --- |
| Risks with | Current Plan | Proposed Plan A | Proposed Plan B | Current Plan | Proposed Plan A | Proposed Plan B |
| Lowest mod | 0.70 | 0.70 | 0.70 | 1.03 | 0.97 | 0.89 |
| Next lowest | 0.85 | 0.80 | 0.90 | 1.02 | 1.02 | 0.92 |
| Middle | 1.05 | 1.05 | 1.05 | 0.98 | 0.96 | 0.93 |
| Next highest | 1.20 | 1.15 | 1.15 | 0.97 | 1.02 | 1.06 |
| Highest mod | 1.45 | 1.55 | 1.35 | 0.96 | 1.06 | 1.11 |

### Part a (0.75 pts)

The average experience modification factor for the current plan is 1.05 and for the proposed Plan A is 0.99. The analyst says that proposed Plan A performs better because the average factor is less than 1. Critique this statement.

### Part b (0.75 pts)

The actuarial analyst recommends staying with the current plan because it has made the higher mod groups more attractive to write and it has the least standard loss ratio spread. Critique this reasoning.

## Solution

I assume each plan has been sorted by their own mods, so the same row doesn't contain the same risks across the different plans.

### Part a

While ideally the value of the average modification factor should remain close to 1 so as not to influence the overall premium level, this is not a major criteria in determining the best plan for experience rating. Instead, a plan can be evaluated by looking at the dispersion of manual loss ratios across quintiles to see how well the plan identifies risk differences, and then looking at both the trend in standard loss ratios and the variance in standard loss ratios to see how well the plan corrects for these risk differences.

### Part b

|   | Curr Plan | Plan A | Plan B |
| --- | --- | --- | --- |
| Std LR Variance | 0.00097 | 0.00168 | 0.00937 |

<details><summary>Formulas</summary>

- `C37` = `=VAR.S(F9:F13)`
- `D37` = `=VAR.S(G9:G13)`
- `E37` = `=VAR.S(H9:H13)`

</details>

The current plan does have the lowest variance in standard loss ratios, which is an important criteria in choosing the best plan. However, it has a downward trend in the standard loss ratios, which means too much credibility is being assigned, and is why the higher mod groups are more attractive to write. Ideally, you would want to see a flat trend across standard loss ratios so all risks are equally attractive to write and credibility is assigned appropriately. Based on this trend criteria, Plan A would be the best performing plan as it has no trend in the standard loss ratios.
