---
tia_section: C3
tia_topic: mahler
title: 2021 Exam 8 - Credibility
source: past_exam
exam_year: 2021
exam_sitting: null
exam_number: 8
question_number: null
practice_number: null
revised: false
points: 3.5
parts: [a, b, c, d]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [mahler/]
source_workbook: tia_excel/section-c/C_3_Mahler_practice_solutions.xlsx
source_sheet: 2021 Exam 8 - Credibility
---

# 2021 Exam 8 - Credibility

**Points:** 3.5

## Question

The following are historical loss ratios for three risks in a class:

| Year | Risk 1 | Risk 2 | Risk 3 |
| --- | --- | --- | --- |
| 2,012 | 63.1% | 72.5% | 52.3% |
| 2,013 | 59.0% | 52.6% | 48.9% |
| 2,014 | 63.5% | 69.7% | 53.9% |
| 2,015 | 74.3% | 73.8% | 50.1% |
| 2,016 | 45.9% | 61.7% | 50.9% |
| 2,017 | 42.3% | 57.8% | 46.6% |
| 2,018 | 58.9% | 67.2% | 48.6% |
| 2,019 | 60.2% | 56.5% | 50.7% |
| 2,020 | 52.8% | 58.3% | 46.1% |

**Grand Mean:** 57%

To estimate 2021 loss ratios for each risk, an actuary gives equal weight to the 3 most recent years (N = 3), and the grand mean of 57% is used as the complement (weight 1 - Z).

### Part a (1.50 pts)

Calculate the credibility, to the nearest tenth (Z = 0, 0.1, 0.2, etc...), that minimizes the mean squared error of the actuary's prediction.

### Part b (1.00 pts)

Using the Small Chance of Large Errors Criterion with an error threshold of 5%, determine if the credibility calculated in Part a is the most appropriate.

### Part c (0.75 pts)

Justify which of the above two criteria the actuary should use to determine credibility, and use that credibility to estimate the loss ratio for 2021 for each of the three risks.

### Part d (0.25 pts)

Briefly describe a test that can be used to determine if the recommendation in Part c is reasonable.

## Solution

### Part a

Here we can set up formulas to calculate the MSEs, and then iterate with the small number of credibility choices to obtain the credibility value that minimizes the MSE for the years of data where we have actual LRs.

Z — 0.6 — <-- iterate the credibility options here (Z =0, 0.1, 0.2,…, 1)

The prediction formula we are told to use is based on method 4 from the Mahler paper:

Predicted LR for year y = [(Z/3)*(LR for y-1) + (Z/3)*(LR for y-2) + (Z/3)*(LR for y-3)] + (1-Z)*Grand Mean LR Since we require 3 prior years of LRs to make a prediction with this method, the first prediction we can make is for 2015.

Below is a table showing the results for all iterations:

| Predicted LRs |   |   |   | Squared Errors |   |   |   | Z options | Resulting MSE | Portion above 5% error: |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Year | Risk 1 | Risk 2 | Risk 3 | Year | Risk 1 | Risk 2 | Risk 3 | 0.0 | 0.00835 | 77.78% |  |
| 2,015 | 59.9% | 61.8% | 53.8% | 2,015 | 0.0207 | 0.0145 | 0.0014 | 0.1 | 0.00783 | 77.78% |  |
| 2,016 | 62.2% | 62.0% | 53.4% | 2,016 | 0.0264 | 0.0000 | 0.0006 | 0.2 | 0.00741 | 77.78% |  |
| 2,017 | 59.5% | 63.8% | 53.8% | 2,017 | 0.0297 | 0.0036 | 0.0052 | 0.3 | 0.00709 | 72.22% |  |
| 2,018 | 55.3% | 61.5% | 52.3% | 2,018 | 0.0013 | 0.0033 | 0.0014 | 0.4 | 0.00685 | 83.33% |  |
| 2,019 | 52.2% | 60.1% | 52.0% | 2,019 | 0.0064 | 0.0013 | 0.0002 | 0.5 | 0.00671 | 77.78% |  |
| 2,020 | 55.1% | 59.1% | 52.0% | 2,020 | 0.0005 | 0.0001 | 0.0035 | 0.6 | 0.00667 | 72.22% | <-- minimum MSE for part (a) |
|  |  |  |  |  |  |  |  | 0.7 | 0.00672 | 72.22% |  |
|  |  |  |  | MSE: | 0.00667 |  |  | 0.8 | 0.00686 | 66.67% |  |
|  |  |  |  |  |  |  |  | 0.9 | 0.00710 | 61.11% | <-- minimum large errors for part (b) |
| Using Z = 0.6 results in the lowest MSE of 0.00667. |  |  |  |  |  |  |  | 1.0 | 0.00743 | 61.11% | <-- minimum large errors for part (b) |

<details><summary>Formulas</summary>

- `K14` = `=$K$6/3*SUM(C7:C9)+(1-$K$6)*$C$17`
- `L14` = `=$K$6/3*SUM(D7:D9)+(1-$K$6)*$C$17`
- `M14` = `=$K$6/3*SUM(E7:E9)+(1-$K$6)*$C$17`
- `P14` = `=(K14-C10)^2`
- `Q14` = `=(L14-D10)^2`
- `R14` = `=(M14-E10)^2`
- `K15` = `=$K$6/3*SUM(C8:C10)+(1-$K$6)*$C$17`
- `L15` = `=$K$6/3*SUM(D8:D10)+(1-$K$6)*$C$17`
- `M15` = `=$K$6/3*SUM(E8:E10)+(1-$K$6)*$C$17`
- `P15` = `=(K15-C11)^2`
- `Q15` = `=(L15-D11)^2`
- `R15` = `=(M15-E11)^2`
- `K16` = `=$K$6/3*SUM(C9:C11)+(1-$K$6)*$C$17`
- `L16` = `=$K$6/3*SUM(D9:D11)+(1-$K$6)*$C$17`
- `M16` = `=$K$6/3*SUM(E9:E11)+(1-$K$6)*$C$17`
- `P16` = `=(K16-C12)^2`
- `Q16` = `=(L16-D12)^2`
- `R16` = `=(M16-E12)^2`
- `K17` = `=$K$6/3*SUM(C10:C12)+(1-$K$6)*$C$17`
- `L17` = `=$K$6/3*SUM(D10:D12)+(1-$K$6)*$C$17`
- `M17` = `=$K$6/3*SUM(E10:E12)+(1-$K$6)*$C$17`
- `P17` = `=(K17-C13)^2`
- `Q17` = `=(L17-D13)^2`
- `R17` = `=(M17-E13)^2`
- `K18` = `=$K$6/3*SUM(C11:C13)+(1-$K$6)*$C$17`
- `L18` = `=$K$6/3*SUM(D11:D13)+(1-$K$6)*$C$17`
- `M18` = `=$K$6/3*SUM(E11:E13)+(1-$K$6)*$C$17`
- `P18` = `=(K18-C14)^2`
- `Q18` = `=(L18-D14)^2`
- `R18` = `=(M18-E14)^2`
- `K19` = `=$K$6/3*SUM(C12:C14)+(1-$K$6)*$C$17`
- `L19` = `=$K$6/3*SUM(D12:D14)+(1-$K$6)*$C$17`
- `M19` = `=$K$6/3*SUM(E12:E14)+(1-$K$6)*$C$17`
- `P19` = `=(K19-C15)^2`
- `Q19` = `=(L19-D15)^2`
- `R19` = `=(M19-E15)^2`
- `P21` = `=AVERAGE(P14:R19)`

</details>

### Part b

Now we can compare the predictions from part (a) against the small chance of large errors criterion. Just like in part (a), we will iterate among the Z options.

Percent Errors

| J | K | L | M | O | R |
| --- | --- | --- | --- | --- | --- |
| Year | Risk 1 | Risk 2 | Risk 3 | Portion above 5%: | 72.22% |
| 2,015 | 24.0% | 19.5% | 6.9% |  |  |
| 2,016 | 26.2% | 0.5% | 4.6% | Iterating among the Z options, Z of 0.6 from part (a) is not the most appropriate |  |
| 2,017 | 29.0% | 9.5% | 13.4% | choice for minimizing the chance of large errors. Using Z=0.9 or 1 would be optimal for this criterion. |  |
| 2,018 | 6.5% | 9.3% | 7.1% |  |  |
| 2,019 | 15.3% | 6.1% | 2.5% |  |  |
| 2,020 | 4.1% | 1.4% | 11.3% |  |  |

<details><summary>Formulas</summary>

- `R29` = `=COUNTIF(K30:M35,">0.05")/COUNT(K30:M35)`
- `K30` = `=ABS(K14-C10)/K14`
- `L30` = `=ABS(L14-D10)/L14`
- `M30` = `=ABS(M14-E10)/M14`
- `K31` = `=ABS(K15-C11)/K15`
- `L31` = `=ABS(L15-D11)/L15`
- `M31` = `=ABS(M15-E11)/M15`
- `K32` = `=ABS(K16-C12)/K16`
- `L32` = `=ABS(L16-D12)/L16`
- `M32` = `=ABS(M16-E12)/M16`
- `K33` = `=ABS(K17-C13)/K17`
- `L33` = `=ABS(L17-D13)/L17`
- `M33` = `=ABS(M17-E13)/M17`
- `K34` = `=ABS(K18-C14)/K18`
- `L34` = `=ABS(L18-D14)/L18`
- `M34` = `=ABS(M18-E14)/M18`
- `K35` = `=ABS(K19-C15)/K19`
- `L35` = `=ABS(L19-D15)/L19`
- `M35` = `=ABS(M19-E15)/M19`

</details>

### Part c

There is no single best answer here since focusing on either criterion or the Z value itself could be appropriate.

Solution 1: use Z=0.6 based on MSE since 5% threshold for SCLE seems arbitrary

I would recommend using the MSE criterion to make the decision since the 5% threshold for the SCLE approach seems arbitrary, and changing it could change the optimal Z to use.

| J | L | M | N | O |
| --- | --- | --- | --- | --- |
| Selected Z | 0.6 |  |  |  |
|  |  | Risk 1 | Risk 2 | Risk 3 |
| Predicted 2021 LRs |  | 57.2% | 59.2% | 51.9% |

<details><summary>Formulas</summary>

- `M46` = `=$L$44/3*SUM(C13:C15)+(1-$L$44)*$C$17`
- `N46` = `=$L$44/3*SUM(D13:D15)+(1-$L$44)*$C$17`
- `O46` = `=$L$44/3*SUM(E13:E15)+(1-$L$44)*$C$17`

</details>

Solution 2: use Z=0.9 based on SCLE since larger Z implies more correlation between recent years

I would recommend using the SCLE criterion since it results in a larger Z value that gives more weight to recent experience, which suggests years closer together maybe heavily correlated.

| J | L | M | N | O |
| --- | --- | --- | --- | --- |
| Selected Z | 0.9 |  |  |  |
|  |  | Risk 1 | Risk 2 | Risk 3 |
| Predicted 2021 LRs |  | 57.3% | 60.3% | 49.3% |

<details><summary>Formulas</summary>

- `M55` = `=$L$53/3*SUM(C13:C15)+(1-$L$53)*$C$17`
- `N55` = `=$L$53/3*SUM(D13:D15)+(1-$L$53)*$C$17`
- `O55` = `=$L$53/3*SUM(E13:E15)+(1-$L$53)*$C$17`

</details>

Solution 3: use Z=0.6 based on MSE since smaller Z gives more stable estimates

I would recommend using the MSE criterion since it results in a lower Z value that gives more weight to the grand mean, which means predictions will be more stable.

| J | L | M | N | O |
| --- | --- | --- | --- | --- |
| Selected Z | 0.6 |  |  |  |
|  |  | Risk 1 | Risk 2 | Risk 3 |
| Predicted 2021 LRs |  | 57.2% | 59.2% | 51.9% |

<details><summary>Formulas</summary>

- `M64` = `=$L$62/3*SUM(C13:C15)+(1-$L$62)*$C$17`
- `N64` = `=$L$62/3*SUM(D13:D15)+(1-$L$62)*$C$17`
- `O64` = `=$L$62/3*SUM(E13:E15)+(1-$L$62)*$C$17`

</details>

### Part d

The intention here was for you to discuss either the chi-squared test or the correlations test. Those tests are really for whether risk parameters are shifting over time, which is completely different than determining whether the credibility selected in part (c) was optimal. To determine optimal credibility, we would use criteria like Least Squared Error or Small Chance of Large Errors that we already used in parts (a) and (b) here. So I'll show answers that were accepted and should have been accepted here.

Solution 1 (regardless of choice in part c): reiterate that we already did the "test" in parts (a) or (b)

The choice in part (c) was already "tested" because it resulted in optimizing the criterion we used earlier in this problem.

Solution 2 (regardless of choice in part c): use Meyers/Dorweiler

We can use the Meyers/Dorweiler criterion to confirm there is no correlation between predictions and prediction errors.

Solution 3 (corresponding to solution 1 in part c): test sensitivity of error threshold for SCLE

We could test different values of the error threshold for the SCLE criterion to test the sensitivity of outcomes.

Solution 4 (model solution that I don't agree with): use chi-square or correlation test

We could test for shifting risk parameters over time using chi-squared or check correlations for pairs of years.
