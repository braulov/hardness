# Joint factorization across CSP blocks: exact matching-number characterization

**Date:** 2026-11-02. **Status:** elementary exact lemma PROVED; a quantitative **architectural** tension for block factorization is derived. This does NOT give an arbitrary critical-density CSP algorithm and does NOT rule out general algebraic tensor-network compression.

## 1. Setup and why individual relation ranks are insufficient

Let a binary CSP have $k$ variables, $m=\Theta(k\sqrt{\log k})$ constraints, and domain $[q]$ with $q=k^c$, fixed $c>0$. For disjoint vertex blocks $A,B$ let $E(A,B)$ be the crossing constraints and define the joint binary interaction matrix

\[
\Phi_{A,B}(x_A,x_B)=\prod_{uv\in E(A,B)}R_{uv}(x_u,x_v),
\quad x_A\in[q]^A,\ x_B\in[q]^B.
\]

Its factor rank may be FAR SMALLER than the product of the individual ranks of $R_e$, because all relations between $A$ and $B$ share endpoint variables.

## 2. Exact universal worst-case rank is governed by maximum matching

**Lemma.** Let $\nu(A,B)$ be the maximum matching size of the bipartite cross-edge graph $(A,B,E(A,B))$. Then for arbitrary binary relation tables:

\[
\operatorname{rank}_{\mathbb Q}\Phi_{A,B}\le q^{\nu(A,B)},
\quad\text{and}\quad
\max_{\{R_e\}}\operatorname{rank}_{\mathbb Q}\Phi_{A,B}=q^{\nu(A,B)}.
\tag{1}
\]

**Proof of upper bound.** By König's theorem take a vertex cover $C\subseteq A\cup B$ of the crossing graph, with $|C|=\nu(A,B)$. Introduce a message $z\in[q]^C$. Put a Kronecker delta $[x_v=z_v]$ on the respective side for each covered vertex. Because each crossing edge meets $C$, allocate its relation factor to the side whose *other* endpoint is read directly, using the covered endpoint's $z$-value. This yields an explicit factorization

\[
\Phi_{A,B}(x_A,x_B)=\sum_{z\in[q]^C}
f_A(x_A,z)f_B(x_B,z).
\tag{2}
\]

Both factor entries are computable in $O(|A|+|B|+|E(A,B)|)$ ordinary table operations, after a polynomial-time maximum matching and vertex cover computation. Thus the matrix rank is at most $q^{|C|}$.

**Proof of tightness.** On a maximum matching put equality relations $[a=b]$; on all other cross edges put the universal $1$ relation. Up to duplicate rows/columns, $\Phi$ is a tensor product of $\nu$ identity matrices, with rank exactly $q^\nu$. All these are legitimate Boolean relation tables. This is an elementary statement about **worst-case joint flattening rank**, not a claim that random Boolean relations always reach it.

Consequently the optimal *worst-case logarithmic bond capacity* of one joint block-to-block matrix factorization is exactly $\nu(A,B)\log_2q$ bits. This is the correct graph invariant to track when choosing block partitions; it is more informative than the sum of edge ranks.

## 3. Why this appears to offer a large win

Partition $k$ vertices into $g$ balanced groups of size $s=k/g$. On a typical graph with average degree $d=\sqrt{\log k}$, a group pair carries about

\[
|E(A_i,A_j)|\approx s\,d/g
\]

edges, but the joint block matrix has rank at most $q^s$. When $g=o(d)$, its potential interface budget is $s\log q$, a factor about $d/g$ less than the raw per-edge $|E(A_i,A_j)|\log q$. Summing over $O(g^2)$ pairs suggests only

\[
M_{\rm block}=O(gk\log q)
\tag{3}
\]

bit wires, versus $M_{\rm standard}=\Theta(kd\log q)$.

For example $g=(\log k)^{1/4}$ would formally suggest $M_{\rm block}=O(k(\log k)^{5/4})=o(k(\log k)^{3/2})$. **This is only a formal bond count, not yet a valid tensor instance under the external theorem.**

## 4. The local-arity obstruction to naive large blocks

A direct pair-factor tensor computing either $f_A(x_A,z)$ or $f_B(x_B,z)$ from complete assignments on a group has at least $\Theta(s\log q)$ input bits if it reads the entire group value. The claimed full Boolean tensor-contraction theorem [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md) requires maximum local degree at most $S^{9/10}$, where $S$ is the scale parameter controlling the speed $2^{O(S/\sqrt{\log S})}$.

In the **one-layer full-block architecture** with $g$ groups, $s=k/g$, total intended wire budget $S=O(gk\log q)$ and at least one pair tensor reading a complete group assignment, compatibility demands

\[
\frac{k\log q}{g}\lesssim (gk\log q)^{9/10}
\quad\Longrightarrow\quad
g\gtrsim (k\log q)^{1/19}.
\tag{4}
\]

For critical-density graphs, $d=\sqrt{\log k}$, so $g=o(d)$ (needed for a superconstant-factor bond saving) is incompatible with (4). Padding $S$ to permit a huge local tensor forces at least $S\gtrsim((k\log q)/g)^{10/9}$, making the fast-contraction bound far worse than $2^{o(k\log k)}$ in the polylogarithmic-$g$ regime.

This is a valid obstruction **only** when one local factor directly reads all $s$ variable labels (or equivalently has degree $\Omega(s\log q)$). Clever staged representations may evade this; an expensive high-degree factor cannot simply be relabeled a polynomial-time oracle and ignored.

Splitting the factor into its constituent edge tests typically reintroduces $\Theta(m\log q)$ wires. The [small-support bucket obstruction](36_rank_dual_critical_csp.md) proves that a raw-copy implementation using buckets on at most $k^{1-\epsilon}$ variables cannot gain a superconstant factor on certain random critical-density graphs.

## 5. The actual open technical question

Can one obtain BOTH:
- a **joint block-interface compression** exploiting shared input variables across many independent full-rank constraints (as in (1) and (2)); and
- a *low-arity realization* of those block-factor functions with polynomial-time local entries and total **$o(m\log q)$** wires,

without reproducing the original per-edge constraint incidence network?

This requires more than edgewise rank reduction or grouping complete source assignments into a single huge tensor. The matching-number lemma supplies an exact lower/upper target for each block interaction. Any claimed compiler must account separately for (i) cross-block bond bits, (ii) internal factor decomposition, (iii) precision and tensor ring, (iv) maximum arity, and (v) degree/network-count overhead.

**Related literature:** standard matrix flattening, König's vertex cover theorem, Holant/holographic factorization; see e.g. connection tensor work https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/perfect-matchings-rank-of-connection-tensors-and-graph-homomorphisms/46898FD6A40484251A432661320116F4 .

**No algorithm or new hardness theorem is claimed for unrestricted critical-density CSP.**
