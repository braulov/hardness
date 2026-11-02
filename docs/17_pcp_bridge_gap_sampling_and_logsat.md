# Permutation Clique -> sparse CSP via exact noninteractive proof tests

**CRITICAL 2026-11-02 UPDATE:** See [the domain-uniform CSP alert](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md). An UNVERIFIED new preprint claims a q^{O(v/sqrt(log v))} deterministic algorithm for bounded-degree binary CSP. If correct SPACH/rSPACH are FALSE and, assuming RPCC-H, generic linear-size bounded-degree compilers are impossible. This updates motivation but does not invalidate the elementary PCP sampling lemmas.


> **2026-11-02 CONDITIONAL CLOSURE OF HARDNESS-TRANSFER TARGET.** If the *full* OpenAI Boolean tensor-contraction theorem is correct, any explicitly represented sparse polynomial-alphabet 2-CSP with \(r=k'+m'\) variables plus constraints can be solved in \(2^{O(r\sqrt{\log K})}\operatorname{poly}(K)\) when the output alphabet is \(K^{O(1)}\). Therefore, under the separately conjectured no-\(2^{o(K\log K)}\) PCC-hardness assumption, a polynomial-time PCC \(\to\) sparse 2-CSP compiler with \(r=o(K\sqrt{\log K})\), **including the O(K) stretch goal, cannot exist**: otherwise it gives a faster PCC algorithm. The downstream SPACH/rSPACH hardness claims are also conditionally refuted. **Keep the exact gadgets, PCP sampling lemmas, and structural barriers; do not claim the mathematical existence question has been disproved unconditionally.** The full tensor theorem is not part of the documented Lean scope. See [audit and branch triage](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).


**Research iteration 2026-11-02.** Elementary lemmas and a sharpened research target; NOT an O(k) generic compiler. Distinguish proved implications from conjectures. This note adds a clean proof-system interface and gap-sensitive theorem to the pre-existing PCP program in docs/psch/2026-11-02_full_checkpoint_v7.md, rather than reasserting that its earlier PCP ideas were new.

## 0. Correction to the rank-quotient example

The 0/1 instance used in docs/16_permutation_mixed_difference_rank_and_routing.md to prove r_perm(B)=Omega(k^2) has nontrivial original constraints **only** between row pairs (i,s+i), 1<=i<=s. Thus its source constraint graph is already a matching with k/2 edges! It demonstrates that neither raw rank nor permutation-effective rank measures sparse existential representability. It DOES NOT demonstrate any difficulty in compiling a dense source. Its high-rank proof remains correct as a representation-specific counterexample.

## 1. Exact proof-test / 2-CSP equivalence (PROVED; syntactic statement)

Fix an instance I of Permutation k x k Clique (or any parameterized decision problem). A *nonadaptive two-query test system* consists of:
- an explicitly enumerated finite set T of at most Ck deterministic tests, each reading <=2 of l<=Ck proof coordinates;
- alphabet [Q] with Q<=k^C, and an input-dependent predicate R_t:[Q]^2->{0,1} for each test, explicitly tabulated in poly(k) time (unary tests can be handled by allowed values);
- perfect completeness: YES iff there exists a proof accepted by *ALL* tests. This exact global quantification is equivalently perfect completeness (some proof passes every seed) and soundness strictly <1 (no proof passes every seed) under a uniform test distribution.

Map proof coordinates to CSP variables and tests to binary constraints. The CSP has l=O(k) variables, O(k) constraints, alphabet poly(k). If some proof symbols have many incident tests, replace occurrences by copies joined along equality paths, adding O(k) variables and edges and achieving maximum degree <=3. Any 0/1 or unary relation is preserved via domain restrictions/degree-one auxiliary gadgets. The construction is deterministic polynomial time.

Conversely a CSP instance of l,m=O(k), alphabet poly(k) gives a two-query nonadaptive test system: proof is a CSP assignment and seed chooses one constraint. Perfect completeness is 1; for NO instances each proof violates at least one test, hence uniform rejection probability >=1/m. Thus two-way equivalence holds at **weak** soundness 1/O(k). Upgrading this to constant soundness with O(k) tests is a separate gap-amplification problem.

A verifier with r<=log_2 k+O(1) unbiased random bits has O(k) seeds/tests, but *nonadaptivity*, perfect completeness, and two-coordinate tests are essential. A general interactive PCP / IOP, especially an adaptive sum-check, does NOT instantiate this equivalence by guessing its transcript.

## 2. Robust NO => O(v log q / delta) unsatisfiable subinstance (PROVED)

Let a binary CSP have v variables, common alphabet [q], and m original constraints. Suppose **every** complete assignment violates >=delta m constraints, with 0<delta<=1. Draw t independent uniform random constraints, with replacement, where

    t >= (v ln q + ln(1/eta))/delta.

For each fixed assignment the chance of satisfying all sampled constraints is at most (1-delta)^t <= exp(-delta t). There are q^v assignments, so by union bound the sampled instance is UNSAT with probability >=1-eta. If the original instance is SAT, any satisfying assignment satisfies every sampled constraint for every sample (perfect one-sided YES-preservation). Consequently robust unsatisfiability has a subinstance of size O((v log q)/delta), and there is a randomized polynomial-time procedure finding one with constant/high probability.

For Permutation Clique, assume a **robust NO promise**: every permutation violates at least delta binom(k,2) of the original pairwise compatibility conditions. The union bound may be taken over k! permutations, giving

    t >= (ln(k!) + ln(1/eta))/delta = O(k log k/delta).

Keep AllDifferent via the O(k log k) Beneš gadget already in docs/psch/, and for each sampled pair add the original compatibility constraint. Equality-copy degree reduction gives a max-degree-3 binary CSP with O(k log k+k log k/delta) variables/constraints and common alphabet k^{O(1)}. It is a **randomized, one-sided, promise** reduction, not a deterministic reduction for ordinary PCC. This is a direct application of the union bound, not a novel PCP construction.

A deterministic small core EXISTS by the probabilistic method, but we have not shown a deterministic polynomial-time algorithm to locate it for arbitrary explicit instances (checking whether an arbitrary sampled subinstance is UNSAT is itself generally hard).

## 3. Why this is quantitatively insufficient for SPACH (PROVED bookkeeping)

For fixed delta>0 the robust-PCC compilation has v'=Theta(k log k) after size-normalizing/padding (or O(k log k) with conventional bounds), q'=k^{O(1)}, max degree 3. Its binary SAT encoding uses

    n_SAT=Theta(k log^2 k), width O(log k), polynomially many clauses.

Thus this yields restricted LogSAT-A and B instances, but a PCC-hardness assumption excluding 2^{o(k log k)} only excludes **2^{o(n_SAT/log n_SAT)}** on this image, NOT a universal lower bound of the no-2^{o(n_SAT)} kind. Moreover PCC-hardness alone says nothing about hardness of this *gap promised* class. A generic reduction turning arbitrary PCC into robust-gap PCC without a large parameter loss is an additional OPEN step.

For ordinary non-gap PCC, plain subsampling is not sound: source assignments may violate only one pair. The older PSCH checkpoint's edge-critical complete disequality CSP (k variables, q=k-1, all pairwise inequalities) is UNSAT but becomes SAT after deleting ANY pairwise constraint. This establishes a lower bound for *deleting original checks*, not for arbitrary input-preprocessed existential compiler.

## 4. Connection to the most relevant proof-system literature (EXTERNALLY VERIFIED BACKGROUND, NOT OUR RESULT)

- Kalai--Raz (ICALP 2008), *Interactive PCP*: proof size poly(witness length) for some large formulas despite larger verification size, but **interactive** and only poly(k), not assured O(k) nor a static O(k)-test noninteractive system: https://doi.org/10.1007/978-3-540-70583-3_44
- Ron-Zewi--Rothblum (JACM 2024), *Local Proofs Approaching the Witness Length*: IOP communication approaching witness length for specified polynomial-space NP verifiers, but again **interactive oracle proofs**, not nonadaptive two-query static PCP with O(k) tests: https://doi.org/10.1145/3661483
- Guruswami--Lin--Ren--Sun--Wu (STOC 2025), *Almost Optimal Time Lower Bound for Approximating Parameterized Clique, CSP, and More, under ETH*: near-linear parallel PCP for *vector-structured sources*, not a proved generic arbitrary PCC -> O(k) cubic CSP reduction: https://arxiv.org/abs/2404.08870

These are the most interesting proof systems to audit for a **strict noninteraction + alphabet + symbol-count** compilation. Do not claim they already solve the intended conversion.

## 5. A precise next research subproblem

Seek, for **arbitrary** graph A on [k]x[k], a polynomial-time constructed, noninteractive two-query proof system:
- proof positions l=O(k), alphabet Q=k^{O(1)};
- <=O(k) tests (the input itself has up to k^4 adjacency bits, each input-dependent local predicate may have a table Q^2=poly(k));
- YES: there is a proof that passes every test;
- NO: every proof fails >=1 test;
- ideally every accepting proof decodes to an actual Permutation Clique, although decision preservation alone is enough for conditional hardness.

Equivalently, construct a deterministic O(k)-variable, O(k)-constraint max-degree-3 binary 2-CSP compiler, the open goal already in docs/14_permutation_clique_sparse_2csp_branch.md. A stronger constant-gap test system with only polynomially many tests could allow randomized O(k log k) sampling, but does not automatically yield the linear goal or deterministic hardness. A fixed sampled verifier challenge may be gamed by an existentially selected proof; the correct sampling criterion is a **simultaneous union bound over all proofs**.

A concrete local experiment: choose a vector-structured special class of PCC adjacency tables admitting an *input-preprocessed* two-query verifier, e.g. a constant-size composition of permutation-transport, interval/threshold relations, and arbitrary O(k) exceptional pairs. Require an explicit O(k)-test construction with degree reduction, and compare to the already-known composition/path-consistency tricks. Do not mistake a special-class positive lemma for general PCC compression.

## 6. Research verdict

ESTABLISHED: exact test-system/CSP equivalence, robust-gap sampling, parameter accounting, correction that the high r_perm witness is already sparse.
OPEN: a new generic polynomial-time O(k)-constraint compiler for arbitrary PCC, a static witness-length O(k)-symbol noninteractive 2-query PCP with O(k) tests, a gap-creating PCC reduction with controlled k, deterministic short-core construction in arbitrary robust-gap cases.
