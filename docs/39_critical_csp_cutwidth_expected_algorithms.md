# Critical random CSP: exact expected-time algorithms from cutwidth and forward checking

**Date:** 2026-11-02. **Status:** PROVED mathematical derivations (internal proof audit only), novel-priority OPEN. Importantly, these are **unconditional**, correct-on-all-input algorithms with **expected running times over a specified random table distribution**. They are exponentially slower asymptotically than the externally claimed Nguyen \(q^{O(k/\sqrt{\log k})}\) worst-case bound, so they DO NOT establish a new general CSP speedup or disprove SqrtLog-SPACH.

Predecessors: [note 35](35_critical_expander_csp_poisson_and_arc_consistency.md), [note 37](37_critical_expander_low_degree_fourier_and_path_saturation.md), [note 38](38_flat_cut_spectrum_backtracking_barrier_and_two_factor_enumeration.md).

## A. Exact expected prefix count = cut entropy

Let \(G\) be a **fixed** connected simple 3-regular graph on \(k\) vertices, with \(m=3k/2\). For every edge independently sample every ordered pair of labels from \([q]^2\) into \(R_e\) with probability \(p=q^{-2/3}\); all entries and edge tables are mutually independent. The algorithm knows \(G\) and \(q\), but not the relation tables when constructing its variable ordering.

For every \(S\subseteq V(G)\), let \(N_S\) count assignments on \(S\) satisfying exactly the original constraints completely inside \(S\). Since each such assignment has \(e(S)\) independently required Bernoulli table entries,
\[
 \mathbb E N_S=q^{|S|}p^{e(S)}
 =q^{\,|S|-\frac23e(S)}
 =\boxed{q^{|\delta(S)|/3}},
\tag{1}
\]
using \(3|S|=2e(S)+|\delta(S)|\).

Given an ordering \(\pi=(v_1,\ldots,v_k)\), simple DFS assigns variables in that order and rejects each new label immediately if it violates an original edge whose other endpoint is already assigned. Correctness is exact (decision, enumeration, and exact counting); it is a finite exhaustive search on any explicit input. If \(S_i=\{v_1,\ldots,v_i\}\), the number of successful prefixes at depth \(i\) is exactly \(N_{S_i}\). Checking rejected children costs at most a polynomial factor \(q\). Hence
\[
 \boxed{\mathbb E_{\rm tables}\, T_\pi
 \le \operatorname{poly}(k,q)\,
 q^{\operatorname{cw}_\pi(G)/3}},
 \quad
 \operatorname{cw}_\pi(G)=\max_{0\le i\le k}|\delta(S_i)|.
\tag{2}
\]
The big polynomial includes reading the \(O(kq^2)\) complete-table input and integer counter bit operations. The ordering must be **table-independent** for (1) to be used without adaptive-selection bias.

## B. Constructing an ordering with cutwidth \(k/4+o(k)\) (uniform for cubic graphs)

Choose a spanning tree \(T\) of \(G\). For an integer \(L=L(k)\) with \(L\to\infty\) and \(L=o(k)\), partition the tree into \(b=O(k/L)\) connected vertex blocks of size at most \(O(L)\), with at most one remainder block of size below \(L\).

**Constructive tree partition lemma.** Root \(T\); process bottom-up. At a vertex \(v\), merge \(v\) with the not-yet-emitted residual connected subtrees of its children. Each child residual has \(<L\) vertices; if the aggregate reaches \(L\), emit it as one block (size at most \(1+2(L-1)\) for a rooted cubic tree, or \(1+3(L-1)\) at the root) and return an empty residual; otherwise pass this residual upward. Finally emit the root residual if nonempty. Every emitted block is connected, at least \(L\) except possibly the final one, and of size \(O(L)\).

At least \(k-b\) spanning-tree edges lie within blocks, so the number \(M\) of original edges *between different blocks* satisfies
\[
 M\le m-(k-b)=k/2+b=k/2+O(k/L).
\tag{3}
\]
Choose a uniformly random order of the \(b\) blocks and concatenate arbitrary internal vertex orders. At a prefix containing exactly \(t\) full blocks, every interblock edge crosses with probability
\(2t(b-t)/(b(b-1))\), so
\[
 \mathbb E |\delta(S_t)|
 =M\frac{2t(b-t)}{b(b-1)}
 \le k/4+O(k/L+L).
\tag{4}
\]
Interchanging two blocks in the chosen \(t\)-set affects the status of at most \(O(L)\) incident edges (maximum degree 3). Standard bounded-difference concentration for uniform fixed-size subsets / random permutations, followed by a union bound over \(b\le k\) prefixes, yields simultaneously
\[
 |\delta(S_t)|\le k/4+
 O(k/L+\sqrt{kL\log k}+L).
\tag{5}
\]
While scanning the \(O(L)\) vertices of one block, the cut size changes by at most \(O(L)\). Pick \(L=\lceil(k/\log k)^{1/3}\rceil\). Then (5) becomes
\[
 \boxed{\operatorname{cw}_\pi(G)\le
 k/4+O(k^{2/3}(\log k)^{1/3})=k/4+o(k).}
\tag{6}
\]
One may resample block permutations and check the maximum cut in \(\operatorname{poly}(k)\) time, accepting the first one satisfying (5) with a large enough absolute concentration constant. The probability of acceptance is \(1-o(1)\); expected preprocessing is polynomial. (The weaker \(k/4+o(k)\) suffices and does not depend on the sharp constant.) No expander or bipartiteness assumption is needed here.

**Theorem (unconditional expected exact counting/decision/search):**
\[
 \boxed{\mathbb E_{\rm tables}T
 \le \operatorname{poly}(k,q)\,
 q^{k/12+O(k^{2/3}(\log k)^{1/3})}
 =q^{k/12+o(k)}\operatorname{poly}(k,q).}
\tag{7}
\]
The ordering is constructed before the random relations are inspected. This improves the previous unconditional \(q^{k/3}\) *expected-time* 2-factor enumeration bound (note 38) by a factor four in the leading constant of the \(k\log q\) exponent. It is not a \(q^{o(k)}\) algorithm.

**For \(\Delta\)-regular graphs**, set critical density \(p=q^{-2/\Delta}\). Then \(\mathbb E N_S=q^{|\delta(S)|/\Delta}\). The same spanning-tree block argument bounds cutwidth by \((\Delta-2)k/4+o(k)\), giving the generalized expected bound \(q^{(\Delta-2)k/(4\Delta)+o(k)}\operatorname{poly}(k,q)\) for every fixed \(\Delta\ge3\). The source graph should be connected; handle components independently otherwise.

## C. Stronger *structural* pruning when the cubic graph has logarithmic girth

Assume additionally that \(G\) is simple, **triangle-free**, cubic, and has girth \(g(G)=\Omega(\log k)\). This includes suitable explicit bipartite high-girth expander families. This section does NOT assert the result for arbitrary cubic expanders with short cycles.

Use a polynomial-time many-leaf spanning tree with \(\ell\ge k/3+O(1)\) leaves (Bonsma 2008 for connected triangle-free graphs of minimum degree \(\ge3\); the weaker Kleitman–West 1991 bound \(\ell\ge k/4+2\) applies without the triangle-free strengthening). Divide this tree into connected blocks as above, now with \(L=\Theta(\log k)\) chosen so that every block has \(<g(G)\) vertices. Then **no non-tree edge can lie within one block**, since a non-tree edge and the tree path inside the block would form a cycle shorter than \(g(G)\). Every spanning-tree leaf therefore has two non-tree neighbors outside its own block. Blocks are of size \(O(L)\).

For a currently assigned set \(S\) and a partial assignment \(x_S\), perform **forward checking**: for every \(w\notin S\) require at least one label \(a\in[q]\) satisfying *all* its constraints to assigned neighbors in \(S\). Reject \(x_S\) otherwise. This never rejects a prefix that extends to a global solution and requires only polynomial time in \(k,q\).

Put \(d_S(w)=|N_G(w)\cap S|\), and \(N_j(S)=|\{w\notin S:d_S(w)=j\}|\). For a fixed, table-independent \(S\), the exact expected number of forward-check-surviving partial assignments is
\[
 \boxed{
 \mathbb E N_S^{\rm FC}
 =q^{|\delta(S)|/3}
 \prod_{j=0}^3\pi_j^{N_j(S)},
 \quad \pi_j=1-(1-p^j)^q.
 }
\tag{8}
\]
Reason: the original internally satisfied edges use independent table bits from the crossing edges, and the forward-support events for different unassigned vertices depend on pairwise disjoint sets of crossing edge tables. For \(j=2,3\),
\(\pi_2\le qp^2=q^{-1/3}\) and \(\pi_3\le qp^3=q^{-1}\). Therefore
\[
 \mathbb E N_S^{\rm FC}
 \le q^{|\delta(S)|/3-N_2(S)/3-N_3(S)}
 =\boxed{q^{(N_1(S)+N_2(S))/3}}.
\tag{9}
\]

Consider a prefix \(S_t\) of \(t\) entire blocks of a random block order, with \(u=t/b\). Let \(Y_t\) count the **original spanning-tree leaves** outside selected blocks whose *two non-tree neighbors' blocks* have both already been selected. Every such leaf has \(d_S(w)\ge2\), so \(N_2+3N_3\ge Y_t\). Since the graph girth ensures the neighbor blocks are distinct from the leaf's block (but they may coincide with one another),
\[
 \mathbb E_{\rm block-order}Y_t
 \ge \ell(1-u)u^2-O(k/b)
 \ge (k/3)(1-u)u^2-o(k).
\tag{10}
\]
Simultaneously, by (3)–(4),
\[
 \mathbb E_{\rm block-order}|\delta(S_t)|
 \le k u(1-u)+o(k).
\tag{11}
\]
Both functions of the selected block subset change by \(O(L)\) if two blocks are swapped: each block affects only \(O(L)\) vertices and \(O(L)\) edges. Bounded-difference concentration plus union bound over all prefixes shows that **one polynomial-time findable order** satisfies, for every prefix (including positions inside a block, which cost only \(O(L)\) additional change),
\[
 |\delta(S)|-Y(S)
 \le k\,u(1-u)(1-u/3)+o(k),
\tag{12}
\]
with the appropriate block-fraction \(u\) for that prefix. Consequently forward-checking DFS has expected runtime at most
\[
 \boxed{
 \operatorname{poly}(k,q)\,q^{c_*k+o(k)},
 \quad
 c_*=\frac13\max_{0\le u\le1}u(1-u)(1-u/3)
 =\frac{14\sqrt7-20}{243}
 \approx0.07012558994.
 }
\tag{13}
\]
This improves \(1/12\approx0.0833333\) on this more structured graph family. The \(\ell\ge k/3\) and \(g(G)=\Omega(\log k)\) requirements are explicit. The algorithm's correctness is unconditional for **all** relation-table inputs; the stated expected runtime holds over the critical iid table distribution.

## Next refinement: group-lookahead and a computable matching gain

[Note 40](40_group_lookahead_boundary_entropy_and_matching.md) extends the single-vertex forward-check expectation to any vertex-disjoint family of free induced trees \(U\): the group-local extension expectation is \(q^{(b_R(U)-b_S(U))/3}\), and its effect on the prefix exponent is the credit \((b_S(U)-b_R(U))_+/3\). Taking all singletons or selected adjacent pairs, the **best provable improvement** is found by maximum-weight matching: an unassigned edge joining vertices with \(j\in\{1,2\}\) and \(j'\in\{2,2\}\) receives a positive bonus. This produces an exact polynomial-overhead search improvement on some prefixes, but it does **not yet establish a smaller universal asymptotic coefficient** than the \(0.070126\) in Section C. Checking all connected induced-tree groups of \(O(\log k)\) vertices is still polynomial per node, and leads to a precise new boundary-entropy potential whose sublinearity remains open.

## D. Comparison and honest limitations

| Method | Expected running time on the critical Bernoulli CSP |
|---|---|
| Naive full assignment enumeration | \(q^k\) |
| 2-factor enumeration for cubic **bipartite** graphs (note 38) | \(q^{k/3}\operatorname{poly}\) |
| Fixed-order local-check DFS with connected blocks (this note) | \(q^{k/12+o(k)}\operatorname{poly}\) |
| Forward-checking DFS, **triangle-free cubic girth \(\Omega(\log k)\)** (this note) | \(q^{0.070126k+o(k)}\operatorname{poly}\) |
| **Externally claimed** general deterministic tensor counting (Nguyen 2026) | \(q^{O(k/\sqrt{\log k})}\operatorname{poly}\) **worst case** |

The general tensor algorithm asymptotically dominates these elementary expected-time bounds for sufficiently large \(k\). Our fixed-order DFS lower bound from note 38 remains consistent: it gives \(q^{\Omega(k)}\) for local-check DFS on UNSAT instances with any fixed order, but the constant is at most that allowed by our optimized upper bounds. Forward checking is **outside** the precise local-check-only lower-bound model from note 38.

**Novelty caveat:** expected prefix-count analysis, random connected-block orderings, many-leaf spanning trees, and constraint support propagation are all classical ingredients. This combined estimate is an internally derived benchmark, NOT presented as a new published algorithm or a breakthrough against 2026 tensor contraction. It motivates testing adaptive cutwidth/frontier optimization and globally coupled algebraic algorithms.


## E. Source references / novelty audit

- P. S. Bonsma, [*Spanning Trees with Many Leaves in Graphs With Minimum Degree Three*](https://doi.org/10.1137/060664318), SIAM J. Discrete Math. 22(3), 2008: in connected triangle-free minimum-degree-three graphs a spanning tree with at least \((k+4)/3\) leaves exists **constructively**.
- D. J. Kleitman and D. B. West, [*Spanning Trees with Many Leaves*](https://doi.org/10.1137/0404010), SIAM J. Discrete Math. 4(1), 1991: constructive \(k/4+2\) bound for minimum degree three.
- B. Monien and R. Preis, [*Upper Bounds on the Bisection Width of 3- and 4-Regular Graphs*](https://doi.org/10.1016/j.jda.2005.12.009), J. Discrete Algorithms, 2006: classical bounds \(k/6+o(k)\) for **bisection width**, a different parameter from cutwidth.
- F. V. Fomin and K. Høie, [*Pathwidth of cubic graphs and exact algorithms*](https://doi.org/10.1016/j.ipl.2005.10.008), Inf. Process. Lett. 97, 2006: \(k/6+o(k)\) **pathwidth** for cubic graphs (distinct from cutwidth).
- Source of high-girth cubic expander families: classical Ramanujan constructions; for explicitness and girth see e.g. the [LPS original](https://doi.org/10.1007/BF02126799) and literature on degree-\(q+1\) families for prime-power \(q\). We do **not** rely on explicit construction details for the conditional-on-\(G\) algorithm statement.

The cutwidth-based random-prefix expectation and pruning estimates above are elementary *notebook deductions*. Their precise asymptotic constants and whether the same formulas appear in older random CSP search literature have not been checked against all prior work. Do not advertise publication-level novelty until that review.
