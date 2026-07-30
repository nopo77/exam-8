---
tia_section: C2
tia_topic: iso_experience_rating
title: 2007 Exam 9 - Q27 revised
source: past_exam
exam_year: 2007
exam_sitting: null
exam_number: 9
question_number: 27
practice_number: null
revised: true
points: 4.0
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-c/C_2_ISO_experience_rating_practice_solutions.xlsx
source_sheet: 2007 Exam 9 - Q27 revised
---

# 2007 Exam 9 - Q27 revised

**Points:** 4

## Question

A commercial general liability policy has premises / operations exposure only.

The policy has been rated on an occurrence basis for many years and will continue to be rated on an occurrence basis when renewed.

When the policy renews it will have the following characteristics:

| B | C |
| --- | --- |
| $80,000,000 | Exposure (Sales) |
| $55,000 | Basic Limits Premium |
| $100,000 | Basic Limit Underlying Rates |
| 65% | Expected Loss Ratio |

The pricing actuary has decided to calculate the experience modification factor for this policy using the "Present Average Company Rate Method" in the ISO CGL Experience and Schedule Rating Plan based on the following data:

| Policy Term | Sales |
| --- | --- |
| Latest | $56,000,000 |
| 2nd Latest | $42,000,000 |
| 3rd Latest | $32,000,000 |

Historical Loss Information (Latest Three Terms)

| Claim # | Indemnity | ALAE | Indemnity + ALAE |
| --- | --- | --- | --- |
| 1 | $1,000 | $0 | $1,000 |
| 2 | $2,500 | $0 | $2,500 |
| 3 | $0 | $64,000 | $64,000 |
| 4 | $130,000 | $0 | $130,000 |
| Total | $133,500 | $64,000 | $197,500 |

The actuary has decided to exclude the adjustment to reflect the ultimate level of losses.

Calculate the total actual includable losses limited by the MSL (not including any development).

## Solution

**Avg rate per exposure for new policy:** 0.000687 — `=B12/B11`

Since all policies are occurrence, the PAFs will be 1. Use the Detrend factors for Rule 5C since using the Present Average Company Rate Method.

| Policy Term | Avg Rate | Sales | ELR | BLEL | PAF 13B | PAF 13C | Detrend | CSLC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Latest | 0.000687 | $56,000,000 | 65% | 25,025 | 1 | 1 | 0.949 | 23,748.725 |
| 2nd Latest | 0.000687 | $42,000,000 | 65% | 18,768.75 | 1 | 1 | 0.919 | 17,248.48125 |
| 3rd Latest | 0.000687 | $32,000,000 | 65% | 14,300 | 1 | 1 | 0.887 | 12,684.1 |
| Total |  |  |  |  |  |  |  | 53,681.30625 |

<details><summary>Formulas</summary>

- `J12` = `=L$5`
- `K12` = `=C21`
- `L12` = `=B$14`
- `M12` = `=PRODUCT(J12:L12)`
- `Q12` = `=PRODUCT(M12:P12)`
- `J13` = `=L$5`
- `K13` = `=C22`
- `L13` = `=B$14`
- `M13` = `=PRODUCT(J13:L13)`
- `Q13` = `=PRODUCT(M13:P13)`
- `J14` = `=L$5`
- `K14` = `=C23`
- `L14` = `=B$14`
- `M14` = `=PRODUCT(J14:L14)`
- `Q14` = `=PRODUCT(M14:P14)`
- `Q15` = `=SUM(Q12:Q14)`

</details>

Lookup CLSC of 53,681 in Table 16 to get

**MSL:** 95,350

| Basic Loss | Basic Loss+ALAE Lim by MSL |
| --- | --- |
| $1,000 | $1,000 |
| $2,500 | $2,500 |
| $0 | $64,000 |
| $100,000 | $95,350 |
| Total ratable loss | $162,850 |

<details><summary>Formulas</summary>

- `I27` = `=MIN(C27,$B$13)`
- `K27` = `=MIN(I27+D27,$M$18)`
- `I28` = `=MIN(C28,$B$13)`
- `K28` = `=MIN(I28+D28,$M$18)`
- `I29` = `=MIN(C29,$B$13)`
- `K29` = `=MIN(I29+D29,$M$18)`
- `I30` = `=MIN(C30,$B$13)`
- `K30` = `=MIN(I30+D30,$M$18)`
- `K31` = `=SUM(K27:K30)`

</details>
