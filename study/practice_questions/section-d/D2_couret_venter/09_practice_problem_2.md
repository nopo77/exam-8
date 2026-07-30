---
tia_section: D2
tia_topic: couret_venter
title: Practice Problem 2
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 2
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [couret_&_venter/]
source_workbook: tia_excel/section-d/D_2_Couret_Venter_practice_solutions.xlsx
source_sheet: Practice Problem 2
---

# Practice Problem 2

## Question

Suppose you are working on an analysis to estimate v_i^cred, the credibility weighted ratio of Fatal claim counts to TT claim counts for class i. You have sample data with the following variables:

V_h = The hazard group (containing class i) ratio of Fatal claim counts to TT claim counts V_i = The sample data ratio of Fatal claim counts to TT claim counts for class i

W_h = The hazard group (containing class i) ratio of PT claim counts to TT claim counts W_i = The sample data ratio of PT claim counts to TT claim counts for class i

X_h = The hazard group (containing class i) ratio of Major claim counts to TT claim counts X_i = The sample data ratio of Major claim counts to TT claim counts for class i

Y_h = The hazard group (containing class i) ratio of Minor claim counts to TT claim counts Y_i = The sample data ratio of Minor claim counts to TT claim counts for class i

### Part a

Write the formula for v_i^cred using one-dimensional credibility, using the hazard group as the complement of credibility.

### Part b

Write the formula for v_i^cred using multi-dimensional credibility, using the hazard group as the complement of credibility.

## Solution

### Part a

v^cred_i = Z * V_i + (1 - Z) * V_h = V_h + Z * (V_i - V_h)

### Part b

v^cred_i = V_h + b(V_i - V_h) + c(W_i - W_h) + d(X_i - X_h) + e(Y_i - Y_h)
