---
tia_section: B2
tia_topic: excess_distributions
title: 2006 Exam 9 - Q8 revised
source: past_exam
exam_year: 2006
exam_sitting: null
exam_number: 9
question_number: 8
practice_number: null
revised: true
points: 3.5
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: 2006 Exam 9 - Q8 revised
---

# 2006 Exam 9 - Q8 revised

**Points:** 3.5

## Question

A portfolio of insurance policies currently has the size of loss distribution shown below:

| Occurrence Limit | Probability that a Claim is less than the Occurrence Limit | Expected Limited Severity for the Occurrence Limit |
| --- | --- | --- |
| 100,000 | 66.5% | $45,500 |
| 125,000 | 68.9% | $56,000 |
| 150,000 | 71.1% | $65,500 |
| 175,000 | 72.9% | $74,100 |
| 200,000 | 74.5% | $82,000 |
| 225,000 | 76.0% | $89,200 |
| 250,000 | 77.4% | $95,700 |
| 300,000 | 80.0% | $107,000 |
| 400,000 | 84.3% | $124,700 |
| 500,000 | 88.2% | $138,300 |
| 750,000 | 94.4% | $162,000 |
| 800,000 | 95.4% | $165,600 |
| 900,000 | 96.3% | $172,000 |
| 1,000,000 | 97.1% | $177,700 |
| 1,250,000 | 98.8% | $181,400 |
| 1,500,000 | 99.5% | $185,500 |

40 — It is estimated that these policies will generate 40 claims in excess of $250,000 in the current year.

During the next two years, this portfolio is expected to experience the following trends (total trend for two years):

| B | C |
| --- | --- |
| 25% | Claim severity inflation |
| 44% | Exposure growth |

### Part a (1.50 pts)

Calculate the expected number of claims exceeding $250,000 after two years.

### Part b (2.00 pts)

Calculate the expected losses for this portfolio in the layer $1,000,000 excess of $250,000 after two years.

## Solution

### Part a

While it might be tempting to calculate Tau_N and apply that to the 40 excess counts given, that would not account for the exposure growth.

| K | N | O |
| --- | --- | --- |
| Current GU # claims | 177.0 |  |
| GU # claims in 2 years | 254.9 | assume no chg in frequency |

<details><summary>Formulas</summary>

- `N10` = `=B24/(1-C13)`
- `N11` = `=N10*(1+B30)`

</details>

Finally, we know the severity distribution will change due to inflation. We need to find the new probability that a claim will exceed $250,000 after 2 years, which is just 1 - F_X(a/τ) . Here, τ is 1.25, and a = $250,000.

**Pr(X after 2 years > 250,000) = Pr(X > 250,000/1.25) = Pr(X > 200,000):** 25.5% — `=1-C11`

**Expected # claims above 250k in 2 years:** 65.0 — `=Q17*N11`

### Part b

Solution 1: Calculate E[N_a after 2 years]*E[X_a after 2 years;l]

| l | l/tau | E[X;l/tau] |
| --- | --- | --- |
| $250,000 | $200,000 | $82,000 |
| $1,250,000 | $1,000,000 | $177,700 |

<details><summary>Formulas</summary>

- `L24` = `=K24/(1+$B$29)`
- `M24` = `=D11`
- `K25` = `=K24+1000000`
- `L25` = `=K25/(1+$B$29)`
- `M25` = `=D20`

</details>

**Excess severity for layer after inflation:** $469,117.65 — `=((1+$B$29)*(M25-M24))/(1-C11)`

**Total losses in layer after inflation:** $30,488,496 — `=O27*Q19`

Solution 2: Calculate E[N after 2 years]*(E[X after 2 years;a+l] - E[X after 2 years;a])

| l | l/tau | E[X;l/tau] |
| --- | --- | --- |
| $250,000 | $200,000 | $82,000 |
| $1,250,000 | $1,000,000 | $177,700 |

<details><summary>Formulas</summary>

- `L34` = `=K34/(1+$B$29)`
- `M34` = `=D11`
- `K35` = `=K34+1000000`
- `L35` = `=K35/(1+$B$29)`
- `M35` = `=D20`

</details>

**Unconditional severity for layer after inflation:** $119,625 — `=(1+B29)*(M35-M34)`

**Total losses in layer after inflation:** $30,488,496 — `=N11*O37`
