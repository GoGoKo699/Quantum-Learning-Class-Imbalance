# The prediction experiment

A learner receives quantum examples before it knows the individual specimen it must classify. It can measure the training set and retain a classical description, or preserve quantum examples until prediction. This account asks when the two interfaces have the same optimal error as class prevalence changes.

## Inputs, chronology and risk

Draw two independent unknown pure qubit states from normalized Haar measure once. Write their rank-one density matrices as $`P_0`$ and $`P_1`$. Supply exactly $`n`$ labeled copies of each:

```math
A=P_0^{\otimes n},\qquad C=P_1^{\otimes n}.
```

After training has ended, supply one test qubit $`B`$. It equals $`P_0`$ with known probability $`p`$ and $`P_1`$ with probability $`q=1-p`$. Conditional on the prototypes and label, the supplied specimens are independent products. The output is one classical label, with ordinary zero-one loss.

The training composition is fixed at $`n,n`$ independently of deployment prevalence. This corresponds to a deliberately balanced training library followed by an imbalanced deployment stream. The prevalence is known before training; both learners may optimize their training operations for it. This is not an unknown-prior estimation penalty.

Let $`R_{\rm C}(n,p)`$ and $`R_{\rm Q}(n,p)`$ be the infimum error probabilities averaged over the prototypes, test label and measurement outcomes.

| Interface | Permitted processing |
|---|---|
| Classical record after training | Any collective POVM on all training copies and independent ancillas; unlimited classical outcome, computation and storage; any later test POVM controlled by that outcome. All quantum information correlated with training must be discarded before the test arrives. |
| Retained quantum training | Any processing of the supplied training registers, followed by a joint decision with the test and independent ancillas. The program may be consumed. |
| Known-prototype benchmark | Exact classical descriptions of both prototypes supplied separately; the test is measured with their Helstrom decision. This is an information benchmark with stronger inputs. |

The classical interface includes adaptive processing within training. It is substantially more general than estimating the two states independently. The retained interface includes the classical one.

No state description, purification, preparation inverse, controlled unknown preparation, extra post-test examples or QRAM is supplied. The [resource account](resources.md) charges specimens, storage, known processing and output separately.

## Notation and endpoint conventions

Exchange labels when necessary and set

```math
s=|2p-1|,\qquad
D_{\rm C}=1-2R_{\rm C},\qquad
D_{\rm Q}=1-2R_{\rm Q}.
```

A risk written as a function of $`s`$ uses this label symmetry; a risk written as a function of $`p`$ uses the original class prior. They refer to the same experiment. The minority probability is $`\min(p,q)`$.

The main strictness theorem concerns every finite integer $`n\geq1`$ and $`0<p<1`$. At $`p=0,1`$, the label is known and risk is zero. At $`n=0`$, both averaged test states equal $`I/2`$, so both interfaces have risk $`\min(p,q)`$ for every prior. At $`p=1/2`$, exact equality for pure qubits is the established result of Sentís et al.

All risks are Bayesian for this fixed Haar source model. They are not worst-case risks for every pair of prototypes: identical prototypes cannot be classified at the same contrast as orthogonal ones.

## What the result changes

The [activation theorem](activation.md) proves that balance is the only nontrivial prior at which classical training can attain the retained optimum for finite $`n`$. The [one-copy calculation](one_copy.md) solves the entire classical curve in the smallest experiment. The [plateau theorem](plateau.md) and [fixed-prior analysis](asymptotic.md) quantify two different limits. The [rare-class law](rare_class.md) quantifies samples needed for a fixed fractional reduction of the small minority risk.

The single-test and consumption conventions matter. These results do not establish an indefinitely reusable quantum model. Many-test inductive learning has separate classicalization results; see the [comparison with earlier work](../references/related_work.md).

