# Global span constraints and input-efficient program SAT

**OPEN objectives.** Decide sparse graphic/cographic Span-CSP in subexponential time, and extend the two-sweep algorithms to substantially broader branching programs while retaining the number of original input bits as the parameter. These are related investigations, not a proved equivalence.

## What is available

The [span note](../results/graphic-span.md) gives exact sparse graph encodings and a parity identity. The [two-sweep note](../results/two-sweep-programs.md) gives deterministic existence tests from explicit feature spaces, polynomial exact counting for a width-two first sweep, polynomial SAT for fixed affine/unitriangular first sweeps, and the irreversible width-three hardness boundary. These supersede the earlier focus on commutator cutrank as a universal indicator of difficulty.

The first unresolved span step is **decision**, not the parity identity. A finite-field weighted counting theorem with the right overhead would suffice by identity testing, but the documented unweighted fixed-width #SAT statement is not that theorem. Alternatively, a bounded-fanin rank circuit of size o(n√log n/(log log n)²), combined with the stated fixed-width counting bound, would yield a subexponential decision algorithm. Word-RAM connectivity time is not the required Boolean-gate count.

For branching programs, compact feature spaces must span endpoint predicates and admit effective updates. A general first sweep need not have small degree, Fourier support, or product-feature rank. Width-three equality already has exponential product-feature rank. That is a representation barrier; it is not a general exponential-time lower bound.

## Promising concrete next steps

1. Find a constructible feature representation for the **intersection language** rather than preserving every first-sweep endpoint observation. The current span algorithm is a useful sufficient criterion, not a necessary one.
2. Study larger explicitly described first-transition groups/monoids, with S₄ a natural next small case. Existing group equation/ProgramSat results must be matched to the present two-sweep model before transferring complexity claims.
3. Retain order-structure methods as complementary tools. The historical four-boundary DP composes common intervals of the two read orders; separable orders and deletion distance to them offer exact counting algorithms. Their finer parameter claims remain outside this revision's retained proof set, with [notes 21–29](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs) available for a focused follow-up.
4. For the span problem, audit the algebraic requirements of weighted counting, including characteristic two, rather than assuming an unweighted engine is semiring-generic. Keep the hypothetical engine separate from the elementary polynomial identity.

## A useful warning about spectral intuition

In a group program, truly disjoint private input blocks give convolution of their output distributions. Shared inputs do not: E[M₁(x)M₂(x)] generally differs from E[M₁(x)]E[M₂(x)]. A syntactic word U(x)V(x)U(x)^{-1} can be stripped to V for conjugacy-invariant acceptance, even with shared variables; that is an exact identity. It does not apply to arbitrary distinguished-state acceptance.

The old A₅ construction uses this sandwich to retain an exponentially rare accepting input while giving the whole output distribution a constant nontrivial Fourier gap. Thus a constant gap of one distribution does not establish positive mass at every desired output. Strong pointwise mixing from independent blocks and exact cancellation are different mechanisms. The numerical spectral constants and full character calculation are not needed for the retained algorithms and remain in [notes 16–19](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs).

The proposed circuit-lower-bound payoff still requires the [input-efficient bridge](clique-and-circuits.md#circuit-lower-bounds-unresolved-bridge). Occurrence-copy expansion changes the parameter from input count to word length, and does not supply it.
