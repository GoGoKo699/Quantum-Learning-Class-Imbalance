# Finite-example robustness to prototype depolarization

## Finite-example robustness under prototype depolarization

Suppose each supplied copy is independently depolarized:

```math
\rho_i(\eta)=(1-\eta)\psi_i+\eta I/2,
\qquad 0\leq\eta\leq1.
```

Both the $`2n`$ training copies and the one test copy obey this noise model. There are no noise flags. Let $`R_C^\eta,R_Q^\eta`$ denote the corresponding optimized risks on the full physical Hilbert spaces. This changes the statistical model; no claim that the pure-state symmetric-support proof remains exact is being made.

For either fixed-prototype hypothesis, the pure $`(2n+1)`$-copy product is an eigenvector of the noisy product, with eigenvalue $`(1-\eta/2)^{2n+1}`$. Hence its trace distance from the noisy product is exactly

```math
\delta_n(\eta)=1-(1-\eta/2)^{2n+1}
\leq\frac{(2n+1)\eta}{2}.
```

Averaging the prototypes can only decrease trace distance. Any fixed classifier's risk therefore changes by at most $`\delta_n(\eta)`$. The admissible strategy sets do not depend on $`\eta`$, so optimization preserves the bound:

```math
|R_C^\eta-R_C^0|\leq\delta_n(\eta),
\qquad
|R_Q^\eta-R_Q^0|\leq\delta_n(\eta).
```

Moreover, both allowed learner classes can simulate the known depolarizing channel on noiseless data before following a noisy-data strategy. Noise therefore cannot decrease either optimized error:

```math
R_C^\eta\geq R_C^0,\qquad R_Q^\eta\geq R_Q^0.
```

Using the classical monotonicity and the quantum continuity bound gives the stronger one-sided comparison

```math
R_C^\eta-R_Q^\eta
\geq (R_C^0-R_Q^0)-\delta_n(\eta)
\geq (R_C^0-R_Q^0)-\frac{(2n+1)\eta}{2}.
```

A certified pure-state gap $`\gamma`$ remains positive whenever $`\delta_n(\eta)\lt \gamma`$; the simpler sufficient condition is $`\eta\lt 2\gamma/(2n+1)`$. On the proven plateau, $`\eta\lt 2s/[(n+2)(2n+1)]`$ is sufficient.

As a concrete small example, the exact $`n=1`$ formulas at $`p=3/5`$ give

```math
R_C^0-R_Q^0=\frac{3\sqrt{19}-7}{90}\approx0.067519.
```

At one percent prototype depolarization, the simple continuity estimate still certifies a gap exceeding $`0.0525`$ (the exact trace-distance expression gives approximately $`0.052594`$). This is a finite-example robustness guarantee; it does not establish a uniform fixed-noise advantage as $`n\to\infty`$ or determine the optimal noisy classifier.
