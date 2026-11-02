# Critical random cubic CSP: group lookahead, boundary-entropy identity, pair matching, and logarithmic-size tree tests

**2026-11-02. Status:** The expectation/boundary identities and the precise pair-matching optimization below are elementary **PROVED notebook statements**. They apply to a fixed cubic graph with independent Bernoulli relation-table entries at \(p=q^{-2/3}\), with an ordering/group collection chosen **independently of the table contents**. The group feasibility algorithms are exact on *all* instances. **No new \(q^{o(k)}\) runtime is established.** These lookahead ideas fall within long-established constraint-consistency research; see attribution.

Previous work: [cutwidth and forward checking, note 39](39_critical_csp_cutwidth_expected_algorithms.md); [critical Poisson, note 35](35_critical_expander_csp_poisson_and_arc_consistency.md); [model barriers, note 38](38_flat_cut_spectrum_backtracking_barrier_and_two_factor_enumeration.md).

## 1. Core identity: exact expected number of extensions of a connected group

Let \(G=(V,E)\) be a simple 3-regular graph on \(k\) vertices; every entry of every binary relation \(R_e\subseteq[q]^2\) is independent Bernoulli \(p=q^{-2/3}\). Fix a subset \(S\subseteq V\), a **specific** assignment \(x_S\), and \(U\subseteq V\setminus S\), where \(U\) is any nonempty group.

Put
\[
 e_U=|E(G[U])|,\quad
 b_S(U)=|E(U,S)|,\quad
 b_R(U)=|E(U,V\setminus(S\cup U))|.
\]
Then \(3|U|=2e_U+b_S(U)+b_R(U)\).

Let \(Z_U(x_S)\) count assignments \(y\in[q]^U\) satisfying every edge wholly in \(U\) and every edge between \(U\) and the already fixed \(S\). Edges between \(U\) and other unassigned vertices are intentionally ignored. For each \(y\), the required entries live on \(e_U+b_S(U)\) distinct edges and are independent, hence
\[
 \boxed{\mathbb E[Z_U(x_S)]
  =q^{|U|}p^{e_U+b_S(U)}
  =q^{(b_R(U)-b_S(U))/3}.}
\tag{1}
\]
Therefore Markov's inequality gives the **uniform in \(x_S\)** upper bound
\[
 \boxed{\Pr[Z_U(x_S)>0]
  \le \min\{1,q^{-(b_S(U)-b_R(U))/3}\}.}
\tag{2}
\]
The law is the same for every fixed \(x_S\) because each table entry on each edge has the same independent distribution. The event on \(U\) is independent of all relations fully inside \(S\).

**Computability:** when \(G[U]\) is a forest, exact test \(Z_U(x_S)>0\) is polynomial in \(k,q\) using tree-CSP dynamic programming. Edges from \(U\) to fixed \(S\) contribute only unary filters, even when several such edges share endpoints in \(S\). A tree of *arbitrary cardinality* can be tested in \(O(|U|q^2+\deg(U)q)\) time with explicit tables. This is stronger than simply enumerating \(q^{|U|}\) extensions. For bounded treewidth \(w\), \(O(|U|q^{w+1})\) is an analogous generalization.

## 2. Independent disjoint-group pruning, exact expected prefix upper bound

Let \(\mathcal U=\{U_1,\dots,U_t\}\) be **pairwise vertex-disjoint** groups within \(V\setminus S\), fixed before drawing the relation tables. Retain a partial assignment \(x_S\) only if:

(i) it satisfies every original relation fully inside \(S\); and  
(ii) for every \(U_i\), there is a group-local extension to \(U_i\) as in Section 1.

Conditional on \(x_S\), these group feasibility events involve disjoint edge-table sets: distinct groups have disjoint internal edges and disjoint edges to \(S\). Inter-group edges are not checked by either event. They are therefore independent of one another and of the events inside \(S\).

The expected number of locally surviving assignments \(N_S^{\mathcal U}\) is bounded by
\[
 \boxed{
 \mathbb E N_S^{\mathcal U}
 \le q^{\Phi(S;\mathcal U)},\qquad
 \Phi(S;\mathcal U)=\frac13\left(
  |\delta(S)|-\sum_{U\in\mathcal U}(b_S(U)-b_R(U))_+
 \right).
 }
\tag{3}
\]
Proof: \(\mathbb E N_S=q^{|\delta(S)|/3}\) from note 39; multiply the upper bounds (2), and sum over all \(q^{|S|}\) assignments. The exponent is nonnegative because \(\sum (b_S-b_R)_+\le\sum b_S\le|\delta(S)|\).

**No false negatives:** a global satisfying assignment extends \(x_S\) on every tested group. Any DFS applying these tests is correct on every deterministic instance; the expectation bound relies on the **random** tables.

If the unassigned induced graph \(G[V\setminus S]\) is a forest, use each of its connected components as one group. Each such group has \(b_R=0\) and the sum of its \(b_S\)'s is \(|\delta(S)|\), giving \(\Phi=0\); in fact the group checks are then complete extension tests, so at most the actual full solutions survive.

## 3. An exact polynomial-time pair selection via maximum-weight matching

For an unmatched unassigned vertex \(v\), let \(j_v=|N(v)\cap S|\in\{0,1,2,3\}\). The singleton group has credit
\[
 c_v=(b_S(\{v\})-b_R(\{v\}))_+=(2j_v-3)_+.
\]
For an edge \(uv\in E(G[V\setminus S])\), the two-vertex induced group has four exterior edges (3-regularity), of which \(j_u+j_v\) go to \(S\), so its credit is
\[
 c_{uv}=(2(j_u+j_v)-4)_+.
\]
Its improvement over two singleton tests is
\[
 \beta_{uv}=c_{uv}-c_u-c_v.
\]
All \(\beta_{uv}>0\) cases are:
\[
  \{j_u,j_v\}=\{1,2\}\implies\beta_{uv}=1,\qquad
  \{j_u,j_v\}=\{2,2\}\implies\beta_{uv}=2.
\]
Every other pair has \(\beta_{uv}\le0\). Therefore the best disjoint collection of singleton/pair groups (measured by the rigorous exponent (3)) is obtained by a **maximum-weight matching** \(M_S\) on the current unassigned graph with edge weights \(\max(0,\beta_{uv})\). Let \(B(S)=\sum_{uv\in M_S}\beta_{uv}\); test each matched pair jointly and all unmatched vertices individually. Each pair test takes \(O(q^2)\) time by direct table scanning and fixed-neighbor unary filtering. The selection of \(M_S\) depends only on \(G,S\), not on the random table contents.

We obtain the explicit polynomial-time per-prefix search rule and expectation bound
\[
 \boxed{
 \mathbb E N_S^{(2)}
 \le q^{\Psi_2(S)},\quad
 \Psi_2(S)=\frac13\left(
 |\delta(S)|-\sum_{v\notin S}(2j_v-3)_+-B(S)
 \right).
 }
\tag{4}
\]
This is never a weaker **bound** than singleton forward checking; whenever \(B(S)>0\), it saves a factor \(q^{B(S)/3}\) in that bound. It need not improve an entire algorithm's worst-over-prefixes exponent without a new graph-ordering lemma guaranteeing \(B(S)\) at the bottleneck.

**Small, fully explicit example:** \(G=K_{3,3}\), let \(S\) consist of two left vertices and one right vertex. The remaining graph is a three-vertex path: the free left vertex has \(j=1\), both free right vertices have \(j=2\). Here \(|\delta(S)|=5\), singleton credit \(2\), and a matching gives bonus \(1\). Thus the baseline expected prefix count is \(q^{5/3}\), singleton bound \(q\), pair-check bound \(q^{2/3}\). Checking the entire unassigned three-vertex tree is polynomial and gives bound \(1\). For \(q=16\), the exact singleton survivor expectation is \(q^{5/3}[1-(1-p^2)^q]^2\approx11.125\), below the upper bound \(q=16\). No numerical simulation or assumption about expansion is needed for this example.

## 4. Tree lookahead of logarithmic size still takes polynomial time per prefix

For cubic \(G\), the number of connected vertex subsets of size at most \(r\) is at most \(k\,3^{O(r)}\): encode a spanning-tree Euler traversal of length at most \(2(r-1)\), recording an incident-edge choice (at most 3 at every step) at each traversal step. Consequently, for
\[
 r\le C\log k
\]
with any fixed \(C\), we may enumerate **every** nonempty connected set \(U\subseteq V\setminus S\) of size at most \(r\), and test every one whose induced graph is a tree, in total \(\operatorname{poly}_C(k,q)\) time per search node. This is a legitimate polynomial-time **group-lookahead** algorithm for explicit relation tables; it preserves global solutions exactly. If \(\operatorname{girth}(G)>r\), *every* such connected set is a tree.

For analysis, choose any family \(\mathcal U\) of pairwise disjoint induced trees among the tested sets. Because the algorithm tests **all** of them, its surviving prefixes are a subset of those passing just \(\mathcal U\), so (3) remains an upper bound. Define the *analysis-only* potential
\[
 \boxed{
 \Phi_r(S)=\frac13\left(
  |\delta(S)|-
  \max_{\substack{\mathcal U\ \text{disjoint induced trees}\\U\subseteq V\setminus S,\ |U|\le r}}
     \sum_{U\in\mathcal U}(b_S(U)-b_R(U))_+
 \right).
 }
\tag{5}
\]
Then for any fixed, table-independent vertex order \(\pi\), the exact DFS using all such tests satisfies
\[
 \boxed{
 \mathbb E T
 \le \operatorname{poly}_C(k,q)
 \sum_{i=0}^{k} q^{\Phi_r(S_i)}
 \le \operatorname{poly}_C(k,q)\,q^{\max_i\Phi_r(S_i)}
 }
\tag{6}
\]
up to a harmless additional \(kq\) factor for generating/checking children. \(\Phi_{r+1}(S)\le\Phi_r(S)\), \(\Phi_1\) is the previous singleton credit potential, and \(\Phi_2=\Psi_2\) from (4).

**Important computational subtlety:** the maximizing disjoint-tree packing in the *definition of \(\Phi_r\)* need not be polynomial-time computable when \(r\ge3\). This does **not** invalidate the stated algorithm or bound: the algorithm explicitly checks all candidate small trees without computing that packing. The maximum is used only analytically to choose a convenient disjoint subfamily to upper-bound its survival probability.

At this point **no proof** shows that \(\max_i\Phi_{\lceil C\log k\rceil}(S_i)=o(k)\) for a useful table-independent order \(\pi\) on all cubic expanders, nor that it beats the existing note 39 leading \(0.070126\,k\) coefficient uniformly. This is the precise missing combinatorial theorem for obtaining an unconditional new sublinear expected exponent from logarithmic-size tree lookahead.

## 4a. Finite exact-order sanity checks and the actual competitive target

For graphs with at most 12 vertices, the whole optimization
\[
 \omega_r(G)=\min_{\pi}\max_i\Phi_r(S_i)
\]
for \(r=1,2\) can be calculated by subset DP: \(D_r(\varnothing)=0\) and
\[
 D_r(S)=\max\left\{\Phi_r(S),\min_{v\in S}D_r(S\setminus\{v\})\right\}.
\]
For \(r=2\), each \(\Phi_2(S)\) is computed via maximum-weight matching as above. In internal finite exact computations, the results were:
\[
\begin{array}{c|c|c|c}
 G&k&\omega_1(G)&\omega_2(G)\\
 K_{3,3}&6&1&1\\
 Q_3\ \text{(cube)}&8&4/3&4/3\\
 \text{Petersen}&10&5/3&5/3\\
 \text{three independently generated random cubic graphs}&12&1&1
\end{array}
\]
(the random graphs were produced with NetworkX \`random_regular_graph(3,12,seed)\` for seeds 1, 2, and 3). **No improvement in the globally optimal worst-prefix potential was detected in these small checks**, despite strict per-prefix bonuses on some other orders. This is *numerical evidence only*, not an equivalence theorem for \(r=1,2\) or a test of asymptotic expanders.

Also distinguish the two goals:
- proving \(\omega_{C\log k}(G)=o(k)\) yields an **unconditional** \(q^{o(k)}\) expected algorithm on the critical random input distribution, although a stronger \(q^{O(k/\sqrt{\log k})}\) **worst-case** bound is externally claimed in Nguyen 2026;
- to **beat Nguyen asymptotically** and contradict the proposed average-case SqrtLog hardness, one would need the stricter bound \(\omega_{C\log k}(G)=o(k/\sqrt{\log k})\), or another algorithmically faster technique. Simply obtaining \(\omega=o(k)\) is insufficient for that goal.

## 5. Relation to known CSP consistency frameworks and open next step

Lookahead, neighborhood inverse consistency, relational neighborhood inverse consistency, and tree-based constraint propagation have been studied for decades. These precise group tests **are not claimed as new general CSP algorithms**, and the probabilistic boundary-entropy calculation is simply the direct first moment for the particular \(p=q^{-2/3}\) model.

Useful prior art:
- Haralick–Elliott, *Increasing Tree Search Efficiency for Constraint Satisfaction Problems*, IJCAI 1979, https://ijcai.org/proceedings/1979/78 .
- Woodward–Karakashian–Choueiry–Bessière, *Solving Difficult CSPs with Relational Neighborhood Inverse Consistency*, AAAI 2011, https://doi.org/10.1609/aaai.v25i1.7825 .
- Rina Dechter's bucket-elimination and tree-CSP methods, already cited in [note 13](13_binary_csp_cyclomatic_reduction.md).
- Related random large-domain CSP threshold and resolution literature: Frieze–Molloy, *The satisfiability threshold for randomly generated binary constraint satisfaction problems*, Random Struct. Algorithms 2006, https://doi.org/10.1002/rsa.20118 .

**Concrete next research question:** construct/identify orders \(\pi\) and polynomial-time-checkable families of disjoint induced trees of size \(O(\log k)\) for which
\[
  \max_i\Phi_r(S_i)=o(k/\sqrt{\log k})
\]
on fixed cubic expanders for an **asymptotic improvement over Nguyen**, or the weaker (o(k)) bound for a self-contained subexponential average-case algorithm, or rigorously prove a lower bound \(\max_i\Phi_r(S_i)\ge\varepsilon k\) for a precisely restricted ordering/potential family. This would settle the performance of this *specific* grouped-search strategy, **not** general average-case CSP hardness. The external Nguyen algorithm remains asymptotically faster regardless of the outcome.
