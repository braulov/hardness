# Uniform coarse-partition matching saturation and the limits of row-sensitive grouping

**Research date:** 2026-11-02. **Status:** unconditional random-graph lemma with full proof; elementary parameter consequences for a **particular pairwise vertex-cover factorization** of CSP group interactions. This is *not* an unconditional CSP algorithm or lower bound. It strengthens [note 39](39_adaptive_block_rank_barrier.md) at the opposite (coarse-group) scale and supersedes the fixed-partition assumption in [note 40](40_nguyen_grouping_overhead_and_random_csp_greedy.md) for this range.

## 1. Strong coarse-partition lemma: all adaptive balanced partitions simultaneously

Let d=sqrt(log k), p=d/k, and G~G(k,p). Consider every integer g with 2<=g<=d/(100 log d) and every **balanced** partition into g parts, of sizes floor(k/g) or ceil(k/g), which may be selected after inspecting all of G.

**Theorem.** With probability 1-o(1), simultaneously for all these g and partitions, for all distinct i,j,
\[
\nu(G[A_i,A_j])\ge \left\lfloor\frac{1}{2}\left\lfloor\frac{k}{g}\right\rfloor\right\rfloor
=\frac{k}{2g}-O(1).
\tag{1}
\]
Here nu means maximum matching size in the bipartite cross-edge graph.

**Proof.** Fix g and put t=floor(floor(k/g)/2). If there exist two disjoint sets S,T of size t with no edge between them, then
\[
\Pr[\exists S,T]\le {k\choose t}^2(1-p)^{t^2}
\le \exp\!\left(t[2\log(ek/t)-pt]\right).
\]
For all g in the stated range, t>=k/(3g), hence pt>=d/(3g)>= (100/3)log d. Meanwhile log(ek/t)<=log(3eg)<=2log d for large d. Consequently the displayed probability is at most exp(-c t log d) for an absolute c>0. A union bound over at most d values of g still gives o(1), since t>=k/(3d) and k/d diverges.

On the resulting event, **every** two disjoint sets of at least t vertices have an edge. If a balanced pair A_i,A_j had matching number <t, by König's theorem the crossing edges would have a vertex cover of size <t. Removing this cover leaves at least t vertices in each part without any crossing edges: contradiction. No union bound over partitions is needed because the empty-rectangle event was quantified over *all* vertex subsets. QED.

The above random-graph statement is about the primal GRAPH, not about its relation tables. It is not a guarantee that arbitrary given relation tables have full joint rank, nor that one fixed collection of relations is hard simultaneously against all partitions.

## 2. Why replacing gP by sum of row capacities is asymptotically vacuous here

Let b=ceil(log2(q)). For each pair of vertex blocks use the **explicit minimum-vertex-cover factorization** (not a potentially smaller relation-specific factorization) from [note 37](37_joint_block_matching_rank_and_arity.md). Its interface length is
\[
c_{ij}=b\,\nu(G[A_i,A_j]).
\]
Let $\rho_i=\sum_{j\ne i}c_{ij}$ be the row bond length and $\ell_i=b|A_i|$ be the group setting length. Let the minimal necessary group capacity be
\[
P_i=\max\{\ell_i,\rho_i\},\quad P=\max_iP_i,\quad
U=\sum_{i<j}c_{ij}.
\]
On the graph event of Section 1, for every balanced partition with 2<=g<=d/(100log d),
\[
\frac{(g-1)kb}{3g}\le\rho_i\le(g-1)\lceil k/g\rceil b.
\]
Consequently
\[
P=\Theta(kb),\qquad \sum_iP_i=\Theta(gkb),\qquad
U=\Theta(gkb),\qquad gP=\Theta(gkb).
\tag{2}
\]
(The constants can be taken absolute and the asymptotics are uniform over the listed g.)

Therefore a hoped-for replacement of the imported grouping overhead $gP/K$ by $(\sum_iP_i)/K$ does not provide a superconstant saving **for this particular cover-based factorization on this random graph family**. Both terms have order $gkb/K$.

In Nguyen's [Theorem 1.2 / Proposition 3.1](https://hub.valency.io/works/W_88675vdy), $g=3K^8$, so the corresponding overhead term in the **published bound** has order
\[
gP/K=\Theta(kb K^7)
\]
whenever the coarse range and partition assumptions above hold. The certified clique rate only gives $e_K=O(1/\sqrt{\log K})$; the known upper bound from the imported theorem is insufficient to certify sub-$q^k$ time by simply substituting these cover factors.

**Caveat:** the formula for a runtime *upper bound* being too large is not a runtime *lower bound*. A better implementation, relation-specific low-rank interfaces, or a new recursion may avoid the estimate. The formula does not refute the mathematical existence of a better CSP algorithm.

## 3. Matching the fine-partition barrier

At fine scale, [note 39](39_adaptive_block_rank_barrier.md) shows that with high probability **all** graph-adaptive partitions with blocks of size <=k^{1-eps} obey
\[
\sum_{i<j}\nu(G[A_i,A_j])\ge m-O(k)
=(1-o(1))m,\qquad m=\Theta(kd).
\]
Hence these small-block pairwise cover factorizations use essentially the original $m$ q-symbol channels.

At coarse scale, this note proves that even graph-adaptive balanced partitions with g=o(d/log d) have **saturated pair interactions** $\nu(A_i,A_j)=\Omega(k/g)$, and hence $U=\Theta(gkb)$. Those are the two complementary reasons ordinary pairwise grouping does not yield a new sub-$q^k$ bound through the *existing* recursive contraction estimate.

No conclusion is claimed for arbitrary very unbalanced partitions with a giant block, or for arbitrary global multilevel sharing.

## 4. An unconditional oracle lower bound on capacity-only grouping

Consider a single vertex carrying an arbitrary table-query oracle $W:\{0,1\}^{\ell}\to\{0,1\}$, with no edges, so U=0. Its network value is
\[
Z_W=\sum_{x\in\{0,1\}^{\ell}}W(x).
\]
Any deterministic algorithm that must compute $Z_W$ for ALL such oracles needs at least $2^\ell$ oracle queries. If it leaves one input unseen, it cannot distinguish W=0 from a function equal to 1 only at that unseen point. Any bounded-error randomized oracle algorithm distinguishing these two promise types also needs $\Omega(2^\ell)$ queries by Yao's principle (the location of the unique 1 is chosen uniformly).

Therefore a **generic black-box** counting/grouping theorem cannot have running time depending *only* on external bond capacity U, independent of the amount/structure of local setting information. This proves that some local-weight complexity charge is indispensable in such an oracle model.

**Scope:** compactly described local weights (for example, polynomial-size circuits or explicitly tabulated binary CSP relations) are NOT arbitrary oracle tables. This does **not** establish an exponential lower bound for compact CSP input, prove #P != FP, or disprove a structural fast SAT algorithm. It is a sanity check against overoptimistic capacity-only conjectures.

## 5. Revised concrete algorithmic target

Replacing g*max(row capacity) by sum(row capacity) is not enough on the balanced coarse random graphs. Any real gain must do one of the following:

(a) exploit *relation-specific* factorizations with shared latent variables across several group pairs (so messages are NOT independent pairwise cover labels);
(b) exploit structured local-weight computation to avoid the arbitrary-oracle lower bound, while keeping the cost of evaluating internal sums explicit;
(c) improve the growing-degree dependence of the Nguyen tensor recursion with a genuinely uniform theorem f(Delta)=o(Delta), as quantified in [note 38](38_multilevel_factorization_and_degree_uniformity.md).

A candidate construction must track: source k,m,q; number and sizes of groups; local setting lengths; total bond bits; polynomial-time procedures for local entries; numerical precision; imported recursion parameters K,g,P,B,U and their exact runtime charges; and any existential-witness adaptivity. A reduction of U alone is not a complete algorithm.

**Status:** no generic q^{o(k)} algorithm for m=Theta(k sqrt(log k)); no general hardness result. Only the architecture-specific saturation and the oracle-model query lemma are proved here.

## References

- [Full Nguyen grouping formulas (15)–(18)](https://hub.valency.io/works/W_88675vdy).
- [Anthropic quantitative tensor-recursion overview](https://github.com/anthropics/formal-math/blob/main/eth/README.md).
- [Adaptive fine partition saturation](39_adaptive_block_rank_barrier.md).
- [Joint interaction rank via bipartite matching](37_joint_block_matching_rank_and_arity.md).
- [Growing-degree CSP criterion and earlier fixed-partition calculation](38_multilevel_factorization_and_degree_uniformity.md).


**Decision-only contrast (2026-11-02):** The negative results here concern exact pairwise *tensor interface* factorization. [Note 42](42_robust_alphabet_quotients_fullrank_dense_csp.md) instead proves a robust alphabet quotient with exact **SAT iff**, even when every edge matrix has full rank $q$. Such a quotient is discovered by multi-edge Hamming signatures and supports greedy witness lifting, but generally does NOT preserve the exact number of witnesses. It bypasses the rank-based *method*, not the unsolved arbitrary-CSP algorithmic question.
