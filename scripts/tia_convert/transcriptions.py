"""Vision transcriptions of the images that carry content no cell holds.

Only two classes are transcribed: `formula_snippet` (equations pasted as
pictures) and `question_exhibit` (data and charts a question depends on). The
229 `examiner_scan` images stay as plain file references -- they restate a
solution already captured from the cells, so transcribing them would cost the
most and add the least.

Keyed by the first 12 hex chars of the image sha256, so an image reused across
sheets is transcribed once. emit.py inlines these beneath the image reference.
"""

TRANSCRIPTIONS: dict[str, str] = {

    # ---------------- formula snippets ----------------------------------
    "55e485843223": (
        "Exponential severity with mean $\\beta$:\n\n"
        "$$E[X; l] = \\beta\\left(1 - e^{-l/\\beta}\\right)"
        " \\qquad F(x) = 1 - e^{-x/\\beta}$$"
    ),
    "eed2d41e58d9": (
        "Uniform severity on $(a, b)$:\n\n"
        "$$E[X; l] = \\frac{2bl - a^2 - l^2}{2(b-a)}"
        " \\qquad F(x) = \\frac{x-a}{b-a}$$"
    ),
    "46307935f076": (
        "Limited second moment (uniform on $(0, b)$):\n\n"
        "$$E[X^2; l] = \\frac{l^3}{3b} + \\frac{l^2(b-l)}{b}$$"
    ),
    "06bc9fbef081": (
        "Poisson claim-count density:\n\n"
        "$$f(n) = \\frac{\\lambda^n e^{-\\lambda}}{n!}$$"
    ),
    "1002bf79a63c": (
        "Exponential severity with mean $\\beta$:\n\n"
        "$$E[X; l] = \\beta\\left(1 - e^{-l/\\beta}\\right)$$\n"
        "$$E[X^2; l] = 2\\beta^2\\left(1 - e^{-l/\\beta}\\right)"
        " - 2\\beta l\\,e^{-l/\\beta}$$"
    ),
    "3a192b949dd4": (
        "Pareto severity with parameters $\\alpha, \\beta$:\n\n"
        "$$E[X; l] = \\frac{\\beta}{\\alpha-1}"
        "\\left(1 - \\left(\\frac{\\beta}{l+\\beta}\\right)^{\\alpha-1}\\right)"
        " \\qquad F(x) = 1 - \\left(\\frac{\\beta}{x+\\beta}\\right)^{\\alpha}$$"
    ),
    "481cbddf02e8": (
        "Lognormal severity with parameters $\\mu, \\sigma$:\n\n"
        "$$E[X; l] = e^{\\mu + \\frac{1}{2}\\sigma^2}"
        "\\times \\Phi\\!\\left(\\frac{\\ln l - \\mu - \\sigma^2}{\\sigma}\\right)"
        " + l \\times \\Phi\\!\\left(\\frac{-\\ln l + \\mu}{\\sigma}\\right)$$\n"
        "$$F(x) = \\Phi\\!\\left(\\frac{\\ln x - \\mu}{\\sigma}\\right)$$"
    ),
    "433288c4f93c": (
        "Formula sheet supplied with the question.\n\n"
        "Poisson distribution:\n"
        "$$\\Pr(N = n) = \\frac{\\lambda^n e^{-\\lambda}}{n!}$$\n\n"
        "Pareto distribution:\n"
        "$$f(x) = \\frac{\\alpha\\beta^{\\alpha}}{(x+\\beta)^{\\alpha+1}}"
        " \\qquad F(x) = 1 - \\left(\\frac{\\beta}{x+\\beta}\\right)^{\\alpha}$$\n"
        "$$E[X; x] = \\frac{\\beta}{\\alpha-1}"
        "\\left[1 - \\left(\\frac{\\beta}{x+\\beta}\\right)^{\\alpha-1}\\right]$$"
    ),
    "7d1575ecee5b": (
        "Pareto formulas supplied with the question:\n\n"
        "$$E[X] = \\frac{\\beta}{\\alpha-1}$$\n"
        "$$E[X; x] = \\frac{\\beta}{\\alpha-1}"
        "\\left[1 - \\left(\\frac{\\beta}{x+\\beta}\\right)^{\\alpha-1}\\right]$$\n"
        "$$e_X(x) = \\frac{x+\\beta}{\\alpha-1}"
        " \\qquad F_X(x) = 1 - \\left(\\frac{\\beta}{x+\\beta}\\right)^{\\alpha}$$"
    ),

    # Insurance-charge relations (Fisher et al., aggregate excess loss).
    "041444fa1e82": "$$\\phi(r_H) - \\phi(r_G) = \\frac{(e + E[A])T - H}{c\\,E[A]\\,T}$$",
    "d3187e887ab5": "$$\\phi(r_H) - \\phi(r_G) = \\frac{(e + E[A])T - H}{c\\,E[A]\\,T}$$",
    "6c6463c22fb1": (
        "Per-occurrence-limited (large deductible) form:\n\n"
        "$$\\phi^{LM}(r^*_H) - \\phi^{LM}(r^*_G)"
        " = \\frac{(e + E[A])T - H}{c\\,E[A_D]\\,T}$$"
    ),
    "76d06e5c8d8c": "$$r_G - r_H = \\frac{G - H}{c\\,E[A]\\,T}$$",
    "8ba7323a13df": "$$r_G - r_H = \\frac{G - H}{c\\,E[A]\\,T}$$",
    "d320749e7c2c": "$$r_G - r_H = \\frac{G - H}{c\\,E[A]\\,T}$$",
    "e27dbf4b992e": "$$r_G - r_H = \\frac{G - H}{c\\,E[A]\\,T}$$",
    "8977aedf2dab": (
        "Entry ratios on the limited (large-deductible) basis:\n\n"
        "$$r^*_G - r^*_H = \\frac{G - H}{c\\,E[A_D]\\,T}$$"
    ),

    # Penalized-regression penalty terms.
    "0de642af2ded": (
        "Elastic-net penalty:\n\n"
        "$$\\lambda\\left(\\alpha\\sum|\\beta|"
        " + (1-\\alpha)\\tfrac{1}{2}\\sum\\beta^2\\right)$$"
    ),
    "057431737f95": "Lasso ($L_1$) penalty:\n\n$$\\lambda\\left(\\sum|\\beta|\\right)$$",
    "fca6a951d7db": (
        "Ridge ($L_2$) penalty:\n\n"
        "$$\\lambda\\left(\\tfrac{1}{2}\\sum\\beta^2\\right)$$"
    ),

    # ---------------- question exhibits ---------------------------------
    "11d519bc04c0": (
        "**Lee diagram.** Vertical axis = Size of Loss, horizontal axis = "
        "Cumulative Claim Frequency running 0 to 1. A diagonal loss-size line "
        "rises from the origin to the top-right. Two horizontal lines mark "
        "sizes $R$ (lower) and $S$ (upper), and two vertical lines split the "
        "frequency axis into three bands, giving twelve labelled regions:\n\n"
        "- Above $S$: **A** (left band), **B** (middle), **C** (right), with "
        "**D** the sliver right of the diagonal at level $S$.\n"
        "- Between $R$ and $S$: **E** (left), **F** (just above the diagonal, "
        "middle), **G** (below/right of the diagonal, middle), **H** (right).\n"
        "- Below $R$: **I** (left, above the diagonal), **J** (left, below), "
        "**K** (middle), **L** (right).\n\n"
        "Area below the diagonal = losses; area above = the complement."
    ),
    "0fc56f10c26d": (
        "**Table M / entry-ratio diagram.** Vertical axis = Entry Ratio, "
        "horizontal axis = $F(y)$ from 0 to 1. Two cumulative curves are "
        "drawn: $F(y)$ (upper, total losses) and $F_D(y)$ (lower, limited "
        "losses). Horizontal lines mark $R = \\text{Max ER}$ and "
        "$S = \\text{Min ER}$; dashed vertical lines subdivide the width. "
        "Labelled regions run A through Z: **A, C, D, E, G, N, O, P** cluster "
        "at the right where the curves rise; **B** spans the band above $R$; "
        "**H, I, J, K, L, M** lie between $S$ and $R$; **Q, T, U, V, W, Z** "
        "lie below $S$. Used to express the insurance charge and savings as "
        "sums of these areas."
    ),
    "6e43f0129197": (
        "**Table M / entry-ratio diagram** (same construction as the exhibit "
        "in Practice Problem 10). Vertical axis = Entry Ratio, horizontal "
        "axis = $F(y)$ from 0 to 1, with curves $F(y)$ (total) and $F_D(y)$ "
        "(limited), horizontal lines at $R = \\text{Max ER}$ and "
        "$S = \\text{Min ER}$, and regions labelled A through Z."
    ),
    "572034412ba5": (
        "**Entry-ratio diagram with two curves.** Vertical axis $y$, "
        "horizontal axis 0 to 1. Solid curve $F(y)$ rises convexly; dashed "
        "curve $F^*(y)$ lies below it. Horizontal lines mark $r_H$ (lower) "
        "and $r_G$ (upper). Nine labelled regions:\n\n"
        "- Below $r_H$: **A** (far left, above the solid curve), **B** (left, "
        "between the curves), **C** (the wide band beneath both curves).\n"
        "- Between $r_H$ and $r_G$: **D** (left), **E** (centre), **F** "
        "(right, below the dashed curve).\n"
        "- Above $r_G$: **G** (left, above the solid curve), **H** (right, "
        "between the curves), **I** (far right)."
    ),
    "e098b65e6e20": (
        "**Entry-ratio diagram, single curve.** Vertical axis = Entry Ratio "
        "$y$, horizontal axis $F(y)$ from 0 to 1. One S-shaped cumulative "
        "curve rises to the right. Dashed horizontal lines mark $S$ (lower) "
        "and $R$ (upper); dashed vertical lines cut the width. Nine regions: "
        "**A** top right above the curve, **B** and **C** in the band between "
        "$S$ and $R$ above the curve, **D** and **E** to the right of that "
        "band, **F** at the far left below $S$, and **G**, **H**, **I** "
        "forming the area beneath the curve from left to right."
    ),
    "fa7b33bfeb10": (
        "**Entry-ratio diagram, total vs limited losses.** Vertical axis = "
        "Entry Ratios, horizontal axis = Cumulative Claim Frequency 0 to 1. "
        "A solid curve labelled *Total Loss* and a dashed curve labelled "
        "*Limited Loss* both rise steeply near $F = 1$. Heavy horizontal "
        "lines mark $r_1$ (lower) and $r_2$ (upper). Regions: **A** and **B** "
        "at the far left near the origin, **C** the wide area beneath both "
        "curves below $r_1$, **D** and **E** between $r_1$ and $r_2$ above "
        "the curves, **F** between $r_1$ and $r_2$ below the dashed curve, "
        "**G** and **H** above $r_2$, and **I** at the top right corner."
    ),
    "48f1f66240e2": (
        "**Empirical loss-ratio step function.** Horizontal axis = Percent of "
        "Risks (0-100%), vertical axis = Loss Ratio (0-200%). The cumulative "
        "step function takes these values:\n\n"
        "| Percent of risks | Loss ratio |\n| --- | --- |\n"
        "| 0% - 5% | 20% |\n| 5% - 20% | 40% |\n| 20% - 55% | 60% |\n"
        "| 55% - 70% | 80% |\n| 70% - 80% | 100% |\n| 80% - 90% | 120% |\n"
        "| 90% - 100% | 180% |"
    ),
    "af8a958e9992": (
        "**Bar chart titled \"Unlimited Loss\".** Horizontal axis = Percent of "
        "Risks in 10% bands, vertical axis = Loss Ratio (0 to 1.2). Bar "
        "heights by band:\n\n"
        "| Band | Loss ratio |\n| --- | --- |\n| 10% | 0 |\n| 20% | 0 |\n"
        "| 30% | 0.2 |\n| 40% | 0.4 |\n| 50% | 0.6 |\n| 60% | 0.8 |\n"
        "| 70% | 0.8 |\n| 80% | 1.0 |\n| 90% | 1.0 |\n| 100% | 1.2 |"
    ),
    "87ce028ec2bd": (
        "**Two bar charts, \"Observations of Subset A\" and \"Observations of "
        "Subset B\".** Both plot Claim Size (vertical, 0 to 80,000) against "
        "Observation 1-10 (horizontal).\n\n"
        "| Observation | Subset A | Subset B |\n| --- | --- | --- |\n"
        "| 1-5 | ~20,000 | ~10,000 |\n| 6 | ~31,000 | ~10,000 |\n"
        "| 7-9 | ~31,000 | ~40,000 |\n| 10 | ~42,000 | ~80,000 |\n\n"
        "Subset A is tightly clustered; Subset B is far more dispersed, with "
        "a single large observation at 80,000."
    ),
    "021c359d6d52": (
        "**Scatter plot titled \"Working Residuals\".** Horizontal axis = "
        "Exposures (0 to 2,500), vertical axis = Binned Working Residual "
        "(-0.14 to 0.06). Residuals fan out widely at low exposure counts "
        "(spread roughly -0.02 to +0.05, with two outliers at -0.10 and "
        "-0.12 near zero exposures) and collapse to essentially zero for "
        "bins with 500 or more exposures — the classic funnel showing "
        "variance decreasing as exposure grows."
    ),
    "7e5c21f6c850": (
        "**Scatter plot titled \"Partial Residuals for ln(InsuredAge)\".** "
        "Horizontal axis = ln(InsuredAge) from 2.8 to 4.2, vertical axis = "
        "Partial Residual from 0.5 to 3. Points scatter between about 0.9 and "
        "2.7, and a straight red *Fit Line* rises steadily from roughly 1.35 "
        "at ln(age) = 2.8 to about 1.85 at ln(age) = 4.1. The points dip "
        "below the line around ln(age) 3.1-3.4 and sit above it beyond 3.7, "
        "hinting the linear term does not capture the true curvature."
    ),
    "f291d86fb9e3": (
        "**Combined bar and line chart: wind frequency relativity by credit "
        "score.** Left axis = Wind Frequency Relativity (0.6 to 1.8), right "
        "axis = Exposures in thousands (0 to 300), categories Good / Fair / "
        "Poor.\n\n"
        "| Credit score | Indicated relativity | Approx. exposures | "
        "+/- 2 standard errors |\n| --- | --- | --- | --- |\n"
        "| Good | 1.00 | ~255,000 | very tight |\n"
        "| Fair | 1.15 | ~48,000 | ~1.12 to ~1.19 |\n"
        "| Poor | 1.49 | ~13,000 | ~1.36 to ~1.62 |\n\n"
        "The confidence band widens sharply as exposure volume falls."
    ),
    "210416654c72": (
        "**Line chart, \"Actual vs. Modeled Expected Loss Ratio\".** "
        "Horizontal axis = Manual Premium Range, vertical axis = Manual Loss "
        "Ratio (50% to 80%). Two series, *Model Expected Loss Ratio* and "
        "*Actual Loss Ratio*:\n\n"
        "| Manual premium range | Model expected | Actual |\n| --- | --- | --- |\n"
        "| < 1,000 | 66% | 64.5% |\n| 1,000-2,500 | 65.5% | 66% |\n"
        "| 2,500-5,000 | 64.5% | 64% |\n| 5,000-10,000 | 66% | 65% |\n"
        "| 10,000-25,000 | 64% | 59.5% |\n| 25,000-50,000 | 65% | 68.5% |\n"
        "| 50,000-100,000 | 65.5% | 61% |\n| 100,000-250,000 | 67% | 72% |\n"
        "| 250,000-500,000 | 64.5% | 59% |\n| 500,000-1,000,000 | 67% | 73% |\n"
        "| > 1,000,000 | 65% | 60% |\n\n"
        "The model is flat near 65% throughout while actuals swing "
        "increasingly wildly as premium size grows."
    ),
    "36bc0444fc69": (
        "**Combined chart: observations and estimated beta by vehicle type.** "
        "Left axis = # Observations (0 to 12,000), right axis = Estimated Beta "
        "(0 to 0.3), categories Sedan / Truck / Van. Bars show observation "
        "counts; three lines show estimated betas from different fits.\n\n"
        "| Vehicle | Observations | Beta (line 1) | Beta (line 2) | Beta (line 3) |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| Sedan | 10,000 | 0 (base) | 0 | 0 |\n"
        "| Truck | 8,000 | 0.25 | 0.23 | 0.17 |\n"
        "| Van | ~300 | 0.13 | 0.06 | 0.005 |\n\n"
        "Sedan is the base level. The three fits agree closely for Truck "
        "(high volume) but diverge sharply for Van, which has very few "
        "observations."
    ),
    "1b60fbfa2852": (
        "**Line chart: pseudo-$R^2$ against $\\log(\\lambda)$** for training "
        "and cross-validation.\n\n"
        "| $\\log(\\lambda)$ | training | cross-validation |\n"
        "| --- | --- | --- |\n"
        "| -10 | 0.180 | 0.140 |\n| -9 | 0.174 | 0.140 |\n"
        "| -8 | 0.168 | 0.140 |\n| -7 | 0.161 | 0.140 |\n"
        "| -6 | 0.152 | 0.136 |\n| -5 | 0.135 | 0.120 |\n"
        "| -4 | 0.104 | 0.095 |\n\n"
        "Training fit improves monotonically as the penalty shrinks, while "
        "cross-validation flattens at 0.140 below $\\log(\\lambda) = -7$ — "
        "the extra flexibility buys no out-of-sample gain."
    ),
    "5c474ee92979": (
        "**Cross-validation curves: pseudo-$R^2$ on validation folds against "
        "$\\log(\\lambda)$.** Several thin coloured lines show individual "
        "folds; a heavy black line is the *average of the folds*. The average "
        "peaks near $\\log(\\lambda) \\approx -3.5$ at about 0.0335 and is "
        "very flat across the middle of the range. Two dashed verticals are "
        "annotated:\n\n"
        "| $\\log(\\lambda)$ | average pseudo-$R^2$ | spread across folds |\n"
        "| --- | --- | --- |\n"
        "| -6 | 0.0326 | 0.024 to 0.041 |\n"
        "| -2 | 0.0323 | 0.029 to 0.036 |\n\n"
        "The two averages are nearly identical, but the fold-to-fold spread "
        "is much narrower at $\\log(\\lambda) = -2$."
    ),
    "03f73c6a85c1": (
        "**Scatter plot: accident frequency against aircraft age, smooth "
        "fit.** Red points are actual frequency; a cyan curve is the fitted "
        "frequency, decaying smoothly. Labelled fitted values:\n\n"
        "| Aircraft age | Fitted frequency |\n| --- | --- |\n"
        "| 0 | 0.0100 |\n| 10 | 0.0060 |\n| 30 | 0.0030 |\n| 50 | 0.0025 |\n\n"
        "Actual points track the curve closely to about age 40, then rise "
        "away from it (roughly 0.0038-0.0046) for ages 42-50, where the "
        "fitted curve keeps declining."
    ),
    "e55adc0789a7": (
        "**Scatter plot: accident frequency against aircraft age, step "
        "fit.** Red points are actual frequency; cyan horizontal segments are "
        "the fitted frequency, piecewise constant across binned age ranges:\n\n"
        "| Aircraft age band | Fitted frequency |\n| --- | --- |\n"
        "| 0-10 | 0.008 |\n| 10-25 | 0.005 |\n| 25-50 | 0.003 |\n\n"
        "Actual frequency declines steadily and continuously from about "
        "0.009 at age 0 to roughly 0.002 at age 50, so the three-step fit "
        "systematically over- and under-shoots within each band — the "
        "contrast with the smooth fit for the same data."
    ),
}
