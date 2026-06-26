---
paper: chalk_et_al
chapter: 5
title: Nonlinear Effects
topics: [feature_engineering, step_functions, hinge_functions, mars, nonlinear_effects, fused_lasso, ordinal_categorical_variables]
key_formulas: [step_function, hinge_function_max_0, fused_lasso_penalty]
---

> **TL;DR**
> - GLMs are linear in features; step functions (I[x ≥ t]) and hinge functions (max(0, x − t)) are engineered features that let the GLM approximate any piecewise-linear nonlinear effect.
> - Create many step/hinge functions (e.g., one per unique age value), then use LASSO to select the relevant subset via k-fold CV; MARS automates knot placement in a forward-stepwise manner.
> - MARS generates knots using the target variable, so cross-validation must create MARS knots separately within each fold to avoid leakage.
> - Step functions are equivalent to the fused LASSO (with λ₁=0); they are also the basis functions used by tree-based models; hinges are piecewise-linear versions of ReLU functions.
> - For ordinal categorical variables, encode as cumulative step functions (one per level) with a monotonicity constraint to ensure interpretable, non-decreasing relativities.

# 5. Nonlinear Effects

## 5.1. Feature Engineering

The aim of our models is to capture the relationship between things we know about the risk and the frequency of accidents. We refer to the things we know about our risk as features. We have seen above that, given a set of features, the LASSO and elastic net can select the relevant features based on your data. This is known as “feature selection.”

GLMs cannot create features themselves. For example, we might know that the weather at or near certain locations is extreme, and therefore certain types of claim have a higher frequency at or near those locations. We know that for each policy we need to calculate the distance from the nearest extreme weather area and to use that as a feature. Now we add to each line of our data the location of all the extreme weather areas and of the policy itself. Although we have put the information into the dataset, the GLM will not do the calculation itself and will not pick up the effect. For example, Table 5.1 shows some sample data. Each observation contains the location of a risk and the location of high risk weather area 1. The GLM will not pick up the fact that location A is near high-risk weather area 1 and location B is not.

**Table 5.1. Even if all of Latitude, Longitude, Latitude\_1, and Longitude\_1 are features, a GLM will not pick up that location A is near high-risk weather area area 1 and location B is not. We need to add a new feature, distance\_1, which is the distance from the high-risk weather area.**

| Location                   | Latitude   | Longitude   | Latitude_1 | Longitude_1 |
|----------------------------|------------|-------------|------------|-------------|
| A (Metairie, Louisiana)    | 29.9841° N | 90.1529° W  | 29.9511° N | 90.0715° W  |
| B (Sacramento, California) | 38.5816° N | 121.4944° W | 29.9511° N | 90.0715° W  |

We need to do the calculation and add just one new column—the distance from the nearest extreme weather area—into the dataset. In our example, we add a new feature, `distance_1`, which is the distance of each location from high-risk weather area 1 (9 km for location A, and 3,000 km for location B). Creating a new feature is called feature engineering.

Another example of feature engineering is the creation of a credit score. It might be that the credit score is created from 50 features. While we could include all 50 features in the model, there are various reasons why we might want to create a credit score feature and use only that:

- The model output will be easier to interpret.
- If many of the features underlying the credit score are only marginally effective, penalized regression might remove them completely from the model so that the final credit score implied by the fitted model is not as strong as it could have been.
- Credit score as a whole might strongly interact with other features in the model, whereas this interaction would be very hard to fit to the individual components of the credit score even if it is visible.
- There may be a separate department (or an external vendor) which understands all credit-related features (and the legal aspects of which can be used and which cannot). They might best be placed to build and maintain a credit score model, passing only the result to the insurance model-building team.

Sometimes it is not obvious that we need to engineer new features. Consider aircraft age on our FAA-NTSB model. We know that accident frequency varies with aircraft age, and we have the aircraft age feature on our model. However, as we have seen above, this is not sufficient because the relationship is not linear in aircraft age (or the log of aircraft age). We need to somehow engineer new features to allow our GLM to pick up the right shape for this effect.

Goldburd et al. (2025) discuss three approaches:

- binning the variable
- adding polynomial terms
- using piecewise linear functions.

They note various disadvantages of the first two approaches. Binning the variables can add many extra parameters into the model, can lead to lack of continuity in the estimates, and will ignore variation within the bins. Polynomial terms may behave erratically at the edges of the data.

We will look at two types of piecewise linear functions: step functions and hinge functions. After discussing each of these, our approach will be simple. We will create lots of them, add them to our data, and then use LASSO or elastic net to choose those most relevant to our model based on our data.

## 5.2. Step Functions

A step function is a function which outputs 1 if its input is at or above a threshold and zero otherwise. Table 5.2 shows an example. The function takes aircraft\_age as an input and returns 1 when aircraft age  $\geq 30$  and zero otherwise.

**Table 5.2. A step function which has a threshold at aircraft age 30.**

| aircraft_age | aircraft_age_stp_30 |
|--------------|---------------------|
| 1            | 0                   |
| 7            | 0                   |
| 17           | 0                   |
| 31           | 1                   |
| 42           | 1                   |

Let's remove aircraft age from our model and replace it with the step function in Table 5.2—the first column will be replaced by the second column.

We now fit a model using only the feature aircraft\_age\_stp\_30. The fitted model is

$$\log \text{ frequency} = -5.2815 - 1.4689 \times \text{aircraft\_age\_stp\_30}$$

or, taking exponents of both sides

$$\text{frequency} = 0.00509 \times \exp[-1.4689 \times \text{aircraft\_age\_stp\_30}].$$

In other words, the model predicts a frequency of 0.00509 for aircraft ages 29 or less and  $0.00509 \times 0.2302$  for aircraft ages 30 or more ( $\exp[-1.4689] = 0.2302$ ). This result is shown in Figure 5.1.

![Scatter plot of accident frequency vs aircraft age with a step function model.](dff659a422a9e5edd8ce41823a863379_img.jpg)

The figure is a scatter plot showing 'accident frequency' on the y-axis (ranging from 0.0000 to 0.0100) against 'aircraft age' on the x-axis (ranging from 0 to 50). Red dots represent 'actual frequency' data points. A blue line represents the 'predicted frequency' from a GLM model using a single step function at age 30. The predicted frequency is constant at approximately 0.0050 for ages 0 to 29, then drops sharply to approximately 0.0010 for ages 30 and above. The actual data shows a general downward trend with significant fluctuations, including a peak near age 0 and a sharp drop around age 30.

Scatter plot of accident frequency vs aircraft age with a step function model.

**Figure 5.1. A model for aircraft age using one step function only. The step is at age 30. The GLM picks up the lower frequency after age 29 but has not been given any features to be able to pick up any changes in frequency between age 0 and 29.**

We can see visually that there are some big frequency changes near aircraft ages 5 and 15 which the GLM could not model since it was not given the relevant features. We can therefore add two more features—these being step functions at 5 and 15. Our model will now use the columns shown in Table 5.3 (except aircraft age).

**Table 5.3. Step function with thresholds at aircraft ages 5, 15 and 30.**

| aircraft_age | aircraft_age_stp_5 | aircraft_age_stp_15 | aircraft_age_stp_30 |
|--------------|--------------------|---------------------|---------------------|
| 1            | 0                  | 0                   | 0                   |
| 7            | 1                  | 0                   | 0                   |
| 17           | 1                  | 1                   | 0                   |
| 31           | 1                  | 1                   | 1                   |
| 42           | 1                  | 1                   | 1                   |

The fitted model is

$$\begin{aligned} \log \text{ frequency} = & -4.8292 \\ & -0.6881 \times \text{aircraft\_age\_stp\_5} \\ & -0.5711 \times \text{aircraft\_age\_stp\_15} \\ & -0.6237 \times \text{aircraft\_age\_stp\_30}. \end{aligned}$$

Taken exponents, this simplifies to

$$\text{frequency} = \begin{cases} 0.00783 & \text{if aircraft age} < 5 \\ 0.00394 & \text{if } 5 \leq \text{aircraft age} < 15 \\ 0.00222 & \text{if } 15 \leq \text{aircraft age} < 30 \\ 0.00119 & \text{if aircraft age} \geq 30. \end{cases}$$

This result is shown in Figure 5.2. The shape of the GLM predicted frequencies is closer to the actual frequencies but is still limited by the model only being given three features.

![Figure 5.2: A scatter plot comparing actual aircraft accident frequencies with predicted frequencies from a GLM model. The x-axis is 'aircraft age' (0 to 50) and the y-axis is 'accident frequency' (0.0000 to 0.0100). Red dots represent actual frequencies, and a blue step function represents predicted frequencies. The predicted function has steps at ages 5, 15, and 30, showing a general downward trend that matches the overall shape of the actual data but lacks fine detail.](09b5a76dd3d981abcc585df1314ef30a_img.jpg)

Figure 5.2 is a scatter plot comparing actual aircraft accident frequencies (red dots) with predicted frequencies (blue step function). The x-axis represents aircraft age (0 to 50), and the y-axis represents accident frequency (0.0000 to 0.0100). The predicted frequency is a step function that decreases at ages 5, 15, and 30, capturing the general downward trend of the actual data but missing some local details.

| Aircraft Age | Actual Frequency (approx.) | Predicted Frequency |
|--------------|----------------------------|---------------------|
| 0 - 5        | 0.0090 - 0.0100            | 0.00783             |
| 5 - 15       | 0.0030 - 0.0060            | 0.00394             |
| 15 - 30      | 0.0010 - 0.0040            | 0.00222             |
| 30 - 50      | 0.0000 - 0.0040            | 0.00119             |

Figure 5.2: A scatter plot comparing actual aircraft accident frequencies with predicted frequencies from a GLM model. The x-axis is 'aircraft age' (0 to 50) and the y-axis is 'accident frequency' (0.0000 to 0.0100). Red dots represent actual frequencies, and a blue step function represents predicted frequencies. The predicted function has steps at ages 5, 15, and 30, showing a general downward trend that matches the overall shape of the actual data but lacks fine detail.

**Figure 5.2. A model for aircraft age using three step functions only. The GLM is now able to pick up some of the key aspects of the shape, but there is clearly some detail still missing.**

There is a problem with this approach so far—we are continually having to look at the result and decide ourselves whether or not it is good enough. Given that we know that LASSO and elastic net can simply select the features needed based on the data, the obvious solution is to give the GLM many features—one step function for each age and to allow the penalization to select the features which optimize k-fold cross-validation performance. We therefore create 50 features—one step function for each age and run a penalized GLM. The k-fold cross-validation curve is shown in Figure 5.3. We can see that at the best cross-validation performance there are 19 nonzero coefficients and that the simplest model with a cross-validation performance within 1 s.e. of this performance has 11 parameters. As we have previously seen, when the standard errors are large, the “1 s.e.” model is not on the flat part of the cross-validation performance curve. Also, although not shown here, for every fold the performance of the “1 s.e. model” is not as good as the model with the maximum average cross-validation performance. We therefore choose the simplest model with a cross-validation performance within 2%<sup>18</sup> of the best cross-validation performance—the upper horizontal dashed line shows this level. Our chosen model has 17 step functions.

![Figure 5.3: A cross-validation curve plot showing pseudo-R^2 on the y-axis (ranging from 0.00 to 0.03) versus log(lambda) on the x-axis (ranging from -15.0 to -7.5). The plot features a red line with circular markers representing the mean cross-validation performance, accompanied by a grey shaded area indicating the standard error. A vertical dashed line at log(lambda) = -10.0 is labeled 'max' and corresponds to 19 nonzero coefficients. Another vertical dashed line at log(lambda) = -7.5 is labeled '1 s.e.' and corresponds to 11 nonzero coefficients. Two horizontal dashed lines are present: the upper one represents 98% of the best performance, and the lower one represents the 1 s.e. level. The red curve is relatively flat between log(lambda) = -15.0 and -10.0, then drops sharply after the 1 s.e. point.](57e7a913a27e03b719a102d02c6bf985_img.jpg)

Figure 5.3: A cross-validation curve plot showing pseudo-R^2 on the y-axis (ranging from 0.00 to 0.03) versus log(lambda) on the x-axis (ranging from -15.0 to -7.5). The plot features a red line with circular markers representing the mean cross-validation performance, accompanied by a grey shaded area indicating the standard error. A vertical dashed line at log(lambda) = -10.0 is labeled 'max' and corresponds to 19 nonzero coefficients. Another vertical dashed line at log(lambda) = -7.5 is labeled '1 s.e.' and corresponds to 11 nonzero coefficients. Two horizontal dashed lines are present: the upper one represents 98% of the best performance, and the lower one represents the 1 s.e. level. The red curve is relatively flat between log(lambda) = -15.0 and -10.0, then drops sharply after the 1 s.e. point.

**Figure 5.3. 50 step functions as features—one for each age. At the maximum validation performance, 19 of these features are selected. The “1 s.e.” model is simpler, with only 11 features, but is not on the flat part of the cross-validation performance curve. The upper dashed line is at 98% of the best cross-validation performance, and we have chosen the simplest model with this performance.**

<sup>18</sup> This is based on our judgment that the cross-validation performance is fairly flat at this point, and we prefer a slightly simpler model where possible, as it might generalize better.

Figure 5.4 shows the model predictions compared to the actual frequency. The penalized GLM has come close to picking up most of the shape of how actual frequency varies by age but without overreacting to the noise. However, at aircraft ages greater than 20 years old the predictions look too high. The reason for this is that the LASSO has not only selected the best step functions, it has also shrunk the coefficients of the remaining ones—and this is not necessarily optimal. A solution (the Relaxed Lasso) is discussed in Section 4.5.

![Figure 5.4: A scatter plot showing accident frequency (y-axis, 0.0000 to 0.0100) versus aircraft age (x-axis, 0 to 50). Red dots represent actual frequency data points. A teal line represents the model's predicted frequency, which is a step function. The prediction starts high (around 0.0085) for age 0, drops sharply to about 0.0055 by age 3, then more gradually to about 0.0025 by age 20, and remains flat at that level for ages 20 to 50. The actual data points generally follow this downward trend but show significant noise, with some points as high as 0.0100 and others as low as 0.0000.](14294c70b5a0effb6bdaf09c46bbdc9f_img.jpg)

Figure 5.4: A scatter plot showing accident frequency (y-axis, 0.0000 to 0.0100) versus aircraft age (x-axis, 0 to 50). Red dots represent actual frequency data points. A teal line represents the model's predicted frequency, which is a step function. The prediction starts high (around 0.0085) for age 0, drops sharply to about 0.0055 by age 3, then more gradually to about 0.0025 by age 20, and remains flat at that level for ages 20 to 50. The actual data points generally follow this downward trend but show significant noise, with some points as high as 0.0100 and others as low as 0.0000.

**Figure 5.4. Predicted compared to actual frequency. The 17 step-functions selected pick up much of the shape of the actual frequency, though the predictions above age 20 look high.**

## 5.3. Hinge Functions

If we look again at Figure 5.4 we see that the shape of the aircraft age effect is really made up of three parts: 0 to 3 years—a steeply reducing linear trend; 4 to 28 years—a less steep, but still reducing, linear segment; 29 years onward—a mostly flat segment. The flat step functions we have been using so far cannot easily pick up an effect which is a slope. We have to use lots of small flat line segments to pick up a slope. That is why we needed 11–17 step functions to get close to the correct shape. A simple way to pick up a shape which is made up of segments of straight-line slopes is to use “hinge functions.” These are discussed in Goldburd et al. (2025), Section 5.4.4. Consider:

$$h(\text{aircraft age}, 28) = \max(0, \text{aircraft age} - 28)^{19}$$

Examples of some values of this function are shown in Table 5.4, and the shape of this function is shown graphically in Figure 5.5.

**Table 5.4. A hinge function with a “hinge” at aircraft age 28.**

| aircraft_age | aircraft_age_h_28 |
|--------------|-------------------|
| 0            | 0                 |
| 20           | 0                 |
| 28           | 0                 |
| 29           | 1                 |
| 49           | 21                |

![Figure 5.5: A graph of a hinge function with a hinge at age 28. The x-axis is labeled 'aircraft age' and ranges from 0 to 50. The y-axis is labeled 'feature value' and ranges from 0 to 20. The function is zero for aircraft age up to 28, and then increases linearly with a slope of 1 for aircraft age greater than 28. The line starts at (28, 0) and ends at (50, 22).](02c999e5846341813b658e446e9a6fda_img.jpg)

Figure 5.5: A graph of a hinge function with a hinge at age 28. The x-axis is labeled 'aircraft age' and ranges from 0 to 50. The y-axis is labeled 'feature value' and ranges from 0 to 20. The function is zero for aircraft age up to 28, and then increases linearly with a slope of 1 for aircraft age greater than 28. The line starts at (28, 0) and ends at (50, 22).

**Figure 5.5. An example of a hinge function with a “hinge” at age 28. The function is zero until age 28 and then increases with age. If there is a change of slope of the age effect at age 28, this hinge function can pick it up.**

<sup>19</sup> This is sometimes expressed as  $(\text{aircraftage} - 28)^+$

We now create two hinge functions so that our GLM will have (besides the intercept) three features, age itself (which is a hinge function with the knot at zero), and hinge functions with knots at 4 and 28. The penalized GLM fits the following model:

The fitted model is

$$\begin{aligned} \log \text{ frequency} = & -4.5566 \\ & -0.1599 \times \text{aircraft\_age} \\ & +0.1011 \times \text{aircraft\_age\_h\_4} \\ & +0.0336 \times \text{aircraft\_age\_h\_28}. \end{aligned}$$

We can see that the slope gets less steep for ages 4 and above and then again for ages 28 and above. The actual and predicted frequencies are shown in Figure 5.6. With only three features, the GLM has closely picked up the shape that we see in the data. This is not surprising, given that we choose the knots having seen the data. Besides being time-consuming if we were to do this for every continuous dependent variable, it is also suboptimal as we may be misled by patterns that we think we see in the data which are actually just noise.

![Figure 5.6: A scatter plot showing accident frequency versus aircraft age. The x-axis is 'aircraft age' ranging from 0 to 50. The y-axis is 'accident frequency' ranging from 0.0000 to 0.0100. Red dots represent 'actual frequency' data points. A solid blue line represents the 'predicted frequency' from the GLM model. The curve starts at approximately 0.0100 at age 0 and decreases, with a noticeable change in slope around age 4 and again around age 28, as indicated by black diamonds on the curve. The model closely follows the general trend of the data points.](b387daba28c5aa523b84b26d6ba3d177_img.jpg)

Figure 5.6: A scatter plot showing accident frequency versus aircraft age. The x-axis is 'aircraft age' ranging from 0 to 50. The y-axis is 'accident frequency' ranging from 0.0000 to 0.0100. Red dots represent 'actual frequency' data points. A solid blue line represents the 'predicted frequency' from the GLM model. The curve starts at approximately 0.0100 at age 0 and decreases, with a noticeable change in slope around age 4 and again around age 28, as indicated by black diamonds on the curve. The model closely follows the general trend of the data points.

**Figure 5.6. FAA-NTSB: A model for aircraft age using two hinge functions only. This GLM closely picks up the shape of the effect that we see.**

As previously, one approach is to give the GLM 50 features—a hinge function with knots at each age. The k-fold cross-validation curve is shown in Figure 5.7. We can see that the performance is very similar for models for the maximum number of features down to much simpler models. As previously, due to the large standard error of the cross-validation means, the “1 s.e. rule” seems to pick a model which is too simple. We instead choose a model which is within 2%<sup>20</sup> of the best performance (the upper dashed line in the figure).

![Figure 5.7: A k-fold cross-validation curve for a model for aircraft age using 50 hinge functions as features. The x-axis is log(lambda) ranging from -14 to -6. The y-axis is pseudo-R^2 ranging from 0.010 to 0.030. The curve shows a peak around log(lambda) = -12, followed by a sharp decline. A left vertical dashed line marks the 'max' point at log(lambda) = -12. A right vertical dashed line marks the '1 s.e.' point at log(lambda) = -8.5. An upper dashed line indicates the 2% rule threshold. The number of features (hinges) is indicated above the x-axis: 29, 27, 20, 14, 12, 10, 9, 3, 1, 1, 1, 1, 1, 0.](a4cabfec798f5330bf8cc750d4d518ee_img.jpg)

Figure 5.7: A k-fold cross-validation curve for a model for aircraft age using 50 hinge functions as features. The x-axis is log(lambda) ranging from -14 to -6. The y-axis is pseudo-R^2 ranging from 0.010 to 0.030. The curve shows a peak around log(lambda) = -12, followed by a sharp decline. A left vertical dashed line marks the 'max' point at log(lambda) = -12. A right vertical dashed line marks the '1 s.e.' point at log(lambda) = -8.5. An upper dashed line indicates the 2% rule threshold. The number of features (hinges) is indicated above the x-axis: 29, 27, 20, 14, 12, 10, 9, 3, 1, 1, 1, 1, 1, 0.

**Figure 5.7. A model for aircraft age, using 50 hinge functions as features—one for each age. The left vertical dashed line shows the choice of  $\log(\lambda)$  which maximizes pseudo- $R^2$ . The average cross-validation performance is quite flat at that point. We choose instead a simpler model which has a performance within 2% of the maximum—the upper dashed line. That model has aircraft age and seven hinges.**

The model chosen above uses only the original aircraft\_age features and seven hinge functions. The resulting predictions are shown in Figure 5.8. They seem mostly reasonable, though predictions at ages 0 and 1 might be too low.

<sup>20</sup> As above, this is based on our judgment. It leads to a reasonably performing model being chosen, and at this point in our work we preferred simpler models, as they are easier to explain. However, a 2% performance reduction is significant, and later on, when we were looking to maximize performance, we did use models at the maximum of the cross-validation curve.

As an example of hard-thresholding (see Section 4.5), in Figure 5.9 we show a model with the same hinge functions as above, but without penalization.

![Figure 5.8: A scatter plot showing accident frequency vs aircraft age. Red dots represent actual frequency, and a teal line represents predicted frequency. Black diamonds indicate hinge points. The predicted frequency is generally lower than the actual frequency for ages 0-10 and higher for ages 10-50.](4af0349328e735d480210fe9a3e595cb_img.jpg)

Figure 5.8 is a scatter plot with 'aircraft age' on the x-axis (ranging from 0 to 50) and 'accident frequency' on the y-axis (ranging from 0.0000 to 0.0100). Red dots represent 'actual frequency' data points. A teal line represents the 'predicted frequency' from a model. Black diamonds are placed on the teal line at specific ages, representing the hinge points. The predicted frequency starts high at age 0 (around 0.0085) and decreases as age increases, following a smooth curve that is generally lower than the actual frequency for ages 0-10 and higher for ages 10-50.

Figure 5.8: A scatter plot showing accident frequency vs aircraft age. Red dots represent actual frequency, and a teal line represents predicted frequency. Black diamonds indicate hinge points. The predicted frequency is generally lower than the actual frequency for ages 0-10 and higher for ages 10-50.

**Figure 5.8. Predictions from a model using aircraft age itself and seven hinges (the black diamonds show the points chosen for the hinges). The predictions at older ages look better, but predictions for ages 0 and 1 may be low.**

![Figure 5.9: A scatter plot showing accident frequency vs aircraft age. Red dots represent actual frequency, and a teal line represents predicted frequency. Black dots indicate hinge points. The predicted frequency is generally higher than the actual frequency for ages 0-10 and lower for ages 10-50.](47e01b9fff5e98218a11fa5958b988fb_img.jpg)

Figure 5.9 is a scatter plot with 'aircraft age' on the x-axis (ranging from 0 to 50) and 'accident frequency' on the y-axis (ranging from 0.0000 to 0.0100). Red dots represent 'actual frequency' data points. A teal line represents the 'predicted frequency' from a model. Black dots are placed on the teal line at specific ages, representing the hinge points. The predicted frequency starts high at age 0 (around 0.0095) and decreases as age increases, following a smooth curve that is generally higher than the actual frequency for ages 0-10 and lower for ages 10-50.

Figure 5.9: A scatter plot showing accident frequency vs aircraft age. Red dots represent actual frequency, and a teal line represents predicted frequency. Black dots indicate hinge points. The predicted frequency is generally higher than the actual frequency for ages 0-10 and lower for ages 10-50.

**Figure 5.9. As an example of hard-thresholding. The age feature itself and the seven hinge functions chosen by the LASSO are used in a model with no penalization. The black dots show the points chosen for the hinges. Predictions for ages 0 and 1 are closer to the data.**

## 5.4. Step Versus Hinge

Given our discussion of step and hinge functions, which is better? There is no clear answer, but the following points might be considered by the practitioner.

We mentioned previously that a disadvantage of polynomial terms is that they may behave erratically at the edges of the data. Step and hinge functions tend to behave in a more stable—but different—way at the edges. Step functions are flat at the edges of the data, and hinges may slope up or down.

Consider a feature such as annual mileage in private auto, where the last step or hinge function is at 10,000 miles, but some policies have a declared annual mileage of 100,000 or more. If we use step functions and the last step is 10,000 miles, then the price will be the same for all mileages greater than 10,000. If the last hinge was upward sloping at 10,000 miles, then prices at much higher mileage will be exceedingly high. The practitioner may prefer one approach or the other.

Sometimes, we want and expect the “customer journey” through successive renewals (i.e., change in premium charged) to be smooth. For example, we might wish the private auto price to go down smoothly as customer age increases from age 17 to age 30. A step function might be flat from age 17 to 20, followed by a significant drop at age 21, and then flat again from age 21 to age 30. While a practitioner can smooth the results of a GLM based on step functions, the cross-validation performance will no longer be available (unless the practitioner repeats the smoothing for each fold looking only at the training data). In these cases, hinge functions may be preferable.

There is one situation where monotonic step functions may be particularly useful: ordinal categorical features.<sup>21</sup> We consider this in more detail in Section 5.7.2.

If the practitioner does expect the price to suddenly change from one value of a feature to another, in a discontinuous manner, then step functions are preferred for that feature.

As an aside, we note certain similarities to machine learning techniques. Step functions are the functions used by tree-based predictive models, albeit usually with more complicated conditions for assigning a one to a record. They are therefore the basic functions used in random forests and gradient boosting machines. Hinge functions are a generalization of functions widely used in deep learning called Rectified Linear Unit (ReLU) functions. These functions are not linear, but they are differentiable almost everywhere and allow parameters in neural networks to be found through a differentiation process called back-propagation.

---

<sup>21</sup> Ordinal categorical features are categorical features which have a meaningful order—this will be explained later in detail.

## 5.5. Multivariate Adaptive Regression Splines (MARS)

Our approach above was to create many features (either step functions or hinges) and then to allow penalized regression to choose the most suitable hinges. We suggested creating one feature for each age. Doing this for every continuous variable will create possibly hundreds or even thousands of features, and fitting a penalized regression model on that many features is computationally expensive. If the full design matrix is stored in memory, then the problem can be memory intensive as well. While proprietary software exists which uses custom solvers to solve this problem, we instead choose a limited number of knots. Although this is likely to produce a less powerful model, if the knots are chosen carefully, the reduction in performance may be limited. One approach is to choose knots based on percentiles or weighted percentiles of the data. Alternatively (and as mentioned in Goldburd et al. (2025) Section 10.4) we can use a model type called multivariate adaptive regression splines (MARS<sup>22</sup>).

MARS (Friedman (1991)) can be considered a type of decision tree, but using hinges<sup>23</sup> rather than step functions. Consider a decision tree using aircraft age. At the start of training, the first decision will be created by finding the “best” aircraft age at which to split aircraft into two groups, one with higher frequency and one with lower. By “best” we mean that if we create predictions in this way, the performance will be better than if any other split was made. It is exactly the same as using one step function in our discussion above where that one step function is chosen so that it maximizes performance on the training data. Likewise at the start of training, MARS will find the best knot so that if it creates a spline at that point, and finds the best coefficient to apply to that spline, performance will be maximized on the training data. Again, this is exactly the same as using one spline function in our discussion above, where that one spline function is chosen so that it maximizes performance.

After the first spline, MARS will continue to add splines in a stepwise manner (similarly to stepwise forward linear regression), so that each added spline improves the performance more than any other spline would have done. MARS is designed with interactions in mind, in the same way as decision trees; however, typical implementations allow the user to ask for interactions not to be fitted—which is what we will do.

---

<sup>22</sup> Friedman, the inventor of this method, could equally have called it “Adaptive Piecewise Linear Regression for Multivariate Data,” but that would not have had the same catchy acronym. Because the term “MARS” is trademarked, the implementation in R is called EARTH. Its creator, Stephen Milborrow, said that the “backronym” for EARTH is Enhanced Adaptive Regression Through Hinges.

<sup>23</sup> The “S” in MARS is an abbreviation for “splines.” A spline is a function that, in some sense, smoothly passes through a set of points. MARS actually uses linear splines, which are essentially identical to the hinges we have discussed. We will use the terms “hinge” and “spline” interchangeably.

Given that MARS continues to add splines based only on improvements to training error, without some adjustment, it would be guaranteed to overfit. This was understood in its original implementation and a “pruning” method was included which removed the splines most likely to lead to overfitting. However, in a manner consistent with our general approach in this monograph, we turn off the pruning in MARS and allow the LASSO to select the relevant splines.

There is a further issue we need to consider. In our first discussion above, our step functions and hinges were created without reference to our target variable, in an unsupervised manner. We then proceeded to use cross-validation to find the best level of penalization. Cross-validation works because it uses data which our model fitting process has not yet seen. When we create splines with MARS, we are looking at the target variable in order to decide where to put the knots. If we use all of our data to create the MARS splines, by the time we get to cross-validation, our model fitting process has already seen the values of the target variable on the validation folds and the chosen value of  $\lambda$  will be too low. We therefore take care during cross-validation to create the splines separately for each fold.

Although we do not consider it further here, in the same way that MARS can be used to create spline-based features for inclusion in the LASSO, decision trees can be used to create the thresholds for step functions.

## 5.6. Case Study—Piecewise Linear Functions

Finally, we return to our FAA-NTSB case study. We still exclude the High Cardinality Categorical Variables (HCCVs) but for numeric variables, we use an approach based on the above discussion. We use three approaches to choose the features to use in the LASSO:

- Start with 25 equally spaced step functions for each numeric feature.
- Start with 25 equally spaced hinge functions for each numeric feature.
- Allow MARS to select the starting hinges. In this case, the starting hinges are created separately for each fold.

Table 5.5 compares the cross-validation performance and the number of nonzero step or hinge functions chosen for three methods.

**Table 5.5. Model performance (pseudo- $R^2$ ) and number of nonzero features based on three ways of choosing the starting features to capture nonlinear effects.**

| feature creation | cross-validation performance | nonzero features |
|------------------|------------------------------|------------------|
| step functions   | 0.150                        | 67               |
| hinges           | 0.149                        | 77               |
| MARS hinges      | 0.150                        | 63               |

The three approaches have similar levels of performance. We don't have a preference between the step functions model and the MARS hinges model. Performance-wise, they both perform slightly better than the hinges model. The step functions model is easier to fit than the MARS model (we do not need to add the MARS step into the model building of each fold). The MARS hinges function uses slightly fewer features and will probably require less manual adjustment (interpolation) when creating the actual rate plan.

![Figure 5.10: Two plots showing frequency vs. aircraft age and maximum speed. Each plot includes a histogram (yellow bars), actual response (red dots), and a fitted model (teal line).](9bceafff3642dab71de6f646228793d7_img.jpg)

Figure 5.10 consists of two plots. The top plot shows 'frequency' on the y-axis (ranging from 0.000 to 0.009) versus 'aircraft age' on the x-axis (ranging from 0 to 50). It includes a histogram of yellow bars, red dots representing 'Actual response', and a teal line representing the 'Fitted model'. The bottom plot shows 'frequency' on the y-axis (ranging from 0.000 to 0.006) versus 'maximum speed' on the x-axis (ranging from 80 to 200). It also includes a histogram of yellow bars, red dots for 'Actual response', and a teal line for the 'Fitted model'.

Figure 5.10: Two plots showing frequency vs. aircraft age and maximum speed. Each plot includes a histogram (yellow bars), actual response (red dots), and a fitted model (teal line).

**Figure 5.10. The model seems to pick up key aspects of how frequency varies with the features shown. The height of the yellow bars indicates the relative amount of exposure for each value on the x-axis.**

One issue with the fitted model is that the predictions continue to reduce as the aircraft age increases—even at high ages, where there is little data. This is the result of extrapolation based on the hinges, as discussed in Section 5.4. Where a practitioner prefers hinge to step functions but is concerned by this issue, they could consider manually adjusting the values of the hinge functions to be constant at the extremes of the data (for example, for all values of each numeric feature greater than the 99th percentile).

## 5.7. Practically Speaking

### 5.7.1. *Random features*

In the above discussion on MARS, we allowed it to generate hinges which we then fed into the LASSO to benefit from its implicit feature selection. Depending on the values of certain MARS parameters, it will continue to generate hinges, even when those hinges are picking up random noise in the training data, rather than signal. While we rely on the LASSO to ignore irrelevant features, as datasets increase in size, having tens or possibly hundreds of irrelevant features can cause computation time and resource requirements to increase. We therefore added a random numeric feature<sup>24</sup> to our data. Once the MARS generated list of hinges started to select hinges based on this random feature, we knew that it must be picking up random noise (because there is no signal in the random feature), and we stopped the process from generating further hinges.

In general, the idea of adding one or two randomly generated features to a dataset can be very useful. If whichever process is used to create the model ends up including these features, we ought to be concerned.

The idea of “shadow” variables in some machine learning techniques is similar. Each feature is randomly shuffled and added back to the data alongside the original feature.<sup>25</sup> If, in the final model, the random version of the feature is more important than the original feature, there is probably something wrong with the modeling process.

### 5.7.2. *Ordinal categorical variables*

Consider a feature “quality of pilot” which takes the values poor, worse than average, average, better than average, and good. This is a categorical feature—it has five different categories. There is also meaning in the order of the variable—each level of the category is “better” than the previous level. Hence, this feature is called an ordinal categorical variable. In a GLM, one simple way we can deal with ordinal categorical variables is as follows. We first replace the text of the categories with numbers. “Poor” becomes 1,

<sup>24</sup> We simply created a new feature which was the row number of the dataset, and then we shuffled it.

<sup>25</sup> See for example Kursu and Rudnicki (2010). In our MARS work, too, a shadow variable could be created for each feature, and hinges for that feature would not be used after MARS starts creating hinges for its shadow feature.

“worse than average” becomes 2, and so on. We should not simply put this new numeric feature in the GLM. That is because although 2 is twice 1, it is not true to say that “worse than average” is twice “poor.” Actually, even if that were true, there is no reason to assume that incident frequency will increase or decrease linearly with quality of pilot. However, given our discussion above, what does seem natural is to use step functions at each level of quality. Each level of pilot quality will be represented by five step functions (Table 5.6 shows their values).

**Table 5.6. Values of step functions applied to levels of an ordinal categorical feature.**

| category                | step_1 | step_2 | step_3 | step_4 | step_5 |
|-------------------------|--------|--------|--------|--------|--------|
| 1 – good                | 1      | 0      | 0      | 0      | 0      |
| 2 – better than average | 1      | 1      | 0      | 0      | 0      |
| 3 – average             | 1      | 1      | 1      | 0      | 0      |
| 4 – worse than average  | 1      | 1      | 1      | 1      | 0      |
| 5 – poor                | 1      | 1      | 1      | 1      | 1      |

If accident frequency for some level of quality and above is worse (or better) than accident frequency below that level of quality, then the step function will pick this up. For example, if a nonzero linear predictor is fitted for step\_2, it will be applied to all pilots whose quality is less than good.

We don’t have pilot quality on our FAA data, but to provide some sample output, we simulated this feature. Table 5.7 shows the fitted coefficients for each step function.

**Table 5.7. The first row shows the coefficient for the step function. The next row shows the exponent of the coefficient. Finally, the last row shows for each level of the ordinal categorical feature, the relativity applied to a pilot with that level of experience.**

| category                | step_1 | step_2 | step_3 | step_4 | step_5 |
|-------------------------|--------|--------|--------|--------|--------|
| coefficient             | 0      | 0.515  | 0      | 0.211  | 0.206  |
| exponent of coefficient | 1      | 1.673  | 1      | 1.235  | 1.229  |
| cumulative product      | 1      | 1.673  | 1.673  | 2.06   | 2.539  |

Table 5.8 compares the fitted effects to the true relativities (which we know because we simulated the data). We can see that the step functions have correctly fitted an effect which increases for poorer quality and which is not linear.

**Table 5.8. A comparison of the ground truth with the fitted effect. We can see that the fitted effect is monotonically increasing. The fitted effect for some levels of the factor is quite far out—this is driven by the randomness (and limited volume) of the simulated data.**

| category                | true relativity | fitted effect |
|-------------------------|-----------------|---------------|
| 1 – good                | 1.00            | 1.00          |
| 2 – better than average | 1.66            | 1.67          |
| 3 – average             | 1.80            | 1.67          |
| 4 – worse than average  | 2.01            | 2.07          |
| 5 – poor                | 2.06            | 2.54          |

We decided, before fitting this model, that we wanted the pilot quality effect to be monotonic increasing. For example, we wanted the relativity for a “worse than average” pilot to be more than an “average” pilot. We achieved this by adding a constraint on the linear predictors for each level of pilot quality to be non-negative—hence the coefficients in the first row of Table 5.7 were guaranteed to be non-negative. This ensured that the relativity applied to each function was greater than or equal to 1 and so the overall cumulative effect is monotonic increasing. Adding such constraints is often not a good idea. It is often better to “let the data do the talking.”

If the effect of pilot quality on accident frequency is indeed monotonic increasing then, as long as we have sufficient data in each class, we will get that effect. On the other hand if our classification process for quality of pilot is poor, so that the accident frequency for a “worse than average” pilot is actually better than that of an “average” pilot, the constraints will hide this effect and we will not be able to feed the problem back to the business or whoever created the classification system. Some practitioners therefore have a strong preference to avoid such constraints.

A further example of the above issue is the discount scale in private auto insurance for where a car is parked overnight. There are typically at least three levels for this feature; 1—garaged, 2—parked on a driveway, 3—parked on the road. We might have the expectation that the frequency of claims will be least for the garaged car. For example, it is least likely to be stolen or vandalized or knocked into overnight by a car driving carelessly down the road. It might be tempting therefore to treat it as an ordinal categorical feature and apply non-negative constraints to the linear predictors.

However, in practice, the level 1—garaged feature often has a higher claims frequency than the others. This is because the parked overnight feature is self-declared, and a significant proportion of vehicles declared as parked overnight in a garage are not (in fact, a fair percentage of such policyholders don’t actually have a garage). Beyond misreporting

of this feature, it may also serve as an indicator for the potential misreporting of other self-declared information.

In some cases, insisting on monotone increasing effects does seem reasonable. For example, for the number of historic claims declared at policy inception. We should expect future claims frequency for a policy to increase in line with historic frequency. However, often there is only a small amount of data for three or more historic claims. This can lead to three or more claims being predicted with a lower frequency than one or two claims, which would not be a reasonable rating plan to bring to the market.

### 5.7.3. Surrogate GLMs

Various machine learning model types are much more flexible than GLMs and, with sufficient data and careful tuning, have the potential to perform better than well-fitted GLMs in predicting the value of a target variable given the features. In addition, they can just be given the numeric features and will find a way to make good predictions even if the effect is not linear with the numeric feature. A downside to some of these models is that they are not easy to interpret—there is no easy way to explain to a human the link between the value of the features and the prediction output by the models. Techniques have therefore been developed to help interpret the outputs of such models.

In *Interpretable Machine Learning: A Guide for Making Black Box Models Explainable*, Molnar (2020) provides an accessible introduction to this topic. One of the approaches he mentions is “surrogate models.” This is explained as when “an interpretable model...is trained to approximate the predictions of a black-box model.” A surrogate GLM is a GLM which is trained to approximate the predictions of a machine learning model which is not easily interpretable.

This suggests the following approach to nonlinear effects:

- Train a good machine learning model on the data (for example, a Gradient Boosting Machine)
- Extract information about the shape of the nonlinear effects
- Use the above information to fit a GLM

## 5.8. Technical Note

### 5.8.1. Step functions and the fused LASSO

The penalty term used in penalized regression will impact both the features in the fitted model and their coefficients. In our work above, we wanted the coefficients for aircraft ages near each other to be similar. This is because we have a prior belief that aircraft of similar ages pose a similar risk of accident (all other factors being the same). An early approach to this problem in the literature is called the “fused LASSO.” In their work on this approach, Tibshirani et al. (2005) had  $n$  features that were “close” to each other, much in the same way that aircraft ages are close to each other—that a priori they expected coefficients to be similar. And they proposed to minimize

$$\min_{\beta} \left( -l(\beta) + \lambda_1 \sum_{i=1}^n |\beta_i| + \lambda_2 \sum_{i=2}^n |\beta_i - \beta_{i-1}| \right).$$

The first penalty term is the familiar LASSO penalty term, and the second term adds an extra penalty for changes of coefficient from one feature to the next. This is a very direct and clear way of ensuring that the coefficients for features near each other are the same if possible.

In the fused LASSO, the penalization added by a coefficient depends not only on itself but also on the values of the coefficients next to it. This creates complications in trying to find the optimal coefficients. The approach we have taken here is not to change the penalty term but to change the features going into the model.

In the paper behind the `aglm` R package (Fujita et al. (2020), Kondo (2021)), the authors show a strong connection between the fused LASSO and using step functions. As an example, consider the case where we have four aircraft only, with ages 0, 1, 2, and 3. There is an intercept which picks up the base frequency for age 0 and which is  $\beta_0$ . The coefficients for ages 1, 2, and 3 are  $\beta_1$ ,  $\beta_2$ , and  $\beta_3$ . For convenience, we assume that  $\beta_2 > \beta_1$  and  $\beta_3 > \beta_2$ . Under the fused LASSO, the total penalty is

$$\lambda_1 \times (\beta_1 + \beta_2 + \beta_3) + \lambda_2 \times [\beta_1 + (\beta_2 - \beta_1) + (\beta_3 - \beta_2)].$$

(The first term inside the  $\lambda_2$  multiplication is the full value of the first coefficient since there is no previous coefficient.) If we set  $\lambda_1$  to zero, the penalty is  $\lambda \times \beta_3$ .

Using step functions, we would have steps at 1, 2, and 3. If we choose the intercept to be the same and the parameters to be  $\beta_1$ ,  $\beta_2 - \beta_1$ , and  $\beta_3 - \beta_2$ , then we will get exactly the same predictions, so the likelihood will be the same. In addition, the penalty will be  $\lambda \sum |\beta_i| = \lambda \times \beta_3$ , which is also the same.

Hence we see that our use of step functions is the same as the fused LASSO with  $\lambda_1 = 0$ .

## 5.9. Next Steps

From the results in Section 5.6 we now have a reasonable model for the FAA-NTSB data, with nonlinear effects being fitted and with a better performance than our baseline model. However, it excludes all features that are high cardinality categorical variables. In the next section, we will consider how we might help our GLM to model such features.

