# Randomized exact sparsification from low-soundness, two-query PCPs

**CRITICAL 2026-11-02 UPDATE:** See [the domain-uniform CSP alert](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md). A brand-new UNVERIFIED independent preprint claims a uniform q^{O(v/sqrt(log v))} deterministic algorithm for ALL bounded-degree binary CSPs. **If correct, SPACH/rSPACH as formulated here are FALSE**, and under RPCC-H no O(k)-size (indeed no o(k sqrt(log k))-size) general polynomial-alphabet bounded-degree CSP compiler exists. All earlier PCP/encoding lemmas should be viewed through this conditional algorithmic upper bound; don't present a purported compiler as SPACH evidence.


**Research iteration 2026-11-02. Status:** elementary sampling theorem proved below; existence of the required PCP for arbitrary Permutation Clique is OPEN. Focus on randomized algorithms and reductions as first-class outcomes. This is a quantitative refinement of docs/17_pcp_bridge_gap_sampling_and_logsat.md and its predecessor, not a claim to have solved generic dense-to-sparse CSP compression.

## 1. Hypothesis bookkeeping: randomized is acceptable

Write PCC(k) for k-by-k Permutation Clique. The *randomized PCC hardness candidate* (RPCC-H) states: no uniform bounded-error randomized algorithm solves all PCC(k) instances in 2^{o(k log k)} poly(k) time. Separate it carefully from:
- the deterministic candidate with the same time barrier;
- PSCH (ordinary k-Clique on <=k^2 vertices, with the much weaker 2^{o(k/log k)} exponent), neither known to imply RPCC-H;
- the historical ETH-dependent 2^{o(k log k)} theorem, which cannot serve as an unconditional hypothesis replacement if ETH is false.

Similarly **rSPACH**: for some fixed c>=1, max-degree-3 binary CSP with v variables, q=ceil(v^c), and m=Theta(v) has no uniform bounded-error randomized algorithm in 2^{o(v log v)} poly(input length) time. This is *stronger as an algorithm-exclusion statement* than deterministic SPACH, not automatically implied by it.

A randomized reduction with one-sided completeness and >=2/3 NO-rejection composed with a bounded-error randomized solver gives a bounded-error randomized PCC solver after standard repetition/amplification. Thus proving rSPACH from RPCC-H requires precisely a suitably parameter-preserving randomized reduction.

## 2. Main sampling theorem: inverse-polynomial soundness removes the log factor (PROVED)

Let x be a given input of parameter k. Suppose a uniformly/polynomially explicitly constructible **nonadaptive, two-query** proof test system has:
- l<=a k proof positions, each with alphabet size Q<=k^b;
- an efficiently samplable distribution D_x on tests; each sampled test queries <=2 predetermined proof positions and applies an explicit relation table R_t subset [Q]^2, computable in poly(k) time, possibly depending on all of x;
- **perfect completeness in the strong same-proof sense**: if x is YES, one proof P passes every test with nonzero sampling probability;
- **NO soundness <=s(k)**: if x is NO, every proof P satisfies Pr_{t~D_x}[test_t accepts P] <= s(k);
- polynomial preprocessing and test predicate generation, including any input-dependent lookup tables.

Sample t independent tests from D_x and create the 2-CSP requiring all sampled tests. For each fixed proof P on a NO instance, P[all t sampled tests accept] <= s(k)^t. There are <=Q^l proofs, hence

    P[there EXISTS a proof passing all sampled tests | x NO]
      <= Q^l s(k)^t.

So choosing

    t >= (l log Q + log(1/eta))/log(1/s(k))

makes the resulting CSP UNSAT with probability >=1-eta; for YES every sample is SAT. Finally clone variables for occurrences and connect occurrence copies by equality paths; there are O(t+l) variables and constraints, max degree <=3 (unary relation normalization as needed), common alphabet Q or Q^{O(1)} and polynomial size. This is a **randomized, one-sided, exact decision reduction** with high-probability soundness. Adaptive/interactive challenges cannot be replaced by samples without separate nonadaptivity/binding proofs.

Quantitative corollaries for l=Theta(k), Q=k^{Theta(1)}:
- constant s<1 => t=Theta(k log k);
- s=k^{-gamma}, any fixed gamma>0 => t=Theta(k), so **an O(k)-variable, O(k)-constraint, degree-3, polynomial-alphabet CSP compiler**;
- s=exp(-(log k)^alpha), 0<alpha<1 => t=Theta(k (log k)^{1-alpha});
- more generally t=Theta(k log k/log(1/s)).

Use O(k) in the second line as an upper bound; matching lower bounds for every system are NOT claimed.

**Crucial:** the alphabet Q=k^b and proof length O(k) must be parameters relative to PCC witness length k log k, NOT relative to the k^4-bit adjacency input or the Theta(k^2) adjacency verification circuit. This is the main currently missing construction.

## 3. Precise lower limit for two-query PCP soundness (PROVED under a nonempty-test promise)

Assume every sampled binary test on two distinct proof coordinates has at least one accepting ordered pair, and every unary test has at least one accepting value. A uniformly independently random proof over [Q]^l passes each binary test with probability at least 1/Q^2 (unary >=1/Q). By averaging, **for any input, including NO**, there exists a proof accepted with probability at least 1/Q^2. Thus soundness s<1/Q^2 is impossible for such systems. For projection tests with a legal response for each first-label the lower bound improves to 1/Q. Consequently s=k^{-Theta(1)} is the natural extremal scale for polynomial proof alphabet; exponentially small soundness is not available without expanding the alphabet or allowing empty tests. This lower bound is elementary and explicitly conditional on nonempty predicates; a preprocessing algorithm that can output an empty test on NO bypasses it by recognizing NO early.

Similarly if the test support contains m nonempty tests and every test has probability weight at least w>0, there exists some proof satisfying at least one test, so s>=w on NO. Thus soundness k^{-gamma} with gamma>1 generally requires polynomially many original tests of polynomial support or sufficiently tiny weights. Random sampling compresses the support *after* the high-soundness-gap construction, not before.

## 4. Why naive randomness on the original dense PCC misses the goal (PROVED examples)

For original dense constraints there need not be constant, let alone near-one, rejection probability for every false witness. A particular assignment may violate a single pair, giving acceptance fraction 1-1/binom(k,2). Under any uniform subsampling of original pairs, O(k) samples miss that violation with probability 1-O(1/k). In the all-different pigeonhole NO example from docs/psch/2026-11-02_full_checkpoint_v7.md (k variables, alphabet k-1, all pairwise !=), EVERY proper subset of constraints is SAT, so sampling fewer than binom(k,2) *distinct original tests* cannot preserve NO at all.

Over a prime p>k^2 the single quadratic equation Q(a)=sum_{i<j} forbidden_ij(a_i,a_j)=0 mod p is already **exact** (nonnegative integer count <p); random linear combinations of the original violations provide no fundamental improvement in soundness. The bottleneck is evaluating/compiling this dense polynomial with O(k) small-alphabet local constraints. A random fingerprint whose seed is visible to the existential CSP witness cannot be justified by per-fixed-witness probability alone. The main theorem handles this with a union bound, but needs s=k^{-Omega(1)} on a SHORT two-query proof.

## 5. How the randomized implication fits log-SAT (PROVED conditional bookkeeping)

A successful PCC -> cubic 2-CSP randomized compiler with v=O(k), q=k^{O(1)}, m=O(k), constructed in poly(k), followed by direct binary CSP -> CNF yields

    n_SAT=O(k log k), clause width O(log k), number of clauses k^{O(1)}.

The image lies in both variable-relative polynomial-size LogSAT-A and input-relative LogSAT-B. However PCC itself ALREADY has a deterministic direct encoding of these SAT parameters via its dense k-variable 2-CSP (Theta(k^2) constraints); thus the new payoff of the PCP path is **sparse CSP hardness and possible downstream HOM reductions**, not the mere existence of a PCC -> log-SAT reduction.

Assuming RPCC-H, a completed linear randomized compiler would imply rSPACH on the image / a chosen output subclass (after q-padding/regularization checks); it would not by itself prove any generic nonuniform circuit lower bound. Conversely, no randomized PCC-hypothesis is established from ETH after the October 2026 announcements.

## 6. Relation to existing PCP results (EXTERNAL LITERATURE; requirements not met by citation alone)

- Moshkovitz--Raz (JACM 2010), *Two-Query PCP with Subconstant Error*, obtains near-linear PCP size for 3-SAT with o(1) soundness; neither inverse-polynomial soundness with our precise *k-witness* proof size nor O(k) positions for arbitrary PCC input is supplied by this statement. https://doi.org/10.1145/1754399.1754402
- Dinur--Harsha--Kindler (2015), *Polynomially Low Error PCPs with polyloglog n Queries via Modular Composition*, obtains 1/poly(n) error with superconstant polyloglog(n) queries and nontrivial alphabet; not automatically a two-query poly-alphabet near-witness PCP. https://arxiv.org/abs/1505.06362
- Bafna--Minzer--Vyas--Yun (STOC 2025), *Quasi-Linear Size PCPs with Small Soundness from HDX*, obtains two-query quasilinear PCP with arbitrarily small CONSTANT soundness, not necessarily k^{-gamma} and not proof size O(k) for a k^4-bit explicit graph input. https://doi.org/10.1145/3717823.3718197
- Guruswami--Lin--Ren--Sun--Wu (STOC 2025), *Almost Optimal Time Lower Bound for Approximating Parameterized Clique, CSP, and More, under ETH*, has parallel PCPs for a specially structured vector CSP; no verified arbitrary PCC -> O(k)-proof-position transfer. https://doi.org/10.1145/3717823.3718130
- Ben-Sasson--Goldreich--Harsha--Sudan--Vadhan (CCC 2005), *Short PCPs Verifiable in Polylogarithmic Time*: verification time and proof-size are stated relative to nondeterministic TIME T, not automatically the shorter witness length; encoding the explicit input in an error correcting code does not repair a T=Theta(k^2) verification circuit. https://www.wisdom.weizmann.ac.il/~oded/p_bghsv2.html
- Ron-Zewi--Rothblum, *Local Proofs Approaching the Witness Length*: very short **interactive** IOP, not a static two-query PCP. https://doi.org/10.1145/3661483

A randomized low-soundness *construction* therefore remains a sharp, meaningful research target. Sliding-scale style polynomially small error and super-short proof length are two separate obstacles; obtaining both simultaneously is not an off-the-shelf consequence of the sources.

## 7. New research target

Develop a polynomial-time input-preprocessed, two-query, nonadaptive PCP for ALL Permutation Clique instances with:

    proof length l=O(k) symbols,
    alphabet Q=k^{O(1)},
    perfect completeness,
    NO acceptance s<=k^{-gamma}, gamma>0 fixed,
    polynomial-time test sampling and relation-table generation.

Then sample O(k) tests and normalize to cubic CSP. If full construction is out of reach, first achieve one of:
(A) an efficient high-gap PCP for a structured but nontrivial special PCC class not already easy by direct algorithms;
(B) a theorem that such a PCP cannot be obtained by a particular low-degree encoding / direct-product scheme at l=O(k);
(C) an explicit k-dependent quantitative transfer from an existing parallel-PCP into the required parameters without confusing input length and witness length.

For any proposed construction, report four independent costs: proof positions, alphabet bits, test arity, and soundness. Also track the original verifier cost and any input-dependent preprocessing. *Randomized algorithms are explicitly welcome:* use a randomized hardness conjecture rather than forbidding randomized intermediate steps.

## 8. Alternative route: constant soundness plus small VC dimension (PROVED conditional transfer)

For a fixed NO input x, let Omega_x be the universe of sampled verifier tests with distribution D_x. Every proof P defines its *failure set* F_P={t in Omega_x: t rejects P}; write F_x={F_P: P in [Q]^l}. The verifier has soundness s iff D_x(F_P)>=delta=1-s for every proof P.

By the standard epsilon-net sampling theorem (Haussler--Welzl), if the range space (Omega_x,F_x) has VC dimension d, then

    t=O((d/delta)*log(1/delta) + (1/delta)*log(1/eta))

independent samples from D_x hit EVERY failure set with probability at least 1-eta. Thus even with **constant soundness gap delta>0**, having d=O(k) suffices for an O(k)-constraint one-sided randomized compiler! This bypasses the generic union bound over Q^l proof assignments. Another sufficient condition is at most 2^{O(k)} *distinct* failure sets, which yields t=O(k) directly by union bound.

This is conditional, not a claim that the desired low-VC PCP exists. The generic bound d<=l log_2 Q=O(k log k) follows just by counting proofs, and can be tight: take l symbols from alphabet [2^b] and lb unary tests, each checking one chosen bit of a symbol. Their failure patterns shatter all lb tests, so VCdim=lb=Theta(l log Q). Such proof-test systems need not be unsatisfiable; the example establishes only that binary/low-query syntax by itself gives no VC improvement. Seeking a special verifier whose NO failure-set family has VCdim O(k), while still distinguishing arbitrary PCC inputs, is therefore a separate precise research target. An explicit low VC-dimension bound must be proved for **all** proofs, not only well-formed encodings of actual permutations.

Reference: Haussler--Welzl epsilon-net theorem, e.g. https://sites.cs.ucsb.edu/~suri/cs235/EpsilonNet.pdf .

## Additional VC and algebraic gap audit

[`19_vc_dimension_permutation_tests_and_algebraic_dichotomy.md`](19_vc_dimension_permutation_tests_and_algebraic_dichotomy.md) demonstrates why a generic VCdim=O(k) cannot be inferred from permutation witnesses: native pair-check failure sets attain VCdim Theta(k log k). Conversely AllDifferent has VCdim=k-1 but gap as low as Theta(k^-2) in its critical UNSAT case. Affine zero/nonzero tests have VCdim<=l+1; pure polynomial nonzero-acceptance tests of degree d over F_p have NO gap <=d/p by Schwartz-Zippel. Both low VC and constant gap need an explicit nontrivial verifier construction.
