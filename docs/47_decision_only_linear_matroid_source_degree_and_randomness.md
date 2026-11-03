# Checkpoint 47 — A sharp algebraic-degree barrier for deterministic decision-only PCC→linear-matroid compilers

**Date:** 2026-11-03. **Branch:** PCC/PSCH, determinant-compatible decision-only input compilers.
**Status:** Elementary, **PROVED and quantitatively sharp** lower bound for a restricted deterministic/zero-false-positive source-polynomial model, together with an explicit bounded-error randomized affine counterexample outside that model. NO unconditional lower bound for arbitrary polynomial-time preprocessing or ordinary randomized PCC reductions; NO generic PCC algorithm and NO critical sparse 2-CSP compiler. Related checkpoints [45](45_pcc_ingleton_fieldsize_and_gf7_edge_gadget.md), [46](46_pcc_all_fields_zero_pattern_nonrepresentability.md), [20](20_two_layer_affine_nonlinear_pcc_audit.md). Priority novelty NOT independently checked; the Boolean degree of AND is classical.

## 1. Source input cube: exactly one possible original clique

For K>=2 let M=binom(K,2). Consider the explicitly defined family of PCC graphs A(z), z∈{0,1}^M: each candidate position other than the K diagonal positions (i,i) is isolated. Between diagonal candidates (i,i) and (j,j), put an edge iff z_{ij}=1. Every nonidentity permutation differs from the identity in >=2 positions, hence selects two isolated candidates and is not a clique (when K=2 these two candidates are distinct and have no edge). Thus

    PCC(A(z))=YES  iff  z=1^M.

The unique possible original witness on YES is identity. A compiler is **NOT** required to preserve this witness or its labels in any way.

## 2. Formal model and main lower bound

Fix ONE common field F (of arbitrary characteristic and size). A deterministic source-polynomial compiler maps A(z) to N output row positions and N output column positions, together with r>=1 explicitly represented linear matroid independence layers. The layer h has a vector
    v^{(h)}_{i,a}(z)∈F^{d_h}
for every candidate output position (i,a), and EVERY coordinate of EVERY output vector is the restriction to {0,1}^M of some polynomial in the source bits z_e of total degree ≤D. The output field and the labeled matching universe [N]×[N] are FIXED throughout the input cube (they may depend on K but not on z).

The output predicate is:
    exists sigma∈S_N such that for every layer h=1,...,r,
       {v^{(h)}_{i,sigma(i)}(z):i∈[N]} is linearly independent.
There is NO condition connecting sigma with the original identity permutation: **decision-only**, not solution-preserving. Input-dependent disallowed output positions may be implemented by making their vector zero, provided the resulting coordinates satisfy the same degree D promise.

**THEOREM.** If this output predicate equals PCC(A(z)) on EVERY z∈{0,1}^M, then
    r·N·D >= M = binom(K,2).

**Proof.** At z*=1^M the output is YES. Choose one accepting output permutation sigma*, possibly completely unrelated to the original identity. For each layer h, the d_h×N matrix formed by the selected vectors has rank N; select a nonzero N×N minor f_h(z*)≠0. Its determinant f_h(z) is a polynomial of degree ≤ND, regardless of ambient dimension d_h. The product
    F(z)=∏_{h=1}^r f_h(z)
has degree ≤rND and is nonzero at z*. At every z≠z*, the source is NO, so sigma* cannot be simultaneously independent across all layers, hence at least one f_h(z)=0 and F(z)=0. Thus F restricted to the Boolean cube is supported ONLY on 1^M and equals c·AND_M(z) with c=F(1^M)≠0.

Every polynomial over EVERY field has a unique multilinear representative on {0,1}^M modulo z_e²−z_e; multilinearization cannot increase total degree. The unique multilinear representative of c·AND_M is c∏_e z_e, of degree exactly M. Therefore rND>=M. QED.

**Consequences:**
- With r=O(1), N=O(K), need D=Omega(K).
- With r=O(1), N=O(Ksqrt(log K)), need D=Omega(K/sqrt(log K)).
- With AFFINE/linear source-dependent vector coordinates D=1 and r=O(1), need N=Omega(K²), so a uniform O(K) / O(Ksqrt(log K)) decision-only reduction of this affine form is impossible.
- If all vector-entry arithmetic circuits have source-bit multiplication depth t, degree ≤2^t (input variables degree one; additions and scalar multiplications do not raise degree), so
      t >= log_2(M/(rN))
  whenever the ratio >1.
- Theorem says nothing when output entry functions may have polynomial-time computable but HIGH algebraic degree (the AND of all M bits itself has a polynomial-size circuit). It says nothing about input-dependent field changes, unrestricted nonlinear decisions, or general algorithms. A trivial source scanner can decide the special cube in O(K²) time.

**r-matroid composition interpretation:** A constant number of F_7 determinant layers assembled by merely AFFINE source dependence cannot encode arbitrary PCC satisfiability at O(K) matching size, even if the accepted output permutation may change. To escape the lower bound, one must increase r, N, or source degree D. The r=1 single-forbidden-edge gadget in [45](45_pcc_ingleton_fieldsize_and_gf7_edge_gadget.md) is not in tension because it only handles one variable forbidden predicate.

## 3. Sharpness (for this source cube)

The lower bound is EXACT up to ceiling. Partition all M edge-bit indices into rN groups E_{h,i}, with each group of size at most
    D=ceil(M/(rN)).
For every h, output row i and column i, define
    v^{(h)}_{i,i}(z) = e_i · ∏_{e∈E_{h,i}} z_e ∈F^N.
Let every off-diagonal candidate output vector be the zero vector. The only possible independent output perfect matching is identity. It is independent in every matroid layer iff ALL group products are nonzero, which over {0,1}^M is equivalent to all M input bits being one.

Each vector coordinate has total degree ≤ceil(M/(rN)), achieving equality asymptotically in the inequality rND≥M. The required vector values are computable in O(M) arithmetic operations. This construction only solves the deliberately easy one-clique cube, not arbitrary PCC; it proves that no *stronger* lower bound in terms of r,N,D can follow from this promise family alone.

The accompanying small Python test enumerates all source inputs for K=2,...,5 (taking r=2,N=K) and verifies this exact group-product predicate.

## 4. Randomized affine sketch escapes the deterministic degree bound

Crucial quantifier issue: with ordinary bounded-error randomization, a low-degree compiler CAN solve the same special source cube with **r=1, N=K, D=1**.

Work over F_2. Independently sample two uniform random masks R,S∈F_2^M. Let b_e=1−z_e and
    L_R(z)=1+Σ_e R_e b_e mod 2,
    L_S(z)=1+Σ_e S_e b_e mod 2.
Return a rank-K explicitly represented linear matroid on output candidates, with:
    v_{1,1}(z)=L_R(z)e_1,
    v_{2,2}(z)=L_S(z)e_2,
    v_{i,i}(z)=e_i for i=3,...,K,
    v_{i,a}(z)=0 for a≠i.
Every selected vector coordinate has source degree ≤1.

For z=1^M, both L_R,L_S=1 and the output has an independent perfect matching for EVERY seed (perfect completeness). For any NO input z with b≠0, the independent uniform parities R·b,S·b are each unbiased, so the output mistakenly accepts with probability exactly 1/4 and otherwise rejects. Hence a 3/4-sound randomized one-sided-YES-preserving, decision-only affine compiler exists on this *easy source cube*.

This does NOT provide an affine decision-only compressor for ALL PCC inputs: on a general graph a seed can be chosen BEFORE the existential output witness, so one must bound false acceptance uniformly over all possible witnesses. The special family has effectively only one original candidate and allows a fixed-output-matching sketch, so no large union bound is needed. Therefore the deterministic degree lower bound MUST NOT be extrapolated to ordinary randomized reductions.

Sanity check: for K=2,3,4, exact enumeration over all 2^{2M} pairs of random masks and every NO input confirms 1/4 false-acceptance probability. For K=5, the probability follows algebraically from uniform independent parities. Code: [experiments/47_decision_only_linear_degree_sanity.py](../experiments/47_decision_only_linear_degree_sanity.py).

## 5. A robust source-sensitivity statement (also for randomized compilers)

The following qualitative barrier DOES survive randomization, but needs a fixed interpretation of output vector positions and a fixed output field across source input changes.

Suppose a randomized compiler of the above matching-plus-r-matroid type has perfect YES completeness: for every random seed rho, A(1^M) outputs YES. Suppose on EVERY NO input A(z), in particular on each single-deletion neighbor A(1^M−e), its output is NO with probability at least 2/3.

For each seed rho choose any accepting output permutation sigma_rho on the all-ones YES input. Let U_{rho,h,i}(z) be the selected vector v^{(h)}_{i,sigma_rho(i)}(z), and let Sens_{rho,h,i} be the set of source bit indices e such that
    U_{rho,h,i}(1^M) != U_{rho,h,i}(1^M−e).

If for some e none of the rN selected vectors changed, the SAME sigma_rho would remain independent after deleting that source edge, causing a false positive. Hence for every e,
    Pr_rho[e belongs to union_{h,i} Sens_{rho,h,i}] >= 2/3.
Summing over all M source edges,
    E_rho |union_{h,i} Sens_{rho,h,i}| >= (2/3) M,
and by averaging, for some seed rho and selected output vector (h,i),
    |Sens_{rho,h,i}| >= 2M/(3rN).

This necessary GLOBAL SENSITIVITY holds even when the vector-entry functions are arbitrary polynomial-time algorithms, not low-degree polynomials. But sensitivity is not a time-complexity lower bound: a vector can depend on many source edge bits and still be computed in polynomial time. The random affine sketch of Section 4 actually has source sensitivity on every edge with probability 3/4, illustrating how low algebraic degree can coexist with massive global source dependence.

The hypothesis that the representation field and output coordinate system remain meaningful across deletion neighbors is necessary. If a compiler changes field, matching universe or auxiliary metadata between inputs, one must charge that change as part of the output data rather than compare vectors naively.

## 6. Research verdict

A mathematically sharp **decision-only** lower bound now exists for one narrow but concrete architecture: polynomial-in-source-bit vector entries of uniformly bounded degree. It quantitatively rules out constant-layer affine/low-degree compositions of the GF(7) local determinant gadget at near-linear matching size, *without any demand to preserve individual solutions*. The gap between deterministic and randomized compilers is genuine and witnessed by a two-parity affine construction on the unique-original-matching family.

Still OPEN: a general polynomial-time, possibly randomized PCC→explicit linear-matroid independent-perfect-matching reduction with N=O(K) (or N=o(Klog K)) and arbitrary nonlinear preprocessing, preserving only YES/NO; the desired 2^{O(K)} algorithm would follow from [43](43_matroid_factor_matching_deterministic_2exp.md). The finite/all-fields *solution-preserving* no-go in [46](46_pcc_all_fields_zero_pattern_nonrepresentability.md) does not settle it.

**External mathematical ingredients:** only the classical uniqueness of multilinear representatives of functions on the Boolean cube and basic linear-algebraic rank/determinant facts; the result is an elementary polynomial-method observation, NOT a claim of an unconditionally novel theorem.
