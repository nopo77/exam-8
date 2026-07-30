---
tia_section: D2
tia_topic: couret_venter
title: Practice Problem 6
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 6
revised: false
points: null
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [couret_&_venter/]
source_workbook: tia_excel/section-d/D_2_Couret_Venter_practice_solutions.xlsx
source_sheet: Practice Problem 6
---

# Practice Problem 6

## Question

You are given the following information related to Workers' Compensation data:

- The risk to be rated is entirely in class 1 in state S.
- Class 1 is in Hazard Group A.
- Excess Loss Factors (ELFs) are given relative to expected ground-up loss.

| B | C |
| --- | --- |
| $10,000,000 | Standard Premium for risk |
| 60% | Expected Loss Ratio for risk |

- You have the following information for class 1 and Hazard Group A in state S:

| Injury Type | HG A/State S ELF at $250,000 | Class 1/State S Claim Count Ratios to TT | HG A/State S Severity |
| --- | --- | --- | --- |
| Fatal | 14% | 0.014 | $150,000 |
| PT | 40% | 0.012 | $650,000 |
| Major | 21% | 0.141 | $240,000 |
| Minor | 0% | 0.324 | $25,000 |
| TT | 0% | 1 | $12,000 |
| Med-Only | 0% | 2.666 | $500 |

Calculate the expected losses in excess of a $250,000 limit for this risk.

## Solution

First we can come up with the injury type weights we'll need to get the class 1 ELF. Then we can weight the ELFs given with these weights to get the class 1 ELF. Finally, we can apply the ELF to the expected ground-up loss for the risk.

| Injury Type | Pure Prem per TT Count | Weights | Class ELF |
| --- | --- | --- | --- |
| Fatal | $2,100 | 3.222193% | 0.45% |
| PT | $7,800 | 11.968146% | 4.79% |
| Major | $33,840 | 51.923342% | 10.90% |
| Minor | $8,100 | 12.42846% | 0.00% |
| TT | $12,000 | 18.412533% | 0.00% |
| Med-Only | $1,333 | 2.045326% | 0.00% |
| Total | $65,173 | 100% | 16.14% |

<details><summary>Formulas</summary>

- `I7` = `=D16*E16`
- `K7` = `=I7/I$13`
- `L7` = `=K7*C16`
- `I8` = `=D17*E17`
- `K8` = `=I8/I$13`
- `L8` = `=K8*C17`
- `I9` = `=D18*E18`
- `K9` = `=I9/I$13`
- `L9` = `=K9*C18`
- `I10` = `=D19*E19`
- `K10` = `=I10/I$13`
- `L10` = `=K10*C19`
- `I11` = `=D20*E20`
- `K11` = `=I11/I$13`
- `L11` = `=K11*C20`
- `I12` = `=D21*E21`
- `K12` = `=I12/I$13`
- `L12` = `=K12*C21`
- `I13` = `=SUM(I7:I12)`
- `K13` = `=I13/I$13`
- `L13` = `=SUM(L7:L12)`

</details>

**Risk expected GU Loss:** $6,000,000 — `=B10*B11`

**Expected XS Loss:** $968,536 — `=J15*L13`
