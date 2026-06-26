# Contents

|                                                                         |           |
|-------------------------------------------------------------------------|-----------|
| <b>1. Introduction .....</b>                                            | <b>1</b>  |
| <b>2. Overview of Technical Foundations.....</b>                        | <b>2</b>  |
| 2.1. The Components of the GLM .....                                    | 2         |
| 2.1.1. The Random Component: The Exponential Family .....               | 3         |
| 2.1.2. The Systematic Component .....                                   | 4         |
| 2.1.3. An Example .....                                                 | 5         |
| 2.2. Exponential Family Variance .....                                  | 7         |
| 2.3. Variable Significance .....                                        | 8         |
| 2.3.1. Standard Error .....                                             | 8         |
| 2.3.2. p-value .....                                                    | 9         |
| 2.3.3. Confidence Interval .....                                        | 9         |
| 2.4. Types of Predictor Variables .....                                 | 10        |
| 2.4.1. Treatment of Continuous Variables .....                          | 10        |
| 2.4.2. Treatment of Categorical Variables .....                         | 12        |
| 2.4.3. Choose Your Base Level Wisely! .....                             | 15        |
| 2.5. Weights.....                                                       | 16        |
| 2.6. Offsets .....                                                      | 17        |
| 2.7. An Inventory of Distributions.....                                 | 19        |
| 2.7.1. Distributions for Severity .....                                 | 19        |
| 2.7.2. Distributions for Frequency .....                                | 21        |
| 2.7.3. A Distribution for Pure Premium: the Tweedie Distribution .....  | 22        |
| 2.8. Logistic Regression.....                                           | 25        |
| 2.9. Correlation Among Predictors, Multicollinearity and Aliasing ..... | 27        |
| 2.10. Limitations of GLMs .....                                         | 28        |
| <b>3. The Model-Building Process .....</b>                              | <b>31</b> |
| 3.1. Setting Objectives and Goals.....                                  | 31        |
| 3.2. Communication with Key Stakeholders .....                          | 32        |
| 3.3. Collecting and Processing Data.....                                | 32        |
| 3.4. Conducting Exploratory Data Analysis .....                         | 32        |
| 3.5. Specifying Model Form.....                                         | 33        |
| 3.6. Evaluating Model Output .....                                      | 33        |
| 3.7. Validating the Model .....                                         | 33        |
| 3.8. Translating the Model into a Product.....                          | 33        |
| 3.9. Maintaining and Rebuilding the Model .....                         | 34        |

|                                                                              |           |
|------------------------------------------------------------------------------|-----------|
| <b>4. Data Preparation and Considerations .....</b>                          | <b>35</b> |
| 4.1. Combining Policy and Claim Data .....                                   | 35        |
| 4.2. Modifying the Data .....                                                | 37        |
| 4.3. Splitting the Data.....                                                 | 38        |
| 4.3.1. Train and Test .....                                                  | 40        |
| 4.3.2. Train, Validation and Test .....                                      | 40        |
| 4.3.3. Use Your Data Wisely! .....                                           | 40        |
| 4.3.4. Cross Validation.....                                                 | 41        |
| <b>5. Selection of Model Form .....</b>                                      | <b>43</b> |
| 5.1. Choosing the Target Variable .....                                      | 43        |
| 5.1.1. Frequency/Severity versus Pure Premium .....                          | 43        |
| 5.1.2. Policies with Multiple Coverages and Perils.....                      | 44        |
| 5.1.3. Transforming the Target Variable.....                                 | 45        |
| 5.2. Choosing the Distribution .....                                         | 46        |
| 5.3. Variable Selection.....                                                 | 47        |
| 5.4. Transformation of Variables .....                                       | 48        |
| 5.4.1. Detecting Non-Linearity with Partial Residual Plots .....             | 48        |
| 5.4.2. Binning Continuous Predictors.....                                    | 49        |
| 5.4.3. Adding Polynomial Terms .....                                         | 51        |
| 5.4.4. Using Piecewise Linear Functions .....                                | 53        |
| 5.4.5. Natural Cubic Splines .....                                           | 55        |
| 5.5. Grouping Categorical Variables.....                                     | 55        |
| 5.6. Interactions.....                                                       | 55        |
| 5.6.1. Interacting Two Categorical Variables.....                            | 56        |
| 5.6.2. Interacting a Categorical Variable<br>with a Continuous Variable..... | 58        |
| 5.6.3. Interacting Two Continuous Variables.....                             | 61        |
| <b>6. Model Refinement.....</b>                                              | <b>62</b> |
| 6.1. Some Measures of Model Fit.....                                         | 62        |
| 6.1.1. Log-Likelihood .....                                                  | 62        |
| 6.1.2. Deviance.....                                                         | 63        |
| 6.1.3. Limitations on the Use of Log-Likelihood and Deviance.....            | 64        |
| 6.2. Comparing Candidate Models.....                                         | 64        |
| 6.2.1. Nested Models and the F-Test.....                                     | 64        |
| 6.2.2. Penalized Measures of Fit .....                                       | 66        |
| 6.3. Residual Analysis.....                                                  | 67        |
| 6.3.1. Deviance Residuals .....                                              | 67        |
| 6.3.2. Working Residuals .....                                               | 70        |
| 6.4. Assessing Model Stability .....                                         | 73        |
| <b>7. Model Validation and Selection .....</b>                               | <b>75</b> |
| 7.1. Assessing Fit with Plots of Actual vs. Predicted.....                   | 75        |
| 7.2. Measuring Lift .....                                                    | 76        |
| 7.2.1. Simple Quantile Plots .....                                           | 77        |
| 7.2.2. Double Lift Charts.....                                               | 78        |

|                                                                               |            |
|-------------------------------------------------------------------------------|------------|
| 7.2.3. Loss Ratio Charts.....                                                 | 79         |
| 7.2.4. The Gini Index.....                                                    | 80         |
| 7.3. Validation of Logistic Regression Models .....                           | 81         |
| 7.3.1. Receiver Operating Characteristic (ROC) Curves .....                   | 82         |
| <b>8. Model Documentation.....</b>                                            | <b>86</b>  |
| 8.1. The Importance of Documenting Your Model .....                           | 86         |
| 8.2. Check Yourself.....                                                      | 86         |
| 8.3. Stakeholder Management.....                                              | 87         |
| 8.4. Code as Documentation .....                                              | 88         |
| <b>9. Other Topics .....</b>                                                  | <b>89</b>  |
| 9.1. Modeling Coverage Options with GLMs<br>(Why You Probably Shouldn't)..... | 89         |
| 9.2. Territory Modeling .....                                                 | 90         |
| 9.3. Ensembling.....                                                          | 91         |
| <b>10. Variations on the Generalized Linear Model.....</b>                    | <b>93</b>  |
| 10.1. Generalized Linear Mixed Models (GLMMs) .....                           | 93         |
| 10.2. GLMs with Dispersion Modeling (DGLMs).....                              | 96         |
| 10.3. Generalized Additive Models (GAMs) .....                                | 98         |
| 10.4. MARS Models .....                                                       | 100        |
| 10.5. Elastic Net GLMs .....                                                  | 101        |
| <b>Bibliography .....</b>                                                     | <b>105</b> |
| <b>Appendix .....</b>                                                         | <b>107</b> |

