# Classical training plateaus and quantitative quantum-memory advantage

This account concerns one future classification, after balanced quantum training on two unknown pure qubit prototypes. A classical training record may contain arbitrarily many bits and may be obtained by an arbitrary joint measurement of all training systems. The distinction is whether quantum information survives from training to the future test. The retained quantum program need not survive that inference.

## Model and notation

Let $`n\geq1`$. Independently choose pure qubit states $`\psi_0,\psi_1`$ with normalized Haar measure. Training registers contain

```math
A=\psi_0^{\otimes n},\qquad C=\psi_1^{\otimes n}.
```

A future test qubit $`B`$ is $`\psi_0`$ with probability $`p`$ and $`\psi_1`$ with probability $`q=1-p`$. The training counts remain $`n,n`$ regardless of deployment prevalence. Exchanging class names allows us to take $`p\geq q`$ and write

```math
s=p-q=2p-1\in[0,1].
```

Write $`R_C(n,s)`$ for the minimum Haar-averaged error if training is converted into a classical record before $`B`$ arrives. Write $`R_Q(n,s)`$ for the minimum error with unrestricted joint access to retained training and $`B`$. It is convenient to use biases

```math
D_C=1-2R_C,\qquad D_Q=1-2R_Q.
```

Each training register lies in the symmetric spin-$`n/2`$ representation. Its dimension is $`n+1`$, and the training Hilbert space has dimension

```math
d_T=(n+1)^2.
```

Let $`J_A^u,J_C^u`$ denote spin components in direction $`u`$ on these two registers. Under simultaneous rotations, the training space decomposes without multiplicities:

```math
\mathcal H_T=\bigoplus_{j=0}^n\mathcal H_j,
\qquad \dim\mathcal H_j=2j+1.
```

$`P_j`$ denotes the projector onto $`\mathcal H_j`$.

## The exact classical optimization

For any training POVM outcome with nonzero effect $`E`$, its probability is

```math
w_E=\frac{\mathrm{Tr}E}{d_T}.
```

This is independent of the future test label. The two conditional test states have Bloch vectors

```math
\mu_0(E)=\frac{2}{n+2}\frac{\mathrm{Tr}(E\mathbf J_A)}{\mathrm{Tr}E},
\qquad
\mu_1(E)=\frac{2}{n+2}\frac{\mathrm{Tr}(E\mathbf J_C)}{\mathrm{Tr}E}.
```

To verify these identities, use

```math
\int\psi^{\otimes n}\,d\psi=\frac{I_{\rm sym}}{n+1},
\qquad
\int\psi^{\otimes n}\mathrm{Tr}(\psi\sigma_u)\,d\psi
=\frac{2J^u}{(n+1)(n+2)}.
```

The second identity follows by taking a Pauli component of the $`(n+1)`$-copy symmetric-projector integral. Here a pure state symbol inside an integral means its rank-one density operator.

The conditional Helstrom bias equals

```math
\max\{s,\,|p\mu_0(E)-q\mu_1(E)|\}.
```

Define the training operators

```math
H_u(s)=\frac{2(pJ_A^u-qJ_C^u)}{n+2}.
```

The two available actions for a training outcome are therefore: always guess the majority, with payoff $`s\mathrm{Tr}E`$; or choose a test Stern–Gerlach direction $`u`$, with payoff $`\mathrm{Tr}(EH_u)`$. Optimizing all training outcomes gives the exact primal problem

```math
D_C(n,s)=\frac1{d_T}\sup
\left\{s\mathrm{Tr}E_0+\sum_a\mathrm{Tr}(E_aH_{u_a}(s)):
E_0,E_a\succeq0,\ E_0+\sum_aE_a=I\right\}.
```

Allowing general measures over directions gives the same optimum. It is attained with finitely many outcomes: refine effects to rank one and consider the compact set consisting of a normalized rank-one training state together with one of its action payoffs. Feasible measurements correspond to convex combinations whose average state is $`I/d_T`$. The objective is a linear coordinate on this compact convex hull. Carathéodory's theorem supplies an optimizer using at most $`d_T^2+1`$ such state/action pairs. No finite precision or bounded classical-memory assumption is being imposed.

The dual problem is

```math
D_C(n,s)=\frac1{d_T}\min_Y\mathrm{Tr}Y,
\qquad Y\succeq sI,\quad Y\succeq H_u(s)\ \text{for every }u.
```

Weak duality follows by summing the operator inequalities against the POVM effects. There is no duality gap: the primal compact convex formulation admits separation, and the dual has a strictly feasible point $`Y=LI`$ for sufficiently large $`L`$. Equivalently, this is finite-dimensional conic duality applied to the compact measurement-action hull.

Twirl $`Y`$ under simultaneous rotations. Its trace is unchanged and all constraints are preserved, since the family $`\{H_u\}`$ rotates covariantly. Hence the dual can be restricted exactly to

```math
Y=\sum_{j=0}^ny_jP_j.
```

For such $`Y`$, every direction constraint is equivalent by rotation to the $`z`$ constraint. Thus an exact finite SDP is

```math
D_C(n,s)=\frac1{(n+1)^2}
\min_{y_0,\ldots,y_n}\sum_{j=0}^n(2j+1)y_j,
```

subject to

```math
Y\succeq sI,\qquad Y\succeq H_z(s).
```

The $`z`$ constraint splits further into magnetic blocks $`m=-n,\ldots,n`$. This SDP describes arbitrary classical-record training, rather than only separate state estimation or a chosen learning architecture.

## Spin coefficients

Set

```math
H_0=\frac{J_A^z-J_C^z}{n+2}.
```

Then

```math
H_z(s)=H_0+\frac{sJ_{\rm tot}^z}{n+2}.
```

Choose phases of the coupled basis $`|j,m\rangle`$ so that the nonzero offdiagonal coefficients of $`H_0`$ are positive. In a fixed $`m`$ block,

```math
\langle j,m|H_0|j-1,m\rangle
=h_j^{(m)}
=\frac{\sqrt{[(n+1)^2-j^2](j^2-m^2)}}{(n+2)\sqrt{4j^2-1}},
```

for $`j=|m|+1,\ldots,n`$. All diagonal entries vanish.

For completeness, these coefficients can be reconstructed without assuming an optimization result. The operator $`\mathbf D=\mathbf J_A-\mathbf J_C`$ is a vector under total rotations and is odd under interchange of the two equal spins. Its selection rules therefore allow only $`j\leftrightarrow j\pm1`$. The rank-one angular-momentum coefficient gives the $`m`$ dependence $`\sqrt{1-m^2/j^2}`$. Write $`a_j=\langle j,0|D_z|j-1,0\rangle`$. Rotational invariance and

```math
\mathbf D^2=n(n+2)I-\mathbf J_{\rm tot}^2
```

give the recurrence

```math
\frac{2j-1}{j}a_j^2+
\frac{2j+3}{j+1}a_{j+1}^2
=n(n+2)-j(j+1),
```

for $`1\leq j\leq n`$, with $`a_{n+1}=0`$; the starting equation at $`j=0`$ is $`3a_1^2=n(n+2)`$. Induction yields

```math
a_j^2=\frac{[(n+1)^2-j^2]j^2}{4j^2-1},
```

which is the stated formula after division by $`n+2`$.

## An optimal balanced dual and an attaining measurement

Define the positive vector $`\phi_j=\sqrt{2j+1}`$ and

```math
y_j=
\frac{j\sqrt{(n+1)^2-j^2}+
(j+1)\sqrt{(n+1)^2-(j+1)^2}}
{(n+2)(2j+1)},
\qquad 0\leq j\leq n.
```

Terms with a zero square root vanish. Let

```math
Y_0=\sum_{j=0}^ny_jP_j,
\qquad y_{\min}=\min_jy_j\gt 0.
```

In the $`m=0`$ block, $`y_j=(H_0\phi)_j/\phi_j`$. Thus, writing $`x_j=\phi_jz_j`$,

```math
x^\dagger(Y_0-H_0^{(0)})x
=\sum_{j=1}^nh_j^{(0)}\phi_{j-1}\phi_j
|z_j-z_{j-1}|^2\geq0.
```

So this block is a weighted graph Laplacian, with kernel spanned by $`\phi`$.

For $`m\ne0`$, the relevant $`j`$ range is a principal subspace of the $`m=0`$ block, and its offdiagonal entries shrink. A Perron comparison, proved explicitly in the next section, gives $`Y_0-H_0^{(m)}\succeq0`$. Consequently $`Y_0`$ is dual feasible at $`s=0`$.

An attaining training measurement is obtained from the normalized seed

```math
|v\rangle=\frac1{n+1}\sum_{j=0}^n\sqrt{2j+1}\,|j,0\rangle.
```

Let $`U_g`$ rotate both training registers. Schur orthogonality gives

```math
\int U_g|v\rangle\langle v|U_g^\dagger\,dg=\frac{I}{d_T}.
```

The effects $`d_TU_g|v\rangle\langle v|U_g^\dagger dg`$ therefore form a POVM. On observing $`g`$, measure the test along the correspondingly rotated $`z`$ direction. Its bias is

```math
\langle v|H_0|v\rangle
=\frac{2}{(n+1)^2(n+2)}
\sum_{j=1}^nj\sqrt{(n+1)^2-j^2}.
```

This equals $`\mathrm{Tr}Y_0/d_T`$, proving optimality. The continuous orbit is optional. Since $`I/d_T`$ lies in the convex hull of the orbit projectors, at most $`d_T^2`$ weighted orbit points reproduce its average exactly; every such point has the same aligned payoff. This supplies a finite attaining POVM with the same risk.

Write the balanced optimum as

```math
D_0(n)=D_C(n,0)
=\frac{2}{(n+1)^2(n+2)}
\sum_{j=1}^nj\sqrt{(n+1)^2-j^2}.
```

The equality $`D_C(n,0)=D_Q(n,0)`$ is the established memory-free balanced classifier result of Sentís, Calsamiglia, Muñoz-Tapia and Bagan, *Scientific Reports* **2**, 708 (2012), [arXiv:1106.2742](https://arxiv.org/abs/1106.2742). The argument above reconstructs its attaining covariant measurement and dual value in the conventions needed here.

