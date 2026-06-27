---
paper: holmes_&_casotto
chapter: 8
title: Conclusion—Overall
topics: [lasso_credibility, asop_25, ordinal_variables, model_review, penalized_regression]
key_formulas: []
---

> **TL;DR**
> - Lasso credibility is mathematically linked to Bühlmann credibility and Bayesian statistics, but should be reviewed as a standalone credibility technique — not through GLM or classical credibility validation lenses.
> - Model reviewers should not directly apply GLM (p-values, AIC) or classical credibility review standards; lasso credibility requires combined expertise in penalized regression and credibility procedures.
> - Ordinal treatment of continuous variables is strongly recommended; it enables objective, credibility-based feature engineering and avoids slope-extrapolation issues in thin-data tails.
> - Lasso credibility extends to smaller and smaller data sets by leaning on an appropriate complement; actuaries can model segments that would be unstable under a standard GLM.
> - The technique is not just for big data — smaller subsets of larger books can also benefit from lasso credibility with a suitable complement of credibility.

# 8. Conclusion—Overall

As we have seen, penalized regression can be applied as a credibility procedure and has strong mathematical links with widely accepted credibility procedures. Appendix A identifies a special case of equivalence between penalized regression and Bühlmann credibility, and it is important to note that equivalence is not necessary, as Appendix B defines penalized regression as a credibility procedure without relying on the link to other widely used procedures. Similarly, best practices applied to building lasso credibility models should be based on best practices of penalized regression in general—not taken from classical or Bühlmann credibility procedures directly. This change in perspective from lasso penalization to lasso credibility does not change the mathematical foundation of penalized regression, but rather it constitutes a new actuarial application of the existing technique.

Model reviewers should not directly take model validation requirements from either GLM or Bühlmann credibility techniques. Lasso credibility should be reviewed as a stand-alone credibility technique with its own model review standards. Those standards are taken from a combination of penalized regression and credibility procedure expertise. Straightforward application of existing model validation procedures to lasso credibility will be suboptimal.

We recommend an ordinal treatment of continuous variables in lasso credibility because it allows the model to identify credible differences from the complement during model fitting. The technique was popularized in Iwasawa and Wang (2022) and expanded upon in Casotto and Holmes (2023). We encourage the reader to investigate these techniques; they provide support for moving to a modeling approach where feature engineering is objective and fully credibility based.

Lasso credibility deserves a place in every actuary's analytical tool kit. By combining lasso penalization with a complement of credibility in the offset, one can use lasso credibility to analyze data sets of increasingly small sizes. Similarly, increasingly small subsets of larger data sets can be analyzed for insights and additional segmentation opportunities. Such complements of credibility can come from many sources and can be applied to many different types of analysis. Penalized regression is not just for big data!

We hope that this monograph has provided the necessary background for the reader to begin using penalized regression and lasso credibility. Happy modeling, and all the best in your actuarial and personal endeavors.

