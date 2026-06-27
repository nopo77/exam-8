---
paper: mahler
chapter: 12
title: 12. MISCELLANEOUS
topics: [meyers_dorweiler_criterion, ratemaking_application, balance_property, prediction_method_selection]
key_formulas: []
---

> **TL;DR**
> - Meyers/Dorweiler focuses on error pattern (zero correlation), not magnitude — can disagree sharply with criteria 1 and 2.
> - All credibility estimates using the grand mean as complement are automatically in balance (average prediction = grand mean).
> - Ratemaking application: declining weights from covariance structure approximate commonly used actuarial weights (e.g., 10/15/20/25/30%).
> - Practical recommendation: use 2–3 years of data with more weight on the most recent year; grand mean for complement.

# 12. MISCELLANEOUS

Section 12.1 contrasts the Meyers/Dorweiler Criterion vs. the other criteria. Section 12.2 discusses a somewhat artificial ratemaking example. It is intended to point the way towards applying these or similar methods to practical situations. Section 12.3 compares the baseball example to typical insurance applications. Section 12.4 shows that the estimates that result herein from the use of the credibilities are in balance. Section 12.5 discusses the question of what estimation method to select for predicting the future loss record of baseball teams. It is included in order to complete the illustrative example used throughout this paper.

## *12.1 Contrasting the Meyers/Dorweiler Criterion vs. the Other Criteria*

Section 10.1 provides a good example of how criterion #3, Meyers/Dorweiler, differs on a basic conceptual level from the first two criteria. Both of the other criteria are concerned with eliminating large errors.<sup>49</sup> Criterion #1, least squares, does this since even a few large errors will

---

<sup>49</sup> Mahler [7] compares the credibilities that result from the application of the Bühlmann/least squares criterion and the credibilities that result from the application of the classical/limited fluctuation criterion.

greatly increase the sum of squared errors. Criterion #2, limited fluctuation, does this directly by minimizing the number of errors larger than the selected size.

In contrast, criterion #3, Meyers/Dorweiler, is concerned with the pattern of the errors. Large errors are not a problem, as long as there is no pattern relating the errors to the experience rating modifications. For example, consider the following two situations. In each case, for simplicity, only four risks are assumed.

| <u>Situation #1</u> |              |
|---------------------|--------------|
| <u>Modification</u> | <u>Error</u> |
| 1.20                | + 30%        |
| 1.20                | - 30%        |
| .80                 | + 40%        |
| .80                 | - 40%        |

| <u>Situation #2</u> |              |
|---------------------|--------------|
| <u>Modification</u> | <u>Error</u> |
| 1.30                | + 2%         |
| 1.10                | + 1%         |
| .90                 | - 1%         |
| .70                 | - 2%         |

Situation #2 with its small errors is preferable under the first two criteria. Situation #1 with its lack of a pattern of errors is preferable under the Meyers/Dorweiler criterion. Most actuaries would prefer Situation #2.

This example is not meant to discourage use of the Meyers/Dorweiler criterion. Rather it is meant to point out the potential hazards of relying solely on any single criterion, as well as the importance of understanding exactly what is being tested by any criterion that is being used.

## 12.2 A Ratemaking Example

Assume for a given line of insurance that the five most recent annual loss ratios are being combined to calculate a rate level indication.<sup>50</sup> Assume that it is three years from the latest year of data to the average date of loss under the proposed new rates.<sup>51</sup> A weighted average of the annual loss ratios will be used to estimate the future loss ratio.

If we assume a given covariance structure, equations 11.6 and 11.7 can be used to calculate the optimal least squares set of weights,  $Z_i$ , such that

$$\sum_{i=1}^5 Z_i = 1.$$

Assume the covariance of the loss ratios separated by a given number of years is as follows:<sup>52</sup>

| Separation in Years | Covariance in Loss Ratios (.00001) |
|---------------------|------------------------------------|
| 0                   | 130                                |
| 1                   | 60                                 |
| 2                   | 55                                 |
| 3                   | 50                                 |
| 4                   | 45                                 |
| 5                   | 40                                 |
| 6                   | 35                                 |
| 7                   | 30                                 |

Then the optimal weights are: 11.6%, 13.4%, 17.3%, 23.8%, 33.9%, with the more recent data receiving more weight. It is interesting to note that these weights can be reasonably approximated by the weights used in Walters [13], i.e., 10%, 15%, 20%, 25%, and 30%.

This example is for illustrative purposes only. It should not be taken as a derivation of the correct weights to use in any real world application. Unfortunately, in order to apply this idea to real world applications one

<sup>50</sup> The loss ratios for the separate years are presumed to have been adjusted for trend, development, and any other factors such as law changes.

<sup>51</sup> This period will vary, but  $\Delta = 3$  is not uncommon.

<sup>52</sup> This would be produced by  $\delta^2 = .0004$ ,  $\zeta^2 = .0009$ ,  $\ell(1) = .667$ ,  $\ell(2) = .611$ ,  $\ell(3) = .556$ ,  $\ell(4) = .500$ ,  $\ell(5) = .494$ ,  $\ell(6) = .389$ ,  $\ell(7) = .333$ , where the quantities are defined as in Appendix D.

has to estimate the covariance matrix. This will be affected by shifting parameters over time. It will also be affected by the varying quantity of data available in each year.<sup>53</sup> It will be affected by the uncertainty in the trend estimates and loss development estimates applied to each year. These complications are beyond the scope of this paper.

## *12.3 Baseball Example vs. Typical Insurance Applications*

In many typical insurance applications, credibility is used in the process of determining relativities. For example, credibility is used to determine the rate for a class or territory relative to the overall rate level. Credibility is also used in experience rating, where the rate for an individual risk is adjusted relative to an average.

In these situations, where a class, territory, or individual risk is compared relative to an average, the result depends on the other classes, territories, or risks which make up the average. An automobile territory with a low relativity in Massachusetts could have a higher loss potential than a automobile territory with a high relativity in Vermont. A workers compensation insured could have a credit experience modification simply because of the bad loss experience of several other employers in the same business in the same state. An insured with a .9 experience modification could have a higher loss potential than another risk with 1.1 modification in a different business or in a different state. The baseball example has this same feature. A team is being compared relative to the average in the league. The losing percentage only has relevance to rank teams in a single league relative to the average for that league. The difference in this example is that the average is a known constant. The grand mean is always .500.

In baseball if somebody loses, then somebody else wins. Thus the win-loss records of seven teams determine that of the remaining team in an eight team league.<sup>54</sup>

---

<sup>53</sup> In this paper, each year of baseball data represented a comparable number of games, so this aspect was not important.

<sup>54</sup> The win-loss record of teams in the same league should be negatively correlated by an amount proportional to the number of games the two teams have played.

This could have had a major impact on the analysis of this example. However, each team played each other team in the league approximately the same number of times each year and each team played approximately the same number of games in total.<sup>55</sup> Thus no team had its results distorted by playing a weaker or stronger schedule.

## 12.4 Estimates in Balance

The estimation methods used herein are always in balance.

The most general estimation method considered herein was given by equation 9.1, where the subscript  $j$  has been added to identify team  $j$ :

$$F_j = \sum_{i=1}^N Z_i X_{ij} + \left(1 - \sum_{i=1}^N Z_i\right)M$$

Then the average of the estimates  $F_j$  for all the teams in the league is given by:

$$\begin{aligned} \frac{1}{8} \sum_{j=1}^8 F_j &= \sum_{i=1}^N Z_i \left( \frac{1}{8} \sum_{j=1}^8 X_{ij} \right) + \left(1 - \sum_{i=1}^N Z_i\right)M \\ &= \left( \sum_{i=1}^N Z_i \right)M + \left(1 - \sum_{i=1}^N Z_i\right)M \\ &= M \end{aligned}$$

Note that for a given year  $i$ , the credibility  $Z_i$  assigned to each team's experience  $X_{ij}$  for that year is the same for all teams. Also note the fact that the grand mean is the same for all years.

That the estimates are in balance can be verified directly for the example given in Table 20. The predicted losing percentages for each year average to .500, subject to rounding.

## 12.5 Choice of a Prediction Method

The example in this paper is for illustrative purposes only; the purpose of this paper was not to predict baseball teams' win-loss records. Nevertheless, it may be of interest to choose a reasonable prediction method

---

<sup>55</sup> The schedule was exactly balanced, but a few scheduled games are sometimes not played.

TABLE 20

### NATIONAL LEAGUE, PREDICTIONS OF LOSING PERCENTAGES

|      | <u>NL1</u> | <u>NL2</u> | <u>NL3</u> | <u>NL4</u> | <u>NL5</u> | <u>NL6</u> | <u>NL7</u> | <u>NL8</u> |
|------|------------|------------|------------|------------|------------|------------|------------|------------|
| 1904 | .541       | .479       | .461       | .495       | .469       | .575       | .379       | .606       |
| 1905 | .582       | .568       | .432       | .456       | .398       | .610       | .423       | .534       |
| 1906 | .615       | .613       | .424       | .480       | .368       | .504       | .408       | .588       |
| 1907 | .627       | .568       | .334       | .533       | .389       | .531       | .421       | .598       |
| 1908 | .594       | .559       | .351       | .544       | .448       | .463       | .426       | .616       |
| 1909 | .578       | .598       | .375       | .529       | .408       | .476       | .405       | .631       |
| 1910 | .633       | .599       | .366       | .508       | .427       | .498       | .354       | .614       |
| 1911 | .614       | .576       | .371       | .509       | .426       | .492       | .430       | .581       |
| 1912 | .651       | .563       | .411       | .524       | .400       | .490       | .443       | .522       |
| 1913 | .624       | .582       | .414       | .511       | .376       | .508       | .425       | .557       |
| 1914 | .561       | .555       | .438       | .550       | .377       | .454       | .471       | .596       |
| 1915 | .458       | .526       | .478       | .570       | .441       | .504       | .515       | .509       |
| 1916 | .468       | .493       | .505       | .541       | .504       | .443       | .517       | .529       |
| 1917 | .437       | .438       | .536       | .574       | .464       | .440       | .551       | .559       |
| 1918 | .503       | .506       | .519       | .511       | .423       | .442       | .603       | .492       |
| 1919 | .534       | .519       | .425       | .493       | .440       | .512       | .514       | .565       |
| 1920 | .560       | .512       | .467       | .394       | .413       | .584       | .509       | .565       |
| 1921 | .567       | .448       | .488       | .458       | .449       | .573       | .490       | .528       |
| 1922 | .509       | .486       | .543       | .501       | .419       | .618       | .449       | .474       |
| 1923 | .592       | .492       | .499       | .469       | .426       | .596       | .461       | .466       |
| 1924 | .596       | .503       | .485       | .448       | .412       | .626       | .450       | .479       |
| 1925 | .615       | .448       | .478       | .462       | .418       | .605       | .440       | .536       |
| 1926 | .553       | .522       | .525       | .474       | .441       | .562       | .418       | .505       |
| 1927 | .556       | .516       | .485       | .458       | .488       | .583       | .452       | .465       |
| 1928 | .571       | .550       | .472       | .497       | .441       | .610       | .422       | .436       |
| 1929 | .613       | .509       | .441       | .487       | .434       | .648       | .452       | .418       |
| 1930 | .603       | .530       | .406       | .539       | .449       | .558       | .442       | .471       |
| 1931 | .556       | .472       | .430       | .570       | .448       | .614       | .476       | .434       |
| 1932 | .564       | .487       | .452       | .586       | .448       | .559       | .498       | .403       |
| 1933 | .513       | .478       | .441       | .584       | .504       | .520       | .467       | .492       |

TABLE 20

(CONTINUED)

|      | <u>NL1</u> | <u>NL2</u> | <u>NL3</u> | <u>NL4</u> | <u>NL5</u> | <u>NL6</u> | <u>NL7</u> | <u>NL8</u> |
|------|------------|------------|------------|------------|------------|------------|------------|------------|
| 1934 | .487       | .537       | .455       | .588       | .442       | .564       | .460       | .468       |
| 1935 | .487       | .523       | .447       | .609       | .434       | .578       | .492       | .433       |
| 1936 | .633       | .534       | .405       | .558       | .427       | .568       | .460       | .417       |
| 1937 | .545       | .543       | .442       | .532       | .426       | .603       | .470       | .440       |
| 1938 | .518       | .563       | .421       | .582       | .412       | .579       | .457       | .467       |
| 1939 | .498       | .536       | .436       | .490       | .449       | .635       | .450       | .507       |
| 1940 | .543       | .486       | .456       | .437       | .477       | .641       | .518       | .445       |
| 1941 | .547       | .458       | .494       | .398       | .508       | .635       | .495       | .466       |
| 1942 | .569       | .406       | .522       | .433       | .510       | .659       | .491       | .411       |
| 1943 | .572       | .381       | .538       | .477       | .472       | .661       | .525       | .378       |
| 1944 | .551       | .452       | .519       | .457       | .573       | .590       | .492       | .368       |
| 1945 | .559       | .530       | .515       | .451       | .544       | .586       | .455       | .363       |
| 1946 | .546       | .470       | .428       | .543       | .513       | .629       | .472       | .399       |
| 1947 | .450       | .487       | .468       | .538       | .562       | .559       | .538       | .400       |
| 1948 | .434       | .459       | .511       | .531       | .495       | .579       | .559       | .433       |
| 1949 | .453       | .439       | .548       | .554       | .504       | .554       | .497       | .451       |
| 1950 | .413       | .492       | .571       | .564       | .511       | .502       | .527       | .419       |
| 1951 | .440       | .470       | .564       | .556       | .470       | .454       | .570       | .477       |
| 1952 | .414       | .501       | .572       | .548       | .429       | .503       | .563       | .472       |
| 1953 | .411       | .542       | .518       | .541       | .428       | .458       | .646       | .457       |
| 1954 | .375       | .455       | .553       | .543       | .503       | .475       | .627       | .469       |
| 1955 | .416       | .456       | .554       | .521       | .423       | .497       | .626       | .507       |
| 1956 | .395       | .454       | .532       | .515       | .481       | .497       | .594       | .531       |
| 1957 | .419       | .434       | .572       | .453       | .521       | .523       | .566       | .512       |
| 1958 | .451       | .421       | .567       | .482       | .533       | .504       | .571       | .471       |
| 1959 | .507       | .425       | .538       | .492       | .501       | .532       | .492       | .512       |
| 1960 | .464       | .451       | .523       | .509       | .482       | .551       | .502       | .518       |

Note: Using latest three years of data, with weights of 10%, 10%, 55% (55% weight to the most recent year; 25% weight to grand mean).

for this particular problem. Assume that  $\Delta = 1$ , i.e., 1910 data are available to predict 1911, etc.

Based on Table 19, the credibilities in Table 16 work well.

The author would recommend avoiding using many years of data unless it substantially improved the accuracy. It is better to keep things simple. For this particular problem, based on Table 19, there seems little advantage to using more than 3 years of data. For example, giving 55% weight to the most recent year, 10% weight to the next most recent year, 10% weight to the third most recent year, and the remaining 25% weight to the grand mean works reasonably well.<sup>56</sup>

The predictions that result from this method of estimation applied to the National League data are shown in Table 20.<sup>57</sup> The errors are shown in Table 21.

The mean squared error is .0046.<sup>58</sup> There is a 14% chance of an error of more than 20%. The correlation used in the Meyers/Dorweiler criterion is .02, not significantly different from zero. Thus according to all three criteria this prediction method works well.

