# Actual simultaneous overlapping-tree-lookahead barrier on a spaced prefix

**Date:** 2026-11-03.  
**Status:** PROVED elementary second-moment and union-bound notebook argument, NOT independently reviewed or claimed as new in random-CSP literature. **Precisely restricted model:** an intentionally chosen fixed variable order starting with a large distance-5 packing; exact DFS only prunes via fully assigned original relations and *all* connected free-group feasibility checks of size \(\le r=C\ln k\). This is an actual search-tree lower bound for that order, not just a lower bound on the disjoint-family potential \(\Phi_r\). It **does not** rule out better orders, data-dependent ordering, learned constraints, global algebraic tests or the claimed tensor algorithm.

Relation to [note 40](40_group_lookahead_boundary_entropy_and_matching.md) and [note 43](43_expander_group_lookahead_potential_no_go.md). Previous note 43 ruled out using a disjoint-family *upper-bound potential* to certify sublinear expected time. This note analyzes the **joint event** that *every* overlapping tree test passes.

## Model and theorem

Let \(G=(V,E)\) be a fixed simple cubic graph with \(|V|=k\), girth \(g(G)>r+1\), \(r=\lceil C\ln k\rceil\). Independently for each edge \(e\) and each label pair \((a,b)\in[q]^2\), mark it allowed with probability \(p=q^{-2/3}\). These are **complete-table Bernoulli CSPs**, not random sparse lists of tuples. Suppose \(q=\lceil k^c\rceil\) with \(c>3(2+C\ln18)\).

Choose a vertex set \(S\subseteq V\) of pairwise distance at least 5, of size \(s\ge k/46\). Such a set is computable greedily: repeatedly select any remaining vertex and remove its radius-4 ball, of size at most \(1+3+6+12+24=46\). Take *exactly* \(\lfloor k/46\rfloor\) selected vertices if a uniform size is desired.

Fix any order of the vertices of \(S\) as the **first** \(s\) assigned variables. Before/after each assignment, the DFS algorithm rejects a prefix if (a) any original constraint is violated by its assigned endpoints or (b) any connected vertex set \(U\) in the still-unassigned vertices, with \(|U|\le r\), has **no local extension** satisfying all internal constraints of \(U\) and all constraints from \(U\) to the already-assigned prefix. No other pruning/learning is allowed. Since \(g(G)>r+1\), all such induced connected sets are trees, and each test is polynomial-time solvable by tree-CSP DP. There are only \(k\,9^r=\operatorname{poly}(k)\) such groups for fixed \(C\), and therefore polynomial overhead per search node.

**Theorem A (overlapping checks almost never prune this spaced prefix).** With probability \(1-o(1)\) over the random table input, at least
\[
 \boxed{(1-o(1))q^s}
\]
of the \(q^s\) assignments to \(S\) pass **all** group-lookahead checks at **every** intermediate prefix and are reached by this fixed-order search tree. More precisely, for each deterministic assignment \(x_S\),
\[
 \Pr_{\rm tables}\left[x_S\text{ fails some lookahead test while assigning }S\right]
 \le \epsilon_k:=k^2 18^r q^{-1/3}=o(1),
\tag{1}
\]
so the fraction of failing \(x_S\)'s is at most \(\sqrt{\epsilon_k}=o(1)\) with probability at least \(1-\sqrt{\epsilon_k}\).

If \(G\) additionally belongs to a fixed family of \(\gamma\)-edge-expanders and \(c>\max\{3/\gamma,\,3(2+C\ln18)\}\), [note 35](35_critical_expander_csp_poisson_and_arc_consistency.md) gives \(\Pr[\mathrm{UNSAT}]\to e^{-1}\). Consequently, on a fraction at least \(e^{-1}-o(1)\) of instances the **complete decision DFS** must explore at least \((1-o(1))q^s=q^{\Omega(k)}\) nodes *even with all overlapping \(\le C\ln k\)-size tree tests*, since on UNSAT it cannot stop after a YES witness.

## Proof of Theorem A

### 1. Sparse anchor geometry for every tested tree

Fix an intermediate prefix \(S'\subseteq S\), fixed label assignment \(x_{S'}\), and a connected set \(U\subseteq V\setminus S'\), \(|U|\le r\). Write \(T=G[U]\), a tree.

Let \(B=\{u\in U:\text{\(u\) has at least one neighbor in }S'\}\), the "anchored" vertices of \(U\). The following are crucial:

- **At most one prefix neighbor per \(u\in B\).** Two different vertices \(s_1,s_2\in S'\) sharing \(u\) would have graph distance 2, contradicting the distance-\(\ge5\) packing.
- **No two anchored vertices \(u,v\in B\) have distance \(<3\) in \(T\).** If their prefix neighbors are *different*, such a short path would connect two vertices of \(S'\) by a path of length at most 4. If their prefix neighbor is the *same*, the \(u\)–\(v\) path inside \(T\) plus the two edges through that prefix neighbor forms a cycle of length at most \((r-1)+2=r+1\), contradicting \(g(G)>r+1\). This second case is exactly why a girth assumption is necessary: distance separation of distinct prefix vertices alone does not rule out multiple contacts with the *same* prefix vertex through one tree.

Therefore \(B\) is a **distance-3 packing** in \(T\), and the number \(b_{S'}(A)=|E(A,S')|\) equals \(|A\cap B|\).

### 2. Combinatorial overlap bound for an arbitrary agreement set

Let \(A\subseteq U\) be nonempty. Since \(T\) is a tree, the induced \(T[A]\) is a forest; write \(c_A=\operatorname{cc}(T[A])\). For any connected component \(C_0\) of \(T[A]\) of size \(\ge2\), anchored vertices in \(C_0\) are at pairwise distance at least 3 in \(C_0\). Their closed neighborhoods in \(C_0\) are disjoint, and each contains at least two vertices because \(C_0\) is connected. Thus \(|C_0\cap B|\le |C_0|/2\). A singleton component contains at most one anchored vertex. Summing over all components yields
\[
 e_T(A)+b_{S'}(A)
 \le\tfrac32|A|-\tfrac12 c_A.
\tag{2}
\]
Indeed, a component of order \(t\ge2\) contributes at most \((t-1)+t/2=1.5t-1\), while a singleton contributes at most \(1=1.5-0.5\).

### 3. Second moment for one tree-local extension test

Let \(Z_U(x_{S'})\) count label assignments to \(U\) satisfying all tree-internal constraints and all edges to fixed \(S'\). For each fixed assignment \(y_U\), the needed relation-table entries lie on \(e(T)+|E(U,S')|\) **different edges**. Therefore
\[
 \mathbb E Z_U
 =q^{|U|}p^{e(T)+|E(U,S')|}.
\]

Two independently uniformly selected labelings \(y_U,z_U\) have agreement set \(A=\{u:y_U(u)=z_U(u)\}\). Their required Bernoulli table entries coincide precisely on the internal edges with both endpoints in \(A\) and the prefix-boundary edges with endpoint in \(A\). Thus
\[
 \frac{\mathbb E Z_U^2}{(\mathbb E Z_U)^2}
 =\sum_{A\subseteq U}
   q^{-|A|}(1-q^{-1})^{|U|-|A|}
   p^{-[e_T(A)+b_{S'}(A)]}.
\tag{3}
\]
By (2), \(p=q^{-2/3}\), each nonempty \(A\) contributes at most \(q^{-c_A/3}\le q^{-1/3}\) (the factor \((1-q^{-1})^{|U|-|A|}\le1\)). The \(A=\varnothing\) term is at most 1, yielding
\[
 \boxed{
 \frac{\operatorname{Var}(Z_U)}{(\mathbb E Z_U)^2}
 \le(2^{|U|}-1)q^{-1/3}\le2^r q^{-1/3}.
 }
\tag{4}
\]
Chebyshev gives a **uniform over fixed \(x_{S'}\)** failure bound
\[
 \boxed{\Pr[Z_U(x_{S'})=0]\le2^r q^{-1/3}.}
\tag{5}
\]

### 4. Union bound across all overlapping groups, prefixes, and most assignments

The number of connected vertex sets \(U\) with \(|U|\le r\) in a cubic graph is at most \(k9^r\): root a spanning tree at a chosen vertex and encode an Euler walk of length at most \(2r\), with at most three choices per step. Hence for a *fixed* full \(x_S\), across at most \(k\) intermediate prefix stages and all tested groups, the probability **any** local check rejects its corresponding restriction is at most
\[
 k\cdot(k9^r)\cdot2^r q^{-1/3}
 =k^2 18^r q^{-1/3}.
\]
All intermediate \(S'\) are independent sets, so no original edge has both endpoints assigned during this first phase and original-relation checks cannot prune.

With \(q=k^c\), \(r=C\ln k+O(1)\), \(\epsilon_k=O(k^{2+C\ln18-c/3})=o(1)\) by the stated condition. Averaging over all \(x_S\), the expected *fraction* of assignments rejected at any first-phase stage is at most \(\epsilon_k\). Markov's inequality proves the high-probability fraction statement and thus the actual search-tree node bound.

### Why the high-girth hypothesis is substantive

Without \(g(G)>r+1\), two vertices of the same tested tree may have a common already-assigned neighbor \(s\in S'\), with the tree-path between them closing a short cycle. Then anchored vertices need not be a distance-3 packing, and the bound (2) can fail. The proof **does not claim** this barrier for arbitrary cubic expanders of short girth.

## Extension to any fixed regular degree \(\Delta\ge3\)

The same proof extends cleanly beyond cubic graphs, but **only after changing the critical relation density** to \(p=q^{-2/\Delta}\) (since now \(|E|=\Delta k/2\)).

Choose pairwise distance-\(\ge5\) vertices \(S\) greedily, with
\[
 |S|\ge k/B_\Delta,\quad
 B_\Delta=1+\Delta\sum_{j=0}^{3}(\Delta-1)^j.
\]
For a group \(U\) with \(|U|\le r<g(G)-1\), the same anchored-vertex packing and forest-component argument gives
\(e_U(A)+b_{S'}(A)\le\tfrac32|A|-\tfrac12\operatorname{cc}(U[A])\).
The corresponding second moment now obeys
\[
 \frac{\operatorname{Var}(Z_U)}{(\mathbb EZ_U)^2}
 \le2^r q^{-1/\Delta}
\]
because
\[
 |A|-\frac2\Delta(e_U(A)+b_{S'}(A))
 \ge(1-3/\Delta)|A|+\operatorname{cc}(U[A])/\Delta
 \ge1/\Delta.
\]
The complete union bound over tree groups and first-phase prefixes is
\[
 \epsilon_{k,\Delta}
 \le k^2(2\Delta^2)^r q^{-1/\Delta}.
\]
Thus for \(r=C\ln k\), \(q=k^c\), it suffices that \(c>\Delta(2+C\ln(2\Delta^2))\), and almost every assignment to the first \(\Omega_\Delta(k)\) spaced vertices survives all tests.

If \(G\) also has uniform edge expansion \(\gamma>0\), the Chen–Stein argument in note 35 generalizes with the proper-subset overlap contribution \(q^{-\gamma\min(s,k-s)/\Delta}\): one gets \(Z\Rightarrow\operatorname{Pois}(1)\) once \(c>\Delta/\gamma\). Hence a constant \(e^{-1}-o(1)\) fraction of null instances are UNSAT and force \(q^{\Omega_\Delta(k)}\) work for this specific bad-order lookahead DFS.

This shows that the phenomenon is caused by **girth and separated boundary anchors**, not by a cubic-only counting coincidence. The cubic case remains the project's central source because of its direct link to the HOM reduction.

## Literature/provenance caveat

Relevant classical work includes Gao–Culberson, [*Consistency and Random Constraint Satisfaction Models*](https://mlanthology.org/jair/2007/gao2007jair-consistency/) (JAIR 2007), and Atserias, [*Unsatisfiable Random Formulas are Hard to Certify*](https://lics.siglog.org/2002/Atserias-UnsatisfiableRandom.html) (LICS 2002). They address consistency / certification barriers in random constraint systems, and may overlap substantially with the conceptual lesson here. **No publication novelty is claimed for this particular second-moment argument or lookahead lower bound without a dedicated priority review.**

## A complementary two-vertex local/global gap

[Note 47](47_conditional_poisson_after_one_edge_and_endpoint_injectivity.md) proves a result for a *different* prefix: fix the endpoints \(u,v\) of one edge \(e=uv\), delete \(e\), and consider any connected unassigned tree \(U\) of size \(r<g(G)-2\). Girth implies \(U\) has **at most one** boundary edge to \(\{u,v\}\). Since every row and column of every random relation table has an allowed pair with high probability, **every possible pair \((x_u,x_v)\in[q]^2\)** passes all these local tree checks. Nevertheless, only \((1+o(1))q^{2/3}\) endpoint pairs extend to a global solution after deleting \(e\), and only \(\mathrm{Pois}(1)+o_{\rm TV}(1)\) survive after reinstating \(e\). The argument is completely independent of group-test overlaps. It does not show exponential DFS time from this 2-vertex prefix, but is a sharper local-to-global *projection* gap.

## Exact conclusion and remaining open algorithmic question

**PROVED restricted lower bound:** if one starts the search with a large distance-5 separated set and only performs fully assigned relation checks plus *all* \(\le C\ln k\)-size connected-tree existential checks, then with positive constant probability over the critical random expander-CSP tables the algorithm needs \(q^{\Omega(k)}\) time, even though it performs overlapping group tests. This is a *genuine lower bound for that deliberately bad order*, not for all fixed orders. If the algorithm chooses a different order (e.g. connected spanning-tree blocks as in [note 39](39_critical_csp_cutwidth_expected_algorithms.md)), we have no such conclusion from this argument.

**Still OPEN:** whether a suitably optimized/table-dependent ordering together with all overlapping small group tests reaches \(q^{o(k)}\) expected time; whether stronger global algebraic algorithms improve on the external \(q^{O(k/\sqrt{\log k})}\) claim; and a worst-case or average-case hardness theorem. Existing local-consistency lower-bound techniques (Atserias/Dalmau, Gao/Culberson) are relevant, so priority/novelty must be checked before publication.
