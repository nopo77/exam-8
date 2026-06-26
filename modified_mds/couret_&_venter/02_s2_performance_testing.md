---
paper: couret_&_venter
chapter: 2
title: "2. PERFORMANCE TESTING"
topics: [quintiles_test, sum_of_squared_prediction_errors, credibility_validation, hazard_groups, regression_toward_the_mean, workers_compensation_classification]
key_formulas: []
---

> **TL;DR**
> - Validation uses an even/odd holdout: credibility weights estimated from even-year data, tested on odd years; a modest improvement in sum of squared prediction errors for individual classes is expected because the estimator minimizes within-period error but is tested across different periods
> - The quintiles test (adapted from NCCI) groups classes by credibility-predicted relativity into five quintiles and checks if those predictions track hold-out-year relativities — credibility SSE of 0.0105 vs. 0.5618 (HG average) and 0.7315 (raw class data)
> - Raw class data overfits (slope too steep): odd-year data regresses toward the mean; credibility shrinks estimates appropriately toward the hazard-group average
> - Quintile-level "R²" of ~98% for class relativities shows the procedure captures most between-class heterogeneity
> - Hazard group A is homogeneous; credibility does not improve (and can worsen) estimation there

## 2. PERFORMANCE TESTING

We had seven years of class data, at various levels of maturity, for the estimation, but for testing we discarded the quite immature first report. As a test, we calculated injury-type relativities from the even reports (2, 4, and 6) and used these to predict the hold out sample of odd reports (3, 5, and 7). Holding out the last two years and predicting by the older years gave comparable results. For testing credibility itself, the current approach seems to make more sense, as it is more neutral with respect to trend and loss development. Table A summarizes the sum of squared prediction errors by hazard group for the ratio of major permanent partial to temporary total claims. The squared errors are calculated for each combination of state and class – about 16,000 observations overall. Table B lists totals for all injury types.

TABLE A  
SUM OF SQUARED PREDICTION ERRORS – MAJOR PERMANENT PARTIAL CLAIMS

| (1)<br>Hazard<br>Group | (2)<br>Prediction<br>Based on HG | (3)<br>Prediction<br>Based on Raw Even | (4)<br>Prediction<br>Based on Cred. Proc. |
|------------------------|----------------------------------|----------------------------------------|-------------------------------------------|
| A                      | 33.4                             | 52.9                                   | 33.0                                      |
| B                      | 206.9                            | 363.2                                  | 205.1                                     |
| C                      | 250.8                            | 479.3                                  | 248.0                                     |
| D                      | 89.9                             | 129.9                                  | 89.3                                      |
| E                      | 333.2                            | 484.0                                  | 330.8                                     |
| F                      | 247.1                            | 306.3                                  | 242.6                                     |
| G                      | 263.7                            | 386.2                                  | 256.9                                     |
| Total                  | 1,425.0                          | 2,201.7                                | 1,405.6                                   |

TABLE B  
SUM OF SQUARED PREDICTION ERRORS BY INJURY TYPE

| (1)<br>Injury<br>Type | (2)<br>Prediction<br>Based on HG | (3)<br>Prediction<br>Based on Raw Even | (4)<br>Prediction<br>Based on Cred. Proc. |
|-----------------------|----------------------------------|----------------------------------------|-------------------------------------------|
| Fatal                 | 43.6                             | 65.2                                   | 43.5                                      |
| PT                    | 34.7                             | 83.6                                   | 34.6                                      |
| Major PP              | 1,425.0                          | 2,201.7                                | 1,405.6                                   |
| Minor PP              | 6,756.9                          | 10,360.3                               | 6,558.0                                   |
| Med. Only             | 417,260.8                        | 434,837.9                              | 351,270.8                                 |

The credibility procedure yields a modest reduction in the sum of squared prediction errors. The credibility procedure is designed to minimize the expected deviation between the true class mean and its sample estimator *over the same time period* (the even years). In performance testing, however, a three-year holdout sample of odd years is used as a proxy for the even year’s true mean. That is, the estimator derived from even-year data is compared to the ratio for the holdout sample from odd years. Thus, there is some disconnect between the expectation being minimized and the statistic being used to gauge performance.

Relative incidence ratios are impacted by unknown covariates – with levels varying between odd and even years, indeed over all years. Such unknown effects contribute to the error of the predictions. A class code represents the experience of a dynamic portfolio of individual insurance policies whose composition varies over time. In addition, the individual class-state ratios are quite

volatile. Improving the estimates of the means might produce only a small improvement in the total sum of squared errors.

Interestingly, researchers trying to test the Capital Asset Pricing Model (CAPM) faced a similar measurement problem. Under CAPM, individual excess stock returns are hypothetically proportional to beta. The Security Market Line (SML) is a graphical representation of this relationship. Early tests of CAPM which focused on empirical validation of the SML ran into statistical problems. Bodie, Kane and Marcus (BKM) write:

*“The next wave of tests was designed to overcome the measurement error problem that led to biased estimates of the SML. The innovation in these tests, pioneered by Black, Jensen, and Scholes (BJS), was to use portfolios rather than individual securities. Combining into portfolios diversifies away most of the firm-specific part of the returns, thereby enhancing the precision of estimates of beta and the expected rate of return of the portfolio of securities. This mitigates the statistical problems that arise from measurement error in the beta estimates.”*

Instead of assigning stocks to portfolios randomly, BJS sort by descending beta and then group by quantile. BKM, in their heuristic explanation of BJS, write:

*“.. we need to construct portfolios with the largest possible dispersion of beta coefficients. Other things being equal, a sample yields more accurate regression estimates the more widely spaced are the observations of the independent variables.”*

*“Rather than allocate 20 stocks to each portfolio randomly, we can rank portfolios by betas. Portfolio 1 will include the 20 highest-beta stocks and Portfolio 5 the 20 lowest beta stocks. In that case a set of portfolios with small nonsystematic components,  $e_p$ , and widely spaced betas will yield reasonably powerful tests of the SML.”*

CAPM is a theory about the relationship between beta and *expected* excess return. Even an average of returns for an individual stock is volatile. Additionally, there are systematic effects that vary over time, which means that a firm's beta is not constant over time. The BJM approach of using portfolios diversifies away the systematic, firm specific part of variation in returns.

In our case, performance testing based on a sum of squared errors criteria only produces a slight improvement; however, testing based on *ranked portfolios* of state-class combinations demonstrates a significant improvement. Our approach is based on the “quintiles test”, a technique developed by NCCI for testing their experience rating plan.

Dorweiler wrote in 1934:

*“A necessary condition for proper credibility is that the credit risks and debit risks equally reproduce the permissible loss ratio. Also, if the proper credibility has been attained, each [random] subgroup of the credit and debit risks, provided it has adequate volume, should give the permissible loss ratio.”*

Gillam (1992) explains that the “quintiles test” is a logical extension of Dorweiler's criteria. (Dorweiler's groups were defined by modification range, but varied by size.) In our analysis, class relativities to the hazard group average are analogous to the experience rating modifications of interest to Gillam.

TABLE C  
ILLUSTRATION OF QUINTILES TEST – HAZARD GROUP D, PERMANENT TOTAL CLAIMS

| (1)<br>Quintile | (2)<br>Odd<br>Relativity | (3)<br>Prediction<br>Based on<br>HG | (4)<br>Prediction<br>Based on<br>Raw Even | (5)<br>Prediction<br>Based on<br>Cred. Procedure |
|-----------------|--------------------------|-------------------------------------|-------------------------------------------|--------------------------------------------------|
| 1               | 0.4951                   | 1.0000                              | 0.3065                                    | 0.5648                                           |
| 2               | 0.8634                   | 1.0000                              | 0.4260                                    | 0.8732                                           |
| 3               | 0.9861                   | 1.0000                              | 0.7513                                    | 1.0000                                           |
| 4               | 1.1269                   | 1.0000                              | 1.3473                                    | 1.1038                                           |
| 5               | 1.5215                   | 1.0000                              | 2.1547                                    | 1.4519                                           |
| Mean            | 1.0000                   | 1.0000                              | 1.0000                                    | 1.0000                                           |
| SSE             |                          | 0.5618                              | 0.7315                                    | 0.0105                                           |

We illustrate the procedure using  $W$  relativities for classes in the fairly large hazard group D, but the procedure for the other injury types is the same. This is illustrated in Table C.

For the quintiles test, the classes within hazard group D were first grouped by credibility weighted relativity from the even years’ data into five groups of roughly equal size. (The boundaries were selected to make the number of TT claims in each quintile about equal.) The lowest 20% of the credibility weighted class relativities belong to the risks in the first quintile; the next 20% to the second; and so on. Column (2) represents the average relative frequency  $W$  for the classes in the quintile *divided by* the corresponding estimate for all of hazard group D. For example, the relative frequency of PT claims (as a ratio to TT) for the classes in the first quintile is about half of the hazard group average; the fifth quintile average exceeds the hazard group average by 52%. Upwardly sloping relativities are desirable, indicating that the credibility procedure used to determine quintiles tends, on average, to identify class differences in  $W$ .

The goal is to predict the column (2) frequency relativity for each quintile. Column (3) is a prediction based on the hazard group average. All its entries are equal to unity – since by assumption every quintile has the hazard group D relative frequency for PT. The predictions in Column 4 are based on raw class relativities observed for the even years. The aggregation of the classes in the fifth quintile, for example, has an *even year* relative PT frequency that is 215% of the hazard group average. Column (5) predictions were derived using the multi-dimensional credibility procedure described in this paper.

The exhibit is based on five groups with about 1400 PT claims in the even years. As expected, the ratios in column (2) increase across the quintiles; classes for which credibility predicts high relativities using even year data tend to generate high relativities during the odd years. The predictions in column (3), are too high for the first three quintiles and too low for the last two; the sum of

squared prediction errors based on column (3) predictions is 0.5618. Similarly, the sum of squared prediction errors based on column (4) predictions is 0.7315. The upward slope in column (4) is too steep; the odd years exhibit regression toward the mean. The credibility procedure predictions in column (5), have a sum of squared prediction errors of 0.0105. To the extent the class relativity procedure performs, the ratios in column (5) will track those in column (2); producing a lower sum of squared deviations.

As indicated by the sum of squared prediction errors in Table D, the results are similar for most other combinations of injury type and hazard group, the exception being hazard group A for all three injury types. The quintiles test suggests that hazard group A is homogeneous and the credibility procedure is not improving the estimation there, although the sum of individual squared errors is slightly better for the credibility estimates. For major the raw class data provides surprisingly good estimates for the quintiles as a whole once these have been defined by the credibility procedure. These estimates are quite good

TABLE D  
QUINTILES TEST SUM OF SQUARED PREDICTION ERRORS BY HAZARD GROUP AND INJURY TYPE

| HG | Injury Type | Prediction Based on HG | Prediction Based on Raw Even | Prediction Based on Cred. Proc. |
|----|-------------|------------------------|------------------------------|---------------------------------|
| A  | Fatal       | 0.13227                | 0.94431                      | 0.18952                         |
| B  | Fatal       | 0.32630                | 1.79940                      | 0.05637                         |
| C  | Fatal       | 0.83604                | 1.39413                      | 0.03376                         |
| D  | Fatal       | 0.97498                | 0.87260                      | 0.12111                         |
| E  | Fatal       | 0.49691                | 1.44023                      | 0.05096                         |
| F  | Fatal       | 0.39060                | 1.35362                      | 0.07280                         |
| G  | Fatal       | 0.55650                | 1.23015                      | 0.06035                         |
| A  | PT          | 0.03941                | 1.94151                      | 0.57993                         |
| B  | PT          | 0.38273                | 1.34145                      | 0.11044                         |
| C  | PT          | 0.56175                | 0.55609                      | 0.01180                         |
| D  | PT          | 0.56183                | 0.73151                      | 0.01053                         |
| E  | PT          | 0.73195                | 0.82350                      | 0.07050                         |
| F  | PT          | 0.56872                | 0.53817                      | 0.01812                         |
| G  | PT          | 1.09139                | 0.52326                      | 0.07946                         |
| A  | Major       | 0.58481                | 0.01988                      | 0.05079                         |
| B  | Major       | 0.33888                | 0.03729                      | 0.00870                         |
| C  | Major       | 0.38001                | 0.04108                      | 0.00738                         |
| D  | Major       | 0.18900                | 0.03928                      | 0.01850                         |
| E  | Major       | 0.28775                | 0.07476                      | 0.01030                         |
| F  | Major       | 0.32418                | 0.04703                      | 0.01781                         |
| G  | Major       | 0.58518                | 0.14046                      | 0.00538                         |

![Figure 1: Distribution of Predicted PT:TT Ratios by Hazard Group. The figure consists of seven horizontal histograms, one for each hazard group (A through G). The x-axis is labeled 'PT:TT Ratio' and ranges from 0.000 to 0.059. The y-axis is labeled 'Percent' and ranges from 0 to 80. Each histogram shows the distribution of predicted PT:TT ratios for that hazard group. To the right of each histogram, a box contains the 10th Percentile, Median, and 90th Percentile values.](f176174c2978785e86a8352bd45e322e_img.jpg)

| Hazard Group | 10th Percentile | Median | 90th Percentile |
|--------------|-----------------|--------|-----------------|
| A            | .0027           | .0027  | .0027           |
| B            | .0032           | .0037  | .0048           |
| C            | .0031           | .0046  | .0070           |
| D            | .0043           | .0056  | .0084           |
| E            | .0060           | .0089  | .0132           |
| F            | .0088           | .0123  | .0194           |
| G            | .0114           | .0182  | .0267           |

Figure 1: Distribution of Predicted PT:TT Ratios by Hazard Group. The figure consists of seven horizontal histograms, one for each hazard group (A through G). The x-axis is labeled 'PT:TT Ratio' and ranges from 0.000 to 0.059. The y-axis is labeled 'Percent' and ranges from 0 to 80. Each histogram shows the distribution of predicted PT:TT ratios for that hazard group. To the right of each histogram, a box contains the 10th Percentile, Median, and 90th Percentile values.

FIGURE 1: Distribution of Predicted PT:TT Ratios by Hazard Group.

![Figure 2: Distribution of Predicted Major:TT Ratios by Hazard Group. The figure consists of seven horizontal histograms, one for each hazard group (A through G). The x-axis is labeled 'Major:TT Ratio' and ranges from 0.014 to 0.558. The y-axis is labeled 'Percent' and ranges from 0 to 40. Each histogram shows the distribution of predicted Major:TT ratios for that hazard group. To the right of each histogram, a box contains the 10th Percentile, Median, and 90th Percentile values.](252ea48d02dce93965b91746fb376f35_img.jpg)

| Hazard Group | 10th Percentile | Median | 90th Percentile |
|--------------|-----------------|--------|-----------------|
| A            | .0173           | .0214  | .0293           |
| B            | .0366           | .0433  | .0602           |
| C            | .0418           | .0537  | .0716           |
| D            | .0657           | .0768  | .1000           |
| E            | .1000           | .1283  | .1607           |
| F            | .1208           | .1706  | .2069           |
| G            | .1816           | .2774  | .4091           |

Figure 2: Distribution of Predicted Major:TT Ratios by Hazard Group. The figure consists of seven horizontal histograms, one for each hazard group (A through G). The x-axis is labeled 'Major:TT Ratio' and ranges from 0.014 to 0.558. The y-axis is labeled 'Percent' and ranges from 0 to 40. Each histogram shows the distribution of predicted Major:TT ratios for that hazard group. To the right of each histogram, a box contains the 10th Percentile, Median, and 90th Percentile values.

FIGURE 2: Distribution of Predicted Major:TT Ratios by Hazard Group.

for minor as well (not shown). However Table B shows that raw class data does poorly in predicting individual class ratios for all injury types.

Thinking in  $R^2$  terms, the class relativities could be said to “explain” 98% of the “between quintiles” variance. This is not actually a regression, but the statistic is still impressive by real-life actuarial standards. The use of class relativities significantly improves the class frequency by injury type estimation.

The predicted mean ratios by class are distributed around the hazard-group ratios. In some cases these distributions are fairly tight, and in other cases fairly dispersed. Figure 1 illustrates this for PT. Figure 2 is the comparable graph for Major.

In both cases the later hazard groups have higher means and greater dispersion of classes about the mean.

