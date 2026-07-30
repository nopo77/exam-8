---
tia_section: D2
tia_topic: couret_venter
title: Practice Problem 4
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 4
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [couret_&_venter/]
source_workbook: tia_excel/section-d/D_2_Couret_Venter_practice_solutions.xlsx
source_sheet: Practice Problem 4
---

# Practice Problem 4

## Question

Describe the steps required to perform a Quintiles Test using injury type data by hazard group.

## Solution

The following is done separately for each injury type and hazard group:

i Sort injury type relativities from the credibility procedure for all classes in the hazard group in increasing order. ii Group the classes into quintiles based on the sorted relativities. Each quintile should have about the same number of TT claims. iii Calculate the weighted average injury type relativity across all classes within each quintile and within the hazard group. Do this step for each of the 3 methods and for the holdout sample using their respective relativities. iv Calculate the SSE for each method as:

SSE=sum across quintiles(Step3Relativity_quintile / Step3Relativity_HG - Step3HoldoutRelativity_quintile / Step3HoldoutRelativity_HG)^2 v The method with the lowest SSE is deemed best for that particular injury type and all classes in that hazard group.
