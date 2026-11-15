# Class-prior imbalance activates quantum training memory

## Statement and model

Let $`n\geq 1`$ be finite. Draw two independent Haar-distributed pure qubit states $`P_\psi`$ and $`P_\phi`$ once, and supply the labeled training registers $`A=P_\psi^{\otimes n}`$ and $`C=P_\phi^{\otimes n}`$. A later, independent test register $`B`$ contains $`P_\psi`$ with known probability $`p`$ and $`P_\phi`$ with probability $`q=1-p`$.

A classical training procedure may perform any collective POVM on $`AC`$, retain its entire classical outcome, and choose any subsequent test POVM from that outcome. A quantum procedure may retain the training registers until the test arrives and measure all registers together. Write their minimum Haar-average single-test error probabilities as $`R_{\rm C}(n,p)`$ and $`R_{\rm Q}(n,p)`$.

For every finite $`n\geq1`$,

```math
R_{\rm C}(n,p)=R_{\rm Q}(n,p)
\quad\Longleftrightarrow\quad
p\in\{0,\tfrac12,1\}.
```

In particular, every nonzero interior class imbalance makes the quantum optimum inaccessible to every classical training record. The statement is an exact finite-sample distinction. It does not assert a gap uniform in $`n`$ or $`p`$, an advantage for ordinary classical input data, or a reusable quantum program.

The equal-prior equality is the result of [Sentís et al. (2012)](https://doi.org/10.1038/srep00708). The proof below establishes the unequal-prior inequality. Global programmable-discrimination spectra, including arbitrary priors, are earlier work; see [He and Bergou (2007)](https://doi.org/10.1103/PhysRevA.75.032316).

## Averaged hypotheses and the classical restriction

Work on the supplied program support

```math
\mathcal H
=
\operatorname{Sym}^{n}(\mathbb C^2)_A
\otimes\mathbb C^2_B
\otimes\operatorname{Sym}^{n}(\mathbb C^2)_C.
```

Let $`P_k`$ denote the projector onto the symmetric subspace of $`k`$ qubits, and set $`\kappa_n=1/[(n+1)(n+2)]`$. Haar integration gives the normalized hypothesis states

```math
\sigma_0=\kappa_n P_{n+1}^{AB}\otimes I_C,
\qquad
\sigma_1=\kappa_n I_A\otimes P_{n+1}^{BC}.
```

The identities are on the already symmetric training supports. Put $`\Delta=p\sigma_0-q\sigma_1`$. If $`E`$ is the effect for outputting label $`1`$, its error probability is

```math
R(E)=q+\operatorname{Tr}(E\Delta),
\qquad 0\leq E\leq I.
```

A measured-training classifier has

```math
E=\int L_y^{AC}\otimes D_{1|y}^{B}\,{\rm d}y,
\qquad
I-E=\int L_y^{AC}\otimes D_{0|y}^{B}\,{\rm d}y.
```

Both effects are separable, and therefore positive under partial transpose on $`B`$. Thus such classifiers lie inside the compact finite-dimensional set

```math
\mathcal P=
\{E:0\leq E\leq I,\ E^{T_B}\geq0,\ (I-E)^{T_B}\geq0\}.
```

It is enough to prove that no globally optimal effect belongs to $`\mathcal P`$.

## A three-dimensional obstruction for every training size

By exchanging the labels, assume $`p>q>0`$, and write $`t=p-q>0`$. Let $`|\Omega\rangle`$ be the all-up state of the $`2n+1`$ qubits. Both symmetric projectors fix it, so

```math
\Delta|\Omega\rangle=\kappa_n t|\Omega\rangle.
```

Every minimum-error effect for the minority label therefore satisfies $`E|\Omega\rangle=0`$.

Consider the invariant one-excitation subspace $`W`$ with normalized basis $`|A\rangle,|B\rangle,|C\rangle`$: the down spin lies respectively in the symmetric $`A`$ register, in the test, or in the symmetric $`C`$ register. Directly projecting the $`AB`$ and $`BC`$ registers onto their symmetric subspaces gives

```math
\left.\frac{\Delta}{\kappa_n}\right|_W
=
M=
\begin{pmatrix}
\dfrac{pn}{n+1}-q & \dfrac{p\sqrt n}{n+1} & 0\\[4pt]
\dfrac{p\sqrt n}{n+1} & \dfrac{t}{n+1} &
-\dfrac{q\sqrt n}{n+1}\\[4pt]
0 &-\dfrac{q\sqrt n}{n+1}&
p-\dfrac{qn}{n+1}
\end{pmatrix}.
```

The vector $`(\sqrt n,1,\sqrt n)`$ has eigenvalue $`t`$. The other two eigenvalues are

```math
\lambda_\pm
=
\frac{t\pm
\sqrt{1-4pq\,n^2/(n+1)^2}}{2}.
```

Because $`0<p,q<1`$ and $`n/(n+1)<1`$, one has $`\lambda_-<0<\lambda_+`$. Thus the optimal restriction of $`E`$ to $`W`$ is the rank-one projector $`|w\rangle\langle w|`$ onto the negative eigenvector.

All three components of $`w`$ are nonzero. Indeed, if $`w_B=0`$, the middle row forces $`pw_A=qw_C`$. Neither remaining component can vanish. The first and third rows would then require their diagonal entries to agree, whereas their difference is $`-1/(n+1)`$. This is a contradiction. Once $`w_B\ne0`$, the first and third rows imply $`w_A,w_C\ne0`$.

Consequently,

```math
\langle B|E|A\rangle=w_B\overline{w_A}\ne0.
```

Partial transpose on the test turns this entry into an entry of the row of $`|\Omega\rangle`$:

```math
\langle\Omega|E^{T_B}|A,B\rangle
=
\langle B|E|A\rangle\ne0.
```

Here $`|A,B\rangle`$ has one symmetric down spin in $`A`$ and a down test spin. At the same time,

```math
\langle\Omega|E^{T_B}|\Omega\rangle
=
\langle\Omega|E|\Omega\rangle=0.
```

A positive semidefinite matrix with a zero diagonal entry has an entirely zero corresponding row, by the two-by-two principal-minor inequality. Hence $`E^{T_B}`$ is not positive semidefinite. No quantum-optimal minority effect is PPT.

This argument uses only the forced actions on $`|\Omega\rangle`$ and $`W`$. It does not assume that the global weighted difference has no kernel elsewhere.

## Why the risk inequality is strict

The continuous risk functional attains a minimum on the compact set $`\mathcal P`$. If that minimum were $`R_{\rm Q}`$, its minimizer would be a globally optimal effect, contradicting the obstruction just proved. Therefore

```math
R_{\rm C}
\geq \min_{E\in\mathcal P}R(E)
>
R_{\rm Q}.
```

This also excludes a sequence of classical training measurements whose risks merely approach the quantum optimum at fixed $`n`$ and fixed unequal interior prior.

At $`p=1/2`$, the all-up eigenvalue is zero. The minority effect is no longer forced to annihilate that state, so the obstruction does not apply. The balanced-prior classical protocol of Sentís et al. attains the quantum optimum. At $`p=0`$ or $`1`$, the risk is zero by always choosing the known label. With no training, $`n=0`$, the two averaged test states are both $`I/2`$, and both interfaces have risk $`\min\{p,q\}`$ for every prior.

