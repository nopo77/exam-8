---
paper: holmes_&_casotto
chapter: 5
title: Lasso Credibility
topics: [lasso_credibility, offset_as_complement, ordinal_variables, complement_of_credibility, asop_25, penalty_parameter]
key_formulas: [lasso_credibility_decomposition, credibility_weighted_coefficient_with_offset]
---

> **TL;DR**
> - Lasso credibility = lasso penalized regression + offset encoding the complement of credibility; the model estimates credible *deviations from* the complement rather than raw coefficients.
> - Key identity: Total coefficient = β_offset + β_lasso, where β_lasso → 0 as λ → ∞ (full credibility to complement) and β_lasso → β_GLM − β_offset as λ → 0 (full credibility to data).
> - Ordinal variable treatment converts continuous variables into stepwise indicators so all coefficients represent magnitude (not slope), enabling intuitive credibility interpretation at each step.
> - Complement examples: prior rating plan, countrywide model, competitor relativities, industry relativities, or 1.0 (default — use only when no substantive prior knowledge exists).
> - When using the default 1.0 complement for all variables, call it "lasso penalized regression," not "lasso credibility."
> - ASOP 25 applies: offset = relevant experience; modeling data = subject experience; λ acts as the credibility parameter analogous to Bühlmann's k.

# 5. Lasso Credibility

We have identified penalized regression as a credibility procedure where the complement of credibility is a null coefficient  $\beta = 0$ . This complement of credibility coincides with the null hypothesis in  $p$ -value testing. The next logical step is to enhance this procedure by using a more appropriate complement of credibility than  $\beta = 0$  for all  $\beta$ .

Implementing such a credibility procedure has three requirements: an **offset** representing the complement of credibility, an **ordinal** or **categorical** treatment of all variables, and the **use of penalized regression** as the credibility procedure. This methodology is best applied through lasso penalization instead of ridge or elastic net, and we will refer to it as **lasso credibility**.

## 5.1. The Offset: Applying a Complement in Lasso Credibility

In actuarial modeling, the offset has traditionally been reserved for the application of weights as well as deductibles, limits, or other rating relativities that are best selected outside of a GLM. The reader can find a comprehensive overview of the applications of offsetting in Yan et al. (2009). When applied to GLMs and traditional penalized regression, an offset is normally included without a corresponding predictor variable.

The mathematical definition of an offset is a fixed column of coefficients that contributes to the linear component  $X\beta$  of a GLM or penalized regression:

$$\eta = g(\mu) = \beta_0 + X\beta + \text{offset}.$$

Consider the example in Section 4.5, where we wanted to incorporate a complement of credibility of 1.1 to the fire extinguisher variable.

Lasso credibility implements such a complement of credibility via a new application of the offset. In lasso credibility (as opposed to GLMs or traditional penalized regression) it is necessary to **include both an offset as well as the predictor variable for the same rating characteristic**.

The model's prediction can be stated as

$$\begin{aligned}\log(\mu) &= \log(\text{Prediction}) = \beta_0 + \text{offset} + \beta_1 X_1 + \beta_2 X_2 \\ &= \beta_0 + \beta_{1 \text{ offset}} X_1 + \beta_{2 \text{ offset}} X_2 + \beta_1 X_1 + \beta_2 X_2 \\ &= \beta_0 + (\beta_{1 \text{ offset}} + \beta_1) X_1 + (\beta_{2 \text{ offset}} + \beta_2) X_2.\end{aligned}\quad (5.1)$$

We see that the coefficients of the model can be decomposed into two components:

- The **fixed** component  $\beta_{j,\text{offset}}$  fully determined by the modeler's assumption
- The **variable** component  $\beta_j$ , determined by the data and the methodology (GLM or penalized GLM).

**Fitting this model as a GLM with or without an offset will yield the exact same predictions because of the GLM's assumption of full credibility** (see Section A.1). If the offset is not included, the GLM will output the best  $\beta_j$  to maximize the likelihood in the optimization process. We call this  $\beta_{j,\text{glm}}$ . If an offset is included, the GLM will output a  $\beta_j$  such that

$$\beta_{j,\text{offset}} + \beta_j = \beta_{j,\text{glm}}$$

and the likelihood is again maximized. The accompanying code for Chapter 7's case study contains an example of a GLM with and without offsets producing the exact same predictions.

## 5.2. Ordinal Variables

Ordinal variables, like categorical variables, represent **magnitude**; continuous variables, on the other hand, represent **slope**. By representing every variable in the model as ordinal or categorical, all of the resulting coefficients represent a **magnitude** of change. That magnitude is consistent with traditional credibility approaches, and therefore actuarial judgment and the considerations of ASOP 25 are easy to apply. Additionally, by using an ordinal treatment of variables, lasso credibility can also automatically identify deviations from the selected complement of credibility without additional feature engineering.

By treating a continuous variable as a stepwise ordinal variable (one step for every driver age, for example), a lasso credibility model has the ability to identify the **magnitude** of a credible difference from the complement at any step. It is by chaining these ordinal steps together that lasso credibility can fit complex and unknown deviations from a complement of credibility. Those steps without a credible difference are automatically removed when using lasso penalization, while steps with a credible difference are included. It is recommended that ordinal steps be sufficiently granular to not inappropriately pregroup levels of a given characteristic.

## 5.3. Lasso Credibility as a Credibility-Weighted GLM

We now focus on how penalized regression can be leveraged to find solutions that are trade-offs between the complement of credibility (here  $\beta_{\text{offset}}$ ) and the observed data (in this case  $\beta_{\text{glm}}$ ).

Suppose that we are building a lasso regression model, with penalty level  $\lambda$ , with the following prediction structure:

$$\text{Prediction} = \exp\left(\beta_0 + (\beta_{1,\text{offset}} + \beta_1)x_1 + (\beta_{2,\text{offset}} + \beta_2)x_2 + \cdots\right).$$

When  $\lambda = 0$  (hence no penalization is used), the offset and modeled coefficients will sum to the unpenalized GLM coefficient as the coefficient will be given full credibility:

$$\begin{aligned}\text{Unpenalized coefficient} &= \beta_{j,\text{offset}} + \beta_j \\ &= \beta_{j,\text{glm}}\end{aligned}$$

When  $\lambda$  is sufficiently high ( $\lambda \gg 0$ ), all variable components  $\beta_j$  will be removed from the model and our indicated coefficient will be  $\beta_{j,\text{offset}}$ :

$$\begin{aligned}\text{Fully penalized coefficient} &= \beta_{j,\text{offset}} + \beta_j \\ &= \beta_{j,\text{offset}} + 0 \\ &= \beta_{j,\text{offset}}\end{aligned}$$

As demonstrated in Section 3.1.3, the coefficient of a penalized regression model moves from a GLM coefficient to zero as the penalty term moves from zero to a sufficiently high number. In lasso credibility, we cannot separate the modeled coefficient from its accompanying offset. The graph in Figure 5.1 shows the paths of the combined offset and modeled coefficients in lasso credibility. Rather than shrinking to zero, our coefficient estimates collapse to our offset complement of credibility.

Therefore, for a general value of  $\lambda$ :<sup>6</sup>

$$\begin{aligned}\beta_{j,\text{offset}} &\leq \beta_{j,\text{offset}} + \beta_{j,\text{lasso}} \leq \beta_{j,\text{glm}} && \text{if } \beta_{j,\text{offset}} \leq \beta_{j,\text{glm}} \\ \beta_{j,\text{offset}} &\geq \beta_{j,\text{offset}} + \beta_{j,\text{lasso}} \geq \beta_{j,\text{glm}} && \text{if } \beta_{j,\text{offset}} \geq \beta_{j,\text{glm}}\end{aligned}$$

It follows that lasso credibility behaves as we would expect from a credibility procedure and there exists a  $Z$  such that

$$\text{Coefficient}_j = (\beta_{j,\text{offset}} + \beta_j) = Z \times (\beta_{j,\text{glm}}) + (1 - Z) \times (\beta_{j,\text{offset}})$$

In this section, we have provided the intuition behind and practical effect of the relationship between penalized regression and credibility. In Appendix A we formalize this intuition and prove that penalized regression is a sound mathematical credibility procedure. Both Bühlmann credibility and penalized regression can be seen as examples of Bayesian estimation. Under a Bayesian interpretation, the connection between the two methodologies is evident. For the scope of this introduction, the reader can take for granted that penalized regression is a sound framework for applying credibility in a multivariate setting.

<sup>6</sup> The inequality is presented for illustrative purposes, and although it will hold in many situations, there are cases where it will not. In general, it will not hold when the coefficient will change sign through the coefficient path, which happens under high correlation. A comprehensive description of how the coefficient may change sign with varying  $\lambda$  can be found in Efron et al. (2004).

**Figure 5.1. When Coefficients Collapse to Zero, the True Effect of the Variable Collapses to the Offset**

Lasso coefficient path with offset

![Figure 5.1: Lasso coefficient path with offset. The graph shows the relationship between the Lasso coefficient path (solid lines) and the complement (offset) (dotted lines) as a function of ln λ. The x-axis represents ln λ, ranging from -9 to -6. The y-axis represents the Coefficients, ranging from -0.2 to 0.4. There are four pairs of lines: a green pair starting at approximately 0.38 and 0.2, a blue pair starting at approximately 0.2 and 0.05, a purple pair starting at approximately 0.05 and 0, and a red pair starting at approximately -0.25 and -0.1. As ln λ increases, the solid lines (Coefficients + offset) decrease and eventually collapse to the dotted lines (Complement (offset)).](2d62ff2bded0c21414a0f40fdf8fd537_img.jpg)

Figure 5.1: Lasso coefficient path with offset. The graph shows the relationship between the Lasso coefficient path (solid lines) and the complement (offset) (dotted lines) as a function of ln λ. The x-axis represents ln λ, ranging from -9 to -6. The y-axis represents the Coefficients, ranging from -0.2 to 0.4. There are four pairs of lines: a green pair starting at approximately 0.38 and 0.2, a blue pair starting at approximately 0.2 and 0.05, a purple pair starting at approximately 0.05 and 0, and a red pair starting at approximately -0.25 and -0.1. As ln λ increases, the solid lines (Coefficients + offset) decrease and eventually collapse to the dotted lines (Complement (offset)).

## 5.4. Terminology and ASOP 25

The terms in bold below are defined generally in ASOP 25’s Section 2, “Definitions”—the definitions we provide in this list are meant to clarify how we apply the terms in the monograph going forward:

- **Risk characteristics:** the characteristics of the risk represented by our predictor variables
- **Risk classification system:** assignment of risks to groups based on expected relativities determined by the lasso’s penalized regression procedure, which blends the chosen complement of credibility with the credible difference found in the subject experience
- **Subject experience:** experienced relativities in the modeling data set
- **Relevant experience:** the selected offset relativities *or* a 1.0 relativity
- **Credibility procedure:** lasso credibility (penalized regression)

Appendix B contains a more extensive description of penalized regression as a credibility procedure through the lens of ASOP 25. Possible complements of credibility will fulfill the requirements of ASOP 25’s Section 3.3, “Selection of Relevant Experience.” Additional guidance can be found in Boor (1996). Here are some examples of complements of credibility when using lasso credibility for a pure premium loss model:

- A 1.0 relativity (lasso credibility’s default assumption)
- A prior loss model’s relativities
- A countrywide loss model that includes the data being modeled as a small subset
- An existing rating plan
- Competitor relativities
- Industry relativities

If all variables use the default assumption, we would refer to the model as lasso penalized regression instead of lasso credibility. We can use this 1.0 assumption in lasso credibility by including no complement where there is no prior knowledge of a variable's effect on risk and including an appropriate complement for other variables where such knowledge exists.

## 5.5. Selecting and Evaluating a Penalty Parameter in Lasso Credibility

In lasso credibility, one can select a penalty parameter using the methodology described in Section 3.3. An actuary can reframe this process as testing the level of credibility that generalizes the best test statistic across the data set for all  $\beta$ . As before, cross-validation will select a single  $\lambda$  value, and the variation in optimal values of  $\lambda$  between model folds allows a modeler to make a credibility selection that deviates from this point estimate. This expert judgment applied when selecting a penalty parameter in lasso credibility is supported both through cross-validation statistical support as well as the considerations in ASOP 25's Section 3.4.

Here are some examples of an appropriate judgmental increase of the penalty parameter:

- If the complement of credibility consists of the current factors, the increase of the penalty parameter can be used as a methodology to select between current and indicated to mitigate policyholder impacts.
- If the model factors are showing instability, the penalty can be increased to provide additional stability. This is most common on small data sets or when using techniques like derivative lasso (Casotto and Holmes 2023) and AGLM (Fujita et al. 2020) that use penalization to create ordinal variable factor curves.
- If modeling data is adjusted for trend or incurred but not reported (IBNR) claims, or if case reserves are based on generic estimates, the volatility of the data may be understated. In this case, an increase of the penalty parameter may be appropriate to avoid overestimating the credibility of the modeling data.
- The increase is warranted if the modeler believes the selection produces a more actuarially appropriate model given all information available.

While cross-validation produces a statistical range of appropriate penalty terms both higher and lower than the best estimate, it is generally actuarial best practice to select only values of lambda higher than the point estimate. Such a higher estimate will be more conservative and is similar to selecting “between current and indicated” when using traditional actuarial methodologies. It is uncommon but supportable to decrease the penalty parameter using actuarial judgment. This may be appropriate in the following situations:

- When pricing a line of business where the complement is known to have some deficiencies

- When there is a known change of significant magnitude from the selected complement of credibility
- If the relevant experience is from an older or more out of date source and the actuary wants to give greater weight to the more recent subject experience

For additional considerations in adjusting the penalty parameter, refer to ASOP 25's Section 3.4, "Professional Judgment."

## 5.6. Calculating Indicated Rates in Lasso Credibility

Let's return again to our two-variable homeowners model. In this example, we are refitting the two-variable homeowners model using an old model's factor table output as a complement of credibility. We will rearrange the equation for our model predictions as we did in Equation 5.1:

$$\begin{aligned}\text{Prediction} &= \exp\left(\beta_0 + \log(\text{offset factors}) + \beta_1 X_1 + \beta_2 X_2\right) \\ &= \exp\left(\beta_0 + \beta_{1 \text{ offset}} X_1 + \beta_{2 \text{ offset}} X_2 + \beta_1 X_1 + \beta_2 X_2\right) \\ &= \exp\left(\beta_0 + (\beta_{1 \text{ offset}} + \beta_1) X_1 + (\beta_{2 \text{ offset}} + \beta_2) X_2\right)\end{aligned}$$

As a reminder, these are the coefficients from our prior model that we are using as a complement of credibility:

$$\beta_{1 \text{ offset}} = 0.182$$

$$\beta_{2 \text{ offset}} = 0.01$$

For now, we will ignore the recommendation that ordinal variables be used in place of continuous variables in lasso credibility. Let's say our new model fits with these convenient coefficients:

$$\beta_0 = 4.6057$$

$$\beta_1 = -0.087$$

$$\beta_2 = 0.01$$

While  $\beta_1$  and  $\beta_2$  are the coefficients output from the model, the indicated coefficients will be  $(\beta_{1 \text{ offset}} + \beta_1)$  and  $(\beta_{2 \text{ offset}} + \beta_2)$ . The corresponding factor for not having a fire extinguisher would then be  $\exp((\beta_{1 \text{ offset}} + \beta_1)X_1)$ . If the coefficient  $\beta_1$  was penalized out of the model, the model is giving full credibility to the complement and the indicated coefficient would be  $\beta_{1 \text{ offset}}$ . In this case, the indicated relativity would be identical to our prior model.

Our new indicated rating tables would be calculated as follows:

**Base rate:**  $\exp(4.6057) = 100$ .

| Fire Extinguishers | Factor                                   |
|--------------------|------------------------------------------|
| No                 | $\exp((0.182 - 0.087) \times 1) = 1.100$ |
| Yes                | $\exp((0.182 - 0.087) \times 0) = 1.000$ |

  

| Age of Home | Factor                                  |
|-------------|-----------------------------------------|
| 0           | $\exp((0.01 + 0.01) \times 0) = 1.000$  |
| 1           | $\exp((0.01 + 0.01) \times 1) = 1.020$  |
| 2           | $\exp((0.01 + 0.01) \times 2) = 1.040$  |
| 3           | $\exp((0.01 + 0.01) \times 3) = 1.061$  |
| 4           | $\exp((0.01 + 0.01) \times 4) = 1.082$  |
| 5           | $\exp((0.01 + 0.01) \times 5) = 1.104$  |
| 6           | $\exp((0.01 + 0.01) \times 6) = 1.126$  |
| 7           | $\exp((0.01 + 0.01) \times 7) = 1.149$  |
| 8           | $\exp((0.01 + 0.01) \times 8) = 1.172$  |
| 9           | $\exp((0.01 + 0.01) \times 9) = 1.195$  |
| 10          | $\exp((0.01 + 0.01) \times 10) = 1.219$ |

This example's calculations are simple because our current and prior models had an identical parameterization. In practice, the prior model's parameterization may not be known or the complement may be based on post-modeling selected rates. Lasso credibility does not require the knowledge of prior parameterization as the decomposition of the linear equation generalizes in all cases when using **ordinal** variables.

When the link is logarithmic, each coefficient  $\beta_j$  has an equivalent factor representation as  $\exp(\beta_j)$ . In this case, it is more intuitive to think about the indicated relativities in terms of **factors** than **coefficients**. For each item in a rating table, we will calculate the new indicated relativity by multiplying the offset relativity by the corresponding factor  $\exp(\beta_j X_j)$  from the model. By Equation 5.1:

$$\begin{aligned}
 \text{Prediction} &= \exp(\beta_0 + \text{offset} + \beta_1 X_1 + \beta_2 X_2) \\
 &= \text{intercept} \times \text{offset factor} \times \text{fire extinguisher factor} \\
 &\quad \times \text{home age factor} \\
 &= \text{intercept} \times \text{extinguisher offset} \times \text{home age offset} \\
 &\quad \times \text{fire extinguisher factor} \times \text{home age factor}
 \end{aligned}$$

where

$$\text{Indicated fire extinguisher factor} = \text{extinguisher offset} \times \text{extinguisher indicated factor};$$

and

$$\text{Indicated home age factor} = \text{home age offset} \times \text{home age indicated factor}.$$

This generalization has important implications for variable transformations and the building of a lasso credibility model. In penalized regression or a GLM, we are modeling the relationship of variables to a target. However, in lasso credibility, we are instead modeling the credible differences between a complement of credibility and a target. This difference is part of why in the next chapter we recommend applying an ordinal treatment to any variable previously considered continuous.

## 5.7. Lasso Credibility Conclusions

Lasso credibility is a powerful technique that can be used to enhance penalized regression by using the offset to implement a complement of credibility. As we will see in Chapter 7's case study, this enhancement allows lasso credibility to be used on data sets that are too small to build either a GLM or lasso penalized regression model. Where a GLM would be unstable and lasso penalized regression would shrink too many variables to zero, lasso credibility can reflect credible signal where available and shrink volatile experience instead toward an appropriate complement relativity.

The statistical components of this methodology—lasso penalized regression, ordinal variables, and the offset—are not new. What we have introduced in this section is simply a shift in perspective to make full use of the credibility-based nature of penalized regression. As actuaries explore additional data science methodologies, we expect that similar perspective shifts will allow other known tools to be used in innovative and actuarially sound ways.

