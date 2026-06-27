---
paper: mahler
chapter: 8
title: 8. THE CRITERIA APPLIED TO THE SIMPLE SOLUTIONS
topics: [least_squares_criterion, limited_fluctuation_credibility, meyers_dorweiler_criterion, optimal_credibility, data_delay_effect, squared_error_reduction]
key_formulas: [mean_squared_error_by_Z_and_N, optimal_credibility_table]
---

> **TL;DR**
> - All three criteria converge on optimal single-year credibility of roughly 65–70%.
> - Using more years with equal weight does NOT improve estimates when parameters shift — older data hurts.
> - Data delay substantially increases MSE and lowers optimal credibility (e.g., Z ≈ 68% at delay=1 drops to ~11% at delay=10).
> - Credibility reduces MSE to ~83% of the naive baseline; theoretical maximum improvement is to 75%.

# 8. THE CRITERIA APPLIED TO THE SIMPLE SOLUTIONS

In this section the three criteria in Section 7 will be applied to the simple solutions given in Section 6. More knowledgeable readers may wish to skip to Section 8.4 which compares the results of applying the three different criteria. Section 8.5 discusses the reduction in squared error. Section 8.6 examines the impact of a delay in receiving data.

## 8.1 The Two Base Cases

The two simplest solutions either always use as the estimate the overall mean ( $Z = 0$ ), or always use as the estimate the most recent observation ( $Z = 1$ ). While neither of these solutions is expected to be chosen, they serve as the base cases for testing the other solutions.

---

<sup>18</sup> Meyers in [1] used the Kendall  $\tau$  statistic. In the example here, any other reasonable measure of the correlation could be substituted.

The first criterion is the smallest mean squared error. For the two data sets the results are:

|         | Mean Squared Error |           |
|---------|--------------------|-----------|
|         | <u>NL</u>          | <u>AL</u> |
| $Z = 0$ | .0091              | .0095     |
| $Z = 1$ | .0059              | .0068     |

The second criterion is to produce a small probability of being wrong by more than  $k$  percent. For the two data sets the results are as follows:

|         | Percent<br>of time that<br>the estimate<br>is in error<br>by more than 5% |           | Percent<br>of time that<br>the estimate<br>is in error<br>by more than 10% |           | Percent<br>of time that<br>the estimate<br>is in error<br>by more than<br>20% |           |
|---------|---------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------|-----------|
|         | <u>NL</u>                                                                 | <u>AL</u> | <u>NL</u>                                                                  | <u>AL</u> | <u>NL</u>                                                                     | <u>AL</u> |
| $Z = 0$ | 82.2%                                                                     | 80.3%     | 64.8%                                                                      | 63.8%     | 29.0%                                                                         | 31.4%     |
| $Z = 1$ | 75.8%                                                                     | 72.9%     | 52.3%                                                                      | 55.7%     | 19.1%                                                                         | 22.0%     |

The third criterion is to have a correlation as close to zero as possible between the ratio of the actual to estimated and the ratio of estimated to the overall mean. For the two data sets the results are as follows:

|           | Correlation (Kendall $\tau$ ) |           |
|-----------|-------------------------------|-----------|
|           | <u>NL</u>                     | <u>AL</u> |
| $Z = 0^*$ | .48                           | .46       |
| $Z = 1$   | -.24                          | -.27      |

\* Limit as  $Z$  approaches zero.

## 8.2 *Applying Credibility to the Latest Year of Data*

The third prediction method, explained in Section 6.3, uses credibility to combine the latest year of data and the grand mean. The mean squared error depends on the credibility. As shown in Table 6, the mean squared error is a minimum for  $Z$  between 60% and 70%.<sup>19</sup> The probability of having errors of 20% or more is displayed in Table 7. Based on this second criterion, the optimal  $Z$  is between 50% and 80%.<sup>20</sup> This criterion does not distinguish very sharply between the different values of credibility.

The correlations used in the third criterion are displayed in Table 8. Based on the third criterion the optimal  $Z$  is approximately 70%.<sup>21</sup>

## 8.3 *Applying Credibility to the Latest $N$ Years of Data*

The fourth method, explained in Section 6.4, uses credibility to combine the grand mean with the latest  $N$  years of data (giving each year of data the same weight.)

The results of applying the first criterion are shown in Table 6. Based on most actuarial uses of credibility, an actuary would expect the optimal credibilities to increase as more years of data are used. In this example they do not. In fact, using more than one or two years of data does an inferior job according to this criterion.

This result is to be expected, since the parameters shift substantially over time. Thus the use of older data (with equal weight) eventually leads to a worse estimate.<sup>22</sup>

---

<sup>19</sup> For the NL data set, the minimum occurs when  $Z = 68\%$ . For the AL data set, the minimum occurs when  $Z = 66\%$ . Also, it should be noted that the squared errors for  $Z = 0$  vary somewhat with the number of years of data used, solely due to the differing periods of time over which the test can be performed.

<sup>20</sup> For the NL data set, the optimal  $Z$  is 75%. For the AL data set, the optimal  $Z$  is 55%. It should be noted that, given the limited number of observations, two values of  $Z$  can produce identical results for this criterion.

<sup>21</sup> For the NL data set, the correlation is closest to zero for  $Z = 71\%$ . For the AL data set, the correlation is closest to zero for  $Z = 66\%$ .

<sup>22</sup> The number of years of data to use to get the best estimate will depend on the particular example. This general subject was explored in Mahler [5].

TABLE 6  
MEAN SQUARED ERROR (.0001)

| Z    | NL           |              |              |              |              |              |               |               |               |               |
|------|--------------|--------------|--------------|--------------|--------------|--------------|---------------|---------------|---------------|---------------|
|      | <u>N = 1</u> | <u>N = 2</u> | <u>N = 3</u> | <u>N = 4</u> | <u>N = 5</u> | <u>N = 7</u> | <u>N = 10</u> | <u>N = 15</u> | <u>N = 20</u> | <u>N = 25</u> |
| 0    | 91           | 90           | 90           | 89           | 87           | 84           | 80            | 80            | 80            | 80            |
| .10  | 80           | 80           | 80           | 80           | 79           | 77           | 74            | 75            | 76            | 77            |
| .20  | 70           | 72           | 72           | 72           | 71           | 71           | 70            | 72            | 72            | 74            |
| .30  | 62           | 65           | 65           | 65           | 65           | 66           | 67            | 69            | 69            | 71            |
| .40  | 56           | 59           | 60           | 60           | 60           | 62           | 64            | 67            | 67            | 69            |
| .50  | 52           | 55           | 56           | 56           | 57           | 59           | 63            | 66            | 65            | 68            |
| .60  | 50           | 53           | 53           | 53           | 53           | 57           | 62            | 65            | 64            | 68            |
| .70  | 49           | 52           | 52           | 52           | 53           | 56           | 63            | 65            | 63            | 68            |
| .80  | 51           | 53           | 52           | 52           | 54           | 57           | 64            | 66            | 64            | 69            |
| .90  | 54           | 55           | 53           | 53           | 55           | 58           | 66            | 68            | 65            | 70            |
| 1.00 | 59           | 59           | 56           | 56           | 57           | 61           | 70            | 70            | 66            | 72            |
|      |              |              |              |              |              |              |               |               |               |               |
| Z    | AL           |              |              |              |              |              |               |               |               |               |
|      | <u>N = 1</u> | <u>N = 2</u> | <u>N = 3</u> | <u>N = 4</u> | <u>N = 5</u> | <u>N = 7</u> | <u>N = 10</u> | <u>N = 15</u> | <u>N = 20</u> | <u>N = 25</u> |
| 0    | 95           | 96           | 96           | 95           | 95           | 95           | 95            | 92            | 91            | 95            |
| .10  | 84           | 85           | 86           | 86           | 88           | 89           | 90            | 88            | 87            | 91            |
| .20  | 75           | 77           | 78           | 79           | 81           | 83           | 86            | 85            | 83            | 87            |
| .30  | 67           | 69           | 71           | 73           | 75           | 79           | 82            | 82            | 80            | 83            |
| .40  | 61           | 64           | 66           | 68           | 71           | 75           | 80            | 81            | 78            | 80            |
| .50  | 58           | 60           | 62           | 64           | 68           | 73           | 78            | 79            | 76            | 78            |
| .60  | 56           | 57           | 60           | 62           | 66           | 71           | 78            | 79            | 74            | 76            |
| .70  | 56           | 56           | 59           | 61           | 66           | 71           | 78            | 79            | 73            | 74            |
| .80  | 58           | 57           | 59           | 62           | 66           | 72           | 79            | 79            | 73            | 73            |
| .90  | 62           | 59           | 61           | 64           | 68           | 74           | 81            | 81            | 73            | 73            |
| 1.00 | 68           | 63           | 64           | 67           | 71           | 77           | 84            | 83            | 74            | 73            |

TABLE 7  
PERCENT OF TIME THAT THE ESTIMATE IS IN ERROR BY MORE THAN 20%

| Z    | <u>NL</u>    |              |              |              |              |              |               |               |               |               |
|------|--------------|--------------|--------------|--------------|--------------|--------------|---------------|---------------|---------------|---------------|
|      | <u>N = 1</u> | <u>N = 2</u> | <u>N = 3</u> | <u>N = 4</u> | <u>N = 5</u> | <u>N = 7</u> | <u>N = 10</u> | <u>N = 15</u> | <u>N = 20</u> | <u>N = 25</u> |
| 0    | 29           | 29           | 29           | 28           | 28           | 27           | 25            | 25            | 25            | 26            |
| .10  | 25           | 26           | 25           | 25           | 25           | 25           | 25            | 24            | 24            | 25            |
| .20  | 23           | 23           | 23           | 23           | 24           | 24           | 23            | 24            | 23            | 26            |
| .30  | 19           | 21           | 22           | 22           | 21           | 22           | 23            | 23            | 23            | 24            |
| .40  | 18           | 19           | 20           | 20           | 22           | 23           | 22            | 22            | 23            | 25            |
| .50  | 17           | 19           | 18           | 19           | 21           | 21           | 21            | 22            | 24            | 25            |
| .60  | 17           | 18           | 18           | 18           | 18           | 21           | 21            | 22            | 24            | 25            |
| .70  | 17           | 18           | 18           | 19           | 19           | 21           | 21            | 22            | 26            | 26            |
| .80  | 17           | 17           | 18           | 19           | 20           | 22           | 23            | 24            | 25            | 27            |
| .90  | 18           | 19           | 17           | 18           | 21           | 22           | 24            | 25            | 25            | 27            |
| 1.00 | 19           | 20           | 18           | 20           | 21           | 23           | 25            | 26            | 25            | 28            |

  

| Z    | <u>AL</u>    |              |              |              |              |              |               |               |               |               |
|------|--------------|--------------|--------------|--------------|--------------|--------------|---------------|---------------|---------------|---------------|
|      | <u>N = 1</u> | <u>N = 2</u> | <u>N = 3</u> | <u>N = 4</u> | <u>N = 5</u> | <u>N = 7</u> | <u>N = 10</u> | <u>N = 15</u> | <u>N = 20</u> | <u>N = 25</u> |
| 0    | 31           | 31           | 32           | 32           | 32           | 32           | 33            | 32            | 32            | 34            |
| .10  | 27           | 27           | 27           | 27           | 27           | 28           | 28            | 28            | 29            | 30            |
| .20  | 23           | 24           | 25           | 25           | 25           | 27           | 27            | 27            | 28            | 30            |
| .30  | 21           | 21           | 22           | 23           | 24           | 25           | 27            | 27            | 27            | 29            |
| .40  | 19           | 19           | 21           | 23           | 24           | 26           | 27            | 26            | 26            | 27            |
| .50  | 18           | 19           | 21           | 22           | 23           | 24           | 28            | 26            | 26            | 27            |
| .60  | 18           | 18           | 21           | 21           | 22           | 25           | 27            | 25            | 26            | 26            |
| .70  | 20           | 18           | 19           | 20           | 22           | 25           | 26            | 25            | 25            | 27            |
| .80  | 19           | 19           | 18           | 20           | 21           | 26           | 27            | 26            | 25            | 26            |
| .90  | 20           | 21           | 19           | 22           | 23           | 27           | 26            | 27            | 25            | 27            |
| 1.00 | 22           | 23           | 22           | 24           | 26           | 28           | 29            | 28            | 27            | 26            |

TABLE 8  
CORRELATION (KENDALL  $\tau$ )

| Z    | <u>NL</u>    |              |              |              |              |              |               |               |               |               |
|------|--------------|--------------|--------------|--------------|--------------|--------------|---------------|---------------|---------------|---------------|
|      | <u>N = 1</u> | <u>N = 2</u> | <u>N = 3</u> | <u>N = 4</u> | <u>N = 5</u> | <u>N = 7</u> | <u>N = 10</u> | <u>N = 15</u> | <u>N = 20</u> | <u>N = 25</u> |
| 0*   | .48          | .45          | .46          | .45          | .43          | .39          | .31           | .28           | .29           | .25           |
| .10  | .44          | .41          | .42          | .41          | .40          | .35          | .27           | .24           | .26           | .22           |
| .20  | .38          | .36          | .37          | .36          | .35          | .30          | .23           | .20           | .22           | .18           |
| .30  | .32          | .30          | .31          | .31          | .30          | .25          | .18           | .16           | .18           | .14           |
| .40  | .25          | .24          | .25          | .25          | .24          | .20          | .12           | .11           | .14           | .10           |
| .50  | .17          | .17          | .19          | .19          | .18          | .14          | .07           | .06           | .10           | .06           |
| .60  | .09          | .09          | .12          | .12          | .12          | .08          | .02           | .02           | .05           | .02           |
| .70  | .01          | .02          | .04          | .05          | .05          | .02          | -.04          | -.03          | .01           | -.02          |
| .80  | -.08         | -.06         | -.03         | -.02         | -.02         | -.04         | .09           | -.07          | -.03          | -.06          |
| .90  | -.16         | -.13         | -.01         | -.09         | -.08         | -.10         | .14           | -.12          | -.08          | -.10          |
| 1.00 | -.24         | -.21         | -.17         | -.16         | -.15         | -.16         | -.19          | -.16          | -.12          | -.14          |

\*Limit as Z approaches zero

CORRELATION (KENDALL  $\tau$ )

| Z    | <u>AL</u>    |              |              |              |              |              |               |               |               |               |
|------|--------------|--------------|--------------|--------------|--------------|--------------|---------------|---------------|---------------|---------------|
|      | <u>N = 1</u> | <u>N = 2</u> | <u>N = 3</u> | <u>N = 4</u> | <u>N = 5</u> | <u>N = 7</u> | <u>N = 10</u> | <u>N = 15</u> | <u>N = 20</u> | <u>N = 25</u> |
| 0*   | .46          | .45          | .44          | .41          | .38          | .34          | .28           | .24           | .27           | .30           |
| .10  | .42          | .41          | .40          | .38          | .35          | .30          | .25           | .21           | .25           | .28           |
| .20  | .36          | .36          | .35          | .33          | .30          | .26          | .21           | .17           | .21           | .25           |
| .30  | .29          | .30          | .30          | .27          | .25          | .21          | .16           | .13           | .18           | .22           |
| .40  | .22          | .24          | .23          | .22          | .19          | .16          | .12           | .09           | .15           | .19           |
| .50  | .14          | .16          | .17          | .15          | .13          | .11          | .07           | .05           | .11           | .16           |
| .60  | .05          | .08          | .10          | .08          | .07          | .05          | .02           | .01           | .07           | .12           |
| .70  | -.03         | .00          | .02          | .02          | .00          | -.01         | -.03          | -.03          | .03           | .09           |
| .80  | -.11         | -.07         | -.05         | -.05         | -.06         | -.07         | -.07          | -.07          | -.01          | .05           |
| .90  | -.19         | -.15         | -.12         | -.12         | -.12         | -.12         | -.12          | -.11          | -.05          | .01           |
| 1.00 | -.27         | -.22         | -.19         | -.18         | -.18         | -.17         | -.16          | -.15          | -.09          | -.02          |

\*Limit as Z approaches zero

The results of applying the second criterion are displayed in Table 7. This criterion does not sharply distinguish between the different values of credibility. There is a broad range of credibilities all of which do reasonably well.<sup>23</sup> This is particularly true for larger values of  $N$ . Again the use of more years of data eventually leads to an inferior estimate.

The results of applying the third criterion are displayed in Table 8. Again the optimal credibility does not increase as  $N$  increases. Unlike the other criteria, the third criterion cannot be used to distinguish between values of  $N$ . For each  $N$ , there is a  $Z$ , such that the correlation is zero. Thus each value of  $N$  performs as well as all the others.

Meyers points out that the distribution of Kendall's  $\tau$  can be used to obtain a confidence interval for the credibility. As explained in Appendix B, for this example a 95% confidence interval for  $\tau$  around zero has a radius of about .07.

For example, using 10 years of data, the optimal credibility using the Meyers/Dorweiler criterion for the NL set of data is 63%. However, this point estimate for the credibility is actually an estimate of an interval of credibilities that correspond to  $\tau$  between plus and minus .07. The optimal credibility is  $63\% \pm 13\%$ .<sup>24</sup>

## 8.4 Comparison of the Results of the Three Criteria

In Table 9 the optimal credibilities are displayed as determined by the three criteria for various values of  $N$ . Note that the listed values of credibility are those that happened to work best over the period of time observed. Values close to these values would also work well over this period of time.

One should think of the point estimates listed in Table 9 as the centers of interval estimates. This is illustrated when one compares the different estimates obtained by analyzing the NL and AL data sets. There is no inherent difference in the two data sets. Thus one would expect the credibilities from the two analyses to be the same. They are similar,

<sup>23</sup> This is true to a lesser extent for the first criterion. This subject is explored in Mahler [9].

<sup>24</sup> For  $Z = 63.3\%$ ,  $\tau = 0$ . For  $Z = 50.1\%$ ,  $\tau = .07$ . For  $Z = 76.4\%$ ,  $\tau = -.07$ .

but far from identical. This indicates that the peculiarities of the specific observed values are sufficient to affect the answers somewhat. There is some lack of precision in the estimates in Table 9.

TABLE 9

#### OPTIMAL CREDIBILITY

| Number of<br>Years of<br>Data Used | NL              |                 |                 | AL              |                 |                 |
|------------------------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
|                                    | Criterion<br>#1 | Criterion<br>#2 | Criterion<br>#3 | Criterion<br>#1 | Criterion<br>#2 | Criterion<br>#3 |
| 1                                  | 68%             | 75%             | 71%             | 65%             | 55%             | 66%             |
| 2                                  | 71              | 80              | 72              | 70              | 56              | 70              |
| 3                                  | 74              | 87              | 76              | 72              | 77              | 73              |
| 4                                  | 76              | 57              | 77              | 72              | 69              | 72              |
| 5                                  | 74              | 61              | 77              | 70              | 70              | 71              |
| 7                                  | 71              | 64              | 73              | 67              | 51              | 68              |
| 10                                 | 60              | 49              | 63              | 62              | 70              | 64              |
| 15                                 | 63              | 43              | 64              | 65              | 69              | 62              |
| 20                                 | 71              | 40              | 73              | 81              | 82              | 77              |
| 25                                 | 64              | 30              | 64              | 97              | 61              | 94              |

Criterion #1: Least Squares (Section 7.1)

Criterion #2: Small Chance of Large Errors (Section 7.2)

Criterion #3: Meyers/Dorweiler (Section 7.3)

This can be illustrated further by reversing the time arrow and analyzing the data sets going backwards in time rather than forwards. For example, one could use data from years 1902 to 1911 to “predict” 1901. This analysis is equally valid for determining optimal credibilities in this example as was the original analysis.

For  $N = 10$ , one gets the following optimal credibilities for the different data sets, where NLR and ALR represent respectively the NL and AL data sets reversed in time.

|              | Optimal Credibilities ( $N = 10$ ) |           |            |           |                |
|--------------|------------------------------------|-----------|------------|-----------|----------------|
|              | <u>NLR</u>                         | <u>NL</u> | <u>ALR</u> | <u>AL</u> | <u>Average</u> |
| Criterion #1 | 72%                                | 60%       | 57%        | 62%       | 63%            |
| Criterion #2 | 58                                 | 49        | 42         | 70        | 55             |
| Criterion #3 | 77                                 | 63        | 58         | 64        | 65             |

The optimal credibilities differ between the four data sets. The amount of variation provides some idea of the imprecision of the different estimates. While the optimal credibilities differ between the three criteria, the differences do not appear to be sufficiently large to allow one to draw any definitive conclusions.

In this case, the use of any value of credibility between 50% and 70% would perform reasonably well according to all three criteria for all four data sets. As a practical matter, the difference in the predictions will not vary that much depending on which value of credibility is chosen in that range.<sup>25</sup>

In most applications of credibility, values for the credibility that differ somewhat from optimal perform reasonably well and the choice between these values has a relatively small practical impact.

## *8.5 Putting the Reduction in Squared Error in Context*

The first criterion used to determine the optimal credibility is to minimize the squared error. Using the optimal credibility based on this criterion will reduce the squared error between the observed and predicted result. What should be considered a significant reduction in squared error?

<sup>25</sup> The maximum difference in any prediction for  $N = 10$  between using 50% and 70% credibility is 3.3% in the losing percentage. In most cases it is much smaller. On average it would make about a 1% difference.

Let us examine an example. For the NL data, using one year of data, the optimal credibility is 68% as shown in Table 9. As shown in Table 6 the mean squared errors are:

| <u>Z</u> | <u>Mean<br/>Squared Error</u> |
|----------|-------------------------------|
| 0        | .0091                         |
| 68%      | .0049                         |
| 100%     | .0059                         |

In this case, by the use of credibility, the squared error has been reduced from .0059 if the data were relied upon totally, or .0091 if the data were totally ignored, to .0049. In this case, the squared error has been reduced to 83% (.0049/.0059) of its previous value.<sup>26</sup>

As discussed in Appendix E, in the current case, the best that can be done using credibility to combine two estimates is to reduce the mean squared error between the estimated and observed values to 75% of the minimum of the squared errors from either relying solely on the data or ignoring the data.<sup>27</sup>

The reduction of the squared error to 83% of its previous value appears significant in light of the maximum possible reduction to 75%.<sup>28</sup>

## 8.6 *Effect of Delay in Receiving Data*

It has been shown previously for the data set examined in this paper that the further apart in time two years are, the lower the correlation between them. Thus if there is a delay before the data are available for use in experience rating, the resulting estimate of the future will be less accurate.

<sup>26</sup> The "previous" value of the squared error is considered to be the minimum of the squared errors that result from either ignoring the data entirely or relying on the data entirely.

<sup>27</sup> When using more than two or more years of data, the reduction in squared error depends on the impact of shifting parameters over time. However, in the absence of shifting parameters over time, for  $N$  years with the same weight applied to each year, the maximum possible reduction is  $1 \div (2(N + 1))$ .

<sup>28</sup> The maximum reduction is possible when the squared errors for  $Z = 0$  and  $Z = 1$  are equal.

As is shown in Table 10, as the delay increases, the squared error increases significantly. The increase in squared error is particularly significant as one goes from a situation of having the data from the most recent year available to predict the coming year to a situation of having

TABLE 10  
MINIMUM SQUARED ERROR (.0001)

| Time Between Latest<br>Data Point and<br>Future Prediction | NL                  |                     |                     |                     |                     |
|------------------------------------------------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|                                                            | <u><i>N</i> = 1</u> | <u><i>N</i> = 2</u> | <u><i>N</i> = 3</u> | <u><i>N</i> = 4</u> | <u><i>N</i> = 5</u> |
| 1                                                          | 49                  | 52                  | 51                  | 51                  | 53                  |
| 2                                                          | 66                  | 62                  | 60                  | 60                  | 60                  |
| 3                                                          | 69                  | 66                  | 65                  | 64                  | 65                  |
| 4                                                          | 73                  | 71                  | 69                  | 69                  | 70                  |
| 5                                                          | 77                  | 73                  | 73                  | 72                  | 72                  |
| 6                                                          | 76                  | 75                  | 75                  | 73                  | 74                  |
| 7                                                          | 78                  | 77                  | 75                  | 75                  | 75                  |
| 8                                                          | 79                  | 77                  | 77                  | 76                  | 75                  |
| 9                                                          | 78                  | 78                  | 77                  | 76                  | 75                  |
| 10                                                         | 78                  | 78                  | 76                  | 75                  | 75                  |

| Time Between Latest<br>Data Point and<br>Future Prediction | AL                  |                     |                     |                     |                     |
|------------------------------------------------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|                                                            | <u><i>N</i> = 1</u> | <u><i>N</i> = 2</u> | <u><i>N</i> = 3</u> | <u><i>N</i> = 4</u> | <u><i>N</i> = 5</u> |
| 1                                                          | 56                  | 56                  | 59                  | 61                  | 66                  |
| 2                                                          | 71                  | 70                  | 71                  | 74                  | 76                  |
| 3                                                          | 78                  | 77                  | 80                  | 81                  | 83                  |
| 4                                                          | 83                  | 85                  | 85                  | 87                  | 88                  |
| 5                                                          | 89                  | 89                  | 90                  | 91                  | 91                  |
| 6                                                          | 91                  | 91                  | 92                  | 93                  | 93                  |
| 7                                                          | 93                  | 93                  | 94                  | 93                  | 94                  |
| 8                                                          | 95                  | 94                  | 94                  | 94                  | 93                  |
| 9                                                          | 95                  | 94                  | 94                  | 93                  | 93                  |
| 10                                                         | 94                  | 94                  | 93                  | 93                  | 94                  |

only the next most recent year available. Unfortunately, the latter situation is more common in insurance than is the former.

As is shown in Table 11, the optimal credibility (as determined using the least squares criterion) decreases as the delay increases. Less current information is less valuable for estimating the future.

TABLE 11  
OPTIMAL CREDIBILITY (CRITERION #1, LEAST SQUARES)

| Time Between Latest<br>Data Point and<br>Future Prediction | <u>NL</u>           |                     |                     |                     |                     |
|------------------------------------------------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|                                                            | <u><i>N</i> = 1</u> | <u><i>N</i> = 2</u> | <u><i>N</i> = 3</u> | <u><i>N</i> = 4</u> | <u><i>N</i> = 5</u> |
| 1                                                          | 68                  | 71                  | 74                  | 76                  | 74                  |
| 2                                                          | 51                  | 59                  | 64                  | 64                  | 63                  |
| 3                                                          | 47                  | 53                  | 55                  | 56                  | 55                  |
| 4                                                          | 40                  | 45                  | 47                  | 47                  | 45                  |
| 5                                                          | 33                  | 38                  | 40                  | 39                  | 36                  |
| 6                                                          | 30                  | 33                  | 34                  | 32                  | 30                  |
| 7                                                          | 24                  | 26                  | 26                  | 25                  | 24                  |
| 8                                                          | 19                  | 20                  | 21                  | 21                  | 20                  |
| 9                                                          | 14                  | 16                  | 17                  | 18                  | 20                  |
| 10                                                         | 11                  | 13                  | 15                  | 18                  | 21                  |

| Time Between Latest<br>Data Point and<br>Future Prediction | <u>AL</u>           |                     |                     |                     |                     |
|------------------------------------------------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|                                                            | <u><i>N</i> = 1</u> | <u><i>N</i> = 2</u> | <u><i>N</i> = 3</u> | <u><i>N</i> = 4</u> | <u><i>N</i> = 5</u> |
| 1                                                          | 65                  | 70                  | 72                  | 72                  | 70                  |
| 2                                                          | 51                  | 57                  | 58                  | 57                  | 56                  |
| 3                                                          | 42                  | 47                  | 46                  | 46                  | 45                  |
| 4                                                          | 35                  | 36                  | 37                  | 36                  | 36                  |
| 5                                                          | 25                  | 28                  | 28                  | 28                  | 25                  |
| 6                                                          | 21                  | 22                  | 22                  | 19                  | 18                  |
| 7                                                          | 15                  | 16                  | 14                  | 14                  | 13                  |
| 8                                                          | 11                  | 9                   | 10                  | 10                  | 9                   |
| 9                                                          | 6                   | 7                   | 8                   | 7                   | 9                   |
| 10                                                         | 7                   | 7                   | 7                   | 9                   | 10                  |

