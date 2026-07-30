---
tia_section: B2
tia_topic: excess_distributions
title: 2017 Exam 8 - Q14 revised
source: past_exam
exam_year: 2017
exam_sitting: null
exam_number: 8
question_number: 14
practice_number: null
revised: true
points: 2.5
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: vertical
split_confidence: clean
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: 2017 Exam 8 - Q14 revised
---

# 2017 Exam 8 - Q14 revised

**Points:** 2.5

## Question

A reinsurer has been supplied the following information from a large insurance company:

| Bottom of Claim Size Interval | Top of Claim Size Interval | Expected Number of Claims | Expected Ultimate Losses |
| --- | --- | --- | --- |
| $0 | $1,000,000 | 19,000 | $6,750,500,000 |
| $1,000,001 | $2,000,000 | 359 | $525,300,000 |
| $2,000,001 | $3,000,000 | 230 | $566,500,000 |
| $3,000,001 | $4,000,000 | 147 | $507,700,000 |
| $4,000,001 | infinity | 264 | $1,650,000,000 |
| TOTAL |  | 20,000 | $10,000,000,000 |

The reinsurer is entering into an excess of loss contract with the primary insurance company. The reinsurer will pay all losses above the insurer's per claim retention.

$5,000,000 — Insurer's per-claim retention

### Part a (1.00 pts)

Calculate the excess severity for claim sizes of $1,000,000, $2,000,000, $3,000,000, and $4,000,000.

### Part b (1.50 pts)

Calculate the reinsurer's expected losses under the proposed contract.

## Solution

### Part a

| Limit l | F(l) | E[X;l] | Excess Severity |
| --- | --- | --- | --- |
| $1,000,000 | 0.95 | $387,525 | $2,249,500 |
| $2,000,000 | 0.96795 | $427,890 | $2,249,922 |
| $3,000,000 | 0.97945 | $453,765 | $2,249,878 |
| $4,000,000 | 0.9868 | $470,300 | $2,250,000 |
| unlimited | 1 | $500,000 |  |

<details><summary>Formulas</summary>

- `C27` = `=SUM(D$7:D7)/D$12`
- `D27` = `=(SUM(E$7:E7)+SUM(D8:D$11)*B27)/D$12`
- `E27` = `=(D$31-D27)/(1-C27)`
- `C28` = `=SUM(D$7:D8)/D$12`
- `D28` = `=(SUM(E$7:E8)+SUM(D9:D$11)*B28)/D$12`
- `E28` = `=(D$31-D28)/(1-C28)`
- `C29` = `=SUM(D$7:D9)/D$12`
- `D29` = `=(SUM(E$7:E9)+SUM(D10:D$11)*B29)/D$12`
- `E29` = `=(D$31-D29)/(1-C29)`
- `C30` = `=SUM(D$7:D10)/D$12`
- `D30` = `=(SUM(E$7:E10)+SUM(D11:D$11)*B30)/D$12`
- `E30` = `=(D$31-D30)/(1-C30)`
- `C31` = `=SUM(D$7:D11)/D$12`
- `D31` = `=E12/D12`

</details>

### Part b

This was a tricky question since the source material doesn't cover this type of situation. We can calculate the expected losses in the excess layer as expected excess claim counts * expected excess claim size.

For the expected excess claim size, we don't have that at a 5M limit directly from the data. As such, we have to make an excess claim size distribution assumption to obtain it. Based on the flat excess severity from part (a), the question writer intended for excess severity to have an exponential distribution. However, since we have E[X] = $500k <> E[Xa] = $2.25M, the ground-up claim size distribution is different than the excess claim size distribution. So this means we are dealing with a mixed distribution. Based on the flat excess severities in part (a), it seems like the exponential excess claim size distribution starts at 1M (or lower perhaps, but we don't have data for that).

Assumed excess severity at 5M limit: — $2,249,825 — `=AVERAGE(E27:E30)` — this is consistent with an exponential excess claim size distribution

Next, we need to get the number of claim counts expected above a 5M limit. Again, since we know the excess claim size distribution has an exponential distribution, we can use the CDF of that distribution along with the sample claim count data to get the expected excess counts. We can split the sample/excess claim size distributions at any limit between 1M and 4M and the results will be similar. I'll show splits at both 1M and 4M limits.

Approach 1: split distributions at 1M limit

Pr(X>5M) = Pr(X>1M) * Pr(X>5M | X>1M)

| B | C | D |
| --- | --- | --- |
| Pr(X>1M) | 0.0500 | use empirical data |
| Pr(X>5M \| X>1M) | 0.1690 | use excess claim size distribution with beta = 2.25M |

<details><summary>Formulas</summary>

- `C55` = `=1-C27`
- `C56` = `=(1-EXPON.DIST(B17,1/D43,TRUE))/(1-EXPON.DIST(B27,1/D43,TRUE))`

</details>

**Pr(X>5M):** 0.0084 — `=C55*C56`

**Expected counts above 5M:** 168.99 — `=C58*D12`

**Reinsurer's expected losses:** $380,197,844 — `=C60*D43`

Approach 2: split distributions at 4M limit

Pr(X>5M) = Pr(X>4M) * Pr(X>5M | X>4M)

| B | C | D |
| --- | --- | --- |
| Pr(X>4M) | 0.0132 | use empirical data |
| Pr(X>5M \| X>4M) | 0.6412 | use excess claim size distribution with beta = 2.25M |

<details><summary>Formulas</summary>

- `C68` = `=1-C30`
- `C69` = `=(1-EXPON.DIST(B17,1/D43,TRUE))/(1-EXPON.DIST(B30,1/D43,TRUE))`

</details>

**Pr(X>5M):** 0.0085 — `=C68*C69`

**Expected counts above 5M:** 169.27 — `=C71*D12`

**Reinsurer's expected losses:** $380,818,384 — `=C73*D43`

Approach 3: rely on the memoryless property of the exponential distribution, split at 4M limit

Pr(X>5M) = Pr(X>4M) * Pr(X>5M | X>4M)

Exponential distribution has memoryless property, so Pr(X>5M | X>4M) = Pr(X>4M+1M|X>4M)=Pr(X>1M)

We can use the actual counts above 4M and then the excess claim size curve to help estimate counts above 5M.

Est counts above 5M = GU counts * Pr(X>5M) = GU counts * Pr(X>4M) * Pr(X>1M) = counts above 4M * Pr(X>1M)

**Pr(X>1M):** 0.641 — `=1-EXPON.DIST(B27,1/D43,TRUE)`

**Estimated counts above 5M:** 169.27 — `=C87*D11`

**Reinsurer's expected losses:** $380,818,384 — `=C89*D43`
