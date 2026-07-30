---
tia_section: C2
tia_topic: iso_experience_rating
title: 2004 Exam 5 - Q43 revised
source: past_exam
exam_year: 2004
exam_sitting: null
exam_number: 5
question_number: 43
practice_number: null
revised: true
points: 3.0
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-c/C_2_ISO_experience_rating_practice_solutions.xlsx
source_sheet: 2004 Exam 5 - Q43 revised
---

# 2004 Exam 5 - Q43 revised

**Points:** 3

## Question

Using the ISO experience rating plan for a policy with premises/operations coverage and the following information, calculate the experience debit or credit. Show all work.

| Policy Period | Detrend Factors | Expected Percent of Basic Limits Loss & ALAE Unreported as of September 30, 2002 |
| --- | --- | --- |
| 1,999 | 0.78 | 15% |
| 2,000 | 0.85 | 25% |
| 2,001 | 0.94 | 40% |

- Policy being rated is a January 1, 2003 - December 31, 2003 occurrence policy.
- All policies in experience period are occurrence policies.

| B | C |
| --- | --- |
| $240,000 | Premises/operations premium for basic limits coverage |
| $300,000 | Reported loss and ALAE for experience period as of September 30, 2002 (limited by basic limits losses and MSL) |
| 0.90 | Expected experience ratio |
| 0.62 | Expected loss and ALAE ratio |
| $120,000 | Maximum single limit per occurrence |
| 0.35 | Credibility |

## Solution

Since all policies are occurrence policies, the 13B and 13C PAFs will all equal 1.

**BLEL:** $148,800 — `=B15*B18`

| Policy Period | BLEL | PAF 13B | PAF 13C | Detrend | CSLC | EER | % Unreported | Expected Dev |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1,999 | $148,800 | 1 | 1 | 0.78 | $116,064 | 0.90 | 15% | $15,669 |
| 2,000 | $148,800 | 1 | 1 | 0.85 | $126,480 | 0.90 | 25% | $28,458 |
| 2,001 | $148,800 | 1 | 1 | 0.94 | $139,872 | 0.90 | 40% | $50,354 |
| Total |  |  |  |  | $382,416 |  |  | $94,481 |

<details><summary>Formulas</summary>

- `C28` = `=C$25`
- `F28` = `=C8`
- `G28` = `=PRODUCT(C28:F28)`
- `H28` = `=$B$17`
- `I28` = `=D8`
- `J28` = `=G28*H28*I28`
- `C29` = `=C$25`
- `F29` = `=C9`
- `G29` = `=PRODUCT(C29:F29)`
- `H29` = `=$B$17`
- `I29` = `=D9`
- `J29` = `=G29*H29*I29`
- `C30` = `=C$25`
- `F30` = `=C10`
- `G30` = `=PRODUCT(C30:F30)`
- `H30` = `=$B$17`
- `I30` = `=D10`
- `J30` = `=G30*H30*I30`
- `G31` = `=SUM(G28:G30)`
- `J31` = `=SUM(J28:J30)`

</details>

**AER:** 1.03 — `=(B16+J31)/G31`

Mod — 0.051 — `=B20*(C33-B17)/B17` — Mod = Z * (AER - EER)/EER

So the mod is a 5.1% debit (a multiplicative factor of 1 + 0.051 = 1.051).
