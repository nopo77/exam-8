---
paper: chalk_et_al
chapter: 8
title: Modeling in Two Stages
topics: [two_stage_modeling, offsets, residuals_modeling, geospatial_smoothing, hypothesis_space, frequency_model, proxy_variables]
key_formulas: [offset_log_link, adjusted_frequency_residual, shi_2010_weights]
---

> **TL;DR**
> - Offsets fix pre-determined relativities in the log-linear predictor: η = (GLM terms) + log(fixed_relativity); correlated features then adjust to partially compensate for mismatches.
> - Residual modeling (actual/predicted from stage 1) is mathematically equivalent to offset modeling for Poisson/log-link models (Shi 2010); correct weights: frequency Σe_i·u_i, severity Σc_i, loss cost Σe_i·u_i^(2-p).
> - GLMs cannot perform geospatial smoothing directly; use a two-stage approach: stage-1 GLM without zip code → stage-2 GAM on spatial residuals → combine multiplicatively.
> - Leakage in two-stage models: stage-2 residuals must use cross-validation predictions (not in-sample) from stage 1.
> - Rating groups: map zip codes to groups so the spatial table can be communicated and updated independently of other rating factors.

# 8. Modeling in Two Stages

Often a single GLM is not sufficient to create a full rating plan, and thus there are situations where we want to do something along the lines of:

- Fit a GLM or insist on some fixed starting point as a first stage.
- Then carry out some adjustment or another modeling process as a second stage.
- Finally, recombine the original GLM and the results of the second stage into a model which can make predictions based on both stages.

There are various situations when splitting out one aspect of our model into a second stage has operational or technical advantages. Some examples are:

- Sometimes, when we submit a new rating plan to a regulator, we don't want too much to change at once. One easy way to ensure control over what changes is to somehow insist that our existing rates are a fixed first-stage model and to fit a second-stage GLM to see what incremental changes we might want to propose.
- We have one or more features for which the relativities are fixed, and we want to fit a GLM given these loads/discounts. An example often seen in practice is a deductible discount scale.
- In a rating system, we have some basic features, such as age and location, provided by the customer. We have further data enrichment features that are available at the time of quote (at a cost). The enrichment features are correlated with the basic features. An example might be that the enrichment feature is credit score (if it is permitted), and this is correlated with customer age. Consider the case where the average load in the rating plan for a 20-year-old driver consists of a 20% load based on age and a further 5% load based on credit score (because average credit scores are poor for younger drivers). If the enrichment services which provided credit score data fail for a day (say), then the average quote on that day will be 5% too cheap for those drivers. In such a case, it might be beneficial to first fit a GLM for customer age, and as a second stage add credit score to the model while insisting that the relativity for age does not change ("controlling" for age). This way, if enrichment fails at the time of the quote, at least the age relativity

will be correct.<sup>57</sup>

- Sometimes, a GLM is not sufficient for our needs because it cannot fully capture the relationship (we will explain this further below). Consider dealing with risk which varies by geographical area. It is not easy to deal with this purely in a GLM framework. We might therefore want to fit all the features that we can within a GLM. Then, as a second stage, we can complete our geographical area rating using some other approach.

In this chapter, we will discuss some of the reasons for two-stage modeling in more detail and how technically we might go about it. We will look at some aspects of our simulated auto insurance and FAA-NTSB case studies for which we might want to use this technique. There are three straightforward practical techniques we will need:

- fixing coefficients with an offset
- using the residuals from a first model in a second model
- combining parts of multiplicative models.

We will not exhaustively cover all situations where these might be used, but once the three ideas are understood, their application to novel modeling challenges is straightforward.

## 8.1. Fixing Coefficients With an Offset

Offsets and reasons for using them are discussed in Goldburd et al. (2025) Section 2.6 and in significant detail in the clear and easy-to-read paper, “Applications of the Offset in Property-Casualty Predictive Modeling” (Yan et al. (2009)). The latter source covers much of what we discuss in this chapter. The mathematics of offsets and their application was further extended in Shi (2010).

What follows is an example to motivate why we might want to use an offset and how to do it.

Consider a very simple model in private passenger auto. There are only two features, age and no claims bonus (NCB). NCB is a number which is awarded to each insured based on their claims history. Every driver starts with an NCB of zero. If they drive for a certain number of years without any claim, then their NCB increases by one up to a maximum of four. Age will be represented by a categorical variable A, B, ..., E, where A represents the lowest ages and E represents the highest ages.<sup>58</sup>

---

<sup>57</sup> As an aside, another way to deal with this is to include in the credit score table in the rating plan a line for failed enrichment, which varies by age.

<sup>58</sup> In practice we would never replace a numeric feature such as age with a categorical feature, as it destroys relevant information about the order and proximity of the ages. We have done it here for pedagogical reasons only.

Data were simulated to represent this situation, and a sample of the simulated data is shown in Table 8.1. Age group takes values A, B, ..., E and NCB takes values 0, 1, ..., 4.  $gt\_rel\_ncb$  (the true relativity for NCB) and  $rel\_ncb\_mkt$  (the relativity for NCB communicated by the marketing department) will be discussed below.  $num\_cl$  is the simulated number of claims.

**Table 8.1. Simulated data for private auto example. Age group takes values A, B, ..., E. NCB takes values 0, 1, ..., 4.  $gt\_rel\_ncb$  is the true relativity for NCB, and  $rel\_ncb\_mkt$  is the relativity for NCB communicated by the marketing department.  $num\_cl$  is the simulated number of claims.**

| id | age | ncb | $gt\_rel\_ncb$ | $rel\_ncb\_mkt$ | $num\_cl$ |
|----|-----|-----|----------------|-----------------|-----------|
| 1  | B   | 1   | 0.95           | 0.65            | 0         |
| 2  | D   | 3   | 0.85           | 0.40            | 0         |
| 3  | D   | 3   | 0.85           | 0.40            | 0         |
| 4  | A   | 0   | 1.00           | 1.00            | 0         |
| 5  | D   | 2   | 0.90           | 0.50            | 1         |
| 6  | B   | 1   | 0.95           | 0.65            | 0         |
| 7  | D   | 4   | 0.80           | 0.20            | 0         |
| 8  | D   | 2   | 0.90           | 0.50            | 0         |
| 9  | D   | 3   | 0.85           | 0.40            | 1         |
| 10 | A   | 2   | 0.90           | 0.50            | 0         |

Typically, only drivers at older ages have been insured long enough to earn the higher levels of NCB, and so there is a very strong relationship between age and NCB (see Table 8.2).

**Table 8.2. The number of insureds in each combination of age and NCB in the simulated data. There is a strong relationship between age and NCB. (Note that the age categories and NCB step-back rules were not specifically defined in the simulations—we simply ensured that the typical expected correlations between older ages and higher NCB levels exist.)**

|     | NCB 0  | 1     | 2     | 3     | 4      |
|-----|--------|-------|-------|-------|--------|
| age |        |       |       |       |        |
| A   | 132381 | 54519 | 12194 | 1237  | 26     |
| B   | 55624  | 82213 | 49354 | 12283 | 952    |
| C   | 11053  | 49903 | 77029 | 50248 | 11291  |
| D   | 920    | 12187 | 49027 | 81946 | 55690  |
| E   | 22     | 1178  | 12396 | 54286 | 132041 |

Since the data are simulated, we know the underlying ground truth for the true relativities for age and NCB (see Table 8.3).

**Table 8.3. The ground truth relativities for NCB and age used to simulate the data.**

|                 | age | A | B    | C   | D    | E   |
|-----------------|-----|---|------|-----|------|-----|
| true relativity |     | 1 | 0.7  | 0.6 | 0.5  | 0.4 |
|                 | NCB | 0 | 1    | 2   | 3    | 4   |
| true relativity |     | 1 | 0.95 | 0.9 | 0.85 | 0.8 |

For simulations, we set claim frequency for age A and NCB 0 to 10%, and then the frequencies for all other combinations of age and NCB can then be derived from Table 8.3.

For simplicity, we assume that if there is a claim, it will be for exactly \$10,000. This means that the correct risk premium for an insured in age band A and NCB 0 is the product of the intercept of the claims frequency model (0.10), the relativity for age group A (1.0), the relativity for NCB level 0 (1.0), and the expected severity (10,000):

$$0.10 \times 1.0 \times 1.0 \times 10000 = \$1,000$$

Likewise the correct risk premium for an insured in age band E and NCB 4 is

$$0.10 \times 0.4 \times 0.8 \times 10000 = \$320.$$

A Poisson GLM with a log link was fitted to the data, using age and NCB as predictors. The exponents of the fit coefficients ( $\exp \beta$ ) from the GLM are close to the ground truth and are shown in Table 8.4.

**Table 8.4.  $\exp \beta$  are the exponents of the fitted coefficients from a GLM with age and NCB. It can be seen that they are close to the true relativities.**

|                 | age | A | B     | C     | D     | E     |
|-----------------|-----|---|-------|-------|-------|-------|
| true relativity |     | 1 | 0.7   | 0.6   | 0.5   | 0.4   |
| $\exp \beta$    |     | 1 | 0.702 | 0.605 | 0.494 | 0.390 |
|                 | NCB | 0 | 1     | 2     | 3     | 4     |
| true relativity |     | 1 | 0.95  | 0.9   | 0.85  | 0.8   |
| $\exp \beta$    |     | 1 | 0.937 | 0.900 | 0.846 | 0.826 |

Based on the coefficients from the fit GLM (and given that the exponent of the fit intercept is 0.10), the risk premium for an insured in age band E and NCB 4 is

$$0.10 \times 0.39 \times 0.826 \times 10000 = \$322,$$

which is close to \$320, which we know to be correct.

When we present our relativities to the business, we are told that they cannot use the NCB relativities. This is because the marketing department has already communicated to potential insureds a scale of discounts for NCB which are much larger than those output by the GLM. Table 8.5 shows the discounts communicated by the marketing department<sup>59</sup>—it can be seen that they are far larger than those from the fitted GLM or the ground truth.

**Table 8.5.**  $\exp \beta$  are the exponents of the fitted coefficients from a GLM with age and NCB. The table compares these to the marketing relativities (or discounts). We can see that there are some large differences.

|                      | NCB | 0     | 1     | 2     | 3     | 4 |
|----------------------|-----|-------|-------|-------|-------|---|
| true relativity      | 1   | 0.95  | 0.9   | 0.85  | 0.8   |   |
| $\exp \beta$         | 1   | 0.937 | 0.900 | 0.846 | 0.826 |   |
| marketing relativity | 1   | 0.65  | 0.50  | 0.40  | 0.20  |   |

If we use the GLM relativities for age and the marketing discount for NCB, then the risk premium for an insured in age band E and NCB 4 is

$$0.10 \times 0.39 \times 0.20 \times 10000 = \$78,$$

which is far too low.

Since age is highly correlated with NCB, we should be able to fix this at least partially by adjusting the coefficients for age to allow for the very large marketing discount for NCB level 4. We could try to do this manually, but we can actually achieve this very easily by just “telling” the GLM that it must use the marketing relativities for NCB and only to fit the coefficient for age.

Given a log link, we use  $\mu$  to refer to the expected (annual) claim frequency<sup>60</sup> and  $\eta = \log(\mu)$  to refer to the linear predictor (i.e., the log of the expected claim frequency). Then for an insured in age band E and NCB band 4, our first model was

$$\begin{aligned} \mu = & \text{intercept} \times (\text{coefficient for age band E}) \\ & \times (\text{coefficient for NCB band 4}) \end{aligned}$$

<sup>59</sup> This is a very extreme example for illustrative purposes.

<sup>60</sup> In our simplified simulation example, every observation represents exactly one year of exposure. In most practical situations, each observation represents an amount of exposure ( $ex$ ) between zero and one, the claim frequency is calculated as  $num\_cl/ex$ , and the expected number of claims for an observation is  $ex \times \mu$ .

and taking logs,

$$\begin{aligned}\eta &= \log \mu \\ &= \log \text{intercept} + \log(\text{coefficient for age band E}) \\ &\quad + \log(\text{coefficient for NCB band 4}).\end{aligned}$$

Given the marketing discounts for NCB, we now need to fit a model where the linear predictor is given by

$$\eta = \log \mu = \log \text{intercept} + \log(\text{coefficient for age band E}) + \log(0.20)$$

The value  $\log(0.20)$  in the above model is known as the offset because it adjusts (offsets) the linear predictor by a given amount.

A Poisson GLM with a log link was fitted to the data, using age as the predictor and including an offset for the logarithm of the relative marketing discount. The coefficients for age in this GLM are shown in Table 8.6.

**Table 8.6. The exponents of the coefficients for age from a GLM where the marketing relativities for NCB are offset. The fitted intercept (not shown in the table) is 0.112.**

| age                         | A | B     | C     | D     | E     |
|-----------------------------|---|-------|-------|-------|-------|
| true relativity             | 1 | 0.7   | 0.6   | 0.5   | 0.4   |
| exp $\beta$                 | 1 | 0.702 | 0.605 | 0.494 | 0.390 |
| exp $\beta$ when NCB offset | 1 | 0.849 | 0.925 | 0.980 | 1.057 |

Given an estimated intercept of 0.112 and using the marketing discounts for NCB and the revised relativities for age, the risk premium for an insured in age band E and NCB 4 is

$$0.112 \times 1.057 \times 0.20 \times 10000 = \$237,$$

which while still far from the true risk premium of \$320 (or our original risk premium of \$322) is significantly better than \$78.

In this case, the GLM has used the strong relationship between age and NCB to correct for the excessive NCB discount communicated by the marketing department. For example, for NCB group 4 the true relativity is 0.8 and the marketing discount is 0.2—hence without adjusting the age coefficient—the resulting premium will be  $0.25 \left(\frac{0.2}{0.8}\right)$  of the correct amount. Since most of the NCB group 4 is in age group E, the increase of the age coefficient for age group E to 1.057, compared to 0.39 in the original model, helps to make up some of the difference.

To the extent that other features are correlated with the feature to which the offset applies, their coefficients will change in order to bring the model predictions closer to what they would have been using all the features. We end up charging less unreasonable premiums to all customers despite our marketing department's bold promises on NCB discount.

In the introduction to this chapter, we mentioned that in practice we may wish to offset a given deductible relativity. In this and similar cases, if we are fitting both frequency and severity models, the question arises: how much of the discount should be offset in the frequency model and how much in the severity model? Unless it is obvious from the situation that the effect should be offset totally in one or the other, a simple approach is to offset equally (i.e., the square root of the load/discount) in each.<sup>61</sup>

Before moving on, we note that Table 8.6 exhibits what is known as a “reversal”: the estimated coefficients for age increase with driver age, even though we know they should decrease. While the application of the offset has indeed left us with less unreasonable premiums, the outcome is far from perfect. For example young, safe drivers will now be grossly undercharged.

## 8.2. The Hypothesis Space of GLMs

In the introduction to this chapter, we mentioned that the hypothesis space of GLMs is occasionally insufficient for our needs, and so the GLM cannot “grasp” some relationships between risk classes. Here we discuss this point in more detail. In the two following sections we show how we can use offsets or residuals to create two-stage models, as well as the mathematical equivalence of these methods.

Once a GLM has been fit, we essentially have a function which maps from the input features to the predicted target. If  $x_1, x_2, \dots, x_p$  are the features and  $\hat{y}$  is the predicted target, then our GLM is a function:

$$f : (x_1, x_2, \dots, x_p) \mapsto \hat{y}.$$

For example, if we fit a GLM with an identity link, and the only feature is aircraft age and the estimated coefficient is 2, then the fit GLM is

$$f : (x_1) \mapsto 2 \times x_1,$$

---

<sup>61</sup> Alternatively, more accurate approaches could be used. For example, we could fit separate frequency and severity models and include the feature that we want to offset. We can then inspect the coefficients fit in the frequency and severity models and use them to inform how we split the offset.

where  $x_1$  is aircraft age. The estimated function is known as a hypothesis, and the set of all functions that could have been fit is known as the hypothesis space. There are an infinite number of possible functions in this GLM's hypothesis space because there are an infinite number of coefficients that could be chosen instead of 2. Despite there being infinite functions in the GLM hypothesis space, there are a great many that are not. For example,

$$f : (x_1) \mapsto 2 \times \frac{1}{x_1}$$

is not (because with an identity link,  $\mu$  is not a linear function of  $x_1$ ). We can get around this quite easily by creating a new feature  $x_2 = \frac{1}{x_1}$  and then we would have

$$f : (x_1, x_2) \mapsto 2 \times x_2.$$

Now consider a harder case from auto insurance. Each car is associated with two locations: the house where the owner lives ( $x_{1long}$  and  $x_{1lat}$ ) and the place where the car is parked overnight ( $x_{2long}$  and  $x_{2lat}$ ). We might want to test whether the distance between these two locations impacts the probability of an accident or of a theft. Using the two sets of longitude and latitude as features in a GLM will not help. Rather, we need to create a new feature to represent the distance:

$$x_3 = \sqrt{(x_{1long} - x_{2long})^2 + (x_{1lat} - x_{2lat})^2}$$

and use this new feature in the GLM. This idea of engineering new features is exactly how we overcame the two limitations of the GLM hypothesis space discussed so far in this note. We engineered hinge and step functions to overcome the GLM hypothesis space only containing functions which are (roughly) linear combinations of the features. Allowing the GLM to fit interactions also involves engineering new features (although this is often built into the software which fits the GLMs). We have to pay very careful attention to feature engineering to successfully use the GLM with its relatively simple hypotheses space.

An alternative to GLMs is to use a model with a less restrictive hypothesis space, allowing us to avoid much manual feature engineering. Back in 1989 it was proved (Cybenko (1989), Universal Approximation Theorem) that, given our original features, and without us doing any feature engineering, a neural network can approximate any continuous function of those features as accurately as we would like. For example, with appropriate training the neural network will find the correct shape for the nonlinear effects. Other machine learning methods, such as gradient boosting machines, given the original features, have a different hypothesis space than GLMs and might be able to fit a model

which performs better than a GLM.

The downside of models that are more complex than GLMs is that they are not easily interpreted. If a customer or a regulator asks for an explanation of the rate, it will not be easy to provide it. There is a compromise. We can use a GLM for the features that it can easily fit and for those which we can easily engineer. Then, as a second stage, we can feed the residuals from this model into a more complex model to deal with aspects of the modeling task which are not as easily represented or discovered by a GLM. We will then need to find a way to combine the output from the more complex model, or the features that it has generated, with the GLM.

A particular widespread (in current practice) application of the above is geographic rating. Consider zip codes (or census tracts), an extreme case of an HCCV. We can partially deal with this by not modeling zip codes directly but rather adding features related to zip codes to our dataset, such as population density or the distance to the nearest school or police station or fire hydrant. However, whether or not we have such data, there is another point to consider. Following Tobler (1970) the famous (and maybe obvious) first law of geography is “Everything is related to everything else, but near things are more related than distant things.” In our case, we expect that claims experience in nearby zip codes is similar. Although we don’t have a lot of information in each zip code, if we can somehow smooth or average the claims experience of nearby zip codes, this might be an important feature in our model. It is not easy within a GLM framework to carry out geospatial smoothing.<sup>62</sup> This suggests to us again a two-stage model:

- Fit a GLM to all features except zip code (and possibly zip code related features).
- Use the output of the GLM (offsets or residuals) to carry out geospatial smoothing with a different model type.
- If necessary, combine the results of the geospatial smoothing with the GLM.

## 8.3. Two-Stage Models Using Offsets

In this section, we show how we can use an offset to fit another model which aims to find additional relationships between features and risk, above and beyond what a first-stage model has found. The example we will use is our FAA-NTSB case study, and we will look to fit a second-stage model to produce a smoothed view of geospatial risk across the US. We use the zip code of the person to whom the aircraft is registered as the location of interest. (This example is for pedagogical interest only—there is no particular reason to assume that the zip code of the registered owner should impact the frequency of the types of aircraft accidents in the NTSB database.)

---

<sup>62</sup> It can be done to some extent with a bespoke penalization scheme. See for example GLUM Contributors (n.d.).

The model fit so far as a result of our work in previous chapters is our first-stage model. We have a file, which for each row in our original data, contains a unique id and the predicted<sup>63</sup> number of claims from stage 1. To this file, we add the zip code and then look up the longitude and latitude. A sample of the resulting file is shown in Table 8.7. The “ex” column is the number of aircraft-years represented by each line—for these observations, 1.<sup>64</sup>

**Table 8.7. A sample of the records and predictions from our first-stage model. (Note that exposure is one (year) on these records, but this is not true across all observations.)**

| unique_id_line | fold | zip5  | ex | lon      | lat    | number of claims |          |
|----------------|------|-------|----|----------|--------|------------------|----------|
|                |      |       |    |          |        | actual           | expected |
| 285985         | 5    | 15668 | 1  | −79.670  | 40.461 | 0                | 0.00085  |
| 1670670        | 0    | 21822 | 1  | −75.636  | 38.281 | 0                | 0.00260  |
| 1769520        | 0    | 60077 | 1  | −87.757  | 42.035 | 0                | 0.00932  |
| 454832         | 2    | 83607 | 1  | −116.751 | 43.709 | 0                | 0.00145  |
| 1387894        | 4    | 85248 | 1  | −111.870 | 33.215 | 0                | 0.00183  |

For convenience, we summarize this file to zip code level. (It is not obvious that we can do this without changing the results of our second-stage model—but in the case where we use a Poisson distribution, it happens to be true.) The resulting table has information on about 700,000 aircraft-years spread across 20,000 zip codes. For this example, we use the first five digits of zip code, we exclude Alaska and Hawaii, and also only use records for registered owners who are individuals (as opposed to corporations). A sample of the resulting table is shown in Table 8.8.

In order to visualize any possible geographic patterns, we now plot the residuals from the first model on a map. Given the multiplicative nature of all our modeling so far, we define “residual” as the actual number of claims divided by the predictions from the stage 1 model ( $\frac{y_j}{\hat{y}_j}$ , where  $j$  represents a zip code). (Where the actual number of claims is zero, we replace the zero residual with a small number, e.g., 0.01—this will be important later on, where we might want to take the log of the residuals.) Figure 8.1 shows the log of the residuals summarized to the first three digits of the zip code and where we include only zip codes with more than 500 aircraft-years.

<sup>63</sup> Sometimes referred to as expected.

<sup>64</sup> The techniques being discussed will work for any (positive) numeric values for exposure.

**Table 8.8. A sample of the records and predictions from our first-stage model summarized to zip code level (first five digits). For example, across all our records for zip code 15668, the sum of aircraft exposure years is 15.65, the total number of claims is zero, and the sum over these records of exposure times predicted (annual) frequency from our previous model is 0.014.**

| zip5  | ex     | lon      | lat    | number of claims |          |
|-------|--------|----------|--------|------------------|----------|
|       |        |          |        | actual           | expected |
| 15668 | 15.65  | −79.670  | 40.461 | 0                | 0.014    |
| 21822 | 15.14  | −75.636  | 38.281 | 0                | 0.037    |
| 60077 | 9.37   | −87.757  | 42.035 | 0                | 0.039    |
| 83607 | 182.28 | −116.751 | 43.709 | 1                | 0.759    |
| 85248 | 249.62 | −111.870 | 33.215 | 0                | 0.739    |

![Map of the United States showing the log of residuals (actual number of claims divided by predictions) from the stage 1 model. The map displays numerous colored dots representing residuals for various zip codes. A color scale on the right indicates residuals from -1.0 (blue) to 1.0 (red). The map shows a band of higher residuals (red/orange) running from Oregon through Idaho and into western Montana, and Florida has consistently low residuals (blue).](9b9b63ddab6e5f3b3d8ccaf71f7f0d79_img.jpg)

The figure is a map of the contiguous United States with latitude and longitude coordinates. Latitude ranges from 25°N to 50°N, and longitude ranges from 120°W to 70°W. Numerous colored dots are plotted across the map, representing the log of residuals for various zip codes. A color scale on the right, labeled 'residuals', ranges from -1.0 (blue) to 1.0 (red), with 0.0 being white. The map shows a clear pattern: a band of higher residuals (red/orange) runs diagonally from the northwest (Oregon/Idaho/Montana) towards the southeast. Florida and parts of the Southeast show consistently low residuals (blue/purple).

Map of the United States showing the log of residuals (actual number of claims divided by predictions) from the stage 1 model. The map displays numerous colored dots representing residuals for various zip codes. A color scale on the right indicates residuals from -1.0 (blue) to 1.0 (red). The map shows a band of higher residuals (red/orange) running from Oregon through Idaho and into western Montana, and Florida has consistently low residuals (blue).

**Figure 8.1. The log of the residuals (actual number of claims divided by predictions) from the stage 1 model. Only zip codes (first three digits used here) with 500 or more aircraft-years are shown. Patterns are not easy to spot, but possibly Florida has consistently low residuals, whereas there seems to be a band of higher residuals running from Oregon through Idaho and into western Montana.**

We want our second-stage model to predict the number of claims for each aircraft using longitude and latitude of its owner's residence. We also want it to start where the first model left off—a high number of claims for a particular area does not mean that area is a high-risk geography—we might have been expecting a high number of claims simply given the predictions from our stage 1 model. If  $pred_1$  and  $pred_2$  are the predicted

frequency from our first-stage and second-stage models, we need

$$pred_2 = pred_1 \times \text{geographic effect.}$$

Taking the log of both sides, we have

$$\log pred_2 = \log pred_1 + \log (\text{geographic effect}).$$

So, if our second-stage model is multiplicative and allows for the use of an offset, then our target variable is claim frequency (with exposure as weights), and we use the log of the expected claim frequency from the first-stage model as the offset.<sup>65</sup> The model type that we chose to use for the spatial smoothing (generalized additive models, GAMs) does allow this formulation.

Our main aim here is to demonstrate the use of an offset to achieve second-stage models, but nevertheless, out of interest we show the result of the spatial smoothing in Figure 8.2.

![A map of the United States showing the log of predictions from a GAM. The map is color-coded by longitude and latitude, with a color scale on the right ranging from -0.4 (blue) to 0.4 (red). High values (red) are concentrated in the western United States, particularly in Oregon, Idaho, and western Montana. Low values (blue) are seen in the southeastern United States, including Florida. The map includes latitude lines from 25°N to 50°N and longitude lines from 120°W to 70°W.](9326aeab3108a1d46b5d30a235855628_img.jpg)

A map of the United States showing the log of predictions from a GAM. The map is color-coded by longitude and latitude, with a color scale on the right ranging from -0.4 (blue) to 0.4 (red). High values (red) are concentrated in the western United States, particularly in Oregon, Idaho, and western Montana. Low values (blue) are seen in the southeastern United States, including Florida. The map includes latitude lines from 25°N to 50°N and longitude lines from 120°W to 70°W.

**Figure 8.2. The log of the predictions from the GAM are shown. It can be seen that these are high from Oregon through Idaho and into western Montana and somewhat low in Florida.**

Above, we used predictions from a first-stage model in a second-stage model. If we are not careful, the predictions of the first-stage model for each observation will be based on having seen the value of the target variable for that observation. The problems this might cause, and how to avoid them, are discussed further in Section 8.9.

<sup>65</sup> An alternative formulation is: Target variable—number of claims; offset—log of (exposure times the expected claim frequency from the first-stage model); weight—not needed.

## 8.4. Two-Stage Models Using Residuals

When we use a second-stage model as part of our modeling process, there is no guarantee that it will have the option for an offset. In the cases where an offset is not available, we can model the residuals instead. Given the multiplicative nature of our modeling, we define the residuals as the target for the first-stage model divided by the predictions from the first-stage model,<sup>66</sup> and we use these as the target for the second-stage model. Continuing to look at our data aggregated to zip code level in Table 8.8, the target for the first row will be  $\frac{0}{0.014} = 0$  and for the fourth row will be  $\frac{1}{0.739} = 1.353$ . Some residuals are based on more data, and we are therefore more certain about them (they have a lower variance). We allow for this in the second-stage model by using the weight option and setting it equal to exposure times the predicted (annual) frequency from the first-stage model.

In our case, the results from the second-stage model with this approach are identical to those when using an offset. We would typically expect this when using a Poisson, log-link model, since it has been shown by Yan et al. (2009) (Appendix A), and then generalized by Shi (2010), that the two approaches are mathematically identical.

## 8.5. Two-Stage Models Using Preadjustment

This section draws directly from Shi (2010). In order that the interested reader can refer to that paper without confusion, we will use a similar<sup>67</sup> notation here; for observation  $i$ ,  $c_i$  is the actual number of claims,  $l_i$  is the cost of claims incurred, and  $e_i$  is exposure. Finally  $u_i$  is used to refer to the predictions from the first-stage model.

Above, we talked about modeling residuals. For a frequency model, in our first-stage model, the target was claims frequency ( $\frac{c_i}{e_i}$ ), the weights were the exposure ( $e_i$ ), the predicted frequency is denoted by  $u_i$ , and the predicted number of claims is  $e_i \times u_i$ . We then defined residuals as the actual number of claims divided by the predicted number of claims

$$\frac{c_i}{e_i \times u_i}$$

and we used this residual as a target variable, and we claimed (without much proof) that we should use the predicted claim counts ( $e_i \times u_i$ ) as weights.

If we express our residual as

$$\frac{c_i/e_i}{u_i}$$

<sup>66</sup> Using division rather than subtraction to arrive at the residuals is not a theoretical nicety; it is a practical necessity. This is because the result of this analysis will be an extra table in our rating structure whose relativities will multiply the results until that point.

<sup>67</sup> Our notation is similar but not identical.

we can consider our target as the frequency, adjusted by the predictions from the first model. Where the prediction is high, we reduce the frequency as we don't need the second-stage model to pick up this effect which is already picked up by the first model.

Shi (2010) proved that modeling the adjusted frequency and using weights  $e_i \times u_i$  is correct and identical to using the offset. Consistent with referring to the target as “adjusted frequency,” Shi refers to  $e_i \times u_i$  (which are our claim count predictions from the first-stage model) as “adjusted exposures.”

In Table 8.8, we summarized our residuals by each level of the zip code (zip5). Shi (2010) proves that in this case, too, the weight that we used (the sum of the predicted claims for the zip code,  $\sum_{i \text{ in a given zip code}} (e_i \times u_i)$ ) is correct.

The case studies in this monograph focus on modeling claims frequency. The techniques discussed (dealing with nonlinear effects, HCCVs, etc.) apply equally to modeling claim severity ( $\frac{l_i}{c_i}$ ) or (annualized) loss cost ( $\frac{l_i}{e_i}$ ). In our discussion here, too, we may wish to see how predicted claims severity from a first-stage Gamma GLM should be adjusted by zip code or how predicted (annualized) loss costs (i.e. risk premiums) from a Tweedie GLM should be adjusted. The process is the same, fit a first-stage model without zip code, summarize the predictions by zip code, calculate the residuals (or “adjusted claim severity” and “adjusted loss cost”), and then fit the stage-two model with appropriate weights.

Shi (2010) provides the correct weights in these situations, too. For the convenience of the reader, we summarize Shi's results (see Shi (2010), Table 3) in Table 8.9.

**Table 8.9. The correct weights for modeling adjusted frequency, severity, or loss costs. The notation is described in the main text. Note in particular that  $u_i$  on each line in this table represents the predictions from the first-stage model fitted in that case. The sums are over all observations in a given zip code. If there are 100,000 zip codes, then the resulting dataset will have 100,000 lines, one for each zip code, each line containing the value of the target variable and the weight, as well as any features used in the second-stage model. If the second-stage model requires cross-validation or similar, the summations are per zip code and fold.**

| Model     | Distribution   | Response Variable           | Weight Variable      |
|-----------|----------------|-----------------------------|----------------------|
| Frequency | Poisson        | $\sum c_i / \sum (e_i u_i)$ | $\sum e_i u_i$       |
| Severity  | Gamma          | $\sum l_i / \sum (c_i u_i)$ | $\sum c_i$           |
| Loss cost | Tweedie( $p$ ) | $\sum l_i / \sum (e_i u_i)$ | $\sum e_i u_i^{2-p}$ |

## 8.6. Recombining the Two Models

The result of the second-stage model fitted above, whether using a GAM or any other method to deal with spatial data, is a file which contains a relativity for each zip code. For any individual aircraft we look up the zip code relativity and apply it to the result of the rating plan so far. Some examples of the result of our analysis are shown in Table 8.10.

**Table 8.10. A sample of zip code relativities from the stage 2 model. If the predicted frequency for an aircraft in zip code 15668 from the stage 1 model (i.e., rating plan excluding this table) is 0.001, then the prediction including this table is  $0.001 \times 0.53113$ .**

| zip5  | stage2_pred |
|-------|-------------|
| 15668 | 0.53113     |
| 21822 | 1.01655     |
| 60077 | 0.92112     |
| 83607 | 1.72816     |
| 85248 | 0.71129     |

To find a predicted frequency from our two models, we simply calculate a prediction from the first model and multiply it by the zip code relativity from the second model. No further analysis needs to be done.

A practical point to note is that it might be more convenient to provide the results as an allocation of each zip code to an area group—this is discussed further in Section 8.9.2.

## 8.7. Combining Parts of Multiplicative Models

Our FAA-NTSB model has various features that are related to the make and model of the aircraft. Some examples of these features are:

- `faa_eng_hp_char`—horsepower for piston engines. Coded as a letter (e.g., “A” represents 0–149 hp and “B” represents 150–249 hp).<sup>68</sup> For example, the Lycoming O-320 series of engines, with around 160 hp, is used in the Cessna 172M—a very popular training aircraft—and is coded as “B.”

<sup>68</sup> In reading details of this and the following features, the reader could feel, rightly, shocked. It looks like the authors have taken a useful numeric variable, split it into discrete chunks, and labeled those chunks with letters which have no inherent order. Discarding order and proximity information in numeric data by encoding it as categorical destroys information! However, the FAA data for these fields was not provided as continuous numeric variables, but rather in groups, e.g., for weight, four classes were provided, CLASS 1: Up to 12,499 lb., etc. In addition, we have no a priori reason to assume that there is any order in how accident frequency varies by the weight category.

- `faa_eng_thrust_char`—thrust for turbine engines, measured in pounds. Coded as a letter (“A” represents thrust up to 10,000 lb.). Lycoming O-320 is not a turbine engine, and its power is measured in horsepower (hp), not pounds of thrust. In the raw FAA data it is coded as thrust 0. In our data preparation we code this engine to “Y,” where the “Y” category is reserved for nonturbine engines.
- `faa_acft_ac_weight`—aircraft maximum gross takeoff weight in pounds, grouped into four classes. For example, class 1 is “up to 12,499 lb.,” and class 4 is “UAV (unmanned aerial vehicle) up to 55 lb.” The Cessna 172M maximum gross takeoff weight is 2,550 lb., and so it is coded to “A.”
- `faa_acft_type_acft`—fixed-wing single engine (coded to “4”), fixed-wing multi-engine (coded to “5”), and rotorcraft (coded to “6”).
- `faa_acft_num_eng`—the number of engines (one, two, three, or four). The Cessna 172M has one engine.
- `faa_acft_num_seats`—the number of seats. UAVs have zero seats, other aircraft have from one to 400+ seats. The Cessna 172M has four seats.

In addition to the above, we also have a separate relativity for each make-model of aircraft which we calculated in the chapter on HCCVs. There will therefore be seven tables which combine to give a relativity for each aircraft. If we can combine these seven tables into one, we will immediately have practical advantages of a rating plan that is both easier to communicate and quicker to calculate. We will also have the advantage that we can see the relative riskiness of craft (according to our rating plan) from one rating table. This would allow an underwriter with experience in the field to challenge the relative risk assigned to each aircraft.<sup>69</sup>

Achieving this is straightforward. We prepare a table that has all the features for each aircraft. Then for each feature, we find the relativity for that table and multiply them together. As an example, the data for the Cessna 172M would be as in Table 8.11. The product of all the relativities shown is 1.37. This compares to relativities of above 3 for various makes of helicopter.

---

<sup>69</sup> This also helps enormously with model interpretation, as the factors estimated for each of these variables may be distorted by correlation, given the common grain and risk element underlying all of them. Rolled up into a single factor, that correlation is “aggregated away,” and the impact of this “area” of the rating plan can be seen and understood more clearly.

**Table 8.11. An example of how to calculate the overall relativity for an aircraft.**

| feature             | feature value | relativity |
|---------------------|---------------|------------|
| make                | CESSNA        | 1.30       |
| model               | 172M          | 1.15       |
| faa_eng_hp_char     | B             | 1.00       |
| faa_eng_thrust_char | Y             | 1.36       |
| faa_acft_ac_weight  | CLASS 1       | 1.69       |
| faa_acft_type_acft  | 4             | 1.00       |
| faa_acft_num_eng    | 1             | 0.41       |
| faa_acft_num_seats  | 4             | 0.97       |

## 8.8. Further Examples

### 8.8.1. Credit scores

We have mentioned previously that it might be beneficial for certain parts of the GLM to be built separately—even if they are also fitted with a GLM. Credit score is one example.<sup>70</sup> From an operational perspective, there may be some team members or parts of the business (or outside vendors) who are experts in understanding the various credit features, what they mean, and how to use them in a GLM. Scores like this are also very helpful for interactions, allowing pockets of the data to be identified by common score which otherwise would be scattered across disparate combinations of the score components. Such groups would be obfuscated without a score to demonstrate the similarity of their constituent records. There are various possible orders for this process. One example is:

- A GLM is first fitted without the credit features.
- A separate model which uses all the credit features is fitted to the residuals of the first model.
- The result of the credit GLM is a credit score which is then appended to the original data as a new feature.
- A new GLM is fit using the credit score feature.

As previously, the GLM which uses the credit score feature can either fit together with all the other features using the original target or it can be fit on the credit score feature only using the residuals from the first model.

<sup>70</sup> More generally this point applies to any specialized sets of predictors and areas of the data beyond just credit.

We note also that in the above process, where the result of second model is appended to our data as a score and then used in the first GLM, there is no technical need for the type of the second model to be limited to a GLM. With territorial rating, our motivation for using a different model form was that a GLM could not easily “grasp” and allow for the idea of geographic proximity. In this case, our motivation might simply be that it is easier or quicker to use a different type of model or that it results in scores which are more accurate. There are potential practical issues with this approach. Firstly (as opposed to territorial rating where the results of any model type can be stored in a zip code relativity table), the credit score model needs to be applied at the time of quote—and model types more complex than GLMs may not be supported. There is also the issue that the results of more complex model types are not as easily explained as GLMs.

### **8.8.2. Usage-based insurance**

In usage-based auto insurance, the price is often given as a cost per mile. If when developing rating plans, we need to ensure that the cost per mile is constant, we can simply use (the log of) mileage as an offset.

### **8.8.3. Use of proxy variables**

There can be situations where the regulator requires certain variables not to be used (e.g., credit score in some states or gender in Europe). This topic has been addressed in “Implementing Anti-discrimination Policies in Statistical Profiling Models” (Pope and Sydnor (2011)) and in “Discrimination-free Insurance Pricing” (Lindholm et al. (2022)).

Consider the case where one of our features is credit score, and the regulator tells us that our rates must not depend on it in any way. If we exclude credit score from our models and there are other features which are highly correlated with it, they will act as a proxy for it and pick up some of the credit score effect (in the same way that in our example above, age picked up some of the NCB effect). In this case, management might prefer to fit a GLM with both age and credit score and then, in the final rating plan, ignore the coefficient for credit score.

Another case may be that credit score is a permitted variable, but the relativities are fixed by the regulator. Once again, if we fit a model without credit score and use the permitted credit score relativities as an offset, then other correlated features may pick up the difference between the permitted relativities and the true relativities. While this was the desired outcome in our above example with age and NCD, we might not want that here. The alternative is to include the credit score feature in the model and then in the rating plan replace its coefficient with the permitted coefficient. This approach (and others) is discussed further in the above references.

In the above cases, it is important to note that the intercept may need to be re-estimated. Consider the simple example of not being able to use gender in a rating plan and where the multiplicative relativities for gender are 1 for females and 2 for males. Setting the relativity for all customers to 1 without adjusting the intercept will lead to the overall premium across all customers being too low.<sup>71</sup> Whatever adjustment is made needs to be monitored over time, as the proportion of customers of each gender may change over time.

## 8.9. Practically Speaking

### 8.9.1. Leakage in two-stage models

Consider a two-stage model where we use the results of a first model in a second model. In the case of our multiplicative model, we will define “residual” as the target variable (let’s say this is the number of claims) divided by the predicted number of claims.<sup>72</sup> (The discussion would be identical if we were using preadjusted frequency, see Section 8.5.) If the first model is saturated (for example, a unique identifier for each record was used as a feature so that the prediction from the first model is exactly equal to the actual number of claims for each record), the results from the first model will look something like Table 8.12. The residual being modeled will be one for all observations, and the second stage will fit an intercept-only model.

**Table 8.12. num\_cl is the number of claims. Predictions from an overfitted first-stage model will render a second-stage model useless.**

| unique_id | fold | num_cl | stage 1 prediction | residual |
|-----------|------|--------|--------------------|----------|
| 1         | 1    | 5      | 5                  | 1        |
| 2         | 3    | 3      | 3                  | 1        |
| 3         | 2    | 7      | 7                  | 1        |
| ...       |      |        |                    |          |
| 1000001   | 9    | 5      | 5                  | 1        |
| ...       |      |        |                    |          |

In general, an overfit first-stage model will reduce the power of the second-stage model.<sup>73</sup> It “uses up” the signal, leaving the second model with less meaningful variation to pick up.

<sup>71</sup> Actuaries often refer to such adjustments as “off-balance” adjustments. See, for example, the interesting discussion in Boor (2022) which notes that off-balance adjustments following credibility and other analyses should not necessarily be the same for all classes.

<sup>72</sup> As discussed above, the weight is also adjusted.

<sup>73</sup> As mentioned elsewhere, it also memorizes the random component of the response, which will not help it better predict outcomes on unseen data.

To avoid this problem, we need, when fitting the second-stage model, to use the “cross-validation predictions.” By “cross-validation predictions,” we mean the predictions for each record will be from a model trained excluding all records in that fold. For example, the first record above (with unique id = 1) is in fold 1. We use the model which was created on all folds except fold 1 to create a prediction on this record. We do the same for all records. We then use these cross-validation predictions to create the residual which is modeled in the second stage.

In our particular case where the unique identifier itself was used as a feature, the cross-validation model will not be able to make a prediction specific to record 1 and will probably just predict the overall mean. The same will be true for all records. The resulting predictions and residuals are shown in Table 8.13. The two records which have values different from the overall mean (of 5) have residuals different from 1, and so there is a chance that the second-stage model might find something (if there is anything to find).

**Table 8.13. cv predictions from an overfitted first-stage model will still leave sensible residuals for a second-stage model to try to fit.**

| unique_id | fold | target | stage 1 cv prediction | residual |
|-----------|------|--------|-----------------------|----------|
| 1         | 1    | 5      | 5                     | 1        |
| 2         | 3    | 3      | 5                     | 0.6      |
| 3         | 2    | 7      | 5                     | 1.4      |
| ...       |      |        |                       |          |
| 1000001   | 9    | 5      | 5                     | 1        |
| ...       |      |        |                       |          |

In this section, we used the word “overfit.” By “overfit,” practitioners sometimes mean that the model has become so overly complicated that while the training performance has improved compared to a simpler model, performance on data not used in training the model has actually deteriorated. In this context, however, we mean any case where a more complex model starts to pick up patterns which are in the training data only and which do not improve performance on unseen data.<sup>74</sup>

### 8.9.2. Rating groups

A rating plan based on GLM output will consist of a set of tables, one for each feature and interaction. The table for each feature will have one row for each level of the feature. Table 8.14 shows how the table looks for the feature “type of registrant.”

<sup>74</sup> That is, data not used for parameter estimation and model structure determination in training.

**Table 8.14. Relativities for type of registrant.**

| type_registrant             | relativity |
|-----------------------------|------------|
| 1 (Individual)              | 0.937      |
| 2 (Partnership)             | 1          |
| 3 (Corporation)             | 2.063      |
| 4 (Co-Owned)                | 1          |
| 5 (Government)              | 1.090      |
| 7 (LLC)                     | 1          |
| 8 (Non-Citizen Corporation) | 1          |
| 9 (Non-Citizen Co-Owned)    | 1          |

When we make a rating plan change, we will typically want to communicate the whole rating structure, i.e., all the rating tables. Any number of tables of a similar size to Table 8.14 is fairly easy to communicate, whether it be in a spreadsheet or some other manner. However, the table for zip codes contains over 30,000 records when using just the first five characters of zip code. Using the full zip code would lead to a table of millions of rows. To have to communicate this table every time we want to communicate the rates, or changes to them, can be onerous. We can instead break the zip code table into two parts. The first part will map each zip code to a group. The second will match each group to a relativity. For example, Table 8.10 could be restated as Table 8.15. This way, so long as the mapping from zip code to group does not change, we can communicate it just once. The regular rate updates can include just the relativity for area groups.

**Table 8.15. Zip code relativities separated into a first mapping between zip codes and area groups and then from area groups to relativity.**

| zip code | area group | area group | relativity |
|----------|------------|------------|------------|
| 15668    | 22         | 1          | 0.379      |
| 21822    | 62         | 2          | 0.385      |
| 60077    | 56         | 3          | 0.391      |
| 83607    | 95         | ...        | ...        |
| 85248    | 40         | 22         | 0.531      |
| ...      | ...        | ...        | ...        |
| ...      | ...        | 56         | 0.917      |
| ...      | ...        | ...        | ...        |

(Note that the difference of 1.0162 between each group was derived as follows: in our case, the minimum zip code relativity is 0.379 and the maximum is 1.851. The (multiplicative) difference is 4.884. If we are prepared to have 100 groups, then the (multiplicative) difference between each group is 1.0162, that is,  $1.0162^{99} = 4.908$ ).<sup>75</sup>

The above separation of area rating into two separate tables serves another useful purpose. A separate team or project can work on allocating zip codes to high- and low-area groups. The first-stage model can then be fit with area group as a feature.

The above discussion applies equally to aircraft groups, where the underwriters may (or may not) find it easier to discuss the Cessna 172M being in group 5 and the Bell 47G helicopter being in group 95 rather than talking about relativities of 1.37 and 3.13. In general, splitting out the tables in this way gives transparency and interpretability. We can easily show the composition of the final rate, and business experts can more easily challenge it.<sup>76</sup>

---

<sup>75</sup> While this is one sensible way to create the relativities, it is not the only such way.

<sup>76</sup> ...which is a good thing.

