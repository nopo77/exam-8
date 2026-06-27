---
paper: chalk_et_al
chapter: 7
title: Highly Correlated Variables
topics: [multicollinearity, principal_component_analysis, ridge_regression, lasso_feature_selection, correlated_variables, coefficient_paths, variance_inflation]
key_formulas: [ridge_regression_coefficient_paths, pca_components]
---

> **TL;DR**
> - Highly correlated features cause: GLM convergence failures or large/unstable coefficients (including reversals), reduced interpretability, potential adverse selection if a reversal goes live, and unnecessary operational cost.
> - Common causes: natural correlation (age vs. driving experience), data enrichment (credit features), or feature engineering (spread measures of the same underlying variable).
> - LASSO implicitly selects one feature from each correlated group (Zou & Hastie 2005); Ridge retains all but shrinks competing coefficients, often producing same-effect features with opposite signs.
> - PCA replaces correlated features with uncorrelated principal components but is unsupervised — components ranked by variance may not be predictive; use PLS-GLM for a supervised alternative.
> - Coefficient paths (plot of coefficients vs. log λ) reveal reversals at low penalization that resolve as penalization increases — useful diagnostic tool for correlated-variable problems.

# 7. Highly Correlated Variables

The issue of highly correlated variables in data is discussed in Goldburd et al. (2025) (Section 2.9, Correlation Among Predictors, Multicollinearity and Aliasing). In this chapter, we discuss this topic in more detail and illustrate some of the points with a worked example. We will begin by identifying the scenarios that can lead to our data having high correlations. Then we will try to understand why this matters at all—why not just fit a model and proceed as normal? Finally, we will discuss the various approaches to dealing with the issue.

So far in this monograph we have focused on fitting GLMs. The issue we address in this chapter is more general, and therefore before we proceed, it is worth stepping back a little and considering the general process of how to approach supervised learning tasks.

Supervised learning refers to any situation when our data contains a history of many examples with their outcomes. Typically, each example is a row in our dataset and has features (e.g., policyholder age, aircraft make and model) and the outcome (e.g., accident or no accident). We want our model to find a relationship between the features and outcomes on the historic data such that when we apply that relationship to future data, it accurately predicts outcomes when we don't yet know the outcome. Some of the stages in any supervised learning task are:

- Which type of model should we use? This could be a linear model, a tree-based model, or a neural network.
- Which model should we use? If we had decided to use a tree-based model, we could then choose from decision trees, random forests, gradient boosting machines, and their various derivatives. If we had decided to use a linear model, we might decide to use a GLM with penalization and the LASSO. This and the previous choice may simply be performance driven. That is, we will train many model types and choose the one with the best validation performance.
- Given that we already have some data with features, should we try to augment the features and if so how? This is a surprisingly hard task. It includes trying to create or purchase data assets relevant to the problem and trying to engineer new features from features that we already have. This process is called “feature engineering.” It is

not limited to purchasing and engineering features when training the model, we also have to ensure that identically defined features are available when the model is applied operationally.

- Finally, given the model type we are going to use and the set of features in the training data, we may wish to select only certain features to use in training our model or to appear in our final model. This is called “feature selection.”

Issues involving highly correlated variables tend to relate to one or more of these stages, and we will refer to them in our discussion below. Much of what we cover will be related to feature engineering and selection. For a much more detailed coverage we refer the reader to the excellent and easy-to-read book, *Feature Engineering and Selection, A Practical Approach for Predictive Models* (Kuhn and Johnson (2019)).

## 7.1. How Do Highly Correlated Variables Arise?

### 7.1.1. Naturally

Correlation between features in our data can arise naturally. Let us consider a portfolio of young drivers in auto insurance and a jurisdiction where the minimum age to take a driving test is 17. When preparing rates for auto insurance, two features that will often be in the data are driver age and driver experience. Age is often recorded as the driver’s age rounded down to the nearest whole number at the policy start date. Driving experience is often recorded as the number of years since passing the driving test, rounded down to the nearest integer, at the policy start date. (For younger drivers or those with more limited driving experience, rounding down to the nearest month might result in better performing models). If every driver passes their test shortly after their 17th birthday and immediately buys a car and takes out insurance, then every 17-year-old in our data will have zero years’ experience since passing their test, every 18-year-old will have one year, and so on. Driver age and driving experience will be perfectly correlated. In practice we should certainly expect to see among younger drivers a high correlation between driving experience and age.

As an aside, we note that whether or not two features are correlated will depend on the type of insurance and how they are measured. For example in General Aviation insurance, if we are measuring pilot experience as the number of flight hours in the type of aircraft they are insuring, then we would not necessarily expect this to be highly correlated with age—a pilot might move from one type of aircraft to another at various points in their career.

Part of getting to know the data one is working on is to check for highly correlated features. Where we see high correlations when we were not expecting any (and vice versa) we have an opportunity to increase our understanding of the data by finding out why

this is the case.

### **7.1.2. *As a result of data enrichment***

There are very many situations where data enrichment may lead to highly correlated features. Here are some examples:

- In locations where regulation permits use of credit score in rating plans, data might be enriched not only with credit score but also with all the underlying features that are used to create the score. It would be surprising not to find high correlations both between these features themselves (e.g., monthly income, home ownership, average account balance, etc.) and between them and the credit score.
- More generally, enrichment can consist of thousands of new features, many of which measure similar things. A feature may related to whether or not the insured has had certain types of court judgments against them and if so, how many. This feature might be present a few times, being measured (say) over the past three months, six months, one year, and three years. These features will be highly correlated.
- Enrichment features for geographical analysis may include the distance to the nearest school, the nearest police station, and the nearest fire hydrant. These may all be correlated with population density and with each other—hence, we may find some of these features to be highly correlated.

As mentioned above, before using data, correlations should be checked and the reasons for high correlations should be understood. This is especially true for data enrichment sources which might be coming from third parties—understanding the reliability of such data is particularly important.

### **7.1.3. *As a result of feature engineering***

To “engineer features” means to create new columns of data (features) which are based on the original columns that were provided. We have met feature engineering a few times in this monograph. When we took a single numeric feature and added many step or hinge functions, we were engineering features to allow our GLM to express a particular relationship. This is known as one-to-many feature engineering. We also discussed adding the distance between two points (e.g., address of the policyholder and the address where their vehicle is garaged) as a new feature. Later in this chapter we will replace all the numeric features in the example we will be working on with a different set of features (that are not correlated with each other). That is known as many-to-many feature engineering.

It is up to the modeler together with expertise from the business to ensure that any potentially useful features that the model would not otherwise engineer for itself are created and added to the data. Sometimes this process may lead to having highly correlated

features. Consider the case of commercial aviation insurance. Each insured is a commercial airline operating a fleet of craft (e.g., United Airlines, Southwest Airlines). For each fleet our data might contain one line per aircraft per year, with details of the aircraft and of any accidents or incidents it was involved in, together with the cost. As of 2024, Southwest Airlines has about 800 aircraft in its fleet. For each year that we have data on the fleet we will have about 800 lines of Southwest Airlines information in our data. We will certainly want to ensure that we add to each line information about the company itself and its attitude towards safety and risk management, pilot training, and so on. One aspect which is of interest and which might tell us something about the fleet and its operations is the range or spread of certain aircraft features across all aircraft. An airline which has an old fleet will have all old aircraft. As it starts to renew the fleet, the range of ages will increase. If the fleet is completely renewed, all the aircraft will be relatively new. Hence we may wish to add features related to the range and spread of aircraft ages. We would probably add range, interquartile range, standard deviation, and then the same measures (range, interquartile range, etc.) but split by the different types of aircraft on the fleet. We might also apply the same approach used for aircraft age to the value of the aircraft (incorporating features such as range, interquartile range, and standard deviation). At the end of this process we will have created many features, and given that they measure very similar things, we will expect them to be correlated.

## 7.2. Why Do They Matter?

There are various reasons why having highly correlated features in our data (or our final model) might be problematic:

- computational issues
- performance
- interpretability and communication
- cost

### 7.2.1. Computational issues

All supervised models are trained by trying to minimize a loss function (or sometimes to maximize a likelihood). If the loss function is curved near a minimum, it will be easy to identify the model parameters which achieve this minimum. However, if two features are highly correlated, their effects in the model can be traded off against each other—small increases in one parameter can be offset by small decreases in the other, leading to very similar predictions. This makes the surface of the loss function nearly flat in certain directions near the minimum. As a result the minimum will be hard to find.

The extent to which the above issue is a problem depends on the model type being trained.

The procedures used to fit GLMs can be badly affected by this issue. A non-penalized GLM might simply return some kind of warning or error and not return any fitted model. If it does return a fitted model, the parameters may be unstable. For example, two highly correlated parameters on which the target does not depend should both return a coefficient of zero, but it is possible that one would return  $-50$  and the other  $50$ . In addition, the confidence intervals around the parameters will be large. Penalized regression should always return an answer, but it might take a very long time.

Tree-based models should not suffer from large offsetting coefficients. The reason for the difference between GLMs and tree-based models in this matter lies in the way they are trained. Procedures to fit GLMs often consider how best to change all the variables at once by small amounts in order to get closer to the minimum of the loss function. Where two features are correlated, they can get changed in opposite directions at the same time with no effect on the loss function.

Tree-based models, however, are fitted in a “greedy” manner. This means that only the contribution of one feature is changed at the time. The tree has to make a decision on which feature to introduce a split on next. If two highly correlated features do not separately have an impact on the loss function then it is exceedingly unlikely to choose to introduce a split on either of them. And if they both have an impact, then it will choose one or the other—not both.

### 7.2.2. Performance

Kuhn and Johnson (2019) (Chapter 10, Section 10.3) consider the effect of irrelevant features on performance. In their example, the performance of penalized regression (LASSO) is not affected by irrelevant features, but all other model types that they look at (tree-based models, neural networks, and others) are affected to a greater or lesser extent. Our case, however, is different. We don’t know whether the highly correlated features are irrelevant or not. We do know, however, that after including one of many highly correlated features, then the rest will be irrelevant. In the authors’ experience, performance of tree-based model types is certainly adversely affected, and we will see below whether for a particular dataset GLM performance is affected—though a priori we would not expect it to be, since if the training of a GLM converges at all, it should converge to the minimum of the loss function.

In the presence of highly correlated features, even if the performance of the trained model is good, it relies on the same high correlation continuing into the future. If the correlation between the features changes, then the accuracy of the model may be compromised, even if no other element of the “ground truth” has changed. As an example, consider a case where a credit score and its five (say) components are all included as features when training a model. Credit score is a weighted average of the features with the

most significant weight on feature 1. The true relationship is between feature 1 and the target, but the trained model finds and uses the relationship between the credit score itself and the target. If in the future, the team that creates the credit score significantly reduces the weighting for feature 1, credit score will not be a proxy for feature 1 and model performance will suffer.

There is another, potentially much more dangerous way in which the correlation between features can change. This arises where customers can shop for different prices and the correlation has caused a “reversal”—that is to say that the coefficient is of the opposite sign than expected. For example, in private auto insurance (or in fact any insurance) we expect that, as the deductible reduces the price will increase. However, if the policy excess is very highly correlated with some other feature (for example, vehicle value), the fitted GLM might set the slope of the coefficient for vehicle value to be steeper than expected and the coefficient for policy excess to be upward sloping so that lower excesses have lower prices instead of higher prices. If the rating plan is available to the public or it is otherwise possible for customers to get different quotes for different excesses, customers with high value cars will very quickly start selecting low excesses, and losses will be made.

### **7.2.3. *Interpretability and communication***

If we are lucky, we might find that in the presence of many highly correlated features our GLM converges to the minimum of the loss function in a reasonable amount of time and the parameters look sensible. Nevertheless, we may still not want many highly correlated features in our model.

Consider a simple case where we are asked which features are important in our GLM. As long as the features are all on a similar scale, we can normally just look at the absolute coefficients in the fitted model. Features with large absolute coefficients are more important than those with low coefficients (as long as they both affect similar proportions of customers). In the presence of highly correlated features, however, we have to be much more careful. If we have 10 highly correlated features, all measuring driver experience in slightly different ways, then each of the coefficients may be small, but their overall effect on the predictions may be very large. If the effect of experience on the target variable is nonlinear, then the only way to find the overall shape is to somehow add up the effects of all of the correlated features. These difficulties are not insurmountable, but they add complexity in trying to understand our model and will certainly make it much harder to communicate to the business of feature importance and the shape of the effects.

In some cases, the standard approaches in the software we use will not work in the presence of highly correlated features, for example, the detection of interactions. One method of doing this is to see how often two features appear in consecutive decisions or

along one decision path in trees. Consider driving experience and the power-weight ratio of the car. We might expect these to interact (i.e., inexperienced drivers in a car with a high power-weight ratio are a much worse risk than the individual coefficients would imply). In this case, when a tree is split on power-weight ratio, we would often expect the next split (or another in the same path) to be driving experience. Across all the trees, we might find that 100 times, a path which splits on power-weight ratio also splits on experience. Yet, if 10 correlated features are used to measure experience, we may only get 10 paths for each of them, and this might not stand out compared to other combinations of features.

### 7.2.4. Cost

There is a cost to having a feature in our final model. It has to be collected at runtime either from the proposer or from enrichment sources. It has to be stored. Likewise, a table of coefficients needs to be created and stored. It has to be added to a calculation. In future training, it becomes part of data quality audits and exploratory data analysis. It is much easier to monitor model performance and data drift for 10 features than for 100 features. Some costs may “just” be time costs, others may be actual expenditure or the risk of making errors. Either way, it seems that our aim should be, in the words of Kuhn and Johnson (2019),

*to reduce the number of features as far as possible without compromising predictive performance.*

## 7.3. Introducing a Case Study

We will illustrate some of the approaches we are about to discuss with the UK road traffic accident data mentioned in Section 2.2. To avoid issues with missing values, we use data for England only. In these data, England is split into about 34,000 areas (called Lower-layer Super Output Areas or LSOAs), each with around 1,000 households. In order to focus on local traffic, we exclude accidents on highways and similar types of roads. Figure 7.1 shows the number of accidents per quarter over the five-year period covered by the data. During 2018 and 2019 there were about 24,000 accidents per quarter. Data from 2020 and the first part of 2021 are heavily affected by the impact of COVID-19 on road traffic. The number of accidents per quarter after COVID-19 is about 10% lower than before COVID-19.

![Line graph showing the number of accidents on the police database for England over a five-year period from 2018-Q1 to 2022-Q4. The y-axis represents the number of accidents, ranging from 16,000 to 24,000. The x-axis shows quarters from 2018-Q1 to 2022-Q4. The graph shows a general upward trend from 2018 to 2019, followed by a sharp decline in 2020-Q1 and 2020-Q2, a recovery in 2020-Q3 and 2020-Q4, another sharp decline in 2021-Q1, and a subsequent recovery and stabilization through 2022-Q4.](9f5235ae671ed02fbc9a2203e9dc6df6_img.jpg)

| Quarter | Number of Accidents (approx.) |
|---------|-------------------------------|
| 2018-Q1 | 23,500                        |
| 2018-Q2 | 24,500                        |
| 2018-Q3 | 24,500                        |
| 2018-Q4 | 25,000                        |
| 2019-Q1 | 23,000                        |
| 2019-Q2 | 23,500                        |
| 2019-Q3 | 24,000                        |
| 2019-Q4 | 24,500                        |
| 2020-Q1 | 20,500                        |
| 2020-Q2 | 15,000                        |
| 2020-Q3 | 22,500                        |
| 2020-Q4 | 21,000                        |
| 2021-Q1 | 15,000                        |
| 2021-Q2 | 23,000                        |
| 2021-Q3 | 23,500                        |
| 2021-Q4 | 23,500                        |
| 2022-Q1 | 22,000                        |
| 2022-Q2 | 22,500                        |
| 2022-Q3 | 23,000                        |
| 2022-Q4 | 23,000                        |

Line graph showing the number of accidents on the police database for England over a five-year period from 2018-Q1 to 2022-Q4. The y-axis represents the number of accidents, ranging from 16,000 to 24,000. The x-axis shows quarters from 2018-Q1 to 2022-Q4. The graph shows a general upward trend from 2018 to 2019, followed by a sharp decline in 2020-Q1 and 2020-Q2, a recovery in 2020-Q3 and 2020-Q4, another sharp decline in 2021-Q1, and a subsequent recovery and stabilization through 2022-Q4.

**Figure 7.1. The number of accidents on the police database for England over the five-year period covered by the data. The data is affected by the impact of COVID-19 on road traffic.**

We added various indices of deprivation and information from the 2019 UK census to the above data. These will be our features.

Examples of indices of deprivation are:

- **crime\_rank:** Deprivation as measured by the risk of personal and material victimization. Low values indicate high levels of deprivation.
- **income\_rank:** Deprivation as measured by the proportion of the population experiencing deprivation related to low income. The definition of low income used includes both those people who are out-of-work and those who have work but have low earnings. Low values indicate high levels of deprivation.
- **employment\_rank:** Deprivation as measured by the proportion of the working-age population in an area involuntarily excluded from the labor market. This includes people who would like to work but are unable to do so due to unemployment, sickness or disability, or caregiving responsibilities. Low values indicate high levels of deprivation.

The Index of Multiple Deprivation (IMD) is also included as a feature. It is an overall relative measure of deprivation constructed by combining seven types of deprivation according to their respective weights. Unsurprisingly, it is highly correlated with some of

its constituent indices. For example, IMD and employment rank have a 0.91 (Pearson) correlation coefficient.

Census data measure various aspects for each household, such as:

- Legal partnership status
- Household composition
- Country of birth
- Age
- Distance traveled to work

Some of these aspects are measured both at a higher level and then broken down into detail. For example, the percentage of the population who are widowed or a surviving civil partnership partner is a feature. In addition, there are two further features: the percentage of the population who are widowed and the percentage of the population who are a surviving civil partnership partner. (This is very similar to how enrichment data will include many features that measure similar aspects of the risk.) This multiple measurement of very similar aspects of the population leads to highly correlated features.

In total, there are 70 features, of which 20 pairs (out of 2,415) have a 0.90 or greater (Pearson) correlation coefficient.

We define accident frequency as the number of accidents per 1,000 of census population. We should really define accident frequency as the number of accidents divided by the amount of traffic or the total distance traveled by cars on the roads. However, we have not added such information to our data. We therefore use population (of the LSOA) as a proxy.

We can see from the initial graphs that the accident frequency seems to vary with some of our features. For example, Figure 7.2 shows that accident frequency reduces for higher values (less deprivation) of crime rank.

Our aim is to build a model based on the available features and then to use it to predict the accident rate for areas not used in training the model. We will look at various methods of dealing with highly correlated variables and see if and how they impact our final model. As per usual, we will create a fold variable to be used for cross-validation during training and to exclude some data for testing. Given the time dimension of our data, there are one or two issues we need to think about when creating the fold variable, and these are discussed in Section 7.5.

![Line graph showing the relationship between crime aspect of deprivation and number of accidents per thousand of population. The x-axis is 'decile of crime rank' (1 to 10) and the y-axis is 'number of claims per thousand population' (0.90 to 1.10). The line shows a general downward trend from decile 1 to 7, followed by a slight increase at decile 8, a sharp drop at decile 9, and a rise at decile 10.](a6d1b7d9be84a290d618aee634d06d3d_img.jpg)

| decile of crime rank | number of claims per thousand population |
|----------------------|------------------------------------------|
| 1                    | 1.11                                     |
| 2                    | 1.02                                     |
| 3                    | 1.00                                     |
| 4                    | 0.97                                     |
| 5                    | 0.95                                     |
| 6                    | 0.94                                     |
| 7                    | 0.92                                     |
| 8                    | 0.93                                     |
| 9                    | 0.90                                     |
| 10                   | 0.92                                     |

Line graph showing the relationship between crime aspect of deprivation and number of accidents per thousand of population. The x-axis is 'decile of crime rank' (1 to 10) and the y-axis is 'number of claims per thousand population' (0.90 to 1.10). The line shows a general downward trend from decile 1 to 7, followed by a slight increase at decile 8, a sharp drop at decile 9, and a rise at decile 10.

**Figure 7.2. The relationship between crime aspect of deprivation (higher values means less deprived) and number of accidents per thousand of population.**

## 7.4. Dealing with Highly Correlated Variables

### 7.4.1. Common sense

The original census data contains counts of the population in each category being measured. We prefer percentages because they lie in the range 0–100 and because they are easier to understand. We created percentages by dividing the number in each category by the total population. Similarly, the raw deprivation indices actually rank all of the LSOAs and therefore run from 1 to 34,000 (with the LSOA with value 1 being the most deprived). We grouped the LSOAs into 100 groups according to the percentile of their deprivation index.

After the above data manipulation, our census data contained both counts and percentages, and our deprivation data contained the original ranks and our derived groups. Every feature therefore had a pair with which it was perfectly correlated (this is known as intrinsic aliasing). Common sense tells us to exclude such features. We therefore removed the counts and the original ranks.

More generally, if an initial check of our data shows a pair of features with correlations close to one, it may be obvious that one should be removed.

Common sense has its limits though. Consider another issue with our data. For any aspect measured by the census, the sum of percentages across all categories must sum to 100%. Any one column can therefore be derived as a linear combination of the others in the same category (i.e., 100% minus the sum of all the other columns). This is an example of multicollinearity, and in non-penalized regression, it can lead to the same issues as having highly correlated features. We could exclude one of the columns, but it is not clear a priori which column to exclude. We therefore now consider other approaches. Note that for tree-based models, removing the column that represents one category is not a good idea. If the tree needs to split on that category, it will not be able to, and while it can split on all the other categories, this will lead to a more complicated model.

### **7.4.2. *Removing some features before model training***

A simple approach to dealing with highly correlated features is to remove some of them before training. One way to do this (as implemented in the R package, *caret* Kuhn (2008)) is to find the two most highly correlated features and, of those two, to remove the feature that has the highest mean absolute correlation with all other features. This is repeated until none of the remaining correlations is above a certain cutoff. Using this approach on our data (with a cutoff of 0.90) removes three of the deprivation indices (including the overall IMD) and nine census features.

If this approach is used, the value of the cutoff needs to be chosen. One approach would be to go train models for various values of the cutoff and for each to find the average cross-validation performance. Starting from a model containing all features, as we exclude more correlated features by reducing the cutoff we would expect cross-validation performance initially to either improve or at least not to deteriorate. The cutoff can be set at the level below which performance starts to deteriorate.

### **7.4.3. *Ridge regression***

The constraints created by penalization allow Ridge regression to find a set of parameters which maximizes performance, even in the presence of highly correlated features (or multicollinearity).

![Two line graphs showing coefficients from a Ridge regression model. The top graph shows a negative linear relationship between Index of Multiple Deprivation rank and addition to linear predictor. The bottom graph shows a positive linear relationship between Employment Deprivation rank and addition to linear predictor.](80c366f70734d6478525700d647ba655_img.jpg)

The figure consists of two vertically stacked line graphs. Both graphs have a light gray grid background.

The top graph has a y-axis labeled 'addition to linear predictor' ranging from 0.0 to -0.5 in increments of 0.1. The x-axis is labeled 'Index of Multiple Deprivation rank' with major ticks at 0, 25, 50, 75, and 100. A solid black line starts at (0, 0.0) and slopes downward linearly to approximately (95, -0.5).

The bottom graph has a y-axis labeled 'addition to linear predictor' ranging from 0.0 to 0.5 in increments of 0.1. The x-axis is labeled 'Employment Deprivation rank' with major ticks at 0, 25, 50, 75, and 100. A solid black line starts at (0, 0.0) and slopes upward linearly to approximately (100, 0.05).

Two line graphs showing coefficients from a Ridge regression model. The top graph shows a negative linear relationship between Index of Multiple Deprivation rank and addition to linear predictor. The bottom graph shows a positive linear relationship between Employment Deprivation rank and addition to linear predictor.

**Figure 7.3. Coefficients from a Ridge regression model for IMD and Employment Deprivation Rank have different signs. This means that their contribution to the linear predictor cancels out to some extent. It can also be seen that the coefficient for Employment Deprivation is much smaller. Overall, although Ridge regression was successfully fit in the presence of highly correlated features, model interpretability suffers—the model would have been more easily understandable if Employment Deprivation Rank was excluded and the coefficient for IMD were slightly lower.**

In extreme cases, run times may become very long and certain solvers may fail. In our case, training was quick and returned a fitted model with no difficulties. All 66 features have nonzero coefficients. The cross-validation performance (pseudo- $R^2$ ) is 0.26. We will use this model's performance as our baseline as it is a simple model to fit and it is the first model that we have fit. We will soon see that this is a reasonable performance compared to other models. While performance is reasonable, model interpretability has suffered to some extent. Highly correlated features with nonzero coefficients are in the model. Sometimes their coefficients have different signs, which means that looking at only one of them does not give the full picture of how that feature affects the model. This point is illustrated in Figure 7.3—the coefficients for IMD and employment have opposite signs, and so their contributions to the linear predictor cancel out to some extent. In other cases, the coefficients of correlated feature have the same sign, but if only one was in the model, then its coefficients would be much larger and it would be more obvious that it was an important feature.

### 7.4.4. LASSO

In their paper “Regularization and Variable Selection Via the Elastic Net,” Zou and Hastie 2005 state that

*If there is a group of variables among which the pairwise correlations are very high, then the LASSO tends to select only one variable from the group and does not care which one is selected.*

While in the analysis they were writing about, this is actually not ideal (and hence they were motivated to introduce the elastic net); in our case, having LASSO's implicit feature selection choose only one of each group of correlated features in our data seems like a reasonable and useful outcome. We will end up with a model that still performs well, while being easier to understand. (An alternative—which might work better—is to construct a new feature from the correlated features. This is discussed in Section 7.4.5.)

Figure 7.4 shows the output of k-fold cross-validation. The number of features selected as the LASSO penalty increases is shown along the top of the figure. The dashed vertical line close to 59 selected features is at the maximum pseudo- $R^2$ . The dotted line at 31 features is a simpler model whose performance is within one standard deviation of the model with the best cross-validation performance. The performance of this model is a cross-validation pseudo- $R^2$  of 0.274, which is better than the Ridge regression model above. We would therefore choose this model over the Ridge regression model.

![Figure 7.4: stats19 elastic net. A plot showing average pseudo-R^2 versus log(lambda). The x-axis ranges from -7.5 to -2.5, with log(lambda) values. The y-axis ranges from 0.0 to 0.3. A red line with error bars shows the average pseudo-R^2, which is constant at approximately 0.3 for log(lambda) < -5.0 and then decreases sharply as log(lambda) increases. Two vertical dashed lines are present: one at log(lambda) ≈ -6.8 and another at log(lambda) ≈ -3.2. Above the plot, a sequence of numbers (66, 65, 64, 62, 59, 59, 54, 54, 45, 44, 42, 31, 24, 21, 17, 9, 30) is displayed, corresponding to the number of non-zero coefficients in the model for each value of lambda.](d0fa84472b5dd65e67bc406ceaaf3816_img.jpg)

Figure 7.4: stats19 elastic net. A plot showing average pseudo-R^2 versus log(lambda). The x-axis ranges from -7.5 to -2.5, with log(lambda) values. The y-axis ranges from 0.0 to 0.3. A red line with error bars shows the average pseudo-R^2, which is constant at approximately 0.3 for log(lambda) < -5.0 and then decreases sharply as log(lambda) increases. Two vertical dashed lines are present: one at log(lambda) ≈ -6.8 and another at log(lambda) ≈ -3.2. Above the plot, a sequence of numbers (66, 65, 64, 62, 59, 59, 54, 54, 45, 44, 42, 31, 24, 21, 17, 9, 30) is displayed, corresponding to the number of non-zero coefficients in the model for each value of lambda.

**Figure 7.4. stats19 elastic net.  $\alpha$ , the mixing parameter between Ridge regression ( $\alpha = 0$ ) and the LASSO ( $\alpha = 1$ ), is set to 0.99.**

We extracted the coefficients for all features that are 0.70 or more (absolute value) correlated with IMD rank. Table 7.1 shows the correlation of each feature<sup>51</sup> and also the coefficients from the Ridge regression and the LASSO models. It can be seen that the Ridge regression model is complicated—inasmuch as every coefficient is nonzero. In addition, some of the effects are in opposite directions. For example, the features `income_rank` and `as_rank` (adult skills subdomain which measures the lack of qualifications in the resident working-age adult population) are both positively correlated with IMD rank, yet their coefficients are of opposite signs. The LASSO model is simpler, with only four features being selected. It will be much easier to discuss and communicate this model to stakeholders. Nevertheless, it is far from perfect. The coefficients for the two last features in the table are both negative, yet their correlations are of opposite signs—which will mean that their overall contribution to the model mostly cancels out.

<sup>51</sup> Definitions are as follows: `imd_rank` (Index of Multiple Deprivation) is an overall average measure of deprivation. `income_rank` measures the proportion of the population experiencing deprivation relating to low income. `employment_rank` measures the proportion of the working-age population in an area involuntarily excluded from the labor market. `hd_rank` (Health Deprivation and Disability) measures the risk of premature death and the impairment of quality of life through poor physical or mental health. `as_rank` (Adult Skills) measures the lack of qualifications in the resident working-age adult population. `cayp_rank` (Children and Young People) measures the attainment of qualifications and associated measures. `crime_rank` measures the risk of personal and material victimization at local level. `c_ts063_occ_9_pct` measures the percent of residents aged 16 years and over in “elementary occupations” during the week before the census.

**Table 7.1. This table shows the Ridge regression and LASSO coefficients for all features whose (absolute) correlation with IMD rank is 0.70 or more. It can be seen that the Ridge regression model is complicated, with every feature having a coefficient and some of them going in opposite directions. The LASSO model is simpler, with only four features being selected, though even in this simpler model we see the effects going in opposite directions.**

| feature           | correlation | coef_ridge | coef_lasso |
|-------------------|-------------|------------|------------|
| imd_rank          | 1.00        | −0.0054    | −0.0011    |
| income_rank       | 0.95        | 0.0025     | 0.0000     |
| employment_rank   | 0.92        | 0.0004     | 0.0000     |
| hd_rank           | 0.84        | 0.0006     | 0.0000     |
| est_rank          | 0.82        | 0.0007     | 0.0000     |
| as_rank           | 0.78        | −0.0018    | 0.0000     |
| cayp_rank         | 0.76        | 0.0006     | 0.0002     |
| c_ts063_occ_9_pct | −0.74       | −0.0063    | −0.0014    |
| crime_rank        | 0.71        | −0.0012    | −0.0014    |

Overall, the LASSO provides a model with better performance than Ridge regression, and its implicit feature selection tends to select just one (or a small number) out of each group of correlated features. There are some potential practical difficulties though, and these are discussed in Section 7.5.3 below.

Before we move on, we use this opportunity to discuss coefficient paths—the values that each coefficient takes as the penalty increases. In an insurance rating context, two high correlated features can each have a positive impact (say) on risk. When fitted separately in a GLM, each will have a positive coefficient. When both features are entered into the same GLM, though, it is possible that one will have a large positive coefficient and the other will have a negative coefficient. This is known as a reversal. If either of these two features are self-declared by the policyholder, or chosen at the time the policy is taken out, then this reversal is almost guaranteed to cause adverse selection. An example is if the correlation between car value and deductible leads to lower deductibles having higher discounts. Policyholders will obviously choose higher discounts. In this particular case, it might be possible to exclude the deductible from the model, model claims gross of the deductible, and then manually calculate the deductible scale. Such manual intervention is not always possible. The LASSO can sometimes help, i.e., it is possible—but not guaranteed—that as penalization increases, the LASSO will deal with reversals for us. Figure 7.5 shows the full coefficient paths for the highly correlated features shown above in Table 7.1.

![Figure 7.5: Coefficient paths for some highly correlated features. The plot shows the coefficient value (y-axis, ranging from -0.008 to 0.004) versus the log of the lambda parameter (x-axis, ranging from -7.5 to -2.5). A vertical dashed line at log(lambda) ≈ -3.5 marks the 1 s.e. model. Nine lines represent different features: as_rank (red), cayp_rank (yellow), employment_rank (green), hd_rank (blue), income_rank (pink), c_ts063_occ_9_pct (orange), crime_rank (dark green), est_rank (cyan), and imd_rank (purple). The lines show how coefficients change as lambda decreases (moving from left to right). At high lambda (left), coefficients are large and many lines show reversals (changes in sign). As lambda decreases towards the 1 s.e. model, the coefficients generally shrink towards zero, and many reversals are resolved.](222504639ead694ed82f40a26573e6c3_img.jpg)

Figure 7.5: Coefficient paths for some highly correlated features. The plot shows the coefficient value (y-axis, ranging from -0.008 to 0.004) versus the log of the lambda parameter (x-axis, ranging from -7.5 to -2.5). A vertical dashed line at log(lambda) ≈ -3.5 marks the 1 s.e. model. Nine lines represent different features: as\_rank (red), cayp\_rank (yellow), employment\_rank (green), hd\_rank (blue), income\_rank (pink), c\_ts063\_occ\_9\_pct (orange), crime\_rank (dark green), est\_rank (cyan), and imd\_rank (purple). The lines show how coefficients change as lambda decreases (moving from left to right). At high lambda (left), coefficients are large and many lines show reversals (changes in sign). As lambda decreases towards the 1 s.e. model, the coefficients generally shrink towards zero, and many reversals are resolved.

**Figure 7.5. Coefficient paths for some highly correlated features. Models with small amounts of penalization show reversals and high coefficients. At the 1 s.e. model, most of the reversals have been dealt with and the coefficients are much smaller.**

It can be seen that among models with little penalization (far left), the coefficients were very large, and there were many reversals (given that these features are all picking up the same effect, the coefficients should all have the same sign<sup>52</sup>).

### 7.4.5. Principal component analysis

In Table 7.1 we saw that the LASSO selected four out of nine highly correlated features. All of these features involve deprivation. The only feature in this list that is not directly related to deprivation is `c_ts063_occ_9_pct`. This feature is the percentage of households in an area where employment is in an “elementary occupation”. A high percentage here may also signify a highly deprived area. The features that have been selected are therefore really a proxy for any measure of deprivation. In communicating this, we cannot really say that the main effect being measured is crime or elementary occupations. It might therefore be easier to replace all of these features with one feature representing deprivation and to have just one coefficient for this replacement feature.

<sup>52</sup> One feature, `c_ts063_occ_9_pct`, had a negative correlation with the others, but we have multiplied its coefficient by  $-1$ .

Principal component analysis (PCA<sup>53</sup>) potentially allows us to do this. It replaces our original features with a new set of features which are not correlated with each other. The new features are linear combinations of the old features. If we are lucky, inspection of the weights of these new features might allow us to describe them in some general and useful way.

The largest loadings of the first principal component from a PCA on our data are as follows:

$$\begin{aligned} \text{pca}_1 = & 0.0275 * \text{imd\_rank} \\ & + 0.0274 * \text{income\_rank} \\ & \dots \\ & - 0.0307 * \text{c\_ts063\_occ\_9\_pct} \end{aligned}$$

The imd\_rank and income\_rank are indices of deprivation with higher scores meaning less deprived. The positive loadings above mean that high values of the first principal component mean that households in LSOA do not suffer from deprivation. c\_ts063\_occ\_9\_pct is the percent of households in the LSOA where employment is in “elementary” occupations. Given the negative loading, higher values of this feature will be associated with low values for this component. Overall, then, this component is very much related to deprivation, with higher values relating to less deprivation.

The second feature (loadings not shown here) is harder to understand. Large positive loadings are given to the features professional occupations and working from home. Large negative loadings are given to the features country of birth in Europe and skilled trades occupations. Further features are also not that easy to understand. Therefore, in our particular case, the PCA components may not help that much with interpretability.

Regarding performance, we note that in GLMs, the linear predictor is a linear combination of features. Therefore, with appropriate coefficients a GLM using PCA based components (which are themselves linear in the original features) can give exactly the same predictions as any GLM based on the original features. In addition, a small number of principal components represent (in a mathematical sense) much of the information conveyed by our features (as measured by variance). In our case, the first two components represent almost 90% of the variance of our data. We can therefore hope that our PCA based model will have the same or similar performance as our original model but with less features.

---

<sup>53</sup> PCA is a dimensionality-reduction technique that transforms correlated variables into a smaller set of uncorrelated variables called principal components, which capture the most variance in the data. We assume that the reader is familiar with it.

In our case study, performance using only a small number of the principal components is not good. We trained a model using enough components (the first 17) to capture 99% of the variance of the data. Pseudo- $R^2$  was only 0.13 - this is much worse than previous models. The reason for this (as discussed in Maitra and Yan (2008)) is that PCA is unsupervised - it does not look at the target variable when creating components. There might be a component that is quite minor as measured by the amount variance in the original data that it accounts for, but is very important in predicting accident frequency. That is exactly the case for us. In the LASSO fitted on all the principal components, the largest coefficient is for component 54, despite accounting for less than 0.001 % of the variance in the original data. This situation still seems surprising and is further discussed in Section 7.5.4.

PCA has not led to a simpler or more easily interpretable model. In addition, since each component is made up by loadings on every original feature, a model based on PCA requires all of the features and so is actually harder to implement operationally than the simple LASSO model which did not require all of them. Operational issues are not always a consideration, though. We might be interested in ranking areas in terms of accident risk as part of a broader geographical risk analysis. As in the case of our FAA-NSTB study, we might implement our findings by assigning each zip code to a group and so how we arrived at these groups does not need to be operationalized. In these cases, the fact the PCA requires all of the original features is not a disadvantage, and as long as it provides other advantages (such as making the models easier to fit) we should use it.

Before the LASSO was easily available, PCA would have been (and still is) one way to get a non-penalized linear model to converge and to have sensible confidence intervals for parameter estimates. Overall, as we have seen PCA has advantages (e.g., dimension reduction, interpretability of components, non-correlated features, and so quicker run times, convergence of non-penalized GLMs) and possible disadvantages (e.g., it is not supervised so early components may not be predictive, use of all original features is necessary). Whether or not PCA is overall beneficial will depend on the particular analysis and more generally on the domain (e.g., insurance, genomics, chemical engineering, etc.).

Other than PCA, any other dimension reduction technique can also be used to try to deal with highly correlated features. Two examples are Independent Component Analysis (ICA) and autoencoders. ICA transforms the features to be independent. Unlike PCA there is no focus on trying to represent as much as possible of the variation of the original data in the first few features. We carried out ICA followed by the LASSO on our data. Performance was the same as for the LASSO and the components were of interest. Autoencoders use neural networks to create low-dimensional (nonlinear) representations of our data, and they are not discussed further here.

The above dimension reduction techniques are all unsupervised, and, as discussed, there is no guarantee that the components extracted will be important in terms of predictive power. Partial Least Squares (PLS, see An Introduction to Statistical Learning James et al. (2021), Section 6.3) is a supervised method that creates components in such a way that they are important for prediction. It was specifically created for situations like ours, where many of the features are highly correlated. PLS has been extended to work in the GLM setting and is called, unsurprisingly, PLS-GLM.<sup>54</sup> To ensure sparsity, the PLS-GLM components can be extracted and then used as input to the LASSO. In our case, the LASSO selects the first 10 PLS-GLM components and performance is reasonable. The components themselves are also fairly interesting. We don't discuss PLS-GLM further in this note, but it certainly seems useful, especially for gaining insight into the underlying features that are driving performance of the model.

Cluster analysis is often discussed alongside dimension reduction – because they are both examples of unsupervised learning. However, in our context, it does not seem particularly useful. We could create clusters of similar areas based on their features. This might be of interest from a data exploration perspective - but this would not necessarily lead to useful features to use in a regression.<sup>55</sup>

## 7.5. Practically Speaking

### 7.5.1. *Fold variable in time series data*

An observation for each LSOA is present for every quarter from 2018 to 2022. Consider the case where, within each LSOA, observed accident frequency is fairly stable over time. If we choose our fold variable for each line in our dataset at random, then the same LSOA will be in different folds. If we then see good cross-validation performance, we will not be sure if some of the performance is the result of the model having seen the LSOAs in the validation dataset during training. We therefore allocated all the observations for each LSOA into one (randomly selected) fold. In private auto insurance, the same policy number can be present in the dataset many times. For example, in any one policy year, each time there is a midterm adjustment to the policy (for example, a change of address) a new line of data may be generated. And the same policy number may be present over multiple years if the policy renews. For the same reason as discussed in our case study, it seems sensible to allocate all observations for any one policy to a (random) fold.

---

<sup>54</sup> At the time of writing This is available as a the `plsRglm` package in R, see Bertrand and Meyer (2018).

<sup>55</sup> Incidentally the distance that each observation is from the cluster centroid can be useful, for example in fraud modeling. In some domains, it can be the case that customers or transactions who are unusual in some way are more likely to be fraudulent. Isolation forests are an easy machine learning technique to find such customers or transactions.

### 7.5.2. *Hinges and splines with correlated features*

The astute reader may have noticed that the graphs and tables of coefficients in this chapter were only for the original features. No hinges or splines were added. In the authors' experience, it is often the case that the contribution to predicted accident frequency of this type of data is not a linear relationship. One possibility is that across much of the range of a feature there is no effect and only at the extreme values is there an increase in risk. Our reason for excluding splines here was purely for simplicity of exposition. If splines are included at the start of the analysis before highly correlated features are excluded, then things get a little more complicated. This is because it is possible that feature selection will select one of the original features for the main effect and the spline of one of the other features to capture some of the nonlinear shape of the effect. Adding this element to the case study was not needed to illustrate the main points in this chapter.

### 7.5.3. *LASSO in the presence of highly correlated features*

A difficulty encountered in this case study was that, in the presence of highly correlated features, the LASSO implemented in one software often failed to converge and the run times were very long.<sup>56</sup> Part of the solution to this was to use the elastic net with high values ( $\alpha = 0.95$ ). Proprietary software with custom solvers can perform more consistently. In either case, it does seem reasonable to use common sense first and remove the most highly correlated features.

### 7.5.4. *High coefficients in later principal components*

Despite principal component analysis (PCA) being unsupervised and, therefore, us not being totally surprised that a later component might be predictive, the extent in our study is unusual. Investigation showed that we had made a basic error in our features. We had originally noticed that one of the deprivation indices (living environment) is based partly on air quality and partly on the accident rate itself. We therefore only included the air quality feature. We excluded the living environment and accident rates features as it is clearly an error—and the ultimate in leakage—to include a feature derived from accidents to predict the accident rate. However, we did still include the overall IMD.

---

<sup>56</sup> The ability of the model to converge at all, regardless of runtime, also depended on the hardware on which it was run

Principal component 54 has the following main loadings:

$$\begin{aligned} \text{pca}_{54} = & + 0.274 * \text{imd\_rank} \\ & - 0.109 * \text{income\_rank} \\ & - 0.055 * \text{bhs\_rank} \\ & - 0.054 * \text{hd\_rank} \\ & - 0.053 * \text{employment\_rank} \\ & - 0.038 * \text{crime\_rank} \end{aligned}$$

We can see that this feature “reverse engineers” the living environment feature by deducting the other deprivation indices from the overall index. Hence, one feature in our model is based partly on accident frequency itself, which, of course, is simply wrong. The way to proceed at this stage would be to remove the overall IMD and to repeat the whole analysis. (The authors leave this to the interested reader.)

Therefore, while PCA has not been very helpful to us in terms of interpretability or sparsity of our model, it has provided us with an interesting way to check the quality of our data preparation. It seems reasonable that whenever regression is carried out on principle components and large coefficients are fitted to the later components, an investigation should be carried out to understand why and to ensure there are no data preparation issues.

