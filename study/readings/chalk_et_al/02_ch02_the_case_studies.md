---
paper: chalk_et_al
chapter: 2
title: The Case Studies
topics: [frequency_model, high_cardinality_categorical_variables, correlated_variables, case_studies, two_stage_modeling, geospatial_smoothing, model_validation]
key_formulas: []
---

> **TL;DR**
> - Three case studies: FAA-NTSB aircraft accident frequency (primary), UK STATS19 road traffic accidents (highly correlated features), and simulated auto data (known ground truth).
> - Aircraft make is an HCCV with 40,000+ levels; naive inclusion causes memory/convergence issues and unreliable predictions for thin categories.
> - UK road accident data has many feature pairs with correlations ≥ 0.90 (up to −0.96) from census data, illustrating multicollinearity challenges.
> - Simulated data provides ground-truth relativities (e.g., frequency × 4.65 for 17-year-old male), allowing calibration of performance metrics.
> - Four challenges previewed: HCCVs, combining separate model results with a GLM, controlling for disallowed features, and highly correlated variables.

# 2. The Case Studies

## 2.1. FAA-NTSB Data for Aircraft Incident Frequency

In the US, the Federal Aviation Administration (FAA) maintains records of all registered aircraft, and the National Transportation Safety Board (NTSB) maintains a database of all incidents (accidents and near misses) involving aircraft. Our main case study will be based on these records. Our dataset consists of all aircraft from the FAA records. Each aircraft is represented by one or more lines of data, one for each calendar year, depending on its certificate issue date and expiration date. For example, if the certificate issue date is July 1, 2010, and the expiration date is December 31, 2014, then the aircraft will be represented by five lines of data, one for each calendar year from 2010 to 2014. The exposure variable (named "ex" in our data) will be 0.5 (i.e., the six months from July 1, 2010 to December 31, 2020) for the first year and 1 (year) for the others. We added a target variable (number of claims, named "num\_cl" in our data) set to 1 where there was a match to an accident on the NTSB data and set to zero otherwise. Our aim will be to build a frequency model that predicts the probability of an aircraft accident (given the information we have about the aircraft, its use, etc.).

Although our focus will be on building a frequency model, almost everything we discuss applies equally to severity models. We note also that sometimes in aviation, rates for total loss insurance are supplied separately. Provided that the policy is on a declared value basis,<sup>2</sup> and the rate is charged per dollar of declared value, a severity model would not be needed. For example, our final model predicts a frequency of about 0.6 accidents per 1,000 aircraft for the Cessna Skyhawk. If about a third of these accidents are total losses, then an estimate of the total loss rate would be 20 cents per \$100.<sup>3</sup>

NTSB accidents since 2008 are used, and only aircraft with some active registration since that year are included. The FAA data includes the registration number (N-number) for each aircraft and has fields for certificate issue date and expiration date. We merged

---

<sup>2</sup> A declared (or agreed) value basis means the insurer and policyholder agree in advance on the amount payable in the event of a total loss, regardless of the actual replacement cost or market value at the time of the claim.

<sup>3</sup> If one was using the NTSB data for such purposes, one would need to remember that total loss incidents can happen without being reported to the NTSB.

the claims where the FAA N-number matched the NTSB N-number and the date of the NTSB incident was between the FAA certificate issue date and expiration date. On this basis, about 50% of claims were merged into the FAA data. Inspection of the unmatched incidents shows that many of them are for foreign aircraft not registered with the FAA. Were we to be using this data as part of a real rating exercise, we would look into this in further detail. However, for our purposes, the resulting dataset is sufficient as it allows us to illustrate and discuss various practical issues when fitting GLMs. For example:

- There are many different makes of aircraft, which leads to practical problems when trying to create a rating plan which has make of aircraft as a rating factor.
- The accident frequency varies with aircraft age<sup>4</sup> but not in a linear way—see Figure 2.1.

![Scatter plot showing accident frequency versus aircraft age. The y-axis is labeled 'accident frequency' and ranges from 0.0000 to 0.0100. The x-axis is labeled 'aircraft age' and ranges from 0 to 50. The data points show a general downward trend, starting at approximately 0.0100 for age 0 and decreasing to near 0.0000 for ages 40 and above, with some fluctuations.](cbc4516eb885829fe8c9dabc0946dcbe_img.jpg)

| Aircraft Age | Accident Frequency |
|--------------|--------------------|
| 0            | 0.0100             |
| 1            | 0.0085             |
| 2            | 0.0065             |
| 3            | 0.0055             |
| 4            | 0.0050             |
| 5            | 0.0045             |
| 6            | 0.0040             |
| 7            | 0.0035             |
| 8            | 0.0030             |
| 9            | 0.0025             |
| 10           | 0.0020             |
| 11           | 0.0018             |
| 12           | 0.0015             |
| 13           | 0.0012             |
| 14           | 0.0010             |
| 15           | 0.0008             |
| 16           | 0.0007             |
| 17           | 0.0006             |
| 18           | 0.0005             |
| 19           | 0.0004             |
| 20           | 0.0003             |
| 21           | 0.0002             |
| 22           | 0.0001             |
| 23           | 0.0001             |
| 24           | 0.0001             |
| 25           | 0.0001             |
| 26           | 0.0001             |
| 27           | 0.0001             |
| 28           | 0.0001             |
| 29           | 0.0001             |
| 30           | 0.0001             |
| 31           | 0.0001             |
| 32           | 0.0001             |
| 33           | 0.0001             |
| 34           | 0.0001             |
| 35           | 0.0001             |
| 36           | 0.0001             |
| 37           | 0.0001             |
| 38           | 0.0001             |
| 39           | 0.0001             |
| 40           | 0.0001             |
| 41           | 0.0001             |
| 42           | 0.0001             |
| 43           | 0.0001             |
| 44           | 0.0001             |
| 45           | 0.0001             |
| 46           | 0.0001             |
| 47           | 0.0001             |
| 48           | 0.0001             |
| 49           | 0.0001             |
| 50           | 0.0001             |

Scatter plot showing accident frequency versus aircraft age. The y-axis is labeled 'accident frequency' and ranges from 0.0000 to 0.0100. The x-axis is labeled 'aircraft age' and ranges from 0 to 50. The data points show a general downward trend, starting at approximately 0.0100 for age 0 and decreasing to near 0.0000 for ages 40 and above, with some fluctuations.

**Figure 2.1. FAA-NTSB data. The frequency of accidents varies with the age of the aircraft, but not in a linear way.**

An example of some of the data in the FAA-NTSB dataset is shown in Table 2.1. (Note that across all of our observations, N-number is not a unique identifier of an aircraft, because once an aircraft is deregistered, the same N-number can be used for a new aircraft.)

<sup>4</sup> Throughout this monograph, when we use the term "aircraft age," we actually mean the number of years since the FAA certificate was issued. This is an error as these two features are not the same. We discuss this matter further in Section 10.1.

**Table 2.1. A sample of information in the FAA-NTSB data. There is a separate line of data for each aircraft for each calendar year. For example, the second aircraft in the table will have eight lines in the data, from age 0 to age 7. ex is the exposure time (the proportion of the calendar year during which the aircraft was operated). num\_cl is the number of claims (none of these records was matched to an accident on the NTSB data).**

| n_number | city         | aircraft<br>make | aircraft<br>age (years) | ex   | num_cl |
|----------|--------------|------------------|-------------------------|------|--------|
| N106K    | KONAWA       | BEECH            | 25                      | 1.00 | 0      |
| N64882   | GREELEY      | CESSNA           | 7                       | 1.00 | 0      |
| N6407    | ASHEBORO     | HILLER           | 36                      | 1.00 | 0      |
| N6644V   | COLLEYVILLE  | BELLANCA         | 5                       | 0.66 | 0      |
| N9271W   | SOUTH RIDING | PIPER            | 11                      | 1.00 | 0      |

Finally, we note that for the purpose of quicker fitting of our models, we used only a 25% random sample of this dataset.

## 2.2. Road Accident Frequency Model

In the UK, the police maintain a record of every road traffic accident involving injury which they attend. The dataset is known as STATS19, and the UK government makes it available for download in order to encourage research into road safety. It is (much more) conveniently available through an R data package called stats19 (see Lovelace et al. 2019) available on CRAN.<sup>5</sup> We summarized this data by geographic region and added some fields from the UK census which provide sociodemographic features. Our aim will be to build a model which predicts the probability of road traffic accidents in a given region.<sup>6</sup>

The data preparation process led to this dataset including many highly correlated variables. Table 2.2 shows examples of some of the high negative correlations. We will see that this presents practical difficulties when we try to fit a model.

<sup>5</sup> <https://cran.r-project.org/web/packages/stats19/index.html>

<sup>6</sup> Such a model may be useful in helping to target road safety programs and expenditure.

**Table 2.2. Some of the high negative correlations present in the road traffic accident data. The meanings of some key variables in this dataset will be explained as we progress through this case study (see the footnote for an example).**

| variable 1            | variable 2           | cor   |
|-----------------------|----------------------|-------|
| c_ts011_hhd_0_pct     | c_ts011_hhd_3_pct    | −0.86 |
| c_ts002_mcp_never_pct | c_ts002_mcp_mrcp_pct | −0.92 |
| c_ts002_mcp_never_pct | c_ts002_mcp_m_pct    | −0.92 |
| c_ts002_mcp_never_pct | c_ts002_mcp_mos_pct  | −0.92 |
| c_ts011_hhd_0_pct     | c_ts011_hhd_2_pct    | −0.95 |
| c_ts004_cob_uk_pct    | c_ts004_cob_oth_pct  | −0.96 |

## 2.3. Simulated Data—Auto Insurance

We have simulated data to imitate some aspects of frequency rating for auto insurance.

When simulating the data, we decide in advance what the true underlying frequencies will be. For example, we can decide that the starting point will be a frequency of 5% and that risk is increased by 4.65 times for a 17-year-old male and 2.55 times for a 17-year-old female. We call these true underlying frequencies and relativities the "ground truth." As part of our work on case studies using real data, we will be choosing performance metrics to measure model quality. It is not always obvious what a good or bad value is for a performance metric, and we will use these data to illustrate the values we might typically expect.

## 2.4. The Challenges

### 2.4.1. High cardinality categorical variables (HCCVs)

In the FAA-NTSB dataset, the rating factor "make of aircraft" (Cessna, Piper, Beech, etc.) is a categorical variable. It divides our data into groups or categories, and these groups do not have a natural order or ranking. The CAS GLM monograph explains that when using a GLM (not penalized), the prediction for any category is the average claims experience for that category. There are many different makes of aircraft, and given the overall moderate size of the dataset there may be some makes which have no accidents in our data. If we include aircraft make as one of our rating factors, then our model will predict a frequency of 0% for such makes. This is not a reasonable prediction. Also,

<sup>1</sup> As an example, `c_ts002_mcp_never_pct` and `c_ts002_mcp_mrcp_pct` both address marital and civil partnership status. The former is the percent of the population in a region who were never married and never registered a civil partnership, and the latter is the percent of the population who are married or in a registered civil partnership. We clearly expect these to be negatively correlated.

any category which does not have sufficient data for the observed claims frequency to be sufficiently credible will potentially have a predicted claims frequency which is much too high or much too low. In addition to unreliable predictions, we will see that in certain approaches to modeling, including a categorical variable with many features will lead to significant computational complexity.

Categorical variables with a large number of levels, to the extent that they lead to the type of problem above (given the size dataset being used), are known as high cardinality categorical variables (HCCV), and we will discuss how to deal with the challenges that they present.

### **2.4.2. *Combining other models with a GLM***

In our FAA-NTSB data, we want to end up with a rate for each make of aircraft. As discussed above, the make of the aircraft is an HCCV. Some techniques used for dealing with HCCVs are quite different from GLMs and are most easily done in a separate exercise. One approach therefore is to do some initial modeling with the GLM, but then to leave the GLM behind and do some further modeling, and finally to combine our non-GLM modeling back into the GLM. Even where HCCV modeling of make and model of aircraft can be done within the framework of one single GLM, we may wish as a second stage to adjust the rates based on underwriter or other input. In such cases, we will need to integrate our changes back into the GLM.

Geospatial smoothing (something we might want to do whenever we think that the level of risk depends on location) presents a similar issue. A GLM cannot directly do geospatial smoothing. We may therefore wish to start off with some GLM modeling, once again leave the GLM behind and fit a different type of model, and finally combine the results back with the GLM.

Another example is credit modeling. In a rating plan, the rates might depend on features related to an individual's credit rating. We have a choice; we can include all the credit-related features in the main model, or we can create a separate "credit score" model and use the score as a feature in the main model. Separate credit score modeling has various advantages. For transparency, we might want to know the total impact that credit-related features have on the rate, and this is very easy to know if a credit score is used. In addition, score variables, such as credit, group records in ways that might not otherwise be obvious from the underlying features. This allows for parsimony; the main model can use fewer features. In addition, it allows us to more easily discover and estimate interactions, since there might be strong interactions with the credit score that are not apparent with the individual components of the credit score.

### **2.4.3. "Controlling" for certain features**

In our case studies and other examples, we will sometimes need to isolate the effect of one or more features on a target variable. Once we know the effect, we might need to ignore it (if it is a disallowed rating feature) or adjust it. We will discuss various approaches and their impact on the final rates.

### **2.4.4. Highly correlated variables**

Goldburd et al. (2025) Section 2.9 explains that when the correlation between any two features is large, the coefficients fitted by a GLM can swing wildly in response to small changes in the data, and the standard errors associated with those coefficients will become large. They propose two approaches to dealing with this; removing all but one of any group of highly correlated predictors and preprocessing with principal component analysis (PCA) or similar techniques. We will encounter highly correlated features in one of our case studies and will use the opportunity to discuss the challenges posed by highly correlated features more broadly and to look at the possibility of using penalized regression to resolve them.

## **2.5. Next Steps**

We have now seen the aims of our case studies—essentially in each case to build the best frequency model that we can given any constraints. We also understand some of the challenges that we will face. However, before we start modeling we need to think about performance measurement—and we look at that in the next chapter.
