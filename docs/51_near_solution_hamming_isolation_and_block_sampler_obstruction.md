# Critical expander-CSP near-solutions are Hamming-frozen at linear scale

**Date:** 2026-11-03. **Status:** PROVED internal random-CSP second-moment deduction, not independently reviewed, priority/novelty unverified. This is **not** a lower bound for unrestricted sampling, simulated annealing through unsatisfied states, or exact CSP solving. It specifically obstructs **feasible-only block-update dynamics** that change at most half the variable labels at once.

Predecessors: [note 47 — near-solutions and single-site isolation](47_conditional_poisson_after_one_edge_and_endpoint_injectivity.md), [note 48 — statistical easy controls](48_karger_cut_counting_conditional_poisson_and_easy_prism_counterexample.md), [note 49 — near-solution enumeration vs treewidth](49_edge_deletion_treewidth_vs_near_solution_count.md).

## 1. Statement

Let \(G=(V,E)\) be a fixed **simple cubic \(\gamma\)-edge-expander**, \(|V|=k\), \(|E|=m=3k/2\), with girth \(g(G)\ge a\ln k\) for constants \(\gamma,a>0\). Generate all binary constraint-table entries independently with probability \(p=q^{-2/3}\) and take \(q=\lceil k^c\rceil\), where \(c>\max\{9,9/\gamma\}\) suffices.

For each edge \(e\), let \(\mathcal S_e\) be the solution set after **deleting \(e\)**; note 47 shows \(|\mathcal S_e|=(1+o_{\mathsf P}(1))q^{2/3}\) simultaneously for all \(e\).

Let
\[
 B_e=|\{\sigma\in\mathcal S_e:\exists\tau\in\mathcal S_e,\ \tau\ne\sigma,\ d_H(\sigma,\tau)\le k/2\}|.
\]

**Theorem (typical Hamming freezing).** With probability \(1-o(1)\), simultaneously for every edge \(e\),
\[
 \boxed{
 |\mathcal S_e|=(1+o(1))q^{2/3},
 \qquad
 B_e=o(q^{2/3}).
 }
\tag{1}
\]
Equivalently, a \((1-o(1))\)-fraction of the \(\Theta(q^{2/3})\) solutions to each deleted-edge CSP is **Hamming-isolated from every other solution at radius \(\lfloor k/2\rfloor\)**.

**Restricted sampling consequence:** any Markov chain whose states are **feasible near-solutions** and whose transitions modify at most \(k/2\) vertex labels has an absorbing singleton at each of these isolated states. Thus it cannot be irreducible on \(\mathcal S_e\), even with arbitrary computation inside each block update. This is substantially stronger than the single-site Glauber observation in note 47, but does **not** apply to chains that temporarily enter infeasible states or use global moves changing \(>k/2\) coordinates.

## 2. Exact near-solution pair first moment by disagreement cut

For any \(e=uv\), let \(C_e\) count **ordered pairs** \((\sigma,\tau)\) of distinct members of \(\mathcal S_e\) with Hamming distance at most \(k/2\). Then \(B_e\le C_e\).

For such a pair, put
\[
 T=\{v:\sigma(v)\ne\tau(v)\},\quad 1\le|T|\le k/2.
\]
There are \(q^k(q-1)^{|T|}\) ordered pairs with exact disagreement set \(T\). For an edge \(f\ne e\), the two assignments require **two distinct** relation-table entries precisely when \(f\) is incident to at least one vertex of \(T\). The number of those edges is
\[
 d_{G-e}(T)=\frac{3|T|+|\delta_G(T)|}{2}
 -\mathbf1[e\cap T\ne\varnothing].
\]
Both assignments satisfy every edge \(f\ne e\) with probability
\(p^{(m-1)+d_{G-e}(T)}\). Since \(q^kp^{m-1}=q^{2/3}\) and \(p=q^{-2/3}\),
\[
\boxed{
 \mathbb E C_e=
 q^{2/3}\!\!\sum_{\substack{T\subseteq V\\1\le|T|\le k/2}}
 (1-q^{-1})^{|T|}
 q^{-|\delta_G(T)|/3+
       \frac23\mathbf1[e\cap T\ne\varnothing]}.
}
\tag{2}
\]
This identity is exact for every finite \(k,q\) (aside from using real \(p=q^{-2/3}\), which is exactly the Bernoulli parameter).

## 3. Sum over small disagreement sets, using high girth

For \(1\le|T|<g(G)\), \(G[T]\) is a forest with \(r=\mathrm{cc}(G[T])\) components. Cubic regularity implies
\[
 |\delta_G(T)|=|T|+2r.
\]
Assign each nonempty connected induced vertex set \(U\) of size \(<g\) the weight
\[
 w(U)=q^{-(|U|+2)/3}.
\]
Since maximum degree is three, the number of connected sets of size \(s\) containing a specified vertex is at most \(9^s\). Thus the sum of all polymer weights obeys
\[
 H:=\sum_{U:\mathrm{connected},\,|U|<g} w(U)
 \le k\sum_{s\ge1}9^s q^{-(s+2)/3}
 =O(k/q)
\]
when \(q^{1/3}>18\). For a specified deleted edge \(e=uv\), the sum over connected \(U\) touching at least one endpoint of \(e\) is similarly
\[
 H_e=O(1/q).
\]

Each forest disagreement set \(T\) is a *collection of vertex-disjoint, pairwise nonadjacent connected components*. Dropping the disjointness/nonadjacency restriction and summing the exponential generating series yields the safe upper bounds
\[
 \sum_{\substack{T\ne\varnothing\\|T|<g}}
 q^{-|\delta(T)|/3}
 \le e^H-1=O(k/q),
\]
and
\[
 \sum_{\substack{T\ne\varnothing,\ |T|<g\\e\cap T\ne\varnothing}}
 q^{-|\delta(T)|/3}
 \le H_e e^H=O(1/q).
\]
The contribution of all \(|T|<g\) terms to (2) is therefore at most
\[
 \boxed{O(q^{2/3}\cdot k/q+q^{4/3}\cdot1/q)
 =O(kq^{-1/3}+q^{1/3}).}
\tag{3}
\]

## 4. Intermediate disagreements, using expansion

For \(g(G)\le|T|\le k/2\), expansion implies \(|\delta_G(T)|\ge\gamma|T|\). Put \(\rho=kq^{-\gamma/3}\). The contribution of these sets to (2) is bounded by
\[
 q^{4/3}\sum_{t\ge g}\binom{k}{t}q^{-\gamma t/3}
 \le q^{4/3}\sum_{t\ge g}\frac{\rho^t}{t!}
 \le q^{4/3}e^\rho\frac{\rho^g}{g!}
 =k^{-\omega(1)}
\]
when \(q=k^c\), \(c>3/\gamma\), and \(g\ge a\ln k\). Therefore uniformly over edges
\[
 \boxed{
 \mathbb E C_e
 \le O(q^{1/3}+kq^{-1/3})+k^{-\omega(1)}.
 }
\tag{4}
\]

Summing over \(m=O(k)\) edges,
\[
 \frac1{q^{2/3}}\mathbb E\left[\sum_{e\in E}B_e\right]
 \le\frac1{q^{2/3}}\sum_e\mathbb E C_e
 =O(kq^{-1/3}+k^2/q)+o(1)=o(1)
\]
for \(c>9\). Markov thus gives \(\sum_e B_e=o(q^{2/3})\) with high probability, which implies **each** \(B_e=o(q^{2/3})\) simultaneously. Combine with the all-edge near-solution-count concentration from note 47 (available for \(c>\max\{6,9/\gamma\}\)) to obtain Theorem (1).

## 5. Exact finite identity sanity check

The identity (2) can be checked independently by enumerating all ordered pairs of \(q^k\) assignments for a small cubic graph, grouping by their exact disagreement set, and comparing with the cut sum. On \(K_{3,3}\), \(q=2\), \(e=(0,3)\), \(k=6\), and Hamming radius \(k/2=3\), both computations give approximately
\[
 \mathbb E C_e=7.2733892693446.
\]
This verifies the **finite identity**, not the high-girth asymptotics (the chosen graph has girth four).

## 6. Interpretation and what algorithms remain open

- **CLOSED (restricted):** sampling near-solutions by moving between feasible assignments using updates of \(\le k/2\) variables. Almost every solution is an isolated absorbing state on the critical high-girth expander ensemble.
- **NOT CLOSED:** global direct samplers, rejection-free methods proposing large synchronized changes, simulated annealing on **infeasible** states, output-sensitive global join algorithms, and any Nguyen-type tensor solver.
- **General hardness:** Nothing here yields a computational lower bound for randomized algorithms with access to the entire input. In particular, the treewidth of the graph remains linear (note 49), but a random-instance algorithm might exploit further algebraic distributional properties.

This Hamming geometry is a structural reason that a near-solution **enumerator** cannot simply take one found solution and perform local walk updates to obtain the other \(q^{2/3}\) solutions. Even blocks of linear size \(\le k/2\) do not help for almost all solution states.

**Related literature/priority warning:** reconstruction and clustering in random CSPs is a mature area (e.g. Montanari–Restrepo–Tetali, *Reconstruction and Clustering in Random Constraint Satisfaction Problems*, SIAM J. Discrete Math. 2011, https://doi.org/10.1137/090755862 ). The precise Bernoulli large-domain calculation is an internal deduction, not a claimed new general clustering principle or publication priority.
