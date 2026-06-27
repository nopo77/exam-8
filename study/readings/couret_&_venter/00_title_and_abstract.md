

# USING MULTI-DIMENSIONAL CREDIBILITY TO ESTIMATE CLASS FREQUENCY VECTORS IN WORKERS COMPENSATION

BY

JOSE COURET AND GARY VENTER

## ABSTRACT

The US workers compensation system is different from those in many countries, but it is reinsured in the world-wide market and so has international impact. From its origin in the early 20<sup>th</sup> century it has been a laboratory for actuarial credibility techniques. In recent years deductibles have been increasing, so that fairly high excess coverage is now commonplace. This puts growing emphasis on estimation of the percentage of loss that is excess of high deductibles. A key element of the excess percentage is the frequency of loss by injury type. Fatalities and permanent disabilities cost more than other injury types, so when they have high relative frequency, more of the claims cost arises from large losses. The vector of claim frequency by injury type can be estimated by class of business using multi-dimensional credibility techniques. Historically the fraction of costs excess of various retentions has been calculated for large groups of classes (hazard groups) and not individual classes. We show, by testing a hold-out sample, that credibility estimation by class does produce additional information in comparison to a widely-used seven-hazard-group system.

# USING MULTI-DIMENSIONAL CREDIBILITY TO ESTIMATE CLASS FREQUENCY VECTORS IN WORKERS COMPENSATION

The regression framework for credibility started with Hachemeister (1975) and has generated an impressive literature since. We apply a small portion of this to estimate vectors of relative frequency by injury type for classes of US workers compensation insureds. Credibility is non-parametric so it is not usually considered necessary to look at the actual distributions of the data or the parameters, but since it is based on minimizing squared error, it may be inappropriate for heavy-tailed distributions, where relative error is more important. Credibility on the logarithms of the data is often suggested in that case. Here, however, credibility is applied to loss frequencies, which are probably safely within the applicability of squared error. Some performance tests show that credibility does help with this estimation.

US workers compensation classes are based on industry breakdowns and in some cases even particular occupations within industries, to the extent that these have different accident potential. For instance, workers comp rates and excess losses for casting can differ significantly depending on whether you are casting pig iron, pottery, broken bones, dice or actors. Also, the occupation class rates vary by state, but usually not among the regions within a state.

Estimating loss costs by class has been a focus of actuaries since the workers compensation system started in 1912. In fact early versions of credibility theory and even the creation of the Casualty Actuarial Society arose to deal with workers compensation issues. The recognition that large individual claims are a driving force in loss costs also came early, with an excess reinsurance pool formed by 1914. Rating plans that charge large manufacturers their actual small losses plus expected large losses also have a long history, so excess rates are not a new topic. However true excess coverage is newer, and is now a large part of the workers compensation business. Thus there is a growing interest in estimation of excess loss costs.

This is driving an exploration of methodologies that might be useful for excess loss estimation. Insurance companies in the US report class-by-state data to rating bureaus. These bureaus also license data that can be used in studies of loss risk, but the licenses typically do not allow further dissemination of the data. Rating bureaus as well as large insurers and reinsurers are all investigating ways to improve the estimation of excess costs for the class/state cells. Traditionally this estimation used a four-hazard-group breakout for estimation of injury-type<sup>1</sup> frequencies. Hazard groups are collections of classes similar in their excess loss potential, relative to total losses. There are significant claims-cost differences across injury types, so estimating the frequency of claims by type for each hazard group has been the main emphasis of excess rating.

Recent innovations in excess rating include bureaus using more hazard groups – as many as nine, with seven being the industry standard – to get more homogeneity in loss potential; looking at possible differences in claims costs within an injury type across classes or hazard groups; and looking for better ways to combine data from different state systems. Some insurers and reinsurers have tried to produce individual class excess rates, at least for the larger classes. We compare the proposed class credibility approach to the seven-hazard-group frequency-only method, and find that it does provide improved estimation.

There are some variations in the way injury types are defined. We use the following injury types: fatal, permanent total injury, major permanent partial impairment, minor permanent partial, temporary total, and medical-only. We abbreviate these F, PT, major, minor, TT, and med. A typical breakout of relative frequency and severity by injury type, using TT as the base, is:

---

<sup>1</sup> A categorization of injuries by severity, defined in more detail below.

| Type:                    | F     | PT    | Major | Minor | TT   | Med |
|--------------------------|-------|-------|-------|-------|------|-----|
| FREQUENCY RELATIVE TO TT | 0.006 | 0.006 | 0.085 | 0.37  | 1.00 | 4.3 |
| SEVERITY                 | 60    | 125   | 40    | 4     | 1.00 | 0.2 |

These numbers are illustrative and can vary significantly by state and class, but they show the extent to which the excess costs are driven by the rare but expensive serious injuries. Excess losses above different retentions will be driven by different mixes of injury types, since minor – for example – is much more frequent but less severe than F or PT. Thus getting a good estimate of the class relative frequency vector is a key step in calculating excess loss potential. We will focus on estimating the vector of relativities of F, PT, major, and minor to TT.

