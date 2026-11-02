# VC dimension of Permutation Clique tests: exact extremal examples and algebraic barriers

**Research iteration 2026-11-02.** PROVED elementary theorems and explicit cautions; no general PCC-to-linear-CSP compiler is claimed. Randomized reductions and algorithms are fully welcome. Follows notes 17 and 18.

## 1. Main extremal theorem: native PCC tests have VC dimension Theta(k log k) even on genuine permutations (PROVED; probabilistic existence)

Let k be sufficiently large, m=floor(k/2), b=floor((log_2 k)/2), and q=2^b<=sqrt(k). There exist maps f_i:[k]->{0,1}^b, i=1,...,m, such that:

    For EVERY choice of words c_1,...,c_m in {0,1}^b,
    there exist pairwise distinct a_1,...,a_m in [k]
    satisfying f_i(a_i)=c_i for every i.

**Proof by Hall and a union bound.** Sample every f_i(a) uniformly and independently from [q]. For fixed S subseteq[m] of s>=1 rows, fixed T subseteq[k] of size s-1, and fixed requests c_i (i in S), the probability no row i in S has a matching image outside T is

    (1-1/q)^{s(k-s+1)} <= exp(-s(k-s+1)/q)
                             <= exp(-sk/(2q)),

since s<=m<=k/2. Count all triples (S,T,requests) by

    binom(m,s) binom(k,s-1) q^s <= (k^2 q)^s.

For q<=sqrt(k), their sum over s=1,...,m is <=sum_s exp(s(2.5 log k-sqrt(k)/2))<1 for large k. Thus with positive probability none of the bad Hall events occurs. This establishes the simultaneous system-of-distinct-representatives property for every request vector.

Now choose b distinct 'anchor rows' j_1,...,j_b from {m+1,...,k}. Define a valid undirected PCC input graph on [k]x[k] with the **only nontrivial pairs of row classes** (i,j_t), i in [m], t in [b]. The adjacency on this row-class pair is

    A_{i,j_t}(a,z)=1 iff bit_t(f_i(a))=0,

independent of the anchor's column z. All other cross-row pair constraints are complete. The actual PCC witness is still required to be a permutation, ensuring distinct columns globally.

Let E0={(i,j_t):i in [m],t in [b]}, with |E0|=mb=Theta(k log k). For ANY subset U of E0, prescribe c_i so bit_t(c_i)=1 iff (i,j_t) in U. The Hall property supplies pairwise distinct a_i for active rows, which can be extended arbitrarily to a permutation pi of [k]. Then exactly the checks in U are violated. Hence E0 is shattered by the failure sets of **valid permutation witnesses**:

    VCdim({F_pi:pi in S_k})>=mb=Omega(k log k).

Conversely |S_k|=k!, so VCdim<=log_2(k!)=O(k log k). Therefore the VC dimension of the native PCC pair-check failure family is Theta(k log k) for this concrete existentially produced input family, even when the number of nontrivial tests is only Theta(k log k).

**Scope:** This DOES NOT rule out PCP recoding with a different O(k)-VC failure family, or a reduction whose only goal is decision preservation. It only rules out an automatic VC saving from simply restricting raw pair tests to permutation witnesses. The constructed example can be an easy YES instance.

## 2. Exact AllDifferent VC dimension and a tiny NO gap (PROVED)

On variables x_1,...,x_k with alphabet size q>=2, let the tests range over pairs e={i,j}, accepting iff x_i != x_j. The failure set for assignment x consists of edges whose endpoints have the same value.

**Claim:** the failure-set range space has VC dimension exactly k-1 for the complete set of all pair tests, independent of q>=2.

Lower bound: any spanning tree E_T of K_k is shattered. For any desired subset U subset E_T, root the tree and assign each child's value equal to its parent's if the connecting edge is in U, otherwise flip between two distinct colors. This realizes exactly U on the selected tree edges.

Upper bound: a shattered collection S cannot contain a cycle. On a cycle, demanding equality (failure) on every edge except one, and inequality (acceptance) on that last edge, is impossible by transitivity. Thus |S|<=k-1.

For q=k-1 (the usual pigeonhole UNSAT instance), every assignment violates >=1 of the M=binom(k,2) disequality tests, while one can achieve exactly ONE violation by duplicating one color and using all other colors once. The best NO rejection gap of uniform original-pair sampling is therefore precisely delta=1/M=Theta(k^{-2}), despite VC dimension k-1. Small VC dimension alone cannot yield O(k) sampling via the epsilon-net theorem. This instance is easy/structured; it is not a generic hardness lower bound.

## 3. Polynomial-span bound on test failure-set VC dimension (PROVED)

Let each proof P be a vector z in F_p^l, and let test t accept or reject according only to whether a polynomial P_t(z) over F_p equals zero. Tests may orient equality/non-equality differently. Let D=dim_Fp span{P_t:t in T} as formal polynomials, or use the linear span of their evaluation functions over F_p^l (which can give a better bound). Then

    VCdim({{t:test t rejects z}:z in F_p^l}) <= D.

Indeed, any D+1 test polynomials are linearly dependent: choose t0 in their dependence with nonzero coefficient. If those tests were shattered, some z would make all remaining polynomials zero and P_t0(z) nonzero (the chosen failure/acceptance pattern depends on orientation), contradicting the dependency.

For affine forms P_t(z)=a_t·z+b_t, D<=l+1 regardless of alphabet p and number of tests. This is an exact and often useful O(k)-VC conclusion for l=O(k).

**Critical orientation distinction:**
- If acceptance is P_t(z)=0 for every test, a basis of the span of test polynomials suffices to preserve the full joint zero set exactly. One gets a D-test DETERMINISTIC reduction by Gaussian elimination on coefficient vectors when they are efficiently available. Pure affine-equation CSP is in P.
- If acceptance is P_t(z)!=0, selecting a basis is generally WRONG: P_1(z)!=0 and P_2(z)!=0 do not imply P_1(z)+P_2(z)!=0. The low-VC bound still holds, and potentially nontrivial randomized epsilon-net sampling applies if a genuine gap is proved. This includes the AllDifferent disequality test system.

For total-degree<=d polynomial equality/inequality tests on l scalar field coordinates, the formal monomial basis gives D<=binom(l+d,d); with d=2 this is Theta(l^2), not the desired O(l) without additional structure.

## 4. Gap obstruction for nonzero tests over a growing field (PROVED)

Suppose tests all ACCEPT iff P_t(z)!=0, where each P_t is a nonzero polynomial of total degree at most d<p, and proof coordinates range independently over the entire F_p^l. By Schwartz--Zippel, a uniform random z gives

    Pr_z[test t rejects] = Pr[P_t(z)=0] <= d/p.

Averaging over t under ANY input-dependent test distribution, there exists a proof z rejected with probability at most d/p. Thus the verifier cannot have a NO rejection gap delta>d/p. In particular d=O(1), p=k^{Omega(1)} precludes constant-gap NO soundness in this pure model. If m<p/d and tests are equally weighted, a union-bound argument even gives an assignment satisfying all (every z belongs to no zero set with positive probability). This assumes no identically-zero polynomial tests, no external nonlinear restriction on allowed proofs, and the specified nonzero-acceptance direction.

This is a MODEL-SPECIFIC impossibility: mixed equality/inequality tests, limited-domain codeword promises, higher degrees, and highly nonlinear local predicates are outside the hypothesis. For equality-ACCEPTING tests, the argument is inapplicable (random proofs often fail those tests).

## 5. Synthesis and an improved next target

Three independently necessary resources for linear randomized sampling are:
1. l=O(k) proof positions over Q=poly(k);
2. constant NO rejection gap delta (or polynomially small soundness in the alternative theorem of doc 18);
3. VCdim of the *entire* proof failure-set family O(k), not merely of true permutation encodings.

The native pair tests fail condition (3) in the worst case (Section 1). AllDifferent has property (3) but fails (2) on its critical unsatisfiable case (Section 2). Pure low-degree polynomial nonzero tests over a large field also fail (2) by averaging (Section 4). Affine equality tests satisfy (3) but have a trivial deterministic linear-basis reduction and are polynomial-time solvable (Section 3).

**High-priority open experiment:** combine hard, nonlinear input-dependent predicates with an algebraic consistency layer whose checks have low span/low VC, then prove constant-gap robust rejection for ALL malformed proofs. Tests must remain nonadaptive two-query with total proof length O(k) polynomial-alphabet symbols. The nonlinear layer must not quietly use Theta(k^2) independent tests. Compare Reed--Muller/projection tests, algebraic constraint propagation, and parallel-PCP schemes; no construction is claimed yet.

Related notes: docs/13_log_width_sat_and_polynomial_alphabet_csp.md ; docs/14_permutation_clique_sparse_2csp_branch.md ; docs/18_randomized_low_soundness_pcp_to_linear_csp.md .

## References

- Haussler--Welzl epsilon-net theorem; survey: https://www.math.tau.ac.il/~michas/enet.pdf
- Schwartz--Zippel lemma (standard algebraic identity-testing bound).
- Guruswami--Lin--Ren--Sun--Wu, STOC 2025: https://arxiv.org/abs/2404.08870

## Two-layer follow-up

[`20_two_layer_affine_nonlinear_pcc_audit.md`](20_two_layer_affine_nonlinear_pcc_audit.md) replaces vague 'linear consistency + nonlinear checks' with a quantitative formulation. Pure two-query affine consistency cannot be a positive-rate/positive-distance code; 3-ary affine checks are exactly compilable into linear-size cubic CSP. Fixed-decoder exact projection of ALL genuine PCC permutations demands tQ²=Omega(k⁴) input-dependent nonlinear table bits. The critical remaining subproblem is a robust globally sensitive nonlinear interface; low VC or good code distance alone does not solve it.
