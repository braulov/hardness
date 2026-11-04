# Restricted local-search obstacles in random CSP

These are **PROVED for their specified random models**. They do not rule out unrestricted sampling, algorithms using all cross constraints, or paths through infeasible assignments. Statistical global dependence alone has an [easy prism counterexample](../results/random-csp.md#an-easy-family-with-the-same-statistics).

## Freezing a side without consulting the crossing tables

In the growing-degree model G∼G(k,d/k), d=√ln k, q=k^c, ρ=q^{-γ/d}, fix a vertex subset W of size ⌊ak⌋ independently of G, where a∈(0,1). An algorithm may inspect G and all W-internal tables to choose x_W, but no crossing table. For every fixed c,γ>0, with high probability this assignment has no extension even satisfying just the crossing constraints.

Indeed, for a fixed δ>0 put t*=ceil((1+δ)d/γ). The cross-degrees of vertices outside W are independent Bin(|W|,d/k). A lower bound on the mass at t* is exp(−O(d)), so with high probability at least k^{1−o(1)} vertices have cross-degree ≥t*. Conditional on G,x_W, each such vertex has at least one compatible value with probability at most qρ^{t*}≤q^{-δ}. Their crossing tables are disjoint. The probability that all have a value is at most q^{-δ k^{1−o(1)}}.

This can happen despite an exponentially large expected number of extensions. If the selected assignment satisfies the W-internal constraints, then, conditional on typical G and those internal tables, its expected number of full extensions is

$$
q^{((1-a)(1-\gamma(1+a)/2)+o(1))k},
$$

which grows when γ<2 and a is sufficiently small. Rare favorable tables dominate the expectation. This argument does not cover a graph-adaptive cut W or an assignment chosen after reading crossing tables.

## Most deleted-edge solutions admit no feasible half-variable move

Let G be a fixed simple cubic γ-expander of girth at least a ln k. Use the critical independent-table model p=q^{-2/3}, q=⌈k^c⌉ with c>max(9,9/γ). For every edge e, let S_e be the solution set after deleting e. With high probability, simultaneously for all e,

$$
|S_e|=(1+o(1))q^{2/3},
\quad
|\{\sigma\in S_e:\exists\tau\ne\sigma\text{ in }S_e,
                      d_H(\sigma,\tau)\le k/2\}|=o(q^{2/3}).
\tag{1}
$$

Here is the pair bound. Let C_e count ordered distinct pairs at distance at most k/2, with disagreement set T. The number of edges of G−e incident with T is (3|T|+|δ(T)|)/2−[e∩T≠∅]. Hence

$$
\mathbb EC_e=q^{2/3}\sum_{1\le|T|\le k/2}
(1-q^{-1})^{|T|}q^{-|\delta(T)|/3+(2/3)[e\cap T\ne\varnothing]}.
\tag{2}
$$

If |T| is below the girth, its induced graph is a forest. Each connected component U contributes weight q^{-(|U|+2)/3}. At most 9^s connected sets of size s contain a fixed vertex, so the total component weight is O(k/q), and the total touching an endpoint of e is O(1/q). Dropping disjointness/nonadjacency restrictions and expanding exp(sum of weights) bounds the small-set contribution in (2) by O(kq^{-1/3}+q^{1/3}).

For larger T, expansion gives |δ(T)|≥γ|T|. With r=kq^{-γ/3}, their contribution is at most q^{4/3}e^r r^{girth}/girth!=k^{-ω(1)}. Therefore

$$
\frac{\mathbb E\sum_e C_e}{q^{2/3}}
=O(kq^{-1/3}+k^2/q)+o(1)=o(1).
$$

Markov bounds all bad solutions simultaneously. Concentration of |S_e| follows from the overlap identity and expansion: the normalized variance is at most q^{-2/3}+2[(1+q^{-γ/3})^k−1], and a union bound over edges applies at the stated c. This proves (1) without needing a 3-edge-connectivity assumption.

A chain whose states are S_e and whose moves alter at most k/2 labels has absorbing singleton states at almost all solutions. It cannot be irreducible. This blocks the specific plan of finding one near-solution and enumerating the others by feasible block moves. Global jumps, infeasible intermediate states, and direct global enumeration remain open.

Provenance: notes 45 and 51. Finite verification of (2): `py experiments/51_nearsolution_close_pair_formula_sanity.py`. The asymptotic argument, not that finite test, supplies the proof.
