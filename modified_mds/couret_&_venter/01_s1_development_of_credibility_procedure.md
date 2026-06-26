---
paper: couret_&_venter
chapter: 1
title: "1. DEVELOPMENT OF THE CREDIBILITY PROCEDURE"
topics: [buhlmann_credibility, multivariate_credibility, variance_of_hypothetical_means, expected_process_variance, covariance_matrix, injury_type_correlation, workers_compensation_classification]
key_formulas: [credibility_factor_z, vhm_estimator, epv_estimator, optimal_weight_matrix_equation]
---

> **TL;DR**
> - Injury types (Fatal, PT, Major PP, Minor PP) are positively correlated within a class; multi-dimensional credibility exploits these correlations to improve frequency estimates for each type
> - Optimal weights (b, c, d, e) for estimating class PT mean w_i solve the matrix equation C·(b,c,d,e)' = (Cov(V_i,w_i), Cov(W_i,w_i), Cov(X_i,w_i), Cov(Y_i,w_i))', where C is the covariance matrix of sample injury-type ratios to TT
> - Process variance of observed ratio W_i given true mean w_i equals σ²_W / m_i, where m_i is total TT claims — more TT exposure means lower fluctuation
> - VHM_V = (Σ m_i(V_i − V̄)² − (R−1)·EPV_V) / (m − (1/m)Σm_i²); set to 0 if negative (then all variation is attributed to process variance)
> - EPV_V = Σ_i Σ_t m_{it}(V_{it} − V_i)² / [R(N−1)]; this is process variance per unit of TT exposure

## 1. DEVELOPMENT OF THE CREDIBILITY PROCEDURE

The serious injury types have low frequencies so class claim counts are fairly unstable. What helps however is that they are correlated. The physical circumstances producing fatal, permanent total, and major permanent partial injuries are often quite similar, as slight differences in an accident can yield significantly different outcomes. Thus a class that experiences a lot of major claims is likely to have a higher-than-average propensity to produce PT and fatal claims as well. By applying multi-dimensional credibility theory, the correlations can be used to improve the estimates of each of the elements.

Credibility estimation is similar to regression in that it is a linear model fit by minimizing squared errors. Taking correlation into account is like doing a multiple regression, where the levels of several variables get different weights in estimating the outcomes. However credibility is not exactly the same as regression. Credibility estimates the (unobserved) population mean for a group, and the sample mean is one of the estimators that gets some credibility. In a regression the sample mean would be the dependent variable and the factors (coefficients) would only apply to the other variables. Credibility can be looked at as a regression for which the dependent variable (the population mean) is not observed. Instead a model is postulated about how the observed variables arise stochastically from the unobserved population mean. The data is used to estimate the parameters of that model in order to minimize the expected squared error in the estimate of the population mean. The approach below is basically an application of the methods outlined in Venter (1985).

This is based on a somewhat simplified version of credibility theory, which is outlined first. In standard credibility theory, an individual insured (policyholder or class) is assumed to have  $n$  iid observations  $X_1, \dots, X_n$  whose distribution is controlled by a parameter  $\theta$ , where  $\theta$  is an instance of a random variable  $\Theta$  with density  $\pi(\theta)$ . Define  $\mu(\theta) = E(X_j | \Theta = \theta)$  and  $v(\theta) = \text{Var}(X_j | \Theta = \theta)$ .

Often  $\mu(\theta)$  is called the hypothetical mean and  $v(\theta)$  the process variance. In classical statistics,  $\mu(\theta)$  is called the population mean, but Charles Hewitt, a Bayesian actuary, considered  $\mu(\theta)$  to be a model construct, not a truly existing entity, and so called it hypothetical, and the terminology has persisted. Let  $\mu = E\mu(\Theta)$ ,  $v = Ev(\Theta)$ , and  $a = \text{Var}[\mu(\Theta)]$ . Here  $v$  is the expected process variance and  $a$  is the variance of the hypothetical means.

The standard Bühlmann approach is to estimate  $\mu(\theta)$  linearly as  $a_0 + \sum a_j X_j$  by minimizing the expected squared error. The answer is  $a_0 = (1 - z)\mu$ ,  $a_i = z/n$  for  $j > 0$ , where  $z = n/(n + k)$ ,  $k = v/a$ . Denoting by  $X^*$  the average of the  $X_j$ , this estimates  $\mu(\theta)$  by  $zX^* + (1 - z)\mu = \mu + z(X^* - \mu) = EX^* + z(X^* - EX^*)$ .

The simplified approach is to start with the estimator  $zX^* + (1 - z)\mu$  for  $\mu(\theta)$  so only  $z$  has to be estimated. This simplification does not give up much because the best linear estimate of the mean from the observations is the sample mean. The assumptions imply  $\mu(\theta) = X^* + v(\theta)^{\frac{1}{2}}\varepsilon = \mu + a^{\frac{1}{2}}\eta$ , where  $\varepsilon$  and  $\eta$  are independent mean 0, variance 1 deviations. This can be generalized somewhat to having two estimators  $X$  and  $Y$  of  $C$  with expected squared errors  $s^2$  and  $t^2$ , respectively, where  $s$  and  $t$  might even be random variables themselves. The problem then becomes to find the  $z$  that minimizes  $E\{[C - zX + (z - 1)Y]^2\}$ .

The assumptions imply that  $X = C + s\varepsilon$ ,  $Y = C + t\eta$ . To find  $z$ , set the derivative of the expected squared error to zero. Then  $0 = E\{[C - zX + (z - 1)Y][Y - X]\} = E\{-zs\varepsilon + (z - 1)t\eta\}[t\eta - s\varepsilon] = E[zs^2\varepsilon^2 + (z - 1)t^2\eta^2] = zE[s^2] + (z - 1)E[t^2]$ . Thus  $z = E(t^2) / [E(s^2) + E(t^2)]$ .

In the credibility model  $E(s^2)$  is the expected process variance and  $t^2$  is already a constant – the variance of the hypothetical means. The general result can be expressed as  $z = [1/E(s^2)] / [1/E(s^2) + 1/E(t^2)]$  so the weight on  $X$  is proportional to the reciprocal of its variance, and similarly for  $Y$ . This is a standard statistical result.

The multivariate correlated credibility derivation below follows this approach. The class population means for the injury types are estimated as linear functions of the sample means of all the injury types for the class, and the coefficients are estimated by minimizing the expected squared error.

This procedure is applied to ratios of claims counts by injury type to TT claims counts. Denote the observed ratios for the four injury types F, PT, major, and minor as  $V$ ,  $W$ ,  $X$ , and  $Y$ . Assume that each class has parameters that determine its distribution of claim counts by injury type but since the parameters are unobserved they are considered random variables. For the  $i^{\text{th}}$  class, denote its population (or hypothetical) mean ratios as  $v_i$ ,  $w_i$ ,  $x_i$ , and  $y_i$ . These means are among the parameters that are considered random variables since they are not known.

Focusing on PT, the observed sample claim count ratio to TT,  $W$ , for class  $i$  at time  $t$ ,  $W_{it}$ , based on  $m_{it}$  TT claims, can be formulated:

$$m_{it} W_{it} = \sum_{j=1}^{m_{it}} (w_i + \varepsilon_{jt})$$

or

$$W_{it} = w_i + \left( \sum_{j=1}^{m_{it}} \varepsilon_{jt} \right) / m_{it}$$

where the  $\varepsilon_{jt}$  are independent mean-zero innovations whose standard deviation  $\sigma_{W_i}$  varies by class but not by time. This looks at each TT claim as an exposure that could produce a PT claim and sometimes does. As one possible example,  $\varepsilon_{jt}$  might be  $1 - w_i$  with probability  $w_i$  and  $-w_i$  with probability  $1 - w_i$ . This gives it mean 0 and variance  $\sigma_{W_i}^2 = w_i(1 - w_i)$ . Then every TT claim produces a random draw of 0 or 1, and the sum of these  $m_{it}$  draws is the number of PT claims  $m_{it}W_{it}$ . Then  $\text{Var}(W_{it} | w_i) = \sigma_{W_i}^2 / m_{it}$ . This is the statistical import of this formulation. The more TT claims there are, the lower the random fluctuation of the annual observed class ratio  $W_{it}$  from its mean is assumed to be.

Denote by  $W_i$  the class sample mean ratio over all the time periods (assumed independent):

$$W_i = \sum_{t=1}^N m_{it} W_{it} / \sum_{t=1}^N m_{it}$$

where there are  $N$  periods of observation, and similarly for  $V$ ,  $X$ , and  $Y$ . Let  $m_i$  denote the sum over times  $t$  of the  $m_{it}$  and  $m$  denote the sum over classes  $i$  of the  $m_i$ . Then the assumption that  $\text{Var}(W_{it} | w_i) = \sigma_{W_i}^2 / m_{it}$  implies that  $\text{Var}(W_i | w_i) = \sigma_{W_i}^2 / m_i$ .

Taking correlation into account in a linear estimate would estimate an injury-type ratio to TT for a class as a linear combination of the observations for all the injury types for that class. The simplified credibility theory uses only those estimators that are linear combinations of sample means, and looks for the linear combination that minimizes the expected squared error of the estimate. Here the expected squared error is taken across all the classes in the hazard group. For PT this can be expressed as minimizing the expected squared difference between the linear estimator and the unobserved conditional mean  $w_i$ :

$$(1) \quad \text{minimize } E[(a + bV_i + cW_i + dX_i + eY_i - w_i)^2],$$

The coefficients sought are  $a$ ,  $b$ ,  $c$ ,  $d$ , and  $e$ . Differentiating (1) wrt  $a$  gives:

$$(2) \quad a = -E(bV_i + cW_i + dX_i + eY_i - w_i).$$

Substituting this  $a$  back into  $a + bV_i + cW_i + dX_i + eY_i$  makes this estimate of  $w_i$

$$Ew_i + b(V_i - EV_i) + c(W_i - EW_i) + d(X_i - EX_i) + e(Y_i - EY_i)$$

The expectation for  $w_i$  is unconditional, so it is over all classes. If this procedure is done within a hazard group, it then estimates the hazard group mean ratio of PT to TT. Thus if the class' own data gets zero credibility, the hazard

group ratio will be used. Also the unconditional expected value of  $W_i$  is  $Ew_i$  (the conditional mean is  $w_i$ ), so  $c$  is the traditional credibility factor  $Z$ . In the traditional case, the estimation uses only class  $i$ 's own sample mean  $W_i$  so the estimator is  $Ew_i + c(W_i - EW_i) = cW_i + (1 - c)EW_i$ .

The derivative of (1) wrt  $b$  gives:

$$aEV_i + E[V_i(bV_i + cW_i + dX_i + eY_i - w_i)] = 0$$

Plugging in (2) for  $a$  then yields:

$$(-E(bV_i + cW_i + dX_i + eY_i - w_i)) EV_i + E[V_i(bV_i + cW_i + dX_i + eY_i - w_i)] = 0.$$

This can be rearranged to give:

$$(3) \quad \text{Cov}(V_i, w_i) = b \text{Var}(V_i) + c \text{Cov}(V_i, w_i) + d \text{Cov}(V_i, X_i) + e \text{Cov}(V_i, Y_i).$$

Doing the same thing for  $c$ ,  $d$ , and  $e$  will yield three more equations that look like (3), but with the variance moving over one position each time. This will end up with four equations that can be written as a single matrix equation:

$$(4) \quad \begin{pmatrix} \text{Cov}(V_i, w_i) \\ \text{Cov}(W_i, w_i) \\ \text{Cov}(X_i, w_i) \\ \text{Cov}(Y_i, w_i) \end{pmatrix} = C \cdot \begin{pmatrix} b \\ c \\ d \\ e \end{pmatrix},$$

where  $C$  is the covariance matrix of the class by injury-type sample means, which show up in (3), for instance. Thus (4) is the requirement needed for  $b$ ,  $c$ ,  $d$ , and  $e$  to be the optimal weights for estimation of  $w_i$ .

The problem becomes how to estimate the covariances needed to solve (4). The variance of  $V_i$  conditional on the true class mean  $v_i$  is  $\sigma_{V_i}^2/m_i$  where  $\sigma_{V_i}^2$  is called the process variance for  $V_i$ . The unconditional variance of  $V_i$  is  $EPV_V/m_i + VHM_V$ , where the latter term, the variance of the hypothetical means for  $V$ , is the variance across the classes of the unobserved  $V$  means  $v_i$ .  $EPV_V$  is  $E(\sigma_{V_i}^2)$ , which does not depend on  $i$  as the expectation is across all classes.

This uses the well-known formula  $\text{Var}(V_i) = E[\text{Var}(V_i|\lambda)] + \text{Var}[E(V_i|\lambda)]$ . Assuming the conditioning is on all the unobserved parameters for the class, the analogous formula for covariance is  $\text{Cov}(V_i, W_i) = E[\text{Cov}(V_i, W_i|\lambda)] + \text{Cov}[E(V_i|\lambda), E(W_i|\lambda)] = E[\text{Cov}(V_i, W_i|\lambda)] + \text{Cov}(v_i, w_i)$ . Since  $W$  is  $w_i$  plus a random innovation independent of  $w_i$ ,  $\text{Cov}(W_i, w_i)$  is  $\text{Cov}(w_i, w_i)$  which is  $VHM_W$ . Similarly,  $\text{Cov}(V_i, w_i) = \text{Cov}(v_i, w_i)$ , etc.

This model assumes that the ratios observed for any year for each type of injury by class are the class-injury means plus independent random draws. This assumption makes  $E[\text{Cov}(V_i, W_i|\lambda)]$  zero. This can be seen by expanding

$E(V_i W_i)$  and  $E(V_i)E(W_i)$  in terms of means and independent innovations. Thus  $\text{Cov}(V_i, W_i) = \text{Cov}(v_i, w_i)$  which can be estimated by the sample covariance.

Thus the off-diagonal elements of  $C$  can be estimated by the sample covariances,  $\text{Cov}(W_i, w_i)$  is  $VHM_W$  and the covariances of  $V_i$ ,  $X_i$ , and  $Y_i$  with  $w_i$  are their covariances with  $W_i$  from the sample covariance. A reasonable calculation of the sample covariance, say of  $V$  and  $W$ , would seem to be

$$\Sigma(V_i - V)(W_i - W)m_i/m = \Sigma V_i W_i m_i/m - VW.$$

The estimates of  $VHM_W$  and  $EPV_W$ , etc. needed for this are standard in credibility theory. One reference is Dean (2005) who gives the following formula for  $VHM_V$ , converted to our notation:

$$(5) \quad V\hat{H}M_V = \left( \sum_{i=1}^R m_i (V_i - V)^2 - (R-1) E\hat{P}V_V \right) / \left( m - \left( \frac{1}{m} \right) \sum_{i=1}^R m_i^2 \right).$$

Here  $V$  is the weighted average of the  $V_i$ 's using weights  $m_i$  and  $EPV$  is estimated from the sample variances for each class. This estimate can be negative, in which case it is set to 0, as then  $EPV$  accounts for all the observed variation and there is no support for individual risk differences. Also Dean (2005) gives:

$$(6) \quad E\hat{P}V_V = \frac{\sum_{i=1}^R \sum_{t=1}^N m_{it} (V_{it} - V_i)^2}{R(N-1)}.$$

Note that this is not divided by the sum of the  $m$ 's as it is the process variance per unit of exposure, which here is the TT count. The diagonal elements of  $C$  for the  $i^{\text{th}}$  class are then  $EPV_V/m_i + VHM_V$ ,  $EPV_W/m_i + VHM_W$ , etc.

