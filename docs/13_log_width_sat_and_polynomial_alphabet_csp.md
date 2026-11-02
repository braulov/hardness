# Sparse polynomial-alphabet 2-CSP and two versions of log-width SAT

**CRITICAL 2026-11-02 UPDATE:** See [the domain-uniform CSP alert](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md). A brand-new UNVERIFIED independent preprint claims a uniform q^{O(v/sqrt(log v))} deterministic algorithm for ALL bounded-degree binary CSPs. **If correct, SPACH/rSPACH as formulated here are FALSE**, and under RPCC-H no O(k)-size (indeed no o(k sqrt(log k))-size) general polynomial-alphabet bounded-degree CSP compiler exists. All earlier PCP/encoding lemmas should be viewed through this conditional algorithmic upper bound; don't present a purported compiler as SPACH evidence.


> **STATUS UPDATE — 2026-11-02: SPACH / rSPACH CONDITIONALLY REFUTED; ARCHIVED AS HARDNESS HYPOTHESES.** The general Boolean tensor-contraction theorem stated in OpenAI's October 25, 2026 manuscript, if correct, gives deterministic \(q^{o(v)}\operatorname{poly}(L)\) exact counting on **all** sparse explicit binary CSPs with \(q=v^{\Theta(1)}\); hence both the deterministic and randomized SPACH hypotheses as defined below are false under that external theorem. The newer result is NOT covered by the specifically documented fixed-width CNF Lean formalization. **Do not use SPACH to deduce no-fast-LogSAT, CEH, or HOM hardness while accepting the full tensor theorem.** The definitions, elementary reductions, and open dense-PCC/LogSAT questions are preserved as historical mathematical notes. Full proof/parameter audit: [tensor contraction and branch triage](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).


**Research note, 2026-11-02. Status: definitions and elementary reductions PROVED; hardness assumptions CONJECTURED; dense-to-sparse compilation OPEN.** This is separate from Sparse (Co)Graphic Span-CSP and from PSCH. Do not treat claimed October 2026 fixed-width #SAT results as externally settled without an audit.

## Definitions and parameters

Let a binary CSP instance have v variables, a common explicit domain [q], m binary constraints with explicitly listed allowed/forbidden pairs, and input bit length L. For sparse instances m=O(v), the explicit representation has size L=poly(v,q) (typically O(m q^2 log q)). We may demand a simple bipartite maximum-degree-3 or 3-regular constraint graph, but the exact version must always be stated.

**Sparse Polynomial-Alphabet CSP Hypothesis (SPACH; candidate).** There exists a fixed constant c>=1 such that binary 2-CSP on v variables, q=ceil(v^c), m=Theta(v), and maximum degree at most 3 (possibly the stronger 3-regular bipartite restriction) has **no uniform deterministic** algorithm of running time 2^{o(v log v)} poly(L). This is a proposed hardness hypothesis, not an ETH consequence. A randomized analogue must be stated separately. The choice between max-degree-3 and 3-regular bipartite is an unresolved strength distinction, and exact regularization must be checked with parameter bookkeeping.

An equivalent running-time scale in this fixed polynomial-alphabet regime is q^{o(v)} poly(L). For c variable or q<=v^c, keep explicit quantifiers rather than silently changing the hypothesis. SPACH is **not** the already existing SGR/SCGS graphic-rank conjecture.

Two distinct SAT algorithm statements:

- **LogSAT-A (variable-relative width):** For each fixed constants C,D, CNF on n Boolean variables, M<=n^D clauses, clause width <=C log(n+2), can be decided in 2^{o(n)} poly(L). The desired little-o may depend on C,D; require uniformity in n.
- **LogSAT-B (input-relative width):** For each fixed C, arbitrary explicitly written CNF on n variables, input length L, width <=C log(L+2), can be decided in 2^{o(n)} poly(L). Here L is allowed to be superpolynomial in n. B is a strictly broader *promise class* than A, although no separation of the corresponding algorithmic statements is asserted.

Avoid the casual statement that failure of B proves FPT=W[1]. The immediate established consequence is an N^{o(k)} poly(N) algorithm for unrestricted k-CLIQUE; this does not by itself exhibit an f(k)N^{O(1)} algorithm.

## Exact elementary lemma: binary CSP -> CNF

Take b=ceil(log_2 q) bits per CSP variable. For each forbidden pair (a,c) of a relation on variables x,y, add the clause '(x != a) OR (y != c)' where each inequality expands into b Boolean literals. For each unused bit code z>=q, add a width-b clause forbidding x=z. Then:

- n = v b original Boolean bits, no existential auxiliary bits;
- width <= 2b;
- number of clauses M <= m q^2 + v(2^b-q);
- decision equivalence and exactly one valid Boolean assignment per original CSP assignment (parsimonious encoding);
- construction polynomial in the explicit relation-table input size.

If q=v^{Theta(1)} and m=O(v), this is polynomial-size LogSAT-A with n=Theta(v log v) and width O(log n); thus it also lies in LogSAT-B. Therefore a universal algorithm for A (or B) would violate SPACH. **Implication of assumptions:** SPACH => no such algorithm for A and B. The converse does not follow because CSP -> SAT is the wrong reduction direction for transferring SAT hardness to sparse CSP.

For arbitrary explicitly represented q (including exponential q), the same reduction lies in LogSAT-B, since width O(log q)<=O(log L), but may not lie in LogSAT-A.

## Reverse direction: CSP -> multicolored Clique

Create v independent color classes, each with q vertices (x,a), and connect (x,a) and (y,b) for x!=y iff the pair is allowed by their CSP constraint (or there is no constraint on x,y). A v-clique must take one vertex from each class and corresponds exactly to a CSP solution. N=vq vertices; dense graph encoding size O(v^2 q^2). Consequently a uniform N^{o(k)}-time general k-CLIQUE algorithm (with polynomial input factor) gives q^{o(v)} poly(L) for q=v^{Theta(1)}. This does not provide a parameter-preserving *dense Clique -> sparse CSP* reduction.

## The 2024 Marx et al. route: what survives and what breaks

Source: Karthik C. S., Marx, Pilipczuk, Souza, *Conditional lower bounds for sparse parameterized 2-CSP: a streamlined proof*, SOSA 2024, https://arxiv.org/html/2311.05913v3 . It gives a constructive connected embedding of an N-vertex bounded-degree source graph into a k-vertex cubic bipartite expander of depth d=O(N log k/k). The resulting alphabet is q_source^d. Alon--Marx give worst-case lower bound Omega(N log k/k) for this notion of embedding (see Theorem 1.7 in the 2024 paper).

- Starting with N=Theta(k) Boolean/constant-alphabet source variables gives d=O(log k), hence q_target=k^{O(1)}. But the **old ETH-based exponent** q_target^{o(k/log k)} corresponds only to 2^{o(k)}. The 2026 fixed-width SAT algorithm removes the old ETH contradiction.
- Attempting a source with N=Theta(k log k) independent Boolean choices, to match an intended 2^{Omega(k log k)} source lower bound, gives d=O(log^2 k), hence q_target=2^{O(log^2 k)}, typically quasipolynomial rather than polynomial. Worst-case graph embeddings cannot systematically remove this logarithm.
- The embedding and alphabet-translation theorems themselves remain combinatorially valid. Replacing 3-SAT by harder LogSAT-A/B requires a **new source structure or new compression mechanism**, not substitution of a hypothesis in the final line of the 2024 proof.

For a dense K_k source constraint graph and a max-degree-3 H with |V(H)|=O(k), any connected embedding of depth d needs d=Omega(sqrt(k)): each vertex or edge of H can witness at most O(d^2) distinct pairs of source bags, whereas K_k has Theta(k^2) distinct pairs and H only O(k) vertices/edges. Thus this specific embedding method forces q_source^d to be superpolynomial when q_source=k. This is a METHOD-SPECIFIC barrier, not a no-go theorem for all decision-preserving existential reductions.

## Two distinct hardness-source programs

1. **Permutation k x k Clique (PCC).** Each row i selects column a_i in [k]; every pair i,j checks adjacency of (i,a_i),(j,a_j) AND a_i != a_j. Direct dense 2-CSP: v=k, q=k, m=Theta(k^2). Binary encoding gives n=k ceil(log_2 k), width <=2 ceil(log_2 k), M=O(k^4). Both LogSAT-A and B contain the image. If one separately hypothesizes that PCC requires 2^{Omega(k log k)} in the no-2^{o(k log k)} sense, then neither A nor B admits 2^{o(n)} poly(L) algorithms. The old ETH-based lower bound alone is no longer a valid justification if ETH is false.
2. **SPACH for cubic sparse CSP.** A much more specialized hard core. To obtain SPACH from a PCC hardness hypothesis, prove PCC -> max-degree-3 2-CSP with v'=O(k), q'=k^{O(1)} and polynomial explicit output size. A weaker v'=O(k polylog k) does NOT transmit a 2^{o(v' log v')} lower bound of the desired strength; keep this quantitative distinction explicit. Dense CSP -> sparse CSP is the actual open reduction; CSP -> SAT has already been solved.

For PCC the all-different/permutation requirement can be existentially compiled by a Beneš switching network using O(k log k) binary constraints with polynomial alphabet (recorded in docs/psch/2026-11-02_full_checkpoint_v7.md). This does NOT compress the remaining arbitrary Theta(k^2) pairwise adjacency relations. See docs/14_permutation_clique_sparse_2csp_branch.md.

## Immediate research questions

1. Can a special LogSAT source with n=Theta(k log k) be expressed as O(k)-constraint, q=k^{O(1)} cubic 2-CSP? Identify precise structural restrictions and whether SAT -> CSP preserves n/log n groups.
2. Can PCC's arbitrary pairwise adjacency be checked through O(k) bounded-degree existential interfaces with polynomial domain? Do not confuse the easy AllDifferent compression with this step.
3. Which features of the 2024 graph-embedding proof can survive if the source is structured log-width SAT rather than constant-width bounded-degree 3-coloring? Track d, graph size, relation-table size, and quantifiers.
4. Compare the strength of PCC-hardness, SPACH, PSCH and CNF-ETH without assuming any two are equivalent.
5. Study whether algorithms on LogSAT-B yield N^{o(k)} Clique and stronger consequences; do NOT assert FPT=W[1] without an independent theorem.

References: https://arxiv.org/html/2311.05913v3 ; https://toc.cs.uchicago.edu/articles/v006a005/ ; https://epubs.siam.org/doi/10.1137/1.9781611973082.60 ; https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026

## Randomized hypothesis variant and 2026-11-02 sampling bridge

Randomized algorithms and reductions are fully allowed. Define **rSPACH** by excluding uniform bounded-error randomized 2^{o(v log v)} poly(L) algorithms on the same fixed-polynomial-alphabet cubic 2-CSP class. This is a separate, logically stronger hardness assumption than deterministic SPACH, and cannot be deduced from the latter. Define randomized PCC hardness analogously: no bounded-error randomized 2^{o(k log k)} poly(k) algorithm for arbitrary k-by-k Permutation Clique. A one-sided randomized PCC -> cubic CSP compiler plus a randomized fast CSP algorithm would produce a randomized fast PCC algorithm (after error amplification), not necessarily a deterministic one.

**Main new conditional theorem:** [`18_randomized_low_soundness_pcp_to_linear_csp.md`](18_randomized_low_soundness_pcp_to_linear_csp.md) proves that an O(k)-position, poly(k)-alphabet, nonadaptive two-query PCC verifier with inverse-polynomial NO soundness can be randomly sampled to O(k) explicit CSP constraints with cubic degree and one-sided correctness. Also a constant-gap verifier with O(k) VC dimension of the entire proof failure-set family suffices. Neither verifier is currently constructed for arbitrary PCC; this is the new research target.


## CEH fixed-topology subprogram (2026-11-02)

A separately developed candidate source is **Colored Expander Hypothesis (CEH)**: binary 2-CSP with polynomial alphabet on one predetermined cubic expander for each parameter size. This is stronger as a *hardness assumption* than unrestricted SPACH. The exact research goal is a decision-preserving reduction from arbitrary sparse polynomial-alphabet 2-CSP to such a fixed expander with only $O(k)$ variables and polynomial alphabet. The reduction is **OPEN**. Direct CEH conditional reductions to Set Cover / Dominating Set / Independent Set / Set Packing / polynomial-target 2-degenerate HOM, a port normal form $C_{2m}\cup M$, an input-dependent cubic expander reduction, and the full unreviewed matching-compiler log are archived at [ceh/README.md](ceh/README.md). Do not confuse the compiler's model-specific no-go arguments with impossibility of a general satisfiability-only reduction.
