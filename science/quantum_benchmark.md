# The retained quantum and known-prototype benchmarks

The unrestricted programmable discriminator is inherited from earlier work, including He and Bergou. This page fixes its normalization and derives the formulas used in the classical-interface comparison.

## Finite training

On the symmetric program support, the averaged hypotheses are

```math
\sigma_0=\frac{P_{\rm sym}^{AB} \otimes I_C}{(n+1)(n+2)},
\qquad
\sigma_1=\frac{I_A\otimes P_{\rm sym}^{BC}}{(n+1)(n+2)}.
```

The projectors symmetrize $`n+1`$ qubits. The identities act on $`n`$-qubit symmetric spaces of dimension $`n+1`$. Put $`\Delta=p\sigma_0-q\sigma_1`$ and $`s=|p-q|`$. Helstrom's formula gives $`D_{\rm Q}=\lVert\Delta\rVert_1`$.

Coupling the two spin-$`n/2`$ program representations with the spin-$`1/2`$ test gives the globally symmetric sector of dimension $`2n+2`$, and two-dimensional multiplicity blocks at total spin $`k-1/2`$, for $`k=1,\ldots,n`$. The two symmetric coupling schemes have rank-one projectors in each such block, with overlap $`k/(n+1)`$. This Clebsch–Gordan/Jordan overlap is the standard programmable-discrimination ingredient.

For normalized vectors with overlap $`c`$, the two eigenvalues of $`p|a\rangle\langle a|-q|b\rangle\langle b|`$ are

```math
\frac{p-q\pm\sqrt{1-4pq\,c^2}}2.
```

For $`c\lt 1`$ and interior priors they have opposite signs, so their absolute sum is the square root. Include the spin degeneracy $`2k`$ and the common normalization. The top sector contributes $`2s/(n+2)`$. Therefore

```math
D_{\rm Q}(n,s)=\frac{2s}{n+2}
+\frac{2}{(n+1)(n+2)}
\sum_{k=1}^n k
\sqrt{1-(1-s^2)\frac{k^2}{(n+1)^2}}.
```

The optimum is implemented by the sign measurement of the known averaged matrix $`\Delta`$. The matrix depends only on $`n,p`$, not on descriptions of the unknown prototypes. Its implementation and memory cost are discussed in [resources](resources.md).

At one copy per class,

```math
D_{\rm Q}(1,s)=\frac{2s}{3}+\frac{\sqrt{3+s^2}}6.
```

At balance the expression equals the attaining classical value reconstructed in [classical training](classical_training.md). This equality is credited to Sentís et al.; the new result is its failure for every interior unequal prior.

## Oracle error and fixed-prior expansion

Let $`\mathbf r,\mathbf u`$ be the two unknown unit Bloch directions and let

```math
d=p\mathbf r-q\mathbf u,\qquad D=|d|.
```

For known prototypes the error is $`(1-D)/2`$. The overlap of two independent Haar pure qubits is uniform, so $`D`$ has density $`2D/(1-s^2)`$ on $`[s,1]`$. Its mean is

```math
I(s)=\frac{2(1-s^3)}{3(1-s^2)}
=\frac{2(1+s+s^2)}{3(1+s)},
\qquad
R_{\rm or}(s)=\frac{1-I(s)}2.
```

Use the continuous endpoint values. In particular $`I(0)=2/3`$ and $`I(1)=1`$.

For every fixed $`0\lt s\lt 1`$, set $`N=n+1`$ and apply Euler–Maclaurin to the smooth function $`f(x)=2x\sqrt{1-(1-s^2)x^2}`$. Since $`f(0)=0`$ and $`f(1)=2s`$,

```math
\sum_{k=1}^{N-1} f(k/N)
=N I(s)-s+O_s(N^{-1}).
```

Substitution into the exact bias gives

```math
D_{\rm Q}(n,s)
=I(s)+\frac{s-I(s)}n+O_s(n^{-2}),
```

and hence

```math
\lim_{n\to\infty}n\bigl(R_{\rm Q}(n,s)-R_{\rm or}(s)\bigr)
=\frac{I(s)-s}{2}.
```

The fixed positive $`s`$ is essential to this smooth-endpoint argument. It is not a uniform expansion through $`s=0`$.

See [related work](../references/related_work.md) for the earlier arbitrary-prior programmable solution. The finite suite independently compares this normalized sum with dense averaged-state trace norms.

