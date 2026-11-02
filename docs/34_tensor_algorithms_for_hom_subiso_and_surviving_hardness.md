# Post-ETH tensor algorithms for HOM/SubISO and surviving hardness scales

**Date:** 2026-11-02  
**Status:** Research checkpoint. Elementary reductions PROVED. Fast runtimes CONDITIONAL on externally claimed tensor counting algorithms, not independently audited here. No new general-purpose CSP or Circuit-SAT algorithm and no new proven lower bound.

## 0. Premises and precise attribution

1. **Nguyen, "A Sublinear Treewidth Exponent for Binary Constraint Satisfaction", 2026-11-02, Theorem 1.2:** claims a deterministic exact counter for complete-table binary CSP on \(K\) variables, alphabet \(q\ge2\), maximum primal degree at most any fixed \(\Delta\), in \(L^{O_\Delta(1)}q^{O_\Delta(K/\sqrt{\log K})}\). The constant is uniform in \(q\). Its result imports the weighted/signed tensor-network recursion of **Claude (Anthropic)** and foundations from OpenAI. The downstream Lean formalization and upstream import boundary require independent audit.
   Source: https://hexagonmath.org/2611.00004v1
   Previous audit: [note 22](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md).
2. **OpenAI 2026 full Boolean tensor-contraction theorem:** conditional \(2^{O(M/\sqrt{\log M})}\) scalar contraction for networks with \(O(M)\) bit-wires and suitable local entry and ring assumptions. Not included in the specifically listed Lean formalization of fixed-width #CNF.
   Source: https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex
   Earlier audit: [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).
3. **Jizhou Guo, "Conditional consequences of a Boolean tensor-contraction theorem: threshold circuits and sparse connectivity", v2, 2026-10-30:** already derives deterministic \(2^{O(N/\sqrt{\log N})}\) algorithms for Hamiltonian cycles/paths, TSP, FVS, Steiner tree, connected vertex cover and connected dominating set on \(O(N)\)-edge graphs, assuming the full tensor theorem. A distinct *randomized* Cut&Count/isolation route requires only the weaker Lean-scoped fixed-width #3-SAT counting theorem and gives \(2^{O(N(\log\log N)^2/\sqrt{\log N})}\). **These are existing conditional reductions, NOT discoveries of the present notebook.**
   Source: https://github.com/aster2024/openai-math-followups/tree/main/tensor-contraction-consequences

We use \(\log(2+x)\) instead of \(\log x\) when small instances matter. Polynomial factors account for complete relation tables and integer-output arithmetic. The asymptotic bounds are not claimed to be practical for relevant input sizes.

## 1. Counting HOM on a sparse source graph — conditional

Let \(G\) be a simple pattern/source graph with \(n\) vertices, \(m\) edges, and \(H\) a simple target graph with \(h\ge2\) vertices. The count \(\#\mathrm{HOM}(G,H)\) is exactly the number of assignments \(f:V(G)\to V(H)\) satisfying one explicit relation \(A_H(f(u),f(v))=1\) per source edge. Common-list variants are unary restrictions.

If \(\deg_G(v)=d>0\), replace \(v\) by \(d\) occurrence copies. Connect them with \(d-1\) binary equality constraints along a path, and attach one original adjacency constraint to each occurrence. Isolated vertices stay as unary-domain variables. There are at most \(n+2m\) variables, at most \(3m\) binary edges, and maximum primal degree at most 3. Each original homomorphism extends **uniquely** to an occurrence-copy assignment. The new common alphabet remains \([h]\), and equality plus adjacency relations have explicit tables of size \(O(h^2)\), so the complete representation is polynomial in \(|G|+|H|\).

**Consequence (if Nguyen Theorem 1.2 is correct):**
\[
  \boxed{\#\mathrm{HOM}(G,H)\text{ computable in }
   \operatorname{poly}(|G|,|H|)\,
   h^{O((n+m)/\sqrt{\log(n+m)})}.}
\]
Compare with direct enumeration \(h^n\); take the minimum. For \(m=O(n)\), \(h=n^{\Theta(1)}\), the new claimed bound is \(2^{O(n\sqrt{\log n})}\). The reduction does not depend on \(\operatorname{degen}(H)\). It also applies to **list homomorphisms** and their counts, via unary domains.

For a connected source \(G\), each image lies in one connected component of \(H\). If the largest such component has size \(h_{\max}\), we may count homomorphisms separately into each component at cost \(\operatorname{poly}(|H|)\,h_{\max}^{O((n+m)/\sqrt{\log(n+m)})}\); this can be substantially smaller than the bound in total \(h\).

## 2. New-to-this-notebook transfer: sparse Subgraph Isomorphism from #HOM

Let \(G\) have \(n\) vertices and \(m\) edges; \(H\) have \(h\ge n\) vertices. We want an **injective edge-preserving** map \(G\hookrightarrow H\), not an induced embedding.

Choose a coloring \(\chi:V(H)\to[n]\). For \(S\subseteq[n]\), define \(H_S=H[\chi^{-1}(S)]\) and compute
\[
 Z_\chi=\sum_{S\subseteq[n]}(-1)^{n-|S|}\#\mathrm{HOM}(G,H_S).
\]

For a homomorphism \(f\), its contribution is
\[
 \sum_{S\supseteq\chi(f(V(G)))}(-1)^{n-|S|}
 = \begin{cases}1&\text{if its image uses all }n\text{ colors},\\0&\text{otherwise.}\end{cases}
\]
There are exactly \(n\) pattern vertices, so a homomorphism using all \(n\) colors is injective. Thus \(Z_\chi\) equals the **nonnegative integer** number of \(\chi\)-colorful subgraph embeddings.

For any fixed embedding \(f\), a uniformly random coloring is injective on its \(n\) images with probability \(n!/n^n=e^{-O(n)}\). Testing \(e^{O(n)}\) independent colorings is a one-sided Monte Carlo decision algorithm with constant success probability (never false YES). Alternatively the classical \(n\)-perfect hash families of Alon–Yuster–Zwick provide deterministic \(2^{O(n)}\operatorname{poly}(h)\) colorings.

Each coloring requires \(2^n\) exact #HOM calls; consequently:

**Consequence (conditional on Nguyen or OpenAI tensor theorem in the polynomial-domain regime):**
\[
 \boxed{
 T_{\mathrm{SubISO}}(G,H)
 =2^{O(n)}
 h^{O((n+m)/\sqrt{\log(n+m)})}
 \operatorname{poly}(|G|,|H|).
 }
\]
For \(m=O(n)\) and \(h=n^{\Theta(1)}\), this is \(2^{O(n\sqrt{\log n})}\); derandomization is possible using known perfect hash families. The method handles any target degeneracy.

**Do not extend this proof to induced SubISO:** requiring nonedge preservation adds up to \(\Theta(n^2)\) constraints on a sparse pattern. The method does not imply a comparable bound for induced embeddings.

The color-coding technique is classical; the only present observation is combining it quantitatively with the newly claimed #HOM upper bound. Reference: Alon–Yuster–Zwick, *Color-coding*, JACM 1995, https://www.math.tau.ac.il/~nogaa/PDFS/col5.pdf

## 3. A hardness scale compatible with the claimed algorithm

Old SPACH / CEH forbid \(q^{o(k)}\) on \(k\)-variable polynomial-domain sparse CSP. They are **conditionally refuted**, see notes 22/33.

A **new proposed** candidate, here called **SqrtLog-SPACH**, is:

> There exists a fixed \(c>0\) such that explicit binary CSP with \(k\) variables, a **simple bipartite 3-regular** constraint graph, and \(q=\lceil k^c\rceil\) admits no uniform deterministic \(q^{o(k/\sqrt{\log k})}\operatorname{poly}(L)\)-time decision algorithm.

State a separate randomized-hardness variant if needed; deterministic vs randomized hardness must not be conflated.

This does not conflict with Nguyen's claimed \(q^{O(k/\sqrt{\log k})}\) upper bound. Under the candidate, a matching worst-case lower bound would identify the exponent up to constants, although there is **no proof** and the truth of the candidate is entirely open.

**Verified transfer to polynomial-target 2-degenerate HOM:** Theorem 4.2 of Braulov–Chukhin–Kulikov–Mihajlin, [*Complexity of the Graph Homomorphism Problem w.r.t. Degeneracy*](https://arxiv.org/html/2607.09377v1), applies *precisely* to binary CSP on a **simple bipartite 3-regular** constraint graph. It constructs in polynomial combined input/output size an equivalent HOM instance with
\[
 n=|V(G)|=\Theta(k),\quad |E(G)|=O(k),\quad
 \operatorname{degen}(H)\le2,\quad
 |V(H)|+|E(H)|=O(kq^2).
\]
The theorem's published ETH hardness conclusion no longer supplies hardness after the 2026 SAT refutations, but the reduction and parameter bounds are unconditional. Substituting the **new, unproved** SqrtLog-SPACH-BIP3 assumption, a uniform \(h^{o(n/\sqrt{\log n})}\operatorname{poly}(|G|,|H|)\) HOM algorithm on those instances would give \(q^{o(k/\sqrt{\log k})}\operatorname{poly}(k)\) for the source, a contradiction; in particular \(2^{O(n)}\operatorname{poly}(|G|,|H|)\) would be excluded. This exactly matches the *form* of Nguyen's conditional upper bound for this class, up to constants in the exponent, but it is **not** a proven lower bound.

One may separately hypothesize **SqrtLog-CEH** on a predetermined cubic expander. It is *stronger as a hypothesis* than unrestricted SqrtLog-SPACH; the known logarithmic-overhead fixed-expander compilation is not enough to transfer the matching \(\sqrt{\log}\)-scale between them. Do not label them equivalent.

## 4. Quantitative hard-source compiler thresholds

Let PCC(K) be permutation \(K\times K\) Clique. Assume a separate no-\(2^{o(K\log K)}\) PCC hardness hypothesis. A polynomial-time, decision-preserving (or appropriately randomized, under randomized PCC hardness) PCC \(\to\) degree-3 CSP compiler with polynomial alphabet \(q'=K^{O(1)}\), \(k'+m'=O(K\sqrt{\log K})\) would imply SqrtLog-SPACH **for the compiler output subclass**, and hence for the general class, provided the output domains meet the selected fixed-exponent regime after harmless padding. Indeed \(k'/\sqrt{\log k'}=O(K)\), so a \(q'^{o(k'/\sqrt{\log k'})}\) algorithm would solve PCC in \(2^{o(K\log K)}\) time.

By contrast, \(k'+m'=o(K\sqrt{\log K})\) is *incompatible* with PCC hardness AND Nguyen's claimed CSP algorithm. The former linear-size PCC compiler is closed **as a hardness transfer route under these simultaneous premises**, not unconditionally as a mathematical construction. The old Beneš AllDifferent gadget has \(O(K\log K)\) size and does not by itself achieve the new target, nor does it handle arbitrary dense PCC adjacency constraints.

For **unrestricted polynomial-size Circuit-SAT**, let \(s\) be the number of primary inputs, \(\operatorname{size}(C)\le s^d\). Suppose a no-\(2^{o(s)}\) Circuit-SAT hypothesis holds. An input-efficient SAT-iff compiler into binary CSP with \(r=k'+m'\) and \(q'=s^{O_d(1)}\) has the new algorithm's time \(2^{O(r\log s/\sqrt{\log r})}\) when \(r\) is polynomial and nontrivial. Therefore \(r=o(s/\sqrt{\log s})\) is incompatible with both the tensor bound and Circuit-SAT hardness; \(r=O(s/\sqrt{\log s})\) is the **quantitatively tight unexcluded target**. If such a compiler existed with a checked \(n_{\mathrm{HOM}}=O(r)\), \(h=\operatorname{poly}(s)\) reduction, a \(2^{O(n_{\mathrm{HOM}})}\) HOM algorithm would refute Circuit-SAT hardness, but the tensor upper bound would only give \(2^{O(s)}\).

## 4a. Direct attempt to exploit target degeneracy: four functional edge types

A \(2\)-degenerate loopless target \(H\) has an acyclic orientation with outdegree at most two. Partition each vertex's outgoing neighbors into two slots, giving partial functions \(f_1,f_2:V(H)\rightharpoonup V(H)\). For any two *ordered* vertices \(a,b\),
\[
 \boxed{
 A_H(a,b)=[f_1(a)=b]+[f_2(a)=b]+[f_1(b)=a]+[f_2(b)=a].
 }
\]
Exactly **one** term is one if \(ab\in E(H)\); all terms are zero otherwise. This is an identity over \(\mathbb N\), not modulo two. For a source \(G\) with \(m\) edges, expanding the product of these adjacency factors produces at most \(4^m=2^{O(m)}\) nonnegative terms. Each term is a count of solutions of binary **functional** constraints of the form \(x_v=f_i(x_u)\) or \(x_u=f_i(x_v)\).

**Conditional algorithmic target:** If this special two-global-function satisfiability/counting problem could be solved in \(\operatorname{poly}(n,h)\) time *for the functional instances arising in the expansion*, we would obtain a \(2^{O(m)}\operatorname{poly}(|G|,|H|)\) counting algorithm for HOM into 2-degenerate \(H\), and hence a \(2^{O(n)}\) algorithm on sparse \(G\). The known \(\sqrt{\log}\) CSP upper does **not** achieve this.

**Exact obstacle: functional relations are not automatically easy.** Even two *globally shared* partial maps with unary lists can encode any binary CSP. Given \(\Gamma\) with variables \(x_v\in[q]\) and relations \(R_e\subseteq[q]^2\), define a common domain
\[
D=\{(v,a):v\in V,\ a\in[q]\}
 \ \cup\ \{(e,a,b):e=(u,v),\ (a,b)\in R_e\}.
\]
Let partial functions \(f_1,f_2\) map each \((e,a,b)\) to \((u,a)\) and \((v,b)\), respectively. For every original variable introduce \(X_v\) with unary list \(\{(v,a)\}\); for every original constraint introduce \(Z_e\) with unary list \(\{(e,a,b):(a,b)\in R_e\}\); enforce the two functional binary constraints
\[
X_u=f_1(Z_e),\qquad X_v=f_2(Z_e).
\]
Every original satisfying assignment extends **uniquely** by choosing the corresponding allowed pair for each \(Z_e\), and all functional solutions arise this way. The incidence graph has \(k+m\) vertices and \(2m\) edges; on cubic original CSP its maximum degree is three; \(|D|\le kq+mq^2\), polynomial for polynomial \(q\). Thus generic polynomial-time solving of two-global-function **list** CSP would solve all sparse explicit CSPs in polynomial time. This is a structural reduction, not a complexity lower bound under an unproved hypothesis.

**Research lesson:** a promising degen-2 algorithm must exploit more than "the target adjacency is a sum of four functional relations"; the functional subinstances retain arbitrary pair compatibility through shared preimages. Potentially valuable restrictions include no unary tags, bounded inverse fibers, or special correlations among the four functional summands. The unrestricted case is precisely the bottleneck.

## 4b. Exact source-SCC compression for functional constraints; expander obstruction

Let \(D=(V,A)\) be a directed graph, and each arc \(e:u\to v\) carry an arbitrary **partial** map \(f_e:[h]\rightharpoonup[h]\). We seek assignments satisfying \(x_v=f_e(x_u)\) on every arc, optionally with unary lists.

**Lemma (exact count by source SCCs).** Let \(\sigma(D)\) be the number of source strongly connected components in the condensation DAG. Then the number of solutions can be computed in
\[
  h^{\sigma(D)}\operatorname{poly}(|V|+|A|,h)
\]
time. In every source SCC choose a representative. Select a directed spanning **out-forest** rooted at these representatives covering all vertices: each SCC has an internal out-arborescence; every non-source SCC is reached from a predecessor. A vertex \(v\) is assigned a unique root \(r(v)\) and composition \(F_v\) of arc functions along its forest path. Every valid assignment has \(x_v=F_v(z_{r(v)})\); enumerate representative values and check all original equations (including definedness and lists). The extension is unique when it exists, hence exact counting. This statement also holds with different \(f_e\) on every arc.

**Source-SCC quotient.** Rather than enumerating, substitute all \(x_v=F_v(z_{r(v)})\). Every original arc \(u\to v\) yields a unary/binary relation
\[
  F_v(z_{r(v)})=f_e(F_u(z_{r(u)}))
\]
between at most two root variables; explicit tables are polynomial in \(h\). Call the resulting primal graph \(Q_D\). It is a minor of the undirected graph underlying \(D\): contract each connected out-tree to its root and discard internal edges. The quotient has \(\sigma(D)\) vertices, but need not have small treewidth.

For any orientation \(D\) of an undirected graph \(G\), \(\sigma(D)\le\alpha(G)\): distinct source SCC representatives are nonadjacent. This bound is tight **maximizing over orientations**: choose a maximum independent set \(S\), orient its incident edges outward, and orient the complement acyclically. Because \(S\) is maximal/dominating, precisely its vertices are source SCCs, so \(\max_D\sigma(D)=\alpha(G)\). Hence for a 2-degenerate target \(H\), expanding each target-edge indicator as four partial-function indicators yields an unconditional exact counting algorithm \(O(4^{|E(G)|}h^{\alpha(G)}\operatorname{poly})\). On sparse \(G\), Caro–Wei implies \(\alpha(G)=\Omega(|V(G)|)\); this does **not** beat the claimed tensor solver asymptotically.

**Counterexample: a single functional term can preserve expander treewidth.** Let \(C\) be any simple 3-regular graph on \(k\) vertices with positive edge expansion \(\varepsilon\), and give every edge \(e=uv\) an arbitrary CSP relation \(R_e\subseteq[q]^2\). Construct the 1-subdivision / incidence graph \(B\): one source node \(W_e\) per original edge, one sink node \(X_v\) per original vertex, and arcs \(W_e\to X_u,W_e\to X_v\) labeled 1,2. The alphabet is a disjoint union of variable labels \((v,a)\) and relation-witness labels \((e,a,b)\) for \((a,b)\in R_e\). Define two **global** partial functions
\[
 f_1(e,a,b)=(u,a),\quad f_2(e,a,b)=(v,b)
\]
using a fixed ordering of endpoints. Give \(W_e\) the unary list of \(e\)-witnesses and \(X_v\) the list of \(v\)-labels. Then a solution to these **two-global-function** constraints is in bijection with a solution of the original CSP. The undirected target with edges from each witness to its two endpoint labels is 2-degenerate: every nonisolated subgraph contains a witness of degree at most two, unless it contains only isolated variable labels. Thus one single functional term already represents generic cubic expander CSP (with unary lists).

All \(W_e\) are sources, so \(\sigma(D)=|E(C)|=3k/2\). For any rooted out-forest, each \(X_v\) chooses one incident \(W_e\) as parent. Contracting those chosen incidence edges partitions \(B\) into connected clusters of size **at most three** (one edge-witness and at most its two endpoint variables). Thus \(Q_D\) has \(3k/2\) vertices and maximum multigraph degree at most nine.

**Expansion is preserved.** First \(B\) is a bounded-degree edge-expander. For \(S\subseteq V(B)\), let \(A=S\cap V(C)\), \(F=S\cap E(C)\), \(a=|A|\), \(b=|F|\), and \(c=|\partial_B S|\). Every original edge crossing \(A,V(C)\setminus A\) induces exactly one boundary edge of \(B\), so \(c\ge\varepsilon\min(a,k-a)\). Moreover,
\[
 b\le3a/2+3c/2,\qquad
 |S|\le5a/2+3c/2,
\]
and the symmetric inequality holds for \(S^c\), yielding
\[
 |\partial_B S|
 \ge \frac{\varepsilon}{5/2+3\varepsilon/2}
    \min(|S|,|V(B)\setminus S|).
\]
Now for any set \(U\) of quotient clusters, its lift \(S\) is a union of whole clusters and has at least \(|U|\) vertices, while its complement has at least the number of complementary clusters. Contraction preserves boundary-edge counts (including multiplicity). Consequently \(Q_D\) retains constant edge expansion. Since its maximum degree is bounded, it has **treewidth \(\Theta(k)\)** by the standard balanced-separator/expansion argument (parallel edges do not affect treewidth).

**Scope:** this is a no-go for the *particular shortcut* "reduce functional constraints to source SCC roots, then perform low-treewidth DP." It is **not** a proof of a computational lower bound, nor a refutation of possible algebraic/special-purpose algorithms on the quotient. The expander may have trivially satisfiable relations. What survives is exactly the generic sparse-CSP difficulty we set out to accelerate.

## 4c. A concrete, balanced expander-CSP hardness stress test

The [new critical-expander CSP note](35_critical_expander_csp_poisson_and_arc_consistency.md) now contains a complete Chen–Stein argument, sharpening the earlier unaudited CEH random-instance claim. On any fixed simple 3-regular (optionally bipartite) \(\gamma\)-edge-expander, independently include each allowed pair on each edge with probability \(p=q^{-2/3}\). For \(q=k^c\) with \(c>3/\gamma\), the number of CSP solutions converges **in total variation** to \(\operatorname{Poisson}(1)\), hence \(\Pr[\mathrm{UNSAT}]\to e^{-1}\) and \(\Pr[\mathrm{SAT}]\to1-e^{-1}\). Simultaneously every value has local support on every edge with high probability; arc consistency does not reject. This is a **proved distributional construction, NOT a computational lower bound**.

The proposed *average-case* Critical-Expander-CSP hardness at the \(\sqrt{\log}\) scale is an explicit, experimentally testable candidate. It is **strictly more speculative** than worst-case SqrtLog-SPACH and should be evaluated against global spectral/rank/coding algorithms; it does not follow from Poisson statistics or failure of local consistency.

## 5. Implications for project priorities

- **ALREADY COVERED externally under stated assumptions:** sparse HC / FVS / connectivity-type algorithms (Guo 2026). Preserve attribution and the distinction between the full tensor theorem and the weaker Lean-scoped fixed-width theorem.
- **NEW DERIVED UPPER BOUNDS:** sparse-source #HOM and ordinary (non-induced) SubISO; test target degeneracy, list restrictions, and disconnected targets further. Establish novelty separately before claiming publication.
- **OPEN / promising hardness route:** SqrtLog-SPACH and its checked reduction to polynomial-target 2-degenerate HOM; this would match the new general HOM exponent and still rule out single-exponential HOM.
- **OPEN and much harder:** arbitrary Circuit-SAT \(\to\) sparse polynomial-domain binary CSP with \(O(s/\sqrt{\log s})\) variables plus constraints.
- **ALTERNATIVE OPEN:** PCC \(\to\) degree-3 sparse CSP with \(O(K\sqrt{\log K})\) size, no longer attempting an unconditionally hardness-preserving linear output.
- **DO NOT REVIVE:** old \(q^{o(k)}\) SPACH/CEH hypotheses, or incorrectly claim that their easy solvability implies easy *general* graph problems via one-way reductions.

**Next checks:** independent audit of the imported Anthropic recurrence, exact CSP-to-HOM 2-degenerate gadget parameters, and comparison with existing #HOM-to-SubISO color coding results to establish priority.
