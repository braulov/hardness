# Random sparse CSP near-solutions: deleting few constraints preserves linear treewidth

**Date:** 2026-11-03  
**Status:** PROVED elementary graph separator lemma and exact random-CSP first moment. The class-specific algorithmic tradeoff is rigorous; this is **not** a time lower bound for arbitrary enumeration algorithms. No claim of publication novelty. Research motivation: finding the typically \(q^{2/3}\) solutions after deleting just one edge (notes 47/48).

## 1. Robust treewidth of bounded-degree expanders under edge deletion

Let \(G\) be a simple graph with \(k\) vertices, maximum degree \(\Delta\), and edge expansion \(\gamma>0\):
\[
 |\delta_G(X)|\ge\gamma\min(|X|,k-|X|)
 \quad\text{for every }X\subseteq V(G).
\]
Delete an arbitrary (possibly input-adaptively selected) set \(D\subseteq E(G)\) of \(t\) edges, and put \(H=G-D\), \(w=\mathrm{tw}(H)\).

**Theorem A (deterministic and universal over \(D\)).**
\[
 \boxed{t+\Delta(w+1)\ge\gamma k/4.}
\tag{1}
\]
In particular for cubic \(G\),
\[
 \boxed{t+3(w+1)\ge\gamma k/4.}
\tag{2}
\]

**Proof.** From a width-\(w\) tree decomposition of \(H\), take a bag \(X\) of size at most \(w+1\) which is a \(\tfrac12\)-balanced separator: each component of \(H-X\) has at most \(k/2\) vertices. This standard bag separator exists by assigning each vertex to one topmost bag and taking a weighted centroid bag of the tree decomposition.

If \(|X|\ge k/4\), the desired inequality follows from
\(\Delta|X|\ge\Delta k/4\ge\gamma k/4\) since \(\gamma\le\Delta\).

Otherwise \(|X|<k/4\), and there are at least \(3k/4\) vertices outside \(X\). Select a union \(A\) of components of \(H-X\) with \(k/4\le|A|\le k/2\): if a component has size in this range, take it; otherwise all components have size below \(k/4\), and greedily accumulate them until their union first reaches \(k/4\), then its size is below \(k/2\).

All edges of \(H\) leaving \(A\) end at \(X\), so
\[
 |\delta_G(A)|
 \le |E_H(A,X)|+|D|
 \le\Delta|X|+t
 \le\Delta(w+1)+t.
\]
By expansion and \(k/4\le|A|\le k/2\), the LHS is at least \(\gamma k/4\). This proves (1). ∎

The conclusion is robust under arbitrary **edge choices** and does not assume that \(D\) is fixed in advance or independent of the CSP relation tables.

## 2. Every removed constraint multiplies the expected number of assignments by \(q^{2/3}\)

Now take a fixed **3-regular** \(G\), so \(m=3k/2\), and generate independent Bernoulli-\(p\) full relations on each edge with \(p=q^{-2/3}\).

For any **fixed** \(D\subseteq E(G)\) of \(t\) edges, let \(Z_{-D}\) be the number of assignments satisfying all edges outside \(D\). Every assignment must satisfy \(m-t\) independent entries, therefore
\[
 \boxed{\mathbb E Z_{-D}
 =q^kp^{m-t}=q^{2t/3}.}
\tag{3}
\]

Under the extra standard assumption of edge expansion and \(q=k^c\) for sufficiently large constant \(c\), note 36 gives a second-moment bound uniform in *any preselected* proper retained-edge set:
\[
 \frac{\mathrm{Var}(Z_{-D})}{(\mathbb E Z_{-D})^2}
 \le\eta_k=q^{-2/3}
   +2\bigl[(1+q^{-\gamma/3})^k-1\bigr]=o(1),
 \quad t\ge1.
\]
Thus for each **table-independent** \(D\), \(Z_{-D}=(1+o_{\mathsf P}(1))q^{2t/3}\). **Do NOT claim simultaneous concentration for every \(D\) or apply this expectation automatically to a relation-table-adaptively chosen \(D\)**: selection bias matters and the naive second-moment union bound does not cover exponentially many sets \(D\).

## 3. Precise failure of the naive output-sensitive route

A classical exact CSP enumeration scheme:
1. choose and delete \(D\);
2. find a width-\(w\) tree decomposition of \(G-D\), preprocess extension tables using \(q^{w+1}\operatorname{poly}(k,q)\) arithmetic/Boolean operations;
3. enumerate all \(Z_{-D}\) satisfying assignments of the retained constraints with polynomial delay, checking removed-edge relations on each.

For a **preselected** set \(D\) and a supplied width-\(w\) decomposition, standard tree-CSP dynamic programming supports such enumeration, with a conservative expected runtime *upper bound*
\[
 \operatorname{poly}(k,q)\left(q^{w+1}+q^{2t/3}\right).
\tag{4}
\]
This is an **algorithmic upper bound**, not a lower bound; a more clever algorithm on the same subinstance may use less than \(q^w\) time, so one cannot infer generic runtime hardness from (1).

Equation (1) gives the unavoidable **parameter tradeoff**:
- If \(t=O(1)\) so only \(q^{O(1)}\) near-solutions are expected, then \(w\ge\gamma k/(4\Delta)-O(1)=\Omega(k)\).
- If \(w=o(k)\) so the standard tree-DP preprocessing has sublinear q-exponent, then \(t\ge\gamma k/4-o(k)\), and \(Z_{-D}\) has expectation at least \(q^{\gamma k/6-o(k)}\) in the cubic model.
- Consequently no choice of deletion set \(D\) can simultaneously satisfy \(w=o(k)\) and \(t=o(k)\). In particular, the "remove one edge, enumerate \(q^{2/3}\) near-solutions by **small-treewidth** DP" plan is impossible on expanders *as a structural plan*.

For graph classes *admitting* supplied \(D\) with \(w=o(k)\), \(t=o(k)\), the very same scheme **does** give an **unconditional** \(q^{o(k)}\operatorname{poly}(k,q)\) *expected-time* algorithm for the critical random ensemble. With \(w,t=O(1)\), expected time is polynomial. This is a valid positive result on near-bounded-treewidth graph classes, and it explains the easy 3-edge-connected prism control in note 48.

## 4. What survives, and a separate proposed direction

We have not proved lower bounds on:
- unrestricted algorithms enumerating the polynomially many near-solutions in \(\Gamma_{-e}\) without a tree-decomposition;
- randomized global algebraic samplers, high-rank tensor contraction, or conditional partition-function approximations;
- algorithms choosing \(D\) *adaptively* using relation-table contents and exploiting correlations in the resulting subinstances.

The deterministic tradeoff (1) still holds for every adaptively selected \(D\), but (3)'s expected-solution assertion for the selected \(D\) does not follow.

A promising algorithmic alternative is to find a **global sampler or output-sensitive join** that directly enumerates the polynomial-sized near-solution set in time \(\operatorname{poly}(k,q,Z_{-e})\) *even though the retained graph has linear treewidth*. See [note 47](47_conditional_poisson_after_one_edge_and_endpoint_injectivity.md). The challenge is global constraint coupling, not enumerating small-treewidth local solutions.

**Attribution and literature context:** balanced treewidth separators are standard. Graph deletion into bounded treewidth has an extensive literature; see Gupta–Lee–Li–Manurangsi–Włodarczyk, [*Losing Treewidth by Separating Subsets*, SODA 2019](https://doi.org/10.1137/1.9781611975482.104). Equations (1)–(3) are elementary and are not asserted to be new published results.
