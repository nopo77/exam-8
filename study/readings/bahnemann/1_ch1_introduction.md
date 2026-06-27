---
paper: bahnemann
chapter: 1
title: 1. Introduction
topics: [probability_spaces, random_variables, probability_distributions, mathematical_expectation, moment_generating_functions, mixed_distributions, conditional_probability, joint_distributions]
key_formulas: [conditional_probability_formula, cumulative_distribution_function, moment_generating_function, variance_formula]
---

> **TL;DR**
> - A probability space (Ω, S, P) assigns probabilities to events; random variables map outcomes to real numbers and are characterized by CDF F(x) = Pr{X ≤ x}, which is right-continuous, non-decreasing, with limits 0 and 1
> - Claim-size variables can be discrete, continuous, or **mixed** (e.g., a continuous distribution with a discrete lump at 0 or at a policy limit — this mixed type recurs throughout Chapters 2–6)
> - Expected value E[g(X)] = ∫g(x)dF(x) (Riemann–Stieltjes form unifies discrete and continuous); E[aX+b]=aE[X]+b; E[X+Y]=E[X]+E[Y] always; E[XY]=E[X]E[Y] for independent X,Y
> - Var[X] = E[X²] − (E[X])²; MGF M(t) = E[e^{tX}] uniquely determines a distribution and yields moments via M^(m)(0) = E[X^m]
> - Conditional probability P(E|F) = P(E∩F)/P(F); independence means P(E∩F) = P(E)P(F)

# 1. Introduction

Property/casualty insurance policies are written to cover policyholder losses that arise from certain unpredictable events. These events, which occur more or less randomly over time, must happen during the time period the policy is in effect in order to qualify as insured events. To cite just a few possibilities, an insured event could be property damage due to fire or storm, medical treatment due to illness, or personal injury due to accident or professional malpractice. The occurrence of such an event can trigger a claim against the policy.

In order to determine a reasonable premium charge for a policy, actuaries must be able to quantify the random aspects of the underlying claim process. In particular, they must be able to construct appropriate probability models for the incidence and size of claims, topics which are the subjects of Chapters 3 and 2, respectively. We begin here in Chapter 1 with a brief summary of basic probability concepts.

***A Note on Notation.*** In addition to providing a review of the probability prerequisites, this chapter establishes most of the notational conventions used throughout the subsequent chapters. In general, the notation is consistent with standard usage employed by expositors of probability and mathematical statistics. Probability spaces are denoted by upper-case Greek letters and probability events are denoted by upper-case Roman letters. The probability of a general random-variable-related event is usually denoted by  $\Pr\{\cdot\}$ . As usual, cumulative probability functions are denoted by  $F(\cdot)$  and probability density functions by the associated lower-case Roman letter:  $f(\cdot)$ . For most parametric distributional families, parameters are denoted by lower-case Greek letters. Random variables are denoted by upper-case Roman letters, with  $X$  or  $Y$  denoting a claim-size variable,  $N$  a claim-count variable, and  $S$  an aggregate-loss variable. In every case, the introduction of a concept is accompanied by sufficient mathematical display to establish the applicable notational conventions.

## 1.1. Probability Spaces

Consider an experiment of chance for which the outcome cannot be predicted in advance. For example, tossing a coin and observing whether it lands Heads ( $H$ ) or Tails ( $T$ ) is an experiment with a set of two possible, but unpredictable outcomes:  $\{H, T\}$ . The roll of a single die or pair of dice, the blind selection of objects from a well-mixed collection such as cards from a shuffled deck, the time to failure of an electronic or mechanical component, or the occurrence of an insurance claim—each

can be interpreted as an experiment of chance with outcomes that cannot be predicted in advance.

A set  $\Omega$  of all possible distinct outcomes of an experiment of chance is called a **sample space** for the experiment. Each element  $\omega$  of  $\Omega$  is referred to as an **elementary outcome**. A performance of the experiment, obtaining one of the elementary outcomes as a result, is a **trial** of the experiment.

Note that different sets of elementary outcomes may be defined for any given experiment, depending on what attributes of the outcomes are of particular interest. For example, if an experiment consists of tossing a coin twice in succession, then one set of elementary outcomes could consist of all ordered pairs of Heads and Tails:

$$\Omega_1 = \{HH, HT, TH, TT\}.$$

If the order is unimportant, then the elementary outcomes could be the unordered pairs of Heads and Tails:  $\Omega_2 = \{\{H, H\}, \{H, T\}, \{T, T\}\}$ . Alternatively, if only the number of Heads obtained is material, then  $\Omega_3 = \{0, 1, 2\}$  would suffice as a sample space. However, sometimes selecting a sample space for which the elementary outcomes can be assigned equal probabilities makes all subsequent probability calculations easier—see Example 1.2(a).

An **event**  $E$  for an experiment of chance is a subset of the sample space:  $E \subseteq \Omega$ . If, at a trial of the experiment, outcome  $\omega \in \Omega$  is obtained and it also happens that  $\omega \in E$ , then one says that **event  $E$  has occurred**.

**Example 1.1.** (a) An experiment consists of tossing a coin three times in succession and observing the resulting sequence of Heads and Tails. A sample space consists of eight elementary outcomes, each an ordered triple of  $H$ s and  $T$ s:

$$\Omega = \{HHH, THH, HTH, HHT, HTT, THT, TTH, TTT\}. \quad (1.1)$$

Thus, if on the first and second tosses the coin falls Heads and on the third Tails, then the outcome of the trial is  $HHT$ . The event  $E$  of obtaining at most one Heads among the three tosses is defined by the set  $E = \{HTT, THT, TTH, TTT\}$ .

(b) Another experiment consists of rolling a pair of dice and observing the number of spots on each die in turn (a *die* being a cube whose six faces are marked with one through six spots). There are 36 elementary outcomes in the sample space:

$$\begin{aligned} \Omega = \{ & (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), \\ & (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), \\ & (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6) \}. \end{aligned} \quad (1.2)$$

For example, if one observes five spots on the first die and two spots on the second, then the outcome of the trial is  $(5,2)$ .

The set  $E = \{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$  defines the event that the sum of the spots is seven. The event

$$F = \{(1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (4,1), (4,2), (4,3), (4,5), (4,6)\}$$

occurs when four spots are obtained on at least one die. Having obtained the outcome (5,2) on a trial, we observe that event  $E$  has occurred because  $(5,2) \in E$  and that event  $F$  has not occurred because  $(5,2) \notin F$ .

(c) An insurance policy pays at most \$200,000 for an incurred claim. The issuing of such a policy can be interpreted as a trial of an experiment of chance for which the uncertain outcome is the occurrence (or non-occurrence) of one or more claims. A reasonable set of elementary outcomes would be the number of incurred claims:  $\Omega_1 = \{0, 1, 2, 3, \dots\}$ . In addition, the occurrence of a claim can be interpreted as another experiment of chance for which the size of the claim is the unpredictable outcome. For this experiment the sample space can be expressed as an interval of real numbers:  $\Omega_2 = [0; 200,000]$ .<sup>1</sup> ■

Generally, most—but not necessarily all—subsets of  $\Omega$  can be considered events for an experiment with sample space  $\Omega$ . In order to define probabilities for the events of an experiment of chance in a reasonable way, the set  $S$  of events must have certain properties. In particular, (i)  $S$  must contain  $\Omega$  and (ii)  $S$  must contain the complement  $E^c = \{\omega \in \Omega : \omega \notin E\}$  whenever  $E \in S$ . Moreover, (iii)  $S$  must contain the union of every countable collection of events in  $S$ .<sup>2</sup> A collection of sets with these properties is called a  $\sigma$ -algebra or *Borel field*.<sup>3</sup> When the sample space  $\Omega$  is finite or countably infinite, it is customary to assume that  $S$  is just the set of all subsets of  $\Omega$ . The alternate case for the sample space that is uncountably infinite will be discussed briefly in Section 2.

Consider now an experiment of chance with a sample space  $\Omega$  and a set of events  $S$ . To construct a **probability space**  $(\Omega, S, P)$  for the experiment, one must assign a real number  $P(E)$  to each event  $E$ —the **probability** of the event—that serves as a measure of the likelihood of the event will occur in a trial of the experiment. An event that is certain to occur—that is, the event  $\Omega$ —is assigned the maximum probability of 1, and all other events have a probability measure between 0 and 1. A real-valued function  $P$  defined on the set of events  $S$  is called a **probability set function** if it satisfies the following three axioms:

$$\begin{aligned} \mathbf{A}_1 \quad & P(\Omega) = 1, \\ \mathbf{A}_2 \quad & 0 \leq P(E) \leq 1 \text{ for } E \in S, \\ \mathbf{A}_3 \quad & \text{If } \{E_1, E_2, E_3, \dots\} \text{ is a countable collection of disjoint events,} \\ & \text{that is, } E_i \cap E_j = \emptyset \text{ for } i \neq j, \text{ then } P(\bigcup_i E_i) = \sum_i P(E_i). \end{aligned} \quad (1.3)$$

Other properties of function  $P$  can be derived from axioms  $\mathbf{A}_1$ ,  $\mathbf{A}_2$ ,  $\mathbf{A}_3$  and the properties of  $S$ . Verification of the following set of statements is requested in Problem 1.2.

<sup>1</sup> In reality the value of an insurance claim is expressed in whole monetary units (cents or dollars, for example), but it is convenient to assume that all values on the continuous interval are possible outcomes.

<sup>2</sup> We observe the usual convention that a **countable** set  $A$  contains either a finite or countably infinite number of elements. Set  $A$  is **countably infinite** if it can be put into one-to-one correspondence with the set of positive integers.

<sup>3</sup> After the French mathematician, Emile Borel (1871–1956). Borel was a pioneer in the development of modern measure theory and the theory of functions. Throughout the period 1905–1950, he published more than 50 papers and several longer works in probability theory.

### **Properties of $P(x)$**

Assume that  $E, F \in S$  are events for a probability space  $(\Omega, S, P)$ . Then

$$(a) \quad P(E^c) = 1 - P(E). \quad (1.4)$$

$$(b) \quad P(\emptyset) = 0. \quad (1.5)$$

$$(c) \quad P(E) + P(F) = P(E \cup F) + P(E \cap F). \quad (1.6)$$

$$(d) \quad P(E) = P(E \cap F) + P(E \cap F^c). \quad (1.7)$$

$$(e) \quad \text{If } E \subseteq F \text{ then } P(E) \leq P(F). \quad (1.8)$$

$$(f) \quad \text{If } E = \{\omega_1, \omega_2, \omega_3, \dots\} \text{ is a countable subset of } \Omega, \\ \text{then } P(E) = \sum_i P(\{\omega_i\}). \quad (1.9)$$

There are many ways to assign the probability function  $P$  for a probability space  $(\Omega, S, P)$ . Methods range from those founded on *a priori* assumptions about the underlying experiment to methods based on analyses of sample data.

In the special case in which  $\Omega$  is a finite set of  $n$  elementary outcomes, there are often situations in which the outcomes can be assumed, by *a priori* reasoning based on symmetry arguments, to have equal probabilities:  $P(\{\omega\}) = 1/n$  for each  $\omega \in \Omega$ . For example, in the toss of single fair coin (that is, a coin of uniform composition with a symmetrical shape), it is reasonable to assume that outcomes Heads and Tails are equally probable:  $P(H) = P(T) = 1/2$ . Similarly, single objects selected blindly (“at random”) from a collection of  $n$  similar objects can also be assumed to be equally probable. Thus, a specified card drawn from a well-shuffled bridge deck would have probability  $1/52$ .<sup>4</sup>

In the finite case for which the  $n$  elementary outcomes are assigned equal probability, the probability  $P(E)$  of an event  $E$  containing  $m$  elementary outcomes can be calculated by the following formula based on property (1.9) above, where  $\#(E)$  denotes the number of elements in the set  $E$ :

$$P(E) = \sum_{\omega \in E} P(\{\omega\}) = \frac{\#(E)}{\#(\Omega)} = \frac{m}{n}. \quad (1.10)$$

**Example 1.2.** (a) As in Example 1.1(a), an experiment involves tossing a coin three times and observing the sequence of Heads and Tails. The sample space  $\Omega$  is displayed in equation (1.1). If the coin is assumed to be fair, then it makes sense to assign equal probabilities to the eight elementary outcomes in  $\Omega$ :  $P(\{\omega\}) = 1/8$  for each  $\omega \in \Omega$ . Applying formula (1.10) to the event

$$E = \{HTT, THT, TTH, TTT\}$$

yields the probability of obtaining at most one Head:  $P(E) = 4/8 = 0.5000$ .

---

<sup>4</sup> A bridge deck contains 52 distinct playing cards, divided into four suits of 13 cards each: Hearts, Diamonds, Spades, Clubs. Each suit contains 10 numbered cards—Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10—and three Face cards: Jack, Queen, King. Hearts and Diamonds are red cards; Spades and Clubs are black cards.

(b) An experiment consists of drawing a single card at random from a bridge deck, so that each of the 52 elementary outcomes is assigned probability  $1/52$ . We define events  $E$  and  $F$  by

$E$ : card drawn is a Face card    and     $F$ : card drawn is a Heart.

The probabilities of events  $E$ ,  $E^c$ ,  $F$ ,  $E \cap F$  and  $E \cup F$  are calculated from formula (1.10):

$$P(E) = \frac{\#(E)}{52} = \frac{12}{52} = 0.2308,$$

$$P(E^c) = \frac{\#(E^c)}{52} = \frac{52-12}{52} = 0.7692,$$

$$P(F) = \frac{\#(F)}{52} = \frac{13}{52} = 0.2500,$$

$$P(E \cap F) = \frac{\#(E \cap F)}{52} = \frac{3}{52} = 0.0577,$$

$$P(E \cup F) = P(E) + P(F) - P(E \cap F) = \frac{12}{52} + \frac{13}{52} - \frac{3}{52} = \frac{22}{52} = 0.4231.$$

(c) An experiment consists of dealing a hand of five cards at random from a standard deck of 52. Since the order of the cards is immaterial, the number of elementary outcomes is given by the combinatoric formula  ${}_nC_k = n!/[k!(n-k)!]$  for the number of distinct selections (or combinations) of  $k$  objects from a collection of  $n$  distinguishable objects:

$${}_{52}C_5 = \frac{52!}{5!47!} = 2,598,960.$$

Let  $E$  be the event of obtaining five cards from the same suit, and let  $F$  be the event of obtaining no face cards. Thus,

$$P(E) = \frac{(4)({}_{13}C_5)}{{}_{52}C_5} = \frac{5,148}{2,598,960} = 0.0020,$$

$$P(F) = \frac{{}_{40}C_5}{{}_{52}C_5} = \frac{658,008}{2,598,960} = 0.2532,$$

$$P(E \cap F) = \frac{(4)({}_{10}C_5)}{{}_{52}C_5} = \frac{1,008}{2,598,960} = 0.0004. \blacksquare$$

One of the most useful probability concepts is that of **conditional probability**. Often one has partial information about the result of an experiment of chance, information which can alter the likelihood that a particular event could occur. For instance, consider the experiment of Example 1.1(b) involving the roll of a pair of

dice. Assuming that each die is fair, we assign the probability  $1/36$  to each elementary outcome in (1.2). As a result, the probability of obtaining a total of seven spots (event  $E$  in that example) is  $P(E) = 6/36 = 0.1667$ . However, this probability changes if we know that event  $F$  has already occurred, namely, that at least one die shows four spots. In this case, the number of possible elementary outcomes has been reduced from 36 in  $\Omega$  to only 11 in event  $F$ . In addition, there are only two outcomes in  $E$  that are also in  $F$ —that is,  $E \cap F = \{(3,4), (4,3)\}$ —and these remain equally probable. Thus, the conditional probability of  $E$  given that  $F$  has occurred, denoted by  $P(E|F)$ , is

$$P(E|F) = \frac{\#(E \cap F)}{\#(F)} = \frac{2}{11} = 0.1818.$$

However, the first quotient in this equation could also be expressed as

$$\frac{\#(E \cap F)}{\#(F)} = \frac{\#(E \cap F)/\#(\Omega)}{\#(F)/\#(\Omega)} = \frac{P(E \cap F)}{P(F)},$$

which can be generalized to provide a definition for conditional probability. If  $P(F) > 0$ , then  $P(E|F)$ , the probability of event  $E$ , given that event  $F$  has occurred, is defined by

$$P(E|F) = \frac{P(E \cap F)}{P(F)} \quad (1.11)$$

In addition, one can express (1.11) in the following multiplicative form, which is satisfied even when  $P(F) = 0$ :

$$P(E \cap F) = P(F) \cdot P(E|F). \quad (1.12)$$

Equation (1.12) is occasionally useful in calculating  $P(E \cap F)$ , as in Example 1.3(b).

**Example 1.3.** (a) An experiment consists of tossing a fair coin two times in succession and observing the resulting sequence of Heads and Tails. The sample space contains four equally probable outcomes:  $\Omega = \{HH, HT, TH, TT\}$ .

The probability of obtaining two Tails (event  $E$ ), given that at least one of the coins lands Tails (event  $F$ ), is therefore

$$P(E|F) = \frac{P(E \cap F)}{P(F)} = \frac{P(\{TT\})}{P(\{HT, TH, TT\})} = \frac{1/4}{3/4} = \frac{1}{3}.$$

(b) An urn contains eight white chips and five black chips. Two chips are drawn at random without replacing the first chip before drawing the second—at each draw the chips in the urn are equally likely to be drawn.

Let  $E_1$  denote the event that the first chip is white, and let  $E_2$  denote the event that the second chip is white. Clearly,

$$P(E_1) = \frac{8}{13} \quad \text{and} \quad P(E_2|E_1) = \frac{8-1}{13-1} = \frac{7}{12}.$$

Thus, (1.12) implies that the probability  $P(E_1 \cap E_2)$  that both chips are white is

$$P(E_1 \cap E_2) = P(E_1) \cdot P(E_2|E_1) = \frac{8}{13} \cdot \frac{7}{12} = \frac{56}{156} = 0.3590. \blacksquare$$

It is possible, however, that the occurrence of event  $F$  does not alter the probability of  $E$ , that is,  $P(E|F) = P(E)$ . In this situation, we have

$$P(E \cap F) = P(E) \cdot P(F). \quad (1.13)$$

Events  $E$  and  $F$  for which equation (1.13) holds are said to be ***stochastically independent*** (or merely ***independent***) ***events***; otherwise, they are said to be ***dependent events***.

**Example 1.4.** Consider again the experiment of Example 1.1(b), involving the roll of two fair dice. The 36 equally probable elementary outcomes are displayed in (1.2). Let  $E_7$  denote the event of obtaining a total of seven spots, and  $F_2$  denote the event that the first die shows two spots. Thus,

$$P(E_7) = \frac{6}{36} = \frac{1}{6} \quad \text{and} \quad P(F_2) = \frac{6}{36} = \frac{1}{6}.$$

Since

$$P(E_7 \cap F_2) = P(\{(2,5)\}) = \frac{1}{36} = P(E_7) \cdot P(F_2),$$

events  $E_7$  and  $F_2$  are independent, by definition.

On the other hand, let  $E_5$  be the event of obtaining a total of five spots, so that  $P(E_5) = 4/36 = 1/9$ . In this case,

$$P(E_5 \cap F_2) = P(\{(2,3)\}) = \frac{1}{36}.$$

Therefore,  $E_5$  and  $F_2$  are dependent events:

$$P(E_5) \cdot P(F_2) = \frac{1}{9} \cdot \frac{1}{6} \neq \frac{1}{36} = P(E_5 \cap F_2). \blacksquare$$

## 1.2. Random Variables and Probability Distributions

When working with a random phenomenon modeled by a probability space, one is often more concerned with some numerical function of the outcomes in the sample space than in the actual set of outcomes. For example, interpreting the occurrence of an insurance claim as the outcome of a random experiment, actuaries usually focus on the monetary *amount* of the claim. From another perspective, they may be primarily interested in the *number* of claims occurring during the policy term.

Assume that  $(\Omega, \mathcal{S}, P)$  is a probability space for an experiment of chance. Consider now a function  $X$  defined on the sample space  $\Omega$  that assigns a real number  $X(\omega)$  to each outcome  $\omega \in \Omega$ . The function  $X$  is called a **random variable** on  $\Omega$  provided that for every real number  $x$  the set  $\{\omega \in \Omega : X(\omega) \leq x\}$  is an event in  $\mathcal{S}$  (such a function  $X$  is a **measurable function** with respect to  $\mathcal{S}$ ). The **range space** or **value space** of  $X$  is the range of the function  $X$ :

$$R_X = \{x \in \Re : x = X(\omega) \text{ for some } \omega \in \Omega\}.$$

We denote random variables by upper-case letters— $X, Y, N$ . Specific values that a random variable assumes are represented by lower-case letters— $x, y, n$ .

Most commonly encountered random variables can be classified as one of two major types—the **discrete type** or the **continuous type**—although actuaries also meet the **mixed type** of variable that combines features of both the discrete and the continuous. A discrete random variable  $X$  has a countable range space,  $R_X = \{x_1, x_2, x_3, \dots\}$ , whereas for continuous random variables the range space consists of one or more intervals of real numbers—finite or infinite in length.

Assume now that  $(\Omega, \mathcal{S}, P)$  is a probability space and that  $X$  is a random variable defined on  $\Omega$ . The set function  $P_X$  defined on subsets of the real numbers  $\Re$  is called a **probability distribution** (or merely **distribution**) for  $X$  provided it assigns to a set  $A$  of real numbers the probability that  $X$  takes on a value in  $A$ :<sup>5</sup>

$$P_X(A) = P(\{\omega \in \Omega : X(\omega) \in A\}). \quad (1.14)$$

In particular, the probability that  $X$  lies in the semi-infinite interval  $(-\infty, x]$  is

$$P_X((-\infty, x]) = P(\{\omega \in \Omega : X(\omega) \leq x\}). \quad (1.15)$$

**Example 1.5.** An experiment consists of tossing three fair coins. As discussed in Examples 1.1(a) and 1.2(a), the sample space (1.1) consists of eight elementary outcomes, each with probability 1/8. Let the discrete random variable  $X$  denote the number of Heads obtained. There are clearly four possible values for  $X$ :  $R_X = \{0, 1, 2, 3\}$ . Thus, variable  $X$  is defined on the sample space by

$$X(\omega) = \begin{cases} 0 & \text{if } \omega = TTT \\ 1 & \text{if } \omega \in \{HTT, THT, TTH\} \\ 2 & \text{if } \omega \in \{HHT, HTH, THH\} \\ 3 & \text{if } \omega = HHH. \end{cases}$$

<sup>5</sup> Technically speaking, set  $A$  must belong to the  $\sigma$ -algebra  $\mathcal{B}$  generated by all the semi-infinite intervals  $(-\infty, x]$ . The resulting induced probability space  $(\Re, \mathcal{B}, P_X)$  is defined on all of  $\Re$ . Virtually every set of real numbers encountered in practice belongs to  $\mathcal{B}$ . Details of this formal approach to random variables and probability distributions can be found in an advanced textbook of probability.

Each value of  $X$  defines an event in the underlying sample space, with an associated probability. Thus, the probability set function  $P$  defined on the sample space induces in a natural way a probability distribution  $P_X$  for the random variable  $X$ :

$$\begin{aligned} P_X(\{0\}) &= \Pr\{X = 0\} = P(\{TTT\}) = \frac{1}{8}, \\ P_X(\{1\}) &= \Pr\{X = 1\} = P(\{HTT, THT, TTH\}) = \frac{3}{8}, \\ P_X(\{2\}) &= \Pr\{X = 2\} = P(\{HHT, HTH, THH\}) = \frac{3}{8}, \\ P_X(\{3\}) &= \Pr\{X = 3\} = P(\{HHH\}) = \frac{1}{8}. \blacksquare \end{aligned} \quad (1.16)$$

In the final set of equations (1.16) of this example we introduced a somewhat simplified notation. If  $H(X)$  is a statement about the values of  $X$  that can be true or false, then  $\Pr\{H(X)\}$  represents the more precise expression

$$\Pr\{H(X)\} = P_X(\{x: H(x) \text{ is true}\}).$$

### Probability Distribution Functions

In practice, however, the probability distribution for a random variable  $X$  is usually expressed by a function defined directly on the real-number values of  $X$ . Specifically, one often generates a probability distribution for  $X$  by means of a **probability density function**  $f$  (abbreviated **p.d.f.**) defined on all of the real numbers  $\Re$ . (The density function for  $X$  may be denoted by  $f_X$  when it is important to distinguish the random variable from other variables in a given context.) Function  $f$  has a distinctive form, depending on whether  $X$  is of the discrete type or continuous type. Beginning with the discrete case, we shall in the following discussion take up these two types, as well as the mixed type, in turn.

Often  $f$  depends on a set of one or more numbers  $\Theta = \langle \theta_1, \theta_2, \dots, \theta_r \rangle$ , which can vary over a range of values, each value-set of numbers determining a specific density function. Such numbers are called **parameters**. The resulting distributions are then said to belong to a **parametric distribution family**.

Whenever  $X$  has a countable range space  $R_X = \{x_1, x_2, x_3, \dots\}$ ,  $X$  is said to be a discrete random variable. To serve as a probability density function in the discrete case, function  $f$  must have properties (i), (ii), (iii) listed below. In the discrete case  $f$  is also called a **probability mass function**.

$$\begin{aligned} (i) \quad & f(x_i) \geq 0 && \text{for } x_i \in R_X, \\ (ii) \quad & f(x) = 0 && \text{for } x \notin R_X, \\ (iii) \quad & \sum_i f(x_i) = 1, && i = 1, 2, 3, \dots \end{aligned} \quad (1.17)$$

Function  $P_X$  is defined by setting  $P_X(\{x_i\}) = f(x_i)$  for  $i = 1, 2, 3, \dots$ . Moreover, for a set  $A$ ,  $A \subseteq \mathfrak{N}$ , it follows that

$$P_X(A) = \sum_{x_i \in A} f(x_i). \quad (1.18)$$

The next example describes three common families of discrete distributions.

**Example 1.6.** (a) The simplest non-trivial random variable takes on only two distinct values:  $\{0, 1\}$ . Such a variable  $X$  can be defined on any probability space relative to a fixed event  $E$  with  $P(E) = p$ , where  $0 < p < 1$ :

$$X(\omega) = \begin{cases} 1 & \text{if } \omega \in E \\ 0 & \text{if } \omega \notin E. \end{cases}$$

A trial resulting in the occurrence of  $E$  is often termed a “success,” whereas the occurrence of the complement  $E^c$  is called a “failure.” Therefore, the probability of obtaining a success is  $\Pr\{X = 1\} = p$ , and the probability mass function is

$$f(x) = \begin{cases} p & \text{if } x = 1 \\ 1 - p & \text{if } x = 0 \\ 0 & \text{if } x \notin \{0, 1\}. \end{cases}$$

The probability distribution with this function is called a ***Bernoulli distribution*** with parameter  $p$ , and  $X$  is accordingly known as a ***Bernoulli random variable***.<sup>6</sup>

(b) Another family of discrete distributions, related to the Bernoulli, comprises the ***binomial distributions*** with parameters  $n$  and  $p$ .  $X$  is a binomial random variable if  $X$  equals the number  $x$  of successes, each with probability  $p$ , obtained in  $n$  independent Bernoulli trials ( $n = 1, 2, 3, \dots$ ).<sup>7</sup> The probability of  $x$  successes in  $n$  trials is  $\Pr\{X = x\} = {}_n C_x p^x (1 - p)^{n-x}$ , and the probability mass function is

$$f(x) = \begin{cases} {}_n C_x p^x (1 - p)^{n-x} & \text{if } x \in \{0, 1, 2, \dots, n\} \\ 0 & \text{if } x \notin \{0, 1, 2, \dots, n\}. \end{cases} \quad (1.19)$$

<sup>6</sup> The Bernoulli variable is named for Jacob [James] Bernoulli (1654–1705), a prominent member of the Bernoulli family of Swiss mathematicians. His most significant work in probability, the *Ars conjectandi*, was published posthumously in Basel in 1713.

<sup>7</sup> Informally, we say that successive trials of a single experiment or trials of separate experiments are said to be independent whenever the probabilities of the outcomes in one trial do not depend on those of another. In particular, if event  $E$  is associated with a certain trial and event  $F$  with another trial in the sequence, then  $\Pr\{E \text{ and } F\} = P(E) \cdot P(F)$ . A more formal treatment of this topic can be found in a standard probability theory text.

The factors  ${}_nC_x$  in (1.19) are the ordinary binomial coefficients. The Binomial Theorem is used at step (2) in the following verification that the probabilities in (1.19) all sum to 1:

$$\sum_{x=0}^n f(x) = \sum_{x=0}^n {}_nC_x p^x (1-p)^{n-x} \stackrel{(2)}{=} (p + 1 - p)^n = 1.$$

(c) Consider a Bernoulli experiment with two elementary outcomes: success or failure. Independent trials with  $\Pr\{\text{success}\} = p$  are performed until the first success is obtained. For this experiment the elementary outcomes in  $\Omega$  form a countably infinite set of sequences beginning with a number  $(0, 1, 2, \dots)$  of failures ( $F$ ) and ending with a single success ( $S$ ):

$$\Omega = \{S, FS, FFS, FFFS, FFFFS, FFFFFS, \dots\}.$$

Let  $N$  denote a random variable with value equal to the number  $n$  of trials required to obtain the first success. Independence of the component Bernoulli trials implies that for  $n = 1, 2, 3, \dots$  the probability mass function is

$$f(n) = \Pr\{\text{first } S \text{ obtained on the } n^{\text{th}} \text{ trial}\} = (1-p)^{n-1} p. \quad (1.20)$$

Note that the sum of an infinite geometric series is used at step (2) in the following verification of the sum of all nonzero probabilities:

$$\sum_{n=1}^{\infty} f(n) = p \sum_{n=0}^{\infty} (1-p)^n \stackrel{(2)}{=} p \cdot \frac{1}{1-(1-p)} = 1.$$

A distribution with probability mass function (1.20) is accordingly called a **geometric distribution** with parameter  $p$ . Refer also to Problem 3.21. ■

A probability distribution for a random variable  $X$  can also be characterized by a function related to the probability density function, the **cumulative distribution function** (sometimes shortened to **distribution function** or abbreviated **c.d.f.**). This function is denoted by  $F$ —or by  $F_X$  whenever the dependence on  $X$  must be emphasized—and is defined for all real numbers  $x$  by

$$F(x) = \Pr\{X \leq x\}. \quad (1.21)$$

Therefore, if  $X$  is a discrete variable with range space  $R_X = \{x_1, x_2, x_3, \dots\}$  with a probability mass function  $f$  satisfying (1.17), then function  $F$  is given by

$$F(x) = \sum_{x_i \leq x} f(x_i). \quad (1.22)$$

**Example 1.7.** Let  $X$  be the random variable of Example 1.5. The probability density function can be expressed by the table

| # Heads $x$ | 0     | 1     | 2     | 3     |
|-------------|-------|-------|-------|-------|
| $f(x)$      | 0.125 | 0.375 | 0.375 | 0.125 |

**Figure 1.1. Cumulative Distribution Function  
 $y = F(x)$  [Example 1.7]**

![Graph of the cumulative distribution function F(x) for a discrete random variable X. The x-axis ranges from -2 to 3, and the y-axis ranges from 0 to 1.0. The function is a step function with jumps at x=0, 1, 2, and 3. The jumps are at y=0.125, 0.500, 0.875, and 1.000 respectively. The function is 0 for x < 0, 0.125 for 0 ≤ x < 1, 0.500 for 1 ≤ x < 2, 0.875 for 2 ≤ x < 3, and 1.000 for x ≥ 3. The jumps are marked with solid dots at the right end of each interval and open circles at the left end of each interval.](485c57a6add7e0bd7898009db1179ee6_img.jpg)

Graph of the cumulative distribution function F(x) for a discrete random variable X. The x-axis ranges from -2 to 3, and the y-axis ranges from 0 to 1.0. The function is a step function with jumps at x=0, 1, 2, and 3. The jumps are at y=0.125, 0.500, 0.875, and 1.000 respectively. The function is 0 for x < 0, 0.125 for 0 ≤ x < 1, 0.500 for 1 ≤ x < 2, 0.875 for 2 ≤ x < 3, and 1.000 for x ≥ 3. The jumps are marked with solid dots at the right end of each interval and open circles at the left end of each interval.

As usual, we assume that  $f(x) = 0$  for  $x \notin R_X = \{0, 1, 2, 3\}$ . A graph of the cumulative distribution function, below, is shown in Figure 1.1:

$$F(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 0.125 & \text{if } 0 \leq x < 1 \\ 0.500 & \text{if } 1 \leq x < 2 \\ 0.875 & \text{if } 2 \leq x < 3 \\ 1.000 & \text{if } 3 \leq x < \infty. \blacksquare \end{cases}$$

Example 1.7 illustrates the fact that for a discrete random variable  $X$ ,  $F(x)$  has a jump discontinuity at each value  $x_i \in R_X$  for which  $f(x_i) > 0$ . Moreover, the height of the jump at  $x_i$  is just  $f(x_i)$ . Elsewhere the function is constant:

$$F(x) = \begin{cases} 0 & \text{if } x < x_1 \\ \sum_{j=1}^{i-1} f(x_j) & \text{if } x_{i-1} \leq x < x_i, i = 2, 3, \dots \\ 1 & \text{if } \max R_X \text{ exists and } x \geq \max R_X. \end{cases}$$

Thus, for every probability distribution defined on a discrete random variable the cumulative distribution function  $F(x)$  is a step function.

Suppose now that random variable  $X$  is a non-discrete variable. This means the range space  $R_X$  is an uncountable set, and we shall further assume that  $R_X$  consists of one or more intervals (of finite or infinite length) of real numbers. To serve as a probability density function in this case  $f$  must be defined on all of  $\Re$  and be Riemann integrable there (“Riemann integrable” generally means that the function has at most a countable

set of points of discontinuity).<sup>8</sup> Function  $f$  must also have properties analogous to those of the discrete case (1.17):

$$\begin{aligned} (i) \quad & f(x) \geq 0 \quad \text{for } x \in \mathcal{R}_X, \\ (ii) \quad & f(x) = 0 \quad \text{for } x \notin \mathcal{R}_X, \\ (iii) \quad & \int_{-\infty}^{\infty} f(x) dx = 1. \end{aligned} \tag{1.23}$$

If such a density function exists, the probability function  $P_X$  is defined for a set  $A$  of real numbers by the integral

$$P_X(A) = \int_A f(x) dx. \tag{1.24}$$

Thus, for example,

$$P_X([a, b]) = \int_a^b f(x) dx, \quad [a, b] \subseteq \mathcal{R}. \tag{1.25}$$

In particular, the cumulative distribution function is given by

$$F(x) = \int_{-\infty}^x f(u) du. \tag{1.26}$$

A basic theorem of calculus guarantees that for such an integrand  $f(x)$ , the function  $F(x)$  is a continuous function of  $x$  on all of  $\mathcal{R}$ . Moreover, when the density function  $f(x)$  is continuous at  $x$ , then  $F(x)$  is also differentiable at  $x$ , with  $F'(x) = f(x)$ . As a result, the random variable  $X$  and its associated probability distribution  $P_X$  are said to be **continuous**.

The next example illustrates a trio of important continuous distributions.

**Example 1.8.** (a) Random variable  $X$  takes on values throughout an interval  $[\alpha, \beta]$  of real numbers ( $\alpha < \beta$ ). Variable  $X$  is said to have a **uniform distribution** on  $[\alpha, \beta]$  if the probability density function is given by

$$f(x) = \begin{cases} \frac{1}{\beta - \alpha} & \text{if } x \in [\alpha, \beta] \\ 0 & \text{if } x < \alpha \text{ or } x > \beta. \end{cases}$$

<sup>8</sup> Named for the German professor of mathematics, Bernhard Riemann (1826–1866), who gave the first rigorous definition, the Riemann integral is the ordinary integral of elementary calculus. Riemann's approach to integration was later extended by other mathematicians, notably Henri Lebesgue (1875–1941). Although today the most general and rigorous treatments of probability are founded on the Lebesgue theory of measure and integration, the Riemann approach (and its generalization by Stieltjes, discussed in the next section) is adequate for the present work.

Thus, the probability that  $X$  lies in a subinterval  $[c, d]$ , where  $\alpha \leq c < d \leq \beta$ , is proportional to the length of the subinterval:

$$P_X([c, d]) = \int_c^d f(x) dx = \frac{1}{\beta - \alpha} \int_c^d dx = \frac{d - c}{\beta - \alpha}.$$

(b) Let  $X$  denote the size of an insurance claim that is unrestricted by any policy limit. Then it is reasonable to consider the nonnegative real numbers as the range space of  $X$ :  $R_X = [0, \infty)$ . When  $X$  has the probability density function

$$f(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ (1/\beta)e^{-x/\beta} & \text{if } 0 \leq x < \infty \quad (\beta > 0) \end{cases}$$

$X$  is said to have an **exponential distribution**. The cumulative distribution function is

$$F(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 - e^{-x/\beta} & \text{if } 0 \leq x < \infty. \end{cases}$$

In the case  $\beta = 200$  the probability that  $X$  falls in the interval  $[300, 400]$  is

$$\Pr\{300 \leq X \leq 400\} = \frac{1}{200} \int_{300}^{400} e^{-x/200} dx = F(400) - F(300) = 0.0878.$$

(c) The random variable  $Z$  with the important **standard normal distribution**—known also as the **Gaussian distribution**<sup>9</sup>—has a continuous nonzero density function defined on all of  $\Re$ :

$$f(z) = \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{1}{2}z^2\right), \quad -\infty < z < \infty. \quad (1.27)$$

Because  $f$  is a function of  $z^2$ , the distribution is symmetric about  $z = 0$ .

The cumulative distribution function, denoted in this case by the special notation  $\Phi(z)$ , is therefore

$$\Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z \exp\left(-\frac{1}{2}u^2\right) du. \quad (1.28)$$

Because the integral in (1.28) cannot be evaluated by elementary methods of calculus, values of  $\Phi$  must be obtained by some approximation method—refer to Appendix A.1 for details. A graph of  $y = \Phi(z)$  is shown in Figure 1.2. ■

<sup>9</sup> The German mathematician Karl Friedrich Gauss (1777–1855) is widely acknowledged as the greatest mathematician of the nineteenth century. Working at the University of Göttingen, he made significant contributions to a broad range of fields in mathematics and physics. He used the normal distribution to model the distribution of measurement errors.

**Figure 1.2. Cumulative Distribution Function**  
 **$y = \Phi(z)$  [Example 1.8(c)]**

![Graph of the Cumulative Distribution Function y = Phi(z). The horizontal axis is labeled z and ranges from -3 to 3 with tick marks at -3, -2, -1, 0, 1, 2, 3. The vertical axis is labeled y and ranges from 0 to 1.0 with tick marks at 0.2, 0.6, 0.8, 1.0. A dashed horizontal line is drawn at y = 1.0. The curve starts near 0 for z = -3, passes through (0, 0.5), and approaches 1.0 as z increases towards 3.](391ab9e5616ba6311161af4d7a93422b_img.jpg)

Graph of the Cumulative Distribution Function y = Phi(z). The horizontal axis is labeled z and ranges from -3 to 3 with tick marks at -3, -2, -1, 0, 1, 2, 3. The vertical axis is labeled y and ranges from 0 to 1.0 with tick marks at 0.2, 0.6, 0.8, 1.0. A dashed horizontal line is drawn at y = 1.0. The curve starts near 0 for z = -3, passes through (0, 0.5), and approaches 1.0 as z increases towards 3.

In addition to the special properties for cumulative distribution functions for discrete and continuous random variables already mentioned, the function  $F(x)$  has a number of general properties, listed below.

#### ***Properties of $F(x)$***

*Assume that  $c$  is an arbitrary real constant. Then*

$$(a) \quad 0 \leq F(x) \leq 1 \quad \text{for all } x \in \Re. \quad (1.29)$$

$$(b) \quad F(x_1) \leq F(x_2) \quad \text{for } x_1 < x_2. \quad (1.30)$$

$$(c) \quad \lim_{x \rightarrow \infty} F(x) = 1 \quad \text{and} \quad \lim_{x \rightarrow -\infty} F(x) = 0. \quad (1.31)$$

$$(d) \quad \Pr\{X = c\} = \lim_{x \rightarrow c+} F(x) - \lim_{x \rightarrow c-} F(x) = F(c+) - F(c-). \quad (1.32)$$

$$(e) \quad F(x) \text{ is continuous from the right, that is, } \lim_{x \rightarrow c+} F(x) = F(c). \quad (1.33)$$

##### ***Proof:***

(a) The inequality follows from the definition (1.21) of  $F$  as a probability.

(b) The inequality follows from

$$F(x_2) - F(x_1) = \Pr\{x_1 < X \leq x_2\} \geq 0.$$

(c) Let  $\langle x_n \rangle$  be an increasing sequence of reals with  $\lim_{n \rightarrow \infty} x_n = \infty$ . Then  $\langle I_n \rangle = \langle (-\infty, x_n] \rangle$  is an ascending sequence of intervals, with  $\bigcup_n I_n = (-\infty, \infty)$  and  $P_X(I_n) = F(x_n)$ . Applying the result of Problem 1.3(a):

$$\lim_{n \rightarrow \infty} F(x_n) = \lim_{n \rightarrow \infty} P_X(I_n) = P_X\left(\bigcup_n I_n\right) = P_X((-\infty, \infty)) = 1.$$

- (d) The sequence  $\langle I_n \rangle = \langle (c - \frac{1}{n}, c + \frac{1}{n}] \rangle$  is a descending sequence of intervals, with  $\{c\} = \bigcap_n I_n$ . The result of Problem 1.3(b) yields

$$\begin{aligned} \Pr\{X = c\} &= P_X(\bigcap_n I_n) = \lim_{n \rightarrow \infty} P_X(I_n) \\ &= \lim_{n \rightarrow \infty} \left( F\left(c + \frac{1}{n}\right) - F\left(c - \frac{1}{n}\right) \right) \\ &= F(c+) - F(c-). \end{aligned}$$

- (e) Let  $\langle x_n \rangle$  be a decreasing sequence of reals with  $\lim_{n \rightarrow \infty} x_n = c$ . Then  $\langle I_n \rangle = \langle (-\infty, x_n] \rangle$  is a descending sequence of intervals, with  $\bigcap_n I_n = (-\infty, c]$  and  $P_X(I_n) = F(x_n)$ . Again applying Problem 1.3(b):

$$\lim_{x \rightarrow c+} F(x) = \lim_{n \rightarrow \infty} F(x_n) = \lim_{n \rightarrow \infty} P_X(I_n) = P_X(\bigcap_n I_n) = P_X((-\infty, c]) = F(c). \blacksquare$$

Note that property (d) above implies that if  $X$  is a continuous random variable then  $\Pr\{X = x\} = 0$  for every real  $x$ .

Occasionally one encounters random variables that are neither entirely discrete nor entirely continuous but whose distribution is a hybrid of these two main types. Such a random variable is said to have a ***mixed distribution***, with a cumulative distribution function of the form described below.

A distribution function  $F$  is of the mixed type if the function can be expressed as

$$F(x) = \omega_1 F_1(x) + \omega_2 F_2(x), \quad (1.34)$$

where  $F_1(x)$  is the distribution function of a continuous variable  $X_1$ ,  $F_2(x)$  is the distribution function of a discrete random variable  $X_2$  with  $R_{X_2} = \{x_i\}$ , and the nonnegative numbers  $\omega_1$  and  $\omega_2$  satisfy  $\omega_1 + \omega_2 = 1$ . Here the numbers  $\omega_1$  and  $\omega_2$  can be interpreted as the respective probabilities of being (1) in the continuous state or (2) in the discrete state. A graph of  $y = F(x)$  is continuous except at the points  $\{x_i\}$ , where it has a jump discontinuity of height  $\omega_2 f_{X_2}(x_i)$ .

The next example illustrates some types of mixed distributions often encountered in the modeling of property/casualty claim processes.

**Example 1.9.** The distribution of an unlimited claim-size random variable  $Y$  has the exponential c.d.f.

$$F_Y(x) = \begin{cases} 0 & \text{if } -\infty \leq x < 0 \\ 1 - e^{-0.01x} & \text{if } 0 \leq x < \infty. \end{cases}$$

- (a) The variable  $X$  is distributed like  $Y$  for positive  $x$ , but takes on the value 0 with probability 0.25. Thus, the distribution of  $X$  is a mixed distribution with a discrete lump of probability at  $x = 0$ . Since

$$\omega_1 = \text{Probability of being in the continuous state} = 1 - \Pr\{X = 0\} = 0.75,$$

the cumulative distribution function of  $X$  has the form

$$\begin{aligned}
 F(x) &= (0.75) \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 - e^{-0.01x} & \text{if } 0 \leq x < \infty \end{cases} + (0.25) \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 & \text{if } 0 \leq x < \infty \end{cases} \\
 &= \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 - 0.75e^{-0.01x} & \text{if } 0 \leq x < \infty. \end{cases}
 \end{aligned}$$

(b) Alternatively, suppose that  $X$  is distributed like  $Y$ , but is limited above by the value 200—that is, claims less than or equal to 200 are paid at full value, but claims greater than 200 are paid at the maximum value of 200. In this case, however,

$$\omega_1 = \text{Probability of being in the continuous state} = F_Y(200) = 1 - e^{-2}.$$

Therefore,

$$\begin{aligned}
 F(x) &= (1 - e^{-2}) \begin{cases} 0 & \text{if } -\infty < x < 0 \\ \frac{1 - e^{-0.01x}}{1 - e^{-2}} & \text{if } 0 \leq x < 200 \\ 1 & \text{if } 200 \leq x < \infty \end{cases} + e^{-2} \begin{cases} 0 & \text{if } -\infty < x < 200 \\ 1 & \text{if } 200 \leq x < \infty \end{cases} \\
 &= \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 - e^{-0.01x} & \text{if } 0 \leq x < 200 \\ 1 & \text{if } 200 \leq x < \infty. \end{cases}
 \end{aligned}$$

(c) Finally, again assume that  $X$  is distributed like  $Y$ , but simultaneously has both modifications described in parts (a) and (b): it takes on the value 0 with probability  $\Pr\{X=0\} = 0.25$  and is limited above by the value 200. Thus, the modified variable  $X_c$  has a mixed distribution with two discrete lumps of probability mass, one at  $x=0$  and another at  $x=200$ . Observe that

$$\omega_1 = \text{Probability of being in the continuous state} = 0.75F_Y(200) = 0.75(1 - e^{-2}).$$

Variable  $X$  then has the cumulative distribution function

$$F(x) = 0.75(1 - e^{-2}) \begin{cases} 0 & \text{if } -\infty < x < 0 \\ \frac{1 - e^{-0.01x}}{1 - e^{-2}} & \text{if } 0 \leq x < 200 \\ 1 & \text{if } 200 \leq x < \infty \end{cases}$$

$$\begin{aligned}
 & + (0.25 + 0.75e^{-2}) \begin{cases} 0 & \text{if } -\infty < x < 0 \\ \frac{0.25}{0.25 + 0.75e^{-2}} & \text{if } 0 \leq x < 200 \\ 1 & \text{if } 200 \leq x < \infty \end{cases} \\
 = & \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 - 0.75e^{-0.01x} & \text{if } 0 \leq x < 200 \\ 1 & \text{if } 200 \leq x < \infty. \end{cases}
 \end{aligned}$$

Graphs of  $y = F(x)$  for parts (a), (b), and (c) are shown in Figures 1.3, 1.4, and 1.5, respectively. ■

**Figure 1.3. Mixed Distribution Function  $y = F(x)$   
[Example 1.9(a)]**

![Graph of the mixed distribution function y = F(x) for Example 1.9(a). The x-axis ranges from -400 to 600, and the y-axis ranges from 0 to 1.00. The function is 0 for x < 0. At x = 0, there is a jump discontinuity from 0 to 0.25, marked with a solid dot at (0, 0.25) and an open circle at (0, 0). For 0 <= x < 200, the function follows the curve y = 1 - 0.75e^{-0.01x}, starting at (0, 0.25) and approaching 1.00. At x = 200, there is another jump discontinuity to 1.00, marked with a solid dot at (200, 1.00) and an open circle at (200, approximately 0.85). The function is 1.00 for x >= 200.](99938fa8d7d80af041634eba601e418b_img.jpg)

Graph of the mixed distribution function y = F(x) for Example 1.9(a). The x-axis ranges from -400 to 600, and the y-axis ranges from 0 to 1.00. The function is 0 for x < 0. At x = 0, there is a jump discontinuity from 0 to 0.25, marked with a solid dot at (0, 0.25) and an open circle at (0, 0). For 0 <= x < 200, the function follows the curve y = 1 - 0.75e^{-0.01x}, starting at (0, 0.25) and approaching 1.00. At x = 200, there is another jump discontinuity to 1.00, marked with a solid dot at (200, 1.00) and an open circle at (200, approximately 0.85). The function is 1.00 for x >= 200.

**Figure 1.4. Mixed Distribution Function  $y = F(x)$   
[Example 1.9(b)]**

![Graph of the mixed distribution function y = F(x) for Example 1.9(b). The x-axis ranges from -400 to 600, and the y-axis ranges from 0 to 1.00. The function is 0 for x < 0. At x = 0, there is a jump discontinuity from 0 to 0, marked with an open circle at (0, 0). For 0 <= x < 200, the function follows the curve y = 1 - 0.75e^{-0.01x}, starting at (0, 0) and approaching approximately 0.85 at x = 200. At x = 200, there is a jump discontinuity to 1.00, marked with an open circle at (200, approximately 0.85) and a solid dot at (200, 1.00). The function is 1.00 for x >= 200.](343d625a23e27ef3e1fe56dc003bb072_img.jpg)

Graph of the mixed distribution function y = F(x) for Example 1.9(b). The x-axis ranges from -400 to 600, and the y-axis ranges from 0 to 1.00. The function is 0 for x < 0. At x = 0, there is a jump discontinuity from 0 to 0, marked with an open circle at (0, 0). For 0 <= x < 200, the function follows the curve y = 1 - 0.75e^{-0.01x}, starting at (0, 0) and approaching approximately 0.85 at x = 200. At x = 200, there is a jump discontinuity to 1.00, marked with an open circle at (200, approximately 0.85) and a solid dot at (200, 1.00). The function is 1.00 for x >= 200.

**Figure 1.5. Mixed Distribution Function  $y = F(x)$**   
**[Example 1.9(c)]**

![Graph of a mixed distribution function y = F(x). The x-axis ranges from -400 to 600, and the y-axis ranges from 0.25 to 1.00. The function is 0 for x < 0, jumps to 0.25 at x = 0, increases as a curve to approximately 0.9 at x = 200, and then jumps to 1.0 at x = 200, remaining at 1.0 for x > 200. Open circles are at (0,0) and (200,0.9), while closed circles are at (0,0.25) and (200,1.0).](ec36a1ba48e13289c395fab4a7730bdb_img.jpg)

Graph of a mixed distribution function y = F(x). The x-axis ranges from -400 to 600, and the y-axis ranges from 0.25 to 1.00. The function is 0 for x < 0, jumps to 0.25 at x = 0, increases as a curve to approximately 0.9 at x = 200, and then jumps to 1.0 at x = 200, remaining at 1.0 for x > 200. Open circles are at (0,0) and (200,0.9), while closed circles are at (0,0.25) and (200,1.0).

### Joint Distributions

It is frequently necessary to work with two or more random variables at the same time, recognizing that the values of one variable may influence the values of another. Accordingly, one must consider the probability distribution of the variables jointly. For example, suppose that  $X$  and  $Y$  are random variables with respective density functions  $f_X(x)$  and  $f_Y(y)$ . We define  $F(x, y)$ , the **joint cumulative distribution function** of  $X$  and  $Y$ , by

$$F(x, y) = \Pr\{X \leq x \text{ and } Y \leq y\}, \quad -\infty < x, y < \infty. \quad (1.35)$$

The **joint probability density function**  $f(x, y)$  is a function that, in the case that  $X$  and  $Y$  are both discrete variables, satisfies

$$f(x_i, y_j) = \Pr\{X = x_i \text{ and } Y = y_j\}, \quad x_i \in R_X, y_j \in R_Y, \quad (1.36)$$

as well as

$$\begin{aligned} f_X(x_i) &= \sum_{y_j \in R_Y} f(x_i, y_j), \quad x_i \in R_X, \\ f_Y(y_j) &= \sum_{x_i \in R_X} f(x_i, y_j), \quad y_j \in R_Y. \end{aligned} \quad (1.37)$$

In this context, functions  $f_X(x)$  and  $f_Y(y)$  are called the **marginal probability density functions** of  $X$  and  $Y$ , respectively.

In the case that  $X$  and  $Y$  are both continuous variables, the density function  $f(x, y)$  must satisfy

$$F(x, y) = \int_{-\infty}^x \int_{-\infty}^y f(u, v) du dv, \quad -\infty < x, y < \infty, \quad (1.38)$$

with the marginal density functions given by

$$f_X(x) = \int_{-\infty}^{\infty} f(x, y) dy \quad \text{and} \quad f_Y(y) = \int_{-\infty}^{\infty} f(x, y) dx. \quad (1.39)$$

When it is true that the density functions satisfy the relation

$$f(x, y) = f_X(x) \cdot f_Y(y), \quad -\infty < x, y < \infty, \quad (1.40)$$

we say that random variables  $X$  and  $Y$  are **independent**. For independent random variables, the probability distribution of one variable is not affected by the values of the other. In particular, the probability  $\Pr\{X \leq x\}$  is mathematically independent of the value of  $Y$ , and vice versa. Consequently, we also have

$$F(x, y) = F_X(x) \cdot F_Y(y), \quad -\infty < x, y < \infty. \quad (1.41)$$

## 1.3. Mathematical Expectation

One of the most useful random-variable concepts is that of mathematical expectation, which we define in the following way. Assume that  $X$  is a random variable with p.d.f.  $f$ —and range space  $R_X = \{x_i\}$  if  $X$  is discrete. Let  $g$  be a function such that

$$\sum_i g(x_i) f(x_i) \quad \text{or} \quad \int_{-\infty}^{\infty} g(x) f(x) dx,$$

depending on whether  $X$  is discrete or continuous, respectively, exists as a finite number. Thus, whenever the above expression is an infinite series or improper Riemann integral, it must be convergent. The **expectation** or **expected value** of  $g(X)$  is denoted by  $E[g(X)]$ , and it is defined by

$$E[g(X)] = \begin{cases} \sum_i g(x_i) f(x_i) & \text{if } X \text{ is discrete} \\ \int_{-\infty}^{\infty} g(x) f(x) dx & \text{if } X \text{ is continuous.} \end{cases} \quad (1.42)$$

**A Note on Integrals.** Students of integration theory will recognize that the dual expressions in (1.42) can be represented by a single formula in which the integral is of the Riemann–Stieltjes type, as opposed to the ordinary Riemann integral of elementary calculus:<sup>10</sup>

$$E[g(X)] = \int_{-\infty}^{\infty} g(x) dF(x). \quad (1.43)$$

Without going into the theoretical details, unnecessary for the present discussion and which can be obtained from a text of real analysis, the Riemann–Stieltjes integral

<sup>10</sup> Thomas Jan Stieltjes (1856–1894) was a prominent Dutch mathematician who made contributions to continued fractions, number theory, and analysis. Appearing in his 1894 paper, “*Recherches sur les fractions continues*,” his was the first published generalization of the Riemann integral. Details concerning the Riemann–Stieltjes integral can be found in textbooks of probability theory or advanced calculus; for example, refer to McCord and Moroney [14], pp. 82–92, or Apostol [2], pp. 140–182.

has the following properties which support the use of the expression in (1.43). Whenever  $F(x)$  is a nondecreasing differentiable function for which  $F'(x) = f(x)$  and  $f(x)$  is Riemann-integrable, the Stieltjes integral in (1.43) reduces to the Riemann integral

$$\int_{-\infty}^{\infty} g(x) dF(x) = \int_{-\infty}^{\infty} g(x) f(x) dx. \quad (1.44)$$

In the case that  $F(x)$  is a nondecreasing step function with jumps at a countable set of values  $\{x_i\}$  and with the height of the jump at  $x_i$  equal to  $f(x_i)$ , then

$$\int_{-\infty}^{\infty} g(x) dF(x) = \sum_i g(x_i)(F(x_i) - F(x_{i-1} -)) = \sum_i g(x_i) f(x_i). \quad (1.45)$$

As a result, we are justified in using the notation of (1.43) in place of (1.42), with the integral  $\int_{-\infty}^{\infty} g(x) dF(x)$  interpreted as a Riemann–Stieltjes integral.

Properties (1.46) through (1.50) below are straightforward consequences of definition (1.42). Verification is requested in Problem 1.8.

### ***Properties of $E[g(X)]$***

*Assume that  $c$  is a real constant and that  $h$  and  $g$  are functions for which  $E[g(X)]$  and  $E[h(X)]$  exist. Then*

$$(a) \quad E[c] = c. \quad (1.46)$$

$$(b) \quad E[c g(X)] = c E[g(X)]. \quad (1.47)$$

$$(c) \quad E[g(X) + h(X)] = E[g(X)] + E[h(X)]. \quad (1.48)$$

$$(d) \quad E[g(X)] \leq E[h(X)] \text{ whenever } g(x) \leq h(x) \text{ for all } x. \quad (1.49)$$

$$(e) \quad |E[g(X)]| \leq E[|g(X)|]. \quad (1.50)$$

One of the most important expected values for a random variable  $X$  is the **mean**  $E[X]$ , obtained from (1.43) when  $g(X) = X$ :

$$E[X] = \int_{-\infty}^{\infty} x dF(x). \quad (1.51)$$

In addition, the expectation of  $g(X) = (X - E[X])^2$  defines the **variance** of  $X$ :

$$\text{Var}[X] = E[(X - E[X])^2]. \quad (1.52)$$

The mean is a familiar measure of central tendency. For claim-size distributions, discussed in Chapter 2, the mean  $E[X]$  is often called the **severity**.<sup>11</sup> The variance is

<sup>11</sup> Actuaries sometimes use the term “severity” as a synonym for “claim size” when referring to claim-size distributions as “severity distributions.” However, in this monograph we shall consistently use the term to denote *mean claim size*.

a standard measure of the dispersion of the distribution—the larger the variance, the more widely dispersed over the range space is the unit mass of probability. The square root of the variance is known as the **standard deviation**:  $SD[X] = \sqrt{Var[X]}$ .

### **Properties of $Var[X]$**

If  $c$  is a real constant, then

$$(a) \quad Var[c] = 0. \quad (1.53)$$

$$(b) \quad Var[cX] = c^2 Var[X]. \quad (1.54)$$

$$(c) \quad Var[X] = E[X^2] - (E[X])^2. \quad (1.55)$$

Proofs of these variance properties are requested in Problem 1.9.

Generalizing the expected values involved in definitions (1.51) and (1.52), we define the expectation of  $g(X) = X^m$  for  $m = 1, 2, 3, \dots$ :

$$E[X^m] = \int_{-\infty}^{\infty} x^m dF(x). \quad (1.56)$$

When the expression in (1.56) exists, the expected value  $E[X^m]$  is called the  **$m^{\text{th}}$  moment about 0** (or more simply, the  **$m^{\text{th}}$  moment**) of  $X$ . In addition, the expected value  $E[(X - E[X])^m]$  is called the  **$m^{\text{th}}$  central moment** of  $X$ . Accordingly,  $Var[X]$  is the second central moment of  $X$ .

Although we have defined the moments, as well as the variance and other moment-based entities, as characteristics of a random variable, it is customary to refer to them interchangeably as properties of the random variable and of its associated probability distribution. In a formal treatment of probability these concepts can be defined separately, but we shall not do so here.

**Example 1.10.** (a) Random variable  $X$  has a Bernoulli distribution with parameter  $p$ . Then

$$E[X] = (0)(1-p) + (1)p = p,$$

$$E[X^2] = (0^2)(1-p) + (1^2)p = p,$$

so that equation (1.55) yields  $Var[X] = p(1-p)$ .

(b) Variable  $X$  is uniformly distributed on  $[\alpha, \beta]$ . Integrating over the interval, we obtain the mean and variance as functions of parameters  $\alpha$  and  $\beta$ :

$$E[X] = \frac{1}{\beta - \alpha} \int_{\alpha}^{\beta} x \, dx = \frac{\beta^2 - \alpha^2}{2(\beta - \alpha)} = \frac{\alpha + \beta}{2},$$

$$Var[X] = \frac{1}{\beta - \alpha} \int_{\alpha}^{\beta} x^2 \, dx - (E[X])^2 = \frac{\beta^3 - \alpha^3}{3} - \frac{(\alpha + \beta)^2}{4} = \frac{(\beta - \alpha)^2}{12}.$$

(c)  $Z$  has the standard normal distribution with p.d.f. (1.27). Then

$$E[Z] = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} z \exp\left(-\frac{1}{2}z^2\right) dz = 0,$$

$$E[Z^2] = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} z^2 \exp\left(-\frac{1}{2}z^2\right) dz = \frac{1}{\sqrt{2\pi}} \sqrt{2\pi} = 1,$$

and so  $\text{Var}[Z] = 1 - 0^2 = 1$ . ■

Finally, we examine another special expected value for a random variable  $X$ , namely that of the function  $g(X) = e^{tX}$ . If there exists a positive number  $K$  such that the expectation  $E[g(X)] = E[e^{tX}]$  exists for all  $|t| < K$ , then the resulting function of  $t$ ,  $M(t) = E[e^{tX}]$ , is called the **moment-generating function** of  $X$ . Thus,

$$M(t) = E[e^{tX}] = \int_{-\infty}^{\infty} \exp(tx) dF(x).^{12} \quad (1.57)$$

Moment-generating functions play an important role in probability. When it exists, the moment-generating function of a random variable is unique and, moreover, completely characterizes the probability distribution of the variable. That is, two random variables with the same moment-generating function have the same distribution. In addition, when it exists, the  $m^{\text{th}}$  derivative of  $M(t)$  evaluated at  $t = 0$  is just the  $m^{\text{th}}$  moment:

$$\left. \frac{d^m}{dt^m} M(t) \right|_{t=0} = E[X^m], \quad m = 1, 2, 3, \dots \quad (1.58)$$

Proofs of both these assertions about the moment-generating function can be found in a standard text of probability theory.

**Example 1.11.** (a) Assume that random variable  $X$  has a binomial distribution with parameters  $n$  and  $p$  ( $n = 1, 2, 3, \dots$  and  $0 < p < 1$ ). Function  $M(t)$  exists for all real  $t$ , and

$$M(t) = \sum_{x=0}^n e^{tx} f(x) = \sum_{x=0}^n {}_n C_x (pe^t)^x (1-p)^{n-x} = (1-p+pe^t)^n.$$

The first two derivatives are

$$\frac{d}{dt} M(t) = n(1-p+pe^t)^{n-1} pe^t,$$

$$\frac{d^2}{dt^2} M(t) = \begin{cases} n(n-1)(1-p+pe^t)^{n-2} p^2 e^{2t} + n(1-p+pe^t)^{n-1} pe^t & \text{if } n \geq 2 \\ pe^t & \text{if } n = 1. \end{cases}$$

<sup>12</sup> For a continuous random variable the moment-generating function is a type of Laplace transform of its probability density function. Although useful when it exists, the moment-generating function fails to exist for a number of important distributions, notably the lognormal family discussed in Chapter 2. However, the *characteristic function* of a random variable  $X$ , defined as the complex-valued function  $E[\exp(itX)]$ , always exists and has similar moment-generating properties. The uniqueness of the moment-generating function is usually obtained from a corresponding uniqueness theorem about the characteristic function. For example, see Parzen [18], pp. 400–404. Refer also to Section 4.5.

Evaluating these derivatives at  $t = 0$ , we obtain

$$E[X] = M'(0) = np,$$

$$E[X^2] = M''(0) = n(n-1)p^2 + np,$$

and hence  $\text{Var}[X] = n(n-1)p^2 + np - (np)^2 = np(1-p)$ .

(b) Assume that  $X$  is exponentially distributed with parameter  $\beta$ . Then

$$M(t) = \frac{1}{\beta} \int_0^{\infty} e^{tx} e^{-x/\beta} dx = \frac{1}{1-\beta t}, \quad -\infty < t < 1/\beta,$$

and the first two derivatives are

$$\frac{d}{dt} M(t) = \frac{\beta}{(1-\beta t)^2} \quad \text{and} \quad \frac{d^2}{dt^2} M(t) = \frac{2\beta^2}{(1-\beta t)^3}.$$

Therefore,

$$E[X] = M'(0) = \beta \quad \text{and} \quad E[X^2] = M''(0) = 2\beta^2,$$

so that  $\text{Var}[X] = 2\beta^2 - \beta^2 = \beta^2$ . ■

For two or more random variables considered jointly, there are several useful and important results about expectations.

First, consider  $g(X, Y) = X + Y$ . The expectation  $E[X + Y]$  is just the sum  $E[X] + E[Y]$ . If, for example,  $X$  and  $Y$  are continuous variables, then

$$\begin{aligned} E[X + Y] &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x + y) f(x, y) dx dy \\ &= \int_{-\infty}^{\infty} x \left[ \int_{-\infty}^{\infty} f(x, y) dy \right] dx + \int_{-\infty}^{\infty} y \left[ \int_{-\infty}^{\infty} f(x, y) dx \right] dy \\ &= \int_{-\infty}^{\infty} x f_X(x) dx + \int_{-\infty}^{\infty} y f_Y(y) dy \\ &= E[X] + E[Y]. \end{aligned} \tag{1.59}$$

Secondly, assume that  $X$  and  $Y$  are *independent* random variables and that  $g$  and  $h$  are functions for which  $E[g(X)]$  and  $E[h(Y)]$  each exist. Then the expectation of the product  $XY$  is the product of the expected values:

$$E[g(X) \cdot h(Y)] = E[g(X)] \cdot E[h(Y)]. \tag{1.60}$$

In the continuous case, we have

$$\begin{aligned} E[g(X) \cdot h(Y)] &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x) h(y) f_X(x) f_Y(y) dx dy \\ &= \int_{-\infty}^{\infty} g(x) f_X(x) dx \cdot \int_{-\infty}^{\infty} h(y) f_Y(y) dy \\ &= E[g(X)] \cdot E[h(Y)], \end{aligned}$$

and a similar argument applies in the discrete case.

Again, suppose that  $X$  and  $Y$  are independent random variables. Then

$$\text{Var}[X + Y] = \text{Var}[X] + \text{Var}[Y]. \quad (1.61)$$

To verify (1.61), use (1.59) and (1.60) to obtain

$$E[(X + Y)^2] = E[X^2 + 2XY + Y^2] = E[X^2] + 2E[X]E[Y] + E[Y^2],$$

and so

$$\begin{aligned} \text{Var}[X + Y] &= E[X^2] + 2E[X]E[Y] + E[Y^2] - (E[X] + E[Y])^2 \\ &= E[X^2] - (E[X])^2 + E[Y^2] - (E[Y])^2 \\ &= \text{Var}[X] + \text{Var}[Y]. \end{aligned}$$

When random variable  $Y$  is the sum of  $n$  independent, identically distributed random variables,  $Y = X_1 + X_2 + \cdots + X_n$ , there is a useful result involving the moment-generating functions. If each variable  $X_i$  has the same distribution as some random variable  $X$ , the generating function of  $Y$  can be expressed in terms of  $M_X(t)$ . Observe that the independence of the variables  $\{X_i\}$  is used at step (3):

$$\begin{aligned} M_Y(t) &= E[\exp(tX_1 + tX_2 + \cdots + tX_n)] = E[\exp(tX_1)\exp(tX_2)\cdots\exp(tX_n)] \\ &\stackrel{(3)}{=} \prod_{i=1}^n E[\exp(tX_i)] \\ &= (M_X(t))^n. \end{aligned} \quad (1.62)$$

**Example 1.12.** Assume that random variable  $Y$  is the sum of  $n$  independent random variables  $\{X_i\}$ , each having the distribution of  $X$ , a Bernoulli random variable with parameter  $p$ :

$$Y = X_1 + X_2 + \cdots + X_n.$$

The moment-generating function of each variable  $X_i$  exists for all real  $t$ , and

$$M_{X_i}(t) = M_X(t) = E[\exp(tX)] = e^{0t}(1-p) + e^{1t}p = 1 - p + pe^t.$$

Thus, by (1.62) the generating function for the sum  $Y$  is

$$M_Y(t) = (1 - p + pe^t)^n.$$

Because this is the moment-generating function of a binomial distribution with parameters  $n$  and  $p$ , the uniqueness of the generating function implies that  $Y$  is binomially distributed with parameters  $n$  and  $p$ . ■

## 1.4. Random Samples

The problem of fitting a parametric distribution to a set of claim data, discussed briefly in the next section, relies heavily on the theory of sampling from a population,

a collection of objects with identical distributional characteristics. For example, an actuary is often interested in inferring the distribution of sizes or numbers of claims from a set of data obtained from a portfolio of similar policies. We begin with the definition of random sample, which is fundamental to the discussion that follows.

An ordered set  $\langle X_1, X_2, \dots, X_n \rangle$  of independent, identically-distributed random variables is a **random sample** from a population random variable  $X$  if each  $X_i$  has the distribution of  $X$ . Thus, the distribution of  $X_i$  does not depend on the value of any other random variable  $X_j$  ( $i \neq j$ ) in the sample. In practice, a random sample of size  $n$  may be generated by performing  $n$  successive independent trials of a single experiment—for example, tossing a coin  $n$  times—or perhaps by making  $n$  selections from a collection of similar objects, each time replacing the selected object before making the next selection, a method called selection with replacement. The set of particular values of the random variables  $\langle X_i \rangle$ , denoted by  $\langle x_1, x_2, \dots, x_n \rangle$ , is referred to as a set of **sample observations**. A **statistic** is a function of the sample variables  $\langle X_1, X_2, \dots, X_n \rangle$ .

The sample moments, analogs of formula (1.56) for moments of the population distribution, are useful statistics in the analysis of sample data:

$$M_m = \frac{1}{n} \sum_{i=1}^n X_i^m, \quad m = 1, 2, 3, \dots \quad (1.63)$$

The first moment is sometimes denoted by  $\bar{X}$ :

$$\bar{X} = M_1 = \frac{1}{n} \sum_{i=1}^n X_i \quad (1.64)$$

and the sample variance by  $S^2$ :

$$S^2 = \frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2 = \frac{1}{n} \sum_{i=1}^n X_i^2 - \bar{X}^2 = M_2 - M_1^2. \quad (1.65)$$

Because they are functions of random variables, statistics are also random variables, with probability distributions induced by that of the population random variable. For instance, if the distribution of the population variable  $X$  has mean  $E[X] = \mu$  and variance  $Var[X] = \sigma^2$ , then

$$\begin{aligned} E[\bar{X}] &= E\left[\frac{1}{n} \sum_{i=1}^n X_i\right] = \frac{1}{n} \sum_{i=1}^n E[X_i] = \mu, \\ Var[\bar{X}] &= Var\left[\frac{1}{n} \sum_{i=1}^n X_i\right] = \frac{1}{n^2} \sum_{i=1}^n \sigma^2 = \frac{\sigma^2}{n}. \end{aligned} \quad (1.66)$$

In addition,

$$\begin{aligned} E[S^2] &= E\left[\frac{1}{n} \sum_{i=1}^n (X_i - \mu + \mu - \bar{X})^2\right] \\ &= E\left[\frac{1}{n} \sum_{i=1}^n (X_i - \mu)^2 - (\bar{X} - \mu)^2\right] \end{aligned}$$

$$\begin{aligned}
 &= \sigma^2 - \text{Var}[\bar{X}] \\
 &= \frac{n-1}{n} \sigma^2.
 \end{aligned}
 \tag{1.67}$$

Assume that  $\langle x_1, x_2, \dots, x_n \rangle$  is a set of observations from the random sample  $\langle X_1, X_2, \dots, X_n \rangle$  of size  $n$ . The **sample distribution function** or **empirical distribution function**  $F_n(x)$  is defined for all real  $x$  by

$$F_n(x) = \sum_{x_i \leq x} \frac{1}{n} = \frac{\# \text{ observations } \leq x}{n}. \tag{1.68}$$

Although it is not itself a probability distribution function,  $F_n(x)$  has the same form as a cumulative distribution function for a discrete random variable defined on a finite set of equally probable outcomes.  $F_n(x)$  therefore has the properties of such a function—specifically, (1.29) through (1.33). In particular, the first moment evaluated at the observations  $\langle x_1, x_2, \dots, x_n \rangle$  is the mean of the sample distribution:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i. \tag{1.69}$$

The variance of the sample distribution is defined similarly:

$$s^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2. \tag{1.70}$$

Often, for ease of analysis, data in a set of observations from a random sample are grouped into a collection of disjoint intervals or cells:  $\{(c_{k-1}, c_k]\}$  ( $k = 1, 2, \dots, m$ ). In this case, (1.69) has the form

$$\bar{x} = \frac{1}{n} \sum_{k=1}^m n_k a_k, \tag{1.71}$$

where

$$n_k = \# \text{ observations in } (c_{k-1}, c_k] \quad \text{and} \quad n = \sum_{k=1}^m n_k,$$

$$a_k = \sum_{x_i \in (c_{k-1}, c_k]} \frac{x_i}{n_k} = \text{average observation in } (c_{k-1}, c_k].$$

If the sum of the observations in the  $k^{\text{th}}$  cell is unavailable, so that  $a_k$  is not known exactly, one could approximate the average  $a_k$  in formula (1.71) by the interval midpoint:

$$a_k \approx \frac{1}{2}(c_{k-1} + c_k). \tag{1.72}$$

## 1.5. Fitting Distributions

Actuaries frequently find it desirable to fit a parametric distribution model to a set of claim data, both for the purpose of smoothing the empirical distribution but also for interpolating among or extrapolating beyond the existing data. The problem of extrapolation is particularly important in describing the behavior of the very large claims in a claim-size distribution—the probability of such claims is usually so small that in any given sample of claim-size data the number of large claims is insufficient to characterize adequately the right-hand tail of the underlying population distribution. In this section we review the rudimentary details of several methods used to fit probability models to data.

We begin with a finite set of claim data  $\langle x_1, x_2, \dots, x_n \rangle$ , which can be interpreted as a set of particular values for a random sample  $\langle X_1, X_2, \dots, X_n \rangle$  from a population random variable  $X$  with an unknown distribution. The variables  $\langle X_i \rangle$  are independent, and each has the same distribution as  $X$ , representing the results of a single random selection from the population variable  $X$ . Here,  $X$  could be either a claim-size or claim-count variable, as discussed in Chapters 2 and 3. The aim is to find a probability model for the distribution of  $X$ , consistent with the sample observations  $\langle x_1, x_2, \dots, x_n \rangle$ .

In practice, in order to justify the interpretation as a random sample from a single population, claim data must often be adjusted in order that all are on the same basis. For example, claim-size data obtained from multiple policy or accident years may very well require the application of trend factors to remove the effects of monetary inflation over time.

Methods of fitting models to sample data usually depend on first selecting a distribution family, that is, a collection of distribution functions  $\{F_{\Theta}(x)\}$  indexed by a finite set of numeric parameters  $\Theta = \langle \theta_1, \theta_2, \dots, \theta_r \rangle$ . The choice of such a family can be arbitrary, but should take into consideration any known or desired properties of the distribution under investigation.

Having chosen such a family, one must next identify the particular member of the selected distribution family that, according to some selection criterion, best describes the data. This is usually done by finding an appropriate *point estimate* for each distribution parameter—usually in the form of a statistic, that is, a function of the sample random variables:

$$\hat{\theta}_i = g_i(X_1, \dots, X_n), \quad i = 1, 2, \dots, r. \quad (1.73)$$

For example, the sample-moment statistics (1.63) are useful in this regard.

In a given situation there may exist several possible parameter estimators, statistics which could differ in their ease of computation or in the general properties of estimators deemed desirable by statisticians. The latter include the three estimator properties described below—*bias*, *consistency*, *efficiency*.

Assume that  $X$  is a random variable with a distribution that depends on the unknown parameter  $\theta$ . Let  $\langle X_1, X_2, \dots, X_n \rangle$  be a random sample of  $X$  of size  $n$  and assume that

$\hat{\theta}_n$  is a function of the sample random variables, a statistic whose distribution depends on the parameter  $\theta$ .

- $\hat{\theta}_n$  is said to be an **unbiased estimate** of  $\theta$  whenever the mean of  $\hat{\theta}_n$  is just  $\theta$ :  $E[\hat{\theta}_n] = \theta$ . For example, the expected value of the sample mean  $\bar{X}$  is  $E[\bar{X}] = E[X]$ . Thus, if  $E[X] = \theta$ , then  $\hat{\theta}_n = \bar{X}$  is an unbiased estimate of  $\theta$ . However, because  $E[S^2] = (1 - \frac{1}{n}) \text{Var}[X]$ , the sample variance statistic is a **biased** estimate of  $\text{Var}[X]$ , although the bias  $\frac{1}{n} \text{Var}[X]$  is insignificant for large samples.
- $\hat{\theta}_n$  is said to be a **consistent estimate** of  $\theta$  if  $\hat{\theta}_n$  converges in probability to  $\theta$ , that is,

$$\lim_{n \rightarrow \infty} \Pr \{ |\hat{\theta}_n - \theta| < \varepsilon \} = 1 \quad \text{for all } \varepsilon > 0.$$

It can be shown that when  $\text{Var}[X]$  is finite  $\bar{X}$  converges in probability to  $E[X]$ , and so, as in the above example,  $\hat{\theta}_n = \bar{X}$  is a consistent estimate of  $\theta = E[X]$ . In addition, if  $\hat{\theta}_n$  is an unbiased estimate of  $\theta$  and if  $\lim_{n \rightarrow \infty} \text{Var}[\hat{\theta}_n] = 0$ , then  $\hat{\theta}_n$  is also a consistent estimate of  $\theta$ .

- Suppose that  $\hat{\theta}_n$  is an unbiased estimate of  $\theta$  and that for all estimates  $\hat{\theta}_n^*$  for which  $E[\hat{\theta}_n^*] = \theta$ , we have  $\text{Var}[\hat{\theta}_n] \leq \text{Var}[\hat{\theta}_n^*]$  for all  $\theta$ . In this case  $\hat{\theta}_n$  is said to be an **unbiased, minimum variance estimate** of  $\theta$ . Statistic  $\hat{\theta}_n$  is also called the **most efficient estimator** of  $\theta$ .

To find an optimal fitted distribution it is often advisable to try more than one method of calculating a set of parameter estimates  $\hat{\Theta}$  and sometimes work with more than one distribution family. Then, after deciding on a particular parameter estimate, one should in the final step evaluate how well the distribution  $F_{\hat{\Theta}}(x)$  fits the sample data. One could do this with an informal comparison of the fitted and empirical distribution functions or more rigorously by employing a standard goodness-of-fit test, such as that based on the chi-square statistic.

Briefly described below are four useful techniques of parameter estimation: the *method of moments*, the *maximum-likelihood method*, the *minimum chi-square method*, and *minimum-distance methods*.<sup>13</sup>

### Method-of-Moments Estimation

First proposed by the English statistician Karl Pearson, this is the oldest technique of estimating parameters and perhaps the easiest to apply in practice. The method-of-moments method is based on the usually reasonable assumption that the sample moments are good estimates of the corresponding population moments.<sup>14</sup>

Accordingly, one computes successive sample moments  $M_m = \frac{1}{n} \sum_{i=1}^n x_i^m$  evaluated at the sample data points  $\langle x_1, x_2, \dots, x_n \rangle$  and then equates them to the corresponding

<sup>13</sup> More complete discussions of estimation techniques can be found in standard mathematical statistics texts. For example, see Hogg and Craig [7], chapter 6, or Lindgren [13], chapter 5.

<sup>14</sup> Karl Pearson (1857–1936), founder of the field of mathematical statistics, established the world's first college department of statistics at University College London. His contributions include the foundations of statistical hypothesis testing and decision theory, and he is the eponymous inventor of the chi-square goodness-of-fit test.

moments of the assumed distributional model, which depend on the unknown parameters  $\Theta$ :

$$M_m = E_{\Theta}[X^m], \quad m = 1, 2, 3, \dots \quad (1.74)$$

One must use as many of these equations as is necessary to determine the parameters uniquely—in general, when there are  $r$  parameters to estimate use (1.74) for  $m = 1, 2, \dots, r$ . The resulting system of equations could then be solved to obtain  $\hat{\Theta} = \langle \hat{\theta}_1, \hat{\theta}_2, \dots, \hat{\theta}_r \rangle$  in terms of the observed data values  $\langle x_i \rangle$ .

Method-of-moments estimates have the advantage of usually being very easy to calculate, but they do not always have the desirable properties indicated above—they are often consistent, but are sometimes biased.

**Example 1.13.** A possibly unbalanced die is rolled and the number of spots on the upper surface is observed. We define a Bernoulli random variable:

$$X = \begin{cases} 1 & \text{if \# spots} = 6 \\ 0 & \text{if \# spots} \neq 6. \end{cases}$$

The probability distribution for  $X$  has a single unknown parameter

$$p = \Pr\{X = 1\} = \Pr\{\text{\# spots} = 6\}$$

with the probability mass function

$$f(x) = \begin{cases} p^x (1-p)^{1-x} & \text{if } x \in \{0, 1\} \\ 0 & \text{if } x \notin \{0, 1\}. \end{cases}$$

It is evident that  $E[X] = p$ .

In order to estimate parameter  $p$ , the die is rolled 50 times, creating a random sample of size  $n = 50$ . Twelve sixes are observed, so that  $\sum_{i=1}^{50} x_i = 12$ . The method-of-moments estimate of parameter  $p$  is obtained from the unbiased, consistent estimator  $\hat{p} = \bar{x}$ :

$$\hat{p} = \frac{12}{50} = 0.2400. \blacksquare$$

### Maximum-Likelihood Estimation

Simply stated, a maximum-likelihood estimator  $\hat{\Theta}$  of distribution parameters  $\Theta$  specifies the member  $F_{\hat{\Theta}}(x)$  of a distribution family which maximizes the probability of obtaining the values  $\langle x_1, x_2, \dots, x_n \rangle$  actually observed in a random sample  $\langle X_1, X_2, \dots, X_n \rangle$ .

To begin, let  $\langle X_1, X_2, \dots, X_n \rangle$  be a random sample from a probability distribution with density function  $f_{\Theta}(x)$ . The joint probability density function for the sample is then  $\prod_{i=1}^n f_{\Theta}(x_i)$ . Evaluated at the observed sample values  $\langle x_1, x_2, \dots, x_n \rangle$ , this product

can be regarded as a function of the parameters  $\Theta$ . As such, it is called the **likelihood function** of the random sample:

$$L(\Theta) = \prod_{i=1}^n f_{\Theta}(x_i). \quad (1.75)$$

Therefore,  $\hat{\Theta} = \langle \hat{\theta}_1, \hat{\theta}_2, \dots, \hat{\theta}_r \rangle$  is a maximum-likelihood estimator if it yields a maximum value for the likelihood function:

$$L(\hat{\Theta}) \geq L(\Theta) \quad \text{for all } \Theta.$$

Because they are located at points at which the likelihood function attains an extreme value, maximum-likelihood estimators are usually, but not always, unique.

An analytic solution of the maximum-value problem can be sought by setting the  $r$  partial derivatives of the likelihood function equal to 0 and solving the resulting system of equations. However, in most situations it is easier to solve the equivalent problem of maximizing the **log-likelihood function**  $\log L(\Theta)$ , using the same technique:<sup>15</sup>

$$\begin{cases} \frac{\partial}{\partial \theta_1} \log L(\theta_1, \dots, \theta_r) = 0 \\ \vdots \\ \frac{\partial}{\partial \theta_r} \log L(\theta_1, \dots, \theta_r) = 0. \end{cases}$$

(Recall that  $\log x$  is an increasing function of  $x$ , so that whenever  $L(\hat{\Theta})$  is a maximum value of the likelihood function,  $\log L(\hat{\Theta})$  is a maximum value of  $\log L(\hat{\Theta})$ , and conversely.) If, as it often does, the analytic approach proves intractable, one could employ an iterative solving algorithm, available in many computer software packages.

Maximum-likelihood estimators are usually consistent and efficient, but not always unbiased, estimators of the distribution parameters.

**Example 1.14.** Returning to the problem of Example 1.13, we now determine the maximum-likelihood estimator of  $p = \Pr\{X = 1\}$  for a sample of size  $n$ . The likelihood function is

$$L(p) = \prod_{i=1}^n p^{x_i} (1-p)^{1-x_i} = p^{\sum x_i} (1-p)^{n-\sum x_i}$$

and so the log-likelihood function is

$$\log L(p) = (\log p) \sum_{i=1}^n x_i + \log(1-p) \left( n - \sum_{i=1}^n x_i \right).$$

<sup>15</sup> Throughout this monograph,  $\log x$  denotes the natural (base  $e$ ) logarithm function of  $x$ .

Therefore, the equation

$$\frac{\partial}{\partial p} \log L(p) = \frac{1}{p} \sum_{i=1}^n x_i - \frac{1}{1-p} \left( n - \sum_{i=1}^n x_i \right) = 0$$

has the solution  $\hat{p} = \frac{1}{n} \sum_{i=1}^n x_i = \bar{x}$ , a maximum-likelihood estimate of  $p$ . ■

### Minimum Chi-Square Estimation

The minimum chi-square estimator  $\hat{\Theta}$  of distribution parameters  $\Theta$  specifies the member  $F_{\hat{\Theta}}(x)$  of a selected distribution family that minimizes an associated chi-square statistic. This statistic is identical in form to that used in the classic Pearson chi-square goodness-of-fit test.

To construct the chi-square statistic one must first group the data from a random sample of size  $n$  into a smaller number  $m$  of classes or cells. If the population distribution is of the continuous type, like that of most size-of-loss random variables, then the cells may take the form of intervals of real numbers. Otherwise, if the distribution is discrete and the random variable is integer-valued—like that of a claim-count random variable—then the cells must be subsets of the nonnegative integers.

We then calculate the cell frequencies:

$$n_k = \# \text{ observations in the } k^{\text{th}} \text{ cell } (k = 1, 2, \dots, m) \quad \text{and} \quad n = \sum_{k=1}^m n_k.$$

The statistic  $\chi^2(\Theta)$  is given by

$$\chi^2(\Theta) = \sum_{k=1}^m \frac{|n_k - \phi_k(\Theta)|^2}{\phi_k(\Theta)}, \quad (1.76)$$

where  $\phi_k(\Theta)$  is the expected number of sample observations in the  $k^{\text{th}}$  cell, based on the population distribution with parameters  $\Theta$ . For example, if the random variable  $X$  has a continuous distribution, with cells of the form  $(c_{k-1}, c_k]$ , then

$$\phi_k(\Theta) = n \cdot (F_{\Theta}(c_k) - F_{\Theta}(c_{k-1})).$$

Since each expected value  $\phi_k(\Theta)$  is a function of  $\Theta$ , so is  $\chi^2(\Theta)$ , and a minimum chi-square estimate of  $\Theta$  is a value  $\hat{\Theta}$  at which the statistic achieves a minimum value:

$$\chi^2(\hat{\Theta}) \leq \chi^2(\Theta) \text{ for all } \Theta.$$

Calculation of  $\hat{\Theta}$  is complicated by the fact that both numerator and denominator of  $\chi^2(\Theta)$  depend on  $\Theta$ . However, use of a computer-implemented iterative solving algorithm is a practical way of overcoming such computational complexities.

One advantage of using minimum chi-square estimation of the distribution parameters, of course, is the fact that at the end of the procedure one has a built-in

goodness-of-fit test available. The value of the chi-square statistic under the assumption of the fitted distribution—the null hypothesis—has already been computed. For illustrations of this method, refer to Examples 2.8 and 2.11.

### Minimum-Distance Estimation

As with the minimum chi-square method discussed previously, minimum-distance methods are applied to grouped sample data. In particular, the method is most useful in estimating parameters for a random variable  $X$  with a continuous distribution. Suppose, for example, the  $n$  sample values have been assigned to  $m$  cell intervals of the form  $(c_{k-1}, c_k]$ , where

$$n_k = \# \text{ observations in } (c_{k-1}, c_k] \quad (k = 1, 2, \dots, m) \quad \text{and} \quad n = \sum_{k=1}^m n_k.$$

The empirical sample distribution function at the cell boundary point  $c_k$  is

$$F_n(c_k) = \frac{1}{n} \sum_{i=1}^k n_i. \quad (1.77)$$

One minimum-distance estimator of parameter  $\Theta$  is the value  $\hat{\Theta}$  that minimizes the “distance”  $D(\Theta)$  between the sample and parametric distribution functions,  $F_n(x)$  and  $F_\Theta(x)$ , evaluated at the cell boundary points:

$$D(\Theta) = \sqrt{\sum_{k=1}^m |F_n(c_k) - F_\Theta(c_k)|^2}. \quad (1.78)$$

Clearly,  $D(\Theta)$  is a function of  $\Theta$ , and  $\hat{\Theta}$  must satisfy  $D(\hat{\Theta}) \leq D(\Theta)$  for all  $\Theta$ .

An analytic solution of a minimum-distance problem is unlikely to be straightforward, but as in the case of minimum chi-square estimation,  $\hat{\Theta}$  can usually be obtained by applying a computer utility or software that implements an iterative solving algorithm. Minimum-distance methods in an actuarial setting are more fully discussed in a paper by Klugman and Parsa [12]. Examples of minimum-distance fitting can be found in Examples 2.9 and 2.10.

## 1.6. Problems

**1.1** Let  $\Omega$  be the sample space for an experiment of chance.

- (a) Show that the set  $\{\emptyset, E, E^c, \Omega\}$  is a  $\sigma$ -algebra.
- (b) Assume that  $S$  is a  $\sigma$ -algebra, with  $E, F \in S$ . Show that  $E \cap F \in S$ .
- (c) Assume that  $\Omega = \{a, b, c, d\}$  and that  $\{a\}$  and  $\{b, c\}$  are events. Find the smallest  $\sigma$ -algebra  $S$  containing this pair of events—this is the  $\sigma$ -algebra generated by  $\{a\}$  and  $\{b, c\}$ .

**1.2** Assume that  $(\Omega, S, P)$  is a probability space. Verify the following properties of  $P$ :

- (a) Equation (1.4).                      (b) Equation (1.5).
- (c) Equation (1.6).                      (d) Property (1.7).
- (e) Equation (1.8).                      (f) Property (1.9).

- 1.3** Assume that  $(\Omega, S, P)$  is a probability space. Verify the following properties of the probability function  $P$
- (a) If  $E_1 \subseteq E_2 \subseteq E_3 \subseteq \dots$  is an ascending sequence of sets in  $S$ , then  $P(\bigcup_n E_n) = \lim_{n \rightarrow \infty} P(E_n)$ .
  - (b) If  $E_1 \supseteq E_2 \supseteq E_3 \supseteq \dots$  is a descending sequence of sets in  $S$ , then  $P(\bigcap_n E_n) = \lim_{n \rightarrow \infty} P(E_n)$ .
- 1.4** An urn contains three red and four black chips. Two chips are drawn at random without replacement. Calculate:
- (a) the probability that both chips are red.
  - (b) the probability that both chips are black.
  - (c) the expected number of red chips.
- 1.5** For a probability space  $(\Omega, S, P)$  with events  $E$  and  $F$  show that
- (a)  $P(E) = P(F) \cdot P(E|F) + P(F^c) \cdot P(E|F^c)$ .
  - (b) If  $E$  and  $F$  are independent, then  $P(E \cup F) = 1 - P(E^c)P(F^c)$ .
- 1.6** Consider the following generalization of Example 1.4. Two fair dice are rolled. Let  $E_m$  denote the event of obtaining a total of  $m$  spots ( $m = 2, 3, \dots, 12$ ) and  $F_n$  the event that the first die shows  $n$  ( $n = 1, 2, \dots, 6$ ) spots. For what values of  $(m, n)$  are events  $E_m$  and  $F_n$  independent? Explain.
- 1.7** A random variable  $X$  takes on five values with nonzero probability:  $R_X = \{1, 2, 3, 4, 5\}$ . The probability mass function is tabulated below, where  $k$  is a constant.

| $x$    | 1     | 2       | 3   | 4       | 5      |
|--------|-------|---------|-----|---------|--------|
| $f(x)$ | $k^2$ | $0.50k$ | $k$ | $0.25k$ | $0.50$ |

Calculate:

- (a)  $k$ .
- (b)  $F(2)$ .
- (c)  $\Pr\{X \text{ is odd}\}$ .
- (d)  $E[X]$ .
- (e)  $\text{Var}[X]$ .

- 1.8** Verify the following properties of the expected value  $E[g(X)]$ .
- (a) Equation (1.46).
  - (b) Equation (1.47).
  - (c) Equation (1.48).
  - (d) Property (1.49).
  - (e) Property (1.50).
- 1.9** Verify the following properties of the variance  $\text{Var}[X]$ .
- (a) Equation (1.53).
  - (b) Equation (1.54).
  - (c) Equation (1.55).
- 1.10** A discrete random variable  $N$  has the countably infinite range space  $R_N = \{1, 2, 3, \dots\}$ .
- (a) Can the outcomes in  $R_N$  be assigned equal probabilities?
  - (b) Find the constant  $k$  such that  $f(n) = k p^n$  ( $0 < p < 1$ ,  $n \in R_N$ ) is a probability mass function for  $N$ .
  - (c) Using the function of part (b), calculate  $E[N]$  and  $\text{Var}[N]$ .

**1.11** A random variable  $X$  has the cumulative distribution function

$$F(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 - 0.25e^{-0.50x} & \text{if } 0 \leq x < \infty. \end{cases}$$

Calculate:

- (a)  $\Pr\{X = 0\}$ .      (b)  $\Pr\{X = 1\}$ .      (c)  $\Pr\{X < 1\}$ .  
 (d)  $\Pr\{1 < X < 2\}$ .      (e)  $E[X]$ .      (f)  $\text{Var}[X]$ .

**1.12** Assume random variable  $X$  has a continuous distribution, with c.d.f.  $F(x)$ .

- (a) Show that  $\Pr\{X = c\} = 0$  for all real  $c$ .  
 (b) Show that  $\Pr\{a < X < b\} = \Pr\{a \leq X \leq b\} = F(b) - F(a)$  for all  $a$  and  $b$ .

**1.13** Evaluate these Riemann–Stieltjes integrals.

- (a)  $\int_0^1 x \, d(x^2)$ .      (b)  $\int_1^3 x^2 \, d(\log x)$ .  
 (c)  $\int_0^\infty d(1 - e^{-x})$ .      (d)  $\int_0^5 x \, d(\llbracket x \rrbracket)$ .<sup>16</sup>

**1.14** Evaluate these Riemann–Stieltjes integrals, in which  $F$  denotes the discrete cumulative distribution function of Example 1.7.

- (a)  $\int_0^\infty x \, dF(x)$ .      (b)  $\int_0^\infty x^2 \, dF(x)$ .      (c)  $\int_0^\infty \exp(tx) \, dF(x)$ .

**1.15** Evaluate these Riemann–Stieltjes integrals, in which  $F$  denotes the continuous c.d.f. of the uniform distribution of Example 1.8(a).

- (a)  $\int_0^\infty x \, dF(x)$ .      (b)  $\int_0^\infty x^2 \, dF(x)$ .      (c)  $\int_0^\infty \exp(tx) \, dF(x)$ .

**1.16** A random variable  $X$  has the distribution function

$$F(x) = \begin{cases} 0 & \text{if } -\infty < x < 0 \\ 1 - (0.20)e^{-x/100} - (0.80)e^{-x/200} & \text{if } 0 \leq x < \infty. \end{cases}$$

- (a) Show that the distribution of  $X$  can be interpreted as the mixture of two exponential distributions.  
 (b) Determine  $E[X]$  and  $\text{Var}[X]$ .

**1.17** Calculate  $E[X]$  and  $\text{Var}[X]$  for the random variable  $X$  of Example 1.8(a).

**1.18** Calculate  $E[X]$  and  $\text{Var}[X]$  for the random variable  $X_a$  of Example 1.9(a).

**1.19** Assume that  $X$  is a random variable with  $E[X] = 0$  and  $\text{Var}[X] = 1$ . Calculate  $E[Y]$  and  $\text{Var}[Y]$  for  $Y = \sigma X + \mu$ .

**1.20** Find the moment-generating functions for:

- (a) the standard normal distribution.  
 (b) the normal distribution of  $Y = \sigma Z + \mu$ , where  $Z$  is the standard normal random variable.  
 (c) the distribution of  $X$ , uniformly distributed on the interval  $[\alpha, \beta]$ .

<sup>16</sup>  $\llbracket x \rrbracket$  denotes the *greatest integer function*, defined for every real  $x$  as the unique integer  $m$  satisfying  $m \leq x < m + 1$ . For example,  $\llbracket 5 \rrbracket = 5$ ,  $\llbracket \pi \rrbracket = 3$ ,  $\llbracket -1.5 \rrbracket = -2$ .

**1.21** Random variable  $N$  has the geometric distribution defined by (1.20). Determine:

- (a)  $M(t)$ .                      (b)  $E[N]$ .                      (c)  $Var[N]$ .  
 (d) the probability that an odd number of trials is required to obtain the first success.

**1.22** Justify the algebraic rearrangement in the second step of (1.67).

**1.23** Find the maximum-likelihood estimator of the parameter  $\beta$  for the exponential distribution of Example 1.8(b).

**1.24** Random variable  $X$  has a mixed probability density function  $f$  defined by

$$f(x) = \sum_{k=1}^n \omega_k f_k(x), \text{ where } 0 < \omega_k < 1 \text{ and } \sum_{k=1}^n \omega_k = 1.$$

Show that  $E[X]$  and  $Var[X]$  are given by

$$E[X] = \sum_{k=1}^n \omega_k \mu_k \quad \text{and} \quad Var[X] = \sum_{k=1}^n \omega_k \sigma_k^2 + \sum_{k=1}^n \omega_k (\mu_k - E[X])^2,$$

where  $\mu_k$  and  $\sigma_k^2$  are the respective mean and variance of the  $k^{th}$  distribution.

