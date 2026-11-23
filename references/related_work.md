# Related work and attribution

The experiment supplies labeled copies of two unknown independent Haar pure qubits, then one test promised to equal one prototype. The deployment prior is known and need not match the balanced training composition. The comparison permits arbitrary collective training measurements and unlimited classical records; it asks whether retaining quantum examples can lower the later prediction error.

## The closest classical-sufficiency result

[Sentís, Calsamiglia, Muñoz-Tapia and Bagan (2012)](https://doi.org/10.1038/srep00708), *Quantum learning without quantum memory*, constructs a classical-record learner attaining the fully quantum programmable-discrimination optimum for every balanced pure-qubit training size at equal class priors. Its training measurement is collective and is more capable than separately estimating the prototypes. That balanced equality and its covariant attaining measurement are inherited here.

The [finite activation theorem](../science/activation.md) establishes the exact boundary under the same equal training counts: every unequal interior deployment prior gives a strict retained-quantum advantage, even when the classical learner knows that prior before choosing its training POVM. The [one-copy solution](../science/one_copy.md) optimizes the entire classical curve, while [plateau bounds](../science/plateau.md) quantify a neighborhood around balance.

Training-count imbalance and deployment-prior imbalance are different model changes. This work does not infer that any unequal training composition has the same boundary.

## Global programmable discrimination is an input

[He and Bergou (2007)](https://doi.org/10.1103/PhysRevA.75.032316), [quant-ph/0610226v3](https://arxiv.org/abs/quant-ph/0610226), solve multicopy programmable discrimination with arbitrary prior probabilities using Jordan bases. Earlier Haar identification and later generalizations also establish the symmetric-space reduction and binary global optimum.

The [quantum benchmark](../science/quantum_benchmark.md), its recoupling overlaps and biased Helstrom values are therefore credited foundations. The present contribution does not consist of a new global biased-discrimination formula. It concerns which of those decisions can be compiled into a classical training record and the statistical price of that restriction.

## Asymptotic quantum learning and estimation

[Guță and Kotłowski (2010)](https://doi.org/10.1088/1367-2630/12/12/123032), [arXiv:1004.2468](https://arxiv.org/abs/1004.2468), study learning the test Helstrom measurement from unknown qubits, with general class weights and a local asymptotic minimax criterion. Their Theorem 5.1 uses training allocation proportional to the class weights and optimizes a training-measurement-to-classical-estimator architecture. It distinguishes direct learning of the decision from plug-in state estimation. This is an important methodological antecedent, not a theorem comparing retained programs with optimal classical records in the present finite equal-budget Haar experiment.

[Gill and Guță (2013)](https://doi.org/10.1214/12-IMSCOLL909), [arXiv:1112.2078v3](https://arxiv.org/abs/1112.2078), Theorem 1, supplies the integrated Bayesian Holevo lower bound used in [the fixed-prior analysis](../science/asymptotic.md). Its positive-definite induced weight and finite prior-information assumptions are retained. The proof here repairs the rank-two directional target by an explicitly charged auxiliary estimation argument before taking ordered limits; it does not assume an unstated singular-weight extension.

The resulting fixed-prior comparison proves a positive lower coefficient and an upper bound of matching order. It does not determine the exact leading classical coefficient. Numerical finite SDP curves are supporting checks.

## Other matching and learning models

[Sasaki and Carlini (2002)](https://doi.org/10.1103/PhysRevA.66.022303), [quant-ph/0202173](https://arxiv.org/abs/quant-ph/0202173), compare fully quantum and semiclassical matching with unknown templates. Their solved setting uses equatorial qubit families and a fidelity-matching score for a general feature state. The promised-membership zero-one loss used here is different. Generic quantum-template learning and comparison with classical preprocessing are established ideas.

[Fanizza, Mari and Giovannetti (2019)](https://doi.org/10.1109/TIT.2019.2916646), [arXiv:1805.03477v3](https://arxiv.org/abs/1805.03477), derive universal learning machines with different information about prototype purities and overlaps. Their class probabilities are explicitly equal. Their use of the term “prior information” does not itself supply a result about deployment-class imbalance.

[Conlon et al. (2023)](https://doi.org/10.1038/s42005-023-01454-z), [arXiv:2302.08882](https://arxiv.org/abs/2302.08882), show that unequal priors can activate collective-measurement advantage for known mixed-qubit hypotheses. This is a direct conceptual precursor to bias activating quantum value. The present distinction lies in unknown learned prototypes and the training-to-test classical-memory cut; generic bias activation is not claimed as a new concept.

[Monras, Sentís and Wittek (2017)](https://doi.org/10.1103/PhysRevLett.118.190503), [arXiv:1605.07541](https://arxiv.org/abs/1605.07541), analyze inductive supervised quantum learning and many-test classicalization through a channel de Finetti result. The current task consumes a finite program for one prediction. It supplies no indefinitely reusable quantum-model advantage.

## Standard primitives and implementation

Pure-state covariant estimation and its fidelity $`(n+1)/(n+2)`$ are established estimation results, including [Massar and Popescu (1995)](https://doi.org/10.1103/PhysRevLett.74.1259). The nonsymmetric-subspace test in the [rare-class construction](../science/rare_class.md) is established universal state comparison, including [Barnett, Chefles and Jex](https://arxiv.org/abs/quant-ph/0202087). Its zero-false-positive pure-state property is inherited.

The new rare-class statement is the exact no-improvement threshold for *every* classical training record and the matching order of the samples required for fixed fractional error reduction. The attaining quantum comparison mechanism is credited rather than counted again as a new protocol.

The [several-copy extension](../science/rare_class_query_copies.md) uses the [weighted library threshold](https://github.com/GoGoKo699/Quantum-Reference-Identification/blob/d1b6e1583c5fba0dc757f3a75f0db622183315f8/science/prior_weighted_identification.md). The threshold draws on [Chiribella's symmetric posterior-channel identity](https://arxiv.org/abs/1010.1875) and the common-component method of [Anshu, Landau and Liu](https://arxiv.org/abs/2111.03273). The extension derives the classical rarity exponent from that threshold and an attainable covariant majority-reference procedure.

Schur compression follows [Bacon, Chuang and Harrow](https://arxiv.org/abs/quant-ph/0407082). A loose paid dense decision-circuit realization uses standard unitary synthesis, including [Shende, Bullock and Markov](https://arxiv.org/abs/quant-ph/0406176). These ingredients make the statistical access model concrete; they do not prove a hardware runtime advantage.

## Related supplied-state classification results

The following public accounts have adjacent models:

| Account | Relation and distinction |
|---|---|
| [Quantum Reference Identification](https://github.com/GoGoKo699/Quantum-Reference-Identification/tree/1212b747bf8c5dca54a9d210cd554536bc0f67ae) | Independent Haar libraries and the same delayed-query classicalization boundary; its central results concern uniform growing libraries and revealed-query saturation. |
| [Quantum Classification Rank Limits](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/tree/5974494ec900f2e5ed8193db18ef6c5633d4a48e) | Flat-rank unknown source versus known maximally mixed background; supplies credited classical-posterior/comparison machinery, with rank and dimension as the central resources. |
| [Quantum Training Contamination](https://github.com/GoGoKo699/Quantum-Training-Contamination/tree/c1b011f516a8b9d15b2674ed5d8d9bccc506f155) | Contaminated training for one clean pure target against a known mixed background. Its clean endpoint overlaps the rare-class comparison primitive used here. |
| [Quantum Learning Under Drift](https://github.com/GoGoKo699/Quantum-Learning-Under-Drift/tree/5abbebb11139e955488a62a8ba1c5b9d392f4f98) | Online hidden-state refresh; reconstructs the arbitrary-effect Haar posterior identity also used in the present threshold. |

These relationships do not identify the tasks or supply the all-prior boundary for two learned qubit prototypes. Shared posterior and state-comparison ingredients are credited once.

## Reading boundary

This is a targeted model-and-theorem comparison, not an exhaustive priority certificate. The full contribution retains independent Haar pure prototypes, equal training counts, known deployment prior and one test. Numerical checks, new terminology and a different presentation do not establish novelty by themselves. The authoritative mathematical claims and their proofs are the linked scientific pages.

