---
paper: mahler
chapter: 5
title: 5. STATEMENT OF THE PROBLEM
topics: [linear_credibility_estimate, credibility_weights, experience_rating]
key_formulas: [weighted_average_credibility_formula]
---

> **TL;DR**
> - Goal: find weights Z_i in X = ΣZ_i·Y_i that best estimate future loss potential.
> - Estimators restricted to single-year past data or the grand mean (no schedule rating or subjective information).
> - Standard two-estimate form: X = Z·Y₁ + (1−Z)·Y₂; credibility Z and its complement are mathematically symmetric.
> - Problem reduces to choosing the best Z since all estimators considered are unbiased.

# 5. STATEMENT OF THE PROBLEM

Let  $X$  be the quantity we wish to estimate. In this case,  $X$  is the expected losing percentage for a risk.

Let  $Y_1, Y_2, Y_3$ , etc., be various estimates for  $X$ . Then one might estimate  $X$  by taking a weighted average of the different estimates  $Y_i$ .

$$X = \sum_{i=1}^n Z_i Y_i,$$

where  $X$  = quantity to be estimated,

$Y_i$  = one of the estimates of  $X$ ,

$Z_i$  = weight assigned to estimate  $Y_i$  of  $X$ .

Here only linear combinations of estimators are being considered. In addition, the estimators themselves will be restricted to a single year of past data for the given risk or to the grand mean (which is 50% in this case).<sup>14</sup> No subjective information or additional data beyond the past annual losing percentages will be used.<sup>15</sup> In other words, this is a situation analogous to (prospective) experience rating. This is not a situation analogous to schedule rating.

<sup>14</sup> In other words, in this case,  $Y$  either equals the observed losing percentage for the risk in one year or equals the grand mean of 50%. Credibility methods can be applied to more general estimators.

<sup>15</sup> The use of information on the retirement of players or acquisition of new players might enable a significant increase in the accuracy of the estimate. The breakdown of the data into smaller units than an entire year might enable a significant increase in the accuracy of the estimate.

The problem to be considered here is what weights  $Z_i$  produce the “best” estimate of future losing percentage. In order to answer that question, criteria will have to be developed that allow one to compare the performance of the different methods to determine which is better. In the example being dealt with in this paper, it is easy to get unbiased estimators. Since all of the estimators being compared will be unbiased, the question of which method is better will focus on other features of the estimators.

Usually the weights  $Z_i$  are restricted to the closed interval between 0 and 1. In the most common situation we have two estimates, i.e.,  $i = 2$ . In that case we usually write:

$$X = Z \cdot Y_1 + (1 - Z) \cdot Y_2$$

where  $Z$  is called the credibility and  $(1 - Z)$  is called the complement of credibility. However, it is important to note that the usual terminology tempts us into making the mistake of thinking of the two weights and two estimates differently. The actual mathematical situation is symmetric.

