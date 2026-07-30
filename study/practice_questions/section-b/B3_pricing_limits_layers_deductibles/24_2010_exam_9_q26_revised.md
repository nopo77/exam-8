---
tia_section: B3
tia_topic: pricing_limits_layers_deductibles
title: 2010 Exam 9 - Q26 revised
source: past_exam
exam_year: 2010
exam_sitting: null
exam_number: 9
question_number: 26
practice_number: null
revised: true
points: 2.5
parts: []
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/6_ch6_limits_and_deductibles.md]
source_workbook: tia_excel/section-b/B_3_Pricing_limits_layers_deductibles_practice_solutions.xlsx
source_sheet: 2010 Exam 9 - Q26 revised
---

# 2010 Exam 9 - Q26 revised

**Points:** 2.5

## Question

The following claim distribution and policy information apply to a particular book of business:

| Size of Loss | Number of Claims | Total Loss Dollars |
| --- | --- | --- |
| $0 | 64 | $0 |
| $25 | 50 | $1,250 |
| $50 | 73 | $3,650 |
| $100 | 88 | $8,800 |
| $150 | 112 | $16,800 |
| $250 | 66 | $16,500 |
| $400 | 55 | $22,000 |
| $500 | 42 | $21,000 |
| Total | 550 | $90,000 |

| B | C |
| --- | --- |
| 12.222% | Given that the loss elimination ratio is equal to 12.222%, calculate the dollar amount at which a $50 |
| $50 | disappearing deductible would disappear. |

## Solution

To solve this, we will need to use a bit of trial and error. We know for certain what will happen to the loss sizes of $50 and below, but since we don't know the size at which the deductible disappears, we don't know what the effective deductible will be at levels above $50. So what we can do is see what number results in getting the total loss eliminated equal to $11,000.

You could have instead used the FORECAST function to get the deductibles between d and D:

| Claim size | Effective Deductible | Claim size | Effective Deductible |
| --- | --- | --- | --- |
| 50 | 50 | 50 | 50 |
| 150 | 0 | 250 | 0 |

| B | C | E | F |
| --- | --- | --- | --- |
| $100 | 25 | $100 | 37.5 |
|  |  | $150 | 25 |

<details><summary>Formulas</summary>

- `C32` = `=FORECAST(B32,$C$29:$C$30,$B$29:$B$30)`
- `F32` = `=FORECAST(E32,$F$29:$F$30,$E$29:$E$30)`
- `F33` = `=FORECAST(E33,$F$29:$F$30,$E$29:$E$30)`

</details>

**Loss eliminated by D:** $11,000 — `=B17*D15`

| Effective Deductible if D is |   |   |   | Loss eliminated for different values of D: |   |   |
| --- | --- | --- | --- | --- | --- | --- |
| $100 | $150 | $250 |  | $100 | $150 | $250 |
| $0 | $0 | $0 |  | $0 | $0 | $0 |
| $25 | $25 | $25 |  | $1,250 | $1,250 | $1,250 |
| $50 | $50 | $50 |  | $3,650 | $3,650 | $3,650 |
| $0 | $25 | $38 |  | $0 | $2,200 | $3,300 |
| $0 | $0 | $25 |  | $0 | $0 | $2,800 |
| $0 | $0 | $0 |  | $0 | $0 | $0 |
| $0 | $0 | $0 |  | $0 | $0 | $0 |
| $0 | $0 | $0 |  | $0 | $0 | $0 |
|  |  |  | Total | $4,900 | $7,100 | $11,000 |

<details><summary>Formulas</summary>

- `K7` = `=B7`
- `L7` = `=B7`
- `M7` = `=B7`
- `O7` = `=K7*$C7`
- `P7` = `=L7*$C7`
- `Q7` = `=M7*$C7`
- `K8` = `=B8`
- `L8` = `=B8`
- `M8` = `=B8`
- `O8` = `=K8*$C8`
- `P8` = `=L8*$C8`
- `Q8` = `=M8*$C8`
- `K9` = `=B9`
- `L9` = `=B9`
- `M9` = `=B9`
- `O9` = `=K9*$C9`
- `P9` = `=L9*$C9`
- `Q9` = `=M9*$C9`
- `K10` = `=$B$18/(K$6-$B$18)*(K$6-$B10)`
- `L10` = `=$B$18/(L$6-$B$18)*(L$6-$B10)`
- `M10` = `=$B$18/(M$6-$B$18)*(M$6-$B10)`
- `O10` = `=K10*$C10`
- `P10` = `=L10*$C10`
- `Q10` = `=M10*$C10`
- `L11` = `=$B$18/(L$6-$B$18)*(L$6-$B11)`
- `M11` = `=$B$18/(M$6-$B$18)*(M$6-$B11)`
- `O11` = `=K11*$C11`
- `P11` = `=L11*$C11`
- `Q11` = `=M11*$C11`
- `M12` = `=$B$18/(M$6-$B$18)*(M$6-$B12)`
- `O12` = `=K12*$C12`
- `P12` = `=L12*$C12`
- `Q12` = `=M12*$C12`
- `O13` = `=K13*$C13`
- `P13` = `=L13*$C13`
- `Q13` = `=M13*$C13`
- `O14` = `=K14*$C14`
- `P14` = `=L14*$C14`
- `Q14` = `=M14*$C14`
- `O15` = `=SUM(O7:O14)`
- `P15` = `=SUM(P7:P14)`
- `Q15` = `=SUM(Q7:Q14)`

</details>

At D=$250, loss eliminated matches the given LER, so deductible disappears at $250
