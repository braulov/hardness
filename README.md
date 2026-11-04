# Hardness: sparse constraints, global witnesses, and exact algorithms

This notebook asks how much information a small constraint system must retain to certify a global combinatorial witness. The clearest remaining problem is:

> For each fixed c,a, can binary CSP with v variables, at most av constraints, and at most v^c labels be decided in 2^{O_{c,a}(v)} time, up to polynomial input factors?

A label assignment contains Θ(v log v) bits. Removing that logarithmic factor from exhaustive search would be substantial. A checked linear-size reduction makes this question equivalent to the corresponding family of single-exponential **ordinary graph homomorphism** algorithms when both graphs are 2-degenerate and the target has polynomial size. General sparse CSP has not been reduced to an already tractable class.

The broader program explores two possible outcomes: better algorithms that compress witnesses, or useful independent hardness assumptions and reductions. A hoped-for connection to general circuit lower bounds still lacks an input-efficient reduction. **No new general hardness theorem or circuit lower bound is established here.**

## Established results

| Result | What it establishes | Main limitation |
|---|---|---|
| [Sparse CSP ↔ 2-degenerate HOM](results/csp-hom.md) | An ordinary, uncolored decision reduction with source size 255v+257m+251; precise algorithmic equivalence | Changes fixed polynomial alphabet/target exponents; does not preserve counts |
| [Structured CSP algorithms](results/csp-algorithms.md) | Exact counting in poly(L)∏_{e outside a forest} rank_Q(R_e); Boolean-cover and certified decision-quotient variants | Requires useful relation structure; high rank is not hardness |
| [Two-sweep branching programs](results/two-sweep-programs.md) | Constructible feature spans give deterministic SAT; fixed affine/unitriangular first sweeps are tractable; width-two exact counting is polynomial | Irreversible width three already encodes 3-SAT; even S₃ can have #P-hard counting |
| [Permutation constraints with supplied factors](results/permutation-factors.md) | Biclique/Ferrers covers reduce to matching; explicit fixed-many linear matroids admit 2^{O(K)} algorithms | Does not find a short factorization of arbitrary PCC; matroid oracles are not vector representations |
| [Random CSP statistics and controls](results/random-csp.md) | Exact overlap identities, critical cubic Poisson laws, conditional laws after deleting a table, and a growing-degree existence/search gap | The same cubic statistics hold on easy bounded-treewidth prisms |
| [Linear-size randomized isolation](results/isolation.md) | Inverse-polynomial isolation success into unique bipartite cubic CSP with polynomial alphabet | Promise/error accounting matters; no transfer to the random-table distribution |
| [Graphic/cographic span](results/graphic-span.md) | Sparse encodings of familiar graph problems, duality, and an exact parity identity | Parity is not decision; the weighted-counting route remains conditional |

Here **PROVED** means a complete mathematical argument is supplied and was checked in this audit, allowing identified classical theorems. It does not mean formal verification or a claim of novelty. **CONDITIONAL** identifies explicit unverified or conjectural premises; **OPEN**, **PARTIAL**, **REFUTED**, and **UNVERIFIED** are used where appropriate. The [audit report](AUDIT.md) records material corrections and the limits of the review.

## Barriers and active directions

Three groups of rigorous, restricted barriers survive:

* [Encoding barriers](barriers/encoding.md): fixed-view witness codes need quadratic many tests; generic PCC validity patterns cannot be represented by one linear matroid over any field, or by sufficiently small fixed-degree additive features. A separate degree lower bound applies to deterministic decision-only vector compilers. Randomization and existential auxiliary choices change the models.
* [Structural compression barriers](barriers/structural-compression.md): small graph-adaptive blocks retain almost all separate matching interfaces; naive large tensors violate local-cost requirements; deleting few expander edges cannot remove linear treewidth.
* [Restricted local-search barriers](barriers/local-search.md): freezing labels without crossing-table information fails, and almost all deleted-edge solutions on suitable cubic expanders are isolated under feasible moves changing at most half the variables.

None excludes every decision-preserving compiler or every CSP algorithm. A failed construction is not treated as a general barrier. A universal obstruction to single-exponential algorithms remains conjectural; the present evidence does not establish one.

The active directions and their first missing steps are:

1. **[Sparse CSP and HOM](directions/csp-hom.md).** Prove a useful decomposition combining propagation, quotients, and residual cycle cost, or find a global way to enumerate the few deleted-edge solutions of random expander instances.
2. **[Clique compression and circuit lower bounds](directions/clique-and-circuits.md).** Construct a genuinely short compatibility verifier, or a decision-only compiler escaping the preserved-witness barriers. The circuit branch separately needs controlled original-input overhead.
3. **[Span and program SAT](directions/span-and-programs.md).** Extend effective feature spaces beyond the current classes; resolve the weighted-counting requirements for span decision.

The [conceptual guide](intuitions/what-to-compress.md) explains why existence, exact counts, original witnesses, and information access lead to different valid compressions.

## External claims and the current frontier

Recent primary sources claim subexponential SAT/tensor algorithms. Their relevant statements were checked on 2026-11-04, but their full proofs and formal builds were **not independently certified here**. The [source audit and parameter derivation](directions/csp-hom.md#external-algorithm-status) are explicit about that boundary.

Assuming the general tensor theorem, sparse polynomial-alphabet CSP has an exact counting algorithm in 2^{O(v√log v)} time. This would invalidate older hypotheses forbidding q^{o(v)} time, but it still does not provide 2^{O(v)}. Accordingly those older hypotheses are suspended as hardness sources **conditional on that external theorem**, rather than declared unconditionally refuted. PSCH, randomized PCC hardness, and the proposed no-single-exponential CSP hypothesis remain distinct unproved assumptions.

## Reading and provenance

Start with this page, [CSP ↔ HOM](results/csp-hom.md), and [the live CSP direction](directions/csp-hom.md). Read [AUDIT.md](AUDIT.md) for the mathematical corrections, unresolved historical arguments, validation, and suggested review order.

The chronological notes, prompts, and duplicate summaries are preserved at commit [c994435b692c37958eeff2c997188603dcaeddb6](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6), with pinned provenance links in the current notes. Omission from the current exposition is not a claim that an old statement is false.

The standard-library programs in scripts/ and experiments/ are optional finite checks. Their historical numbering is retained for traceability. Passing them is evidence about finite implementations and identities, not proof of asymptotic claims.
