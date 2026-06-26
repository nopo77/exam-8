---
paper: chalk_et_al
chapter: 10
title: Challenges and Considerations in Ratemaking Models
topics: [data_quality, model_drift, cross_validation_limitations, regulatory_constraints, outliers, missing_values, adverse_selection]
key_formulas: []
---

> **TL;DR**
> - Data understanding before modeling is critical: verify field meanings, expected ranges, and coding consistency by consulting data owners and business experts.
> - Model drift (concept drift): the relationship between predictors and response changes over time; detect with time-interaction GLMs, segmented models by year, or rolling-window analysis.
> - Cross-validation fails when future business mix differs significantly from training data (adverse selection on thin segments can cause actual performance far worse than CV performance).
> - Regulatory constraints: forbidden variables (race, gender, education) require offset or proxy-variable approaches; fixed-relativity variables (regulated credit scores) require offset methods.
> - Data quality checklist: negative/impossible values, inconsistent categorical coding over time, drone/irrelevant exposure contamination, and inappropriate combining of heterogeneous datasets.

# 10. Challenges and Considerations in Ratemaking Models

In this monograph, we have focused on certain technical challenges that occur during the training of GLMs. Throughout the process and after, we need to be aware of the limitations of our data and the impact this may have on the performance of our models. In this chapter, we look at some of the issues that a practitioner should consider.

## 10.1. Understanding the Data

Before working with a dataset, we need to understand it. We need to be clear on the meaning of each field and the range of values we should expect. In order to do this it is a good idea to speak to the team that created the dataset and/or to people who have previously carried out analysis on the data. Likewise it is useful to speak with underwriters or others who understand the line of business.

In our work, we made a basic error which could have been avoided with additional conversations prior to carrying out our analysis. During data preparation, we noticed that the age of manufacture was missing in about 20% of cases, which meant that for those cases we could not calculate the age of the aircraft. We could have set aircraft age to missing for those cases and then dealt with missing values in one of a number of ways. However, on the assumption that the certificate (for which the data contains the feature “certificate\_issue\_date”) is issued shortly after manufacture, a “shortcut” seemed to be to use the certificate issue year instead of year of manufacture. We later realized that registration certificates (as opposed to airworthiness certificates) are issued at various stages during an aircraft’s life, in particular upon change of ownership or use. This is apparent from the data as well but is an error that would certainly have been avoided with discussions prior to analysis.<sup>83</sup>

Other areas where discussions would have benefited our analysis are in the treatment of drones and in the treatment of aircraft for which we assumed that the registered users

---

<sup>83</sup> We have not redone the analysis including the corrected aircraft age and years since aircraft certificate issue. We leave that as an exercise to the interested reader.

have addresses outside of the US.<sup>84</sup> It is possible that some of the strong interactions seen in the previous chapter are due more to aspects of our data preparation than true differences in the probability of accidents.

## 10.2. Technical Errors

There are errors that we practitioners should not make during modeling, but we do. At best, they can waste time by requiring us to rework an analysis; at worst, they can negatively impact our results and cause incorrect rating plans to be implemented.

Examples include:

- Inconsistent coding of rating variables between modeling train and test datasets or, worse, between analysis data and operational data. A simple example of where this can go wrong is where variables which are strings are coded to categorical variables, e.g., Cessna is coded as 1 and Piper is coded as 2 in training data, but in test data the coding is reversed. In certain software, this coding is mostly invisible to the user and needs to be explicitly checked.
- Coding categorical features as numbers that are then treated in an ordinal manner. In our FAA-NTSB work, we intended to treat the number of engines as a categorical feature, but early on we were treating it as a number. An easy way to ensure that this does not happen is to store categorical features using letters (for example, one engine is coded as “A”).
- Including segments of data which are not relevant and whose experience might adversely impact areas of the model where performance matters. For example, drone insurance may be sold under a separate product and rating plan. Including a significant amount of drone exposure (which has no claims) in our data is unlikely to help performance on other general aviation business.

These and a multitude of other technical errors are easy to make. Peer reviews during modeling and after implementation of the rating plan are required to avoid, or at least reduce, such errors.

## 10.3. Data Does Not Meet Model Assumptions

Insurance data often contains inherent dependencies that challenge the assumption of independent and identically distributed (iid) observations, which is a foundational premise for most supervised learning techniques, including GLMs and their variants. For example, someone who has previously filed a claim is more likely to file another in the future, which is why insurers often apply surcharges for recent claim experience. Similarly, in-

---

<sup>84</sup> Our assumption that the US region being missing meant that the registered user has an address outside of the US was wrong.

suring two neighboring townhouses introduces a dependency because a fire in one could easily spread to the other, a scenario unlikely if the houses were miles apart.

These examples highlight that our data are often not independent and, while we can still build effective models despite violating the iid assumption, it's crucial to verify and account for this lack of independence. In such cases care must be taken in setting up cross-validation folds to avoid data leakage. For instance, in personal auto insurance, all vehicles under the same policy should be placed in the same fold, and for weather-driven perils, each year could serve as a separate fold to prevent storms from leaking across them.

Provided that this is done, we can then benefit from the power of cross-validation to help measure the uncertainty of our model's predictions, even in the presence of non-independent data. By dividing the data into folds and training and testing in various combinations, cross-validation can provide insights into how the lack of independence impacts our model's performance. While cross-validation does not alter the final model, it can inform decisions about model adjustments and offer a more accurate assessment of how dependencies in the data might affect the model's predictions.

## 10.4. Stability Over Time

### 10.4.1. *Coefficients can change over time*

Model drift (or concept drift) refers to the situation when a model's performance gets worse over time because the relationship between the predictors and the response variable changes over time. For example, the risk associated with young drivers might increase due to rising distractions, or underwriting discounts might evolve into surcharges if they are gamed by insureds. Some changes may be quite sudden and may also reverse at some point. For example, for private auto portfolios which use occupation as a rating factor, the relativities for different occupations may have changed during COVID-19.

Generalized linear models (GLMs) and generalized additive models (GAMs) can be vulnerable to time inconsistencies because they tend to average out such inconsistencies in the final coefficients, potentially masking important temporal trends. Therefore checking and accounting for the time consistency of parameters is a critical consideration. If this is not done, the model's coefficients could misrepresent the true risk for future policies, leading to suboptimal pricing or risk assessment.

Reviewing the time consistency of parameters involves analyzing how coefficients evolve over different periods. This can help identify general instability or emerging trends that may otherwise go unnoticed. Some techniques to do this include:

- For each feature individually create a new GLM where that feature is interacted with time. Then either inspect the fitted coefficients or (having used LASSO regularization) check if the interaction effect is selected by the LASSO. The latter approach can easily

be automated.

- Segmented modeling. In our context, by “segmented modeling” we mean fitting the model to one year of data at the time and comparing the coefficients as time moves forward.
- Rolling window analysis. This is similar to segmented modeling except that the periods overlap. For example, with five years of data we fit a model to years 1–3 and then 2–4, etc. Finally we compare the resulting coefficients.
- Regular recalibration. This means refitting the existing model on updated data.

These (and other) methods can help us take a proactive approach to monitoring and to adjust for time inconsistencies. This, in turn, helps ensure that the models remain robust and relevant, even as underlying risk factors evolve.

### **10.4.2. *The meaning of data can change over time***

When relying on third-party models, such as obtaining a roof score<sup>85</sup> via API from a vendor, it is important to recognize the potential risks associated with changes to those models. If the vendor updates their model, the new scores might represent something different than historical records, which could lead to inconsistencies in your analysis. While adding a control variable for the model version might help if the vendor notifies you of changes, this approach may be insufficient on its own. Resolving these discrepancies often requires a case-by-case approach, depending on the nature of the changes and the data involved.

A relevant example in the US is the use of credit-based scores, where an actuary might be working with different programs that use varying credit models. Combining these scores or simply applying control variables may not adequately address the differences. Properly accounting for these variations often requires deep domain knowledge or additional outside analysis to ensure the integrity and consistency of the data. Without appropriate adjustments, reliance on third-party models can introduce significant risks, potentially compromising the accuracy of predictive models.

### **10.4.3. *Business mix can change over time***

Generally, GLMs are robust to mix of business changes. By this we mean that well-fitted GLMs (with appropriate feature engineering and interaction effects) can produce reliable results even when there are shifts in the distribution of policyholders,<sup>86</sup> such as writing relatively more young drivers in recent years compared to earlier periods. However, this

---

<sup>85</sup> For household insurance, external vendors exist that provide scores of roof material, shape, and condition that can help predict frequency or severity of future claims related to roof damage or failure. These scores are typically based on analysis of geospatial imagery.

<sup>86</sup> Above, we referred to model drift. The shift referred to here is known as data drift.

robustness has its limits, particularly when the changes are substantial and involve factors that were previously excluded from the model.

For instance, if underwriting rules had previously prevented the inclusion of coastal risks, but now these risks are being written, the model may struggle to accurately predict outcomes. (This is a specific example of the danger of extrapolation beyond the range of the training data.) Even with geographic variables and territorial ratemaking in place, the GLM might not fully account for the differences between coastal and non-coastal risks, leading to potential inaccuracies. The model may be attempting to fit fundamentally different risks within the same framework, which can undermine its predictive power. In such cases, additional modeling adjustments or more granular risk segmentation may be necessary to maintain accuracy.

### **10.4.4. When cross-validation will fail**

The point above, that business mix can change over time, is very pertinent to our use of cross-validation. We have discussed that cross-validation is an estimate of generalization performance—how well our model will do on policies that will be written in the future and which it has not seen during training. Cross-validation performance is calculated by taking an average over policies in the cross-validation folds. Within those policies there may be small segments which perform really poorly but where there are not currently sufficient policies for this to be noticeable in overall performance (or to calculate coefficients accurately). If we incorrectly price those policies and attract a large number of them (due to adverse selection), our business mix will in the future be skewed towards the poorer performing segment, and actual performance will be far worse than cross-validation performance.<sup>87</sup> A careful check of proposed price changes by segment can help limit this risk. If possible, price comparisons by segment with chief competitors should be carried out. An ongoing and careful monitoring of business mix post rate change can be useful in allowing the business to react quickly to any issues that arise.

## **10.5. Regulation**

In predictive modeling, it is important to recognize that the meaning of predictors can vary significantly depending on the context, particularly across different states or jurisdictions. For instance, the criteria for a safe driver discount might be determined by the underwriter in one state, while in another state, it could be mandated by the regulator to be offered to anyone who completes a specific course. This variation means that simply using the state as a control variable may not adequately capture the true differences in what “safe driver” represents from one state to another. To address this, actuaries may

---

<sup>87</sup> This issue is not unique to cross-validation—it applies more generally. Most standard modeling techniques are far from impervious to the baleful confluence of thin data and consumer response.

need to employ interaction terms or residual models to better account for these material differences and improve the accuracy of their models. Another example—an insurer may have been collecting “number of stories” for a homeowners line of business. However, those data may have been populated in many different ways over the years. First, it was agent input, then a vendor provided it based on public record, now a new vendor is providing it based on satellite imagery.

Depending on the line of business and jurisdiction, regulation can also impact factor limitations. The main rating variable where the regulations limit or heavily regulate use is credit scores. In home and auto insurance, this is highly predictive but controversial in its use. Some states have outright disallowed its use in rating, while others restrict it to underwriting only (i.e., writing company placement). There are the “disallowed” rating variable (race, religion, education, income, etc.) which, despite being predictive in many cases/lines, are not allowed. These are the main restrictions; so while they may be predictive in a model, use in practice for rating, underwriting, marketing, etc., are challenged for insurance companies. We discussed in Chapter 8 the options for dealing with disallowed data types during the modeling process.

## 10.6. Outliers and Model Stability

Outliers in predictors, rather than in the observed target variable, can significantly impact methods such as the GLM, particularly in insurance datasets. For example, insuring a Ferrari—an extreme outlier in terms of vehicle value and performance characteristics—can skew the distribution of predictors such as vehicle cost and engine size. These outliers can exert an undue influence on the model, potentially distorting the relationships between predictors and the target variable, leading to biased or unstable coefficients. Additionally, they can inflate the variance of the model’s predictions, reduce overall model accuracy, and complicate the interpretation of the results. To mitigate these effects, it is crucial to identify and appropriately handle outliers. The simplest approach is to omit such records, but alternatives include techniques such as robust regression, transformation of variables, or applying capping and flooring strategies to limit the influence of extreme predictor values.

## 10.7. Data Quality

Data are seldom complete or correct.

Before carrying out an analysis, we need to understand the deficits in our data. Ideally, we will ensure that our data is of a reasonable quality, and it remains so over time. This is hard. Scrubbing (making the data usable for modeling purposes) includes simple things like making sure there are no negative ages; that there are no impossibly large values of variables; that levels of categorical factors are consistent over time and that their mean-

ing is consistent over time; that where data is missing, we understand why, and so on. There may be other departments who also have examined the quality of this data in the past or who do so on an ongoing basis for various operational processes. We should take advantage of what they have found. There could be operational issues causing errors in our data. As important as remediating the data is, so too are tests for confirming that the data has been remediated and that these tests are independent of the specific remediation techniques applied.

Inevitably, we spot further errors during modeling—some data deficits are most (or only) visible during the model training or evaluation process. Ideally, we would have the time to return to data preparation and remediation during the modeling steps which follow it and to redo our models. We can help ourselves by ensuring that our modeling process is well documented and replicable, so that if rework is required, it can be done quickly.

Even after our best efforts, the statement—data is seldom complete or correct—is usually true. We are then faced with the challenge of what changes can be made to the data in order to fix deficits preventing correct analysis. This is a complete topic in its own right. Here we briefly mention some possibilities:

- Observations with nonsensical values for an important feature (e.g., age) can be deleted. If the incorrect value is for a feature which we know is not important, the value can be set to missing, and then it can be dealt with together with other missing values.
- Missing values<sup>88</sup> for categorical variables can be set to a missing category (e.g., “XXX”).
- Missing values for numeric values can be imputed, either replacing missing values with the mean (mean imputation) or using more sophisticated methods.

Besides the above points, there are broader issues. The expression “garbage in, garbage out” typically highlights the importance of accurate and high-quality data in producing reliable model output. However, this concept also applies to the composition of the data. For instance, if a book of business has been largely adversely selected against, the data may no longer be capable of generating meaningful parameters to effectively segment risk. Adverse selection can lead to a downward spiral, where the quality of the data deteriorates to the point that even sophisticated models cannot produce reliable predictions. In such cases, “garbage in, garbage out” is more than just a cautionary phrase—it’s a terminal diagnosis that requires more than basic modeling adjustments to resolve. Addressing this issue often demands a fundamental reevaluation of the data collection process, under-

---

<sup>88</sup> Dealing with missing values deserves a monograph in its own right. We note here that it is important to understand if the data is missing at random or not. If there is a pattern, i.e., a certain segment of data is always missing one or more fields—the impact at both model training stage and at prediction stage should be carefully considered.

writing practices, and even the business strategy to break the cycle of adverse selection.

Many actuaries may consider combining seemingly similar datasets, such as closed programs with open ones, or merging data following a merger or acquisition with a similar business. The aim is to increase volume, and since the data might not be homogeneous, the practitioner will add a control variable which indicates which dataset the data on each line comes from and includes that variable in the GLM. However, differences in the underlying data can lead to significant issues. Adding data from disparate sources can introduce noise and obscure meaningful patterns. Therefore, great care should be taken to thoroughly evaluate whether combining datasets is appropriate, ensuring that the integrity and predictive power of the model are maintained.

## 10.8. Conclusion

One can say that there are three parts to creating a rating plan:

- Preparing the data.
- Carrying out the analysis.
- Making sure that the rating plan is fit to go to market.

Data preparation is hard and time-consuming. There are many aspects to it: collection of data from business systems, preparation and collection of data assets, data storage, ensuring data quality, checking for data drift, understanding each feature, and so on. An ongoing and significant effort is needed in this area (even if it is not always appreciated).

Making sure that the rating plan is fit to go to market is also a time-consuming and vital task. In many lines of business, one small misstep in a rating plan will be taken advantage of by the segment of the market which is advantaged by the mistake, and the resulting losses may well outweigh any performance advantages gained through months of rating plan analysis. Careful comparisons between rating series and also with other rates in the market are needed. In specialty lines of business, detailed discussions with underwriters are vital.

In this monograph, we have mainly focused on the easiest and quickest<sup>89</sup> aspect of this process. Nonetheless, optimizing performance through our analysis is clearly a big part of what gives each business the opportunity to thrive in its marketplace. We hope that this monograph goes some way towards helping the practitioner achieve that aim.

---

<sup>89</sup> ...and possibly the most fun for actuaries!

