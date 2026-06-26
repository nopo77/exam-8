---
paper: mahler
chapter: 11
title: 11. EQUATIONS FOR LEAST SQUARES CREDIBILITIES
topics: [covariance_structure, least_squares_credibility, between_variance, within_variance, matrix_equations, lagrange_multipliers]
key_formulas: [squared_error_polynomial_V_of_Z, matrix_equations_11_3, least_squares_formula_11_4, constrained_equations_11_6_and_11_7]
---

> **TL;DR**
> - Expected squared error V(Z) is a quadratic in the credibility weights Z_i; differentiating yields N linear matrix equations (Eq. 11.3) solvable for optimal credibilities.
> - Between variance ≈ 0.0012–0.0016; within variance ≈ 0.0079 for the baseball data.
> - Most recent year gets ~56% credibility; subsequent years receive small, sometimes negative, weights.
> - Constraining weights to sum to 1 (no grand mean) increases MSE substantially, especially for small N.

# 11. EQUATIONS FOR LEAST SQUARES CREDIBILITIES

In Section 11.2 are equations to solve for the least squares credibility. These equations follow from the assumed covariance structure discussed in Section 11.1. In Section 11.3 the equations in Section 11.2 are modified to constrain them to place no weight on the grand mean. Section 11.4 compares the mean squared errors that result from different credibilities. Section 11.5 briefly discusses the validity of the results derived in this paper.

## 11.1 The Covariance Structure

By analyzing the covariance structure, one can set up matrix equations to solve for the credibilities that minimize the squared error. These matrix equations are discussed in the next section.

As shown in Appendix D, the variance of the data can be broken down into two pieces. There is the variance between the risks.<sup>38</sup> There is also the variance within the risks.<sup>39</sup> These two variances add up to the total variance.

|    | <u>Between Variance</u> | <u>Within Variance</u> | <u>Total Variance<sup>40</sup></u> |
|----|-------------------------|------------------------|------------------------------------|
| NL | .001230                 | .007892                | .009121                            |
| AL | .001619                 | .007875                | .009494                            |

<sup>38</sup> This has been denoted as  $\tau^2$ .

<sup>39</sup> This has been denoted as  $\delta^2 + \zeta^2$ .  $\delta^2$  is what is usually termed process variance, while  $\zeta^2$  is the variance due to shifting parameters over time.

<sup>40</sup> May differ slightly from the sum of the other two variances due to rounding.

Also of interest is the covariance between the years of data. It is assumed that this is a function of the number of years separating the data. The observed values are given in Table 15. As was seen in Table 5, the covariance decreases as the years of data are further apart. After about 6 years the covariances are relatively close to zero.

TABLE 15

COVARIANCE (.0001)

| Years<br>Separating<br>Data | NL   | AL    |
|-----------------------------|------|-------|
| 0*                          | 7892 | 7875  |
| 1                           | 4919 | 4527  |
| 2                           | 3416 | 3175  |
| 3                           | 3128 | 2411  |
| 4                           | 2541 | 1766  |
| 5                           | 1810 | 780   |
| 6                           | 1566 | 383   |
| 7                           | 955  | -99   |
| 8                           | 387  | -561  |
| 9                           | -74  | -1068 |
| 10                          | -394 | -878  |
| 11                          | -558 | -980  |
| 12                          | -389 | -1092 |
| 13                          | 3    | -737  |
| 14                          | 59   | -814  |
| 15                          | 212  | -453  |
| 16                          | 603  | -39   |
| 17                          | 786  | -139  |
| 18                          | 302  | 214   |
| 19                          | 47   | 279   |
| 20                          | -268 | 415   |

\*Equal by definition to the within variance.

It is possible to divide the within variance into two parts. The first part is the process variance excluding the effect of shifting parameters over time.<sup>41</sup> The second part is that portion of the within variance due to shifting parameters over time.<sup>42</sup> While this division may aid our understanding, it is not necessary for the calculation of the least squares credibilities. Not coincidentally, this division cannot be performed based solely on the reported data contained in Tables 1 and 2. This subject is discussed in more detail in Appendix D.

## 11.2 Matrix Equations for Least Squares Credibilities

Using the estimation method described in Section 9.2:

$$F = \sum_{i=1}^N Z_i X_i + (1 - \sum_{i=1}^N Z_i) M \quad (11.1)$$

As derived in Appendix C, one gets the following expression for the expected squared error between the observation and prediction:

$$\begin{aligned} V(Z) &= \sum_{i=1}^N \sum_{j=1}^N Z_i Z_j (\tau^2 + C(|i - j|)) \\ &\quad - 2 \sum_{i=1}^N Z_i (\tau^2 + C(N + \Delta - i)) \\ &\quad + \tau^2 + C(0) \end{aligned} \quad (11.2)$$

In equation (11.2) we have used the following quantities defined in Appendix D.

- $\tau^2$  = between variance
- $C(k)$  = covariance for data for the same risk,  $k$  years apart  
= “within covariance”
- $C(0)$  = within variance
- $\Delta$  = the length of time between the latest year of data used and the year being estimated

<sup>41</sup> This has been denoted as  $\delta^2$ .

<sup>42</sup> This has been denoted as  $\xi^2$ .

Equation 11.2 shows that the squared error is a second order polynomial in the  $Z_i$ .<sup>43</sup> This equation is the fundamental result for analyzing least squares credibility.

One can differentiate equation 11.2 in order to get  $N$  linear equations in  $N$  unknowns, which can be solved for the optimal credibilities.

$$\sum_{j=1}^N Z_j(\tau^2 + C(|i - j|)) = \tau^2 + C(N + \Delta - i) \quad i = 1, 2, \dots, N \quad (11.3)$$

The set of equations 11.3 can be solved on a computer relatively easily using the usual methods from matrix theory. The results of doing so for  $\Delta = 1$ , using the average of the variances and covariance determined from the NL and AL data separately,<sup>44</sup> are shown in Table 16.

TABLE 16  
LEAST SQUARES CREDIBILITIES, SOLUTIONS OF MATRIX EQUATIONS 11.3 ( $\Delta = 1$ )

| Number<br>of Years of<br>Data Used ( $N$ ) | Years Between Data and Estimate |      |      |     |      |     |      |      |     |     |
|--------------------------------------------|---------------------------------|------|------|-----|------|-----|------|------|-----|-----|
|                                            | 1                               | 2    | 3    | 4   | 5    | 6   | 7    | 8    | 9   | 10  |
| 1                                          | 66.0%                           | —    | —    | —   | —    | —   | —    | —    | —   | —   |
| 2                                          | 57.7                            | 12.6 | —    | —   | —    | —   | —    | —    | —   | —   |
| 3                                          | 56.1                            | 4.8  | 13.5 | —   | —    | —   | —    | —    | —   | —   |
| 4                                          | 55.6                            | 4.6  | 11.5 | 3.5 | —    | —   | —    | —    | —   | —   |
| 5                                          | 55.7                            | 5.1  | 11.7 | 6.0 | -4.4 | —   | —    | —    | —   | —   |
| 6                                          | 55.9                            | 4.9  | 11.3 | 5.8 | -6.6 | 3.9 | —    | —    | —   | —   |
| 7                                          | 56.0                            | 4.7  | 11.5 | 6.2 | -6.5 | 5.9 | -3.5 | —    | —   | —   |
| 8                                          | 56.0                            | 4.7  | 11.4 | 6.2 | -6.3 | 5.9 | -2.8 | -1.2 | —   | —   |
| 9                                          | 56.1                            | 4.9  | 11.0 | 6.6 | -6.7 | 5.3 | -3.1 | -4.3 | 5.6 | —   |
| 10                                         | 55.9                            | 5.0  | 11.2 | 6.4 | -6.4 | 5.1 | -3.4 | -4.5 | 3.6 | 3.5 |

The complement of credibility is applied to the grand mean.

First column is the credibility applied to the most recent year, second column is the credibility applied to the next most recent year, etc.

Note: Based on the average of the variances and covariances determined from the NL and AL data separately; however, assumes that for a separation of eight years or more, the covariance is zero.

<sup>43</sup> When  $N = 1$ , the squared error is a parabola as a function of the credibility. This has been noted before, for example in Appendix B of Meyers [12].

<sup>44</sup> It is assumed that for a separation of eight years or more, the covariance is zero.

The results conform reasonably well to those determined in Section 10.2.

The credibilities applied to the most recent year quickly converge to about 56%. The credibilities for the less recent years are much smaller. However, these credibilities do not monotonically decline as the years get less recent. There is a complicated pattern of weights determined by the covariance matrix. Some of the weights are even less than zero.<sup>45</sup>

The optimal credibilities are uniquely determined given the covariance structure. However, there are many other sets of credibilities which produce expected squared errors very close to minimal. The precise values of the credibilities are not particularly important, although the general range of credibilities that perform well might be instructive.

One can apply equation (11.2) to the method discussed in Sections 6.5 and 8.3 of applying equal weight  $Z_i$  to the latest  $N$  years of data, where

$$Z_i = Z/N \text{ for } i = 1, \dots, N$$

As shown in Appendix C, the least squares credibility in this case is given by:

$$Z = N \frac{N\tau^2 + \sum_{i=1}^N C(N + \Delta - i)}{N^2\tau^2 + \sum_{i=1}^N \sum_{j=1}^N C(|i - j|)} \quad (11.4)$$

The results of applying this equation for  $\Delta = 1$ , using the average of the variances and covariances determined from the NL and AL data separately,<sup>46</sup> are shown in Table 17.

Table 17 can be compared to Table 11.

The results in Table 11 conform reasonably well to those determined empirically for each data set (for  $\Delta = 1$ ).

<sup>45</sup> Giving negative weight to some years allows a larger weight to be given to other years. The net effect is to reduce the expected squared error.

<sup>46</sup> It is assumed that for a separation of eight years or more, the covariance is zero.

TABLE 17

LEAST SQUARES CREDIBILITY, SOLUTION TO  
EQUATION 11.4 ( $\Delta = 1$ )

| <u>Number of Years<br/>of Data Used (<math>N</math>)</u> | <u><math>Z</math></u> | <u><math>Z \div N</math></u> |
|----------------------------------------------------------|-----------------------|------------------------------|
| 1                                                        | 66.0%                 | 66.0%                        |
| 2                                                        | 70.3                  | 35.2                         |
| 3                                                        | 72.9                  | 24.3                         |
| 4                                                        | 73.6                  | 18.4                         |
| 5                                                        | 72.2                  | 14.4                         |
| 6                                                        | 71.3                  | 11.9                         |
| 7                                                        | 69.9                  | 10.0                         |
| 8                                                        | 68.2                  | 8.5                          |
| 9                                                        | 67.3                  | 7.5                          |
| 10                                                       | 66.9                  | 6.7                          |

Equal weight  $Z/N$  is applied to each of the  $N$  most recent years of data. The complement of credibility,  $1 - Z$ , is applied to the grand mean.

Note: Based on the average of the variances and covariances determined from the NL and AL data separately; however, assumes that for a separation of eight years or more, the covariance is zero.

## *11.3 Placing No Weight on the Grand Mean*

Once the estimation method described in Sections 9.1 and 10.1 gets “up to speed,” the initial estimate, which was taken as the grand mean, has very little weight. For all intents and purposes each risk is estimated based on its own past data, without relying on the data of other risks, in particular the grand mean.<sup>47</sup>

---

<sup>47</sup> The covariance structure is herein estimated using the data for all risks. This in turn is used to estimate the optimal credibilities. However, the credibilities are applied to the data for the particular risk we are estimating.

One can constrain the credibilities used in equation 11.1, so that they add to unity, thus giving no weight to the grand mean. Equation 11.1 then becomes

$$F = \sum_{i=1}^N Z_i X_i \quad (11.5)$$

with the constraint

$$\sum_{i=1}^N Z_i = 1. \quad (11.6)$$

The least squares credibilities for equations 11.5 and 11.6 are derived in Appendix C using the method of Lagrange Multipliers. The result is a set of  $N + 1$  linear equations in  $N + 1$  unknowns, the  $Z_i$  for  $i = 1, \dots, N$ , and  $\lambda$ , the Lagrange Multiplier. There is the single constraint equation 11.6, plus the  $N$  equations 11.7.

$$\sum_{j=1}^N Z_j C(|i - j|) = C(N + \Delta - i) + \frac{\lambda}{2}, \quad i = 1, 2, \dots, N \quad (11.7)$$

The set of equations 11.6 and 11.7 can be solved on a computer relatively easily using the usual methods from matrix theory. The results of doing so for  $\Delta = 1$ , using the average of the variances and covariances determined from the NL and AL data separately,<sup>48</sup> are shown in Table 18.

## 11.4 Mean Squared Errors

The mean squared errors that result from using the credibilities in Tables 16, 17, and 18 are displayed in Table 19.

When applying general weights to the latest  $N$  years of data, giving the most remote year of data no weight is equivalent to the case of using the latest  $N - 1$  years of data. Since using the latest  $N - 1$  years of data is a special case of using the latest  $N$  years of data, we expect the squared errors to decline, or remain constant.

This is what we observe for the credibilities from Table 16. They decline until  $N = 6$ , where the point of diminishing returns is reached.

<sup>48</sup> It is assumed that for a separation of eight years or more, the covariance is zero.

TABLE 18

LEAST SQUARES CREDIBILITIES, SOLUTIONS OF EQUATIONS 11.6 AND 11.7 ( $\Delta = 1$ )

| Number<br>of Years of<br>Data Used ( <i>N</i> ) | Years Between Data and Estimate |      |      |      |      |      |      |      |      |     |
|-------------------------------------------------|---------------------------------|------|------|------|------|------|------|------|------|-----|
|                                                 | 1                               | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10  |
| 1                                               | 100.0%                          | —    | —    | —    | —    | —    | —    | —    | —    | —   |
| 2                                               | 72.6                            | 27.4 | —    | —    | —    | —    | —    | —    | —    | —   |
| 3                                               | 66.1                            | 10.3 | 23.6 | —    | —    | —    | —    | —    | —    | —   |
| 4                                               | 63.5                            | 9.1  | 16.0 | 11.4 | —    | —    | —    | —    | —    | —   |
| 5                                               | 63.1                            | 8.7  | 15.8 | 9.5  | 2.9  | —    | —    | —    | —    | —   |
| 6                                               | 62.8                            | 7.6  | 14.1 | 8.6  | -3.9 | 10.8 | —    | —    | —    | —   |
| 7                                               | 62.5                            | 7.7  | 13.8 | 8.2  | -4.1 | 9.0  | 2.9  | —    | —    | —   |
| 8                                               | 62.3                            | 7.3  | 14.0 | 7.7  | -4.8 | 8.6  | -0.2 | 5.1  | —    | —   |
| 9                                               | 61.8                            | 7.3  | 13.0 | 8.3  | -5.7 | 7.0  | -1.1 | -1.9 | 11.2 | —   |
| 10                                              | 60.8                            | 7.5  | 13.1 | 7.7  | -5.2 | 6.3  | -2.2 | -2.5 | 6.1  | 8.4 |

The credibilities are constrained to sum to unity.

First column is the credibility applied to the most recent year, second column is the credibility applied to the next most recent year, etc.

Note: Based on the average of the variances and covariances determined from the NL and AL data separately; however, assumes that for a separation of eight years or more, the covariance is zero.

Applying the same weight to each year is a special case of using the general weights. Thus the squared errors that result from using the credibilities from Table 17 should be greater than or equal to those that result from the credibilities from Table 16. This is the case, as shown in Table 19. Also, as was observed in Section 8.3, using more years of data leads in this case to larger squared errors.

Applying no weight to the grand mean is a special case of using the general weights. Thus the squared errors that result from using the credibilities from Table 18 should be greater than or equal to those that result from the credibilities from Table 16. As is shown in Table 19, the squared errors are substantially greater, with the gap narrowing as the number of years increases.

TABLE 19

| Number<br>of Years of<br>Data Used ( <i>N</i> ) | Mean Squared Errors (.0001)*                     |                                                   |                                                    |
|-------------------------------------------------|--------------------------------------------------|---------------------------------------------------|----------------------------------------------------|
|                                                 | Using the<br>Credibilities<br>From<br>Table 16** | Using the<br>Credibilities<br>From<br>Table 17*** | Using the<br>Credibilities<br>From<br>Table 18**** |
| 1                                               | 52                                               | 52                                                | 63                                                 |
| 2                                               | 51                                               | 54                                                | 58                                                 |
| 3                                               | 49                                               | 55                                                | 54                                                 |
| 4                                               | 48                                               | 57                                                | 52                                                 |
| 5                                               | 48                                               | 60                                                | 52                                                 |
| 6                                               | 47                                               | 61                                                | 51                                                 |
| 7                                               | 47                                               | 64                                                | 51                                                 |
| 8                                               | 47                                               | 66                                                | 51                                                 |
| 9                                               | 47                                               | 68                                                | 51                                                 |
| 10                                              | 47                                               | 70                                                | 50                                                 |

\* Mean squared error using the stated credibilities to predict for the NL and AL data sets.

\*\* The complement of credibility is given to the grand mean.

\*\*\* Equal weight to *N* years, with the complement of credibility given to the grand mean.

\*\*\*\* The credibilities add up to one, and thus no weight is given to the grand mean.

## *11.5 Validity of Results*

The credibilities determined in Sections 10 and prior are all determined empirically by directly working with the data. In this section equations for the least squares credibilities have been introduced along with an assumed covariance structure.

The credibilities resulting from the use of the equations in this section are comparable to those determined in the previous sections empirically. As is shown in Appendix F, the observed pattern of squared errors is comparable to that derived from the assumed covariance structure.

Therefore, the results of this section are an appropriate means of estimating least squares credibilities for this example. How well these results would apply to another situation would depend on the covariance structure that underlies the particular data set.

