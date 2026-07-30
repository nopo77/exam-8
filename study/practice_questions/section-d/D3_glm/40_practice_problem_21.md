---
tia_section: D3
tia_topic: glm
title: Practice Problem 21
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 21
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [goldburd_et_al/]
source_workbook: tia_excel/section-d/D_3_GLM_practice_solutions.xlsx
source_sheet: Practice Problem 21
---

# Practice Problem 21

## Question

### Part a

Fully discuss why coverage related variables should not be priced using GLMs.

### Part b

Discuss how territory should be modeled in conjunction with GLMs.

## Solution

### Part a

Coverage related variables (such as deductibles or limits) in GLMs can give counterintuitive results, such as indicating a lower rate for more coverage. This could be due to correlations with other variables outside of the model, including possible selection effects (e.g., insureds self-selecting to higher limits since they know they are higher risk, underwriters forcing high risk insureds to have higher deductibles). Charging rates for coverage options that reflect anything other than pure loss elimination could lead to changes in insured behavior, which means the indicated rates based on past experience would no longer be expected to be appropriate for new policies. As such, rates for coverage options should be estimated outside of the GLM first and included in the GLM as offset terms.

### Part b

Territories are challenging in GLMs since there may be a very large number of territories, and aggregating them into a smaller number of groups may cause you to lose important information. Techniques like spatial smoothing can be used to price territories, and then territorial rates can be included in the GLM with the offset terms. However, the territory model should also be offset for the rest of the classification plan, so the process should be iterative until each model converges to an acceptable degree.
