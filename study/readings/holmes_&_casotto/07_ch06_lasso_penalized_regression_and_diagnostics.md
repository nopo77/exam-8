---
paper: holmes_&_casotto
chapter: 6
title: Lasso Penalized Regression and Lasso Credibility Model Diagnostics
topics: [model_diagnostics, relativity_plots, credibility_review, penalty_parameter, ordinal_variables, complement_review]
key_formulas: []
---

> **TL;DR**
> - Lasso models produce no p-values; model review shifts from significance testing to evaluating the penalty parameter λ and the complement of credibility.
> - Relativity plots display complement relativity, indicated relativity (offset + model output), observed relativity, and exposures — the primary diagnostic tool for lasso credibility.
> - Full credibility to complement (coefficient = 0): either data matches complement or segment is too thin; do not use thin-segment behavior to judge complement quality.
> - Partial credibility: indicated estimate lies between complement and GLM; deviations proportional to exposure are expected and appropriate.
> - Categorical variables: maintain granularity; lasso automatically collapses insignificant levels to the complement — no need to pre-group thin categories.
> - Ordinal variables: non-monotone reversals signal λ too low; increase λ until curves are actuarially smooth; avoid continuous variables in lasso credibility — use ordinal treatment instead.

# 6. Lasso Penalized Regression and Lasso Credibility Model Diagnostics

The modeler must review lasso penalized regression and lasso credibility models in a different manner than they would a GLM. Lasso models provide no  $p$ -values, and the evaluation of variables shifts from significance to credibility. Additionally, lasso credibility models require review of the complement of credibility as the complement can greatly influence the indicated coefficients or receive full credibility. New visualizations such as relativity plots and a switch from continuous to ordinal variables will greatly aid model building and model review.

## 6.1. Review of the Lambda Penalty Parameter

GLM validation relies heavily on the evaluation of  $p$ -values and standard errors, but lasso penalization does not provide such statistics. Methods that exist to create approximate  $p$ -values have not been largely successful (Casella et al. 2010) and are not recommended for model review as they can be misleading. Fortunately, as we described earlier, lasso penalization removes the need for post hoc significance testing through the application of partial credibility during the fitting process. Therefore, review of lasso credibility models should move from post hoc significance analysis to an evaluation of the lambda penalty term used to assign credibility.

- GLM review focuses on **significance**: Are we sure that a coefficient should be included?
- Lasso review focuses on **credibility**: How much can we trust the subject experience, if at all?

Table 6.1 compares treatment of variables in a GLM and treatment in lasso.

A properly selected penalty term automatically accounts for all considerations reviewed by  $p$ -value significance analysis through the application of credibility. The following questions are sufficient when reviewing the selected penalty term for appropriateness:

- Was the lambda parameter selected via cross-validation or another robust methodology?
- If there was an adjustment to the lambda penalty parameter, was the adjustment favoring a more robust model? Why was this adjustment made?
- Is the behavior of variables intuitive with the selected lambda penalty parameter?

**Table 6.1. A Comparison of Variable Behavior in GLM and Lasso Credibility by Statistical Importance**

| Variable Importance | GLM                                                                                                                                                      | Lasso Credibility                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Low                 | Subjective decision rule, i.e., remove when $p$ -value $> 0.05$ .                                                                                        | Automatically set to 0.0.                                                                                 |
| High                | Full credibility is assigned to the observed relativity.                                                                                                 | Credibility is assigned <b>more</b> to the <b>observed</b> than the complement of credibility.            |
| Medium              | Full credibility is assigned to the observed relativity during model fitting.<br><br>Manual adjustments may be appropriate for $p$ -values near to 0.05. | Credibility is assigned <b>more</b> to the <b>complement</b> of credibility than the observed experience. |

The lasso penalty term provides a data-driven, uniform, and efficient method of addressing partial credibility. Lasso penalization eliminates the need for post hoc significance testing, hence significantly reducing the effort for model reviews. In the validation of lasso credibility models, a review of the complement of credibility is necessary.

## 6.2. Review of the Complement of Credibility

The review of a complement of credibility can be initially guided by the considerations in ASOP 25 and existing actuarial literature. We will not spend time on these traditional review criteria (i.e., similarities and differences between the subject and relevant experience, etc.) but will instead discuss considerations unique to lasso credibility and where a reviewer may want to focus their review depending on what is most material to their scope.

Lasso credibility is a multivariate procedure, and therefore we should consider correlations between risk characteristics that are being offset. Penalized regression natively assigns signal among correlated predictors, but using an offset can hinder the model's ability to detect shifts in signal between them. A reviewer should also pay special attention to correlated risk characteristics if their complements come from multiple sources. This combination of complements may provide an overestimated or underestimated prior assumption.

In addition to reviewing a complement of credibility by itself, modeling results will provide information on the appropriateness of the complement of credibility. To compare the complement of credibility to model output, we recommend the use of **relativity plots**. These plots will help to identify segments where a reviewer may want to spend additional time evaluating both the complement of credibility and the modeled results.

## 6.3. Relativity Plots

Traditional univariate charts are insufficient for lasso credibility model review. The indicated relativities from a lasso credibility model are deviations from a complement of credibility, and therefore it is essential to combine those relativities with the offset to see the true indicated coefficient. We recommend the use of relativity plots, which may contain the following items:

- The complement relativity (offset relativity)
- The indicated relativity (offset combined with modeled relativity)
- The observed relativity (optional)
- Exposures

See Figure 7.17 for an example of a relativity plot.

If one uses several transformations for a single variable, one needs to combine all such transformations to create the final indicated relativity. This combined relativity allows a reviewer to see how and where the model has indicated credible differences from the complement. By overlaying the observed values, we can see how reactive the model is to the experience in the data. Although lasso credibility is likelihood based rather than exposure based, benefit to likelihood correlates highly with amount of exposure. Including exposure bars allows a reviewer to see a representation of the amount of experience supporting a deviation from the complement of credibility. The combination of these four above elements makes relativity plots a helpful tool for lasso credibility model review.

### 6.3.1. Using Relativity Plots to Guide Model Review

The review of relativity plots focuses on the following question: Are the deviations from the complement of credibility stable and intuitive across all variables?

The question is not trivial as what is considered “stable” and “intuitive” varies between and within models. We first discuss how such definitions differ when the complement is receiving full, partial, or no credibility. Then we provide guidance on how to review stability and intuitiveness differently in categorical, ordinal, and continuous variables.

### 6.3.2. Full Credibility in the Complement

A reviewer could start by examining coefficients where the complement has received full credibility. Here are two scenarios where lasso credibility will assign full credibility to the complement:

1. When there is sufficient exposure to model but the experience is too similar to the complement of credibility to deviate
2. When there is insufficient data in a segment to pass the threshold of lasso credibility

The first scenario is ideal because the segment is credible and our model has penalized the modeled coefficient to zero. We can be confident that the estimate is reasonable

given the high credibility, and it is not recommended for a reviewer to spend significant time scrutinizing this coefficient.

In the second scenario, the complement is likely to receive full credibility—even if it is unreasonable. Even though this segment may not be a material portion of the book today, an inappropriate complement could expose an insurer to adverse selection, prohibit growth, or place an unreasonable burden on policyholders. Large deviations between observed and predicted (offset) are expected for these smaller segments and should not be used to justify that the complement is unreasonable, and similarly, small deviations should not be used to justify that the complement is reasonable. Instead, a reviewer should rely purely on traditional considerations when reviewing the complement when little data is available.

### ***6.3.3. Partial Credibility in the Complement***

A more common situation is that the complement will receive partial credibility. The predicted relativity will be somewhere between the observed relativity and complement relativity. Two common scenarios are as follows:

1. Where a specific segment has a medium amount of data that passes the threshold of significance but not enough to deviate significantly.
2. Where the entire data set is smaller than necessary to achieve full credibility.

Small differences between the complement and indicated relativities are most often an ideal result in a lasso credibility model. In a GLM, small coefficients are often scrutinized for low significance as it may be hard to reject the null hypothesis that the true coefficient is zero. Small coefficients should be far more accepted in lasso credibility as they have overcome the lasso credibility standard and reflect the assignment of partial credibility between the complement and experienced relativities. When deviations are proportional to the data in a segment and reasonable given the complement experienced relativities, the assigned credibility is likely appropriate.

We recommend an observer focus more of their time on segments with medium or small amounts of data that have large differences between the complement and indicated relativities. Large differences across many coefficients could indicate that the penalty term is too small and needs to be increased. Large differences in single categories or unexpected areas of an ordinal variable could suggest the presence of an outlier in the data that may need adjustment. When reviewing large deviations, remember that the same likelihood-based credibility standard is applied to all variables equally. It is possible that a large deviation is supportable based on the data—especially if that deviation is actuarially intuitive and other coefficients are behaving appropriately.

When the entire data set is smaller than necessary to achieve full credibility, a review of coefficient stability and intuitiveness is extremely important. If many coefficients have actuarially unintuitive deviations, that is a sign that the selected penalty term may be too small. Be careful not to reject unintuitive deviations outright as sometimes the real world does not behave as expected.

It is also helpful to think of this situation as relativities being pulled toward a complement or pulled toward the data's experience. We want this pull to be balanced toward the truth, and not over- or underreactive. A penalty term that is too small will potentially overshoot the true relativities while a penalty term that is too large will not sufficiently move toward the true relativities. Small data sets create the trickiest situation to review because both the complement of credibility and selected penalty term will have a large impact on model output. Lasso credibility is still worth it, however, and we show that it provides the highest benefit over other methodologies when modeling on smaller data sets in the case study (Section 7.6.2).

### **6.3.4. Limited or Materially No Credibility in the Complement**

Sometimes, our complement is receiving limited or materially no credibility because the segment has a large amount of data. For example, a large data set with a binary characteristic split 50/50 in data will see limited effect from all but the worst of complements. Large deviations from the complement should still be investigated, but a change of complement of credibility is unlikely to be material to the model output. If a segment is receiving full credibility with limited experience, it may be a sign that the penalty parameter is too low. If a segment is receiving full credibility with large experience, a reviewer can be confident in the estimates being produced without extensive review.

## **6.4. Review by Variable Type**

When building a lasso credibility model, the modeler is seeking to identify the credible difference between the complement and the signal in the data. This is problematic, as often the location of that difference is unknown at the beginning of the modeling process! For categorical variables, we will see that a modeler has the freedom to use more granular categorical variables in lasso credibility than in a GLM or penalized regression. Continuous variables do not receive a similar benefit and are best substituted with an ordinal treatment of variables in lasso credibility.

### **6.4.1. Categorical Variables**

Categorical variables are the most intuitive to review in lasso credibility.

In a GLM, categorical levels that are insignificant may be grouped with each other or with the base level to obtain a stable coefficient. In lasso credibility, we recommend avoiding the grouping of categories and instead maintaining categories that are at least as granular as the selected complement of credibility. When a level is insignificant, it will be collapsed to the complement. This assignment of full credibility to the complement removes the need to group a noncredible category with another category.

Each of the categorical levels can be evaluated using similar criteria to classical or Bühlmann credibility with the difference that any change to the penalty term will result in changes across all variables. The most important item to review in categorical relativity plots is whether the deviation is directionally appropriate and whether the magnitude of the change is properly responsive.

### 6.4.2. Continuous Variables

Continuous variables are difficult to conceptualize in lasso credibility as it is the **slope** that is penalized and not a categorical **magnitude**. Additionally, variable transformations no longer reflect the shape of the overall curve, but rather the shape of the **difference** from the curve of the complement of credibility. As we said earlier, the shape of that deviation is usually unknown and is in fact part of what a lasso credibility model is meant to discover.

Because of this, great care is needed when using continuous variables in lasso credibility. The example in Chapter 7 uses continuous variable transformations that are known to reflect the true distribution of the data, but that will never be the case in practice. Continuous variables are used later only so that our GLM and lasso credibility models both start with the same information and can be more easily compared. In practice, we **highly** discourage the use of continuous variables in lasso credibility.

Review should focus first on the ability of the continuous transformation to accurately capture potential differences from the complement. For example, if a linear variable alone is included, the only difference the model will identify is a change in overall slope and not a hinge or change in slope after a certain value.

Second, review can focus on the potential extrapolation of continuous variables to levels where there is minimal credibility. One should investigate whether an indicated change continues to grow in magnitude in the tails of a continuous variable—especially if the experience in the data does not strongly support such a change. This could be a sign of unintuitive extrapolation, and the variable will need to be adjusted.

Again, we use continuous variables in our case study in Chapter 7 only because the true form of the deviation from the complement of credibility is known. Similarly, we would recommend the use of continuous variables in lasso credibility only if one knows that a change in slope will properly capture the deviation from a complement of credibility. We cannot provide an example of this situation in a real application.

### 6.4.3. Ordinal Variables

On the other hand, ordinal variables are easy to review in lasso credibility and can be quite useful in determining an appropriate penalty term. If an ordinal variable contains reversals (up for age 20, down for 21, up for 22, etc.), the selected penalty term is likely too low. A common method of selecting a credibility standard is to start with the indicated penalty term and gradually increase that term until all unintuitive reversals are removed from the indicated relativities. In most situations, this results in both an actuarially and statistically sound model.

The tails of ordinal variables also have the benefit of not extrapolating beyond what is indicated by the data as an uncapped continuous variable will extrapolate. At the same time, ordinal variables may not extrapolate where a modeler believes it is justified. Ordinal variables force a modeler to choose and justify an extrapolation as opposed to allowing a selected variable transformation to provide “support” for a relativity beyond what may be statistically justified. For this reason, judgmental adjustments and

extrapolation at the tails of ordinal variables may be appropriate when using both lasso credibility and traditional lasso penalization.

### **6.4.4. Control Variables**

Whether or not to apply a complement for control variables is a judgmental decision, and both options can be motivated by different arguments.

It is reasonable to include a best estimate complement of credibility for control variables when using lasso credibility. For example, each state's prior overall rate relativity could be used as an offset in a loss model. With this complement, coefficients for individual state categories will correct for any significant difference between the estimate and experienced relativity. Determining this complement is difficult for a factor such as "year," which can include effects from trend, development, and changes in legal environment.

It is also reasonable not to include offsets for control variables. As with traditional penalized regression, if the model views the effect of a control variable as insignificant, that insignificant signal is unlikely to have a material effect on other variables. Although a modeler should continue to use control variables in lasso credibility, it is up to them to decide whether using a corresponding complement of credibility is material and necessary.

## **6.5. Model Validation Conclusions**

By moving away from the full credibility assumption of GLMs, lasso credibility model validation changes from a review of significance to a review of credibility. The change is motivated first by the benefits of penalized regression through the bias–variance trade-off and second by the ability to introduce bias toward a selected complement of credibility. The change in focus greatly simplifies model review.

The statistical and actuarial review of a lasso credibility model is quite straightforward. If the complement is appropriate and all variables are treated as categorical or sufficiently granular ordinal variables, the only item left to review is the penalty parameter. If the parameter was initially selected in a statistically sound manner (cross-validation) and adjusted in an actuarially sound manner (adjusted higher to produce actuarially sound relativities as reviewed in relativity plots), we suggest that the model is a proper statistical application of lasso credibility. Review can focus mostly on post-modeling selections and any application of further actuarial judgment.

Given the simplicity of the ideal application of lasso credibility, it is difficult to build a deficient model without some clear red flags in the test statistics or relativity plots. Questionable behavior of a lasso credibility model should be further evaluated through a combination of penalized regression and traditional credibility expertise.

The next chapter consists of a case study that provides examples of both good and poor lasso credibility models. We hope that these examples can help readers become more comfortable with the processes of building and evaluating lasso credibility models.

