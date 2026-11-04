# Hardness after ETH: one conditional application

This project sought useful replacements for ETH and algorithms that compress global combinatorial witnesses. The November 4, 2026 reassessment leaves **one application worth checking further**, not a new hardness hypothesis or circuit lower bound.

## Surviving result

[Dense vertex-connectivity problems from exact counting](results/dense-connectivity.md): conditional on the stated arbitrary-density exact #4SAT algorithm, **Connected Dominating Set, Connected Vertex Cover, and unweighted Steiner Tree** on arbitrary n-vertex graphs have randomized, one-sided-error algorithms running in

\[
\operatorname{poly}(n+m)\,2^{O(n\log\log n/\sqrt{\log n})}.
\]

The exponent counts vertices even on dense graphs. The proof combines established Cut & Count and linear-size isolation ingredients; it does not require weighted counting. The implication is checked here; the recent counting theorem's full proof and formal build are not independently certified. The [focused literature comparison](results/dense-connectivity.md#literature-comparison-november-4-2026) found no subsumption in the papers inspected: the closest connectivity follow-up only sketches these applications on sparse graphs. **This is not a certificate of novelty or publishability.**

## Why the old center is gone

Nguyen's [November 2026 CSP preprint](https://hexagonmath.org/2611.00004v1) claims a domain-uniform bound \(L^{O_\Delta(1)}q^{O_\Delta(v/\sqrt{\log v})}\) for fixed maximum degree. Splitting occurrences with equality constraints extends it to O(v)-constraint instances. For q=v^{Θ(1)}, this is \(2^{O(v\sqrt{\log v})}\). Conditional on that theorem, the old prohibition of q^{o(v)} algorithms fails. The remaining 2^{O(v)} question has no sufficiently developed approach here to justify retaining the CSP–HOM reduction as a central result.

No other reviewed direction currently combines a major payoff with concrete mathematical leverage. There is no retained general barrier or unconditional new major theorem.

## Next decision

Seek independent mathematical review of the [external premise and vertex-count accounting](results/dense-connectivity.md#external-premise-and-review-boundary). The remaining possible contribution is the explicit arbitrary-density, vertex-parameter corollary with one-sided randomization, not the established parity technique. Its value as a separate research result remains uncertain. If a matching prior result is identified, remove this application too.

Original work remains in [the pre-cleanup tree](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6) and the research branches. The [earlier audit](https://github.com/braulov/hardness/tree/c20ace6fad1f958e69aa2c7a113bb3a6a26b8d99) was too permissive and incorrectly left sparse Span-CSP decision waiting on weighted counting; the historical parity-and-isolation argument already supplied a conditional unweighted route.
