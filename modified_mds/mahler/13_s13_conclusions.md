---
paper: mahler
chapter: 13
title: 13. CONCLUSIONS
topics: [credibility_theory, experience_rating, shifting_parameters, least_squares_credibility]
key_formulas: []
---

> **TL;DR**
> - When parameters shift over time, older data should receive substantially less credibility.
> - Minimizing delay in receiving data is important when parameters shift significantly.
> - All three criteria (least squares, limited fluctuation, Meyers/Dorweiler) gave similar optimal credibilities; Meyers/Dorweiler can diverge from the others.
> - MSE is a second-order polynomial in credibility weights; linear equations from covariance structure solve for the optimal set.

## 13. CONCLUSIONS

The data from baseball used in this paper provide a useful way to examine and illustrate credibility concepts.

The methods and concepts illustrated here can be applied to problems actuaries deal with in insurance. However, this paper is only a first step; there is further work required to apply these general concepts to any specific practical situation.

---

<sup>56</sup> Many other choices would also work reasonably well. This illustrates the typical situation where once the general form of the weights is determined, there is a range of weights that work well. Usually, the specific choice of weights within that range has relatively little impact on the final result.

<sup>57</sup> For example, the 1904 entry under NL2:  $.479 = (.10)(.419) + (.10)(.457) + (.55)(.485) + (.25)(.500)$ , where the first three values are from Table 1, and .500 is the grand mean.

<sup>58</sup> The mean squared error is .0049 when the method is applied to both the AL and NL data sets. This is a standard deviation of  $10\frac{1}{2}$  losses out of a season of 150 games; the process standard deviation is about 6 losses out of a season of 150 games.

TABLE 21

### NATIONAL LEAGUE, ERRORS OF PREDICTIONS IN TABLE 20

|      | <u>NL1</u> | <u>NL2</u> | <u>NL3</u> | <u>NL4</u> | <u>NL5</u> | <u>NL6</u> | <u>NL7</u> | <u>NL8</u> |
|------|------------|------------|------------|------------|------------|------------|------------|------------|
| 1904 | -.100      | -.155      | .069       | .070       | .162       | -.083      | -.052      | .093       |
| 1905 | -.087      | -.116      | .033       | -.028      | .084       | .156       | .050       | -.089      |
| 1906 | -.060      | .047       | .187       | -.096      | .000       | -.032      | .016       | -.065      |
| 1907 | .019       | .007       | .038       | -.036      | -.075      | .096       | .012       | -.062      |
| 1908 | .003       | -.097      | -.006      | .018       | .084       | .002       | .062       | -.066      |
| 1909 | -.128      | -.043      | .055       | .032       | .009       | -.040      | .129       | -.014      |
| 1910 | -.021      | .015       | .041       | -.005      | .018       | .008       | -.084      | .026       |
| 1911 | -.095      | .003       | -.032      | -.033      | .073       | .012       | -.018      | .084       |
| 1912 | -.009      | -.058      | .018       | .014       | .082       | -.030      | .059       | -.066      |
| 1913 | .081       | .018       | -.011      | -.071      | .040       | .091       | -.052      | -.103      |
| 1914 | .175       | .042       | -.056      | -.060      | -.078      | -.065      | -.081      | .125       |
| 1915 | .004       | .052       | -.045      | .031       | -.105      | .096       | -.011      | -.020      |
| 1916 | .054       | .103       | -.057      | -.067      | .070       | .038       | -.061      | -.079      |
| 1917 | -.092      | -.098      | .017       | .080       | .100       | .012       | -.118      | .098       |
| 1918 | -.070      | -.042      | .170       | .042       | -.004      | -.111      | .123       | -.113      |
| 1919 | -.056      | .012       | -.039      | .179       | .061       | -.145      | .025       | -.041      |
| 1920 | -.032      | .116       | -.046      | -.070      | -.029      | -.011      | .022       | .052       |
| 1921 | .083       | -.045      | -.094      | -.084      | .063       | -.096      | .078       | .097       |
| 1922 | -.145      | -.020      | .062       | .059       | .023       | -.009      | .001       | .026       |
| 1923 | -.057      | -.014      | .038       | .060       | .047       | -.079      | .026       | -.018      |
| 1924 | -.058      | .100       | .014       | -.010      | .020       | -.010      | .038       | -.099      |
| 1925 | .073       | -.108      | -.080      | -.015      | -.016      | .049       | .061       | .039       |
| 1926 | -.013      | -.014      | .057       | .039       | -.069      | -.054      | -.033      | .083       |
| 1927 | -.054      | -.059      | .041       | .052       | .085       | .086       | .062       | .066       |
| 1928 | -.102      | .053       | .063       | .010       | .045       | -.107      | -.019      | .053       |
| 1929 | -.023      | -.033      | .086       | -.084      | -.010      | .112       | .027       | -.069      |
| 1930 | .058       | .088       | -.010      | -.078      | .014       | -.104      | -.039      | .068       |
| 1931 | -.028      | -.008      | -.025      | -.053      | .020       | .043       | -.037      | .090       |
| 1932 | .064       | .013       | .036       | -.024      | -.084      | .065       | .056       | -.129      |
| 1933 | .052       | -.097      | -.001      | -.034      | .103       | -.085      | .032       | .028       |

TABLE 21

(CONTINUED)

|      | <u>NL1</u> | <u>NL2</u> | <u>NL3</u> | <u>NL4</u> | <u>NL5</u> | <u>NL6</u> | <u>NL7</u> | <u>NL8</u> |
|------|------------|------------|------------|------------|------------|------------|------------|------------|
| 1934 | .004       | .004       | .025       | -.068      | .050       | -.060      | -.047      | .089       |
| 1935 | -.265      | -.019      | .096       | .053       | .029       | -.004      | .054       | .056       |
| 1936 | .094       | -.031      | -.030      | .039       | .024       | -.081      | .005       | -.018      |
| 1937 | .065       | -.052      | .046       | -.104      | .051       | .002       | .028       | -.034      |
| 1938 | .025       | .026       | .007       | .129       | -.035      | -.121      | .030       | -.063      |
| 1939 | -.085      | .085       | -.019      | .120       | -.041      | -.067      | -.106      | .108       |
| 1940 | -.029      | .061       | -.057      | .091       | -.049      | -.032      | .024       | -.006      |
| 1941 | -.050      | .107       | -.051      | -.031      | -.008      | -.086      | .021       | .100       |
| 1942 | -.032      | .081       | -.036      | -.067      | .069       | -.063      | -.060      | .099       |
| 1943 | .016       | -.090      | .022       | .042       | -.169      | .077       | .044       | .060       |
| 1944 | -.027      | -.139      | .006       | .035       | .008       | -.011      | .080       | .050       |
| 1945 | .000       | .095       | .151       | -.153      | .057       | -.115      | -.013      | -.020      |
| 1946 | .161       | -.001      | -.036      | -.022      | -.091      | .077       | -.119      | .027       |
| 1947 | .060       | .045       | -.084      | .012       | .088       | -.038      | -.059      | -.022      |
| 1948 | -.021      | .054       | -.073      | -.051      | .001       | .008       | .098       | -.015      |
| 1949 | .083       | -.074      | -.056      | -.043      | -.022      | .080       | -.042      | .074       |
| 1950 | -.009      | .031       | -.011      | -.005      | .069       | .093       | -.100      | -.071      |
| 1951 | .058       | -.036      | -.033      | -.002      | .094       | -.072      | -.014      | .003       |
| 1952 | .041       | -.081      | .072       | -.004      | .026       | .068       | -.164      | .043       |
| 1953 | .093       | .139       | -.060      | -.017      | -.117      | -.003      | -.029      | -.004      |
| 1954 | -.028      | .033       | -.031      | .024       | .133       | -.038      | -.029      | -.063      |
| 1955 | .057       | .008       | .025       | .008       | -.058      | -.003      | .016       | -.051      |
| 1956 | -.001      | .051       | -.078      | .106       | -.084      | -.042      | .023       | .025       |
| 1957 | -.036      | .051       | -.025      | -.028      | -.031      | .023       | -.031      | .077       |
| 1958 | -.088      | .018       | .035       | -.024      | .052       | -.048      | .116       | -.061      |
| 1959 | .071       | -.024      | .019       | -.027      | .040       | -.052      | -.002      | -.027      |
| 1960 | -.004      | .022       | -.087      | -.056      | -.005      | -.066      | .119       | .076       |

Note: Predicted Losing Percentage minus Actual Losing Percentage

When shifting parameters over time is an important phenomenon, older years of data should be given substantially less credibility than more recent years of data. The more significant this phenomenon, the more important it is to minimize the delay in receiving the data that is to be used to make the prediction.

In this paper three different criteria were examined that can be used to select the optimal credibility: least squares, limited fluctuation, and Meyers/Dorweiler. In applications, one or more of these three criteria should be useful. While the first two criteria are closely related, the third criterion can give substantially different results than the others.

Generally the mean squared error can be written as a second order polynomial in the credibilities. The coefficients of this polynomial can be written in terms of the covariance structure of the data. This in turn allows one to obtain linear equation(s) which can be solved for the least squares credibilities in terms of the covariance structure.

