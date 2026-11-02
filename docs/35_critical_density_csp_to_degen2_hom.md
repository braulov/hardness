# Critical-density polynomial-alphabet 2-CSP as a surviving HOM hardness candidate

**Research note, 2026-11-02. Status:** the reductions and exponent bookkeeping below are elementary / direct extensions of an existing construction. The **critical-density hardness hypothesis is NEW AND UNPROVED**, and is NOT a consequence of ETH, CEH, SPACH, or any checked conjecture. All use of the November 2026 Nguyen/OpenAI algorithms is conditional on those externally claimed results.

## 1. The narrow question

After [CEH/SPACH closure](34_csp_hypothesis_closure_registry_2026_11_02.md), is there a polynomial-alphabet binary CSP source that could still exclude a **single-exponential** algorithm for $\mathrm{HOM}(G,H)$ with a *polynomial-size 2-degenerate target* $H$?

Yes, **as a conditional hardness template**, by allowing mildly superlinear constraint count $m$ rather than $m=O(k)$.

Write $k$ for source CSP variables, $m$ for constraints, $q=\lceil k^c\rceil$ for a **fixed** constant $c>0$, and $L$ for complete-table input length. Fix $\alpha\in[0,1)$ and an absolute $B>0$. Define the proposed **intermediate-density CSP hypothesis $\mathrm{ID\text{-}CSP}_{\alpha,c,B}$**:

> There is no uniform algorithm deciding every explicitly represented binary CSP on $k$ variables, domain $[q]$, with $m\le Bk(\log k)^\alpha$ constraints, in time $q^{o(k)}\operatorname{poly}(L)$.

This is a *hardness assumption*, not a theorem. Define deterministic and bounded-error randomized variants separately. Multiple constraints on the same variable pair can be combined by relation intersection; loops are unary and easily eliminated, so assume a simple graph if desired. The family has $\operatorname{poly}(k)$ explicit input size for fixed $c,B,\alpha$.

**For $\alpha<1/2$ this assumption is already conditionally false** under the Nguyen theorem / full OpenAI tensor-contraction theorem. For $\alpha=1/2$ it is *not contradicted by the known bound*, and for $1/2<\alpha<1$ it likewise survives this particular algorithm. This says nothing about other, potentially faster algorithms.

## 2. The easy direction: degree splitting and the algorithmic threshold

Given a general binary CSP with $k$ variables and $m$ binary constraints, create one occurrence copy per constraint-variable incidence and link the copies belonging to each original variable in a path by binary equality constraints. Every copy has at most three incident constraints. Isolated variables may be handled separately. This gives degree at most 3, with
\[
k'=O(k+m),\qquad m'=O(k+m),\qquad q'=q.
\]
All relation tables remain explicit and the construction is polynomial in $L$, since $q=k^c$.

**Assuming Nguyen's domain-uniform Theorem 1.2**, solve the new bounded-degree instance by deterministic counting in
\[
\operatorname{poly}(L)\cdot q^{O((k+m)/\sqrt{\log(k+m)})}.
\tag{A}
\]
The same bound in the polynomial-$q$ regime follows, **conditional on the full Boolean tensor theorem** described in [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).

If $m=O(k(\log k)^\alpha)$,
\[
\log_q T=O\bigl(k(\log k)^{\alpha-\tfrac12}\bigr)
\]
for any fixed $0\le\alpha<1$ (and up to harmless terms when $m$ is small).

| $\alpha$ | Result of (A) | Compatibility with no-$q^{o(k)}$ hypothesis |
|---|---|---|
| $\alpha<1/2$ | $q^{o(k)}$ | **INCOMPATIBLE** (conditionally refuted) |
| $\alpha=1/2$ | $q^{O(k)}$ | Not refuted by this estimate |
| $1/2<\alpha<1$ | $q^{O(k\log^{\alpha-1/2} k)}$ (weaker than the trivial $q^k$ bound) | Not refuted by this estimate |

The threshold $\alpha=1/2$ is only the point where **this particular upper bound** ceases to be sub-$q^k$. It is not a lower-bound theorem or a density phase transition established for CSP itself.

## 3. Extending HOM paper §4 to $m$ not necessarily linear in $k$

The source construction is the **sparse pinning frame**, types for every original variable and every constraint, one source value vertex per original variable, and one source constraint vertex per constraint. Target vertices encode either values $(v,a)$ or compatible endpoint pairs $(e,a,b)$.

In the published statement, §4.2 of [Braulov–Chukhin–Kulikov–Mihajlin, arXiv:2607.09377](https://arxiv.org/html/2607.09377) starts from a simple bipartite cubic constraint graph, because that is the hard source invoked there. The pinning proof (Lemmas 4.3–4.6) and three-subdivision trick (Lemmas 4.7–4.8) use **only** the fact that the distinct types are correctly pinned, not cubic regularity or bipartiteness of the CSP constraint graph.

Consequently the same explicitly described construction extends to an arbitrary simple binary CSP constraint graph with $k$ vertices and $m$ edges; with $t=k+m$ types and a frame of size $O(t)$:

- Source before subdivision: $O(k+m)$ vertices and $O(k+m)$ edges (frame $O(t)$, $k$ variable vertices and $m$ constraint vertices).
- Target before subdivision: $O(k+m+kq+mq^2)$ vertices **and edges**, since each value vertex has two pin edges and each pair-constraint vertex has three edges.
- Subdivide every edge of each graph into a 3-edge path; Lemma 4.7 preserves the homomorphism relation, and Lemma 4.8 makes the target **2-degenerate**.

Therefore the fully ordinary HOM instance $(G,H)$ satisfies
\[
\Gamma\in\mathrm{SAT}\iff G\to H,\quad
n=|V(G)|=O(k+m),\quad
|E(G)|=O(k+m),\quad
h=|V(H)|=O(k+m+kq+mq^2),\quad
\operatorname{degen}(H)\le2.
\tag{B}
\]
For $q=k^c$ and $m=O(k\log^\alpha k)$ this gives $h=\operatorname{poly}(n)$, and the reduction runs in $\operatorname{poly}(L)$ time.

**Proof-status nuance:** The extension to arbitrary source degree is a short, transparent audit of the existing §4 gadget proof, not a theorem explicitly stated in the published manuscript under these parameters. Before submitting a new paper, spell out all edge/type pinning and source graph size constants formally.

## 4. Conditional theorem: critical-density CSP hardness forbids fast degeneracy-2 HOM

**Theorem (conditional, elementary exponent transfer).** Fix $c>0$, $B>0$ and $0\le\alpha<1$. If $\mathrm{ID\text{-}CSP}_{\alpha,c,B}$ holds, then there is **no uniform** algorithm solving every sparse-source HOM instance $(G,H)$ with $\operatorname{degen}(H)\le2$ and $h=n^{O(1)}$ in time
\[
\boxed{2^{o(n(\log n)^{1-\alpha})}\operatorname{poly}(n,h).}
\tag{C}
\]

**Proof.** Apply reduction (B) to arbitrary promised CSP instances. Then $n=O(k\log^\alpha k)$, $n\ge\Omega(k)$, and $\log n=\Theta(\log k)$. If an algorithm with time (C) existed, its exponential factor on the reduced instances would be
\[
2^{o(k(\log k)^\alpha\cdot(\log k)^{1-\alpha})}
=2^{o(k\log k)}
=q^{o(k)}.
\]
The reduction and the target polynomial prefactor cost only $\operatorname{poly}(L)$. Contradiction.

**Critical case $\alpha=1/2$:**
\[
\boxed{
\mathrm{ID\text{-}CSP}_{1/2}
\Longrightarrow
\text{no }2^{o(n\sqrt{\log n})}\operatorname{poly}(n,h)
\text{ HOM algorithm on sparse }G,\;
\operatorname{degen}(H)\le2,\;h=\operatorname{poly}(n).
}
\tag{D}
\]
This automatically excludes $2^{O(n)}\operatorname{poly}(n,h)$, since $2^{O(n)}=2^{o(n\sqrt{\log n})}$.

**The upper bound at the same exponent:** For **every** sparse-source HOM, encoding each source vertex as a $q=h$-valued CSP variable yields $m=O(n)$ constraints. Conditional on Nguyen,
\[
T_{\mathrm{HOM}}(n,h)=\operatorname{poly}(n,h)\,h^{O(n/\sqrt{\log n})}
=2^{O(n\sqrt{\log n})}\operatorname{poly}(n,h)\quad(h=n^{O(1)}).
\tag{E}
\]
Thus the critical density hypothesis, *if true*, exactly matches the new upper-bound exponent on this restricted HOM class up to the $O/o$ distinction. **This is not evidence that the hypothesis is true.**

For $1/2<\alpha<1$, (C) becomes a weaker bound $2^{o(n\log^{1-\alpha}n)}$; only at $\alpha=1/2$ do the available CSP upper and conditional HOM lower exponents meet.

## 5. What survives / what's new about the question

- The old **SPACH and CEH no-$q^{o(k)}$ assumptions with $m=O(k)$ are closed** under the November algorithms; this note does not resurrect them.
- $\mathrm{ID\text{-}CSP}_{1/2}$ allows $m=\Theta(k\sqrt{\log k})$ and *unbounded / growing source constraint-graph degree*; after degree splitting there are $\Theta(k\sqrt{\log k})$ variables. Nguyen's constant-degree bound does not contradict the source claim.
- An even weaker separate survivor is **NoSingleExpSparseCSP**: no $2^{O(k)}\operatorname{poly}(L)$ algorithm when $m=O(k)$ and $q=k^c$; it excludes a HOM $2^{O(n)}$ algorithm by (B), but does **not** directly match the $2^{O(n\sqrt{\log n})}$ HOM upper bound.
- Neither survivor is derived from ETH, SETH, PCC, PSCH, LogSAT-A/B, or Circuit-SAT in this repository. The arbitrary dense-source to intermediate-density compilation needed to establish such implications remains OPEN.
- A hypothetical fixed-expander/compiler project can remain mathematically interesting, but is no longer needed for the simple **conditional** HOM reduction (B) from intermediate-density CSP.

## 6. Research tasks

1. **Strongest first:** Try to obtain a $q^{o(k)}$ algorithm for arbitrary $k$-variable, $m=O(k\sqrt{\log k})$, polynomial-domain binary CSP. If successful, the $\alpha=1/2$ candidate also collapses and the algorithm may feed directly into HOM.
2. **Hardness-source alternative:** Identify an independently plausible $2^{o(k\log k)}$-hard special input class with $O(k\sqrt{\log k})$ constraints, or a *linear-preserving* reduction from a **surviving** dense-CSP/LogSAT/PCC hypothesis to it. This is a substantial open compression problem; no bridge is claimed.
3. **Prove §4 generalization formally**, checking pinning for arbitrary source constraint graph degree, self-loops, parallel constraints, and target source-edge sizes. Handle repeated edges by intersecting relations and loops as unary restrictions.
4. If one needs lower bounds for general (possibly dense-source) HOM, any sparse-source lower bound automatically rules out universal algorithms; the matching upper bound (E) is claimed **only for sparse-source** HOM.
5. Maintain the logical distinction between “algorithm bound stops refuting a hypothesis” and “evidence supports that hypothesis.”

## 7. References

- Nguyen (2026-11-02): https://hexagonmath.org/2611.00004v1
- Full tensor theorem analysis: [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).
- Earlier closure ledger: [note 34](34_csp_hypothesis_closure_registry_2026_11_02.md).
- Original pinning and subdivision gadget, §4: https://arxiv.org/html/2607.09377.


## 8. A concrete ALGORITHMIC attack: any superconstant savings in tensor wires would kill the critical hypothesis

In the *critical* case $m=\Theta(k\sqrt{\log k})$, $q=k^c$ and $b=\Theta(\log k)$, the direct Boolean tensorization of [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md) uses
\[
M=\Theta((k+m)b)=\Theta(k(\log k)^{3/2})
\]
bit wires. The **externally claimed full Boolean tensor theorem** evaluates this in time
\[
2^{O(M/\sqrt{\log M})}
=2^{O(k\log k)}
=q^{O(k)}.
\]
This is exactly the threshold at which the new CSP counting bound stops refuting a no-$q^{o(k)}$ hypothesis.

**Sufficient algorithmic breakthrough:** Find a uniform, polynomial-time **exact** tensorization of *every* such critical-density CSP with
\[
M'=o(k(\log k)^{3/2})
\]
bit wires and compatible polynomial-time local-entry queries, legal local degrees and modulus/precision. Use the theorem's size parameter $S=\Theta(\max\{M',k\log k\})$ (padding if required to accommodate $P_0=k\lceil\log_2q\rceil+1$ precision bits). Since $S=o(k(\log k)^{3/2})$, the full tensor theorem would give
\[
2^{O(S/\sqrt{\log S})}=2^{o(k\log k)}=q^{o(k)},
\]
conditionally refuting the critical-density hypothesis.

For example, an $\Omega(\log\log k)$-fold reduction in wire count, from $\Theta(k\log^{3/2}k)$ to $O(k\log^{3/2}k/\log\log k)$, would yield $q^{O(k/\log\log k)}$. (Polytime construction and input-size factors still need checking.)

**Caveat:** This is an upper-bound research target, not a proven compression. Naive equality-copy trees already use $\Theta(m\log q)$ wires for independent relation interfaces, so savings must come from *joint constraint batching*, implicit multilinear tensors or more sophisticated grouped support. Merely hiding a superpolynomial tensor table inside one high-degree vertex is invalid. The repository's prior [projected-support / edge-bucket experiment](12_projected_support_edge_buckets.md) is relevant structurally, but does not already provide this universal reduction.

If such a method is found, it would give a meaningful algorithmic result rather than a new hardness assumption, and by the §4 gadget it might improve algorithms on a structured family of 2-degenerate HOM instances.


**Follow-up (2026-11-02):** [Rank-dual exact CSP counting, sparse-partner branching, and the literal edge-bucket barrier](36_rank_dual_critical_csp.md). An exact integer Smith-factorization of each relation yields an **unconditional** solver of time poly(L) * product_e rank_Q(R_e); hence m=O(k sqrt(log k)) CSP is already q^{o(k)} when ranks are uniformly at most 2^{o(sqrt(log k))}. Low allowed-partner degree gives an independent spanning-tree solver. Conversely, with high probability a random critical-density primal graph has no dense subgraphs of size <=k^{1-eps}, preventing any superconstant wire savings by raw q-value edge-bucket grouping of such small supports. This is strictly a **model-specific** obstacle, not a general CSP lower bound.

**Joint-factor follow-up (2026-11-02):** [Exact matching-number formula for cross-block CSP relation rank and the large-tensor arity bottleneck](37_joint_block_matching_rank_and_arity.md). For arbitrary tables, the maximum rank of the joint interaction matrix across groups A,B is exactly q^(maximum matching in G[A,B]). This permits a substantial formal reduction in bonds when many edges share block endpoints, but a naive full-group tensor violates the external contraction theorem's maximum-local-degree bound precisely in the useful regime. No general critical-density CSP algorithm is obtained.
