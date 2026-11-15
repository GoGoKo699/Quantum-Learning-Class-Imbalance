# Thirty milestones through the class-imbalance result

This is a common understanding map for the project. Its targets and dependencies are determined by the scientific argument. The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018), standard-layout author manuscript; the [anchor bridge](WATROUS_BRIDGE.md) identifies the relevant source sections, translates notation, and supplies the steps beyond the textbook. Primary research references provide attribution and proof ingredients, rather than additional educational anchors.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background must connect quantum specimens, statistical decisions, a training-to-test memory boundary, operator positivity, symmetry, and local estimation. The narrative then assembles the finite obstruction, exact small example, quantitative regimes, and their resource meaning. Each phase moves from individual objects to an integrated account; neither phase is a list of every technical lemma.

Dependencies name earlier milestones only. Source pointers lead to the canonical scientific files; an understanding target does not replace their hypotheses or proofs.

## Background and preliminaries

### M01: Quantum specimens and their states

**Phase:** Background/preliminaries.

**Central question:** What does it mean to receive an unknown quantum specimen rather than a classical description of it?

**Understanding target:** Explain a qubit density operator, a pure-state projector, and the difference between manipulating a specimen and knowing its amplitudes. Recognize that a supplied unknown state does not grant a preparation circuit or an inverse.

**Dependencies and story role:** None. This establishes the physical object that every later resource and decision refers to.

**Conceptual connection:** A quantum training example is an input system with an unknown state, so a memory restriction changes which physical information is available later.

**Source pointers:** Watrous §§2.1.2–2.1.3 (states and composite-state foundations), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [model: inputs and chronology](../science/model.md#inputs-chronology-and-risk); [resources: what is paid](../science/resources.md#what-is-paid).

### M02: Copies, tensor products, and hidden common prototypes

**Phase:** Background/preliminaries.

**Central question:** How can several independently supplied specimens share an unknown source without supplying its description?

**Understanding target:** Read a tensor power, distinguish a product conditional on a prototype from its correlated Haar average, and use partial trace to describe a subsystem.

**Dependencies and story role:** M01. Connects one specimen to a training library and a later test, preparing the correct averaged hypotheses.

**Conceptual connection:** The test and the matching training class share a latent prototype; averaging that common unknown state jointly is essential to the learning problem.

**Source pointers:** Watrous §2.1.3, especially the partial trace on manuscript p. 67, via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [model](../science/model.md#inputs-chronology-and-risk); [quantum benchmark: averaged hypotheses](../science/quantum_benchmark.md#finite-training).

### M03: Measurements, records, and the time of a decision

**Phase:** Background/preliminaries.

**Central question:** What information remains if all training quantum systems must be discarded before the test arrives?

**Understanding target:** Explain a POVM effect, its classical outcome, outcome-controlled test measurements, and the distinction between unlimited classical storage and retained quantum training information.

**Dependencies and story role:** M01–M02. Introduces the operational cut that the two learner classes share on either side but cross differently.

**Conceptual connection:** Arbitrary quantum processing during training is allowed in the classical-record baseline. The restriction concerns what survives the training-to-test delay.

**Source pointers:** Watrous §§2.3.1–2.3.2 (measurements and their implementations), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [model: interface table](../science/model.md#inputs-chronology-and-risk); [activation: the classical restriction](../science/activation.md#averaged-hypotheses-and-the-classical-restriction).

### M04: Class prevalence and zero-one risk

**Phase:** Background/preliminaries.

**Central question:** Why can changing deployment probabilities change the best classifier even when the training library stays balanced?

**Understanding target:** Distinguish the training counts from the known test prior, read ordinary error probability, and explain the majority-guessing risk and the imbalance parameter $`s=|2p-1|`$.

**Dependencies and story role:** M02–M03. Gives the physical decision problem its statistical objective before operator optimization is introduced.

**Conceptual connection:** The same two quantum class prototypes receive different weights in the decision as prevalence changes; the comparison does not penalize a learner for estimating an unknown prior.

**Source pointers:** Watrous §3.1.1 and Theorem 3.4 (weighted binary discrimination), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [model: risk and endpoint conventions](../science/model.md#notation-and-endpoint-conventions); [rare-class target](../science/rare_class.md#constant-fractional-improvement-costs-order-1q-classical-training-copies).

### M05: The weighted Helstrom decision

**Phase:** Background/preliminaries.

**Central question:** How does the sign of a weighted state difference determine an optimal binary measurement?

**Understanding target:** Relate $`p\rho_0-q\rho_1`$, its positive and negative eigenspaces, the trace norm, and the bias $`D=1-2R`$. Explain why a zero eigenspace permits multiple optimal decisions.

**Dependencies and story role:** M01, M03–M04. Turns the statistical objective into the operator sign problem used throughout the project.

**Conceptual connection:** The freedom on a zero sector becomes central at balance, while posterior positivity later explains the majority-risk threshold and its equality ties.

**Source pointers:** Watrous §3.1.1 and Theorem 3.4, manuscript pp. 128–129, via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [quantum benchmark](../science/quantum_benchmark.md#finite-training); [rare-class equality convention](../science/rare_class.md).

### M06: Haar averaging and symmetric copy support

**Phase:** Background/preliminaries.

**Central question:** Why can unknown pure-state copies be averaged into known symmetric-space operators?

**Understanding target:** Explain the Haar source assumption, the symmetric subspace of repeated pure states, and the difference between a known average operator and a known individual prototype.

**Dependencies and story role:** M01–M02, M05. Supplies the source-specific reduction that makes exact finite calculations possible.

**Conceptual connection:** Symmetric-projector identities describe the supplied-state ensemble and enable both the retained benchmark and the conditional test-state formulas.

**Source pointers:** Watrous §7.1.1, Proposition 7.1 and Corollary 7.3; §7.2.1 and Lemma 7.24, via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [quantum benchmark: finite training](../science/quantum_benchmark.md#finite-training); [classical training: posterior moments](../science/classical_training.md#the-exact-classical-optimization).

### M07: Separability and the partial-transpose obstruction

**Phase:** Background/preliminaries.

**Central question:** Which operator property must a training-measurement-then-test classifier satisfy?

**Understanding target:** Explain a separable effect across the training/test cut, why such an effect is positive under partial transpose, and why the PPT condition is a necessary restriction rather than a complete characterization of the classical interface.

**Dependencies and story role:** M02–M03, M05. Introduces the converse tool without imposing extra restrictions on the classical training measurement.

**Conceptual connection:** Showing that every globally optimal effect violates a necessary property excludes every allowed classical record, including records from collective quantum training.

**Source pointers:** Watrous §6.1.1 (separability) and §6.2.3, Definition 6.39 (partial transpose and PPT), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [activation: classical restriction](../science/activation.md#averaged-hypotheses-and-the-classical-restriction); [activation proof](../science/activation.md).

### M08: Optimization certificates and physical attainment

**Phase:** Background/preliminaries.

**Central question:** What evidence distinguishes an optimal risk from a feasible strategy or a numerical estimate?

**Understanding target:** Explain primal measurement strategies, dual operator bounds, weak and strong duality, and a matching attainable certificate. Distinguish an exact proof from floating-point SDP output.

**Dependencies and story role:** M03, M05, M07. Provides the framework needed to understand complete classical optimization rather than a restricted baseline.

**Conceptual connection:** A feasible dual bounds every classical training protocol; an explicit POVM with the same value closes the optimization.

**Source pointers:** Watrous §1.2.3 (semidefinite programming), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [classical training: exact optimization](../science/classical_training.md#the-exact-classical-optimization); [resources: statistical attainability](../science/resources.md#statistical-attainability-and-finite-records).

### M09: Rotation covariance and spin blocks

**Phase:** Background/preliminaries.

**Central question:** How does a rotation-invariant source reduce a large optimization to small structured blocks?

**Understanding target:** Explain averaging an operator over common rotations, spin and magnetic-sector labels as a way to organize symmetric-copy spaces, and the distinction between a representation change and an additional information source.

**Dependencies and story role:** M06, M08. Joins the ensemble symmetry to the finite classical SDP and the inherited global spectrum.

**Conceptual connection:** Twirling preserves the decision objective; multiplicity blocks and covariant seeds expose both the balanced equality and its response to prior tilt. The required spin coefficients are supplied in the project.

**Source pointers:** Watrous §7.2.1 (unitarily invariant measures), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); spin coupling is supplied locally; [classical training: spin coefficients](../science/classical_training.md#spin-coefficients); [quantum benchmark](../science/quantum_benchmark.md#finite-training).

### M10: Local estimation and decision loss

**Phase:** Background/preliminaries.

**Central question:** How can uncertainty in a measurement axis become an excess classification error?

**Understanding target:** Distinguish the known-prototype oracle from an attainable learned measurement, explain a local parameter perturbation, and read a quadratic directional loss as a small-error cost.

**Dependencies and story role:** M04–M05, M09. Prepares the statistical language needed for the fixed-prior large-training result.

**Conceptual connection:** At fixed nonzero imbalance, estimating the relevant decision axis gives a route to bounding the risk of every classical-record learner.

**Source pointers:** Watrous §2.3.1 and §3.1.1 (measurement and decision foundations), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); locally supplied [classification-to-estimation reduction](../science/asymptotic.md#exact-local-reduction-from-a-classifier-to-an-estimator); [oracle benchmark](../science/quantum_benchmark.md#oracle-error-and-fixed-prior-expansion).

### M11: Incompatible information and collective estimation

**Phase:** Background/preliminaries.

**Central question:** Why can the cost of learning two decision directions exceed the sum of independent scalar estimates?

**Understanding target:** Explain the role of noncommuting response observables and the imaginary covariance term in a multiparameter information bound. Distinguish the Holevo estimation bound from the Helstrom binary-decision formula.

**Dependencies and story role:** M05, M08, M10. Supplies the conceptual bridge from finite operator optimization to the research-level asymptotic ingredient.

**Conceptual connection:** The positive incompatibility contribution in the pure-pair model is what makes a first-order classical-memory penalty possible. Its detailed statistical theorem is a primary research dependency, beyond the anchor's foundations.

**Source pointers:** Watrous §2.3.1 (measurement foundations), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route); [pure-pair Holevo cost](../science/asymptotic.md#the-pure-pair-holevo-cost); [statistical input and attribution](../science/asymptotic.md#the-statistical-input); [related work](../references/related_work.md).

### M12: Assemble the matched learning experiment

**Phase:** Background/preliminaries.

**Central question:** What must remain matched when comparing the two training interfaces?

**Understanding target:** Reconstruct the complete source, chronology, known prior, permitted measurements, one-test output, averaged risk, and paid memory. Separate this experiment from classical-data learning, worst-case source pairs, and indefinitely reusable deployment.

**Dependencies and story role:** M01–M11. Integrates the background into one operational model before the new results are assembled.

**Conceptual connection:** Operator, symmetry, and estimation methods answer the same physical question only when their input promises and resource cut remain consistent.

**Source pointers:** [Anchor bridge](WATROUS_BRIDGE.md); [model](../science/model.md); [resources](../science/resources.md); [interpretation](../science/interpretation.md).

## Narrative and innovation

### M13: The inherited retained-training benchmark

**Phase:** Narrative/innovation.

**Central question:** What optimal quantum risk is the classical record being asked to reproduce?

**Understanding target:** Derive the known averaged hypotheses from the copy ensemble, explain the signed multiplicity-block spectrum, and identify the globally symmetric contribution to the exact retained-training bias.

**Dependencies and story role:** M05–M06, M09, M12. Establishes the credited benchmark against which the new classical-interface statements are measured.

**Conceptual connection:** The programmable discriminator depends on known ensemble data $`n,p`$, rather than access to unknown prototype descriptions. Its arbitrary-prior optimum is inherited prior work.

**Source pointers:** [Quantum benchmark: finite training](../science/quantum_benchmark.md#finite-training); [related work](../references/related_work.md); Watrous §3.1.1 and Lemma 7.24, via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route).

### M14: Why balance permits classical sufficiency

**Phase:** Narrative/innovation.

**Central question:** Which freedom lets a classical training record attain the global optimum at equal priors?

**Understanding target:** Explain the known balanced covariant classifier and the zero weighted difference on the globally symmetric sector. Identify why an equality at one prior does not establish sufficiency at every prior.

**Dependencies and story role:** M05, M09, M13. Places the new question directly beside the established memory-free result.

**Conceptual connection:** A prior tilt changes a zero sector into a signed sector, removing freedom in the global optimum without changing the supplied training counts.

**Source pointers:** [Classical training: balanced dual and attaining measurement](../science/classical_training.md#an-optimal-balanced-dual-and-an-attaining-measurement); [interpretation: signed decision sector](../science/interpretation.md#a-decision-sector-becomes-usable); [attribution](../references/related_work.md).

### M15: Every finite training size activates memory under imbalance

**Phase:** Narrative/innovation.

**Central question:** How can a three-dimensional subspace exclude every possible classical training record?

**Understanding target:** Follow the all-up and one-excitation argument: a biased optimal minority effect has a forced zero diagonal and a nonzero transition entry; partial transpose makes these incompatible with positivity. State the exact finite-$`n`$ equality set, including the trivial prior endpoints.

**Dependencies and story role:** M05, M07, M13–M14. Assembles the decisive finite-sample converse from its local operator mechanism.

**Conceptual connection:** The obstruction applies to the entire classical-record interface because its effects are separable, rather than because a chosen tomography procedure is weak.

**Source pointers:** [Activation theorem and proof](../science/activation.md); [model: endpoints](../science/model.md#notation-and-endpoint-conventions); Watrous §6.1.1 and §6.2.3 (separability and PPT), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route).

### M16: Reduce one-copy learning to a seed geometry

**Phase:** Narrative/innovation.

**Central question:** What does a pure two-qubit training effect reveal about the next test?

**Understanding target:** Derive the shrunken posterior Bloch vectors, explain the singlet-fraction constraint from POVM completeness, and understand why optimizing at fixed singlet fraction reduces the problem to a scalar moment constraint.

**Dependencies and story role:** M03, M05–M06, M08–M09, M15. Opens a complete small experiment where the strict theorem can be seen quantitatively.

**Conceptual connection:** The collective training measurement is represented by a distribution of seeds; optimizing that distribution still covers arbitrary classical records.

**Source pointers:** [One-copy posterior states](../science/one_copy.md#posterior-states-produced-by-a-training-effect); [fixed-singlet optimization](../science/one_copy.md#optimize-a-pure-training-effect-at-fixed-singlet-fraction); [anchor bridge](WATROUS_BRIDGE.md).

### M17: The complete one-copy phase diagram and its attainment

**Phase:** Narrative/innovation.

**Central question:** How do a plateau, a tangent branch, and majority guessing arise from one scalar optimization?

**Understanding target:** Explain the concave envelope at mean singlet fraction one quarter, identify the two transition biases, and connect every branch to a physical finite-outcome training POVM. Distinguish a risk equality at the majority boundary from a unique decision rule.

**Dependencies and story role:** M08–M09, M16. Closes the small example with both converse and attainable construction.

**Conceptual connection:** This gives an exact quantitative version of prior-induced activation, including why a finite classical record suffices to attain the classical optimum even though that optimum loses to retained training.

**Source pointers:** [One-copy phase diagram](../science/one_copy.md#the-phase-diagram); [concave envelope and attainment](../science/one_copy.md#concave-envelope-and-its-attainment); [finite records](../science/resources.md#statistical-attainability-and-finite-records).

### M18: Optimize every classical training protocol at general size

**Phase:** Narrative/innovation.

**Central question:** How can arbitrary training measurements be bounded and attained without enumerating them?

**Understanding target:** Follow the posterior-moment reduction to a finite covariant SDP, explain its dual constraints, and connect the explicit balanced graph-Laplacian certificate to an attaining covariant seed. Recognize finite POVM attainment and the role of dual feasibility.

**Dependencies and story role:** M06, M08–M09, M14, M17. Scales the fully optimized classical analysis beyond the small example.

**Conceptual connection:** The same training optimization supplies exact balanced performance and a certificate that survives small changes in prevalence.

**Source pointers:** [Classical training: exact optimization](../science/classical_training.md#the-exact-classical-optimization); [spin coefficients](../science/classical_training.md#spin-coefficients); [balanced certificate](../science/classical_training.md#an-optimal-balanced-dual-and-an-attaining-measurement); Watrous §1.2.3, via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route).

### M19: A certified all-size classical plateau

**Phase:** Narrative/innovation.

**Central question:** Why can the best classical risk remain exactly unchanged while the quantum risk improves?

**Understanding target:** Explain how shrinking magnetic-block couplings leaves the balanced dual feasible on an explicit interval, while its $`m=0`$ attaining seed has unchanged payoff. Interpret the resulting gap bound and distinguish a sufficient plateau from the maximal one.

**Dependencies and story role:** M13–M14, M18. Turns strict activation into a quantitative finite-size statement with explicit constants.

**Conceptual connection:** A persistent classical optimum and a newly signed quantum sector produce the linear-in-tilt lower bound $`R_C-R_Q\geq s/(n+2)`$ on the certified interval.

**Source pointers:** [Plateau theorem](../science/plateau.md#a-finite-interval-of-exactly-unchanged-classical-performance); [quantitative advantage](../science/plateau.md#quantitative-advantage-of-retained-quantum-training); [classical certificate](../science/classical_training.md).

### M20: Hold the prior fixed before increasing training size

**Phase:** Narrative/innovation.

**Central question:** What does the exact retained benchmark approach when a nonzero interior imbalance is fixed?

**Understanding target:** Explain the known-prototype oracle error, the Haar distribution of decision-vector length, and the fixed-prior inverse-training expansion of the retained risk. Identify why the expansion is not uniform through balance.

**Dependencies and story role:** M10, M13, M19. Establishes the reference term needed to interpret a large-training classical penalty.

**Conceptual connection:** A finite-sample inequality does not by itself determine the asymptotic order; the oracle and coherent expansion separate irreducible test error from learning cost.

**Source pointers:** [Oracle error and fixed-prior expansion](../science/quantum_benchmark.md#oracle-error-and-fixed-prior-expansion); [asymptotic statement and limiting order](../science/asymptotic.md#statement-and-limiting-order); [anchor bridge](WATROUS_BRIDGE.md).

### M21: Classification becomes a multiparameter estimation cost

**Phase:** Narrative/innovation.

**Central question:** What local information must a classical record preserve to choose the right test axis?

**Understanding target:** Explain the exact directional-loss identity, the treatment of constant and general final qubit actions, and the response-observable calculation $`V+2C`$. Keep all four unknown prototype tangent parameters in the model.

**Dependencies and story role:** M10–M11, M18, M20. Builds the load-bearing local ingredient for a converse covering arbitrary classical-record learner sequences.

**Conceptual connection:** The measurement axis is the target, while the prototype parameters remain unknown nuisance parameters; supplying them for free would change the problem.

**Source pointers:** [Classification-to-estimation reduction](../science/asymptotic.md#exact-local-reduction-from-a-classifier-to-an-estimator); [pure-pair Holevo cost](../science/asymptotic.md#the-pure-pair-holevo-cost); [statistical source](../science/asymptotic.md#the-statistical-input).

### M22: Apply the statistical theorem with its actual hypotheses

**Phase:** Narrative/innovation.

**Central question:** How is a directional target bounded without assuming an unsupported singular-weight theorem?

**Understanding target:** Explain positive nuisance-weight regularization, smooth compact patch priors, the finite prior-information condition, and the role of explicitly charged additional copies. Preserve the order of the sample limit, nuisance-weight limit, and extra-data fraction limit.

**Dependencies and story role:** M08, M11, M20–M21. Closes the regularity and quantifier gap between the local cost calculation and a valid Bayesian lower bound.

**Conceptual connection:** A research-level information inequality applies only after its positive-weight and smoothness conditions are met; the auxiliary data are a controlled proof device, not free inputs to the learner.

**Source pointers:** [Positive weights and prior information](../science/asymptotic.md#positive-weights-and-the-finite-prior-information-term); [charged extra-data limit](../science/asymptotic.md#removing-the-nuisance-weight-with-charged-additional-data); Gill–Guță primary theorem as identified in the [statistical input](../science/asymptotic.md#the-statistical-input).

### M23: The first-order penalty and the coefficient still open

**Phase:** Narrative/innovation.

**Central question:** What is established about the large-training memory penalty after integration and comparison?

**Understanding target:** Combine the integrated Holevo lower bound, the convergent retained expansion, and a feasible classical upper bound to obtain $`R_C-R_Q=\Theta_s(1/n)`$ for fixed $`0\lt s\lt 1`$. Read $`A(s)`$ as a positive liminf lower coefficient, rather than the exact optimal coefficient.

**Dependencies and story role:** M19–M22. Integrates the asymptotic argument into a complete order statement with its unresolved coefficient visible.

**Conceptual connection:** The penalty survives at first order for each fixed imbalanced prior, while the exact balanced equality and different joint limits remain consistent.

**Source pointers:** [Asymptotic statement](../science/asymptotic.md#statement-and-limiting-order); [integrating the lower bound](../science/asymptotic.md#integrating-the-lower-bound); [classical upper-order strategy](../science/asymptotic.md#a-classical-strategy-supplies-the-upper-order); [interpretation of limits](../science/interpretation.md#three-limits-answer-different-questions).

### M24: The exact rare-class majority-risk threshold

**Phase:** Narrative/innovation.

**Central question:** When does every classical training record fail to improve on the majority-guessing risk?

**Understanding target:** Use the posterior spectral bound to obtain $`R_C=q`$ exactly when $`q\leq1/(n+2)`$ after majority labeling. Explain the positive-probability training effect proving sharpness above the threshold, and distinguish a boundary tie from strict uniqueness of majority decisions.

**Dependencies and story role:** M04–M06, M18, M23. Moves from fixed-prior large training to a different operational question in the vanishing-minority regime.

**Conceptual connection:** Finite-copy posterior uncertainty prevents an extreme likelihood ratio, even with unlimited classical records from a collective training measurement.

**Source pointers:** [Rare-class statement and posterior bound](../science/rare_class.md); [threshold sharpness](../science/rare_class.md#sharpness-of-the-threshold); [one-copy boundary convention](../science/one_copy.md#the-phase-diagram).

### M25: Price a fixed fractional minority-risk improvement

**Phase:** Narrative/innovation.

**Central question:** How many training specimens are required to reduce a rare class's small baseline error by a fixed fraction?

**Understanding target:** For each fixed target fraction $`0\lt \eta\lt 1/2`$, combine the arbitrary-classical-training lower bound with an estimating strategy to obtain $`\Theta_\eta(1/q)`$ copies per class. Explain why an established coherent state-comparison test attains the same target with a constant number of retained majority references, and keep the vanishing absolute contrast visible.

**Dependencies and story role:** M03–M04, M24. Converts the rare-risk threshold into a resource comparison under a matched relative-error target.

**Conceptual connection:** The new classical lower bound is distinct from the inherited universal-comparison protocol; the retained reference is consumed in one inference.

**Source pointers:** [Classical fractional-improvement cost](../science/rare_class.md#constant-fractional-improvement-costs-order-1q-classical-training-copies); [retained-reference construction](../science/rare_class.md#a-retained-reference-avoids-the-rarity-dependent-cost); [rarity and evaluation costs](../science/resources.md#rarity-and-the-cost-of-a-claimed-saving); [attribution](../references/related_work.md).

### M26: A finite noisy neighborhood of the advantage

**Phase:** Narrative/innovation.

**Central question:** Which part of the advantage survives a small amount of independent prototype depolarization?

**Understanding target:** Explain the product trace-distance bound, why both learner classes can simulate the known noise, and how continuity certifies a positive gap around a concrete finite example. Distinguish this guarantee from an optimal noisy classifier or a fixed-noise large-training law.

**Dependencies and story role:** M02–M03, M05, M17, M19, M25. Tests physical robustness while retaining the exact scope of the pure-state results.

**Conceptual connection:** Full-rank noise removes the exact no-false-positive support property, so the finite robustness statement uses continuity and monotonicity rather than silently reusing the pure-state proof.

**Source pointers:** [Noise theorem and finite example](../science/noise.md); [resources: noise and scope](../science/resources.md#noise-and-scope); Watrous §3.1.1 and §2.2.1 (trace-distance decisions and channels), via the [verified textbook route](WATROUS_BRIDGE.md#verified-textbook-route).

### M27: Pay for a concrete realization

**Phase:** Narrative/innovation.

**Central question:** What must be supplied and implemented to turn the statistical optimum into an actual prediction?

**Understanding target:** Account for original specimens, persistent quantum storage, symmetric-support compression, known preprocessing, measurement synthesis, classical record precision, ancillas, and an implementation-error budget. Treat logarithmic coherent storage as an upper bound, not a proved minimum.

**Dependencies and story role:** M03, M08–M09, M18, M23, M25–M26. Joins the statistical results to a paid implementation without promoting them to a runtime crossover.

**Conceptual connection:** Efficient support compression does not erase input handling or physical storage time; an implementation error larger than the desired risk gap can erase the operational distinction.

**Source pointers:** [Resource table](../science/resources.md#what-is-paid); [finite records](../science/resources.md#statistical-attainability-and-finite-records); [compression and paid realization](../science/resources.md#coherent-compression-and-a-paid-realization); [anchor bridge](WATROUS_BRIDGE.md).

### M28: Subtract inherited results to identify the contribution

**Phase:** Narrative/innovation.

**Central question:** What changes after the earlier balanced classifier, programmable discriminator, information bounds, and comparison test are credited?

**Understanding target:** Distinguish inherited ingredients from the exact prior-dependent classical-sufficiency boundary, complete one-copy classical curve, quantitative plateau, fixed-prior order result, and optimal rarity-dependent classical sample cost.

**Dependencies and story role:** M13–M15, M17–M19, M23–M27. Integrates the mathematical components into a scientifically attributed claim rather than counting every known tool as a discovery.

**Conceptual connection:** The contribution is a boundary and cost of converting quantum training into a classical record as deployment weights change. It does not replace the earlier quantum optimum or claim a new universal comparison protocol.

**Source pointers:** [Related-work comparison](../references/related_work.md); [scientific route](../science/README.md); [interpretation](../science/interpretation.md); [single-anchor bridge](WATROUS_BRIDGE.md).

### M29: Keep the regimes and limits consistent

**Phase:** Narrative/innovation.

**Central question:** Which conclusions can be combined, and which answer different limiting questions?

**Understanding target:** Reconcile fixed finite training, a certified small-tilt interval, fixed interior imbalance with growing training, vanishing minority probability at a relative-risk target, and finite noise. Preserve $`n=0`$ and trivial-prior endpoints, the majority-threshold tie, one-test consumption, and the open exact asymptotic coefficient.

**Dependencies and story role:** M12, M15, M17, M19–M28. Checks the complete account before final synthesis by making each conclusion's quantifiers and resource promises explicit.

**Conceptual connection:** Exact finite equality, an order law at fixed prior, and a rarity-dependent sample saving are mutually consistent because their assumptions and limiting orders differ.

**Source pointers:** [Model conventions](../science/model.md#notation-and-endpoint-conventions); [three limits](../science/interpretation.md#three-limits-answer-different-questions); [asymptotic scope](../science/asymptotic.md#statement-and-limiting-order); [rare-class scope](../science/rare_class.md#resources-and-scope); [noise](../science/noise.md).

### M30: The complete class-imbalance story

**Phase:** Narrative/innovation.

**Central question:** Why does a known change in deployment prevalence alter the value of retained quantum training?

**Understanding target:** Give one connected explanation from unknown quantum specimens and the training/test cut through balanced sufficiency, signed-sector activation, optimal classical risk, asymptotic and rare-class costs, and paid finite robustness. State both the established consequence and the limits that remain.

**Dependencies and story role:** M13–M29. Synthesizes the narrative as a single project-level understanding target rather than adding another theorem or assessment.

**Conceptual connection:** The same balanced training library can be sufficient as a classical record for one decision weighting and insufficient for every unequal interior weighting. The size and practical meaning of the loss must then be read in the appropriate quantitative regime.

**Source pointers:** [Interpretation](../science/interpretation.md); [scientific route](../science/README.md); [model](../science/model.md); [resources](../science/resources.md); [anchor bridge](WATROUS_BRIDGE.md).
