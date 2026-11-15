# A classical risk plateau around balanced priors

Use the model, spin coefficients and explicit balanced dual in [classical training](classical_training.md).

## A finite interval of exactly unchanged classical performance

**Theorem.** For every $`n\geq1`$, define

```math
s_0(n)=y_{\min}\min\left\{1,\frac{n+2}{2n^2}\right\}.
```

Then

```math
D_C(n,s)=D_0(n)\qquad(0\leq s\leq s_0(n)).
```

**Proof.** Normalize the $`m=0`$ adjacency matrix by $`Y_0`$:

```math
K_0=Y_0^{-1/2}H_0^{(0)}Y_0^{-1/2}.
```

It is real symmetric, entrywise nonnegative and bipartite. Its positive vector $`Y_0^{1/2}\phi`$ has eigenvalue one. The Laplacian inequality also gives $`K_0\preceq I`$. Bipartiteness reflects its spectrum around zero; hence $`\lVert K_0\rVert=1`$.

For a fixed nonzero magnetic number $`m`$, its normalized adjacency matrix $`K_m`$ has a smaller index range and offdiagonal ratios

```math
\frac{h_j^{(m)}}{h_j^{(0)}}
=\sqrt{1-\frac{m^2}{j^2}}
\leq\sqrt{1-\frac{m^2}{n^2}}
\leq1-\frac{m^2}{2n^2}.
```

For $`|m|=n`$ there are no offdiagonal entries, so the same bound holds directly. A principal submatrix of $`K_0`$ has operator norm at most one. Monotonicity of the Perron eigenvalue under entrywise domination consequently yields

```math
\lambda_{\max}(K_m)\leq1-\frac{m^2}{2n^2},
```

and therefore

```math
Y_0-H_0^{(m)}
\succeq\frac{m^2}{2n^2}Y_0
\succeq\frac{m^2y_{\min}}{2n^2}I.
```

The prevalence perturbation in this block is the scalar $`sm/(n+2)`$. For $`m\gt 0`$, the assumed bound $`s\leq(n+2)y_{\min}/(2n^2)`$ implies

```math
\frac{sm}{n+2}\leq\frac{my_{\min}}{2n^2}
\leq\frac{m^2y_{\min}}{2n^2}.
```

For $`m\lt 0`$ the perturbation improves the inequality, and for $`m=0`$ it vanishes. Thus $`Y_0\succeq H_z(s)`$. The other dual constraint $`Y_0\succeq sI`$ follows from $`s\leq y_{\min}`$. This proves the upper bound $`D_C(n,s)\leq D_0(n)`$.

The same covariant seed $`v`$ has $`m=0`$, so its aligned payoff $`\langle v|H_z(s)|v\rangle`$ remains $`D_0(n)`$. It supplies the reverse inequality. Hence equality holds throughout the stated interval. $`\square`$

The interval is explicit and positive. For $`j\geq1`$, the first term of $`y_j`$ alone gives

```math
y_j\geq\frac13\frac{\sqrt{2n+1}}{n+2}.
```

The $`j=0`$ expression obeys the same lower bound. Thus

```math
y_{\min}\geq\frac{\sqrt{2n+1}}{3(n+2)}.
```

For $`n\geq2`$, a simple sufficient plateau is therefore

```math
0\leq s\leq L_n,
\qquad L_n=\frac{\sqrt{2n+1}}{6n^2}.
```

This is a sufficient interval; no claim that it is the maximal plateau is needed.

## Quantitative advantage of retained quantum training

The known global programmable-discrimination calculation gives

```math
D_Q(n,s)=\frac{2s}{n+2}
+\frac{2}{(n+1)(n+2)}
\sum_{k=1}^nk
\sqrt{1-(1-s^2)\frac{k^2}{(n+1)^2}}.
```

This formula follows from the two-dimensional multiplicity blocks of the two symmetric coupling schemes. The highest total spin contributes $`2s/(n+2)`$; every other block contributes the displayed square root. The arbitrary-prior global optimization is antecedent programmable-discrimination work, rather than the classical-record converse proved here; see He and Bergou, *Phys. Rev. A* **75**, 032316 (2007), [quant-ph/0610226](https://arxiv.org/abs/quant-ph/0610226).

Every square-root term is nondecreasing in $`s^2`$. Consequently the plateau theorem yields

```math
R_C(n,s)-R_Q(n,s)
=\frac{D_Q(n,s)-D_0(n)}2
\geq\frac{s}{n+2}
\qquad(0\leq s\leq s_0(n)).
```

For example, choosing $`s=L_n/2`$ for $`n\geq2`$ certifies

```math
R_C-R_Q\geq
\frac{\sqrt{2n+1}}{12n^2(n+2)}.
```

Thus the finite-data activation has a provable inverse-polynomial interval and risk gap. This statement supplements the strict-separation theorem for every nonzero interior bias; it does not assert a practical end-to-end learning speedup, repeated consumption-free inference, or the sharp asymptotic size of the gap at fixed prevalence.

