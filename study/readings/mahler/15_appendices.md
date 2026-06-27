---
paper: mahler
chapter: null
title: APPENDIX A
topics: [kendall_tau, baseball_analogy, covariance_structure, lagrange_multipliers, squared_error_decomposition]
key_formulas: [kendall_tau_formula, lagrange_multiplier_credibility_equations]
---

> **TL;DR**
> - Appendix A: Baseball as an analogy to workers compensation risk (players ~ workers, field manager ~ plant manager).
> - Appendix B: Meyers/Dorweiler — Kendall's τ = 1 − 4Q/[n(n−1)]; zero τ means no pattern between experience modification and modified loss ratio.
> - Appendices C–D: Derivation of V(Z) quadratic, matrix equations for optimal credibilities, variance decomposition into between/process/shifting components.
> - Appendices E–G: Theoretical minimum squared error reduction; validation; relation to classical credibility.

## APPENDIX A

### SOME RELEVANT FEATURES OF BASEBALL

Baseball is a competitive sport involving a combination of luck and skill. Two teams play against each other in a game; the team that scores the most “runs” wins the game, the other team loses.<sup>1</sup>

Each team has nine players in the game at a time.<sup>2</sup> Players may be substituted for, but once they leave the game they cannot return. Over this period of time each team had 20 to 25 players on its roster.<sup>3</sup> The individual skills of the players, as well as how their skills complement each other, has a direct impact on the quality of the team.

In addition to the players, a team has coaches and a field manager. By supervising the players’ training and conditioning, providing advice, deciding who plays, and by various decisions throughout the game, these people have some effect on the percentage of games lost or won by the team.

Each team has an owner(s) and other office personnel.<sup>4</sup> By developing new players, trading for players with other teams, etc., management has some effect on the percentage of games lost or won by the team.

All of these elements that affect the quality of the team shift over time. A team’s roster of players typically changes a little during the course of a single year; over the course of several years the changes are substantial. It is unusual for a player to be with a single team for more than 10 years, although on very rare occasions a player has played for a single team for 20 years.

Even if the identity of the players were to stay the same, the skill level of individual players changes over time. The most important effect is aging; as a player gets older he generally improves until he reaches a

---

<sup>1</sup> While it is possible for a baseball game to end in a tie, such games are ignored in major league standings.

<sup>2</sup> Currently the American League has added a tenth player, the designated hitter.

<sup>3</sup> Of the players on the roster, about half get most of the playing time, while the remainder see much less playing time.

<sup>4</sup> During the latter half of this period a team had a general manager.

peak and then declines. Injuries can have a profound impact on a player's skill; sometimes that impact is temporary while sometimes it is permanent.

The field managers and coaching staff also change over time.<sup>5</sup> In addition, the owner(s) and upper management change, but much less frequently.

Finally, a team occasionally relocates to another city.

It might be useful to think of the following analogy to a workers compensation risk. The baseball players correspond to the workers in the factory. The field manager corresponds to the plant manager. The baseball upper management corresponds to the corporation's upper management.

---

<sup>5</sup> Quite often the departure of the field manager will be related to the poor record of the team.

## APPENDIX B

### MEYERS/DORWEILER CRITERION AND KENDALL'S TAU

If an experience rating plan works properly, then after the application of experience rating, an insurer should be equally willing to write debit and credit risks. In other words, the modified loss ratio of expected losses to modified premiums should be the same for debit and credit risks.

Mathematically, we desire that the correlation between the experience modification and the modified loss ratio be zero.<sup>1</sup>

In the example in this paper, the experience modification corresponds to the ratio of predicted losing percentage to the grand mean losing percentage.<sup>2</sup> For example, a predicted losing percentage of 60% is equivalent to an experience modification of  $60\% \div 50\% = 1.2$ . The modified loss ratio corresponds to the ratio of the actual losing percentage and the predicted losing percentage.<sup>3</sup> The third criterion used in this paper is that the correlation between these two ratios be zero. This corresponds to the criterion used by Meyers.

Meyers [1] uses the Kendall  $\tau$  to measure correlation.

Let  $X$  and  $Y$  be two vectors of length  $n$ .<sup>4</sup> Kendall's  $\tau$  can be calculated as follows [14]. Suppose  $Y$  is arranged in its natural order. Assume that the corresponding ranks of  $X$  are  $X_1, X_2, \dots, X_n$ , a permutation of  $1, 2, \dots, n$ . Let  $Q$  be the number of inversions in  $X_1, X_2, \dots, X_n$ .<sup>5</sup> Then let

$$\tau = 1 - \frac{4Q}{n(n-1)}$$

<sup>1</sup> If the correlation is positive, then insurers would prefer to write credit risks. The credits and debits given are on average too small, i.e., the credibility assigned to the experience is too small. The situation is reversed for a negative correlation.

<sup>2</sup> The predicted losses are equal to the experience modification times the expected losses for an average risk in the class. In a more general situation one would have classifications of risks; in this example we have only one such classification and thus use the grand mean rather than the class mean.

<sup>3</sup> In general the modified loss ratio is equal to the expected loss ratio times the actual losses over the predicted losses. In this example, the expected loss ratio can be thought of as unity.

<sup>4</sup> In our case,  $X$  would be the experience modifications and  $Y$  would be the corresponding modified loss ratios.

<sup>5</sup> For example, in the  $X$ -ranking 3214 for  $n = 4$ , there are 3 inversions of order.

$\tau$  is symmetrically distributed on the range  $[-1, +1]$ . As is usual for measures of correlation,  $+1$  signifies complete agreement and  $-1$  signifies complete disagreement.

As shown in Kendall and Stuart [14],

$$\text{Var } \tau = \frac{2(2n + 5)}{9n(n - 1)}$$

As  $n$  approaches infinity the distribution of  $\tau$  approaches the normal distribution.

In the examples in this paper, the variance of  $\tau$  varies from .0009 to .0016.<sup>6</sup> The standard deviation of  $\tau$  goes from .031 to .040. Thus an approximate 95% confidence interval around zero for  $\tau$  has a radius of approximately .07, about two standard deviations.

---

<sup>6</sup>  $n = 8$  teams times 59 years = 472 to  $n = 8$  times 35 = 280.

## APPENDIX C

### MATRIX EQUATIONS FOR LEAST SQUARES CREDIBILITY

In this appendix, equations 11.2, 11.3, 11.4, and 11.7 in the main text are derived. The squared error is written as a second order polynomial in the credibilities, with the coefficients depending on the covariance structure discussed in Appendix D. This squared error is minimized by setting the partial derivative(s) with respect to the credibilities equal to zero.

Assume an estimate for year  $N + \Delta$ , using  $N$  years of data, is given by:

$$F = \sum_{i=1}^N Z_i X_i + (1 - \sum Z_i) M$$

where  $X_i$  is the data for year  $i$ , and  $M$  is the grand mean.<sup>1</sup> Let  $Z_0 = 1 - \sum Z_i$ . Write  $Z$  for the vector  $Z_0, Z_1, \dots, Z_N$ .

Then the mean squared error between the prediction and the observation is given by the expected value of the squared difference between  $F$  and  $X_{N+\Delta}$ .

$$\begin{aligned} V(Z) &= E[(F - X_{N+\Delta})^2] \\ &= E\left[\left\{\sum_{i=1}^N Z_i (X_i - X_{N+\Delta}) + Z_0 (M - X_{N+\Delta})\right\}^2\right] \\ &= \sum_{i=1}^N Z_i^2 E[(X_i - X_{N+\Delta})^2] \\ &\quad + \sum_{i=1}^N \sum_{j \neq i}^N Z_i Z_j E[(X_i - X_{N+\Delta})(X_j - X_{N+\Delta})] \\ &\quad + 2 \sum_{i=1}^N Z_0 Z_i E[(X_i - X_{N+\Delta})(M - X_{N+\Delta})] \\ &\quad + Z_0^2 E[(M - X_{N+\Delta})^2] \end{aligned}$$

<sup>1</sup> It is assumed that the grand mean is known. This is the case in this paper. It is the case whenever one is only concerned with relativities compared to the overall average.

From Appendix D we have,<sup>2</sup>

$$\begin{aligned} E[(X_i - X_{N+\Delta})^2] &= 2\delta^2 + 2\zeta^2(1 - \ell(N + \Delta - i)) \\ E[(X_i - X_{N+\Delta})(X_j - X_{N+\Delta})] &= \delta^2 + \zeta^2(1 + \ell(|i - j|) \\ &\quad - \ell(N + \Delta - i) - \ell(N + \Delta - j)) \\ E[(X_i - X_{N+\Delta})(M - X_{N+\Delta})] &= \delta^2 + \zeta^2(1 - \ell(N + \Delta - i)) \\ E[(M - X_{N+\Delta})^2] &= \delta^2 + \zeta^2 + \tau^2 \end{aligned}$$

Therefore

$$\begin{aligned} V(Z) &= \sum_{i=1}^N Z_i^2(2\delta^2 + 2\zeta^2(1 - \ell(N + \Delta - i))) \\ &\quad + \sum_{i=1}^N \sum_{j \neq i} Z_i Z_j \left[ \delta^2 + \zeta^2(1 + \ell(|i - j|) - \ell(N + \Delta - i) \right. \\ &\quad \left. - \ell(N + \Delta - j)) \right] \\ &\quad + 2Z_0 \sum_{i=1}^N Z_i(\delta^2 + \zeta^2(1 - \ell(N + \Delta - i))) \\ &\quad + Z_0^2(\delta^2 + \tau^2 + \zeta^2) \\ V(Z) &= \delta^2 \left[ \sum_{i=0}^N \sum_{j=0}^N Z_i Z_j + \sum_{i=1}^N Z_i^2 \right] + Z_0^2 \tau^2 \\ &\quad + \zeta^2 \left[ \sum_{i=0}^N \sum_{j=0}^N Z_i Z_j + \sum_{i=1}^N \sum_{j=1}^N Z_i Z_j (\ell(|i - j|) - \ell(N + \Delta - i) \right. \\ &\quad \left. - \ell(N + \Delta - j)) - 2Z_0 \sum_{i=1}^N Z_i \ell(N + \Delta - i) \right] \end{aligned}$$

but

$$\sum_{i=0}^N Z_i = Z_0 + \sum_{i=1}^N Z_i = (1 - \sum_{i=1}^N Z_i) + \sum_{i=1}^N Z_i = 1$$

<sup>2</sup> In Appendix D,  $X(\theta, t)$  = the observation for risk  $\theta$  at time  $t$ . Since in this appendix none of the calculations are performed for individual risks, the  $\theta$  has been suppressed in order to simplify the notation.

Therefore

$$\begin{aligned}
 V(Z) &= \delta^2 + Z_0^2 \tau^2 + \zeta^2 + \delta^2 \sum_{i=1}^N Z_i^2 \\
 &\quad + \zeta^2 \sum_{i=1}^N \sum_{j=1}^N Z_i Z_j (\ell(|i-j|) - \ell(N + \Delta - i) - \ell(N + \Delta - j)) \\
 &\quad - \zeta^2 Z_0 2 \sum_{i=1}^N Z_i \ell(N + \Delta - i)
 \end{aligned}$$

$$\begin{aligned}
 V(Z) &= \delta^2 + \zeta^2 + \tau^2 + \tau^2 \left[ \sum_{i=1}^N Z_i \right]^2 - 2\tau^2 \sum_{i=1}^N Z_i \\
 &\quad + \delta^2 \sum_{i=1}^N Z_i^2 + \zeta^2 \sum_{i=1}^N \sum_{j=i}^N Z_i Z_j (\ell(|i-j|) - \ell(N + \Delta - i) \\
 &\quad - \ell(N + \Delta - j)) - 2\zeta^2 \sum_{i=1}^N Z_i \ell(N + \Delta - i) \\
 &\quad + 2\zeta^2 \sum_{i=1}^N \sum_{j=1}^N Z_i Z_j \ell(N + \Delta - i)
 \end{aligned}$$

$$\begin{aligned}
 V(Z) &= \delta^2 + \zeta^2 + \tau^2 + \tau^2 \sum_{i=1}^N \sum_{j=1}^N Z_i Z_j - 2\tau^2 \sum_{i=1}^N Z_i \\
 &\quad + \delta^2 \sum_{i=1}^N Z_i^2 + \zeta^2 \sum_{i=1}^N \sum_{j=i}^N Z_i Z_j (\ell(|i-j|) - \ell(N + \Delta - j)) \\
 &\quad - 2\zeta^2 \sum_{i=1}^N Z_i \ell(N + \Delta - i)
 \end{aligned}$$

$$\begin{aligned}
 V(Z) &= \sum_{i=1}^N \sum_{j=1}^N Z_i Z_j (\delta^2 \delta_{ij} + \tau^2 + \zeta^2 \ell(|i-j|)) \\
 &\quad - 2 \sum_{i=1}^N Z_i (\tau^2 + \zeta^2 \ell(N + \Delta - i)) + \delta^2 + \zeta^2 + \tau^2
 \end{aligned}$$

This is equation 11.2 in the main text, with  $\delta^2\delta_{ij} + \zeta^2\ell(|i - j|) = C(|i - j|)$  the covariance between data for a given risk  $|i - j|$  years apart. It is left as an exercise to the reader to verify that the formula for the mean squared error compared to the underlying mean rather than the observed value would be exactly  $\delta^2$  less.

In order to minimize this squared error, one sets the partial derivatives with respect to  $Z_i$  equal to zero. This yields the following set of  $N$  equations.

$$\begin{aligned} 2Z_i(\delta^2 + \tau^2 + \zeta^2) + \sum_{j \neq i} 2Z_j(\tau^2 + \zeta^2\ell(|i - j|)) \\ - 2(\tau^2 + \zeta^2\ell(N + \Delta - i)) \\ = 0, \quad i = 1, \dots, N \end{aligned}$$

$$\begin{aligned} \sum_{j=1}^N Z_j(\delta^2\delta_{ij} + \tau^2 + \zeta^2\ell(|i - j|)) = \tau^2 + \zeta^2\ell(N + \Delta - i), \\ i = 1, \dots, N \end{aligned}$$

This is equation 11.3 in the main text, again with

$$\delta^2\delta_{ij} + \zeta^2\ell(|i - j|) = C(|i - j|).$$

It is worth noting that equation 11.3 is very similar to the usual general matrix equation for optimal least squares credibilities:

$$\vec{Z} = \frac{\text{COV}[\vec{X}, Y]}{\text{COV}[\vec{X}, \vec{X}]}$$

where  $\vec{X}$  is the vector of observations, and  $Y$  is the quantity to be estimated.<sup>3</sup> Here in equation 11.3, there is an additional term of  $\tau^2$ , the between variance, added to the covariances. This is due to the application of the complement of credibility to the grand mean.

In the absence of shifting parameters over time ( $\zeta^2 = 0$ ), the squared error is given by:

$$V(Z) = \delta^2 \left( 1 + \sum_{i=1}^N Z_i^2 \right) + \tau^2 \left( 1 - \sum_{i=1}^N Z_i \right)^2$$

<sup>3</sup> See, for example, Theorem 3.3 in Chapter III of De Vylder [15].

The optimal credibilities are given by the solution to the equations:

$$\sum_{j=1}^N Z_j (\delta^2 \delta_{ij} + \tau^2) = \tau^2, \quad i = 1, \dots, N$$

The solution has all the credibilities equal:

$$Z_i = \frac{\tau^2}{N\tau^2 + \delta^2}, \quad i = 1, \dots, N$$

$$\sum_{i=1}^N Z_i = \frac{N\tau^2}{N\tau^2 + \delta^2} = \frac{N}{N + \delta^2/\tau^2}$$

This is the familiar expression for the least squares credibility in the absence of shifting parameters over time.

If we set  $Z_i = Z/N$  for  $i = 1, \dots, N$  then equation 11.2 becomes:

$$\begin{aligned} V(Z) = & \frac{Z^2}{N^2} \left\{ N\delta^2 + N^2\tau^2 + \zeta^2 \sum_{i=1}^N \sum_{j=1}^N \ell(|i-j|) \right\} \\ & - 2 \frac{Z}{N} \left\{ N\tau^2 + \zeta^2 \sum_{i=1}^N \ell(N + \Delta - i) \right\} + \delta^2 + \zeta^2 + \tau^2 \end{aligned}$$

Setting the derivative of  $V(Z)$  equal to zero gives the least squares credibility:

$$Z = N \frac{N\tau^2 + \zeta^2 \sum_{i=1}^N \ell(N + \Delta - i)}{N^2\tau^2 + N\delta^2 + \zeta^2 \sum_{i=1}^N \sum_{j=1}^N \ell(|i-j|)}$$

This is equation 11.4 in the main text, with  $C(|i-j|) = \delta^2 \delta_{ij} + \zeta^2 \ell(|i-j|)$ .

We can minimize  $V(Z)$  in equation 11.2, given the constraint  $\sum_{i=1}^N Z_i = 1$ , by using Lagrange Multipliers.

We set the partial derivatives with respect to  $Z_i$  of

$$V(Z) - \lambda \left( \sum_{i=1}^N Z_i - 1 \right) \text{ equal to zero.}$$

This produces the following  $N$  equations:

$$\sum_{j=1}^N Z_j(\delta^2\delta_{ij} + \zeta^2\ell(|i - j|)) = \zeta^2\ell(N + \Delta - 1) + \frac{\lambda}{2} \quad i = 1, \dots, N$$

This is equation 11.7 in the main text. It is worth noting the absence from the above equation of  $\tau^2$ , the between variance. This follows logically from the fact that the grand mean is given no weight and each risk is estimated solely from its own data.

## APPENDIX D COVARIANCE STRUCTURE

In this appendix, the covariance structure for the data sets in Tables 1 and 2 will be analyzed. As discussed in Section 11.1, the variance is the sum of three pieces, the between variance, the variance due to shifting parameters over time, and the process variance excluding the effect of shifting parameters over time. The analysis herein will define these three pieces.

Let  $X(\theta, t)$  be the observation for risk  $\theta$  at time  $t$ .

Let  $\mu(\theta, t)$  be the expected value for risk  $\theta$  at time  $t$ .

$$\mu(\theta, t) = E[X(\theta, t)].$$

$$\text{Let } \mu(\theta) = E_t[X(\theta, t)].$$

Let  $M$  be the grand mean.

$$M = E[\mu(\theta, t)] = E_\theta[\mu(\theta)].$$

In our case,  $\theta$  and  $t$  are both discrete rather than continuous variables. We can observe  $X$ .  $M$  is known since we are dealing with relativities compared to the overall average. On the other hand  $\mu(\theta, t)$  is unknown and can never be observed directly.

We can observe the squared error that results from using different estimations. This squared error can be usefully expressed in another form. To do so, we split the variance of  $X$  into various pieces. Define

$$\delta^2 = E_\theta[E_t[E[(X(\theta, t) - \mu(\theta, t))^2 | \theta, t]]]$$

$$\zeta^2 = E_\theta[E_t[(\mu(\theta, t) - \mu(\theta))^2 | \theta]]$$

$$\begin{aligned} \zeta^2 \ell(s) &= E_\theta[E_t[\text{COV}[X(\theta, t), X(\theta, t + s)] | \theta]] \\ &= E_\theta[E_t[\text{COV}[\mu(\theta, t), \mu(\theta, t + s)] | \theta]] \end{aligned}$$

$$\tau^2 = \text{VAR}_\theta[E_t[\mu(\theta, t)]] = \text{VAR}_\theta[\mu(\theta)]$$

Then  $\delta^2$  is the process variance excluding any impact of shifting risk parameters over time.  $\zeta^2$  is the variance due to shifting parameters over time.  $\ell(s)$  is a correlation measuring how much the risk parameters shift over time.  $\ell(0) = 1$ .  $\ell(s) \leq 1$  for  $s > 0$ .<sup>1</sup>  $\tau^2$  is the parameter variance, the variance between the different risks.

For later convenience of notation define

$$\delta^2(\theta, t) = E[(X(\theta, t) - \mu(\theta, t))^2 | \theta, t]$$

$$\delta^2(\theta) = E_t[\delta^2(\theta, t)]$$

$$\zeta^2(\theta) = E_t[(\mu(\theta, t) - \mu(\theta))^2 | \theta]$$

$$\ell(s, \theta) = E_t[\text{COV}[\mu(\theta, t), \mu(\theta, t + s)]] + \zeta^2(\theta)$$

then

$$\delta^2 = E_{\theta}[\delta^2(\theta)] = E_{\theta, t}[\delta^2(\theta, t)]$$

$$\zeta^2 = E_{\theta}[\zeta^2(\theta)]$$

$$\ell(s)\zeta^2 = E_{\theta}[\ell(s, \theta)\zeta^2(\theta)]$$

It is useful to rearrange the definitions of the variances in the usual manner so as to express the expected value of a quantity squared as the sum of a squared mean and a variance.

$$E[X^2(t, \theta) | t, \theta] = \mu^2(t, \theta) + \delta^2(\theta, t)$$

$$E_t[\mu^2(t, \theta)] = \mu^2(\theta) + \zeta^2(\theta)$$

$$E_{\theta}[\mu^2(\theta)] = M^2 + \tau^2$$

A similar expression can be derived from the definition of the covariance.

$$E_t[\mu(t, \theta)\mu(t + s, \theta)] = \mu^2(\theta) + \ell(s, \theta)\zeta^2(\theta)$$

For the formula for the expected value of the squared error of the estimate from the observation, one needs to express various expected values in terms of the variances and correlations defined above.

<sup>1</sup> One should note that it is an assumption that this correlation depends only upon the separation of the two years in question. Whether or not this is a reasonable approximation to reality is an empirical question which depends on the particular application.

$$\begin{aligned}
 E_{t, \theta}[X^2(t, \theta)] &= E_{\theta}[E_t[E[X^2(t, \theta)|t, \theta]]] \\
 &= E_{\theta}[E_t[\mu^2(t, \theta) + \delta^2(\theta, t)]] \\
 &= E_{\theta}[\mu^2(\theta) + \zeta^2(\theta) + \delta^2(\theta)] \\
 &= M^2 + \tau^2 + \zeta^2 + \delta^2
 \end{aligned}$$

$$\begin{aligned}
 E_{t, \theta}[X(t, \theta)X(t + s, \theta)] &= E_{\theta}[E_t[E[X(t, \theta)X(t + s, \theta)|t, \theta]]] \\
 &= E_{\theta}[E_t[\mu(t, \theta)\mu(t + s, \theta)]] \\
 &= E_{\theta}[\mu^2(\theta) + \ell(s, \theta)\zeta^2(\theta)] \\
 &= M^2 + \tau^2 + \ell(s)\zeta^2
 \end{aligned}$$

$$E_{t, \theta}[MX(t, \theta)] = ME[X(t, \theta)] = M^2$$

Then it follows that:

$$\begin{aligned}
 E_{t, \theta}[(X(t, \theta) - X(t + s, \theta))^2] &= E_{t, \theta}[X^2(t, \theta)] + E_{t, \theta}[X^2(t + s, \theta)] \\
 &\quad - 2E_{t, \theta}[X(t, \theta)X(t + s, \theta)] \\
 &= M^2 + \tau^2 + \zeta^2 + \delta^2 + M^2 + \tau^2 \\
 &\quad + \zeta^2 + \delta^2 - 2(M^2 + \tau^2 + \ell(s)\zeta^2) \\
 &= 2\delta^2 + 2\zeta^2(1 - \ell(s))
 \end{aligned}$$

$$\begin{aligned}
 E_{t, \theta}[(X(t, \theta) - X(t + s, \theta))(X(t + u, \theta) - X(t + s, \theta))] \\
 &= E_{t, \theta}[X(t, \theta)X(t + u, \theta)] + E_{t, \theta}[X^2(t + s, \theta)] \\
 &\quad - E_{t, \theta}[X(t + s, \theta)X(t + u, \theta)] - E_{t, \theta}[X(t, \theta)X(t + s, \theta)] \\
 &= M^2 + \tau^2 + \ell(u)\zeta^2 + M^2 + \tau^2 + \zeta^2 + \delta^2 - (M^2 + \tau^2 \\
 &\quad + \ell(s - u)\zeta^2) - (M^2 + \tau^2 + \ell(s)\zeta^2) \\
 &= \delta^2 + \zeta^2(1 + \ell(u) - \ell(s - u) - \ell(s))
 \end{aligned}$$

$$\begin{aligned}
 E_{t, \theta}[(X(t, \theta) - X(t + s, \theta))(M - X(t + s, \theta))] \\
 &= M^2 - M^2 + (M^2 + \tau^2 + \zeta^2 + \delta^2) \\
 &\quad - (M^2 + \tau^2 + \ell(s)\zeta^2) \\
 &= \delta^2 + \zeta^2(1 - \ell(s))
 \end{aligned}$$

$$\begin{aligned} E_{t, \theta}[(M - X(t, \theta))^2] &= M^2 - 2M^2 + (M^2 + \tau^2 + \zeta^2 + \delta^2) \\ &= \delta^2 + \zeta^2 + \tau^2 \end{aligned}$$

These results are used in Appendix C.

It is of interest to note that variance of  $X = E_{t, \theta}[(M - X(t, \theta))^2] = \delta^2 + \zeta^2 + \tau^2$ . This is the split of the variance of  $X$  into three pieces that was discussed above.

Let  $C(s) =$  Covariance for data for the same risk,  $\Delta$  years apart. Then for  $s > 0$

$$C(s) = E[(X(t, \theta) - \mu(\theta))(X(t + s, \theta) - \mu(\theta))]$$

$$\begin{aligned} C(s) &= E[X(t, \theta)X(t + s, \theta)] - E[X(t, \theta)\mu(\theta)] - E[X(t + s)\mu(\theta)] \\ &\quad + E[\mu^2(\theta)] \\ &= M^2 + \tau^2 + \ell(s)\zeta^2 - (M^2 + \tau^2) - (M^2 + \tau^2) + M^2 + \tau^2 \\ &= \ell(s)\zeta^2 \end{aligned}$$

$$\begin{aligned} C(0) &= E[(X(t, \theta) - \mu(\theta))^2] = E[X^2(t, \theta)] - 2E[X(t, \theta)\mu(\theta)] \\ &\quad + E[\mu^2(\theta)] \\ &= M^2 + \tau^2 + \zeta^2 + \delta^2 - 2(M^2 + \tau^2) + M^2 + \tau^2 \\ &= \zeta^2 + \delta^2 \end{aligned}$$

It is worth noting that the covariance structure assumed herein differs from that in Gerber and Jones [16]. The covariance structure which in Gerber and Jones is shown to give credibility formulas of the updating variety<sup>2</sup> can be written as:

$$\text{COV}[X_i, X_j] = \begin{cases} W_i & i < j \\ W_i + V_i & i = j \end{cases}$$

That covariance structure would assume for example that the covariance of the 1940 data with the data for each of the years earlier than

---

<sup>2</sup> Credibilities of the updating variety are such that new estimate = (prior estimate  $\times$  complement of credibility) + (new data  $\times$  credibility). This is the form of the estimate discussed in Section 9.1.

1940 is the same. In fact we observe that the distance between the years has an extremely significant impact on the covariance between the years.

The covariance structure assumed here can be written as:

$$\text{COV}[X_i, X_j] = \begin{cases} \ell(j-i)\zeta^2 & i < j \\ \zeta^2 + \delta^2 & i = j \end{cases}$$

Thus the optimal least squares credibilities that result from the matrix equations that are given in Appendix C will generally not be of the updating variety.<sup>3</sup>

We can directly estimate only the following quantities from the data:  $\tau^2$ ,  $C(0)$ ,  $C(1)$ ,  $C(2)$ , etc. Not coincidentally, these are the quantities that enter into the formula in Appendix C for the squared error. Thus, these are also the quantities that enter into the calculation of the optimal credibilities.

Thus, it is not necessary to estimate  $\delta^2$  by itself. However, if one does so, the values for  $\zeta^2$  and  $\ell(i)$  follow. We will estimate  $\delta^2$  here solely in order to aid our understanding; it does not affect any of the calculated values of the credibilities.<sup>4</sup>

For a binomial process, with a success rate of .4 or .6, the variance is  $.24n$ .<sup>5</sup> This is approximately the variance for the average risk in this example, with  $n = 150$ .<sup>6</sup> The resulting variance of games lost is  $(150)(.24)$ . The variance in losing percentage is  $(150)(.24)/(150)^2 = .0016$ .

Thus a reasonable approximate value for  $\delta^2$  is .0016. The values for the variances and correlations are shown in Table D1. It should be noted that as the difference in years increases, the correlations get close to zero.

For example, the observed value for the NL data for  $\delta^2 + \zeta^2 = .007892$ . Thus since we assume  $\delta^2 = .001600$ , we estimate  $\zeta^2 = .006292$ . The observed value of  $\zeta^2\ell(1) = .004919$ . Thus we estimate  $\ell(1) = .004919/.006292 = .782$ . For this example, the observed value of  $\tau^2 = .001230$ .

<sup>3</sup> They will be of the updating variety when  $\ell(s) = 1$  for all  $s$ .

<sup>4</sup> In general if something cannot be observed in the squared errors, then it is not needed to calculate the optimal least squares credibilities.

<sup>5</sup> The variance is  $p(1-p)n$ .

<sup>6</sup> Teams played about 150 games per year over this period of time.

It is important to note that the total variance of the observations is equal to  $\delta^2 + \zeta^2 + \tau^2 = .009122$ . Thus, what has been done here is just an analysis of variance, breaking the variance into its various sources. For this example, about 13.5% of the variance of the observation is due to the differences between the risks, about 17.5% is due to the process variance, and about 69.0% is due to shifting parameters over time.

One can verify that the observed pattern in the covariance structure in Table D1 is not due solely to random chance. One can rearrange the data in random fashion, and observe the covariances.

TABLE D1

### COVARIANCE STRUCTURE

|               | <u>NL</u> | <u>AL</u> |
|---------------|-----------|-----------|
| $\tau^2$      | .001230   | .001619   |
| $\delta^{2*}$ | .001600   | .001600   |
| $\zeta^{2**}$ | .006292   | .006275   |
| $\ell(0)***$  | 1.000     | 1.000     |
| $\ell(1)$     | .782      | .721      |
| $\ell(2)$     | .543      | .506      |
| $\ell(3)$     | .497      | .384      |
| $\ell(4)$     | .404      | .283      |
| $\ell(5)$     | .288      | .124      |
| $\ell(6)$     | .249      | .061      |
| $\ell(7)$     | .158      | -.016     |
| $\ell(8)$     | .062      | -.089     |
| $\ell(9)$     | -.012     | -.170     |
| $\ell(10)$    | -.063     | -.140     |

\*  $\delta^2$  estimated as .001600 based on an assumed binomial process.

\*\*  $\zeta^2$  is based on the assumed value of  $\delta^2$  and the observed value of  $\zeta^2 + \delta^2$ .

\*\*\*  $\ell(0)$  is unity by definition.

First one can rearrange the entries in each row of Table 1; for each row separately, assign each entry in that row to a randomly selected column. Similarly one can rearrange the entries in each column of Table 1; for each column separately, assign each entry in that column to a randomly selected row. The resulting covariances that are computed for these two “scrambled” data sets are shown in Table D2. All of the covariances  $\ell(i)$ ,  $i > 0$  are close to zero. Therefore, one can conclude that there is a significant pattern being displayed in Table D1.

TABLE D2

COVARIANCE STRUCTURE, SCRAMBLED DATA

|               | NL<br>Entries in<br>Each Row Rearranged | NL<br>Entries in Each<br>Column Rearranged |
|---------------|-----------------------------------------|--------------------------------------------|
| $\tau^2$      | .000191                                 | .001230                                    |
| $\delta^{2*}$ | .001600                                 | .001600                                    |
| $\zeta^{2**}$ | .007330                                 | .006292                                    |
| $\ell(0)***$  | 1.000                                   | 1.000                                      |
| $\ell(1)$     | .010                                    | -.117                                      |
| $\ell(2)$     | -.009                                   | .021                                       |
| $\ell(3)$     | .008                                    | -.070                                      |
| $\ell(4)$     | -.084                                   | -.035                                      |
| $\ell(5)$     | -.025                                   | -.039                                      |
| $\ell(6)$     | -.020                                   | -.006                                      |
| $\ell(7)$     | -.030                                   | -.053                                      |
| $\ell(8)$     | -.058                                   | .082                                       |
| $\ell(9)$     | .049                                    | .091                                       |
| $\ell(10)$    | .042                                    | -.019                                      |

\*  $\delta^2$  estimated at .001600 based on an assumed binomial process.

\*\*  $\zeta^2$  is based on the assumed value of  $\delta^2$  and the observed value of  $\zeta^2 + \delta^2$ .

\*\*\*  $\ell(0)$  is unity by definition.

## APPENDIX E

### PUTTING THE REDUCTION IN SQUARED ERROR IN CONTEXT

The first criterion used to determine the optimal credibility is to minimize the squared error. Using the optimal credibility based on this criterion will reduce the squared error between the observed and predicted result. What should be considered a significant reduction in squared error?

Let us examine an example. For the NL data set, using one year of data, the optimal credibility is 68% as shown in Table 9. As shown in Table 6 the mean squared errors are:

| <u>Z</u> | <u>Mean<br/>Squared Error</u> |
|----------|-------------------------------|
| 0        | .0091                         |
| 68%      | .0049                         |
| 100%     | .0059                         |

In this case, by the use of credibility, the squared error has been reduced from .0059 if the data were relied upon totally, or .0091 if the data were totally ignored, to .0049. In this case, the squared error has been reduced to 83% (.0049/.0059) of its previous value.<sup>1</sup>

All of these squared errors include the variation of the observed results around the expected value.<sup>2</sup> The use of credibility does not affect this source of variation. Thus credibility methods cannot reduce the squared error between the observed value and the estimated/predicted value to as great an extent as they reduce the squared error between the true mean and the estimated/predicted mean.<sup>3</sup>

It is shown in Mahler [9] that the best that can be done using credibility to combine two estimates is to halve the mean squared error between the estimated and theoretical true underlying mean. However,

<sup>1</sup> The "previous" value of the squared error is considered to be the minimum of the squared errors that result from either ignoring the data entirely or relying on the data entirely.

<sup>2</sup> This random variation is usually referred to as process risk.

<sup>3</sup> It should be noted that the former squared error is concrete and easily observed, while the latter squared error is theoretical and difficult if not impossible to observe.

in this paper the squared error being examined is between the estimated/predicted and the observed result, rather than the true underlying mean. This squared error is inherently larger due to the random variation in the observed result. Also the result derived in Mahler [9] was derived in the absence of shifting parameters over time.

It turns out that, in the current case, the best that can be done using credibility to combine two estimates is to reduce the mean squared error between the estimated and observed values to 75% of the minimum of the squared errors from either relying solely on the data or ignoring the data.<sup>4</sup> One can think of half<sup>5</sup> of the squared error as being due to two sources: the inherent process variance associated with comparing to observed results, and the presence of shifting parameters over time. This portion of the squared error is independent of the value chosen for the credibility. The remainder of the squared error can be thought of as that which is affected by the choice of the value of credibility; as stated above this can be at most cut in half by the use of credibility methods. If half of the squared error is cut in half, this reduces the total squared error to 75% of what it was.

Assume one is estimating the future by credibility weighting together a single year of data and the grand mean.<sup>6</sup> Let  $V(0)$  be the squared error between the predicted and observed results for  $Z = 0$ . Let  $V(1)$  be the squared error between the predicted and observed results for  $Z = 1$ . Then as is shown in Appendix F:

| $Z$     | Squared Error Between<br>Predicted and Observed |
|---------|-------------------------------------------------|
| 0       | $V(0)$                                          |
| Optimal | $V(1) \left( 1 - \frac{V(1)}{4V(0)} \right)$    |
| 100%    | $V(1)$                                          |

with the optimal credibility given by:  $Z \text{ optimal} = 1 - V(1)/2V(0)$ .

<sup>4</sup> When using more than two or more years of data, the reduction in squared error depends on the impact of shifting parameters over time. However, in the absence of shifting parameters over time, for  $N$  years with the same weight applied to each year, the maximum possible reduction is  $1/(2(N + 1))$ .

<sup>5</sup> This is only a half for the case when the squared errors for  $Z = 0$  and  $Z = 1$  are equal. However, this is the case when one gets the maximum reduction in squared error.

<sup>6</sup> The formula given below does not hold when using several years of data.

In the example above, we had  $V(0) = .0091$ ,  $V(1) = .0059$ . Using these values in the above formula gives  $Z$  optimal = 68%, equal to the empirically determined 68%. The formula for the minimum squared error gives a value of .0049, which is equal to the empirical minimum squared error. The reduction of the squared error to 83% of its previous value appears significant in light of the maximum possible reduction to 75%.<sup>7</sup>

---

<sup>7</sup> The maximum reduction is possible when the squared errors for  $Z = 0$  and  $Z = 1$  are equal.

## APPENDIX F

### SQUARED ERRORS

In Appendix C, the fundamental formula for the squared error was derived:

$$V(Z) = \sum_{i=1}^N \sum_{j=1}^N Z_i Z_j (\delta^2 \delta_{ij} + \tau^2 + \zeta^2 \ell(|i - j|)) \\ - 2 \sum_{i=1}^N Z_i (\tau^2 + \zeta^2 \ell(N + \Delta - i)) + \delta^2 + \zeta^2 + \tau^2.$$

One can actually check this result against the observed squared errors.<sup>1</sup> For example, let  $N = 2$  and  $\Delta = 3$ . Then

$$V(Z_1, Z_2) = Z_1^2 (\delta^2 + \tau^2 + \zeta^2) + 2Z_1 Z_2 (\tau^2 + \zeta^2 \ell(1)) \\ + Z_2^2 (\delta^2 + \tau^2 + \zeta^2) - 2Z_1 (\tau^2 + \zeta^2 \ell(4)) \\ - 2Z_2 (\tau^2 + \zeta^2 \ell(3)) + \delta^2 + \zeta^2 + \tau^2$$

Using the average of the NL and AL values in Table D1 for the covariance structure:

$$\tau^2 = .001425 \quad \delta^2 + \zeta^2 = .007884 \\ \zeta^2 \ell(1) = .004723 \quad \zeta^2 \ell(3) = .002770 \quad \zeta^2 \ell(4) = .002158 \\ V(Z_1, Z_2) = Z_1^2 (.009309) + Z_1 Z_2 (.012296) + Z_2^2 (.009309) \\ - Z_1 (.007166) - Z_2 (.008390) + .009309$$

Table F1 contains the results of the test for various values of  $Z_1$  and  $Z_2$ . ( $Z_1$  is the credibility applied to the less recent year of the two.) The mean squared errors are a close match to those given by the equation.<sup>2</sup>

<sup>1</sup> The covariances were estimated from the same data as is being used to test the equation for the squared error. Thus, the magnitude of the covariances is not being tested. However, the validity of the assumed form of the covariance structure as well as the validity of the derivation of the equation for  $V(Z)$  are being tested.

<sup>2</sup> The differences are largely due to the fact that at the two ends of the data period there are either no predictions or no actual observation to enter into the computation of an error.

When  $N = 1$ , one gets the following parabola for  $V(Z)$ :

$$V(Z) = Z^2(\delta^2 + \tau^2 + \zeta^2) - 2Z(\tau^2 + \zeta^2\ell(\Delta)) + \delta^2 + \zeta^2 + \tau^2$$

$$V(0) = \delta^2 + \tau^2 + \zeta^2 = \text{squared error ignoring the data}$$

$$V(1) = 2\delta^2 + 2\zeta^2(1 - \ell(\Delta)) = \text{squared error relying solely on the data}$$

$$Z \text{ optimal} = \frac{\tau^2 + \zeta^2\ell(\Delta)}{\tau^2 + \delta^2 + \zeta^2} = \frac{V(0) - V(1)/2}{V(0)} = 1 - \frac{V(1)}{2V(0)}$$

$$\begin{aligned} V(Z \text{ optimal}) &= -\frac{(\tau^2 + \zeta^2\ell(\Delta))^2}{\tau^2 + \delta^2 + \zeta^2} + \delta^2 + \zeta^2 + \tau^2 \\ &= -\frac{(V(0) - V(1)/2)^2}{V(0)} + V(0) \\ &= -V(0) + V(1) - \frac{V(1)^2}{4V(0)} + V(0) \\ &= V(1) \left(1 - \frac{V(1)}{4V(0)}\right) \end{aligned}$$

This is the result referred to in Appendix E. The reduction in mean squared error is greatest when  $V(1) = V(0)$ ; then the squared error is reduced to 75% of the minimum of the squared errors that result from relying solely on the data or ignoring the data.

In the absence of shifting parameters over time,<sup>3</sup> the estimate improves as one uses more and more years of data. For large  $N$ , relying solely on the data produces a very good estimate; this is reflected in the fact that the optimal credibility approaches 1 as  $N$  gets large. Thus for large  $N$ , one cannot reduce the squared error significantly by using credibility.

---

<sup>3</sup> In the presence of shifting parameters over time the situation is much more complicated.

TABLE F1  
MEAN SQUARED ERRORS (.0001)

| <u>Z<sub>1</sub></u> | <u>Z<sub>2</sub></u> | <u>Observed</u> | <u>Estimated<br/>by 2nd Order<br/>Polynomial</u> |
|----------------------|----------------------|-----------------|--------------------------------------------------|
| 0                    | 0                    | 9,182           | 9,309                                            |
| 0                    | .25                  | 7,592           | 7,793                                            |
| .25                  | 0                    | 7,963           | 8,099                                            |
| 0                    | .5                   | 7,202           | 7,441                                            |
| .15                  | .35                  | 7,087           | 7,293                                            |
| .25                  | .25                  | 7,172           | 7,352                                            |
| .5                   | 0                    | 7,949           | 8,053                                            |
| 0                    | .75                  | 8,011           | 8,253                                            |
| .25                  | .5                   | 7,581           | 7,769                                            |
| .5                   | .25                  | 7,957           | 8,057                                            |
| .75                  | 0                    | 9,140           | 9,171                                            |
| 0                    | 1                    | 10,020          | 10,228                                           |
| .25                  | .75                  | 9,189           | 9,349                                            |
| .5                   | .5                   | 9,165           | 9,260                                            |
| .75                  | .25                  | 9,947           | 9,961                                            |
| 1                    | 0                    | 11,536          | 11,452                                           |
| .75                  | .75                  | 15,162          | 15,031                                           |
| 1                    | 1                    | 25,162          | 24,667                                           |

Note: Mean Squared Errors in estimating NL and AL data.  $N = 2$ ,  $\Delta = 3$ . Estimate uses data from the fourth and third years prior to the estimation period with weights  $Z_1$  and  $Z_2$ , respectively, and the complement of credibility applied to the grand mean.  $Z_1 = 15\%$  and  $Z_2 = 35\%$  is the solution to equation 11.3 for the least squares credibility.

The exact behavior can be derived using the results of Appendix C. In the absence of shifting parameters over time ( $\zeta^2 = 0$ ), and applying equal weight  $Z/N$  to each of  $N$  years, based on the result in Appendix C, the squared error is given by:

$$V(Z) = Z^2 \left( \frac{\delta^2}{N} + \tau^2 \right) - 2Z\tau^2 + \delta^2 + \tau^2$$

$$V(0) = \delta^2 + \tau^2$$

$$V(1) = \delta^2 \left( \frac{N+1}{N} \right)$$

$$Z \text{ optimal} = \frac{N\tau^2}{N\tau^2 + \delta^2} = \frac{(N+1)V(0) - NV(1)}{(N+1)V(0) - (N-1)V(1)}$$

$$\begin{aligned} V(Z \text{ optimal}) &= \delta^2 + \tau^2 - \frac{\tau^4 N}{N\tau^2 + \delta^2} \\ &= V(1) \left( 1 - \frac{V(1)}{(N+1)^2 V(0) - (N^2 - 1)V(1)} \right) \end{aligned}$$

The maximum reduction in squared error compared to the minimum of  $V(0)$  and  $V(1)$  occurs when  $V(0) = V(1)$ . For this case

$$Z \text{ optimal} = 1/2$$

$$V(Z \text{ optimal}) = V(1) \left( 1 - \frac{1}{2(N+1)} \right)$$

As  $N$  gets large, there is no significant reduction in squared error due to using credibility (in the absence of shifting parameters over time).

## APPENDIX G

### THE SECOND CRITERION AND LIMITED FLUCTUATION CREDIBILITY

The second criterion in Section 7 deals with the probability that the observed result will be more than a certain percent different than the predicted result. The less this probability, the better the solution.

This is related to the basic concept behind "classical" credibility which has also been called "limited fluctuation" credibility [7]. In classical credibility, the full credibility criterion is chosen so that there is a probability,  $P$ , of meeting the test, that the maximum departure from expected is no more than  $k$  percent.

The reason the criterion is stated in this way rather than the way it is in classical credibility is that, unlike the actual observations, one cannot observe directly the inherent loss potential.<sup>1</sup>

However, the two concepts are closely related. If there is a small chance of the estimate differing by a large amount from the true value of the inherent loss potential, then, since the observed values are distributed about the true value, the chance of the estimate differing by a large amount from the observed value will be smaller than it would otherwise be.

For example, assume the inherent loss potential is .550 and that the observed values are distributed approximately normally with a standard deviation of .050. Then there is approximately a 95% probability that the observed value will be between .452 and .648.<sup>2</sup>

Assume the estimated values are also approximately normally distributed about the inherent loss potential.<sup>3</sup> Assume a standard deviation of .028. Then there is a 95% chance that the estimate will be between .495 and .605, i.e., within 10% of the true inherent loss potential.

---

<sup>1</sup> It has been shown that the loss potential varies for a risk over time. Thus, it cannot be estimated as the average of many observations over time.

<sup>2</sup> The mean plus or minus 1.96 standard deviations.

<sup>3</sup> An unbiased estimator has the same expected value as the inherent loss potential.

The difference between the estimated value and the observed value will also be approximately normally distributed about zero.<sup>4</sup> The standard deviation is .057.<sup>5</sup> Thus, there would be a 95% chance that the absolute difference between the estimated and observed value will be less than .112. This corresponds to about a 95% chance that the estimated value will be within  $\pm 20\%$  of the observed value.<sup>6</sup>

In a particular example, the result would depend on the relative size of the variances of the observations and the estimates. However, the smaller the variance in the estimates, the smaller the variance in the difference between the estimates and the observations. Thus the smaller the probability that the estimate and the true mean differ by a large amount, the smaller the probability that the estimate and the observation differ by a large amount.

---

<sup>4</sup> The sum or difference of two normal distributions is also a normal distribution. The new mean is the difference of the two means.

<sup>5</sup> The new variance is the sum of the two variances.

<sup>6</sup>  $.112 \div .550 = .204$ .
