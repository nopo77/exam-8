---
tia_section: D3
tia_topic: glm
title: Practice Problem 13
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 13
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
source_sheet: Practice Problem 13
---

# Practice Problem 13

## Question

Discuss 2 advantages and 2 disadvantages of modeling frequency and severity separately instead of modeling pure premium directly.

## Solution

Advantages: any 2 of:

- Modeling frequency and severity separately allows you to gain more insight and intuition

about the impact of each predictor variable.

- Each of frequency and severity separately is more stable (e.g., a variable that only impacts

frequency will look less significant in a pure premium model).

- Pure premium modeling can lead to overfitting if a predictor variable only impacts frequency

or severity but not both. For example, if a variable is significant for frequency but not for severity, the randomness of the severity of that variable might be considered to be part of the signal instead of part of the random noise.

- The Tweedie distribution in a pure premium model assumes both frequency and severity move

in the same direction, but this may not be true.

Disadvantages:

- Creating a separate model for frequency and severity takes more time since 2 separate models

need to be created instead of a single pure premium model.

- The claim level data may not be available to model frequency and severity separately.
