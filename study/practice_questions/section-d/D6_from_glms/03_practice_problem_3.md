---
tia_section: D6
tia_topic: from_glms
title: Practice Problem 3
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 3
revised: false
points: 3.75
parts: [a, b, c, d, e]
good_problem: true
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: [chalk_et_al/]
source_workbook: tia_excel/section-d/D_6_From_GLMs_practice_solutions.xlsx
source_sheet: Practice Problem 3
---

# Practice Problem 3

**Points:** 3.75

## Question

You are validating a Poisson claim-frequency GLM on a held-out validation fold, summarized as six rating cells. For each cell i you are given the earned exposure E_i, the observed claim count Y_i, the claims predicted by the fitted GLM (μ_i), and the claims predicted by the incumbent rating plan (benchmark b_i). The null (intercept-only) model uses the training frequency 0.10 claims per exposure unit.

The POISSON.DIST(n, λ, FALSE) spreadsheet function gives the probability Pr(N=n) for a Poisson distribution with parameter λ.

Given the following information:

| Cell i | Exposure E_i | Claims Y_i | GLM μ_i | Benchmark b_i |
| --- | --- | --- | --- | --- |
| 1 | 40 | 2 | 3.6 | 3.9 |
| 2 | 120 | 13 | 13.2 | 12.5 |
| 3 | 60 | 9 | 7.8 | 6.6 |
| 4 | 200 | 16 | 18.0 | 19.2 |
| 5 | 50 | 6 | 4.0 | 4.7 |
| 6 | 150 | 12 | 16.5 | 15.4 |

### Part a (1.50 pts)

Calculate the total Poisson (unweighted) log-likelihood of the saturated, null, and fitted models.

### Part b (0.50 pts)

Calculate the null model and fitted model scaled (unweighted) deviances.

### Part c (0.25 pts)

Calculate the (unweighted) validation pseudo-R² for the fitted model.

### Part d (1.00 pts)

Calculate the exposure-weighted validation pseudo-R² for the fitted model.

### Part e (0.50 pts)

An underwriter objects: "A pseudo-R² of about 0.20 means the model explains only 20% of risk, so it is not worth filing." Critique this claim in 2 to 3 sentences.

## Solution

### Part a

The key here is that the "likelihood" is just the probability from the POISSON.DIST function, so the log-likelihood is just the natural log of that for a given observation. Note that the saturated model perfectly predicts the actual counts, so we use the actual counts as the mean for that model.

Log-likelihoods

| Cell | Null | GLM | Saturated |
| --- | --- | --- | --- |
| 1 | -1.921 | -1.731 | -1.307 |
| 2 | -2.248 | -2.209 | -2.208 |
| 3 | -2.676 | -2.115 | -2.027 |
| 4 | -2.740 | -2.426 | -2.310 |
| 5 | -1.923 | -2.261 | -1.829 |
| 6 | -2.491 | -2.847 | -2.168 |
| Total | -13.998 | -13.590 | -11.849 |

<details><summary>Formulas</summary>

- `K9` = `=B16`
- `L9` = `=LN(POISSON.DIST($D16,0.1*C16,FALSE))`
- `M9` = `=LN(POISSON.DIST($D16,E16,FALSE))`
- `N9` = `=LN(POISSON.DIST($D16,D16,FALSE))`
- `K10` = `=B17`
- `L10` = `=LN(POISSON.DIST($D17,0.1*C17,FALSE))`
- `M10` = `=LN(POISSON.DIST($D17,E17,FALSE))`
- `N10` = `=LN(POISSON.DIST($D17,D17,FALSE))`
- `K11` = `=B18`
- `L11` = `=LN(POISSON.DIST($D18,0.1*C18,FALSE))`
- `M11` = `=LN(POISSON.DIST($D18,E18,FALSE))`
- `N11` = `=LN(POISSON.DIST($D18,D18,FALSE))`
- `K12` = `=B19`
- `L12` = `=LN(POISSON.DIST($D19,0.1*C19,FALSE))`
- `M12` = `=LN(POISSON.DIST($D19,E19,FALSE))`
- `N12` = `=LN(POISSON.DIST($D19,D19,FALSE))`
- `K13` = `=B20`
- `L13` = `=LN(POISSON.DIST($D20,0.1*C20,FALSE))`
- `M13` = `=LN(POISSON.DIST($D20,E20,FALSE))`
- `N13` = `=LN(POISSON.DIST($D20,D20,FALSE))`
- `K14` = `=B21`
- `L14` = `=LN(POISSON.DIST($D21,0.1*C21,FALSE))`
- `M14` = `=LN(POISSON.DIST($D21,E21,FALSE))`
- `N14` = `=LN(POISSON.DIST($D21,D21,FALSE))`
- `L15` = `=SUM(L9:L14)`
- `M15` = `=SUM(M9:M14)`
- `N15` = `=SUM(N9:N14)`

</details>

### Part b

Scaled Deviance = 2 * (ll_saturated - ll_model) Here we just need this in total, but you could also calculate it by cell and then sum.

| K | M |
| --- | --- |
| Null Deviance | 4.299 |
| Fitted Deviance | 3.481 |

<details><summary>Formulas</summary>

- `M20` = `=2*(N15-L15)`
- `M21` = `=2*(N15-M15)`

</details>

### Part c

You could calculate this using either the log-likelihoods or deviances, and it would be the same.

Pseudo-R^2 — 0.190 — `=1-M21/M20` — or equivalently: — 0.190 — `=(M15-L15)/(N15-L15)`

### Part d

Now we need to calculate the deviance by cell so we can weight them.

| Cell | Null dev | Fitted dev |
| --- | --- | --- |
| 1 | 1.227 | 0.849 |
| 2 | 0.081 | 0.003 |
| 3 | 1.298 | 0.176 |
| 4 | 0.859 | 0.231 |
| 5 | 0.188 | 0.866 |
| 6 | 0.645 | 1.357 |
| Wtd | 414.689 | 337.903 |

<details><summary>Formulas</summary>

- `K30` = `=B16`
- `L30` = `=2*($N9-L9)`
- `M30` = `=2*($N9-M9)`
- `K31` = `=B17`
- `L31` = `=2*($N10-L10)`
- `M31` = `=2*($N10-M10)`
- `K32` = `=B18`
- `L32` = `=2*($N11-L11)`
- `M32` = `=2*($N11-M11)`
- `K33` = `=B19`
- `L33` = `=2*($N12-L12)`
- `M33` = `=2*($N12-M12)`
- `K34` = `=B20`
- `L34` = `=2*($N13-L13)`
- `M34` = `=2*($N13-M13)`
- `K35` = `=B21`
- `L35` = `=2*($N14-L14)`
- `M35` = `=2*($N14-M14)`
- `L36` = `=SUMPRODUCT(L30:L35,C16:C21)`
- `M36` = `=SUMPRODUCT(M30:M35,C16:C21)`

</details>

**Wtd Pseudo-R^2:** 0.185 — `=1-M36/L36`

### Part e

Typical models in insurance have relatively low values of pseudo-R^2 because of the inherent randomness of claims. A more important question is whether it is an improvement over existing models and the current rating plan. If so, it can improve pricing segmentation and accuracy and would be worth implementing.
