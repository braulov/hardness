# Clique compression and circuit lower bounds

The two source hypotheses in the notebook are different and remain **OPEN**:

* **PSCH:** no uniform deterministic algorithm for ordinary k-Clique on every graph with N≤k² vertices in 2^{o(k/log k)}poly(N) time.
* **RPCC-H:** no bounded-error randomized algorithm for k×k Permutation Clique in 2^{o(k log k)}poly(k) time.

Neither is established here. Ordinary Clique, multicolored Clique, and Permutation Clique are not interchangeable at these scales. A fast general algorithm handles a subclass; hardness of the general problem does not automatically imply hardness of that subclass. Likewise deterministic hardness does not justify a randomized reduction's hardness consequence.

## What direct reductions actually buy

Ordinary k-Clique is binary CSP on k variables, domain N≤k², and binom(k,2) adjacency constraints. The same instance is HOM(K_k,H). Thus PSCH only transfers the 2^{o(k/log k)} prohibition, which does not exclude 2^{O(k)}. Splitting occurrences to degree three costs Θ(k²) variables, losing another square root in the parameter.

Subdividing every edge **once** gives K_k⊆H iff S(K_k)⊆S(H) for k≥4: pattern branch vertices have degree at least three and must map to original host vertices; subdivision vertices force the corresponding host edges. This works for induced embeddings too, by choosing just the subdivision vertices corresponding to clique edges. Both graphs are 2-degenerate, but the pattern has Θ(k²) vertices. The transferred PSCH prohibition is only 2^{o(√n/log n)}. It gives no Hamiltonian-cycle lower bound: the hard pattern is a subdivided clique, not a cycle.

## Corrected SAT-to-Clique starting point

The historical sketch grouped **variables** and assumed pairwise consistency sufficed for 3-clauses. A clause meeting three blocks need not be enforceable by those pair checks; even x∨y∨z has full binary projections. The stated quantitative starting implication can instead be justified by grouping **clauses**.

For m clauses of width at most three, put b=floor(log₂m/6) clauses in each group (handle bounded m separately). Each group uses at most 3b variables and has at most 2^{3b}≤√m local satisfying assignments. Make these assignments the vertices of one independent color class; join assignments in different groups iff they agree on shared variables. With k=ceil(m/b)=Θ(m/log m), there are at most k² vertices for large m. A k-clique picks one assignment per class, and pairwise consistency produces a global satisfying assignment; conversely restrict any satisfying assignment to the groups. Empty classes correctly encode UNSAT.

A hypothetical FastClique algorithm at the PSCH-negating scale therefore solves this formula in 2^{o(m/log²m)}poly(m) time. This is a **conditional algorithmic implication**, not a circuit lower bound by itself. The replacement proof is explicit; it does not validate the original variable-grouping argument.

## The short-verifier route

Suppose a nonadaptive two-query verifier for PCC has ℓ=O(k) proof symbols over Q=k^{O(1)}, polynomial-time samplable tests with explicit polynomial-size tables, perfect completeness, and soundness s(k) on every NO proof. Sampling

$$
t=\left\lceil\frac{\ell\ln Q+\ln6}{\ln(1/s)}\right\rceil
$$

tests preserves a YES proof surely. On NO inputs, a union bound over Q^ℓ proofs bounds false satisfaction by Q^ℓs^t≤1/6. The sampled CSP has O(ℓ+t) size after occurrence splitting, degree at most three, and polynomial alphabet. This proves the sampling lemma, **not existence of the verifier**.

If s=o(1), the size is O(k+k log k/log(1/s))=o(k log k). A uniform family of randomized single-exponential sparse-CSP solvers covering the resulting fixed domain exponent would then contradict RPCC-H. Existing PCP theorems measured in input/formula length do not automatically give O(k) symbols measured in this witness parameter.

Under both RPCC-H and the [external tensor premise](csp-hom.md#external-algorithm-status), soundness with log(1/s)=ω(√log k) is too strong: the sampled instance and the conditional CSP upper bound would already give 2^{o(k log k)} PCC. The remaining target is, for example, s=1/log k, or a comparable subconstant soundness within log(1/s)=O(√log k). These are necessary compatibility calculations, not evidence that the desired verifier exists.

## Current barriers and useful normal forms

The [fixed-view, all-fields, and source-degree barriers](../barriers/encoding.md) exclude several exact or low-degree encodings. The [structured factor algorithms](../results/permutation-factors.md) show that general relation matrices can sometimes be compressed much more than their ordinary rank suggests. The missing step is a universal construction preserving only existence with enough parameter savings.

Two historical normal forms remain useful as formulations, not breakthroughs:

* A single universal selector can check arbitrary dense CSP using an ∃x∀t∃state tree-CSP with O(k) constraints: propagate (t,a,b) along a path and check the selected endpoints. Removing the universal quantifier is exactly the unresolved issue; ordinary tree-CSP DP cannot be applied across that prefix.
* Beneš routing puts any degree-three CSP on one fixed degree-three skeleton with O(v log v) variables and polynomial alphabet. The topology can be fixed at a logarithmic cost; the relations still depend on the input. This is not an O(v)-size compiler onto one prescribed expander.

See the [selector proof](https://github.com/braulov/hardness/blob/c994435b692c37958eeff2c997188603dcaeddb6/docs/psch/2026-11-02_universal_selector_qcsp.md) and [fixed-topology proof](https://github.com/braulov/hardness/blob/c994435b692c37958eeff2c997188603dcaeddb6/docs/psch/2026-11-02_universal_fixed_topology_csp.md). The latter uses standard rearrangeability of the Beneš network, not a new routing theorem. Algebraic divisibility, Sidon/Walsh normal forms, and the CEH matching-compiler variants are retained in history; none supplies the missing compiler.

## Circuit lower bounds: unresolved bridge

The ambition is a new strong lower bound, such as NEXP⊄P/poly, from a sufficiently fast algorithm for a natural restricted problem. The [Williams algorithms-to-lower-bounds framework](https://www.cs.cmu.edu/~ryanw/improved-algs-lbs2.pdf) requires an appropriately quantified circuit-SAT speedup; a speedup only for sparse CNF or occurrence-expanded programs is not enough.

The original quantitative E^NP circuit-size sketch and the claimed route to a superpolynomial general lower bound are **UNVERIFIED/OPEN**, respectively. No complete uniform reduction from arbitrary polynomial-size circuit checkers with controlled **original input count** has been retained as proved. Adding a dummy rank constraint to Circuit-SAT does not create a meaningful new bridge.

The first tasks are to state the exact checker class and circuit-size quantifiers, then charge its input-efficient compilation. For the sparse-CSP branch, the first task is instead a concrete short verifier or a decision-only compatibility factorization. Do not combine these two missing theorems into an asserted win-win.
