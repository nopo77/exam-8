# Contents

|                                                            |           |
|------------------------------------------------------------|-----------|
| Acknowledgments .....                                      | vii       |
| About the Authors .....                                    | viii      |
| <b>1. Introduction .....</b>                               | <b>1</b>  |
| 1.1 Objectives .....                                       | 1         |
| <b>2. The Case Studies.....</b>                            | <b>3</b>  |
| 2.1 FAA-NTSB Data for Aircraft Incident Frequency .....    | 3         |
| 2.2 Road Accident Frequency Model .....                    | 5         |
| 2.3 Simulated Data—Auto Insurance .....                    | 6         |
| 2.4 The Challenges .....                                   | 6         |
| 2.4.1 High cardinality categorical variables (HCCVs) ..... | 6         |
| 2.4.2 Combining other models with a GLM .....              | 7         |
| 2.4.3 “Controlling” for certain features .....             | 8         |
| 2.4.4 Highly correlated variables .....                    | 8         |
| 2.5 Next Steps.....                                        | 8         |
| <b>3. Performance Measurement .....</b>                    | <b>9</b>  |
| 3.1 Pseudo- $R^2$ .....                                    | 9         |
| 3.2 Train—Validate—Test .....                              | 12        |
| 3.3 Generalization Error.....                              | 15        |
| 3.4 Null Models.....                                       | 15        |
| 3.5 Baseline Models.....                                   | 17        |
| 3.6 Benchmark Models .....                                 | 20        |
| 3.7 Practically Speaking .....                             | 21        |
| 3.7.1 Typical values for pseudo- $R^2$ .....               | 21        |
| 3.7.2 Weights.....                                         | 22        |
| 3.7.3 Creating folds.....                                  | 22        |
| 3.7.4 Rebasing predictions .....                           | 23        |
| 3.8 Next Steps.....                                        | 25        |
| <b>4. Penalized Regression .....</b>                       | <b>26</b> |
| 4.1 Introduction .....                                     | 26        |
| 4.2 Types of Penalty .....                                 | 28        |

|           |                                                             |           |
|-----------|-------------------------------------------------------------|-----------|
| 4.2.1     | Ridge regression .....                                      | 28        |
| 4.2.2     | LASSO .....                                                 | 30        |
| 4.2.3     | Elastic net .....                                           | 32        |
| 4.3       | Choosing $\lambda$ Using k-Fold Cross-Validation .....      | 32        |
| 4.4       | Case Study—Penalized Regression .....                       | 35        |
| 4.5       | The Relaxed LASSO .....                                     | 38        |
| 4.6       | Practically Speaking .....                                  | 40        |
| 4.6.1     | Software.....                                               | 40        |
| 4.6.2     | How many models? .....                                      | 40        |
| 4.6.3     | Penalization parameter names— $\lambda$ and $\gamma$ .....  | 41        |
| 4.6.4     | Performance graphs—x-axis.....                              | 41        |
| 4.6.5     | Choosing $\lambda$ .....                                    | 41        |
| 4.6.6     | Flavors of penalized regression .....                       | 44        |
| 4.7       | Technical Note.....                                         | 45        |
| 4.7.1     | Solving Ridge regression .....                              | 45        |
| 4.7.2     | Standardization .....                                       | 46        |
| 4.7.3     | Solving the LASSO .....                                     | 48        |
| 4.8       | Next Steps.....                                             | 50        |
| <b>5.</b> | <b>Nonlinear Effects .....</b>                              | <b>52</b> |
| 5.1       | Feature Engineering .....                                   | 52        |
| 5.2       | Step Functions.....                                         | 54        |
| 5.3       | Hinge Functions.....                                        | 58        |
| 5.4       | Step Versus Hinge .....                                     | 63        |
| 5.5       | Multivariate Adaptive Regression Splines (MARS) .....       | 64        |
| 5.6       | Case Study—Piecewise Linear Functions .....                 | 65        |
| 5.7       | Practically Speaking .....                                  | 67        |
| 5.7.1     | Random features .....                                       | 67        |
| 5.7.2     | Ordinal categorical variables .....                         | 67        |
| 5.7.3     | Surrogate GLMs.....                                         | 70        |
| 5.8       | Technical Note.....                                         | 71        |
| 5.8.1     | Step functions and the fused LASSO .....                    | 71        |
| 5.9       | Next Steps.....                                             | 72        |
| <b>6.</b> | <b>High Cardinality Categorical Variables (HCCVs) .....</b> | <b>73</b> |
| 6.1       | Introduction .....                                          | 73        |
| 6.2       | Target Encoding .....                                       | 74        |
| 6.3       | Leakage.....                                                | 77        |
| 6.4       | Some Other Encoding Approaches.....                         | 79        |
| 6.4.1     | Grouping rare categories .....                              | 79        |
| 6.4.2     | Frequency encoding .....                                    | 80        |

|           |                                                           |            |
|-----------|-----------------------------------------------------------|------------|
| 6.4.3     | Hierarchical grouping .....                               | 81         |
| 6.4.4     | Feature creation and word embeddings .....                | 82         |
| 6.5       | Generalized Linear Mixed Models .....                     | 83         |
| 6.6       | Case Study—HCCVs .....                                    | 86         |
| 6.7       | Practically Speaking .....                                | 90         |
| 6.7.1     | Sense-checking the results and ad-hoc adjustments .....   | 90         |
| 6.7.2     | Target encoding using GLM predictions .....               | 91         |
| 6.7.3     | Novel categories in the future .....                      | 92         |
| 6.7.4     | What does zero mean? .....                                | 92         |
| 6.7.5     | Keeping up with other ideas .....                         | 93         |
| 6.7.6     | Read the documentation .....                              | 93         |
| 6.7.7     | Are HCCVs really predictive? .....                        | 95         |
| 6.7.8     | Sense-checking the data .....                             | 95         |
| 6.8       | Technical Note .....                                      | 96         |
| 6.8.1     | HCCV estimates using Ridge regression .....               | 96         |
| 6.8.2     | Link to the Bayesian approach .....                       | 98         |
| 6.9       | Next Steps .....                                          | 101        |
| <b>7.</b> | <b>Highly Correlated Variables .....</b>                  | <b>102</b> |
| 7.1       | How Do Highly Correlated Variables Arise? .....           | 103        |
| 7.1.1     | Naturally .....                                           | 103        |
| 7.1.2     | As a result of data enrichment .....                      | 104        |
| 7.1.3     | As a result of feature engineering .....                  | 104        |
| 7.2       | Why Do They Matter? .....                                 | 105        |
| 7.2.1     | Computational issues .....                                | 105        |
| 7.2.2     | Performance .....                                         | 106        |
| 7.2.3     | Interpretability and communication .....                  | 107        |
| 7.2.4     | Cost .....                                                | 108        |
| 7.3       | Introducing a Case Study .....                            | 108        |
| 7.4       | Dealing with Highly Correlated Variables .....            | 111        |
| 7.4.1     | Common sense .....                                        | 111        |
| 7.4.2     | Removing some features before model training .....        | 112        |
| 7.4.3     | Ridge regression .....                                    | 112        |
| 7.4.4     | LASSO .....                                               | 114        |
| 7.4.5     | Principal component analysis .....                        | 117        |
| 7.5       | Practically Speaking .....                                | 120        |
| 7.5.1     | Fold variable in time series data .....                   | 120        |
| 7.5.2     | Hinges and splines with correlated features .....         | 121        |
| 7.5.3     | LASSO in the presence of highly correlated features ..... | 121        |
| 7.5.4     | High coefficients in later principal components .....     | 121        |

|                                                                     |            |
|---------------------------------------------------------------------|------------|
| <b>8. Modeling in Two Stages .....</b>                              | <b>123</b> |
| 8.1 Fixing Coefficients With an Offset .....                        | 124        |
| 8.2 The Hypothesis Space of GLMs .....                              | 129        |
| 8.3 Two-Stage Models Using Offsets .....                            | 131        |
| 8.4 Two-Stage Models Using Residuals .....                          | 135        |
| 8.5 Two-Stage Models Using Preadjustment .....                      | 135        |
| 8.6 Recombining the Two Models .....                                | 137        |
| 8.7 Combining Parts of Multiplicative Models .....                  | 137        |
| 8.8 Further Examples .....                                          | 139        |
| 8.8.1 Credit scores .....                                           | 139        |
| 8.8.2 Usage-based insurance .....                                   | 140        |
| 8.8.3 Use of proxy variables .....                                  | 140        |
| 8.9 Practically Speaking .....                                      | 141        |
| 8.9.1 Leakage in two-stage models .....                             | 141        |
| 8.9.2 Rating groups .....                                           | 142        |
| <b>9. Learning From Black-Box Models .....</b>                      | <b>145</b> |
| 9.1 Model Variance Revisited .....                                  | 146        |
| 9.2 Variable Selection and Importance .....                         | 147        |
| 9.3 Nonlinear Effects .....                                         | 153        |
| 9.4 Interactions .....                                              | 159        |
| 9.5 Practically Speaking .....                                      | 162        |
| 9.5.1 Feature importance—train or test data .....                   | 162        |
| 9.6 Technical Note .....                                            | 163        |
| 9.6.1 Reasons that certain model types include all features .....   | 163        |
| <b>10. Challenges and Considerations in Ratemaking Models .....</b> | <b>164</b> |
| 10.1 Understanding the Data .....                                   | 164        |
| 10.2 Technical Errors .....                                         | 165        |
| 10.3 Data Does Not Meet Model Assumptions .....                     | 165        |
| 10.4 Stability Over Time .....                                      | 166        |
| 10.4.1 Coefficients can change over time .....                      | 166        |
| 10.4.2 The meaning of data can change over time .....               | 167        |
| 10.4.3 Business mix can change over time .....                      | 167        |
| 10.4.4 When cross-validation will fail .....                        | 168        |
| 10.5 Regulation .....                                               | 168        |
| 10.6 Outliers and Model Stability .....                             | 169        |
| 10.7 Data Quality .....                                             | 169        |
| 10.8 Conclusion .....                                               | 171        |
| <b>Bibliography .....</b>                                           | <b>172</b> |

