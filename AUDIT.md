# Mathematical audit and cleanup — 2026-11-04

## Scope and standard of confidence

This revision replaces a chronological accumulation of 107 research documents, prompts, and repeated summaries with a small topical exposition. It preserves the original repository at commit [c994435b692c37958eeff2c997188603dcaeddb6](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6). No history was rewritten.

The audit traced the main research branches and reconstructed the arguments retained in results/ and barriers/, checking reductions, error models, parameters, and relevant primary sources. Existing claims of AI verification were not treated as proof. This is **not a certification of every sentence in all historical notes**: several finer results, literature-priority questions, and imported algorithms remain outside the independently checked proof set. They are identified below, rather than silently promoted or called false.

The current theorem statements are intended to be usable with the proofs and explicit external ingredients supplied beside them. Classical facts such as the Isolation Lemma, König's theorem, the Beneš routing theorem, and standard finite-field algorithms are used as such. This audit is not a formal proof-assistant verification.

## Material mathematical changes

| Historical claim or ambiguity | Current conclusion and location |
|---|---|
| A bounded-error randomized unique-CSP solver was claimed to yield one-sided error just by amplification | **Incorrect composition argument.** Amplification gives bounded error; one-sidedness follows directly for an exact promise oracle. An additional verified-witness argument would be needed for the stronger randomized claim. [Isolation, error accounting](results/isolation.md#promise-and-error-accounting) |
| Early isolation text denied a one-output reduction; a later addendum supplied one | Consolidated the valid single-output, inverse-polynomial-success promise reduction. Outputs need not always satisfy the uniqueness promise. |
| SAT-to-Clique starting point grouped variables and assumed pair checks handled arbitrary 3-clauses | **Incomplete proof, not a refutation of the claimed implication.** Replaced it openly with a clause-grouping proof yielding k=Θ(m/log m), N≤k², and the claimed 2^{o(m/log²m)} consequence. [Corrected reduction](directions/clique-and-circuits.md#corrected-sat-to-clique-starting-point) |
| Quiet planting's hidden-assignment recovery rate was stated after averaging over random G | **Unjustified exponential rate.** The displayed rate is valid conditional on typical G; merely o(1) exceptional probability gives only an unconditional o(1) recovery guarantee without further tail analysis. [Recovery quantifier](results/random-csp.md#quiet-planting-and-the-correct-recovery-quantifier) |
| Recent tensor algorithms were sometimes treated as settled, sometimes as nonexistent | The cited primary statements exist. Their full proofs/builds are **UNVERIFIED here**. The CSP consequence is **CONDITIONAL**, with the bit-wire, arity, precision, and evaluation budgets written out. [External algorithm status](directions/csp-hom.md#external-algorithm-status) |
| Poisson counts, all-edge dependence, or arc-consistency failure could suggest computational hardness | The elementary bounded-treewidth prism family has the same properties and polynomial counting. The interpretation as sufficient hardness evidence is **REFUTED**. This counterexample already appeared in the history; it is now central. [Easy control](results/random-csp.md#an-easy-family-with-the-same-statistics) |
| High relation rank, commutator rank, or large product-feature rank was used as a difficulty proxy | Retained only sufficient algorithmic criteria and explicitly scoped representation lower bounds. Functional constraints, decision quotients, affine features, and Ferrers factors show why a large parameter is not a runtime lower bound. |
| Block-interface rank could be read as simultaneously defeating every adaptive partition | The theorem says **for each partition there exist tables** attaining matching-number rank. It does not provide one hard table set against all relation-adaptive partitions. [Structural barrier](barriers/structural-compression.md) |
| Rational rank expansion counted field operations without explicit common-denominator accounting | Added a common denominator for each chord's factor products, giving polynomial bit length for exact accumulation. [Rank-cycle proof](results/csp-algorithms.md#expand-only-the-non-tree-relations) |
| All-fields zero-pattern counting was attributed imprecisely | The cross-characteristic ingredient is Nelson's extension of the fixed-field Rónyai–Babai–Ganapathy result. The quantitative substitution and scope are explicit. [Encoding barrier](barriers/encoding.md#exact-linear-representations-can-fail-over-every-field) |
| Thin summaries obscured ordinary-HOM pinning, parameter changes, or preservation of counts | Reconstructed the complete pinning and length-three subdivision arguments, exact sizes, and family-indexed algorithmic equivalence. The reduction preserves decision, not homomorphism counts. [CSP–HOM proof](results/csp-hom.md) |
| A hard subdivided-clique SubISO family was used to motivate Hamiltonian-cycle hardness by specialization | That specialization is invalid: the hard pattern is not a cycle. Only the actual parameter-controlled SubISO consequence is retained. [Direct reductions](directions/clique-and-circuits.md#what-direct-reductions-actually-buy) |

Several of these cautions were already present in later notes. Consolidating them does not constitute a new research discovery.

## What was kept, and why

The strongest usable material is the exact CSP–HOM transfer; the feature-span, factor-matching, and chord-rank algorithms; the precise limits on preserved-witness encodings; and the random-CSP moment calculations with their easy controls and restricted search obstacles. The span/parity identities and isolation construction are useful reusable tools. They have been kept as coherent proofs, with decision, counting, and promise consequences separated.

No theorem proves a universal favorable decomposition, a short general PCC verifier, a 2^{O(v)} sparse-CSP algorithm, or a new circuit lower bound. Those remain research objectives. No repository-specific result is claimed novel without a literature audit.

## Historical material that is not part of the current proof set

The [pinned original docs tree](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs) remains the source for the following. File-number ranges overlap because several branches used the same numbering; filenames, not numbers alone, identify a note.

* **Span and early win-win plans (01–20).** Core identities survive. Broad rank-budget algorithms, the weighted counting engine, and input-efficient circuit/Barrington interfaces remain open. Detailed gauge/spectral calculations are historical supporting examples; the exact conjugation identity and shared-input warning survive.
* **Order decompositions and group refinements (21–32).** The strongest general feature-span argument and width boundaries survive. Finer separable-order/deletion-distance algorithms, observable quotients, class-two cutrank formulas, and some group-action refinements were not all reconstructed here. Their omission is not a refutation; original scripts remain available for later review.
* **CSP/HOM and grouping (33–43).** The reduction, exact algorithms, and uniform graph-partition obstruction survive. More specialized SubISO, SCC, cutwidth, row-sensitive grouping, and tensor recurrence variants are not independently certified by this revision. All imported contraction consequences remain conditional.
* **Random CSP and local search (35–51).** Exact moments, cut counting, conditional Poisson, the prism control, freezing, and feasible-move isolation survive. Overlapping-tree lookahead/search-tree bounds in notes 40 and 43–44 depend on a more elaborate algorithm model and were not promoted to a general barrier.
* **PCC algebra and matroids (40–48).** Supplied factor algorithms, all-fields counting, deterministic source-degree, and public-hash quantifier barriers survive. Individual GF(7)/Ingleton gadgets, oracle sparse-paving encodings, and detailed group-algebra normal forms remain in history; an oracle construction does not become an explicit vector representation.
* **PSCH and CEH subtrees.** The explicit hypotheses, corrected starting reduction, short-verifier sampling argument, and scope warnings survive. The claimed quantitative E^NP lower-bound route remains **UNVERIFIED**. Universal-selector and fixed-routing normal forms are linked for future use; neither removes its missing quantifier or logarithmic cost. Long derivations of failed individual algebraic compilers were not copied into the main exposition.

The removed prompts and repeated English/Russian summaries contribute no additional proof once their useful content has been extracted. Git history, rather than a second chronological archive in the current tree, preserves them.

## External-source checks

The current files link directly to primary sources. In particular:

* Braulov–Chukhin–Kulikov–Mihajlin §4: inspected the pinning and subdivision arguments and checked the generalized construction and constants.
* Nelson §2: inspected the all-fields zero-pattern theorem and checked its parameter substitution.
* Karger, Theorem 4.7.6, and Arratia–Goldstein–Gordon, Theorem 1: checked the cut-counting and dependency-neighborhood statements used in the random-CSP proof.
* Deterministic matroid truncation/rank-condensing sources: checked the relevant construction context; the needed folded-Wronskian argument is supplied locally.
* OpenAI tensor statement, its documented Lean scope, and Nguyen v1: checked the actual statements and their differing scopes. Did **not** independently certify the full contraction proof or replay formal builds.
* Carbonnel's target-class hypothesis and Williams's algorithm-to-lower-bound setting were checked to avoid applying a theorem outside its model. No full literature-priority search or certification of every historical external citation was performed.

## Validation

The mathematical arguments, not finite scripts, justify the asymptotic statements. Existing standard-library checks were run for graphic span/parity, low-degree two-sweep features, the S₃ counting gadget, biclique/Ferrers factors, exterior-algebra matching and rank condensation, two simultaneous matroids, endpoint-collision and close-pair identities, degree-restricted compilers, public fingerprints, prism decompositions, and cubic bipartite completion. All passed.

The new [rank-cycle check](experiments/check_rank_cycle.py) compares exact rational chord expansion plus forest messages with direct enumeration, including disconnected graphs, zero relations, unequal ranks, and factorizations with negative fractional entries. It is a finite regression check, not evidence of a general speedup beyond the proved formula.

Other historical experiments are retained for provenance but are not claimed to have all been rerun. There is no new test framework or status registry.

## Suggested mathematical review order

1. **CSP–HOM proof and external boundary:** check the fixed pins, subdivision reflection, exact size constants, and the distinction between a derived conditional bound and an audited external theorem.
2. **Random-CSP quantifiers:** inspect conditional recovery, deletion-table independence, the simultaneous c>9 estimates, and the separation between access/search restrictions and unrestricted algorithms.
3. **Encoding models:** check all-fields quantification, the decision-only degree assumption, and the public-seed existential witness issue before using a barrier against a new construction.
4. **Two-sweep feature lemma:** check that stored basis elements are actual assignments, and that occurrence-copy hardness uses word length rather than original input count.
5. **Corrected SAT-to-Clique and isolation statements:** these are localized proof/error corrections with downstream consequences.

The most promising immediate projects are a relation-sensitive decomposition theorem, global near-solution enumeration on expanders, and a concrete short-verifier construction. A dedicated audit of the imported contraction theorem is a separate high-impact prerequisite for any unconditional claim about the changed complexity frontier.
