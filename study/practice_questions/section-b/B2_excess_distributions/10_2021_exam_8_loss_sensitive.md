---
tia_section: B2
tia_topic: excess_distributions
title: 2021 Exam 8 - Loss Sensitive
source: past_exam
exam_year: 2021
exam_sitting: null
exam_number: 8
question_number: null
practice_number: null
revised: false
points: 3.0
parts: [a, b, c, d]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [bahnemann/5_ch5_excess_claims.md]
source_workbook: tia_excel/section-b/B_2_Excess_distributions_practice_solutions.xlsx
source_sheet: 2021 Exam 8 - Loss Sensitive
---

# 2021 Exam 8 - Loss Sensitive

**Points:** 3

## Question

A company operates two independent lines of business, line X and line Y. It seeks to contract an insurance coverage for both lines.

Information about the severity distributions for each line can be found below:

- X is uniformly distributed between 0 and 500,000.
- Y has the following distribution:

| k | Pr(Y=k) |
| --- | --- |
| 0 | 0.50 |
| 200,000 | 0.30 |
| 400,000 | 0.20 |

### Part a (0.50 pts)

An insurer agrees to write two different large deductible policies. The policy covering line X has a 250,000 deductible while the policy covering line Y has a 100,000 deductible. Calculate the insurer's expected severity for each line.

### Part b (1.50 pts)

The company asks the insurer to add a clash coverage on top of the policies described in Part a. The clash coverage will limit the combined deductible reimbursement by the company to a maximum of 300,000 on a given occurrence.

Assuming the occurrence results in one claim from each line, calculate the expected loss with the addition of the clash coverage.

### Part c (0.50 pts)

The insurer faces credit risk under the policies described in Part a. Briefly explain why this credit risk exists and how the insurer can protect against it.

### Part d (0.50 pts)

Identify an alternative Loss-Sensitive Plan that would decrease the credit risk faced by the insurer and briefly explain how it reduces credit risk when compared to the large deductible option.

## Solution

### Part a

It's very unusual to see a large probability of 0 loss for a severity distribution as we see with line Y since a severity distribution means that a claim has occurred, so a 50% chance of the claim resulting in 0 loss is unusual. That said, there's no issue with calculating the solution. Since we are already given this large probability of 0 loss in the severity distribution, I'll assume we don't need to restate the expected severity to be conditional on a non-zero loss occurring.

Net of the 250k deductible, the insurer's payment on X has a 50% chance of being 0 (for losses in the [0,250k] range), and a 50% change of being uniform on [0,250k] (for losses in the [250k,500k] range less the 250k deductible)

| Line | Expected Severity |
| --- | --- |
| X | $62,500 |
| Y | $90,000 |

<details><summary>Formulas</summary>

- `K13` = `=(250000/500000)*0+(1-250000/500000)*(500000-250000)/2`
- `K14` = `=C11*D11+(C12-100000)*D12+(C13-100000)*D13`

</details>

### Part b

The best way to think about this is to think about when the clash coverage would make a payment. The clash coverage will pay out the amount by which the combined effective deductibles exceed 300k. As such, we just need to identify when the combined deductibles will exceed 300k. Since there are infinite outcomes for X, it makes sense to start with the 3 Y outcomes and condition based on those. If the deductible on line Y is 100k, the clash coverage will only make a payment when the deductible for line X exceeds 200k. This occurs when line X has a claim of at least 200k. And since the maximum deductible for line X is 250k, the maximum the clash coverage will pay out is 50k (100k Y deductible + 250k X deductible - 300k for clash).

**Maximum clash payment:** $50,000 — `=100000+250000-300000`

| GU Loss on Y | Ded for Y | Expected clash payment | Notes |
| --- | --- | --- | --- |
| $0 | $0 | $0 | Clash never pays since only 250k deductible is needed for X. |
| $200,000 | $100,000 | $27,500 | Clash pays 0 when X<=200k, pays between 0 and 50k (25k avg) when X is between 200k and 250k, and pays 50k when X is above 250k. |
| $400,000 | $100,000 | $27,500 | Clash pays 0 when X<=200k, pays between 0 and 50k (25k avg) when X is between 200k and 250k, and pays 50k when X is above 250k. |

<details><summary>Formulas</summary>

- `J27` = `=C11`
- `K27` = `=MIN(J27,100000)`
- `J28` = `=C12`
- `K28` = `=MIN(J28,100000)`
- `L28` = `=0*K$31 + (K$32-K$31)*(L$24-0)/2 + (1-K$32)*L$24`
- `J29` = `=C13`
- `K29` = `=MIN(J29,100000)`
- `L29` = `=0*K$31 + (K$32-K$31)*(L$24-0)/2 + (1-K$32)*L$24`

</details>

| J | K |
| --- | --- |
| F_X(200k) | 0.4 |
| F_X(250k) | 0.5 |

<details><summary>Formulas</summary>

- `K31` = `=200000/500000`
- `K32` = `=250000/500000`

</details>

| J | M |
| --- | --- |
| Expected Clash Payment | $13,750 |
| Total Expected Loss | $166,250 |

<details><summary>Formulas</summary>

- `M34` = `=SUMPRODUCT(D11:D13,L27:L29)`
- `M35` = `=SUM(K13:K14,M34)`

</details>

### Part c

The insurer pays the ground-up losses first and then seeks reimbursement from the insured for amounts below the deductibles, and the insured may be unable to pay those amounts.

The insurer can protect against this by holding collateral from the insured.

### Part d

Solution 1: Self-Insured Retention

A self insured retention with an excess policy would eliminate the credit risk for the insurer since the insurer would no longer be responsible for handling and paying claims below the retention.

Solution 2: Retro rating plan

A retrospectively rated policy could reduce the credit risk if the initial premium is sufficiently high (e.g., it covers expected losses) as the insurer won't have to collect additional retro premium from the insured for low levels of losses.
