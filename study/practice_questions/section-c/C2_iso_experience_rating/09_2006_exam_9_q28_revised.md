---
tia_section: C2
tia_topic: iso_experience_rating
title: 2006 Exam 9 - Q28 revised
source: past_exam
exam_year: 2006
exam_sitting: null
exam_number: 9
question_number: 28
practice_number: null
revised: true
points: 4.5
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-c/C_2_ISO_experience_rating_practice_solutions.xlsx
source_sheet: 2006 Exam 9 - Q28 revised
---

# 2006 Exam 9 - Q28 revised

**Points:** 4.5

## Question

Al's Manufacturing Company is receiving an insurance quote for a January 1, 2007 commercial general liability claims made policy providing products and completed operations coverage only. Given the following information:

| Annual Policy Effective Date | Policy Type | Loss Development Factor |
| --- | --- | --- |
| 2005-01-01 | Claims Made | n/a |
| 2004-01-01 | Occurrence | 0.45 |
| 2003-01-01 | Occurrence | 0.35 |

Actual Insured Claim Experience:

| Claim Number | Date of Loss | Incurred Indemnity | Incurred ALAE |
| --- | --- | --- | --- |
| 1 | 2002-02-01 | $225,000 | $20,000 |
| 2 | 2004-07-02 | $0 | $200,611 |
| 3 | 2004-12-04 | $145,000 | $85,000 |
| 4 | 2005-06-07 | $185,000 | $37,000 |
| 5 | 2005-12-04 | $500,000 | $438,250 |

Assume:

- All claims are reported on the date of loss.

| B | C |
| --- | --- |
| $323,125 | Annual basic limits manual premium for the policy |
| 0.80 | Expected loss and ALAE ratio |
| 6% | Annual loss trend |

Calculate the experience modification factor.

## Solution

The 2007 policy being rated is a 3rd year claims made policy, since 2005 was the 1st claims-made policy.

The experience period will be 1/1/2003 - 12/31/2005.

Since the basic limits are not stated in the problem, I will use the normal approach of using Rule 5A for Products/Completed Operations, which gives a per occurrence limit of $100,000.

Basic Loss — Basic Loss+ALAE Lim by MSL

Prior to experience period

| H | I | J |
| --- | --- | --- |
| $0 |  | $200,611 |
| $100,000 |  | $185,000 |
| $100,000 |  | $137,000 |
| $100,000 |  | $317,500 |
|  | Total | $840,111 |

<details><summary>Formulas</summary>

- `H16` = `=MIN(D16,100000)`
- `J16` = `=MIN(H16+E16,$K$36)`
- `H17` = `=MIN(D17,100000)`
- `J17` = `=MIN(H17+E17,$K$36)`
- `H18` = `=MIN(D18,100000)`
- `J18` = `=MIN(H18+E18,$K$36)`
- `H19` = `=MIN(D19,100000)`
- `J19` = `=MIN(H19+E19,$K$36)`
- `J20` = `=SUM(J16:J19)`

</details>

I will use the annual trend  and LDFs given rather than the ISO manual for the Detrend factors and LDFs. We de-trend from the average accident date of the 2017 policy on 7/1/2017 to the average accident dates of the prior terms on 7/1/20YY.

**BLEL:** $258,500 — `=B24*B25`

| Annual Policy Effective Date | BLEL | PAF 13B | PAF 13C | Detrend | CSLC | EER | LDF | Expected Dev |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2005-01-01 | $258,500 | 1.59 | 0.22 | 0.890 | $80,476 | 0.981 | 0 | 0 |
| 2004-01-01 | $258,500 | 1.59 | 1 | 0.840 | $345,096 | 0.981 | 0.45 | 152,342.682004 |
| 2003-01-01 | $258,500 | 1.59 | 1 | 0.792 | $325,562 | 0.981 | 0.35 | 111,781.842141 |
| Total |  |  |  |  | $751,135 |  |  | $264,125 |

<details><summary>Formulas</summary>

- `I28` = `=I$25`
- `L28` = `=(1+$B$26)^(-2)`
- `M28` = `=PRODUCT(I28:L28)`
- `N28` = `=K$35`
- `P28` = `=PRODUCT(M28:O28)`
- `I29` = `=I$25`
- `L29` = `=(1+$B$26)^(-3)`
- `M29` = `=PRODUCT(I29:L29)`
- `N29` = `=K$35`
- `O29` = `=D10`
- `P29` = `=PRODUCT(M29:O29)`
- `I30` = `=I$25`
- `L30` = `=(1+$B$26)^(-4)`
- `M30` = `=PRODUCT(I30:L30)`
- `N30` = `=K$35`
- `O30` = `=D11`
- `P30` = `=PRODUCT(M30:O30)`
- `M31` = `=SUM(M28:M30)`
- `P31` = `=SUM(P28:P30)`

</details>

Lookup CLSC of 751,135 in Table 16 to get:

| J | K |
| --- | --- |
| Z | 0.68 |
| EER | 0.981 |
| MSL | 317,500 |

**AER:** 1.470 — `=(J20+P31)/M31`

Mod — 0.34 — `=K34*(I38-K35)/K35` — Mod = Z * (AER - EER)/EER

**Factor form:** 1.34 — `=1+I40`
