---
paper: mahler
chapter: 10
title: 10. THE CRITERIA APPLIED TO THE MORE GENERAL SOLUTIONS
topics: [exponential_smoothing, geometrically_decreasing_weights, meyers_dorweiler_criterion, varying_credibility_weights, optimal_credibility]
key_formulas: []
---

> **TL;DR**
> - Exponential smoothing with ~55% credibility on the latest year performs similarly to the simple single-year approach.
> - Meyers/Dorweiler criterion prefers very small credibility (~5–10%) for exponential smoothing, implying a long effective history with slow decay.
> - Using general varying weights (not equal) reduces MSE further than the equal-weight approach.
> - Most recent year consistently receives ~56% credibility in the optimal general solution.

## 10. THE CRITERIA APPLIED TO THE MORE GENERAL SOLUTIONS

In this section the three criteria in Section 7 will be applied to the more general solutions to the problem given in Section 9. For simplicity, the results will be shown for the situation where there is no delay in obtaining the data for use in making the next estimate. In Section 8.6, an example was given of the results of such a delay in receiving data. The same general pattern would apply here.

## 10.1 *Geometrically Decreasing Weights*

In Section 9.1, weight  $Z$  is applied to the latest available year of data, while weight  $1 - Z$  is applied to the previous estimate.

---

<sup>32</sup> Double exponential smoothing, sometimes called linear exponential smoothing, would be equivalent to a weighted linear least squares regression, with geometrically decreasing weights as the data got less recent.

Table 12 gives the mean squared errors for various values of  $Z$ . The optimal values of  $Z$ , using criterion #1 (least squares), are all close to 55%.<sup>33</sup> This results in weights to the various years of data very similar to those in the example in Section 9.1.

TABLE 12

MEAN SQUARED ERRORS\* (.0001) THAT RESULT FROM  
APPLYING  $Z$  TO LATEST YEAR OF DATA  
AND  $1 - Z$  TO PREVIOUS ESTIMATE

| <u>Z</u> | <u>NL</u> | <u>NLR**</u> | <u>AL</u> | <u>ALR**</u> |
|----------|-----------|--------------|-----------|--------------|
| 0        | 79        | 97           | 95        | 96           |
| .1       | 61        | 70           | 72        | 78           |
| .2       | 56        | 63           | 65        | 71           |
| .3       | 52        | 60           | 60        | 67           |
| .4       | 50        | 57           | 57        | 64           |
| .5       | 49        | 56           | 55        | 63           |
| .6       | 50        | 56           | 55        | 63           |
| .7       | 50        | 57           | 55        | 64           |
| .8       | 52        | 58           | 56        | 66           |
| .9       | 54        | 59           | 58        | 69           |
| 1.0      | 57        | 62           | 61        | 73           |

\* First 10 years are not included in the computation of the squared errors in order to eliminate the calibration period.

\*\* Data reversed in time.

In this case there is no significant reduction in squared error beyond what was previously obtained by applying credibility to the latest available year.<sup>34</sup>

Table 13 displays the results of applying criterion #2, limited fluctuation. Values of the credibility between 40% and 80% generally perform well.

<sup>33</sup> For the NL data set the optimal credibility is 53%. For the NLR data set, it is 58%. For the AL data set it is 60%. For the ALR data set it is 54%.

<sup>34</sup> Compare the results in Table 6 for  $N = 1$  with those in Table 12.

Table 14 displays the results of applying criterion #3, Meyers/Dorweiler.<sup>35</sup> Unlike the previous two cases, the optimal credibilities are close to zero; 5% to 10% credibility produces correlations close to zero. The use of such small credibilities is approximately the same as using 10 to 20 years of data as the basis for the estimate, since the geometrically decreasing weights decline only slowly.

TABLE 13

PERCENT OF TIME\* THAT THE ESTIMATE IS IN ERROR BY  
MORE THAN 20%  
APPLYING  $Z$  TO LATEST YEAR OF DATA  
AND  $1 - Z$  TO PREVIOUS ESTIMATE

| <u>Z</u> | <u>NL</u> | <u>NLR**</u> | <u>AL</u> | <u>ALR**</u> |
|----------|-----------|--------------|-----------|--------------|
| 0        | 25        | 31           | 33        | 31           |
| .1       | 23        | 23           | 25        | 26           |
| .2       | 21        | 22           | 24        | 25           |
| .3       | 18        | 21           | 21        | 23           |
| .4       | 16        | 21           | 20        | 21           |
| .5       | 16        | 20           | 19        | 22           |
| .6       | 16        | 20           | 19        | 21           |
| .7       | 17        | 19           | 20        | 22           |
| .8       | 18        | 19           | 19        | 22           |
| .9       | 18        | 20           | 18        | 23           |
| 1.0      | 19        | 21           | 19        | 26           |

\* First 10 years are not included in the computation in order to eliminate the calibration period.

\*\* Data reversed in time.

---

<sup>35</sup> In this case, the results of the first 20 years were excluded from the computation, in order to eliminate the calibration period. Twenty years were used, rather than ten years as in the previous two tables, since in this case smaller credibilities are optimal and smaller credibilities require a longer calibration period.

TABLE 14

CORRELATIONS\* (KENDALL TAU) THAT RESULT FROM  
 APPLYING  $Z$  TO LATEST YEAR OF DATA  
 AND  $1 - Z$  TO PREVIOUS ESTIMATE

| <u>Z</u> | <u>NL</u> | <u>NLR**</u> | <u>AL</u> | <u>ALR**</u> |
|----------|-----------|--------------|-----------|--------------|
| 0***     | .11       | .16          | .28       | .14          |
| .1       | -.03      | .01          | .00       | -.09         |
| .2       | -.05      | -.05         | -.04      | -.10         |
| .3       | -.08      | -.09         | -.07      | -.12         |
| .4       | -.10      | -.12         | -.10      | -.13         |
| .5       | -.13      | -.15         | -.12      | -.15         |
| .6       | -.15      | -.18         | -.14      | -.17         |
| .7       | -.18      | -.20         | -.16      | -.20         |
| .8       | -.20      | -.23         | -.18      | -.22         |
| .9       | -.23      | -.25         | -.21      | -.24         |
| 1.0      | -.26      | -.27         | -.23      | -.28         |

\* First 20 years are not included in the computation of the correlations in order to eliminate the calibration period.

\*\* Data reversed in time.

\*\*\* Limit as  $Z$  approaches zero.

### 10.2 More General Varying Weights

In Section 9.2, varying weights  $Z_i$  are applied to the most recent  $N$  years, while the remaining weight is given to the grand mean. This method will only be examined using criterion #1, least squares. One can solve numerically for the set of weights which produce the least squared error, using a given number of years of data.<sup>36</sup> The results are as follows:

<sup>36</sup> Unfortunately, as the number of years increases, the amount of computer time required also increases.

### Using Most Recent Two Years of Data ( $N = 2, \Delta = 1$ )

|    | Credibility             |                  | Mean Squared Error (.0001) |
|----|-------------------------|------------------|----------------------------|
|    | Second Most Recent Year | Most Recent Year |                            |
| NL | 9.6%                    | 61.1%            | 48                         |
| AL | 13.1%                   | 56.9%            | 54                         |

### Using Most Recent Three Years of Data ( $N = 3, \Delta = 1$ )

|    | Credibility            |                         |                  | Mean Squared Error (.0001) |
|----|------------------------|-------------------------|------------------|----------------------------|
|    | Third Most Recent Year | Second Most Recent Year | Most Recent Year |                            |
| NL | 16.4%                  | 1.1%                    | 59.0%            | 45                         |
| AL | 8.1%                   | 9.1%                    | 55.7%            | 53                         |

Most of the credibility is assigned to the most recent year. The complement of credibility, which is assigned to the grand mean, is about 25 to 35 percent, decreasing as  $N$  increases.

### Complement of Credibility

|    | $N = 1^*$ | $N = 2$ | $N = 3$ |
|----|-----------|---------|---------|
| NL | 32%       | 29%     | 24%     |
| AL | 35%       | 30%     | 27%     |

\* One minus the optimal credibility from Table 9.

The mean squared error is reduced from that using only the latest year of data.<sup>37</sup>

<sup>37</sup> Since the use of fewer years of data is just a special case, the least squared error using more years of data must be less than or equal that using fewer years of data.

| Mean Squared Error (.0001) |                             |                           |                           |
|----------------------------|-----------------------------|---------------------------|---------------------------|
|                            | <u><math>N = 1^*</math></u> | <u><math>N = 2</math></u> | <u><math>N = 3</math></u> |
| NL                         | 49                          | 48                        | 45                        |
| AL                         | 56                          | 54                        | 53                        |

\* From Table 6.

