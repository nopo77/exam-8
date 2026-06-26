

# Errata

## Penalized Regression and Lasso Credibility (2025 Revision)

Date Approved: 12/5/2025

In the corrections below, the **boldface text** indicates the corrected wording.

###### Page 12

“Figure 2.1. Evolution of the credibility factor  $Z$  for a given estimate  $j$  as a function of the number of observations  $n$ . The  $Z$  for the classical credibility is computed using Equation 2.1 with  **$N_{\text{full}} = 10,000$** . Bühlmann credibility uses  $k = 1,600$  in Equation 2.2.”

###### Page 74

*Under 7.5.4. Lasso Credibility Moves Toward Experienced Relativities*

“On the other hand, Figure 7.20 shows that the **20%** shrinkage applied to the vehicle\_age\_10\_99\_hinge coefficient assigns some credibility to the simulated experience, and this experience is quite far from the true relativity. This variable’s insignificance in the GLM does not solve the problem, as removing the coefficient would result in an even more incorrect aggregate relativity.”

###### Page 113

*Under D.2. General Proof of the Lasso Problem*

$$\begin{cases} |\nabla NLL(y, X, \beta)_j| < \lambda \leftrightarrow \hat{\beta}_j = 0 \\ \nabla NLL(y, X, \beta)_j = -\lambda \leftrightarrow \hat{\beta}_j > 0 \\ \nabla NLL(y, X, \beta)_j = \lambda \leftrightarrow \hat{\beta}_j < 0, \end{cases}$$