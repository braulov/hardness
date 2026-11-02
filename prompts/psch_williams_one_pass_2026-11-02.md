# One-pass research challenge: FastClique ⇒ general circuit lower bounds

**Status:** research prompt, not a proved implication. Companion to [PSCH notebook](../docs/psch/README.md).

## Main hypothesis and goal

Assume a deterministic uniform algorithm solving **ordinary** (k)-CLIQUE on every graph with at most (k^2) vertices in time (2^{o(k/\log k)}\operatorname{poly}(k)). Call this **FastClique** or (
eg\mathrm{PSCH}).

Your highest-priority target is to rigorously prove

[
\mathrm{FastClique}\Longrightarrow
\mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{P/poly}.
]

Do not limit yourself to a particular encoding of an accepting tableau. Think aggressively about alternative languages, verification relations, local PCPs, witness encodings, non-black-box simulations, and algorithms-to-lower-bounds transfers. Complete at least one deep line of attack or produce a precisely stated new barrier. Distinguish a genuine mathematical advance from a change of presentation.

## Baseline that MUST be independently audited

Grouping sparse 3-SAT variables into blocks of (\Theta(\log m)) yields a (k\times k) multicolored Clique instance with (k=\Theta(m/\log m)). Hence FastClique appears to imply sparse 3-SAT in (2^{o(m/\log^2m)}) time. A Williams-style easy-witness/time-hierarchy argument suggests circuit lower bounds of scale (n\log^2n) for a language in (\mathrm E^{\mathrm{NP}}). Check precise theorems, quantifiers, decoder size, conversion to 3-CNF, and whether these bounds genuinely follow. Do **not** accept this baseline uncritically.

## Main bottleneck

Suppose a hard unary language has a locally decodable exponentially long constraint formula (F_n). Given a putative witness circuit (C) of size (n^c), define (D_C(i)) to indicate whether the i-th local constraint is violated. A standard 3-SAT/Tseitin encoding has size (n^{\Theta(c)}) and cannot be handled in subexponential time using the baseline. Can a specialized verification problem instead be compiled into Clique on (O(n\log n)) parameter and (k^2) vertices, with total construction time (2^{o(n)}), **for every fixed** (c)? Or can you prove a circuit lower bound without this compilation?

A crucial barrier: the completely local formula (F_n=\bigwedge_{i\in\{0,1\}^n}z_i) with (C_Q(i)=1-Q(i)) reproduces arbitrary Circuit-SAT. A universal *polynomial-time* compression of such checkers would violate Dell–van Melkebeek-style sparsification under standard assumptions. Locality alone cannot suffice. Investigate specialized computations, subexponential-time or nondeterministic reductions, succinct consistency certificates, hashing/finite-field fingerprints, and alternate hard languages.

## Independent attack routes

- Direct Williams algorithm-to-lower-bound transfer, witness-generation and useful-properties machinery.
- Change the computation/witness representation, rather than compressing an arbitrary 3-CNF.
- Clique as an algebraic global-consistency certificate, exploiting the structure of the verification relation.
- Oracle or non-black-box barriers; if a universal reduction is impossible, identify the exact excluded model.
- Weaker but nontrivial consequences: (\mathrm E^{\mathrm{NP}}\not\subseteq \operatorname{SIZE}(s(n))) for (s(n)\gg n\log^2n), ideally (n^{1+\varepsilon}); or (\mathcal C\not\subseteq\mathrm{P/poly}) for a well-defined nearby class.

For every construction record: witness-circuit size (s(n)), Clique parameter (k(n)), host graph size (N(n)), reduction time, and complete simulation time. Protect all asymptotic little-o requirements and distinguish deterministic from randomized reductions, ordinary from multicolored Clique, and decision from witness-generation algorithms.

## Deliverable

A self-contained report with (1) strongest **fully proved** implication; (2) strongest candidate toward (\mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{P/poly}); (3) exact missing lemma; (4) hardest obstruction/counterexample; (5) quantitative parameter ledger; (6) literature/novelty audit; and (7) final verdict with PROVED / CONDITIONAL / OPEN labels. Do not present wishful implications as theorems.

Useful starting points: R. Williams, *Improving Exhaustive Search Implies Superpolynomial Lower Bounds*; Jahanjou–Miles–Viola, *Local Reductions*; Dell–van Melkebeek, SAT sparsification lower bounds; Lokshtanov–Marx–Saurabh on (k\times k) Clique; October 2026 ETH-refutation manuscripts (verify their exact current status).
