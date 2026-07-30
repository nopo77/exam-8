---
tia_section: C3
tia_topic: mahler
title: Practice Problem 4
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 4
revised: false
points: null
parts: [a, b]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [mahler/]
source_workbook: tia_excel/section-c/C_3_Mahler_practice_solutions.xlsx
source_sheet: Practice Problem 4
---

# Practice Problem 4

## Question

Given the following information:

- The following formula used will be to get estimated claim frequency:

Estimated Frequency t = Z × Actual Frequency at t-1 + (1 - Z) × Mean Frequency

- The only values of Z to be evaluated are

0.50

0.75

- The overall mean frequency is

5%

- You are given the following actual data:

| Year | Exposures | Actual Freq |
| --- | --- | --- |
| 2,016 | 50,000 | 5.02% |
| 2,017 | 50,000 | 5.15% |
| 2,018 | 100,000 | 4.42% |

### Part a

Using the least squared error criterion, determine whether the optimal credibility in this situation is Z = 0.50 or Z = 0.75.

### Part b

Using the limited fluctuation criterion with an error threshold of 13%, determine whether the optimal credibility in this situation is Z = 0.50 or Z = 0.75.

## Solution

### Part a

In the source material, there are no exposures to be concerned with since each team plays the same number of games each year, so the "exposures" don't vary over time. In theory, it likely makes sense to use a weighted sum of squares here, but I'll avoid it since it isn't in the source paper and it hasn't been tested that way. So essentially, I'll ignore the exposures column altogether.

Note that we won't have a 2016 estimate since we don't have the actual frequency for 2015 to use in the formula.

| Year | Z=0.5 Est Freq | Z=.75 Est Freq | Z=0.5 SSE | Z=0.75 SSE |
| --- | --- | --- | --- | --- |
| 2,017 | 5.010% | 5.015% | 0.0002% | 0.0002% |
| 2,018 | 5.075% | 5.113% | 0.0043% | 0.0048% |
| Total |  |  | 0.0045% | 0.0050% |

<details><summary>Formulas</summary>

- `L11` = `=$C$12*$E22+(1-$C$12)*$C$17`
- `M11` = `=$C$13*$E22+(1-$C$13)*$C$17`
- `N11` = `=($E23-L11)^2`
- `O11` = `=($E23-M11)^2`
- `L12` = `=$C$12*$E23+(1-$C$12)*$C$17`
- `M12` = `=$C$13*$E23+(1-$C$13)*$C$17`
- `N12` = `=(E24-L12)^2`
- `O12` = `=($E24-M12)^2`
- `N13` = `=SUM(N11:N12)`
- `O13` = `=SUM(O11:O12)`

</details>

We can already conclude that the SSE is lower for Z=0.50 so it is preferred, but I'll go ahead and calculate the MSE by dividing by the number of observations, which is 2 in this case.

| K | L |
| --- | --- |
| Z=0.5 MSE | 0.0022% |
| Z=0.75 MSE | 0.0025% |

<details><summary>Formulas</summary>

- `L18` = `=N13/2`
- `L19` = `=O13/2`

</details>

Since MSE is lower for Z of 0.50, select Z = 0.50 as optimal credibility.

### Part b

We already have our estimates from part (a), so here we can just calculate the errors.

| Year | Z=0.5 error | Z=0.75 error |
| --- | --- | --- |
| 2,017 | 2.79% | 2.69% |
| 2,018 | 12.91% | 13.55% |

<details><summary>Formulas</summary>

- `L26` = `=ABS(L11-$E23)/L11`
- `M26` = `=ABS(M11-$E23)/M11`
- `L27` = `=ABS(L12-$E24)/L12`
- `M27` = `=ABS(M12-$E24)/M12`

</details>

The Z=0.75 estimate exceeds the 13% threshold 50% of the time, while the Z=0.50 estimate exceeds the 13% threshold 0% of the time. As such, Z=0.50 would be the optimal credibility.
