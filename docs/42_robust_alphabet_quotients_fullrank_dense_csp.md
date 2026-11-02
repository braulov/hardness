# Decision-only robust alphabet quotients: full-rank dense relations can hide a tiny CSP

**Date:** 2026-11-02. **Status:** elementary exact SAT-iff quotient lemma, unconditional deterministic algorithm on certified inputs, and a polynomial-time recovery algorithm for a specific *hidden-block / Hamming-separated* family. This is a positive structurally restricted result, **not** a universal $q^{o(k)}$ algorithm for critical-density binary CSP, and novelty relative to the wider CSP literature is not established. It is deliberately different from rational-rank factorization or sparse-partner branching in [note 36](36_rank_dual_critical_csp.md).

## 1. Robust quotient / greedy-lifting lemma

Let $\Gamma=(V,E,[q],\{R_e\})$ be an explicit binary CSP, with $|V|=k$ and $m=|E|$. For every vertex $v$ suppose we are supplied a nonempty partition
\[
[q]=C_{v,1}\dot\cup\cdots\dot\cup C_{v,r_v}.
\]
For each $e=uv$, let $S_e\subseteq[r_u]\times[r_v]$ be a *coarse* binary relation. Require:

1. **No false fine pairs:** if $(i,j)\notin S_e$, the entire rectangle $C_{u,i}\times C_{v,j}$ is forbidden by $R_e$.
2. **Per-endpoint bounded defects:** if $(i,j)\in S_e$, for every fixed $a\in C_{u,i}$ at most $b_{e,v}$ values $b\in C_{v,j}$ are forbidden, and for every fixed $b\in C_{v,j}$ at most $b_{e,u}$ values $a\in C_{u,i}$ are forbidden. The nonnegative integers $b_{e,v}$ are independent of the chosen allowed coarse pair.
3. **Local spare capacity:** for every $v$ and every class $C_{v,i}$,
\[
|C_{v,i}|>\sum_{e\ni v}b_{e,v}.
\tag{1}
\]

**Lemma.** Under these hypotheses,
\[
\Gamma\in\mathrm{SAT}\quad\Longleftrightarrow\quad\Gamma_{\rm coarse}\in\mathrm{SAT}.
\tag{2}
\]
Every coarse satisfying assignment can be greedily lifted to a fine satisfying assignment in arbitrary vertex order.

**Proof.** A fine satisfying assignment projects to an allowed coarse pair on each edge by (1). Conversely, fix a coarse satisfying assignment. At the moment vertex $v$ is visited, each previously assigned neighbor forbids at most $b_{e,v}$ candidates in the fixed chosen class $C_{v,i}$. By (1), at least one fine candidate remains. Choose it, preserve all previously checked edges, and continue. QED.

All conditions, including the *worst-case* endpoint defect counts in every permitted rectangle, can be certified in $\operatorname{poly}(L,k,q)$ time from explicit relations and partitions. Hence **given a certifying partition**, exact SAT is decided in
\[
\operatorname{poly}(L)\prod_{v\in V}r_v\le \operatorname{poly}(L)\,r^k,\quad r=\max_vr_v.
\tag{3}
\]
For $q=k^c$ and $r=k^{o(1)}$ this is $q^{o(k)}$; for constant $r$, this is $2^{O(k)}$.

**Counting is NOT preserved:** the number of fine lifts of different coarse assignments can vary. This is fundamentally a **decision-only** quotient method. It is not a low-rank factorization of $R_e$ over the rationals.

## 2. An adversarial fully ranked dense-table construction

Fix an integer $r\ge2$, a fine alphabet size $L\ge2$, and $q=rL$. Let each vertex $v$ secretly identify its q values with pairs $(c,t)\in[r]\times[L]$ using an arbitrary vertex-specific bijection $\psi_v$ (independent value permutation). On every edge $e=uv$, choose any **invertible zero-one** coarse matrix $S_e\in\{0,1\}^{r\times r}$ and let
\[
R_e((c,t),(d,s))=S_e(c,d)\,[t\ne s].
\tag{4}
\]
The actual input gives the relation table after applying $\psi_u,\psi_v$; the algorithm need not know those bijections.

Ignoring row/column permutations, the matrix is the Kronecker product
\[
R_e=S_e\otimes(J_L-I_L).
\]
For $L\ge2$, the matrix $J_L-I_L$ is invertible over $\mathbb Q$ (eigenvalues $L-1$ and $-1$), so
\[
\boxed{\operatorname{rank}_{\mathbb Q}R_e=rL=q.}
\tag{5}
\]
Thus **every edge relation can have full rational rank**, defeating the rank-dual enumeration [note 36].

In the especially transparent case $S_e=J_r-I_r$ for all edges, with $r\ge2$, all relations are full rank, and each row and column has exactly
\[
(r-1)(L-1)=\Theta(q)
\tag{6}
\]
allowed partners. Consequently the sparse-partner spanning-tree algorithm of note 36 also gives no sub-$q^k$ guarantee. The quotient CSP is precisely ordinary graph r-COLORING on the same primal graph. For r=3 and arbitrary graphs this can encode genuinely nontrivial decision instances, not merely an everywhere-SAT triviality.

**Lifting:** Each fine value on a neighbor forbids exactly ONE fine label within the selected permitted coarse class. Thus $b_{e,v}=1$ and condition (1) holds whenever $L>\Delta(G)$. Any satisfying coarse coloring extends to a fine assignment by a greedy proper L-coloring of the fine coordinates.

For $r=O(1)$ and $L>\Delta$, this gives an unconditional $r^k\operatorname{poly}(L_{\rm input})$ SAT algorithm, despite full-rank, dense allowed-pair tables.

## 3. Recover the hidden coarse alphabet in polynomial time

There is no need to **supply** the hidden bijections $\psi_v$ if the coarse matrices $S_e$ have pairwise distinct rows and pairwise distinct columns (invertibility suffices). In particular this holds for $S_e=J_r-I_r$.

For any non-isolated $v$, define the **incident-row Hamming distance** between two fine values $a,a'$ at v by
\[
D_v(a,a')=\sum_{e=vw\in E}
\#\{b\in[q]:R_e(a,b)\ne R_e(a',b)\},
\tag{7}
\]
orienting each incident matrix to treat v as its row-side (transpose if needed).

If $a,a'$ lie in the SAME hidden coarse class, then on an edge e their rows differ only at two fine-label positions for each allowed opposite coarse class. Therefore
\[
D_v(a,a')\le2r\deg(v).
\tag{8}
\]

If $a,a'$ lie in DIFFERENT hidden coarse classes, then every incident $S_e$ has distinct rows for the two classes. On at least one opposite coarse class, one row is identically zero and the other has $L-1$ ones. Hence for any non-isolated v,
\[
D_v(a,a')\ge L-1.
\tag{9}
\]

If
\[
\boxed{L-1>2r\Delta(G),}
\tag{10}
\]
then the threshold test $D_v(a,a')\le2r\deg(v)$ **exactly recovers hidden coarse-class equivalence** at every non-isolated vertex. Isolated vertices can simply be discarded or given one unrestricted coarse value.

The distances and equivalence classes are computable in $O(mq^3)$ time directly from explicit input relation tables. Recover all partitions, define $S_e$ by whether a class rectangle contains any permitted pair, then independently verify all robustness requirements of §1. Once verified, solve the coarse CSP and greedily lift any solution. Verification makes the procedure *sound even if a non-promised input accidentally passes the clustering heuristic*.

If r is not supplied, enumerate candidate divisors $r\le r_{\max}$ of q (or all $r\le r_{\max}$) and attempt recovery + certification; this incurs only polynomial overhead in q. Choose a successful certified quotient with smallest r. If none passes, fall back to a general correct CSP solver. On the promised hidden-block family with $r\le r_{\max}$ and (10), the special algorithm runs in
\[
O(mq^3)+r^k\operatorname{poly}(L_{\rm input}).
\tag{11}
\]
For r=k^{o(1)}, this is $q^{o(k)}\operatorname{poly}(L_{\rm input})$.

This is an **algorithmic extraction of a common latent code across all edges incident to a variable**. Individual relation rank remains q. It exploits robust satisfiability-preserving quotient structure rather than exact tensor value preservation.

## 4. Interpretation and limitations

- Positive: full-rank, $\Theta(q)$-dense binary relation matrices can still admit efficiently recognizable **shared low-alphabet structure** with a strong $r^k$ decision algorithm.
- It strictly goes beyond the *sufficient* rank and sparse-neighbor criteria already derived in note 36, but **does not** imply that general full-rank dense relations are tractable.
- For r=3, the quotient is 3-COLORING, so no claim of polynomial-time algorithm is made; the unconditional $3^k$ bound is enough to be $q^{o(k)}$ when q=k^c.
- This decision quotient does NOT supply a small exact tensor network computing #SAT. Thus it does not directly remove Nguyen's grouping-overhead term for arbitrary counting instances. It does suggest a different priority: detect shared *robust latent labels* and solve the quotient before applying exact tensor counting to the residual hard core.
- General arbitrary relations may have no such near-rectangular quotient, or discovering a good quotient may be computationally hard outside the Hamming-separated promise. Neither a universal extraction theorem nor a critical-density $q^{o(k)}$ algorithm is established.

**Next research question:** Can robust quotient decomposition be combined with a weaker invariant than simple Hamming clustering (e.g. simultaneous approximate block decompositions or multiway neighborhood signatures), while retaining deterministic polynomial-time recognition and a certificate of greedy lifting? This would enlarge the class beyond the explicit Kronecker family without falsely advertising a universal improvement.

## References / related project notes

- [Critical-density CSP hardness candidate / HOM transfer](35_critical_density_csp_to_degen2_hom.md).
- [Rank-dual and sparse-partner algorithms](36_rank_dual_critical_csp.md).
- [Joint-block matrix rank](37_joint_block_matching_rank_and_arity.md).
- [Source-level grouping and black-box obstacles](41_uniform_coarse_partitions_and_row_sensitive_grouping.md).


## 5. Stronger recovery theorem: adversarially deleted entries, not just Kronecker matrices

The exact $S\otimes(J-I)$ form is unnecessary for hidden-label recovery.

Assume every hidden coarse class has the same size $L$, with $q=rL$. There is a **hidden** partition for each vertex and coarse tables $S_e$ such that:
- for every *forbidden* coarse pair, the associated $L\times L$ rectangle is identically zero;
- for every *allowed* coarse pair, each row and each column of the $L\times L$ rectangle contains **at most $t$ zero entries**, where $t\ge1$ may grow;
- **joint row/column separation:** for any non-isolated vertex v and two distinct coarse classes c,c', *some incident edge e* has an opposite coarse class d such that the two coarse rows (or columns, if v is the second endpoint) disagree at d.

The first two promises imply the robust quotient conditions with $b_{e,v}=t$. Thus, if $\Delta t<L$, exact decision projects to the coarse problem.

**Recovery theorem.** If
\[
\boxed{L-t>2rt\,\Delta(G),}
\tag{12}
\]
then the **same Hamming signature method** of §3 recovers every hidden coarse partition of a non-isolated vertex in polynomial time.

**Proof.** For two fine values of the same coarse class, the rows on any one edge differ only inside at most r allowed coarse rectangles; within each permitted rectangle, each row contains at most t zeros, so their Hamming distance is at most $2rt$. Summing over incident edges gives $D_v(a,a')\le2rt\deg(v)$. For different coarse classes, the separation promise supplies some edge and some opposite coarse class on which one row is identically zero while the other has at least $L-t$ ones; hence $D_v(a,a')\ge L-t$. Inequality (12) separates the two cases. Therefore the threshold test $D_v\le2rt\deg(v)$ is exactly hidden-class equivalence. QED.

The algorithm computes all distances, clusters with the given $(r,t)$ threshold, constructs coarse relations, then **independently verifies** all forbidden-rectangle/allowed-row-and-column requirements and the greedy-lifting inequality. So its correctness on *every* input does not depend on trusting the promise. If $(r,t)$ are not supplied, one may enumerate polynomially many guesses up to stated polynomial caps, check them, and use the cheapest successful certificate.

This is a robust **adversarial-deletion** generalization of the special full-rank Kronecker family; the allowed rectangles may have arbitrary missing entries, provided defects are bounded per row and column. Note that such arbitrary deletions do not guarantee full rational rank; equation (5) establishes full rank for the explicit Kronecker subclass.

This supplies an actual **multi-edge latent-label extraction** algorithm, not simply an existential encoding or a small interface rank bound. Its limitation is intrinsic: fully general constraint tables need not admit any sufficiently coarse robust quotient.
