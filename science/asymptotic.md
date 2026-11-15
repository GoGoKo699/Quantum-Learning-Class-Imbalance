# A first-order penalty at every fixed imbalanced prior

The [finite-training activation theorem](activation.md) is an exact statement about equality of the two interfaces. This page shows that, at each fixed interior imbalanced prior, the difference also persists at the leading order in inverse training size. The proof uses a Bayesian Holevo information bound, with its positive-weight and regularity hypotheses made explicit.

## Statement and limiting order

Use the [prediction model](model.md), exchange class labels so that $`p>q>0`$, and set $`s=p-q\in(0,1)`$. Let $`R_{\rm or}(s)`$ denote the known-prototype error. Define

```math
I(s)=\frac{2(1+s+s^2)}{3(1+s)},\qquad
J(s)=\frac{s}{2}\left(1+\frac{2\log(1/s)}{1-s^2}\right),
\qquad A(s)=\frac{J(s)+s}{2}.
```

For every fixed $`s\in(0,1)`$,

```math
\boxed{
\liminf_{n\to\infty}n\bigl(R_{\rm C}(n,s)-R_{\rm Q}(n,s)\bigr)
\geq A(s)>0
}
```

and the finite upper bound

```math
0\leq R_{\rm C}(n,s)-R_{\rm Q}(n,s)
\leq\frac{I(s)}{n+2}
```

holds for all $`n\geq1`$. Consequently

```math
R_{\rm C}(n,s)-R_{\rm Q}(n,s)=\Theta_s(n^{-1}).
```

The prior is held fixed before $`n`$ tends to infinity. The constants and the sufficiently large training threshold may depend on $`s`$. These bounds neither identify the exact leading coefficient nor give a joint law as imbalance vanishes or the minority becomes rare. In particular, $`A(s)`$ is a proved lower coefficient; equality with it is not asserted.

## The statistical input

Gill and Guță, [*On Asymptotic Quantum Statistical Inference*, arXiv:1112.2078v3](https://arxiv.org/abs/1112.2078), Theorem 1 and equations (7)–(16), establish an integrated asymptotic Holevo lower bound for arbitrary collective measurement and estimator sequences in smooth finite-dimensional quantum iid models. Their theorem requires a compact smooth prior vanishing at its boundary, a finite prior-information term, and a positive-definite induced parameter weight. The proof below uses that positive-weight theorem; it does not assume its unproved singular-weight extension.

One iid system here is the four-dimensional pure pair

```math
\rho(\theta)=P_{\mathbf r_0}\otimes P_{\mathbf r_1},
\qquad \theta\in S^2\times S^2.
```

There are $`n`$ such pairs. A known permutation identifies this input with exactly $`n`$ examples from each class, so arbitrary collective training measurements are covered. On compact coordinate patches the model has four independent real tangent directions and nonsingular SLD information. Pure-state models are included in the statistical theorem's finite-dimensional setting.

The local classification-to-estimation method is related to Guță and Kotłowski, [arXiv:1004.2468](https://arxiv.org/abs/1004.2468). Their stated local model and training allocation differ from the equal-budget pure-Haar experiment here. The global programmable benchmark is credited separately in [quantum benchmarks](quantum_benchmark.md).

## Exact local reduction from a classifier to an estimator

For fixed prototypes put

```math
d=p\mathbf r_0-q\mathbf r_1,\qquad D=|d|,\qquad e=d/D.
```

Then $`s\leq D\leq1`$, with equality $`D=s`$ only for identical directions. A projective test with axis $`\widehat e`$ has the exact excess over the known-state error

```math
L(\theta,\widehat e)=\frac{D}{4}|\widehat e-e|^2.
```

The constant majority and minority guesses have excess $`(D-s)/2`$ and $`(D+s)/2`$, respectively.

This also covers general final qubit POVMs. If an effect has eigenvalues $`\lambda_{\min}\leq\lambda_{\max}`$, it is a convex mixture of the extreme effects $`I`$, a rank-one projector, and $`0`$, with weights $`\lambda_{\min}`$, $`\lambda_{\max}-\lambda_{\min}`$, and $`1-\lambda_{\max}`$. The risk is linear in that effect.

Choose a small compact coordinate patch $`U`$ on which $`D-s\geq\gamma>0`$. Let $`e_0`$ be the axis at its center, and shrink the patch until

```math
\sup_{\theta\in U}\frac D4|e(\theta)-e_0|^2\leq\frac\gamma2.
```

Replace every constant final action by the estimate $`e_0`$, and keep every projective action's axis. The resulting direction estimator has quadratic loss at most the original classification excess, pointwise in the parameter and training outcome. It may use the patch index, which only makes the estimation problem easier. Thus a lower bound for this directional estimation problem applies to every classical-record learner, without assuming that its final decision is always projective.

## The pure-pair Holevo cost

At a nonparallel pair, let $`k`$ be normal to the two Bloch directions and let $`l=k\times e`$. Choose oriented tangent coordinates along $`k\times\mathbf r_0,k`$ for the first state and $`k\times\mathbf r_1,k`$ for the second. Write

```math
c_0=\mathbf r_0\cdot e
=\frac{p-q\mathbf r_0\cdot\mathbf r_1}{D},\qquad
c_1=\mathbf r_1\cdot e
=\frac{p\mathbf r_0\cdot\mathbf r_1-q}{D}.
```

The transverse perturbations of $`d`$ are

```math
z_l=p c_0u_1-q c_1v_1,\qquad
z_k=p u_2-q v_2.
```

In a basis with the local pair state $`|00\rangle`$, the four normalized tangent derivatives are $`|10\rangle/2,i|10\rangle/2,|01\rangle/2,i|01\rangle/2`$. Local unbiasedness therefore fixes the tangent components of the two response-observable vectors to

```math
x_l=(p c_0,-q c_1),\qquad x_k=(ip,-iq).
```

Their summed intrinsic variance and imaginary covariance are

```math
V=p^2c_0^2+q^2c_1^2+p^2+q^2
=\frac{(D^2+1)(D^2+s^2)}{2D^2},
```

```math
C=\operatorname{Im}\langle x_l,x_k\rangle
=p^2c_0+q^2c_1
=\frac{s(1+D^2)}{2D}>0.
```

Extra components in the normal direction $`|11\rangle`$ cannot reduce the Holevo cost: their summed squared norms are at least twice the absolute value of their imaginary covariance. The triangle inequality then gives

```math
\text{extra variance}+2|C+\text{extra imaginary covariance}|
\geq2C.
```

Taking no extra components attains the response-observable cost $`V+2C`$. The derivative of $`e`$ divides the transverse components by $`D`$, while the loss weight is $`D/4`$. Hence the local target Holevo constant is

```math
\mathcal H(\theta)=\frac{V+2C}{4D}.
```

This calculation retains all four unknown tangent parameters. It does not supply the nuisance parameters to the learner.

## Positive weights and the finite prior-information term

The direction target alone induces a rank-two weight on a four-parameter model. To use the cited theorem as stated, augment the target to $`\Psi(\theta)=(e(\theta),\theta)`$ with quadratic loss

```math
\frac D4|\widehat e-e|^2+\varepsilon|\widehat\theta-\theta|^2,
\qquad \varepsilon>0.
```

Its induced chart weight is

```math
G_\varepsilon
=\frac D4(\partial e)^\mathsf T(\partial e)+\varepsilon I_4\succ0.
```

The regularity needed for the statistical theorem can be verified explicitly. In a smooth locally QFI-orthonormal oriented tangent frame, the four full-parameter response vectors have minimal Gram matrix

```math
Z_0=I_4+i\Omega,\qquad
\Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\oplus\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad \Omega^2=-I_4.
```

Let $`G\succ0`$ be a weight in these normalized coordinates. Any other locally unbiased response adds a positive Gram matrix $`W`$ from the normal components. For such a Gram matrix,

```math
\operatorname{Tr}(G\operatorname{Re}W)
\geq\left\|i\sqrt G(\operatorname{Im}W)\sqrt G\right\|_1.
```

Indeed the positive matrix $`\sqrt G W\sqrt G`$ and its complex conjugate imply that its real part dominates both signs of its Hermitian imaginary part; taking positive and negative spectral projections gives the trace bound. The trace-norm triangle inequality now proves the full-parameter Holevo formula

```math
C_G=\operatorname{Tr}G+
\operatorname{Tr}\left|i\sqrt G\Omega\sqrt G\right|.
```

A real optimal covariance field is

```math
V_0(G)=I_4+G^{-1/2}
\left|i\sqrt G\Omega\sqrt G\right|G^{-1/2}.
```

To check feasibility, set $`H=i\sqrt G\Omega\sqrt G`$. Then

```math
V_0-Z_0=G^{-1/2}(|H|-H)G^{-1/2}\succeq0.
```

The matrix $`|H|=\sqrt{H^2}`$ is real symmetric positive definite: $`H`$ is Hermitian and invertible because $`G`$ and $`\Omega`$ are invertible, and $`H^2`$ is real positive definite. Thus $`V_0`$ is real positive definite and its cost equals $`C_G`$. Principal square roots and inverses are smooth on positive-definite matrices, including at repeated eigenvalues. A smooth invertible congruence transfers this covariance field from the normalized tangent frame to any compact coordinate chart.

For each fixed $`\varepsilon>0`$, the augmented weight, this optimal covariance field, and their derivatives are bounded on the compact patch. Consequently the matrix field used in the Gill–Guță van Trees proof, $`\mathsf C=\widetilde G\Psi'V_0`$, is smooth and bounded there. Choose compact smooth bump priors that vanish faster than any power at their boundary. The derivatives of the bump contribute only polynomial inverse-boundary factors, so the prior-information integral in their equation (16) is finite. This closes that theorem's regularity condition for the present model.

## Removing the nuisance weight with charged additional data

Suppose the candidate direction estimator uses $`n`$ pairs. For a fixed $`\delta>0`$, append $`m=\lfloor\delta n\rfloor`$ additional independent pairs only to estimate the full coordinate vector. Separate Pauli measurements followed by chart projection give, on the compact patch,

```math
\sup_{\theta\in U}\mathbb E_\theta
|\widehat\theta-\theta|^2\leq B_U/m.
```

Apply the positive-weight theorem to the combined measurement on $`N=n+m`$ iid pairs. Let $`\mathcal H_\varepsilon`$ be the augmented Holevo constant. Discarding the nonnegative nuisance cost and compressing the Holevo primal covariance constraint to the directional block gives $`\mathcal H_\varepsilon\geq\mathcal H`$. For every smooth patch prior $`\pi`$,

```math
\liminf_{n\to\infty}n\mathbb E_\pi L_n
\geq\frac{\mathbb E_\pi\mathcal H_\varepsilon}{1+\delta}
-\frac{\varepsilon B_U}{\delta}
\geq\frac{\mathbb E_\pi\mathcal H}{1+\delta}
-\frac{\varepsilon B_U}{\delta}.
```

First take $`\varepsilon\downarrow0`$ at fixed $`\delta`$, then $`\delta\downarrow0`$. This proves

```math
\liminf_{n\to\infty}n\mathbb E_\pi L_n
\geq\mathbb E_\pi\mathcal H.
```

The additional copies are a conservative proof device. Their count is included in $`N`$, their estimation error is included above, and they are removed in the stated order of limits. They are not free examples in the original prediction experiment.

## Integrating the lower bound

Temporarily restrict to a compact subset away from identical or antipodal prototypes and chart boundaries. Cover it by finitely many patches satisfying the action-replacement inequality. Take nonnegative smooth partition weights whose sum is at most one everywhere and equals one on that compact subset. Apply the patch lower bound to each weighted Haar prior and sum. Classification excess is nonnegative, so discarding the uncovered parameter region is valid. Increase the compact subsets to full Haar measure. For fixed $`s>0`$, $`D\geq s`$ makes $`\mathcal H`$ integrable.

This gives a Bayesian bound for arbitrary learner sequences, including approximate minimizers of the global risk:

```math
\liminf_{n\to\infty}n
\bigl(R_{\rm C}(n,s)-R_{\rm or}(s)\bigr)
\geq\int\mathcal H(\theta)\,d\mu(\theta).
```

For independent Haar directions, $`D`$ has density $`D/(2pq)`$ on $`[s,1]`$. Direct integration yields

```math
\int\frac{V}{4D}\,d\mu=\frac{I(s)}2,
\qquad
\int\frac{2C}{4D}\,d\mu=\frac{J(s)}2.
```

Therefore

```math
\liminf_{n\to\infty}n
\bigl(R_{\rm C}(n,s)-R_{\rm or}(s)\bigr)
\geq\frac{I(s)+J(s)}2.
```

The [coherent benchmark expansion](quantum_benchmark.md#oracle-error-and-fixed-prior-expansion) is

```math
\lim_{n\to\infty}n
\bigl(R_{\rm Q}(n,s)-R_{\rm or}(s)\bigr)
=\frac{I(s)-s}{2}.
```

Subtracting this convergent sequence from the classical liminf proves the lower coefficient $`A(s)=(J(s)+s)/2`$.

## A classical strategy supplies the upper order

Independently make optimal covariant direction estimates of each $`n`$-copy training block. The conditional predictive Bloch vectors have shrinkage $`r_n=n/(n+2)`$, and the two estimate directions are independently Haar distributed after averaging. Their optimal conditional test therefore has bias

```math
D_{\rm ED}(n,s)=\mathbb E\max\{s,r_nD\}
\geq r_n\mathbb E D=r_n I(s).
```

This is a permitted strategy within the general [classical-training optimization](classical_training.md). Since $`R_{\rm C}\leq R_{\rm ED}`$ and $`R_{\rm Q}\geq R_{\rm or}`$,

```math
R_{\rm C}-R_{\rm Q}
\leq R_{\rm ED}-R_{\rm or}
\leq\frac{I(s)-r_nI(s)}2
=\frac{I(s)}{n+2}.
```

Together with the positive lower coefficient, this proves the fixed-prior order. A matching formula for the optimal classical coefficient, the crossover through balance, and a uniform rare-prior asymptotic require separate analysis. The [rare-class result](rare_class.md) addresses a different operational limit.
