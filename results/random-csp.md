# Random CSP: exact moments, Poisson behavior, and a search gap

**PROVED**, using the classical cut-counting and dependency-graph Poisson theorems identified below. Two different random models occur here. Neither establishes computational hardness, and no novelty claim is made.

## A common overlap identity

On a fixed graph G=(V,E), |V|=k, choose every entry of every edge's q×q allowed-pair table independently with probability p. Write Z_F for the number of assignments satisfying an edge set F, μ_F=q^k p^{|F|}. Two assignments with exact agreement set S use the same random entry on precisely the edges of F induced by S. Counting such pairs gives

$$
\frac{\mathbb E Z_F^2}{\mu_F^2}
=\sum_{S\subseteq V}q^{-|S|}(1-q^{-1})^{k-|S|}p^{-e_F(S)}.
\tag{1}
$$

This formula, rather than presumed independence of assignments, is the basis of the results.

## Cubic critical model: a Poisson number of solutions

Assume G is simple, cubic, and 3-edge-connected, m=3k/2, and p=q^{-2/3}. Then EZ=1 for Z=Z_E. Set

$$
\Xi_G(q)=\sum_{\varnothing\ne S\subsetneq V}q^{-|\delta_G(S)|/3}.
$$

[Karger's cut-counting theorem, Theorem 4.7.6](https://people.csail.mit.edu/karger/Papers/thesis.pdf), bounds the number of cuts of size at most d by k^{2d/3}. Counting both shores,

$$
\Xi_G(q)\le2\sum_{d\ge3}(k^2/q)^{d/3}
=\frac{2k^2/q}{1-(k^2/q)^{1/3}},\quad q>k^2.
\tag{2}
$$

For each assignment σ let I_σ indicate satisfaction. Its dependency neighborhood consists of assignments agreeing with it on both endpoints of at least one edge. Outside that neighborhood all underlying table bits are disjoint, including from their joint collection. The dependency-graph Poisson parameters satisfy

$$
b_1\le m/q^2,\qquad b_2\le\Xi_G(q),
$$

using 2e(S)=3|S|−|δ(S)| and excluding σ=τ from b₂. The [Arratia–Goldstein–Gordon theorem, Theorem 1](https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/AGG-1.pdf) therefore gives

$$
d_{TV}(Z,\operatorname{Pois}(1))=O(k/q^2+k^2/q)=o(1)
\quad(q\gg k^2).
\tag{3}
$$

In particular P(UNSAT)→e^{-1}. Every value nevertheless has support on every incident edge with probability at least 1−2mq exp(−q^{1/3}), so arc consistency removes nothing with high probability for polynomial q.

## Deleting one table: concentration and conditional Poisson

For any proper **fixed** F⊊E, (1) gives

$$
\operatorname{Var}(Z_F)/\mu_F^2\le
\eta:=q^{-2/3}+\Xi_G(q).
\tag{4}
$$

For e=uv let N_e=Z_{E\setminus\{e\}}, so EN_e=q^{2/3}. Chebyshev and a union bound imply max_e|N_e/q^{2/3}−1|→0 in probability if kη→0.

Let Y_e count ordered distinct solutions of this deleted-edge instance that have the same endpoint pair at u,v. With disagreement set T⊆V\{u,v}, direct pair counting yields

$$
\mathbb EY_e=q^{2/3}\sum_{\varnothing\ne T\subseteq V\setminus\{u,v\}}
 (1-q^{-1})^{|T|}q^{-|\delta(T)|/3}
\le q^{2/3}\Xi_G(q)=O(k^2q^{-1/3}).
\tag{5}
$$

For q=⌈k^c⌉, c>9, a union bound gives Y_e=0 for all edges with high probability. Conditional on the other tables, the missing table consists of fresh Bernoulli bits. If Y_e=0, each near-solution queries a distinct such bit, hence **exactly**

$$
Z\mid R_{-e}\sim\operatorname{Bin}(N_e,p).
\tag{6}
$$

Together with concentration, this tends to Pois(1), uniformly over the edges on a high-probability event. Also, with high probability every N_e>Z, by Markov's bound on Z and (4). Thus every relation is logically essential, and the probability of an edge-minimally UNSAT, arc-consistent instance tends to e^{-1}.

### What an observer missing a table cannot learn

An expected conditional-TV error bound follows by combining (4)–(6) with the binomial Poisson approximation:

$$
\delta_k:=\max_e\mathbb E\,d_{TV}(\mathcal L(Z\mid R_{-e}),\operatorname{Pois}(1))
\le O(k^2q^{-1/3}+kq^{-1/2}+q^{-1/3}).
$$

Let U=[Z=0] and α=EU. For each e, E|E[U|R_{-e}]−α|≤2δ_k. Since the difference is bounded by one, its squared L₂ norm is also ≤2δ_k. In the orthogonal product-space (Hoeffding) decomposition U=α+Σ_{∅≠F⊆E}U_F, summing over omitted edges yields

$$
\sum_{\varnothing\ne F\subsetneq E}\|U_F\|_2^2\le2m\delta_k=o(1).
$$

Thus essentially all nonconstant variance is in the full-table component when c>9. The same bounds apply to adaptive algorithms that query **whole tables** and stop with at least one unread: partition transcripts by a deterministically chosen unread edge; on each part the transcript is measurable from the other tables. Summing the per-edge conditional error bounds gives O(mδ_k)=o(1). Such an observer cannot predict U better than its majority value, up to o(1). This is an access restriction, not a running-time lower bound for reading the full input.

## An easy family with the same statistics

Take the prism C_s□K₂, k=2s, s≥4. It is cubic and 3-edge-connected. An elementary proof of the latter: for a vertex cut shore, if either horizontal cycle is partially selected it contributes at least two cut edges; if exactly one is partial and the other is full or empty, a rung also crosses. If both are full/empty, any nontrivial choice separates the two cycles and cuts s rungs.

Write its columns (a_i,b_i). The bags

$$
\{a_0,b_0,a_i,b_i,a_{i+1},b_{i+1}\},\quad1\le i\le s-2
$$

form a path decomposition of width at most five. Every edge is covered and each vertex's bags are consecutive. Exact #CSP takes O(kq^6) arithmetic operations by DP. Yet (3)–(6), minimal UNSAT, and the full-table variance concentration all hold on these graphs.

**REFUTED interpretation:** those statistical properties alone imply computational difficulty. They also occur in this polynomial-time family. Expansion is relevant to excluding this particular DP, but still does not prove general hardness.

## Growing-degree model: existence versus efficient search

Now change models: d=√ln k, G∼G(k,d/k), q=⌈k^c⌉, and relation density ρ=q^{-γ/d}, with fixed γ>0. For fixed c>1, γ<2 implies SAT with high probability; γ>2 implies UNSAT with high probability. For γ<1 and any fixed c>0 there is a polynomial-time greedy search algorithm succeeding with high probability. No polynomial search theorem is established here for 1≤γ<2.

Here are the details of the existence claim. For any small fixed η>0 choose α>0 sufficiently small. With high probability, simultaneously for all S,

$$
e_G(S)\le
\begin{cases}
\eta d|S|,&|S|\le\alpha k,\\
(1+\eta)d|S|^2/(2k),&|S|\ge\alpha k.
\end{cases}
\tag{7}
$$

For small sets, the union bound with t=⌈ηds⌉ is at most [(ek/s)(es/(2ηk))^{ηd}]^s (impossible events t>binom(s,2) contribute zero). Choose α<η/e; the bracket is uniformly exp(−Ω(d)), and the sum tends to zero. For large sets a Chernoff tail exp(−Ω_η(α²kd)) dominates the 2^k choices.

Choose η with c(1−γη)>1 and δ=1−γ(1+η)/2>0. In (1), conditional on a graph satisfying (7), nonempty small overlaps contribute at most (1+q^{-(1−γη)})^k−1=o(1); large overlaps contribute at most 2^k q^{-δαk}=o(1). The empty overlap is (1−1/q)^k=1−o(1). Hence EZ²/(EZ)²=1+o(1) and SAT holds with high probability. For γ>2, m=(1+o(1))kd/2 makes EZ=q^{k−γm/d}=o(1); use Markov on typical graphs and add their exceptional probability. This proves only a fixed-gap transition, not a critical-window theorem.

For γ<1, (7) gives a degeneracy order with at most D=(1+ζ)d earlier neighbors, where ζ>0 is chosen with γ(1+ζ)<1. Each fixed assignment of these neighbors lacks an extension with probability at most exp(−qρ^D)=exp(−k^{Ω(1)}). Union bound over kq^D choices is o(1). Thus all greedy steps succeed. More modestly for c>1, γ<2, restricting each alphabet to the first q^β labels with max(γ/2,1/c)<β<1 preserves the SAT-with-high-probability theorem and gives q^{(β+o(1))k} distributional search by enumeration. This is not q^{o(k)}.

## Quiet planting and the correct recovery quantifier

Condition on a graph G and let P be the independent-table law. Plant a uniform assignment by forcing its required entries. The resulting instance law Q has likelihood ratio Z/μ_G, μ_G=q^kρ^m. Therefore TV(P,Q)≤½√(Var Z/μ_G²). The preceding second moment proves TV=o(1) for the growing-degree model with c>1, γ<2, after averaging over G. Any algorithm finding **some** solution under one law transfers to the other, with o(1) change in success probability.

Given the instance, the planted assignment is uniform among its Z solutions. The optimal probability of recovering that particular hidden assignment, **conditional on G**, is exactly

$$
\mathbb P_P(Z>0\mid G)/\mu_G\le1/\mu_G.
$$

On typical G this is q^{-(1−γ/2+o(1))k}. The same exponential bound **has not been established unconditionally over G**: exceptional graphs must be charged, and an o(1) exceptional probability need not have that exponential rate. What follows without additional tail analysis is unconditional recovery probability o(1). Finding any solution remains a different task.

Provenance: original notes 35–37 and 44–48. The cut-count bound was checked in Karger's thesis and the Poisson theorem is a standard external ingredient; no external recent SAT algorithm is used. Finite identity/decomposition checks are in `experiments/47_endpoint_collision_formula_sanity.py` and `48_prism_cutcount_and_pathwidth_sanity.py`. Random-CSP priority against the existing growing-domain literature remains unverified.
