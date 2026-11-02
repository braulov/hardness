# Graphic Rank and Global-Obstruction Complexity

**CORRECTION / SOURCE CHECK — 2026-11-02:** Nguyen, [*A Sublinear Treewidth Exponent for Binary Constraint Satisfaction*](https://hexagonmath.org/2611.00004v1), Theorems 1.1–1.2: fixed-degree binary CSP admits a CLAIMED uniform deterministic (L^{O_\Delta(1)}q^{O_\Delta(v/\sqrt{\log v})}) exact counting algorithm, and an expander class with (\operatorname{tw}(G)=\Theta(v)) violates the literal Marx 2010 conjecture excluding (f(G)|I|^{o(\mathrm{tw}(G))}). **SPACH / rSPACH / CEH (no (q^{o(v)})) are conditionally FALSE.** For polynomial (q=v^c), the same bound is (2^{O(v\sqrt{\log v})}), NOT (2^{O(v)}); so rNSE-SCSP (no single-exponential algorithm) remains *logically compatible*, but completely UNPROVED. Do NOT present it as an established hardness source. The more ambitious surviving critical-density candidate (m=\Theta(v\sqrt{\log v})) is separately described in [critical-density CSP note](docs/35_critical_density_csp_to_degen2_hom.md). The full external algorithm/Lean imports have not been independently reverified in this repository.



**New surviving HOM-hardness candidate (2026-11-02):** [Critical-density 2-CSP and 2-degenerate HOM](docs/35_critical_density_csp_to_degen2_hom.md). Although SPACH and CEH are conditionally refuted, a new *unproved* hypothesis excluding $q^{o(k)}$ for $k$ variables with $m=O(k\sqrt{\log k})$ constraints and polynomial alphabet is **not** contradicted by the cited CSP upper bound. The existing §4 pinning/subdivision reduction extends to $n=O(k+m)$ source vertices and polynomial-size 2-degenerate targets. If the new hypothesis holds, it rules out $2^{o(n\sqrt{\log n})}$ time for sparse-source HOM, matching the new **conditional** upper bound $2^{O(n\sqrt{\log n})}$. This is an open hardness source, not a theorem that the lower bound holds.

**Canonical hypothesis status ledger (Nov. 2, 2026):** [Closed versus surviving hardness sources](docs/34_csp_hypothesis_closure_registry_2026_11_02.md). SPACH/CEH/rSPACH are conditionally refuted by claimed sub-$q^k$ binary-CSP algorithms; the dense Clique/LogSAT/Span branches are **not** thereby refuted.

**CRITICAL RESEARCH ALERT — 2026-11-02:** [Note 22](docs/22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md) examines a brand-new Nguyen preprint CLAIMING a uniform deterministic degree-3 binary-CSP algorithm in time L^{O(1)}q^{O(v/sqrt(log v))}. **If valid, original SPACH/rSPACH are FALSE**. Under independent randomized Permutation Clique hardness, any general polynomial-time randomized reduction to polynomial-alphabet bounded-degree CSP requires at least Omega(k sqrt(log k)) output variables in the little-o sense. Algorithm and Lean dependencies are NOT independently audited. Treat earlier SPACH-based conclusions as suspended, not established.


**Research notebook — 2026-10-27.** Preliminary, not a theorem announcement. Independent review of the 2026 OpenAI ETH-refutation manuscript is ongoing.

## 2026-11-02: conditional tensor-contraction update and CLOSED hardness branches

**Main new audit:** [Boolean tensor contraction for sparse binary CSP; proof, parameter checks, and branch triage](docs/33_tensor_contraction_sparse_2csp_and_hardness_triage.md). Assuming the **full**, currently independently unaudited Boolean tensor-contraction theorem in OpenAI's October 25 manuscript, any explicit binary CSP with \(k\) variables, \(O(k)\) constraints and polynomial alphabet \(q=k^{\Theta(1)}\) admits deterministic exact counting in \(q^{O(k/\sqrt{\log k})}\operatorname{poly}(|I|)\). The tensorization uses \(O(k\log q)\) bit wires. This is a conditional deduction, **not** covered by the specifically documented Lean formalization of fixed-width #CNF.

**CLOSED under that premise:** the sparse polynomial-alphabet hardness conjecture **SPACH / rSPACH**, the fixed-cubic-expander hypothesis **CEH**, and CEH/SPACH-based \(q^{o(k)}\)-lower-bound routes for HOM, Set Cover, Independent Set, etc. Retain exact reductions and mathematical compiler constructions as archived work; the hypothesis supporting the claimed hardness is what fails.

**CONDITIONALLY INCOMPATIBLE with Circuit-SAT hardness:** an input-efficient universal polynomial-time reduction from arbitrary \(s\)-input polynomial-size Circuit-SAT to binary CSP with \(k+m=O(s/\log s)\) and \(q=\operatorname{poly}(s)\) would give \(2^{o(s)}\) Circuit-SAT via the same tensor algorithm. More generally any uniform \(k+m=o(s/\sqrt{\log s})\) is incompatible with both the full tensor theorem and a no-\(2^{o(s)}\) Circuit-SAT hypothesis. Weaker \(k+m=o(s)\) targets above that threshold remain OPEN.

**Not closed by this argument:** dense Permutation Clique / PSCH, LogSAT-A/B, full-span graphic/cographic rank feasibility, generic Circuit-SAT, and the structural fixed-expander compiler as a mathematical question. No actual Git research branches are deleted; status supersessions are recorded in the linked audit and original notes.

## 2026-11-02 follow-up: faster HOM/SubISO and a surviving hardness scale

[New research checkpoint: fast sparse-source HOM/SubISO and SqrtLog-SPACH](docs/34_tensor_algorithms_for_hom_subiso_and_surviving_hardness.md). Under Nguyen's externally claimed domain-uniform binary-CSP counting theorem, sparse-source **#HOM** takes \(h^{O(n/\sqrt{\log n})}\operatorname{poly}\) time; standard color coding plus inclusion–exclusion extends this to ordinary **Subgraph Isomorphism** with only a \(2^{O(n)}\) factor. For \(h=n^{\Theta(1)}\), both have \(2^{O(n\sqrt{\log n})}\) conditional upper bounds. The 2026 Guo paper already obtains stronger conditional \(2^{O(n/\sqrt{\log n})}\) algorithms for sparse FVS/HC/Steiner/connectivity tasks, and randomized bounds from a narrower Lean-scoped #SAT premise. **New candidate hypothesis:** no \(q^{o(k/\sqrt{\log k})}\)-time algorithm for polynomial-alphabet cubic binary CSP (SqrtLog-SPACH), quantitatively compatible with the upper bound and potentially sufficient to exclude \(2^{O(n)}\) for polynomial-target 2-degenerate HOM after a fresh gadget audit. Alternative compiler targets: PCC \(\to O(K\sqrt{\log K})\)-size CSP or Circuit-SAT \(\to O(s/\sqrt{\log s})\)-size CSP. None is constructed.

### Further November 2 research: functional bottleneck and critical random expanders

- [Functional-source SCC compression and expander obstruction](docs/34_tensor_algorithms_for_hom_subiso_and_surviving_hardness.md#4b-exact-source-scc-compression-for-functional-constraints-expander-obstruction): an exact \(h^{\sigma(D)}\) procedure for systems of partial functional equations; a cubic-expander incidence example proves that the source-SCC quotient can still have linear treewidth, even with two global functions and a 2-degenerate target. This is **not** a general lower bound.
- [Critical random cubic-expander CSP: Poisson limit and failure of arc consistency](docs/35_critical_expander_csp_poisson_and_arc_consistency.md): at relation density \(q^{-2/3}\) and polynomial \(q=k^c\) for sufficiently large fixed \(c\), the exact solution count approaches \(\mathrm{Poisson}(1)\) while all values have local supports with high probability. A clean average-case hardness stress test, **not** a proven hardness source.

### Stronger November 2 checkpoints: minimal UNSAT and unconditional HOM baseline

- [Minimal-UNSAT and planted-vs-null all-edge phenomenon](docs/36_critical_random_csp_minimal_unsat_and_all_edge_statistical_dependence.md): for critical random CSP on a fixed cubic expander and sufficiently large polynomial alphabet, **every** constraint is logically essential with high probability; an asymptotic \(e^{-1}\) share of inputs are *edge-minimally UNSAT* and arc-consistent. Planted and null distributions have vanishing TV distance after hiding **any one complete edge-relation table**, but constant distance on the full collection. This is a proved statistical/model-restricted barrier, not computational hardness.
- [Acyclic functional orientation yields an unconditional HOM baseline](docs/34_tensor_algorithms_for_hom_subiso_and_surviving_hardness.md#4b1-acyclicity-eliminates-all-cyclic-functional-terms-an-unconditional-half-exponent-bound): for fixed target degeneracy \(d\), exact \(\#\mathrm{HOM}\) on an \(n\)-vertex, \(m\)-edge source can be counted in \(2^{O(n+m)}h^{n/2}\operatorname{poly}\) time, **without** assuming any external 2026 algorithm. The orientation paradigm is classical; no novelty is claimed for this baseline.

### Global statistical bottleneck for critical random CSP (2026-11-02)

[Fourier likelihood-ratio and path-saturation checkpoint](docs/37_critical_expander_low_degree_fourier_and_path_saturation.md): in the balanced random CSP on a fixed cubic expander with alphabet \(q=k^c\) and critical relation density \(p=q^{-2/3}\), the planted-vs-null likelihood ratio \(L=Z\) has an **exact** \(p\)-biased Fourier spectrum. Its entire nonconstant mass below degree \(3k/2\) tends to zero if \(c>\max(3/2,3/\gamma)\), even though full total-variation distance tends to \(e^{-1}\). This is a strict barrier to normalized low-degree polynomial **mean distinguishers**, not to all efficient algorithms. Independently, random relation compositions along any length-4 path become complete with high probability, identifying why naive short-path elimination loses global information. An \(o(q^2)\)-bit adaptive query transcript also has vanishing planted-vs-null advantage by a direct coupling. Proofs and caveats are in note 37.

### 2026-11-02: exact flat Schmidt spectrum and unconditional random-CSP baselines

[New note 38: flat edge-cut Schmidt spectrum, DFS lower bound and 2-factor enumeration](docs/38_flat_cut_spectrum_backtracking_barrier_and_two_factor_enumeration.md). The centered global planted-vs-null statistic has **exactly \(q^{|B|}\) equal nonzero Schmidt coefficients** across every partition of edge tables, where \(B\) is the common incident-vertex boundary. On cubic edge expanders any balanced edge split has \(|B|=\Omega(k)\), giving an unconditional \(q^{\Omega(k)}\) *cross-cut separation-rank* requirement even for L2 approximation. This does **not** lower-bound arbitrary time-bounded algorithms. Independently, fixed-order local-check DFS visits \(q^{\Omega(k)}\) partial solutions on a constant fraction of UNSAT random instances, while deleting one perfect matching and enumerating solutions of the remaining 2-factor gives a genuine **unconditional expected \(q^{k/3}\operatorname{poly}(k,q)\)** exact algorithm. Neither implies or refutes the proposed \(q^{k/\sqrt{\log k}}\) average-case hardness.

### New unconditional average-case CSP algorithmic baselines (2026-11-02)

[Note 39 — critical random CSP via cutwidth and forward checking](docs/39_critical_csp_cutwidth_expected_algorithms.md): for critical iid Bernoulli-\(q^{-2/3}\) relation tables on **any fixed connected cubic graph** with \(k\) vertices, a polynomial-time constructed, table-independent variable order has cutwidth \(k/4+o(k)\). Consequently exact counting, decision, and search by ordinary local-check DFS have expected \(q^{k/12+o(k)}\operatorname{poly}(k,q)\) runtime over the random table distribution (vs. the old \(q^{k/3}\) 2-factor enumeration). For **triangle-free cubic graphs of logarithmic girth**, a many-leaf spanning tree and sound one-variable forward checking improve this to \(q^{ck+o(k)}\operatorname{poly}\), \(c=(14\sqrt7-20)/243\approx0.070126\). These are **fully unconditional expected-time** statements for a specified input distribution, not \(q^{o(k)}\) and not general worst-case algorithms; the externally claimed Nguyen tensor bound is asymptotically stronger. Proofs and exact model restrictions are in note 39.

### Group-lookahead CSP algorithmic checkpoint (2026-11-02)

[Note 40 — exact group-extension entropy, maximum-weight matching, and polynomial logarithmic-tree lookahead](docs/40_group_lookahead_boundary_entropy_and_matching.md). At critical \(p=q^{-2/3}\) on cubic graphs, the expected number of assignments extending a fixed prefix \(S\) locally to a free group \(U\) is **exactly** \(q^{(b_R(U)-b_S(U))/3}\). Disjoint group lookahead yields the explicit expected-prefix exponent \((|\delta(S)|-\sum_U(b_S(U)-b_R(U))_+)/3\). Optimizing singleton-or-pair checks is a **polynomial-time maximum-weight matching** problem and gives a rigorous per-prefix improvement over ordinary forward checking when the matching has positive weight. All connected induced-tree groups of size \(O(\log k)\) can be tested in polynomial time per search node. **No \(q^{o(k)}\) algorithm or uniform improvement on the prior \(q^{0.070126k}\) bound is proved.** The exact missing step is a graph-ordering / disjoint-tree packing theorem forcing sublinear maximum entropy.

## Research question

Can a *restricted*, fine-grained-preserving graphic-rank feasibility problem act as a single source of hardness for graph problems involving connectedness, acyclicity, covers, and tours? Can a circuit representation of its rank predicate instead yield genuinely new subexponential algorithms?

We deliberately distinguish **exact encodings** from **parameter-preserving reductions** and **unproved hypotheses**.

### Canonical core: Sparse Graphic Rank-CSP (SGR-CSP)

Input with size parameter `n`:

1. An undirected (multi)graph `G=(V,E)` with `|V|+|E|=O(n)`.
2. `O(n)` Boolean variables `z`, including one activation bit `y_e` per edge; a 3-CNF `phi(z)` with `O(n)` clauses.
3. Affine integer threshold `t(z)=c+sum_i a_i z_i`, with `O(n)` terms and coefficients in `{-1,0,1}`. Optionally a fixed number of linearly computable cardinality constraints is compiled into `phi` using linear-size Boolean circuits.

Question:

```
exists z: phi(z) = 1 and rank_F2(B_G[:, {e: y_e=1}]) >= t(z) ?
```

Here `B_G` is the unsigned `vertex x edge` incidence matrix over `F_2`. For every activated subset `Y`,
`rank(B_Y) = |V| - cc(V,Y)`.

The number `n` counts ALL the core graph objects and variables/clauses up to constant factors, not a chosen one-dimensional parameter after a polynomial blow-up. This prevents vacuous claims of `2^{o(n)}` from being transported across polynomial-size encodings.

### Stronger unifying formulation: one FULL-SPAN matroid constraint

**New central result of the notebook:** after taking the cographic dual and using a root gadget, all the graph families below can use the same **full-spanning** rank predicate rather than different affine thresholds. The underlying binary matroid is graphic, cographic, or a direct sum. The star instance also exactly represents SAT and Set Cover, with important parameter-loss caveats. See [`docs/09_full_span_matroid_conjecture.md`](docs/09_full_span_matroid_conjecture.md).

### Why this core matters

- **FVS** in bounded-degree graphs: retained vertices induce an acyclic graph iff `rank(Y) >= |Y|`.
- **Undirected Hamiltonian Cycle** in bounded-degree graphs: selected degree-two subgraph is Hamiltonian iff `rank(Y) >= |V|-1`.
- **Directed Hamiltonian Cycle** in bounded-(total-)degree digraphs: selected arcs form directed cycle cover; weak connectivity, certified by graphic rank, forces one tour.
- **Connected Dominating Set, Connected Vertex Cover, unweighted node-Steiner connectivity** in bounded-degree graphs: `rank(Y) >= |S|-1` for the subgraph induced by chosen vertices `S`, plus local feasibility.
- **Connected FVS**: two separate rank requirements can be combined into a *single* rank bound on the disjoint union of two graph copies.

Full proofs, special cases and corner conditions are in [`docs/01_core_formalism.md`](docs/01_core_formalism.md) and [`docs/02_encoding_registry.md`](docs/02_encoding_registry.md).

### Important second layer: a rank representation of Set Cover and SAT

Set Cover's union-cardinality function is graphic rank on a **star with repeated/activated parallel edges**. The number of activated distinct star spokes is the coverage size. A CNF can also use a star spoke per clause, activated when that clause is satisfied.

**This is an exact algebraic representation, not a linear-parameter reduction for unrestricted instances.** General Set Cover may have `m >> |U|` sets; arbitrary CNF may have many clauses and incidences. See [`docs/03_rank_coverage_envelope.md`](docs/03_rank_coverage_envelope.md).

### Parity-based route without rank circuits

A second exact identity: the number of nullspace certificates for a fixed assignment is `2^(rank deficit)`; modulo two it is 1 iff full span. Graphic-cut and cographic-cycle certificates have linear-size local Boolean verifiers. **Therefore the parity of the number of solutions** for the bounded-degree graph families reduces to exact #3-SAT on O(n) variables. Whether one can turn this parity algorithm into a decision algorithm is unresolved; a promising conditional route is arbitrary-field **weighted #SAT** plus polynomial identity testing. See [`docs/10_obstruction_parity_and_weighted_counting.md`](docs/10_obstruction_parity_and_weighted_counting.md).

## ETH-replacement / Williams win–win

The present SCGS hypothesis is **not yet** a strong ETH replacement: its failure implies at most the already available linear-circuit lower bound from 3-SAT. A substantially stronger circuit-lower-bound payoff would require **input-efficient compilation of polynomial-size Circuit-SAT** into a syntactically restricted span class, with 2^{o(n)} depending on genuine input bits rather than all auxiliary gates. The resulting conditional program, with correct reduction arrows and no dummy-matroid encodings, is in [`docs/11_eth_replacement_winwin.md`](docs/11_eth_replacement_winwin.md).

## New: edge-bucket projection for counting tensors (2026-10-28)

A proposed exact regrouping of incidence-indexed polynomial-counting tensors replaces per-block selected-incidence sets by their projected variable supports, with internal summation inside test-bucket tensors. On structured grouped-support instances this reduces the wire budget from the generic O(n loglog n) to O(n), *conditional on the October 2026 external tensor-contraction theorem* giving 2^{O(n/sqrt(log n))} counting time. There is **no universal dense-#SAT improvement** and **no NEXP lower bound** yet. Full proof, hybrid encoding, local-entry/precision audit, communication-rank obstruction, and concrete SAT/Circuit-SAT open problems: [`docs/12_projected_support_edge_buckets.md`](docs/12_projected_support_edge_buckets.md).

## Useful CSP preprocessing: cycle-rank core (2026-11-02)

For an explicit binary CSP whose constraint graph has cyclomatic number \(\mu=m-n+\operatorname{cc}(G)\), exact degree-\(\le2\) variable elimination either detects UNSAT or leaves at most \(2\mu\) variables and \(3\mu\) binary constraints **without increasing the alphabet**. Independently, cycle-cutset conditioning gives a \(q^{\mu}\operatorname{poly}(n,m,q)\)-time algorithm. This is a classical consequence of known techniques, not a new complexity result. See [the full statement, proof, caveats and original references](docs/13_binary_csp_cyclomatic_reduction.md).

## Research branches

All branches are also documented on `main`; independent Git topic branches keep experimental approaches apart.

- **A — rank-to-SAT circuit compression**: [`docs/04_branch_A_algorithms.md`](docs/04_branch_A_algorithms.md). Design `o(n sqrt(log n)/(log log n)^2)`-gate circuits (or analogous Tseitin 3-CNF) for graphic-rank predicates.
- **B — hardness and parameter-preserving reductions**: [`docs/05_branch_B_hardness.md`](docs/05_branch_B_hardness.md). Find a restricted canonical problem and nontrivial linear-preserving reductions.
- **C — common rank/coverage envelope**: [`docs/03_rank_coverage_envelope.md`](docs/03_rank_coverage_envelope.md). Capture CNF and Set Cover without hiding the parameter loss.
- **E — parity and weighted #SAT**: [`docs/10_obstruction_parity_and_weighted_counting.md`](docs/10_obstruction_parity_and_weighted_counting.md). A proved cancellation identity and a conditional randomized-decision route.
- **G — ETH-replacement / circuit win–win**: [`docs/11_eth_replacement_winwin.md`](docs/11_eth_replacement_winwin.md). A stronger input-efficient class, not yet established complete for Circuit-SAT.
- **D — structural/logical boundary**: [`docs/06_branch_D_logic.md`](docs/06_branch_D_logic.md). Relate Linear Monadic NP, MSO2, graphic rank and succinct global constraints.

For the distinction between **SCGS as a candidate hardness core** and an **ETH replacement with new circuit-lower-bound win-win**, see [`docs/11_eth_replacement_and_circuit_winwin.md`](docs/11_eth_replacement_and_circuit_winwin.md).

See [`docs/07_open_problems.md`](docs/07_open_problems.md), [`docs/08_status_and_caveats.md`](docs/08_status_and_caveats.md), and [`SUMMARY_RU.md`](SUMMARY_RU.md).

## Validation

Run `python3 scripts/check_small_instances.py`. This enumerates small graphs and checks the elementary rank equivalences via independent GF(2) elimination and brute-force graph checks.

## Status

Verified elementary rank identities and direct encodings **do not** establish a novel complexity conjecture, a fast rank circuit, or equivalence of the natural hard problems. The claim 'one conjecture -> all lower bounds' would additionally require reductions FROM the canonical problem TO every target problem. Conversely, a universal SGR-CSP subexponential algorithm immediately accelerates all the direct special cases.

## Sources

- OpenAI (2026), *The Exponential Time Hypothesis is False* — manuscript: https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf
- OpenAI Lean formalization scope: https://github.com/openai/math/blob/main/lean/docs/378.md
- OpenAI release and external review plan: https://openai.com/index/building-scientific-understanding-with-academic-communities/
- Ganian, de Haan, Kanj, Szeider (2016; journal 2020), *On Existential MSO and Its Relation to ETH*: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.42 ; https://doi.org/10.1145/3417759
## PSCH research notebook (2026-11-02)

A separate two-branch investigation of the **Polynomial-Size Clique Hypothesis** is archived at [docs/psch/README.md](docs/psch/README.md). Branch A studies whether a very fast polynomial-size Clique algorithm implies strong general circuit lower bounds; branch B studies conditional fine-grained reductions to CSP/HOM/SubISO and exact existential sparsification constructions (including Beneš/AllDifferent and Hamiltonian Path). These are working results requiring independent audit, not theorem announcements.

## Log-width SAT and sparse polynomial-alphabet CSP (2026-11-02)

A separate candidate **Sparse Polynomial-Alphabet CSP Hypothesis (SPACH)** and two non-equivalent width/size regimes for log-SAT (width O(log number-of-variables) with polynomially many clauses, versus width O(log input-length) with potentially superpolynomial length) are formalized in [`docs/13_log_width_sat_and_polynomial_alphabet_csp.md`](docs/13_log_width_sat_and_polynomial_alphabet_csp.md). The note gives the exact parsimonious binary 2-CSP -> CNF encoding and identifies why the 2024 Marx-style expander embedding does not automatically transfer new log-SAT hardness to cubic polynomial-alphabet CSP.

The focused **Permutation k x k Clique -> cubic sparse 2-CSP** research branch is in [`docs/14_permutation_clique_sparse_2csp_branch.md`](docs/14_permutation_clique_sparse_2csp_branch.md). The direct translation into logarithmic-width SAT is elementary and complete; the nontrivial goal is an O(k)-constraint, degree-3, polynomial-alphabet existential compiler of arbitrary pairwise compatibility. Existing Beneš-network AllDifferent compression gives only a partial O(k log k)-constraint gadget. Both the candidate hardness and universal compression are OPEN; avoid identifying the former with PSCH or any still-unverified ETH replacement.


**Quadratic-form iteration (2026-11-02):** [`docs/15_quadratic_form_and_alldifferent_interface_barriers.md`](docs/15_quadratic_form_and_alldifferent_interface_barriers.md) proves an O(kr)-constraint cubic CSP compiler for rank-r quadratic incompatibility matrices, exhibits a rank Theta(k^2) AllDifferent matrix with an O(k log k) Beneš encoding, and proves nondeterministic streaming and exact-projection separator lower bounds for AllDifferent. These are model-specific results; the arbitrary PCC -> O(k) compiler is still OPEN.


**Further PCC iteration:** [`docs/16_permutation_mixed_difference_rank_and_routing.md`](docs/16_permutation_mixed_difference_rank_and_routing.md) proves a polynomial-time computable mixed-difference lower-bound certificate for the rank modulo all permutation identities, gives an explicit 0/1 PCC instance with quotient rank Omega(k^2), and proves Omega(k log k) total literal-routing cost on constant-degree permutation networks with bounded congestion. These model-specific barriers do not rule out general existential decision-preserving CSP reductions.


**Static proof-test interface and robust-gap sampling:** [`docs/17_pcp_bridge_gap_sampling_and_logsat.md`](docs/17_pcp_bridge_gap_sampling_and_logsat.md) formalizes the equivalence between an O(k)-test, O(k)-symbol noninteractive two-query verifier (weak soundness suffices) and an O(k)-constraint explicit polynomial-alphabet 2-CSP, plus a randomized O(k log k/delta)-constraint sparsification for delta-robust NO instances. It also corrects an interpretation of the high permutation-quotient-rank example: that source constraint graph was already a matching. General arbitrary PCC -> linear cubic CSP remains OPEN.


**Randomized PCC/PCP branch (2026-11-02):** [`docs/18_randomized_low_soundness_pcp_to_linear_csp.md`](docs/18_randomized_low_soundness_pcp_to_linear_csp.md) proves a conditional O(k)-constraint one-sided randomized sparsification from O(k)-symbol two-query PCPs with inverse-polynomial soundness; alternatively, constant-gap proof tests with O(k) VC dimension suffice. The existence of either short verifier for arbitrary Permutation Clique is OPEN. Both deterministic and bounded-error randomized algorithmic directions are accepted; hardness hypotheses for randomized algorithms are explicitly distinct from deterministic versions.

## CEH — fixed-expander polynomial-alphabet CSP (2026-11-02)

The proposed **Colored Expander Hypothesis (CEH)** asserts hardness at the $q^{o(k)}$ scale for arbitrary explicit binary relations on **one predetermined cubic expander** with $k$ vertices and alphabet $q=k^{\Theta(1)}$. This is the strong version; excluding merely $2^{O(k)}$ algorithms is not our goal.

Full research checkpoint: [docs/ceh/README.md](docs/ceh/README.md). Further notes: [reductions, parameter audit and random instances](docs/ceh/01_reductions.md), [matching compiler, matrix and separator research log](docs/ceh/02_matching_compiler_research_log.md), [claims requiring audit and next objectives](docs/ceh/03_audit_and_next_steps.md).

Under CEH, explicit reductions give conditional $2^{o(k\log k)}$-scale hardness for parameterized Set Cover, Dominating Set, Independent Set, Set Packing, and (subject to verifying the HOM paper's quantitative reduction) polynomial-target degeneracy-2 HOM. The **OPEN** objective is an $O(k)$-variable, polynomial-domain, **decision-preserving** reduction from arbitrary sparse binary CSP to that **one fixed cubic expander**. This is separate from existing PCC/Circuit-SAT research. The many exact matching-compiler and $C=5/6$ arguments are research-log claims, **not independently audited** and not universal impossibility results.


**Two-layer PCC compiler audit (2026-11-02):** [`docs/20_two_layer_affine_nonlinear_pcc_audit.md`](docs/20_two_layer_affine_nonlinear_pcc_audit.md) proves a two-query affine-code distance obstruction, an elementary O(k)-size compilation of 3-ary affine checks into cubic 2-CSP, and a genuine permutation solution-set counting tradeoff: in an exact-projection two-layer model with t input-dependent binary tables of alphabet Q, tQ²=Omega(k^4), hence Q=Omega(k^1.5) for t=O(k). Under randomized PCC hardness, any universal linear compiler must have worst-case treewidth Omega(k) (infinitely often). These restrictions DO NOT exclude decision-only randomized reductions; no generic compiler has been constructed.


**Quadratic fixed-encoding two-query lower bound + 2026 LTC audit:** [`docs/21_oblivious_two_query_pcc_quadratic_barrier_and_2026_ltc.md`](docs/21_oblivious_two_query_pcc_quadratic_barrier_and_2026_ltc.md) proves that any input-independent encoding of permutations into poly(k)-alphabet symbols, checked at t fixed pairs of code positions with *arbitrary input-dependent* binary relations, must use t=Omega(k²) to exactly preserve EVERY permutation's clique validity. This extends to randomized exact-solution-preserving compilers with input-independent random test topology. Existential auxiliary proofs and decision-only randomized reductions are NOT excluded. Also notes First–Lazarovici's 2026 good nonlinear two-query LTC theorem; code testability alone does not provide the missing compatibility interface.


**Primary-source tensor audit and post-SPACH candidate (2026-11-02):** [`docs/34_tensor_theorem_primary_source_audit_and_surviving_single_exp.md`](docs/34_tensor_theorem_primary_source_audit_and_surviving_single_exp.md) checks the EXACT OpenAI tensor-theorem hypotheses against arbitrary sparse binary CSP (not just degree-3), distinguishes the narrower Lean 378 scope and Anthropic imported endpoints, derives a conditional wider m=O(v log^a v), a<1/2, algorithmic regime, and defines **rNSE-SCSP(c)**: no bounded-error randomized 2^{O(v)} poly(L) algorithm for cubic CSP with q=v^c. This candidate is unproved but not contradicted by the claimed 2^{O(v sqrt(log v))} upper bound. A linear-parameter CSP -> degen-2 ordinary HOM transfer remains UNVERIFIED and must not be assumed.


**SOLVED transfer audit (2026-11-02):** [`docs/35_general_sparse_binary_csp_to_2deg_hom_linear_source.md`](docs/35_general_sparse_binary_csp_to_2deg_hom_linear_source.md) re-checks our arXiv 2607.09377 Section 4 and proves that its pinning-frame gadget works for **arbitrary sparse** binary CSP, not just the bipartite 3-regular ETH-hard source in the theorem statement. Exact construction: n=255v+257m+251, h<=250(v+m)+251+5vq+7\sum_e|R_e|, degen(H)<=2, and no lists. In particular the unproved randomized rNSE-SCSP(c) (no 2^{O(v)} algorithm) WOULD IMPLY no randomized 2^{O(n)}poly(h) ordinary HOM algorithm even with degen(H)<=2 and h=O(n^{2c+1}). The REDUCTION is proved; the hardness hypothesis is OPEN. For c=1, h=O(n³). No new HOM gadget is needed.


**rNSE-SCSP research iteration (2026-11-02):** [`docs/36_rnse_scsp_attack_mild_pcp_and_structured_algorithms.md`](docs/36_rnse_scsp_attack_mild_pcp_and_structured_algorithms.md) substantially weakens the PCP goal needed for the post-SPACH no-single-exp hypothesis: under randomized Permutation Clique hardness, an O(k)-symbol, poly(k)-alphabet 2-query PCP with ANY subconstant soundness s=o(1) yields O(k log k/log(1/s))=o(k log k) cubic CSP and therefore rNSE-SCSP(c) for some fixed c. This remains an OPEN short PCP, not an obtained hardness proof. The note also proves exact hybrid 2^{O(v)} algorithms for low rectangular-cover budgets, O(v/log q) exceptional edges, and bounded fibers on spanning forests, with a randomized-input greedy theorem showing dense random constraint tables are easy. The full unrestricted 2^{O(v)} problem remains OPEN.


**Follow-up (2026-11-02):** [Rank-dual exact CSP counting, sparse-partner branching, and the literal edge-bucket barrier](docs/36_rank_dual_critical_csp.md). An exact integer Smith-factorization of each relation yields an **unconditional** solver of time poly(L) * product_e rank_Q(R_e); hence m=O(k sqrt(log k)) CSP is already q^{o(k)} when ranks are uniformly at most 2^{o(sqrt(log k))}. Low allowed-partner degree gives an independent spanning-tree solver. Conversely, with high probability a random critical-density primal graph has no dense subgraphs of size <=k^{1-eps}, preventing any superconstant wire savings by raw q-value edge-bucket grouping of such small supports. This is strictly a **model-specific** obstacle, not a general CSP lower bound.


**New exact rank-cycle CSP algorithm + two-way HOM equivalence (2026-11-02):** [`docs/37_weighted_cycle_rank_exact_counting_and_sparse_hom_equivalence.md`](docs/37_weighted_cycle_rank_exact_counting_and_sparse_hom_equivalence.md) proves exact #CSP in poly(L)*product(rank(A_e): e outside an optimal MAXIMUM-rank spanning forest), using rank-factorization of chord relations and weighted tree DP. A corresponding Boolean rectangle-cover SAT algorithm needs rectangle choices only on chords, not all edges. A small-prime modular variant is one-sided randomized. Most importantly, the all-polynomial-exponents 2^{O(v)} algorithm question for sparse binary CSP is algorithmically EQUIVALENT to 2^{O(n)}poly(h) HOM on sparse 2-degenerate G and polynomial-size 2-degenerate H, using our already proved gadget (both G and H are 3-subdivisions). Neither universal single-exponential algorithm nor source hardness is proved.

**Joint-factor follow-up (2026-11-02):** [Exact matching-number formula for cross-block CSP relation rank and the large-tensor arity bottleneck](docs/37_joint_block_matching_rank_and_arity.md). For arbitrary tables, the maximum rank of the joint interaction matrix across groups A,B is exactly q^(maximum matching in G[A,B]). This permits a substantial formal reduction in bonds when many edges share block endpoints, but a naive full-group tensor violates the external contraction theorem's maximum-local-degree bound precisely in the useful regime. No general critical-density CSP algorithm is obtained.


**Multilevel factorization audit (2026-11-02):** [Fixed-partition rank loss and the growing-degree algorithmic criterion](docs/38_multilevel_factorization_and_degree_uniformity.md). For random critical-density CSP graphs, independent pairwise rank factorization across any predetermined fine balanced partition with g/sqrt(log k) -> infinity has total interface rank (1-o(1))m. A naive multi-level refinement therefore loses its coarse-block savings. An alternative sufficient breakthrough is a *uniform-in-growing-degree* CSP counting theorem with exponent q^{O(f(Delta)n/sqrt(log n))} for f(Delta)=o(Delta); standard occurrence splitting would then give q^{o(k)} on the entire critical-density class. Neither a general compression nor this stronger degree theorem is proved.


**Adaptive-block rank barrier (2026-11-02):** [Uniform no-go for all graph-adaptive small-block vertex-cover factorizations](docs/39_adaptive_block_rank_barrier.md). On a random graph with $\Theta(k\sqrt{\log k})$ edges, with high probability **every** vertex partition into blocks of size at most $k^{1-\varepsilon}$ satisfies $\sum_{i<j}\nu(G[A_i,A_j])\ge m-O(k)$. It strengthens the earlier **fixed-partition** bound and shows that optimal pairwise cover interfaces have no superconstant-factor savings even after adaptively choosing the blocks. This is an architecture-specific graph lemma, NOT a general CSP/tensor lower bound.


**Further CSP audit (2026-11-02):** [Nguyen grouping overhead and random-table greedy solvability](docs/40_nguyen_grouping_overhead_and_random_csp_greedy.md). The source-level recursion includes $gP/K$ with $g=3K^8$, so merely substituting low-rank group-pair factors does not certify $q^{o(k)}$. Independently, on *any* graph of maximum degree $\Delta$, independent Bernoulli($\rho$) binary relations satisfy universal local extension with probability at least $1-kq^\Delta e^{-q\rho^\Delta}$; hence greedy CSP is polynomial-time with high probability for $q=k^c$, fixed $\rho$, $\Delta=o(\log k)$. Random half-dense full-rank relations are therefore not a useful critical-density hard distribution.


**2026-11-02: stronger grouping obstruction.** [Uniform coarse-partition matching saturation and row-sensitive grouping](docs/41_uniform_coarse_partitions_and_row_sensitive_grouping.md) proves that *every* balanced graph-adaptive partition of a typical critical-density graph into $g\le\sqrt{\log k}/(100\log\sqrt{\log k})$ groups has $\nu(A_i,A_j)\ge k/(2g)-O(1)$ for each group pair. For the vertex-cover factorization, $U,\sum_iP_i,g\max_iP_i$ all have order $gk\log q$. Thus replacing $gP/K$ by a sum of row capacities alone yields **no asymptotic saving**. Also recorded: a black-box query lower bound showing an external-bond-only grouping theorem must charge internal weights.
