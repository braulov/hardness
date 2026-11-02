# CRITICAL ALERT 2026-11-02: reported domain-uniform sub-q^v bounded-degree binary CSP algorithm

**Status: externally CLAIMED theorem, NOT independently verified. All complexity and no-go deductions below are conditional on its correctness.** This note takes priority over the earlier SPACH and Permutation Clique compiler notes. Randomized and deterministic algorithms/reductions are both allowed.

## A. Primary source and exact claimed parameters

Troy Tri Nguyen, "A Sublinear Treewidth Exponent for Binary Constraint Satisfaction," Hexagon 2611.00004v1, dated November 2, 2026:
https://hexagonmath.org/2611.00004v1
Index: https://hub.valency.io/works/W_88675vdy

The abstract and reported Theorem 1.2 assert one UNIFORM deterministic algorithm which exactly counts solutions of EVERY explicitly tabulated binary CSP with v variables, q>=2 alphabet symbols, and constant maximum degree Delta in time

    L^{p_Delta} * q^{C_Delta*v/sqrt(log v)},

for constants p_Delta,C_Delta depending only on Delta, NOT on q, and L the complete-table input length. Arbitrary binary relations are allowed. The new work is AI-assisted and reports a Lean 4 formalization, but neither the exact source of the algorithm nor the imported results were independently inspected in this iteration. The manuscript cites Anthropic tensor recursion plus OpenAI contributions.

CAUTION: https://github.com/aster2024/openai-math-followups explicitly notes that the related Boolean tensor contraction Theorem D.1 of the OpenAI ETH manuscript was not among the original Lean-certified main statements. This is NOT evidence of invalidity; it is a reason to inspect precisely what Nguyen formalized and what dependencies are axiomatized.

CRITICAL CHECKS: single fixed machine, q-independent constants, arbitrary explicit relations, finite-alphabet bit complexity, polynomial input-length factors, ring precision, genuinely verified Lean theorem versus assumed tensor contraction primitive.

## B. Conditional falsification of SPACH AND rSPACH (direct exponent calculation)

Recall SPACH says: for a fixed polynomial alphabet q=v^c, no uniform deterministic 2^{o(v log v)}poly(L) algorithm solves all cubic (max degree 3) sparse binary CSP. rSPACH excludes bounded-error randomized algorithms too.

Plug Delta=3 and q=v^c into the CLAIMED theorem:

    log_2 T = O(log L) + O((v/sqrt(log v))*log(v^c))
            = O(v sqrt(log v))
            = o(v log v).

Because q=v^c and constant degree imply polynomial explicit input size, this directly contradicts SPACH, and the deterministic algorithm also contradicts rSPACH. IF the theorem is valid, both candidate hypotheses are FALSE, not just weak. More generally it defeats a no-q^{o(v)} hypothesis at any fixed degree, with polynomially describable domains.

It does NOT contradict a weaker hypothetical lower bound q^{Omega(v/log v)}, which is smaller than the algorithmic upper exponent v/sqrt(log v).

## C. Conditional universal reduction lower bound assuming randomized PCC hardness RPCC-H

RPCC-H (separate NEW hypothesis): no bounded-error randomized 2^{o(k log k)}poly(k) algorithm decides arbitrary k-by-k Permutation Clique.

Suppose a uniform randomized, one-sided bounded-error polynomial-time reduction maps EVERY PCC(k) input to binary CSP with
- v'(k) variables, v'=o(k sqrt(log k)),
- max degree <=3 (or any fixed Delta),
- alphabet q'=k^{O(1)}, with a uniform constant exponent,
- output explicit input length L'=k^{O(1)}.

Solve the target by Nguyen. Since x/sqrt(log x) is eventually increasing and v'=o(k sqrt(log k)), we obtain

    log T <= O(log k) + O(v' log k/sqrt(log v'))
          = o(k log k).

Composition yields a bounded-error randomized 2^{o(k log k)} algorithm for PCC, contradicting RPCC-H. This applies to FULL decision-preserving randomized reductions; it assumes no fixed encoder, no rank bound, no projection of every source solution, and no small treewidth.

Quantitative threshold: if v'=O(k log^beta k), then log T=O(k log^{beta+1/2}k). Every beta<1/2 contradicts RPCC-H. At beta=1/2 this bound is 2^{O(k log k)} and no contradiction follows; beta=1 (Beneš-size overhead) is also not ruled out.

In particular an O(k) compiler would yield a 2^{O(k sqrt(log k))} randomized algorithm for PCC, DISPROVING RPCC-H if Nguyen is correct. Thus continue a linear compiler only as an ALGORITHMIC goal, not a strategy to establish RPCC-H -> SPACH hardness.

## D. Elementary exact CSP-to-tensor translation

For a degree-Delta graph of v variables with domain [q], create one equality tensor of arity degree(x) per variable x, and one binary relation tensor R_e for each original constraint e=xy. Connect equalities to relation tensors along variable-edge incidences. Number of tensors and wires O_Delta(v), bond dimension q, maximal arity max(Delta,2); tensor contraction is exactly the number of CSP solutions. Bit precision P>v log_2 q suffices for exact integer answer via a modular 2^P count if needed.

This proves a reduction to bounded-valence tensor contraction but DOES NOT by itself establish q^{O(v/sqrt log v)}. That demands a contraction theorem UNIFORM in growing bond dimension q, including bit complexity. Boolean-only q=2 tensor results do not automatically imply it. This is the key independent audit point.

## E. What remains unaffected and priorities

- Dense PCC -> log-width CNF with Theta(k log k) Boolean variables is still a valid deterministic reduction. The new CSP algorithm does not automatically solve all log-width SAT in 2^{o(n)}, because a suitable linear-parameter reduction to bounded-degree polynomial-alphabet CSP is missing.
- The proposed general lower-bound transfer to HOM with target degeneracy 2 and polynomial target size is not automatically rescued or refuted; it requires fresh parameter bookkeeping.
- Existing restricted-model rank, routing, VC, LTC and fixed-encoder lemmas may remain correct but are no longer the bottleneck if Nguyen is correct.
- The historical ETH lower bound for cubic CSP is conditional on ETH and does not prevent a q^{o(v)} upper bound post-2026.
- Unconditional correctness of RPCC-H is not established; the compression no-go is conditional on BOTH it and Nguyen's claimed theorem.
- Check exact Lean proof dependencies and source correctness ASAP. If confirmed, archive SPACH/rSPACH as FALSE, formulate a weaker hypothesis compatible with q^{O(v/sqrt log v)}, and seek an efficient PCC algorithm or an appropriately weaker sparse-CSP/HOM hardness source.
