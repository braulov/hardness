# Rank-parameterized Permutation Clique via group-algebra determinants, and effective quadratic rank

**Research date:** 2026-11-02. **Branch:** PCC / sparse-CSP compatibility interface.
**Status:** Proved elementary reduction of PCC to a low-rank quadratic form, and a randomized one-sided p^{r} poly(K)-time solver via a **known algebraic group-labeled matching mechanism**. A separate exact O(Kr+KlogK) degree-3 polynomial-alphabet binary CSP construction is proved. Polynomial-time equivalence testing and a counting lower bound for effective rank are also proved. **No universal dense-to-sparse compiler, no critical PCP, and no novelty over the relevant QAP / group-labeled matching literature is claimed.**

## 0. Setup and conventions

Input: an arbitrary K×K Permutation Clique (PCC) instance, with rows i∈[K], columns a∈[K], and compatibility A_{ij}(a,b)∈{0,1} for i≠j. A witness π∈S_K selects the K positions (i,π(i)) and must have A_{ij}(π(i),π(j))=1 for all i<j.

Choose a prime p>K(K−1) and p=O(K²) (Bertrand's postulate), so p is odd for K≥2. Input is explicit O(K⁴) bits; all claimed preprocessing costs are polynomial in K and in that input length.

Let N=K². Define an N×N symmetric 0/1 *forbidden-pair matrix* B indexed by (i,a), with
  B_{(i,a),(j,b)}=1−A_{ij}(a,b) when i≠j, and 0 for i=j.
In particular B is symmetric, B_{(i,a),(i,a)}=0. Set r=rank_{F_p}(B).
Let z_π∈{0,1}^N be the one-hot indicator of π. Then
  z_π^T B z_π=2·(# forbidden row-pairs selected by π),
as an integer in [0,K(K−1)] and hence, by the choice p,
  π valid PCC iff z_π^T B z_π=0 in F_p.     (1)

## 1. Exact compatibility compiler for rank-r matrices

Factor B=UV^T with U,V∈F_p^{N×r} by ordinary Gaussian elimination, in poly(K) time. For each t∈[r], introduce a chain computing
  u_t=Σ_{i=1}^K U_{(i,x_i),t},
  v_t=Σ_{i=1}^K V_{(i,x_i),t}
where x_i∈[K] are chosen columns. Both sums cost O(Kr) additions/lookups in F_p. A final chain of r products and r additions enforces Σ_t u_t v_t=0. The identity Σ_t u_t v_t=z_x^TBz_x is exact for every list x.

Each table lookup, addition or multiplication relation has constant arity and can be compiled into O(1) binary relations using a gate-state tuple with alphabet at most p^{O(1)}; high-degree/fanout variables are replaced by occurrence copies joined by equality paths. With an independent O(KlogK)-constraint sorting/Beneš AllDifferent gadget, the resulting binary CSP has
  variables, constraints = O(Kr+Klog K),   max degree<=3,
  alphabet Q=K^{O(1)},
  exact projection onto the satisfying PCC permutations.
The value of r can be as large as N=K², in which case this is worse than the direct Θ(K²) dense compatibility CSP. It is a true compression only in the low-rank regime.

No approximation of field zero is involved: p>K(K−1), so a zero field sum of original nonnegative defect bits is genuinely zero.

## 2. Symmetric rank factorization and additive matching weights

Because B is symmetric and char(F_p)≠2, there is a polynomial-time factorization B=WDW^T, where W∈F_p^{N×r} is full-column rank and D∈F_p^{r×r} is symmetric. Construction: take W a column-space basis of B, choose any left inverse L with LW=I_r, put D=LBL^T. Then WL acts as identity on columns of B, and by symmetry on its rows, so WDW^T=B.

Write w_{ia}∈F_p^r for the row of W indexed by (i,a). For a permutation π set s_π=Σ_i w_{i,π(i)}∈G=(F_p)^r. Then
  z_π^TBz_π=s_π^TDs_π.
By (1):
  PCC is YES iff there exists a perfect matching π of K rows to K columns with s_π^TDs_π=0.    (2)

Optional: D may be diagonalized by congruence over the odd characteristic field; this makes evaluating s^TDs an O(r) rather than O(r²) process. It does not affect the group dimension r.

## 3. Randomized exact-group-weight matching via determinant in characteristic two

**Theorem (one-sided RP algorithm).** Given a K×K complete bipartite graph with edge labels w_{ia}∈G=(F_p)^r and ANY efficiently recognizable set S⊆G, there is a randomized one-sided-error algorithm deciding whether some perfect matching has total label in S in time
  p^r · poly(K,p,r),
with the field/character computation polynomial in K,p,r. Its false-positive probability is zero, and its false-negative probability can be made ≤1/3.

**Proof.** Take an auxiliary finite field F of characteristic 2 with (a) a primitive p-th root of unity ζ, and (b) |F|≥3K. Since p is odd, take F=GF(2^a) with a a positive multiple of ord_p(2), increased until a≥log_2(3K). We have ord_p(2)≤p−1 and hence a=poly(K), and a field plus ζ can be obtained with randomized polynomial preprocessing. Sample independent random coefficients y_{ia}∈F.

For every Fourier character t∈G, define a K×K matrix
   M_t(i,a)=y_{ia} ζ^{<t,w_{ia}>},
and compute d_t=det_F(M_t). Since F has characteristic 2, the determinant equals the permanent. Expanding the determinant,
   d_t=Σ_{π∈S_K} (Π_i y_{i,π(i)}) ζ^{<t,s_π>}.
This is the Fourier transform of the group-algebra element
   C=Σ_{π∈S_K} (Π_i y_{i,π(i)}) [s_π] ∈F[G].

For all s∈G recover
   C_s=(1/|G|) Σ_{t∈G} d_t ζ^{−<t,s>},
where 1/|G| exists because p^r is odd (indeed equals 1 in characteristic 2). This inversion can be done by a multidimensional FFT/DFT in p^r·poly(p,r) operations or naïvely in p^{2r} operations; either way yields p^{O(r)} poly(K), and the standard separable DFT across r F_p coordinates gives p^r·poly(p,r) by O(r p) transforms of length p per dimension.

Formally, before the random substitution, the coefficient polynomial
   C_s(Y)=Σ_{π:s_π=s} Π_i Y_{i,π(i)}
is nonzero iff some perfect matching has label s: different permutations yield distinct multilinear monomials. If NO matching has label in S, every C_s with s∈S is identically zero for every substitution; thus NO false positives. If a YES matching exists, fix one s∈S with C_s(Y) nonzero, total degree K. Schwartz–Zippel over F gives Pr[C_s(y)=0]≤K/|F|≤1/3. Repeat independently for amplification. QED.

For PCC, take S={s:s^TDs=0}. Construct W,D and run the group-weight solver. Choose p=O(K²), so runtime is
  poly(K)·p^{O(r)} = K^{O(r+1)}.
At r=O(1), polynomial time; at r=O(K/log K), time 2^{O(K)}; at r=o(K), time 2^{o(K log K)}. This algorithm requires no Nguyen/OpenAI 2026 tensor theorem and does not assume RPCC-H.

**Sanity test (not the proof):** a GF(2^6) finite-field implementation for K=3, p=7, r=2, primitive seventh root ζ, explicitly computes all 49 determinants, Fourier-inverts them, and compares the result with all 3! permutations. In 100 seeds each for one YES and one NO low-rank defect construction, all 49 coefficients matched exactly, and the YES/NO decision matched. Code in experiments/40_lowrank_pcc_fourier_sanity.py.

## 4. Effective rank modulo permutation-quadratic identities

The raw rank r can be misleading. For example, B=(J_K−I_K)⊗I_K has rank K² over F_p (since p>K(K−1)), although its quadratic form is identically zero on S_K: a permutation never chooses the same column twice. This example corresponds to redundant 'equal-column' forbidden entries, not to actual PCC hardness.

Define the *effective permutation quadratic rank*
  ρ_perm(B) = min{rank(B+T): T=T^T, z_π^TTz_π=0 for every π∈S_K}.
It captures representations of the SAME exact F_p quadratic score on all permutations, not merely the same YES/NO predicate. If a rank-r witness B'=B+T for this minimum is supplied, we can run the group-weight algorithm in K^{O(r+1)}.

**Proved polynomial verification of a proposed witness:** Given any symmetric T∈F_p^{N×N}, one can decide in poly(K,log p) time whether
    z_π^TT z_π=0 for every π∈S_K.
A direct polynomial-size system of LINEAR equations characterizes the null subspace:
- Put q_T(π)=z_π^TTz_π.
- Check q_T(id)=0.
- For each choice of two different rows i,j and two different columns a,b, consider π with π(i)=a,π(j)=b and π' obtained by swapping their values. Let R=[K]\{i,j}, C=[K]\{a,b}. The change q_T(π')−q_T(π) equals
      d_{ij}^{ab}+Σ_{t∈R} c_t(π(t)),
  with
      d_{ij}^{ab}=T_{ib,ib}−T_{ia,ia}+T_{ja,ja}−T_{jb,jb}
                 +2(T_{ib,ja}−T_{ia,jb}),
      c_t(v)=2(T_{ib,tv}−T_{ia,tv}+T_{ja,tv}−T_{jb,tv}).
- The sum Σ_{t∈R} c_t(π(t)) is constant across all bijections π|_R:R→C iff its coefficient matrix (c_t(v))_{t∈R,v∈C} is additively separable:
      c_t(v)−c_t(v0)−c_{t0}(v)+c_{t0}(v0)=0
  for one reference row t0 and column v0, all t,v (for |R|≤1 this is vacuous).
- Also check d_{ij}^{ab}+Σ_{t∈R}c_t(σ_0(t))=0 for one fixed bijection σ_0:R→C.
These conditions are necessary and sufficient for q_T to be unchanged by every swap of two row values. Such swaps connect all permutations, so together with q_T(id)=0 they are equivalent to q_T≡0.

There are O(K^6) such linear equations (up to constants), each involving O(1) entries of T except the one sum-of-O(K) baseline equation; construct and check them in polynomial time. For K=2 the sum is empty and the same formula applies. This is related to known linearizability tests for the GENERAL quadratic assignment problem (Kabadi–Punnen, Math. Oper. Res. 2011); no originality is claimed.

**Computational gap:** Finding the lowest-rank element of the affine subspace B+Null_quad is a *MinRank* problem and is not known polynomial-time from this verification lemma. We have a polynomial-time CHECKER for a proposed low-rank equivalent form, not a polynomial-time optimizer.

Sanity checks: polynomial swap-derivative test versus brute-force testing across all permutations for K=2,3,4,5, including random symmetric T and structured null-gauge T.

## 5. A counting barrier: generic PCC instances have large effective quadratic rank

**Theorem (exact-score model).** There is c>0 such that, for infinitely many even K and p the chosen O(K²) prime, there exist 0/1 forbidden-pair matrices B arising from genuine PCC inputs with
     ρ_perm(B) >= c K²/log K.
Moreover a uniformly random member of the concrete family constructed below satisfies this with probability 1−2^{−Ω(K⁴)}.

Proof: K=2s. Split rows into s *regular* rows and s filler rows, and columns into s default and s active columns. For each pair of distinct regular rows i<j and distinct active columns a≠b, allow the corresponding ordered forbidden-pair bit β_{ijab}∈{0,1} to vary independently; set all other forbidden entries to zero. There are
   M=binom(s,2)·s(s−1)=Θ(K⁴)
independent bits. For each (i,j,a,b), choose a permutation assigning active column a to regular row i, b to regular row j, and the remaining regular rows their distinct *default* columns; filler rows use all leftover columns. This permutation activates exactly that one arbitrary pair bit β_{ijab}, so its score is 2β_{ijab} mod p. Consequently all 2^M choices of β induce **different exact score functions** q_B:S_K→F_p.

An arbitrary symmetric N×N matrix of rank at most r over F_p can be represented WDW^T with W of dimension N×r and D symmetric r×r. Therefore the number of such matrices is at most
   (r+1) p^{Nr+r²}
(up to harmless rank padding). Consequently at most this many different score functions can have effective rank <=r.

Take N=K², p=O(K²), and r=floor(c K²/log_2 K) for sufficiently small fixed c. Then
   log_2((r+1)p^{Nr+r²}) < M/2
for all sufficiently large K. Thus among the 2^M independent 0/1 choices, at most 2^{M/2} have ρ_perm(B)≤r; all remaining instances have ρ_perm(B)>r. QED.

**Interpretation:** Even if one allows arbitrary "gauge" changes preserving the full quadratic score on EVERY permutation, generic PCC cannot be compressed to rank O(K/log K) or even o(K²/log K). This is a model-restricted lower bound, NOT a decision-only hardness theorem: different score functions may have the same YES/NO answer, and the compiler may use arbitrary nonlinear/global proof encodings.

## 6. Research impact and limitations

- A positive algorithmic result for rank-structured compatibility, with an exact CSP compression O(Kr+KlogK) and a one-sided randomized decision algorithm K^{O(r+1)}. The matching method itself is established algebraic technique; novelty of this particular parameterization was not surveyed exhaustively.
- If one assumes randomized PCC hardness RPCC-H (no 2^{o(KlogK)} randomized algorithm), any genuinely hard PCC input family must escape effective rank o(K), when equivalent low-rank factors can be found efficiently; a supplied low-rank certificate is polynomially checkable by the swap conditions.
- The generic score-counting obstruction means a universally small effective rank CANNOT be obtained merely by changing the quadratic form within its permutation-null affine space.
- The next meaningful algebraic problem is to identify STRUCTURED families where a low-rank equivalent matrix B' can be FOUND efficiently, or to find a nonlinear/decision-only compatibility interface bypassing exact quadratic-score preservation.
- This is separate from, and currently does not build, the critical O(K sqrt(log K))-test PCP. Improvements to this rank-based class of algorithms are algorithmic rather than sources of RPCC-H-hard sparse CSP.

## References

- Group-labeled matroid bases and determinant in a group algebra: *Problems on Group-labeled Matroid Bases*, https://arxiv.org/abs/2402.16259 ; Lemma 4.2 and Theorem 4.5 explicitly use Cauchy–Binet and a labeled determinant with randomized evaluation.
- General QAP linearizability recognition: Kabadi and Punnen, *An O(n^4) Algorithm for the QAP Linearization Problem*, Math. Oper. Res. 36(4), 754–761 (2011), https://doi.org/10.1287/moor.1110.0509 .
- Earlier model-specific PCC work: [PCC archive](14_permutation_clique_sparse_2csp_branch.md), [PCC short-PCP](36_pcc_short_pcp_alphabet_gap_barrier.md), [Fisher–Yates audit](39_fisher_yates_ram_trace_and_routing_bounds.md).
