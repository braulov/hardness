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

## F. Further source audit, 2026-11-02 (source descriptions only, no reproduced Lean build)

The fuller indexed text of https://hub.valency.io/works/W_88675vdy states the decisive details in its introduction: Theorem 1.2 is UNIFORM in D=q, and counts arbitrary complete-table degree-Delta binary CSP in L^{p_Delta}D^{C_Delta k/sqrt(log k)} time. It explicitly warns that binary-encoding domain values into Boolean variables and applying 3SAT DOES NOT provide this bound: arbitrary binary relations require Omega(D² log D) Tseitin variables. It invokes signed tensor-network recursion from Anthropic with factorization capacities, and credits graph constructions to OpenAI.

The indexed text lists formal endpoints DenseCSPTheorem.exists_counter and SparseNativeMachine.exists_native, Lean 4.33.1, 82 downstream modules and selected 633 upstream counting modules, and says the reported axiom dependencies are only propext, Classical.choice, Quot.sound. It gives the Anthropic revision 16a5ce41304fcdaea4e0be7c132e1c361dc26da5 and the OpenAI math revision 7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a. These are claims made in the manuscript; the current audit has NOT executed the build or manually reviewed the imported quantitative theorem.

## G. Candidate surviving hardness for the HOM single-exponential objective

Even if the new algorithm is valid, its cubic poly-alphabet running time is 2^{O(v sqrt(log v))}, which is super-single-exponential in v. Thus the following DIFFERENT working candidate is not refuted by the displayed upper bound:

    NoSingleExpSparseCSP:
    for some fixed c>=1, cubic sparse binary 2-CSP with v variables and q=ceil(v^c)
    has NO uniform 2^{O(v)}poly(L) decision algorithm
    (deterministic or bounded-error randomized variant specified separately).

This is a much WEAKER hardness statement than SPACH/rSPACH and a new unproved hypothesis; no implication from RPCC-H or post-ETH results is established. A q^{Omega(v/log v)} lower bound with a definite positive constant is NOT enough to rule out every 2^{O(v)} algorithm; one must carefully distinguish no q^{o(v/log v)} from no q^{O(v/log v)} for arbitrary constants. For q=v^c, q^{O(v/log v)} = 2^{O(v)}.

If an independently CHECKED reduction maps the assumed hard sparse CSP family into ordinary HOM(G,H), with |V(G)|=O(v), |V(H)|=v^{O(1)} and degenerate target H, then any hypothetical uniform HOM algorithm in 2^{O(|G|)}poly(|H|) would yield a forbidden sparse CSP algorithm. This is only a conditional template: the concrete HOM gadgets, target degeneracy, list elimination and size accounting must be rechecked. It is NOT a proved HOM lower bound.

Separately the weaker no-q^{o(v/log v)} candidate is compatible with the new q^{O(v/sqrt log v)} upper bound, but it does not rule out 2^{O(v)} algorithms; at most it rules out 2^{o(v)} for q polynomial. Avoid conflating these statements.

## H. Another direct consequence: arbitrary m-constraint binary CSP

A general binary CSP with v variables, m binary constraints and domain q can be made maximum-degree-3 by splitting each source variable into occurrence copies connected via a path of equalities. The resulting CSP has v'=O(v+m), m'=O(v+m), the SAME q, and is satisfiable iff the original is. Hence, conditional on Nguyen, one gets an algorithm for ALL explicitly tabulated binary CSPs with

    T=(L+v+m)^{O(1)} q^{O((v+m)/sqrt(log(v+m)))}.

This is not useful on dense PCC itself because m=Theta(k²) and the bound is worse than brute force; it is useful on nearly-sparse CSP. The polynomial prefactor includes writing equality tables, which are q² in size, still polynomial in complete-table input.

## I. Direct verification of the key ARBITRARY-RELATION factorization (elementary, independent of the claimed fast algorithm)

Let v CSP variables have max degree Delta and domain [q], and let b=ceil(log_2 q). Partition them into g groups, each of size s<=ceil(v/g). One group symbol x is the concatenation of s domain labels, so its bit length is at most sb. For groups G,H, let E_GH denote the original constraints crossing them; |E_GH| can be arbitrary but sum_H |E_GH|<=Delta*s.

Let the group-to-group Boolean interaction be Psi_GH(x,y)=product_{e=(i,j) in E_GH} R_e(x_i,y_j). This is arbitrary: each R_e can be any q by q relation. Introduce theta=(theta_e:e in E_GH) in [q]^{E_GH}. Define

    f_GH(x,theta)=prod_{e=(i,j) in E_GH} [x_i=theta_e],
    f_HG(y,theta)=prod_{e=(i,j) in E_GH} R_e(theta_e,y_j).

Then the exact identity

    Psi_GH(x,y)=sum_{theta in [q]^{E_GH}} f_GH(x,theta)*f_HG(y,theta)

holds as an integer equality. The intermediate index theta needs at most b|E_GH| bits, and the sum of capacities incident to a group G is <=Delta*s*b. Local constraints wholly inside a group are included in a 0/1 unary weight W_G(x). Thus the grouped signed network satisfies setting length <=s*b and row capacity <=Delta*s*b, both <=P=O_Delta((v/g+1)log q). Relation-table queries can be computed from the input in time polynomial in L and v (evaluate O_Delta(s) original entries); no huge grouped-state table need be explicitly written.

This part of the reduction is a COMPLETE checked algebraic identity, with the crucial q-dependence only through log q. The unverified external statement is the *uniform rapid evaluation* of the resulting grouped network; no fast algorithm follows merely from this factorization.

## J. Reconciliation with an ALREADY EXISTING stronger local audit (important, 2026-11-02)

Current repository work also contains [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md), independently developing the implications of the **FULL BOOLEAN tensor-contraction theorem (Theorem D.1)** in OpenAI's Oct. 25 manuscript. It is stronger for our immediate purpose: FOR q=k^{O(1)}, the Nguyen q-uniform theorem is not even necessary.

Note 33 gives an explicit Boolean tensorization: represent each q-ary CSP variable by b=ceil(log_2 q) bit wires; introduce an arity-b legality tensor per source variable and an arity-2b relation tensor per binary constraint; copy shared bits with trivalent equality trees and make the network bipartite. This yields

    M=O((v+m)*log q) Boolean wires,
    P_0=v*b+1 precision bits, maximum local arity O(log q),
    contraction = exact #CSP mod 2^{P_0}.

If the FULL Theorem D.1 applies to this network and local-table time assumptions, its runtime is

    poly(L) 2^{O(M/sqrt(log M))}.

For q=v^{Theta(1)} and m=O(v), this is 2^{O(v sqrt(log v))} poly(L). This yields the same conditional refutation of SPACH/rSPACH and compiler threshold O(k sqrt log k). It is NOT a new independently verified fast contraction theorem; the full Boolean contraction theorem is itself an external premise and is not covered by the separately declared Lean fixed-width counting theorem. The new Nguyen preprint CLAIMS an additional q-uniform formalized adaptation. These are two AUDIT PATHS with shared external ideas, not two independently settled proofs.

I initially recorded the Nguyen theorem before discovering note 33 was already in the repository. Do not attribute the reduction or numerical contradiction to this note as novel; use note 33 as the primary archived mathematical analysis for polynomial q, and this note as the fresh November 2 external source/Lean-uniformity audit and surviving-no-single-exponential hypothesis discussion.
