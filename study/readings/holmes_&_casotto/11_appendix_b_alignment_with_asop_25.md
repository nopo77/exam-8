---
paper: holmes_&_casotto
chapter: B
title: Alignment of Lasso Credibility with ASOP 25
topics: [asop_25, relevant_experience, credibility_procedure_definition, professional_judgment, complement_of_credibility]
key_formulas: []
---

> **TL;DR**
> - Lasso credibility satisfies ASOP 25's definition of a credibility procedure: it blends subject experience (modeling data) with relevant experience (the offset complement).
> - Default complement (1.0 relativity) satisfies ASOP 25 §3.3 selection criteria for most models when no prior knowledge of a variable's effect exists.
> - Non-default complement (e.g., countrywide model as offset): assess whether subject data is a material portion of the relevant experience to avoid circular credibility.
> - λ (penalty parameter) functions like Bühlmann k in blending subject and relevant experience; upward adjustment of λ reflects ASOP 25 §3.4 professional judgment toward a more conservative model.
> - ASOP 25 considerations for complement selection apply unchanged from other credibility procedures; additional expertise in penalized regression is needed for judgment calls about λ.

# Appendix B. Alignment of Lasso Credibility with ASOP 25

Lasso credibility is a new technique, but it aligns with the existing considerations in Actuarial Standard of Practice No. 25, *Credibility Procedures*. In this appendix, we spend time detailing that alignment. First, we introduce how the existing terminology of ASOP 25 can be applied when using the default complement in lasso credibility. Then, we confirm that lasso credibility is in ASOP 25's defined scope and show that lasso credibility has all of the characteristics of an actuarially sound credibility procedure. Finally, this section will confirm that these conclusions hold when the selected complement of credibility is applied through the offset and differs from the default assumption of lasso credibility.

## B.1. Definitions: Default Complement of Lasso Credibility

Our first consideration is to verify that penalized regression is a credibility procedure by definition. Note that for the purposes of discussion, in this appendix the displayed text comes from the relevant sections of ASOP 25.

## *2.2 Credibility Procedure*

*A process that involves the following:*

- a. The evaluation of subject experience for potential use in setting assumptions without reference to other data; or*
- b. The identification of relevant experience and the selection and implementation of a method for blending the relevant experience with the subject experience.*

When using the default complement of credibility (no offset), we define the above-mentioned terminology as follows:

- **Relevant experience:** the overall average relativity of a particular segment
- **Subject experience:** the experienced relativity of a particular segment
- **A method for blending the relevant and subject experience:** the penalized regression framework through the application of a penalty while maximizing the likelihood during the fitting process

Therefore, lasso credibility is a *credibility procedure* under ASOP 25’s definition of the term.

## B.2. Considerations and Scope of ASOP 25

Now let’s look at Section 1.2.c of ASOP 25 to confirm that penalized regression is within the scope set out by ASOP 25.

*This Standard applies to actuaries when performing actuarial services involving credibility procedures in the following situations:*

*[ . . . ]*

*c. When the actuary is blending or considering blending subject experience with other experience; [ . . . ]*

As lasso credibility is a credibility procedure and we are blending the subject experience with other relevant experience, it is within the scope of ASOP 25. Having determined that lasso credibility is within the standard’s scope, we should now further scrutinize the application of the default complement of credibility to make sure our relevant experience satisfies the other considerations of ASOP 25.

## 2.4 Relevant Experience

*Sets of data, that include data other than the subject experience, that, in the actuary’s judgment, are predictive of the parameter under study (including but not limited to loss ratios, claims, mortality, payment patterns, persistency, or expenses). Relevant experience may include subject experience as a subset.*

When modeling using our simulated countrywide data, we assume we have no prior knowledge for the risk relativities of the variables we include in our model. Therefore, a 1.0 relativity (there is no relationship between the characteristic and true risk) is appropriate. In general, the 1.0 assumption will be valid in the absence of other information.

The text of ASOP 25’s Section 3.3, “Selection of Relevant Experience,” can be split into four main points.

*The actuary should use care in selecting the relevant experience.*

This first section is the most important. Below, we make generalizations that are appropriate for most modeling exercises. However, data, projects, and models will always have at least one uniqueness that will require special treatment. Please treat the guidance below as guidance for a “normal” project, and take care to identify situations that might require exceptions to these generalities. We continue to assume for now that we have no prior knowledge about the variable being evaluated.

Moving on to the second point:

*Such relevant experience should have characteristics similar to the subject experience. Characteristics to consider include items such as demographics, coverages, frequency, severity, or other determinable risk characteristics that the actuary expects to be similar to the subject experience. If the proposed relevant experience does not meet and cannot be adjusted to meet such criteria, it should not be used.*

Satisfying this requirement relies on the assumption that we have no prior knowledge for a particular characteristic and that our data is sufficiently homogeneous to be modeled together in the first place. Let’s look at the next point:

*The actuary should apply credibility procedures that appropriately consider the characteristics of both the subject experience and the relevant experience.*

The blending of subject and relevant experience in penalized regression is determined by the penalty parameter. The penalty parameter behaves similarly to Bühlmann credibility’s  $k$  parameter as demonstrated in Appendix A. We suggest that if a model fitted through the maximization of likelihood is appropriate for this analysis, then a lasso credibility approach is an appropriate method of blending the subject and relevant experience. Now, to the fourth point:

*The actuary should consider the extent to which subject experience is included in relevant experience. If subject experience data is a material part of relevant experience, the use of that relevant experience may not be appropriate. In some instances, no relevant experience is available to the actuary. In this situation, the actuary should exercise professional judgment, considering available subject experience, in setting an estimate of expected values.*

The goal of this consideration is to ensure that the complement of credibility is not self-deterministic. For example, if the subject experience is 80% of the relevant experience, and the subject and relevant experience are given 50% weight each, we are really giving 90% of the credibility to the subject experience.

The model structure when using the default complement of credibility will automatically fulfill these considerations as the selected complement is not influenced at all by our modeling data. The “null relativity” assumption for categorical and ordinal variables is truly independent of our subject experience. This consideration will be highly material only when applying a selected nondefault complement of credibility through the use of an offset.

We discuss one more item before moving on, ASOP 25’s Section 3.2.c.

*The actuary should use an appropriate credibility procedure when determining if the subject experience is fully credible or when blending the subject experience with relevant experience. The procedure selected or developed may be different for different practice areas and applications. Additional review may be necessary to satisfy applicable law.*

*In selecting or developing a credibility procedure, the actuary should consider the following criteria:*

*[. . .]*

*c. whether the procedure is practical to implement while taking into consideration both the cost and benefit of employing a procedure.*

The use of penalized regression carries additional computation cost. The time required to fit an individual penalized regression model with a fixed penalty value is quite similar to that needed for an equivalent unpenalized GLM. The computation cost of penalized regression increases because of the need to test various penalty parameters in a cross-validation routine. Such time can be costly on very large data sets, but the ubiquity of cloud computing has made penalized regression more accessible on data sets of all sizes.

The preceding sections justify that the default assumptions of lasso credibility are appropriate for a “normal” actuarial loss model when there is no prior knowledge about a given variable. In the next section, we explore how ASOP 25 applies when using a different complement in lasso credibility.

## B.3. Alternate Complements in Lasso Credibility

When using a nondefault complement of credibility, as in the case study, we need to realign our terminology with that of ASOP No. 25. That alignment is the same as earlier with the exception of our relevant experience, which we define as follows:

- **Relevant experience:** relativities produced by our lasso credibility model on the full countrywide data set

Therefore we revisit only ASOP 25's guidance relating to selection of relevant experience.

## 2.4 Relevant Experience

*Sets of data, that include data other than the subject experience, that, in the actuary's judgment, are predictive of the parameter under study (including but not limited to loss ratios, claims, mortality, payment patterns, persistency, or expenses). Relevant experience may include subject experience as a subset.*

In our case study we assumed that the countrywide data is similar enough to individual states for the countrywide model to be used as a complement. In the case study, the relevant experience does include the subject experience as a subset.

Section 3.3, "Selection of Relevant Experience," has additional considerations for relevant experience that are satisfied through the selection of current rates or a countrywide model as an offset for a state-specific model.

*The actuary should use care in selecting the relevant experience. . . . Such relevant experience should have characteristics similar to the subject experience. Characteristics to consider include items such as demographics, coverages, frequency, severity, or other determinable risk characteristics that the actuary expects to be similar to the subject experience. If the proposed relevant experience does not meet and cannot be adjusted to meet such criteria, it should not be used.*

Now to the next relevant point of ASOP 3.3:

*The actuary should consider the extent to which subject experience is included in relevant experience. If subject experience data is a material part of relevant experience, the use of that relevant experience may not be appropriate.*

*In some instances, no relevant experience is available to the actuary. In this situation, the actuary should exercise professional judgment, considering available subject experience, in setting an estimate of expected values.*

Previously, this consideration did not require significant attention as the “null” complement was not related to our subject experience. Now, actuaries should take care to understand the potential influence of their modeling data on the selected complement of credibility. If industry rates or competitor rates are selected, it is unlikely or impossible that the modeling data is a material subset of the selected complement. In our example, the large state data is a subset of the full modeling data set and did have an influence on the creation of the complement of credibility. For our example, we assumed it did not have undue influence. In practice, an actuary should more thoroughly consider the data’s influence on the selected complement.

## **B.4. Lasso Credibility and ASOP 25 Summary**

Lasso credibility meets the definition of an actuarial credibility procedure, and the considerations of ASOP 25 should be directly applied when using this methodology. Considerations for the selection of a complement of credibility are not changed when using lasso credibility instead of a different credibility procedure. However, the application of professional judgment in lasso credibility requires both industry knowledge as well as knowledge of penalized regression. This application of judgment in lasso credibility will be most common in the adjustment of the lambda penalty parameter.

