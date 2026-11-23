# Learning the class-imbalance result

A balanced quantum training library can be followed by imbalanced future tests. The learner knows that prevalence before training. The question is whether a classical record can preserve everything needed for the best later prediction.

Start with the [worked tutorial](TUTORIAL.md). It follows one complete one-copy experiment and connects the example to the general results.

| To understand | Read |
|---|---|
| The physical task and a complete example | [Worked tutorial](TUTORIAL.md) |
| Textbook foundations and verified locations | [Watrous bridge](WATROUS_BRIDGE.md) |
| The project's conceptual dependencies | [30-milestone map](MILESTONES.md) |
| A specialist theorem or proof directly | [Scientific index](../science/README.md) |
| What the finite calculations reproduce | [Verification guide](../verification/README.md) |

## One anchor and one project map

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, in the **standard-layout author manuscript** linked from the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). The bridge identifies a short route through states, measurements, biased discrimination, symmetric-state averages, separable effects and semidefinite optimization. Its printed-page locators were verified against that version.

There are exactly **30 project-defined milestones**: **12 background/preliminaries** and **18 narrative/innovation**. The background joins specimens, recorded outcomes and decision risk into the experiment. The narrative follows the prior-induced obstruction through exact finite results, the leading fixed-prior penalty, rare classes, noise and complete resource accounting. This allocation follows the scientific story and is shared by all readers.

The bridge distinguishes textbook facts, locally supplied derivations and research-level imported theorems. The fixed-prior Bayesian Holevo converse has an explicit specialist route; it is not presented as a result already taught in the textbook's binary-discrimination chapter.

## Keep the regimes distinct

Exchange class labels so that $`p\geq1/2`$. Write $`n`$ for the training copies per class, $`p`$ for the class0 test probability, $`q=1-p`$ for the minority probability, and $`s=p-q=|2p-1|`$ for the imbalance.

| Regime | Supported conclusion |
|---|---|
| Finite $`n\geq1`$, unequal interior prior | The optimal classical-record risk is strictly larger than the retained-quantum risk. |
| A fixed unequal interior prior, then $`n\to\infty`$ | The gap has order $`\Theta_s(1/n)`$, with a positive lower coefficient. Its exact leading coefficient is open. |
| Minority probability $`q\downarrow0`$ at a fixed fractional risk target | Classical training requires order $`1/q`$ copies per class; a constant number of consumed quantum references suffices through established comparison. |
| The same rarity limit with fixed $`t`$ copies of one query | The [several-copy law](../science/rare_class_query_copies.md) changes the classical order to $`q^{-1/t}`$ for its stated fractional targets. The retained budget stays constant. |

At the rare-class threshold equality, minority decisions may tie the majority risk. Finite-noise continuity does not establish a fixed-noise large-training theorem. The program can be consumed, and these advantages concern supplied quantum specimens rather than a generic classical-data speedup.

The shared material supplies scientific explanations and understanding targets. It contains no personal assessment history or learner-progress record.

