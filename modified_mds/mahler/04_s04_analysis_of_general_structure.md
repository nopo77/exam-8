---
paper: mahler
chapter: 4
title: 4. ANALYSIS OF THE GENERAL STRUCTURE OF DATA
topics: [risk_heterogeneity, shifting_parameters, chi_squared_test, correlation_analysis, between_variance, within_variance]
key_formulas: [chi_squared_test_for_stationarity, year_pair_correlation]
---

> **TL;DR**
> - Teams differ significantly in underlying loss potential — experience rating is meaningful.
> - Risk parameters shift over time: chi-squared test across 12 five-year segments rejects stationarity for every team.
> - Year-to-year correlation decays to near zero after ~10 years — older data becomes uninformative.
> - Two testing methods illustrated: chi-squared test for shifting means; average pairwise correlation by year-gap.

# 4. ANALYSIS OF THE GENERAL STRUCTURE OF DATA

The loss experience<sup>5</sup> by risk (team) by year are given in Table 1 for the National League and Table 2 for the American League.<sup>6</sup>

## 4.1 *Is There an Inherent Difference Between Teams?*

The first question to be answered is whether there is any real difference between the experience of the different teams, or is the apparent difference just due to random fluctuations. This is the fundamental question when considering the application of experience rating.

It requires only an elementary analysis in order to show that there is a non-random difference between the teams. The average experience for each team over the whole period of time differs significantly from that of the other teams. If the experience for each team were drawn from the same probability distribution, the results for each team would be much more similar. The standard deviation in losing percentage over a sample of about 9000 games<sup>7</sup> would be .5%.<sup>8</sup> Thus if all the teams' results were drawn from the same distribution, approximately 95% of the teams would have an average losing percentage between 49% and 51%.<sup>9</sup>

The actual results are shown on Table 3. In fact, only 3 of 16 teams have losing percentages in that range. The largest deviation from the grand mean is 15 times the expected standard deviation if the teams all had the same underlying probability distribution.

---

<sup>5</sup> For each of 60 years, the percentage of games lost is given for each team. The data are from *The Sports Encyclopedia* [6].

<sup>6</sup> For the National League the teams are in order: Brooklyn, Boston, Chicago, Cincinnati, New York, Philadelphia, Pittsburgh and St. Louis. For the American League the teams are in order: Boston, Chicago, Cleveland, Detroit, New York, Philadelphia, St. Louis and Washington. In both cases, the city given is that in which the team spent the majority of the data period.

<sup>7</sup> About 150 games for a team each year times 60 years.

<sup>8</sup> A binomial distribution with a 50% chance of losing, for 9000 games, has a variance of  $9000(1/2)(1 - 1/2) = 2250$ . This is a standard deviation of 47 games lost, or  $47 \div 9000 = .5\%$  in losing percentage.

<sup>9</sup> Using the standard normal approximation, 95% of the probability is within two standard deviations of the mean which in this case is 50%.

TABLE 1

#### NATIONAL LEAGUE LOSING PERCENTAGES

|      | <u>NL1</u> | <u>NL2</u> | <u>NL3</u> | <u>NL4</u> | <u>NL5</u> | <u>NL6</u> | <u>NL7</u> | <u>NL8</u> |
|------|------------|------------|------------|------------|------------|------------|------------|------------|
| 1901 | .500       | .419       | .619       | .626       | .620       | .407       | .353       | .457       |
| 1902 | .467       | .457       | .504       | .500       | .647       | .591       | .259       | .582       |
| 1903 | .580       | .485       | .406       | .468       | .396       | .637       | .350       | .686       |
| 1904 | .641       | .634       | .392       | .425       | .307       | .658       | .431       | .513       |
| 1905 | .669       | .684       | .399       | .484       | .314       | .454       | .373       | .623       |
| 1906 | .675       | .566       | .237       | .576       | .368       | .536       | .392       | .653       |
| 1907 | .608       | .561       | .296       | .569       | .464       | .435       | .409       | .660       |
| 1908 | .591       | .656       | .357       | .526       | .364       | .461       | .364       | .682       |
| 1909 | .706       | .641       | .320       | .497       | .399       | .516       | .276       | .645       |
| 1910 | .654       | .584       | .325       | .513       | .409       | .490       | .438       | .588       |
| 1911 | .709       | .573       | .403       | .542       | .353       | .480       | .448       | .497       |
| 1912 | .660       | .621       | .393       | .510       | .318       | .520       | .384       | .588       |
| 1913 | .543       | .564       | .425       | .582       | .336       | .417       | .477       | .660       |
| 1914 | .386       | .513       | .494       | .610       | .455       | .519       | .552       | .471       |
| 1915 | .454       | .474       | .523       | .539       | .546       | .408       | .526       | .529       |
| 1916 | .414       | .390       | .562       | .608       | .434       | .405       | .578       | .608       |
| 1917 | .529       | .536       | .519       | .494       | .364       | .428       | .669       | .461       |
| 1918 | .573       | .548       | .349       | .469       | .427       | .553       | .480       | .605       |
| 1919 | .590       | .507       | .464       | .314       | .379       | .657       | .489       | .606       |
| 1920 | .592       | .396       | .513       | .464       | .442       | .595       | .487       | .513       |
| 1921 | .484       | .493       | .582       | .542       | .386       | .669       | .412       | .431       |
| 1922 | .654       | .506       | .481       | .442       | .396       | .627       | .448       | .448       |
| 1923 | .649       | .506       | .461       | .409       | .379       | .675       | .435       | .484       |
| 1924 | .654       | .403       | .471       | .458       | .392       | .636       | .412       | .578       |
| 1925 | .542       | .556       | .558       | .477       | .434       | .556       | .379       | .497       |
| 1926 | .566       | .536       | .468       | .435       | .510       | .616       | .451       | .422       |
| 1927 | .610       | .575       | .444       | .510       | .403       | .669       | .390       | .399       |
| 1928 | .673       | .497       | .409       | .487       | .396       | .717       | .441       | .383       |
| 1929 | .636       | .542       | .355       | .571       | .444       | .536       | .425       | .487       |
| 1930 | .545       | .442       | .416       | .617       | .435       | .662       | .481       | .403       |

TABLE I

(CONTINUED)

|      | <u>NL1</u> | <u>NL2</u> | <u>NL3</u> | <u>NL4</u> | <u>NL5</u> | <u>NL6</u> | <u>NL7</u> | <u>NL8</u> |
|------|------------|------------|------------|------------|------------|------------|------------|------------|
| 1931 | .584       | .480       | .455       | .623       | .428       | .571       | .513       | .344       |
| 1932 | .500       | .474       | .416       | .610       | .532       | .494       | .442       | .532       |
| 1933 | .461       | .575       | .442       | .618       | .401       | .605       | .435       | .464       |
| 1934 | .483       | .533       | .430       | .656       | .392       | .624       | .507       | .379       |
| 1935 | .752       | .542       | .351       | .556       | .405       | .582       | .438       | .377       |
| 1936 | .539       | .565       | .435       | .519       | .403       | .649       | .455       | .435       |
| 1937 | .480       | .595       | .396       | .636       | .375       | .601       | .442       | .474       |
| 1938 | .493       | .537       | .414       | .453       | .447       | .700       | .427       | .530       |
| 1939 | .583       | .451       | .455       | .370       | .490       | .702       | .556       | .399       |
| 1940 | .572       | .425       | .513       | .346       | .526       | .673       | .494       | .451       |
| 1941 | .597       | .351       | .545       | .429       | .516       | .721       | .474       | .366       |
| 1942 | .601       | .325       | .558       | .500       | .441       | .722       | .551       | .312       |
| 1943 | .556       | .471       | .516       | .435       | .641       | .584       | .481       | .318       |
| 1944 | .578       | .591       | .513       | .422       | .565       | .601       | .412       | .318       |
| 1945 | .559       | .435       | .364       | .604       | .487       | .701       | .468       | .383       |
| 1946 | .385       | .471       | .464       | .565       | .604       | .552       | .591       | .372       |
| 1947 | .390       | .442       | .552       | .526       | .474       | .597       | .597       | .422       |
| 1948 | .455       | .405       | .584       | .582       | .494       | .571       | .461       | .448       |
| 1949 | .370       | .513       | .604       | .597       | .526       | .474       | .539       | .377       |
| 1950 | .422       | .461       | .582       | .569       | .442       | .409       | .627       | .490       |
| 1951 | .382       | .506       | .597       | .558       | .376       | .526       | .584       | .474       |
| 1952 | .373       | .582       | .500       | .552       | .403       | .435       | .727       | .429       |
| 1953 | .318       | .403       | .578       | .558       | .545       | .461       | .675       | .461       |
| 1954 | .403       | .422       | .584       | .519       | .370       | .513       | .656       | .532       |
| 1955 | .359       | .448       | .529       | .513       | .481       | .500       | .610       | .558       |
| 1956 | .396       | .403       | .610       | .409       | .565       | .539       | .571       | .506       |
| 1957 | .455       | .383       | .597       | .481       | .552       | .500       | .597       | .435       |
| 1958 | .539       | .403       | .532       | .506       | .481       | .552       | .455       | .532       |
| 1959 | .436       | .449       | .519       | .519       | .461       | .584       | .494       | .539       |
| 1960 | .468       | .429       | .610       | .565       | .487       | .617       | .383       | .442       |

TABLE 2

#### AMERICAN LEAGUE LOSING PERCENTAGES

|      | <u>AL1</u> | <u>AL2</u> | <u>AL3</u> | <u>AL4</u> | <u>AL5</u> | <u>AL6</u> | <u>AL7</u> | <u>AL8</u> |
|------|------------|------------|------------|------------|------------|------------|------------|------------|
| 1901 | .419       | .390       | .599       | .452       | .489       | .456       | .650       | .545       |
| 1902 | .438       | .448       | .493       | .615       | .638       | .390       | .426       | .551       |
| 1903 | .341       | .562       | .450       | .522       | .463       | .444       | .532       | .686       |
| 1904 | .383       | .422       | .430       | .592       | .391       | .464       | .572       | .748       |
| 1905 | .487       | .395       | .506       | .484       | .523       | .378       | .647       | .576       |
| 1906 | .682       | .384       | .418       | .523       | .404       | .462       | .490       | .633       |
| 1907 | .604       | .424       | .441       | .387       | .527       | .393       | .546       | .675       |
| 1908 | .513       | .421       | .416       | .412       | .669       | .556       | .454       | .559       |
| 1909 | .417       | .487       | .536       | .355       | .510       | .379       | .593       | .724       |
| 1910 | .471       | .556       | .533       | .442       | .417       | .320       | .695       | .563       |
| 1911 | .490       | .490       | .477       | .422       | .500       | .331       | .704       | .584       |
| 1912 | .309       | .494       | .510       | .549       | .671       | .408       | .656       | .401       |
| 1913 | .473       | .487       | .434       | .569       | .623       | .373       | .627       | .416       |
| 1914 | .405       | .545       | .667       | .477       | .545       | .349       | .536       | .474       |
| 1915 | .331       | .396       | .625       | .351       | .546       | .717       | .591       | .444       |
| 1916 | .409       | .422       | .500       | .435       | .481       | .765       | .487       | .503       |
| 1917 | .408       | .351       | .429       | .490       | .536       | .641       | .630       | .516       |
| 1918 | .405       | .540       | .425       | .563       | .512       | .594       | .525       | .437       |
| 1919 | .518       | .371       | .396       | .429       | .424       | .743       | .518       | .600       |
| 1920 | .529       | .377       | .364       | .604       | .383       | .688       | .503       | .553       |
| 1921 | .513       | .597       | .390       | .536       | .359       | .654       | .474       | .477       |
| 1922 | .604       | .500       | .494       | .487       | .390       | .578       | .396       | .552       |
| 1923 | .599       | .552       | .464       | .461       | .355       | .546       | .513       | .510       |
| 1924 | .565       | .569       | .562       | .442       | .414       | .533       | .513       | .403       |
| 1925 | .691       | .487       | .545       | .474       | .552       | .421       | .464       | .364       |
| 1926 | .699       | .471       | .429       | .487       | .409       | .447       | .597       | .460       |
| 1927 | .669       | .542       | .569       | .464       | .286       | .409       | .614       | .448       |
| 1928 | .627       | .532       | .597       | .558       | .344       | .359       | .468       | .513       |
| 1929 | .623       | .612       | .467       | .545       | .429       | .307       | .480       | .533       |
| 1930 | .662       | .597       | .474       | .513       | .442       | .338       | .584       | .390       |

TABLE 2

(CONTINUED)

|      | <u>AL1</u> | <u>AL2</u> | <u>AL3</u> | <u>AL4</u> | <u>AL5</u> | <u>AL6</u> | <u>AL7</u> | <u>AL8</u> |
|------|------------|------------|------------|------------|------------|------------|------------|------------|
| 1931 | .592       | .634       | .494       | .604       | .386       | .296       | .591       | .403       |
| 1932 | .721       | .675       | .428       | .497       | .305       | .390       | .591       | .396       |
| 1933 | .577       | .553       | .503       | .513       | .393       | .477       | .636       | .349       |
| 1934 | .500       | .651       | .448       | .344       | .390       | .547       | .559       | .566       |
| 1935 | .490       | .513       | .464       | .384       | .403       | .611       | .572       | .562       |
| 1936 | .519       | .464       | .481       | .461       | .333       | .654       | .625       | .464       |
| 1937 | .474       | .442       | .461       | .422       | .338       | .642       | .701       | .523       |
| 1938 | .409       | .561       | .434       | .455       | .349       | .651       | .638       | .503       |
| 1939 | .411       | .448       | .435       | .474       | .298       | .638       | .721       | .572       |
| 1940 | .468       | .468       | .422       | .416       | .429       | .649       | .565       | .584       |
| 1941 | .455       | .500       | .513       | .513       | .344       | .584       | .545       | .545       |
| 1942 | .388       | .554       | .513       | .526       | .331       | .643       | .457       | .589       |
| 1943 | .553       | .468       | .464       | .494       | .364       | .682       | .526       | .451       |
| 1944 | .500       | .539       | .532       | .429       | .461       | .532       | .422       | .584       |
| 1945 | .539       | .523       | .497       | .425       | .467       | .653       | .464       | .435       |
| 1946 | .325       | .519       | .558       | .403       | .435       | .682       | .571       | .506       |
| 1947 | .461       | .545       | .481       | .448       | .370       | .494       | .617       | .584       |
| 1948 | .381       | .664       | .374       | .494       | .390       | .455       | .614       | .634       |
| 1949 | .377       | .591       | .422       | .435       | .370       | .474       | .656       | .675       |
| 1950 | .390       | .610       | .403       | .383       | .364       | .662       | .623       | .565       |
| 1951 | .435       | .474       | .396       | .526       | .364       | .545       | .662       | .597       |
| 1952 | .506       | .474       | .396       | .675       | .383       | .487       | .584       | .494       |
| 1953 | .451       | .422       | .403       | .610       | .344       | .617       | .649       | .500       |
| 1954 | .552       | .390       | .279       | .558       | .331       | .669       | .649       | .571       |
| 1955 | .455       | .409       | .396       | .487       | .377       | .591       | .630       | .656       |
| 1956 | .455       | .448       | .429       | .468       | .370       | .662       | .552       | .617       |
| 1957 | .468       | .416       | .503       | .494       | .364       | .614       | .500       | .643       |
| 1958 | .487       | .468       | .497       | .500       | .403       | .526       | .516       | .604       |
| 1959 | .513       | .390       | .422       | .506       | .487       | .571       | .519       | .591       |
| 1960 | .578       | .435       | .506       | .539       | .370       | .623       | .422       | .526       |

TABLE 3

#### AVERAGE LOSING PERCENTAGES (1901-1960)

| Risk (Team)     | <u>NL1</u> | <u>NL2</u> | <u>NL3</u> | <u>NL4</u> | <u>NL5</u> | <u>NL6</u> | <u>NL7</u> | <u>NL8</u> |
|-----------------|------------|------------|------------|------------|------------|------------|------------|------------|
| National League | 53.4       | 49.9       | 47.3       | 51.8       | 44.7       | 56.5       | 47.8       | 48.8       |

| Risk (Team)     | <u>AL1</u> | <u>AL2</u> | <u>AL3</u> | <u>AL4</u> | <u>AL5</u> | <u>AL6</u> | <u>AL7</u> | <u>AL8</u> |
|-----------------|------------|------------|------------|------------|------------|------------|------------|------------|
| American League | 49.5       | 49.4       | 47.0       | 48.5       | 42.6       | 52.9       | 56.4       | 53.5       |

Thus there can be no doubt that the teams actually differ.<sup>10</sup> It is therefore a meaningful question to ask whether a given team is better or worse than average.

A team that has been worse than average over one period of time is more likely to be worse than average over another period of time. If this were not true, we would not have found the statistically significant difference in the means of the teams.

Thus if we wish to predict the future experience of a team, there is useful information contained in the past experience of that team. In other words, there is an advantage to experience rating.

## *4.2 Shifting Parameters Over Time*

A similar, but somewhat different question of interest is whether for a given team the results for the different years are from the same distribution (or nearly the same distribution). In other words, are the observed different results over time due to more than random fluctuation? The answer is yes. This is a situation where the underlying parameters of the risk process shift over time.

<sup>10</sup> The situation here is somewhat complicated by the fact that one team's loss is another team's win. Thus the won-loss records of seven teams determine that of the remaining team. However, the author confirmed with a straightforward simulation that in this case this phenomenon would not affect the conclusion. For 8 teams each with the 50% loss rate playing 9000 games each, in 32 out of 600 cases (5%) a team had a winning percentage lower than 49% or more than 51%. In none of the 600 cases did a team have a winning percentage as low as 48% or as high as 52%.

As discussed in Section 2.1, the extent to which risk parameters shift over time has an important impact on the use of past insurance data to predict the future.

Whether the risk parameters shift over time can be tested in many ways. Two methods will be demonstrated here. These methods can be applied to insurance data as well as the data presented here.

The first method of testing whether parameters shift over time uses the standard chi-squared test. For each risk, one averages the results over separate 5 year periods.<sup>11</sup> Then one compares the number of games lost during the various 5 year periods. One can then determine by applying the chi-squared test that the risk process could not have the same mean over this entire period of time. The results shown in Table 4 are conclusive for every single risk. Even the most consistent risk had significant shifts over time.

In the second method of testing whether parameters shift over time, one computes the correlation between the results for all of the risks for pairs of years. Then one computes the average correlation for those pairs of years with a given difference in time. Finally, one examines how the average correlation depends on this difference. The results in our case are displayed in Table 5.

Observed values of the correlation different from zero are not necessarily statistically significant. For this example, a 95% confidence interval around zero for the correlation is approximately plus or minus .10.<sup>12</sup> Thus, for this example, the correlation decreases as the difference in time increases until about ten years when there is no longer a significant correlation between results.<sup>13</sup>

---

<sup>11</sup> The data were grouped in five year intervals for convenience. Other intervals could also have been used.

<sup>12</sup> For larger distances between the years, we have fewer observations to average, so the confidence interval expands to approximately plus or minus .12. The confidence intervals were determined via repeated simulation in which the actual data for each year were separately assigned to the individual risks at random; thus for the simulated data any observed correlation is illusory.

<sup>13</sup> For a difference of between 15 and 20 years there is again a small but significant positive correlation. The author has no explanation for this long term cycle.

TABLE 4

#### RESULTS OF CHI-SQUARED TEST OF SHIFTING PARAMETERS OVER TIME

For each risk (team) its experience over the 60 year period was averaged into 12 five-year segments. (The simplifying assumption was made of 150 games each year; this did not affect the results.) Then for each risk separately, the chi-square statistic was computed in order to test the hypothesis that each of the five year segments was drawn from a distribution with the same mean. The resulting chi-square values are:

| <u>NL1</u> | <u>NL2</u> | <u>NL3</u> | <u>NL4</u> | <u>NL5</u> | <u>NL6</u> | <u>NL7</u> | <u>NL8</u> |
|------------|------------|------------|------------|------------|------------|------------|------------|
| 107        | 45         | 98         | 35         | 39         | 73         | 114        | 119        |
| <u>AL1</u> | <u>AL2</u> | <u>AL3</u> | <u>AL4</u> | <u>AL5</u> | <u>AL6</u> | <u>AL7</u> | <u>AL8</u> |
| 114        | 69         | 34         | 30         | 97         | 162        | 53         | 65         |

For example, for the risk (team) NL2 the data by five-year segments are as follows:

|                                 | <u>'01</u>   | <u>'06</u>   | <u>'11</u>   | <u>'16</u>   | <u>'21</u>   | <u>'26</u>   | <u>'31</u>   | <u>'36</u>   | <u>'41</u>   | <u>'46</u>   | <u>'51</u>   | <u>'56</u>   |
|---------------------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
|                                 | <u>- '05</u> | <u>- '10</u> | <u>- '15</u> | <u>- '20</u> | <u>- '25</u> | <u>- '30</u> | <u>- '35</u> | <u>- '40</u> | <u>- '45</u> | <u>- '50</u> | <u>- '55</u> | <u>- '60</u> |
| (1) Games Lost*                 | 402          | 451          | 412          | 357          | 370          | 389          | 391          | 386          | 326          | 344          | 354          | 310          |
| (2) Expected Games<br>Lost**    | 374          | 374          | 374          | 374          | 374          | 374          | 374          | 374          | 374          | 374          | 374          | 374          |
| (3)=[(1)-(2)] <sup>2</sup> /(2) | 2.1          | 15.9         | 3.9          | .8           | 0            | .6           | .8           | .4           | 6.2          | 2.4          | 1.1          | 11.0         |

The sum of row (3) is 45, which is the chi-square value for this risk.

For each risk there is less than a .2% chance that the different five-year segments were drawn from distributions with the same mean.\*\*\* Thus we reject the hypothesis that the means are the same over time; we accept the hypothesis of shifting risk parameters over time.

\*Assuming 150 games per year, and the observed losing percentage for the five year segment.

\*\*Assuming 150 games per year, and the observed losing percentage for the whole 60 years.

\*\*\*For 11 degrees of freedom, there is a .16% chance of having a chi-square value of 30 or more. There is a .004% chance of having a chi-square value of 40 or more.

TABLE 5

#### AVERAGE CORRELATIONS OF RISKS EXPERIENCE OVER TIME (1901-1960)

| Difference Between<br>Pairs of<br>Years of Experience | Correlation |      |
|-------------------------------------------------------|-------------|------|
|                                                       | NL          | AL   |
| 1                                                     | .651        | .633 |
| 2                                                     | .498        | .513 |
| 3                                                     | .448        | .438 |
| 4                                                     | .386        | .360 |
| 5                                                     | .312        | .265 |
| 6                                                     | .269        | .228 |
| 7                                                     | .221        | .157 |
| 8                                                     | .190        | .124 |
| 9                                                     | .135        | .078 |
| 10                                                    | .100        | .090 |
| 11                                                    | .083        | .058 |
| 12                                                    | .103        | .063 |
| 13                                                    | .154        | .101 |
| 14                                                    | .176        | .104 |
| 15                                                    | .180        | .141 |
| 16                                                    | .246        | .178 |
| 17                                                    | .278        | .166 |
| 18                                                    | .219        | .198 |
| 19                                                    | .176        | .219 |
| 20                                                    | .136        | .225 |
| 21                                                    | .090        | .159 |
| 22                                                    | .065        | .125 |
| 23                                                    | .055        | .093 |
| 24                                                    | .004        | .048 |
| 25                                                    | -.024       | .006 |

TABLE 5

(CONTINUED)

| Difference Between<br>Pairs of<br>Years of Experience | Correlation |       |
|-------------------------------------------------------|-------------|-------|
|                                                       | NL          | AL    |
| 26                                                    | -.028       | .010  |
| 27                                                    | -.095       | -.002 |
| 28                                                    | -.128       | -.013 |
| 29                                                    | -.107       | -.032 |
| 30                                                    | -.062       | .006  |
| 31                                                    | -.061       | -.019 |
| 32                                                    | -.028       | .027  |
| 33                                                    | -.015       | .002  |
| 34                                                    | .017        | .088  |
| 35                                                    | .038        | .143  |
| 36                                                    | -.014       | .156  |
| 37                                                    | -.024       | .214  |
| 38                                                    | -.012       | .238  |
| 39                                                    | -.017       | .138  |
| 40                                                    | -.095       | .093  |
| 41                                                    | -.174       | .055  |
| 42                                                    | -.216       | .028  |
| 43                                                    | -.332       | -.043 |
| 44                                                    | -.423       | -.018 |
| 45                                                    | -.363       | -.035 |
| 46                                                    | -.332       | .066  |
| 47                                                    | -.324       | .069  |
| 48                                                    | -.373       | .136  |
| 49                                                    | -.423       | .075  |
| 50                                                    | -.475       | .145  |

The correlation between years that are close together is significantly greater than those further apart. This implies that the parameters of the risk process are shifting significantly over time. If the parameters were reasonably constant over time, the correlations would not depend on the length of time between the pair of years.

On the other hand, there is a significant correlation between the results of years close in time. Thus recent years can be usefully employed to predict the future.

