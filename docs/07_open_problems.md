# Open problems and research priorities

> **2026-11-02 sparse-CSP-to-HOM transfer RESOLVED:** Our original HOM paper arXiv:2607.09377 Section 4 already gives a pinning-frame encoding; direct inspection shows its construction works for ALL sparse binary CSP, not only the bipartite 3-regular source used for old ETH hardness. See [exact reduction audit](35_general_sparse_binary_csp_to_2deg_hom_linear_source.md). It yields a simple ordinary HOM target of degeneracy at most 2, size O(v+m+vq+mq²), with source n=255v+257m+251. Therefore the new unproved randomized no-single-exponential sparse-CSP hypothesis rNSE-SCSP(c) IMPLIES no randomized 2^{O(n)}poly(h) HOM algorithm for degen(H)<=2 and h=O(n^{2c+1}). Remaining research should focus on verifying/refuting rNSE-SCSP(c), NOT designing another linear list-removal gadget. This lower bound remains conditional on that unproved hypothesis.\n\n> **2026-11-02 branch triage:** SPACH and CEH (no \(q^{o(k)}\) algorithm for sparse polynomial-alphabet binary CSP, including a fixed cubic expander) are **conditionally refuted by the full Boolean tensor-contraction theorem** and are CLOSED as hardness assumptions under that premise. Likewise, an \(O(s/\log s)\)-size polynomial-alphabet Circuit-SAT-to-sparse-CSP compiler is incompatible with the same theorem **and** a no-\(2^{o(s)}\) Circuit-SAT source hypothesis. The weaker \(o(s)\)-size compiler, dense PCC/PSCH, full-span Span-CSP, and unrelated mathematical compiler constructions are not closed by this argument. **New top priority:** audit the general tensor theorem independently and validate quantitative consequences. Details: [tensor contraction and branch triage](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).


## Priority: potential algorithmic collapse via characteristic-two weighted counting
Audit whether the actual October 2026 fixed-width counting SAT technique extends to field-valued weighted counts in characteristic two without superlinear auxiliary Boolean-variable overhead. If so, exploit the nullspace parity identity and isolation to obtain randomized subexponential decision algorithms for sparse (co)graphic full-span feasibility. This is NOT yet proved.

## Priority: rank-circuit cost
Seek a uniform bounded-fanin Boolean circuit for selected-edge forestness/connectedness/full-rank on sparse graphs of size o(n sqrt(log n)/(log log n)^2). Distinguish gate cost from word operations and field operations.

## Priority: fine-grained completeness
Identify a canonical restricted rank problem with O(n)-blowup reductions *both directions* against cubic HC, bounded-degree FVS and connectivity/covering variants. Hardness of a generic class does not propagate through reverse-only encodings.

## Priority: genuine ETH replacement
Define the desired computational parameter and quantitative speedup. Prove that fast Span algorithms imply sufficiently fast SAT for arbitrary polynomial-size circuits and *then* apply an appropriate algorithms-to-circuit-lower-bounds theorem. Otherwise the project yields a useful graph source of hardness but not the requested unconditional win-win.

## Additional stress tests
- compressed group activations for general Set Cover with universe-size parameter;
- arbitrary CNF with variable-count parameter;
- preservation under dense-to-sparse transformations;
- special cases planar, bipartite, bounded-degree and bounded treewidth;
- explicit examples where simple encodings have logarithmic/superlinear overhead;
- one-sided randomized decision via isolation and sparse XOR hashing.

## Iteration protocol
For each branch maintain: proved lemma or counterexample, exact parameter audit, conditional consequences, next concrete theorem. Mark all new statements PROVED, CONDITIONAL, CONJECTURED or OPEN.