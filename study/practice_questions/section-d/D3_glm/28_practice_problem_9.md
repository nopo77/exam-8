---
tia_section: D3
tia_topic: glm
title: Practice Problem 9
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 9
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [goldburd_et_al/]
source_workbook: tia_excel/section-d/D_3_GLM_practice_solutions.xlsx
source_sheet: Practice Problem 9
---

# Practice Problem 9

## Question

Briefly discuss 3 considerations in merging policy and claim data for use in a GLM.

## Solution

Any 3 of:

- Matching claims to specific vehicles/drivers (for auto) or specific coverages.
- Checking for timing differences between datasets, such as when each dataset is updated.

Timing differences can cause record matching problems.

- Is there a unique key to merge the data (e.g., policy number)? There is the potential for

orphaned claims if there is no matching policy record, or duplicating claims if there are multiple policy records.

- What level should data be aggregated before merging? This needs to be considered along the

time dimension (e.g., CY) and also the policy level versus claimant/coverage level. For commercial, location level or policy level?

- Are there fields in the data not needed for the analysis that can be discarded? Are there fields

desired that are not present that we want to try and obtain from a different data source?
