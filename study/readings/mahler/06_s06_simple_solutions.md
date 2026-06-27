---
paper: mahler
chapter: 6
title: 6. SIMPLE SOLUTIONS TO THE PROBLEM
topics: [credibility_weights, experience_rating, grand_mean, exponential_smoothing]
key_formulas: [credibility_weighted_estimate, equal_weight_n_years]
---

> **TL;DR**
> - Four simple solutions: (1) grand mean only (Z=0), (2) most recent year repeats (Z=1), (3) credibility weight one year vs. grand mean, (4) equal weight to N most recent years vs. grand mean.
> - Credibility weighting (method 3) always dominates both base cases for the proper Z choice.
> - Equal weight to N years (method 4) is a generalization that can further reduce error if parameters don't shift.
> - Bühlmann/Bayesian or classical credibility methods determine the optimal Z value.

## 6. SIMPLE SOLUTIONS TO THE PROBLEM

In this section, various relatively simple solutions to the problem will be presented.

## 6.1 *Every Risk is Average*

The first method is to predict that the future losing percentage for each risk will be equal to the overall mean of 50%. This method ignores all the past data; i.e., the past data are given zero credibility. While this is not a serious candidate for an estimation method in the particular example examined in this paper, it is a useful base case in general.

## 6.2 *The Most Recent Year Repeats*

The second method is to predict that the most recent past year's losing percentage for each risk will repeat. This is what is meant by giving the most recent year of data 100% credibility.

## *6.3 Credibility Weight the Most Recent Year and the Grand Mean*

In the third method, one gives the most recent year of data for each risk weight  $Z$ , and gives the grand mean, which in this case is 50%, weight  $1 - Z$ .

When  $Z = 0$ , one gets the first method; when  $Z = 1$ , one gets the second method. Since each of these is a special case of this more general method, by the proper choice of  $Z$  one can do better than or equal to either of the two previous methods. This is an important and completely general result. It does not depend on either the criterion that is used to compare methods or the means of deciding which value of  $Z$  to use.

## *6.4 Determining the Credibility*

When employing the third method, the obvious question is how does one determine the value of credibility to use. Ideally one would desire a theory or method that would be generally applicable, rather than one that only worked for a single example. There have been many fine papers on this subject in the actuarial literature.

Generally, the credibility considered “best” is determined by some objective criterion. This will be discussed later.

Using either Bühlmann/Bayesian credibility methods or classical/limited fluctuation credibility methods, one determines which credibility will be expected to optimize the selected criterion in the future. One can also empirically investigate which credibility would have optimized the selected criterion if it had been used in the past; i.e., one can perform retrospective tests. This will be discussed in more detail later.

## *6.5 Equal Weight to the $N$ Most Recent Years of Data*

In the fourth method, one gives equal weight to the  $N$  most recent years of data for each risk, and gives the grand mean, which in this case is 50%, weight  $1 - Z$ . This method gives each of the  $N$  most recent

years weight of  $Z/N$ .<sup>16</sup> When  $N = 1$  this reduces to the previous method. Thus this method will perform at least as well as the previous method, with the proper choices of  $N$  and  $Z$ .

