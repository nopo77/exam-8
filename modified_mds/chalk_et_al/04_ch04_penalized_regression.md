---
paper: chalk_et_al
chapter: 4
title: Penalized Regression
topics: [ridge_regression, lasso, elastic_net, bias_variance_tradeoff, lambda_tuning, feature_selection, relaxed_lasso, standardization]
key_formulas: [ridge_regression_penalty, lasso_penalty, elastic_net_penalty, lasso_soft_thresholding]
---

> **TL;DR**
> - Ridge: l_p(β) = l(β) − λΣβ_j²; shrinks coefficients toward zero but never exactly zero. LASSO: l_p(β) = l(β) − λΣ|β_j|; sets some coefficients to exactly zero (implicit feature selection). Elastic net: combination with mixing parameter α.
> - λ chosen by maximizing average k-fold CV pseudo-R²; the "1 s.e." rule accepts a simpler model within 1 standard error of the best cross-validation performance.
> - LASSO improved FAA-NTSB validation pseudo-R² from 0.140 (baseline) to 0.146 while reducing features from 89 to 57; Ridge regression stabilizes models with highly correlated features.
> - Features must be standardized (zero mean, unit variance) before penalization so that coefficient magnitudes are comparable and penalization is scale-invariant.
> - The relaxed LASSO separates feature selection (stage 1, LASSO) from coefficient estimation (stage 2, unpenalized on selected features) to eliminate unwanted shrinkage after selection.

# 4. Penalized Regression

## 4.1. Introduction

Generalized linear models (GLMs) are fitted by maximizing the likelihood on the training data. Adding an extra predictor will almost always increase the likelihood on the training data, even if it is not a useful predictor for future observations (policies sold in the future). If we fit GLMs looking only at the likelihood on the training data, we risk fitting complex models, full of useless predictors, which will be inaccurate on future data. Approaches have been developed which can be used after fitting GLMs to avoid this pitfall, for example, choosing the GLM with the lowest Akaike or Bayesian Information Criterion (AIC or BIC, respectively, see Goldburd et al. (2025) Section 6.2.2).

AIC is given by

$$AIC = -2 \times l_{model} + 2p,$$

where  $p$  is the number parameters in the model other than the intercept.<sup>13</sup> This is the equivalent of trying to make the log-likelihood on the training data ( $l_{model}$ ) as big as possible, except that for every extra parameter, there is a penalty of 1 to be deducted from the log-likelihood. Section 1.8.5 of Wood (2017) shows that AIC is an approximation of how well the model estimates the true underlying patterns—and thus models chosen by minimizing AIC will predict well on future observations not seen in the training data.

Why might models with fewer parameters perform better on future data? Consider a very rare make of car—there are only 10 of them, and each is insured with a separate private-auto insurer for one year. One of them has an accident leading to a claim, and nine do not. If each company uses a GLM on its own training data, then one of the GLMs will predict a claim frequency of 100% and nine will predict a frequency of 0%. Across all the companies, the average of the 10 GLMs is exactly correct. Where the average prediction of a model is close to the correct value across all the training sets it could have seen, we say that it has low bias. However, for each company, the GLM has fitted itself to exactly the experience of that company. This is reflected in the variance of the 10 GLM predictions,

---

<sup>13</sup> Some sources include the intercept. This would not affect the comparison of models.

which is large ( $\sigma^2 = 0.09$ ,  $\sigma = 0.30$ ). Where models fit themselves exactly to random fluctuations in the training data, we say that they have high variance. Sadly in this case, the low bias does not help any individual company—the high variance means they either give insurance away free or they charge far too much.

If the companies choose their GLMs based on AIC, the result would probably be different as AIC would encourage the separate parameter for this car to be removed. The GLMs will predict for this make; the average frequency for all makes, say, is 5%. Now the GLMs suffer from bias, since the average prediction is wrong (5% instead of 10%), but the variance of the GLM predictions for this make is 0 (since they all predict the same). In this particular case, every company is better off inasmuch as all their predictions are closer to the truth. This is because while the simpler models have more bias (except when there are redundant or unnecessary covariates in the more complex models), they suffer less from variance. The possible improvement in performance by accepting more bias in return for less variance is known as the bias-variance tradeoff.

In this chapter, we will discuss penalized regression, which also involves the application of a penalty. However, there are some key differences in the two approaches.

- The penalty in AIC and BIC alters a diagnostic produced from a fitted model but does not directly alter the model's fit. In contrast, we will see that penalized regression applies a penalty in a way that directly influences the training of the model, resulting in different parameter estimates.
- AIC and BIC penalties are based on the number of parameters in the model, encouraging simpler models with fewer features. (We typically view models with fewer features as less complex.) However, the effects of penalties in penalized regression (which will be described in the following sections) can be more subtle. While they may reduce the number of features, they can also lead to models with coefficients closer to zero. Whether a practitioner would call these models less complicated will depend on the context. We will see in Chapter 7 that penalized regression can allow us to fit very complicated models—albeit with small coefficients—in situations where non-penalized GLMs could not be fit at all. On the other hand, in the method we use in Chapter 5 to deal with nonlinear effects, smaller coefficients lead to less complicated models.
- We will see that by combining penalized regression with cross-validation we can control the balance between simple and complex models and so manage the bias-variance tradeoff.

## 4.2. Types of Penalty

### 4.2.1. Ridge regression

In penalized regression, one common penalty is the sum of the squares of the coefficients in the model. We will use  $l(\beta)$  to represent the log-likelihood of training data given the fitted model and  $l_p(\beta)$  to represent the penalized log-likelihood. Typically, the intercept,  $\beta_0$ , is not penalized. The coefficients  $(\beta_1, \beta_2, \dots, \beta_p)$  and  $\beta_0$  are now chosen to maximize

$$l_p(\beta) = l(\beta) - \lambda \sum_{j=1}^p \beta_j^2.$$

(Regarding  $\lambda$ , see the footnote.<sup>14</sup>)

This is known as "Ridge regression."  $\lambda$  is a non-negative parameter which must be chosen. If it is zero, then a normal GLM will be fit. If it is exceedingly high, then adding even one parameter with a small coefficient will not increase  $l_p$ , and a null model (i.e., an intercept-only model) will be fit.

An alternative way to express Ridge regression is that we maximize the log-likelihood subject to the constraint that the sum of the squares of the coefficients must not exceed a certain amount, i.e.,

$$\text{maximize } l(\beta) \text{ subject to } \sum_{j=1}^p \beta_j^2 \leq s.$$

If  $s$  is very large, then a normal GLM will be fit. If  $s$  is zero, then an intercept-only model will be fit (normally the intercept,  $\beta_0$ , is not included in the constraints). While this formulation is mathematically equivalent to the former, it is not generally used in practice. It does, however, emphasize how regularization controls how large the coefficients can be.

Somewhere along the spectrum between the (simple) null model and the (complicated) non-penalized GLM, might be a model which has smaller coefficients (and is potentially less complicated) and performs better on future observations due to the bias-variance tradeoff mentioned previously.

As a simple example of Ridge regression, we look at how accident frequency of aircraft decreases with age. We include only the aircraft age in the model. An unpenalized GLM (Poisson, log-link) fits the following model:

---

<sup>14</sup> Sometimes, to simplify the math,  $\frac{\lambda}{2}$  is used. Software will then just double  $\lambda$  and the sequence of fitted models will be identical.

$$\begin{aligned}\log \text{ of accident frequency} &= \beta_0 + \beta_1 \times \log \text{ of aircraft age} \\ &= -4.352 - 0.548 \times \log \text{ of aircraft age}\end{aligned}$$

Taking the exponents of both sides gives:

$$\text{accident frequency} = 0.013 \times \text{aircraft age}^{-0.548}$$

We now train penalized GLMs with various values of  $\lambda$ . Figure 4.1 shows the relationship between the  $\lambda$  parameter (when we think of the penalized likelihood) and the  $s$  parameter (when we think of the likelihood constrained by the condition that the sum of the squares of the coefficients must be less than  $s$ ). As we increase  $\lambda$ , we are in effect insisting that the sum of the squares of the coefficients must be smaller and smaller.

![Figure 4.1: A scatter plot showing the relationship between the lambda parameter (x-axis) and the sum of the squares of the coefficients (s) (y-axis). The x-axis ranges from 0.0000 to 0.0010, and the y-axis ranges from 0.200 to 0.300. The data points show a clear downward trend, indicating that as lambda increases, the sum of the squares of the coefficients decreases.](74448f9178da618d823e5a5dadc56fb5_img.jpg)

| $\lambda$ | sum of the squares of the coefficients ( $s$ ) |
|-----------|------------------------------------------------|
| 0.0000    | 0.300                                          |
| 0.0001    | 0.270                                          |
| 0.0002    | 0.265                                          |
| 0.0003    | 0.260                                          |
| 0.0004    | 0.255                                          |
| 0.0005    | 0.250                                          |
| 0.0006    | 0.245                                          |
| 0.0007    | 0.240                                          |
| 0.0008    | 0.235                                          |
| 0.0009    | 0.230                                          |
| 0.0010    | 0.225                                          |
| 0.0011    | 0.220                                          |
| 0.0012    | 0.215                                          |
| 0.0013    | 0.210                                          |
| 0.0014    | 0.205                                          |
| 0.0015    | 0.200                                          |

Figure 4.1: A scatter plot showing the relationship between the lambda parameter (x-axis) and the sum of the squares of the coefficients (s) (y-axis). The x-axis ranges from 0.0000 to 0.0010, and the y-axis ranges from 0.200 to 0.300. The data points show a clear downward trend, indicating that as lambda increases, the sum of the squares of the coefficients decreases.

**Figure 4.1. The relationship between the two different ways of looking at penalized regression. Asking for more penalization by increasing the value of  $\lambda$  is the same as insisting the the sum of the squares of the coefficients must be smaller.**

Table 4.1 shows the results from penalized regression. If  $\lambda = 0$ , then as expected we get the same result as unpenalized regression. As  $\lambda$  gets larger, the coefficient shrinks towards zero. Are any of these alternative models for how accident frequency depends on

aircraft age more accurate than our original GLM? No. The third column is the mean cross-validation pseudo- $R^2$ , and we can see that any significant amount of penalization reduces performance. In this case, there is no need for penalization to reduce model variance at the cost of increased bias because the model we are trying to fit is very simple.

**Table 4.1. The log of aircraft age coefficient for various values of  $\lambda$ . When  $\lambda = 0$ , there is no penalization and the coefficient is exactly the same as the unpenalized GLM. The third column is the mean cross-validation pseudo- $R^2$ . It can be seen that any amount of penalization reduces performance.**

| lambda | beta_1 | mean CV pseudo- $R^2$ |
|--------|--------|-----------------------|
| 0.000  | -0.548 | 0.0273                |
| 0.001  | -0.487 | 0.0270                |
| 0.002  | -0.417 | 0.0258                |
| 0.004  | -0.305 | 0.0219                |
| 0.010  | -0.182 | 0.0150                |
| 0.025  | -0.090 | 0.0079                |
| 0.064  | -0.039 | 0.0034                |
| 0.163  | -0.016 | 0.0012                |
| 0.414  | -0.006 | 0.0003                |
| 1.049  | -0.003 | -0.0001               |
| 3.192  | -0.001 | -0.0003               |

Ridge regression has other benefits besides performance. In the presence of highly correlated features, an unpenalized GLM will either fail to fit at all or the coefficients will be unstable. By "unstable" we mean that small changes in the training data can lead to large changes in coefficients. We will see in Chapter 7 that Ridge regression solves this problem.

### 4.2.2. LASSO

Another common penalty is the sum of the absolute values of the coefficients in the model (excluding the intercept). The coefficients  $(\beta_1, \beta_2, \dots, \beta_p)$  and the intercept  $\beta_0$  are chosen to maximize

$$l_p(\beta) = l(\beta) - \lambda \sum_{j=1}^p |\beta_j|.$$

This penalty is known as the LASSO<sup>15</sup> and was proposed by Tibshirani (1996).

Table 4.2 shows the results of the LASSO on our simple FAA-NTSB model, where the accident frequency depends only on aircraft age. Once again, when  $\lambda = 0$ , as expected we get the same result as unpenalized regression. However, once  $\lambda$  gets large enough, the coefficient becomes exactly zero—it is removed from the model.

**Table 4.2. The log of aircraft age coefficient for various values of  $\lambda$ . When  $\lambda = 0$ , there is no penalization and the coefficient is exactly the same as the unpenalized GLM. When  $\lambda$  gets large enough, the parameter is set to exactly zero (i.e., removed from the model).**

| $\lambda \times 10^{-3}$ | beta_1 |
|--------------------------|--------|
| 0.0000                   | −0.548 |
| 0.0279                   | −0.542 |
| 0.1487                   | −0.517 |
| 0.9561                   | −0.352 |
| 2.4240                   | −0.050 |
| 3.1925                   | 0      |

The shrinking of coefficients to exactly zero—effectively removing them from the model if  $\lambda$  is large enough—is a feature of the LASSO. It will happen if the benefit—when measured in a certain way—of including a feature in the model is less than a threshold controlled by the value of  $\lambda$ . Hence, as  $\lambda$  increases, more features will be removed from the model. For a given set of features and a value of  $\lambda$  the LASSO will select nonzero coefficients for the subset of features which are most beneficial to the predictive power of the model and will effectively exclude all the other features. Selecting some of the features and leaving out others is known as "feature selection." The fact that the LASSO does this itself during training and does not require the user to choose which features to include or exclude is known as "implicit" feature selection.

The LASSO is especially useful for datasets which have many features but only some of which are predictive. It will create a model with good performance while keeping it simple by excluding unhelpful features. The feature selection aspect of the LASSO will also work in the presence of highly correlated features but may not be stable, i.e., the features that it selects may differ with only small changes to the training data.

<sup>15</sup> The acronym stands for "least absolute shrinkage and selection operator." Tibshirani chose these letters to form the word "lasso," which has connotations of shrinkage and selection, and as a gentler alternative to "garotte," a term used by Leo Breiman for a related idea that inspired his work.

### 4.2.3. Elastic net

Zou and Hastie (2005) proposed a penalty which is a combination of Ridge regression and the LASSO, leading to

$$l_p(\beta) = l(\beta) + \lambda \left( (1 - \alpha) \frac{1}{2} \sum_{j=1}^p \beta_j^2 + \alpha \sum_{j=1}^p |\beta_j| \right).$$

This is known as "elastic net."  $\alpha$  takes any value in the range  $[0, 1]$  and needs to be chosen. If  $\alpha = 1$ , this simplifies to the LASSO, and if  $\alpha = 0$ , this simplifies to Ridge regression.

We have discussed above that both Ridge regression and the LASSO can improve performance through use of the bias-variance tradeoff. In addition, Ridge regression helps fit stable models where our data contain highly correlated features, and the LASSO helps fit simple models in the presence of large numbers of unhelpful features. Where our datasets suffer from both issues, we can therefore consider the elastic net. From a practical perspective, given the risk that models with the LASSO penalty might be unstable, practitioners will often use elastic net with  $\alpha = 0.99$  rather than the LASSO, even when the focus is purely on feature selection.

## 4.3. Choosing $\lambda$ Using k-Fold Cross-Validation

In Ridge regression, or LASSO or elastic net, the optimal amount of penalization (i.e.,  $\lambda$ ) needs to be chosen. Given that the aim is to find the model which performs best on data which is not in the training data, we will use k-fold cross-validation, as described in Section 3.2.

We divide the data into  $k$  folds (partitions). In our case, we have seven folds labeled 1, 2, ..., 7. We remove the fold 1 and train the penalized regression model on folds 2–7. We don't know which value of  $\lambda$  to use, so we choose a sequence of (typically) 100 values of  $\lambda$ , ranging from a high value (which will tend to shrink all the coefficients to close to zero, leaving us with an intercept-only model) to a very low value of  $\lambda$  (low enough to give a result close to a non-penalized GLM). We now measure the performance (pseudo- $R^2$ ) for the models, one for each value of  $\lambda$ , on fold 1.

We apply this approach to the very simple case where the only feature is aircraft age. Figure 4.2 shows the pseudo- $R^2$  measured on fold 3 for the models trained on folds 1, 2, and 4–7. (The x-axis uses  $\log(\lambda)$  rather than  $\lambda$  simply to space out the lambdas.) We can see that starting from the left of the x-axis, as  $\lambda$  increases, the performance on validation data first improves slightly and then decreases. This suggests that some penalization is useful in this case.

![Figure 4.2: A line graph showing the performance of a model trained on folds 1, 2, and 4-7 as measured on fold 3. The x-axis is labeled 'log(lambda)' and ranges from -8 to 0. The y-axis is labeled 'pseudo-R^2 on fold 3' and ranges from 0.00 to 0.04. The curve starts at approximately (log(lambda) = -8, pseudo-R^2 = 0.004), rises to a peak of about 0.007 at log(lambda) = -5.5, and then gradually declines towards 0.00 as log(lambda) increases towards 0.](f2c40bfbb63eaf7fd84888bdbf1a0a51_img.jpg)

Figure 4.2: A line graph showing the performance of a model trained on folds 1, 2, and 4-7 as measured on fold 3. The x-axis is labeled 'log(lambda)' and ranges from -8 to 0. The y-axis is labeled 'pseudo-R^2 on fold 3' and ranges from 0.00 to 0.04. The curve starts at approximately (log(lambda) = -8, pseudo-R^2 = 0.004), rises to a peak of about 0.007 at log(lambda) = -5.5, and then gradually declines towards 0.00 as log(lambda) increases towards 0.

**Figure 4.2. Performance of a model trained on folds 1, 2, and 4–7 as measured on fold 3. The x-axis uses  $\log(\lambda)$  rather than  $\lambda$  simply to space out the lambdas which are created using an exponential scale. Starting from the left of the x-axis (low penalization), performance first improves slightly as penalization increases and then gets worse. The optimal amount of penalization is at  $\log \lambda = -5.5$ .**

However, performance might vary for models trained and validated on different folds. We therefore repeat this exercise seven times, for example, training the model on folds 1, 3, 4, ..., 7 and then validating on fold 2, and then similarly for the other folds. Figure 4.3 shows the seven results—it can be seen that the results are different for each fold.

We therefore take the average performance across the folds for each value of  $\lambda$ . We can now see (Figure 4.4) that on average the validation performance gets worse as we increase penalization and, for this simple model, the optimal about penalization is zero.<sup>16</sup>

We have thus used k-fold cross-validation for choosing the optimal value for  $\lambda$ .

<sup>16</sup> It has been pointed out to the authors—many times—that a graph showing a case where there is no benefit to penalization is not the best way to introduce the reader to the benefits of penalization. However, even here there is a benefit of sorts—we know that the most complex model is the best performing model and that we are not overfitting the data.

![Figure 4.3: A line graph showing validation performance (pseudo-R^2 on validation folds) versus log(lambda) for seven different folds. The x-axis ranges from -8 to 0, and the y-axis ranges from 0.00 to 0.04. Seven curves are plotted, all showing a general downward trend as log(lambda) increases. The curves are relatively flat for negative log(lambda) values and then drop sharply as log(lambda) approaches 0.](734487b0336ba703328f4484af34e77d_img.jpg)

The graph displays seven individual validation curves. The y-axis is labeled 'pseudo-R^2 on validation folds' and ranges from 0.00 to 0.04. The x-axis is labeled 'log(lambda)' and ranges from -8 to 0. The curves start at various points on the y-axis (approximately 0.005 to 0.035) at log(lambda) = -8 and generally decrease as log(lambda) increases, converging towards 0.00 as log(lambda) approaches 0.

Figure 4.3: A line graph showing validation performance (pseudo-R^2 on validation folds) versus log(lambda) for seven different folds. The x-axis ranges from -8 to 0, and the y-axis ranges from 0.00 to 0.04. Seven curves are plotted, all showing a general downward trend as log(lambda) increases. The curves are relatively flat for negative log(lambda) values and then drop sharply as log(lambda) approaches 0.

**Figure 4.3. Validation performance for each of the seven folds. Though the validation curves mostly convey the same message—that for this simple model less penalization is better—the individual curves are different. We therefore take the average of these curves rather than rely on validation performance of one particular fold.**

![Figure 4.4: A line graph showing average validation performance versus log(lambda). The x-axis ranges from -8 to 0, and the y-axis ranges from 0.00 to 0.04. A single curve is plotted, showing a smooth, decreasing trend as log(lambda) increases. The curve is relatively flat for negative log(lambda) values and then drops sharply as log(lambda) approaches 0.](068b3a3247570c4b78342a943f15de9e_img.jpg)

The graph shows the average validation performance across the seven folds. The y-axis is labeled 'average validation performance' and ranges from 0.00 to 0.04. The x-axis is labeled 'log(lambda)' and ranges from -8 to 0. The curve starts at approximately 0.02 at log(lambda) = -8 and decreases smoothly, reaching 0.00 as log(lambda) approaches 0.

Figure 4.4: A line graph showing average validation performance versus log(lambda). The x-axis ranges from -8 to 0, and the y-axis ranges from 0.00 to 0.04. A single curve is plotted, showing a smooth, decreasing trend as log(lambda) increases. The curve is relatively flat for negative log(lambda) values and then drops sharply as log(lambda) approaches 0.

**Figure 4.4. Average performance across the seven folds. The model with the best average validation performance is the model with no penalization (see footnote).**

## 4.4. Case Study—Penalized Regression

In Section 3.5 we saw that the validation performance of a GLM on the FAA-NTSB data was 0.140. We now train penalized GLMs to see if we can improve performance by using the bias-variance tradeoff or if we can benefit from the feature selection aspect of the LASSO. (For the purpose of exposition, in this monograph we first fitted a non-penalized GLM and then moved to a penalized model. Penalized regression software typically returns models representing GLMs for a range of  $\lambda$ s which include a model close to an unpenalized GLM. Therefore, it is unlikely that, in practice, a practitioner would ever need to run a separate unpenalized regression model.)

In order to investigate potential performance improvement and feature selection, we trained three models: Ridge regression, elastic net with  $\alpha = 0.5$ , and the LASSO. (As mentioned above, rather than the LASSO we actually use an elastic net with  $\alpha = 0.99$  to encourage model stability.) In terms of performance, the three penalized models were similar, showing only a very small improvement over the unpenalized GLM. However, the LASSO does benefit from feature selection, and we discuss its results.

Figure 4.5 shows the validation performance for each fold. Some of the curves are slightly upward sloping to begin with, suggesting a small performance improvement for small penalization.

![Figure 4.5: A line graph showing pseudo-R^2 on the seven validation folds versus the regularization parameter lambda. The y-axis is labeled 'pseudo-R^2 on the seven validation folds' and ranges from 0.00 to 0.15. The x-axis is labeled 'lambda' and has tick marks at 2e-05, 0.00012, and 0.00091. There are seven curves representing different folds. Most curves start at a pseudo-R^2 of approximately 0.14 for small lambda and decrease as lambda increases. One curve starts slightly higher and decreases more gradually, while another starts slightly lower and decreases more sharply. All curves converge towards a pseudo-R^2 of 0.00 as lambda increases beyond 0.00091.](07c5a1c0fddd7da92a8427f5af840ffa_img.jpg)

Figure 4.5: A line graph showing pseudo-R^2 on the seven validation folds versus the regularization parameter lambda. The y-axis is labeled 'pseudo-R^2 on the seven validation folds' and ranges from 0.00 to 0.15. The x-axis is labeled 'lambda' and has tick marks at 2e-05, 0.00012, and 0.00091. There are seven curves representing different folds. Most curves start at a pseudo-R^2 of approximately 0.14 for small lambda and decrease as lambda increases. One curve starts slightly higher and decreases more gradually, while another starts slightly lower and decreases more sharply. All curves converge towards a pseudo-R^2 of 0.00 as lambda increases beyond 0.00091.

**Figure 4.5. FAA-NTSB elastic net ( $\alpha = 0.99$ ) on features excluding HCCVs. The performance on each fold is slightly different but at least some of them show a small benefit for some level of penalization.**

Figure 4.6 shows the average validation performance across all the folds. The dashed vertical line is at the best performance—0.146—which is better than the baseline model (0.140). The numbers along the top are a count of the variables with nonzero coefficients. The best LASSO model benefits from having only 57 nonzero parameters compared to 89 in the non-penalized GLM previously fitted. (We actually gave the penalized regression model 105 features as we did not need to exclude collinear features. In addition, for every categorical variable we gave it a separate feature for each category, whereas in the non-penalized GLM we excluded the most frequently occurring category.)

![Figure 4.6: A plot showing the average pseudo-R^2 performance across all folds for the FAA-NTSB elastic net model with alpha = 0.99. The x-axis is log(lambda) ranging from -11 to -5. The y-axis is pseudo-R^2 ranging from 0.00 to 0.15. A dashed vertical line at log(lambda) ≈ -9.5 marks the 'max' performance point. Above the x-axis, the number of nonzero coefficients is listed for each log(lambda) value: 94, 88, 81, 67, 57, 52, 36, 28, 15, 6, 2, 2, 0. The performance is relatively stable until log(lambda) ≈ -9.5, after which it drops sharply.](9857175bc98d86591d24a161fe615f12_img.jpg)

| log( $\lambda$ ) | Number of nonzero coefficients | pseudo- $R^2$ |
|------------------|--------------------------------|---------------|
| -11.0            | 94                             | 0.145         |
| -10.5            | 88                             | 0.145         |
| -10.0            | 81                             | 0.145         |
| -9.5             | 67                             | 0.145         |
| -9.0             | 57                             | 0.146 (max)   |
| -8.5             | 52                             | 0.145         |
| -8.0             | 36                             | 0.144         |
| -7.5             | 28                             | 0.142         |
| -7.0             | 15                             | 0.135         |
| -6.5             | 6                              | 0.115         |
| -6.0             | 2                              | 0.085         |
| -5.5             | 2                              | 0.065         |
| -5.0             | 0                              | 0.045         |
| -4.5             | 0                              | 0.025         |
| -4.0             | 0                              | 0.015         |
| -3.5             | 0                              | 0.005         |
| -3.0             | 0                              | 0.000         |

Figure 4.6: A plot showing the average pseudo-R^2 performance across all folds for the FAA-NTSB elastic net model with alpha = 0.99. The x-axis is log(lambda) ranging from -11 to -5. The y-axis is pseudo-R^2 ranging from 0.00 to 0.15. A dashed vertical line at log(lambda) ≈ -9.5 marks the 'max' performance point. Above the x-axis, the number of nonzero coefficients is listed for each log(lambda) value: 94, 88, 81, 67, 57, 52, 36, 28, 15, 6, 2, 2, 0. The performance is relatively stable until log(lambda) ≈ -9.5, after which it drops sharply.

**Figure 4.6. FAA-NTSB elastic net ( $\alpha = 0.99$ ) on features excluding HCCVs. Average pseudo- $R^2$  performance across all the folds. The dashed vertical line is at the best performance.**

Previously (Table 3.6) we saw the non-penalized regression coefficients. In Table 4.3 we compare them with the coefficients of our LASSO model. `type_registrant9` and `type_registrant4` which had high  $p$ -values in the non-penalized model have been penalized out completely. Other levels of `type_registrant` remain in the model, but we can see shrinkage (towards zero), which is generally greater when the  $p$ -values in the non-penalized model were high.

In the above case, the benefit of the LASSO was mainly its implicit feature selection (although there was a small performance benefit). In some cases, there can be clearer performance benefits. For example, Figure 4.7 shows the cross-validation results for the simulation case study. It can be seen that, starting from very low levels of penalization (on the left), performance improves as penalization increases, but then decreases.

**Table 4.3. A comparison of the fitted coefficients of an unpenalized regression and the LASSO. type\_registrant9 and type\_registrant4 which had high  $p$ -values have been penalized out of the model. Other levels of this category remain in the model, but we can see shrinkage (towards zero).**

|                  | unpenalized coefficient | $\Pr(> t )$ | LASSO coefficient |
|------------------|-------------------------|-------------|-------------------|
| type_registrant2 | -0.375                  | 0.2628      | -0.194            |
| type_registrant3 | 0.410                   | 0.0000      | 0.392             |
| type_registrant4 | 0.086                   | 0.6987      | .                 |
| type_registrant5 | 0.378                   | 0.0685      | 0.288             |
| type_registrant7 | 0.425                   | 0.0000      | 0.390             |
| type_registrant8 | -0.072                  | 0.8563      | 0.048             |
| type_registrant9 | -12.756                 | 0.9958      | .                 |

![Figure 4.7: A plot showing the pseudo-R^2 value versus log(lambda) for an elastic net model with alpha = 0.99. The x-axis is labeled 'log(lambda)' and ranges from -9 to -4. The y-axis is labeled 'pseudo-R^2' and ranges from 0.000 to 0.020. The plot shows a series of red dots forming a curve that rises to a peak and then falls. A vertical dashed line is drawn at log(lambda) = -6, labeled 'max'. Above the x-axis, there are labels for the number of non-zero coefficients in the model: 43, 42, 39, 37, 28, 25, 14, 13, 6, 3, 2, 0. The curve starts at approximately (log(lambda) = -9, pseudo-R^2 = 0.008), rises to a peak of about 0.022 at log(lambda) = -6, and then falls to about 0.001 at log(lambda) = -4.](9f92854fe6ecaf47760515c891a4fccc_img.jpg)

Figure 4.7: A plot showing the pseudo-R^2 value versus log(lambda) for an elastic net model with alpha = 0.99. The x-axis is labeled 'log(lambda)' and ranges from -9 to -4. The y-axis is labeled 'pseudo-R^2' and ranges from 0.000 to 0.020. The plot shows a series of red dots forming a curve that rises to a peak and then falls. A vertical dashed line is drawn at log(lambda) = -6, labeled 'max'. Above the x-axis, there are labels for the number of non-zero coefficients in the model: 43, 42, 39, 37, 28, 25, 14, 13, 6, 3, 2, 0. The curve starts at approximately (log(lambda) = -9, pseudo-R^2 = 0.008), rises to a peak of about 0.022 at log(lambda) = -6, and then falls to about 0.001 at log(lambda) = -4.

**Figure 4.7. Simulation case study elastic net ( $\alpha = 0.99$ ). The LASSO provides not only implicit feature selection, but also a performance benefit compared to a non-penalized model.**

In other cases, there will be no performance benefit from penalization. The driving factors are the complexity of the model and the size of the dataset. As the size of the dataset increases, more complex unpenalized models can be fit with limited risk of overfitting. While we can describe this tradeoff in general, we cannot know without checking whether overfitting is happening, and therefore using average cross-validation performance (or similar methods) to check is required.

At each level of penalization, the parameters fit are different. Understanding how the parameters change as penalization increases can be useful, and we discuss this further in Chapter 7, Section 7.4.4.

Above, based on Figure 4.6, we selected the model with the best cross-validation performance and with 57 nonzero parameters. We can see that performance is quite flat over a wide range of penalty sizes, and an even simpler model could have been chosen for barely any performance reduction. If model simplicity is important to us, we might accept a small performance degradation in exchange for a less complex model. We should also remember that average cross-validation error (calculated by taking the mean across all the folds) is only an estimate of the generalization error—we don't know the exact value. Hence, the true generalization error of what we took to be the best model might in any case be less than the maximum cross-validation performance. We discuss this further in Section 4.6.5.

## 4.5. The Relaxed LASSO

In our case study above, the LASSO had two effects. It removed some features completely from the model. For example, it set the coefficient for `type_registrant9` (Non-Citizen Co-Owned) to exactly zero. In addition, for all other features left in the model, their fitted parameters were smaller in absolute value than they would have been in a non-penalized regression (using the same nonzero features). For example, the linear predictor for aircraft age is shrunk toward zero; from  $-0.791$  in the unpenalized model to  $-0.731$  in the LASSO.

In general, when using the LASSO, each feature will either be set to exactly zero or will be reduced in absolute value by an amount regulated by  $\lambda$  (see Section 4.7.3 for a proof of this in a simple case). This effect is known as soft-thresholding. An alternative to soft-thresholding is hard-thresholding, where, if the coefficients are not set to zero, they are left at their original values. Figure 4.8 illustrates the difference.

To illustrate an extreme example, we show in Table 4.4 the coefficients in our FAA-NTSB model for a fairly high value of  $\lambda$ , only five out of 105 features have been selected. The table also shows coefficients from fitting an unpenalized model using only the five chosen features, and the final column shows the difference between the penalized and unpenalized coefficients (i.e., the shrinkage).

![Figure 4.8: A line graph comparing soft-thresholding and hard-thresholding. The x-axis is labeled β and ranges from -3 to 3. The y-axis is labeled 'Thresholded value' and ranges from -3 to 3. The legend indicates that the red line represents 'soft_thresholding' and the teal line represents 'hard_thresholding'. The soft-thresholding line is a continuous V-shape that passes through the origin (0,0). The hard-thresholding line is zero for β between -1 and 1, and then increases or decreases linearly with a slope of 1 for |β| > 1.](49281e6ec325a21f4b1574ad0851fea3_img.jpg)

Figure 4.8: A line graph comparing soft-thresholding and hard-thresholding. The x-axis is labeled β and ranges from -3 to 3. The y-axis is labeled 'Thresholded value' and ranges from -3 to 3. The legend indicates that the red line represents 'soft\_thresholding' and the teal line represents 'hard\_thresholding'. The soft-thresholding line is a continuous V-shape that passes through the origin (0,0). The hard-thresholding line is zero for β between -1 and 1, and then increases or decreases linearly with a slope of 1 for |β| > 1.

**Figure 4.8. Soft-thresholding compared to hard-thresholding. In hard-thresholding, the coefficient drops suddenly to zero. In soft-thresholding, when the coefficient is not zero, it is still shrunk towards zero so the transition is smoother.**

**Table 4.4. For a fairly high value of  $\lambda$ , only five features are selected. The LASSO column shows the shrunk coefficients. The unpenalized column shows the fitted coefficients, where the selected features are fitted in an unpenalized model; the unpenalized values are significantly higher. There is no reason to assume that the shrunk coefficients will provide the best performing model for a model with only these five features.**

| var              | coefficients |                 |                   |
|------------------|--------------|-----------------|-------------------|
|                  | LASSO (a)    | unpenalized (b) | shrinkage (b – a) |
| type_registrant3 | 0.320        | 0.545           | 0.225             |
| region2          | −0.070       | −1.194          | 1.124             |
| regionC          | −0.093       | −1.138          | 1.045             |
| faa_eng_type11   | 0.299        | 3.716           | 3.417             |
| veh_age          | −0.003       | −0.071          | 0.069             |

If we choose to use this simple model—with only five features—there is no reason to assume that the best validation performance is with the amount of shrinkage shown. And, in general, there is no guarantee that the penalized model which selects the best subset of features will also fit coefficients for the selected features which are best for model performance. In terms of the bias-variance tradeoff, once the LASSO has selected the features to include, the continued penalization of the remaining coefficients might be adding extra bias without reducing the variance.

One alternative is to allow those features whose coefficients are shrunk to exactly zero to be removed from the model but choosing the unpenalized coefficients for the other features. This is an example of hard-thresholding discussed above.

The relaxed LASSO (Meinshausen (2007)) allows for the above approach. It splits model training into two separate parts. In the first stage, feature selection is achieved. In the second stage, shrinkage is considered. It allows for hard-thresholding (i.e., no shrinkage in the second stage), but it also allows for some shrinkage to be chosen. Running the relaxed LASSO and comparing the CV performance curves allows the practitioner to benefit from feature selection while still ensuring optimal model performance.

## 4.6. Practically Speaking

### 4.6.1. Software

A pricing department, which has so far been limited to unpenalized regression and wishes now to use penalized regression, will need to choose a software. We used one or two standard open-source software<sup>17</sup> to carry out the analyses in this monograph. However, there are many open-source and proprietary software tools available for fitting penalized regression and other types of model, and the choice is not simple. Factors to consider go far beyond the ability of the software to actually fit a model and are beyond the scope of this monograph.

### 4.6.2. How many models?

Software used to train penalized regression models will often fit models for a sequence of  $\lambda$ s from high to low, in order to be able cover in detail the full range of models from simple intercept-only models to models with (almost) no penalization. Typically, models for 100 values of  $\lambda$  may be fitted. If we are using cross-validation with 10 folds, then 100 models will be fitted for each fold, and in addition 100 models for the full path of  $\lambda$ s will be fit on the complete training data from which the final model will be chosen. Hence 1,100 models will be fitted. This is not as bad as it sounds because given a sequence of  $\lambda$ s, the models are fitted in the order of most penalized first. This means that, mostly, for any

---

<sup>17</sup> R and Python.

model in the sequence, the coefficient for a feature will be just slightly bigger than it was in the previous model in the sequence. Therefore, the initial estimate of the coefficients for a given  $\lambda$  can start from the final estimated coefficients of the previous  $\lambda$  in the sequence. These are called "warm starts." Friedman et al. (2010) mention that there are actually examples where it was faster to compute the whole path starting with the largest value  $\lambda$  down to a small value of  $\lambda$  than the solution only at that small value of  $\lambda$ . In addition, the models for the different folds can be done in parallel on different CPU cores. Overall, the speed of finding the coefficients for all the models will depend on the hardware, how well the software uses the hardware, and also the various technical tricks that the algorithm uses to reduce the memory footprint and speed up the calculations.

For this exercise, our training dataset had about 2 million observations, and the open-source software we were using took approximately 40 minutes to fit all the models. On the same hardware, an alternative open-source software took many hours. Hence, if using open-source software, it is important to experiment with the different choices available.

### 4.6.3. Penalization parameter names— $\lambda$ and $\gamma$

Amongst different software and academic papers, there is not always consistency in the Greek letter used to represent the penalization parameter. Common choices are  $\lambda$  or  $\gamma$ . In the software we used, the penalization parameter is represented by  $\lambda$ , and the elastic net mixing parameter is represented by  $\alpha$ . We have done the same here. When using a new software, it is best to check the documentation rather than making assumptions.

### 4.6.4. Performance graphs—x-axis

The x-axis of our performance graphs displays  $\log(\lambda)$ . When there is little or no penalization,  $\lambda$  approaches zero, making  $\log(\lambda)$  negative. Consequently, models with minimal or no penalization—which are the more complex models—appear on the left side of the graph, while simpler models appear on the right.

### 4.6.5. Choosing $\lambda$

We discussed above that in Figure 4.6, performance is quite flat over a wide range of penalty sizes and that we might accept a small performance degradation in exchange for a less complex model.

Generalization error is the expected performance of a model trained on our training data over future data that it has not yet seen. In all of our work, we use the mean cross-validation error as an estimate of the generalization error. Whenever we use a sample mean as an estimate, we can measure the uncertainty of this estimate by its standard error. In our work, the mean is over the seven partitions we created. For any value of  $\lambda$ , we can calculate the standard deviation (s.d.) of the seven values of pseudo- $R^2$  and

hence the standard error of the sample mean ( $\frac{s.d.}{\sqrt{7}}$ ). In an early work on decision trees Breiman et al. (1984), there is a proposal that we should take the simplest model whose performance is within one standard error of the model with the best cross-validation performance. This approach was included as default in one of the early penalized regression software, and we demonstrate it in Figure 4.9. Each red dot is the average cross-validation performance for a given amount of penalization. The error bars show 1 standard error around these means. The best cross-validation performance less 1 s.e. (standard error) is 0.142, and a dashed horizontal line has been drawn at this level. Finally, the vertical line labeled "1 s.e." is at the simplest model whose cross-validation performance is 0.142 or more. Breiman et al. (Section 3.4.3) say that in a way, this model "has an accuracy comparable to" the model with the maximum cross-validation performance.

![Figure 4.9: A plot showing pseudo-R^2 versus log(lambda) for cross-validation performance. The x-axis is log(lambda) ranging from -11 to -5. The y-axis is pseudo-R^2 ranging from 0.07 to 0.15. Red dots with error bars represent the average cross-validation performance for different levels of penalization. A dashed horizontal line at pseudo-R^2 = 0.142 indicates the best performance minus 1 standard error. A vertical dashed line labeled '1 s.e.' is at log(lambda) ≈ -9.5. The top of the plot shows the number of non-zero coefficients in the model, decreasing from 94 on the left to 0 on the right as lambda increases.](fe6af03ab7804980cff28a06241be192_img.jpg)

Figure 4.9: A plot showing pseudo-R^2 versus log(lambda) for cross-validation performance. The x-axis is log(lambda) ranging from -11 to -5. The y-axis is pseudo-R^2 ranging from 0.07 to 0.15. Red dots with error bars represent the average cross-validation performance for different levels of penalization. A dashed horizontal line at pseudo-R^2 = 0.142 indicates the best performance minus 1 standard error. A vertical dashed line labeled '1 s.e.' is at log(lambda) ≈ -9.5. The top of the plot shows the number of non-zero coefficients in the model, decreasing from 94 on the left to 0 on the right as lambda increases.

**Figure 4.9. Choosing a model with a cross-validation performance within 1 s.e. of the best cross-validation performance. The error bars show 1 s.e. around the mean cross-validation for each level of penalization. The dashed horizontal line at 0.142 is at 1 s.e. below the best cross-validation performance. The simplest model whose performance is at or above this level is at the dashed line labeled "1 s.e."**

The above approach should not be used mindlessly (and Breiman et al. certainly did not). It is introduced only to show the thought process which is available to us now that we have available a trade-off between performance and complexity. We can get further insight into this trade-off by comparing the average cross-validation error (which has been our focus until now) with the average training error. Figure 4.10 shows that for simpler

models (to the right of the x-axis) training and cross-validation performance are the same. As models start to become more complex, training performance increases slightly more quickly than cross-validation performance as models begin to pick up some random elements of the training data. At this stage, fitted parameters start to reflect effects in the training data which are not present in the validation data. At the "1 s.e." model the gap is quite small. At the "max" model the gap has widened; based on cross-validation performance, the fitted parameters still predict the better overall. However, it is possible that based on other unseen data, the extra noise picked up might reduce performance. This is a further incentive to choose a simpler model than the "max" model.

![Figure 4.10: A line graph showing training and validation performance versus log(lambda). The x-axis is labeled log(lambda) with values -11, -9, and -7. The y-axis is labeled performance with values 0.00, 0.05, 0.10, and 0.15. The training performance curve (red) starts at approximately 0.155 and decreases to 0.00. The validation performance curve (teal) starts at approximately 0.145, peaks at approximately 0.145 at log(lambda) = -9, and then decreases to 0.00. The gap between the training and validation curves widens as log(lambda) increases. Vertical dashed lines mark the 'max' model at log(lambda) = -9 and the '1 s.e.' model at log(lambda) = -8.5. Above the x-axis, a series of numbers (94, 88, 81, 67, 57, 52, 36, 28, 15, 6, 2, 2, 0) are aligned with the x-axis ticks.](3c47f29e8e1963959009844c7f3ee025_img.jpg)

Figure 4.10: A line graph showing training and validation performance versus log(lambda). The x-axis is labeled log(lambda) with values -11, -9, and -7. The y-axis is labeled performance with values 0.00, 0.05, 0.10, and 0.15. The training performance curve (red) starts at approximately 0.155 and decreases to 0.00. The validation performance curve (teal) starts at approximately 0.145, peaks at approximately 0.145 at log(lambda) = -9, and then decreases to 0.00. The gap between the training and validation curves widens as log(lambda) increases. Vertical dashed lines mark the 'max' model at log(lambda) = -9 and the '1 s.e.' model at log(lambda) = -8.5. Above the x-axis, a series of numbers (94, 88, 81, 67, 57, 52, 36, 28, 15, 6, 2, 2, 0) are aligned with the x-axis ticks.

**Figure 4.10. At the max model the validation curve is flat and the gap between the training and validation curve has widened. The models around this level of complexity have started to pick up patterns which are in the training data only and which do not improve cross-validation performance.**

In our case, a further point to note is the consistency of performance differences for the individual folds. We do not show details here, but for every fold, performance of the "1 s.e." model is worse than the "max" model.

In practice, while good performance of insurance models is exceedingly important, simpler models are easier to understand and explain to underwriters, regulators, and policyholders. One option is to choose a model simpler than the "max" model, but still in the relatively flat part of the cross-validation performance curve and not as simple as the "1 s.e." model.

### 4.6.6. *Flavors of penalized regression*

When we train GLMs, the coefficients can take on infinitely many values. We hope that penalized regression helps us to choose a set of coefficients which will perform well in the future, but there is no guarantee that it will choose the best such model. In fact, there is no guarantee that penalized regression will even choose the model with the best average cross-validation performance.

The earliest type of penalized regression was Ridge regression. This gives a sequence of 100 (say) GLMs. Back when this was the only widely known type of penalty, the practitioner might have been forgiven for thinking that one of the 100 GLMs would be the best model. However, given that in our discussion above we have seen three different types of penalty and the fused LASSO, it should be clear that the sequence of models from any one approach is not guaranteed to contain the best model.

Another flavor of penalized regression is the adaptive LASSO (Zou (2006)). It deals with the problem in the LASSO that the strength of the penalty ( $\lambda$ ) is the same for each feature, yet in practice this might not be reasonable. For example, we might, a priori, have a belief that some features should be in the model and that there is sufficient data to fit them correctly without any shrinkage. We might wish to ensure that such features are subject to much less penalization or are not penalized at all. The adaptive LASSO allows us to apply differing levels of penalty to each feature, depending on an initial estimate of their importance. We will see in Section 4.7.2 that after an adjustment called standardization, the coefficients from penalized regression model do in some way reflect the importance of the features. Hence the approach of the adaptive LASSO is to use the coefficients from a Ridge regression model to inform the amount of penalization applied in the adaptive LASSO.

Sometimes, data contain categorical features that measure the same thing in slightly different ways. This can arise, for example, where data have been enriched from different sources covering similar types of features. In such cases, model interpretation and implementation will be easier if levels are included from one categorical feature or the other, but not from both. A type of penalization, called the grouped LASSO, can help in this case. We do not go into further detail here.

Where does this leave the practitioner? While we cannot assume that Ridge regression or the LASSO will give the best possible models, they are certainly a very good starting point to help with both feature selection and model performance. Should there still be performance or feature selection issues, it is good to know that other flavors of penalization exist.

## 4.7. Technical Note

### 4.7.1. Solving Ridge regression

Consider the very simple case where there is only one feature ( $x$ ) in our model. Assuming a normal distribution and identity link, unpenalized regression needs to minimize

$$l(\beta) = \frac{1}{2n} \sum_{i=1}^n (y_i - \beta x_i)^2.$$

This is easy to solve directly. The derivative is

$$\frac{\delta l}{\delta \beta} = \frac{1}{2n} \sum_{i=1}^n 2(y_i - \beta x_i) \times (-x_i) = -\frac{1}{n} \sum_{i=1}^n x_i y_i + \frac{1}{n} \beta \sum_{i=1}^n x_i^2,$$

and this is zero when

$$\frac{1}{n} \sum_{i=1}^n x_i y_i = \frac{1}{n} \beta \sum_{i=1}^n x_i^2.$$

So, the value of  $\beta$  which minimizes the loss function is

$$\hat{\beta} = \frac{\frac{1}{n} \sum_{i=1}^n x_i y_i}{\frac{1}{n} \sum_{i=1}^n x_i^2}.$$

We now repeat this exercise with the Ridge regression penalty. Our loss function is

$$l(\beta) = \frac{1}{2n} \sum_{i=1}^n (y_i - \beta x_i)^2 + \lambda \frac{1}{2} \beta^2.$$

The derivative is

$$\frac{\delta l}{\delta \beta} = -\frac{1}{n} \sum_{i=1}^n x_i y_i + \frac{1}{n} \beta \sum_{i=1}^n x_i^2 + \lambda \beta = -\frac{1}{n} \sum_{i=1}^n x_i y_i + \beta \left( \frac{1}{n} \sum_{i=1}^n x_i^2 + \lambda \right),$$

and this is zero when

$$\frac{1}{n} \sum_{i=1}^n x_i y_i = \beta \left( \frac{1}{n} \sum_{i=1}^n x_i^2 + \lambda \right).$$

So, the value of  $\beta$  which minimizes the loss function is

$$\hat{\beta} = \frac{\frac{1}{n} \sum_{i=1}^n x_i y_i}{\frac{1}{n} \sum_{i=1}^n x_i^2 + \lambda}.$$

We can see that the impact of penalization is to shrink the estimate  $\hat{\beta}$  towards zero (but not exactly zero) compared to the unpenalized estimate. The role of  $\lambda$  here is not totally dissimilar to the role of  $k$  in Bühlmann's credibility factor  $Z = \frac{n}{n+k}$ , which controls the extent to which group-specific estimates are shrunk towards the overall population estimate (see for example the discussion in Chapter 2 of Holmes and Casotto (2025)).

When there is more than one parameter, the relationship between  $\lambda$  and each of the fitted parameters is not as simple as that shown above. Each estimated parameter is still shrunk towards zero (but not exactly zero) compared to its unpenalized estimate, and the amount of shrinkage increases as  $\lambda$  increases.

### 4.7.2. Standardization

We saw in the last section that the parameter estimate under Ridge regression is

$$\hat{\beta} = \frac{\frac{1}{n} \sum_{i=1}^n x_i y_i}{\frac{1}{n} \sum_{i=1}^n x_i^2 + \lambda}.$$

Consider a case where frequency depends on length (in meters) and for which  $\frac{1}{n} \sum_{i=1}^n x_i y_i = 10$  and  $\frac{1}{n} \sum_{i=1}^n x_i^2 = 5$ . The unpenalized estimate is  $\hat{\beta} = 2$ . The Ridge regression estimate will depend on the value of  $\lambda$ . If  $\lambda = 5$ , then  $\hat{\beta}$  will be shrunk to 1. If we have an observation which is one meter long, the unpenalized estimate is a frequency of 2 and the penalized estimate is 1.

We now move to measuring length in centimeters.  $\frac{1}{n} \sum_{i=1}^n x_i y_i$  will be 100 times bigger (1,000) and  $\frac{1}{n} \sum_{i=1}^n x_i^2$  will be  $100^2$  times bigger (50,000). The unpenalized estimate is  $\frac{1,000}{50,000} = 0.02$  and the penalized estimate is  $\frac{1,000}{50,000+5} = 0.019$ . The frequency estimates are 2 and 1.9. We can see that the impact of penalization changed just because we changed the units by which we measure the length.

If there is only one feature, the issue above does not matter—choosing an appropriate sequence of  $\lambda$ s will still give a range of estimates from unpenalized down to zero. However, when there are many features, then at any level of  $\lambda$ , a feature which is measured in smaller units (and so has larger values and a smaller coefficient) will be less affected by the penalization. This can lead to some features being incorrectly penalized out of the model. The same issue applies in any penalized regression, not just Ridge regression.

In order to make penalized regression estimates independent of the units by which

features are measured, it is usual to standardize all the features before applying the rest of the calculation. This means deducting the mean and dividing by the standard deviation so that each feature has a mean of zero and variance of 1. The standard deviation is  $\frac{1}{n} \sum (x_i - \bar{x})^2$ . For a standardized feature, given that  $\bar{x} = 0$ , the standard deviation is  $\frac{1}{n} \sum x_i^2 = 1$  so that parameter estimate under Ridge regression simplifies when features are standardized from

$$\hat{\beta} = \frac{\frac{1}{n} \sum_{i=1}^n x_i y_i}{\frac{1}{n} \sum_{i=1}^n x_i^2 + \lambda}$$

to

$$\hat{\beta} = \frac{\frac{1}{n} \sum_{i=1}^n x_i y_i}{1 + \lambda}.$$

The default behavior of most penalized regression software is to standardize the numeric features before fitting but to return the coefficients which can be applied to the original features. It can be useful when comparing coefficients to do so on the scale of the standardized features. Table 4.5 shows the coefficients in our fitted model for the number of engines and aircraft age. On the original scale, the magnitude of the coefficient for the number of engines is bigger in absolute value than the coefficient for the number of engines. The number of engines ranges from one to four. The aircraft age ranges from 0 to 50, and despite its smaller coefficient, it will have a large effect on the linear predictor and it is more important in our fitted model. The coefficients on the scale of the standardized features are comparable, and we can see that indeed the magnitude of the aircraft age coefficient is larger.

**Table 4.5. After fitting a penalized model on the standardized numeric features, the coefficients can be viewed on the original scale or on the scale of the standardized features.**

| var              | original scale | standardized |
|------------------|----------------|--------------|
| faa_acft_num_eng | −0.277         | −0.119       |
| aircraft_age     | −0.073         | −0.791       |

Categorical features are typically represented by a column of zeros and ones. For example, for type of registrant category 3 (corporations), there will be a column which is 0 if the registrant is a corporation and 1 if it is not. Such features are often not standardized. Their values are all 0 or 1, and so they are not on very different scales. And their coefficients are easy to interpret. From a practical perspective, some software benefits in memory usage and speed from sparse data (lots of zeros) and standardization of these 0-1

variable would remove that benefit. If optimal model performance is key, then fitting a model both with and without standardization of categorical features and comparing the cross-validation performance curves is straightforward. In insurance pricing, a careful review, and manual adjustment if necessary, of the coefficients in the final rating plan is crucial. This is particularly true where adjustments to the model fitting process make a large difference to coefficients. Hence, if different approaches to standardization make a large difference to fitted coefficients, great care should be taken to review the model based on an understanding of the line of business.

### 4.7.3. Solving the LASSO

Reverting to our simple unpenalized case,

$$l(\beta) = \frac{1}{2n} \sum_{i=1}^n (y_i - \beta x_i)^2,$$

we saw that

$$\hat{\beta} = \frac{\frac{1}{n} \sum_{i=1}^n x_i y_i}{\frac{1}{n} \sum_{i=1}^n x_i^2},$$

which, if  $x$  is standardized, is

$$\hat{\beta} = \frac{1}{n} \sum_{i=1}^n x_i y_i.$$

Now consider the LASSO, we need to minimize

$$l(\beta) = \frac{1}{2n} \sum_{i=1}^n (y_i - \beta x_i)^2 + \lambda |\beta|.$$

Multiplying out the first term gives

$$\frac{1}{2} \left( \sum_{i=1}^n y_i^2 - 2\beta \sum_{i=1}^n x_i y_i + \beta^2 \sum_{i=1}^n x_i^2 \right).$$

If  $x$  is standardized, then this simplifies to

$$\frac{1}{2} \left( \sum_{i=1}^n y_i^2 - 2\beta \hat{\beta} + \beta^2 \right),$$

where  $\hat{\beta}$  is the unpenalized estimate.

Ignoring the constant  $\sum_{i=1}^n y_i^2$ , we need to figure out how to minimize

$$\frac{1}{2} (-2\beta\hat{\beta} + \beta^2) + \lambda|\beta|.$$

For convenience we add the constant  $\hat{\beta}^2$  so that this becomes

$$\frac{1}{2}(\hat{\beta} - \beta)^2 + \lambda|\beta|,$$

which given  $\lambda$  and  $\hat{\beta}$  is a function of  $\beta$  and differs only by a constant from the original loss function  $l(\beta)$ .

Consider the case when the unpenalized estimate  $\hat{\beta} > 0$ . It can never make sense to set  $\beta$  to be more than  $\hat{\beta}$  because the first term in the loss function ( $\frac{1}{2}(\hat{\beta} - \beta)^2$ ) will be positive, and we can easily do better by reducing  $\beta$  to  $\hat{\beta}$  which will set the first term to zero and at the same time reduce the second term. So the impact of the LASSO must always be to shrink the coefficients towards zero.

Now consider what happens when  $\lambda \geq \hat{\beta}$ . If we set  $\beta = 0$ , then the loss function is  $\frac{1}{2}\hat{\beta}^2$ . We will now show that any other value of  $\beta$  gives a higher value for the loss function, which implies that whenever  $\lambda \geq \hat{\beta}$ ,  $\beta$  will be set to exactly zero.

If we allow  $\beta$  to be more than zero, then the loss is

$$\frac{1}{2} (\beta^2 + \hat{\beta}^2 - 2\beta\hat{\beta}) + \lambda\beta.$$

Since  $\lambda \geq \hat{\beta}$ , we know that  $\lambda\beta \geq \hat{\beta}\beta$  and so the loss is greater than

$$\frac{1}{2} (\beta^2 + \hat{\beta}^2 - 2\beta\hat{\beta}) + \hat{\beta}\beta = \frac{1}{2} (\beta^2 + \hat{\beta}^2 - 2\beta\hat{\beta} + 2\beta\hat{\beta}) = \frac{1}{2} (\beta^2 + \hat{\beta}^2),$$

which is certainly more than  $\frac{1}{2}\hat{\beta}^2$ .

Therefore, for all values of  $\lambda$  which are greater than the unpenalized estimate  $\hat{\beta}$ , our penalized estimate is zero.

When  $\lambda < \hat{\beta}$  our estimate of  $\beta$  can be greater than zero. When  $\beta > 0$  the derivative of the loss function is

$$\frac{\delta l}{\delta \beta} = \beta - \hat{\beta} + \lambda.$$

At the minimum this is zero and we have

$$\beta = \hat{\beta} - \lambda.$$

Overall therefore, when the unpenalized coefficient  $\hat{\beta}$  is greater than zero, the penalized estimate reduces that coefficient by the value of  $\lambda$ , until  $\lambda$  is greater than the unpenalized estimate and the penalized estimate is exactly zero.

The same simple relationship does not hold if there is more than one feature. In that case we can still say that given the final fitted penalized model, if we look at one coefficient given all the other fitted coefficients, it will be shrunk towards zero by some amount which will vary for each coefficient but still depends on  $\lambda$ .

When we move to using nonlinear link functions such as the log-link, the simple relationship breaks down further. However, it is still true that the parameters are either shrunk to exactly zero or reduced in size by an amount which gets bigger as  $\lambda$  gets bigger.

## 4.8. Next Steps

We have now fitted a penalized GLM on the FAA-NTSB data. The model includes aircraft age. Figure 4.11 shows the actual accident rate by aircraft age and the average prediction from the model. The frequency predicted by the model (blue line) is reasonably close to the actual frequency (red points), but in some places the shape is not quite right. For example, from aircraft age 30, the model predicted frequency continues to decrease—driven by the aircraft age effect in the model—whereas the actual frequency is reasonably flat.

The aircraft age effect, shown by the green line, is limited by our use of the GLM to being a very simple shape. The fitted model is

$$\log \text{frequency} = \dots - 0.0824 \times \text{aircraft age},$$

or, taking exponents of both sides:

$$\text{frequency} = \dots \times \exp[-0.0824 \times \text{aircraft age}].$$

This gives the smooth decreasing green line in the figure, but the actual frequency does not decrease in such a smooth manner.

In the next section, we will look at some approaches for modeling effects which have shapes not easily picked up by GLMs.

![Scatter plot of actual frequency vs aircraft age with predicted and age relative lines.](55086c71bc8ee4c0abc7160d26a8092c_img.jpg)

The figure is a scatter plot with two lines. The x-axis is labeled 'aircraft age' and ranges from 0 to 40 with major ticks every 10 units. The y-axis is labeled 'freq\_actual' and ranges from 0.0000 to 0.0100 with major ticks every 0.0025 units. The legend at the top identifies three series: 'actual frequency' (red dots), 'age relativity' (green dashed line), and 'predicted frequency' (blue solid line). The red dots represent individual data points, showing a general downward trend from approximately 0.010 at age 0 to near 0.000 at age 40. The green dashed line, representing age relativity, starts at 0.010 at age 0 and decreases steadily to about 0.0005 at age 40. The blue solid line, representing the predicted frequency, starts at approximately 0.0085 at age 0, decreases to about 0.0045 at age 10, and then continues to decrease more slowly, reaching about 0.001 at age 40. The predicted frequency line is generally above the actual frequency points for ages 0-10 and below them for ages 10-40.

| aircraft age | actual frequency | age relativity | predicted frequency |
|--------------|------------------|----------------|---------------------|
| 0            | 0.0100           | 0.0100         | 0.0085              |
| 5            | 0.0055           | 0.0065         | 0.0055              |
| 10           | 0.0040           | 0.0045         | 0.0045              |
| 15           | 0.0030           | 0.0030         | 0.0035              |
| 20           | 0.0020           | 0.0020         | 0.0025              |
| 25           | 0.0015           | 0.0015         | 0.0020              |
| 30           | 0.0010           | 0.0010         | 0.0015              |
| 35           | 0.0015           | 0.0005         | 0.0010              |
| 40           | 0.0005           | 0.0005         | 0.0010              |

Scatter plot of actual frequency vs aircraft age with predicted and age relative lines.

**Figure 4.11. FAA-NTSB LASSO on features excluding HCCVs. The model predicted frequency (blue line) is close to the actual frequency (red points). However, from age 30 the predicted frequency continues to decrease, driven by the aircraft age effect in the model, whereas the actual frequency is reasonably flat.**
