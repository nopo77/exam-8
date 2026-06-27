---
paper: chalk_et_al
chapter: 9
title: Learning From Black-Box Models
topics: [permutation_feature_importance, partial_dependence_plots, interactions, gradient_boosting_machines, model_agnostic_methods, feature_importance, black_box_models]
key_formulas: [permutation_feature_importance, partial_dependence_plot, interaction_strength_measure]
---

> **TL;DR**
> - Permutation feature importance: randomly shuffle one feature column, measure performance drop; larger drop = more important feature. Model-agnostic and uses held-out data.
> - Partial dependence plot (PDP): set all records to a fixed value of a feature, average predictions, repeat for all values — shows marginal effect of one feature across the full data distribution.
> - Interaction detection: pl_A + pl_B − pl_{AB} > 0 indicates possible A-B interaction; top candidates from this ranking are inspected visually.
> - GLM vs GBM comparison on FAA-NTSB: feature importances mostly aligned, but nu_registered ranked 3rd in GBM vs. 11th–12th in GLM — suggests a missing interaction in the GLM.
> - Adding decision-tree leaf nodes from (GBM predictions / GLM predictions) as a new GLM feature improved pseudo-R² from 0.151 to 0.156.

# 9. Learning From Black-Box Models

Black-box models are machine learning models whose predictions are hard or impossible to explain. Our penalized GLM is a machine learning model which is easy to explain. Its predictions are the product of numbers which depend in a simple way on our original features. Our benchmark model, a gradient boosting machine, is close to impossible to explain. It is made from 1,000 decision trees, each tree having many decisions, each of which contributes in some small way to the final prediction. However, it performs better than our GLM. On the FAA-NTSB case study in Section 5.9, the performance of our GLM was about 10% lower than the performance of the gradient boosting machine (GBM). Our preference (and in many cases the regulator's) is for rating plans whose prices are easy to explain—such as those derived from GLMs and generalized additive models (GAMs). We also want to compare the GLM to the GBM and to learn from it if we can. In which ways are the models similar or different? Where we have taken a specific modeling approach—for example, regarding nonlinear effects—how do our predictions compare to the GBM? We do not want to sacrifice performance if we can avoid doing so. Can we find out how the GBM is outperforming our GLM and incorporate this into our model? We will look at three areas:

- Variable selection and importance
- Nonlinear effects
- Interactions

As we have made a significant effort to deal sensibly with the first two items, but have not dealt with the third at all, we expect that if we find ideas to increase the performance of our GLM, it will be with interactions. Nevertheless, we will check all three points.

We will not review the differences in the approach to HCCVs between the two models—because they are essentially the same. In fact, were it not for the fact that the GBM implementation we used has a built-in method for dealing with HCCVs, the approach would have been exactly the same, i.e., we would have created a target encoding independently of the type of model we were using and then used that encoding in both model types. We did however refit our GLM and the benchmark model without

the make-model HCCV discussed earlier—and the differences between the models were more or less unchanged.

The methods we will use in this chapter do not depend on the type of model we used as a benchmark. They would work equally well with random forests, a neural network, or any other model. Such methods are known as “model-agnostic.” (Methods which depend on the model type are called “model-specific” methods.)

Most of the ideas in this chapter are explained in detail in *Interpretable Machine Learning: A Guide for Making Black Box Models Explainable* (Molnar (2020)). In our work, we use only a small subset of the techniques mentioned there that are particularly useful to us as we cover the points above. For each area we discuss in this chapter, there are many other approaches. Our aim is to show generally the kinds of questions that can be asked, rather than to exhaustively provide answers (even if that were possible).

Before looking at the above three items, we will discuss one risk of learning from complex black-box models.

## 9.1. Model Variance Revisited

We saw in Figure 4.10 that, as penalization reduces, our GLM can get more and more complex and as a result might start to suffer from model variance. That is, it might adapt itself to pick up patterns in the training data which are not in the validation folds or in the test data. While it is always tempting to choose the model with the very best cross-validation performance, if this model has a large gap between training and cross-validation performance, then there is a risk that our pricing will include claims patterns for certain segments of our customers that are just random noise and will not be present in future data. In insurance settings, this is especially risky as it might lead to an increase in the proportion of our future customers in those segments and an overall poor performance.

The GBM benchmark that we have used is essentially a phenomenally complicated GLM. It allows numeric features to be built from an almost unlimited number of step functions, and it allows an almost unlimited number of interactions. In fact, if we engineered a very large number of step functions and interaction features, we could express our GBM in the form of GLM. Given its complexity, we should not be surprised if it does suffer from large variance; the equivalent GLM would too. As each tree gets added, the GBM gets more complex, so one way to see how model variance increases with complexity is to plot the train and cross-validation performance as the number of trees in the GBM increases. Figure 9.1 shows that there is a significant gap between train and cross-validation performance as the number of trees increases.

![Figure 9.1: A line graph showing performance versus the number of trees for a benchmark GBM. The x-axis is 'number of trees' (0 to 1000) and the y-axis is 'performance' (0.100 to 0.200). Two lines are plotted: 'train' (teal) and 'cv' (red). The 'train' line starts at ~0.105 and rises to ~0.200. The 'cv' line starts at ~0.105 and rises to ~0.165. The gap between them widens as the number of trees increases.](be982eabf91a49b9c815dae1f34a1cc7_img.jpg)

| number of trees | train performance | cv performance |
|-----------------|-------------------|----------------|
| 0               | 0.105             | 0.105          |
| 250             | 0.175             | 0.155          |
| 500             | 0.190             | 0.160          |
| 750             | 0.198             | 0.163          |
| 1000            | 0.200             | 0.165          |

Figure 9.1: A line graph showing performance versus the number of trees for a benchmark GBM. The x-axis is 'number of trees' (0 to 1000) and the y-axis is 'performance' (0.100 to 0.200). Two lines are plotted: 'train' (teal) and 'cv' (red). The 'train' line starts at ~0.105 and rises to ~0.200. The 'cv' line starts at ~0.105 and rises to ~0.165. The gap between them widens as the number of trees increases.

**Figure 9.1. The gap between train and cross-validation performance for the benchmark GBM. Even at performance levels of around 0.15 (achieved by our GLM), and certainly at higher levels, the gap is wide, suggesting that the GBM is picking up patterns in the training data which are not in the cross-validation partitions—it suffers from high variance.**

Given the above finding, if we attempt to incorporate patterns that the GBM has learned into our GLM we will need to monitor the variance of the GLM model and take appropriate action. These could include excluding patterns that increase variance or accepting the increased variance and putting processes in place to compare the mix of business written after implementation of the new rates to the mix of business in the training data.<sup>77</sup>

## 9.2. Variable Selection and Importance

We would like to know if we have included the right features in our GLM and haven't overlooked any important features from the benchmark model. This is not a straightforward question to answer. While the LASSO (for example) will completely exclude from the GLM the features that it does not select, tree-based and certain other non-GLM machine learning models often include all features. It is just that some of the features will play only a very small role in the value of the final predictions. (The reasons why some machine learning models tend to include all features are discussed briefly in Section 9.6.)

<sup>77</sup> This is something which should be done in any case.

Given the above, rather than asking which features are in our GBM, we ask which features are important to our GBM. We have previously seen that for a GLM, the magnitude of the coefficients for the standardized features can be considered as feature importance. This method is not available for GBMs—they do not have coefficients. Instead, the following simplified example shows how we can understand the importance of features in any model.

In our example, there are three insureds with ages 20, 30, and 40. Frequency is  $age/100$ , and there is no randomness. We also have the height of each insured but frequency does not depend on height. Our trained model has correctly worked out that  $freq = age/100$ . If we knew what resulted from our trained model, we would know that age was a very important feature and height was not at all important. If we don't know how our trained model works, we only have access to the predictions that it makes. So we first ask our model to create predictions on a dataset held out from its training—the results are shown in Table 9.1. The predictions are—unsurprisingly—perfect. For simplicity, our performance metric will be mean absolute error, which is clearly zero.

**Table 9.1. The start of our simple example to illustrate a type of variable importance calculation. We have the ages and heights of three insureds. Frequency is  $age/100$ . There is no randomness, and our trained model has learned the true relationship—though we do not know this or the form of the model that it has learned.**

| age | height | true frequency | num_cl | predictions | absolute error |
|-----|--------|----------------|--------|-------------|----------------|
| 20  | 1.4    | 0.2            | 0.2    | 0.2         | 0              |
| 30  | 1.5    | 0.3            | 0.3    | 0.3         | 0              |
| 40  | 1.6    | 0.4            | 0.4    | 0.4         | 0              |

We will now take our original data but randomly permute the age column and keep all other features—in this case, height—the same. The true frequency remains the same. We ask our model to provide predictions and, of course, this time the predictions are all wrong because the age data has been made rather useless by its being randomly permuted. The results are shown in Table 9.2, and the mean absolute error (MAE) is now 0.133. The increase to MAE, as a result of making the age feature useless, is 0.133.

**Table 9.2. Stage 2 of our simple example. We permute the age column, ask our model for a new set of predictions, and recalculate model performance.**

| age | height | true frequency | num_cl | predictions | absolute error |
|-----|--------|----------------|--------|-------------|----------------|
| 40  | 1.4    | 0.2            | 0.2    | 0.4         | 0.2            |
| 20  | 1.5    | 0.3            | 0.3    | 0.2         | 0.1            |
| 30  | 1.6    | 0.4            | 0.4    | 0.3         | 0.1            |

Next, we take our original data and randomly permute the height column and keep all other features—in this case, age—the same. The true frequency remains the same. We ask our model to provide predictions. This time the predictions are unchanged because our model does not depend on height (though we do not know this up front). The results are shown in Table 9.3, and the MAE is now zero. The increase to MAE, as a result of making the height feature useless, is zero.

**Table 9.3. Stage 3 of our simple example. We permute the height column, ask our model for a new set of predictions, and recalculate model performance.**

| age | height | true frequency | num_cl | predictions | absolute error |
|-----|--------|----------------|--------|-------------|----------------|
| 20  | 1.6    | 0.2            | 0.2    | 0.2         | 0              |
| 30  | 1.4    | 0.3            | 0.3    | 0.3         | 0              |
| 40  | 1.5    | 0.4            | 0.4    | 0.4         | 0              |

Finally, we have for each feature the amount of performance lost by making that feature useless by randomly permuting its column in our data. The worse the loss of performance from permuting a feature, the more important we say it is in our model. This type of feature importance is known as “permutation-based feature importance.” For convenience we divide each value by the maximum value so that the “most important” feature has a feature importance of 100 and all other values are relative to that amount.<sup>78</sup>

<sup>78</sup> We have introduced MAE here for simplicity. In any rating exercise we would expect the calculations done above to use the same performance metric being used in the rest of the rating exercise. For example, for feature importance calculations for our FAA-NTSB study we used pseudo- $R^2$ . In the final presentation of the feature importances one might then choose not to rebase to 100% as the raw pseudo- $R^2$  figures will show how the performance we are familiar with reduces as features are rendered useless.

**Table 9.4. The final stage of our simple example. The importance of each feature is the amount by which performance got worse when that feature was made useless by permuting it. For convenience we divide each value by the maximum value so that the “most important” feature has a feature importance of 100 and all other values are relative to that amount.**

| feature | increase to MAE | permutation-based feature importance |
|---------|-----------------|--------------------------------------|
| age     | 0.133           | 100                                  |
| height  | 0               | 0                                    |

The advantages of permutation-based feature importance are its ease of computation for any model and the fact that it requires only the ability to generate predictions for a dataset. Hence the approach is model-agnostic, i.e., it can be applied to any model. In addition, we have defined an “important” feature as one which helps the model to predict accurately. When applying this approach, we can use data which was not used to train the model, so an important feature is one which helps our model to predict accurately over future data—which is what we really care about. (Alternative approaches consider a feature important if changing it leads to big changes in predictions or if it is important in some way in the trained model itself—for example, did the model use it to make many splits in the tree?)

A disadvantage of this method is that, if our features are correlated, permuting only one column at a time may create observations which are impossible. For example, in our FAA data, engine type can be turboprop or jet. The power of turboprop is measured in horsepower and is included in `faa_eng_hp`. The thrust of jet engines is measured in lb of thrust and included in `faa_eng_thrust`. When we permute the engine type column only, we will end up with jet engine observations with horsepower measurements. We have not just made the contribution from the engine type feature useless, we have made the whole observation meaningless.<sup>79</sup>

We need to remember that we are finding the importance of features in our final trained model, not the importance of features left out of our final model. Imagine that an exceedingly important feature has been excluded. The above approach will give it an importance of zero. In our case, this is not an issue: we are using feature importance to compare the differences in importance between two different models. We are asking if there is an important feature in the GBM which has been left out of the GLM, not if

<sup>79</sup> A separate but related point is that it is often helpful to permute variables in groups. Groups are selected either due to correlation or because they cluster together logically. This formulation can be a useful addition to the basic permutation importances, since seeing the importance of variable groups (e.g., driver, vehicle, and policy level features in personal passenger auto insurance) provides insights not otherwise available.

there is a feature in the original data which has been left out of both models. We are also not determining the importance that the features in our final trained model could have had in some other model.

Consider two very highly correlated features, both in our final trained model, and our model generally uses one of them and not the other. The one which is used most will have a higher permutation-based feature importance, despite the fact that in another trained model it could have been left out completely in favor of the other.

Finally, we note a point which will become useful later. When we permute a column, we don't only make it useless. We make any interactions which rely on it useless. Hence, permutation-based feature importance for a given feature measures its importance both as a main effect and in any interactions in which it is involved.

We calculated permutation-based feature importance for our GLM and the benchmark GBM. The six least important features for our GLM are shown in Table 9.5. For comparison, we show at the top the most important feature. We can see that the GBM agrees that these features are relatively unimportant—all of them have an importance of less than 1% compared to region.

**Table 9.5. The six least important features for our GLM. Both feature importance values and ranks are similar to those of the GBM.**

| feature            | feature importance value |       | feature importance rank |      |
|--------------------|--------------------------|-------|-------------------------|------|
|                    | GLM                      | GBM   | GLM                     | GBM  |
| region             | 100.0                    | 100.0 | 1.0                     | 1.0  |
| street2_ind        | 0.07                     | −0.02 | 16.0                    | 20.0 |
| co_ownership       | −0.001                   | 0.08  | 17.0                    | 18.5 |
| co_owners_num      | −0.01                    | 0.23  | 18.0                    | 16.0 |
| faa_acft_type_acft | −0.02                    | 0.58  | 19.0                    | 13.0 |
| faa_acft_ac_weight | −0.06                    | 0.08  | 20.0                    | 18.5 |
| faa_acft_ac_cat    | −0.12                    | −0.05 | 21.0                    | 21.0 |

We note that none of the feature importances are exactly zero for the GLM. This is surprising given that it was penalized with the LASSO which carries out implicit feature selection. This is partly due to the data and GLMs we used to calculate feature importance, and this is discussed further in Section 9.5.1. Note also that some feature importances are negative. This suggests that we should consider refitting our GLM without these features. In our case, given that we have used a solid performance based approach to including features in our GLM, we would be inclined to believe that these negative values are likely related to randomness in our data and the disadvantage of permutation-based feature importance mentioned above (that it can create impossible observations).

Table 9.6 shows the 15 most important features for our GLM. Both feature importance values and ranks are similar to those of the GBM. However, there are some exceptions. In particular, the number of aircraft registered to the owner is much more important in the GBM than it is in the GLM; it is the third most important in the GBM, but only the 11th or 12th most important in the GLM.

**Table 9.6. The table shows the most important features for our GLM and GBM. Mostly they are similar; however, there are some exceptions. In particular, the number of craft registered to an owner (nu\_registered) is much more important in the GBM than it is in the GLM.**

| feature                 | feature importance value |       | feature importance rank |      |
|-------------------------|--------------------------|-------|-------------------------|------|
|                         | GLM                      | GBM   | GLM                     | GBM  |
| region                  | 100.0                    | 100.0 | 1.0                     | 1.0  |
| veh_age                 | 44.9                     | 47.6  | 2.0                     | 2.0  |
| type_registrant         | 2.7                      | 3.1   | 3.0                     | 4.0  |
| operation               | 2.6                      | 2.4   | 4.0                     | 6.0  |
| faa_acft_num_seats      | 2.0                      | 2.1   | 5.0                     | 7.0  |
| airworthiness           | 1.9                      | 1.4   | 6.0                     | 8.0  |
| faa_acft_speed          | 1.5                      | 2.8   | 7.0                     | 5.0  |
| faa_acft_num_eng        | 1.1                      | 0.7   | 8.0                     | 11.5 |
| faa_eng_thrust_char     | 0.7                      | 0.9   | 9.0                     | 10.0 |
| faa_acft_type_eng       | 0.6                      | 0.7   | 10.0                    | 11.5 |
| nu_registered           | 0.5                      | 4.0   | 11.5                    | 3.0  |
| faa_acft_build_cert_ind | 0.5                      | 0.3   | 11.5                    | 15.0 |
| faa_eng_type            | 0.4                      | 1.2   | 13.0                    | 9.0  |
| kit_indyn               | 0.3                      | 0.4   | 14.5                    | 14.0 |
| faa_eng_hp_char         | 0.3                      | 0.1   | 14.5                    | 18.0 |

Based on the above discussion, we conclude that we have not left out any features from the GLM that were important in the GBM. However, we have missed something with the feature for the number of aircraft registered to the owner. There are two possibilities here; we have incorrectly fitted the main effect, or there is an interaction between this feature and one or more of the other features which we need to add. We will cover these two points in the following sections.

Before moving on, we note that in our case, we only have a relatively small number

of features. In such cases, using feature importance to check on the feature selection does not necessarily add much value. In cases where there are large numbers of features (hundreds or thousands) this approach becomes increasingly useful as a reasonability check and in providing candidate features to add back to the GLM.

## 9.3. Nonlinear Effects

How can we compare the treatment of numeric features that affect our target variable in a nonlinear way? It is easy to plot the average prediction over our training data for each value of the feature. We can do this for both the GLM and GBM and compare the graphs. Figure 9.2 shows the average predicted frequencies for the number of aircraft registered to the owner. We have capped the values shown on the x-axis at 30—the actual values above this are sparse and extend beyond 3,000. The predictions from the two models are mostly similar (especially for values where the proportion of exposure is high), though predictions from the GBM are lower for values of `nu_registered` between 11 and 15. While the GBM may indeed be correct (we will discuss this further below), given the limited amount of exposure, it is unlikely to be the reason why this feature has a much larger importance in the GBM.

![Figure 9.2: A line graph comparing the average predicted frequencies from the GLM and GBM models for the number of aircraft registered to the owner. The x-axis is labeled 'number of craft registered to this owner' and ranges from 0 to 30. The y-axis is labeled 'predicted frequency' and ranges from 0.004 to 0.009. The GLM model is represented by a solid black line, and the GBM model is represented by a dashed red line. The two lines are very close for most values, but the GBM prediction is notably lower than the GLM prediction for values between 11 and 15. Both models show a peak in predicted frequency around 15-16 aircraft.](1c958d1f6c82fbd64f82db2646372715_img.jpg)

| Number of craft registered | GLM Predicted Frequency | GBM Predicted Frequency |
|----------------------------|-------------------------|-------------------------|
| 0                          | 0.0046                  | 0.0046                  |
| 5                          | 0.0053                  | 0.0053                  |
| 10                         | 0.0067                  | 0.0065                  |
| 11                         | 0.0060                  | 0.0056                  |
| 12                         | 0.0062                  | 0.0056                  |
| 13                         | 0.0063                  | 0.0051                  |
| 14                         | 0.0085                  | 0.0070                  |
| 15                         | 0.0060                  | 0.0067                  |
| 16                         | 0.0067                  | 0.0067                  |
| 17                         | 0.0053                  | 0.0051                  |
| 18                         | 0.0063                  | 0.0064                  |
| 20                         | 0.0058                  | 0.0058                  |
| 25                         | 0.0050                  | 0.0050                  |
| 30                         | 0.0045                  | 0.0045                  |

Figure 9.2: A line graph comparing the average predicted frequencies from the GLM and GBM models for the number of aircraft registered to the owner. The x-axis is labeled 'number of craft registered to this owner' and ranges from 0 to 30. The y-axis is labeled 'predicted frequency' and ranges from 0.004 to 0.009. The GLM model is represented by a solid black line, and the GBM model is represented by a dashed red line. The two lines are very close for most values, but the GBM prediction is notably lower than the GLM prediction for values between 11 and 15. Both models show a peak in predicted frequency around 15-16 aircraft.

**Figure 9.2. A comparison of the average predictions from the GLM and GBM. Values shown on the x-axis are capped at 30—the last point including exposure for all craft with `nu_registered`  $\geq$  30. Predictions from the GBM are lower for values of `nu_registered` between 11 and 15, but it would be surprising if this difference, applying to only a limited amount of exposure, explains why this feature should have a much larger importance in the GBM.**

The above approach does not isolate the impact that the feature has on the predictions. For example, the average prediction where the feature is 30 or more depends not only on the feature, but also on the values of all other features for owners who have 30 or more craft registered under their name. We therefore consider a different way of visualizing how predictions depend on a feature.

For GLMs, especially where there are no interactions, we can very easily isolate the impact of a given feature on the predictions—it is expressed by the value of the coefficients. The GLM we are using in this chapter uses step functions for nonlinear effects, and the linear predictor for `nu_registered` is calculated as follows:

$$\begin{aligned} \text{linear predictor} = & -0.0001407 \times \text{nu\_registered} \\ & + 0.02936 \text{ if } \text{nu\_registered} \geq 2 \\ & + 0.07342 \text{ if } \text{nu\_registered} \geq 7 \\ & - 0.15822 \text{ if } \text{nu\_registered} \geq 16 \\ & - 0.17117 \text{ if } \text{nu\_registered} \geq 35 \end{aligned}$$

Taking the exponent gives us the relativities. Figure 9.3 shows the relativities, rebased to be one for `nu_registered` = 1. We can see that the overall shape is made up of four different levels arising from the four step functions, plus a small negative slope (which would be more apparent if we extended the x-axis to higher values). The impact on predicted frequencies is easy to see and easy to challenge, and indeed we would certainly challenge and likely adjust such relativities before their use in a rating plan.

![Figure 9.3: A line graph showing the scaled coefficient (y-axis) versus the number of craft registered to the owner (x-axis). The y-axis ranges from 0.95 to 1.10. The x-axis ranges from 0 to 30. The graph shows a step function with four distinct levels: 1.00 for 0-1, approximately 1.03 for 2-6, approximately 1.11 for 7-15, and approximately 0.94 for 16-30.](456fe8467b753cfa618c7e24c055b5fa_img.jpg)

| Number of craft registered | coefficient (scaled) |
|----------------------------|----------------------|
| 0                          | 1.00                 |
| 1                          | 1.00                 |
| 2                          | 1.03                 |
| 6                          | 1.03                 |
| 7                          | 1.11                 |
| 15                         | 1.11                 |
| 16                         | 0.94                 |
| 30                         | 0.94                 |

Figure 9.3: A line graph showing the scaled coefficient (y-axis) versus the number of craft registered to the owner (x-axis). The y-axis ranges from 0.95 to 1.10. The x-axis ranges from 0 to 30. The graph shows a step function with four distinct levels: 1.00 for 0-1, approximately 1.03 for 2-6, approximately 1.11 for 7-15, and approximately 0.94 for 16-30.

**Figure 9.3. The relativities for `nu_registered` in our GLM.**

The GBM does not have coefficients, so we cannot provide a graph for it on the same basis. We therefore consider an alternative approach, first using our GLM as an example and then applying it to our GBM. We know from the above graph that (compared to  $\text{nu\_registered} = 1$ ) the relativity for  $\text{nu\_registered} = 10$  is 1.107. If we did not know the GLM coefficients, we could still find this out using only our ability to calculate predictions. We first set  $\text{nu\_registered}$  to 1 for every policy in our data and calculate the prediction. The first few lines of our data are in Table 9.7.

**Table 9.7. Predictions from a GLM model having set  $\text{nu\_registered}$  to 1 for all policies.**

| nu_registered | faa_acft_num_seats | craft age | other features | pred    |
|---------------|--------------------|-----------|----------------|---------|
| 1             | 2                  | 1         | ...            | 0.00436 |
| 1             | 9                  | 3         | ...            | 0.00109 |
| 1             | 2                  | 18        | ...            | 0.00048 |
| 1             | 4                  | 0         | ...            | 0.00482 |
| 1             | 6                  | 27        | ...            | 0.00032 |
| Total         |                    |           |                | 0.01107 |

Next, we set the value for  $\text{nu\_registered}$  to 10 for every policy and again calculate the predictions. The revised predictions are shown in Table 9.8.

**Table 9.8. Predictions from a GLM model having set  $\text{nu\_registered}$  to 10 for all policies.**

| nu_registered | faa_acft_num_seats | craft age | other features | pred    |
|---------------|--------------------|-----------|----------------|---------|
| 10            | 2                  | 1         | ...            | 0.00482 |
| 10            | 9                  | 3         | ...            | 0.00120 |
| 10            | 2                  | 18        | ...            | 0.00053 |
| 10            | 4                  | 0         | ...            | 0.00533 |
| 10            | 6                  | 27        | ...            | 0.00036 |
| Total         |                    |           |                | 0.01225 |

Finally, Table 9.9 summarizes our results, showing the predictions for the two values of the feature and the ratio between them. Given that the GLM has no interactions and the only thing that changes is the value of  $\text{nu\_registered}$ , the ratio of the predictions on each line, and in total, must be the ratio of the relativities for  $\text{nu\_registered} = 1$  and  $\text{nu\_registered} = 10$ .

**Table 9.9. We divide the predictions from setting nu\_registered to 10 by those from setting nu\_registered to 1. This must be the ratio of the relativities for those two values, since nothing else has changed.**

| pred_1          | pred_10 | ratio |
|-----------------|---------|-------|
| 0.00436         | 0.00482 | 1.107 |
| 0.00109         | 0.00120 | 1.107 |
| 0.00048         | 0.00053 | 1.107 |
| 0.00482         | 0.00533 | 1.107 |
| 0.00032         | 0.00036 | 1.107 |
| Ratio of totals |         | 1.107 |

We repeated this exercise for every value of nu\_registered, and indeed the resulting relativities and graph are identical to that produced from the coefficients above. Had there been interactions with nu\_registered in the GLM, then the ratio for each policy would depend not only nu\_registered, but also on whether or not it interacted with any level of any other feature for that policy. We could still take the ratio of the totals, however, and this would tell us, on average across all policies used in the calculation, how the predicted frequency changes when nu\_registered is increased from 1 to 10.

We now do exactly the same for our GBM. Unsurprisingly, the ratio on each line is different; however, we can still find the ratio of the mean predictions. The result is 1.104. While this is similar to the GLM, we will soon see that for values of nu\_registered other than 10, the values are quite different.

**Table 9.10. Predictions from the GBM, after first setting nu\_registered to 1 for all policies and then to 10. The ratio of the average predictions is 1.104—which is similar to that of the GLM.**

| unique_id_line     | pred_1   | pred_10  | ratio |
|--------------------|----------|----------|-------|
| 1                  | 0.00323  | 0.00389  | 1.206 |
| 2                  | 0.00132  | 0.00228  | 1.729 |
| 3                  | 0.00053  | 0.00075  | 1.412 |
| 4                  | 0.00330  | 0.00387  | 1.172 |
| 5                  | 0.00040  | 0.00051  | 1.285 |
| ...                | ...      | ...      | ...   |
| Average prediction | 0.005336 | 0.005892 | 1.104 |

Once again, we can compute the ratio for each value of nu\_registered. Because we look at how our model's predictions depend on just one or a small subset of the features, the approach is called “partial dependence” (Friedman (2001), Section 8.2). The plot of

the partial dependence values for the full range of our feature is known as a partial dependence plot (commonly known by the acronym “PDP”). Figure 9.4 compares the partial dependence plots for the GLM and the GBM. We can see that the two plots are quite different. The biggest difference is in the 11–15 range (although they also differ elsewhere), and we know from our previous discussion that in this range the GBM predictions are lower than the GLM predictions. A review of the step functions that were fed into the LASSO shows that due to the limited exposure in this range, there was no step in this range (there were step functions at `nu_registered` 2, 3, 5, 7, 10, 16, 35, and 283). While we don’t know at this stage whether or not the pattern the GBM has spotted will generalize to test data and future policies, we can certainly rerun the GLM with some extra detail in the step functions.<sup>80</sup>

![Figure 9.4: A comparison of the partial dependence plots for the GLM and GBM. The plot shows mean prediction (rebased to 1) on the y-axis (ranging from 0.8 to 1.1) versus the number of craft registered to the owner on the x-axis (ranging from 0 to 30). The GLM plot (teal line) shows a step function that increases from 1.0 to 1.1 at x=7, stays at 1.1 until x=15, then drops to 0.95 and remains constant. The GBM plot (red line) shows a more complex, non-linear relationship, starting at 1.0, peaking at 1.1 around x=10, then dropping sharply to 0.9 at x=12, and continuing to decrease to approximately 0.82 at x=30.](98625209e11b104f342bc4be17eb4360_img.jpg)

| Number of craft registered | GLM Mean Prediction | GBM Mean Prediction |
|----------------------------|---------------------|---------------------|
| 0                          | 1.00                | 1.00                |
| 2                          | 1.03                | 1.01                |
| 4                          | 1.03                | 0.97                |
| 6                          | 1.03                | 0.97                |
| 7                          | 1.11                | 1.01                |
| 9                          | 1.11                | 1.10                |
| 10                         | 1.11                | 1.08                |
| 11                         | 1.11                | 1.05                |
| 12                         | 1.11                | 0.90                |
| 14                         | 1.11                | 0.89                |
| 15                         | 0.95                | 0.88                |
| 17                         | 0.95                | 0.87                |
| 19                         | 0.95                | 0.85                |
| 21                         | 0.95                | 0.85                |
| 23                         | 0.95                | 0.84                |
| 25                         | 0.95                | 0.83                |
| 27                         | 0.95                | 0.82                |
| 29                         | 0.95                | 0.82                |
| 30                         | 0.95                | 0.82                |

Figure 9.4: A comparison of the partial dependence plots for the GLM and GBM. The plot shows mean prediction (rebased to 1) on the y-axis (ranging from 0.8 to 1.1) versus the number of craft registered to the owner on the x-axis (ranging from 0 to 30). The GLM plot (teal line) shows a step function that increases from 1.0 to 1.1 at x=7, stays at 1.1 until x=15, then drops to 0.95 and remains constant. The GBM plot (red line) shows a more complex, non-linear relationship, starting at 1.0, peaking at 1.1 around x=10, then dropping sharply to 0.9 at x=12, and continuing to decrease to approximately 0.82 at x=30.

**Figure 9.4. A comparison of the partial dependence plots for the GLM and GBM.**

In this section, we have seen how we can use our benchmark black-box model to check and if necessary adjust our GLM approach to numeric features with nonlinear effects. Before we move on, given that we have introduced partial dependence, we mention some caveats in its use. Firstly, as with our permutation-based approach to feature importance, simply changing all policies to take a given value of a certain feature can create impossible observations. More importantly, partial dependence is a global method—it averages the dependence of predictions on a feature over all observations in our data. The actual impact will almost certainly depend on other features (due to the myriad interactions present in most black-box models).

<sup>80</sup> This is an exercise left to the diligent reader.

For example, Table 9.10 shows a wide range of ratios of prediction values when `nu_registered` is changed from 1 to 10 (ranging from 1.172 to 1.729). Figure 9.5 shows a histogram of the ratios, and the red dashed line shows the ratio of the mean predictions, which is what we used in our partial dependence plot. The histogram makes very clear that ratios at the level of each observation span a wide range. Friedman (2001) cautioned the usefulness of the approach used here in exactly this situation.

The red dashed vertical line in the histogram is drawn at 1.104. As discussed above, this represents the ratio of mean predictions between `nu_registered` being set to 10 and 1. Our method of calculating this ratio effectively weights each observation by its predicted frequency. The fact that the red dashed line is so far to the left of the distribution is because the predictions for which the ratio is lower than 1.104 are in general far higher than for cases where the ratio is high. This again reminds us that partial dependence is a global method and the impact of a feature on various segments of the portfolio may be very different from that in the partial dependence plot.

![A histogram showing the density of ratios between catboost predictions where nu_registered is set to 10 compared to being set to 1. The x-axis is labeled 'ratio of mean predictions between nu_registered 10 and 1' and ranges from 0 to 4. The y-axis is labeled 'density' and ranges from 0.0 to 1.5. The histogram bars are dark gray. A red dashed vertical line is drawn at 1.104, which is to the left of the main distribution of ratios.](785ffdb80d7fb12f2eee04b161106715_img.jpg)

A histogram showing the density of ratios between catboost predictions where nu\_registered is set to 10 compared to being set to 1. The x-axis is labeled 'ratio of mean predictions between nu\_registered 10 and 1' and ranges from 0 to 4. The y-axis is labeled 'density' and ranges from 0.0 to 1.5. The histogram bars are dark gray. A red dashed vertical line is drawn at 1.104, which is to the left of the main distribution of ratios.

**Figure 9.5. A histogram of the ratios between catboost predictions where `nu_registered` is set to 10 compared to being set to 1. The red dashed line is drawn at 1.104, being the ratio of the mean predictions across the whole dataset. The histogram demonstrates that there is a very wide range to the ratios—quoting the global value of 1.104 can be very misleading when thinking about any one individual policy. The red dashed line is far to the left because policies with low ratios have much higher predictions and so have a bigger weight in the overall mean.**

Molnar (2020) presents various alternatives to partial dependence plots to deal with the challenges raised above, and we refer the interested reader to that excellent work. We, however, move on now to consider interactions.

## 9.4. Interactions

There are many ways to identify and fit interactions when fitting GLMs, and our work does not aim to cover this topic. However, we do wish to know whether the performance differential between the GLM and GBM is due to interactions being important in the GBM and being completely missed out from the GLM. We will briefly cover two points:

- Are there any interactions in our GBM which are particularly important?
- If we feed a basic approximation of the key interactions into our GLM as features, does its performance improve?

Given that we have introduced permutation-based feature importance above, we now introduce a somewhat simplistic method to use it to rank pairs of features to check for interactions. Since permutation-based feature importance is a model-agnostic method, so is this approach to checking models for interactions. Consider two features, A and B, which do not interact in our model in any way—neither with each other, nor with any other feature. When they are permuted, they reduce performance solely to the extent that predictions depended on them. Say that performance reduced by 1% for A and 1% for B. If they are now both permuted at the same time, performance will reduce by 2%. The sum of the loss of performance from their separate permutations minus loss of performance from permuting both features at the same time is zero.

Consider again two features, A and B, which are separately important but now also interact with each other. When we permute any one of them, we destroy not only its performance but also the performance due to the interaction. Say their own performance is 1% each and the performance due to the interaction is also 1%. In this case, when they are separately permuted, the loss of performance is 2% each time, and when they are jointly permuted, the loss of performance is 3%. Now the sum of loss of performance from their separate permutations, minus loss of performance from permuting both features at the same time, is 1%. (This argument also holds where both features interact with the same third feature but not with each other.)

Based on the above argument, if  $pl_A$  and  $pl_B$  are performance loss from separate permutations, and  $pl_{AB}$  is performance loss from joint permutation, then the extent to which

$$pl_A + pl_B - pl_{AB}$$

is positive indicates either that A and B may interact with each other or interact with a common third feature. Therefore we can rank all pairs of features by this measure and check the top few visually for interaction.

Programmatically, it is simple to permute each feature separately to find and then to also permute all combinations or two features and to find the difference as described above. Some of the calculations for interactions with aircraft age are shown in Table 9.11.

**Table 9.11. There are many possible pairs of features that may interact in our model. This table shows the calculations for three of them. The method used suggests interactions of aircraft age with region and nu\_registered.**

| feature_A       | feature_B    | $pl_{AB}$ | $pl_A$ | $pl_B$ | $pl_A + pl_B - pl_{AB}$ |
|-----------------|--------------|-----------|--------|--------|-------------------------|
| region          | aircraft_age | 0.291     | 0.253  | 0.135  | 0.096                   |
| nu_registered   | aircraft_age | 0.115     | 0.016  | 0.135  | 0.037                   |
| faa_eng_hp_char | aircraft_age | 0.123     | 0.002  | 0.135  | 0.014                   |

The results over all pairs of features are shown in Figure 9.6.

![Figure 9.6: A scatter plot showing the permutation-based interaction strength for all pairs of features, sorted by index. The y-axis is labeled 'Permutation based interaction strength' and ranges from -0.025 to 0.100. The x-axis is labeled 'Index' and ranges from 0 to 200. The plot shows a dense cluster of points at the top left, with the highest point at index 0 having a strength of approximately 0.096. The points generally decrease in strength as the index increases, with a few outliers at the bottom right.](cb99822a837a67a57268344e674782ea_img.jpg)

Figure 9.6: A scatter plot showing the permutation-based interaction strength for all pairs of features, sorted by index. The y-axis is labeled 'Permutation based interaction strength' and ranges from -0.025 to 0.100. The x-axis is labeled 'Index' and ranges from 0 to 200. The plot shows a dense cluster of points at the top left, with the highest point at index 0 having a strength of approximately 0.096. The points generally decrease in strength as the index increases, with a few outliers at the bottom right.

**Figure 9.6. This figure shows all pairs of features in our data, sorted according to the size of our permutation-based interaction strength measure. The top proposed interaction is between region and aircraft age.**

In a typical model-building exercise, we would now inspect, graphically or otherwise, the top few candidate interactions. Figure 9.7 shows an example of a graphic that might be used to inspect an interaction. Aircraft ages have been grouped into reasonably sized buckets, and region (being the location of the registered owner) has been grouped into two groups: the US and elsewhere. The y-axis shows the percentage error in predictions for each bucket (based on actual claims/predicted claims).

![Line graph showing prediction percentage error vs aircraft age for two regions: N (Not outside USA) and Y (Registered owner address outside USA). The Y-axis ranges from -30 to 60. The X-axis ranges from 0 to 10. The N line starts at -15, dips to -10, then rises to 30 at age 12, and continues to rise. The Y line starts at 15, dips to 0, rises to 10 at age 4, then falls to -10 at age 8, and continues to fall to -25 at age 14.](8dcd1fcee82515ccd7ff79fa67508e3a_img.jpg)

| Aircraft Age | Region N (Error %) | Region Y (Error %) |
|--------------|--------------------|--------------------|
| 0            | -15                | 15                 |
| 2            | -10                | 0                  |
| 4            | -10                | 10                 |
| 6            | 0                  | 0                  |
| 8            | 5                  | -10                |
| 10           | 15                 | -5                 |
| 12           | 30                 | -5                 |
| 14           | 45                 | -25                |

Line graph showing prediction percentage error vs aircraft age for two regions: N (Not outside USA) and Y (Registered owner address outside USA). The Y-axis ranges from -30 to 60. The X-axis ranges from 0 to 10. The N line starts at -15, dips to -10, then rises to 30 at age 12, and continues to rise. The Y line starts at 15, dips to 0, rises to 10 at age 4, then falls to -10 at age 8, and continues to fall to -25 at age 14.

**Figure 9.7.** This figure is an example of how we might inspect our data to see if there is an interaction between region and aircraft age. Aircraft ages have been grouped into reasonably sized buckets, and region (being the location of the registered owner) has been grouped into two groups: US and elsewhere. The y-axis shows the percentage error in predictions for each bucket (based on actual claims/predicted claims). It can be seen that there might be benefit in allowing the interaction into our GLM so that at lower aircraft ages, predictions are higher for regions outside the US and lower for regions in the US—and the opposite at higher ages.

We have now seen how we can get a list of candidate interactions from our black-box model and shown briefly how we might inspect them further. Each candidate interaction needs separate checking and fitting with the GLM—depending on how this is done, it can be a fair amount of work. It would be useful to have a quick way to check in advance of all this work whether inclusion of interactions will improve the performance of our GLM. A fairly simple way to do this is based on decision trees. A single decision tree divides our data into separate pieces using a limited number of interactions. Each observation that we ask our decision tree to predict on will be given a leaf number, and the prediction will be the average of all the training data that was sent to that leaf. We will not be interested in the decision tree predictions, but the leaf numbers—each of which represents an interaction—are useful. We therefore start by dividing our black-box predictions by the GLM predictions. Any differences will be mainly due to the interactions in the GBM.<sup>81</sup> We then model these differences using a simple decision tree. An example of an interaction represented by one leaf in the resulting tree is shown below:

<sup>81</sup> A tree model estimates all effects as interactions, including effects which aren't interactions. Any main effect the GLM missed will be picked up by the tree, and the tree's leaf node then may, or may not, represent a real interaction effect. In our case, we have checked that the GLM has not missed out on any main effects, and we therefore expect leaf nodes to represent interactions.

```

node number: 24
root
nu_registered >= 22
aircraft age <= 3
region = X (outside the US)

```

For this subset of observations, the black-box predictions are 65% lower than those of the GLM. However, we are more interested in the interaction itself—we want to feed this into our GLM. We can create a new feature in our training data which labels each observation with the leaf number that it falls into. We use this new feature as the only feature in a penalized GLM (with our original GLM predictions as an offset). Using cross-validation as normal, we find that our GLM pseudo- $R^2$  improves to 0.156. While this still falls 6% short of our gradient boosting benchmark (pseudo- $R^2$  of 0.165), it suggests that with further effort, we should be able to improve our GLM performance using correctly selected and fitted interactions.

This brings us to the end of our discussion on how we can check our work using black-box models and how we can bring insights from them back into our GLM framework.

## 9.5. Practically Speaking

### 9.5.1. Feature importance—train or test data

As discussed above, as our models get more complex, there is a risk that patterns are found in the training data which will not be present in future data. If a feature is important on training data, it does not mean that it will be important for performance on future data. To know which features are important in the final model which is trained over all of our training data, we should base importance on predictions and performance over our test data. However, during modeling, we do not want to look at the test data. Therefore, the permutation-based feature importance reported in this chapter were based on the models created during our cross-validation process. For each of these, we calculated feature importance of all features on the held out fold. If we have 10 folds, then we have 10 cross-validation models, and for each feature we end up with 10 estimates of its importance. The feature importances that we reported above are, for each feature, the average of the importances across all folds. The importances for the LASSO are not exactly zero for any feature because there is no feature which was penalized out of all of the cross-validation models.<sup>82</sup>

---

<sup>82</sup> When using the LASSO it is certainly possible that some features will be penalized out of all the cross-validation models, and then their feature importances would indeed be exactly zero when calculated in the manner discussed here.

## 9.6. Technical Note

### 9.6.1. *Reasons that certain model types include all features*

The reasons why some machine learning models tend to include all features are specific to the various model types. In random forests, each single tree can be—and often is—overfit. This ensures that any one tree has low bias. The averaging over many trees reduces the variance and can potentially result in a good ensemble. Since each tree is overfitted, each tree is likely to contain most of the features that it was allowed to use. GBMs are made up of hundreds or even thousands of trees, each one taking a small step in the direction of the optimal solution given all the trees that came before it. These small steps will often pick up some of the noise in the dataset, and hence, for any feature, there are likely to be at least some trees that contain that feature. Neural networks learn their weights by iteratively increasing the magnitude of weights to connections that improve performance and reducing the magnitude of weights to those that reduce performance. Features which are not important will tend to end up with low weights rather than zero weights.

