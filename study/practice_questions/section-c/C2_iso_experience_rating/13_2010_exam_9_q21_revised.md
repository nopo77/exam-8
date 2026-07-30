---
tia_section: C2
tia_topic: iso_experience_rating
title: 2010 Exam 9 - Q21 revised
source: past_exam
exam_year: 2010
exam_sitting: null
exam_number: 9
question_number: 21
practice_number: null
revised: true
points: 4.0
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-c/C_2_ISO_experience_rating_practice_solutions.xlsx
source_sheet: 2010 Exam 9 - Q21 revised
---

# 2010 Exam 9 - Q21 revised

**Points:** 4

## Question

Consider the following loss experience as of June 30, 2010 under a claims-made commercial general liability policy:

| Policy Year | Claim Number | Basic Limit Indemnity | ALAE |
| --- | --- | --- | --- |
| 2,006 | 1 | $25,000 | $1,000 |
| 2,006 | 2 | $8,500 | $0 |
| 2,007 | 3 | $100,000 | $55,000 |
| 2,007 | 4 | $55,000 | $5,000 |
| 2,009 | 5 | $0 | $150,000 |
| 2,009 | 6 | $32,000 | $8,000 |

The policy being rated has the following characteristics:

- The insurance contract is always effective from January 1 to December 31.
- The insured has had claims-made coverage since 1990.
- The company's annual basic limit premium is:

| B | C |
| --- | --- |
| $100,000 | Premises / Operations |
| $25,000 | Products / Completed Operations |

68% — Expected loss ratio

Calculate the experience modification factor for a policy effective from January 1 to December 31, 2011.

## Solution

The loss amounts are already at basic limits, so we just need to add those to ALAE and cap by the MSL.

Basic Loss+ALAE Lim by MSL Outside of experience period Outside of experience period

$153,400 — `=MIN(D10+E10,E$46)`

$60,000 — `=MIN(D11+E11,E$46)`

$150,000 — `=MIN(D12+E12,E$46)`

$40,000 — `=MIN(D13+E13,E$46)`

**Total:** $403,400 — `=SUM(H10:H13)`

The experience period will be 1/1/2007 - 12/31/2009 for a 1/1/2011 upcoming policy. Note that the table in the problem doesn't show any claims for the 2008 policy year, so I assume there are no claims for that year. Since the insured has had claims-made coverage for a very long time, all the policy terms feature mature claims-made policies. Note that because the policies have been claims-made, the LDFs and thus expected development will be 0.

| Year | BLEL | PAF 13B | PAF 13C | Detrend | CSLC | LDFs all 0 since claims-made |
| --- | --- | --- | --- | --- | --- | --- |
| 2,009 | $68,000 | 1.05 | 0.94 | 0.916 | $61,478 | so no expected development |
|  | $17,000 | 1.24 | 0.72 | 0.882 | $13,387 |  |
| 2,008 | $68,000 | 1.05 | 0.94 | 0.876 | $58,794 |  |
|  | $17,000 | 1.24 | 0.72 | 0.828 | $12,567 |  |
| 2,007 | $68,000 | 1.05 | 0.94 | 0.839 | $56,310 |  |
|  | $17,000 | 1.24 | 0.72 | 0.777 | $11,793 |  |
| Total |  |  |  |  | $214,329 |  |

<details><summary>Formulas</summary>

- `C35` = `=B21*B24`
- `G35` = `=PRODUCT(C35:F35)`
- `C36` = `=B22*B24`
- `G36` = `=PRODUCT(C36:F36)`
- `C37` = `=C35`
- `G37` = `=PRODUCT(C37:F37)`
- `C38` = `=C36`
- `G38` = `=PRODUCT(C38:F38)`
- `C39` = `=C37`
- `G39` = `=PRODUCT(C39:F39)`
- `C40` = `=C38`
- `G40` = `=PRODUCT(C40:F40)`
- `G41` = `=SUM(G35:G40)`

</details>

Lookup CLSC of 214,329 in Table 16 to get:

| D | E |
| --- | --- |
| Z | 0.38 |
| EER | 0.917 |
| MSL | 153,400 |

**AER:** 1.882 — `=H14/G41`

Mod — 0.40 — `=E44*(C48-E45)/E45` — Mod = Z * (AER - EER)/EER

**Factor:** 1.40 — `=1+C50`
