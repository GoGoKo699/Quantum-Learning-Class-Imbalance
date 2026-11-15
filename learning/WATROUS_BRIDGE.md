# Watrous bridge: from quantum decisions to class imbalance

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the **standard-layout author manuscript** linked from the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). The relevant chapter files and numbered statements were checked on 15 November 2026. Page numbers below are the manuscript's printed pages, rather than a PDF viewer's page index.

The [worked tutorial](TUTORIAL.md) begins with the physical experiment. Use this bridge for the specific textbook facts behind each step, then use the [30-milestone map](MILESTONES.md) to follow the complete project. Reading the whole book is unnecessary.

## Verified textbook route

| Project need | Verified location in the selected manuscript | What it supplies |
|---|---|---|
| States, copies and reductions; M01–M02 | §§2.1.2–2.1.3, pp.61–72 | Density operators, tensor-product specimens and partial traces. Removing a register does not provide its unknown state description. |
| Measurements and classical records; M03 | §§2.3.1–2.3.2, pp.100–113 | A POVM describes arbitrary collective training. Its outcome may control the later test measurement. |
| Biased decisions and error; M04–M05 | §3.1.1, *Discriminating between pairs of quantum states*, pp.125–132; Theorem3.4 pp.128–129 | The weighted state difference and its trace norm determine binary success; its sign gives a projective optimum. |
| Pure copies and averaging; M06 | §7.1.1, pp.391–400: Proposition7.1 p.392 and Corollary7.3 p.395. Then §7.2.1, pp.408–420: Lemma7.24 pp.416–417 | Symmetric support has dimension $`n+1`$ for $`n`$ qubits. Its normalized projector is the Haar pure-state moment. |
| The training/test cut; M07 | §6.1.1, p.310 onward, especially Definition6.1 p.311; §6.1.3, p.332 onward, especially Proposition6.28 p.333 | Separability applies to measurement effects. All training registers form one side and the future test forms the other. |
| A necessary constraint on effects; M07 | The partial-transpose discussion in §6.2.3, pp.352–353; Definition6.39 p.353 | Separable positive operators are PPT. PPT is not a sufficient test for separability in general. |
| Certifying the classical optimum; M08 | §1.2.3, *Semidefinite programming*, pp.53–57 | Primal measurements give attainable values; feasible duals bound every allowed measurement. |
| Channels and implementation errors; M26–M27 | §2.2.1, p.72 onward; for reference-stable channel errors, §3.3.2, pp.166–175 | Known depolarization is allowed preprocessing. The completely bounded trace norm supports the separate implementation-error budget. |

For an unfamiliar matrix operation, §§1.1.2–1.1.3, pp.8–35, give the operator and norm definitions used by these stops. Bloch-vector coordinates and the coupled-spin calculations are explained locally.

## Notation and conventions

Watrous uses vector/operator notation rather than Dirac notation.

| Textbook notation or convention | Translation here |
|---|---|
| A unit column vector $`u`$ and $`uu^*`$ | $`|\psi\rangle`$ and $`P_\psi=|\psi\rangle\langle\psi|`$. The star denotes conjugate transpose. |
| $`\mathrm D(\mathcal X)`$ and $`\operatorname{Pos}(\mathcal X)`$ | Density operators and positive semidefinite operators. A POVM effect need not have trace one. |
| A measurement $`\mu(a)`$ | $`L_y`$ for training, then $`D_{i|y}`$ for the test. |
| The prior $`\lambda`$ in Theorem3.4 | $`p`$ for class0 and $`q=1-p`$ for class1. The prior is known before training and is separate from the fixed training counts. |
| Generic known hypotheses $`\rho_0,\rho_1`$ | The Haar-averaged program-plus-test operators $`\sigma_0,\sigma_1`$. The particular unknown prototypes remain $`P_0,P_1`$. |
| $`\langle A,B\rangle=\operatorname{Tr}(A^*B)`$ | For a Hermitian effect and state, the Born probability is $`\operatorname{Tr}(E\rho)`$. |
| Raw trace norm $`\|X\|_1`$ | Classification bias uses this norm directly. The state trace distance in the noise bound includes a factor $`1/2`$. |
| Partial transpose of one factor | $`T_B`$ transposes the test across $`AC:B`$. Transposing the other factor gives the equivalent PPT criterion. |

The textbook theorem gives success; the project reports error:

```math
P_{\rm success}=\frac{1+\|p\sigma_0-q\sigma_1\|_1}{2},
\qquad
R_{\rm Q}=\frac{1-\|p\sigma_0-q\sigma_1\|_1}{2}.
```

The symbols $`D_{\rm C},D_{\rm Q}`$ are scalar biases. In the asymptotic proof $`D=|p\mathbf r_0-q\mathbf r_1|`$ is the known-prototype decision length. Neither is the textbook state set $`\mathrm D(\mathcal X)`$.

## Steps supplied by this project

**Average the unknown source without supplying its description.** Risk is linear in the density operator. Lemma7.24 gives

```math
\int P_\psi^{\otimes n}\,d\psi=\frac{P_{\rm sym}^{(n)}}{n+1}.
```

Applying this identity to the two possible program-plus-test inputs yields

```math
\sigma_0=\frac{P_{\rm sym}^{AB}\otimes I_C}{(n+1)(n+2)},
\qquad
\sigma_1=\frac{I_A\otimes P_{\rm sym}^{BC}}{(n+1)(n+2)}.
```

The identities act on the symmetric training spaces. These matrices depend only on the source model and $`n`$, so a known measurement can use them. No description of the particular drawn prototypes has been provided. See [the model](../science/model.md) and [quantum benchmark](../science/quantum_benchmark.md).

**Translate chronology into a constraint on an effect.** Exchange labels so that $`p\geq q`$. Training measured before the test arrives gives

```math
E_1=\int L_y^{AC}\otimes D_{1|y}^{B}\,dy.
```

This minority-label effect is separable across $`AC:B`$, hence PPT. The classical learner can still process $`A`$ and $`C`$ jointly using a quantum computer. The [activation proof](../science/activation.md) supplies the extra three-dimensional calculation showing that every quantum-optimal minority effect is non-PPT at an unequal interior prior. The relevant non-PPT object is a measurement effect, not a claim that each supplied specimen is entangled.

**Join an attainable method to a bound on every method.** The [one-copy proof](../science/one_copy.md) reduces training effects to a singlet-fraction moment problem, solves its concave envelope and constructs a finite attaining POVM. The [classical optimization](../science/classical_training.md) derives the exact SDP; the [plateau proof](../science/plateau.md) supplies its explicit dual certificate. The singlet optimization, spin coefficients and graph comparison are local derivations, rather than results already contained in the textbook's SDP section.

| Remaining connection | Authoritative account |
|---|---|
| Finite-training equality boundary and endpoint cases | [Activation](../science/activation.md) |
| The full one-copy curve and physical attainment | [One-copy solution](../science/one_copy.md) |
| A positive general-$`n`$ plateau around balance | [Classical optimization](../science/classical_training.md), [plateau](../science/plateau.md) |
| Posterior-purity threshold and the rare-class limit | [Rare classes](../science/rare_class.md) |
| Leading penalty at a fixed unequal prior | [Fixed-prior analysis](../science/asymptotic.md) |
| Finite noise and paid logical implementation | [Noise](../science/noise.md), [resources](../science/resources.md) |
| Inherited benchmark, tools and primitives | [Related work](../references/related_work.md) |

## The fixed-prior converse is a research-level dependency

The Holevo–Helstrom theorem in §3.1.1 solves binary discrimination. The Holevo bound used in the fixed-prior converse is a multiparameter estimation bound. They are different statements.

The [asymptotic proof](../science/asymptotic.md) supplies the pure-pair coordinates, exact decision-to-direction loss and positive-weight augmentation needed for the Bayesian theorem of Gill and Guță. That primary theorem is a scientific proof dependency; it is not a second educational anchor or a theorem attributed to Watrous.

M10–M11 introduce estimating a decision axis and paying for incompatible tangent information. M20–M23 return to the full proof, retaining compact parameter patches, a smooth covariance field, additional counted data, ordered limits and Haar-prior reassembly. Write $`s=|2p-1|`$; $`I(s)`$ is the mean known-prototype Helstrom bias and $`A(s)`$ is the positive lower coefficient defined in that proof. The conclusion is

```math
\liminf_{n\to\infty}n(R_{\rm C}-R_{\rm Q})\geq A(s)>0,
\qquad
R_{\rm C}-R_{\rm Q}\leq\frac{I(s)}{n+2},
\quad\text{for each fixed }0<s<1.
```

It proves the order $`\Theta_s(1/n)`$. The exact leading coefficient and a uniform crossover as $`s`$ changes with $`n`$ remain open.

## Where the route ends

The [milestone map](MILESTONES.md) joins the ingredients into one account. Its final synthesis retains independent Haar pure qubits, equal supplied training counts, a known deployment prior and one consumed prediction. The [interpretation](../science/interpretation.md) compares the finite-training, fixed-prior and rare-class limits. The [verification guide](../verification/README.md) identifies what the finite calculations check.

The manuscript is linked through its author's page for reading. No textbook copy is included or redistributed with this repository.

