# Table of Contents

|                                                                 |             |
|-----------------------------------------------------------------|-------------|
| <b>Acknowledgments .....</b>                                    | <b>vii</b>  |
| <b>About the Authors .....</b>                                  | <b>viii</b> |
| <b>Introduction .....</b>                                       | <b>1</b>    |
| <b>1. A Review of GLMs .....</b>                                | <b>3</b>    |
| 1.1. Definitions and Terminology.....                           | 3           |
| 1.2. The Linear Predictor.....                                  | 4           |
| 1.3. Distributions and Link Functions.....                      | 5           |
| 1.4. The Offset .....                                           | 6           |
| 1.5. Table-Based Output: An Example .....                       | 6           |
| 1.6. Likelihood Optimization: Full Credibility Assumption ..... | 7           |
| 1.6.1. P-Values .....                                           | 9           |
| 1.6.2. Lack of Credibility in GLM Estimates.....                | 10          |
| <b>2. A Brief Review of Credibility .....</b>                   | <b>11</b>   |
| 2.1. Incorporation of Credibility into GLM Estimates .....      | 11          |
| <b>3. Penalized Regression .....</b>                            | <b>14</b>   |
| 3.1. Types of Penalized Regression .....                        | 14          |
| 3.1.1. Role of Penalty Parameter $\lambda$ .....                | 15          |
| 3.1.2. Ridge Regression .....                                   | 16          |
| 3.1.3. Lasso .....                                              | 18          |
| 3.2. Lasso is Recommended for Actuarial Applications .....      | 21          |
| 3.3. Selecting the Penalty Parameter .....                      | 21          |
| 3.4. Lasso and Variable Transformations .....                   | 24          |
| 3.4.1. Categorical Variables .....                              | 24          |
| 3.4.2. Continuous Variables .....                               | 25          |
| 3.4.3. Ordinal Variables.....                                   | 26          |
| 3.4.4. Control Variables .....                                  | 28          |
| 3.5. Lasso for Variable Selection .....                         | 29          |
| <b>4. The Bias–Variance Trade-Off.....</b>                      | <b>30</b>   |
| 4.1. Introducing the Bias–Variance Trade-Off .....              | 30          |
| 4.2. Defining the Bias–Variance Trade-Off .....                 | 30          |
| 4.3. Bias–Variance Trade-Off: A GLM Perspective.....            | 32          |

|                                                                                    |           |
|------------------------------------------------------------------------------------|-----------|
| 4.4. Evaluating the Bias–Variance Trade-Off.....                                   | 33        |
| 4.5. Bias–Variance Trade-Off and Credibility .....                                 | 34        |
| 4.6. Penalized Regression and Credibility .....                                    | 35        |
| 4.7. Conclusion: Benefits of Lasso Penalization .....                              | 36        |
| <b>5. Lasso Credibility.....</b>                                                   | <b>38</b> |
| 5.1. The Offset: Applying a Complement in Lasso Credibility.....                   | 38        |
| 5.2. Ordinal Variables.....                                                        | 39        |
| 5.3. Lasso Credibility as a Credibility-Weighted GLM.....                          | 39        |
| 5.4. Terminology and ASOP 25 .....                                                 | 41        |
| 5.5. Selecting and Evaluating a Penalty Parameter in Lasso Credibility .....       | 42        |
| 5.6. Calculating Indicated Rates in Lasso Credibility.....                         | 43        |
| 5.7. Lasso Credibility Conclusions .....                                           | 45        |
| <b>6. Lasso Penalized Regression and Lasso Credibility Model Diagnostics .....</b> | <b>46</b> |
| 6.1. Review of the Lambda Penalty Parameter .....                                  | 46        |
| 6.2. Review of the Complement of Credibility .....                                 | 47        |
| 6.3. Relativity Plots .....                                                        | 48        |
| 6.3.1. Using Relativity Plots to Guide Model Review .....                          | 48        |
| 6.3.2. Full Credibility in the Complement .....                                    | 48        |
| 6.3.3. Partial Credibility in the Complement .....                                 | 49        |
| 6.3.4. Limited or No Credibility in the Complement.....                            | 50        |
| 6.4. Review by Variable Type.....                                                  | 50        |
| 6.4.1. Categorical Variables .....                                                 | 50        |
| 6.4.2. Continuous Variables .....                                                  | 51        |
| 6.4.3. Ordinal Variables.....                                                      | 51        |
| 6.4.4. Control Variables .....                                                     | 52        |
| 6.5. Model Validation Conclusions .....                                            | 52        |
| <b>7. Case Study .....</b>                                                         | <b>53</b> |
| 7.1. Countrywide Modeling and State Refits .....                                   | 53        |
| 7.2. Case Study Summary .....                                                      | 54        |
| 7.2.1. Data Description.....                                                       | 55        |
| 7.2.2. Predictor Variables.....                                                    | 56        |
| 7.2.3. Methodological Notes .....                                                  | 61        |
| 7.2.4. Prediction and Relativity Plots.....                                        | 62        |
| 7.3. Countrywide Model Results .....                                               | 63        |
| 7.3.1. Large Data Approaches Full Credibility.....                                 | 63        |
| 7.3.2. Additional Exercises—Full Data.....                                         | 63        |
| 7.3.3. Full Data Conclusion—Lasso Penalization,<br>but Not Lasso Credibility ..... | 64        |
| 7.4. “Large State” Modeling Results .....                                          | 67        |
| 7.4.1. Low Significance Correlates with High Shrinkage .....                       | 67        |
| 7.4.2. Shrinkage Varies between Engineered Features .....                          | 69        |
| 7.4.3. Credibility and Feature Engineering.....                                    | 69        |
| 7.4.4. Penalized Regression Benefits .....                                         | 69        |

|                                                                                      |            |
|--------------------------------------------------------------------------------------|------------|
| 7.5. “Large State”—Lasso Credibility Versus GLM.....                                 | 71         |
| 7.5.1. Coefficients of Zero Show Confidence in the Complement<br>of Credibility..... | 71         |
| 7.5.2. Partially Credible Categories Avoid Overreactions .....                       | 72         |
| 7.5.3. Credible Categories React Quickly .....                                       | 72         |
| 7.5.4. Lasso Credibility Moves Toward Experienced Relativities .....                 | 73         |
| 7.5.5. Performance Comparison: Lasso Credibility Versus Lasso<br>Versus GLM.....     | 74         |
| 7.5.6. Large State Conclusion.....                                                   | 76         |
| 7.6. “Medium State”—Lasso Credibility Versus GLM.....                                | 77         |
| 7.6.1. Evaluating the Assigned Credibility .....                                     | 78         |
| 7.6.2. Some Credibility is Better Than None .....                                    | 78         |
| 7.6.3. Medium State Conclusion.....                                                  | 81         |
| 7.7. “Small States”—Lasso Credibility Versus GLM .....                               | 81         |
| 7.7.1. Lasso Credibility is Viable When GLM Fails .....                              | 81         |
| 7.7.2. A Good Complement Creates a Sparse Model.....                                 | 83         |
| 7.7.3. Small-State Conclusion .....                                                  | 83         |
| 7.8. Case Study Conclusion.....                                                      | 83         |
| <b>8. Conclusion—Overall .....</b>                                                   | <b>85</b>  |
| <b>Appendix A. Bayesian Interpretation of Credibility .....</b>                      | <b>86</b>  |
| A.1. Why GLMs Give 100% Credibility to the Data .....                                | 86         |
| A.2. Credibility: A Bayesian Interpretation .....                                    | 89         |
| A.3. Penalized Regression: A Bayesian Interpretation.....                            | 92         |
| A.4. Practical Comparison.....                                                       | 93         |
| A.4.1. Comparison with Increasing Exposures<br>(Fixed Observed Average) .....        | 93         |
| A.4.2. Comparison with an Increasing Observed Average<br>(Fixed Exposure) .....      | 95         |
| A.4.3. Final Comparison .....                                                        | 96         |
| A.5. Degrees of “Bayesian-ness” .....                                                | 97         |
| <b>Appendix B. Alignment of Lasso Credibility with ASOP 25 .....</b>                 | <b>99</b>  |
| B.1. Definitions: Default Complement of Lasso Credibility .....                      | 99         |
| B.2. Considerations and Scope of ASOP 25 .....                                       | 100        |
| B.3. Alternate Complements in Lasso Credibility .....                                | 102        |
| B.4. Lasso Credibility and ASOP 25 Summary .....                                     | 104        |
| <b>Appendix C. Miscellaneous.....</b>                                                | <b>105</b> |
| C.1. Rebasing Model Output .....                                                     | 105        |
| C.2. Penalized Regression and Near Aliasing .....                                    | 106        |
| C.3. Penalized Regression and the AIC.....                                           | 106        |
| <b>Appendix D. Sparsity: A Convex Optimization Perspective .....</b>                 | <b>108</b> |
| D.1. Simplified Proof of the Lasso Problem.....                                      | 109        |
| D.2. General Proof of the Lasso Problem .....                                        | 111        |
| <b>References .....</b>                                                              | <b>114</b> |

