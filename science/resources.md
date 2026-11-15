# Specimens, memory and implementation

The results compare prediction risk under matched native quantum inputs. A classical-record learner is allowed a quantum computer during training. Its restriction is the training-to-test memory boundary, not classical arithmetic or a chosen circuit architecture.

## What is paid

| Resource | Account |
|---|---|
| Training source | Exactly $`2n`$ supplied labeled qubits, $`n`$ per unknown prototype. Preparing them is an external source cost. Neither learner receives their amplitudes. |
| Test source and output | One supplied test qubit; one output label. An experiment repeated for risk estimation needs new specimens. |
| Retained storage | The direct global implementation holds $`2n`$ program qubits until test arrival. The constant-fraction rare-class construction holds only the required majority references and may discard the rest. |
| Classical storage | Unrestricted in the converse. Finite attaining POVMs exist, so the statistical optimum need not require a continuum of recorded bits. |
| Controls | All gates and measurements may depend on known $`n,p`$, and the fixed source prior. They cannot depend on unknown prototype descriptions. |
| Reuse | The global program and test may be consumed. No output is promised to be an undisturbed reusable training library. |
| Timing and hardware | The training-to-test delay requires coherent storage when quantum examples are retained. Noise protection, source latency, physical duration and hardware crossover are separate costs. |

The strict finite-$`n`$ separation excludes arbitrary collective training measurements with unlimited classical records. It is not a comparison against separate tomography only. The [rare-class theorem](rare_class.md) states its sample budget per class; multiplying by two gives the full balanced-library supply.

## Statistical attainability and finite records

The [classical optimization](classical_training.md) is a finite-dimensional measurement decision problem. Its optimum has a finite POVM with at most $`d_T^2+1`$ outcomes, where $`d_T=(n+1)^2`$. Thus a label for an ideal training outcome needs $`O(\log n)`$ bits, together with a fixed known table specifying its later test measurement. This table, its construction, numerical precision and gate compilation are not free preprocessing.

For $`n=1`$, the exact classical phase diagram has an explicit construction with at most 48 outcomes using single-qubit Clifford rotations of one or two fixed two-qubit seeds. It acts collectively on the two training qubits and retains only the outcome. A Naimark dilation therefore has constant dimension; ideal seed angles depend on the known prior. Finite gate approximation adds a controllable decision error.

For general $`n`$, the finite SDP determines the optimum and certified feasible duals give upper bounds on the bias. A floating-point solver value alone is not an exact optimum certificate. The analytical plateau uses an explicit feasible dual and a matching physical covariant POVM, so it does not rely on numerical optimization.

## Coherent compression and a paid realization

Each $`n`$-copy pure program is supported on a known symmetric space of dimension $`n+1`$. A Schur transform separates that spin-$`n/2`$ irrep from fixed permutation registers. Those fixed registers can be returned or discarded, leaving at most $`\lceil\log_2(n+1)\rceil`$ coherent qubits per program. Thus

```math
2\lceil\log_2(n+1)\rceil
```

persistent logical qubits suffice for exact statistical support compression of both programs; approximate gate implementations require an error budget. This is an upper bound, not a theorem about the minimum memory needed for the optimal decision. Input handling still touches the $`2n`$ original specimens.

Efficient approximate Schur circuits are established by Bacon, Chuang and Harrow, [quant-ph/0407082](https://arxiv.org/abs/quant-ph/0407082). They have size polynomial in input count and logarithmic inverse precision for fixed local dimension. The compression cost is included here; the change of representation is not an additional source oracle.

After compression, the program-plus-test support has dimension $`d=2(n+1)^2`$. The averaged matrix $`\Delta`$ is known. A classical eigendecomposition can precompute its sign measurement using dense linear algebra, with a direct arithmetic cost $`O(d^3)`$ and storage $`O(d^2)`$ at fixed numerical precision. An arbitrary unitary on a padded $`O(d)`$-dimensional register admits a dense realization using $`O(d^2)`$ elementary continuous rotations and entangling gates, by standard synthesis; see Shende, Bullock and Markov, [quant-ph/0406176](https://arxiv.org/abs/quant-ph/0406176). These loose polynomial upper bounds suffice to make the statistical decision concrete. They are not optimized gate counts or a runtime separation.

If the Schur compression, final decision and any intermediate known channels have total half-diamond implementation error at most $`\xi`$, every output-label probability changes by at most $`\xi`$. Budget the sum of the actual channel errors, including initial workspace mismatch. Distinguishing an inverse-polynomial risk gap requires implementation error smaller than that gap. Clean ancillas, synthesis precision and their return obligations belong to this channel budget.

## Rarity and the cost of a claimed saving

For fixed fractional minority-risk reduction, the [classical lower bound](rare_class.md) requires order $`1/q`$ examples per class as $`q\downarrow0`$. A constant number of retained references suffices through established universal state comparison. This saves specimens at the same target *relative* risk, whose absolute size is order $`q`$.

Observing that relative benefit empirically is itself costly when the minority is rare. If deployment labels occur with frequency $`q`$, collecting labeled minority tests generally requires order $`1/q`$ deployment trials per minority observation. The theorem counts the supplied training/test specimens of one prediction and does not erase this external evaluation cost.

## Noise and scope

The finite [depolarization bound](noise.md) guarantees an open noisy neighborhood of concrete finite examples. It does not make zero-false-positive state comparison survive full-rank noise, establish a fixed-noise large-$`n`$ advantage, or provide a fault-tolerance threshold. The source assumptions, chronology, average-risk criterion and known prior remain part of every quantitative statement.

