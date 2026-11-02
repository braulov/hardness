# Two-layer PCC compiler audit: affine consistency, nonlinear information capacity, and high-treewidth interface

**CRITICAL 2026-11-02 UPDATE:** See [the domain-uniform CSP alert](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md). A brand-new UNVERIFIED independent preprint claims a uniform q^{O(v/sqrt(log v))} deterministic algorithm for ALL bounded-degree binary CSPs. **If correct, SPACH/rSPACH as formulated here are FALSE**, and under RPCC-H no O(k)-size (indeed no o(k sqrt(log k))-size) general polynomial-alphabet bounded-degree CSP compiler exists. All earlier PCP/encoding lemmas should be viewed through this conditional algorithmic upper bound; don't present a purported compiler as SPACH evidence.


**2026-11-02. Status:** self-contained elementary proved lemmas, a quantified restricted-model obstruction, and a concrete OPEN compiler interface. Randomized algorithms and reductions are fully permitted. No generic Permutation Clique -> O(k)-constraint 2-CSP compiler is claimed. This iteration follows notes 14, 18, 19 and the existing PSCH checkpoint; avoid overstating originality.

## A. Two-layer target and parameter ledger

Input: an arbitrary k x k Permutation Clique instance with binary compatibility tables A_ij(a,b), i<j, a,b in [k]. A witness is a permutation pi with all A_ij(pi(i),pi(j))=1.

Seek a randomized polynomial-time construction with one-sided decision correctness producing at most Ck variables and Ck binary constraints, max degree <=3, and a common domain Q=k^{O(1)}. Algebraic consistency checks may be input-independent; the input-dependent nonlinear checks may use explicit Q x Q relation tables with polynomial preprocessing. Aim to separate:

- C: an input-independent consistency/coding layer encoding k field symbols (or O(k log k) Boolean bits) by O(k) polynomial-alphabet proof symbols, ideally constant relative distance and robust testability;
- N_A: O(k) nonlinear relations depending arbitrarily on the input A;
- a coupling mechanism guaranteeing NO even after existentially choosing *all* proof and auxiliary symbols. Per-fixed-witness randomized soundness is insufficient; any sampling must hold simultaneously over all witnesses (as in docs/18).

The direct binary CSP -> CNF encoding still gives n_SAT=O(k log k), width O(log k), poly(k) clauses IF the linear compiler is obtained; this direct SAT reduction is not itself the novelty.

## B. Two-query affine consistency cannot give a positive-rate, positive-distance linear code (PROVED)

Let C subset F_p^ell be a nonempty affine solution set of equations alpha z_u+beta z_v=gamma involving at most two coordinates, plus optional unary equations. Form the graph of constraints with alpha*beta !=0. Each connected component has affine dimension at most one: choosing the root value fixes every other coordinate, while cycle consistency may fix the root or rule out solutions. Therefore if dim(C)>=k, there are >=k free components. Since total ell<=C_0 k, some free component has size at most C_0. Varying only its root value gives two distinct solutions at Hamming distance at most C_0, and hence

    d_min(C)<=ell/k=O(1).

Consequently, this cannot produce a constant-rate and constant-relative-distance linear code for k independent field symbols. This is a special exact-consistency statement, NOT a prohibition on:
(i) nonlinear two-query checks,
(ii) constant-arity 3+ linear checks subsequently compiled to binary CSP,
(iii) arbitrary decision-preserving PCC reductions,
(iv) distance of a nonlinear *subset* of the solution space rather than the full affine code.

Relevant literature: Kol--Raz, *Bounds on 2-query Locally Testable Codes with affine tests* (Information Processing Letters, 2016), https://doi.org/10.1016/j.ipl.2016.03.008. Our graph argument is elementary for exact affine constraints and does not claim the full strength of their LTC theorem.

## C. A useful positive subroutine: 3-ary linear parity checks -> cubic binary CSP with O(t) constraints (PROVED)

Suppose a proposed code is described by ell=O(k) F_p symbols and t=O(k) linear equations, each involving at most 3 symbols. For each equation a x+b y+c z=d create an auxiliary variable g ranging over the allowed triples of F_p^3, domain at most p^3. Connect g to x,y,z via three binary equality/projection relations. If an original symbol appears in d constraints, split it into d occurrence copies arranged along an equality path, connecting one occurrence to each check; the degree is at most 3 and the number of vertices/equalities is O(ell+t). All predicates have polynomial explicit tables when p=k^{O(1)}. Thus

    v,m=O(k), max degree <=3, Q<=p^3=k^{O(1)}.

This exact compilation is readily available and NOT the missing lemma. The missing part is a suitable robust code *and* a nonlinear predicate whose checks certify arbitrary PCC compatibility at the same linear size. LDPC distance alone does not give local testability or amplify the error in one forbidden pair.

Relevant coding reference: Dinur--Evra--Livne--Lubotzky--Mozes, *Good Locally Testable Codes*, Annals of Mathematics 203 (2026), https://annals.math.princeton.edu/2026/203-2/p03 . It proves existence of constant-rate, constant-distance, constant-query LTCs; it DOES NOT automatically provide a 3-query affine realization nor the k-ary grouping/2-CSP parameters wanted here.

## D. Counting theorem for genuine *permutation*-solution sets (PROVED; solution-preserving model)

Let k=2s. Partition rows into regular rows R=[s] and filler rows F=[s+1,2s]; columns into default D=[s] and active U=[s+1,2s]. For each pair i<j in R and each ordered pair of *distinct* active values a,b in U, freely choose an input bit B_ij(a,b) indicating whether the selected pair is forbidden. All remaining cross-row compatibility entries are 1. There are

    M=binom(s,2)*s*(s-1)=Theta(k^4)

independent bits.

**Injectivity claim.** For every i<j and a!=b in U, choose a permutation pi assigning a to i and b to j, assigning every regular row r!=i,j its default column r, and mapping filler rows bijectively onto the remaining s unused columns. In this pi, the ONLY arbitrary compatibility predicate that is activated is B_ij(a,b). Therefore its membership in the satisfying-permutation set S_B exactly reveals this bit. Thus B->S_B is injective, and the family has 2^{Theta(k^4)} distinct sets S_B subset S_k.

Suppose for EVERY input B a compiler outputs a cubic 2-CSP with:
- at most ell=O(k) variables, at most m=O(k) constraints, alphabet [Q], with Q>=k;
- a fixed input-INDEPENDENT decoder Dec:[Q]^ell -> S_k (or partial decoder), such that the set of satisfying decoded permutations is EXACTLY S_B;
- at most t of the explicit binary relation tables are input-dependent; the rest, including the affine/coding layer, are fixed. Unary input-dependent tables and input-dependent scalar affine coefficients are permitted provided their descriptions total O(kQ+k log k) bits; any variable/constraint wiring contributes O(k log k) bits.

The total number of distinct possible outputs is at most

    2^{ t Q^2 + O(kQ+k log k) },

ignoring harmless constant factors and domain-type conventions. Since distinct S_B require distinct output CSP descriptions (given a fixed decoder),

    t Q^2 + O(kQ+k log k) = Omega(k^4).

In the usual regime Q=k^{O(1)} and t=O(k), this forces Q=Omega(k^{3/2}) up to constant factors (the O(kQ) unary term cannot match k^4 for Q=o(k^{3/2})). In particular an O(k)-test exact projection compiler with Q=O(k) is impossible in this model, even if randomized: for each B with positive probability of an exact output there must be a DISTINCT suitable output description.

**Crucial limitations.** This is NOT a lower bound on decision-only (YES/NO) polynomial-time or randomized reductions: different B may have different satisfying-permutation sets but the same satisfiability status. Also it does NOT hold if the decoder or other uncharged input-dependent auxiliary artifact can encode Theta(k^4) input bits; all encoded information must be charged. The count is an information-capacity lower bound, not a constructive compiler at Q=k^{3/2}.

**Connection to the existing checkpoint:** the PSCH archive already contains a similar 2^{Theta(k^4)} counting argument for independent k-colored Clique choices using a default label. The result here adapts the injection to *genuine permutations* through filler rows and states the two-layer nonlinear-table / alphabet tradeoff explicitly.

## E. Input-sensitivity stress test for robust PCP soundness (elementary, revisiting PSCH checkpoint)

Let I_0 be a PCC input with a unique satisfying permutation pi_0: only the k vertices (i,pi_0(i)) are mutually adjacent, all other candidates are isolated. For any of the M=binom(k,2) edges e of the unique clique, delete e to get a NO instance I_e.

Assume a perfectly complete nonadaptive verifier has a proof P_0 accepted on I_0 for every test, and each NO I_e rejects that SAME proof on at least a constant delta fraction of its test seeds. Couple seeds across I_0 and I_e, and write Sens(t)={e: test t's acceptance on P_0 differs between I_0 and I_e}. Summing over e gives

    E_t |Sens(t)| >= delta M = Omega(k^2).

Thus a constant-gap proof verifier must have tests with **global sensitivity to Omega(k^2) distinct input edges on average**, in this adversarial family. In a strict original-edge oracle model where a test reads at most b edge bits, b>=delta M. With arbitrary input-dependent preprocessing of each large Q x Q relation table, this is NOT impossible: a table entry may depend on many edges. The lemma is another explicit reason the nonlinear layer must be genuinely global, not direct subsampling of source pair checks.

This is a refinement/recall of a similar sensitivity audit already in docs/psch/2026-11-02_full_checkpoint_v7.md. Do not claim priority.

## F. High-treewidth necessity under randomized PCC hardness (CONDITIONAL, PROVED IMPLICATION)

Assume RPCC-H: no bounded-error randomized 2^{o(k log k)} poly(k) algorithm for arbitrary PCC(k). Suppose a randomized polynomial-time reduction outputs cubic binary CSP with ell=O(k) variables and Q=k^{O(1)} alphabet and has one-sided bounded-error correctness.

If ALL output constraint graphs had treewidth w(k)=o(k), use a 2^{O(w)}poly(ell) constant-factor treewidth decomposition algorithm (Bodlaender et al., SIAM J. Comput. 2016) then standard CSP treewidth dynamic programming in Q^{O(w)}poly(input). This would give a bounded-error randomized 2^{o(k log k)}poly(k) algorithm for PCC, contradiction. Thus no such universal reduction can have worst-case treewidth o(k); some outputs must have treewidth Omega(k) infinitely often. Cubic expander-like topology is consistent with this necessity but not sufficient to build the nonlinear interface.

Reference: Bodlaender et al., *A c^k n 5-Approximation Algorithm for Treewidth*, https://doi.org/10.1137/130947374 .

## G. Program evaluation / narrow next experiment

The missing statement is precisely:

    [linearly many, polynomial-alphabet proof coordinates]
      + [constant-query genuinely robust consistency checks]
      + [O(k) input-preprocessed, globally sensitive nonlinear pair tables]
      -> [every NO proof fails, YES has a passing proof].

There is currently no construction for arbitrary PCC. The consistency layer and coding gadgets are not the missing key by themselves; every genuine permutation of an invalid clique still has a perfectly consistent codeword. One must *amplify global input incompatibility*, not merely code distance.

A new constructive experiment should formalize an input-dependent 'global adjacency interface' for permutation codewords. Its local predicates MUST: (i) aggregate Omega(k^2) source-edge sensitivities, (ii) have Q=Omega(k^{3/2}) if all permutation solutions are exactly preserved with t=O(k), and (iii) be embedded in a topology with linear treewidth if the RPCC-H source is genuinely hard. The decision-only randomized version may circumvent condition (ii), but still must prove simultaneous soundness against existentially chosen proofs. All claims are OPEN until an explicit verifier is built.

Potential alternative to 2-query affine codes: arity-3+ parity checks compiled to binary CSP via gate states as in Section C; c^3 locally testable codes or high-dimensional-expander-based PCPs are relevant sources, but no ready-made linear-size compiler follows.

## Fixed-encoding barrier strengthened to quadratic (2026-11-02)

See [`21_oblivious_two_query_pcc_quadratic_barrier_and_2026_ltc.md`](21_oblivious_two_query_pcc_quadratic_barrier_and_2026_ltc.md). For ANY fixed encoding E:S_k->[k^C]^ell and t fixed two-coordinate proof tests whose **relation tables may depend on the whole input graph**, exact per-permutation validity on all PCC inputs requires t=Omega_C(k²). Single-deleted source edges force some two-symbol view to reveal both selected rows/columns; a two-symbol view fixes only O(C) permutation entries on average. Randomized exact-solution-preserving versions obey the same bound. This is strictly stronger than the table-bit counting bound for this **narrower oblivious model**. It does NOT rule out input-adaptive proof encodings, existential auxiliaries, input-adaptive test positions, or decision-only randomized compilation. First–Lazarovici APPROX/RANDOM 2026 good two-query LTCs remove the old nonlinear-code concern but do not break this fixed-encoding obstruction.
