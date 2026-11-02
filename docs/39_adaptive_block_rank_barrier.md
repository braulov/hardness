# Adaptive-partition no-go for vertex-cover block factorizations

**Date:** 2026-11-02. **Status: proved self-contained probabilistic/combinatorial lemma; architecture-specific.** This strengthens [note 38](38_multilevel_factorization_and_degree_uniformity.md): its fixed, input-oblivious partition is no longer required. It remains *not* a lower bound for arbitrary exact tensor networks or CSP algorithms.

## 1. Main theorem

Let $d=\sqrt{\log k}$, $p=d/k$, and $G\sim G(k,p)$. Fix a constant $\varepsilon\in(0,1)$. Then with probability $1-o(1)$, **simultaneously for every vertex partition** $V(G)=A_1\dot\cup\cdots\dot\cup A_g$ satisfying $\max_i|A_i|\le k^{1-\varepsilon}$ (arbitrary $g$, unequal sizes, graph-adaptive choices),

\[
\boxed{\sum_{i<j}\nu(G[A_i,A_j])\ge m-O(k)=(1-o(1))m,}
\tag{1}
\]
where $m=|E(G)|=(1+o(1))kd/2$ and $\nu$ is maximum matching size in the bipartite cross-block graph.

For example, the additive $O(k)$ term can be bounded by $(35/12)k$ using the constants below.

Since the [joint-rank lemma](37_joint_block_matching_rank_and_arity.md) says the **maximum over arbitrary relation tables** of the rational rank of the interaction matrix between $A_i$ and $A_j$ equals $q^{\nu(A_i,A_j)}$, this theorem says that an interface construction that transmits the minimum vertex-cover labels *for each pair* does NOT save a superconstant factor in bit wires, even with input-adaptive grouping. For every *fixed* partition one can simultaneously saturate every pair's rank by putting equality on a maximum matching in that pair and universal relations on all other edges. It does **not** follow that one common set of relation tables defeats *all adaptive partition-selection algorithms*, nor that arbitrary non-cover factorizations need this many wires.

## 2. Two high-probability graph properties

Fix $\delta\in(0,1)$ and the same $\varepsilon>0$.

(A) **Uniform induced small-set sparsity:** with high probability for *all* $S\subseteq V$ with $|S|\le k^{1-\varepsilon/2}$,
\[
|E(G[S])|\le (1+\delta)|S|.
\tag{2}
\]

Proof: for $s=|S|$, let $r=\lceil(1+\delta)s\rceil$. If $r>{s\choose2}$ the bad event is impossible. Otherwise a union bound gives
\[
\Pr[\exists S,\ |S|=s,\ e(S)\ge r]
\le {k\choose s}{{s\choose2}\choose r}p^r
\le \left[C_\delta d^{1+\delta}(s/k)^\delta\right]^s
\]
for all $s\le k^{1-\varepsilon/2}$ and large $k$ (use $sp\to0$ uniformly). The bracket is $\le k^{-\varepsilon\delta/2+o(1)}$, so summing over $s$ yields $o(1)$.

(B) **Maximum degree bound:** $\Delta(G)\le\log k$ with high probability, by binomial upper tails and a union bound, since the mean degree is $d=\sqrt{\log k}$.

All further claims hold deterministically on the joint event (A)+(B).

## 3. Strong uniform "few repeated neighbors" inequality

Take **any** set $B$ of size $s\le k^{1-\varepsilon}$. Let
\[
T_B=\{v\notin B:\deg(v,B)\ge2\},\quad r=|T_B|,\quad
D(B)=\sum_{v\notin B}(\deg(v,B)-1)_+.
\]
Because each member of $T_B$ has at least two neighbors in $B$ and $\Delta(G)\le\log k$,
\[
r\le s\log k/2,\quad |B\cup T_B|\le s(1+\log k/2)\le k^{1-\varepsilon/2}.
\]
The between-$B$-and-$T_B$ edge count equals $r+D(B)$, and it is at least $2r$. Applying (2) to $B\cup T_B$:
\[
2r\le r+D(B)\le(1+\delta)(s+r).
\]
Thus
\[
r\le\frac{1+\delta}{1-\delta}s,\qquad
D(B)\le (1+\delta)s+\delta r
\le\boxed{\frac{1+\delta}{1-\delta}s}.
\tag{3}
\]
This holds **simultaneously for every** eligible $B$, regardless of how it is selected.

## 4. Sum the losses over ANY partition

In a cross-block graph $G[A_i,A_j]$, delete at each endpoint all but at most one incident edge **to that other block**. The remaining graph is a matching. Number of deleted edges is bounded by
\[
\sum_{v\in A_i}(\deg(v,A_j)-1)_+
+\sum_{w\in A_j}(\deg(w,A_i)-1)_+.
\]
Summing this expression over all unordered pairs $i<j$ gives precisely $\sum_jD(A_j)\le\frac{1+\delta}{1-\delta}k$ by (3). Therefore
\[
\sum_{i<j}\nu(G[A_i,A_j])
\ge m_{\rm cross}-\frac{1+\delta}{1-\delta}k.
\]
For internal edges, (2) gives
\[
m_{\rm internal}=\sum_i|E(G[A_i])|\le(1+\delta)k.
\]
Together,
\[
\sum_{i<j}\nu(G[A_i,A_j])
\ge m-\left((1+\delta)+\frac{1+\delta}{1-\delta}\right)k.
\tag{4}
\]
With $\delta=1/4$ the penalty is $(5/4+5/3)k=(35/12)k$. Since $m=\Theta(k\sqrt{\log k})$, (1) follows.

## 5. Architectural consequence and non-consequence

1. **Adaptive refinement cannot rescue the obvious cover-factorization.** If all leaf blocks at a level have size at most $k^{1-\varepsilon}$ for some fixed $\varepsilon>0$, then their pairwise minimum-vertex-cover $q$-label budget is $(1-o(1))m$ labels. In particular Nguyen's published balanced grouping uses $g\gtrsim k^{1/40}$ and block size $O(k^{39/40})$, so the bound applies **even if one were allowed to choose balanced groups after looking at the input graph**.
2. To save a superconstant factor via this type of pairwise cover interfaces on these graphs, a partition must contain a block of size $k^{1-o(1)}$; otherwise (4) applies for some fixed $\varepsilon$. For a very large block, evaluating or representing all its internal CSP interactions is another computational challenge. E.g. the trivial one-block partition has zero cross-rank cost but leaves the original #CSP computation hidden inside its local weight.
3. This is a statement about graph-based cover-interface capacity and that *particular constructive factorization*. The rank of a specific binary interaction matrix may be lower, and clever algebraic mixing/cancellation, non-pairwise latent variables, nonuniform tensor recursions, or decision-only algorithms remain open.

**Research implication:** The actual algorithmic goal is not just adaptive grouping, but a qualitatively new cross-level/shared-latent representation that avoids separately transmitting cover labels for every fine block pair. This theorem gives a precise baseline any claimed improvement must beat.

## References / notes

- [Joint block matching rank lemma](37_joint_block_matching_rank_and_arity.md)
- [Earlier fixed-partition result and degree-uniformity target](38_multilevel_factorization_and_degree_uniformity.md)
- [Unconditional rank-dual enumeration and small-support raw bucket obstacle](36_rank_dual_critical_csp.md)
- [Critical-density HOM template](35_critical_density_csp_to_degen2_hom.md)
- [Nguyen 2611.00004v1](https://hexagonmath.org/2611.00004v1)
