# Rare classes: an exact classical threshold and a sample-cost separation

## Model and threshold

Use the independent-Haar pure-qubit model in [class-prior activation](activation.md). The training set has $`n`$ labeled copies per class. Let the known minority test probability be $`q\in(0,1/2]`$, with majority probability $`p=1-q`$.

For every finite $`n\geq0`$,

```math
R_{\rm C}(n,p)=q
\quad\Longleftrightarrow\quad
q\leq\frac1{n+2}.
```

For $`n=0`$, both sides hold for every $`q\leq1/2`$. For $`n\geq1`$, the inequality is sharp: above the threshold some measured-training classifier strictly improves on always choosing the majority label.

At strict $`q\lt 1/(n+2)`$, the majority decision is forced at every training outcome of nonzero probability. At equality, the optimum risk is still $`q`$, but zero posterior eigenvalues allow some minority decisions that tie that risk. Thus the equality case does not imply zero minority recall.

Equivalently, if $`p/q\geq n+1`$, even an arbitrary collective training measurement followed by unlimited classical storage cannot improve the minimum total error over the majority-only rule.

## A posterior-purity bound valid for collective training

Let $`L_y`$ be a training POVM effect on the two symmetric program registers, and let $`\mathbf a_y,\mathbf c_y`$ denote the posterior Bloch vectors of the two unknown source states. With $`J_i`$ the spin-$`n/2`$ generators, the standard Haar moment identities are

```math
\int P_\psi^{\otimes n}\,{\rm d}\psi=\frac{I}{n+1},
\qquad
\int r_i(\psi)P_\psi^{\otimes n}\,{\rm d}\psi
=
\frac{2J_i}{(n+1)(n+2)}.
```

Consequently, for every nonzero-probability outcome,

```math
a_{y,i}
=
\frac2{n+2}
\frac{\mathrm{Tr}[L_y(J_{A,i}\otimes I_C)]}
{\mathrm{Tr}L_y},
\qquad
c_{y,i}
=
\frac2{n+2}
\frac{\mathrm{Tr}[L_y(I_A\otimes J_{C,i})]}
{\mathrm{Tr}L_y}.
```

The largest eigenvalue of a directional spin component is $`n/2`$, so

```math
|\mathbf a_y|,\ |\mathbf c_y|
\leq \frac n{n+2}.
```

This bound does not require product training effects. It applies to every joint effect on $`AC`$.

The two conditional test states are $`(I+\mathbf a_y\cdot\boldsymbol\sigma)/2`$ and $`(I+\mathbf c_y\cdot\boldsymbol\sigma)/2`$. Their weighted difference has eigenvalues

```math
\frac{p-q\pm|p\mathbf a_y-q\mathbf c_y|}{2}.
```

If $`p-q\geq n/(n+2)`$, both are nonnegative because

```math
|p\mathbf a_y-q\mathbf c_y|
\leq p|\mathbf a_y|+q|\mathbf c_y|
\leq\frac n{n+2}.
```

The conditional minimum error is therefore exactly $`q`$ for every outcome. The condition is precisely $`q\leq1/(n+2)`$. With strict inequality the weighted posterior is positive definite, forcing the majority decision; at equality it can have a zero eigenvalue.

## Sharpness of the threshold

Suppose $`n\geq1`$ and $`q\gt 1/(n+2)`$. Include the nonzero training effect

```math
L=e\,
|\uparrow\rangle\langle\uparrow|_A^{\otimes n}
\otimes
|\downarrow\rangle\langle\downarrow|_C^{\otimes n},
\qquad 0\lt e\leq1,
```

and its positive complement. On this outcome the two posterior Bloch vectors are opposite and have length $`n/(n+2)`$. Thus

```math
|p\mathbf a-q\mathbf c|=\frac n{n+2}\gt p-q.
```

The conditional Helstrom decision strictly improves on the majority rule. The event has positive probability $`e/(n+1)^2`$; use the majority rule on every other outcome. The overall risk is strictly below $`q`$.

This establishes the exact threshold for any strict improvement. It does not claim that the improvement just above threshold is a constant fraction of $`q`$.

## Constant fractional improvement costs order $`1/q`$ classical training copies

Fix a target fraction $`\eta\in(0,1/2)`$ and require

```math
R\leq(1-\eta)q.
```

Let $`n_{\rm C}(q,\eta)`$ be the least number of training copies per class sufficient for that target. The threshold gives the necessary condition

```math
n_{\rm C}(q,\eta)\gt \frac1q-2.
```

For a matching-order upper bound, ignore the minority training register. Perform the usual covariant pure-state estimation measurement on the $`n`$ majority copies. Its average fidelity is $`(n+1)/(n+2)`$. On the test, predict the minority label only when the projector orthogonal to the estimated majority state clicks. The majority false-positive probability is $`1/(n+2)`$, while the independent Haar minority clicks with probability $`1/2`$. Hence

```math
R\leq\frac{p}{n+2}+\frac q2.
```

It suffices that

```math
n+2\geq\frac{p}{(1/2-\eta)q}.
```

Combining the bounds gives

```math
n_{\rm C}(q,\eta)=\Theta_\eta(q^{-1})
\qquad(q\downarrow0).
```

The lower bound covers arbitrary collective training measurements, not only this state-estimation construction.

## A retained reference avoids the rarity-dependent cost

Keep $`n`$ majority reference qubits until the test arrives and project their joint state with the test onto the nonsymmetric subspace. Predict minority only on that outcome. Under a majority test all $`n+1`$ states are identical, so there is no false positive. Under an independent Haar minority test, the symmetric outcome has probability

```math
\frac12\left(1+\frac1{n+1}\right)
=
\frac{n+2}{2(n+1)}.
```

The resulting risk is exactly

```math
R_{\rm comparison}
=
q\,\frac{n+2}{2(n+1)}.
```

Thus any fixed $`\eta\lt 1/2`$ is reached with

```math
n\geq\frac{2\eta}{1-2\eta},
```

rounded up to an integer. This number is independent of $`q`$. In particular, one retained majority qubit and a singlet test give $`R=3q/4`$ for every prior.

The attaining mechanism is the established universal comparison of unknown pure states. It is not a new comparison protocol. The contribution of the resource comparison is the optimal measured-training rarity dependence, with arbitrary collective training processing allowed, and its relation to the exact classical-sufficiency boundary.

## Resources and scope

The formal training budget is copies per labeled class; the full supplied balanced training set contains $`2n`$ specimens. The upper protocols may ignore the minority references, and the coherent comparison needs only majority references. Test frequency $`q`$ and training composition are distinct assumptions.

These are supplied-state sample costs. Source preparation, storing a quantum reference until test arrival, controlled gates, collective measurements, classical precision and physical noise are additional resources. The constant-size quantum procedure consumes its reference in one classification. It does not supply a reusable classifier, free replay, a generic classical-data speedup or a hardware crossover.

The separation concerns a relative improvement over the majority risk $`q`$. Its absolute error advantage vanishes as $`q\downarrow0`$; class rarity cannot be hidden by reporting only a relative ratio. The two source states are independent Haar pure qubits, and the test is promised to equal one of them. Mixed sources or a worst-case guarantee over arbitrary source pairs are different tasks.

