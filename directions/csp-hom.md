# Sparse CSP and the single-exponential HOM question

**OPEN.** For each fixed c,a, does every explicit binary CSP with v variables, q≤v^c labels and m≤av constraints admit a deterministic or bounded-error randomized 2^{O_{c,a}(v)}poly(L) decision algorithm? Treat the two algorithm models separately. By the [proved reduction](../results/csp-hom.md), this is equivalent to the corresponding family of single-exponential HOM algorithms on polynomial-size 2-degenerate targets and sparse 2-degenerate sources.

This is the clearest central problem left by the notebook. The reduction is available; the unresolved step is the CSP algorithm or an independent hardness source.

## External algorithm status

Primary sources checked on 2026-11-04:

* [OpenAI's general Boolean tensor-contraction statement](https://raw.githubusercontent.com/openai/math/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex) specifies O(s) bit wires, polynomially many vertices, maximum local degree ≤ceil(s^{9/10}), ring (Z/2^{P₀}Z)[V]/(V^ℓ) with P₀,ℓ=O(s), and uniform local evaluation time poly(s+L)2^{O(s^{9/10})}, polynomial space. It claims exact contraction in poly(s+L)2^{O(s/√log s)}.
* [The documented Lean scope](https://raw.githubusercontent.com/openai/math/main/lean/docs/378.md) states fixed-width exact #CNF with exponent O_k(n(log log n)²/√log n). That scope statement does not itself certify the general tensor theorem.
* [Nguyen, version 1, Theorems 1.1–1.2](https://hexagonmath.org/2611.00004v1), claims a fixed-degree, domain-uniform q^{O_Δ(v/√log v)}poly(L) counting algorithm using imported tensor-recursion foundations. This is not independent confirmation of those foundations.

**UNVERIFIED here:** the full tensor recurrence, all imported proof dependencies, and native-machine formalization. The source statements exist; this audit neither reproved them nor replayed their complete Lean builds. Consequences using them are explicitly **CONDITIONAL**. Do not infer that ETH, SETH, or a new hypothesis is true or false from the notebook's labels.

### The elementary consequence, with its actual budget

Encode each q-label by b=ceil(log₂q) bits. Give each relation a 2b-port table tensor, each variable a legality tensor, and connect occurrence bits by bounded-degree equality trees. Subdivide wires to make the network bipartite. There are O((v+m)b) wires, maximum local degree O(log q), and polynomial-time entry evaluation. Every legal CSP assignment has exactly one extension through the equality trees.

The integer contraction is #CSP. Precision P₀=vb+1 suffices since #CSP≤q^v≤2^{vb}; take ℓ=1. For polynomial q, s=Θ((v+m)log q) satisfies the stated arity and precision conditions. Thus, **assuming the general tensor theorem**, exact counting takes

$$
\operatorname{poly}(L)\,2^{O((v+m)\log q/\sqrt{\log((v+m)\log q)})}.
\tag{1}
$$

For m=O(v), q=v^{Θ(1)}, this is 2^{O(v√log v)}=q^{O(v/√log v)}, not 2^{O(v)}. This derivation does not require bounded primal degree.

Accordingly the old SPACH/rSPACH/CEH assumptions excluding q^{o(v)} algorithms are **incompatible with that external premise**. They are suspended as hardness sources, not independently disproved in this audit. The equations and reductions developed under them can still be valid mathematical statements.

## Surviving candidates and their limitations

The candidate rNSE-SCSP(c) excludes every bounded-error randomized 2^{Av}L^B algorithm for cubic CSP with q=ceil(v^c), for any fixed A,B. This is an **unproved hypothesis**, stronger than its deterministic analogue. Compatibility with (1) is not affirmative evidence for it. The target is exclusion of 2^{O(v)}, not merely 2^{o(v)}.

A separate, stronger-scale candidate uses m=Θ(v√log v), q=v^c, and excludes q^{o(v)}. Formula (1) only becomes q^{O(v)} there. Under that new hypothesis, the linear-in-v+m HOM construction would exclude 2^{o(n√log n)} on its polynomial-target output family. Nothing proves that this density scale is intrinsic or that the candidate is true. For m=O(v(log v)^a) with fixed a<1/2, (1) already gives q^{o(v)} conditionally.

[Carbonnel's 2026 theorem](https://arxiv.org/abs/2602.23000) gives single-exponential HOM for target classes excluding a fixed topological minor. It does not settle arbitrary 2-degenerate targets. In our actual gadget, one universal relation contains a subdivision of K_{q,q}, hence subdivisions of arbitrarily large cliques as q grows. Bounded degeneracy alone does not give the exclusion required by that theorem.

## The first unresolved obstacles and next steps

1. **Algorithmic structure.** Combine [rank-cycle expansion, bounded fibers, and certified quotients](../results/csp-algorithms.md) with a quantitative cost budget. No theorem says every sparse instance has one of these useful decompositions. Seek a recognition/branching lemma with a proved decrease, rather than interpreting failure of a parameter as hardness.
2. **Random-instance search.** For cubic critical expanders, deleting one edge leaves polynomially many near-solutions. Can they be found globally in polynomial output-sensitive time? [Treewidth deletion](../barriers/structural-compression.md) and [feasible local moves](../barriers/local-search.md) block specific strategies. Separately, the growing-degree model has a proved existence/search gap for 1<γ<2; quiet planting suggests testing algorithms that find some solution, not the original planted witness.
3. **Independent hardness.** The [short-verifier route](clique-and-circuits.md#the-short-verifier-route) would transfer randomized PCC hardness, but its verifier is missing. The isolation theorem preserves worst-case promise hardness; it says nothing about the Bernoulli ensemble.
4. **External verification.** A dedicated audit of the general contraction theorem would clarify the quantitative frontier. It is a separate substantial mathematical project, not a status upgrade justified by a passing local script.

Historical extensions not needed for these conclusions include sparse-source SubISO via color coding, source-SCC functional quotients, and detailed growing-degree grouping recurrences: original notes 33–41 in the [history](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs). Their omission from the current theorem list is not a refutation.
