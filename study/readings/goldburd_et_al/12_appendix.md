---
paper: goldburd_et_al
chapter: null
title: "Appendix"
topics: [working_residuals, working_weights, binned_residuals_derivation, homoscedasticity_proof]
key_formulas: [working_residual_formula, working_weight_formula, binned_working_residual_formula]
---
> **TL;DR**
> - Derives E(brb) = 0: binned working residuals are unbiased for any well-specified model
> - Derives Var(brb) = φm/SWW = constant: bins with equal sums of working weights are homoscedastic
> - Working weight wwᵢ = ωᵢ / (V(μᵢ) × [g′(μᵢ)]²); equal-weight bins ensure equal variance across all bins
> - Practical rule: choose m bins such that Var(brb) ≤ 0.01

# Appendix

In section 6.3.2, which discusses binned working residuals, we noted two properties that such residuals hold for a well-specified model, which makes them highly useful for performing residual analysis on models built from large datasets: (1) They follow no predictable pattern, as the mean of these residuals is always zero; and (2) they are homoscedastic, i.e., their variance is constant. In this appendix we show the derivation of these properties.

Given a model with  $n$  observations, let  $i = 1, \dots, n$  be the index of the observations. We divide the observations into  $m$  bins; let  $b = 1, \dots, m$  be the index of the bins.

Define *working residual* as

$$wr_i = (y_i - \mu_i) \cdot g'(\mu_i)$$

Define *working weight* as

$$ww_i = \frac{\omega_i}{V(\mu_i) \cdot [g'(\mu_i)]^2}$$

Define *binned working residual* as

$$br_b = \frac{\sum_{i \in b} wr_i \cdot ww_i}{\sum_{i \in b} ww_i}$$

We assign observations to bins such that all bins have equal sums of working weights, i.e.,  $\sum_{i \in b} ww_i = k$ . It follows that

$$\sum_{i=1}^n ww_i = SWW = m \cdot k \rightarrow k = \frac{SWW}{m}$$

For a properly specified model, the following holds:

$$E(y_i) = \mu_i,$$

$$Var(y_i) = \frac{\phi \cdot V(\mu_i)}{\omega_i},$$

$$E\left(\omega_i \frac{(y_i - \mu_i)}{V(\mu_i) g'(\mu_i)}\right) = 0.^1$$

**Property 1:**  $E(br_b) = 0$ .

$$\begin{aligned} E(br_b) &= E\left(\frac{\sum_{i \in b} w r_i \cdot w w_i}{\sum_{i \in b} w w_i}\right) \\ &= \frac{1}{k} E\left(\sum_{i \in b} w r_i \cdot w w_i\right) \\ &= \frac{1}{k} E\left(\frac{(y_i - \mu_i) \cdot g'(\mu_i) \cdot \omega_i}{V(\mu_i) \cdot [g'(\mu_i)]^2}\right) \\ &= \frac{1}{k} E\left(\omega_i \frac{(y_i - \mu_i)}{V(\mu_i) g'(\mu_i)}\right) = 0 \end{aligned}$$

**Property 2:**  $Var(br_b) = Constant = \frac{\phi \cdot m}{SWW}$

$$\begin{aligned} Var(br_b) &= Var\left(\frac{\sum_{i \in b} w r_i \cdot w w_i}{\sum_{i \in b} w w_i}\right) \\ &= \frac{1}{k^2} Var\left(\sum_{i \in b} w r_i \cdot w w_i\right) \end{aligned}$$

Assume that the working residuals are independent. Therefore,

$$\frac{1}{k^2} Var\left(\sum_{i \in b} w r_i \cdot w w_i\right) = \frac{1}{k^2} \sum_{i \in b} Var(w r_i \cdot w w_i)$$

Let's simplify the  $Var(w r_i \cdot w w_i)$  term:

$$Var(w r_i \cdot w w_i) = Var\left(\omega_i \frac{y_i - \mu_i}{V(\mu_i) \cdot g'(\mu_i)}\right)$$

---

<sup>1</sup> See Klinker (2011b), who demonstrates that  $\sum \omega_i \frac{(y_i - \mu_i)}{V(\mu_i) g'(\mu_i)} = 0$ , both over the entire GLM training data as well as over any subset with the same level of a categorical variable. In a well-fit model there is no predictable pattern in the residuals, and so the expected value  $E\left(\omega_i \frac{(y_i - \mu_i)}{V(\mu_i) g'(\mu_i)}\right) = 0$  for any individual observation as well.

$$\begin{aligned}
&= \frac{\omega_i^2}{V(\mu_i)^2 \cdot [g'(\mu_i)]^2} \text{Var}(y_i - \mu_i) \\
&= \frac{\omega_i^2}{V(\mu_i)^2 \cdot [g'(\mu_i)]^2} \text{Var}(y_i) \\
&= \frac{\omega_i^2}{V(\mu_i)^2 \cdot [g'(\mu_i)]^2} \cdot \frac{\phi V(\mu_i)}{\omega_i} \\
&= \frac{\omega_i \cdot \phi}{V(\mu_i) \cdot [g'(\mu_i)]^2} = \phi \cdot ww_i
\end{aligned}$$

Plugging this simplified term back into the original equation,

$$\begin{aligned}
\text{Var}(br_b) &= \frac{1}{k^2} \sum_{i \in b} \text{Var}(wr_i \cdot ww_i) = \frac{1}{k^2} \sum_{i \in b} \phi \cdot ww_i \\
&= \frac{\phi}{k^2} \sum_{i \in b} ww_i = \frac{\phi \cdot k}{k^2} = \frac{\phi}{k} = \frac{\phi \cdot m}{SWW}
\end{aligned}$$

A good rule of thumb is to select the number of bins  $m$  such that  $\text{Var}(br_b) \leq 0.01$ .





