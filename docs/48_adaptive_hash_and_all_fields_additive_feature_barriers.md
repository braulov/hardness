# Checkpoint 48 — Adaptive fingerprint failure and all-fields zero-pattern bounds for additive features

**Research date:** 2026-11-03. **Program:** PCC / randomized decision-only matroid and CSP compilers.
**Status:** An explicit *single NO PCC instance* on which public, obliviously random linear fingerprints of violated source pairs almost certainly accept a false permutation when the fingerprint vector contains too few bits; and an **all-fields, robust lower bound** for bounded-complexity polynomial predicates of a small number of additive position features on the previously defined independently-labeled PCC YES family. The first is a concrete obstruction to a very specific hashing architecture, the second to **approximate solution-preserving** algebraic feature encodings. Neither excludes arbitrary randomized decision-only compilers. Proofs are elementary except for the all-characteristics zero-pattern bound of Rónyai–Babai–Ganapathy/Nelson. Novelty/prior art for these restricted corollaries not independently established.

Related work:
- [40: rank-factorized defect and group algebra](40_lowrank_pcc_group_algebra_effective_rank.md).
- [46: all-fields no exact/approximate linear-matroid matching-support representation](46_pcc_all_fields_zero_pattern_nonrepresentability.md).
- [47: deterministic source-degree decision-only barrier, randomized parity escape](47_decision_only_linear_matroid_source_degree_and_randomness.md).

## 1. Deterministic count makes one random fingerprint unnecessary

For an ordinary PCC graph A, let
    D_A(pi)=Σ_{1≤i<j≤K} [A_ij(pi(i),pi(j))=0]
be the number of violated row-pair constraints of π. This is a nonnegative integer at most binom(K,2). Hence for any prime p>binom(K,2),
    pi valid ⇔ D_A(pi) ≡ 0 mod p.
This is ONE deterministic quadratic field equation with a polynomial-size field. Random weights do not help reduce the *number of output field equations*; the obstacle is evaluating D_A(pi) through a near-linear algebraic/CSP interface instead of naively reading all Θ(K²) selected pair checks. Arbitrary dense compatibility matrices generally have rank Θ(K²), so checkpoint 40's O(Kr) low-rank sum-of-products computation does not solve the generic case.

For comparison, choose independent uniform α_e∈F_q for every potentially forbidden source candidate pair e (or just each unordered source row pair, with weights α_ij) and set H_α(pi)=Σ_{e violated by pi}α_e. For any fixed *invalid* π, H_α(pi) is uniform on F_q, thus Pr[H=0]=1/q. Taking q>3K! makes
    Pr_α[∃ invalid π with H_α(pi)=0] ≤ K!/q <1/3.
This is a correct strong all-witness guarantee with a field of O(K log K) **bits per element** (cardinality exponential in K log K), but strictly inferior to the deterministic violation count for binary CSP when the only task is recognizing zero.

## 2. A concrete PCC NO instance with 2^{Θ(K)} affine-coset defect witnesses

Take K=2d+2 for integer d≥1. Partition the first 2d rows and columns into d pairs B_j={2j−1,2j}. Add two designated anchor rows and columns a=2d+1 and b=2d+2.

Allow candidates only inside the d diagonal 2×2 blocks, plus (a,a) and (b,b). Make all other candidates isolated (no compatible pair with any distinct selected candidate).

Between allowed candidates set all pairs compatible EXCEPT:
  e_0 = { (a,a), (b,b) }, always forbidden;
  e_j = { (2j−1,2j), (a,a) }, forbidden for j=1,...,d.

Any permutation choosing only allowed positions is determined by x∈{0,1}^d, where x_j indicates whether block j swaps its two columns. It always chooses both anchors and hence violates e_0, so the ENTIRE PCC instance is NO. For its 2^d allowed-position permutations π_x, the forbidden-edge set is EXACTLY
    Viol(π_x)={e_0} ∪ {e_j:x_j=1}.
All extra prohibitions caused by isolated positions are absent from these π_x. This was explicitly exhaustively checked for K=4,6,8.

Now choose independent uniform weights α_0,...,α_d∈F_{2^b}^t (with all other forbidden-edge weights arbitrary independent as well), and test H_α(π)=Σ_{e∈Viol(π)}α_e=0. On the candidate family,
    H_α(π_x)=α_0+Σ_{j=1}^d x_j α_j.
Identify the additive group F_{2^b}^t with F_2^{bt}. Let W=span_F2{α_1,...,α_d}. A false accepting π_x exists iff α_0∈W.

**Theorem A (sharp collision transition on this candidate family):**
For all b,t,d≥1,
   Pr_α[∃ x∈{0,1}^d : H_α(π_x)=0]
     = E_α[2^{dim W−bt}].
If d≥bt, a union bound over nonzero linear functionals F_2^{bt}→F_2 shows
   Pr[W != F_2^{bt}] ≤ 2^{bt−d},
and hence
   Pr[∃ x:H=0] ≥ 1−2^{bt−d}.
For all d, since dim W≤d,
   Pr[∃ x:H=0] ≤ min(1, 2^{d−bt}).
Thus the required total linear sketch length to suppress collisions on this candidate family has a threshold bt≈d=Θ(K), up to additive constants. In particular, one poly(K)-size field (b=O(log K)) or t=o(K/log K) such field hashes gives false acceptance probability 1−2^{−Ω(K)} on this NO PCC input.

This does **NOT** exclude:
- deterministic nonnegative defect counting over p>binom(K,2), already exact;
- input-aware choice of weights that explicitly detects anchor edge e_0;
- nonlinear or witness-relocating decision-only compilers;
- special fixed NO graphs with a small a-priori hitting set of forbidden pairs;
- t sketches with an allowed-position mask (the displayed upper bound controls only the 2^d candidate permutations, not additional isolated-position permutations).

This proves the quantifier-order failure of *oblivious randomly weighted violations* in a particularly simple, explicit genuine NO source instance.

## 3. Robust all-fields barrier for low-rank bilinear additive fingerprints

Let N=K². Fix a rank parameter r. For every candidate x=(i,a) choose arbitrary vectors u_x,v_x∈F^r, over an ARBITRARY field F, chosen after seeing the entire PCC graph. For each permutation π set
    U(π)=Σ_i u_{(i,π(i))}, V(π)=Σ_i v_{(i,π(i))},
    h_{u,v}(π)=U(π)·V(π).
Equivalently h(π)=z_π^T C z_π for the rank≤r matrix C=UV^T, where U,V∈F^{N×r}. We classify π by whether h_{u,v}(π) is ZERO or NONZERO.

This includes ANY input-dependent rank-r bilinear factorization; field/cardinality/characteristic are unrestricted, and a randomized compiler may output arbitrary distributions over such factorizations. We do NOT require h(π) to equal the original defect COUNT — only classify its zero set.

Use the explicit PCC input family from [checkpoint 46](46_pcc_all_fields_zero_pattern_nonrepresentability.md): K=2s, M=binom(s,2)s(s−1)=Θ(K⁴) independently uniform forbidden bits β_b, and M designated permutations π_b each activating exactly the source bit β_b. Thus the true invalidity labels on these M π_b form a uniform vector β∈{0,1}^M.

For each b, the symbolic polynomial
    g_b(U,V)=Σ_{t=1}^r(Σ_{x∈S_{π_b}}U_{x,t})(Σ_{y∈S_{π_b}}V_{y,t})
has total degree 2, integer coefficients height 1, and m=2Nr=2K²r scalar indeterminates. The binary label predicted by the model is 1[g_b!=0].

**Theorem B (all-fields, robust):** For every fixed ε>0, if
    r=o(K²/log K),
then with probability at least 1−2^{−Ω_ε(K⁴)} over β, EVERY such bilinear additive classifier over ANY field agrees with the source's designated M invalidity labels on at most
    (1/2+ε)M
of them.

**Proof:** Invoke the all-characteristics Rónyai–Babai–Ganapathy/Nelson polynomial zero-pattern bound on M polynomials of degree 2 in m=2K²r variables, coefficient height 1. Provided m=o(M/log K), Nelson's explicit lemma implies the TOTAL number of realizable zero/nonzero patterns, varying both scalar substitutions and the field, is
    ≤2^{O(m log K)} =2^{o(M)}.
The bound is obtained by taking the candidate number t=2^{C m log K} in the inequality
    2^t > (2 t c(dM)^d)^{M binom(dM+m,m)}
for suitable C, with d=2,c=1 and m≤M. Indeed log binom(dM+m,m)=O(m log K), and the other factors are polynomial in log t, M and m.
For a random target β∈{0,1}^M, the probability that ANY one of at most 2^{o(M)} realizable patterns agrees with β on more than (1/2+ε)M positions is bounded using the binary entropy function:
    2^{o(M)} · 2^{-(1-H_2(1/2−ε)) M}
        =2^{−Ω_ε(M)}.
This proves the uniform all-fields statement.

In particular NO randomized, possibly unbounded-time, algorithm that outputs ONE such rank-r classifier per seed can make EACH designated permutation's validity correct with probability >=2/3 on EVERY input, for r=o(K²/log K). On an input satisfying the theorem with ε=1/10, EVERY possible output has agreement <3M/5, contradicting an expected agreement ≥2M/3 if every designated π_b were correct with probability ≥2/3.

**What this strengthens:** Checkpoint 40 ruled out low-rank representations preserving the *exact quadratic score* over a fixed polynomial field by a basic count. Theorem B rules out preserving even the ZERO/NONZERO status approximately, across ALL fields and ALL randomly selected representations, with a sharp scale r=o(K²/log K). It still does **NOT** exclude decision-only compilers that may relocate the accepting matching.

## 4. Fixed-degree nonlinear predicates of additive features

The method in Section 3 extends beyond quadratic bilinear forms.

Choose r input-dependent additive features f_t(x)∈F, form s_t(π)=Σ_{x∈S_π} f_t(x), and let P∈F[Z_1,...,Z_r] be an ARBITRARY input-dependent polynomial of total degree ≤d, where d is a fixed constant. Classify by 1[P(s(π)) !=0]. The polynomial P is specified by all its coefficients, NOT allowed to hide an arbitrary exponential-size formula; the point here is a conventional degree-d recognizer with polynomially many explicit parameters.

There are
    m=Nr+binom(r+d,d)=K²r+O_d(r^d)
scalar parameters (feature values and polynomial coefficients). For each designated π_b, the composition P(s(π_b)) is an integer polynomial in these parameters of total degree ≤d+1 and integer coefficient height K^{O_d(1)}. Hence Nelson's all-fields bound gives
    at most 2^{O_d(m log K)}
possible classification patterns for r=K^{O(1)}, provided m≤M. Consequently:

**Theorem C:** For fixed d and fixed ε>0, if
    (K²r+r^d) log K = o(K⁴),
then on almost every PCC instance from the checkpoint-46 distribution EVERY such additive-feature degree-d classifier over ANY field gets at most (1/2+ε)M of the M independent designated permutation labels correct. The same model-specific randomized 2/3 per-permutation no-go follows.

In particular with r=O(K), EVERY fixed d≤3 satisfies the hypothesis and is ruled out, even if P and all features depend arbitrarily on the entire source graph and the field size is unrestricted. Degree d=4 with r=Θ(K) is **not excluded by this coarse parameter count**, but that is NOT an existence theorem or a proposed efficient construction.

For a FIXED input-independent P the coefficient-variable term binom(r+d,d) disappears, yielding a stronger bound depending only on Nr and the degree/height of the expanded test; track P's explicit integer representation separately.

**Limits:** The statements are about zero/nonzero acceptance on each *original* permutation, even if only approximate. No restriction on an arbitrary *decision-only* map, which may discard source witnesses or use existentially chosen auxiliary matching positions. General high-degree input-dependent polynomial circuits with exponentially many monomials are outside the stated scalar-parameter bound.

## 5. What to investigate next

(A) The randomized linear fingerprint of violated edges is invalid as a standalone **low-bit** public sketch for all existential witnesses, even though each fixed bad witness is rejected with probability 1−2^{-bt}; one explicit NO PCC family proves the distinction. But deterministic nonnegative counting avoids this issue entirely.

(B) A polynomial-description **global evaluation circuit** for D_A(pi) is trivial of size Θ(K²) in terms of pair-check *operations*. Our target is a genuinely near-linear existential/coded evaluation circuit or a decision-only witness-relocating reduction. Reducing scalar output size or using a larger field does not reduce the number of interactions.

(C) Low-rank bilinear features and even an arbitrary cubic polynomial of O(K) additive features cannot approximate *which permutations are valid* on generic PCC, over any field. To evade this, one must depart from all-witness preservation (decision-only), enlarge the feature/predicate description, or use auxiliary witness variables and high-complexity global consistency.

(D) The deterministic source-degree obstruction in [47](47_decision_only_linear_matroid_source_degree_and_randomness.md) still applies to a DIFFERENT architecture: low-degree input-dependent output *vectors*, and does restrict a decision-only reduction. There is no contradiction: Theorem B/C here concern the *acceptance predicate as a function of the selected permutation*, not the degree of vector coordinates as functions of source graph bits.

## Primary sources

- Rónyai, Babai, Ganapathy, *On the Number of Zero-Patterns of a Sequence of Polynomials*, JAMS 14 (2001), https://doi.org/10.1090/S0894-0347-01-00367-8 and https://people.cs.uchicago.edu/~laci/papers/zero.pdf .
- Peter Nelson, *Almost all matroids are non-representable* (2018) and his all-fields integer-polynomial zero-pattern lemma, https://matroidunion.org/?p=1986 .
- Project [checkpoint 40](40_lowrank_pcc_group_algebra_effective_rank.md) and [checkpoint 46](46_pcc_all_fields_zero_pattern_nonrepresentability.md).

**Bottom line:** An explicit NO instance exposes the quantifier-order failure of public low-bit random defect hashing; and a robust all-fields counting theorem shuts down an entire family of low-dimensional, low-degree additive-feature status-preserving encodings. Neither result settles unrestricted decision-only PCC linearization. Novelty against all literature not verified.


## 6. Fundamental guardrail: pure size-only lower bounds cannot exclude decision-only linearization

For EVERY PCC input A, irrespective of computational time, there exists a rank-K representable linear matroid over the TWO-element field on the original K×K candidate positions whose independent perfect matchings exist iff PCC(A) is YES.

Proof: If PCC(A) is YES, let v_{i,i}=e_i∈F_2^K and every off-diagonal vector zero. Then the only independent perfect matching is the identity and it exists. If PCC(A) is NO, set every candidate vector to zero; then no independent perfect matching exists. Both representations have dimension exactly K, field F_2, and O(K³) explicitly written field entries. The difficulty lies ENTIRELY in computing WHICH of the two templates to output, since that selection itself answers PCC.

Thus a **pure existence/counting argument** about the number of small linear matroids, the number of output perfect matchings or dimensions/field sizes CANNOT rule out a decision-only PCC→linear-matroid compiler without imposing restrictions on computation of the output. Any meaningful no-go for the general decision-only branch must use a computational hypothesis (such as RPCC-H) or genuinely restrict source preprocessing (e.g. deterministic low-degree entry functions as in checkpoint 47, source locality, uniform sparse circuits). This is not a breakthrough; it is an important quantifier sanity check preventing misuse of the all-fields solution-preservation counting lemmas.
