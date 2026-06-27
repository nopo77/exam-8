---
paper: chalk_et_al
chapter: 6
title: High Cardinality Categorical Variables (HCCVs)
topics: [high_cardinality_categorical_variables, target_encoding, bühlmann_credibility, generalized_linear_mixed_models, leakage, one_hot_encoding, hierarchical_grouping]
key_formulas: [target_encoding_formula, credibility_weight, ridge_regression_hccv_estimate]
---

> **TL;DR**
> - Target encoding: x'_k = (ȳ_k − ȳ) / (λ/n_k + 1); this is a credibility-weighted estimate shrinking toward the overall mean. Multiplicative form uses AvE ratio (ȳ_k/ȳ).
> - The λ parameter plays the role of Bühlmann's k ≈ within-group variance / between-group variance; for FAA-NTSB aircraft makes, estimated λ ≈ 648.
> - Leakage prevention: for each cross-validation fold, compute the target encoding using only the out-of-fold training data; compute a final encoding on all training data for test/scoring.
> - GLMMs treat the HCCV as a random effect, producing similar shrinkage behavior to target encoding but extending naturally to hierarchical structures (e.g., model within make).
> - Sense-check encoded values: very rare categories with one claim produce extreme AvE ratios; ad hoc adjustments to credibility are appropriate for stable, defensible rating plans.

# 6. High Cardinality Categorical Variables (HCCVs)

## 6.1. Introduction

Generalized linear models (GLMs) require every feature to be in numeric form. This is because there is always a stage whether in training the model or in creating predictions where each feature is multiplied by a numeric coefficient. However, in the GLM that we built in the last section, there are 15 categorical variables—such as the type of aircraft, type of engine, and type of registrant. For example, two of the engine types are

- Turboprop<sup>26</sup> (code “2”)
- Rotary<sup>27</sup> (code “11”)

and our fitted model does have coefficients for these:  $-0.09$  for turboprop engines and  $3.58$  for rotary engines. Since the GLM could not take the codes or descriptions of engine type as features, the software we are using first created additional numeric columns to deal with these features, and it was these features that it provided to the GLM fitting process. For example, it created a column called “faa\_eng\_type.11,” which is 1 whenever the engine type is rotary and zero otherwise. It did the same for all other engine codes and also for all levels of any other factors. The extra columns are sometimes called dummy variables, and this process is known as one-hot encoding. The 15 categorical features in this model had between them 99 levels. To represent these levels, the GLM model matrix used 84 columns of 0/1 indicators. One level from each categorical feature does not require a separate column as it is captured by the intercept.<sup>28</sup> In the full FAA-NTSB data there are 2 million rows, and the 84 new columns of the model matrix require 900MB of memory. Actually, since the new columns consist only of zeros and ones, we can use a sparse way of storing the matrix, which only stores the ones and the extra storage required reduces

---

<sup>26</sup> Turboprop engines are fitted on fixed-wing craft and use a gas turbine to drive a propeller.

<sup>27</sup> Light engines with a high power-to-weight ratio. In our data, these are often used in home-built or custom-built aircraft.

<sup>28</sup> When fitting non-penalized GLMs, this approach is required. When using penalized regression, all 99 levels can be used.

to 90MB. In our data there are 97 different countries, 16,304 different cities, and over 40,000 different makes of aircraft. These are referred to as HCCVs because they have a large number of levels.<sup>29</sup> If we were to use the same one-hot encoding approach for these variables, we would need a large amount of memory. Given that this is not a particularly large dataset and HCCVs could be far bigger cardinality than this, the memory issues are potentially significant.

In this chapter, we discuss methods for handling HCCVs. The central idea is to shift from representing each HCCV level with a separate column (resulting in hundreds or even thousands of columns) to encoding each level with one or a small number of values (leading to just one or at least only a small number of columns).

## 6.2. Target Encoding

If the one-hot approach to HCCVs would create models that performed well on future data and there was absolutely no other way to deal with the issue, then we would certainly find a way to overcome the large memory requirements seen above. For example, we can train models on one row of the data at the time (this is known as online learning). We, therefore, further consider the impact of using one-hot encoding for HCCVs.

Adding a huge number of one-hot features to our data and then using unpenalized regression is likely in general to encourage overfitting and to lead to unreliable parameter estimates for levels of the feature which have few observations. If we were to use penalized regression, then these problems could possibly be overcome. Consider the simple case of Gaussian regression with an identity link function and using only one feature, which is an HCCV. A small amount of algebra (see Section 6.8.1) suggests that, given the one-hot approach, it is not unreasonable to use the following coefficient for the  $k$ 'th one-hot column (which is the one-hot representation of the  $k$ 'th level of the HCCV):

$$\beta_k = \frac{(\bar{y}_k - \bar{y})}{\frac{\lambda}{n_k} + 1} \quad \text{for } k = 1, 2, \dots, p, \quad (6.1)$$

where  $\beta_k$  is the coefficient,  $n_k$  is the number of ones in the one-hot column (which is the same as the number of observations in level  $k$ ), there are  $p$  levels (where  $p$  is large),  $\bar{y}$  is the overall average response,  $\bar{y}_k$  is the average response for the  $k$ th group, and  $\lambda$  is the

---

<sup>29</sup> There is no particular dividing line for when to use one-hot encoding and when to use the methods discussed in this chapter. In fact, some software have a parameter for the number of levels below which one-hot encoding is used and at or above what another method will be used. The optimal level for this parameter can be chosen by cross-validation.

regularization parameter chosen by cross-validation. The predictions would then be

$$\bar{y} + \frac{(\bar{y}_k - \bar{y})}{\frac{\lambda}{n_k} + 1},$$

which can be rearranged as

$$\frac{\frac{\lambda}{n_k}}{(\frac{\lambda}{n_k} + 1)} \bar{y} + \frac{1}{(\frac{\lambda}{n_k} + 1)} \bar{y}_k.$$

The outcome of this approach seems reasonable. For example, assuming that  $\lambda$  is fairly high, if we have only one observation for a given level of the factor, the coefficient for this group will be shrunk to close to zero, and the prediction will be the estimate of the overall mean. However, if we have a very large number of observations in a group, the coefficient for that group will be close to the difference in the mean level of the response for that group and the overall mean.

The formula for predictions, being a weighted average of the overall mean and the mean for each level, with the weight on the mean for a level increasing with the number of observations, is familiar to us as a credibility estimate. We show in Section 6.8.2 that the penalization parameter plays a similar role to the ratio of the “between group variance” to the “within group variance.” (An early version of this estimator is known as the James-Stein estimator and is discussed in the very interesting note by Efron and Morris (1977).) There is, however, a clear difference in the approach. In the credibility theory, the ratio of variances<sup>30</sup> is assumed to be the optimal parameter. Here, we do not claim to know, a priori, what is optimal. We find  $\lambda$  which optimizes average cross-validation performance. So long as our validation data is representative of future data and is large enough to give stable results, we may end up with better generalization performance than the traditional credibility approach.

While the manner in which we derived the above simple result does not apply where there is more than just the one HCCV feature in the penalized regression or for cases besides the Gaussian identity link, the general idea of some amount of shrinkage between the overall mean and the group mean, depending on the number of observations in each level of the factor, will be preserved.

Based on the above, besides the huge memory problems, it seems like penalized regression would deal with HCCVs well. However, there is another issue. The  $\lambda$  which we need to be using to deal with the HCCV might not be the same level of penalization

<sup>30</sup> In Empirical Bayes Credibility/Nonparametric Credibility one estimates the expected value of the process variance and the variance of hypothetical means from the data.

required to optimally deal with all the other features which are not HCCVs. This could possibly be dealt with using a versions of penalization discussed in Section 4.6.6, such as the adaptive LASSO or the grouped LASSO. Overall, it seems that using the one-hot approach with penalized regression would lead to reasonable results, but it might present some significant technical or practical problems along the way.

Given Equation 6.1, it does seem that we can achieve results very similar to one-hot penalized regression on HCCVs in a different way. For each level of the categorical feature,  $x_k$ ,  $k = 1, \dots, p$ , we replace  $x_k$  by

$$x'_k = \frac{(\bar{y}_k - \bar{y})}{\frac{\lambda}{n_k} + 1} \quad \text{for } k = 1, 2, \dots, p$$

and use this feature in the penalized regression.<sup>31</sup> This simple approach resolves all the technical challenges mentioned above. In our FAA-NTSB case, this would be very simple, for each make of aircraft we calculate the difference between average frequency for that make and the overall average frequency, shrink it towards zero, and then use those values as a new feature in the model.

This type of encoding is often called “Target Encoding” or “Mean Encoding.” Care needs to be taken when using software with such methods to make sure that there is some credibility adjustment, since implementations will often only replace the HCCV with the mean response (e.g., the mean accident frequency in our case). We note also that where there is a natural hierarchy, the complement of credibility can be chosen to reflect it. This is discussed further in Section 6.4.3.

The discussion above was based on an additive model. In the absence of significant credibility for level  $k$ , we shrink the value of the target encoded feature for level  $k$  ( $x'_k$ ) to zero. We can be more explicit about the shrinkage towards zero by adding a term where zero is the complement of credibility and it is multiplied by 1 minus the credibility factor. Equation 6.1 then becomes

$$x'_k = \left( \frac{\frac{\lambda}{n_k}}{\frac{\lambda}{n_k} + 1} \right) \times 0 + \left( \frac{1}{\frac{\lambda}{n_k} + 1} \right) \times (\bar{y}_k - \bar{y}) \quad \text{for } k = 1, 2, \dots \quad (6.2)$$

In a multiplicative world, in the absence of significant credibility, we shrink the value

<sup>31</sup> Note the difference in the letter used in this formula compared to the almost identical formula 6.1. Previously the formula gave a suggestion as to what might be a reasonable coefficient to be fitted to a one-hot column representing the  $k$ 'th level of our HCCV. That is why 6.1 uses  $\beta_k = \dots$ . Here, we are creating a new feature, hence the use of the letter  $x'$ . With appropriate choices for  $\lambda$ , it may turn out that the value for the  $k$ 'th level of the new feature is similar to the coefficient that it would have been fitted as the  $k$ 'th one-hot column in a GLM.

of the target encoded feature for level  $k$  to one. This suggests that we replace the equation above with

$$x'_k = \left( \frac{\frac{\lambda}{n_k}}{\frac{\lambda}{n_k} + 1} \right) \times 1 + \left( \frac{1}{\frac{\lambda}{n_k} + 1} \right) \times (\bar{y}_k/\bar{y}) \quad \text{for } k = 1, 2, \dots \quad (6.3)$$

If our target,  $y$ , is the number of claims, then  $(\bar{y}_k/\bar{y})$  is the ratio of average claims frequency in group  $k$  to the overall average claims frequency.  $(\bar{y}_k/\bar{y})$  is an example of the ratio of actual to expected experience since  $\bar{y}_k$  is the actual experience for the group and  $\bar{y}$  is the expected experience for the group (under a simple intercept-only model). We will refer to this as the actual versus expected (AvE) ratio. If level  $k$  has a high AvE ratio and a large number of observations, it will be represented by a high value of the target encoded feature.

An alternative formulation to 6.3 is to shrink the log of the AvE ratio towards zero

$$\log(x'_k) = \left( \frac{\frac{\lambda}{n_k}}{\frac{\lambda}{n_k} + 1} \right) \times 0 + \left( \frac{1}{\frac{\lambda}{n_k} + 1} \right) \times \log(\bar{y}_k/\bar{y}) \quad \text{for } k = 1, 2, \dots$$

In the case study in Section 6.6, we will be using the log of the target encoded feature in the GLM. This formulation gives that log directly and is potentially better suited to its use in this context.

In any case, when using the log of the target encoded feature with the log link function, then the multiplicative contribution of this feature to the prediction is  $x_{te}^{\beta_{te}}$ , where  $\beta_{te}$  is the coefficient fitted to the target encoded feature.<sup>32</sup>

There remains the practical issue of how to choose  $\lambda$ . This is discussed in Section 6.6.

## 6.3. Leakage

We give our GLM various useful features like aircraft age, make, and model, and we essentially ask the GLM to find a function which takes these inputs and to provide as an output the estimate of the claims frequency. This function is not necessarily going to be very accurate, but we expect that on future data it will perform better than a naive or baseline model. In order to help the GLM get accurate results during training, we could just give it a new feature which, for each observation, is the value of the target it is trying

<sup>32</sup> See Goldburd et al. (2025) Figure 1 and Section 2.4.1 which states: “When a log link is used, it is often appropriate to take the natural logs of continuous predictors before including them in the model, rather than placing them in the model in their original forms.” In our case, if  $\beta_{te}$  ends up being close to 1, then the final relativity for each level of the target encoded feature is close to its (shrunk) AvE. This seems reasonable and is an outcome which is easy to communicate to underwriters.

to predict. In this case the GLM would get perfect results during training by ignoring all other features and just setting the prediction to be equal to the target variable which we have given it. This model would be totally useless—it could not actually make a prediction on future observations since for future observations we don't yet know the value of the target. And any useful relationships between the other features and the target will not be picked up because the GLM can get a zero training error just using the one target feature that we gave it.

Allowing the GLM to see the target or part of the target during training is called leakage. And given that it is guaranteed to make our model less good, we try to avoid it.

In the above approach (target encoding), we have introduced leakage. We allow the GLM to see the average value of the target for each level of the HCCV. While this is not quite as bad as allowing the GLM to see the value of the target for each observation, it is not far off—since for HCCVs many of the factors may only have one observation or a small number of observations. The solution to this is that for observations in any one of our validation folds, we only allow the target encoding to use observations from all the other folds.

For example, consider the aircraft manufacturer (known as “make” in our dataset). This is certainly an HCCV, having over 40,000 levels in our dataset. If for one of the makes, we have six aircraft split into three folds as in Table 6.1, then the target encoded feature for fold 1 is the average frequency for folds 2 and 3, which is  $\frac{3}{4} = 0.75$ . Likewise the feature value for fold 2 is  $\frac{2}{4} = 0.50$  and for fold 3 it is  $\frac{1}{4} = 0.25$ .

**Table 6.1. Target encoding for each fold.**

| fold | accidents | across other folds |           |           |
|------|-----------|--------------------|-----------|-----------|
|      |           | aircraft           | accidents | frequency |
| 1    | 0         | 4                  | 3         | 0.75      |
| 1    | 0         | 4                  | 3         | 0.75      |
| 2    | 0         | 4                  | 2         | 0.50      |
| 2    | 1         | 4                  | 2         | 0.50      |
| 3    | 1         | 4                  | 1         | 0.25      |
| 3    | 1         | 4                  | 1         | 0.25      |

We end up therefore with a separate target encoding for each fold. In the above example, the target encoding for fold 1 is estimated only using data from the other two partitions. We now create a model using the data from folds 2 and 3 and the target encoding for fold 1. We can now safely validate performance on fold 1 data, since the target encoding used did not see fold 1 data.

By the time we are finished training our model, we will have one column on the training data which is a target encoding of the HCCV. However, its value for a given make

will depend on the fold the observation is in. When we wish to predict on test data, we need a single value for the target encoding for each make. We therefore create one final target encoding on all the training data, which we can then use when doing any final tests of our model.

Table 6.2 shows the raw accident frequency (before credibility adjustments) for some aircraft makes based on all training folds and also the raw frequencies we would use for folds 1 to 3 (e.g., the frequencies shown for fold 1 are calculated excluding the aircraft in fold 1). We can see that the accident frequency for the aircraft with more exposure in our dataset is fairly stable but for those with less exposure there is some variance depending on which fold we leave out. However, we can see that even when there is some variance, there is also consistency—the accident frequency for Socata is consistently high and that for Learjet is consistently low.

**Table 6.2. Raw accident frequency (before credibility adjustments) for some aircraft makes.**

| faa_acft_make          | ex     | train     | train frequency excluding |        |        |
|------------------------|--------|-----------|---------------------------|--------|--------|
|                        |        | frequency | fold_1                    | fold_2 | fold_3 |
| CESSNA                 | 440577 | 0.0046    | 0.0045                    | 0.0046 | 0.0046 |
| PIPER                  | 277902 | 0.0046    | 0.0046                    | 0.0046 | 0.0046 |
| BEECH                  | 108464 | 0.0045    | 0.0045                    | 0.0044 | 0.0045 |
| BOEING                 | 45257  | 0.0040    | 0.0040                    | 0.0042 | 0.0039 |
| MOONEY                 | 30744  | 0.0033    | 0.0033                    | 0.0034 | 0.0034 |
| WACO                   | 4181   | 0.0022    | 0.0025                    | 0.0022 | 0.0020 |
| AIRBUS INDUSTRIE       | 4164   | 0.0041    | 0.0048                    | 0.0034 | 0.0036 |
| SOCATA                 | 4075   | 0.0066    | 0.0060                    | 0.0069 | 0.0069 |
| EMBRAER                | 4069   | 0.0020    | 0.0020                    | 0.0023 | 0.0014 |
| ENGINEERING & RESEARCH | 4051   | 0.0012    | 0.0014                    | 0.0014 | 0.0009 |
| LEARJET INC            | 3877   | 0.0015    | 0.0012                    | 0.0018 | 0.0015 |

## 6.4. Some Other Encoding Approaches

### 6.4.1. Grouping rare categories

A much simpler approach than target encoding is to combine categories that appear infrequently into a single “Other” category. This approach will reduce the number of categories so that we can safely revert to one-hot encoding and penalized regression. It also avoids us having to explicitly choose the credibility weighting part of the target encoding. If most of our data is in a small number of categories and the rest of our data very sparsely populates a large number of other categories, this approach will group together levels of

the factor for which our credibility adjustment would probably have been zero anyway.

In grouping rare categories, the practitioner may be able to use their own domain knowledge to determine which levels “belong” together, e.g., should all rare makes from the same country or continent be grouped together and kept separate from rare makes from other countries or continents?

The idea of grouping rare levels as suggested here may also be used to improve the results from target encoding. When target encoding is used on a rare level, the credibility adjustment will lead it to be encoded at the value of the complement of credibility. If domain knowledge is used to group similar rare levels into a larger category, the resulting group may be a reasonable size and the target encoding will be able to reflect the experience of the group.<sup>33</sup>

### 6.4.2. Frequency encoding

In various machine learning and modeling software that deal with HCCVs, an approach called frequency encoding is included. It does not address our key issue, which is how does each individual level of the HCCV relate to our target variable? We do include it here, though, for completeness and in case it is encountered during modeling.

In frequency encoding we replace each category with the proportion of the training data that belongs to that category. Table 6.3 shows this type of encoding on our data; the feature `faa_acft_make` (which a GLM cannot use directly) is turned into `faa_acft_make_fe`, a numeric feature, which the GLM can use.

**Table 6.3. Frequency encoding of aircraft make. 25.88% of the aircraft are Cessna, 16.21% are Piper, and so on. The GLM can directly use the numeric feature `faa_acft_make_fe`.**

| <code>faa_acft_make</code> | <code>faa_acft_make_fe</code> |
|----------------------------|-------------------------------|
| CESSNA                     | 0.2588                        |
| PIPER                      | 0.1621                        |
| PILATUS AIRCRAFT LTD       | 0.0020                        |
| DASSAULT AVIATION          | 0.0019                        |
| SMITH                      | 0.0009                        |

While frequency encoding does not solve our original problem, it might provide a useful feature. For example, the appearance of a make of aircraft very infrequently in our dataset may imply something about the riskiness of the aircraft or of the type of people who choose to fly such an aircraft.

<sup>33</sup> In workers compensation, for example, very small classes are often grouped with other classes for ratemaking purposes and are thus charged the same rate.

### 6.4.3. Hierarchical grouping

Micci-Barreca (2001) discuss cases where the HCCVs have some hierarchy. They give various examples:

- Zip codes sharing the same first three digits are typically located within the same metropolitan area.
- Standard Industry Codes (SIC), which are used to classify commercial organizations based on their primary line of business. For example, code “4512 – Air Transportation, Scheduled” is part of major group “45 – Transportation By Air,” which itself is part of group “4 (known as division E) – Transportation, Communications, Electric, Gas, And Sanitary Services.”
- The first three digits of a telephone number often represent a natural grouping, such as an area or a specific service (such as a toll-free number).

Even where a formal hierarchy does not exist, the practitioner may be able to use domain-specific knowledge to create one.

Once we have a hierarchy, we could simply replace the HCCV with the broader categories and then use them as one-hot features in a GLM. However, we can do better than that. We can continue with the target encoding approach above but use as a complement of credibility not the overall mean, but the mean of the value encoded for a higher level of the HCCV, which has more data. Micci-Barreca (2001) discuss approaches to hierarchical HCCVs in more detail.

If we are going to use a hierarchy, especially as a complement of credibility, we need to be exceedingly careful that it is meaningful in the correct way. For example, consider manufacturer (make) and model of motorcycle when creating rates for motorcycle insurance. This is certainly a hierarchy—each model belongs to the category of its manufacturer. However, in terms of helping to predict the target variable using this hierarchy, it would be a very bad idea. Yamaha manufactures the YZF-R1 and YZF-R6, which are high-performance sport bikes. It also manufactures mopeds and scooters used for commuting, such as Yamaha Vino and Yamaha Jog. In a dataset used for rating, the average performance for Yamaha will be the average across their full range (to the extent it is in the data). Imagine now that only a small number of the high-end sport bikes are insured. Their credibility factor will be low, and if we use manufacturer as the complement of credibility, their final rate will reflect the average Yamaha performance and will be much too low.<sup>34</sup>

---

<sup>34</sup> In a few years, after significant insurer losses (due to adverse selection), the majority of Yamaha bikes in the portfolio will be high-end sports bikes and the price will finally be corrected.

### 6.4.4. *Feature creation and word embeddings*

In this section, we give an outline of two methods that can be used when the practitioner is faced with an HCCV. If an approach along these lines seems promising for a given line of business and HCCV, one could first apply it and then use target encoding in a second stage. The idea of splitting modeling into two stages is discussed in Chapter 8.

Target encoding is a supervised learning approach—it explicitly looks at the target variable in our data. The approaches outlined here create additional features, manually or automatically, without directly looking at our data, and then use these columns in a GLM.

As an example, consider insuring businesses against the risk of fire, where SIC is one of our features. We can ask risk engineers and other domain experts to explain the key drivers of fire claims and their cost. We might find that they can be split between the risk of inception of a fire and the risk of spread of a fire. We might further find that inception risk is greatly increased for businesses which use application of heat in their processes (main street restaurants as opposed to a main street clothing stores). Likewise, the risk of spreading a fire can be significantly increased for businesses that store combustible materials or those that create dust as part of some process. Further discussions might lead to 10 questions which seem to be most important in driving the frequency or severity of fire claims. These questions can then be asked of domain experts for each SIC code.<sup>35</sup> We now include in the GLM 10 new features—the responses to the 10 questions, but not the HCCV itself. It is highly likely that these will be predictive.

Another non-supervised approach is based on “word embeddings.” These are the backbone of any neural network which involves language (for example, large language models). Each word is represented as a vector. The vectors are derived so that words used in similar contexts have vectors which are close together in some way and are known as word embeddings. Today, the most advanced large language models make their underlying word embeddings available, and it is therefore relatively simple to get the word embeddings for every make or model of aircraft. The embeddings we use here each consist of 1,536 numbers (dimensions), and in Table 6.4, we show the first three numbers for three different aircraft.

---

<sup>35</sup> In the past, these conversations were time intensive and required the collaboration of a wide range of experts from around the business. Today, with appropriate prompts, large language models can sometimes create draft output relatively quickly.

**Table 6.4. The first three numbers (dimensions) in word embeddings for the three aircraft listed.**

| make   | model          | position_1 | position_2 | position_3 |
|--------|----------------|------------|------------|------------|
| PIPER  | PA-28 Cherokee | −0.021193  | −0.007403  | −0.006449  |
| PIPER  | CUB            | −0.021803  | −0.012660  | 0.014906   |
| CESSNA | Skyhawk        | −0.013765  | 0.000489   | −0.003003  |

A measure called “cosine similarity” can be used to check whether two vectors are similar. For this measure, an outcome close to one means the vectors are similar (point in the same direction), and an outcome close to zero means that they are very different. In our case, the output is 0.131 when comparing the Piper Cherokee to the Piper Cub and 0.108 when comparing the Cherokee to the Cessna Skyhawk. This does not seem particularly useful as the Piper Cherokee is actually more similar to the Cessna Skyhawk (in landing gear and usage) than it is to the Piper Cub.<sup>36</sup>

Given the (long) word embeddings, we can apply principal component analysis to represent their key features in a smaller number of dimensions. Finally, we can use these features in a GLM. There is no guarantee that these features—having been derived in an unsupervised manner—will help our GLM to pick up the key aspects of the underlying HCCV. However, this approach and the previous more manual approach have proven useful to the authors in some cases.

## 6.5. Generalized Linear Mixed Models

Generalized linear mixed models (GLMMs) are discussed in Goldburd et al. (2025), Section 10.1, and in West et al. (2022).<sup>37</sup> In this section, we first motivate the need for GLMMs with examples from various lines of business. We then briefly revisit how they are formulated and finally consider how we can use them as a solution to modeling HCCVs.

The fitting of GLMs relies on an independence assumption: the value of the target variable ( $y_i$ ) for one observation must not influence or depend on the value of the target variable for any other observation (e.g.,  $y_j$ ) in the dataset, given the model’s parameters (coefficients). This assumption is crucial because it allows the model to be applied to each observation individually and it underpins the use of techniques like maximum likelihood estimation. Consider the following lines of business:

<sup>36</sup> The generation of word embeddings is complex and understanding what their 1,000 or more dimensions represent is hard. The overall process described here is therefore somewhat opaque. Nevertheless if the resulting features are useful, we can ask an underwriter to sense-check them and provide adjustments as needed.

<sup>37</sup> At the time of writing, *Linear Mixed Models: A Practical Guide to Using Statistical Software* (West et al. (2022)) is required reading for MAS II.

- An insurance product which covers high-net-worth individuals who own and drive many cars. Our dataset consists of one line per car. Each line of data contains significant information about the type of car and also a unique identifier for the individual. If a high-net-worth individual owns 10 cars, then 10 observations will have that person's unique identifier.
- Fleet insurance: A product which provides auto cover for a pool of cars which companies provide to their employees. The cars in each company's pool are varied, and our data contains one line of information for each car within each company but limited or no information is available about the drivers. A unique company identifier is associated with each company. If one company has 100 cars in its fleet and was insured for three years, then 300 observations will have that company's unique identifier.
- The same as Fleet insurance above, but now there is a unique identifier for each company and also for the division within the company.

In all of the above cases, can we use a linear model or a GLM to find the coefficients for the features associated with the car? Yes. Clearly, we can. There is nothing to stop us. The question is: should we, though?

Imagine that we have fitted a model to all the features about the cars. Consider a company for which we have 100 observations. Were we to look at 50 of those observations and find that the residuals are high, does that tell us anything about the other 50 observations? Yes, it does. It suggests that the employees of that company are higher risks than average and therefore that the other 50 observations will also have high residuals. This means that, given the coefficients, the target variables are not independent between observations. The independence assumption that we mentioned above is not met.

To overcome the above problem, we could add the company identifier (or the company and division identifiers) into the GLM. This would of course be an HCCV because we insure many companies and the identifier takes a different value for each company. This leads us immediately to another problem. If we want to insure a new company that we have not insured before, our historic data will not have the unique identifier for that company, and so we cannot rate new companies. We can get around this, too, but all of these problems suggest that a different approach is warranted.

We can model the features for car in the normal way but treat the impact of the company on the level of risk as a random effect which varies from company to company. This random effect will increase or decrease the intercept term for each company but will not affect the coefficients for the vehicle features. If we build our model in such a way that this random effect has a mean of zero, then for future companies, in the absence of information and experience about the company, it will be reasonable to assume that the random effect is zero.

In the above model, the coefficients for the vehicles are not considered random. They are the same across every observation and are known as fixed effects. Overall, then we have a mix of fixed effects and random effects in the same model. Such models are known as linear mixed-effects models.

In these types of models—known as (generalized<sup>38</sup>) linear mixed models—the resulting behavior of the coefficient for the HCCV is similar to target encoding, i.e., it is pulled towards the central tendency of the response, in proportion to the quantity of the data in the level of the HCCV. However, while the effect might resemble target encoding, the underlying mechanics and statistical reasoning are different. Additionally, there are practical tools and software available that implement these models and thus they can be used as a useful check on target encoding results.

Given  $p$  fixed effects (e.g.,  $p$  features that we know about each car) and an intercept term  $\beta_0$ , we add the random effects ( $a_k$ ) to our model specification as follows:

$$\begin{aligned}y_{ik} &= \beta_0 + \beta_1 x_{1k} + \beta_2 x_{2k} + \cdots + \beta_p x_{pk} + a_k + \epsilon_{ik} \\a_k &\sim \mathcal{N}(0, \sigma_{company}^2) \\ \epsilon_{ik} &\sim \mathcal{N}(0, \sigma^2),\end{aligned}$$

where  $a_k$  is the random effect for company  $k$  and is distributed with a normal<sup>39</sup> distribution mean 0 and variance  $\sigma_{company}^2$ .

Historically in random-effects models, statisticians were not necessarily interested in the value of the fitted random effects. They just wanted to make sure that they were dealing with the structure of the dependency between observations correctly. In the above example, we would certainly be interested in the values of the fitted random effects, as it would inform the rate for renewals of existing clients. Fortunately, open-source software is available which fits these models and provides estimates of both fixed and random effects.

Given the above, we can treat aircraft make as a random effect, and we will then get estimates for the impact of aircraft make on frequency from the fitted random effects. We could also treat the aircraft model as a random effect within each aircraft make.<sup>40</sup>

<sup>38</sup> The difference between linear mixed models (LMMs) and generalized linear mixed models (GLMMs) is analogous to the difference between linear models (LMs) and generalized linear models (GLMs).

<sup>39</sup> A reason for using the normal distribution for random effects is that we have no a priori belief on how the experience for individual companies will be different from average performance, but we expect some to be worse than average and some better in a symmetric way.

<sup>40</sup> As per our previous discussion in the section on hierarchical grouping, this is not necessarily a sensible thing to do.

## 6.6. Case Study—HCCVs

As part of our FAA-NTSB case study, we applied both target encoding and GLMMs to our HCCVs to see if this would improve performance. We had hoped for a large performance improvement, but cross-validation performance was only slightly improved. Real-life data does not always do what we expect it to.<sup>41</sup> The authors have found that, in practice, dealing properly with HCCVs does normally improve performance, and we therefore proceed to demonstrate these approaches on our case study, using aircraft make and model as an example. (For our target encoding approach, we used overall means and not make as the complement of credibility.) The main effort in target encoding is to find an appropriate level for  $\lambda$ , and we now discuss this in some detail.

As mentioned above and as we will show below in the technical section, the  $\lambda$  parameter in the target encoding section can be thought of as the ratio of the “within group variance” to the “between group variance.” (In Bühlmann credibility, the terms used are “variance of hypothetical means” and “process variance”; and the ratio is referred to as Bühlmann’s  $k$ .)

“Within group variance” is the variance of the random number of accidents (for one aircraft over one year) for aircraft within a given make and model. We can get a rough idea of the magnitude of this by reasoning that the number of accidents for one aircraft is a 0-1 Bernoulli random variable<sup>42</sup> and that the typical mean accident rate is the overall mean accident rate in our training dataset, which is 0.004584. The mean of the binomial distribution with probability  $p$  is  $p$  and the variance is  $p \times (1 - p)$ , therefore the variance is  $0.004584 \times (1 - 0.004584) = 0.004562987$ .

“Between group variance” is the variance of the true differences in mean accident frequency between aircraft makes and model. For example, if we only had three aircraft (equally common in our data) and we knew that, compared to the average frequency, they have accident frequencies of 0.1% less, the same, and 0.1% more, then the between group variance would be the variance of the three numbers  $-0.1\%$ ,  $0$ , and  $+0.1\%$ . If we knew the true group means we could easily calculate this variance—but then we would not be doing all this work to estimate them (i.e., our target encoded HCCV will essentially be our best estimate of the group means). However, given that we already have a GLM which generates predictions excluding make, we can find the mean residual by make. If

<sup>41</sup> A while back, a colleague told one of the authors that the predictions from an analysis should be used because the method was statistically sound. Cross-validation is a harsh taskmaster and gives us an additional framework within which to carefully consider whether our models will improve performance. On the other hand, we should not be slave to cross-validation performance—this is discussed further in the final chapter.

<sup>42</sup> Equally, if we are concerned about the very small number of craft which actually had more than one accident in a year, we could stick with our Poisson assumption and assume a variance equal to the mean. The difference is small.

we had a huge number of observations for each make and model, these mean residuals would be a reasonable estimate of the effect of make on accident frequency. We don't have a huge number of observations for each, but we can take only those makes for which we have a reasonable number of observations. Doing this gives an estimate of the between group variance of  $7.038492 \times 10^{-6}$ .

Finally, the ratio of within group variance to between group variance is

$$0.004562987 / (7.038492 \times 10^{-6}) = 648.$$

This gives an idea of the magnitude of  $\lambda$ . This would mean, for example, that if we have 1,000 aircraft-years of experience for a make, then we would give  $\frac{1000}{1000+648} = 0.61$  credibility to claims experiences for that make.

If we simply used  $\lambda = 648$ , we would now calculate the target encoded feature for each fold and then run our GLM including all our previous features and the new target encoded feature. In general, though, we prefer to use our cross-validation procedure to choose the best features and best models, so instead, we carry out a model fitting process for a range of values of  $\lambda$  (4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384),<sup>43</sup> and for each value we calculate the average validation performance. The result is shown in Figure 6.1. It can be seen that performance improves (slightly) compared to the model without HCCVs. The dashed vertical line shows the performance at  $\lambda = 648$ . We can see that this is, in fact, close to the best average cross-validation performance, but the best improvement is for  $\lambda = 1024$  (or 2048).

The actual feature we used in our GLM was the log of the target encoding discussed above. Given the log link we have

$$\log(\text{predicted frequency}) = \text{intercept} + \dots + (\beta_{te} \times \log x_{te}),$$

where  $x_{te}$  is the target-encoded feature and  $\beta_{te}$  is the fitted coefficient.

Taking the exponent of both sides, we have

$$\text{predicted frequency} = k \times \dots \times x_{te}^{\beta_{te}},$$

where  $k$  is the exponent of the fitted intercept.

<sup>43</sup> The values were chosen simply to span a significant range, with our estimate of 648 somewhere in the middle. If a graph of the results would have shown the need for more details in one area of this range, we would have rerun the analysis accordingly.

<sup>43</sup> The results of using credibility are relatively insensitive to misestimates of  $K$ . See "An Actuarial Note on Credibility Parameters" by Mahler (1986).

![Figure 6.1: A line graph showing performance improvement (%) on the y-axis (ranging from 0.2 to 0.4) versus lambda (λ) on the x-axis (logarithmic scale with values 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384). The curve rises from approximately 0.15% at λ=4 to a peak of about 0.45% at λ=1024 and λ=2048, then declines to about 0.35% at λ=16384. A dashed vertical line is drawn at λ=648, indicating a point near the peak performance.](d00a62f7383d6fbf52a233df5ab63e70_img.jpg)

| $\lambda$ | Performance Improvement (%) |
|-----------|-----------------------------|
| 4         | 0.15                        |
| 8         | 0.17                        |
| 16        | 0.19                        |
| 32        | 0.21                        |
| 64        | 0.25                        |
| 128       | 0.30                        |
| 256       | 0.35                        |
| 512       | 0.42                        |
| 1024      | 0.45                        |
| 2048      | 0.45                        |
| 4096      | 0.42                        |
| 8192      | 0.38                        |
| 16384     | 0.35                        |

Figure 6.1: A line graph showing performance improvement (%) on the y-axis (ranging from 0.2 to 0.4) versus lambda (λ) on the x-axis (logarithmic scale with values 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384). The curve rises from approximately 0.15% at λ=4 to a peak of about 0.45% at λ=1024 and λ=2048, then declines to about 0.35% at λ=16384. A dashed vertical line is drawn at λ=648, indicating a point near the peak performance.

**Figure 6.1. The percentage increase in performance when including the target encoded aircraft make and model feature using different values for  $\lambda$ . The dashed vertical line shows the performance at  $\lambda = 648$ . This is close to the best average cross-validation performance but  $\lambda = 1024, 2048$  are slightly better (see footnote).**

In practice we often find that, if we have carried out the target encoding process correctly and there are no data issues, then the value of  $\beta_{te}$  associated with optimal cross-validation performance is not far from 1. We also expect that as  $\lambda$  increases,  $\beta_{te}$  increases. We therefore inspected the  $\beta$  coefficient in the GLM for the target encoded feature as a function of  $\lambda$ .

Figure 6.2 shows the coefficients for each value of  $\lambda$ . As we expected, we see that  $\beta_{te}$  increases as  $\lambda$  increases. Optimal cross-validation performance is around  $\lambda = 1024$  or  $\lambda = 2048$ , and the associated value of  $\beta_{te}$  are 0.4 and 0.5. Increasing  $\lambda$  to 4096 would produce a coefficient closer to 1 but would lose performance as cross-validation performance is not flat near the maximum.<sup>44</sup> Therefore we proceeded with  $\lambda = 2048$ . The target encoded feature was included in the GLM, and the average cross-validation performance increased from pseudo- $R^2$  0.150 to 0.151.

<sup>44</sup> Usually, given that the  $\lambda$  associated with the best cross-validation performance is somewhat lower than 1, we would inspect our data to see if any levels of the HCCV have large amounts of exposure relative to the others and are dominating the fitting process. In our case, the actual changes in performance (rather than the percentages) are all rather small and so we have not investigated further.

![Figure 6.2: A line graph showing the fitted coefficient for the target encoded feature versus the regularization parameter lambda. The x-axis is labeled lambda and has values 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, and 16384. The y-axis is labeled 'coefficient for target encoded feature' and has values 0, 1, 2, and 3. A vertical dashed line is drawn at lambda = 2048. The curve starts near 0 for small lambda and increases as lambda increases, passing through the value 1 at lambda = 2048.](a05ad7b3a9ed890d8ef5f717f1b912b1_img.jpg)

| $\lambda$ | Coefficient for target encoded feature |
|-----------|----------------------------------------|
| 8         | 0.05                                   |
| 16        | 0.08                                   |
| 32        | 0.10                                   |
| 64        | 0.12                                   |
| 128       | 0.15                                   |
| 256       | 0.20                                   |
| 512       | 0.25                                   |
| 1024      | 0.35                                   |
| 2048      | 0.55                                   |
| 4096      | 0.80                                   |
| 8192      | 1.20                                   |
| 16384     | 1.90                                   |
| 32768     | 3.20                                   |

Figure 6.2: A line graph showing the fitted coefficient for the target encoded feature versus the regularization parameter lambda. The x-axis is labeled lambda and has values 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, and 16384. The y-axis is labeled 'coefficient for target encoded feature' and has values 0, 1, 2, and 3. A vertical dashed line is drawn at lambda = 2048. The curve starts near 0 for small lambda and increases as lambda increases, passing through the value 1 at lambda = 2048.

**Figure 6.2. The y-axis shows the fitted coefficient for the target encoded feature. A value close to 1 would suggest that we used a reasonable level of credibility. The coefficient at  $\lambda = 2048$  is not close to 1.**

Section 6.5 introduced GLMMs. Open-source software is available which fits such models and provides estimates of both fixed effects and random effects. An advantage to the GLMM approach is that it extends naturally to dealing with hierarchical variations in risk, such as aircraft model within aircraft make. We therefore expected to be able to easily use this approach and that performance would be similar to the target encoding approach used above. In practice, we were not able to achieve consistent results using this approach. In particular, the software we were using gave error messages when fitting. Given that target encoding has the added advantage that it stays within our overall cross-validation framework and that its performance did exceed any of the GLMM models we were able to fit, we proceeded with target encoding.<sup>45</sup>

<sup>45</sup> We would, nevertheless, encourage the interested reader to try GLMMs in this and similar situations as they can be a very useful tool. They do also have the advantages being part of a statistically sound framework and of taking only a very small number of lines to code given the packages readily available for them.

## 6.7. Practically Speaking

### 6.7.1. Sense-checking the results and ad-hoc adjustments

Within an insurance company, pricing would be done by or in conjunction with people who understand the risks being dealt with. We can use the results of our encoding to highlight areas that need further research. In early work not presented above, we used target encoding at the level of make only. Table 6.5 shows the two highest and two lowest values for the target encoding. For this output, we would want to understand more about DJI: why do they have zero claims given the large amount of exposure. We research DJI and find out that they manufacture drones. We can then talk to subject matter experts to understand why they have zero accidents entered in the NTSB database and whether or not it makes sense to include their data in our analysis.

The two highest adjustments in Table 6.5 are cases which have one claim but only a small amount of exposure and, therefore, a very high AvE ratio. Taking “STUMP GREAT LAKES,” for example, the AvE ratio is 223.75. With  $z = \frac{12}{12+1024} = 0.011583$  the credibility calculation then gives the target encoding as  $1 \times (1 - 0.011583) + 222.22 \times 0.011583 = 3.58$ .

**Table 6.5. Examples of the output of target encoding aircraft make. ex and num\_cl are exposure and the number of claims, respectively. AvE ratio is the ratio of the GLM predicted frequency to the actual frequency. z is the credibility factor based on the value of  $\lambda$  that we chose. make\_te is the target encoded value. In 11,900 aircraft-years of exposure for the DJI make, there were no accidents. This compares to 3.692 accidents expected from the model. The credibility adjustment of 0.92 leads to a target encoding of 0.079, which then gets used in the GLM. Makes with one claim and very low exposure have a very high AvE ratio value, so that even though z is low, the value of the target encoded variable is very high.**

| aircraft make        | ex    | num_cl | AvE ratio | z      | make_te |
|----------------------|-------|--------|-----------|--------|---------|
| DJI                  | 11900 | 0      | 0         | 0.9208 | 0.079   |
| TEXTRON AVIATION INC | 5483  | 12     | 0.24356   | 0.8426 | 0.363   |
| MARLIN JOHN E        | 13    | 1      | 186.59373 | 0.0122 | 3.266   |
| STUMP GREAT LAKES    | 12    | 1      | 223.74936 | 0.0116 | 3.579   |

Now, imagine discussing with an underwriter why you have proposed to more than triple the rate for this make on the basis of seeing exactly one claim. You will try arguing that on average your approach is a good approach, but it will not be an easy conversation. While our approach works on average, there are some edge cases where we or others do

not feel comfortable in implementing the proposed outcomes.<sup>46</sup>

The approach we have taken is to make an ad hoc adjustment to the credibility given to the group mean where the expected number of claims is small (e.g., 0.005) and the number of claims is also small (e.g., 1).<sup>47</sup>

The edge cases can be driven simply by the randomness of claims experience (as in our case above), in which case a slight adjustment to the general approach seems reasonable. However, edge cases can also be driven by data quality or operational issues. For example, a system may by default give a driver who is not listed on a policy but who legally drives the car one day of exposure—simply because the true amount of exposure is not known and a default is needed. If this driver has a claim, the annualized frequency will be high. Across all such records, the frequency will be very high. The practitioner will need to deal with such situations on a case-by-case basis.

### 6.7.2. Target encoding using GLM predictions

We have discussed target encoding using as the actual versus expected ratio,  $(\bar{y}_k/\bar{y})$ , the ratio of the mean response for group  $k$  to the mean overall response. Given that we already have a GLM excluding the HCCVs, there is an alternative. We can calculate the predictions  $(\hat{y}_i)$  for each observation within a particular make and model and then calculate their average  $(\bar{\hat{y}}_k)$ . Finally, we proceed as above but using as the actual versus expected ratio,  $(\bar{y}_k/\bar{\hat{y}}_k)$ . As an example, say that the average overall frequency ( $\bar{y}$ ) is four accidents per thousand aircraft-years, but Bell helicopters (helicopters are included in the data) have an accident frequency of 16 accidents per thousand years of experience, then the first approach above would set the target encoding at 4<sup>48</sup>—which is very high. On the other hand, our GLM includes a feature that differentiates between fixed-wing and rotor-wing craft. This feature will have already picked up that helicopters generally have a high claims experience. It might therefore be that the average prediction for Bell helicopters is 20 per thousand. The target encoding on the second basis mentioned above would be 0.80.<sup>49</sup>

Intuitively, it feels right to first allow less complicated features, such as aircraft age and number of engines to pick up the key patterns, and then to allow the target encoded HCCV to pick up any remaining inaccuracies in the model predictions. However, it is certainly more work as we first need to fit a GLM, then create the ( $k$ -fold) predictions, and then fit another GLM.

<sup>46</sup> This is a general situation that can occur when applying credibility methods.

<sup>47</sup> The manner of this adjustment is not particularly important—we chose to reduce the exposure used in the credibility calculation so that it remained at zero until a certain threshold had been passed. The main point here is that a method that performs well on average can leave dangerous weak points in certain areas of the rating plan, and great care is needed.

<sup>48</sup>  $\bar{y}_k = 16$  and  $\bar{y} = 4$ .

<sup>49</sup>  $\bar{y}_k = 16$  and  $\bar{\hat{y}}_k = 20$ .

Our approach in the case study was indeed to create the target encoding using the GLM predictions. Indeed any eagle-eyed underwriters reading this paper might have noticed that the higher end of the target encoded variable did not include helicopters. Had we been using the overall mean as the expectation in our AvE ratio, helicopters would be likely to feature (since the actual frequency of helicopter accidents is much higher than the average accident frequency) (see Table 6.6).

**Table 6.6. Target encoding using the overall mean as the expectation in the AvE ratio. Helicopters tend to have higher frequencies than fixed-wing craft and indeed appear at the higher end.**

| faa_acft_make          | ex    | num_cl | AvE ratio | z      | make_te |
|------------------------|-------|--------|-----------|--------|---------|
| DJI                    | 11900 | 0      | 67.5796   | 0.9197 | 0.0803  |
| AERONCA                | 27451 | 45     | 136.2547  | 0.9640 | 0.3544  |
| ROBINSON HELICOPTER CO | 5693  | 122    | 30.4230   | 0.8475 | 3.5511  |
| ROBINSON HELICOPTER    | 7513  | 153    | 39.1231   | 0.8800 | 3.5615  |

### 6.7.3. Novel categories in the future

What happens if a new make of aircraft, which is not in our historic data, appears in the future and requires us to provide a rate? There will be no value for the target encoded feature for this make. One choice is to set the value of the target encoded feature to the average of value of this feature across all makes and to produce a quote. This would seem to be a particularly bad idea. If make is an important part of our rating, we are completely guessing that the right price for this make is the average price across all makes. There is no reason at all for this to be true. If the make is associated with high risk, we will leave ourselves open to massive adverse selection. It would seem far better to set up our systems not to offer a quote and to flag to the administrators that a new make of aircraft has been encountered. Discussions can then be had and deliberate value for the feature can be chosen based on similarities of the new make with existing makes.

### 6.7.4. What does zero mean?

What does zero mean for a target encoded feature? (Or a one in a multiplicative structure.) It can mean two very different things.

- That we have lots of exposure and, across this, the mean experience for the make is very close to the mean experience for all makes. We are very sure that the true experience of this make reflects the average experience.
- We have very little experience, and regardless of how experience for this make looks compared to average, we are ignoring it because we don't know if it is a fluke or not.

We are completely unsure as to whether the true experience of this make reflects average experience.

This is truly a problem. If we blindly use rates from target encoded HCCVs we run the risk of pretending that we understand all the types of risk when we are actually totally uncertain about some of them. A systematic and statistical approach to this would be to set our prices not at the mean predictions from our GLM but at some other (higher) percentile. More simply though, given that there are (hopefully) people in the insurance business who understand the risk, the derived rates and relativities should be discussed with them. This is particularly easy if there are existing rates for the make, as any significant changes (for makes with small amounts of exposure) can then be discussed.

### 6.7.5. *Keeping up with other ideas*

In order to keep up with ideas of how to approach HCCVs, it is useful to look at what is implemented in popular platforms. For example, Python’s scikit-learn package has a section called category encoders (sklearn\_category\_encoders) which implements (as of the date of writing) 20 approaches to encoding categorical variables. Simply reading the documentation for each of them gives a good overview of the types of approaches currently being used.

### 6.7.6. *Read the documentation*

Applying methods and functions written by third parties into open-source software like R and Python is easy. It is not always easy to understand what the software is doing. Reading the documentation helps. Sometimes documentation is not perfect, though, and some further digging is required. For example, at the time of writing this monograph, an alternative software has a method to create target encoding. An example of how it is called (from R) is:

```
target_encoder <- targetencoder(training_frame = df_,
x = 'faa_acft_make',
y = "resid",
fold_column = "fold",
data_leakage_handling = "Kfold",
blending = TRUE,
inflection_point = 500,
smoothing = 100)
```

We can quickly get a rough idea of what most of these arguments mean, but “inflection\_point” and “smoothing” are not clear. The documentation tells us that the inflection\_point “determines half of the minimal sample size for which we completely trust the estimate based on the sample at the particular level of the categorical variable” and

that “smoothing controls the rate of transition between the particular level’s posterior probability and the prior probability. For smoothing values approaching infinity, it becomes a hard threshold between the posterior and the prior probability.” This is more clear, but we have to dig into the code of the alternative software to find that the formula actually implemented is

$$z = 1.0/(1 + \exp((\text{inflection\_point} - n_k)/\text{smoothing})).$$

In Figure 6.3 we look at two examples of this function, compared to the credibility estimate we have been using. The solid black line is our usual formula  $\frac{n_k}{n_k + \lambda}$  where  $\lambda = 500$ . The dashed line shows the formula implemented with  $\text{inflection\_point} = 500$  and  $\text{smoothing} = 100$ . We can see that the size at which 50% credibility is given is the same, but the behavior elsewhere is quite different from our standard formula. If we increase the smoothing parameter to try to make the behavior more similar in the middle, we find that about 25% credibility is given where size = 0. Given that we would always hope that credibility tends to zero for group sizes close to zero, we should not automatically expect this formula to perform well. Indeed, various tests with different values of the arguments for this formula did not provide good average validation performance.

![Figure 6.3: A line graph comparing three credibility functions. The x-axis is labeled 'n_k' and ranges from 0 to 1000. The y-axis is labeled 'credibility factor (z)' and ranges from 0.00 to 1.00. The legend indicates three lines: a solid line for 'n_k / (n_k + 500)', a dashed line for 'smoothing=100', and a dotted line for 'smoothing=500'. The solid line starts at (0,0) and increases smoothly, passing through (500, 0.5). The dashed line starts at (0,0), remains near zero until n_k ≈ 250, then rises steeply to approach 1.0 as n_k increases. The dotted line starts at (0, 0.25) and increases gradually, passing through (500, 0.5).](b887c82301e35c9558c59ba20e72108d_img.jpg)

Figure 6.3: A line graph comparing three credibility functions. The x-axis is labeled 'n\_k' and ranges from 0 to 1000. The y-axis is labeled 'credibility factor (z)' and ranges from 0.00 to 1.00. The legend indicates three lines: a solid line for 'n\_k / (n\_k + 500)', a dashed line for 'smoothing=100', and a dotted line for 'smoothing=500'. The solid line starts at (0,0) and increases smoothly, passing through (500, 0.5). The dashed line starts at (0,0), remains near zero until n\_k ≈ 250, then rises steeply to approach 1.0 as n\_k increases. The dotted line starts at (0, 0.25) and increases gradually, passing through (500, 0.5).

**Figure 6.3. A comparison of the credibility function we have been using (solid back line) to a function implemented in one software for target encoding. We can see that the shapes are quite different.**

Overall, we see that it is always worth checking which formula are being implemented by the methods and functions we use.

### 6.7.7. *Are HCCVs really predictive?*

The risk of accident arises from the pilot (human error), the aircraft (failure of the machine), and the environment (e.g., the runway surface, weather, etc.). Many of the features that one might use are clearly linked to one (or more) of these sources of accident. For example, pilot age, flight hours on the same type of craft, total flight hours—all clearly link to the risk of pilot error. Aircraft make and model clearly link to the aircraft. However, if we also have in our model full details about the maintenance of the aircraft, its age, and the number of type of engines, we might think that there is no longer any need to include the make and model itself since every possible feature that directly describes the risk of failure of the machine is already in the model.

We nevertheless will always include the make and model (and other HCCVs) in our GLM. Essentially, we “let the data do the talking.” Regardless of what we might think, provided that we do actually want the best performing model, if average validation performance across all folds improves, we will be better off with aircraft make and model in the GLM. If performance does improve considerably it is worth trying to understand why. In particular, if we see that one level of an HCCV with significant volume is very predictive, we should check if it is due to one particular feature and then find a way to populate that feature across the whole dataset. Alternatively, that level of the HCCV may represent a class of risks which are so different from the rest of the data, they are best priced in a different model.

HCCVs can also be important because they pick up some residual information about the machine (or whatever they are describing) or because they are proxies for some other source of risk. A careful (or risky) person may tend to pilot certain makes and models of aircraft.

### 6.7.8. *Sense-checking the data*

We have been talking about there being over 40,000 (43,617 in fact) different makes of aircraft in our data. There are not 43,617 different manufacturers of aircraft. A quick look at the name of the make of craft for which only one has ever been built shows the names to be those of individual people. The field in our data “aircraft builder certification code” takes the value of “1: Not Type Certificated” for almost all these craft. These are amateur-built aircraft. The number of different makes including only the “0: Type Certificated” category reduces to 994, which seems more reasonable. Even within these data, there are some craft with only one record, however, the make seems to indicate a commercial manufacturer (e.g., AIRBUS HELICOPTER, BOEING/HUMM STAN-

LEY, CESSNA-LOOMIS-BUEHN, etc.).

Once again, therefore, our data preparation has let us down,<sup>50</sup> this time in two ways. Firstly we should have realized upfront that aircraft make includes many individuals rather than aircraft manufacturing companies. And even within the commercial manufacturers we might want to relabel some to group them together. For example, given that we saw AIRBUS HELICOPTER above, we then looked at the different makes with the name AIRBUS in them and we found: “AIRBUS,” “AIRBUS CANADA LP,” “AIRBUS CANADA LTD PTNRSP,” “AIRBUS DEFENCE AND SPACE LTD,” “AIRBUS DEFENSE AND SPACE S A,” “AIRBUS HELICOPTER,” “AIRBUS HELICOPTERS,” “AIRBUS HELICOPTERS DEUTSCHLAND,” “AIRBUS HELICOPTERS INC,” “AIRBUS INDUSTRIE,” “AIRBUS S A S,” and “AIRBUS SAS.” We might actually be happy for each of these “makes” to have different prices arising from different values of the target encoding—but we should certainly allow that only after discussing the data with a person who understands the different parts of AIRBUS.

## 6.8. Technical Note

### 6.8.1. HCCV estimates using Ridge regression

In this section, we derive the Ridge regression estimates of coefficients in a Gaussian regression with identity link where we have only one HCCV and no intercept.

Assuming our HCCV has  $p$  levels, we have  $p$  columns from the one-hot encoding, with each column having its own coefficient,  $\beta_1, \dots, \beta_p$ .

We can imagine sorting our data so that all the observations with level 1 of the factor come first. There are  $n_1$  of them with values  $y_{11}, y_{21}, \dots, y_{n_1 1}$ .

In general, for group  $k$  we have coefficient  $\beta_k$  and  $y$  values  $y_{1k}, y_{2k}, \dots, y_{n_k k}$ .

The loss function is essentially made up of the sum of squared errors of each level plus the penalty. Previously we have put the fraction  $\frac{1}{2n}$  before the sum of squares—this is typically done to simplify the algebra—it makes no difference to the solution path since  $2n$  is a constant. We could equally remove the  $\frac{1}{2n}$  fraction and multiply  $\lambda$  by  $2n$  and get the same solution. In this case, we will use a fraction  $\frac{1}{2}$  as the result will then look simpler.

---

<sup>50</sup> And we are reminded that an actuary needs to understand the data with which they are working. The actuary should understand the situation being modeled, with help from others when necessary.

$$\begin{aligned}
 l(\beta) = & \frac{1}{2} \sum_{i=1}^{n_1} (y_{i1} - \beta_1)^2 \\
 & + \frac{1}{2} \sum_{i=1}^{n_2} (y_{i2} - \beta_2)^2 \\
 & \dots \\
 & + \frac{1}{2} \sum_{i=1}^{n_p} (y_{ip} - \beta_p)^2 \\
 & + \frac{1}{2} \lambda \beta_1^2 + \frac{1}{2} \lambda \beta_2^2 + \dots + \frac{1}{2} \lambda \beta_p^2
 \end{aligned}$$

Only one of the  $\beta$ s appears in any one term, so when we differentiate with respect to any one  $\beta$  all the other terms disappear. For example, if we differentiate with respect to  $\beta_1$  we get

$$\frac{\delta l(\beta)}{\delta \beta_1} = - \sum_{i=1}^{n_1} (y_{i1} - \beta_1) + \lambda \beta_1.$$

Setting this to zero at the minimum gives:

$$\sum_{i=1}^{n_1} y_{i1} = (n_1 + \lambda) \beta_1$$

and

$$\hat{\beta}_1 = \frac{n_1 \bar{y}_1}{(n_1 + \lambda)}$$

i.e.,

$$\hat{\beta}_1 = \frac{\bar{y}_1}{(1 + \frac{\lambda}{n_1})}.$$

The same is true for any other coefficient, and so we have

$$\hat{\beta}_k = \frac{\bar{y}_k}{(1 + \frac{\lambda}{n_k})}.$$

As discussed in the main text, having no intercept is not a good idea. For some large  $\lambda$ , as we get fewer observations at one factor level, we would prefer to predict the overall mean and not zero. Hence, it seems reasonable to carry out the above penalized regression after first deducting the mean response from every value of  $y$ . This way, the coefficients

tell us how far the prediction for a level should differ from the overall mean, and we have

$$\hat{\beta}_k = \frac{(\bar{y}_k - \bar{y})}{(1 + \frac{\lambda}{n_k})},$$

and our prediction for group  $k$  is

$$\bar{y} + \frac{(\bar{y}_k - \bar{y})}{(1 + \frac{\lambda}{n_k})}.$$

This can be rearranged to give

$$\frac{\frac{\lambda}{n_k}}{(1 + \frac{\lambda}{n_k})} \bar{y} + \frac{1}{(1 + \frac{\lambda}{n_k})} \bar{y}_k.$$

As an aside, we note that the above is not what would result from including an unpenalized intercept term and carrying out penalized regression on the  $y$  values without deducting the mean. In that case the penalized regression would ensure that the one-hot coefficients summed to zero—and that is not the case for our solution above, where there are different numbers of observations for each factor (which is pretty much always).

### 6.8.2. *Link to the Bayesian approach*

In our approach to model fitting so far, we have thought of each individual coefficient (each separate  $\beta$ ) as a fixed value which we are trying to estimate. The penalization ensures shrinkage and/or feature selection. Although we do not discuss it in any detail here, it is known that carrying out a Bayesian regression with an appropriate prior on each coefficient separately and then choosing the maximum a posteriori (MAP) estimate will lead to the same estimates as Ridge regression or the LASSO (see for example the original LASSO paper, Tibshirani (1996), Section 5).

There is a similar Bayesian approach which is particularly useful for HCCVs. We start off with a prior belief that the true different levels of risk for each make of aircraft are independent and are distributed according to a normal distribution with mean zero and variance of  $\tau^2$ . We assume that the coefficients for each level of the HCCV are independent. Our prior is therefore

$$\beta_k \sim \mathcal{N}(0, \tau^2) \quad \text{for } k = 1, 2, \dots, p.$$

Consider a model where the only feature is the HCCV. Within each group, we have

$n_k$  observations  $y_{1k}, y_{2k}, \dots, y_{n_k k}$  which are distributed as follows:

$$\begin{aligned}y_{ik} &= \beta_k + \epsilon_{ik} \\ \epsilon_{ik} &\sim \mathcal{N}(0, \sigma^2) \\ \beta_k &\sim \mathcal{N}(0, \tau^2).\end{aligned}$$

Using Bayes' theorem,

$$Pr[\beta|y, X] = Pr[y|\beta, X] \frac{Pr[\beta|X]}{Pr[y|X]}.$$

Given that  $Pr[y|X]$  is some fixed constant and that the prior distribution of  $\beta$  does not depend on  $X$ , we have

$$Pr[\beta|y, X] \propto Pr[y|\beta, X]Pr[\beta].$$

Taking the log of each side and noting that  $Pr[y|\beta, X]$  is the likelihood of the observed  $y$ s given  $\beta$  and  $X$  (which we will refer to as  $L(\beta)$ ) we have

$$\log Pr[\beta|y, X] \propto \log L(\beta) + \log Pr[\beta],$$

where  $Pr[\beta|y, X]$  is the posterior distribution of the  $\beta$ s given the data.

Firstly, let us look at  $\log L(\beta)$ . Within any group ( $k$ ), given the value of  $\beta_k$ , the probability of the value  $y_{ik}$  is

$$\frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(y_{ik} - \beta_k)^2}{2\sigma^2}\right).$$

Ignoring constants and taking logs, for one observation,  $y_{ik}$ ,

$$\log L(\beta) \propto -\frac{(y_{ik} - \beta_k)^2}{2\sigma^2}.$$

Summing over all observations in each group and over all groups, we have

$$\log L(\beta) \propto -\frac{1}{2\sigma^2} \sum_{k=1}^p \sum_{i=1}^{n_k} (y_{ik} - \beta_k)^2.$$

As for  $\log Pr[\beta]$ , this is just the product of the  $p$  independent prior distributions for the  $\beta$ s and is  $\propto -\frac{1}{2\tau^2} \sum_{k=1}^K \beta_k^2$ .

Therefore

$$\log Pr[\beta|y, X] \propto -\frac{1}{2\sigma^2} \sum_{k=1}^p \sum_{i=1}^{n_k} (y_{ik} - \beta_k)^2 - \frac{1}{2\tau^2} \sum_{k=1}^K \beta_k^2.$$

To find the value of  $\beta_k$  which maximizes this posterior, we differentiate and set equal to zero:

$$\begin{aligned} \frac{d}{d\beta_k} \left[ -\frac{1}{2\sigma^2} \sum_{i=1}^{n_k} (y_{ik} - \beta_k)^2 - \frac{1}{2\tau^2} \beta_k^2 \right] &= 0 \\ \Rightarrow \frac{1}{\sigma^2} \sum_{i=1}^{n_k} (y_{ik} - \beta_k) - \frac{1}{\tau^2} \beta_k &= 0 \\ \Rightarrow \sum_{i=1}^{n_k} (y_{ik} - \beta_k) - \frac{\sigma^2}{\tau^2} \beta_k &= 0 \\ \Rightarrow \sum_{i=1}^{n_k} y_{ik} - n_k \beta_k - \frac{\sigma^2}{\tau^2} \beta_k &= 0 \\ \Rightarrow \beta_k \left( n_k + \frac{\sigma^2}{\tau^2} \right) &= \sum_{i=1}^{n_k} y_{ik} \\ \Rightarrow \beta_k &= \frac{\sum_{i=1}^{n_k} y_{ik}}{n_k + \frac{\sigma^2}{\tau^2}}. \end{aligned}$$

If we express the average value of the target variable within each group as

$$\bar{y}_k = \frac{1}{n_k} \sum_{i=1}^{n_k} y_{ik}$$

we can then write

$$\beta_k = \frac{n_k \bar{y}_k}{n_k + \frac{\sigma^2}{\tau^2}}$$

and divide the top and bottom by  $n_k$  to get

$$\beta_k = \frac{\bar{y}_k}{1 + \frac{\sigma^2}{n_k \tau^2}}.$$

## 6.9. Next Steps

We have now trained a GLM on our FAA-NTSB data. We avoided overfitting, dealt with numeric features which affect the target in a nonlinear way, and dealt with HCCVs. Yet our performance (pseudo- $R^2$  of 0.151) still falls 9% short of our gradient boosting benchmark (pseudo- $R^2$  of 0.165). In Chapter 9 we discuss how we can use the gradient boosting model (or any complex machine learning model) to check the work we have done so far with our GLM and how we can try to extract any patterns it has found which we have not used and incorporate them into our GLM.

There is a choice with how to deal with our target-encoded HCCVs which we did not discuss above. The first option is to refit the GLM including the HCCV together with all other features previously used. If we do this, we will get fitted coefficients for the target encoding variable and also revised fitted coefficients for all the other features. They may be different from the previous model, and indeed, unless the other features are completely independent of the target encoded features, it is likely that they will be different. The other option is to allow the coefficients from the first model to remain as they were and to fit the target encoded HCCVs in a separate, second-stage model.

In a business which has a complex GLM which drives its prices, it may not want to have to implement changes in every table of coefficients just because it carries out a detailed review of one of its features.

The choice we made for our modeling in this chapter was to fit our target encoded variable in a second-stage GLM and so to avoid changing the coefficients for all the other features. The method for achieving this has many applications, and we discuss it in some detail in Chapter 8. However, we first take a break from the FAA-NTSB study and turn to the issue of modeling in the presence of highly correlated features.

