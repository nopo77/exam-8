---
paper: mahler
chapter: 7
title: 7. CRITERIA TO DECIDE BETWEEN SOLUTIONS
topics: [least_squares_criterion, limited_fluctuation_credibility, meyers_dorweiler_criterion, kendall_tau]
key_formulas: [kendall_tau_statistic]
---

> **TL;DR**
> - Criterion 1 (Least Squares): minimize mean squared error — the Bühlmann/Bayesian approach.
> - Criterion 2 (Limited Fluctuation): minimize probability that error exceeds k% — the classical approach.
> - Criterion 3 (Meyers/Dorweiler): correlation between (actual/predicted) and (predicted/mean) should be zero.
> - Kendall's τ = 1 − 4Q/[n(n−1)] measures the correlation for criterion 3; 95% CI radius is ~0.07 here.

## 7. CRITERIA TO DECIDE BETWEEN SOLUTIONS

In this section, we will discuss *three* criteria that can be used to distinguish between solutions. These criteria can be applied in general and not just to this example.

## 7.1 *Least Squared Error*

The first criterion involves calculating the mean squared error of the prediction produced by a given solution compared to the actual observed result. The smaller the mean squared error, the better the solution.

The Bühlmann/Bayesian credibility methods attempt to minimize the squared error; i.e., they are least squares methods. Minimizing the squared error is the same as minimizing the mean squared error.

## 7.2 *Small Chance of Large Errors*

The second criterion deals with the probability that the observed result will be more than a certain percent different than the predicted result. The less this probability, the better the solution.

This is related to the basic concept behind “classical” credibility which has also been called “limited fluctuation” credibility [7]. In classical credibility, the full credibility criterion is chosen so that there is a probability,  $P$ , of meeting the test that the maximum departure from expected is no more than  $k$  percent.

The reason the criterion is stated in this way rather than the way it is in classical credibility is that, unlike the actual observations, one cannot observe directly the inherent loss potential.<sup>17</sup> However, the two concepts are closely related, as discussed in Appendix G.

---

<sup>16</sup> In later methods, the weights given to the different years of data will be allowed to differ from each other.

<sup>17</sup> It has been shown that the loss potential varies for a risk over time. Thus it cannot be estimated as the average of many observations over time.

## 7.3 Meyers/Dorweiler

The third criterion has been taken from Glenn Meyers' paper [1]. Meyers in turn based his criterion upon the ideas of Paul Dorweiler [8].

This criterion involves calculating the correlation between two quantities. The first quantity is the ratio of actual losing percentage to the predicted losing percentage. The second quantity is the ratio of the predicted losing percentage to the overall average losing percentage. The smaller the correlation between these two quantities, i.e., the closer the correlation is to zero, the better the solution.

To compute the correlation, the Kendall  $\tau$  statistic is used.<sup>18</sup> This is explained in detail in Appendix B. The relation of this criterion as used here and as it is used by Meyers to examine experience rating is also discussed in that appendix.

