# CEH / Fixed-Expander CSP — main research checkpoint (2026-11-02)

**Canonical closure registry:** [What the new CSP algorithms refute, and what survives](../34_csp_hypothesis_closure_registry_2026_11_02.md). This historical notebook does **not** support an active CEH hardness hypothesis under the stated new algorithms.

> **STATUS UPDATE — 2026-11-02: CEH AND ITS SPACH MOTIVATION CONDITIONALLY REFUTED.** If the general Boolean tensor-contraction theorem in the October 25 OpenAI manuscript is correct, every fixed-cubic-expander instance below (indeed any sparse explicit polynomial-alphabet binary CSP) is deterministically solvable in \(q^{o(K)}\operatorname{poly}(|I|)\) time. **The CEH hardness conjecture and the CEH-based conditional lower bounds in §2 should therefore be regarded as CLOSED under this premise.** The fixed-topology compilation problem, reductions, and matching-compiler barriers are *not* disproved and are retained as historical constructions. The general tensor theorem itself is NOT among the results explicitly covered by the published Lean-scope note. Details: [tensor contraction and branch triage](../33_tensor_contraction_sparse_2csp_and_hardness_triage.md).


> **Research log, not a theorem announcement.** This is the CEH branch of the 2026-11-01/02 HOM / hardness conversation. It is separate from the PCC/Circuit-SAT work elsewhere in the repository. A number of later linear-coding and separator claims were derived in chat but have **not** passed independent audit; see [03_audit_and_next_steps.md](03_audit_and_next_steps.md).

## 0. Main objective (the strong version only)

Let $F_K$ be an **explicit, predetermined** family of bipartite cubic edge expanders, with a fixed positive expansion constant. Let $q=\lceil K^c\rceil$, for some **fixed** $c>0$. An instance gives an arbitrary relation $R_{uv}\subseteq [q]^2$ on each edge $uv\in E(F_K)$; decide if there is an assignment $x\in[q]^{V(F_K)}$ satisfying them all. The relations are represented explicitly.

**Colored Expander Hypothesis (CEH, proposed):** For some fixed $c>0$, this problem admits no *uniform* $q^{o(K)}\operatorname{poly}(|I|)$-time algorithm, equivalently no $2^{o(K\log K)}\operatorname{poly}(|I|)$-time algorithm in this regime. State deterministic and bounded-error randomized versions separately (randomized hardness is stronger).

**Sparse Polynomial-Alphabet CSP Hypothesis (SPACH, proposed):** The same bound for binary CSP on $k$ variables, $m=O(k)$ constraints, $q=k^c$, and bounded-degree constraint graph (maximum degree 3 is a convenient normal form; the exact requirement of *simple bipartite 3-regularity* needs careful preprocessing). The formulation already appears in [../13_log_width_sat_and_polynomial_alphabet_csp.md](../13_log_width_sat_and_polynomial_alphabet_csp.md).

**Research target:** Give a polynomial-time, decision-preserving reduction

$$
\text{arbitrary sparse binary 2-CSP}(k,q)
\longrightarrow
\text{binary 2-CSP on predetermined }F_{K}(K=O(k),q'=k^{O(1)}),
$$

with explicit relations, $K=O(k)$, and $\log q'=O(log k)$. (More quantitatively, constants in alphabet growth must be independent of (k).)

Then CEH and SPACH become equivalent **as hardness hypotheses** at scale $2^{o(k\log k)}$: CEH already implies SPACH because fixed-expander instances are a subclass; the sought reduction gives the converse. No such reduction has been found.

**Not our target:** merely excluding $2^{O(k)}$; optimizing auxiliary symbol count $C=5$ versus (6); proving hardness from Clique or Circuit-SAT (those are separate branches).

## 1. Why the source changed

The previous HOM project started from bounded-degree sparse 3-COL; its ETH-based lower bound is no longer a reliable hardness source if the October 2026 SAT algorithm claims hold. A dense 3-COL instance on $N$ vertices has a 3-CNF encoding with $3N$ Boolean variables and $O(N+M)$ clauses of width at most 3. Thus a uniform fixed-width $2^{o(n)}$ algorithm also applies to dense 3-COL. Sparse-vs-dense 3-COL does not repair the ETH-based argument.

By contrast, binary CSP with $k$ variables over $q=k^c$ has the exact direct CNF encoding

$$
n_\mathrm{SAT}=k\lceil\log_2q\rceil,\quad
w_\mathrm{SAT}\le 2\lceil\log_2 q\rceil,\quad
m_\mathrm{SAT}=O(kq^2),
$$

so the width grows as $\Theta(log k)$. The presently discussed fixed-width SAT statements do not directly yield $q^{o(k)}$ for such CSP. This is **absence of an identified contradiction**, not evidence of hardness or an exhaustive algorithm survey.

## 2. Direct implications of CEH (conditional hardness)

A CEH instance has $K$ variables and $3K/2$ binary constraints. The reductions below preserve the relevant solution parameter $K$, while the target input sizes grow polynomially in $K$.

| Target | Reduction / parameter | What CEH conditionally rules out |
|---|---|---|
| 2-degenerate graph HOM (as in our HOM paper §4, subject to checking precise gadgets) | source $n=\Theta(K)$, target $h=O(Kq^2)=\operatorname{poly}(n)$ | $h^{o(n)}\operatorname{poly}(n,h)$ |
| $K$-Independent Set | vertices $Kq$; clique for each variable plus edges for forbidden pairs | $2^{o(K\log K)}\operatorname{poly}(N)$ |
| $K$-Set Cover | $Kq$ sets; universe $O(Kq^2)$ | same parameterized time |
| $K$-Dominating Set | $O(Kq^2+K^2)$ graph vertices | same |
| $K$-Set Packing | one set per IS vertex, one shared universe element per IS edge | same; universe elements appear in at most 2 sets |
| Hitting Set | standard dual of Set Cover | same |
| fixed-pattern database join nonemptiness / Boolean tensor-network satisfiability | exact reformulation as $\bigwedge_{uv\in E(F_K)}R_{uv}(x_u,x_v)$ | $q^{o(K)}$ algorithms for this family |

### Parameter-safe gadget descriptions

**Independent Set.** Create one vertex ((v,a)) per $v\in V(F_K),a\in[q]$. Each fiber ${(v,a):a\in[q]}$ is a clique; link ((u,a),(v,b)) whenever $uv\in E(F_K)$ and $(a,b)\notin R_{uv}$. Independent set of size $K$ iff CSP SAT.

**Set Cover.** A set $S_{v,a}$ for each choice. Element $u_v$ lies in exactly the $q$ sets of variable $v$. For each forbidden pair ((a,b)) on (uv), add element $e_{uv,a,b}$ lying in all $S_{u,a'}$ with $a'\ne a$ and all $S_{v,b'}$ with $b'\ne b$. Budget $K$ forces one set per variable; forbidden pairs leave an element uncovered.

**Dominating Set.** A $q$-clique per variable; (K+1) independent guards adjacent only to that clique force one chosen clique vertex per variable if domination budget is $K$. Add one guard for each forbidden ((a,b)), adjacent to all other vertices of the two associated cliques. These can be dominated iff no forbidden pair is selected. Guards have no mutual edges.

**Set Packing.** Independent Set $\to$ sets indexed by graph vertices, with one element for every conflict edge, present in exactly its two endpoint sets.

**Important qualification:** a $2^{o(N)}$ algorithm with $N=\operatorname{poly}(K)$ does **not** refute CEH. E.g. the IS graph has $N=Kq$, giving only $2^{o$Kq$}$. Also bounded-average-degree IS is not a useful target for CEH hardness at parameter $K$: when $M\le CN$, Caro–Wei gives $\alpha(G)\ge N/(2C+1)$, hence $K$-IS can be decided in $2^{O_C(K)}\operatorname{poly}(N)$.

### Direction of implications

The reductions are **CEH instance -> target instance**. Thus a fast general target algorithm refutes CEH, but a fast algorithm for CEH does *not* imply a fast algorithm for IS / Set Cover / HOM or arbitrary sparse CSP. This direction issue is essential.

## 3. Positive reductions and the exact missing ingredient

**A. Arbitrary sparse binary CSP -> bounded-degree CSP.** Make one occurrence-port for each constraint endpoint, connect copies of each variable by equality constraints (cycles/chains); one original binary relation is checked by its paired occurrence-ports. $O(k+m)$ variables/constraints, same $q$, maximum degree at most 3; isolated variables handled separately. A particularly clean form on $2m$ ports is

$$
C_{2m}\cup M,
$$

with a fixed cycle whose arcs enforce equality inside each variable block (universal relations between blocks), plus one arbitrary perfect matching $M$ carrying the original constraints. This is a **normal form**, not an expander and not a fixed topology.

**B. Arbitrary sparse CSP -> an input-dependent cubic expander.** Overlay a fixed constant-degree expander on the original variable set using tautological relations, then split each variable into a constant-size equality cycle with one external port per incident original/expander edge; pad unused ports. This has $O(k)$ variables, same alphabet, cubic constraint graph with positive expansion. The resulting cubic expander still depends on the instance. A direct expansion proof is required when choosing the precise port gadget; see [01_reductions.md](01_reductions.md).

**C. Arbitrary sparse CSP -> one fixed, expanding but not bounded-degree graph.** Use a known universal graph for maximum-degree-3 graphs with $O(k)$ vertices, $O(k^{4/3})$ edges and a computable embedding (the Alon–Capalbo universal-graph route, exact citation/algorithm to re-check). Put original relations on embedded edges, universal relations on all unused edges, and superimpose a predetermined expander. This yields $K=O(k)$, $q'=q$, fixed topology, but superlinear edge count and nonconstant maximum degree. This route also requires bibliographic/constructivity verification before theorem use.

**D. Minor-universal fixed bounded-degree expanders.** A generic graph-minor realization has $K=O(k\log k)$, and equality along branch sets preserves $q$. It does *not* give the desired $K=O(k)$; a CEH algorithm merely running in $q^{o(K)}$ may still take $q^{o(k\log k)}$ after such a reduction. A stronger algorithm, say $q^{O(K/log^{1+\varepsilon}K)}$, would yield $q^{o(k)}$ for arbitrary sparse CSP, *assuming an efficiently findable minor model*.

The unsolved problem is to obtain **fixed topology and constant degree simultaneously** at $O(k)$ variables, using a polynomial domain and **only satisfiability equivalence**; there is no requirement to preserve every original variable's value.

## 4. Failed / incomplete stronger models

A large subproject asked for an **exact permutation compiler** for arbitrary matching $M$: every input array $a$ should extend to local states on one fixed cubic expander, with public outputs satisfying $b_v=a_{M(v)}$, and no incorrect outputs allowed. This is sufficient for a reduction but much stronger than decision-preserving CSP compilation.

Explored: equality routing ($O(\log K)$ congestion, domain $q^{O(\log K)}$ is quasipolynomial); linear and nonlinear encoding; matrix rank conditions; Schur complements; invertible transfer matrices and monodromy; fixed-dimension local subspaces $W_v$; edge-interface and separator bounds; specifically $C=3,4,5,6$ local coordinates; Hamiltonian cycle + fixed matching, with a 3/2 interface profile; mixed profiles. See [02_matching_compiler_research_log.md](02_matching_compiler_research_log.md).

**No universal fixed-topology polynomial-domain compiler was constructed.** Several purported no-go theorems are only *chat-derived, model-specific claims* and should not be relied on until audited. In particular, proving a fixed $C=5$ gadget impossible would not establish impossibility of the main reduction.

## 5. Separate random-instance probe (not hardness)

On cubic $F_K$, take each allowed pair on an edge independently with probability $p=q^{-2/3}$. Then the number $Z$ of solutions satisfies the exact identity

$$
\mathbb E Z=q^K p^{3K/2}=1.
$$

For any $S\subseteq V(F_K)$, expected satisfying assignments of the induced CSP:

$$
\mathbb E Z_S=q^{|S|}p^{|E(F_K[S])|}=q^{|\partial S|/3}.
$$

The chat additionally derived a second-moment formula and claimed convergence $Z\Rightarrow\operatorname{Poisson}(1)$ for sufficiently large $c$ compared with the expansion constant. These proofs have **not been independently audited**, and any average-case algorithmic inference is OPEN. See [01_reductions.md](01_reductions.md).

## 6. Most valuable next step

Find an **existential/decision-preserving** compilation of an arbitrary degree-3 sparse CSP into a predetermined bounded-degree expander using $O(k)$ variables and $k^{O(1)}$ domain. Do *not* mandate exact permutation realization or a specific number of internal coordinates.

Candidate workflows: $i$ leverage a moderately high-degree fixed universal graph plus a constraint-specific batch compression, while keeping its full parameter budget; (ii) group many checks algebraically using existential witnesses without false positives; (iii) pursue conditional impossibility for tightly defined reduction models, not for arbitrary reductions. Every proposal needs exact SAT iff, explicit table-size construction bound, target $K$, alphabet $q'$, uniformity, and audit of randomized error if any.

See [01_reductions.md](01_reductions.md), [02_matching_compiler_research_log.md](02_matching_compiler_research_log.md), and [03_audit_and_next_steps.md](03_audit_and_next_steps.md).


## 7. New constructive bridge: universal factor graphs and sorting (2026-11-02)

A new explicit **logarithmic-overhead**, fixed-topology reduction was reconstructed using a word-level oblivious sorting network (compare Feige–Jozeph 2012). Arbitrary $m=O(k)$ binary relations can be represented as $2m$ labeled occurrence records, sorted by variable label, with local equality checks on adjacent equal keys. This yields a fixed bounded-degree constraint graph of $O(k\log k)$ vertices and polynomial alphabet; overlaying a fixed expander and using an even-cycle port replacement yields **one predetermined simple bipartite cubic expander** of $K=O(k\log k)$ vertices. The reduction is polynomial-time, SAT-iff, and avoids searching for minors. See [04_universal_factor_graph_sorting_bridge.md](04_universal_factor_graph_sorting_bridge.md) for the construction, expansion argument, comparison with published UFG, and exact conditional runtime transfer.

The $\Omega(k\log k)$ size bound for literal 2-by-2 switching/sorting networks is a barrier **only for that architecture**, not for nonlinear/algebraic or decision-only compilers. We still need $K=O(k)$ for full CEH–SPACH equivalence.


## 8. New algebraic normal form: one tagged product identity (2026-11-02)

Given arbitrary sparse binary CSP, create $t=2m=O(k)$ occurrence variables, retain the original $m$ pairwise local relations, and let $\sigma$ cycle the occurrences of each original variable. For a prime $p>tq$, use injective pair tags $h(i,a)=iq+a\in\mathbb F_p$. The complete copy-consistency condition is **exactly**
\[
\prod_i(X-h(i,a_i))\equiv\prod_i(X-h(\sigma(i),a_i))
\]
as a *formal univariate polynomial identity*. Thus all input-dependent topology is encoded in local tag constants; only one global algebraic identity remains. This does **not** by itself yield a fixed cubic expander reduction. Single-point grand-product evaluation has adaptive-witness false positives; a one-pass exact nondeterministic accumulator needs exponentially many states, while an expander may have enough distributed cut capacity. Full proof, explicit finite-field counterexample, caveats and the next exact verifier subproblem: [05_tagged_product_identity.md](05_tagged_product_identity.md).
