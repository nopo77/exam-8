---
paper: mahler
chapter: 9
title: 9. MORE GENERAL SOLUTIONS
topics: [exponential_smoothing, geometrically_decreasing_weights, varying_credibility_weights]
key_formulas: [exponential_smoothing_weights, general_weighted_average]
---

> **TL;DR**
> - Method 5: give latest year weight Z and prior estimate weight (1−Z); yields geometrically decreasing weights on all past years (exponential smoothing).
> - General form F = ΣZ_i·X_i + (1−ΣZ_i)·M allows different weights to each year.
> - Exponential smoothing is equivalent to horizontal weighted least-squares regression with geometrically declining weights once calibrated.
> - Optimal weight vectors are hard to determine empirically as N grows; many near-optimal solutions exist.

## 9. MORE GENERAL SOLUTIONS

In Section 6, four relatively simple forms of a solution were given. In this section, more general forms of a solution will be given.

## 9.1 Combine Previous Estimate and Most Recent Data

In the fifth method, one gives the latest year of *data* weight  $Z$ , and gives the previous *estimate* weight  $1 - Z$ . Of course, one has to choose an initial estimate.<sup>29</sup> In this case, for each risk the initial estimate will be taken as the grand mean of 50%.<sup>30</sup> Once this estimation method has been used for several years, the initial estimate has very little weight.

For example, let us assume  $Z = 60\%$ . Then the weights assigned to the given years of data used in estimating the result for the year 1911 would be as follows:

| <u>Year of Data</u> | <u>Weight in Estimate of 1911</u>                   |
|---------------------|-----------------------------------------------------|
| 1910                | $Z = 60\%$                                          |
| 1909                | $Z(1 - Z) = 40\% \times 60\% = 24\%$                |
| 1908                | $Z(1 - Z)^2 = 40\% \times 40\% \times 60\% = 9.6\%$ |
| 1907                | $Z(1 - Z)^3 = 9.6\% \times 40\% = 3.84\%$           |
| 1906                | $Z(1 - Z)^4 = 3.84\% \times 40\% = 1.54\%$          |
| 1905                | $Z(1 - Z)^5 = 1.54\% \times 40\% = .61\%$           |
| 1904 and Prior      | $(1 - Z)^6 = .41\%$                                 |

The above assumes that the latest year of data is always given 60% weight, while the current estimate is given 40% weight.

Thus in this case, one gets a geometrically decreasing weight. This procedure is called (single) exponential smoothing [10]. It is an example of what mathematicians call a "filter."<sup>31</sup> Once the process of exponential

<sup>29</sup> This is precisely analogous to choosing a "seed" value in exponential smoothing.

<sup>30</sup> One could use subjective judgement to choose the initial estimate for each risk. Also one could use data from the period prior to that displayed in this paper; this has been avoided for the sake of simplicity.

<sup>31</sup> Morrison [11] gives this as an example of a "fading-memory polynomial filter."

smoothing gets “up to speed,” it is equivalent to a weighted least squares regression, where the fitted line is horizontal,<sup>32</sup> and where the weights are geometrically decreasing as the data get less recent.

## 9.2 *More General Varying Weights*

In Section 9.1, one gave geometrically decreasing weight to years of data further in the past. More generally one can make the estimate:

$$F = \sum Z_i X_i + (1 - \sum Z_i)M$$

where the weights  $Z_i$  depend on how far in the past are the data  $X_i$ . For years for which data are not available (presumably because they are too far in the past) one uses the grand mean  $M$  instead of the data. This method is a generalization of the methods in Sections 6 and 9.1.

Unfortunately, calculating or empirically determining the optimal values of the weights  $Z_i$  becomes difficult as more years of data are used. Also, there are many vectors of  $Z_i$  that are very close to optimal; i.e., the  $n$ -dimensional volume of values  $Z_1, \dots, Z_n$  that produce close to optimal results is relatively large.

