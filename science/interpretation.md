# What class imbalance changes

The training supply can stay exactly the same while the optimal use of it changes. Here both unknown qubit classes have the same number of labeled examples, and their deployment probabilities are known. A learner may optimize every training operation for those probabilities.

At balance, the classical record can preserve everything needed for the optimal one-test decision. This is the established memory-free qubit learning example. The new [finite-size theorem](activation.md) shows that the equality is isolated: every interior unequal prior gives a strict advantage for retained examples.

## A decision sector becomes usable

The Haar-averaged discrimination problem has a globally symmetric sector where the two unweighted hypotheses coincide. At balance that sector has zero weighted difference, so an optimal measurement has freedom there. The classical learner uses that freedom in the known covariant construction.

A prior tilt gives the same sector a nonzero sign. The optimal minority effect must now annihilate its all-up vector. A nonzero transition entry in the one-excitation sector then makes the effect nonpositive under partial transpose across the training/test cut. Every classical-record classifier has positive partial transpose across that cut. This is the operational obstruction; it does not depend on limiting the classical outcome length.

The [one-copy example](one_copy.md) makes the response quantitative. Near balance the best classical risk is unchanged on an interval, while the quantum risk has a linear cusp in the absolute prior tilt. At stronger imbalance, every classical training record can become unable to improve on majority guessing.

## Three limits answer different questions

| Regime | Supported statement |
|---|---|
| Fixed finite $`n`$, prior tilted away from balance | Strict risk advantage for every $`0\lt\lvert2p-1\rvert\lt1`$. |
| Fixed nonzero interior tilt, $`n`$ grows | The optimal memory penalty has order $`1/n`$, with a positive asymptotic lower coefficient and a finite upper bound. The exact leading coefficient is open. |
| Minority probability decreases and a fixed fractional reduction of its risk is required | Classical training costs order $`1/q`$ copies per class; a constant number of retained references suffices. |

The [plateau bound](plateau.md) gives a further joint finite interval, with explicit constants. None of the fixed-prior asymptotic statements is uniform through balance or the trivial prior endpoints.

For rare classes the target absolute error itself shrinks with prevalence. A fixed fractional improvement is meaningful for rare-event recognition, but it does not imply constant absolute contrast or inexpensive empirical validation.

## Purity, noise and repeatability

The exact no-false-positive comparison test relies on pure repeated prototypes. Full-rank noise changes that property. The [noise argument](noise.md) instead uses continuity and simulated depolarization to certify an open neighborhood of finite examples. It leaves fixed-noise large-training behavior open.

One prediction may consume the retained reference. A classical record can be reused, while this account promises no returned quantum program. Many-test model reuse is therefore a different resource comparison. The [related-work discussion](../references/related_work.md) places the result beside inductive-learning classicalization.

These are accuracy and supplied-state sample statements with charged quantum storage and processing. They do not establish a generic advantage for classical datasets, an efficient universal learning algorithm for arbitrary distributions, or a hardware runtime crossover.

