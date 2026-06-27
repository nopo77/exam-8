---
paper: mahler
chapter: 2
title: 2. CREDIBILITY AND EXPERIENCE RATING
topics: [credibility_formula, experience_rating, shifting_parameters, prior_estimate]
key_formulas: [credibility_weighted_estimate]
---

> **TL;DR**
> - Standard credibility formula: New Estimate = Data × Z + Prior Estimate × (1−Z).
> - Prior estimate is typically the class average; can also be a previous risk-specific estimate.
> - When risk parameters shift over time, older data should receive substantially less credibility.
> - May be only minimal efficiency gain from additional years of data when shifting is significant.

## 2. CREDIBILITY AND EXPERIENCE RATING

Experience rating and merit rating modify an individual insured's rate above or below average. From an actuarial standpoint, the experience rating plan is using the observed loss experience of an individual insured in order to help predict the future loss experience of that insured. Usually this can be written in the form:

$$\begin{aligned} \text{New Estimate} = & (\text{Data}) \times (\text{Credibility}) \\ & + (\text{Prior Estimate}) \times (\text{Complement of Credibility}) \end{aligned}$$

For most experience rating plans, the prior estimate is the class average. However, in theory the prior estimate could be a previous estimate of the loss potential of this insured relative to the class average. This paper will treat both possibilities.

## 2.1 *Shifting Parameters Over Time*

There are many features of experience rating plans that are worthy of study by actuaries. Meyers [1], Venter [2], Gillam [3], and Mahler [4] present examples of recent work. The example in this paper will deal with only one aspect, that is, how to best combine the different years of past data.

The author, in a previous paper [5], came to the following conclusion concerning this point:

“When there are shifting parameters over time, older years of data should be given substantially less credibility than more recent years of data. There may be only a minimal gain in efficiency<sup>1</sup> from using additional years of data.”

