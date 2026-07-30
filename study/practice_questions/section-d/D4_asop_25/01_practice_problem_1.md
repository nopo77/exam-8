---
tia_section: D4
tia_topic: asop_25
title: Practice Problem 1
source: practice_problem
exam_year: null
exam_sitting: null
exam_number: null
question_number: null
practice_number: 1
revised: false
points: 1.5
parts: []
good_problem: false
has_images: false
has_examiner_report: false
layout: side_by_side
split_confidence: clean
readings: []
source_workbook: tia_excel/section-d/D_4_ASOP_25_practice_solutions.xlsx
source_sheet: Practice Problem 1
---

# Practice Problem 1

**Points:** 1.5

## Question

ABC Insurance Company has recently acquired a small, niche insurance company, XYZ Mutual, which specializes in providing liability coverage for artisanal cheese makers. This is a new line of business for ABC. XYZ Mutual has been writing this coverage for 10 years and has a dataset of 750 claim records over this period for this specific line. The historical average claim severity for XYZ Mutual for this artisanal cheese maker liability coverage has been $15,000 after developing and trending the data.

ABC's actuarial department is tasked with developing a prospective loss cost for this line of business. Due to the limited volume of historical data from XYZ Mutual, one junior analyst, Tom, proposes the following credibility procedure to determine the claim severity to be used in pricing:

Subject Experience: The historical average claim severity of $15,000 from XYZ Mutual's 750 claims that has been developed and trended for the future period being priced.

Relevant Experience: ABC Insurance Company's extensive experience in commercial general liability (CGL) for small to medium-sized food processing businesses (excluding dairy and cheese). ABC has over 100,000 CGL claims in this broader category over the past 10 years, with a well-established average claim severity of $25,000 after adjustment for development and trend to be appropriate for the future period being priced.

Proposed Credibility Procedure: Tom suggests using a classical credibility approach where the full credibility standard for claim severity is set at 2,000 claims, based on a company-wide guideline used for more established lines of business. The credibility factor

(Z) would be calculated as Z = Square root(Number of XYZ Claims / Full Credibility Standard).

The credibility-weighted severity would then be calculated as:

Z × (XYZ Mutual Average Severity) + (1 - Z) × (ABC CGL Average Severity)

As the reviewing actuary, evaluate the appropriateness of Tom's proposed credibility procedure for determining the claim severity for the artisanal cheese maker liability coverage. In your evaluation, discuss the strengths and weaknesses of the proposed procedure.

## Solution

We can evaluate both the complement choice and the credibility formula being used here. While not needed here, you can calculate the credibility-weighted severity using the proposed method as:

| I | K |
| --- | --- |
| Credibility: | 0.612 |
| Cred-Wtd Severity: | 18,876 |

<details><summary>Formulas</summary>

- `K4` = `=SQRT(750/2000)`
- `K5` = `=K4*15000+(1-K4)*25000`

</details>

Strengths:

The complement of ABC's data is large enough to be statistically reliable, it is independent of XYZ's data, and liability for food processing businesses would be expected to be similar to liability for cheese makers. Both sets of data have been trended and developed to be on a comparable basis and at the trend level of the future period being priced. The classical credibility approach with a full credibility standard of 2,000 claim counts seems reasonable, and is consistent with what ABC uses elsewhere in determining credibility.

Weaknesses:

Cheese makers may have different loss characteristics compared with other food processing businesses, so ABC's complement may not be perfectly comparable. The choice of 2,000 claim counts for full credibility isn't fully explained, so it's possible that it may not be an appropriate standard for use with claim severity in this case. The sample severity from XYZ of 15k seems notably different than ABC's severity of 25k, so it may be that ABC's complement isn't a great comparison for XYZ's experience.

Overall, the proposed procedure seems reasonable given the data available, that it makes sense for food processing businesses and cheese makers to have similar characteristics, and that the same credibility formula is used elsewhere by ABC.
