---
paper: holmes_&_casotto
chapter: 7
title: Case Study
topics: [lasso_credibility, countrywide_model, state_level_modeling, double_lift_charts, pricing_model_refresh, bias_variance_tradeoff]
key_formulas: []
---

> **TL;DR**
> - Case study uses synthetic commercial auto data (3.5M records) divided into countrywide base (2.5M), large state (500k), medium state (300k), and two small states (100k each).
> - Countrywide model: GLM and lasso penalized regression perform nearly identically on large data — penalization has little effect at full credibility.
> - Large state: lasso credibility outperforms both GLM and lasso penalization by incorporating the countrywide complement; partial credibility adjusts unstable coefficients without removing them.
> - Small state with different relativities from base: lasso credibility successfully detects credible deviations from the complement even on thin data.
> - Small state with same relativities as base: lasso credibility collapses all coefficients to zero, matching the complement — a good complement produces a sparse lasso credibility model.
> - Performance validated via relativity plots (true vs. modeled) and double lift charts comparing decile-ranked predictions to true pure premiums.

# 7. Case Study

From the previous chapters, we hope the reader has gained a basic understanding of the application of lasso penalized regression as an actuarial credibility procedure. In this chapter we offer a practical application to demonstrate how modeling methods may evolve with lasso credibility. To do so, we replicate a **pricing model refresh** project that is common in the United States. The case study will walk through a model refresh process using generalized linear modeling and lasso credibility in parallel. We identify the differences between the approaches and point out key concepts of lasso credibility along the way.

The case study is not intended to prove that lasso credibility is better than other methodologies in all cases. As the data is simulated, one could select a seed to create favorable or unfavorable model comparisons. Instead, we intend the case study to demonstrate how lasso credibility truly acts as a multivariate credibility procedure with the benefits of both traditional credibility procedures and multivariate penalized regression. Deviations from this methodology are expected based on an insurer's unique situation, and guidance for such deviations should come from both materials on penalized regression and ASOP 25 credibility procedures.

Our hope is that through this monograph, the accompanying case study, and ASOP 25, the reader can gain the necessary understanding and skills to apply lasso credibility effectively in practice.

Accompanying code is provided on the CAS GitHub,<sup>7</sup> together with additional exercises for the reader. One need not do the exercises to understand the basic concepts of lasso credibility, but we highly encourage readers to investigate items that they feel could be relevant to their existing practices. Actuaries working on their coding skills may find such items to be practical exercises for self-improvement, and we encourage code contribution via pull requests to enhance the accompanying code.

## 7.1. Countrywide Modeling and State Refits

A model refresh involves creating one or more models to develop new rating relationships for an insurer's rating plan. It is common practice for U.S. insurers to first fit a model to a large data set, including all relevant data available for the line. For example, an insurer might build a model using all claims data from the last five years' experience

---

<sup>7</sup> <https://github.com/casact/mg-credibility>

for a given line of business, across all states. Such a model is referred to as a **country-wide model**.

The countrywide model may be quite robust if a large amount of data is available. The individual states, however, have unique regulations and varying behavior of risk characteristics. Because of those differences, an insurer may want to adjust the robust countrywide model for each state based on its available data. The process could result in the creation of 51 different rating relativities—one for each state and Washington, D.C. For simplicity, we use three main categories to represent the states:

- **Small state.** Such a state offers the modeler insufficient data with which to build a stable GLM, and therefore the modeler has no choice but to **adopt the country-wide model**.
- **Medium state.** A state in this category has potentially sufficient data for individual modeling but the modeler **usually adopts the countrywide model with post-modeling adjustments** for specific state characteristics. Building a model for a medium state may be relatively more time-consuming due to data variability, and the decision between a new model or adjusting the countrywide model is often based on a cost–benefit analysis. Post hoc univariate adjustment of a model, as mentioned earlier, is often suboptimal versus multivariate approaches.
- **Large state.** Such a state has sufficient credibility for the modeler to rely on the state’s own experience to **build a GLM** if desired.

The full credibility nature of a GLM does not allow a modeler to easily blend countrywide and state-specific experience. Instead, the modeler must choose between adopting the countrywide model, refitting a GLM from scratch, or performing manual ad hoc adjustments. On the other hand, lasso credibility allows a modeler to blend the state’s experience with a complement of credibility provided by the countrywide model during the modeling process. One can expect the credibility assigned to the state-specific experience to vary with the state’s size, being higher for larger states and lower for smaller ones.

## 7.2. Case Study Summary

The case study starts by building a countrywide model from scratch as we assume that there is no complement of credibility that this insurer trusts more than its own data for this model. In our example, the countrywide data set is quite credible and the differences between lasso penalization and GLM are minimal.

Differences begin to appear when looking at the **large state level**, where we will fit a GLM, a lasso penalization model, and a lasso credibility model. The lasso penalization model will still perform similarly to the GLM on this data set. However, we will see that lasso credibility, with the countrywide model as a complement of credibility, can outperform both models due to the extra information included in the complement.

Lasso credibility can also be the best-performing model on the **medium state subset**. In this example, we will detail and discuss the role of a judgmental increase of the penalty parameter when building a lasso credibility model.

The **small state** by our definition is one that cannot be fit reliably with a GLM, making it impossible to compare lasso credibility models to GLMs. Instead, the countrywide model is used as a comparison. We detail two possible behaviors of the small-state use case. First, we consider a small-state data set that has material differences from the base modeling data set. We show that not only is it possible to build a lasso credibility model on this small data set, but the **lasso credibility model outperforms the countrywide model**. Then, we consider a second small-state data set that has an identical underlying distribution to the base modeling data set. In this case, **the lasso credibility model collapses to the countrywide model**. The lasso credibility model is able to correctly identify that the selected complement is a good representation of this data subset.

We focus on the countrywide modeling and state refit use case because it covers the entire range of credibility—nearly full, partial, and little/no credibility. This range of credibility is also applicable to a broader set of scenarios. For instance, data could be divided by time periods or other definitions rather than by state. Similarly, the complement of credibility could be the current filed and implemented model instead of a new countrywide model. We invite the reader to use the guidance of ASOP 25 to identify additional applications of lasso credibility in their own practice.

### 7.2.1. Data Description

The data generated for the case study is a synthetic commercial auto data set containing 3,500,000 total records. We show the risk characteristics of each record in Table 7.1. Those characteristics are assigned using a distribution that mimics a probable real-life distribution on a univariate level, but with no correlation between characteristics. For each value of a risk characteristic, a **true risk relativity** is assigned. **True risk relativities** are consistent within state-level subsets but **may be different between states**, as visualized in Section 7.2.2. Additionally, the true base rate varies within each state-level subset.

A **true pure premium** is generated for each risk by multiplying the true base rate by the true risk relativities assigned to each characteristic. We then simulate an **experienced pure premium** using a Tweedie distribution.<sup>8</sup>

Figure 7.1 illustrates the division of the data across five subsets, corresponding to states of various sizes:

- Base modeling data: 2,500,000 records
  - The largest part of the modeling data set is referred to as the base modeling data set. In practice, this segment would be made up of a combination of other large, medium, and small state subsets. For simplicity, we simulate this all at once.
  - This data set is included so that the countrywide model is highly stable and can be used as a complement of credibility for the smaller models. We will demonstrate

<sup>8</sup> The Tweedie random samples were simulated with a  $p$ -parameter of 1.6 and a dispersion parameter of 800. These parameters were chosen so that the resulting frequency is approximately 4%.

**Figure 7.1. Visual representation of the various subsets in the simulated data. Risk characteristics are consistent within each subset but may (slightly) vary across states.**

![A diagram titled 'Countrywide database' showing the structure of simulated data. It includes a large green box for 'LARGE STATE' (500 K rows), a yellow box for 'MEDIUM STATE' (300 K rows), two small red boxes for 'SMALL' states (each 100 K rows), and a large grey box for 'BASE MODELING DATA' (2.5 M rows).](fef7e3f08b408e4ab937a75f5c8b6bfc_img.jpg)

The diagram, titled "Countrywide database", illustrates the composition of simulated data subsets. It features five colored boxes: a large green box on the left labeled "LARGE STATE" with "• 500 K rows"; a yellow box in the top center labeled "MEDIUM STATE" with "• 300 K rows"; two small red boxes at the bottom center, each labeled "SMALL" with "• 100 K rows"; and a large grey box on the right labeled "BASE MODELING DATA" with "• 2.5 M rows".

A diagram titled 'Countrywide database' showing the structure of simulated data. It includes a large green box for 'LARGE STATE' (500 K rows), a yellow box for 'MEDIUM STATE' (300 K rows), two small red boxes for 'SMALL' states (each 100 K rows), and a large grey box for 'BASE MODELING DATA' (2.5 M rows).

K = thousand; M = million.

that for this large data set, GLM and lasso penalized regression have very similar results. We do not model this data set on its own, but instead combined with all other data.

- Large state subset: 500,000 records
  - This subset represents the insurer’s largest state in the U.S. market.
  - We model this data set using a GLM, lasso penalization, and lasso credibility. We will see that lasso credibility can be an improvement where data is large enough to build a stable GLM.
- Medium state subset: 300,000 records
  - This subset represents one of the insurer’s growing states.
  - We build only a GLM and a lasso credibility model on this data set. We will see that lasso credibility provides more benefit on this data set than on the large state data.
- Small state 1: 100,000 records
  - This small-state data represents a subset containing minimal data.
  - This subset has **different risk relativities** than the base modeling data set.
  - We use this subset to show that, even with small data, lasso credibility is able to identify meaningful changes.
- Small state 2: 100,000 records
  - This second small state also represents a subset containing minimal data.
  - This data has **the same underlying risk relativities** as the base modeling data set.
  - We use this to show that a good complement creates a sparse lasso credibility model.

### 7.2.2. Predictor Variables

The generated data set contains seven risk characteristics, summarized in Table 7.1.

Each of our predictor variables is included to highlight a different scenario when comparing generalized linear modeling and lasso credibility. All charts reflect the exposure distribution and true risk relativity for each of the subsets of the data. For

**Table 7.1. List of Risk Characteristics in the Synthetic Database**

| Name                 | Type        | Values                              |
|----------------------|-------------|-------------------------------------|
| Driver age           | Numerical   | [18–100]                            |
| Vehicle age          | Numerical   | [0–19]                              |
| Industry code        | Categorical | [Education, . . . , Fireworks]      |
| Vehicle weight       | Categorical | [Extra-Light, Light, Medium, Heavy] |
| Multipolicy discount | Categorical | [Yes, No]                           |
| x-Treme turn signal  | Categorical | [Yes, No]                           |

simplicity, the exposure distributions do not vary between the subsets so it is easy to compare the behavior of factors between datasets. In practice, we would expect these exposure distributions to vary along with the true relativities.

#### Driver Age

As we will see, lasso credibility does not prevent a model from identifying the steep increase for young drivers, and it can bring stability to the low-data tail beyond age 76 (Figure 7.2).

**Figure 7.2. Driver age demonstrates that not all transformations within a continuous variable receive the same amount of credibility. This may seem trivial, but it is highly important to demonstrate that we cannot accurately rely on or even meaningfully calculate a credibility score ( $Z$ ) when describing a lasso credibility model's behavior.**

![Figure 7.2: A dual-axis plot showing Relativity (left y-axis, 1 to 3) and Exposure (right y-axis, 0 to 120k) versus Driver age (x-axis, 18 to 99). The plot includes four data series: Base data (solid purple line), Large state (dashed green line), Medium state (dashed orange line), and Small state (dashed blue line). The Base data line starts at approximately 2.7 at age 18, drops to 1.0 by age 36, remains flat until age 76, and then rises slightly to 1.1 at age 99. The Large state line starts at 3.0 at age 18 and decreases steadily to 1.0 at age 99. The Medium state line starts at 1.8 at age 18 and decreases steadily to 1.0 at age 99. The Small state line starts at 1.3 at age 18 and decreases steadily to 1.0 at age 99. The exposure bars (light blue) show a distribution that peaks around age 45-50 and then decreases towards age 99.](6381dcd91bf4636842734ec95bbd75d4_img.jpg)

Figure 7.2: A dual-axis plot showing Relativity (left y-axis, 1 to 3) and Exposure (right y-axis, 0 to 120k) versus Driver age (x-axis, 18 to 99). The plot includes four data series: Base data (solid purple line), Large state (dashed green line), Medium state (dashed orange line), and Small state (dashed blue line). The Base data line starts at approximately 2.7 at age 18, drops to 1.0 by age 36, remains flat until age 76, and then rises slightly to 1.1 at age 99. The Large state line starts at 3.0 at age 18 and decreases steadily to 1.0 at age 99. The Medium state line starts at 1.8 at age 18 and decreases steadily to 1.0 at age 99. The Small state line starts at 1.3 at age 18 and decreases steadily to 1.0 at age 99. The exposure bars (light blue) show a distribution that peaks around age 45-50 and then decreases towards age 99.

#### Vehicle Age

Figure 7.3 shows the risk relativities for the age of an insured's vehicle.

**Figure 7.3.** Across all data, this variable's true risk decreases from 0 to 10, then decreases at a less steep rate beyond 10. We will see that coefficients are highly stable from vehicles ages 0 to 10 and then become increasingly harder to model for older vehicles.

![Figure 7.3: A dual-axis chart showing risk relativity and exposure for vehicle age. The x-axis represents vehicle age from 0 to 19. The left y-axis represents Relativity from 0.9 to 1.5. The right y-axis represents Exposure from 0 to 800k. The chart includes four data series: Base data (solid purple line), Large state (dashed green line), Medium state (dashed orange line), and Small state (dashed blue line). The Base data line starts at approximately 1.35 at age 0 and decreases to about 0.92 at age 19. The state lines start at higher relativity values (around 1.45 to 1.5) and decrease more steeply, crossing the Base data line around age 10. The exposure bars show a peak around age 4-5 and then generally decrease with age.](a8d5c44b9a83b894ec7f81c8dbeca93d_img.jpg)

| Vehicle age | Base data Relativity | Large state Relativity | Medium state Relativity | Small state Relativity | Exposure (k) |
|-------------|----------------------|------------------------|-------------------------|------------------------|--------------|
| 0           | 1.35                 | 1.45                   | 1.45                    | 1.45                   | 20           |
| 1           | 1.28                 | 1.38                   | 1.38                    | 1.38                   | 180          |
| 2           | 1.22                 | 1.32                   | 1.32                    | 1.32                   | 320          |
| 3           | 1.18                 | 1.28                   | 1.28                    | 1.28                   | 380          |
| 4           | 1.15                 | 1.25                   | 1.25                    | 1.25                   | 420          |
| 5           | 1.12                 | 1.22                   | 1.22                    | 1.22                   | 420          |
| 6           | 1.10                 | 1.18                   | 1.18                    | 1.18                   | 400          |
| 7           | 1.08                 | 1.15                   | 1.15                    | 1.15                   | 380          |
| 8           | 1.05                 | 1.12                   | 1.12                    | 1.12                   | 350          |
| 9           | 1.02                 | 1.08                   | 1.08                    | 1.08                   | 300          |
| 10          | 1.00                 | 1.05                   | 1.05                    | 1.05                   | 250          |
| 11          | 0.98                 | 0.98                   | 0.98                    | 0.98                   | 200          |
| 12          | 0.96                 | 0.95                   | 0.95                    | 0.95                   | 180          |
| 13          | 0.95                 | 0.92                   | 0.92                    | 0.92                   | 150          |
| 14          | 0.94                 | 0.90                   | 0.90                    | 0.90                   | 120          |
| 15          | 0.93                 | 0.88                   | 0.88                    | 0.88                   | 100          |
| 16          | 0.92                 | 0.85                   | 0.85                    | 0.85                   | 80           |
| 17          | 0.91                 | 0.82                   | 0.82                    | 0.82                   | 60           |
| 18          | 0.90                 | 0.80                   | 0.80                    | 0.80                   | 40           |
| 19          | 0.92                 | 0.78                   | 0.78                    | 0.78                   | 20           |

Figure 7.3: A dual-axis chart showing risk relativity and exposure for vehicle age. The x-axis represents vehicle age from 0 to 19. The left y-axis represents Relativity from 0.9 to 1.5. The right y-axis represents Exposure from 0 to 800k. The chart includes four data series: Base data (solid purple line), Large state (dashed green line), Medium state (dashed orange line), and Small state (dashed blue line). The Base data line starts at approximately 1.35 at age 0 and decreases to about 0.92 at age 19. The state lines start at higher relativity values (around 1.45 to 1.5) and decrease more steeply, crossing the Base data line around age 10. The exposure bars show a peak around age 4-5 and then generally decrease with age.

#### Multipolicy Discount

This indicator represents whether the insured has another policy with the insurer (Figure 7.4).

**Figure 7.4.** The “Yes” category always has a lower true risk relativity. We will see that multipolicy discount is relatively well predicted across all data sets because both levels have significant data and material signal.

![Figure 7.4: A dual-axis chart showing risk relativity and exposure for multipolicy discount. The x-axis has two categories: Multi no and Multi yes. The left y-axis represents Relativity from 0.6 to 1.0. The right y-axis represents Exposure from 0 to 3M. The chart includes four data series: Base data (solid purple line), Large state (dashed green line), Medium state (dashed orange line), and Small state (dashed blue line). All lines show a decrease in relativity from 'Multi no' to 'Multi yes'. The Base data line starts at 1.0 and ends at approximately 0.8. The state lines start at 1.0 and end at lower values: Large state at ~0.7, Medium state at ~0.75, and Small state at ~0.6. The exposure bars show a significant increase from 'Multi no' to 'Multi yes'.](c959fda5679ea6470e0810c8c29eb823_img.jpg)

| Category  | Base data Relativity | Large state Relativity | Medium state Relativity | Small state Relativity | Exposure (M) |
|-----------|----------------------|------------------------|-------------------------|------------------------|--------------|
| Multi no  | 1.00                 | 1.00                   | 1.00                    | 1.00                   | 1.5          |
| Multi yes | 0.80                 | 0.70                   | 0.75                    | 0.60                   | 2.5          |

Figure 7.4: A dual-axis chart showing risk relativity and exposure for multipolicy discount. The x-axis has two categories: Multi no and Multi yes. The left y-axis represents Relativity from 0.6 to 1.0. The right y-axis represents Exposure from 0 to 3M. The chart includes four data series: Base data (solid purple line), Large state (dashed green line), Medium state (dashed orange line), and Small state (dashed blue line). All lines show a decrease in relativity from 'Multi no' to 'Multi yes'. The Base data line starts at 1.0 and ends at approximately 0.8. The state lines start at 1.0 and end at lower values: Large state at ~0.7, Medium state at ~0.75, and Small state at ~0.6. The exposure bars show a significant increase from 'Multi no' to 'Multi yes'.

#### x-Treme Turn Signal

This is a fictitious new safety feature that is in the early stages of adoption and greatly reduces accidents (Figure 7.5).

**Figure 7.5. x-Treme turn signal has a very low relativity that varies between data sets. We will use this example to show that lasso credibility can react—without overreacting—to strong signal in small segments.**

![Figure 7.5: A dual-axis chart showing the relative signal for 'x-Treme turn signal' across different data sets. The left y-axis represents 'Relativity' (0.2 to 1.0), and the right y-axis represents 'Exposure' (0 to 6M). The x-axis shows two categories: 'x-Treme no' and 'x-Treme yes'. Four lines represent different data sets: 'Base data' (solid purple line), 'Large state' (dashed green line), 'Medium state' (dashed orange line), and 'Small state' (dashed blue line). All lines start at a relativity of 1.0 for 'x-Treme no'. For 'x-Treme yes', the relativity drops significantly, with 'Base data' dropping to approximately 0.2, 'Large state' to 0.4, 'Medium state' to 0.5, and 'Small state' to 0.6. A light blue shaded area is present on the left side of the chart, and a horizontal bar is at the bottom.](b148a4b7f3b149ef40cc21d1091d2664_img.jpg)

| Data Set     | x-Treme no (Relativity) | x-Treme yes (Relativity) |
|--------------|-------------------------|--------------------------|
| Base data    | 1.0                     | 0.2                      |
| Large state  | 1.0                     | 0.4                      |
| Medium state | 1.0                     | 0.5                      |
| Small state  | 1.0                     | 0.6                      |

Figure 7.5: A dual-axis chart showing the relative signal for 'x-Treme turn signal' across different data sets. The left y-axis represents 'Relativity' (0.2 to 1.0), and the right y-axis represents 'Exposure' (0 to 6M). The x-axis shows two categories: 'x-Treme no' and 'x-Treme yes'. Four lines represent different data sets: 'Base data' (solid purple line), 'Large state' (dashed green line), 'Medium state' (dashed orange line), and 'Small state' (dashed blue line). All lines start at a relativity of 1.0 for 'x-Treme no'. For 'x-Treme yes', the relativity drops significantly, with 'Base data' dropping to approximately 0.2, 'Large state' to 0.4, 'Medium state' to 0.5, and 'Small state' to 0.6. A light blue shaded area is present on the left side of the chart, and a horizontal bar is at the bottom.

#### Vehicle Weight

This is a categorical variable with four categories: extra-light, light, medium, and heavy (Figure 7.6). While we are modeling vehicle weight as a categorical variable, we want to point out that vehicle weight could also be modeled as an ordinal variable. Unlike continuous variables, ordinal variables can reflect a link between adjacent categories without enforcing a numeric distance between these categories.

**Figure 7.6. Risk increases as a vehicle becomes lighter, and may plateau with identical relativities for extra-light and light vehicles. Extra-light vehicle weight is very hard to predict due to its low exposure, but in most data sets it has a higher relativity than light vehicles. We will see that our complement of credibility allows us to model low credibility categories without grouping them together.**

![Figure 7.6: A dual-axis chart showing Relativity (left axis, 0.8 to 2.0) and Exposure (right axis, 0 to 4M) for Vehicle weight categories: Weight extra light, Weight heavy, Weight light, and Weight medium. The chart includes four data series: Base data (solid purple line), Large state (dashed green line), Medium state (dashed orange line), and Small state (dashed blue line). Exposure is represented by light blue bars at the bottom. The Small state series shows the highest relativity for 'Weight extra light' (approx. 2.0) and 'Weight light' (approx. 1.3). The Base data series shows a peak in relativity for 'Weight light' (approx. 1.2). The Medium state series shows a peak in relativity for 'Weight light' (approx. 1.3). The Large state series shows a peak in relativity for 'Weight light' (approx. 1.15). The exposure bars show that 'Weight extra light' has the lowest exposure, while 'Weight medium' has the highest exposure (approx. 2.0M).](834359004b142e33f72aea7a3de2440f_img.jpg)

| Vehicle weight     | Base data (Relativity) | Large state (Relativity) | Medium state (Relativity) | Small state (Relativity) | Exposure (M) |
|--------------------|------------------------|--------------------------|---------------------------|--------------------------|--------------|
| Weight extra light | 1.2                    | 1.3                      | 1.4                       | 2.0                      | 0.1          |
| Weight heavy       | 0.7                    | 0.8                      | 0.8                       | 0.8                      | 0.5          |
| Weight light       | 1.2                    | 1.15                     | 1.3                       | 1.3                      | 1.2          |
| Weight medium      | 1.0                    | 1.1                      | 1.1                       | 1.1                      | 2.0          |

Figure 7.6: A dual-axis chart showing Relativity (left axis, 0.8 to 2.0) and Exposure (right axis, 0 to 4M) for Vehicle weight categories: Weight extra light, Weight heavy, Weight light, and Weight medium. The chart includes four data series: Base data (solid purple line), Large state (dashed green line), Medium state (dashed orange line), and Small state (dashed blue line). Exposure is represented by light blue bars at the bottom. The Small state series shows the highest relativity for 'Weight extra light' (approx. 2.0) and 'Weight light' (approx. 1.3). The Base data series shows a peak in relativity for 'Weight light' (approx. 1.2). The Medium state series shows a peak in relativity for 'Weight light' (approx. 1.3). The Large state series shows a peak in relativity for 'Weight light' (approx. 1.15). The exposure bars show that 'Weight extra light' has the lowest exposure, while 'Weight medium' has the highest exposure (approx. 2.0M).

#### Industry Code

The industry code category is separated into 10 categories that are not easily consolidated (Figure 7.7).

**Figure 7.7. Industry code provides a side-by-side example of categorical variables of various discounts, surcharges, and data sizes. The fireworks industry code is known to require a high surcharge but has extremely small data. We suggest that since none of these categories is easily grouped with another it would be best to predict a unique relativity for all categories.**

![Figure 7.7: A dual-axis chart showing industry relativity and exposure. The x-axis lists 10 industries: Construction, Education, Farming, Finance and insurance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The left y-axis represents Relativity (0.5 to 3.0), and the right y-axis represents Exposure (0 to 1.6M). Blue bars show relativity for each industry. Four lines represent different data sources: Base data (solid purple line with circles), Large state (dashed green line with circles), Medium state (dashed orange line with circles), and Small state (dashed blue line with circles). The Fireworks industry shows a significant spike in relativity for the Large state data source, reaching 3.0, while its exposure is very low.](03e25a69b2145b8a280edf2421fbc07f_img.jpg)

| Industry              | Base data (Relativity) | Large state (Relativity) | Medium state (Relativity) | Small state (Relativity) | Exposure (M) |
|-----------------------|------------------------|--------------------------|---------------------------|--------------------------|--------------|
| Construction          | 1.5                    | 1.4                      | 1.4                       | 1.4                      | 0.2          |
| Education             | 1.0                    | 1.0                      | 1.0                       | 1.0                      | 0.8          |
| Farming               | 0.7                    | 0.7                      | 0.7                       | 0.7                      | 0.1          |
| Finance and insurance | 0.5                    | 0.5                      | 0.5                       | 0.5                      | 0.8          |
| Fine arts             | 0.9                    | 0.9                      | 0.9                       | 0.9                      | 0.4          |
| Fireworks             | 2.0                    | 3.0                      | 1.5                       | 1.5                      | 0.05         |
| Food services         | 1.2                    | 1.2                      | 1.2                       | 1.2                      | 0.4          |
| Health care           | 1.3                    | 1.2                      | 1.2                       | 1.4                      | 0.05         |
| Real estate           | 0.6                    | 0.6                      | 0.6                       | 0.6                      | 0.05         |
| Retail                | 0.8                    | 0.8                      | 0.8                       | 0.8                      | 0.2          |

Figure 7.7: A dual-axis chart showing industry relativity and exposure. The x-axis lists 10 industries: Construction, Education, Farming, Finance and insurance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The left y-axis represents Relativity (0.5 to 3.0), and the right y-axis represents Exposure (0 to 1.6M). Blue bars show relativity for each industry. Four lines represent different data sources: Base data (solid purple line with circles), Large state (dashed green line with circles), Medium state (dashed orange line with circles), and Small state (dashed blue line with circles). The Fireworks industry shows a significant spike in relativity for the Large state data source, reaching 3.0, while its exposure is very low.

### 7.2.3. Methodological Notes

#### The Use of Simulated Data

Working with synthetic/simulated data comes with its own advantages and disadvantages. We acknowledge that simulated data amounts to a strong simplification versus using an open, realistic data set, as, for example, in Wüthrich and Merz (2023) or Casotto and Holmes (2023). We still decided to work with simulated data because of the following benefits:

1. We know the true underlying relativities for risk characteristics, and therefore have knowledge of what is signal and what is noise. As a result, we can create charts comparing our model output to the true risk relativities instead of potentially noisy validation data.
2. We know that our risk characteristics are uncorrelated. Correlation will not affect the stability of either our GLM or lasso credibility models.
3. We know the variable transformations that can capture the true risk relativities. Such transformations would allow a model to fit perfectly to the true risk relativities

given sufficient data. This greatly simplifies the feature engineering process as we will use these known transformations for all models. We acknowledge that additional feature engineering would improve all models, but we think that the simplifying assumption is the best way to explain lasso credibility for instructional purposes.

4. The case study can correctly highlight situations where lasso credibility is performing well versus situations where it is performing poorly, and why the model exhibits this performance.
5. The underlying data can be resimulated for additional investigations.

#### Model Types

The generalized linear, lasso penalization, and lasso credibility models are built as follows (if not otherwise indicated):

- The GLM is built using the same feature engineering as the one used to generate the data.
- Lasso penalization uses the same feature engineering as the GLM. The penalty parameter  $\lambda$  is selected using cross-validation. The coefficients are standardized prior to the fit.
- Lasso credibility models are built identically to lasso penalization, but with the addition of a complement of credibility through the offset. The HDtweedie package used in the code does not directly support offsets, so the offsets are included by manually adjusting the response and weight columns through the methodology outlined in Shi (2010).

### 7.2.4. Prediction and Relativity Plots

We do not examine traditional test statistics like Gini or Tweedie deviance but instead focus on a direct comparison to the true relativities. This choice is made because the goal of the case study is to understand the behavior of lasso credibility, and that behavior is best represented as a visual representation of the estimated, simulated, and true relativities to provide insights on a variable-by-variable basis. By understanding the behavior of lasso credibility, a modeler can better understand why a model's test statistics will improve or degrade in various situations.

To efficiently compare true and modeled relativities and predictions, a relativity plot and a prediction plot are provided for all modeled variables.

The **relativity plot** contains the predicted GLM relativity, the lasso penalized regression relativity, and the true relativity. All relativities have been rebalanced to the base level for categorical variables, to age 38 for driver age, and to age 10 for vehicle age. Such relativity plots provide us with better validation metrics than comparing on holdout data because we can compare directly to the true relativities. The model with relativities closest to the true relativity is the better model at predicting on unseen data.

The **prediction plot** contains the true pure premium, the experienced (simulated) pure premium, the GLM prediction of pure premium, and the lasso prediction of pure premium. The prediction plot is not rebalanced for the full modeling data plots

but is rebalanced for the large, medium, and small state models. Rebalancing is done by multiplying the predictions by a constant such that the average prediction is equal to the average observed value. The difference between the experienced (simulated) pure premium and the true pure premium is determined by the random simulation of Tweedie distribution. Comparing these two quantities gives us a sense of how much noise is in the data. For example, if the true and experienced pure premiums are very close, the data is not noisy. If the true and experienced pure premiums are far apart, the mean of the simulated data is not similar to the true mean, and therefore our simulation has introduced noise.

These charts can be busy with overlapping items, so we recommend pulling the code and generating the charts in R so that you can click on items in the chart's legend to toggle their visibility on or off.

Double **lift charts** are provided to compare models. Records are ordered by the ratio of the models being compared and then bucketed into 10 deciles. Then, the ratios of the predictions to the true pure premium are plotted. The model that is closest to the horizontal line (a 1.0 ratio) is considered the best model.

## 7.3. Countrywide Model Results

Our countrywide models are built on the full 3,500,000-row data set. The GLM is quite stable, and our penalized regression model is only slightly penalizing coefficients. As expected, applying a credibility procedure to a large data set does not result in a large amount of weight being put on the complement of credibility.

### 7.3.1. Large Data Approaches Full Credibility

The coefficient chart (Table 7.2) contains GLM coefficients and lasso coefficients. All lasso coefficients are shrunk very slightly toward zero. When categories are sufficiently populated with stable experience, the shrinkage from penalized regression will have limited effect on the modeled coefficients. In large data, even smaller categories may approach full credibility.

The health care and fireworks industry codes are the most interesting results. Our GLM's  $p$ -values assign high significance to these categories, and they are treated as nearly fully credible in penalized regression. Relativity plots show that both models are overpredicting the relativity for these segments. Prediction plots show why: our simulated losses were particularly high in these categories. Neither GLMs nor penalized regression can identify when actual experience is unlucky (or lucky) and different from the true underlying risk.

### 7.3.2. Additional Exercises—Full Data

We recommend the following exercises to explore variable transformations and their effect on the shrinkage of continuous variables.

- Move the hinge point of vehicle age to see how the significance and shrinkage of the new variable transformations change from the current transformations.

**Table 7.2. Comparison of Coefficient Results between GLM and Lasso Penalization**

| Variable                  | GLM Coefficient | Lasso Coefficient |
|---------------------------|-----------------|-------------------|
| (Intercept)               | 8.12177         | 8.12918           |
| driver_age_18_38_hinge    | −0.04886        | −0.04886          |
| driver_age_38_76_hinge    | −0.00213        | −0.00209          |
| driver_age_76_99_hinge    | 0.00685         | 0.00667           |
| ind_construction          | 0.37839         | 0.37833           |
| ind_farming               | −0.38933        | −0.38591          |
| ind_finance_and_insurance | −0.70583        | −0.70410          |
| ind_fine_arts             | −0.09941        | −0.09788          |
| ind_fireworks             | 1.03998         | 1.02833           |
| ind_food_services         | 0.18639         | 0.18654           |
| ind_health_care           | 0.33816         | 0.33555           |
| ind_real_estate           | −0.50757        | −0.50066          |
| ind_retail                | −0.19828        | −0.19636          |
| multi_yes                 | −0.25957        | −0.25890          |
| vehicle_age_0_10_hinge    | −0.03199        | −0.03192          |
| vehicle_age_10_99_hinge   | −0.01697        | −0.01675          |
| weight_extra_light        | 0.18419         | 0.18067           |
| weight_heavy              | −0.33246        | −0.33117          |
| weight_light              | 0.18095         | 0.18030           |
| xTreme_yes                | −1.33088        | −1.32796          |

- Test different polynomial terms for driver age and vehicle age—do these terms behave similarly in GLM and lasso models?
- Replace the hinge terms with an ordinal encoding as referenced in Section 3.4.3. Include all of these variables in your lasso model. How do the predictions change? For example:
  - driver\_age\_over\_18: 0 for age 18, 1 for all ages over 19
  - driver\_age\_over\_19: 0 for ages 19 and below, 1 for all ages 20 and above
  - driver\_age\_over\_20: 0 for ages 20 and below, 1 for all ages 21 and above
  - etc.

### 7.3.3. Full Data Conclusion—Lasso Penalization, but Not Lasso Credibility

Both models are fitting similarly to the data overall, and we see in Figure 7.8 and 7.9 that output coefficients are immaterially different. As expected, both models are performing similarly on the validate data in Figure 7.10 and Figure 7.11.

**Figure 7.8. Both the GLM and Lasso Models Produce Similarly Accurate Predictions on This Large Data Set**

![Figure 7.8: A dual-axis chart showing Relative (left axis, 0.5 to 2.5) and Exposure (right axis, 0 to 1.4M) across various industries. The chart includes bars for Exposure and lines for True, GLM, and Lasso models. The GLM and Lasso models closely follow the True values, indicating high predictive accuracy.](c772a48faa2cb17e1bf2a86ad057b4c9_img.jpg)

Figure 7.8 is a dual-axis chart comparing the performance of GLM and Lasso models against the True values for Relative and Exposure across various industries. The left y-axis represents Relative (0.5 to 2.5), and the right y-axis represents Exposure (0 to 1.4M). The x-axis lists industries: Construction, Education, Farming, Finance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The legend indicates: Exposure (blue bars), True (purple line with dots), GLM (orange line with dots), and Lasso (blue line with dots). The GLM and Lasso models closely follow the True values, indicating high predictive accuracy.

| Industry      | Exposure (M) | True (Relative) | GLM (Relative) | Lasso (Relative) |
|---------------|--------------|-----------------|----------------|------------------|
| Construction  | 0.7          | 1.5             | 1.5            | 1.5              |
| Education     | 1.7          | 1.0             | 1.0            | 1.0              |
| Farming       | 0.4          | 0.7             | 0.7            | 0.7              |
| Finance       | 1.5          | 0.5             | 0.5            | 0.5              |
| Fine arts     | 1.4          | 0.9             | 0.9            | 0.9              |
| Fireworks     | 0.1          | 2.1             | 2.8            | 2.8              |
| Food services | 1.0          | 1.2             | 1.2            | 1.2              |
| Health care   | 0.1          | 1.3             | 1.3            | 1.3              |
| Real estate   | 0.1          | 0.6             | 0.6            | 0.6              |
| Retail        | 0.8          | 0.8             | 0.8            | 0.8              |

Figure 7.8: A dual-axis chart showing Relative (left axis, 0.5 to 2.5) and Exposure (right axis, 0 to 1.4M) across various industries. The chart includes bars for Exposure and lines for True, GLM, and Lasso models. The GLM and Lasso models closely follow the True values, indicating high predictive accuracy.

**Figure 7.9. Neither Model is Able to Identify Situations Where the Experienced Pure Premium is Slightly Different Than the Experienced Pure Premium in Health Care and Fireworks**

![Figure 7.9: A dual-axis chart showing Pure Premium (left axis, 200 to 2000) and Exposure (right axis, 0 to 700k) across various industries. The chart includes bars for Exposure and lines for True, Experienced, GLM, and Lasso models. The GLM and Lasso models fail to identify situations where the Experienced Pure Premium is slightly different from the True values in Health Care and Fireworks.](add5a1a3f3767f6775d7e60cc3c0c188_img.jpg)

Figure 7.9 is a dual-axis chart comparing the performance of GLM and Lasso models against the True values for Pure Premium and Exposure across various industries. The left y-axis represents Pure Premium (200 to 2000), and the right y-axis represents Exposure (0 to 700k). The x-axis lists industries: Construction, Education, Farming, Finance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The legend indicates: Exposure (blue bars), True (purple line with dots), Experienced (red line with dots), GLM (orange line with dots), and Lasso (blue line with dots). The GLM and Lasso models fail to identify situations where the Experienced Pure Premium is slightly different from the True values in Health Care and Fireworks.

| Industry      | Exposure (k) | True (Pure Premium) | Experienced (Pure Premium) | GLM (Pure Premium) | Lasso (Pure Premium) |
|---------------|--------------|---------------------|----------------------------|--------------------|----------------------|
| Construction  | 650          | 900                 | 900                        | 900                | 900                  |
| Education     | 2000         | 600                 | 600                        | 600                | 600                  |
| Farming       | 350          | 400                 | 400                        | 400                | 400                  |
| Finance       | 1750         | 300                 | 300                        | 300                | 300                  |
| Fine arts     | 1700         | 550                 | 550                        | 550                | 550                  |
| Fireworks     | 0            | 1350                | 1950                       | 1700               | 1700                 |
| Food services | 1150         | 750                 | 750                        | 750                | 750                  |
| Health care   | 200          | 800                 | 850                        | 800                | 800                  |
| Real estate   | 200          | 350                 | 350                        | 350                | 350                  |
| Retail        | 900          | 500                 | 500                        | 500                | 500                  |

Figure 7.9: A dual-axis chart showing Pure Premium (left axis, 200 to 2000) and Exposure (right axis, 0 to 700k) across various industries. The chart includes bars for Exposure and lines for True, Experienced, GLM, and Lasso models. The GLM and Lasso models fail to identify situations where the Experienced Pure Premium is slightly different from the True values in Health Care and Fireworks.

**Figure 7.10. Both Models are Doing a Similar Job of Predicting the Simulated Losses in Our Validate Data Set**

![Figure 7.10: A dual-axis chart showing normalized predictions and exposure across 10 deciles. The left y-axis represents 'Normalized predictions' from 0.94 to 1.08. The right y-axis represents 'Exposure' from 0 to 100k. The x-axis is 'Decile' from 1 to 10. A horizontal red line at y=1.0 represents 'Incurred loss'. Light blue bars represent 'Exposure'. A yellow line with diamond markers represents 'GLM' predictions. A blue line with diamond markers represents 'Lasso' predictions. Both GLM and Lasso predictions closely follow the incurred loss line across all deciles.](33d66c42e2c44378aaab641502989484_img.jpg)

| Decile | Exposure (k) | Incurred loss | GLM   | Lasso |
|--------|--------------|---------------|-------|-------|
| 1      | 70           | 1.00          | 1.035 | 1.035 |
| 2      | 20           | 1.00          | 0.965 | 0.965 |
| 3      | 70           | 1.00          | 0.995 | 0.995 |
| 4      | 70           | 1.00          | 0.985 | 0.985 |
| 5      | 70           | 1.00          | 0.945 | 0.945 |
| 6      | 70           | 1.00          | 1.000 | 1.000 |
| 7      | 70           | 1.00          | 1.000 | 1.000 |
| 8      | 70           | 1.00          | 1.005 | 1.005 |
| 9      | 70           | 1.00          | 1.002 | 1.002 |
| 10     | 70           | 1.00          | 1.000 | 1.000 |

Figure 7.10: A dual-axis chart showing normalized predictions and exposure across 10 deciles. The left y-axis represents 'Normalized predictions' from 0.94 to 1.08. The right y-axis represents 'Exposure' from 0 to 100k. The x-axis is 'Decile' from 1 to 10. A horizontal red line at y=1.0 represents 'Incurred loss'. Light blue bars represent 'Exposure'. A yellow line with diamond markers represents 'GLM' predictions. A blue line with diamond markers represents 'Lasso' predictions. Both GLM and Lasso predictions closely follow the incurred loss line across all deciles.

Because we know the true pure premium for each risk, we can create a lift chart using true values instead of simulated values. This lift chart is significantly less noisy and will be useful when evaluating model results on smaller data sets.

The penalized model output could be used to support rating factors identically to GLM output, but we would not refer to this use of lasso penalization as an application of lasso credibility. Instead, the model is behaving appropriately as a traditional

**Figure 7.11. Both lasso and the GLM are doing an excellent job at identifying the true relativities overall in this large data set. This double lift chart is calculated on the validation set and the scale is extremely small.**

![Figure 7.11: A dual-axis chart showing normalized predictions and exposure across 10 deciles. The left y-axis represents 'Normalized predictions' from 0.99 to 1.01. The right y-axis represents 'Exposure' from 0 to 100k. The x-axis is 'Decile' from 1 to 10. A horizontal purple line at y=1.0 represents 'True' values. Light blue bars represent 'Exposure'. A yellow line with diamond markers represents 'GLM' predictions. A blue line with diamond markers represents 'Lasso' predictions. Both GLM and Lasso predictions closely follow the true values line across all deciles.](c51b46bece9e94eff9615851747f31cc_img.jpg)

| Decile | Exposure (k) | True | GLM   | Lasso |
|--------|--------------|------|-------|-------|
| 1      | 70           | 1.00 | 0.990 | 0.992 |
| 2      | 20           | 1.00 | 0.995 | 0.997 |
| 3      | 70           | 1.00 | 1.005 | 1.007 |
| 4      | 70           | 1.00 | 1.000 | 1.002 |
| 5      | 70           | 1.00 | 1.002 | 1.003 |
| 6      | 70           | 1.00 | 1.005 | 1.006 |
| 7      | 70           | 1.00 | 1.006 | 1.007 |
| 8      | 70           | 1.00 | 0.998 | 0.998 |
| 9      | 70           | 1.00 | 0.998 | 0.997 |
| 10     | 70           | 1.00 | 0.998 | 0.996 |

Figure 7.11: A dual-axis chart showing normalized predictions and exposure across 10 deciles. The left y-axis represents 'Normalized predictions' from 0.99 to 1.01. The right y-axis represents 'Exposure' from 0 to 100k. The x-axis is 'Decile' from 1 to 10. A horizontal purple line at y=1.0 represents 'True' values. Light blue bars represent 'Exposure'. A yellow line with diamond markers represents 'GLM' predictions. A blue line with diamond markers represents 'Lasso' predictions. Both GLM and Lasso predictions closely follow the true values line across all deciles.

use of penalized regression. To call it lasso credibility, we would have to justify that the selected default complement of credibility for all variables (a 1.0 relativity) is an actuarially sound complement of credibility. For young drivers and the fireworks industry code in particular, this would be a poor complement.

## 7.4. “Large State” Modeling Results

We build three models on the large state data:

1. A standard GLM model
2. A lasso penalization model
3. A lasso credibility model, using the previously fitted countrywide model as complement of credibility

We begin to see instabilities in the GLM, and those instabilities are automatically accounted for in our penalized regression model. The penalized regression model will outperform the GLM by shrinking coefficients when they are not sufficiently supported by the data.

### 7.4.1. Low Significance Correlates with High Shrinkage

Now that our data is smaller, some GLM coefficients have  $p$ -values above the 5% threshold. This is the case for the tail of the driver age variable in Figure 7.12 (driver\_age\_76\_99\_hinge) and the vehicle age variable in Figure 7.13 (vehicle\_age\_10\_99\_hinge), as well as the health care indicator for the industry code (ind\_health\_care). A modeler would have to remove these factors and try again with different variable transformations.

**Figure 7.12. The Hinge for Older Drivers is Shrunk Toward Zero Slope in the Lasso Model, Not Reacting as Much as in Our GLM**

![Figure 7.12: A dual-axis chart showing Relativity (left y-axis, 0.85 to 1.0) and Exposure (right y-axis, 0 to 14k) versus Driver age (x-axis, 18 to 99). The chart includes four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso (dark blue line). The Exposure bars show a peak around age 45 and then decline. The True line shows a steady decline from age 39 to 75, then a sharp increase. The GLM line follows the True line closely but is slightly lower. The Lasso line follows the True line closely but is slightly higher, showing a flatter slope for older drivers.](6d7ea97b394612dbfb0170561cbee9c6_img.jpg)

| Driver age | Exposure (bars) | True (purple) | GLM (orange) | Lasso (dark blue) |
|------------|-----------------|---------------|--------------|-------------------|
| 18         | ~1k             | ~1.0          | ~1.0         | ~1.0              |
| 21         | ~1.5k           | ~0.98         | ~0.98        | ~0.98             |
| 24         | ~2k             | ~0.96         | ~0.96        | ~0.96             |
| 27         | ~2.5k           | ~0.94         | ~0.94        | ~0.94             |
| 30         | ~3k             | ~0.92         | ~0.92        | ~0.92             |
| 33         | ~3.5k           | ~0.9          | ~0.9         | ~0.9              |
| 36         | ~4k             | ~0.88         | ~0.88        | ~0.88             |
| 39         | ~4.5k           | ~0.86         | ~0.86        | ~0.86             |
| 42         | ~5k             | ~0.84         | ~0.84        | ~0.84             |
| 45         | ~5.5k           | ~0.82         | ~0.82        | ~0.82             |
| 48         | ~6k             | ~0.8          | ~0.8         | ~0.8              |
| 51         | ~6.5k           | ~0.78         | ~0.78        | ~0.78             |
| 54         | ~7k             | ~0.76         | ~0.76        | ~0.76             |
| 57         | ~7.5k           | ~0.74         | ~0.74        | ~0.74             |
| 60         | ~8k             | ~0.72         | ~0.72        | ~0.72             |
| 63         | ~8.5k           | ~0.7          | ~0.7         | ~0.7              |
| 66         | ~9k             | ~0.68         | ~0.68        | ~0.68             |
| 69         | ~9.5k           | ~0.66         | ~0.66        | ~0.66             |
| 72         | ~10k            | ~0.64         | ~0.64        | ~0.64             |
| 75         | ~10.5k          | ~0.62         | ~0.62        | ~0.62             |
| 78         | ~11k            | ~0.6          | ~0.6         | ~0.6              |
| 81         | ~11.5k          | ~0.58         | ~0.58        | ~0.58             |
| 84         | ~12k            | ~0.56         | ~0.56        | ~0.56             |
| 87         | ~12.5k          | ~0.54         | ~0.54        | ~0.54             |
| 90         | ~13k            | ~0.52         | ~0.52        | ~0.52             |
| 93         | ~13.5k          | ~0.5          | ~0.5         | ~0.5              |
| 96         | ~14k            | ~0.48         | ~0.48        | ~0.48             |
| 99         | ~14.5k          | ~0.46         | ~0.46        | ~0.46             |

Figure 7.12: A dual-axis chart showing Relativity (left y-axis, 0.85 to 1.0) and Exposure (right y-axis, 0 to 14k) versus Driver age (x-axis, 18 to 99). The chart includes four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso (dark blue line). The Exposure bars show a peak around age 45 and then decline. The True line shows a steady decline from age 39 to 75, then a sharp increase. The GLM line follows the True line closely but is slightly lower. The Lasso line follows the True line closely but is slightly higher, showing a flatter slope for older drivers.

**Figure 7.13. Both Models are Reacting Only Very Slightly to the Decrease in True Risk Relativity After Vehicle Age 10**

![Figure 7.13: A dual-axis chart showing Relativity (left axis, 0.9 to 1.3) and Exposure (right axis, 0 to 70k) versus Vehicle Age (0 to 19). The chart includes four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso (blue line). The True and GLM lines show a sharp decline in relativity from age 0 to 10, then level off. The Lasso line shows a much flatter decline. Exposure increases with age until age 10, then decreases.](4aa5a040cd7f031e935bff34790ea96f_img.jpg)

| Vehicle Age | Exposure (k) | True Relativity | GLM Relativity | Lasso Relativity |
|-------------|--------------|-----------------|----------------|------------------|
| 0           | 0            | 1.35            | 1.35           | 1.35             |
| 1           | 10           | 1.30            | 1.30           | 1.30             |
| 2           | 25           | 1.25            | 1.25           | 1.25             |
| 3           | 35           | 1.20            | 1.20           | 1.20             |
| 4           | 40           | 1.15            | 1.15           | 1.15             |
| 5           | 45           | 1.10            | 1.10           | 1.10             |
| 6           | 45           | 1.05            | 1.05           | 1.05             |
| 7           | 40           | 1.00            | 1.00           | 1.00             |
| 8           | 35           | 0.95            | 0.95           | 0.95             |
| 9           | 30           | 0.90            | 0.90           | 0.90             |
| 10          | 25           | 0.85            | 0.85           | 0.85             |
| 11          | 20           | 0.80            | 0.80           | 0.80             |
| 12          | 15           | 0.75            | 0.75           | 0.75             |
| 13          | 10           | 0.70            | 0.70           | 0.70             |
| 14          | 5            | 0.65            | 0.65           | 0.65             |
| 15          | 5            | 0.60            | 0.60           | 0.60             |
| 16          | 5            | 0.55            | 0.55           | 0.55             |
| 17          | 5            | 0.50            | 0.50           | 0.50             |
| 18          | 5            | 0.45            | 0.45           | 0.45             |
| 19          | 5            | 0.40            | 0.40           | 0.40             |

Figure 7.13: A dual-axis chart showing Relativity (left axis, 0.9 to 1.3) and Exposure (right axis, 0 to 70k) versus Vehicle Age (0 to 19). The chart includes four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso (blue line). The True and GLM lines show a sharp decline in relativity from age 0 to 10, then level off. The Lasso line shows a much flatter decline. Exposure increases with age until age 10, then decreases.

Rather than rejecting all signal from a variable based on significance, penalized regression is able to reflect some of that experience by imposing a high shrinkage. Additionally, where  $p$ -values are closer to our 0.05 threshold, such as with extra-light vehicles in Figure 7.14, the model has automatically applied shrinkage to reflect that uncertainty. In GLMs, we would have to make this selection judgmentally after model fitting.

**Figure 7.14. Extra-light vehicles are shrunk slightly toward 1.0. The GLM is overestimating the true relativity, whereas our lasso model is underestimating the true relativity.**

![Figure 7.14: A dual-axis chart showing Relativity (left axis, 0.7 to 1.3) and Exposure (right axis, 0 to 450k) versus Vehicle weight categories: Weight extra light, Weight heavy, Weight light, and Weight medium. The chart includes four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso (blue line). The True line shows a sharp dip in relativity for 'Weight heavy' and a peak for 'Weight light'. The GLM line is slightly above the True line for 'Weight extra light' and below for 'Weight light'. The Lasso line is slightly below the True line for 'Weight extra light' and above for 'Weight light'.](fc3763c02020b3a260045bbadc1d36ba_img.jpg)

| Vehicle weight     | Exposure (k) | True Relativity | GLM Relativity | Lasso Relativity |
|--------------------|--------------|-----------------|----------------|------------------|
| Weight extra light | 0            | 1.30            | 1.32           | 1.28             |
| Weight heavy       | 50           | 0.70            | 0.70           | 0.70             |
| Weight light       | 120          | 1.15            | 1.10           | 1.10             |
| Weight medium      | 250          | 1.00            | 1.00           | 1.00             |

Figure 7.14: A dual-axis chart showing Relativity (left axis, 0.7 to 1.3) and Exposure (right axis, 0 to 450k) versus Vehicle weight categories: Weight extra light, Weight heavy, Weight light, and Weight medium. The chart includes four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso (blue line). The True line shows a sharp dip in relativity for 'Weight heavy' and a peak for 'Weight light'. The GLM line is slightly above the True line for 'Weight extra light' and below for 'Weight light'. The Lasso line is slightly below the True line for 'Weight extra light' and above for 'Weight light'.

### 7.4.2. *Shrinkage Varies between Engineered Features*

A corollary to low significance having high shrinkage is that shrinkage will vary for different transformations of continuous variables or for different levels of a categorical variable. The variable `vehicle_age_10_99_hinge` saw significantly more shrinkage than `vehicle_age_0_9_hinge`. This shrinkage is correlated with the exposure distribution of the continuous variable, as there are fewer exposures after vehicle age 10. As we noted earlier, lasso credibility is a likelihood-based credibility procedure and likelihood correlates heavily with exposure distribution. Therefore, the exposure distribution can be used by a modeler to understand where and why coefficients may see shrinkage.

### 7.4.3. *Credibility and Feature Engineering*

It follows that uncapped continuous variables and polynomial terms will not reflect credibility in a way similar to our segmented hinge feature engineering, which changes factors for only a portion of a given feature. A polynomial term such as `vehicle_age_squared` would have an effect across the entire distribution of vehicle ages and will use the “credibility” of the newer ages to extrapolate to the older ages. Intuitively, it is difficult to rationalize how the credibility of vehicle ages 0 to 9 can be used to support changes in ages 10 to 99. An ordinal treatment of variables as in derivative lasso or AGLM will apply shrinkage and credibility intuitively and appropriately. An ideal application of lasso credibility will use feature engineering that is easily understood through the lens of credibility.

### 7.4.4. *Penalized Regression Benefits*

Let’s compare the lasso penalization to two different versions of the GLM: one including all coefficients and another excluding those whose  $p$ -value is greater than 5%.

When we do not exclude insignificant variables, the GLM does slightly outperform the lasso model on a double lift chart (Figure 7.15). However, this GLM includes variables that have failed our significance test. Fortunately for the GLM, those unstable variables have experience similar to the true risk relativities. But without knowing the true relativities, how could we be sure that the insignificant variables are truly beneficial? Unfortunately, the GLM does not have the ability to assign partial credibility, and therefore we must refit the model without those variables. Even if the modeler takes a risk and gives the variables the benefit of the doubt, it is worth noting that the  $y$ -axis of Figure 7.15 is quite condensed and the lasso model is not being outperformed by a large margin.

If we remove the insignificant variables from our GLM (Figure 7.16), the lasso penalized regression model performs significantly better in the tails of the double lift chart while performing within 1% of the true relativities for the middle deciles.

**Figure 7.15. The GLM that Includes Insignificant Variables is Outperforming Our Penalized Regression Model by More Than 2% in the Lowest Decile**

![Figure 7.15: A dual-axis chart showing Normalized predictions and Exposure across 10 deciles. The chart compares four models: Exposure (blue bars), True (purple line), GLM (yellow line), and Lasso (blue line). The left y-axis represents Normalized predictions (0.99 to 1.02), and the right y-axis represents Exposure (0 to 60k). The x-axis represents Decile (1 to 10).](fce2a4a923b40ec0421e00ecb8e809c9_img.jpg)

Figure 7.15 is a dual-axis chart. The x-axis represents Decile (1 to 10). The left y-axis represents Normalized predictions (0.99 to 1.02). The right y-axis represents Exposure (0 to 60k). The chart compares four models: Exposure (blue bars), True (purple line), GLM (yellow line), and Lasso (blue line). The True model is a horizontal line at 1.0. The GLM model starts at approximately 0.998 in decile 1, peaks at 1.006 in decile 2, and then fluctuates around 1.0. The Lasso model starts at approximately 1.022 in decile 1 and decreases steadily to approximately 0.991 in decile 10. The Exposure bars are constant at approximately 40k.

| Decile | Exposure (k) | True  | GLM   | Lasso |
|--------|--------------|-------|-------|-------|
| 1      | 40           | 1.000 | 0.998 | 1.022 |
| 2      | 40           | 1.000 | 1.006 | 1.021 |
| 3      | 40           | 1.000 | 1.003 | 1.013 |
| 4      | 40           | 1.000 | 1.000 | 1.007 |
| 5      | 40           | 1.000 | 1.000 | 1.005 |
| 6      | 40           | 1.000 | 0.998 | 1.001 |
| 7      | 40           | 1.000 | 0.997 | 0.997 |
| 8      | 40           | 1.000 | 0.996 | 0.993 |
| 9      | 40           | 1.000 | 0.998 | 0.991 |
| 10     | 40           | 1.000 | 1.004 | 0.991 |

Figure 7.15: A dual-axis chart showing Normalized predictions and Exposure across 10 deciles. The chart compares four models: Exposure (blue bars), True (purple line), GLM (yellow line), and Lasso (blue line). The left y-axis represents Normalized predictions (0.99 to 1.02), and the right y-axis represents Exposure (0 to 60k). The x-axis represents Decile (1 to 10).

With this comparison we aim to illustrate that **some credibility is better than none**. Where we know that full credibility is not supportable, a partial credibility solution is better than the binary choice of removing a variable. Lasso penalization recognized this partial credibility and applied significant shrinkage to coefficients that were not significant in the GLM. That shrinkage resulted in a coefficient between our fully credible GLM coefficient and a 0.0 coefficient. A partial credibility treatment of coefficients is what allows the lasso model to outperform the GLM.

**Figure 7.16. After Excluding Insignificant Coefficients, the GLM No Longer Outperforms the Lasso Penalized Regression Model**

![Figure 7.16: A dual-axis chart showing Normalized predictions and Exposure across 10 deciles. The chart compares four models: Exposure (blue bars), True (purple line), GLM (yellow line), and Lasso (blue line). The left y-axis represents Normalized predictions (0.96 to 1.04), and the right y-axis represents Exposure (0 to 60k). The x-axis represents Decile (1 to 10).](318f02285df33c4d38cdad30845972d4_img.jpg)

Figure 7.16 is a dual-axis chart. The x-axis represents Decile (1 to 10). The left y-axis represents Normalized predictions (0.96 to 1.04). The right y-axis represents Exposure (0 to 60k). The chart compares four models: Exposure (blue bars), True (purple line), GLM (yellow line), and Lasso (blue line). The True model is a horizontal line at 1.0. The GLM model starts at approximately 0.965 in decile 1, rises to 1.000 in decile 2, and then fluctuates around 1.0. The Lasso model starts at approximately 0.998 in decile 1, rises to 1.012 in decile 2, and then fluctuates around 1.0. The Exposure bars are constant at approximately 40k.

| Decile | Exposure (k) | True  | GLM   | Lasso |
|--------|--------------|-------|-------|-------|
| 1      | 40           | 1.000 | 0.965 | 0.998 |
| 2      | 40           | 1.000 | 1.000 | 1.012 |
| 3      | 40           | 1.000 | 0.998 | 1.007 |
| 4      | 40           | 1.000 | 0.997 | 1.004 |
| 5      | 40           | 1.000 | 0.996 | 1.000 |
| 6      | 40           | 1.000 | 0.996 | 0.998 |
| 7      | 40           | 1.000 | 0.997 | 0.996 |
| 8      | 40           | 1.000 | 1.000 | 0.997 |
| 9      | 40           | 1.000 | 1.002 | 0.997 |
| 10     | 40           | 1.000 | 1.019 | 1.005 |

Figure 7.16: A dual-axis chart showing Normalized predictions and Exposure across 10 deciles. The chart compares four models: Exposure (blue bars), True (purple line), GLM (yellow line), and Lasso (blue line). The left y-axis represents Normalized predictions (0.96 to 1.04), and the right y-axis represents Exposure (0 to 60k). The x-axis represents Decile (1 to 10).

## 7.5. “Large State” —Lasso Credibility Versus GLM

We use the relativities from our full model as a complement for this subset.<sup>9</sup> By using our countrywide model as a complement of credibility, we are modeling credible differences from that model instead of creating an entirely new model from scratch. The inclusion of the extra information allows us to build a much more robust model than our GLM or lasso penalization model.

The large state data contains different true risk relativities than the base modeling data for the variables industry code (Figure 7.7), multipolicy discount (Figure 7.4), driver age (Figure 7.2), and vehicle age (Figure 7.3).

The shrinkage present in the lasso credibility model highlights the model’s ability to react to various levels of credibility in the data. Some coefficients see high shrinkage where the difference between the complement and modeled relativity is set to zero, and others see low shrinkage and high reactivity. To illustrate this, relativity plots will now include each variable’s complement of credibility. The penalized regression relativities are labeled as “lasso credibility” and are always between the complement relativity and the GLM relativity.

### 7.5.1. Coefficients of Zero Show Confidence in the Complement of Credibility

The lasso credibility coefficients for farming and food services are **completely removed** by the model’s penalization. When a coefficient is at or very near zero in a GLM, the modeler can say that this characteristic is not predictive and should be removed from the model. On the other hand, lasso credibility concludes that there is “no credible difference” from our complement. Either the model has high confidence in the complement, low confidence in the data, or a combination of the two where the bias–variance trade-off is optimized through the application of bias.

Looking at Table 7.3, we can see that the difference between the fully credible GLM estimate and the complement of credibility is quite small. In high-exposure segments,

**Table 7.3. A Comparison of Farming and Food Service Industry Code Relativities between Models**

| Model                     | Farming Relativity | Food Service Relativity |
|---------------------------|--------------------|-------------------------|
| Complement of credibility | .680               | 1.205                   |
| Lasso credibility         | .680               | 1.205                   |
| True relativity           | .700               | 1.200                   |
| GLM                       | .668               | 1.171                   |

<sup>9</sup> As always, an actuary should review the considerations in ASOP 25 when selecting a complement of credibility (see Section 5.4). The review should focus on this item in ASOP 25’s Section 3.3, “Selection of Relevant Experience”: “The actuary should consider the extent to which subject experience is included in relevant experience. If subject experience data is a material part of relevant experience, the use of that relevant experience may not be appropriate.” We assume that our large state subset did not have an undue influence on the full model’s predictions.

**Table 7.4. A Comparison of the Construction Industry Code Relativities Across our Different Models**

| Model                     | Construction Relativity |
|---------------------------|-------------------------|
| Complement of credibility | 1.460                   |
| Lasso credibility         | 1.436                   |
| True relativity           | 1.4                     |
| GLM                       | 1.379                   |

the likelihood benefit of small differences may produce credible deviations. However, in these lower-exposure segments, the likelihood improvement of moving toward the GLM estimate does not outweigh the penalty incurred by a nonzero coefficient.

### 7.5.2. Partially Credible Categories Avoid Overreactions

Other categorical coefficients do deviate from the complement of credibility. The lasso coefficient for construction is quite small: only  $-0.0163$ . The credibility-weighted relativity is moving toward the true relativity in our relativity plot but does not quite get there. On the other hand, moving from our complement relativity to the GLM relativity would overshoot the true relativity. The stability provided by lasso credibility can prevent unnecessarily large policyholder impacts caused by assigning too much credibility to noisy data while still moving closer to the true relativity as seen in Table 7.4.

### 7.5.3. Credible Categories React Quickly

The complement for multipolicy discount is not accurate in our large state example, and yet our lasso credibility estimate is still quite close to the GLM estimate as seen in Table 7.5. We can draw two conclusions from this:

1. Large categories can approach full credibility in the same model where small categories receive small or no credibility. (Figure 7.17 and Figure 7.18)
2. The complement of credibility is less material in categories with large exposure and more material in categories with small exposure. (Figure 7.17 and Figure 7.18)

**Table 7.5. A Comparison of Factors for the Multipolicy Discount Variable**

| Model                     | Relativity |
|---------------------------|------------|
| Complement of credibility | .772       |
| Lasso credibility         | .704       |
| True relativity           | .7         |
| GLM                       | .694       |

**Figure 7.17. Categories with High Levels of Exposure are Closer to the GLM Estimates Than Categories with Low Exposure**

![Figure 7.17: A dual-axis chart showing the relative difference between GLM estimates and true values across various industries, plotted against exposure levels. The left y-axis represents 'Relativity' (0.4 to 1.6), and the right y-axis represents 'Exposure' (0 to 150k). The x-axis lists industries: Construction, Education, Farming, Finance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The legend includes: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The chart shows that for industries with high exposure (e.g., Food services, Real estate, Retail), the GLM estimate is closer to the true value than for industries with low exposure (e.g., Construction, Farming).](b3faf87063b80c8f67bb574a903ca7e0_img.jpg)

| Industry      | Exposure (k) | True | GLM  | Lasso credibility | Complement |
|---------------|--------------|------|------|-------------------|------------|
| Construction  | ~10k         | ~1.4 | ~1.4 | ~1.45             | ~1.4       |
| Education     | ~100k        | ~1.0 | ~1.0 | ~1.0              | ~1.0       |
| Farming       | ~10k         | ~0.7 | ~0.7 | ~0.7              | ~0.7       |
| Finance       | ~90k         | ~0.5 | ~0.5 | ~0.5              | ~0.5       |
| Fine arts     | ~90k         | ~0.9 | ~0.9 | ~0.9              | ~0.9       |
| Fireworks     | ~10k         | ~0.4 | ~0.4 | ~0.4              | ~0.4       |
| Food services | ~130k        | ~1.2 | ~1.2 | ~1.2              | ~1.2       |
| Health care   | ~10k         | ~0.4 | ~0.4 | ~0.4              | ~0.4       |
| Real estate   | ~10k         | ~0.6 | ~0.6 | ~0.6              | ~0.6       |
| Retail        | ~60k         | ~0.8 | ~0.8 | ~0.8              | ~0.8       |

Figure 7.17: A dual-axis chart showing the relative difference between GLM estimates and true values across various industries, plotted against exposure levels. The left y-axis represents 'Relativity' (0.4 to 1.6), and the right y-axis represents 'Exposure' (0 to 150k). The x-axis lists industries: Construction, Education, Farming, Finance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The legend includes: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The chart shows that for industries with high exposure (e.g., Food services, Real estate, Retail), the GLM estimate is closer to the true value than for industries with low exposure (e.g., Construction, Farming).

**Figure 7.18. Categories with High Levels of Exposure are Closer to the GLM Estimates Than Categories with Low Exposure**

![Figure 7.18: A dual-axis chart showing the relative difference between GLM estimates and true values for 'Multi policy discount' categories, plotted against exposure levels. The left y-axis represents 'Relativity' (0.7 to 1.0), and the right y-axis represents 'Exposure' (0 to 350k). The x-axis shows two categories: 'Multi no' and 'Multi yes'. The legend includes: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The chart shows that for the 'Multi yes' category, which has a higher exposure level, the GLM estimate is closer to the true value than for the 'Multi no' category.](07b0d4a97040103ce6c822c3983a9c05_img.jpg)

| Category  | Exposure (k) | True | GLM  | Lasso credibility | Complement |
|-----------|--------------|------|------|-------------------|------------|
| Multi no  | ~200k        | ~1.0 | ~1.0 | ~1.0              | ~1.0       |
| Multi yes | ~100k        | ~0.7 | ~0.7 | ~0.7              | ~0.7       |

Figure 7.18: A dual-axis chart showing the relative difference between GLM estimates and true values for 'Multi policy discount' categories, plotted against exposure levels. The left y-axis represents 'Relativity' (0.7 to 1.0), and the right y-axis represents 'Exposure' (0 to 350k). The x-axis shows two categories: 'Multi no' and 'Multi yes'. The legend includes: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The chart shows that for the 'Multi yes' category, which has a higher exposure level, the GLM estimate is closer to the true value than for the 'Multi no' category.

The observation may seem trivial, but it is included to stress that not all components of the complement will be equally influential on model results.

### 7.5.4. Lasso Credibility Moves Toward Experienced Relativities

In Figure 7.19, shrinkage moves the driver\_age\_76\_99\_hinge coefficient toward indicated without overreacting, and the final driver age factor curve produced by our lasso credibility model is extremely close to the true relativities. This coefficient is insignificant in the GLM, and this variable would likely be completely removed from the model. By reflecting the credibility of our data, lasso credibility has achieved a great result.

On the other hand, Figure 7.20 shows that the 20% shrinkage applied to the vehicle\_age\_10\_99\_hinge coefficient assigns some credibility to the simulated experience, and this experience is quite far from the true relativity. This variable's insignificance in the GLM does not solve the problem, as removing the coefficient would result in an even more incorrect aggregate relativity.

Credibility procedures are effective in many cases, but it is still possible for particularly noisy data to draw indicated relativities away from the true relativities.

### 7.5.5. Performance Comparison: Lasso Credibility Versus Lasso Versus GLM

We can see in the double lift charts (Figures 7.21 and 7.22) that lasso credibility outperforms our GLM and penalized regression models in our large state example.

However, *this is not proof that lasso credibility will always outperform other model types*. When data is thin, lasso credibility's performance depends on a properly selected complement to pull the indicated relativities toward the true relativities. To illustrate

**Figure 7.19. Lasso Credibility Prevents the Driver Age Relativity from Flattening Out Too Much for Older Driver Ages**

![Figure 7.19: A dual-axis chart showing Relativity (left axis, 0.85 to 1.15) and Exposure (right axis, 0 to 14k) versus Driver age (x-axis, 18 to 99). The chart compares four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso credibility (green line). The Lasso credibility line closely follows the True line, while the GLM line deviates significantly, especially for older driver ages. A green line labeled 'Complement' is also shown, which is a steep, nearly vertical line at age 36.](9769887d8991efda1c2fcfc74657c52d_img.jpg)

The chart displays the relationship between driver age and relativity/exposure. The x-axis represents driver age from 18 to 99. The left y-axis represents Relativity from 0.85 to 1.15. The right y-axis represents Exposure from 0 to 14k. The blue bars represent Exposure, which increases with age and then decreases for older ages. The purple line represents the True relativity, which starts at 1.0 and decreases as age increases. The orange line represents the GLM relativity, which starts at 1.0 and decreases more sharply than the True line. The green line represents the Lasso credibility relativity, which starts at 1.0 and decreases more gradually than the GLM line, staying closer to the True line. A green line labeled 'Complement' is also shown, which is a steep, nearly vertical line at age 36.

Figure 7.19: A dual-axis chart showing Relativity (left axis, 0.85 to 1.15) and Exposure (right axis, 0 to 14k) versus Driver age (x-axis, 18 to 99). The chart compares four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso credibility (green line). The Lasso credibility line closely follows the True line, while the GLM line deviates significantly, especially for older driver ages. A green line labeled 'Complement' is also shown, which is a steep, nearly vertical line at age 36.

**Figure 7.20. Lasso Credibility Prevents the Vehicle Age Relativity from Becoming Too Flat for Higher Vehicle Ages**

![Figure 7.20: A dual-axis chart showing Relativity (left axis, 0.9 to 1.4) and Exposure (right axis, 0 to 70k) versus Vehicle age (0 to 19). The chart includes five data series: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The GLM line is relatively flat for ages 10 and above, while the Lasso credibility line shows a more pronounced downward trend, staying closer to the True line.](0074c6f00020bf1c56b95a37a7a9e599_img.jpg)

| Vehicle age | Exposure (k) | True Relativity | GLM Relativity | Lasso Relativity | Complement Relativity |
|-------------|--------------|-----------------|----------------|------------------|-----------------------|
| 0           | 2            | 1.35            | 1.35           | 1.35             | 1.35                  |
| 1           | 10           | 1.30            | 1.30           | 1.30             | 1.30                  |
| 2           | 20           | 1.25            | 1.25           | 1.25             | 1.25                  |
| 3           | 30           | 1.20            | 1.20           | 1.20             | 1.20                  |
| 4           | 35           | 1.15            | 1.15           | 1.15             | 1.15                  |
| 5           | 38           | 1.12            | 1.12           | 1.12             | 1.12                  |
| 6           | 35           | 1.10            | 1.10           | 1.10             | 1.10                  |
| 7           | 30           | 1.08            | 1.08           | 1.08             | 1.08                  |
| 8           | 25           | 1.05            | 1.05           | 1.05             | 1.05                  |
| 9           | 20           | 1.02            | 1.02           | 1.02             | 1.02                  |
| 10          | 15           | 1.00            | 1.00           | 1.00             | 1.00                  |
| 11          | 12           | 0.98            | 1.00           | 0.98             | 0.98                  |
| 12          | 10           | 0.96            | 1.00           | 0.96             | 0.96                  |
| 13          | 8            | 0.94            | 1.00           | 0.94             | 0.94                  |
| 14          | 6            | 0.92            | 1.00           | 0.92             | 0.92                  |
| 15          | 5            | 0.90            | 1.00           | 0.90             | 0.90                  |
| 16          | 4            | 0.88            | 0.98           | 0.88             | 0.88                  |
| 17          | 3            | 0.86            | 0.96           | 0.86             | 0.86                  |
| 18          | 2            | 0.84            | 0.94           | 0.84             | 0.84                  |
| 19          | 1            | 0.82            | 0.92           | 0.82             | 0.82                  |

Figure 7.20: A dual-axis chart showing Relativity (left axis, 0.9 to 1.4) and Exposure (right axis, 0 to 70k) versus Vehicle age (0 to 19). The chart includes five data series: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The GLM line is relatively flat for ages 10 and above, while the Lasso credibility line shows a more pronounced downward trend, staying closer to the True line.

this, examine the table below, which displays information on the indicated relativities of the health care and farming categories. The GLM produces an estimate closer to the true relativity for health care because the selected complements 1.399 and 1.0 are quite far from the true relativity of 1.2. The signal from the data was not strong enough to overcome the poor choice of complement. For the farming category relativity, the choice of complement is less material given the larger amount of exposure in this category.

**Figure 7.21. The lasso credibility model clearly outperforms the GLM even when allowing lucky insignificant coefficients. After removing those coefficients, the lift is even more dramatic. This further supports our earlier opinion that some credibility is better than none.**

![Figure 7.21: A dual-axis chart showing Normalized predictions (left axis, 0.96 to 1.08) and Exposure (right axis, 0 to 60k) versus Decile (1 to 10). The chart includes four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso credibility (green line). The GLM line shows a significant upward trend in normalized predictions for deciles 6 through 10, while the Lasso credibility line remains relatively flat and close to the True line.](4a9c983747ecc039ce50538a46311713_img.jpg)

| Decile | Exposure (k) | True Normalized | GLM Normalized | Lasso Normalized |
|--------|--------------|-----------------|----------------|------------------|
| 1      | 5            | 1.00            | 0.96           | 1.00             |
| 2      | 15           | 1.00            | 0.975          | 1.00             |
| 3      | 25           | 1.00            | 0.98           | 0.995            |
| 4      | 35           | 1.00            | 0.99           | 1.00             |
| 5      | 40           | 1.00            | 0.995          | 0.995            |
| 6      | 45           | 1.00            | 1.005          | 1.00             |
| 7      | 45           | 1.00            | 1.005          | 0.995            |
| 8      | 45           | 1.00            | 1.015          | 1.00             |
| 9      | 45           | 1.00            | 1.025          | 0.995            |
| 10     | 45           | 1.00            | 1.07           | 1.015            |

Figure 7.21: A dual-axis chart showing Normalized predictions (left axis, 0.96 to 1.08) and Exposure (right axis, 0 to 60k) versus Decile (1 to 10). The chart includes four data series: Exposure (blue bars), True (purple line), GLM (orange line), and Lasso credibility (green line). The GLM line shows a significant upward trend in normalized predictions for deciles 6 through 10, while the Lasso credibility line remains relatively flat and close to the True line.

**Figure 7.22. The Lasso Credibility Model Clearly Outperforms the Traditional Lasso Penalized Regression Model**

![Figure 7.22: A dual-axis chart comparing four models across 10 deciles. The left y-axis shows 'Normalized predictions' (0.96 to 1.1) and the right y-axis shows 'Exposure' (0 to 60k). The x-axis is 'Decile' (1 to 10). The legend includes: Exposure (blue bars), True (purple line), Lasso (dark blue line), and Lasso credibility (green line). The 'True' line is flat at 1.0. The 'Lasso' line starts at ~0.955 in decile 1 and rises to ~1.09 in decile 10. The 'Lasso credibility' line stays near 1.0 until decile 9, then rises to ~1.025 in decile 10. The 'Exposure' bars are constant at ~40k.](f3d96eb3ce2f7940025d304ba65c1d68_img.jpg)

| Decile | Exposure (k) | True | Lasso | Lasso credibility |
|--------|--------------|------|-------|-------------------|
| 1      | 40           | 1.00 | 0.955 | 1.00              |
| 2      | 40           | 1.00 | 0.975 | 0.995             |
| 3      | 40           | 1.00 | 0.985 | 0.995             |
| 4      | 40           | 1.00 | 0.990 | 0.995             |
| 5      | 40           | 1.00 | 0.995 | 0.995             |
| 6      | 40           | 1.00 | 1.000 | 0.995             |
| 7      | 40           | 1.00 | 1.005 | 0.995             |
| 8      | 40           | 1.00 | 1.010 | 1.000             |
| 9      | 40           | 1.00 | 1.035 | 1.005             |
| 10     | 40           | 1.00 | 1.090 | 1.025             |

Figure 7.22: A dual-axis chart comparing four models across 10 deciles. The left y-axis shows 'Normalized predictions' (0.96 to 1.1) and the right y-axis shows 'Exposure' (0 to 60k). The x-axis is 'Decile' (1 to 10). The legend includes: Exposure (blue bars), True (purple line), Lasso (dark blue line), and Lasso credibility (green line). The 'True' line is flat at 1.0. The 'Lasso' line starts at ~0.955 in decile 1 and rises to ~1.09 in decile 10. The 'Lasso credibility' line stays near 1.0 until decile 9, then rises to ~1.025 in decile 10. The 'Exposure' bars are constant at ~40k.

Both a good complement of .68 and a poor complement of 1.0 produce similar modeled coefficients close to the true relativity as seen in Table 7.6.

In general, lasso credibility will be of more actuarial benefit than a GLM when the complement of credibility is pulling the indicated relativities in the correct direction toward their true relativities. Additionally, lasso credibility should outperform lasso penalization when the selected complement of credibility is more appropriate than the default assumption of 1.0. A poor complement can cause lasso credibility to perform worse than both lasso penalization and GLM.

### 7.5.6. Large State Conclusion

When we subset our data to this level, high-exposure segments still show minimal deviation in indicated relativities between the GLM and lasso credibility models. However, for smaller categories and some continuous variables, the GLM is already unable to provide significant coefficients. A modeler could explore additional feature engineering or the removal of insignificant variables in favor of an offset. Such additional adjustments and feature engineering would also benefit the lasso credibility model.

**Table 7.6. A comparison of the Health Care and Farming Factors between Models**

| Category    | True Relativity | GLM   | Lasso Credibility Complement | Lasso Credibility with Original Complement | "Lasso Credibility" 1.0 Complement |
|-------------|-----------------|-------|------------------------------|--------------------------------------------|------------------------------------|
| Health care | 1.2             | 1.165 | 1.399                        | 1.288                                      | 1.101                              |
| Farming     | .7              | .668  | .680                         | .680                                       | .718                               |

Lasso credibility is effective on data of this size, and we suggest that data of **all** sizes, even as large as our full modeling data set, can benefit from the application of lasso credibility. For every large data set, there is likely a not-fully-credible category. This not-fully-credible category can benefit from lasso credibility. From a theory perspective, this is motivated by the bias–variance trade-off (Chapter 4). For example, industry codes in the full modeling data set can be split into increasingly granular subsets until they begin to lose credibility and significance. Lasso credibility can help a modeler gain lift that would otherwise be unattainable for these segments.

Here are some recommended exercises with the large state subset:

- Rerun the lasso credibility model with different complements of varying quality. Observe how the complement has more effect in low-exposure categories and segments than high-exposure segments.
- Resimulate the large state subset with a different seed. How consistent are the results from lasso credibility? How consistent are the results from a GLM?
- Resimulate the large state subset with different underlying relativities. How quickly does lasso credibility react to these differences? Is a GLM able to model these new relativities with significant coefficients?

## 7.6. “Medium State” – Lasso Credibility Versus GLM

A quick examination of the relativity plot for industry code (Figure 7.23) will show that both the generalized linear and lasso credibility models are producing indicated relativities quite far from the true relativities, and quite nonsensical ones for the fireworks industry code. Additionally, many of the coefficients are insignificant in our GLM. Is this data set too small or volatile to model? The answer is no: an adjustment of the penalty term in lasso credibility enables us to build an acceptable model on this data set.

**Figure 7.23. Both Models are Producing Inaccurate Relativities for Real Estate, and the Indicated Relativity for Fireworks is Directionally Incorrect**

![Figure 7.23: A dual-axis chart comparing Exposure (bars), True Relativity (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line) across various industries. The left Y-axis is Relativity (0 to 3) and the right Y-axis is Exposure (0 to 100k). The X-axis lists industries: Construction, Education, Farming, Finance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The chart shows that both models (GLM and Lasso) produce inaccurate relativities compared to the true values, and the Complement line shows extreme volatility, particularly for Fireworks.](ce951c49dba8deb9a7fda642899b99a4_img.jpg)

| Industry      | Exposure (k) | True Relativity | GLM Relativity | Lasso Relativity | Complement Relativity |
|---------------|--------------|-----------------|----------------|------------------|-----------------------|
| Construction  | 20k          | 1.5             | 1.4            | 1.5              | 1.5                   |
| Education     | 60k          | 1.0             | 1.0            | 1.0              | 1.0                   |
| Farming       | 10k          | 0.7             | 0.6            | 0.7              | 0.7                   |
| Finance       | 40k          | 0.5             | 0.5            | 0.5              | 0.5                   |
| Fine arts     | 40k          | 1.1             | 1.1            | 1.1              | 1.1                   |
| Fireworks     | 0k           | 1.5             | 0.2            | 0.2              | 2.8                   |
| Food services | 30k          | 1.2             | 1.2            | 1.2              | 1.2                   |
| Health care   | 5k           | 1.3             | 1.3            | 1.3              | 1.3                   |
| Real estate   | 5k           | 0.6             | 0.6            | 0.6              | 0.6                   |
| Retail        | 20k          | 0.8             | 0.8            | 0.8              | 0.8                   |

Figure 7.23: A dual-axis chart comparing Exposure (bars), True Relativity (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line) across various industries. The left Y-axis is Relativity (0 to 3) and the right Y-axis is Exposure (0 to 100k). The X-axis lists industries: Construction, Education, Farming, Finance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The chart shows that both models (GLM and Lasso) produce inaccurate relativities compared to the true values, and the Complement line shows extreme volatility, particularly for Fireworks.

### 7.6.1. Evaluating the Assigned Credibility

The relativity plot for industry code in Figure 7.23 has a couple of results that make us question the assigned credibility. First, in smaller data sets, a good complement would usually be given full credibility for some categories when their coefficients are penalized to zero. Only the health care coefficient is penalized to zero in this example. This by itself is not a bad thing, but an actuary should review the credibility of deviations for reasonableness. Second, some of the coefficients are directionally different than the selected complement. Does it make sense that our real estate relativities are slightly surcharged in this subset as opposed to receiving a sizable discount? Maybe—industry knowledge would be necessary to determine whether this is a reasonable movement. Third, and most importantly, we see a truly unintuitive result in the fireworks category. This category of only 69 exposures is deviating from a complement of credibility of 2.796 to an indicated relativity of .167. This is surely a misallocation of credibility.

As discussed earlier in the monograph, one can choose from a range of statistically reasonable lambdas. This result is a reason to select a larger lambda and give more credibility to our complement.

How can we be sure to recognize this misallocation of credibility in practice? A strength of lasso credibility is that the penalty is applied to all coefficients identically and therefore applies an equal credibility standard across all variables. If the credibility standard is incorrect for one variable, it is incorrect for all variables. In practice, this is easily addressed: a modeler should always start with the penalty that produces the most statistically sound model. If that produces unreasonable results for one or more variables, we recommend increasing that penalty term until the results are actuarially reasonable across all variables. An ordinal treatment of variables can make this evaluation quite clear.

Would  $p$ -values have fixed this? Not really. Our GLM has an indicated coefficient of 0.01 for fireworks with a  $p$ -value of 0.0645. This is very close to significance, and if it weren't so obvious that this result is wholly unintuitive, an actuary might use the result as support to judgmentally assign some discount to this industry code. Additionally,  $p$ -values would remove most of our continuous variable transformations and four of the other industry code coefficients. With enough work, a modeler might be able to create a reasonable model through robust variable transformations, but in its current state, the GLM would be unusable.

### 7.6.2. Some Credibility is Better Than None

We have talked about how some credibility is better than none for individual coefficients, and now we describe how some credibility is also better than none in the aggregate. The HDtweedie package allows us to view the range of tested lambdas, so we built models with increasingly high lambdas until the results appeared reasonable for all variables. This process assigns less credibility to our entire data set. Looking at the relativity plots and comparing to true relativities, we can see that this model is not perfect. Older drivers still have too much of a surcharge, real estate is erroneously deviating from the complement of credibility, and the change to our xTreme turn signal

**Figure 7.24.** Although still quite off, the lasso credibility model is a bit closer to the true relative overall than the complement of credibility for the driver age variable.

![Figure 7.24: A dual-axis chart showing Relative (left axis, 1 to 2.5) and Exposure (right axis, 0 to 9000) versus Driver Age (x-axis, 18 to 99). The chart includes five data series: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The Exposure bars show a peak around age 45-50. The True and GLM lines are very close, starting high and decreasing. The Lasso credibility line is slightly higher than the True line, and the Complement line is the highest, starting very high and decreasing sharply.](1c3364622e6fab72c74fd34bf51dffb3_img.jpg)

Figure 7.24: A dual-axis chart showing Relative (left axis, 1 to 2.5) and Exposure (right axis, 0 to 9000) versus Driver Age (x-axis, 18 to 99). The chart includes five data series: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The Exposure bars show a peak around age 45-50. The True and GLM lines are very close, starting high and decreasing. The Lasso credibility line is slightly higher than the True line, and the Complement line is the highest, starting very high and decreasing sharply.

variable is not fully recognized. Despite this, **the lasso credibility model is better than our alternatives.** (See Figures 7.24, 7.25, and 7.26).

The GLM fails to produce significant coefficients for half of the industry codes in our model, and similarly three of our five continuous variable transformations are insignificant. An actuary may be tempted to implement the countrywide model in this state instead of a state-specific model rather than perform significant work to turn this into a usable model.

**Figure 7.25.** Lasso Credibility Partially Reacts to Signal in x-Treme Turn Signal Variable

![Figure 7.25: A dual-axis chart showing Relative (left axis, 0.3 to 1) and Exposure (right axis, 0 to 450k) versus x-Treme Turn Signal (x-axis, no, yes). The chart includes five data series: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The Exposure bars show a significant drop from 'no' to 'yes'. The True and GLM lines show a moderate decrease, while the Lasso credibility line shows a steeper decrease, and the Complement line shows the steepest decrease.](3cde6c4c2ef7528574b0dbbc1b3e23aa_img.jpg)

Figure 7.25: A dual-axis chart showing Relative (left axis, 0.3 to 1) and Exposure (right axis, 0 to 450k) versus x-Treme Turn Signal (x-axis, no, yes). The chart includes five data series: Exposure (blue bars), True (purple line), GLM (orange line), Lasso credibility (green line), and Complement (light green line). The Exposure bars show a significant drop from 'no' to 'yes'. The True and GLM lines show a moderate decrease, while the Lasso credibility line shows a steeper decrease, and the Complement line shows the steepest decrease.

**Figure 7.26. The Increased Penalty Term Has Placed Much More Weight on the Complement of Credibility**

![Figure 7.26: A dual-axis chart showing Relativity (left axis, 0 to 3) and Exposure (right axis, 0 to 100k) across various industries. The chart includes five data series: Exposure (blue bars), True (purple line with dots), GLM (orange line with dots), Lasso credibility (green line with dots), and Complement (light green line with dots). The industries on the x-axis are Construction, Education, Farming, Finance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The Lasso credibility model shows a significant peak in Fireworks, while the Complement model shows a sharp peak in Fine arts.](34cfb1835fdf0d248bc2c4d58956a896_img.jpg)

| Industry      | Exposure (k) | True Relativity | GLM Relativity | Lasso Relativity | Complement Relativity |
|---------------|--------------|-----------------|----------------|------------------|-----------------------|
| Construction  | 20k          | 1.5             | 1.4            | 1.5              | 1.5                   |
| Education     | 45k          | 1.0             | 1.0            | 1.0              | 1.0                   |
| Farming       | 10k          | 0.7             | 0.6            | 0.7              | 0.7                   |
| Finance       | 35k          | 0.5             | 0.5            | 0.5              | 0.5                   |
| Fine arts     | 35k          | 1.1             | 1.1            | 1.1              | 1.1                   |
| Fireworks     | 0k           | 1.5             | 0.0            | 1.7              | 2.8                   |
| Food services | 30k          | 1.2             | 1.1            | 1.2              | 1.2                   |
| Health care   | 5k           | 1.3             | 1.3            | 1.4              | 1.3                   |
| Real estate   | 5k           | 0.6             | 1.1            | 0.9              | 0.6                   |
| Retail        | 25k          | 0.7             | 0.7            | 0.8              | 0.8                   |

Figure 7.26: A dual-axis chart showing Relativity (left axis, 0 to 3) and Exposure (right axis, 0 to 100k) across various industries. The chart includes five data series: Exposure (blue bars), True (purple line with dots), GLM (orange line with dots), Lasso credibility (green line with dots), and Complement (light green line with dots). The industries on the x-axis are Construction, Education, Farming, Finance, Fine arts, Fireworks, Food services, Health care, Real estate, and Retail. The Lasso credibility model shows a significant peak in Fireworks, while the Complement model shows a sharp peak in Fine arts.

On the other hand, the lasso credibility model is improved simply by the tuning of the penalty parameter. Looking at the lift chart (Figure 7.27), we can see that the lasso credibility model is outperforming our countrywide model on this data set. By adjusting the penalty parameter, we are able to move closer to the state's true relativities without being overreactive. One of lasso credibility's key benefits is its ability to build models on data that would normally be considered out of scope for predictive modeling. Finding credible differences in a state's experience from a countrywide model is a key use case for lasso credibility.

**Figure 7.27. The Lasso Credibility Model Outperforms the Countrywide Complement of Credibility**

![Figure 7.27: A dual-axis chart showing Normalized predictions (left axis, 0.7 to 1.4) and Exposure (right axis, 0 to 40k) across deciles. The chart includes four data series: Exposure (blue bars), True (purple line with dots), Lasso credibility (green line with dots), and Complement (dark green line with dots). The x-axis is labeled 'Decile' from 1 to 10. The Lasso credibility model shows a steady increase in normalized predictions across deciles, while the Complement model shows a sharp increase in the final deciles.](a02c9887f2bdb2fc97a46aea5c241d96_img.jpg)

| Decile | Exposure (k) | True Normalized Prediction | Lasso Normalized Prediction | Complement Normalized Prediction |
|--------|--------------|----------------------------|-----------------------------|----------------------------------|
| 1      | 15k          | 1.0                        | 0.92                        | 0.74                             |
| 2      | 15k          | 1.0                        | 0.96                        | 0.84                             |
| 3      | 15k          | 1.0                        | 0.97                        | 0.92                             |
| 4      | 15k          | 1.0                        | 1.00                        | 0.96                             |
| 5      | 15k          | 1.0                        | 1.00                        | 1.00                             |
| 6      | 15k          | 1.0                        | 1.00                        | 1.00                             |
| 7      | 15k          | 1.0                        | 1.02                        | 1.02                             |
| 8      | 15k          | 1.0                        | 1.04                        | 1.06                             |
| 9      | 15k          | 1.0                        | 1.04                        | 1.12                             |
| 10     | 15k          | 1.0                        | 1.07                        | 1.30                             |

Figure 7.27: A dual-axis chart showing Normalized predictions (left axis, 0.7 to 1.4) and Exposure (right axis, 0 to 40k) across deciles. The chart includes four data series: Exposure (blue bars), True (purple line with dots), Lasso credibility (green line with dots), and Complement (dark green line with dots). The x-axis is labeled 'Decile' from 1 to 10. The Lasso credibility model shows a steady increase in normalized predictions across deciles, while the Complement model shows a sharp increase in the final deciles.

### 7.6.3. Medium State Conclusion

Our medium state data set is right on the edge of being able to produce a reasonable GLM, but lasso credibility models can still be built quickly. We can build better models on smaller data sets because **lasso credibility can incorporate prior assumptions and assign partial credibility to coefficients as opposed to assigning full credibility to all significant coefficients.**

## 7.7. “Small States” — Lasso Credibility Versus GLM

As a reminder, our first small-state subset has some different true relativities than the countrywide model, while our second small-state subset has true relativities that are identical to the countrywide model for all characteristics.

### 7.7.1. Lasso Credibility is Viable When GLM Fails

On this size of data, the GLM produces significant coefficients for only nine of the 19 variables included in the model, and a modeling project would likely be abandoned quickly. The lasso credibility model is not perfect—but it manages to build a model that is better than our selected complement of credibility at identifying the true risk relativities overall (Figure 7.28). Rather than adopting the countrywide model directly, an actuary can use lasso credibility to quickly build state-specific models on small data where a GLM is not viable (Figure 7.29).

We can also judgmentally select a higher penalty term to move less toward indicated. Selecting a higher penalty term still produces better relativities than our complement of credibility and will result in smaller policyholder impacts (Figure 7.30). This model still performs better than the countrywide complement.

**Figure 7.28. The Lasso Credibility Model Outperforms a GLM on This Small Subset of Data**

![Figure 7.28: A dual-axis chart comparing Lasso Credibility and GLM models against True Relativities across 10 deciles. The left y-axis shows Normalized predictions (0.75 to 1.2), and the right y-axis shows Exposure (0 to 12k). The x-axis represents Decile (1 to 10). The 'True' line is a flat purple line at 1.0. The 'Lasso credibility' line is a green line that starts at 0.9 and rises to 1.05. The 'GLM' line is a dark green line that starts at 0.8 and rises sharply to 1.15. The 'Exposure' is shown as light blue bars at the top of the chart, increasing from 4k to 8k across deciles.](fdae4b1c1863349bc913d92f62cc2eee_img.jpg)

| Decile | True (Normalized) | Lasso credibility (Normalized) | GLM (Normalized) | Exposure (k) |
|--------|-------------------|--------------------------------|------------------|--------------|
| 1      | 1.00              | 0.90                           | 0.80             | 4.0          |
| 2      | 1.00              | 0.98                           | 0.92             | 5.0          |
| 3      | 1.00              | 0.99                           | 0.94             | 6.0          |
| 4      | 1.00              | 1.00                           | 0.96             | 7.0          |
| 5      | 1.00              | 1.00                           | 0.98             | 8.0          |
| 6      | 1.00              | 1.00                           | 1.00             | 9.0          |
| 7      | 1.00              | 1.01                           | 1.02             | 10.0         |
| 8      | 1.00              | 1.02                           | 1.04             | 11.0         |
| 9      | 1.00              | 1.03                           | 1.08             | 12.0         |
| 10     | 1.00              | 1.05                           | 1.15             | 12.0         |

Figure 7.28: A dual-axis chart comparing Lasso Credibility and GLM models against True Relativities across 10 deciles. The left y-axis shows Normalized predictions (0.75 to 1.2), and the right y-axis shows Exposure (0 to 12k). The x-axis represents Decile (1 to 10). The 'True' line is a flat purple line at 1.0. The 'Lasso credibility' line is a green line that starts at 0.9 and rises to 1.05. The 'GLM' line is a dark green line that starts at 0.8 and rises sharply to 1.15. The 'Exposure' is shown as light blue bars at the top of the chart, increasing from 4k to 8k across deciles.

**Figure 7.29. The Lasso Credibility Model Outperforms the Countrywide Complement of Credibility on This Small Subset of Data**

![Figure 7.29: A dual-axis chart showing normalized predictions and exposure across 10 deciles. The Lasso credibility model (green line) shows a significant improvement in prediction accuracy for higher deciles compared to the complement model (dark green line).](7171c98a283e7be269152129ea8e9173_img.jpg)

Figure 7.29 is a dual-axis chart comparing the performance of the Lasso Credibility Model against the Countrywide Complement of Credibility. The x-axis represents the Decile (1 to 10). The left y-axis represents Normalized predictions (0.75 to 1.2), and the right y-axis represents Exposure (0 to 12k). The chart includes four data series: Exposure (blue bars), True (purple line), Lasso credibility (green line), and Complement (dark green line). The Lasso credibility model shows a significant improvement in prediction accuracy for higher deciles compared to the complement model.

| Decile | Exposure (k) | True (Normalized) | Lasso credibility (Normalized) | Complement (Normalized) |
|--------|--------------|-------------------|--------------------------------|-------------------------|
| 1      | 8.0          | 1.00              | 1.05                           | 0.80                    |
| 2      | 7.5          | 1.00              | 1.01                           | 0.91                    |
| 3      | 7.0          | 1.00              | 1.00                           | 0.93                    |
| 4      | 6.5          | 1.00              | 0.98                           | 0.95                    |
| 5      | 6.0          | 1.00              | 0.97                           | 0.99                    |
| 6      | 6.0          | 1.00              | 1.00                           | 1.07                    |
| 7      | 6.0          | 1.00              | 1.04                           | 1.15                    |
| 8      | 6.0          | 1.00              | 1.03                           | 1.18                    |
| 9      | 6.0          | 1.00              | 1.00                           | 1.19                    |
| 10     | 6.0          | 1.00              | 0.90                           | 1.15                    |

Figure 7.29: A dual-axis chart showing normalized predictions and exposure across 10 deciles. The Lasso credibility model (green line) shows a significant improvement in prediction accuracy for higher deciles compared to the complement model (dark green line).

**Figure 7.30. An Increased Penalty Creates a More Accurate Model by Preventing Overreactions in the Tails of This Lift Chart**

![Figure 7.30: A dual-axis chart showing normalized predictions and exposure across 10 deciles. The Lasso credibility model (green line) shows a more stable prediction accuracy across all deciles compared to the complement model (dark green line).](9d18af84f9d0bd3cb990f22f91fcf938_img.jpg)

Figure 7.30 is a dual-axis chart comparing the performance of the Lasso Credibility Model against the Countrywide Complement of Credibility. The x-axis represents the Decile (1 to 10). The left y-axis represents Normalized predictions (0.75 to 1.2), and the right y-axis represents Exposure (0 to 12k). The chart includes four data series: Exposure (blue bars), True (purple line), Lasso credibility (green line), and Complement (dark green line). The Lasso credibility model shows a more stable prediction accuracy across all deciles compared to the complement model.

| Decile | Exposure (k) | True (Normalized) | Lasso credibility (Normalized) | Complement (Normalized) |
|--------|--------------|-------------------|--------------------------------|-------------------------|
| 1      | 8.0          | 1.00              | 1.02                           | 0.80                    |
| 2      | 7.5          | 1.00              | 1.00                           | 0.91                    |
| 3      | 7.0          | 1.00              | 0.99                           | 0.93                    |
| 4      | 6.5          | 1.00              | 0.98                           | 0.95                    |
| 5      | 6.0          | 1.00              | 0.96                           | 0.97                    |
| 6      | 6.0          | 1.00              | 1.02                           | 1.08                    |
| 7      | 6.0          | 1.00              | 1.04                           | 1.15                    |
| 8      | 6.0          | 1.00              | 1.04                           | 1.18                    |
| 9      | 6.0          | 1.00              | 1.02                           | 1.20                    |
| 10     | 6.0          | 1.00              | 0.93                           | 1.16                    |

Figure 7.30: A dual-axis chart showing normalized predictions and exposure across 10 deciles. The Lasso credibility model (green line) shows a more stable prediction accuracy across all deciles compared to the complement model (dark green line).

### 7.7.2. A Good Complement Creates a Sparse Model

When we build a lasso credibility model on our second small data set (data with the same true risk relativities as our base data), the lambda indicated by cross-validation penalizes every single variable out of the model. Examining the relativity plots, we see that the complement of credibility is quite close to the true relativities for all variables. Without knowing the true relativities, an actuary would conclude that the data shows no credible differences from the complement.

This result is only possible by examining credibility instead of significance. **Rather than a process of evaluating  $p$ -values for significant differentiation from a null level, we are instead looking for credible deviations from a prior assumption.** When our complement is good, we can expect a model to output very few nonzero coefficients.

### 7.7.3. Small-State Conclusion

Lasso credibility models can be used to gain insights into data sets of increasingly small size. How can actuaries use this characteristic to apply lasso credibility in additional analysis?

For this, we turn to Actuarial Standard of Practice No. 56, *Modeling*. ASOP 56 provides significant guidance on the general usage of models, and we focus on one phrase that comes up repeatedly: the “intended purpose” of an analysis. In every aspect of modeling, an actuary should keep in mind the intended purpose and end usage of an analysis. Rather than for the intended purpose of “fully justifying new rates,” an actuary can use lasso credibility for “identifying credible differences for further investigation.” When using lasso credibility for analysis, its scope greatly increases beyond that of traditional GLM building.

Before an insurer has enough data to build a model for implementation, the actuary can use lasso credibility to identify the most credible deviations from that insurer’s current rating plan. This multivariate analysis can save an insurer time when looking for profitability issues by quickly narrowing the scope of further analysis. An ordinal treatment of continuous variables is required in this approach, as the time required to identify the correct continuous variable transformations would likely make the analysis prohibitively long.

An actuary could also perform model monitoring by fitting a lasso credibility model on only the latest year of data. Whereas such a model would almost certainly not be appropriate for implementation, it would identify experience that is credibly out of pattern with the implemented relativities for further investigation.

## 7.8. Case Study Conclusion

We have shown how lasso credibility can outperform GLM and be used to build credible models where traditional GLM or penalized regression approaches would fail. This countrywide-to-state refit is expected to be one of the main use cases of lasso credibility, but we anticipate that actuaries will use the guidance of ASOP 56 to find many additional use cases for lasso credibility.

The key to lasso credibility is the switch from **significance** to **credibility**. This switch is only achievable through penalized regression and a proper modeling setup. In our example, we used known variable transformations as a shortcut for proper model setup. In practice, an ordinal treatment of variables is necessary to create a stepwise application of credibility. Without prior knowledge of feature behavior, the penalization will remove the less credible ordinal steps and leave only the most credible deviations. It is this ordinal treatment of variables that allows us to remove this simplifying assumption and apply lasso credibility on any data set.

We encourage the reader to rerun the provided code with alterations to explore various scenarios to solidify their understanding and test the limits of the application of lasso credibility. Examples include these:

- Start with a better complement of credibility.
- Start with a worse complement of credibility.
- Experiment across multiple starting seeds.
- Experiment with alternate variable transformations.
- Apply an ordinal treatment to continuous variables and/or vehicle weight.
- Perform “model update” scenarios by resimulating the modeling data.
- Start with more volatile or less volatile distribution assumptions.
- Incorporate “random noise” in the true pure premium distribution.
- Incorporate a variable in the true pure premium distribution that is not in the model.
- Incorporate a variable in the model that is not in the true pure premium distribution.

