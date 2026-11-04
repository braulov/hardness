# Structural costs of grouping and deleting constraints

These are **PROVED limitations of specified representations**, not general CSP time lower bounds.

## One block interaction: matching number gives the exact worst-case rank

For disjoint variable blocks A,B, form

$$
\Phi(x_A,x_B)=\prod_{uv\in E(A,B)}R_{uv}(x_u,x_v).
$$

Its rank over any field is at most q^{ν(A,B)}, and this is the maximum over Boolean relation tables. By König's theorem choose a crossing vertex cover C of size ν. Sum over labels z∈[q]^C, enforcing their equality with endpoint labels on the appropriate side; allocate each relation to the side that knows its noncovered endpoint. This expresses Φ as a sum of q^{|C|} rank-one products. For tightness, put equality constraints on a maximum matching and universal relations on other edges; the matrix contains a tensor product of ν identity matrices.

The quantifier is **for each partition there exist tables** attaining the bound. It is not a single set of tables proven to defeat all relation-adaptive partitions. Equality constraints themselves are easy to solve.

## Even graph-adaptive small blocks do not save cover labels

Let G∼G(k,d/k), d=√ln k, and fix ε∈(0,1). With high probability every partition into blocks of size at most k^{1−ε} satisfies

$$
\sum_{i<j}\nu(G[A_i,A_j])\ge |E(G)|-O(k).
\tag{1}
$$

Here is a uniform proof. For fixed δ∈(0,1), with high probability every S of size at most k^{1−ε/2} has e(S)≤(1+δ)|S|. The union bound for s vertices and ceil((1+δ)s) edges is at most [C_δ d^{1+δ}(s/k)^δ]^s; summing gives o(1). Also Δ(G)≤ln k with high probability by binomial tails.

For any eligible block B, let T_B be outside vertices with at least two neighbors in B, r=|T_B|, and D(B)=Σ_{v∉B}(deg(v,B)−1)_+. Then |B∪T_B|≤|B|(1+ln k/2)≤k^{1−ε/2}. Its induced edge count is at least r+D(B)≥2r. Small-set sparsity gives

$$
r+D(B)\le(1+\delta)(|B|+r),
\quad D(B)\le\frac{1+\delta}{1-\delta}|B|.
$$

In each block pair, remove excess incident edges until a matching remains. Summed over pairs, removals cost at most Σ_i D(A_i); internal edges cost at most (1+δ)k. Thus (1) holds with penalty [(1+δ)+(1+δ)/(1−δ)]k, e.g. 35k/12 for δ=1/4.

This rules out superconstant savings in the **sum of separate vertex-cover interfaces** for small blocks. It does not prove equally high ranks for the specific input tables, nor exclude higher-order shared variables, cancellation, or decision quotients.

## Large blocks must pay for local computation

For g balanced blocks, a naive pair tensor reading a whole block has Ω(k log q/g) Boolean ports. A proposed total wire scale S=O(gk log q), together with the [external theorem's](../directions/csp-hom.md#external-algorithm-status) local-degree requirement S^{9/10}, forces

$$
g=\Omega((k\log q)^{1/19}).
$$

Thus polylogarithmically many large full-assignment tensors do not meet that theorem's hypotheses at the advertised wire budget. Padding to satisfy the degree bound also increases the running-time parameter. This is a restriction of that application, not an intrinsic impossibility theorem for every tensor contraction method.

## Deleting constraints cannot cheaply remove expander treewidth

Let a k-vertex graph have maximum degree Δ and edge expansion γ: |δ(S)|≥γ min(|S|,k−|S|). For **every** t-edge deletion set D, including adaptively selected sets,

$$
t+\Delta(\operatorname{tw}(G-D)+1)\ge\gamma k/4.
\tag{2}
$$

Take a balanced separator bag X of a tree decomposition of G−D. If |X|≥k/4 the bound is immediate. Otherwise a union A of components outside X has k/4≤|A|≤k/2: choose a component in this range or accumulate smaller ones. All retained edges leaving A end in X, so γk/4≤|δ_G(A)|≤t+Δ|X|. This proves (2).

In the cubic critical random model, for a **table-independent** deletion set D of size t, EZ_{−D}=q^{2t/3}. Thus deleting O(1) constraints leaves only polynomially many expected solutions but still linear treewidth; reducing treewidth to o(k) requires deleting Ω(k) edges. This is a parameter tradeoff. A standard q^{w+1} DP bound is an upper bound, not a lower bound on every solver. The expectation cannot be applied without qualification to a deletion set chosen using relation contents.

**Ways around these barriers:** exploit relation-specific structure, compress only the decision question, use a global enumeration method not based on small treewidth, or prove a new contraction theorem with the required local-cost guarantees. No general conjectured barrier beyond these models is established by their combination.

Provenance: notes 37 (joint matching rank), 39 (adaptive partitions), and 49 (treewidth deletion) in the [original tree](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs).
