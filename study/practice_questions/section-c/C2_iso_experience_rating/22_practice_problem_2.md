---
tia_section: C2
tia_topic: iso_experience_rating
title: Practice Problem 2
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 2
revised: false
points: 4.0
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-c/C_2_ISO_experience_rating_practice_solutions.xlsx
source_sheet: Practice Problem 2
---

# Practice Problem 2

**Points:** 4

## Question

Josh's Contracting Company is receiving an insurance quote for a January 1, 2013 commercial general liability claims-made policy providing products and completed operations coverage only. The company has the following loss experience as of September 30, 2012:

| Claim Number | Date of Loss | Incurred Indemnity | Incurred ALAE |
| --- | --- | --- | --- |
| 1 | 2008-02-02 | $50,000 | $25,000 |
| 2 | 2009-03-07 | $125,000 | $10,000 |
| 3 | 2009-06-05 | $95,000 | $100,000 |
| 4 | 2009-10-08 | $375,000 | $25,000 |
| 5 | 2010-01-22 | $4,000 | $0 |
| 6 | 2011-11-14 | $80,000 | $100,000 |
| 7 | 2012-01-02 | $50,000 | $15,000 |

Assume:

- All claims are reported on the date of loss.
- Exposures have not changed significantly for the last 10 years.
- The company switched to a claims-made policy from an occurrence policy starting with the

January 1, 2010 policy term.

| B | C |
| --- | --- |
| $250,000 | Annual basic limits manual premium for the policy |
| 0.65 | Expected loss and ALAE ratio |

Using the ISO CGL Experience and Schedule Rating Plan, calculate the experience modification factor.

## Solution

0.25 points for correct 13B PAF 0.25 points for correct 13C PAFs 0.25 points for correct Detrend factors 0.25 points for correct formula for CSLC 0.25 points for correct EER 0.25 points for correct LDFs for all 3 years (including using 0 for 2010-2011) 0.25 points for correct formula for Expected Development 0.25 points for correct Z and MSL 0.25 points for correctly capping indemnity at 100k 0.25 points for adding ALAE to basic indemnity 0.25 points for capping basic limits loss + ALAE by MSL 0.25 points for getting correct total basic loss + ALAE capped by MSL 0.25 points for correctly calculating AER 0.25 points for correctly calculating Mod 0.25 points for adding 1 to get mod in factor form

The experience period for a 1/1/2013 policy will be 1/1/2009 - 12/31/2011.

The policy being rated is a 4th year claims-made policy since 1/1/2010 was the 1st year claims-made, 2011 was 2nd, 2012 was 3rd, so 2013 is 4th. This determines the PAFs. For the LDFs, use 0 for 2010 and 2011 since they are claims-made, and use 45 months for 2009 (1/1/2009 - 9/30/2012). Obtain values in blue from the ISO manual tables.

**BLEL:** $162,500 — `=B23*B24`

| Year | Pol Type | BLEL | PAF 13B | PAF 13C | Detrend | CSLC | EER | LDF | ExpectedDev |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2,011 | 2nd yr CM | $162,500 | 1.51 | 0.35 | 0.882 | $75,747 | 0.942 | 0 | $0 |
| 2,010 | 1st yr CM | $162,500 | 1.51 | 0.22 | 0.828 | $44,698 | 0.942 | 0 | $0 |
| 2,009 | Occ | $162,500 | 1.51 | 1 | 0.777 | $190,656 | 0.942 | 0.358 | $64,296 |
| Total |  |  |  |  |  | $311,101 |  |  | $64,296 |

<details><summary>Formulas</summary>

- `K27` = `=K$24`
- `O27` = `=PRODUCT(K27:N27)`
- `P27` = `=J$34`
- `R27` = `=PRODUCT(O27:Q27)`
- `K28` = `=K$24`
- `O28` = `=PRODUCT(K28:N28)`
- `P28` = `=J$34`
- `R28` = `=PRODUCT(O28:Q28)`
- `K29` = `=K$24`
- `O29` = `=PRODUCT(K29:N29)`
- `P29` = `=J$34`
- `R29` = `=PRODUCT(O29:Q29)`
- `O30` = `=SUM(O27:O29)`
- `R30` = `=SUM(R27:R29)`

</details>

Lookup CLSC of 311,101 in Table 16 to get:

| I | J |
| --- | --- |
| Z | 0.47 |
| EER | 0.942 |
| MSL | 184,500 |

Use Rule 5A for occurrence limit of $100,000 to cap loss.

| Claim | Basic Loss | Basic Loss + ALAE capped by MSL |
| --- | --- | --- |
| 1 | prior to experience period, ignore |  |
| 2 | $100,000 | $110,000 |
| 3 | $95,000 | $184,500 |
| 4 | $100,000 | $125,000 |
| 5 | $4,000 | $4,000 |
| 6 | $80,000 | $180,000 |
| 7 | after experience period, ignore |  |
| Total |  | $603,500 |

<details><summary>Formulas</summary>

- `J41` = `=MIN(D10,100000)`
- `K41` = `=MIN(J41+E10,J$35)`
- `J42` = `=MIN(D11,100000)`
- `K42` = `=MIN(J42+E11,J$35)`
- `J43` = `=MIN(D12,100000)`
- `K43` = `=MIN(J43+E12,J$35)`
- `J44` = `=MIN(D13,100000)`
- `K44` = `=MIN(J44+E13,J$35)`
- `J45` = `=MIN(D14,100000)`
- `K45` = `=MIN(J45+E14,J$35)`
- `K47` = `=SUM(K41:K45)`

</details>

**AER:** 2.147 — `=(K47+R30)/O30`

Mod — 0.60 — `=J33*(K49-J34)/J34` — Mod = Z*(AER-EER)/EER

Mod factor — 1.60 — `=1+K51` — Remember for ISO you need to add 1 to get the mod in factor form.
