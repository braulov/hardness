# CEH: reductions, probabilistic probe, and parameter audit

> **HARDNESS BRANCH CLOSED (conditional on the November 2026 CSP counting theorems).** The Nguyen preprint claims a deterministic $q^{O(k/\sqrt{\log k})}\operatorname{poly}(L)$ algorithm for every fixed-degree binary CSP; the full OpenAI Boolean tensor theorem separately implies the same for sparse polynomial-alphabet CSP. Thus the **SPACH, rSPACH, CEH and randomized-CEH no-$q^{o(k)}$ hypotheses are conditionally refuted**, and their hardness consequences must not be used. This document is retained for its reductions/structural questions; neither the claimed algorithms nor the Lean dependency chains have been independently audited here. See the [closure registry](../34_csp_hypothesis_closure_registry_2026_11_02.md), [Nguyen audit](../22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md), and [tensor analysis](../33_tensor_contraction_sparse_2csp_and_hardness_triage.md).


**Branch:** [README](README.md). **Date:** 2026-11-02. **Proven below** means directly checkable elementary argument as stated; literature-dependent or long unreviewed chat proofs are marked separately.

## 1. Exact problem

For every even $K$ (or a cofinal admissible sequence) fix **one** labeled, efficiently constructible simple bipartite cubic expander $F_K$. An input specifies arbitrary explicit binary relations $R_{uv}\subseteq[q]^2$ for its edges, $q=K^c$. Assignment $x_v\in[q]$, all relations must hold.

Its equivalent guise is **Partitioned / Colored Subgraph Isomorphism**: a graph with $K$ color classes $V_v=\{(v,a):a\in[q]\}$, and between $V_u,V_v$ the allowed edge relation $R_{uv}$ for each $uv\in E(F_K)$; select one vertex per color class realizing all edges of $F_K$. No injectivity issue because classes are disjoint.

$\mathrm{CEH}_c$: no uniform $q^{o(K)}\operatorname{poly}(|I|)$-time algorithm. Strong CEH: $\exists c>0:\mathrm{CEH}_c$. It implies corresponding polynomial-alphabet sparse-CSP hardness because of restriction of inputs; reverse implication requires a nontrivial many-one reduction. Do not replace the hypothesis with the weaker absence of $2^{O(K)}$.

### Warnings on quantifiers

- Distinguish $q=K^c$, $qle K^c$, and unrestricted polynomial $q$.
- Distinguish a *fixed* labeled family $F_K$ from arbitrary cubic expanders / expanders with dummy universal edges. An arbitrary sparse graph can be made expanding by overlaying a fixed expander, without changing semantic constraints; this does not solve the fixed-topology case.
- Distinguish randomized from deterministic hypotheses.
- A lower bound $q^{\Omega(K)}$ is shorthand; the actual hypothesis is *no* $q^{o(K)}$ uniform algorithm, not one universal positive lower exponent for every algorithm.

## 2. Why sparse 3-COL is not the target

3-COL on an arbitrary $N$-vertex graph, with $M$ edges, reduces to a width-3 CNF with $3N$ Boolean variables and $O(N+M)$ clauses. If the claimed October 2026 general fixed-width SAT speedup is correct, it covers even dense 3-COL. Conversely, polynomial-alphabet binary CSP encodes in CNF using $K\lceil\log_2 q\rceil$ bits, clauses of width $O(\log q)$, and $O(Kq^2)$ clauses; the fixed-width result is not automatically applicable at this width.

A local information-counting observation (model-specific): there are $2^{q^2}$ arbitrary binary relations on $[q]^2$, but at most $2^{O(B^3)}$ Boolean 3-CNFs on $B$ Boolean variables. Any universal relation-wise 3-CNF representation (even with existential auxiliary bits) would thus require $B=\Omega(q^{2/3})$ in general. This is not a global CSP reduction lower bound.

## 3. Target reductions with no loss in $K\log K$

### Independent Set

Vertices are ((v,a)), $v\in[K],a\in[q]$. Add every edge inside each class ${(v,a)}_a$, and add a cross-class conflict edge ((u,a)(v,b)) whenever $uv\in E(F_K)$ and $(a,b)\notin R_{uv}$. A size-$K$ independent set chooses one from each class and satisfies exactly the constraints. $N=Kq$, $O(Kq^2)$ edges.

### Set Cover / Hitting Set

Sets $S_{v,a}$. Universe: choice elements $u_v$, covered by all $S_{v,a}$; and for every forbidden pair $(a,b)\notin R_{uv}$, an element $e_{uv,a,b}$, covered by every $S_{u,a'}$ with $a'\ne a$ and every $S_{v,b'}$ with $b'\ne b$. At most $K$ sets cover iff a CSP witness exists. (Kq) sets and $O(Kq^2)$ universe elements. Hitting Set follows by dualization.

### Dominating Set

For each CSP variable $v$, create a $q$-clique $C_v$ of candidate vertices. Add $K+1$ false-twin guards adjacent only to $C_v$: a dominating set of size at most $K$ must choose at least one vertex from every $C_v$, hence exactly one from each and no guards. For each forbidden edge pair $(a,b)\notin R_{uv}$, put a separate guard adjacent to $C_u\setminus\{(u,a)\}$ and $C_v\setminus\{(v,b)\}$; it is not dominated precisely by the forbidden chosen pair. $O(Kq^2+K^2)$ vertices.

### Set Packing

From the IS conflict graph: one set per graph vertex. Each conflict edge contributes one universe element included in its two endpoint sets. A packing of $K$ pairwise disjoint sets is exactly an independent set of size $K$; element frequency is at most 2. Isolated graph vertices can be handled with unique private elements if needed.

### Graph Homomorphism

The previously constructed reduction from sparse binary CSP to HOM in the HOM preprint is claimed to give source size $n=\Theta(K)$, target size $h=O(Kq^2)$, degeneracy (le2). This quantitative claim should be re-checked against the exact statement and gadget definitions in §4 of https://arxiv.org/abs/2607.09377 before publication; no paper modification is made here. Under those parameters, a hypothetical $h^{o(n)}\operatorname{poly}(n,h)$ HOM algorithm with $h=\operatorname{poly}(n)$ would imply $q^{o(K)}\operatorname{poly}(|I|)$.

### Join nonemptiness / tensor networks

This is not a separate gadget: the conjunctive database query $\exists(x_v)_{v\in V(F_K)}\bigwedge_{uv\in E(F_K)}R_{uv}(x_u,x_v)$ is precisely CEH. Its Boolean-semiring tensor contraction has binary edge compatibility tensors and vertex equality tensors of degree 3. It is inappropriate to claim hardness for unrestricted arithmetic-semiring tensor contraction without checking the output semantics.

### No accidental ETH refutation

A general algorithm $2^{o(N)}$ in target input-vertex count $N=\operatorname{poly}(K)$ does not automatically imply $2^{o(K\log K)}$. For sparse $K$-Independent Set with $M\le CN$, Caro–Wei gives $\alpha(G)\ge N/(2C+1)$. If $N>(2C+1)K$, answer YES; otherwise brute force takes $2^{O_C(K)}$. Therefore a parameter-$O(K)$ reduction of CEH to a bounded-average-degree independent-set graph would refute CEH, not provide evidence of CEH hardness. Such a reduction has not been found.

## 4. Source-normalization constructions

### 4.1 Occurrence ports: one cycle + one arbitrary matching

Given binary CSP with $k$ variables and $m=O(k)$ constraints, create a port $p_{v,e}$ for each incident variable-edge pair: total $2m$ ports. Arrange ports of each original variable contiguously along a single cycle $C_{2m}$. On cycle arcs **within** a block enforce equality; on arcs crossing variable-block boundaries use the universal relation. The pairs $(p_{u,e},p_{v,e})$ of each original edge form a perfect matching $M$, where its edge carries original relation $R_e$. Ignore originally isolated variables (assuming domain nonempty), handle $m=0$ and tiny cases separately. The resulting CSP has the *same alphabet* and $K=2m=O(k)$ variables, at most 3 constraints per port. Two constraints can occupy the same port pair; take their intersection or work with a multigraph and then simplify.

The permutation matching is the **only** input-dependent topology. It is the natural input to the auxiliary exact-permutation-compiler program, but that program is not a necessary step toward a decision-preserving reduction.

### 4.2 Input-dependent cubic expander (port-cycle replacement)

Given a max-degree-3 constraint graph $J$ on $k$ variables, overlay a predetermined 3-regular expander $X$ with universal relations on its edges. Replace each original variable $v$ by a cycle of six or another constant number of equality-linked ports: up to three ports for $J$, up to three ports for $X$; fill remaining free ports by universal external pairings or modify the constant-size gadget to obtain 3-regularity. Every original and expander edge consumes one port at each endpoint, so the output graph is cubic, with $O(k)$ ports. All copies of each $v$ must have the same CSP value, and the added expander edges are tautological.

Expansion argument (skeleton, for a precise all-ports-present gadget): for $S$ at most half the ports, let $A$ consist of full six-port groups and $P$ of partially chosen groups. Every partially selected cycle gives at least two internal cut edges, so $h=|\partial S|\ge2|P|$. Expansion of $X$ supplies at least $\beta|A|-3|P|$ crossing edges among complete groups, hence $h\ge\beta|A|-3|P|$. As $|S|\le6(|A|+|P|)$, these imply positive uniform expansion. Check parity/padding and constant bounds in any formal write-up.

**Result:** no alphabet growth and $O(k)$ variables, but cubic expander topology **depends on $J$**.

### 4.3 One fixed higher-degree graph

Claim used in chat: the Alon–Capalbo optimal universal-graph construction gives an explicit graph $U_K$ with $O(K)$ vertices and $O(K^{4/3})$ edges into which every $K$-vertex degree-3 graph embeds with an efficiently computable map. Place actual CSP constraints on those edges, all other relations tautological; union with a predetermined expander to make the **fixed** graph expanding. This is a meaningful halfway house, **conditional on verifying the exact universal-graph theorem and algorithm**. The graph has nonconstant degree and superlinear edge count; don't call it fixed-*cubic*-expander CEH.

### 4.4 Logarithmic-loss minor embedding and the qualitative barrier

A minor model for arbitrary degree-3 sparse $J$ inside a predetermined bounded-degree expander of size $O(k\log k)$ would allow equality on connected branch sets and preserve the alphabet, but not $K=O(k)$. It is important to separate *existence* of minors from *polynomial-time discovery*. An elementary counting obstruction shows one constant-degree $O(k)$-vertex graph has only $2^{O(k)}$ minors / graphs obtained by labeled delete-contract operations, while there are $2^{\Theta(k\log k)}$ nonisomorphic cubic $k$-vertex graphs. The argument rules out all-minor universality, not nonlinear or satisfiability-only reductions.

A second research-literature claim discussed was that degree $K^{\varepsilon}$ may give linear-size universal minor containers for each fixed $\varepsilon>0$, whereas $K^{o(1)}$ degree cannot. Treat the exact theorem hypotheses, references, and algorithmic constructivity as **to be audited** rather than established here.

## 5. Random CSP on a fixed cubic expander

Take each potential ordered pair on each edge independently allowed with probability $p=q^{-2/3}$, and let $Z$ count satisfying assignments.

**Direct calculations:**

$$
\mathbb EZ=q^Kp^{3K/2}=1,
\qquad
\mathbb EZ_S=q^{|S|}p^{|E(F[S])|}=q^{|\partial_F S|/3}.
$$

Here $Z_S$ is the count of assignments to $S$ satisfying all constraints **fully inside $S$**; use $3|S|=2|E(F[S])|+|\partial_F S|$.

For two global assignments (x,y), let $S=\{v:x_v=y_v\}$; then

$$
\mathbb EZ^2
=\sum_{S\subseteq V(F_K)}(1-1/q)^{K-|S|}\,q^{-|\partial_F S|/3}.
$$

The chat argued that if $F_K$ has expansion at least $\beta>0$ and $q=K^c$ with $c>3/\beta$, then $\mathbb EZ^2\to2$ and, using higher moments encoded by partitions of a fixed number of assignments, $Z\Rightarrow\operatorname{Poisson}(1)$. The latter derivation was **not independently audited**; verify the moment accounting carefully before citing. It would imply limiting SAT/UNSAT probabilities $1-e^{-1}$ and $e^{-1}$, but **not** a decision lower bound. In this random model the typical degree of a row of an edge relation is about $q^{1/3}$; a spanning-tree extension search costs roughly $q^{K/3}$ up to subexponential factors, still not $q^{o(K)}$.

## 6. Research priorities

1. Uniformity/parameters check for the actual HOM reduction (subdivision, degeneracy, target encoding size).
2. Verify constructive universal-graph/minor theorems and whether the reported embeddings are polynomial-time.
3. Seek *decision-preserving* fixed-cubic-topology reduction with $O(k)$ variables and polynomial $q'$, using the two proven halfway-house constructions as anchors.
4. Explore a fixed-high-degree universal container followed by **batch existential** degree reduction that does not reintroduce $\Theta(k\log k)$ ports or a quasipolynomial domain.
5. Keep the exact matching-compiler branch separately as a sufficient but stronger problem.
