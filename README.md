# Quantum Learning Class Imbalance

**When does class prevalence make quantum training examples worth keeping?**

A source supplies equally many labeled copies of two unknown pure qubit states. One later test belongs to the first class with known probability $`p`$, and to the second with probability $`1-p`$. A learner may convert all training examples into an unrestricted classical record, or retain quantum examples until prediction.

For independent Haar prototypes and every finite training size $`n\geq1`$, the two optimal error probabilities satisfy

```math
R_{\rm C}(n,p)=R_{\rm Q}(n,p)
\quad\Longleftrightarrow\quad
p\in\{0,\tfrac12,1\}.
```

The balanced equality is the established memory-free learning result of Sentís et al. The contribution here is the exact boundary of that classical sufficiency under changed class weights, together with quantitative risk and sample laws. The classical competitor may optimize an arbitrary collective training measurement for the known prior.

## Make one prediction with retained specimens

1. Take equal numbers of labeled pure qubits from the two sources. The training count and deployment prior are known. Apply a Schur transform to each bank, keep its compressed symmetric spin register until the test arrives, and discard the remaining registers in their fixed states.
2. Use the count and prior to compute and diagonalize the [weighted average difference](science/quantum_benchmark.md#finite-training) classically. Compile the known eigenbasis change into rotations and entangling gates on the two compressed banks and the test qubit.
3. Apply the basis change and measure in the computational basis. Return the first class for a positive eigenvalue and the second class for a negative eigenvalue. Either label has the same Bayes risk at zero. Every outcome gives a prediction, and the operation can consume the banks and test.

The inherited programmable discriminator of He and Bergou gives the optimal average prediction error for the stated Haar source and known prior. The [implementation account](science/resources.md#coherent-compression-and-a-paid-realization) charges specimen preparation, coherent storage, classical preprocessing, gates, clean workspace and finite-precision error. The [three-qubit example](learning/TUTORIAL.md#a-complete-three-qubit-experiment) illustrates the separate singlet test used to expose the memory advantage.

## What is established

| Result | Meaning | Scientific account |
|---|---|---|
| Every interior imbalance activates retained-example value | Strict improvement over every classical training record, for every finite $`n\geq1`$ | [Activation proof](science/activation.md) |
| Fixed-prior statistical order | For every fixed $`0\lt\lvert2p-1\rvert\lt1`$, the optimal risk gap is $`\Theta_p(1/n)`$ | [Asymptotic bounds](science/asymptotic.md) |
| Exact smallest experiment | The complete one-copy classical curve has a plateau, an intermediate regime and a majority-only regime | [One-copy solution](science/one_copy.md) |
| Sharp rare-class threshold | If the minority probability is at most $`1/(n+2)`$, no classical record improves on majority guessing | [Threshold and sample cost](science/rare_class.md) |
| Explicit finite interval around balance | A provable classical plateau and quantitative inverse-polynomial gap | [Plateau theorem](science/plateau.md) |
| Finite noisy neighborhood | At $`n=1,p=0.6`$, one percent depolarization of every supplied copy still certifies a risk gap above $`0.0525`$ | [Noise bound](science/noise.md) |

The fixed-prior theorem gives a positive asymptotic lower coefficient and a finite upper bound of matching order. It does not determine the exact leading coefficient or a uniform crossover through balance. At the rare-class threshold itself, minority predictions may tie the majority risk; uniqueness requires strict inequality.

## Several copies of the future query

With a fixed number $`t`$ of copies of one future query, the [rare-class sample law](science/rare_class_query_copies.md) gives classical reference cost $`\Theta(q^{-1/t})`$ versus constant retained reference cost for the stated fixed fractional risk targets. [Quantum Reference Identification](https://github.com/GoGoKo699/Quantum-Reference-Identification/blob/d1b6e1583c5fba0dc757f3a75f0db622183315f8/science/prior_weighted_identification.md) proves the matching weighted-library threshold and extends strict quantum memory advantage to libraries with a unique most probable label.

## Read the science

Start with the [experiment and interfaces](science/model.md), then follow the [connected scientific route](science/README.md). The [classical optimization](science/classical_training.md) gives an exact finite SDP over all permitted training records. The [quantum benchmark](science/quantum_benchmark.md) fixes the inherited programmable-discrimination formulas.

The [interpretation](science/interpretation.md) explains the signed-sector mechanism and the distinct prevalence/training limits. The [resource account](science/resources.md) includes supplied copies, retained memory, coherent compression, known decision synthesis and consumption. [Related work](references/related_work.md) separates inherited ingredients from the contribution; [BibTeX](references/references.bib) records the sources. [llms.txt](llms.txt) maps questions to the authoritative pages.

## Learn the result

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the standard-layout author manuscript.

Start with the [worked three-qubit experiment](learning/TUTORIAL.md), use the [Watrous bridge](learning/WATROUS_BRIDGE.md) for verified textbook locations and notation, and follow the [30-milestone map](learning/MILESTONES.md) from foundations to the complete result. The map has 12 background milestones and 18 research milestones, with the asymptotic theorem distinguished from its open exact coefficient. The [learning overview](learning/README.md) connects these routes.

## Reproduce the finite checks

With Python 3.12 or later:

~~~bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
~~~

The [verification guide](verification/README.md) documents independent Haar quadrature, dense states, physical covariant POVMs, spin-block duals, posterior thresholds, noise continuity and asymptotic algebra checks. [Recorded results](verification/results.json) give the actual run and its limits. Finite calculations supplement the analytical proofs.

## Scope

The experiment uses native unknown quantum specimens, independent Haar pure prototypes, balanced training counts, a known deployment prior and one consumed prediction. Source preparation, coherent storage and implementation precision remain real costs. The result supplies neither a reusable quantum program nor a runtime advantage for ordinary classical datasets. Finite depolarization continuity does not establish a fixed-noise large-training theorem.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

