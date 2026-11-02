# PSCH — Polynomial-Size Clique Hypothesis

**Research notebook / archive.** Imported from the November 2, 2026 research discussion; last cumulative checkpoint: v7. This is a research program, **not** a paper or a collection of externally verified theorems. Claims marked "PROVED" in the checkpoint are internal proof sketches or arguments and still need an independent mathematical and novelty audit before citation.

## Hypothesis (working formulation)

**PSCH** proposes that there is no deterministic uniform algorithm for ordinary (k)-CLIQUE on graphs with (N\le k^2) vertices running in (2^{o(k/\log k)}\operatorname{poly}(N)) time. Quantifiers, uniformity, and whether to allow randomized algorithms must be fixed rigorously.

Ordinary (k)-CLIQUE and (k\times k) *multicolored* Clique must not be silently identified: a fast ordinary Clique algorithm handles the multicolored subclass, but a reduction valid **only** on that subclass does not establish hardness for all ordinary Clique instances.

## Two separate ongoing branches

**A. Failure of PSCH and circuit lower bounds.** Attack (mathrm{FastClique}\Rightarrow mathrm E^{\mathrm{NP}}\not\subseteq \mathrm{P/poly}), using Williams-style SAT-to-circuit transfer, easy witnesses, locally checkable tableaux, and alternative non-black-box approaches. A quantitative (n\log^2 n) circuit lower-bound transfer is recorded as **audit needed**, not certified. Universal witness-checker compression faces a Dell–van Melkebeek-style obstacle. The full one-pass research brief is [here](../../prompts/psch_williams_one_pass_2026-11-02.md).

**B. Consequences of PSCH for 2-CSP, HOM, Subgraph Isomorphism and related problems.** The direct Clique-to-dense-CSP reduction is standard. The (1)-subdivision construction gives conditional lower bounds for 2-degenerate Subgraph Isomorphism (including the parameter loss). The hard open goal is a **deterministic, decision-preserving** compiler for ordinary (k)-CLIQUE with (N\le k^2) into binary CSP of maximum degree (3), (m=O(k\operatorname{polylog}k)) constraints and alphabet (k^{O(1)}).

## Main research experiments in branch B

- Exact sparse representations via algebraic rank, Boolean rectangle covers, threshold/Ferrers constraints, and global synchronizations/permutation transports (structured subclasses only).
- Lower bounds for fixed linear and nonlinear code/check topologies, and information counting for exact projected-solution representations. These **do not** rule out arbitrary decision-only reductions with existential auxiliary variables.
- Sum-check and PCP approaches: short interaction is not the same as a short deterministic CSP certificate; short constant-gap PCP plus random sampling yields a **randomized** CSP transformation, not automatically a deterministic consequence of PSCH.
- A dense high-rank NP-hard planted-sync example with (O(k))-constraint sparse compilation: illustrative, not a universal reduction.
- Beneš permutation networks: existentially compile (mathrm{AllDifferent}) to (O(k\log k)) binary constraints with polynomial alphabet; combined with path-adjacency, gives a Hamiltonian Path model with (\Theta(k^2)) pairwise inequalities but a short equivalent existential encoding.

**Not established:** universal dense-Clique-to-sparse-CSP compilation; PSCH-based prohibition of single-exponential 2-degenerate HOM; (mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{P/poly}) from FastClique; an improved HC algorithm. The Hamiltonian Path construction is an encoding, **not** an algorithmic speedup.

## Where to continue

1. [Full chronological checkpoint v7, November 2](2026-11-02_full_checkpoint_v7.md) — all recorded arguments, limitations, source links, corrections, and open problems.
2. [Research brief for branch A](../../prompts/psch_williams_one_pass_2026-11-02.md).


3. [Universal-selector quantified CSP compilation (Nov 2)](2026-11-02_universal_selector_qcsp.md) — a precise `exists-forall-exists` tree-CSP with O(k) constraints for *arbitrary* dense binary CSP, identifying one universal index as the exact obstacle; not a solution for unquantified CSP.

4. [One-variable divisibility and quotient-circuit barrier](2026-11-02_univariate_remainder_and_quotient_barrier.md) — exact ordinary-Clique identity, scalar-trace caveat, and an unconditional lower bound for *explicit quotient* arithmetic circuits; universal compilation remains open.

5. [Planar exact-extension separator barrier](2026-11-02_planar_extension_separator_barrier.md) — unconditional Ω(k²/log²Q) lower bound for planar exact projected-solution encodings of a sparse expander-port CSP, plus a separate PSCH-conditional decision-only tradeoff.

The repository's older [graphic-rank/span project](../../README.md) is a related but distinct research program. Keep separate statements and assumptions separate.

## Audit priority

Before publication, verify the exact quantitative Williams implication, all proof details and novel-claim priority, reductions between ordinary and multicolored Clique, and the complexity of all table-encoding gadgets. Preserve "conditional", "model-restricted", and "open" labels when reusing this material.
