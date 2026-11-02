# Multilevel block factorization and growing-degree CSP: two quantitative bottlenecks

**Date:** 2026-11-02. **Status:** elementary probabilistic and parameter calculations; **NO general new CSP algorithm**. The external November CSP counting theorem is a conditional premise when used. Companion to [critical-density CSP](35_critical_density_csp_to_degen2_hom.md), [rank-dual factorization](36_rank_dual_critical_csp.md), and [joint rank](37_joint_block_matching_rank_and_arity.md).

## 1. Fixed fine partitions destroy the worst-case joint-rank saving

Let $d=\sqrt{\log k}$, $p=d/k$, and $G\sim G(k,p)$. For simplicity suppose $g\mid k$ and fix *in advance, independently of $G$* a balanced partition $V=A_1\dot\cup\cdots\dot\cup A_g$ with $s=k/g$. Let
\[
W_g=\sum_{i<j}\nu(G[A_i,A_j]),
\]
where $\nu$ is maximum matching size. By [note 37](37_joint_block_matching_rank_and_arity.md), $W_g\log_2q$ is exactly the worst-case total log-rank capacity of the independently factorized pair-interaction matrices between these groups.

**Lemma (fixed fine partitions).** If $g/d\to\infty$, then with probability $1-o(1)$,
\[
W_g=(1-o(1))m,\qquad m=|E(G)|=\Theta(kd).
\tag{1}
\]

**Proof.** Let $P$ count unordered pairs of distinct cross-block edges that share one endpoint *and also go to the same partner block*. At a vertex $v$ and other block $A_j$, the neighbor count is $\operatorname{Bin}(s,p)$, so
\[
\mathbb EP=k(g-1){s\choose2}p^2=O(kd^2/g)=o(kd).
\]
Chernoff gives $m=(1+o(1))kd/2$ and Markov yields $P=o(m)$ with high probability. Delete at most one edge for every conflicting pair, making the cross edges in each block pair a matching; the number deleted is at most $P$. Total number of *within-group* edges has expectation $O(m/g)=o(m)$, hence is $o(m)$ with high probability. Therefore $W_g\ge m-o(m)$, while trivially $W_g\le m$. QED.

**Scope:** the partition is independent of the random input graph. An adaptive, input-dependent partition requires a separate argument; do not assert (1) uniformly over all partitions.

## 2. Quantitative one-layer/naive multilevel dilemma

If $g$ groups each hold $s=k/g$ variables, then for every graph
\[
W_g\le{g\choose2}s=O(kg).
\]
Thus $g=o(d)$ provides a formal superconstant saving versus the $m=\Theta(kd)$ original edges.

However a one-layer full-block pair factor that directly reads a complete group value has $\Theta(s\log q)=\Theta(k\log q/g)$ Boolean ports. Under the *claimed* full OpenAI tensor theorem, with desired scale $S=O(gk\log q)$ and maximum tensor degree $S^{9/10}$, feasibility would require
\[
k\log q/g\lesssim(gk\log q)^{9/10}
\implies g\gtrsim(k\log q)^{1/19}.
\tag{2}
\]
For $d=\sqrt{\log k}$, (2) is incompatible with $g=o(d)$.

If a multi-level scheme **entirely replaces** coarse pair factors by *independent* fine pair factors on fixed equal leaf groups, a leaf factor that reads its whole group under target scale $S=O(k\log q)$ requires
\[
s\log q\lesssim(k\log q)^{9/10}
\implies g_{\rm leaf}\gtrsim(k\log q)^{1/10}\gg d.
\]
By (1), these fine pair ranks cost $(1-o(1))m$: ordinary recursive regrouping returns the original wire budget.

**Not ruled out:** keeping shared latent coordinates on coarse levels and realizing their global constraints jointly. Such a construction need not decompose into independent fine-pair factorizations and is precisely the unresolved research challenge.

## 3. Alternative breakthrough target: improve the growing-degree dependence

The new Nguyen (Hexagon 2611.00004v1) theorem is stated **for each fixed Delta**, with time $L^{O_\Delta(1)}q^{C_\Delta n/\sqrt{\log n}}$. Its stated quantifiers **do not justify plugging in growing Delta**. Define the new *hypothetical, uniform-in-growing-Delta* algorithmic statement:
\[
T(n,q,\Delta)\le\operatorname{poly}(L)\,
q^{O(f(\Delta)n/\sqrt{\log n})}
\tag{3}
\]
for $\Delta$ as large as $\log\log n$, $q=n^{O(1)}$, and an exponent constant independent of $n,q,\Delta$. More general prefactors are allowed only if they contribute $q^{o(k)}$ to the final reduction.

**Elementary degree-splitting lemma.** For all integers $\Delta\ge4$, every explicitly tabulated binary CSP with $k$ variables and $m$ constraints admits a polynomial-time SAT-iff and count-preserving reduction with the same domain $q$ to degree $\le\Delta$ and
\[
k'\le k+\frac{2m}{\Delta-2}+O(k),\qquad
m'\le m+O(k+m/\Delta).
\tag{4}
\]
For original variable degree $t$, use $\max(1,\lceil t/(\Delta-2)\rceil)$ copies; split original incident edges among copies and connect copies by an equality path. (If a variable has zero occurrences, keep one copy.) Each copy has at most $\Delta-2$ original edges and two equality edges, and every legal original assignment has a unique extension. Explicit equality relations cost polynomial time because $q=k^{O(1)}$.

For critical $m=O(kd)$, $d=\sqrt{\log k}$, choose $4\le\Delta\le d$ growing, for example $\Delta=\lceil\log\log k\rceil+4$. Then $k'=O(kd/\Delta)$ and $\log k'=\Theta(\log k)$. Under (3):
\[
\log_q T=
O\left(\frac{kd}{\Delta}
\frac{f(\Delta)}{\sqrt{\log k}}\right)
=O\left(k\,\frac{f(\Delta)}{\Delta}\right).
\tag{5}
\]
Thus **any uniform sublinear degree dependence** $f(\Delta)=o(\Delta)$ along an unbounded sequence $\Delta\lesssim d$ would produce $q^{o(k)}$ for *all* critical-density polynomial-domain CSP and conditionally refute the intermediate-density hardness hypothesis.

For example, $f(\Delta)=O(\sqrt\Delta)$, $\Delta=\Theta(\log\log k)$ gives $q^{O(k/\sqrt{\log\log k})}$.

**What is actually known here:** the direct bit-wire construction plus the external full tensor theorem yields effectively $f(\Delta)=O(\Delta)$, with no saving after (4). The sublinear function in (3) is an open algorithmic goal, not a consequence of Nguyen's published fixed-Delta theorem. Improving degree dependence may be a more productive target than explicit multi-level wire compression; both ultimately require reusing information across constraints.

## 4. Next steps

- Work directly on uniform-in-Delta CSP tensor recursion and aim for $f(\Delta)=O(\Delta/\log\Delta)$ or $O(\sqrt\Delta)$ at growing Delta.
- Search for **shared latent-variable** multi-level factorizations that evade the independent fine-pair decomposition and preserve polynomial-time local entries, the theorem's arity cutoff, precision and exact counting.
- For any claimed randomized compression, distinguish fixed-witness fingerprinting from soundness against existentially adaptive witnesses.
- Continue to treat the open critical-density no-$q^{o(k)}$ hypothesis as a hypothesis, not as established lower-bound evidence for HOM.

**Sources:** [Nguyen, Hexagon 2611.00004v1](https://hexagonmath.org/2611.00004v1); [full Boolean tensor-contraction analysis](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).


## 5. Source-level check: why Nguyen's published grouping does not use the matching compression

The publicly indexed full text of [Nguyen 2611.00004v1](https://hub.valency.io/works/W_88675vdy) gives its grouped network capacities (25)–(26) as
\[
P=\Delta bs,\quad U\le gP\le2\Delta bk,\quad b=\lceil\log_2q\rceil.
\]
It constructs the cross-group factorization using one $q$-label $\theta_e$ **per crossing edge**. Our [joint-rank lemma](37_joint_block_matching_rank_and_arity.md) permits instead one $q$-label per vertex of a minimum cover of the cross-edge bipartite graph, costing $\nu(A_i,A_j)b$ bits per pair; the factors remain polynomial-time evaluable per query.

**But the proof's clique level chooses**
\[
g=3K^8,\qquad K^{32}\le k<K^{320},
\quad\Longrightarrow\quad
3k^{1/40}<g\le3k^{1/4}.
\]
Therefore $g\gg\Delta$ for every $\Delta=\operatorname{polylog}k$, and on a random critical-degree graph, for a fixed oblivious balanced partition, our Section 1 lemma gives
\[
\sum_{i<j}\nu(A_i,A_j)=(1-o(1))m.
\]
So simply replacing $\theta_e$ by matching-cover labels **does not improve the published application** on the generic critical-density family.

**Important caveat on possible research improvements:** One cannot freely choose $g=\operatorname{polylog}k$ while keeping all other parts of the grouping theorem untouched. In the source, the clique level $K$ controls both $g$ and the savings from recursive contraction; making $K$ only polylogarithmic can degrade the saving itself. The proof also has terms involving $gP/K$, not just the actual capacity $U$. Thus a "few groups with cheap joint factors" result requires a genuinely stronger, quantitatively analyzed grouping/contraction engine, not a one-line change of the integer $g$.

**Why the proposed strengthening would be powerful:** If a hypothetical engine permitted $g=o(\sqrt{\log k})$ and time $2^{O(U/\sqrt{\log k})}$ for arbitrary group-local weights and polynomially-queryable cover factors, then $U=O(gk\log q)$ would give $q^{o(k)}$ even for **dense** binary CSP. This would yield a major dense polynomial-alphabet CSP / multicolored Clique algorithm, so one should not describe the improved grouping theorem as easy or as already proved by the current preprint.

**Research next question:** Can one obtain a *nonuniform group-capacity recursion* charging $\sum_i P_i$ or actual $U$, rather than $g\max_iP_i$, while retaining a saving tied to total input $k$ and tolerating a small number of groups with large settings? This is a specific possible route; no validity or complexity guarantee is established.


**Strengthening (2026-11-02):** The limitation to a fixed partition in §1 has now been **removed**. [Note 39](39_adaptive_block_rank_barrier.md) proves w.h.p. *simultaneously for every (possibly adaptive and uneven) partition* whose maximum block size is at most $k^{1-\varepsilon}$ that $\sum_{i<j}\nu(G[A_i,A_j])\ge m-(35/12)k$. It uses uniform small-set sparsity and repeated-neighbor counting. All stated limitations on non-cover and globally shared algebraic representations remain.


**Source-level refinement (2026-11-02):** [Note 40](40_nguyen_grouping_overhead_and_random_csp_greedy.md) checks Nguyen's imported grouping formulas (17)-(18): with $g=3K^8$, the advertised upper-bound expression includes $2^{2gP/K}$ and the internal rate is only certified as $O(1/\sqrt{\log K})$. For fixed balanced groups on random critical graphs, $g=o(\sqrt{\log k})$ implies each pair has matching size at least half a group, hence the cover-interface row capacity $P=\Omega(k\log q)$ and $gP/K=\Omega(k\log q\cdot K^7)$. Thus naive group compression does not improve the **published bound**; this is not a lower bound on arbitrary implementations. The note also proves that dense random binary relation tables have a strong greedy extension property.
