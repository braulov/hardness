# Domain-uniform sparse CSP, a sharp PCC-compiler window, and subconstant-soundness PCP

**Research date:** 2026-11-02. **Status:** Elementary reductions and parameter algebra PROVED conditional on externally **claimed** theorems. The two serious algorithmic inputs (Nguyen's 2026 domain-uniform counting theorem, OpenAI/Anthropic tensor recursion) have NOT been independently replayed here. The RPCC hypothesis and the sought PCP/reduction remain OPEN. No priority claim is made for the basic gadget transformations.

## A. Primary sources and existing internal notes

- Troy Tri Nguyen, *A Sublinear Treewidth Exponent for Binary Constraint Satisfaction*, Hexagon 2611.00004v1, https://hexagonmath.org/2611.00004v1 . Its Theorem 1.2 claims one deterministic, fixed-Δ, domain-UNIFORM exact counting algorithm for any explicitly tabulated binary CSP on v variables, Q>=2, with time L^{p_Δ} Q^{C_Δ v/sqrt(log v)}; all constants independent of Q.
- OpenAI, *The Exponential Time Hypothesis is False*, October 25, 2026, complete tensor Theorem D.1: https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex . The separately advertised fixed-width-CNF Lean scope does not explicitly include this full theorem.
- Existing notes [34: closure registry](34_csp_hypothesis_closure_registry_2026_11_02.md), [34: surviving single-exponential hypothesis](34_tensor_theorem_primary_source_audit_and_surviving_single_exp.md), [33: Boolean tensor encoding](33_tensor_contraction_sparse_2csp_and_hardness_triage.md), and [18: randomized PCP sampling](18_randomized_low_soundness_pcp_to_linear_csp.md). The degree-cloning observation is ALREADY recorded in note 34 and is repeated here only as a lemma for the extensions below.

## B. Any degree, any q, fixed-arity CSP (conditional exact counting)

**Lemma (binary degree splitting; elementary).** For any binary CSP Γ with v variables, m constraints and maximum common domain size q, replace each occurrence of original variable x in a constraint by a separate copy x_{e}; link the copies for that original variable by binary equality constraints along a path. Keep at least one copy for an isolated variable and its admissible-domain restriction. The output has v'=O(v+m) variables and m'=O(v+m) constraints, degree<=3, the SAME alphabet q, and **exactly one extension per original solution**. The output explicit tabular representation has size polynomial in the input explicit table length L (at most O((v+m)q²)). The Nguyen algorithm therefore gives, for q>=2,
    #SAT(Γ) in time poly(L) · q^{O((v+m)/sqrt(log(v+m)))}
when v+m is sufficiently large; finite cases are brute-forced. When m=O(v), this is poly(L) q^{O(v/sqrt(log v))} for arbitrary q, not merely polynomial q.

**Corollary (fixed arity r).** Let Γ be an arbitrary fixed-arity r CSP, with v variables, m constraints, each table explicit and domains <=q; r is fixed. Introduce for every r'<=r-ary constraint e one auxiliary tuple variable t_e with its allowed states being exactly the tuples satisfying R_e (or with full q^{r'} tuple domain and an explicit unary restriction). Connect its jth port by a projection/equality relation to the original variable at that position. Split each high-degree original and tuple variable into incidence copies using equality paths. Each original solution has exactly ONE extension: the tuple t_e is forced by the values on its ports. The resulting binary CSP has v'=O(v+rm), maximum degree 3, and uniform domain Q<=q^r (typed states/validity allowed), with polynomial description blowup for FIXED r and COMPLETE TABLE input. Hence under Nguyen:
    T_r(v,m,q,L) = poly_r(L) · q^{O_r((v+m)/sqrt(log(v+m)))} .
For m=O(v): poly_r(L) q^{O_r(v/sqrt(log v))}.
Do NOT automatically apply this complete-table parameterization to huge implicitly represented or sparse tuple-list constraints when writing q^r symbols would exceed the original input length. Alternative support-pruned encodings need separate input-size accounting.

**Corollary (HOM).** For any sparse source G with |V(G)|=v and |E(G)|=O(v), and any target H with q=|V(H)|>=2, the number of homomorphisms is computable, conditional on Nguyen, in poly(|G|+|H|) q^{O(v/sqrt(log v))} time. This is domain-UNIFORM, independent of degen(H), and has no asserted polynomial-space bound. With q=v^{Theta(1)}, the exponent in powers of 2 is O(v sqrt(log v)), NOT O(v).

**Corollary (cyclomatic-number decision parameter).** For an arbitrary binary CSP, define μ=m-v+cc(G) for its simple primal graph (after parallel constraints are intersected). The independently proved degree<=2 existential variable elimination in [13](13_binary_csp_cyclomatic_reduction.md) either decides NO or produces a satisfiability-equivalent 3-core on v'<=2μ variables and m'<=3μ constraints, still over q; it does NOT preserve #SAT. Split high-degree variables in this core to degree 3, obtaining O(μ) output variables. Thus, for μ>=2,
    T_DECISION(Γ) = poly(L) · q^{O(μ/sqrt(log μ))}
under Nguyen (for μ=0,1 handle directly in polynomial time). **Do not present this as exact counting:** forgetting a degree-2 variable can alter multiplicities. Example: an unconstrained q-element middle variable in a 3-vertex path contributes an extra factor q after existential elimination.

## C. Quantitative domain-size phase diagram

For m=O(v), write q=exp((log v)^α) with fixed α>=0 (constant factors may be included). Then Nguyen gives
    log T = O(v (log v)^{α-1/2}) + polylog(L).
Therefore:
- α<1/2: 2^{o(v)} up to the polynomial input factor;
- α=1/2: 2^{O(v)} up to the polynomial input factor;
- α>1/2: this theorem's displayed bound is super-single-exponential, but faster algorithms are NOT excluded;
- q=v^c corresponds to α=1 and gives 2^{O(v sqrt(log v))}.

Thus the first remaining open algorithmic question for **polynomial alphabet** is improving the exponent from v sqrt(log v) to O(v); equivalently achieving q^{O(v/log v)} for q=v^Theta(1). The domain-uniform theorem already gives single exponential for much smaller subpolynomial alphabets, namely q<=exp(O(sqrt(log v))).

**Restricted wire-budget obstruction:** The straightforward Boolean 0/1 tensorization with one distinct Boolean wire configuration per satisfying assignment of the edgeless q-domain CSP needs >=v log_2 q bit wires, since there are q^v distinct satisfying assignments and at most 2^M wire configurations. For q=v^c, this is Ω(v log v). To guarantee 2^{O(v)} merely by applying the currently stated full Boolean tensor upper bound 2^{O(M/sqrt(log M))}, one would need a network of M=O(v sqrt(log v)) wires. This is impossible in that exact witness-injective, 0/1, no-arithmetic-weight tensorization model. This is NOT a lower bound on algorithms, on weighted networks, or on existential decision-only compilers; it only says naive bit-blasting plus the **existing bound** cannot certify 2^{O(v)} for polynomial q.

## D. Critical PCC compression window (proved conditional implications)

Define RPCC-H as: no bounded-error randomized 2^{o(K log K)} poly(K)-time algorithm solves arbitrary K-by-K **Permutation Clique**. This is a working HYPOTHESIS separate from PSCH and not established by the post-ETH literature.

Assume a randomized one-sided-error, polynomial-time reduction R maps every PCC(K) to a degree<=3 explicit binary CSP with
    v_K=O(K (log K)^β), m_K=O(v_K), Q_K=K^{O(1)}.
The reduction has constant (e.g. >=2/3) soundness on NO and perfect completeness on YES. The CSP solver is deterministic, so composition has bounded error. Nguyen gives
    log T_PCC = O( v_K log K /sqrt(log(v_K+2)) )+O(log K)
             = O(K (log K)^{β+1/2})
for v_K of near-linear order; smaller v_K only improve the bound.

**If β<1/2**, the composite runs in 2^{o(K log K)}, contradicting RPCC-H. If β=1/2, the composite upper bound is 2^{O(K log K)} and is consistent.

Conversely, **if β<1**, any hypothetical CSP algorithm with time 2^{O(v)} poly(L) on *all* degree-3 polynomial-alphabet CSPs would give a 2^{O(K (log K)^β)}=2^{o(K log K)} PCC algorithm, again contradicting RPCC-H.

Hence under both hypotheses the viable target for a new single-exponential hardness transfer is
    1/2 <= β < 1.
At the boundary β=1/2, R would transfer RPCC-H into a tight conditional no-2^{o(v sqrt(log v))} lower bound for the resulting class of CSPs, exactly matching Nguyen's claimed 2^{O(v sqrt(log v))} upper exponent. This is a *conditional sharpness mechanism*, not an established lower bound, as the reduction R is OPEN.

More generally, if β+γ<1, R+RPCC-H prohibit an algorithm 2^{O(v(log v)^γ)} poly(L) for all targets. In particular γ=0 is the desired no-single-exponential statement.

For the weaker **PSCH** (ordinary k-Clique on <=k² vertices, no 2^{o(k/log k)} deterministic algorithm), the same implications do NOT follow: a 2^{O(k sqrt(log k))} algorithm is far slower than the threshold excluded by PSCH. **Do not interchange RPCC-H and PSCH.**

## E. The matching PCP soundness threshold

Assume a uniformly constructible, **nonadaptive, two-query** PCP for every PCC(K) with:
- ℓ<=aK proof positions, alphabet Q<=K^b;
- perfect completeness (one YES proof passes every supported test);
- NO soundness s(K), each test binary/unary, samplable in poly(K) time with explicit relation table available in poly(K) time.

From the elementary independent sampling lemma in [18](18_randomized_low_soundness_pcp_to_linear_csp.md), sampling
    t=O((ℓ log Q + 1)/log(1/s(K)))
tests and replacing high proof-degree by chains of equality yields a randomized one-sided reduction to degree-3 CSP with v',m'=O(ℓ+t), q'=poly(K).

Therefore:
- soundness exp(-Θ((log K)^a)), 0<a<1, gives t=O(K (log K)^{1-a});
- at a=1/2, the output size is O(K sqrt(log K)), precisely the Nguyen/RPCC critical boundary;
- if log(1/s(K))=ω(sqrt(log K)), output size is o(K sqrt(log K)), violating RPCC-H under Nguyen;
- in particular a proof of inverse-polynomial soundness s=K^{-Ω(1)} with ℓ=O(K), Q=poly(K) would IMPLY a 2^{o(K log K)} randomized algorithm for PCC under Nguyen, so it cannot coexist with RPCC-H.

This is a conditional **PCP no-go** with a concrete quantitative threshold, not a statement that standard PCP theorems fail. Existing PCP constructions must be audited against the unusually short O(K)-symbol, poly(K)-alphabet witness requirement and efficient per-test tables. A PCP with s=exp(-Θ(sqrt(log K))) would be an attractive *critical construction*, if it exists.

## F. Research directions after closure of SPACH/CEH

1. **Algorithmic route:** improve Nguyen's q^{O(v/sqrt(log v))} to q^{O(v/log v)} for polynomial q, i.e. 2^{O(v)}. A pure repackaging of the standard Boolean bit-wire encoding cannot yield this from the unchanged tensor contraction theorem's exponent. New contraction/aggregation or non-injective algebraic witnesses are required.
2. **Hardness route:** prove/justify RPCC-H and design a PCC->sparse CSP compiler with output K(log K)^β for 1/2<=β<1. The critical β=1/2 may exactly match the new upper exponent.
3. **PCP route:** target ℓ=O(K), Q=poly(K), soundness exp(-Θ(sqrt(log K))) with efficient test generation, rather than prematurely aiming for K^{-Ω(1)} which is incompatible with RPCC-H + Nguyen.
4. **HOM route:** to obtain a no-2^{O(|G|)} lower bound for 2-degenerate polynomial-size targets, additionally prove a CSP->HOM reduction with pattern size O(v), polynomial target size and degen(H)<=2. This is a separate nontrivial step; do not assume that eliminating lists preserves degeneracy or size.

**No claim made:** a new proof of the tensor theorem, a universal dense Clique compiler, a new general 2^{O(v)} algorithm, or an unconditional sparse CSP lower bound.
