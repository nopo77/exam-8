---
paper: fisher_et_al
chapter: null
title: "Solutions to Chapter Questions"
topics: [experience_rating, retrospective_rating, table_m, insurance_charge, insurance_savings, lee_diagrams]
key_formulas: [vertical_slicing_method, horizontal_slicing_method, table_l_charge_formula]
---

> **TL;DR**
> - Ch1: Company B (fewer rating classes) benefits more from experience rating; schedule credit is inappropriate if the favorable characteristic was already present during the experience period and is thus already embedded in the e-mod
> - Ch2: Tax multiplier T = 1/(1−tax rate) exceeds 1+tax rate because tax applies to the full gross premium including itself; retro premium = (B + c × ratable losses) × T with ratable losses capped at the per-occurrence limit and the maximum ratable loss amount
> - Ch3: Vertical method: φ(r) = simple average of max(entry_ratio − r, 0) across all risks; horizontal method: starting from the bottom, accumulate (% risks above r) × (Δr) upward; discretizing at intervals wider than the data spacing introduces upward bias in φ
> - ψ(r) = φ(r) + r − 1 for all r; for uniform and exponential distributions both charge and savings have closed-form expressions derivable from the integral definitions
> - Table L: φ*_D(r) = k + area between unlimited and limited CDFs above r on a Lee diagram; ψ*_D(r) = φ*_D(r) + r − 1; independently summing per-occurrence excess k and aggregate excess φ(r) overstates total cost due to overlap region B

## Solutions to Chapter Questions

## Chapter 1 Answers

1. The objectives of experience rating are to:
  - a. Increase equity
  - b. Incentive for safety
  - c. Enhance market competition
2. Experience rating adjusts a risk's rate to be more in line with that risk's expected loss experience. Risks whose expected loss experience is lower than average will pay less premium, and risks whose expected loss experience is higher will pay more premium.
3. Company B—since Company B has fewer rating classes, there will probably be more variation in risks within each rating class. The use of experience rating will allow the company to further tailor each risk's premium with its loss potential.
4. Without experience rating, a company would charge better than average and worse than average risks the same rate. Better than average risks might be able to find a lower rate with another company that recognizes the risk's lower loss potential. If enough of the better than average risks do this, the company will be left with only the worse than average risks.
5. In a group of risks, some of the difference in experience is due to underlying differences in the loss potential of the different risks. This is the variance of the hypothetical means. Some of the difference in experience among the risks is purely random, i.e., the process variance. Experience rating attempts to identify and adjust for the VHM, while at the same time not penalizing risks for differences in experience that are purely random.
6. Probably not. If the safety program in question does in fact reduce this risk's loss potential, this will be reflected in the risk's past experience and will be picked up by the experience rating. Using a schedule credit would double-count the expected benefit of the safety program. However, if the safety program is new (i.e., it was implemented during or after the experience period used by the experience rating program) then there is some expected benefit that would not be reflected in the past experience.

### Chapter 2 Answers

1. There is no credit risk related to self-insured retentions because the insurer does not pay the retained losses up front, and therefore does not need to seek reimbursement from the self-insured.
2.  $1.053 = 1 / (1 - 0.05)$
3.  $0.048 = 1 - 1/1.05$
4. The tax multiplier needs to account for the fact that premium tax is part of premium and therefore is itself taxed.
5.  $13\% = 0.20 - (1.10 - 1) \times 0.70$ . That is, 13% of the guaranteed-cost premium will be collected as a fixed expense through the basic premium amount.
6.  $1.15 = 1 + (0.25 - 0.15) / 0.65$
7. Total losses, limited to the per-occurrence loss limit, are  $315,000 = 25,000 + 15,000 + 25,000 + 50,000 + 2 \times 100,000$ . This is below the maximum ratable loss amount.  
The retrospective premium is  $\$511,892 = (150,000 + 1.1 \times 315,000) \times 1.031$
8. As the loss conversion factor increases, expenses are shifted out of the basic premium, and the basic premium decreases.

As the loss limit increases, the charge for per-occurrence excess exposure decreases, and the basic premium decreases.

As the maximum premium or maximum ratable loss amount increases, the charge for aggregate excess exposure decreases, and the basic premium decreases.

As the minimum premium or minimum ratable loss amount increases, the net charge for aggregate excess exposure (i.e., the net insurance charge) decreases, and the basic premium decreases.

As the account size increases, there are two effects. The amount of premium discount increases, reducing the percentage expense provision in the basic premium. In addition, larger accounts have more stable loss experience, so the charge for aggregate excess exposure decreases. (The latter impact may become clearer after reading chapter 3.) For both of these reasons, the basic premium decreases.

9. The premium is calculated as:

|               |                                                  |
|---------------|--------------------------------------------------|
| 35,000        | fixed expense                                    |
| 30,000        | loss-based expense = $300,000 \times 10\%$       |
| 5,000         | underwriting profit                              |
| 30,000        | per-occurrence excess = $300,000 - 270,000$      |
| <u>10,000</u> | aggregate excess = $270,000 - 260,000$           |
| 110,000       | subtotal                                         |
| 113,402       | including premium tax = $110,000 \times (1/.97)$ |

10. A loss-sensitive dividend plan is unbalanced because if loss experience is better than expected, the insured receives a dividend, but if loss experience is worse than expected, the insured does not incur any additional costs.

11. The risk transfer is the same for a retrospective rating plan and a large deductible plan when:
  - a. The loss limit for the retrospective rating plan equals the per-occurrence deductible.
  - b. The maximum ratable loss amount for the retrospective rating plan equals the aggregate deductible limit.
  - c. There is no minimum ratable loss amount for the retrospective rating plan.

### Chapter 3 Answers

1.

| Problem | Claim # | Claim \$000 | Occ.-Ltd. Agg. Sum | Occ. Excess | Agg. Excess | Total Insurance | Insured Payment |
|---------|---------|-------------|--------------------|-------------|-------------|-----------------|-----------------|
| (a)     | 1       | 3           | 3                  | 0           | 0           | 0               | 3               |
|         | 2       | 8           | 11                 | 0           | 0           | 0               | 8               |
|         | 3       | 14          | 21                 | 4           | 0           | 4               | 10              |
| (b)     | 4       | 12          | 31                 | 2           | 6           | 8               | 4               |
| (c)     | 5       | 18          | 41                 | 8           | 10          | 18              | 0               |

(a) Insurer =  $0+0+4 = 4$ ; Insured =  $3+8+10 = 21$

(b) Insurer =  $4+8 = 12$ ; Insured =  $21+4 = 25$

(c) Insurer =  $12+18 = 30$ ; Insured =  $25+0 = 25$

2.

(a)  $\$500K + \$100K + \$300K + \$2,000K = \$2,900K$

(b)  $\$500K + \$100K + \$250K + \$250K = \$1.1M$

(c)  $\$1.1M - \$1.0M = \$100K$

(d) Only the \$2M claim breaches the per-claim policy limit, so **\$1M**

(e) Prior to application of the policy's aggregate limit, the policy would cover

- \$0 on the small claims
- \$0 on the \$100K claim
- \$50K on the \$300K claim
- \$750K on the \$2M claim
- \$100K for the aggregate on the deductible

For a total of **\$900K**.

(f) **Zero** ( $900K < 5M$ )

(g) **\$900K**

3.

The Table M insurance charge associated with a given outcome is the ratio of the area bounded by  $F(A)$  and that outcome to the total area under  $F(A)$ . The total area under the curve  $F(A) = 100 * 1/2 = 50$ .

![A graph of a linear function F(A) on a coordinate system. The horizontal axis is labeled F(A) and ranges from 0 to 1. The vertical axis is labeled A and ranges from 0 to 100. A solid line starts at the origin (0,0) and goes up to (1,100). Three horizontal dashed lines are drawn at A=40, A=50, and A=60. These lines intersect the solid line at F(A) values of 0.4, 0.5, and 0.6 respectively. The area under the solid line is a triangle with base 1 and height 100, with a total area of 50.](3ae8c7e35a46d9336931efdd39c3760c_img.jpg)

A graph of a linear function F(A) on a coordinate system. The horizontal axis is labeled F(A) and ranges from 0 to 1. The vertical axis is labeled A and ranges from 0 to 100. A solid line starts at the origin (0,0) and goes up to (1,100). Three horizontal dashed lines are drawn at A=40, A=50, and A=60. These lines intersect the solid line at F(A) values of 0.4, 0.5, and 0.6 respectively. The area under the solid line is a triangle with base 1 and height 100, with a total area of 50.

a) The area above the line  $A = 40$  and below  $F(A)$  has area  $= 60 * 0.6 * 1/2 = 18$

$$18/50 = 0.36$$

b) The area above the line  $A = 50$  and below  $F(A)$  has area  $= 50 * 0.5 * 1/2 = 12.5$

$$12.5/50 = 0.25$$

c) The area above the line  $A = 60$  and below  $F(A)$  has area  $= 40 * 0.4 * 1/2 = 8$   
 $8/50 = 0.16$

Calculus:

First we normalize the Lee diagram so that the area under the curve (the distribution of the probability of aggregate loss) adds to 1. Then

$$\text{Let } Y = A/E \sim \text{Uniform}(0,2)$$

$$\text{Then } f(y) = 0.50$$

$$(a) \quad r = 40/50 = 0.80 \quad \phi(0.80) = \int_{0.8}^2 0.50(y - 0.80)dy = \mathbf{0.36}$$

$$(b) \quad r = 50/50 = 1 \quad \phi(1) = \int_1^2 0.50(y - 1)dy = \mathbf{0.25}$$

$$(c) \quad r = 60/50 = 1.20 \quad \phi(1.20) = \int_{1.2}^2 0.50(y - 1.20)dy = \mathbf{0.16}$$

4.

$$E = 10 \quad Y = A/E \sim \text{Expon}(\text{mean} = 1) \quad f(y) = e^{-y}$$

$$\psi(r) = \int_0^r (r - y)e^{-y}dy$$

$$(a) \quad r = 5/10 = 0.50 \quad \psi(0.50) = \mathbf{0.1065}$$

$$(b) \quad r = 10/10 = 1 \quad \psi(1) = \mathbf{0.3679}$$

$$(c) \quad r = 15/10 = 1.5 \quad \psi(1.5) = \mathbf{0.7231}$$

5.

![A graph showing the relationship between the Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has a tick mark at 'r'. The x-axis is labeled 'F(y)' and has tick marks at '0' and '1'. A curve starts at the origin (0,0) and increases monotonically, passing through the point (F(r), r). The area under the curve is divided into two regions: the area to the left of the curve is labeled ψ(r), and the area to the right of the curve is labeled φ(r). The area between the horizontal line at y=r and the curve is labeled r-ψ(r) or 1-φ(r).](4c86e4dfdc04db280a2a1ab345358130_img.jpg)

A graph showing the relationship between the Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has a tick mark at 'r'. The x-axis is labeled 'F(y)' and has tick marks at '0' and '1'. A curve starts at the origin (0,0) and increases monotonically, passing through the point (F(r), r). The area under the curve is divided into two regions: the area to the left of the curve is labeled ψ(r), and the area to the right of the curve is labeled φ(r). The area between the horizontal line at y=r and the curve is labeled r-ψ(r) or 1-φ(r).

6.

- (a)  $\Phi(R) = A$
- (b)  $\Phi(S) = A + D + E$
- (c)  $\psi(R) = B + C + F$
- (d)  $\psi(S) = F$

7.

- (a) Step 1: Expected loss ratio = Average Loss Ratio =  
 $(20\%+40\%+40\%+60\%+80\%+80\%+120\%+200\%)/8 = 80\%$   
 So for each risk,  $r = \text{loss ratio}/0.8$

To solve this precisely, we need to look at every slice at which there is at least one data point, plus all the other points we want factors for:

| r   | # Risks<br>from<br>prior to | # Risks<br>Above | % Risks<br>Above | Difference<br>in r | $\Phi(r)$       | $\psi(r) = \Phi(r)+r-1$ |
|-----|-----------------------------|------------------|------------------|--------------------|-----------------|-------------------------|
| 0   | 0                           | 8                | 1.000            | 0.25               | 1.00            | 0                       |
| .25 | 1                           | 7                | 0.875            | 0.25               | .75             | 0                       |
| .50 | 2                           | 5                | 0.625            | 0.25               | .53125          | .03125                  |
| .75 | 1                           | 4                | 0.500            | 0.25               | .25+.5*.25=.375 | .375+.75-1=.125         |
| 1.0 | 2                           | 2                | 0.250            | 0.50               | .125+.25*.5=.25 | 0.25+1-1=.25            |
| 1.5 | 1                           | 1                | 0.125            | 0.50               | .125+.125*1=.25 | 0.125+1.5-1=0.625       |
| 2.0 | 0                           | 1                | 0.125            | 0.50               | 0+.125*.5=.0625 | .0625+2-1=1.0625        |
| 2.5 | 1                           | 0                | 0.000            | 0.50               | 0               | 0+2.5-1=1.5             |
| 3.0 | 0                           | 0                | 0.000            | 0                  | 0               | 0+3-1=2                 |

|       |   |  |  |  |  |  |
|-------|---|--|--|--|--|--|
| Total | 8 |  |  |  |  |  |
|-------|---|--|--|--|--|--|

This can then be summarized as:

| r     | $\Phi(r)$             | $\psi(r) = \Phi(r)+r-1$ |
|-------|-----------------------|-------------------------|
| 0     | 1.00                  | 0                       |
| .50   | .53125                | .03125                  |
| 1.0   | .25                   | .25                     |
| 1.5   | $0.0625+.125*.5=.125$ | $0.125+1.5-1=0.625$     |
| 2.0   | $0+.125*.5=.0625$     | $0.0625+2-1=1.0625$     |
| 2.5   | 0                     | $0+2.5-1=1.5$           |
| 3.0   | 0                     | $0+3-1=2$               |
| Total |                       |                         |

Note what happens if we just look at intervals of 0.5

| r     | Risks from prior to | # Risks Above | % Risks Above | fference in r | $\Phi(r)$             | $\psi(r) = \Phi(r)+r-1$ |
|-------|---------------------|---------------|---------------|---------------|-----------------------|-------------------------|
| 0     | 0                   | 8             | 1.000         | 0.5           | 1.0625                | .0625                   |
| .50   | 3                   | 5             | 0.625         | 0.5           | .5625                 | .0625                   |
| 1.0   | 3                   | 2             | 0.250         | 0.5           | .25                   | .25                     |
| 1.5   | 1                   | 1             | 0.125         | 0.5           | $0.0625+.125*.5=.125$ | $0.125+1.5-1=0.625$     |
| 2.0   | 0                   | 1             | 0.125         | 0.5           | $0+.125*.5=.0625$     | $0.0625+2-1=1.0625$     |
| 2.5   | 1                   | 0             | 0.000         | 0.5           | 0                     | $0+2.5-1=1.5$           |
| 3.0   | 0                   | 0             | 0.000         | 0             | 0                     | $0+3-1=2$               |
| Total | 8                   |               |               |               |                       |                         |

All looks well until we get to  $r = 0.5$ . Then we end up with 0.5625 for the charge, rather than 0.53125. The calculated charge is too large by 0.03125. The error grows at  $r=0$  to 0.0625. This is because when we “integrate” under the curve, we are assuming each piece we are adding is a rectangle. But if we look at the Lee diagram of the outcomes:

![A bar chart titled 'Entry Ratio = r' vs 'Claim Number (ranked by size)'. The x-axis shows claim numbers 1 through 8. The y-axis shows the entry ratio from 0 to 3. The bars represent the cumulative distribution function. The first bar (claim 1) has a height of 0.5. The second bar (claim 2) has a height of 0.5. The third bar (claim 3) has a height of 0.5. The fourth bar (claim 4) has a height of 1.0. The fifth bar (claim 5) has a height of 1.0. The sixth bar (claim 6) has a height of 1.0. The seventh bar (claim 7) has a height of 1.5. The eighth bar (claim 8) has a height of 2.5. A blue shaded area is shown above the first three bars, with arrows pointing to it from the text 'Extra pieces in the boxes, but above the area representing the outcomes.'](ba99363c7d61d24290635b47b71e41c2_img.jpg)

Entry Ratio = r

Extra pieces in the boxes, but above the area representing the outcomes.

Claim Number (ranked by size)

A bar chart titled 'Entry Ratio = r' vs 'Claim Number (ranked by size)'. The x-axis shows claim numbers 1 through 8. The y-axis shows the entry ratio from 0 to 3. The bars represent the cumulative distribution function. The first bar (claim 1) has a height of 0.5. The second bar (claim 2) has a height of 0.5. The third bar (claim 3) has a height of 0.5. The fourth bar (claim 4) has a height of 1.0. The fifth bar (claim 5) has a height of 1.0. The sixth bar (claim 6) has a height of 1.0. The seventh bar (claim 7) has a height of 1.5. The eighth bar (claim 8) has a height of 2.5. A blue shaded area is shown above the first three bars, with arrows pointing to it from the text 'Extra pieces in the boxes, but above the area representing the outcomes.'

We can see that there are two extra pieces in the boxes, but above the area representing the outcomes. Each has area =  $0.25 \times (1/8) = 0.03125$ . That is the source of the extra in the calculation. This is an example of the problem described in footnote 30 on page 66.

(b) 70% L/R  $\rightarrow r=0.875$

It helps to look again at the Lee diagram to understand the situation

![A bar chart titled 'Entry Ratio = r' vs 'Claim Number (ranked by size)'. The y-axis ranges from 0 to 3 with increments of 0.5. The x-axis shows claim numbers 1 through 8. The bars have heights: 0.25, 0.5, 0.5, 0.75, 1.0, 1.0, 1.5, and 2.5. A horizontal line is drawn at r = 0.875, intersecting the bars for claim numbers 5, 6, 7, and 8.](fe8840a79cf6b30f8b2284064f3d2a36_img.jpg)

| Claim Number (ranked by size) | Entry Ratio = r |
|-------------------------------|-----------------|
| 1                             | 0.25            |
| 2                             | 0.5             |
| 3                             | 0.5             |
| 4                             | 0.75            |
| 5                             | 1.0             |
| 6                             | 1.0             |
| 7                             | 1.5             |
| 8                             | 2.5             |

A bar chart titled 'Entry Ratio = r' vs 'Claim Number (ranked by size)'. The y-axis ranges from 0 to 3 with increments of 0.5. The x-axis shows claim numbers 1 through 8. The bars have heights: 0.25, 0.5, 0.5, 0.75, 1.0, 1.0, 1.5, and 2.5. A horizontal line is drawn at r = 0.875, intersecting the bars for claim numbers 5, 6, 7, and 8.

There are a few ways to approach this problem. First, we will solve it precisely, using the horizontal method:

The width of the distribution between 1.0 and 0.875 is 0.5, four of the 8 claims. So the additional insurance charge is 0.5 times the height of the additional band, or  $(1-0.875) \times 0.5 = 0.0625$ . so

$$\Phi(0.875) = \Phi(1.0) + 0.0625 = 0.25 + 0.0625 = \mathbf{0.3125}$$

We could also have interpolated. Had we estimated  $\Phi(0.875)$  with a linear interpolation, we would have gotten:

$$(\Phi(0.5) \times (1-0.875) + \Phi(1.0) \times (0.875 - 0.5)) / (1.0 - 0.5) = (0.53125 \times 0.125 + 0.25 \times 0.375) / (0.5) = \mathbf{0.3203}$$

Note that the interpolation does not give the exact answer, but is reasonably close.

Since we are interested in the insurance charge at a single point, we might also use the vertical method.

| Risk    | Actual<br>Agg. L/R | Entry<br>Ratio | Excess of<br>$r = 70/80 = 0.875$ | Excess of<br>$r = 110/80 = 1.375$ |
|---------|--------------------|----------------|----------------------------------|-----------------------------------|
| 1       | 20%                | 0.25           | 0                                | 0                                 |
| 2       | 40                 | 0.50           | 0                                | 0                                 |
| 3       | 40                 | 0.50           | 0                                | 0                                 |
| 4       | 60                 | 0.75           | 0                                | 0                                 |
| 5       | 80                 | 1.00           | 0.125                            | 0                                 |
| 6       | 80                 | 1.00           | 0.125                            | 0                                 |
| 7       | 120                | 1.50           | 0.625                            | 0.125                             |
| 8       | 200                | 2.50           | 1.625                            | 1.125                             |
| Total:  |                    |                | <b>2.500</b>                     | <b>1.250</b>                      |
| Average |                    |                | <b>0.3125</b>                    | <b>0.15625</b>                    |

- (c)  $\psi(0.875) = 0.3125 + 0.875 - 1 = \mathbf{0.1875}$
- (d) 110% L/R  $\rightarrow r=1.375$ .  $\Phi(1.375) = \mathbf{0.15625}$  (work done in section b)
- (e)  $\psi(1.375) = 0.15625 + 1.375 - 1 = \mathbf{0.53125}$

### 8. Using Parameterized distributions to develop Tables M

#### Advantages:

1. When you don't have a statistically credible group of policies to base your pricing on, but you have an idea of what shape the distribution of outcomes is likely to approximate, you can fit curves to what data you have.
2. When data is thin, and you have large gaps between empirical entry ratios, you don't have to rely on linear interpolation.
3. Even with large body of data, fitting distributions to frequency and severity can help develop charges that are consistent with the excess charges.

#### Disadvantages:

1. If the assumptions underlying the selected distribution aren't close enough to reality, you can generate plausible, internally consistent, precise, but misleading charges.
2. It might be more computationally complex to build a model than to use empirical data for the desired degree of precision.

### 9.

- (a)  $M_D$  Charge at R = **G**
- (b)  $M_D$  Savings at S = **Q+T+U**
- (c) Per-Occ XS Charge at D = **A+D+E+J+L+N+T+U**

### 10.

- (a)  $\{40,000 + (1.1)(150,000)\} (1.05) = 215,250$ .

*Comment: The insured benefited from neither the maximum premium nor the accident limit.*

- (b)  $\{40,000 + (1.1)(200,000)\} (1.05) = 273,000$ . Limited to the maximum of \$250,000.

*Comment: The insured benefited from the maximum premium.*

- (c)  $\{40,000 + (1.1)(100,000)\} (1.05) = 157,500$ .

*Comment: The insured benefited from the accident limit.*

- (d)  $\{40,000 + (1.1)(200,000)\} (1.05) = 273,000$ . Limited to the maximum of \$250,000.

*Comment: The accident limit decreased the losses entering the calculation, but the insured ended up paying the maximum premium anyway.*

*The last case is an example of the “overlap” between the effects of the maximum premium and the accident limit. In some years, even though there are large accidents, the accident limit will not provide any additional benefit to the insured beyond that provided by the maximum premium. In other words, for large accidents the accident limit and the maximum premium overlap*

11.

- (a)  $\{400,000 + (1.1)(150,000)\}(1.05) = 593,250$ . The insured pays the minimum premium, \$650,000.

- (b)  $\{400,000 + (1.1)(100,000)\}(1.05) = 535,500$ . The insured pays the minimum premium, \$650,000.

*The last case is an example of the “underlap” between the effects of the minimum premium and the accident limit. In some years, even though there are large accidents, the accident limit will not provide any benefit to the insured due to the minimum premium. This has a relatively small overall impact.*

12.

$$E=150,000$$

$$\text{Agg Limit} = 300,000$$

$$R = 300 / 150 = 2.0$$

$$\Phi(2.0) \times 150,000 = 15,000$$

$$\Phi(2.0) = 0.10$$

With only Per-Occurrence Deductible:

$$k * E = 50,000 \rightarrow k = 50,000 / 150,000 = 0.333$$

Note that the Aggregate Limit of 300,000 is three times the expected limited loss of 100,000, so the entry ratio,  $r$ , of the limited loss distribution is  $300,000 / 100,000 = 3$ .

![A graph showing the relationship between Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has a horizontal dashed line at y=1. The x-axis is labeled 'F(y)' and ranges from 0 to 1. Two curves originate from (0,0): the upper curve is labeled F(y) and the lower curve is labeled F_{100K}(y). The area between the curves is divided into regions A, B, and C. Region A is the area under F(y) and above the dashed line. Region B is the area between the two curves above the dashed line. Region C is the area under F_{100K}(y) and above the dashed line. Region D is the area under F_{100K}(y) and below the dashed line. Labels include: 'R = 2 unlimited' and 'R = 3 limited' on the y-axis; 'K_{100K} = A+B = 0.33' in region A; 'phi(2) = B+C = 0.1' near the top of the F(y) curve; and 'phi_{100K}(3) = C >= 0' near the top of the F_{100K}(y) curve.](0f4879d336bad8b1801dee947a7dc617_img.jpg)

A graph showing the relationship between Entry Ratio (y-axis) and F(y) (x-axis). The y-axis is labeled 'Entry Ratio' and has a horizontal dashed line at y=1. The x-axis is labeled 'F(y)' and ranges from 0 to 1. Two curves originate from (0,0): the upper curve is labeled F(y) and the lower curve is labeled F\_{100K}(y). The area between the curves is divided into regions A, B, and C. Region A is the area under F(y) and above the dashed line. Region B is the area between the two curves above the dashed line. Region C is the area under F\_{100K}(y) and above the dashed line. Region D is the area under F\_{100K}(y) and below the dashed line. Labels include: 'R = 2 unlimited' and 'R = 3 limited' on the y-axis; 'K\_{100K} = A+B = 0.33' in region A; 'phi(2) = B+C = 0.1' near the top of the F(y) curve; and 'phi\_{100K}(3) = C >= 0' near the top of the F\_{100K}(y) curve.

Together, the combined charge would be  $0.333+0.10 = 0.433$ , or  $0.433 \times 150,000 = 65,000$ . However, the combined charge is very unlikely to be equal to 65,000. It will generally be less than 65,000 because there is overlap between the two charges, as shown by region B in the graph.

13.

- a) The expected primary losses = 20,000.  
Entry ratio =  $40,000/20,000=2.0$   
The aggregate excess loss factor is 0.04, so the insurance charge =  $0.04 \times 20,000=800$ .  
(Which would be in addition to the \$20,000 charge for the per-occurrence deductible, for a total expected loss cost within the policy of \$20,800.)
- b) The expected primary losses = 30,000.  
Entry ratio =  $40,000/30,000=1.333$ .  
Interpolate the aggregate excess loss factors on the table to get  
 $(1/3)*0.22 + (2/3)*.12 = 0.1533 =$  the aggregate excess loss factor.  
So the insurance charge is  $0.1533 \times 30,000 = 4600$   
(which would be in addition to the \$10,000 charge for the per-occurrence deductible, for a total expected loss cost within the policy of \$14,600.)
- c) The insurer will charge more for (a) because even though the aggregate insurance charge is less than (b), the insured has a much smaller per-occurrence deductible which transfers more expected losses to the insurer.

14.

![A graph showing the relationship between the entry ratio r and the normalized area of loss. The vertical axis is labeled 'r = Entry Ratio to unlimited loss' and has tick marks at 1.5, 1.6, and 2. The horizontal axis is labeled 'F(r)' and has tick marks at 0 and 1. Two lines originate from the origin (0,0). The upper line passes through the point (1, 2). The lower line passes through the point (1, 1.6). A horizontal dashed line is drawn at r = 1.5. This line intersects the upper line at a point labeled 'B' and the lower line at a point labeled 'E'. The area between the two lines from F(r)=0 to F(r)=1 is divided into three regions: 'A' is the area below the lower line; 'B' is the area between the two lines from F(r)=0 to the point where the dashed line intersects the upper line; 'C' is the area below the lower line from the point where the dashed line intersects the lower line to F(r)=1. The area between the two lines from the point where the dashed line intersects the lower line to F(r)=1 is labeled 'D'. The area between the lower line and the dashed line from the point where the dashed line intersects the lower line to F(r)=1 is labeled 'E'.](f72d881958a5863f9fea850513142c46_img.jpg)

A graph showing the relationship between the entry ratio r and the normalized area of loss. The vertical axis is labeled 'r = Entry Ratio to unlimited loss' and has tick marks at 1.5, 1.6, and 2. The horizontal axis is labeled 'F(r)' and has tick marks at 0 and 1. Two lines originate from the origin (0,0). The upper line passes through the point (1, 2). The lower line passes through the point (1, 1.6). A horizontal dashed line is drawn at r = 1.5. This line intersects the upper line at a point labeled 'B' and the lower line at a point labeled 'E'. The area between the two lines from F(r)=0 to F(r)=1 is divided into three regions: 'A' is the area below the lower line; 'B' is the area between the two lines from F(r)=0 to the point where the dashed line intersects the upper line; 'C' is the area below the lower line from the point where the dashed line intersects the lower line to F(r)=1. The area between the two lines from the point where the dashed line intersects the lower line to F(r)=1 is labeled 'D'. The area between the lower line and the dashed line from the point where the dashed line intersects the lower line to F(r)=1 is labeled 'E'.

a)  $\Phi_D^*(1.5) = B + D + E$   
 $\psi_D^*(1.5) = A + B$

- b) The normalized area of the total loss (the area of the large triangle,  $B+C+D+E$ ) is 1. The area of the limited loss is  $400/500$  times the total, or 0.8. It is also the area of the small triangle,  $C + E$ .  
 So the area of  $B + D$  is 0.2.

The area of  $E$  is the  $\frac{1}{2}$  the height times the length. The height is  $1.6 - 1.5 = 0.1$ .

$E$  is the same shape as  $C+E$ , which has height 1.6 and length 1. So the length of  $E$  must be  $(0.1/1.6) = 0.0625$ .

So the area of  $E$  is  $0.1 * 0.0625 / 2 = 0.003125$ .

So  $\Phi_D^*(1.5) = B + D + E = 0.2 + 0.003125 = 0.203125$

And

$\psi_D^*(1.5) = \Phi_D^*(1.5) + r - 1 = 0.203125 + 1.5 - 1 = 0.703125$ .

15.

- a)  $T+U+J+L+N+D+E+A+G$   
 b)  $Q+U+T$

16.

#### Advantages:

- When large tables were awkward (either as a vast pile of paper or a computer file that was difficult to store) ICRL allowed a single unlimited Table M to be used to generate reasonable charges that would otherwise have required a large number of Tables M<sub>D</sub>.
- The ICRL procedure is an expedient way of approximating Table M<sub>D</sub> when a suitable Table M<sub>D</sub> is unavailable. For example, this method can be used to adjust a Table M developed based on one book of business to a similar book for which there isn't adequate data to develop its own Tables M.

#### Disadvantages:

- It is only an approximation to Table M<sub>D</sub> and may introduce additional error in the estimate of the charge for the aggregate limit.

17.

- a) Expected Unlimited Losses = 1,000,000 x 0.75 = 750,000  
Expected Limited Losses = 750,000 x (1 - 0.2) = 600,000  
 $r = 1,200,000 / 600,000 = 2.0 \rightarrow \text{Ins Charge} = 0.04 \times 600,000 = 24,000$
- b) Loss Group Adjustment Ftr =  $\frac{1+0.8(0.2)}{1-0.2} = 1.45$

Losses used in group selection = 750,000 x 0.90 x 1.45 = 978,750  $\rightarrow$  ELG 29  
 $r = 1,200,000 / 600,000 = 2.0$   
Insurance Charge Factor = 0.242  
Total Expected Loss Cost = 0.2(750,000) + 0.242(600,000) = 295,200

18.

The State/Hazard Group Relativity makes an adjustment to reflect for differences in claim size by class of business and geographic location. For a given expected loss size, it treats a risk expected to have more severe individual claims as if it is smaller (and thus more variable) than a risk with the same expected loss resulting from a larger number of less severe claims.

The implicit assumption with using the State/Hazard Group Relativity is that the actual severity distribution has a similar shape as that which is used to determine the insurance charges, and differs mostly due to scale. If the difference is extreme, the severity distribution may need to be adjusted, potentially requiring a different Table M

19.

The Table M charge will be larger when the variance of the loss distribution is larger, all else being equal – see Exhibit 3.32.

20.

a) The insurance charge would increase. The toxic paint claims have a low frequency and a very high severity compared to the historical claims. This means they greatly increase the variance of the severity, which increases the variance of the aggregate losses. In particular, with the original assumptions, an insured would have had to experience twice the expected claims frequency to breach the aggregate, but with the revised understanding of the liability, a single large claim would be almost enough to do so. This will result in a much larger insurance charge at an entry ratio of 2.0.

b) A per-occurrence limit, assuming it is high enough to be above the historical losses, but substantially limits the toxic paint claims, would shift losses from the aggregate limit charge to the per-occurrence charge. Therefore, the charge for the aggregate deductible would decrease.

### Chapter 4 Answers

1. The fair premium should be lower, as the insured is responsible for a significant fraction of the risk.
2. Because you need to price for the risk involved and the expenses of monitoring the claims experience. The risk includes the risk that the insured knows more about the liability than you do. The expenses may include annual or monthly reports to the insured whether or not any losses breach the insurable threshold.
3. Given a large deductible WC policy with the following features:
  - \$2M expected total loss
  - Expected average severity of \$10,000 per claim
  - The insured retains 86% of expected loss under the per-occurrence deductible (14% is expected to be excess of the deductible)
  - There is a limit on the aggregate deductible retained by the insured of \$3M

b.) What is the insurance charge for the aggregate limit?

If the account is larger than the pricing actuary realized, and the expected total losses should have been \$2.5M, what should the insurance charge have been?

