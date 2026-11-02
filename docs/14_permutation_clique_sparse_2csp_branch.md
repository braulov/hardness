# Branch P — Permutation Clique to sparse polynomial-alphabet CSP

> **2026-11-02 CONDITIONAL CLOSURE OF HARDNESS-TRANSFER TARGET.** If the *full* OpenAI Boolean tensor-contraction theorem is correct, any explicitly represented sparse polynomial-alphabet 2-CSP with \(r=k'+m'\) variables plus constraints can be solved in \(2^{O(r\sqrt{\log K})}\operatorname{poly}(K)\) when the output alphabet is \(K^{O(1)}\). Therefore, under the separately conjectured no-\(2^{o(K\log K)}\) PCC-hardness assumption, a polynomial-time PCC \(\to\) sparse 2-CSP compiler with \(r=o(K\sqrt{\log K})\), **including the O(K) stretch goal, cannot exist**: otherwise it gives a faster PCC algorithm. The downstream SPACH/rSPACH hardness claims are also conditionally refuted. **Keep the exact gadgets, PCP sampling lemmas, and structural barriers; do not claim the mathematical existence question has been disproved unconditionally.** The full tensor theorem is not part of the documented Lean scope. See [audit and branch triage](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).


**CRITICAL 2026-11-02 UPDATE:** See [the domain-uniform CSP alert](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md). A brand-new UNVERIFIED independent preprint claims a uniform q^{O(v/sqrt(log v))} deterministic algorithm for ALL bounded-degree binary CSPs. **If correct, SPACH/rSPACH as formulated here are FALSE**, and under RPCC-H no O(k)-size (indeed no o(k sqrt(log k))-size) general polynomial-alphabet bounded-degree CSP compiler exists. All earlier PCP/encoding lemmas should be viewed through this conditional algorithmic upper bound; don't present a purported compiler as SPACH evidence.


**Added 2026-11-02. Status: a concrete OPEN reduction target with known partial gadgetry, not an announced reduction.** This is related to but distinct from the older PSCH -> ordinary Clique compression program in docs/psch/.

## Why Permutation Clique first?

Permutation k x k Clique (PCC) supplies a natural n=Theta(k log k) Boolean-witness hard-source candidate: select a permutation pi of [k] and require all pairs (i,pi(i)), (j,pi(j)) to be adjacent in a given graph on [k] x [k]. The classical Lokshtanov--Marx--Saurabh 2011 ETH lower bound excluded time 2^{o(k log k)}, but once ETH is false this is not a proven current lower bound. Treat PCC-hardness as a separate conjecture if using it.

PCC reduces trivially to binary 2-CSP with k variables and domain [k] but Theta(k^2) constraints. The goal is not to redo that or merely rewrite it as log-width SAT. The **new problem is a direct, deterministic, decision-preserving reduction** from PCC to an explicitly represented cubic 2-CSP with:

- stretch goal: v=O(k), m=O(k), q=k^{O(1)}, max degree 3 (ideally 3-regular bipartite);
- weaker exploratory goal: v,m=O(k polylog k), q=k^{O(1)} (useful compression, but does not give full 2^{o(v log v)} hardness from PCC-hardness);
- polynomial-in-k construction and relation table size; preserve YES/NO for every input graph, not only some planted or structured subclass;
- measure all auxiliary variables and equality edges; prohibit hiding arbitrary Boolean circuits in unnamed oracles.

If the stretch goal holds, PCC-hardness implies SPACH for the target cubic class (assuming the output is in the exact subclass chosen for SPACH), yielding a path to conditional lower bounds for sparse CSP and potentially HOM with separate checked target reductions. This does not follow merely from CSP -> log-SAT.

## What is already solved / prior work in this repository?

The permutation constraint pi being bijective is exactly AllDifferent(a_1,...,a_k). In docs/psch/2026-11-02_full_checkpoint_v7.md an explicit Beneš switching network existentially enforces AllDifferent with O(k log k) binary constraints, q=k^{O(1)}, maximum degree <=3. This is a **good near-linear construction**, but the full input still has Theta(k^2) independent compatibility tests R_ij(a_i,a_j), each depending on arbitrary edges of the PCC input.

The earlier PSCH checkpoint also explores sparse gauge/transport residuals, path consistency, Ferrers relations, rectangle decompositions, and exact projected-solution barriers. Those positive examples restrict the structure of pairwise relations and do not solve the arbitrary PCC case. A universal compiler may use existential variables and need not preserve all projected witness tuples, only satisfiability; do not use fixed deterministic encodings as unconditional barriers.

## Method-specific lower bound for naive embeddings (elementary)

Suppose the complete k-vertex constraint graph is connected-embedded into an auxiliary constraint graph H with |V(H)|=O(k), maximum degree <=3 and vertex depth d: each original vertex is represented by a connected bag, each original edge by two intersecting or adjacent bags, each H-vertex belongs to <=d bags. An H-vertex can witness at most binom(d,2) pairs, and an H-edge at most d^2 bag pairs. Since |E(H)|=O(k), H can witness only O(k d^2) original edges. For K_k this must be Omega(k^2), so d=Omega(sqrt(k)). Marx-style alphabet packing would use [k]^d, not polynomial alphabet. This does **not** exclude other reductions which do not pack individual source labels along connected bags.

For a bounded-degree source graph G with N=Theta(k log k) vertices, the 2024 expander embedding gives depth O(N log k/k)=O(log^2 k), likewise yielding quasipolynomial alphabet for constant source alphabet. Worst-case depth lower bounds by Alon--Marx explain why one should not expect to save this log via a different routing of the same embedding type.

## Three proposed experiments (in priority order)

**P1. Separate bijection from arbitrary compatibility.** Take the Beneš construction as a fixed exact AllDifferent interface; formalize a black-box residual predicate Comp(pi)=AND_{i<j} R_ij(pi(i),pi(j)). Can a constant-domain-size (O(log k) bits per auxiliary variable) *existential* proof of Comp be verified with O(k) binary constraints? Look for a circuit/proof/communication argument that proves or refutes this. Do not count the existing O(k log k) Beneš nodes as O(k).

**P2. Structured classes with explicit and auditable savings.** Restrict the forbidden-edge matrices to unions of r Ferrers/threshold relations, bounded-size common low-rank factors, or consistent permutation-transport plus O(k) exceptional pairs. Try to realize O(k r) cubic constraints and polynomial alphabet, with exact YES/NO; then identify precisely whether r can be sublinear/polylog for arbitrary PCC graphs (there is no such general theorem). Negative representation bounds apply only to the named representation model.

**P3. Analyze the general compression barrier.** A direct source-row gadget for each pair costs Theta(k^2); an embedding into O(k)-vertex cubic H costs depth Omega(sqrt(k)). Explore decision-only existential projection, low-query verification of a full arbitrary adjacency matrix, and whether randomization can yield a one-sided reduction without error/soundness gaps. Quantify time for any deterministic derandomization, distinguish exact from high-probability constraints.

## Consequence table

| Established / assumed | What follows |
|---|---|
| PCC -> LogSAT-A/B, n=Theta(k log k), w=O(log k), M=O(k^4) | PROVED simple reduction; no cubic sparsity |
| PCC-hardness (new conjecture) | Conditional no-2^{o(n)} algorithms for LogSAT-A and LogSAT-B |
| PCC -> cubic CSP, v=O(k), q=k^{O(1)} | OPEN; if proved plus PCC-hardness, conditional SPACH hardness in corresponding class |
| PCC -> cubic CSP, v=O(k polylog k), q=k^{O(1)} | OPEN weaker compiler; incurs potentially decisive exponent loss |
| AllDifferent -> Beneš O(k log k) CSP | Existing exact existential subroutine, *not* arbitrary PCC adjacency compression |
| PSCH for ordinary Clique, no 2^{o(k/log k)} | Does NOT by itself imply PCC's no 2^{o(k log k)} hardness |


## Quantitative loss from near-linear (rather than linear) compilation

If a compiler has v'=Theta(k log^a k) variables and polynomial alphabet, an assumed PCC lower bound at scale k log k only rules out solvers running in 2^{o(v'/log^{a-1} v')} on its image (for fixed a>=1), **not** the desired 2^{o(v' log v')} sparse-CSP solvers. For a=1 this becomes a no-2^{o(v')} statement. Thus a Beneš-sized O(k log k) compiler would be meaningful but not enough for SPACH at its intended exponent. The converse numerical implications of a bound v'=O(...) should always be written with an actual lower/upper relation for v' and the input k; padding can normalize the size when valid.

## Algebraic residual to test

Let X_{i,a} be the one-hot indicator that the row-i choice is a. Define B_{(i,a),(j,b)}=1 for an invalid pair of selected vertices (including repeated columns), and zero otherwise. The nonnegative integer quadratic obstruction

    Q(X) = sum_{i<j} sum_{a,b in [k]} B_{(i,a),(j,b)} X_{i,a} X_{j,b}

vanishes exactly when the one-hot choices form a Permutation Clique. Over any prime p>k^2, Q(X)=0 mod p is still equivalent because Q(X) is an integer in [0,binom(k,2)]. This is an exact encoding, not a small constraint compiler. For an arbitrary input the associated (k^2)x(k^2) coefficient matrix may have rank Omega(k^2), so simple generic low-rank factorization cannot directly produce O(k) local interactions. The possible useful structure would have to arise from existential compression and permutation consistency, not an assumed small rank of every adjacency matrix. Compare the global-quadratic-form line in the HOM research notes, while keeping the distinct problems separate.

## Sources

- Lokshtanov, Marx, Saurabh, *Slightly Superexponential Parameterized Problems*, SODA 2011: https://epubs.siam.org/doi/10.1137/1.9781611973082.60
- Karthik C. S., Marx, Pilipczuk, Souza, *Conditional lower bounds for sparse parameterized 2-CSP*, SOSA 2024: https://arxiv.org/html/2311.05913v3
- Local PSCH research checkpoint: docs/psch/2026-11-02_full_checkpoint_v7.md
- Complementary log-SAT/SPACH note: docs/13_log_width_sat_and_polynomial_alphabet_csp.md

## Follow-up iteration: quadratic form and interface barriers

See [`15_quadratic_form_and_alldifferent_interface_barriers.md`](15_quadratic_form_and_alldifferent_interface_barriers.md) for elementary proofs of (a) rank-r incompatibility compilation with O(k(r+1)) degree-3 binary CSP constraints (without permutations), (b) high collision rank k(k-1) despite the O(k log k) Beneš AllDifferent gadget, (c) a 2^{Omega(k)}-state fooling-set lower bound for even *nondeterministic* sequential permutation verifiers, and (d) treewidth Omega(k/log q) for polynomial-alphabet exact-projection AllDifferent encodings with designated row terminals. None settles unrestricted PCC. The correct priority is to seek a nonsequential expander-like existential interface, not one polynomial-size running checksum.

## Follow-up: efficient quotient-rank certificate and routing barrier

[`16_permutation_mixed_difference_rank_and_routing.md`](16_permutation_mixed_difference_rank_and_routing.md) provides a polynomial-time computable mixed-difference invariant H_B=T^T(B_AB+B_BA^T)T with r_perm(B)>=rank(H_B)/2. An explicit admissible 0/1 PCC obstruction has r_perm(B)=Omega(k^2), so even using ALL quadratic permutation identities does not make every obstruction low-rank. Literal routing of k labels through a bounded-degree network with constant edge congestion requires Omega(k log k) edges, matching the Beneš order. Both are restricted model barriers; arbitrary existential compression remains OPEN.

## Latest iteration: short noninteractive proof-test interface

See [`17_pcp_bridge_gap_sampling_and_logsat.md`](17_pcp_bridge_gap_sampling_and_logsat.md). An exact O(k)-test two-query noninteractive proof system with O(k) symbols over poly(k) alphabet is equivalent (after degree reduction) to the desired O(k)-constraint cubic CSP compiler. Existing interactive PCPs/IOPs do not directly yield this object. Robust gap-NO instances admit randomized O(k log k/delta)-constraint subsampling plus Beneš, not linear/general deterministic compression. Important correction: the explicit high-r_perm example from note 16 already has a matching constraint graph, so its high rank is a *failure of rank as a compression-cost proxy*, not a hard dense instance.

## Randomization-first next target (2026-11-02)

**Randomized reductions are as welcome as deterministic ones.** [`18_randomized_low_soundness_pcp_to_linear_csp.md`](18_randomized_low_soundness_pcp_to_linear_csp.md) establishes an exact sampling theorem: if a nonadaptive two-query PCC PCP has O(k) proof positions, poly(k) alphabet and NO soundness k^{-Omega(1)}, then O(k) random tests yield a degree-3 O(k)-constraint CSP with one-sided correctness. More generally, constant soundness suffices when the range space of all proof failure sets has VC dimension O(k), by epsilon-net sampling. No generic PCC PCP satisfying either condition is known. Distinguish randomized PCC-hardness from deterministic PCC-hardness and from PSCH; for randomized reductions only randomized lower-bound assumptions transfer.

## VC route reality check (2026-11-02)

See [`19_vc_dimension_permutation_tests_and_algebraic_dichotomy.md`](19_vc_dimension_permutation_tests_and_algebraic_dichotomy.md). Native PCC pair tests can have VCdim Theta(k log k), even restricted to permutation witnesses, proved using a random Hall-system construction. AllDifferent pair-disequalities have VCdim k-1, but pigeonhole NO instances have gap only Theta(k^-2). Affine polynomial-zero tests have VCdim at most the rank of their polynomial span, but equality acceptance has a trivial basis sparsifier and nonzero acceptance over large fields fails constant gap. The PCP should combine nonlinear hard predicates and a low-VC algebraic consistency layer while controlling EVERY malformed proof; no universal compiler is claimed.

## New two-layer quantitative audit

[`20_two_layer_affine_nonlinear_pcc_audit.md`](20_two_layer_affine_nonlinear_pcc_audit.md) formalizes the input-independent affine-code / input-dependent nonlinear-tests model. Two-query affine consistency has only one free field symbol per connected component, so a positive-rate solution code has O(1) distance. Arity-three consistency checks CAN be compiled into cubic binary CSP at O(k) cost. A permutation-specific solution-set counting argument using k/2 filler rows yields tQ²=Omega(k^4) for exact witness projection (so O(k) tests require Q=Omega(k^1.5)); this says nothing against decision-only randomized compiler. Under RPCC-H, target graphs cannot have universally sublinear treewidth. The actual globally sensitive nonlinear compatibility interface remains OPEN.

## Fixed-encoding barrier strengthened to quadratic (2026-11-02)

See [`21_oblivious_two_query_pcc_quadratic_barrier_and_2026_ltc.md`](21_oblivious_two_query_pcc_quadratic_barrier_and_2026_ltc.md). For ANY fixed encoding E:S_k->[k^C]^ell and t fixed two-coordinate proof tests whose **relation tables may depend on the whole input graph**, exact per-permutation validity on all PCC inputs requires t=Omega_C(k²). Single-deleted source edges force some two-symbol view to reveal both selected rows/columns; a two-symbol view fixes only O(C) permutation entries on average. Randomized exact-solution-preserving versions obey the same bound. This is strictly stronger than the table-bit counting bound for this **narrower oblivious model**. It does NOT rule out input-adaptive proof encodings, existential auxiliaries, input-adaptive test positions, or decision-only randomized compilation. First–Lazarovici APPROX/RANDOM 2026 good two-query LTCs remove the old nonlinear-code concern but do not break this fixed-encoding obstruction.
