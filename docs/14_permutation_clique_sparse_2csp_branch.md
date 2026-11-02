# Branch P — Permutation Clique to sparse polynomial-alphabet CSP

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
