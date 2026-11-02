# PSCH research program — checkpoint (2026-11-02)

## Working definitions and discipline

**PSCH (working hypothesis)**: There is no uniform deterministic algorithm deciding ordinary `k`-CLIQUE for *every* graph on at most `k^2` vertices in time `2^{o(k/log k)}` (allowing polynomial input-size factors). Precise quantifier conventions, randomization, and whether an `N <= k^C` variant is needed must be fixed before publication. Do not silently identify this with an ETH consequence in the post-October-2026 setting.

The `k × k` Multicolored Clique instance, with `k` independent color classes of size `k`, is already an ordinary `k`-Clique instance on `k^2` vertices: a `k`-clique must take exactly one vertex from each class. Consequently a fast ordinary Clique algorithm solves the multicolored special case.

**Status policy**: tag every claim as PROVED (with complete proof), DERIVED CONDITIONAL, PROPOSED/AUDIT NEEDED, or OPEN. An ETH/SETH lower bound is not evidence for unconditional hardness if ETH is false; the Oct 2026 ETH preprints and their extensions remain under external review.

## Branch A — negate PSCH -> circuit lower bounds

**Main target**: FastClique (`k`-Clique with `N<=k^2` in `2^{o(k/log k)}` time) => `E^NP` not contained in `P/poly`, or another superpolynomial general circuit lower bound.

### Established starting reduction (check details before using as published theorem)

By grouping the variables of a sparse 3-SAT instance with `m` clauses into blocks of `Theta(log m)` variables and taking `k = Theta(m/log m)` groups with at most `k` assignments each, reduce to multicolored `k × k` Clique. Thus FastClique would imply 3-SAT in `2^{o(m/log^2 m)}`.

A Williams-style easy-witness/nondeterministic-time-hierarchy argument **suggests** a transfer to `E^NP` lower bounds at `n log^2 n` circuit size. Earlier chat gave a plausible proof sketch, but precise witness circuits, clause-decoder size, uniformity, and asymptotic quantifiers require an independent complete audit; do not present the exact quantitative consequence as independently certified before that audit.

### Main bottleneck

Given an exponentially long 3-CNF `F_n` with an efficient local clause decoder and a witness circuit `C` of size `n^c`, define `D_C(i)=1` iff the i-th clause is falsified by C's assignment. Aim for a Clique instance with parameter `O(n log n)`, `N<=k^2`, and total reduction/simulation time `2^{o(n)}` (or another direct algorithm-to-lower-bound route).

The naive Tseitin encoding has `Theta(|C|)` or more variables, and hence does not control `k` uniformly in the exponent `c`.

### No-go for universally local checkers

For `F_n = ∧_{i∈{0,1}^n} z_i`, let `C_Q(i)=1-Q(i)` for arbitrary circuit Q. Then `D_{C_Q}(i)=Q(i)`. Thus any universal polynomial-time compression of **all** such checkers into `k=O(n log n)` and `N<=k^a` for a fixed `a` would compress arbitrary `d`-SAT into `n^{O(a)}` bits for arbitrarily large `d`, conflicting with Dell–van Melkebeek-style sparsification lower bounds unless `NP ⊆ coNP/poly`. The special computation checker might still possess extra exploitable structure. Subexponential-time reductions are not directly ruled out by polynomial-kernelization theorems.

### Tasks

1. Independently validate the quantitative Williams transfer and investigate known algorithm-to-lower-bound theorems (including published Oct 2026 manuscripts).
2. Attack the `E^NP ⊄ P/poly` implication non-black-box: change witness relation, computation representation, verification model, deterministic/nondeterministic reductions, algebraic fingerprints, and direct Clique reductions.
3. Precisely test whether the chosen hard local checker embeds arbitrary Circuit-SAT; prove a barrier or identify a usable structural restriction.
4. Derive strongest conditional quantitative lower bound possible, track all polylogs, uniformity, and circuit-size quantifiers.

**Status**: target OPEN; baseline reduction plausible/standard; universal-checker compression has a conditional obstacle.

## Branch B — PSCH-based fine-grained lower bounds for CSP, HOM, SubISO, and others

**Goal**: Make PSCH a useful independent hardness hypothesis, with genuinely strong and varied consequences (not merely trivial parameter substitutions).

### Generic transfer

A polynomial-time reduction from `k`-Clique with `N<=k^2` to a problem with parameter `p=O(k^a (log k)^b)` transfers PSCH into a prohibition on `2^{o(p^{1/a}/(log p)^{1+b/a})}` running time (subject to parameter range and reduction overhead). In particular, no `2^{o(p/log p)}` if `p=O(k)` and no `2^{o(sqrt p/log p)}` if `p=Theta(k^2)`.

### Direct instances

- **2-CSP**: take `k` variables and alphabet `q=k^2=|V(H)|`. Put adjacency `R_ij=E(H)` on every pair. Thus `n=k`, `m=Theta(k^2)`, and PSCH forbids `2^{o(n/log n)}` when `q=n^2`, or equivalently `q^{o(n/log^2 n)}`. This does NOT prohibit `2^{O(n)}`.
- **Subcubic constraint graph**: replace each variable by `k-1` copies along a path of equality constraints; each copy has at most one original constraint and two equalities. Then `Delta<=3`, `m=Theta(k^2)`, `q=k^2`, transferring `2^{o(sqrt m/log m)}` prohibition.
- **HOM**: `K_k -> H` iff H has a k-clique (loopless simple targets), so a direct lower bound `2^{o(n/log n)}` on source size `n=k`, `h=k^2`. This does NOT prevent single-exponential HOM.
- **Subgraph Isomorphism with both graphs 2-degenerate**: define `S(G)` by subdividing every edge once. For `k>=4`, `K_k ⊆ H` iff `S(K_k) ⊆ S(H)` as (non-induced) subgraphs; also the induced version holds. Pattern size `p=k+binom(k,2)=Theta(k^2)`; host size `h=N+|E(H)|=O(k^4)`; both are 2-degenerate. Therefore PSCH prohibits `2^{o(sqrt p/log p)} poly(h)` on this restricted class. Proof of converse: branch vertices have pattern-degree >=3 and must map to original vertices (subdivision vertices have degree 2); adjacency of every branch pair must correspond to an original host edge.
- **Grid Tiling**: standard k-by-k construction using diagonal equality and off-diagonal adjacency relations; parameter `t=k`; transfers `2^{o(t/log t)}` on domain size `k^2`.

### Important correction: no automatic Hamiltonian Cycle lower bound

Hamiltonian Cycle on a host `H` is the special SubISO case with pattern `C_|V(H)|`. The constructed hard family has pattern `S(K_k)`, not a cycle. Indeed `S(K_k)` is **non-Hamiltonian** for `k>=4`: all degree-2 subdividers force use of every incident edge, so each original vertex would need cycle degree `k-1>2`. In fact, `S(H)` is non-Hamiltonian whenever H has any vertex of degree >=3. Therefore PSCH's 2-degenerate SubISO lower bound implies **no HC lower bound by specialization**. Seek an independent parameter-controlled reduction to HC if desired.

### Hamiltonian Cycle upper bounds and late-2026 update

- Classical Held–Karp `O*(2^n)`.
- Björklund randomized undirected decision `O*(1.657^n)`.
- Baitian Li (ICALP 2026), exact #directed/undirected Hamiltonian Cycles `2^{n-Omega(sqrt n)}` (still exponential at base nearly 2).
- Tulsyan, Hexagon preprint of 2026-10-31, **claims conditionally on the new Anthropic #SAT algorithm's inner lemmas** a deterministic exact #HC algorithm for sparse graphs `m<=Dn` in `2^{O_D(n/sqrt(log n))}`; broader claim `2^{O((m+n)/sqrt(log n))}` and `2^{O(n log(average degree)/sqrt(log n))}`. Source labels work primarily AI-generated; no independent human expert review claimed. This is NOT known to follow from a simple linear-size fixed-width CNF reduction: connectivity of a 2-factor is global, and the new work employs determinant/Grassmann/network machinery. Separate a claim about the full Anthropic internal theorem from weaker implications of its top-level formal statements.

### Research priorities

1. Find a radically more efficient reduction from `k`-Clique to **bounded-degree sparse 2-CSP** with `q=k^{O(1)}` and `m=O(k polylog k)` or better. Check feasibility and lower bounds on compression.
2. Transfer sparse CSP to **ordinary HOM**, especially targets of degeneracy 2 and polynomial size, without using list constraints unless lists are eliminated by a checked gadget. Track source size exactly.
3. Clarify whether a stronger and still plausible replacement hypothesis is needed to forbid single-exponential HOM; PSCH by itself cannot exclude `2^{O(n)}` for a linear-size source.
4. Develop nontrivial applications to SubISO, Induced SubISO, partitioned embedding, Grid Tiling, geometric packing, or connectivity, with explicit parameters and statements not already subsumed by modern subexponential algorithms.
5. For HC, first verify Oct 31 preprint, distinguish sparse vs dense inputs, and do NOT claim any transfer from the `S(K_k)` SubISO construction.

**Status**: the simple CSP/HOM/SubISO/Grid-Tiling reductions are mathematically routine/derive as described; stronger compression and ordinary HOM lower bounds OPEN; subexponential sparse HC is a recent conditional, externally unreviewed claim.

## Key sources (for later independent audit)

- Björklund, Determinant Sums for Undirected Hamiltonicity: https://epubs.siam.org/doi/10.1137/110839229
- Baitian Li, Counting Perfect Matchings and Hamiltonian Cycles Faster, ICALP 2026: https://doi.org/10.4230/LIPIcs.ICALP.2026.138
- Tulsyan, Counting Hamiltonian cycles in sparse graphs in subexponential time, assuming the new #SAT algorithms (2026-10-31): https://hexagonmath.org/2610.00672v1
- OpenAI, The Exponential Time Hypothesis Is False (2026-10-25 manuscript): https://github.com/openai/math
- Anthropic, A 2^o(n) Time Algorithm for 3-SAT (2026-10-26 manuscript): https://github.com/anthropics/formal-math
- Jansen–Pieterse, Sparsification Upper and Lower Bounds for Graph Problems: https://link.springer.com/article/10.1007/s00453-016-0189-9
- Jahanjou–Miles–Viola, Local Reductions: https://arxiv.org/abs/1311.3171

## Next review checkpoints

A. Review GPT-6.1's aggressive single-pass attempt at `FastClique => E^NP ⊄ P/poly`. Require precise theorem, proof, losses, and adversarial audit.

B. Independently develop lower bounds via sparse CSP/homomorphism; first measure the gap between quadratic replication and a near-linear number of constraints. Examine other natural graph problems only when the reduction yields a quantitatively meaningful lower bound.

## Branch B progress note — 2026-11-02: dense Clique -> sparse 2-CSP

**Target (OPEN)**: a uniform polynomial-time reduction from ordinary k-CLIQUE on N<=k^2 vertices (or separately from k-colored Clique with k groups of size k) to 2-CSP with m=O(k polylog k), maximum constraint degree O(1), and alphabet Q=k^O(1). IMPORTANT: PSCH for ordinary Clique does not by itself imply hardness of the *restricted* k x k multicolored instances; a reduction proving the target theorem must start with all ordinary Clique instances, or one must strengthen PSCH.

### Proven obstruction 1: local variable-carrying reductions

Suppose a bounded-degree target constraint graph has t=O(m) variables, every target variable carries at most b original source choices, and each one of the binom(k,2) source pair constraints must be checked by a target unary or binary constraint whose endpoints collectively carry the two source choices. A target constraint can involve at most 2b original choices, thus check O(b^2) different original pairs, giving m=Omega(k^2/b^2). When Q>=k^b is needed to store independent k-ary source choices and Q=k^O(1), b=O(1); hence m=Omega(k^2). This applies to straightforward copy/equality gadgets, grouping, minor/low-congestion embeddings and local routing. It DOES NOT apply to arbitrary reductions using global algebraic or encoded auxiliary variables.

### Proven obstruction 2: representation counting for solution-projection-preserving reductions

Consider k-colored clique with k groups, k labels per group. Require every edge incident to the default label 0 to be present. Each of binom(k,2)(k-1)^2 remaining cross-group edges can be independently present/absent. The set of satisfying k-tuples determines every such edge: choose nonzero values only in the corresponding pair of groups and default 0 elsewhere. Hence at least 2^{Omega(k^4)} distinct projected solution sets arise.

Suppose the target is an explicit binary CSP over Q symbols, with m binary constraints, O(m+k) relevant variables, optional unary constraints, and a FIXED projection onto the k source labels (no uncounted graph-dependent decoder). The number of possible target descriptions is at most 2^{O(m Q^2+(m+k)Q + m log(m+k))}. Exact preservation of every original assignment's extendibility requires different projected solution sets to yield distinct descriptions. Thus m Q^2+(m+k)Q+m log(m+k)=Omega(k^4).

For Q=Theta(k), this entails m=Omega(k^2). If m=O(k log^beta k), it entails Q=Omega(k^{3/2}/log^{beta/2}k) (for nonpathological parameter ranges). For Q=k^2, it gives no useful lower bound: merely specifying O(k) relations already uses enough bits to carry arbitrary input data. This is NOT a no-go for decision-only polynomial reductions or for arbitrary graph-dependent projections.

### Positive structured example: globally factorized bilinear edge predicate

Let group i have candidates a in [k] represented by vectors v_i(a) in F_p^d, and declare i<j compatible iff v_i(a)^T M v_j(b)=0 for one common d x d matrix M over F_p. Construct a path CSP with state s_i=(a_i,U_i), where U_i is the subspace spanned by M^T v_1(a_1),...,M^T v_i(a_i). The transition from s_{i-1} to s_i enforces v_i(a_i) orthogonal to U_{i-1}, and U_i=span(U_{i-1},M^T v_i(a_i)); initial U_1=span(M^T v_1(a_1)). Then all pairwise bilinear constraints hold iff the path CSP is feasible. There are <=p^{d^2} subspaces, so alphabet Q<=k p^{d^2}, m=k-1, max degree=2; polynomial Q for constant d and p=poly(k). In fact this structured clique class becomes polynomial-time solvable. This is a toy algebraic success, not hardness for arbitrary graphs.

### Next target

Seek a non-black-box / algebraic verifier that encodes arbitrary k^2 pairwise adjacency tests without locally transporting each pair, with explicit m and Q bounds. Investigate global quadratic forms, succinct algebraic relations, PCP-of-proximity style checks, and *why universal graph edge tables cannot be compressed into a common constant-dimensional bilinear predicate*. Scrutinize completeness AND soundness, uniform construction time, and whether the supposed reduction secretly decides Clique.

References: Marx, Can You Beat Treewidth? (ToC 2010), https://theoryofcomputing.org/articles/v006a005/ ; Karthik–Marx–Pilipczuk–Souza, Conditional lower bounds for sparse parameterized 2-CSP: A streamlined proof (SOSA 2024), https://epubs.siam.org/doi/10.1137/1.9781611977936.35 .

### Further audit: generic global bilinear encoding needs huge dimension

In the bilinear model, let N=k^2 be the total number of candidates and use a common matrix M in F_p^{d x d}, with one assigned vector in F_p^d per candidate. There are at most p^{N d+d^2} such representations. But k-colored graphs with all default-label incident edges present have 2^{Theta(k^4)} distinct possible cross-group edge sets. Therefore a representation of ALL such graphs requires (k^2 d+d^2) log_2 p=Omega(k^4), hence d=Omega(k^2/log p). In particular d=Omega(k^2/log k) for p=poly(k), and d=Omega(k^2) for fixed p. This is a counting lower bound on *faithful global bilinear encodings*, NOT a decision-reduction lower bound. It explains why the constant-dimensional path construction cannot encode all inputs.

### Conditional treewidth requirement

If a hypothetical polynomial-time reduction to 2-CSP with q=k^{O(1)} always produces an efficiently supplied tree decomposition of width w=o(k/log^2 k), ordinary CSP DP would solve the result in q^{O(w)} poly(k)=2^{o(k/log k)}, contradicting PSCH. Thus a PSCH-compatible reduction must avoid uniformly tiny treewidth (or huge alphabet). This is a simple corollary of PSCH rather than a new unconditional barrier.

### Parameter bookkeeping if success occurs

If ordinary k-Clique reduces to bounded-degree 2-CSP with m=O(k log^beta k) and q=k^{Theta(1)}, PSCH forbids 2^{o(m/log^{beta+1}m)} running time on the resulting promise class, equivalently q^{o(m/log^{beta+2}m)}. In the linear case m=O(k), the forbidden time is 2^{o(m/log m)}, not 2^{o(m)}, and not enough by itself to exclude single-exponential HOM.

### Unconditional obstruction 3: small ordinary arithmetic circuits cannot aggregate arbitrary clique checks

Choose p>binom(k,2), p=poly(k). Let variables a_i range over [k], where 0 is the distinguished default. For an arbitrary collection of edge tables A_ij with all edges involving default 0 set to 1, define P_A(a_1,...,a_k)=sum_{i<j}(1-A_ij(a_i,a_j)) in F_p. Because p>binom(k,2), P_A=0 iff all selected pairs are adjacent. Moreover, for the tuple with exactly two nonzero coordinates i=a,j=b, P_A equals the missing-edge indicator for that particular pair. Thus the family {P_A} contains 2^{Theta(k^4)} DISTINCT functions on [k]^k.

A fan-in-two arithmetic circuit over F_p with k inputs, at most s gates, and field constants stored in O(log p) bits can be described in O(s log(k+s+p)) bits. For p=poly(k) and s=poly(k), this is O(s log k). Hence fewer than 2^{O(s log k)} such circuits exist. To compute all functions P_A exactly with one circuit per A, one needs s=Omega(k^4/log k) in the worst case. In particular there is no universal O(k polylog k)-gate algebraic evaluation of these sums with only ordinary field operations and poly(k)-sized field constants. This counting obstruction is unconditional and applies to faithfully computing P_A, NOT to decision-only Clique reductions or arithmetic circuits equipped with input-dependent giant table-lookup gates / CSP relations. It sharply focuses the next search on using large explicit relations and globally coherent existential encoding rather than evaluating P_A with small ordinary circuits.

## Branch B progress note — 2026-11-02 continued: exact interface / fingerprint obstruction

**Rigorous statement (in a restricted, solution-preserving model).** Consider k=2r source choices x_1,...,x_r and y_1,...,y_r, each over a q-element alphabet. Make the only nontrivial binary source relations x_i=y_i (other cross-group pairs and all same-side pairs allow everything). The source satisfying-tuple relation is M(x,y)=[x=y], the q^r-by-q^r identity matrix. This fits k-partite clique with r matching equality interfaces and all remaining pairwise relations complete. It is an EASY source instance; the purpose is a representation lower bound, not complexity hardness.

Suppose an exact extended binary-CSP representation has named terminals for x,y, auxiliary variables, target alphabet Q, and a separator S of t target variables separating left terminals from right terminals. For every fixed assignment s to S, all remaining satisfiability checks on the two sides separate, so M(x,y)=OR_{s in [Q]^t}(L_s(x) AND R_s(y)). This expresses M as a union of at most Q^t Boolean rectangles. Identity matrix I_{q^r} requires q^r rectangles (any 1-rectangle contains at most one diagonal 1). Thus Q^t >= q^r, or t >= r log q/log Q. For q=k^2, Q=k^C, t>=k/C. This also directly rules out a single polynomial-size global checksum state / deterministic fingerprint for exact all-input consistency, even with arbitrary existential auxiliaries on either side.

**Limitations:** applies to *solution-preserving representations with separated named terminals* and the specified separator; does NOT exclude decision-only reductions (which may recognize this easy source and output trivial YES), nor expander-based sparse CSPs with Theta(k)-sized interfaces, nor randomized algorithms with nonzero soundness error. In particular, this does NOT prove target treewidth Omega(k): the equality-matching source itself has treewidth 1 despite having a large separator for this chosen left-right terminal split. Never claim general treewidth lower bound from this lemma.

**Sharper interpretation for random fingerprints:** replacing the whole length-r tuple by a single checksum over F_p fails for *exact* consistency for every possible tuple when p<q^r, by pigeonhole; any fixed randomized hash seed has collisions as well. With field-size p=poly(k), at least Omega(k) field coordinates are needed if both q and p are polynomially related. Random fingerprint soundness for a *single pre-specified pair* is a different, weaker property; the CSP existential quantifier can select a colliding pair, so pointwise probability bounds do not directly prove soundness of a randomized reduction.

**Literature pointers verified:** Guruswami–Lin–Ren–Sun–Wu, STOC 2025 (arxiv:2404.08870) use parallel PCP and Reed–Muller encodings to obtain near-optimal sparse 2-CSP gap hardness under ETH; Bafna–Karthik–Minzer, STOC 2025, prove sparse 2-CSP gap hardness and a *densification* result, not a generic reverse sparsification. Jansen–Pieterse, Optimal Sparsification for Some Binary CSPs Using Low-Degree Polynomials, emphasize that constraint TABLE BIT SIZE, not just number of constraints, is important in sparsification lower bounds. None of these sources was verified to solve the desired ordinary polynomial-size Clique -> O(k polylog k)-constraint CSP conversion with polynomial alphabet.

**Live research question:** can a polynomial-time, decision-preserving reduction replace the quadratic family of arbitrary clique adjacency tests using a bounded-degree expander of O(k polylog k) relations with Q=poly(k) and global coherence not mediated by a low-dimensional deterministic checksum? One possible attack: look for exact witness-checking PCPs with proof length O(k polylog k) symbols and near-linear local consistency checks for arbitrary k-clique input of size k^4 bits, while allowing each binary relation table itself to encode polynomially many input bits. Require soundness for every existential assignment, not only high-probability correctness of individual tests.

### A concrete global-algebraic experiment: very short interactive sum-check (NOT a CSP reduction)

Let an ordinary input host graph H have N<=k^2 vertices. Set d=ceil(log_2 N), pad vertex names to {0,1}^d, and choose a prime p>k^2. For a proposed witness list v_1,...,v_k (possibly repeated), let w:{0,1}^d -> F_p record multiplicities. Let B(u,v)=1 iff u=v or {u,v} is a nonedge of H (and define B=1 for unused padded vertices), otherwise 0. The integer S = sum_{u,v} w(u) w(v) B(u,v) lies in [0,k^2] and vanishes modulo p exactly when the list consists of distinct vertices and all pairs are edges, i.e. is a k-clique.

Let W(X) be the multilinear extension of w and Btilde(X,Y) the multilinear extension of B on 2d Boolean coordinates. Put P(X,Y)=W(X)W(Y)Btilde(X,Y). Each of its 2d coordinates has individual degree at most 2, and sum_{X,Y in {0,1}^d} P(X,Y)=S. Standard sum-check verifies the claimed sum zero in 2d=O(log k) rounds with O(d) field elements of prover communication and soundness error O(d/p). The verifier can evaluate W(r) directly from the k vertex names in O(kd) field operations: W(r)=sum_i chi_{v_i}(r), where chi is the multilinear indicator basis. Evaluating Btilde(r,s) costs O(N^2 d)=poly(k) operations from the explicitly given host; no succinct circuit for an arbitrary adjacency table is assumed. This is an exact arithmetic identity with an information-theoretically SOUND *interactive randomized protocol* for testing a chosen witness, NOT a deterministic/existential CSP certificate.

Critical soundness failure when naively compiling to CSP: a CSP existentially guesses a full transcript. If verifier random challenges r_1,...,r_{2d} are preselected and visible to the existential prover, a false sumcheck claim can generally be made to pass: already in a single round over odd-characteristic F_p, one can choose a degree-2 polynomial g with g(0)+g(1)=0 and g(r)=f(r) for a given honest final value f(r); the two independent linear equations have a solution for every fixed r. Then continue honestly at the later fixed challenges. Thus exists transcript after fixing challenge' is not interchangeable with exists adaptive strategy winning against random verifier'; the correct order of quantifiers/adaptivity is essential. A random hash/fingerprint fixed as part of an existential CSP witness similarly fails because the witness can select a collision. Fiat–Shamir would only be computationally sound under extra assumptions, not an exact deterministic hardness reduction.

Potential next move: find a *short locally checkable encoding of the entire adaptive prover strategy*, with size O(k polylog k) symbols of alphabet poly(k) and soundness against ALL deterministic assignments. This is a parameter-sensitive PCP/PCPP-of-proximity problem. The STOC 2025 parallel PCP work controls length relative to its own CSP/input representation, and does not automatically furnish the extraordinarily short (relative to the k^4-bit adjacency input) proof required here. Quantify proof size, query distribution, verifier randomness, and exact versus gap soundness independently.

References: sum-check overview and bound in https://www.cs.yale.edu/homes/cpap/published/libra-crypto19.pdf ; STOC 2025 parameterized sparse CSP gap hardness https://arxiv.org/abs/2404.08870 .

## Branch B audit — exact verifier vs sparse 2-CSP (2026-11-02, follow-up)

### CRITICAL correction to the prior sum-check display (PROVED)

The earlier notebook incorrectly claimed that `S=sum_{u,v} w(u)w(v) B(u,v)` vanished for a clique while defining `B(u,u)=1`. In fact S >= k, because the k diagonal positional terms contribute 1. Define `S'=S-k = sum_{i != j} B(v_i,v_j)`, for the proposed (possibly repeated) ordered k-tuple. With a prime `p>k(k-1)` and B=1 on equal or nonadjacent vertices, `S'=0 mod p` iff the proposed tuple is a k-clique. The multilinear-extension/sum-check verifier should claim the hypercube sum equals `k` (NOT zero). The 2d-round O(log k) protocol survives this correction. Full evaluation of the arbitrary adjacency-table extension Btilde can take polynomial-in-N time and query many graph edges: short prover COMMUNICATION is NOT a near-linear local verifier.

### Edge-oracle query lower bound for any locally checking proof (PROVED)

Let a possibly randomized oracle verifier V take a graph G with N>=k vertices and arbitrary auxiliary certificate pi, with completeness at least c on some pi for every yes graph and soundness at most s for every pi on every no graph, c>s. Suppose the verifier only accesses the host adjacency through individual oracle queries, with NO input-dependent preprocessing that has already examined the graph. On the graph G=K_k plus N-k isolated vertices, choose the completeness certificate pi. For each edge e of the unique k-clique, G-e has no k-clique. Couple the run of V on G and G-e using identical random bits. If V never queries e, the transcript and decision are identical, hence P_G[query e] >= c-s. Summing over the binom(k,2) clique edges shows E[distinct adjacency queries] >= (c-s) binom(k,2) = Omega(k^2). Applies to arbitrary nondeterministic proof bits and adaptive randomized verification; in particular perfect completeness + 1/3 soundness requires at least 2/3 binom(k,2) expected probes on this yes input. It DOES NOT prohibit precomputing relations from the entire graph in polynomial time: the reduction is allowed to examine all k^4 input bits and encode them across huge polynomial-sized binary tables. Hence the target loophole is *input-dependent global compilation*, not simply fewer oracle probes.

### Linear-check tradeoff (PROVED in the explicit verification-vector model)

Let b(a) be the M=binom(k,2)-bit vector of pairwise violations for a k-tuple. The exact decision criterion is b(a)=0. One can encode it as ONE field-valued equation sum_e b_e(a)=0 mod p with p>M, so reducing the number of scalar equations is trivially possible. But evaluating this equation naively needs M pair lookups; fewer equations != fewer constraint incidences. More generally, for a linear sketch `Rb(a)` to recognize b=0 for every possible violation vector including each standard basis vector e_j, every column of R must be nonzero, and thus `nnz(R)>=M`. Allowing randomized dense R can make a fixed seed sound for all k-tuples with high probability by a union bound, but it does not remove this incidence bound. To beat M local pair checks, a construction must perform nonlocal, input-dependent preprocessing that compiles many pair predicates into one large binary relation, or leave the linear-sketch model.

### Current exact challenge (OPEN)

Construct, in polynomial time for EVERY ordinary k-Clique input with N<=k^2, a bounded-degree explicit 2-CSP with m=O(k polylog k), alphabet Q=k^O(1), and equivalence of SAT/CLIQUE. Each relation table is allowed poly(k) bits and may encode globally preprocessed input information. The construction must have exact existential soundness; a single fixed sum-check transcript is unsound. Do not confuse this with a proof of an O(k)-symbol certificate: the original k chosen vertices already constitute such a certificate. The nontrivial requirement is a *locally checkable/relational* encoding with m near-linear checks.

Literature cross-checks: Guruswami–Lin–Ren–Sun–Wu (STOC 2025) obtain nearly linear *parallel PCP* size for a special structured CSP and conditional gap hardness under ETH, not a verified general dense Clique -> sparse CSP construction. Khanna–Putterman–Sudan (STOC 2025) study preserving all assignment values under CSP sparsification; their near-linear cases do not directly solve decision-only arbitrary-2-CSP compression. Sum-check standard soundness is discussed in the AFP formalization (2024) and contemporary lecture notes. None of these should be cited as proving the OPEN target.

### Useful PCP-to-sparse-CSP lemma (PROVED, randomized reduction)

Suppose a polynomial-time constructible 2-query proof system for an instance of k-Clique has L proof locations over alphabet Q, **perfect completeness**, and constant gap eps: every proof for a NO instance fails >=eps fraction of the random verifier tests. Each test's accepting relation on its two queried alphabet symbols must be computable explicitly in poly(k) time, and tests must be samplable in poly(k) time. Choose t independent random verifier tests, t>= (L ln Q+ln(1/delta))/(-ln(1-eps)). For any fixed NO proof, probability of passing them all is <=(1-eps)^t; union bound over Q^L proofs shows with probability >=1-delta NO proof passes all. YES has a proof passing all tests for every sample (perfect completeness). Turn sampled tests into 2-CSP constraints. Degree-reduce by introducing one occurrence-copy per use of any proof location and imposing a path of equality constraints. This produces Delta<=3, O(t) constraints, alphabet Q, with a randomized polynomial-time reduction. Therefore **short PCP proof length L=O(k polylog k), Q=poly(k), constant gap implies sparse 2-CSP with O(k polylog k) constraints**, up to one extra log Q factor. Number of ORIGINAL random verifier seeds is irrelevant once tests can be sampled and soundness has a constant global gap. This is stronger/cleaner than trying to compile one sumcheck transcript.

CRITICAL quantifier caveat: a randomized reduction plus fast deterministic CSP solver yields a RANDOMIZED fast Clique algorithm, not a deterministic one. To derive a contradiction from the currently *deterministic* PSCH, require either an explicit deterministic test sparsifier, or strengthen PSCH to exclude randomized algorithms. The PCP itself may use randomness safely because the reduction samples tests *before* choosing a satisfying CSP assignment AND guarantees via union bound that all proofs are simultaneously rejected in NO instances.

Existing results relevant to target: Ron-Zewi–Rothblum, Local Proofs Approaching the Witness Length (2023/2024), achieve very short INTERACTIVE ORACLE PROOFS for wide NP relations, not ordinary 2-query PCPs. Fortnow–Santhanam-type short-proof compression barriers for arbitrary SAT (see Ron-Zewi–Rothblum intro) caution against expecting a universal short PCP based only on witness length. But the relevant fixed input family of k-Clique graphs with N=k^2 and explicit input-dependent relations needs a separate parameter audit before such a barrier can be applied.

**Next concrete subproblem:** Construct a noninteractive 2-query PCP with L=k polylog k locations, Q=k^O(1), perfect completeness and constant soundness for *ordinary* k-Clique on N<=k^2 vertices, allowing polynomial-in-k preprocessing of the input adjacency matrix and local relation tables. Prefer a deterministic explicit O(L polylog k)-test subset to support deterministic PSCH. Analyze whether adapting parallel/IOP PCPs meets these exact proof-length, relation-table, and soundness parameters. If impossible, give a precisely stated no-go and model restrictions.

## 2026-11-02 continuation: exact-PCP amplification obstacles and literature cross-check

### An edge-critical dense 2-CSP (PROVED)

Take k variables x_1,...,x_k with domain [k-1] and a disequality constraint x_i != x_j for every i<j. The resulting 2-CSP is UNSAT by pigeonhole principle, but deletion of ANY one constraint (i,j) makes it SAT: assign the same value to x_i,x_j, and pairwise distinct values to the remaining k-2 variables. Thus all M=binom(k,2) constraints are indispensable for this exact NO instance, which is also a k-partite Clique instance with k (or k-1) candidates per part. Any constraint-subsampling reduction that only keeps a proper subset of original constraints fails deterministically on this example. Moreover some assignment violates exactly one out of M tests, giving gap 1/M, not constant. This is a *restricted no-go*, not a barrier to new globally preprocessed predicates or auxiliary encodings.

### Sensitivity lower bound for any constant-gap PCP test (PROVED; relative to original edge-oracle)

Let G_0 consist of K_k plus isolated vertices, and let pi be a proof accepted with probability 1 by a noninteractive PCP verifier V on G_0. Soundness <=1-eps on each G_e=G_0-e, where e is any of M=binom(k,2) clique edges. For each e, the same proof pi must be rejected with probability >=eps on G_e. Coupling the verifier coins, on G_0 the run must access an input-dependent quantity whose value changes after deletion of e in at least eps of runs. Thus, if T_r(G,pi) is the acceptance predicate of test r, then

    E_r[ |{e subset E(K_k): T_r(G_0,pi) != T_r(G_0-e,pi)}| ] >= eps*M.

In the explicit input-edge oracle model, computing each test with at most b adaptive adjacency-bit probes implies b>=eps*M by the usual transcript coupling. If tests are compiled into large binary relation tables using arbitrary polynomial-time input preprocessing, each test *may* depend on Theta(k²) original edges via those tables; the lemma does not rule out such compilation. It pinpoints the need for massively input-dependent relations, not fewer oracle queries.

### Existing near-optimal grouping is insufficient at polynomial alphabet (VERIFIED FROM PAPER)

Guruswami, Lin, Ren, Sun, Wu (STOC 2025; ECCC TR24-075, Lemma 5.1, citing Marx 2010 and Karthik–Marx–Pilipczuk–Souza 2024) establish: an n-variable 2-CSP with m constraints and base alphabet Sigma can be grouped into K variables and a 3-regular constraint graph, with expanded alphabet Sigma^t and t=O((n+m) log K/K) (stated for 6<=K<=n), in time poly(n, |Sigma|^t). Applied to the dense k-variable k×k Clique CSP, n=k, m=Theta(k²), base |Sigma|=k, and K=Theta(k), this produces t=O(k log k), hence |Sigma'|=k^{O(k log k)}, not polynomial in k. This is an UPPER bound on t in that grouping technique, not a theorem requiring such a large t for every possible reduction. The existing sparse hard CSP pipeline begins from sparse coloring (m=O(n)), not dense Clique with arbitrary pair relations. References: https://eccc.weizmann.ac.il/report/2024/075/download , Lemma 5.1, Remark 5.2; https://arxiv.org/abs/2304.02943 §4 (vector 2-CSP retains k+binom(k,2) constraints).

### Better-defined next target (OPEN)

Develop an input-preprocessed, perfectly complete, constant-gap, two-query *noninteractive* PCP for ordinary k-Clique on N<=k² vertices, proof length L=O(k polylog k), alphabet Q=k^{O(1)}, with tests extractable in poly(k) and each test permitted arbitrary poly(k)-time dependence on input adjacency. A randomized sample of O(L log Q) tests and equality-copy degree-reduction would give bounded-degree explicit 2-CSP with O(k polylog k) constraints. FOR deterministic PSCH, a randomized sampler is NOT enough to transfer a deterministic lower bound: either derandomize sample selection or explicitly formulate randomized PSCH. All standard near-linear PCP constructions are linear/quasilinear in verification CIRCUIT SIZE, not necessarily in witness length k log k; arbitrary adjacency checks have Theta(k²) witness-related costs (and input table N²=Theta(k⁴) bits). This is the central quantitative barrier.

Status: no general short-PCP or sparse 2-CSP reduction obtained. This round yielded rigorous critical-instance and test-sensitivity lemmas and verified that existing 2025 grouping does not meet target parameters by straightforward application.

## 2026-11-02 — low-rank incompatibility: exact constructive reduction + limits

### PROVED: algebraic-rank compression for multicolored Clique

Let there be k parts V_1,...,V_k, |V_i|<=q. Define B over F_p, p>k(k-1), indexed by labeled candidates (i,a); B[(i,a),(j,b)] is 1 iff i != j and the candidate pair is NOT adjacent, otherwise 0. Suppose rank(B)=r over F_p. Compute B=UV^T with U,V having r columns. For a candidate tuple a=(a_1,...,a_k), set S_t=sum_i U[(i,a_i),t], T_t=sum_i V[(i,a_i),t]. Then sum_t S_t T_t equals the INTEGER number of ordered incompatible selected pairs, reduced mod p. Because this number lies in [0,k(k-1)] and p is larger, sum_t S_t T_t=0 iff the tuple is a multicolored clique.

Computing the 2r running coordinate sums and their dot product uses O(k(r+1)) arithmetic gates over F_p and input-dependent unary look-up tables of size k q r. A standard exact arity-3-gate to 2-CSP translation introduces an auxiliary symbol (a,b,c) in F_p^3 for each addition/multiplication gate and binary projection relations; equality-copy chains reduce every variable's degree to <=3. Consequently there is a deterministic polynomial-time reduction to an equivalent explicit 2-CSP with m=O(k(r+1)) constraints, Delta<=3, and alphabet Q=poly(q,p,k), with a fixed polynomial exponent independent of r. For q,p=poly(k) and r=polylog(k), this yields m=k polylog(k), Q=poly(k), perfect existential equivalence. This is for a **low-rank structured class**, not arbitrary input graphs.

### PROVED: direct algorithm and conditional decision-only obstruction

The same factorization yields an O(k q p^{2r} poly(r)) deterministic algorithm: DP over states (sum_i U[(i,a_i),*], sum_i V[(i,a_i),*]) in F_p^{2r}, adding one part per layer; at the end test their dot product is zero. Thus this low-rank class is polytime for constant r and quasipolynomial for r=polylog(k) when q,p=poly(k).

If PSCH holds for **ordinary** Clique on N<=k^2, there cannot exist a uniform polynomial-time **decision-only** reduction mapping every ordinary k-Clique instance to a k^{O(1)}-candidate-per-part multicolored instance whose incompatibility matrix has rank r(k)=o(k/log^2 k) over a field p=k^{O(1)}: composing the reduction with the DP takes 2^{O(r log k)} poly(k) =2^{o(k/log k)} poly(k), contradicting PSCH. This does NOT require preserving individual solutions, unlike the counting lower bound below. It specifically rules out the low-rank route to m=k polylog k for *arbitrary* instances under PSCH.

### PROVED: unconditional counting obstruction for tuple-wise exact low-rank quadratic testers

Set q=k and give each part a default label 0. All pairs touching a default are compatible, and every pair of nondefault labels in distinct parts can be independently compatible/incompatible. This gives 2^{Theta(k^4)} different valid-tuple sets (each edge can be recovered by choosing exactly its two nondefault labels and defaults elsewhere).

Consider an arbitrary input-dependent algebraic tester on the tuple of k labels of the form F(a)=c+sum_i l_(i,a_i)+sum_{i,j} M[(i,a_i),(j,a_j)] over a field of p=poly(k) elements, where rank(M)<=r, and require for EVERY tuple a: F(a)=0 iff a is a clique. Here M is an N x N matrix, N=kq=k^2. The number of rank-<=r matrices is <= p^{2Nr+O(1)} (factor M=UV^T), and the unary/constant coefficients add at most p^{N+1} possibilities. Therefore the number of distinct zero sets representable is at most p^{2Nr+N+O(1)}. Covering the 2^{Theta(k^4)} distinct clique-solution sets forces (2Nr+N) log_2 p=Omega(k^4), or r=Omega(k^2/log k). This holds even if the matrix is allowed to differ from the actual nonedge matrix and only the ZERO SET must match. It is **not** a lower bound for arbitrary decision-preserving reductions with existential auxiliary variables and high-rank tables.

### Literature audit and next plan

Existing Clique -> k-VectorSum reductions often suffer quadratic blow-up: e.g., Abboud–Lewi / Lin's framework reduces k-Clique to k'=O(k^2) VectorSum with O(k^2 log n) equations, before algebraic PCP work. See https://eccc.weizmann.ac.il/report/2015/193/ and Lin–Ren–Sun–Wang ICALP 2022 https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.90 . These are not yet a near-linear arbitrary-Clique -> sparse 2-CSP reduction.

**Conclusion**: low rank *does* give an exact almost-linear CSP representation for structured instances, but arbitrary Clique cannot be compiled into uniformly sub-(k/log^2k)-rank instances if PSCH is true. The remaining potentially productive mechanisms must have high-rank intermediate relations while preserving compact existential consistency, or use more powerful objects than a single low-rank global quadratic form. Next prioritize high-rank factored decision representations, vector-structured parallel-PCP methods and exact algebraic certificates, with explicit construction time and input size; avoid reiterating low-rank or plain constraint sampling as if they could be universal.


## 2026-11-02 — Branch B: high field-rank / low Boolean-cover rank and exact-extension counting

### PROVED: Boolean-rectangle cover gives short 2-CSP even with high field rank

Consider colored candidate sets V_1,...,V_k, size at most q. Suppose the directed forbidden relation between candidates of DIFFERENT colors has a Boolean rectangle cover:
  B(u,v) = OR_{t=1}^r ( [u in A_t] AND [v in C_t] ).
For an undirected input, include ordered forbidden pairs in both directions; the relation is required only for distinct color classes. Let u_i be selected from color i. Put a_t=sum_i [u_i in A_t], c_t=sum_i[u_i in C_t], d_t=sum_i[u_i in A_t intersect C_t]. The nonnegative integer a_t*c_t-d_t counts distinct ordered pairs of selected candidates covered by rectangle t. Therefore the tuple is a clique iff a_t*c_t=d_t for every t.

A streaming circuit maintains all 3r counters, requires O(kr) arithmetic operations on O(log k)-bit integers, and can be converted to binary CSP (pairwise constraints encoding gate-input/output tuples, with equality-copy chains) using m=O(k(r+1)), Delta<=3, and alphabet k^{O(1)} (independent of r). The transformation is deterministic polynomial time for r=poly(k).

Strongest special case: define P,Q subset [r] as Boolean masks of A_t/C_t observed in previously chosen candidates. To add candidate u in color class i, require A(u) intersect Q = empty and C(u) intersect P = empty, then update P'=P union A(u), Q'=Q union C(u). This enforces every directed pairwise forbidden relation and ignores self-pairs by checking before updating. Thus the original decision problem reduces to a PATH 2-CSP with k transitions, degree <=2, and alphabet at most 4^r (precompute an allowed transition if some candidate of color i realizes it). Also obtains a direct deterministic algorithm in O(k q 4^r poly(r)) time. For r=O(log k) the path-CSP has O(k) constraints and polynomial alphabet and the instance class is polynomial-time solvable.

High algebraic rank example: let labels be bitstrings x,y in {0,1}^r with B(x,y)=1[x intersect y is nonempty]. Boolean rectangle cover has size <=r. Complement D=1-B is the tensor product [[1,1],[1,0]]^{tensor r}, hence rank(D)=2^r over every field and rank(B)>=2^r-1. This exhibits rank >=k-1 when r=log_2 k although Boolean-cover compression uses O(k log k) constraints (or O(k) path constraints at alphabet 4^r). This is a structured compression, NOT a hardness transfer.

Under PSCH, no uniform polynomial-time decision-preserving reduction from arbitrary ordinary Clique with N<=k^2 to polynomial-size multicolored instances of Boolean rectangle-cover number r=o(k/log k) can exist, assuming a polytime-computable explicit cover is supplied by the reduction. Compose with the O(poly(k) 4^r) DP. This statement does NOT cover target graphs having small Boolean rank but where finding the cover is hard.

### PROVED: exact-extension information tradeoff, including existential auxiliary variables

Restrict to k x k multicolored Clique, which is a special case of ordinary k-Clique on k^2 vertices. Each color class has a default 0. Pairs involving a default are always allowed; the (k-1)^2 candidate pairs between every two distinct colors are freely chosen. The family contains 2^{Theta(k^4)} distinct sets of satisfying k-tuples; an input edge can be recovered by assigning the two relevant non-default values and default values in all other classes.

Consider any source-assignment-preserving translation of EVERY such instance to a binary CSP with <=m explicitly tabulated constraints over target alphabet [Q], any number of existential auxiliary variables incident with constraints, and a FIXED, input-independent projection onto the k original coordinates (with specified output-to-input label encoding). Drop unused auxiliary variables. At most k+2m variables matter. Specifying a binary CSP requires <=m Q^2 bits for tables plus O(m log(k+m)) bits for the constraint graph and lower-order variable identification/unary information. Hence #possible projected solution sets is <=2^{O(mQ^2+m log(k+m))}. Comparing to 2^{Theta(k^4)} yields
  m (Q^2 + log(k+m)) = Omega(k^4).
For polynomial m and Q>=k^epsilon, this simplifies to mQ^2=Omega(k^4).

Consequently, if m=O(k polylog k), then Q>=k^{3/2}/polylog(k)^{1/2}; in particular with Q=k^{1+o(1)} there is an Omega(k^{2-o(1)}) lower bound on m. This remains true with arbitrary existential auxiliary variables and without degree restrictions, but fundamentally uses **preservation of the full projected solution relation**. A decision-only reduction may map different input instances to the same output, so this counting lower bound does not apply. Variable-dependent input-specific huge decoding maps also invalidate the stated encoding count unless their bits are included.

### Structural direction and limitation

A universal decision-only dense-to-sparse compilation, if it exists, must go beyond both low-rank aggregates and low-Boolean-cover aggregates (which give direct algorithms), and beyond solution-preserving representations in the small-alphabet regime. Any target constraint graph with treewidth t=o(k/log^2 k) plus an efficiently supplied decomposition and alphabet Q=k^{O(1)} also contradicts PSCH because standard CSP DP takes Q^{O(t)} poly(k)=2^{o(k/log k)}. Thus a genuinely hard compiled instance must retain substantial global dependency / treewidth, while allowing input-dependent binary tables.

The counting result is a self-contained derivation in a stated syntactic model, not a claim of literature novelty. The original global decision-only compression with m=O(k polylog k), Q=poly(k), Delta<=3 is still OPEN. Related parameterized PCP papers: Guruswami–Lin–Ren–Sun–Wu STOC'25, https://doi.org/10.1145/3717823.3718130 ; Goldwasser–Kalai–Rothblum interactive PCP, https://collaborate.princeton.edu/en/publications/interactive-pcp/ ; Ben-Sasson et al. efficient PCPP https://salil.seas.harvard.edu/publications/short-pcps-verifiable-polylogarithmic-time .

## 2026-11-02 continued: threshold-aggregate compression and direct-linear-code barrier

Status: all constructions below are restricted structural statements. No universal decision-only ordinary Clique -> O(k polylog k)-constraint, polynomial-alphabet sparse 2-CSP reduction is established.

### Exact threshold / Ferrers-union compression (proof)

Given k distinct color groups and up to q candidates per group, let the directed forbidden relation for candidates in DIFFERENT groups have an explicitly supplied representation

  B(u,v) = OR_{t=1}^r [ f_t(u) <= g_t(v) ],

where all f_t and g_t take values in [T], T=poly(k,q). An ordinary undirected forbidden relation should be represented symmetrically, possibly by including both orientations as separate terms. The representation is only required for pairs from different color groups; same-group pairs are ignored by the algorithm.

Process one candidate u_i per group in sequence. For t in [r], maintain F_t=min_{j<i} f_t(u_j) and G_t=max_{j<i} g_t(u_j), initially F_t=T+1, G_t=0. Add u_i iff for all t both f_t(u_i)>G_t and F_t>g_t(u_i), then update minima/maxima. This enforces exactly that no forbidden ordered pair exists among distinct chosen positions. Each feature updates using O(1) bounded-integer operations; a bounded-arity circuit of O(k r) such operations can be translated to an equivalent explicit degree-3 binary CSP with O(k(r+1)) constraints, alphabet (kqT)^{O(1)} with an exponent INDEPENDENT of r, and deterministic polynomial-in-the-explicit-representation construction. Gate-to-binary-CSP uses a variable carrying each small tuple of gate inputs/outputs with binary projection relations and equality-copy chains to enforce fanout, keeping maximum degree <=3. Alternative DP stores all (F_t,G_t), runs in (T+2)^{2r} poly(k,q,r). For fixed r this class is in P.

The staircase relation B(a,b)=[a<=b], a,b in [q], has field rank q (upper triangular invertible matrix), and Boolean rectangle cover number q (diagonal fooling set, since each all-1 rectangle can contain at most one diagonal cell). Yet it uses ONE threshold term. For undirected candidate incompatibilities across two role types L,R, take directed threshold on L -> R and its transpose on R -> L; the upper-triangular q-by-q block witnesses large rank and cover, while r=2. Ferrers/chain graphs are the classical class of nested neighborhoods; no novelty of Ferrers theory is claimed.

Counting obstruction for exact threshold representations: if N=kq candidate identifiers and T=poly(k,q), one threshold term consists of 2N values f,g in [T], and there are at most T^{2N} terms of this form. A union of r threshold relations has at most T^{2Nr} representations. On k color classes with q=k labels and one default label per color, allowing arbitrary forbidden pairs between nondefaults gives 2^{Theta(k^4)} relations that can be recovered from their FULL solution sets. Thus representing every such relation exactly requires r >= Omega(k^2/log k). This argument is not applicable to arbitrary YES/NO-preserving reductions.

### Fourier-support no-go for direct two-query linear-code aggregation

Let p be any ODD prime and x in F_p^k. Let zeta=e^{2 pi i/p} and F(x)=sum_{1<=i<j<=k} zeta^{x_i+x_j}. For a linear map L_e:F_p^k -> F_p^2 and arbitrary function h_e:F_p^2 -> C, the Fourier support of h_e(L_e x) is contained in a linear subspace W_e=im L_e^T of dimension at most 2. Each pair-frequency v_{ij}=e_i+e_j occurs with coefficient 1 in F. Any three distinct v_{ij} are linearly independent over any odd-characteristic field: their three corresponding edges form either a graph with a leaf (the leaf coordinate isolates a nonzero coefficient) or a triangle, in which case the incidence determinant is +/-2. Hence any 2-dimensional W_e contains at most TWO of the C(k,2) pair-frequencies. Therefore an identity F(x)=sum_{e=1}^m h_e(L_e x) requires m>=C(k,2)/2.

This **does not** preclude gate-based or nonlinear local preprocessing: indeed F(x)=((sum_i zeta^{x_i})^2 - sum_i zeta^{2x_i})/2 has an O(k)-size arithmetic circuit using nonlinear per-coordinate transformations and multiplications. The Fourier no-go applies only to sums of arbitrary functions of two LINEAR projections of the original assignment and is useful for rejecting naive proposals to enforce global consistency via a small set of linear-code-pair tests.

### Generic finite-state / path-width obstruction (conditional on PSCH)

If a polynomial-time reduction from all ordinary k-Clique instances N<=k^2 to a representation with S(k) sequential states, polynomially many candidate transitions (explicitly computable in poly(k) time), and exact existence semantics, then ordinary k-Clique is solvable in poly(k)*S(k) time by a reachable-states DP. Under deterministic PSCH, S(k) cannot be 2^{o(k/log k)}. In particular, any O(r)-coordinate summary with values in k^{O(1)} must have r not o(k/log^2 k) if it is to arise from a UNIVERSAL reduction (unless equivalent direct algorithms defeat PSCH). This is a generic, restricted barrier to any sequentially composable multi-code checksum scheme; it does NOT prohibit expander-like nonsequential CSPs of size O(k polylog k).

### Next research goal

Instead of looking for one more easy aggregate feature, target nonsequential interaction of two or more high-rate global codes on an expanding bounded-degree constraint graph, and exhibit at least one explicit family of genuinely hard high-rank, high-rectangle-cover instances with a succinct exact relational encoding that does NOT collapse to a small sequential DP. Track each relation table size, number of constraints, maximum degree, preprocessing time, exact soundness, and how ordinary (not only multicolored) Clique maps to the source.

Literature touchpoints: Ferrers/chain graph definition and nested neighborhood characterization (DMTCS 2026, https://dmtcs.episciences.org/16935/pdf ); short PCPs vs witness length and Fortnow–Santhanam restrictions (JCSS 2011, https://www.sciencedirect.com/science/article/pii/S0022000010000917 ); Guruswami et al STOC 2025 on specialized vector CSP, not universal Clique sparsification.

## 2026-11-02: stronger restricted no-go for fixed linear-code witness encodings

### Theorem (binary checks of a fixed linear encoding require quadratic many tests)

Fix a finite field F=F_q and k>=2. Let E:F^k -> F^L be ANY fixed linear map (not necessarily injective). Consider a family of explicit instances I of multicolored k-Clique with k groups indexed by i in [k], each group with q labels in F. Suppose each instance I is compiled into m binary predicates R_e^I on PAIRS of the L codeword coordinates, with arbitrary dependence on the ENTIRE input I (unbounded preprocessing permitted for the theorem). Require tuple-wise exactness for all x in F^k:

  x is a valid multicolored clique in I  <=>  for all e=(u,v), (E_u(x),E_v(x)) in R_e^I.

Assume that the set of coordinate pairs e=(u,v) can also depend on I, but E itself is fixed. Then the number of binary predicates in the output for at least one instance is >= binom(k,2); in fact, for the input with just one forbidden cross-group candidate pair from groups i and j, some predicate must have its two linear forms spanning BOTH source coordinate functionals e_i,e_j. For a fixed list of tested coordinate pairs independent of the input, requiring exactness for all instances forces at least binom(k,2) predicates globally.

IMPORTANT CORRECTION/NUANCE: The assertion 'for at least one instance m>=binom(k,2)' DOES NOT FOLLOW for input-dependent coordinate pairs from the one-forbidden-pair argument: the reduction can customize a single check for each such input. The unconditional m>=binom(k,2) conclusion requires a FIXED test topology (the queried coordinate pairs independent of I), or a stronger universally structured hard input argument not supplied here. The correct theorem is therefore:

  If E AND the multiset of tested coordinate pairs are fixed independently of I and relation tables are allowed arbitrary input dependence, tuple-wise exactness for all I implies m>=binom(k,2).

Proof. For every source group pair i<j and labels a,b in F, consider the input I_{ijab} with all pairs allowed except the pair x_i=a, x_j=b. Any x in cylinder Z={x:x_i=a,x_j=b} must be rejected by at least one check e, whereas every x outside Z must pass all checks. A rejecting table entry y=pi_e(x), where pi_e=(E_u,E_v), cannot be attained by any x' outside Z; thus its whole linear affine fiber x+ker(pi_e) lies in Z. This holds iff ker(pi_e) subset {z:z_i=z_j=0}, equivalently e_i,e_j in rowspace(pi_e). A rowspace of dimension <=2 contains at most TWO distinct standard coordinate vectors, so any fixed check can serve at most one unordered pair i,j. Since the fixed topology must be capable of rejecting every such I_{ijab}, m>=binom(k,2). Notice the proof works even though each input relation table can depend on all k^4 adjacency bits.

Generalization: for predicates on at most d fixed linear-code coordinates, a rowspace of dimension <=d can contain at most d standard coordinate functionals. Such a test can protect at most binom(d,2) source pairs. Hence m>=binom(k,2)/binom(d,2) for fixed test topology and full assignment preservation, with d>=2.

This is a no-go specifically for fixed linear encoding and fixed test topology with arbitrary preprocessed local predicate tables. It is NOT a lower bound for universal decision-only reductions, arbitrary input-dependent test topology, input-dependent encoding E_I, or existential auxiliary witness variables. All of those alternatives can break the one-forbidden-edge argument. The result demonstrates that placing two linear codeword symbols per edge of a sparse fixed expander does not eliminate all original pair dependencies merely through arbitrary global preprocessing of the edge tables.

A second, weaker-looking but differently quantified result concerns additive testing of a global pair-interaction sum: over odd F_p, F(x)=sum_{i<j}zeta^(x_i+x_j) cannot be written as sum of m arbitrary functions h_e of two linear forms unless m>=binom(k,2)/2, by Fourier support. Unlike the test-topology theorem, this assumes an additive decomposition but allows each pair of linear forms to be chosen adaptively to F. Neither result restricts nonlinear gate-based processing.

### Implication for future attacks

To beat quadratic m in an expander-PCP construction, at least one of the following must occur: the encoding itself depends nontrivially on the input, the test topology changes with the input, the proof includes free existential auxiliary symbols not fixed by the source tuple, the encoding of source choices is nonlinear, or exact pointwise witness preservation is abandoned. More promising than simply adding further independent linear codes is a genuinely nonsequential proof with auxiliary algebraic claims whose valid values are not uniquely determined by the original clique tuple.

## 2026-11-02 — Branch B, iteration V: nonlinear fixed-code no-go for arbitrary arity

### STATUS: PROVED IN EXPLICIT RESTRICTED MODEL, NOVELTY NOT CHECKED

Let q>=2 and k>=2. Consider all k-partite selection CSP instances with variables x_1,...,x_k in [q], whose arbitrary binary allowed relations R_{ij} can be specified for each pair i<j. Let E:[q]^k -> [Q]^L be ANY input-independent encoding, not necessarily linear, injective, or efficiently computable. Fix m query sets J_t of size at most d in [L], independently of input instance. For each instance I, its compiler may choose arbitrary accepting tables A_{I,t} subset [Q]^{|J_t|}, depending on the ENTIRE input I. Assume exact assignment-wise preservation: for every I,x, x satisfies I iff for all t the subtuple E(x)|_{J_t} lies in A_{I,t}. There are no existential auxiliary proof strings that can vary independently of x.

**Theorem (typical-fiber bound).** Set B=floor(log_q(2m Q^d)). Necessarily

  m * binom(B,2) >= binom(k,2).

In particular if q=k, Q <= k^C, and m<=k^D for fixed positive constants C,D, then B<=D+Cd+O(1) and

  m = Omega_{C,D}( k^2/(d+1)^2 ).

For d=2, m=Omega(k^2) even for nonlinear coding and arbitrary global precomputation of the tables. If m=O(k polylog k), necessarily d=Omega(sqrt(k/polylog k)) with constants depending on C,D. The d-ary generalization may have exponentially large explicit constraint tables for growing d, so its use is chiefly an information-locality statement; d=2 is the relevant sparse 2-CSP case.

**Proof.** Let P_t(x)=E(x)|_{J_t}, taking at most Q^d values. For independent uniform X,X' in [q]^k, write p_t(x)=Pr[P_t(X')=P_t(x)]. For each fixed t, Pr_X[p_t(X)<eta] <= Q^d eta, since there are at most Q^d output values. Choose eta=1/(2m Q^d). Union bound gives some x with p_t(x)>=eta for all t. Let S_t(x) be the set of source coordinates i which equal x_i for ALL y in the fiber P_t^{-1}(P_t(x)). The fiber is inside a cylinder fixing |S_t(x)| coordinates, so p_t(x)<=q^{-|S_t(x)|}, whence |S_t(x)|<=floor(log_q(2mQ^d))=B. For any coordinate pair i<j, construct an instance I_{ij,x} in which the only forbidden source pair is (x_i,x_j) for (i,j), and every other pair is allowed. The fixed x must be rejected by some table A_{I,t}. Every assignment y outside that one forbidden cylinder must be accepted and thus passes every table. Therefore the entire P_t-fiber through x must be inside the forbidden cylinder, implying {i,j} subset S_t(x). Every source-coordinate pair is consequently covered by some S_t(x), so binom(k,2) <= sum_t binom(|S_t(x)|,2) <= m binom(B,2). QED.

**What the theorem does NOT exclude.** (1) Instance-dependent E or instance-dependent chosen query positions; (2) nonfunctional existential auxiliary assignments z with a potentially different completion for each instance and x; (3) decision-only reductions that need not preserve the solution set; (4) random choices of an input-dependent encoding or checks. The first two directions are primary escapes. Merely allowing global preprocessing of the acceptance tables, while keeping E and positions fixed, is insufficient.

### Warning on trivial instance-dependent encodings

If one allows E_I(x) to be an arbitrary unverified instance-dependent function, one can set E_I(x)=[x satisfies I] and use one unary constraint. This is not a genuine reduction to CSP unless its consistency with x can be *enforced by the output CSP* with the claimed resources. The correct open model must count the size of constraints enforcing the auxiliary code or witness, not only tests of its claimed values.

### Related work and priority

Goldreich–Gur, Universal Locally Testable Codes: https://www.wisdom.weizmann.ac.il/~/oded/p_ultc.html ; universal locally verifiable codes for CSP (Goldreich–Gur). These deal with related universal local verification, but the exact restricted-model theorem above has not been checked for novelty and should not be advertised as a new publishable result.

### Next attack: nonfunctional existential extensions

Aim for an input-dependent compiler producing <=O(k polylog k) binary constraints, Q=k^{O(1)}, bounded degree, with existential auxiliary variables independent of any fixed deterministic code E(x). A useful intermediate benchmark is a *structurally restricted* hard family that admits such a compiler without also acquiring a k^{O(1)} or 2^{o(k/log k)} algorithm. Beware of apparently input-dependent E_I(x) whose verification cost is hidden rather than removed.

---

# 2026-11-02, Branch B — A hard, dense, maximal-rank family with linear sparse 2-CSP compilation

## Status and provenance

PROVED BELOW (elementary special construction, not a new universal sparse compilation). This explicitly answers the test case raised in v5: a high-rank, high-Boolean-cover, NP-hard family with an input-dependent existential sparse binary CSP representation. Its specific global transport structure is visibly planted; it should **not** be advertised as progress on arbitrary PSCH-to-sparse-CSP compression. The underlying relational composition/consistency formalism is classical (Montanari/Mackworth path consistency).

## Bounded-degree NP-complete source

Let Gamma be a binary CSP with k variables, domain sizes <=a for a fixed constant a<=7, constraint graph F of maximum degree <=3, and |E(F)|=Theta(k), with every constraint nontrivial. This family is NP-hard: for a 3-CNF, make a 7-valued variable per clause corresponding to its satisfying triples, and a binary variable per literal occurrence. Connect clause variables to their three occurrence variables with projection relations, and connect copies of the same Boolean variable in a path of equality constraints. The maximum degree is 3 and size is linear in number of occurrences. The relation alphabet can be shared (with variable-specific allowed subsets encoded in incident relations).

## Dense k-partite graph H(Gamma)

Set T=floor(k/a) (k large), and choose arbitrary beta_i in Z_T. Color class i consists of candidates (i,c,t) with c in D_i, t in Z_T; at most aT<=k candidates per group, so total vertices <=k^2. For i != j, candidate (i,c,t) and (j,d,u) are adjacent iff
(1) t-beta_i = u-beta_j modulo T, and
(2) if ij is an edge of F, then (c,d) in R_ij (orientation as appropriate).
Every pair of groups has a genuinely nontrivial compatibility relation from condition (1).

Exact equivalence: Gamma satisfiable iff H(Gamma) contains a multicolored k-clique (hence iff ordinary H(Gamma) contains K_k, because it is k-partite). If assignment c_i satisfies Gamma, choose any s in Z_T and t_i=s+beta_i. Conversely clique compatibility ensures c satisfies all R_e and all tags have common s. There are exactly T choices of s for each satisfying assignment.

## Explicit sparse existential compiler

Create variables y_i=(c_i,t_i) on the same domains D_i x Z_T. Keep the original constraints on every edge of F (including the tag-transport check), and add transport equality t_i-beta_i=t_j-beta_j on the edges of an arbitrary spanning tree on the k color classes. Thus m<=|E(F)|+k-1=O(k), alphabet Q<=aT=O(k), and the new CSP is equivalent, in fact preserves all chosen candidate tuples. If F has maximum degree 3 and the spanning tree is a path, degree <=5. Split each variable into O(degree) copies connected along an equality chain and assign its incident original constraints to separate copies; this gives maximum degree <=3, O(k) variables and constraints, and the same alphabet Q=O(k). If desired, introduce the common tag s explicitly as an existential witness and propagate it on the path. All input-dependent relations are explicitly computable in poly(k) time.

## Nearly maximal field rank

Let B be the full incompatibility matrix of H(Gamma), with B(u,v)=1 for candidates u,v in distinct groups that are *not* adjacent; set within-color blocks to zero. Pick an independent set I of the source constraint graph F with |I|>=k/4 (degree<=3). Fix one permissible original value c_i for each i in I, and restrict B to rows/columns (i,c_i,t), i in I, t in Z_T. After changing tag coordinates by beta_i, the restricted matrix equals
  (J_|I|-I_|I|) tensor (J_T-I_T).
For any field of characteristic >k, both factors have full rank when |I|,T>=2, since det(J_d-I_d)=(-1)^(d-1)(d-1). Hence rank(B)>=|I| T=Omega(k^2), while B has dimension N x N, N<=k^2. Thus rank is linear in the matrix dimension up to a constant factor.

## Boolean rectangle-cover lower bound

Because F has maximum degree 3 and Omega(k) nontrivial edges, it has an induced matching M of Omega(k) edges. For each e=(i,j) in M, choose a forbidden local pair (c_i,c_j) not in R_e, and choose tags t_i=beta_i and t_j=beta_j (common global tag s=0). The corresponding entry of B is 1, while the cross entries for two different induced-matching edges are 0 (their group pairs are nonedges of F and their tags are consistent). Thus B contains an identity submatrix of order Omega(k), and its Boolean 1-rectangle cover number is Omega(k). Therefore a polylogarithmic rectangle cover is impossible.

## Why no polynomial-time decision algorithm follows

The family is NP-hard by reduction from bounded-degree binary CSP. Therefore a polynomial-time algorithm for these dense graphs would imply P=NP. This does not prove any exponential lower bound on the parameter k. The sparse compiler is not an arbitrary dense-Clique compiler: it exploits an explicit globally consistent permutation/transport layer and a genuinely sparse hard residual.

## Generalization to non-flat groupoid synchronization

Let T be a polynomial-size tag set and for each ordered pair i,j a permutation pi_ij of T (pi_ji=pi_ij^{-1}), and suppose all pairs of groups demand t_j=pi_ij(t_i). Fix a root vertex 1. For each z in T, set t_1=z and t_i=pi_1i(z). In polynomial time enumerate the set
  Z={z in T: pi_ij(t_i)=t_j for every pair i,j}.
If Z is empty, the whole instance is NO. If Z is nonempty, all globally feasible tag choices are parametrized by one z in Z. In the presence of arbitrary additional pair constraints only on a sparse set F of O(k polylog k) group pairs, every local condition can be evaluated as a binary relation on ((c_i,z),(c_j,z)); equality of z is propagated along a spanning tree. Hence one gets an exact sparse 2-CSP with O(k+|F|) constraints, alphabet |T| max_i |D_i|, and degree <=3 after splitting copies. This works without flatness, but the extra non-permutation constraints MUST be sparse. In the flat case pi_ij=pi_1j pi_1i^{-1}, Z=T.

## Algorithmic recognition of a broader sparse relational basis

Given a *candidate* sparse constraint subgraph F of a dense binary CSP, for every omitted pair (i,j), choose a path P in F. Compose its edge relations along P by Boolean matrix multiplication to obtain R_P(i,j). If R_P(i,j) is a subset of the omitted original R_ij for every omitted pair, every satisfying assignment of the sparse CSP automatically satisfies all omitted constraints, hence removing them preserves exactly the set of solutions. Inclusion tests take polynomial time for Q=poly(k), supplied F and paths. In the constructed gauge example, the spanning-tree path enforces exactly the transport part. The method is a standard consequence of relational composition/path-consistency, not a newly invented theorem. The OPEN challenge is to discover a small basis or use additional existential auxiliary codes for arbitrary Clique constraints, rather than for an instance with a planted transport structure.

## Important research interpretation

- Major positive result: explicit examples show that near-maximal matrix rank, large Boolean rectangle cover, and NP-hardness can coexist with O(k) sparse 2-CSP encoding, on graphs of <=k^2 vertices.
- Major limitation: no progress yet toward a compiler applicable to arbitrary Clique; a random k-partite graph generally has no obvious globally consistent transport layer.
- Next attack: characterize and algorithmically find sparse *relational generators* of a dense compatibility system, allowing input-dependent hidden states and more general noninvertible relations. A sharp dichotomy between cheap generation and hardness under PSCH would be interesting, but is currently conjectural.

Literature pointers:
* Karthik–Marx–Pilipczuk–Souza, Conditional lower bounds for sparse parameterized 2-CSP: https://par.nsf.gov/servlets/purl/10545202
* Guruswami–Lin–Ren–Sun–Wu, STOC 2025 parameterized CSP/parallel PCP: https://doi.org/10.1145/3717823.3718130
* Standard relational composition/path consistency: https://bista.sites.dmi.unipg.it/didattica/CSP/CPschool05notes.pdf

---

# 2026-11-02, Branch B — Existential permutation-network compression, a critical NO instance, and limits

## Summary/status

PROVED (elementary, standard switching network theorem as external ingredient). An input-independent Beneš permutation network gives an exact **existential extension** of the global AllDifferent constraint on k variables using O(k log k) binary CSP constraints, polynomial alphabet and maximum degree <=3. Combining this with path-adjacency yields an NP-complete family of dense binary CSPs whose O(k^2) pairwise inequalities are individually critical to satisfiability for a specified NO instance, yet admits O(k log k) constraint compilation. This does not give a universal dense-to-sparse compiler for arbitrary Clique and is not claimed as literature-novel.

## Exact Beneš AllDifferent extension

For k variables x_1,...,x_k taking values from [k], write AllDifferent as inequalities x_i!=x_j on every pair. Set p=2^{ceil(log2 k)}, pad the input list with fixed distinct symbols k+1,...,p, and require the p output wires to carry 1,...,p in order. An explicit rearrangeably nonblocking Beneš network on p wires consists of O(p log p)=O(k log k) 2-by-2 switches, each either straight (a,b)->(a,b) or crossing (a,b)->(b,a). This network can route every permutation. Because switches preserve the global multiset, such settings exist iff x_1,...,x_k contain every symbol of [k] once.

Encode each switch with an auxiliary state variable carrying its 4 input-output port symbols, alphabet [p]^4, constrained by the unary switch predicate. A binary relation between a switch's state and a wire value enforces equality of the relevant port. Every switch variable initially has four port incident edges; split into four equal-valued copies arranged along a path (3 equality links), attach one original port to each copy. New degrees <=3, and a unary switch predicate can be put on an endpoint clone or encoded via a fixed singleton helper. Source x_i and output wires similarly have constant degree. Total O(k log k) variables/constraints, common alphabet Q=O(k^4) after allowed-domain typing, deterministic polynomial construction. All solutions project *exactly* to AllDifferent assignments, but a given input tuple can have many switch-setting extensions.

This contrasts with earlier fixed nonlinear-code no-go: the switch settings and internal wire values are independent existential variables, not functions E_i(x) fixed in advance. For this switching model, Omega(k log k) Boolean switch controls are necessary to support all k! permutations (2^s >= k!), so network size is asymptotically optimal in its restricted two-state switch model.

References: https://homepages.inf.ed.ac.uk/rni/comp-arch/Networks/benes.html ; https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/tje2.12037

## NP-complete dense CSP with Theta(k^2) individually critical constraints

For arbitrary simple undirected H on k vertices, introduce position variables x_1,...,x_k with domain V(H), and constraints:
(i) R_{i,i+1}(x_i,x_{i+1}) = [x_ix_{i+1} in E(H)] for i=1,...,k-1;
(ii) x_i != x_j for all 1<=i<j<=k with j-i>=2.
Since H is loopless, adjacent positions are automatically distinct. This system is satisfiable iff H has a Hamiltonian path. This is an NP-complete family (standard). The source contains Theta(k^2) binary constraints. Replace all nonlocal inequalities with the above existential Beneš network and keep the k-1 adjacency constraints. Thus an exact bounded-degree 2-CSP extension with O(k log k) constraints and Q=O(k^4), uniformly polynomial-time, preserves all position tuples.

Stronger irredundancy test: choose the NO instance H=K_{k-1} disjoint_union K_1. No Hamiltonian path exists. For any nonconsecutive pair i<j, j-i>=2, remove the single inequality x_i != x_j. Assign distinct vertices of the K_{k-1} to all k positions except put the same clique vertex at positions i and j, using all k-1 clique vertices. Because i,j are nonconsecutive, adjacent positions are distinct and hence adjacent in K_{k-1}; every other nonlocal inequality holds. The modified instance is YES. So all binom(k,2)-(k-1)=Theta(k^2) nonlocal constraints are individually critical to UNSAT of this NO instance, yet the entire relation is exactly represented by O(k log k) constraints with auxiliary states. Note: this does not assert the remaining k-1 path constraints are individually critical.

This shows that sampling/deleting original constraints may be impossible even though global existential binary compilation of the full solution relation is easy. It also demonstrates the 'global invariant + local residual' mechanism without reducing NP-hardness to a previously hard sparse residual: the path-adjacency residual alone is easy (existence of a walk), while its conjunction with AllDifferent is NP-hard.

Relevant CSP modeling reference: https://ozanerdem.github.io/jekyll/update/2019/12/01/representation-in-csp.html

## Why this does NOT solve universal k-Clique

The network compresses pairwise distinctness because all k(k-1)/2 comparisons jointly express one multiset invariant: 'the selected labels form a permutation of [k]'. Arbitrary per-pair compatibility relations R_ij have no such known invariant. Routing two selected tokens through a switch and testing their R_ij compatibility directly still requires Omega(k^2) pair encounters in a natural restricted token-routing model (one can compare a YES all-compatible instance to the instance deleting a single chosen pair, keeping a valid routed witness). Such a no-go MUST restrict the only input dependence to the actual pair-comparison gates; arbitrary globally preprocessed relations can invalidate the argument.

Further structural condition: a single evolving state of size poly(k) with polynomial-time computable transitions and O(k polylog k) steps would imply a polynomial-time DP for the resulting family, so universal NP-hard compression cannot be only a polynomial-state sequential aggregate. The permutation network succeeds by having many interacting local states simultaneously.

Concrete open target: is there a polynomial-time compiler for unrestricted k x k Multicolored Clique (and hence ordinary k-Clique N<=k^2) to binary CSP with m=O(k polylog k), alphabet Q=k^{O(1)}, maximum degree <=3, using genuine existential local witnesses and input-dependent relations? No such compiler was obtained. Do not conflate this with proving a PSCH consequence: a polynomial-time reduction from ONLY the multicolored restricted subclass is not automatically a reduction from general ordinary k-Clique unless a size-controlled transformation is also provided.

## Relation to branch A

Branch A (fast polynomial-size Clique => E^NP general circuit lower bounds) remains unaffected. This constructive branch B example is a proof-technique sanity check, not a circuit lower bound or a new fine-grained reduction. Maintain both branches separately.