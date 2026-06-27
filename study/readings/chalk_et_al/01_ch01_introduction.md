---
paper: chalk_et_al
chapter: 1
title: Introduction
topics: [glm_rating_plans, penalized_regression, high_cardinality_categorical_variables, two_stage_modeling, correlated_variables, model_validation, feature_selection]
key_formulas: []
---

> **TL;DR**
> - Chalk et al. is a practical companion to Goldburd et al., demonstrating GLM challenges via three case studies (FAA-NTSB aviation accidents, UK road accidents, simulated auto insurance).
> - Four key practical challenges: HCCVs, combining non-GLM models with a GLM, controlling for disallowed features, and highly correlated variables.
> - Penalized regression (LASSO/elastic net) is the central framework throughout — the authors strongly advocate using it over unpenalized GLMs.
> - Revisits core topics from Goldburd et al.: performance measurement, train/test splitting, and handling nonlinear effects.
> - Human review remains essential even when automated techniques reduce manual modeling steps.

# 1. Introduction

## 1.1. Objectives

The CAS monograph *Generalized Linear Models for Insurance Ratings* by Goldburd et al. (2025) is a comprehensive guide to creating insurance rating plans with generalized linear models (GLMs). It covers the technical foundations of GLMs and practical topics, such as the model-building process, data preparation, selection of model form, model refinement, and model validation.

This monograph assumes that the reader is familiar with Goldburd et al. (2025)<sup>1</sup> and uses case studies to focus on various practical challenges in building GLMs. Many of these challenges, along with suggested solutions, have been mentioned in the CAS GLM monograph. Here, we expand on and demonstrate these solutions using the case studies and discuss some additional practical challenges.

These practical challenges (which will be explained in more detail later on) include:

- Dealing with high cardinality categorical variables (HCCVs).
- Dealing with situations where part of the rating plan has to be calculated separately from the main GLM (for example, geographical analysis). In these situations, we may need to add back to our GLM the results of the separate analysis and then do further GLM-based work.
- Removing from a GLM the effect of variables we are not permitted to use or that we do not want to use. Here we will have to consider whether we allow ourselves to use variables that are correlated with the forbidden variable.
- Dealing with highly correlated variables.

The case studies will require us to revisit various basic ideas discussed in the CAS GLM monograph, including:

- How to measure model performance.
- Splitting the data into training and test sets.
- Dealing with nonlinear effects.

---

<sup>1</sup> ...and with the relevant chapters of *An Introduction to Statistical Learning* (James et al. (2021)).

Penalized regression is an approach to fitting GLMs that is impossible to ignore. Section 10 of Goldburd et al. (2025) discusses it and mentions that the main disadvantage is that it is "much more computationally complex than standard GLMs." On the other hand, the advantages of using it are significant. The reader will see throughout the text that it is easy within the penalized regression framework to ensure that models are not overfitted and therefore perform well on future data (it will also make our life much easier when we develop the case studies). Regarding the issue of computational complexity, while this can be an issue, significant computing power is easily available to us today, either with high-specification machines running locally or in the cloud. Open-source software exists that fits GLMs (and other models) on datasets which are too large to fit into memory. For those who prefer not to write, debug, and maintain code, proprietary software exists that makes it very easy to fit good penalized GLMs. Overall then, we really have no excuse not to use penalized regression. We devote one chapter to reviewing its basic ideas and some theory before applying it in subsequent chapters. Many of the practical concepts above apply equally well whether one uses GLMs with or without penalization. (The relevant R or Python code is also fairly similar.) Therefore, the determined reader who wishes to remain in the "without penalization" world will be easily able to do so.

One word of warning: we discuss methods in this paper that seem automatic and to reduce the level of human input in model training in general and in the setting of insurance rating plans in particular. The reality is that most of the time, these methods simply allow the practitioner to make more informed choices and avoid certain pitfalls. The potential negative consequences of mindlessly creating rating plans without human input and review remain as large now as they ever have been.
