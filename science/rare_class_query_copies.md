# Rare classes with several copies of one query

The [single-copy rare-class law](rare_class.md) requires order $`1/q`$ measured reference copies per class to reduce the minority risk by a fixed fraction. This page asks how that cost changes when the classifier receives $`t`$ copies of the **same** future query. The classical reference cost becomes order $`q^{-1/t}`$ in the regime below. A quantum symmetry test needs a reference budget independent of $`q`$.

## Experiment and sample law

Draw two independent Haar pure states in $`\mathbb C^d`$, with $`d\geq2`$, and provide $`m`$ labeled reference copies of each. The query consists of $`t\geq1`$ copies of the majority state with probability $`p=1-q`$, or of the minority state with probability $`q\in(0,1/2]`$. The prior is known before training. The measured-training interface permits an arbitrary collective reference measurement and an unrestricted classical record, followed by any joint measurement on the query copies. The retained interface lets the reference specimens remain quantum until the query arrives. Risks are Haar-average probabilities of a wrong label, with a single output.

Define

```math
D_s=\binom{d+s-1}{s},\qquad
B=\binom{m+t}{t},\qquad
C=\frac{D_mD_t}{D_{m+t}},\qquad
h_{d,t}=\frac{d-1}{d+t-1}.
```

For fixed $`d,t`$ and $`0\lt\eta\lt h_{d,t}`$, let $`m_{\mathrm C}(q,\eta)`$ and $`m_{\mathrm Q}(q,\eta)`$ be the least per-class reference budgets that give risk at most $`(1-\eta)q`$ at the respective interfaces. As $`q\downarrow0`$,

```math
m_{\mathrm C}(q,\eta)=\Theta_{d,t,\eta}(q^{-1/t}),\qquad
m_{\mathrm Q}(q,\eta)=\Theta_{d,t,\eta}(1).
```

The query budget $`t`$ is fixed in this limit. The fractional improvement is measured against the majority-only risk $`q`$, so its absolute size still vanishes with $`q`$.

## The exact threshold gives the classical lower bound

The [weighted identification theorem](https://github.com/GoGoKo699/Quantum-Reference-Identification/blob/d1b6e1583c5fba0dc757f3a75f0db622183315f8/science/prior_weighted_identification.md) gives $`R_{\mathrm C}=q`$ exactly when $`p/q\geq B`$, including equality. Its converse allows collective measurements of both references. The minimizer may include minority decisions that tie the majority risk at equality. For $`d=2,t=1`$ the condition reduces to $`p/q\geq m+1`$, or $`q\leq1/(m+2)`$, the original threshold.

Any strictly positive fractional improvement therefore requires $`B\gt p/q`$. Since $`B\leq(m+t)^t/t!`$, the required $`m`$ is larger than $`(t!p/q)^{1/t}-t`$. This proves the lower order for every fixed $`\eta\gt0`$ that is attainable.

## Covariant estimation attains the classical order

Measure the $`m`$ majority references with the covariant POVM $`D_m|\phi^{\otimes m}\rangle\langle\phi^{\otimes m}|\,d\phi`$, where $`d\phi`$ is normalized Haar measure. Given its outcome $`\phi`$, predict minority only when all $`t`$ query copies pass the projector onto the orthogonal complement of $`\phi`$. This protocol ignores the minority references.

Write $`(a)_t=a(a+1)\cdots(a+t-1)`$. For a majority query, the posterior overlap $`X=|\langle\phi|\psi_{\mathrm{maj}}\rangle|^2`$ has law $`\mathrm{Beta}(m+1,d-1)`$. Haar overlap has density proportional to $`(1-X)^{d-2}`$, and the measurement multiplies that density by $`X^m`$. Conditional on the unknown ray, the probability that all query copies pass is $`(1-X)^t`$. Averaging gives the majority false-positive probability $`(d-1)_t/(m+d)_t`$. For a minority query the ray remains independent Haar, so the true-positive probability is $`(d-1)_t/(d)_t=h_{d,t}`$. The exact risk of this protocol is

```math
R_{\mathrm{cov}}=p\frac{(d-1)_t}{(m+d)_t}+q(1-h_{d,t}).
```

When $`\eta\lt h_{d,t}`$, the target follows as soon as the false-positive term is at most $`q(h_{d,t}-\eta)`$. For example, it suffices to take any nonnegative integer $`m`$ satisfying

```math
m+d\geq \left[\frac{p(d-1)_t}{q(h_{d,t}-\eta)}\right]^{1/t}.
```

The power law follows with $`d,t,\eta`$ held fixed. At $`t=1,d=2`$, the risk reduces to $`p/(m+2)+q/2`$, as in the single-copy construction.

## A retained symmetry test needs a constant reference budget

Keep only the $`m`$ majority references. When the query arrives, test whether all $`m+t`$ systems lie in the symmetric subspace and predict minority on rejection. A majority query always passes. On a minority query the blocks remain independent, with averaged state $`I_{\mathrm{Sym}^m}/D_m\otimes I_{\mathrm{Sym}^t}/D_t`$. The symmetric projector has rank $`D_{m+t}`$, so the minority passes with probability $`1/C`$. The risk is exactly

```math
R_{\mathrm{sym}}=\frac qC.
```

For fixed $`d,t`$, $`C\to D_t`$ as $`m\to\infty`$. Also $`h_{d,t}\leq1-1/D_t`$, because the rank $`\binom{d+t-2}{t}`$ of the all-orthogonal query projector is at most $`D_t-1`$. Thus a finite $`m`$ independent of $`q`$ achieves any $`\eta\lt h_{d,t}`$. More generally this comparison attains any $`\eta\lt1-1/D_t`$ with a constant budget. With $`m=0`$ the two averaged hypotheses coincide and no positive fractional improvement is possible, giving the constant lower bound. The test is the universal symmetry comparison already used in the [single-copy law](rare_class.md) and the [reference identification decoder](https://github.com/GoGoKo699/Quantum-Reference-Identification/blob/1212b747bf8c5dca54a9d210cd554536bc0f67ae/science/quantum_identification.md).

## Worked example with two query qubits

Take $`d=2,t=2,q=1/100`$ and target a 25% reduction from majority risk. The classical threshold requires $`\binom{m+2}{2}\gt99`$ before any strict improvement, so $`m\geq13`$ is necessary. The covariant protocol gives risk $`2p/[(m+2)(m+3)]+2q/3`$. Its first $`m`$ meeting the target is $`47`$, since this requires $`(m+2)(m+3)\geq2376`$. These bounds give an interval for the optimal classical budget. For the retained procedure, $`m=1`$ gives $`C=3/2`$ and risk $`2q/3`$, meeting the target with one retained qubit from the majority class.

## Resource account

The supplied training set has $`2m`$ specimens and the query has $`t`$. Both explicit procedures ignore the minority references. The measured protocol stores a classical outcome and sets a query measurement from it. Exact covariant estimation and conditional measurement specify ideal POVMs. The retained protocol pays to store $`m`$ specimens through the training-to-query boundary and to perform the symmetry test. The test consumes one query and can consume its references. [Reference identification resources](https://github.com/GoGoKo699/Quantum-Reference-Identification/blob/1212b747bf8c5dca54a9d210cd554536bc0f67ae/science/resources.md) give a known-permutation implementation and its precision requirements. These are specimen bounds for Haar pure states and fixed $`d,t`$, with equal reference counts and known deployment prevalence.
