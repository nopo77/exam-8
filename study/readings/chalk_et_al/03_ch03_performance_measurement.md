---
paper: chalk_et_al
chapter: 3
title: Performance Measurement
topics: [pseudo_r_squared, k_fold_cross_validation, generalization_error, null_model, baseline_model, train_validate_test_split, overfitting]
key_formulas: [pseudo_r_squared, k_fold_cross_validation, rebasing_predictions]
---

> **TL;DR**
> - Pseudo-R² = (l_model − l_null)/(l_saturated − l_null) = 1 − D_model/D_null measures deviance explained; preferred over raw deviance because it is observation-count independent.
> - Test data (≈30%) is held out and never used for any modeling decision; k-fold cross-validation (7 folds) guides all training decisions including feature selection and λ tuning.
> - Each cross-validation model must independently perform all feature selection steps within its own folds to avoid leakage — manual hand-selection of features invalidates cross-validation.
> - Null model pseudo-R² ≈ 0; FAA-NTSB baseline GLM achieved 0.140, gradient-boosting benchmark 0.165 — these bracket the expected performance range.
> - Rebasing predictions: multiply predictions by the ratio of fold mean to training mean to isolate segmentation ability from overall level accuracy.

# 3. Performance Measurement

Section 6 of the CAS GLM monograph discusses measures of model fit and comparing candidate models. Likelihood and deviance are mentioned, as well as penalized measures of fit (Akaike information criterion [AIC] and Bayesian information criterion [BIC]).

The authors note that comparing deviance across different datasets is not feasible. This is because deviance, calculated and summed for each observation, results in larger values for datasets with more observations. (Deviance can also not be compared across models with different error distributions, as it depends on the assumed distributional form.)

They explain that penalized measures of fit (AIC, BIC) are important. This is because without penalization, adding more features to a model always reduces its deviance (when measured on data on which the model was trained). For instance, by including a unique identifier as a feature in a generalized linear model (GLM), you could achieve a zero deviance, but this is not a true measure of the model's effectiveness.

The approach we have chosen to use for this note is to use a measure that does not depend on the number of observations (pseudo- $R^2$ ) and to calculate it over data not used in fitting the model (validation and test data).

## 3.1. Pseudo- $R^2$

In linear regression, the  $R^2$  measure quantifies the proportion of variance in the dependent variable that is explained by the independent variables. The formula for  $R^2$  is

$$R^2 = 1 - \frac{\text{Sum of Squares of Residuals}}{\text{Total Sum of Squares}}.$$

There are various problems with using  $R^2$  to measure the performance of GLMs (see Cameron and Trivedi (2013)). Instead, measures called pseudo- $R^2$  are used. We now introduce the version we will use by way of an example.

We use  $y_i$  to refer to the variable we are trying to predict and  $\hat{y}_i$  refers to the model prediction. The subscript  $i$  refers to each individual record. Example data is given in Table 3.1.

**Table 3.1. Example data. Four observations: two with claims and two without. The model estimated probabilities are given in the third column.**

| unique_id | $y_i$ | $\hat{y}_i$ |
|-----------|-------|-------------|
| 1         | 0     | 0.2         |
| 2         | 0     | 0.4         |
| 3         | 1     | 0.6         |
| 4         | 1     | 0.8         |

Under the Poisson distribution, the probability of  $y_i$  if the Poisson mean is equal to  $\hat{y}_i$  ( $\lambda$  or  $\mu$  are often used for this parameter) is given by:

$$pr[y_i|\hat{y}_i] = \frac{\hat{y}_i^{y_i} e^{-\hat{y}_i}}{y_i!}.$$

Given that  $y_i$  are just our data and will not change from model to model, the denominator is constant and can be ignored in further calculations. (If we kept it in, it would cancel out in both the numerator and denominator of the expression we eventually derive.)

We will move forward by taking logs and working with the log-likelihood. (The motivation for taking logs in the context of our discussion is not obvious. However, more generally in the context of GLMs, it leads to mathematical calculations that are easier to work with and estimators that have useful statistical properties.) In the text below, all logs are to the base  $e$ .

Excluding the ignored constant, each individual contribution to the log-likelihood of our data given our model ( $l_{model}$ ) is therefore:

$$\begin{aligned} \log_e pr[y_i|\hat{y}_i] &= \log_e(\hat{y}_i^{y_i} e^{-\hat{y}_i}) \\ &= y_i \log_e(\hat{y}_i) - \hat{y}_i. \end{aligned}$$

The  $l_{model}$  of the data in Table 3.1, given the predictions shown, is:

$$\begin{aligned} &0 \times \log_e 0.2 - 0.2 \\ &+ 0 \times \log_e 0.4 - 0.4 \\ &+ 1 \times \log_e 0.6 - 0.6 \\ &+ 1 \times \log_e 0.8 - 0.8 \\ &= -2.734 \end{aligned}$$

The simplest model we could fit would have no features at all beyond an intercept and would just fit the mean. This is called the null model. The mean of  $y_i$  in the above data is 0.5, and the null model log-likelihood ( $l_{null}$ ) is therefore:

$$\begin{aligned} & 0 \times \log_e 0.5 - 0.5 \\ & +0 \times \log_e 0.5 - 0.5 \\ & +1 \times \log_e 0.5 - 0.5 \\ & +1 \times \log_e 0.5 - 0.5 \\ & = -3.386 \end{aligned}$$

The improvement in likelihood from the null model to the fitted model is therefore:

$$l_{model} - l_{null} = -2.734 - (-3.386) = 0.652$$

We can suggest that the "perfect" model would predict  $y_i$  for each observation. This is called the saturated model, and its likelihood ( $l_{saturated}$ ) is

$$\begin{aligned} & 0 \times \log_e 0 - 0 \\ & +0 \times \log_e 0 - 0 \\ & +1 \times \log_e 1 - 1 \\ & +1 \times \log_e 1 - 1 \\ & = -2 \end{aligned}$$

The best possible improvement in likelihood is from the null model to the saturated model:

$$l_{saturated} - l_{null} = -2 - (-3.386) = 1.386.$$

We can therefore say, that as a percentage of the best improvement in likelihood possible, the model explains:

$$\frac{l_{model} - l_{null}}{l_{saturated} - l_{null}} = \frac{0.652}{1.386} = 47\%.$$

This measure

$$\text{pseudo-}R^2 = \frac{l_{model} - l_{null}}{l_{saturated} - l_{null}}$$

is what we will use.

Remembering (as mentioned in the CAS GLM monograph Section 6.1.2) that deviance of a model is  $D_{model} = 2 \times (l_{saturated} - l_{model})$ , it is easy to show that:

$$\text{pseudo-}R^2 = 1 - \frac{D_{model}}{D_{null}}.$$

This now looks quite similar to the  $R^2$  statistic that we started off with, where  $D_{null}$  represents the total variance and  $D_{model}$  represents the residual variance. We can say that in the same way that  $R^2$  measures the percent of variance explained, pseudo- $R^2$  measures the percent of deviance explained.

One advantage of using pseudo- $R^2$  is that it leads to a number that modelers can remember. They can remember that typically a certain model can explain, say, 12% of the deviance. It tends to be quite clear whether or not a new model is performing well or not.

In Section 3.7.1 we will use our simulation study to help us understand what typical values we might expect pseudo- $R^2$  to take in an insurance context.

In Section 3.7.2 we briefly discuss why we might need to give each line in our data a different weight and how this affects the pseudo- $R^2$  calculation.

## 3.2. Train—Validate—Test

The risk of overfitting GLMs and the idea of splitting the data into training and test datasets is discussed in Goldburd et al. (2025), Section 4.3. Likewise, they discuss validation and cross-validation. We revisit this discussion and add some extra details.

The CAS GLM monograph required penalization of the performance metrics which were based on deviance, because deviance of a GLM measured on the training data will only ever decrease as more features are added. This will encourage models that are far too complex and do not generalize well to data that the model was not trained on.

This issue can be avoided by never saying that a model is good because our pseudo- $R^2$  measure looks good (i.e., high) on the data on which the model was trained. Instead we hold out some of the data (typically 30%<sup>7</sup>) as a test dataset. (This is also known as a test partition.) We say that a model is good if the pseudo- $R^2$  is good on the test dataset.

No result (or graph) from the test dataset can ever influence the model structure or features used or parameter estimates. If that happens, then it ceases to be a test dataset. The authors of this monograph have seen practitioners who, when faced with a difficult decision during model fitting, have a quick look at certain graphs or other metrics on the test dataset. In such cases, training decisions have been made by use of the test dataset and it is—by definition—no longer a test dataset, and good performance on it does not

---

<sup>7</sup> Others might use similar but somewhat different values.

mean that the model is good. There is at least one proprietary software that hides the test dataset from the practitioner while the model is being fitted. In a team where data are prepared by some colleagues and models are trained by others, it would be reasonable for the data preparation team to withhold the test dataset until the training is complete.<sup>8</sup>

Besides needing to know the performance of our final fitted models, we might also need to know the performance during the model fitting process. This is because, as we will see in this monograph, when fitting GLMs many decisions need to be taken when fitting GLMs, such as which features to include and how to allow for nonlinear effects. In addition, we will see that when using penalized regression there is always one critical parameter whose value has to be chosen based on performance while training the model. If possible, we want to take data-driven decisions, i.e., decisions which improve the performance of the model based on test data. However, we cannot do that. As soon as we start taking model training decisions on the test data, it is no longer a real test.

Our approach to all decisions taken during training is to use k-fold cross-validation. We explain this by example:

Imagine we have a dataset with 100 observations only. We set aside observations 71–100 for the test data. We divide the remaining data into seven parts. Each part is called a "fold." The seven parts we choose are observations 1–10, 11–20, etc. We then train seven models as follows:

- Model 1
  - In this model, observations 1–10 (fold 1) will be used for validation.
  - Train a model on all observations excluding 1–10, i.e., train on observations 11–70.
  - Predict the model on observations 1–10.
  - Calculate the pseudo- $R^2$  on observations 1–10.
- Model 2
  - In this model, observations 11–20 (fold 2) will be used for validation.
  - Train a model on all observations excluding 11–20, i.e., train on observations 1–10 and 21–70.
  - Predict the model on observation 11–20.
  - Calculate the pseudo- $R^2$  on observations 11–20.

and so on. The results might look something like Table 3.2.

---

<sup>8</sup> This is also done for online predictive modeling competitions.

**Table 3.2. Seven models are trained. Validation performance is measured for each model using the validation data for that model. The average cross-validation performance is 0.10.**

| model   | observations used for<br>validation | training       | pseudo- $R^2$ |
|---------|-------------------------------------|----------------|---------------|
| 1       | 1–10                                | 11–70          | 0.10          |
| 2       | 11–20                               | 1–10 and 21–70 | 0.11          |
| 3       | 21–30                               | 1–20 and 31–70 | 0.09          |
| 4       | 31–40                               | 1–30 and 41–70 | 0.10          |
| 5       | 41–50                               | 1–40 and 51–70 | 0.12          |
| 6       | 51–60                               | 1–50 and 61–70 | 0.08          |
| 7       | 61–70                               | 1–60           | 0.10          |
| average |                                     |                | 0.10          |

Our performance metric will therefore be the average cross-validation pseudo- $R^2$  over  $k$  validation folds during training.

If we are faced with multiple alternatives to evaluate during training, we will calculate the average cross-validation performance for each one. We will then usually<sup>9</sup> use the option with the highest performance.

In the context of using cross-validation in place of a test (or holdout) dataset, Goldburd et al. (2025) Section 4.3.4, raise a problem with cross-validation. They explain that every training decision must be taken within the training phase of each of the cross-validation models. If features are "hand selected" with care and judgment, this process would need to be repeated, in our case, seven times—once for each fold. Since highly manual processes cannot be repeated so many times, they must be made before the data are split into folds—which then invalidates the cross-validation performance measurement.

The approach in our case studies is, in fact, to use automatic feature selection and engineering techniques and to do so within each of our seven models. This means that each of the models fitted in our cross-validation process may contain different features. Therefore, once the model training is complete, a final model must be fitted on all the data from all training folds using the decisions arrived at during cross-validation. The pseudo- $R^2$  can be calculated on the test data. This data was not used in any part of the training, and so performance on the test data should therefore be indicative of future performance of the model on unseen data. The use of automatic feature selection and engineering techniques does not mean that the use of care and judgment is now redundant. However, it does mean that the analysis can sometimes proceed to a later stage before manual adjust-

<sup>9</sup> There is room for some actuarial judgment.

ments are made, so that cross-validation performance measurement can be carried out at a later stage and help inform more of our modeling decisions.

## 3.3. Generalization Error

In the above discussion, we talked somewhat informally about "future performance of the model on unseen data." The formal term for the error made on future data by a model trained on our training data is "generalization error".

We proposed using cross-validation to help make modeling decisions and to estimate generalization error. This is a common and accepted technique across many areas of machine learning in situations where there is not sufficient data to separate out datasets for training, validation, and testing.

We will see later—and due to its importance we note now—that the performance we see after implementing our models may be very different from our estimated generalization error. The reason for this is as follows: Our cross-validation partitions are random samples of our data, and so each partition will have a similar distribution of the features. For example, if in one fold most policyholders are above 30, this is likely to be true across all folds. Overall then, our cross-validation estimate of generalization error is for a portfolio consisting mostly of policyholders over 30. If our modeling process leads to a new rating plan which significantly increases prices for policyholders above 30 years old and decreases prices for younger policyholders, then the distribution of the future unseen data will be very different from that in the validation folds, and actual performance may be different from expected. This will particularly be the case if there is a weakness in the new rating plan which savvy policyholders notice and take advantage of. A vital part of premium rating is therefore to monitor (in depth) the mix of business after implementation of the new rates. If the percentage of business written in one segment changes unexpectedly, then performance of that part of the model should be reviewed.

## 3.4. Null Models

A null model is the most basic model possible—often an intercept-only model, where the predicted frequency for each observation is the mean frequency.

For our simulated auto insurance data, we calculate the average frequency on training data, and the null model predicts this value for every row in our validation or test data.

For our FAA-NTSB study, the most basic model possible is one which just predicts the mean frequency on the training data for every aircraft in the validation or test data.

Under some performance metrics, performance of a null model can look very high. For example, in the FAA-NTSB data, the average accident rate is 0.4%. This is true for both the training and test sets. If model predictions are either 0 (no accident) or 1 (accident), we might decide to use accuracy (the percent of predictions that are correct) as a

measure. A very naive model which predicts 0 (no accident) for every craft will have a test accuracy of 99.6%. This might sound good, but the model is clearly of no use. Hence, before starting to train serious models, it is a good idea to create a null model to ensure that we understand what zero performance looks like. It also helps us to set up a basic pipeline for our model—training one model for each of the k-folds, calculating predictions and performance.

In our case, we should expect both training and validation (pseudo- $R^2$ ) performance to be 0% for a null model. This is because

$$\text{pseudo-}R^2 = \frac{l_{\text{model}} - l_{\text{null}}}{l_{\text{saturated}} - l_{\text{null}}},$$

and for a null model the numerator is zero, since the (fitted) model is the null model.

We check this for a small sample (10,000 observations) of the simulated auto insurance data. As discussed above, we first put aside 30% of the data for testing and divide the remaining data into seven folds. (We did this by dividing the data into 10 folds and using the last three for testing.) The folds were labeled 1, 2, ..., 7. We then "trained" seven models as follows:

- Model 1
  - In this model, we used fold 1 for validation.
  - Find the mean frequency on folds 2–7. It is 0.0887.
  - Predict 0.0887 as the frequency for all the observations in fold 1.
  - Calculate the pseudo- $R^2$  for fold 1.
- Model 2
  - In this model, we used fold 2 for validation.
  - Find the mean frequency on folds 1 and 3–7. It is 0.0926.
  - Predict 0.0926 as the frequency for all the observations in fold 2.
  - Calculate the pseudo- $R^2$  for fold 2.

And so on. Table 3.3 shows the results for all folds, and the results are indeed mostly close to zero.

**Table 3.3. Performance under the null model. Pseudo- $R^2$  is close to zero.**

| fold | deviance_model | deviance_null | proportion_explained |
|------|----------------|---------------|----------------------|
| 1    | 2903           | 2902          | -0.0001              |
| 2    | 2954           | 2954          | -0.0000              |
| 3    | 3095           | 3095          | -0.0001              |
| 4    | 3040           | 3040          | -0.0001              |
| 5    | 2861           | 2859          | -0.0004              |
| 6    | 3117           | 3116          | -0.0004              |
| 7    | 2926           | 2925          | -0.0001              |

There is a problem here. Why are the results not exactly zero? The null model is an intercept-only model, which therefore predicts the mean. The model which we are fitting also predicts the mean. These two models are identical, so why is the deviance not identical? The reason is that we train our model, i.e., teach it to predict the mean, on the training data. We calculate performance based on the validation data, which will have a slightly different mean. This issue is discussed further in Section 3.7.4.

Although we will generally avoid looking at test performance until the end of the study, we also fit the null model on all the folds and find performance on the test data.

**Table 3.4. Performance on the test data under the null model. As expected, pseudo- $R^2$  is zero.**

| fold | deviance_model | deviance_null | pseudo- $R^2$ |
|------|----------------|---------------|---------------|
| 99   | 8952           | 8952          | -0.0000       |

We can see that performance of the model on the test data is also very close to 0%. In addition, we can see that the deviances are about three times higher than those for each fold. This is because the test fold contains three times as much data as each fold (30% of the total simulated data compared to only 10% in each validation fold).

Although we do not show the results here, we checked on our other case studies and confirmed that performance as measured by pseudo- $R^2$  is zero for the null model.

## 3.5. Baseline Models

At this stage, before trying to deal with any of the practical problems this monograph will address, it would be useful to train basic GLMs on the various datasets. The purpose of this is to enable us to test later whether our suggested solutions to the practical problems actually improve performance. The main case study we will focus on is the FAA-NTSB

data,<sup>10</sup> and therefore we would like in particular to show the results of a basic GLM on this data.

Examples of the features potentially available to use in our baseline GLM are as follows:

- Information about the aircraft, e.g., aircraft make and model, engine(s) make and model, maximum speed, number of seats, etc.
- Information about the use of the aircraft.
- Information about the owner of the aircraft, e.g., type of registrant (individual, corporation, etc.) and their location (region, country, city), etc.

Unfortunately, we were not able to fit a GLM when naively using all the features. This is because categorical variables like aircraft make and model have many different categories. As we will discuss in Chapter 6, a naive use of these leads to various issues. When we tried, there were memory problems or very long run times. For reasons explained later, even had we managed to fit these models they would have been unlikely to perform well on test data. We therefore excluded from the baseline model all categorical features with more than 20 categories. Even then, GLMs failed to converge. The reason for this is that some of the features in the model are linear combinations of other features. An example is whether an aircraft is licensed for carriage of cargo. Whether or not an aircraft in our dataset is licensed to carry cargo can be determined from a (linear) combination of airworthiness code and other operations it is licensed for. This is called multicollinearity and will be discussed briefly in Chapter 7. We therefore found and dropped the features causing the problem.

Having excluded the troublesome features, we were left with 22, of which seven were numeric and 15 were categorical. For a given categorical feature, a GLM will fit one parameter for each category other than the base level. For example "type\_registrant" has nine categories, and so the GLM will fit eight parameters. (The reason why our GLM will not fit a separate parameter for the base level of categorical features is again due to multicollinearity. Whether or not type\_registrant is 1 can be determined from type\_registrant\_2 to type\_registrant\_9.) Overall our GLM will fit 82 parameters for the 15 categorical features, so the model will have 89 parameters in total (besides the intercept).

Seven GLMs were fit (excluding data from one of the seven folds in turn). For each GLM, performance was measured for the six folds of data it was trained on (training performance) and separately for the one fold of data which was withheld (validation performance). The results are shown in Table 3.5, where we can see an average validation

<sup>10</sup> The full dataset used is available as an R library from GitHub at FAANTSB. After installation of the library, the help on the dataset (?dt\_faa\_ntsb\_clean) provides a list of all the features and their meanings.

performance on the seven folds of pseudo- $R^2$  of 0.142 and the average training performance is 0.157.

**Table 3.5. Performance under the baseline model.**  
**Average pseudo- $R^2$  on validation data is 0.140. Train performance is higher: 0.156. Some of the patterns fitted by the model are just noise in the training data and are not present in the validation data.**

| fold | pseudo- $R^2$ |            |
|------|---------------|------------|
|      | train         | validation |
| 1    | 0.153         | 0.136      |
| 2    | 0.151         | 0.124      |
| 3    | 0.156         | 0.143      |
| 4    | 0.165         | 0.145      |
| 5    | 0.148         | 0.135      |
| 6    | 0.149         | 0.138      |
| 7    | 0.169         | 0.159      |
| mean | 0.156         | 0.140      |

The GLM output contains, as usual, coefficients and  $p$ -values. Part of the output is shown in Table 3.6. Given that we are using a log-link<sup>11</sup> to create a prediction, we sum the coefficients to find the linear predictor, and we then take the exponent. For example, if the coefficients shown were the only ones in the model, the linear predictor for a corporation (type\_registrant 3) with a five-year-old aircraft would be

$$-2.447 + 0.410 + 5 \times (-0.086) = -2.467,$$

and the predicted accident frequency would be

$$\exp(-2.467) = 0.085.$$

We can see some large  $p$ -values and one very large negative coefficient. If we were to continue using unpenalized GLMs, we would need to think about whether these are reasonable to have in our model and, if not, what to do about them. We also note that the impact of age on the linear predictor is linear in age—we will later consider whether or not this is reasonable.

<sup>11</sup> And the Poisson distribution, but that does not determine how we find the predictions given the fitted coefficients.

**Table 3.6. Some of the coefficients and  $p$ -values from the baseline model. Some  $p$ -values are large, and the magnitude of one coefficient is very large. If we were to proceed with unpenalized regression, consideration would need to be given to how to deal with these issues.**

|                  | Estimate | Pr(> t ) |
|------------------|----------|----------|
| intercept        | −2.447   |          |
| type_registrant2 | −0.375   | 0.2628   |
| type_registrant3 | 0.410    | 0.0000   |
| type_registrant4 | 0.086    | 0.6987   |
| type_registrant5 | 0.378    | 0.0685   |
| type_registrant7 | 0.425    | 0.0000   |
| type_registrant8 | −0.072   | 0.8563   |
| type_registrant9 | −12.756  | 0.9958   |
| aircraft age     | −0.086   | 0.0000   |

## 3.6. Benchmark Models

From our baseline model, we have an idea of the minimum performance that we should expect from our GLMs. At the start of a GLM rating analysis, it is also useful to know what is a good level of performance, so that if we get close to it, we might consider moving on to other projects, and if we exceed it, we should both be happy and double-check our work. We will discuss later (Section 8.2) that a challenge in using GLMs is that we need to be sure to feed them the right features—a topic we will discuss in detail. Indeed, we will create a machine learning pipeline, with penalized regression at its heart, which should do exactly that.

Tree-based machine learning models deal implicitly with nonlinear features and with interactions. Their disadvantage is that they are hard to interpret. This means that if we base rating plans on such models, it will be hard to explain in simple terms why the price for a policy is a given amount or why the price has changed following a change in the value of a feature. If all we want is to know what good performance looks like, then interpretability is not necessarily a major concern. A difficulty with training machine learning models is that there are often many parameters to fine-tune, and training them can become an exercise in itself. That being said, there are both open-source and proprietary software solutions that allow relatively easy fitting of machine learning models.

We chose an open-source implementation of gradient boosting whose default parameters are designed to give good performance "out-of-the-box" and which automatically deals with HCCVs. As usual, we trained one model for each fold to get cross-validation performance, and we also trained one overall model. Average cross-validation pseudo- $R^2$  is 0.165. In the authors' experience, well-trained gradient boosting models can some-

times outperform well-trained GLMs, so we would not necessarily expect our GLM to meet this level of performance, but we would hope to get close.

Beyond using alternative machine learning models to check on our GLM's overall performance, we can also use these models and their predictions to check on certain aspects of our model fitting. This will be considered further in Chapter 9.

## 3.7. Practically Speaking

### 3.7.1. *Typical values for pseudo- $R^2$*

Baseline model validation pseudo- $R^2$  for the aviation case study is 0.140. Is this good?

For the simulation data, we have the ground truth, so we know what perfect predictions are. If we measure performance based on these perfect predictions, we get a pseudo- $R^2$  of 0.051. Why does a perfect model have such a (seemingly) low performance? It is because pseudo- $R^2$  compares the part of the deviance that we explain to the deviance explained by predicting every observation at its actual outcome. Since the actual outcome has some randomness, we will never achieve a model that predicts perfectly on that basis.

The typical values of pseudo- $R^2$  that we can achieve on a particular dataset and target variable depend on the signal-to-noise ratio in the data. While we cannot quantify this, it is not a major concern as pseudo- $R^2$  is typically used for relative comparisons between models trained on the same target over a given dataset. In other words, for our aviation case study, asking whether or not 0.142 is good is not a useful question. Rather, we need to measure performance of the various models that we build, and we can then use our performance metric to choose the best performing model. That being said, some practitioners are fond of pseudo- $R^2$  exactly because when applied with care, it can also support inter-dataset comparisons.<sup>12</sup>

In a business context, what we should almost always know is the performance of the existing business model. Our aim is to create a rating plan which is more accurate than the existing one. Therefore, we can define the existing model performance as the benchmark we want to beat. If we are starting with a new model, then our metric allows us to rank models, and while we don't know up front what "good" is, by creating null and baseline model predictions as discussed above, we can ensure that our models are an improvement on a sensible starting position. As discussed above, one can find machine learning models that are relatively easy to train. These can be used to give an idea of the upper limit of good GLM performance.

---

<sup>12</sup> At the end of this monograph, we discuss some errors made in preparing and cleansing the data. Correcting these errors does indeed reduce performance levels towards those seen in the simulated data.

### 3.7.2. Weights

In datasets for frequency models, it is rare for each observation to represent the same amount of exposure. Even if all policies have a period of exactly one year, sometimes a policy may cancel midyear—in which case exposure will be less than one year—or there may be midterm adjustments for which a new line of data is created. In such situations, the pseudo- $R^2$  calculation does not change much;  $y_i$  and  $\hat{y}_i$  in Section 3.1 are the annualized frequencies and the contribution of each prediction to the log-likelihood is multiplied by the exposure.

In slightly more detail, remembering that

$$\text{pseudo-}R^2 = 1 - \frac{D_{\text{model}}}{D_{\text{null}}},$$

the contributions of individual observations to the deviance are multiplied by exposure. If the individual contributions to deviance are  $d_{\text{model}_i}$  and  $d_{\text{null}_i}$  and exposure for each observation is  $ex_i$  then

$$\text{pseudo-}R^2 = 1 - \frac{\sum_i ex_i \times d_{\text{model}_i}}{\sum_i ex_i \times d_{\text{null}_i}}.$$

### 3.7.3. Creating folds

In Section 3.2 we said that we would divide our data into training and testing sets, and that when training models we would use k-fold cross-validation.

There are various ways to create the folds. In Python or R (or any other language), it is very easy to randomly sample your data without replacement. Or we can use packages which contain functions or methods to do this. Different packages will do things differently, and it is worth reading the documentation. For example, in R, the *caret* package will take care to generate balanced cross-validation groupings, i.e., that the frequency of claims is almost the same on the data you use for training, regardless of which fold is being left out.

Creating folds using random sampling can sometimes cause problems. If you forget to set the seed, then your analysis will not be reproducible. Similar problems arise if you are working with different software and the fold is created in one software and not the other. One simple solution is to use a `unique_id` for each record (such as the policy number) to create the fold. Then, even if the folds are for some reason lost, they can be recreated. If the dataset is changed slightly or updated, you can be sure that the folds will be recreated in a very consistent way.

The authors have found the derivation of the fold from the policy number to be practically very useful for the reasons described above. Where the policy whole number is not

numeric, typically one of the trailing digits is. Alternatively, a function that creates a number from any object (known as a hash function) can be used, and the modulus is then taken of the resulting number.

There is another reason why using the policy number to create folds may be important. We want cross-validation folds to be independent tests of our training models. If observations on a cross-validation fold are correlated with the training data, then we do not have an independent test. In insurance datasets, multiple observations often come from the same policy, either due to renewals of the same policy or multiple risks associated with the same policy (e.g., multiple insured vehicles in the same household). Such records will be correlated. If we allow these records to be in different folds and we see good performance, it might just be because the frequency of customer claims in the validation fold is similar to the same customer in the training fold. There is no guarantee that our model will perform well in trying to predict customers it has never seen before. This is a form of "leakage"—an idea which we discuss further in Section 6.3. Using the policy (or customer) number to create the fold variable will ensure that all observations associated with the same customer end up in the same fold.

Some examples of the above issue need more specific care. For example, fire claims in private auto insurance are relatively rare. However, it does happen occasionally that there is a large fire in a parking lot and many cars are total losses as a result of the fire. The resulting claims will likely be mostly in one region. If these policies are spread across all the folds, then a model which trains itself to give a very high coefficient to the region of the parking lot will have a deceptively good cross-validation performance and yet be close to useless in predicting future fire claims (as well as overpricing the region where the parking lot fire occurred). Another example of these high-severity, low-frequency events is homeowners insurance, where large catastrophes (e.g., hurricanes, wildfires, etc.) may impact a specific geography.

### 3.7.4. *Rebasing predictions*

In Table 3.3, our model was a null model which predicted the mean, yet the validation performance was not exactly zero. For example, for fold 1, applying the trained model to the validation fold gave a deviance of 385.88, yet the null deviance of that fold is 383.00, so the numerator in our validation performance metric,  $l_{model} - l_{null}$ , was not exactly zero.

The reason is that we train our (null) model, i.e., calculate the mean, on the training data, whereas  $l_{null}$  uses the mean of validation data itself. For any fold, the mean frequency is not the same on the training data as the validation data. Hence, performance is not exactly zero. We can see in general that the performance rounds to something small but negative. This is because  $l_{null}$  has the advantage of looking directly at the validation

data and therefore gets closer to its mean.

In the very simple case of the FAA-NTSB null model, for the first cross-validation model, the training data (folds 2–7) mean is 0.004579 and validation data (fold 1) mean is 0.004593. We could rebase the model predictions by multiplying each of them by the ratio of the means  $\frac{0.004593}{0.004579} = 1.0031$ . Then, the pseudo- $R^2$  would be focusing on the ability of the trained model to better segment different risks, rather than its ability to correctly estimate the overall level of risk. And then, of course, pseudo- $R^2$  would be exactly zero because the trained model, predicting always the mean, does not differentiate at all between risks (and neither does the null model).

In the case of our Poisson log-link model, for any set of predictions, if their mean is not the same as the target, we can improve the log-likelihood (and hence pseudo- $R^2$ ) by changing the intercept of the linear predictor (i.e., applying a multiplicative constant to the predictions) until the means are the same. To see this, we start with the log-likelihood, which was shown above to be

$$l_{model} = \sum_i y_i \log_e(\hat{y}_i) - \sum_i \hat{y}_i.$$

We will express the linear predictor for each observation as

$$\eta_i = \beta_0 + z_i,$$

where  $\beta_0$  is the intercept (which is the same for all observations) and  $z_i$  is the rest of the linear predictor. Given the log-link, the log-likelihood can be rewritten as

$$l_{model} = \sum_i y_i(\beta_0 + z_i) - \sum_i \exp(\beta_0 + z_i).$$

To find the intercept which gives the maximum, we differentiate with respect to  $\beta_0$ :

$$\begin{aligned} \frac{\partial l_{model}}{\partial \beta_0} &= \frac{\partial}{\partial \beta_0} \left( \sum_i y_i(\beta_0 + z_i) - \sum_i \exp(\beta_0 + z_i) \right) \\ &= \sum_i (y_i - \exp(\beta_0 + z_i)) \\ &= \sum_i (y_i - \hat{y}_i). \end{aligned}$$

At the minimum, the above sum is zero, which means that the mean of the predictions is the same as the mean of the target. Hence, for any given set of predictions, if the mean of the predictions does not equal the mean of the target, the intercept can be

adjusted until it is, and the likelihood will improve.

In the case of our null model, rebasing makes sense. We know that performance should be zero and that differences in predicting the overall mean are driven by noise in the data and not any good or bad model performance. In the case of a more complex model, the ability to get closer to the mean of the validation data might be driven by a much more important issue. The mix of business by rating factor can change over time. If one model is better than another in understanding the differences in risk between different levels of rating factors, and the mix changes, then both at the risk level and at the overall level, performance will be better. This argument would suggest that when we are dealing with complicated models, we should not rebase. However, given that our validation folds are assigned at random, it would be very surprising if there were significant changes in the business mix between the folds.

In addition, a closer look at the means on training and validation data (not shown here) highlights another issue. The difference between these means can vary significantly and yet have only a small effect of pseudo- $R^2$ . It therefore seems that pseudo- $R^2$  is not necessarily a good way to check whether models are on average predicting correctly.

One approach is to first rebase the predictions to be correct on average and only then to use pseudo- $R^2$  to measure how close the model is to the target on each individual observation. The separate question of whether the model predicts correctly on average is easily measured by seeing how much rebasing was needed. If we find that a model with a better pseudo- $R^2$  on average needs more rebasing, we should certainly investigate this further.

We note that the above discussion mirrors the separation between basic and classification ratemaking. The overall price level is determined according to basic ratemaking methods, with its analysis of loss development, loss trends, premium trends, etc. The classification rates are determined separately, and the resulting rating factors are then applied to the base rate. Since the task of classification ratemaking is not concerned with estimating the correct overall rate level, but rather how much higher or lower a specific risk class is compared to that base rate, our evaluation of the models which estimate the classification rate should not be impacted by differences between the average prediction and the average observed value.

## 3.8. Next Steps

We are almost ready to start addressing some of our practical issues. First, though, in the next chapter, we recap the ideas behind penalized regression and refit our base-case models using this approach.
