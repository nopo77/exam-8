

# Errata

## Generalized Linear Models for Insurance Rating, 2nd Edition (2025 revision)

Date Approved: 1/28/2026

In the corrections below, the **boldface text** indicates the corrected wording.

###### Page 33

*Top of page, under 3.4. Conducting Exploratory Data Analysis*

- “Plotting each **predictor variable** versus the target variable to see what (if any) relationship exists. For continuous variables, such plots may help inform decisions on variable transformations.”
- “Plotting continuous **predictor** variables versus each other, to see the correlation between them.”

*Under 3.5 Specifying Model Form*

- “What is the target variable, and which **predictor** variables should be included?”
- “Should transformations be applied to the target variable or to any of the **predictor** variables?”

###### Page 65

*6th paragraph*

“How much greater than 1 is significant? Statistical theory says that the  $F$ -statistic follows an  $F$  distribution, with a numerator degrees of freedom equal to the number of added parameters and a denominator degrees of freedom equal to  $n - p_B$ , or the number of records minus the number of parameters in the big model. **Note, however, that we do not count the dispersion parameter as a parameter when calculating the denominator degrees of freedom for the  $F$ -test.** If the percentile of the  $F$ -statistic on the  $F$  distribution is sufficiently high, we may conclude that the added parameters are indeed significant.”

*7th paragraph*

“As an example, suppose the auto GLM we built on 972 rows of data with **4** parameters yields an unscaled deviance of 365.8 and an estimated dispersion parameter of 1.42.”

###### Page 66

*2nd paragraph*

“To assess the significance of this value, we compare it against an  $F$  distribution with 4 numerator degrees of freedom and  $972 - 7$  (**3 original parameters not counting the dispersion parameter + 4 added parameters**) = **965** denominator degrees of freedom. An  $F$  distribution with those parameters has 2.412 at its 95.2 percentile, indicating a 4.8% probability of a drop in deviance of this magnitude arising by pure chance. As such, rating territory is found to be significant at the 95% significance level.”

*5th paragraph*

“...where  $p$  is the number of parameters in the model.\*”

*[Add new footnote to this sentence.]*

**\*Note that for AIC and BIC, unlike for the F-test, some GLM implementations, including R's `glm()`, count the dispersion parameter as an additional parameter when it is estimated, whereas others do not.**

###### Page 96

*Under 10.1. Generalized Linear Mixed Models (GLMMs)*

*End of the 2nd paragraph*

“Thus, the GLMM is a useful means of introducing **classical** credibility concepts into a GLM for multi-level categorical variables.<sup>23</sup>”

*Footnote 23*

“<sup>23</sup>See Klinker (2011a) for a more detailed discussion on the relationship between **classical** credibility and GLMMs.”