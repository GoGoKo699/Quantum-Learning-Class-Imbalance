# Exact classical risk with one training qubit per class

## The phase diagram

Use the independent-Haar pure-qubit model in [class-prior activation](activation.md), with one labeled training qubit from each class. Let $`s=|2p-1|`$ and write

```math
R_{\rm C}(1,p)=\frac{1-D_{\rm C}(s)}2.
```

The exact optimum over arbitrary collective training measurements, arbitrary retained classical records and arbitrary conditional test measurements is

```math
D_{\rm C}(s)=
\begin{cases}
\dfrac{\sqrt3}{6},
&0\leq s\leq\dfrac1{3\sqrt3},\\[6pt]
\dfrac{3s}{4}+\dfrac1{36s},
&\dfrac1{3\sqrt3}\leq s\leq\dfrac13,\\[6pt]
s,&\dfrac13\leq s\leq1.
\end{cases}
```

The first interval is an exact risk plateau. In the last interval no measured-training classifier improves on always choosing the more frequent label. At the boundary $`s=1/3`$, some posterior test decisions can tie that risk while producing minority predictions; strict $`s\gt 1/3`$ forces the majority decision for every nonzero-probability training outcome.

For comparison, the inherited global programmable-discrimination optimum is

```math
D_{\rm Q}(s)=\frac{2s}{3}+\frac{\sqrt{3+s^2}}6,
\qquad
R_{\rm Q}(1,p)=\frac{1-D_{\rm Q}(s)}2.
```

It follows either from the three-qubit spectrum or the general Jordan-basis calculation of [He and Bergou (2007)](https://doi.org/10.1103/PhysRevA.75.032316). The new optimization here concerns the measured-training interface. The two risks agree at $`s=0,1`$ and satisfy $`R_{\rm C}\gt R_{\rm Q}`$ throughout $`0\lt s\lt 1`$.

## Posterior states produced by a training effect

Assume $`p\geq q=1-p`$, so $`s=p-q`$. Haar averaging makes the training state $`I_{AC}/4`$. Refining a training effect into rank-one effects cannot hurt: the refined outcome includes all the old information and can use the same test decision. We may therefore write each refined effect as $`\lambda|v\rangle\langle v|`$, with $`v`$ normalized. Its outcome probability is $`\lambda/4`$.

Let $`\mathbf a,\mathbf c`$ be the marginal Bloch vectors of $`|v\rangle`$ on the two training qubits. The elementary qubit Haar second moment gives the two conditional mean test states

```math
\bar\rho_{0|v}
=
\frac{I+\mathbf a\cdot\boldsymbol\sigma/3}{2},
\qquad
\bar\rho_{1|v}
=
\frac{I+\mathbf c\cdot\boldsymbol\sigma/3}{2}.
```

The optimal conditional test bias is consequently

```math
g(v)=
\left\lVert p\bar\rho_{0|v}-q\bar\rho_{1|v}\right\rVert_1
=
\max\!\left\{s,\frac{|p\mathbf a-q\mathbf c|}{3}\right\}.
```

Let $`u=|\langle{\rm singlet}|v\rangle|^2`$. Completeness of the training POVM implies

```math
\sum_y w_y=1,\qquad
\sum_y w_yu_y=\frac14,
\qquad
w_y=\frac{\lambda_y}{4}.
```

The same formulas hold with integrals for continuous outcomes.

## Optimize a pure training effect at fixed singlet fraction

At fixed $`u`$, the largest possible length of $`p\mathbf a-q\mathbf c`$ is

```math
f_s(u)=
\begin{cases}
s+(s^{-1}-s)u,
&0\leq u\leq\dfrac{s^2}{1+s^2},\\[5pt]
2\sqrt{u(1-u)},
&\dfrac{s^2}{1+s^2}\leq u\leq1.
\end{cases}
```

At $`s=0`$, use the continuous expression $`f_0(u)=2\sqrt{u(1-u)}`$.

To prove the formula, rotate the vector being maximized to the $`z`$ axis. Its length is the maximum expectation of $`p\sigma_{Az}-q\sigma_{Cz}`$. In the singlet/triplet basis this operator couples the singlet to the zero-magnetization triplet with matrix entry $`1`$, while its other triplet eigenvalues are $`\pm s`$. If $`v_0`$ denotes the population of that zero-magnetization triplet, the maximum at fixed $`u,v_0`$ is

```math
2\sqrt{uv_0}+s(1-u-v_0),
\qquad 0\leq v_0\leq1-u.
```

The maximizer is $`v_0=\min\{1-u,u/s^2\}`$, which gives the displayed branches.

The first branch never improves on the majority bias after the factor $`1/3`$ is included. Defining

```math
h(u)=\frac23\sqrt{u(1-u)},
```

we obtain the particularly simple exact fixed-$`u`$ optimum

```math
\max_{v:\,|\langle{\rm singlet}|v\rangle|^2=u}g(v)
=
\max\{s,h(u)\}.
```

Thus the remaining problem is a scalar moment optimization: maximize the average of $`\max\{s,h(u)\}`$ over distributions on $`[0,1]`$ with mean $`1/4`$.

## Concave envelope and its attainment

If $`s\geq1/3`$, then $`h(u)\leq1/3\leq s`$, so the answer is $`D_{\rm C}=s`$.

For $`0\lt s\lt 1/3`$, the concave envelope joins $`(0,s)`$ tangentially to $`h`$, follows $`h`$, and uses the reflected tangent to $`(1,s)`$. The left contact point solves

```math
h(u_*)-u_*h'(u_*)=s,
\qquad
u_*=\frac{9s^2}{1+9s^2}.
```

If $`u_*\leq1/4`$, equivalently $`s\leq1/(3\sqrt3)`$, the envelope at $`1/4`$ is

```math
h(1/4)=\frac{\sqrt3}{6}.
```

Otherwise $`1/4`$ lies on the left tangent and the value is

```math
s+\frac14h'(u_*)
=
\frac{3s}{4}+\frac1{36s}.
```

The endpoint $`s=0`$ follows directly from concavity of $`h`$. These are upper bounds on every training POVM.

They are also attainable. For any chosen singlet fraction $`u`$, use a pure seed

```math
|v_u\rangle
=
\sqrt u\,|{\rm singlet}\rangle
+
\sqrt{1-u}\,|{\rm triplet},0\rangle
```

when the curved branch is used, and any triplet seed at $`u=0`$. Common rotations of a seed have the same discrimination bias. Their covariance average is

```math
\int (U\otimes U)|v_u\rangle\langle v_u|
(U^\dagger\otimes U^\dagger)\,{\rm d}U
=
uP_{\rm s}+\frac{1-u}{3}P_{\rm t}.
```

A distribution of such seeds whose mean $`u`$ is $`1/4`$, multiplied by the overall factor $`4`$, therefore defines a complete training POVM. Use the single seed $`u=1/4`$ in the plateau; in the intermediate region mix seeds $`u=0`$ and $`u=u_*`$ with probability $`1/(4u_*)`$ on the latter. Follow each outcome by its posterior Helstrom test.

The covariance average can be made a finite POVM by a qubit unitary two-design; for example, the 24 projective single-qubit Clifford rotations suffice. Hence at most 48 training outcomes attain the intermediate branch, and an unbounded continuum-valued record is unnecessary. Exact ideal gates are part of the statistical model; approximate implementation errors require their own accuracy budget.

## Interpretation

At equal priors the classical and quantum optima coincide, as in [Sentís et al. (2012)](https://doi.org/10.1038/srep00708). For small $`s\gt 0`$ the classical optimum remains on its plateau, while the global optimum exploits the newly signed symmetric sector. Quantitatively,

```math
R_{\rm C}(1,p)-R_{\rm Q}(1,p)
=
\frac{s}{3}+O(s^2).
```

This is a statement about the optimal binary error for native unknown quantum specimens and one test. The class prior is known and is allowed to change the training POVM. There is no restriction to separate state tomography, product training measurements, bounded classical computation or a fixed classifier architecture.

