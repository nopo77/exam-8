---
tia_section: C2
tia_topic: iso_experience_rating
title: 2004 Exam 9 - Q41 revised
source: past_exam
exam_year: 2004
exam_sitting: null
exam_number: 9
question_number: 41
practice_number: null
revised: true
points: 5.0
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-c/C_2_ISO_experience_rating_practice_solutions.xlsx
source_sheet: 2004 Exam 9 - Q41 revised
---

# 2004 Exam 9 - Q41 revised

**Points:** 5

## Question

Given the following information:

| Policy Effective Date | Policy Type | Policy Limit Indemnity Losses | Basic Limit Indemnity Losses | ALAE |
| --- | --- | --- | --- | --- |
| 2000-01-01 | Occurrence | $1,000,000 | $100,000 | $750,000 |
|  |  | $100,000 | $100,000 | $55,000 |
|  |  | $35,000 | $35,000 | $5,000 |
| 2001-01-01 | Occurrence | $800,000 | $100,000 | $50,000 |
|  |  | $12,000 | $12,000 | $60,000 |
|  |  | $10,000 | $10,000 | $50,000 |
| 2002-01-01 | Claims-made | $1,000,000 | $100,000 | $35,000 |
|  |  | $250,000 | $100,000 | $70,000 |
|  |  | $3,000 | $3,000 | $3,000 |
| 2003-01-01 | Claims-made | $500,000 | $100,000 | $10,000 |
|  |  | $15,000 | $15,000 | $750,000 |

Assume:

- All losses are valued as of July 1, 2004.
- The loss experience for the occurrence policies is fully developed.
- The risk has only premises/operations exposure.

| B | C |
| --- | --- |
| $350,000 | Basic limits premium |
| 65% | Expected loss ratio |

Using the ISO Commercial General Liability Experience Rating Plan, calculate the total includable losses for a claims-made policy effective January 1, 2005. Show all work.

## Solution

The "total includable losses" refers to the actual basic limit losses and ALAE limited by the MSL. The experience period is 1/1/2001 through 12/31/2003.

Basic Loss+ALAE Lim by MSL Prior to experience period Prior to experience period Prior to experience period

$150,000 — `=MIN(E10+F10,$K$39)`

$72,000 — `=MIN(E11+F11,$K$39)`

$60,000 — `=MIN(E12+F12,$K$39)`

$135,000 — `=MIN(E13+F13,$K$39)`

$170,000 — `=MIN(E14+F14,$K$39)`

$6,000 — `=MIN(E15+F15,$K$39)`

$110,000 — `=MIN(E16+F16,$K$39)`

$238,600 — `=MIN(E17+F17,$K$39)`

**Total:** $941,600 — `=SUM(I10:I17)`

**BLEL:** $227,500 — `=B24*B25`

From the table, we see the insured switched to claims-made coverage in 2002, so the 2002 policy was a first-year claims-made policy, and 2003 was 2nd year claims-made. Technically we don't know whether the 2004 policy was claims-made, but we do know the 2005 policy is claims-made, so we can assume 2004 was also claims-made, making 2005 a 4th year claims-made policy. So PAF 13B is based on a 4th year claims-made policy, and PAF 13C is based on the historical policy types.

Since we are told that the loss experience for the occurrence policies is fully developed, there is no expected development to add for those policies. Also, we never add expected development for claims-made policies. As such, we don't need to calculate the expected development in this problem.

| Year | BLEL | PAF 13B | PAF 13C | Detrend | CSLC |
| --- | --- | --- | --- | --- | --- |
| 2,003 | $227,500 | 1.14 | 0.67 | 0.916 | $159,168 |
| 2,002 | $227,500 | 1.14 | 0.47 | 0.876 | $106,780 |
| 2,001 | $227,500 | 1.14 | 1 | 0.839 | $217,595 |
| Total |  |  |  |  | $483,543 |

<details><summary>Formulas</summary>

- `I33` = `=I$21`
- `M33` = `=PRODUCT(I33:L33)`
- `I34` = `=I$21`
- `M34` = `=PRODUCT(I34:L34)`
- `I35` = `=I$21`
- `M35` = `=PRODUCT(I35:L35)`
- `M36` = `=SUM(M33:M35)`

</details>

Lookup CLSC of 483,543 in Table 16

**MSL:** 238,600
