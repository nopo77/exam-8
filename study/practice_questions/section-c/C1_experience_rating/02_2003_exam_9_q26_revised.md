---
tia_section: C1
tia_topic: experience_rating
title: 2003 Exam 9 - Q26 revised
source: past_exam
exam_year: 2003
exam_sitting: null
exam_number: 9
question_number: 26
practice_number: null
revised: true
points: 5.0
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [fisher_et_al/01_ch01_experience_rating.md]
source_workbook: tia_excel/section-c/C_1_Experience_rating_practice_solutions.xlsx
source_sheet: 2003 Exam 9 - Q26 revised
---

# 2003 Exam 9 - Q26 revised

**Points:** 5

## Question

Using the following set of data for a group of large risks, determine whether the current or proposed experience rating plan is better. Assume the risks are all of the same premium size.

| Risk | Current Plan Mod | Manual Loss Ratio | Current Plan Standard Loss Ratio | Proposed Plan Mod | Proposed Plan Standard Loss Ratio |
| --- | --- | --- | --- | --- | --- |
| A | 0.80 | 0.62 | 0.78 | 0.77 | 0.81 |
| B | 0.85 | 0.70 | 0.82 | 0.92 | 0.76 |
| C | 0.87 | 0.85 | 0.98 | 0.86 | 0.99 |
| D | 0.92 | 0.82 | 0.89 | 0.80 | 1.03 |
| E | 0.94 | 0.94 | 1.00 | 0.81 | 1.16 |
| F | 0.99 | 0.95 | 0.96 | 0.88 | 1.08 |
| G | 1.00 | 0.90 | 0.90 | 1.03 | 0.87 |
| H | 1.07 | 0.99 | 0.93 | 1.05 | 0.94 |
| I | 1.09 | 1.04 | 0.95 | 0.99 | 1.05 |
| J | 1.12 | 1.01 | 0.90 | 1.08 | 0.94 |

## Solution

use SORT function and sort by 5th column (proposed mod)

Sort data by prop mod

| Risk | Current Plan Mod | Manual Loss Ratio | Current Plan Standard Loss Ratio | Proposed Plan Mod | Proposed Plan Standard Loss Ratio |
| --- | --- | --- | --- | --- | --- |
| A | 0.80 | 0.62 | 0.78 | 0.77 | 0.81 |
| D | 0.92 | 0.82 | 0.89 | 0.80 | 1.03 |
| E | 0.94 | 0.94 | 1.00 | 0.81 | 1.16 |
| C | 0.87 | 0.85 | 0.98 | 0.86 | 0.99 |
| F | 0.99 | 0.95 | 0.96 | 0.88 | 1.08 |
| B | 0.85 | 0.70 | 0.82 | 0.92 | 0.76 |
| I | 1.09 | 1.04 | 0.95 | 0.99 | 1.05 |
| G | 1.00 | 0.90 | 0.90 | 1.03 | 0.87 |
| H | 1.07 | 0.99 | 0.93 | 1.05 | 0.94 |
| J | 1.12 | 1.01 | 0.90 | 1.08 | 0.94 |

<details><summary>Formulas</summary>

- `J7` = `=B7`
- `K7` = `=C7`
- `L7` = `=D7`
- `M7` = `=E7`
- `N7` = `=F7`
- `O7` = `=G7`
- `J8` = `={SORT(B8:G17,5)}`

</details>

By "same premium size" the question is referring to manual premium, since the mods will cause the standard premium to differ between risks (that's the point of experience rating). The data is already sorted in order for the current plan mod.

| Current Plan |   |   | Proposed Plan |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
| Quintile | Manual LR | Std LR | Quintile | Manual LR | Std LR |  |
| A,B | 66.0% | 80.0% | A,D | 72.0% | 91.7% | The wtd avg Standard LR for a quintile = Sum(Losses) / Sum(Std Prem). |
| C,D | 83.5% | 93.3% | E,C | 89.5% | 107.2% | Since Sum(Std Prem) = Sum(Manual Prem * Mod), and Manual Prem is constant for all risks, we have: |
| E,F | 94.5% | 97.9% | F,B | 82.5% | 91.7% | Sum(Losses) / Sum(Std Prem) = Sum(Losses) / [Manual Prem * Sum(Mod)] = Sum(Losses / Manual Prem) / Sum(Mod) |
| G,H | 94.5% | 91.3% | I,G | 97.0% | 96.0% | So we get wtd avg Standard LR for a quintile = Sum(Manual LR) / Sum(Mod) |
| I,J | 102.5% | 92.8% | H,J | 100.0% | 93.9% |  |

<details><summary>Formulas</summary>

- `C25` = `=AVERAGE(D8:D9)`
- `D25` = `=SUM(D8:D9)/SUM(C8:C9)`
- `G25` = `=AVERAGE(L8:L9)`
- `H25` = `=SUM(L8:L9)/SUM(N8:N9)`
- `C26` = `=AVERAGE(D10:D11)`
- `D26` = `=SUM(D10:D11)/SUM(C10:C11)`
- `G26` = `=AVERAGE(L10:L11)`
- `H26` = `=SUM(L10:L11)/SUM(N10:N11)`
- `C27` = `=AVERAGE(D12:D13)`
- `D27` = `=SUM(D12:D13)/SUM(C12:C13)`
- `G27` = `=AVERAGE(L12:L13)`
- `H27` = `=SUM(L12:L13)/SUM(N12:N13)`
- `C28` = `=AVERAGE(D14:D15)`
- `D28` = `=SUM(D14:D15)/SUM(C14:C15)`
- `G28` = `=AVERAGE(L14:L15)`
- `H28` = `=SUM(L14:L15)/SUM(N14:N15)`
- `C29` = `=AVERAGE(D16:D17)`
- `D29` = `=SUM(D16:D17)/SUM(C16:C17)`
- `G29` = `=AVERAGE(L16:L17)`
- `H29` = `=SUM(L16:L17)/SUM(N16:N17)`

</details>

From here, we can compare the plans using a Quintiles Test or the Efficiency Test.

Solution 1: Quintiles Test

The current Plan has greater dispersion in manual LRs (66% to 102.5%, vs 72% to 100%), so it better identifies risk differences. The current Plan has a larger trend in standard LRs due to the low standard LR for the first quintile, so the proposed plan appears to better correct for risk differences.

Solution 2: Efficiency Test

|   | Current Plan |   | Proposed Plan |   |
| --- | --- | --- | --- | --- |
| Sample Variances: | 0.01997 | 0.004436 | 0.012833 | 0.004165 |

<details><summary>Formulas</summary>

- `C42` = `=VAR.S(C25:C29)`
- `D42` = `=VAR.S(D25:D29)`
- `G42` = `=VAR.S(G25:G29)`
- `H42` = `=VAR.S(H25:H29)`

</details>

Eff Test Stat — 0.222 — `=D42/C42` — 0.325 — `=H42/G42`

Since the current plan's statistic is lower, the current plan is more effective.
