---
paper: goldburd_et_al
chapter: 7
title: "7. Model Validation and Selection"
topics: [model_lift, gini_index, quantile_plots, double_lift_charts, roc_curves, model_selection, logistic_regression_validation]
key_formulas: [gini_index_lorenz_curve, auroc_gini_relationship]
---
> **TL;DR**
> - Model validation must always use holdout data; scoring only requires predictions, not model internals — enables comparison with external/proprietary models
> - Quantile plots: sort by predicted, bucket into deciles; good model shows accuracy, monotonicity, and large first-to-last spread in actual loss costs
> - Double lift chart: sort by ratio (Model A / Model B predictions); model tracking actual more closely in each decile wins
> - Gini index = 2 × area between Lorenz curve and line of equality; measures risk segmentation ability
> - AUROC = 0.5 × normalized Gini + 0.5; ROC curves plot true positive rate vs. false positive rate as discrimination threshold varies

# 7. Model Validation and Selection

Before diving into this section, some explanation is in order. As described above, the process of model refinement is really a process of creating two candidate models and comparing them. To put it another way, all model refinement involves model selection. But sometimes model selection can be used for goals other than model refinement. Sometimes a decision needs to be made between a number of alternate final models. If the best efforts of two modelers working independently are not identical (and they will never be), how is one to choose between them? The techniques discussed below are suitable for making this decision, while the techniques discussed in Chapter 6 are not. There are two key reasons for this:

First, one or more of the alternate models may be proprietary. Any rating plan is a model, and rating plans can come from all sorts of places: subsidiaries, consultants, competitor filings, rating bureaus, and so on. Most of the time, the data used to build these rating plans will not be available and neither will the detailed form of the underlying model. Even if this information is available, it might be impractical to evaluate it—the rating plan need not have been created using a GLM! The techniques discussed in Chapter 6 cannot be used under these circumstances, but the techniques below can. In order for the techniques below to be used, one only needs a database of historical observations augmented with the predictions from each of the competing models. The process of assigning predictions to individual records is called **scoring**.

Second, while the model refinement process is entirely technical, choosing between two final models is very often a business decision. Those responsible for making the final decision may know nothing about predictive modeling or even nothing about actuarial science. The techniques below compare the performance of competing models in a way that is accessible.

Some of the techniques below can also be used for model refinement, to the extent that they produce new data or insights that can be acted on.

## 7.1. Assessing Fit with Plots of Actual vs. Predicted

A very simple and easily understandable diagnostic to assess and compare the performance of competing models is to create a plot of the actual target variable (on the  $y$ -axis) versus the predicted target variable (on the  $x$ -axis) for each model. If a model fits well, then the actual and predicted target variables should follow each other closely.

Consider Figure 21, which shows plots of actual vs. predicted target variables for two competing models.

**Figure 21.** Actual vs. Predicted Plots for Two Competing Models

![Figure 21: Two side-by-side scatter plots comparing Actual vs. Predicted values for Model 1 and Model 2. Both plots use a log scale for both axes, ranging from 5 to 100 ($000). A diagonal line represents perfect agreement. Model 1 shows a wider scatter of data points around the diagonal line, while Model 2 shows points much more tightly clustered along the diagonal line, indicating a better fit.](f3d96eb3ce2f7940025d304ba65c1d68_img.jpg)

Figure 21: Two side-by-side scatter plots comparing Actual vs. Predicted values for Model 1 and Model 2. Both plots use a log scale for both axes, ranging from 5 to 100 (\$000). A diagonal line represents perfect agreement. Model 1 shows a wider scatter of data points around the diagonal line, while Model 2 shows points much more tightly clustered along the diagonal line, indicating a better fit.

From these charts, it is clear that Model 2 fits the data better than Model 1, as there is a much closer agreement between the actual and predicted target variables for Model 2 than there is for Model 1.

There are three important cautions regarding plots of actual versus predicted target.

First, it is important to create these plots on holdout data. If created on training data, these plots may look fantastic due to overfitting, and may lead to the selection of a model with little predictive power on unseen data.

Second, it is often necessary to aggregate the data before plotting, due to the size of the dataset. A common approach is to group the data into percentiles. The dataset is first sorted based on the predicted target variable, then it is grouped into 100 buckets such that each bucket has the same aggregate model weight. Finally, the averages of the actual and predicted targets within each bucket are calculated and plotted, with the actual values on the  $y$ -axis and the predicted values on the  $x$ -axis.

Third, it is often necessary to plot the graph on a log scale, as was done in Figure 20. Without this transformation, the plots would not look meaningful, since a few very large values would skew the picture.

## 7.2. Measuring Lift

Broadly speaking, model lift is the economic value of a model. The phrase “economic value” doesn’t necessarily mean the profit that an insurer can expect to earn as a result of implementing a model, but rather it refers to a model’s ability to prevent adverse selection. The lift measures described below attempt to visually demonstrate or quantify a model’s ability to charge each insured an actuarially fair rate, thereby minimizing the potential for adverse selection.

Model lift is a relative concept, so it requires two or more competing models. That is, it doesn’t generally make sense to talk about the lift of a specific model, but rather the lift of one model over another.

In order to prevent overfitting, model lift should always be measured on holdout data.

### 7.2.1. Simple Quantile Plots

Quantile plots are a straightforward visual representation of a model's ability to accurately differentiate between the best and the worst risks. Assume there are two models, Model A and Model B, both of which produce an estimate of the expected loss cost for each policyholder. Simple quantile plots are created via the following steps:

1. Sort the dataset based on the Model A predicted loss cost (from smallest to largest).
2. Bucket the data into quantiles, such that each quantile has the same volume of exposures. Common choices are quintiles (5 buckets), deciles (10 buckets), or vigintiles (20 buckets).
3. Within each bucket, calculate the average predicted pure premium (predicted loss per unit of exposure) based on the Model A predicted loss cost, and calculate the average actual pure premium.
4. Plot, for each quantile, the actual pure premium and the pure premium predicted by Model A.
5. Repeat steps 1 through 4 using the Model B predicted loss costs. There are now two quantile plots—one for Model A and one for Model B.
6. Compare the two quantile plots to determine which model provides better lift.

In order to determine the “winning” model, consider the following 3 criteria:

1. **Predictive accuracy.** How well each model is able to predict the actual pure premium in each quantile.
2. **Monotonicity.** By definition, the predicted pure premium will monotonically increase as the quantile increases, but the actual pure premium should also increase (though small reversals are okay).
3. **Vertical distance between the first and last quantiles.** The first quantile contains the risks that the model believes will have the best experience, and the last quantile contains the risks that the model believes will have the worst experience. A large difference (also called “lift”) between the actual pure premium in the quantiles with the smallest and largest predicted loss costs indicates that the model is able to maximally distinguish the best and worst risks.

Figure 22 shows simple decile plots for an example comparison between the current rating plan (left panel) and a newly-constructed plan (right panel). For ease of interpretation, both the actual and predicted loss costs for each graph have been divided by the average model predicted loss cost.

In both plots, the solid line is the predicted loss cost (either by the current rating plan or by the new model) and the broken line is the actual loss cost. Which model is better?

1. *Predictive accuracy*—for the right panel graph, the plotted loss costs correspond more closely between the two lines than for the left panel graph, indicating that the new model seems to predict actual loss costs better than the current rating plan does.
2. *Monotonicity*—the current plan has a reversal in the 6th decile, whereas the model has no significant reversals.

**Figure 22.** Simple Decile Plots for Both the Current Rating Plan (*left panel*) and for a Newly-Constructed Plan (*right panel*)

![Figure 22: Simple Decile Plots for Both the Current Rating Plan (left panel) and for a Newly-Constructed Plan (right panel).](d9390ad6cde8bd9e9ed97b84dabf08bc_img.jpg)

Figure 22 consists of two side-by-side line graphs, each showing loss costs across 10 deciles. Both graphs have a y-axis labeled from 0.0 to 1.6 in increments of 0.4 and an x-axis labeled 'Decile' from 1 to 10. The left graph is titled 'Sorted by Loss Costs Underlying Current Rates' and compares 'Actual' (open triangles) and 'Current plan prediction' (solid circles). The right graph is titled 'Sorted by Model Predicted Loss Cost' and compares 'Actual' (open triangles) and 'Model prediction' (solid circles). In both graphs, the 'Actual' data points are generally higher than the predicted values, with the gap widening in the higher deciles.

| Decile | Actual | Current plan prediction |
|--------|--------|-------------------------|
| 1      | 0.55   | 0.55                    |
| 2      | 0.60   | 0.60                    |
| 3      | 0.65   | 0.65                    |
| 4      | 0.70   | 0.70                    |
| 5      | 0.80   | 0.80                    |
| 6      | 0.90   | 0.90                    |
| 7      | 1.00   | 1.00                    |
| 8      | 1.10   | 1.10                    |
| 9      | 1.20   | 1.20                    |
| 10     | 1.30   | 1.20                    |

| Decile | Actual | Model prediction |
|--------|--------|------------------|
| 1      | 0.40   | 0.40             |
| 2      | 0.50   | 0.50             |
| 3      | 0.60   | 0.60             |
| 4      | 0.70   | 0.70             |
| 5      | 0.80   | 0.80             |
| 6      | 0.90   | 0.90             |
| 7      | 1.00   | 1.00             |
| 8      | 1.10   | 1.10             |
| 9      | 1.20   | 1.20             |
| 10     | 1.30   | 1.60             |

Figure 22: Simple Decile Plots for Both the Current Rating Plan (left panel) and for a Newly-Constructed Plan (right panel).

3. *Vertical distance between the first and last quantiles*—the spread of actual loss costs for the current manual is 0.55 to 1.30, which is not very much. That is, the best risks have loss costs that are 45% below the average, and the worst risks are only 30% worse than average. The spread of the proposed model though is 0.40 to 1.60.

Thus, by all three metrics, the new plan outperforms the current one.

### 7.2.2. Double Lift Charts

A double lift chart is similar to the simple quantile plot, but it directly compares two models. Assume that there are two models, Model A and Model B, both of which produce an estimate of the expected loss cost for each policyholder. A double lift chart is created via the following steps:

1. For each record, calculate Sort Ratio = (Model A Predicted Loss Cost)/(Model B Predicted Loss Cost).
2. Sort the dataset based on the Sort Ratio, from smallest to largest.
3. Bucket the data into quantiles, such as quintiles or deciles.
4. Within each bucket, calculate the Model A average predicted pure premium, the Model B average predicted pure premium, and the actual average pure premium. For each of those quantities, divide the quantile average by the overall average.
5. For each quantile, plot the three quantities calculated in the step above.

In a simple quantile plot, the first quantile contains those risks which Model A thinks are best. In a double lift chart, the first quantile contains those risks which Model A thinks are best *relative to Model B*. In other words, the first and last quantiles contain those risks on which Models A and B disagree the most (in percentage terms).

In a double lift chart, the “winning” model is the one that more closely matches the actual pure premium in each quantile. To illustrate this, consider the example double

**Figure 23.** A Sample Double Lift Chart![A Double Lift Chart comparing three lines: Current plan prediction (thick broken line with squares), Model prediction (solid line with circles), and Actual loss cost (dotted line with triangles) across 10 deciles. The y-axis is Relative Loss Cost (0.0 to 2.5) and the x-axis is Decile of ratio: model prediction / current plan prediction (1 to 10).](1c3364622e6fab72c74fd34bf51dffb3_img.jpg)

**Double Lift Chart**

| Decile | Current plan prediction | Model prediction | Actual loss cost |
|--------|-------------------------|------------------|------------------|
| 1      | 1.1                     | 0.6              | 0.6              |
| 2      | 0.9                     | 0.5              | 0.5              |
| 3      | 0.9                     | 0.6              | 0.6              |
| 4      | 1.1                     | 0.9              | 0.9              |
| 5      | 0.9                     | 0.9              | 1.0              |
| 6      | 1.0                     | 1.0              | 1.0              |
| 7      | 0.9                     | 0.8              | 0.8              |
| 8      | 1.1                     | 1.4              | 1.4              |
| 9      | 0.9                     | 1.4              | 1.4              |
| 10     | 1.0                     | 1.8              | 2.1              |

A Double Lift Chart comparing three lines: Current plan prediction (thick broken line with squares), Model prediction (solid line with circles), and Actual loss cost (dotted line with triangles) across 10 deciles. The y-axis is Relative Loss Cost (0.0 to 2.5) and the x-axis is Decile of ratio: model prediction / current plan prediction (1 to 10).

lift chart in Figure 23, in which we use a double lift chart to compare a proposed rating model to the current rating plan.

The solid line shows the loss costs predicted by the model, the thick broken line shows the loss costs in the current rating plan, and the dotted line shows the actual loss costs. The sort order for this graph is the model prediction divided by the current plan prediction, and the data is segmented into deciles.

It is clear that the proposed model more accurately predicts actual pure premium by decile than does the current rating plan. Specifically, consider the first decile. It contains the risks that the model thinks are best relative to the current plan. As it turns out, the model is correct. Similarly, in the 10th decile, the model more accurately predicts pure premium than does the current plan.

As an alternate representation of a double lift chart, one can plot two curves—the percent error for the model predictions and the percent error for the current loss costs, where percent error is calculated as  $(\text{Predicted Loss Cost})/(\text{Actual Loss Cost}) - 1$ . In this case, the winning model is the one with the flatter line centered at  $y = 0$ , indicating that its predictions more closely match actual pure premium.

### 7.2.3. Loss Ratio Charts

In a loss ratio chart, rather than plotting the pure premium for each bucket, the loss ratio is instead plotted. The steps for creating a loss ratio chart are very similar to those for creating a simple quantile plot:

1. Sort the data based on the predicted loss ratio ( $= [\text{predicted loss cost}]/\text{premium}$ ).
2. Bucket the data into quantiles, such that each quantile has the same volume of exposures.
3. Within each bucket, calculate the *actual loss ratio* for risks within that bucket.

Ideally, the model is able to identify deficiencies in the current rating program by segmenting the risks based on loss ratio. To illustrate this, consider Figure 24. If a

**Figure 24.** A Sample Loss Ratio Chart![A bar chart titled 'Loss Ratio Chart' showing the loss ratio for each of the 10 deciles. The y-axis is labeled 'Loss Ratio' and ranges from 0% to 80% in 10% increments. The x-axis is labeled 'Decile' and ranges from 1 to 10. The bars show an increasing trend in loss ratio as the decile number increases.](34cfb1835fdf0d248bc2c4d58956a896_img.jpg)

**Loss Ratio Chart**

| Decile | Loss Ratio (%) |
|--------|----------------|
| 1      | 32             |
| 2      | 43             |
| 3      | 45             |
| 4      | 48             |
| 5      | 50             |
| 6      | 51             |
| 7      | 52             |
| 8      | 58             |
| 9      | 62             |
| 10     | 70             |

A bar chart titled 'Loss Ratio Chart' showing the loss ratio for each of the 10 deciles. The y-axis is labeled 'Loss Ratio' and ranges from 0% to 80% in 10% increments. The x-axis is labeled 'Decile' and ranges from 1 to 10. The bars show an increasing trend in loss ratio as the decile number increases.

rating plan is perfect, then all risks should have the same loss ratio. The fact that this model is able to segment the data into lower and higher loss ratio buckets is a strong indicator that it is outperforming the current rating plan.

The advantage of loss ratio charts over quantile plots and double lift charts is that they are simple to understand and explain. Loss ratios are the most commonly-used metric in determining insurance profitability, so all stakeholders should be able to understand these plots.

### 7.2.4. The Gini Index

The Gini index, named for statistician and sociologist Corrado Gini, is commonly used in economics to quantify national income inequality.

The national income inequality Gini index is calculated as follows:

1. Sort the population based on earnings, from those with the lowest earnings to those with the highest earnings. (This could also be done based on wealth rather than earnings.)
2. The  $x$ -axis is the cumulative percentage of earners.
3. The  $y$ -axis is the cumulative percentage of earnings.

The locus of points created by plotting the cumulative percentage of earnings against the cumulative percentage of earners is called the **Lorenz curve**. The left panel of Figure 25 plots the Lorenz curve for year 2014 household income in the United States.<sup>16</sup>

The 45-degree line is called the line of equality, so named because, if every person earned the same exact income, then the Lorenz curve would be the line of equality. In that hypothetical scenario, if there are 100 people in the society, then each represents 1% of the population and would earn 1% of the income. Everyone doesn't earn the same income, though, so the Lorenz curve is bow-shaped. As the graph shows, the

<sup>16</sup> Source: <https://www.census.gov/hhes/www/income/data/historical/household/>

**Figure 25.** Gini Index Plots of United States 2014 Household Income (*left panel*) and a Sample Pure Premium Model (*right panel*)

![Figure 25: Two side-by-side Gini Index plots. The left panel shows the Lorenz curve for United States 2014 Household Income, with the x-axis labeled 'Percentage of households' and the y-axis 'Percentage of income'. A dashed line represents the line of equality. A point on the curve at 60% on the x-axis corresponds to 25% on the y-axis. The x-axis is divided into 'lower income' (0-60%) and 'higher income' (60-100%). The right panel shows the Lorenz curve for a Sample Pure Premium Model, with the x-axis labeled 'Percentage of exposures' and the y-axis 'Percentage of losses'. A dashed line represents the line of equality. A point on the curve at 60% on the x-axis corresponds to 20% on the y-axis. The x-axis is divided into 'good risks' (0-60%) and 'bad risks' (60-100%).](8b2fede7511dc55ca8474f946371bb6b_img.jpg)

Figure 25: Two side-by-side Gini Index plots. The left panel shows the Lorenz curve for United States 2014 Household Income, with the x-axis labeled 'Percentage of households' and the y-axis 'Percentage of income'. A dashed line represents the line of equality. A point on the curve at 60% on the x-axis corresponds to 25% on the y-axis. The x-axis is divided into 'lower income' (0-60%) and 'higher income' (60-100%). The right panel shows the Lorenz curve for a Sample Pure Premium Model, with the x-axis labeled 'Percentage of exposures' and the y-axis 'Percentage of losses'. A dashed line represents the line of equality. A point on the curve at 60% on the x-axis corresponds to 20% on the y-axis. The x-axis is divided into 'good risks' (0-60%) and 'bad risks' (60-100%).

poorest 60% of households earn roughly 25% of the total income. The Gini index is calculated as twice the area between the Lorenz curve and the line of equality. (In 2014, that number was 48.0%).

The Gini index can also be used to measure the lift of an insurance rating plan by quantifying its ability to segment the population into the best and worst risks. The Gini index for a model which creates a rating plan is calculated as follows:

1. Sort the dataset based on the model predicted loss cost. The records at the top of the dataset are then the risks which the model believes are best, and the records at the bottom of the dataset are the risks which the model believes are worst.
2. On the  $x$ -axis, plot the cumulative percentage of exposures.
3. On the  $y$ -axis, plot the cumulative percentage of losses.

The locus of points is the Lorenz curve, and the Gini index is twice the area between the Lorenz curve and the line of equality.

The right panel of Figure 25 plots a sample Lorenz curve for a sample pure premium model. As can be seen, this model identified 60% of exposures which contribute only 20% of the total losses. Its Gini index is 56.1%.

Note that a Gini index does not quantify the profitability of a particular rating plan, but it does quantify the ability of the rating plan to differentiate the best and worst risks. Assuming that an insurer has pricing and/or underwriting flexibility, this will lead to increased profitability.

## 7.3. Validation of Logistic Regression Models

For logistic regression models (discussed in Section 2.8), the GLM yields a prediction of the probability of the occurrence of the modeled event. Many of the model validation diagnostics discussed in the previous sections can be applied to such models as well. For example, a quantile plot can be created by bucketing records of the

holdout set into quantiles of predicted probability and graphing the actual proportion of positive occurrences of the event within each quantile against the average predicted probability; a good model will yield a graph exhibiting the properties of accuracy, monotonicity and vertical distance between first and last quantiles, as described in Section 7.2.1. Similarly, a Lorenz curve can be created by sorting the records by predicted probability and graphing cumulative risks against cumulative occurrences of the event, and a Gini index can be computed from the resulting graph by taking the area between the curve and the line of equality.

For such models, a diagnostic called the *receiver operating characteristic* curve, or *ROC* curve, is commonly used due its direct relation to how such models are often used in practice, as discussed in the following section.

### 7.3.1. Receiver Operating Characteristic (ROC) Curves

While a logistic model predicts the *probability* of an event's occurrence, for many practical applications that probability will need to be translated into a binary prediction of occurrence vs. non-occurrence for the purpose of deciding whether to take a specific action in response. For example, suppose we build a model to detect claims fraud; for each new claim, the model yields a probability that it contains fraud. Based on this prediction, we will need to decide whether or not to assign a team to further investigate the claim.

We can make such a determination by choosing a specific probability level, called the *discrimination threshold*—say, 50%—above which we will investigate the claim and below which we will not. This determination may be thought of as the model's "prediction" in a binary (i.e., fraud/no fraud) sense.

Under this arrangement, for any claim, the following four outcomes are possible:

1. The model predicts that the claim contains fraud (that is,  $\mu_i > 0.50$ ), and the claim is indeed found to contain fraud. This outcome is called a *true positive*.
2. The model predicts fraud, but the claim does not contain fraud (i.e., a *false positive*).
3. The model predicts no fraud (i.e.,  $\mu_i < 0.50$ ), but the claim contains fraud (i.e., a *false negative*).
4. The model predicts no fraud, and the claim does not contain fraud (i.e., a *true negative*).

Outcome #1—the true positive—clearly represents a success of the model, as it correctly identifies a fraudulent claim, thus preventing unnecessary payment and saving the company money. Outcome #4, the true negative, while not as dramatic, similarly has the model doing its job by not sending us on a wild-goose chase.

Outcomes #2 and #3—the false positive and false negative—are failures of the model, and each comes with a cost. The false negative allows a fraudulent claim to slip by undetected, resulting in unnecessary payment. The false positive also incurs a cost in the form of unnecessary resources expended on a claims investigation as well as possible impairment of goodwill with the insured.

If the model were perfect—that is, it would predict a probability of 0% for each non-fraud and 100% for each fraud—then the true positive and true negative would be the only possible outcomes, regardless of the threshold chosen. For real-life models, on the other hand, false negatives and false positives are possible, and selection of the

discrimination threshold involves a trade-off: a lower threshold will result in more true positives and fewer false negatives than a higher threshold, but at the cost of more false positives and fewer true negatives.

We can assess the relative likelihoods of the four outcomes for a given model and for a specified discrimination threshold using a test set. We use the model to score a predicted probability for each test record, and then convert the predictions of probability into binary (yes/no) predictions using the discrimination threshold. We then group the records by the four combinations of actual and predicted outcomes, and count the number of records falling into each group. We may display the results in a  $2 \times 2$  table called a *confusion matrix*. The top panel of Table 13 shows an example confusion matrix for a claims fraud model tested on a test set that contains 813 claims, using a discrimination threshold of 50%.

The ratio of true positives to total positive events is called the **sensitivity**; in this example, that value is  $39/109 = 0.358$ . This ratio, also called the *true positive rate* or the *hit rate*, indicates that with a threshold of 50%, we can expect to catch 35.8% of all fraud cases.

The ratio of true negatives to total negative events is called the **specificity**, and is  $673/704 = 0.956$  in our example. The complement of that ratio, called the *false positive rate*, is  $1 - 0.956 = 0.044$ . This indicates that the hit rate of 35.8% comes at the cost of also needing to investigate 4.4% of all non-fraud claims.

We may wish to catch more fraud by lowering the threshold to 25%. The bottom panel of Table 13 shows the resulting confusion matrix. As can be seen, the hit rate under this arrangement improves to  $75/109 = 68.8\%$ —but it comes at the cost of an increase in the false positive rate to  $103/704 = 14.6\%$ .

**Table 13. Confusion Matrices for Example Fraud Model  
With Discrimination Thresholds of 50% (*top*) and 25% (*bottom*)**

| Discrimination Threshold: 50% |                    |     |                    |     |       |
|-------------------------------|--------------------|-----|--------------------|-----|-------|
| Actual                        | Predicted          |     |                    |     | Total |
|                               | Fraud              |     | No Fraud           |     |       |
| Fraud                         | <i>true pos.:</i>  | 39  | <i>false neg.:</i> | 70  | 109   |
| No Fraud                      | <i>false pos.:</i> | 31  | <i>true neg.:</i>  | 673 | 704   |
| Total                         |                    | 70  |                    | 743 | 813   |
| Discrimination Threshold: 25% |                    |     |                    |     |       |
| Actual                        | Predicted          |     |                    |     | Total |
|                               | Fraud              |     | No Fraud           |     |       |
| Fraud                         | <i>true pos.:</i>  | 75  | <i>false neg.:</i> | 34  | 109   |
| No Fraud                      | <i>false pos.:</i> | 103 | <i>true neg.:</i>  | 601 | 704   |
| Total                         |                    | 178 |                    | 635 | 813   |

A convenient graphical tool for evaluating the range of threshold options available to us for any given model is the **receiver operating characteristic curve**, or **ROC curve**, which is constructed by plotting the false positive rates along the  $x$ -axis and the true positive rates along the  $y$ -axis for different threshold values along the range  $[0,1]$ . Figure 26 shows the ROC curve for our example claims fraud model.

The  $(0, 0)$  point of this graph represents a threshold of 100%, with which we catch no fraudulent claims (but investigate no legitimate claims either). Moving rightward, we see that lowering the threshold and thereby incurring some false positives yields large gains in the hit rate; however, those gains eventually diminish for higher false positive rates. The two example thresholds detailed in Table 13 are plotted as points on the graph.

The ROC curve allows us to select a threshold we are comfortable with after weighing the benefits of true positives against the cost of false positives. Different thresholds may be chosen for different claim conditions—for example, we may choose a lower threshold for a large claim where the cost of undetected fraud is higher. Determination of the optimal threshold is typically a business decision that is out of the scope of the modeling phase.

The level of accuracy of the model, though, will affect the severity of the trade-off. A model that yields predictions that are no better than random will yield true positives and false positives in the same proportions as the overall mix of positives and negatives in the data, regardless of the threshold chosen. Therefore, for such a model, the ROC curve will follow the line of equality. A model with predictive power will yield true positives at a higher rate than false positives, resulting in a ROC curve that is higher than the line of equality. Improved accuracy of the model will move the ROC curve farther from equality, indicating that the model allows us a better hit rate for any level of false positive cost.

The model accuracy as indicated by the ROC curve can be summarized by taking the area under the curve, called the **AUROC** (for “area under ROC”). A model with no

**Figure 26.** ROC Curve for Example Fraud Model

![ROC Curve for Example Fraud Model. The graph plots Sensitivity (true positive rate) on the y-axis against 1-Specificity (false positive rate) on the x-axis, both ranging from 0% to 100%. A solid line represents the ROC curve, which is significantly above the dashed line of equality. Two points on the curve are marked: p=0.5 at approximately (10%, 35%) and p=0.25 at approximately (15%, 70%).](89a1c1bd24813c8b1e3b62da144728c8_img.jpg)

The figure is a Receiver Operating Characteristic (ROC) curve for an example fraud model. The x-axis is labeled '1-Specificity (false positive rate)' and ranges from 0% to 100% in 20% increments. The y-axis is labeled 'Sensitivity (true positive rate)' and also ranges from 0% to 100% in 20% increments. A dashed diagonal line from (0,0) to (1,1) represents the 'Line of equality'. A solid black line represents the 'ROC curve', which starts at (0,0) and rises steeply, indicating good predictive performance. Two specific threshold points are marked on the curve with black squares: one at approximately (10%, 35%) labeled 'p=0.5', and another at approximately (15%, 70%) labeled 'p=0.25'. A legend in the bottom right corner identifies the solid line as the 'ROC curve' and the dashed line as the 'Line of equality'.

ROC Curve for Example Fraud Model. The graph plots Sensitivity (true positive rate) on the y-axis against 1-Specificity (false positive rate) on the x-axis, both ranging from 0% to 100%. A solid line represents the ROC curve, which is significantly above the dashed line of equality. Two points on the curve are marked: p=0.5 at approximately (10%, 35%) and p=0.25 at approximately (15%, 70%).

predictive power will yield an AUROC of 0.500. The ROC curve of the hypothetical “perfect” model described earlier will immediately rise to the top of the graph (as any threshold below 100% would correctly identify all fraud cases and trigger no false positives), thereby yielding an AUROC of 1.000. The ROC curve of our example model plotted in Figure 26 yields an AUROC of 0.857.

Note, however, that the AUROC measure bears a direct relationship to the Gini index discussed in the previous section, such that one can be derived from the other.<sup>17</sup> As such, AUROC and the Gini index should not be taken as separate validation metrics, since an improvement in one will automatically yield an improvement in the other.

---

<sup>17</sup> Specifically, the AUROC is equal to  $0.5 \times \text{normalized Gini} + 0.5$ , where *normalized Gini* is the ratio of the model's Gini index to the Gini index of the hypothetical “perfect” model (where each record's prediction equals its actual value).

