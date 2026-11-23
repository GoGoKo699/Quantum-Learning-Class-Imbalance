# When class imbalance makes quantum training memory useful

A balanced library of quantum training examples can be sufficient as a classical record for one deployment prior and insufficient for another. The change concerns the optimal prediction error, even when the prior is known and the classical learner can perform arbitrary collective quantum processing during training.

The [thirty-milestone map](MILESTONES.md) gives the complete understanding route. We begin with a fully specified three-qubit example, then connect its mechanism to the general result. The one educational anchor is Watrous, *The Theory of Quantum Information* (2018), standard-layout author manuscript; the [bridge](WATROUS_BRIDGE.md) identifies its relevant sections and separates textbook foundations from the research ingredients supplied here.

## A complete three-qubit experiment

**Milestone connections:** M01–M05 and M12; a preview of M13, M17, M24 and M25.

Two sources produce pure qubit states. Call their density operators $`P_0`$ and $`P_1`$. A density operator specifies measurement probabilities; a pure-state density operator is a rank-one projector. The two source directions are unknown and independently uniform over the Bloch sphere. This uniform source assumption is the Haar prior.

The learner first receives two labeled training specimens: qubit $`A`$ in state $`P_0`$ and qubit $`C`$ in state $`P_1`$. Later it receives one test qubit $`B`$. The test comes from class 0 with known probability

```math
p=\frac34,
\qquad q=1-p=\frac14.
```

The output is one class label. Risk means the probability of the wrong label, averaged over the source states, test label and measurement outcomes. The training library has one specimen from each class even though deployment is imbalanced.

Compare two interfaces. The first may measure $`A,C`$ jointly in any way, retain an unlimited classical record, discard every training-correlated quantum system, and use its record to choose a later measurement of $`B`$. The second may preserve quantum training specimens until $`B`$ arrives. Both know the prior before training, and both receive exactly the same native quantum inputs. Neither receives source amplitudes, a preparation inverse, or extra copies.

### Why every classical record has error one quarter

A qubit state can be written

```math
\rho=\frac{I+\mathbf r\cdot\boldsymbol\sigma}{2}.
```

Here $`I`$ is the identity, $`\boldsymbol\sigma`$ is the triple of Pauli matrices, and the real Bloch vector $`\mathbf r`$ has length at most one. Length one describes a pure state; a shorter vector describes less directional information.

Condition on any nonzero outcome of any joint training measurement. Averaging the unknown prototypes given that outcome produces two possible test states with Bloch vectors $`\mathbf r_0,\mathbf r_1`$. With one example per class,

```math
|\mathbf r_0|,|\mathbf r_1|\leq\frac13.
```

This posterior bound covers collective training measurements, not only separate estimates of the sources.

For two candidate states, the optimal binary decision is determined by the eigenvalue signs of their weighted difference. In this example it is

```math
p\rho_0-q\rho_1
=\frac{(p-q)I+(p\mathbf r_0-q\mathbf r_1)\cdot\boldsymbol\sigma}{2}.
```

Its eigenvalues are $`[(p-q)\pm|p\mathbf r_0-q\mathbf r_1|]/2`$. The scalar term is $`p-q=1/2`$, while the vector length is at most $`p/3+q/3=1/3`$. Both eigenvalues are therefore strictly positive. After every training outcome, the optimal test decision is simply class 0.

Consequently the exact optimal classical-record risk is

```math
R_C=\frac14.
```

The record may contain information about both prototypes. That information is insufficient to justify a minority prediction at these decision weights.

### One retained reference already improves the risk

Keep $`A`$ quantum and discard $`C`$. When $`B`$ arrives, measure whether the pair $`A,B`$ occupies the singlet, the antisymmetric two-qubit subspace. Predict class 1 only when the singlet outcome occurs.

A majority test has exactly the same pure state as its reference, so the pair is symmetric and the singlet never clicks. For a minority test, the singlet probability is

```math
\frac{1-|\langle\psi_0|\psi_1\rangle|^2}{2},
```

where $`|\psi_i\rangle`$ is a unit vector representing $`P_i`$. Independent Haar qubits have mean squared overlap one half, so the average minority click probability is one quarter. Thus there are no majority false positives, and three quarters of minority tests are missed:

```math
R_{\rm comparison}=q\frac34=\frac3{16}=0.1875.
```

Universal comparison of unknown pure states is an established primitive. The new classical-interface boundary shows why no amount of classical training processing on the same supplied library reaches this risk.

Keeping both references and using the inherited optimal programmable discriminator improves slightly further:

```math
R_Q=\frac13-\frac{\sqrt{13}}{24}\approx0.183102.
```

One prediction can consume the retained reference and test. This experiment promises one label, not a returned, indefinitely reusable quantum model.

**Sources:** [model](../science/model.md), [posterior threshold](../science/rare_class.md), [retained benchmark](../science/quantum_benchmark.md), and [comparison attribution](../references/related_work.md).

## The mathematical language behind the example

**Milestone connections:** M06–M11, completing the background synthesis in M12.

Conditioned on a prototype, its supplied copies form a tensor product. Averaging their common unknown prototype jointly produces correlations. This is why the averaged learning hypotheses are not obtained by replacing every specimen independently by $`I/2`$.

Repeated copies of a pure qubit occupy a known symmetric subspace. For $`n`$ copies it has dimension $`n+1`$, even though the individual pure state remains unknown. Haar integration converts the joint source ensemble into known symmetric-space operators. Common rotations also leave the source distribution unchanged, so averaging a proposed strategy or bound over rotations preserves its performance. Spin and magnetic-sector labels organize this symmetry into manageable blocks; the required coefficients are derived in the project.

Two further distinctions support the converse. First, a measured-training effect followed by a conditional test effect is separable across the training/test cut. Such effects are positive under partial transpose, abbreviated PPT. Partial transpose exchanges the test row and column indices of an operator. A globally optimal effect that fails this necessary positivity condition cannot arise from any classical record. PPT is used as a relaxation; it is not asserted to characterize all classical-record protocols.

Second, an optimization needs both a bound and an attaining strategy. A semidefinite-program dual operator can bound every permitted training measurement. A matching physical POVM proves that the bound is exact. Numerical solver output alone does not provide that certificate.

The later asymptotic argument uses another statistical idea: small uncertainty in a test axis becomes a quadratic excess error, while incompatible parameter directions impose a multiparameter estimation cost. This Holevo estimation bound is different from the Holevo–Helstrom theorem for binary discrimination. Watrous supplies the operator, measurement, discrimination, separability and optimization foundations. The spin calculations and the advanced statistical application are supplied locally with their primary research attribution.

**Sources:** [Watrous bridge](WATROUS_BRIDGE.md), [classical optimization](../science/classical_training.md), and [asymptotic statistical input](../science/asymptotic.md#the-statistical-input).

## Balance is an isolated point of classical sufficiency

**Milestone connections:** M13–M15.

Now supply $`n`$ labeled copies of each unknown prototype. The prior remains known before training. Define the absolute imbalance and discrimination biases by

```math
s=|2p-1|,
\qquad D_C=1-2R_C,
\qquad D_Q=1-2R_Q.
```

A larger bias means a smaller error. At balance, $`s=0`$, Sentís and collaborators established that a suitable classical training record attains the global one-test quantum optimum for every finite $`n`$.

The general finite theorem identifies exactly where that equality survives:

```math
R_C(n,p)=R_Q(n,p)
\quad\Longleftrightarrow\quad
p\in\{0,\tfrac12,1\},
\qquad n\geq1\text{ finite}.
```

The endpoints have a known label and zero error. Every unequal interior prior gives a strict advantage for retained training.

The mechanism is visible in a very small sector of the averaged problem. At balance, the globally symmetric sector has zero weighted difference between the two hypotheses. An optimal decision has freedom there. A prior tilt gives that sector a definite sign and forces the optimal minority effect to annihilate its all-up vector.

In the one-excitation sector, however, the same optimal effect has a nonzero transition entry connecting a test excitation with a training excitation. Partial transpose moves that entry beside the forced zero diagonal. A positive semidefinite matrix cannot have a nonzero entry in a row whose diagonal is zero. The optimal minority effect is therefore not PPT.

This three-dimensional obstruction works for every finite training size and every nonzero interior imbalance. Its force comes from covering the entire classical interface, including unlimited records obtained by collective quantum training.

**Sources:** [activation proof](../science/activation.md), [balanced construction](../science/classical_training.md#an-optimal-balanced-dual-and-an-attaining-measurement), and [interpretation](../science/interpretation.md).

## The complete small curve and the general plateau

**Milestone connections:** M16–M19.

The exact one-copy calculation explains how much performance changes. Refining a training POVM to pure two-qubit effects cannot hurt. Each pure effect has a singlet fraction, call it $`u`$. POVM completeness fixes the average singlet fraction to one quarter. At fixed $`u`$, optimizing the posterior test decision reduces the problem to a scalar function; optimizing its average is a concave-envelope construction.

The resulting exact classical bias is

```math
D_C(1,s)=
\begin{cases}
\sqrt3/6,&0\leq s\leq1/(3\sqrt3),\\[3pt]
3s/4+1/(36s),&1/(3\sqrt3)\leq s\leq1/3,\\[3pt]
s,&1/3\leq s\leq1.
\end{cases}
```

The three regimes are an unchanged optimal risk near balance, a curved intermediate response, and the majority-guessing risk. Covariant seed measurements attain all branches; a finite construction needs at most 48 training outcomes. The global benchmark is

```math
D_Q(1,s)=\frac{2s}{3}+\frac{\sqrt{3+s^2}}6.
```

The quantum bias has a linear cusp at balance while the classical optimum remains flat. At $`p=3/5`$, the exact absolute risk gap is

```math
\gamma=R_C-R_Q
=\frac{3\sqrt{19}-7}{90}\approx0.067519.
```

General training sizes admit an exact finite classical SDP. Its variables describe operator bounds on every possible posterior action. An explicit balanced dual is a weighted graph-Laplacian certificate, and an explicit covariant seed attains it. That same certificate remains feasible on a provable nonzero interval $`0\leq s\leq s_0(n)`$. Thus the classical optimum is exactly unchanged there, while

```math
R_C(n,s)-R_Q(n,s)\geq\frac{s}{n+2}.
```

The project gives explicit constants for $`s_0(n)`$. It is a sufficient plateau, not a claim to have found the largest one.

**Sources:** [one-copy derivation and attainment](../science/one_copy.md), [general classical SDP](../science/classical_training.md), and [plateau theorem](../science/plateau.md).

## A first-order penalty at a fixed imbalanced prior

**Milestone connections:** M20–M23.

A different question fixes $`0\lt s\lt 1`$ and then increases $`n`$. The known-prototype oracle receives exact descriptions of both sources, a stronger input than either learner. Subtracting its error separates irreducible test ambiguity from the cost of learning the decision.

Locally, let $`\mathbf r_0,\mathbf r_1`$ be the unit source Bloch directions and put

```math
\mathbf d=p\mathbf r_0-q\mathbf r_1,
\qquad D=|\mathbf d|,
\qquad \mathbf e=\mathbf d/D.
```

If a learned projective test uses axis $`\widehat{\mathbf e}`$, its exact excess over the known-source error is $`D|\widehat{\mathbf e}-\mathbf e|^2/4`$. The converse reduces arbitrary final qubit actions, including constant guesses, to this directional estimation task on suitable local patches.

Both unknown prototypes still contribute their tangent parameters. The response-observable calculation includes an imaginary covariance term expressing incompatibility. Applying the Bayesian Holevo information bound then requires genuine positive weights and regularity. The proof supplies a small nuisance weight, smooth compact priors, and explicitly counted additional data, removing those auxiliary quantities in a stated order. They are not free examples in the prediction model.

After integration and comparison with the exact coherent benchmark,

```math
\liminf_{n\to\infty}n(R_C-R_Q)\geq A(s)\gt 0,
\qquad
R_C-R_Q\leq\frac{I(s)}{n+2},
```

where

```math
I(s)=\frac{2(1+s+s^2)}{3(1+s)},
\qquad
A(s)=\frac{s}{4}
\left(3+\frac{2\log(1/s)}{1-s^2}\right).
```

Hence the penalty has order $`1/n`$ at each fixed interior imbalanced prior. The constants may depend on that prior. The function $`A(s)`$ is a lower coefficient, not the exact leading coefficient of the optimal classical penalty; that exact coefficient remains open. This limit is not uniform through balance or the trivial prior endpoints.

**Sources:** [fixed-prior benchmark expansion](../science/quantum_benchmark.md#oracle-error-and-fixed-prior-expansion) and [full asymptotic proof with statistical attribution](../science/asymptotic.md).

## Rarity changes the sample question

**Milestone connections:** M24–M25.

Suppose class 1 is the minority, with probability $`q\leq1/2`$. For general $`n`$, every conditional classical-record posterior Bloch vector has length at most $`n/(n+2)`$. This yields the sharp threshold

```math
R_C(n,p)=q
\quad\Longleftrightarrow\quad
q\leq\frac1{n+2}.
```

Below the threshold the majority decision is unique. At equality a posterior weighted difference can have a zero eigenvalue, permitting minority predictions that tie the same total error through balancing false positives. Equality of risks does not imply uniqueness of the decision.

For a fixed fraction $`0\lt \beta\lt 1/2`$, ask for $`R\leq(1-\beta)q`$ as $`q`$ decreases. The threshold lower bound and an attaining-order classical strategy give a necessary and sufficient order of $`1/q`$ training copies per class. In contrast, the established coherent comparison test with $`n`$ retained majority references has risk

```math
R_{\rm comparison}=q\frac{n+2}{2(n+1)}.
```

A constant number depending on $`\beta`$ therefore reaches that fractional target independently of rarity. The reference is consumed, and the absolute error contrast still vanishes with $`q`$. Observing rare labeled events empirically may itself require order $`1/q`$ deployment trials per minority observation.

If the same query arrives as two qubits, the classical threshold becomes $`p/q\geq\binom{m+2}{2}`$, where $`m`$ is the training count per class. For $`q=1/100`$, reducing majority risk by 25% needs at least 13 measured references per class. A concrete covariant estimator with 47 reaches the target. The symmetry test with one retained majority reference gives risk $`2q/3`$ and already reaches it. With a fixed $`t`$, the same argument gives classical order $`q^{-1/t}`$ for the fractional targets specified in the extension.

**Sources:** [rare-class theorem and sample costs](../science/rare_class.md), [several-copy example and proof](../science/rare_class_query_copies.md#worked-example-with-two-query-qubits), [evaluation costs](../science/resources.md#rarity-and-the-cost-of-a-claimed-saving), and [universal-comparison attribution](../references/related_work.md).

## Finite noise and paid implementation

**Milestone connections:** M26–M27.

Let every supplied copy independently undergo known depolarization, replacing $`P_i`$ by $`(1-\lambda)P_i+\lambda I/2`$. The parameter $`\lambda`$ is the noise strength. For $`2n+1`$ supplied copies, their averaged hypothesis states change by trace distance at most

```math
\delta_n(\lambda)=1-(1-\lambda/2)^{2n+1}
\leq\frac{(2n+1)\lambda}{2}.
```

Both learner classes can simulate this known noise, so noise cannot improve their optimal errors. Combining that monotonicity with continuity certifies that a pure-model gap $`\gamma`$ remains at least $`\gamma-\delta_n(\lambda)`$. For the $`n=1,p=3/5`$ example, one percent depolarization on all three specimens still certifies an absolute gap above $`0.0525`$.

This is a finite noisy neighborhood. Full-rank noise removes the exact support argument behind zero false positives, and no fixed-noise large-training advantage or optimal noisy classifier is established.

The statistical optimum also has implementation costs. The symmetric support permits compression of both programs into at most $`2\lceil\log_2(n+1)\rceil`$ persistent logical qubits through known Schur processing. This is a storage upper bound, not a minimum-memory theorem. All original specimens must still be handled, and the training-to-test delay needs coherent storage. Precomputing and synthesizing the known sign measurement, classical tables, ancillas and gate precision are paid operations. A total channel implementation error must be smaller than the risk gap one intends to resolve.

**Sources:** [finite-noise guarantee](../science/noise.md) and [complete resource account](../science/resources.md).

## The single scientific story

**Milestone connections:** M28–M30.

The arbitrary-prior quantum discriminator, balanced memory-free classifier, universal state comparison and Bayesian information-bound tools are credited foundations. The project establishes the prior-dependent boundary of classical training sufficiency, solves the smallest classical curve, and quantifies the penalty in finite, fixed-prior and rare-class regimes.

These regimes answer different questions. Exact finite strictness does not give a uniform gap; the fixed-prior order law does not determine its exact coefficient; a rarity-independent number of retained references does not give constant absolute contrast or inexpensive empirical validation. With no training, both averaged hypotheses are identical, and neither interface improves on the majority risk. A known label at $`p=0`$ or $`p=1`$ is trivial.

The physical consequence is precise: keeping the training library balanced does not make its best classical summary sufficient for every known deployment weighting. At balance a zero decision sector permits exact sufficiency. Any interior tilt removes that freedom, and retained quantum specimens can then support a decision unavailable to every classical record. The size and cost of that benefit must be read in the appropriate quantitative regime, with one-test consumption and supplied-state resources kept explicit.

**Sources:** [interpretation](../science/interpretation.md), [related work](../references/related_work.md), [model and endpoints](../science/model.md), and [milestone map](MILESTONES.md).
