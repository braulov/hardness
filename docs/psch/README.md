# PSCH — Polynomial-Size Clique Hypothesis

**Research notebook / archive.** Imported from the November 2, 2026 research discussion; last cumulative checkpoint: v7. This is a research program, **not** a paper or a collection of externally verified theorems. Claims marked "PROVED" in the checkpoint are internal proof sketches or arguments and still need an independent mathematical and novelty audit before citation.

## Hypothesis (working formulation)

**PSCH** proposes that there is no deterministic uniform algorithm for ordinary (k)-CLIQUE on graphs with (N\le k^2) vertices running in (2^{o(k/\log k)}\operatorname{poly}(N)) time. Quantifiers, uniformity, and whether to allow randomized algorithms must be fixed rigorously.

Ordinary (k)-CLIQUE and (k\times k) *multicolored* Clique must not be silently identified: a fast ordinary Clique algorithm handles the multicolored subclass, but a reduction valid **only** on that subclass does not establish hardness for all ordinary Clique instances.

## Two separate ongoing branches

**A. Failure of PSCH and circuit lower bounds.** Attack (mathrm{FastClique}\Rightarrow mathrm E^{\mathrm{NP}}\not\subseteq \mathrm{P/poly}), using Williams-style SAT-to-circuit transfer, easy witnesses, locally checkable tableaux, and alternative non-black-box approaches. A quantitative (n\log^2 n) circuit lower-bound transfer is recorded as **audit needed**, not certified. Universal witness-checker compression faces a Dell–van Melkebeek-style obstacle. The full one-pass research brief is [here](../../prompts/psch_williams_one_pass_2026-11-02.md).

**B. Consequences of PSCH for 2-CSP, HOM, Subgraph Isomorphism and related problems.** The direct Clique-to-dense-CSP reduction is standard. The (1)-subdivision construction gives conditional lower bounds for 2-degenerate Subgraph Isomorphism (including the parameter loss). The hard open goal is a **deterministic, decision-preserving** compiler for ordinary (k)-CLIQUE with (N\le k^2) into binary CSP of maximum degree (3), (m=O(k\operatorname{polylog}k)) constraints and alphabet (k^{O(1)}).

## Main research experiments in branch B

- Exact sparse representations via algebraic rank, Boolean rectangle covers, threshold/Ferrers constraints, and global synchronizations/permutation transports (structured subclasses only).
- Lower bounds for fixed linear and nonlinear code/check topologies, and information counting for exact projected-solution representations. These **do not** rule out arbitrary decision-only reductions with existential auxiliary variables.
- Sum-check and PCP approaches: short interaction is not the same as a short deterministic CSP certificate; short constant-gap PCP plus random sampling yields a **randomized** CSP transformation, not automatically a deterministic consequence of PSCH.
- A dense high-rank NP-hard planted-sync example with (O(k))-constraint sparse compilation: illustrative, not a universal reduction.
- Beneš permutation networks: existentially compile (mathrm{AllDifferent}) to (O(k\log k)) binary constraints with polynomial alphabet; combined with path-adjacency, gives a Hamiltonian Path model with (\Theta(k^2)) pairwise inequalities but a short equivalent existential encoding.

**Not established:** universal dense-Clique-to-sparse-CSP compilation; PSCH-based prohibition of single-exponential 2-degenerate HOM; (mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{P/poly}) from FastClique; an improved HC algorithm. The Hamiltonian Path construction is an encoding, **not** an algorithmic speedup.

## Where to continue

1. [Full chronological checkpoint v7, November 2](2026-11-02_full_checkpoint_v7.md) — all recorded arguments, limitations, source links, corrections, and open problems.
2. [Research brief for branch A](../../prompts/psch_williams_one_pass_2026-11-02.md).


3. [Universal-selector quantified CSP compilation (Nov 2)](2026-11-02_universal_selector_qcsp.md) — a precise `exists-forall-exists` tree-CSP with O(k) constraints for *arbitrary* dense binary CSP, identifying one universal index as the exact obstacle; not a solution for unquantified CSP.

4. [One-variable divisibility and quotient-circuit barrier](2026-11-02_univariate_remainder_and_quotient_barrier.md) — exact ordinary-Clique identity, scalar-trace caveat, and an unconditional lower bound for *explicit quotient* arithmetic circuits; universal compilation remains open.

5. [Planar exact-extension separator barrier](2026-11-02_planar_extension_separator_barrier.md) — unconditional Ω(k²/log²Q) lower bound for planar exact projected-solution encodings of a sparse expander-port CSP, plus a separate PSCH-conditional decision-only tradeoff.

6. [Decision-only bit-budget lower bound](2026-11-02_decision_only_bit_budget.md) — from Dell–van Melkebeek: no subquadratic-bit universal compression of ordinary Clique with N≤k² unless NP⊆coNP/poly; applies to near-linear CSP even with arbitrary global relations, and to succinct relation descriptors independently of alphabet size.

7. [No-go for polynomial catalogues of precompiled tests](2026-11-02_precompiled_test_catalogue_barrier.md) — m·d≥binom(k,2) for low-degree Boolean per-test acceptance, and M≥k^{Ω(k/√m)} total DNF terms for fixed-skeleton existential CSP compilers, even with nonmonotone source-edge literals.

8. [Davenport zero-sum barrier for global linear sketches](2026-11-02_davenport_linear_sketch_barrier.md) — for arbitrary-existential CSP compilers whose local acceptance predicates depend on r input-oblivious affine F_p sketches, m·r·(p−1)≥binom(k,2); complements the DNF catalogue obstruction.

9. [Universal deletion-certificate cover and a P-time counterexample](2026-11-02_universal_certificate_cover.md) — for any deterministic decision-only compiler, selected local checks must cover all clique-edge deletion certificates; a polynomial-time connected-component predicate simultaneously saturates the bound and needs exponentially many DNF terms.

10. [Fixed-topology Beneš normal form](2026-11-02_universal_fixed_topology_csp.md) — any Δ≤3 binary CSP on n variables can be routed to one fixed Δ≤3 skeleton of O(n log n) constraints with alphabet Q^4; the PSCH target may assume input-independent output topology up to one logarithmic factor.

11. [Universal Sidon-XOR/Walsh normal form](2026-11-02_sidon_xor_walsh_normal_form.md) — encode any graph by an XOR-invariant kernel on O(N²) Boolean-group elements; prove near-full Fourier support for random graphs and Ω(N²/log N) support for every extension on most inputs; exact quadratic clique identity but no sparse-CSP compiler.

11. [Nguyen/PCC critical compression window and PCP soundness threshold](../35_domain_uniform_csp_and_critical_pcc_pcp_window.md) — domain-uniform fixed-arity and cyclomatic corollaries; under RPCC-H and Nguyen the viable compression exponent is 1/2≤β<1, with critical PCP soundness exp(-Θ(√log K)).

The repository's older [graphic-rank/span project](../../README.md) is a related but distinct research program. Keep separate statements and assumptions separate.

## Audit priority

Before publication, verify the exact quantitative Williams implication, all proof details and novel-claim priority, reductions between ordinary and multicolored Clique, and the complexity of all table-encoding gadgets. Preserve "conditional", "model-restricted", and "open" labels when reusing this material.
