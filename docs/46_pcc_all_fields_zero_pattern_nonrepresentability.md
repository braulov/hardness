# Checkpoint 46 — Almost every PCC-derived sparse paving matroid is nonrepresentable over ANY field

**Date:** 2026-11-03. **Status:** PROVED, nonconstructive zero-pattern counting theorem for actual explicitly described PCC graphs; stronger than the finite-field parameter bound of [checkpoint 45](45_pcc_ingleton_fieldsize_and_gf7_edge_gadget.md). Uses the established all-characteristics polynomial zero-pattern theorem (Rónyai–Babai–Ganapathy, via Nelson's explicit quantitative lemma). **Novelty of this particular restricted matroid family relative to the literature is not audited**. This is a rigorous restricted-model no-go, NOT a lower bound on arbitrary decision-only reductions and NOT a proof of PCC computational hardness.

## 1. Main theorem: no exact linear matching-support representation over ANY field

Let K be even, E=[K]×[K], and for every permutation pi write S_pi={(i,pi(i)):i∈[K]}. A *matching-support exact linear representation* of a PCC instance A means ANY field F, ANY finite ambient dimension d, and one vector v_{ia}∈F^d for each candidate position, satisfying for **every** pi∈S_K:

    pi is a valid permutation clique in A
        iff
    {v_{i,pi(i)} : i∈[K]} is linearly independent.

No constraint is imposed on the independence of non-permutation K-element subsets. This is strictly weaker than requiring the full sparse paving matroid M_A to be representable.

**THEOREM (PROVED):** There is an explicitly sampleable distribution of ordinary K×K PCC graphs such that, with probability
    1 − 2^{−Omega(K^4)}
for sufficiently large even K, the input admits **NO matching-support exact linear representation over ANY field and ANY finite dimension**. Hence its full PCC-derived rank-K sparse paving matroid M_A is also nonrepresentable over every field.

The graph A is generated in poly(K) time using Theta(K^4) independent unbiased bits. This theorem does NOT produce a deterministic explicit single hard A with a succinct human-checkable algebraic nonrepresentability certificate; it proves existence and efficient random sampling with exponentially high success probability.

### 1.1 Injecting Theta(K^4) independent bits into designated permutation statuses

Set K=2s. Split the K rows into s regular rows R and s filler rows, and columns into s default columns D and s active columns U. For every i<j among regular rows and every ORDERED a,b∈U with a≠b, independently choose beta_{ijab}∈{0,1}, indicating whether candidate pair (i,a),(j,b) is FORBIDDEN. All other candidate pairs are compatible.

Number of independent bits:
    M = binom(s,2) s(s−1)
      = s²(s−1)²/2 = (1/32+o(1)) K^4.

For each tuple b=(i,j,a,b) of such a bit, choose a designated permutation pi_b that assigns a,b to rows i,j; assigns each other regular row h to its own distinct default column (after indexing D correspondingly); and fills the remaining K−s columns bijectively into the s filler rows.

On this pi_b, the ONLY independently variable forbidden predicate activated is beta_b. So pi_b is a valid PCC witness iff beta_b=0. In particular beta→(PCC-validity(pi_b))_{b∈[M]} is a BIJECTION onto {0,1}^M.

All A in this distribution are trivially YES: map all regular rows to their default columns, and filler rows to all active columns. Thus the theorem has **zero immediate PCC decision-hardness consequences**.

### 1.2 Ambient dimension can be reduced to K over a field extension

Suppose vectors v_{ia}∈F^d give an exact matching-support representation. Because the instance has at least one YES permutation, necessarily d≥K.

Let Z=(z_{ht}) be a generic K×d matrix of algebraically independent indeterminates over F. For each YES permutation pi, the d×K column matrix V_pi has rank K; hence its projected determinant
    f_pi(Z)=det(Z V_pi)
is a NONZERO polynomial over F in the Kd entries of Z (e.g. some projection onto a nonzero K×K row minor makes it nonzero). There are finitely many YES permutations. Thus
    F(Z)=prod_{pi YES} f_pi(Z)
is a nonzero polynomial, since F[Z] is an integral domain. Work over the rational function field F(z_{ht}); then EVERY f_pi(Z) for a YES pi is nonzero. For a NO pi, rank(V_pi)<K, so its projected determinant is identically zero.

Consequently the K-dimensional projected vectors Z v_{ia} over F(z_{ht}) realize EXACTLY the same YES/NO statuses on **ALL** permutations. This reduction loses neither fields (arbitrary extensions are allowed) nor status information.

Therefore existence in arbitrary dimension over an arbitrary field is equivalent, for this exact matching-support question, to existence of a rank-K matrix representation over SOME field.

### 1.3 Apply the zero-pattern theorem to only M designated minors

Create a symbolic matrix X with K rows and N=K² columns indexed by E. Its nvar=K N=K³ entries are independent indeterminates over Z. For every designated permutation pi_b, define the integer polynomial
    g_b(X)=det(X_{S_{pi_b}}).
There are precisely M=Theta(K^4) such polynomials. Each has degree K and all coefficients in {−1,0,1}, hence integer coefficient height ≤1.

We ask which patterns
    {b: g_b(X) is NONZERO after specializing X over an arbitrary field}
can be realized as X and the field are varied.

**External theorem used:** the polynomial zero-pattern bound of L. Rónyai, L. Babai and M. K. Ganapathy, *On the Number of Zero-Patterns of a Sequence of Polynomials*, JAMS 14 (2001), 717–735. A convenient explicit all-fields lemma is reproduced by Peter Nelson in *Almost all matroids are nonrepresentable*, arXiv:1605.04288, and at https://matroidunion.org/?p=1986 :

For N_pol integer polynomials in m variables, degree ≤D, coefficient height ≤c, if integer t satisfies
    2^t > (2 t c (D N_pol)^D)^(N_pol * binom(D N_pol+m,m)),
then at most t different zero/nonzero patterns are realizable over **any field of any characteristic**.

Set:
    N_pol=M=Theta(K^4),   m=K³,   D=K,   c=1.

Let B=binom(D N_pol+m,m). Using
    B ≤ (e(D N_pol+m)/m)^m
gives
    log_2 B = O(K³ log K).
So
    N_pol B = 2^{O(K³ log K)}.
Choose t=2^{C K³ log K} with a sufficiently large absolute constant C. Then t is much larger than N_pol B·(log(2t)+D log(D N_pol)), so the lemma's inequality holds for large K. It follows that the number of realizable zero/nonzero patterns on these M minors across ALL FIELDS is at most
    t=2^{O(K³ log K)}.

But from Section 1.1 the PCC family demands ALL
    2^M=2^{Theta(K^4)}
distinct patterns. Therefore at most a fraction
    2^{O(K³ log K)−M} = 2^{−Omega(K^4)}
can have any exact K-dimensional representation over any field. Section 1.2 extends this to ANY finite dimension d.

**This is the central result.** Unlike the simpler finite-field q^{K³} count in checkpoint 45, it excludes all fields including arbitrarily large finite fields and infinite/rational-function fields.

## 2. Full sparse-paving matroid consequence and the Ingleton paradox

Each input A defines the rank-K sparse paving matroid M_A on the K² position elements whose circuit-hyperplanes are exactly the INVALID permutation sets S_pi; other K-element sets are all bases. Its independence/rank oracle is computable in poly(K).

If M_A had a linear representation over ANY field, then its restriction to permutation K-sets would satisfy the exact matching-support property of Section 1. Thus almost every M_A from Section 1.1 is **nonrepresentable over every field**.

But from [checkpoint 45, Section 1](45_pcc_ingleton_fieldsize_and_gf7_edge_gadget.md) all such M_A satisfy the Ingleton inequalities: the five-circuit forbidden configuration for Ingleton sparse paving matroids necessarily contains three pairs of two-element blocks forming a triangle, while three permutation K-sets cannot realize that triangle because row sets must alternately complement. Thus we have a **polynomial-oracle** family of nonrepresentable Ingleton sparse paving matroids with a simple probabilistic construction. Their nonrepresentability is proved by counting, not explicit Ingleton violations.

The previous generic count of ALL arbitrary forbidden-permutation subsets C⊆S_K, namely 2^{K!}, also proves that many of those oracle matroids are nonrepresentable; HOWEVER it did NOT show the phenomenon for actual polynomially encoded PCC inputs. The restricted-zero-pattern argument above DOES.

## 3. Precise implications for the ongoing linearization program

- **CLOSED (exact):** A universal transformation that only assigns one arbitrary-dimensional linear vector to EACH ORIGINAL PCC candidate (i,a) and requires
       valid(pi) iff the K chosen vectors are independent
  CANNOT exist — even allowing arbitrary fields, arbitrary preprocessing and completely input-dependent vector values, because many instances admit no such vector assignment at all.

- **CLOSED (full matroid):** Exact linear representation of the rank-K sparse paving M_A for ALL original PCC instances is impossible over every possible field family, not merely fields with polynomially many elements.

- **OPEN (decision-only):** A polynomial-time compiler outputting candidate vectors with
       PCC(A) YES iff SOME independent perfect matching exists
  is NOT excluded. In our hard-counting distribution ALL inputs are YES; a trivial uniform matroid suffices for decision, but it destroys exact solution status. The compiler may also alter the matching universe, introduce auxiliary choices, or preserve only existence.

- **OPEN (constructive explicit witness):** Produce a specific deterministically described PCC graph A, with a short inspectable nonrepresentability certificate valid over ALL fields, for its matching-support or full matroid. The random existence proof does not provide such a named example.

- **OPEN (global gadget composition):** [Checkpoint 45 Section 4](45_pcc_ingleton_fieldsize_and_gf7_edge_gadget.md) exhibits a single forbidden candidate pair encoded EXACTLY by one K-dimensional determinant over GF(7). This no-go explains why there can be no unconditional AND-composition mechanism that folds ARBITRARILY MANY such pair gadgets into one fixed-per-candidate linear factor while preserving validity of every original permutation. Some price in auxiliary encodings, solution relaxation or altered quantifiers is unavoidable.

## 4. Relation to algorithms and ETH-replacement work

Given an EXPLICIT linear matroid representation (in any polynomial dimension, with efficient field arithmetic), checkpoint 43 gives a deterministic 2^{O(K)} polynomial-time independent-perfect-matching solver. The present no-go blocks using such a representation as a universally exact encoding of PCC. It does NOT prove that a decision-only compiler is impossible or that RPCC-H is true; if such a compiler existed, it would instead yield a surprising unrestricted PCC algorithm.

This result is INDEPENDENT of the claimed 2026 OpenAI/Nguyen tensor/CSP algorithms and does not require ETH. Its mathematical prerequisites (Johnson-graph stable-set matroid construction and all-fields zero-pattern bound) are established pre-2026 theorems.

## 5. Primary citations

- L. Rónyai, L. Babai, M. K. Ganapathy (2001), *On the Number of Zero-Patterns of a Sequence of Polynomials*, JAMS 14, 717–735, DOI https://doi.org/10.1090/S0894-0347-01-00384-6 . The version used is the all-characteristics integer-polynomial zero-pattern theorem.
- Peter Nelson (2018), *Almost all matroids are nonrepresentable*, BLMS 50, 245–248, https://doi.org/10.1112/blms.12141 ; arXiv https://arxiv.org/abs/1605.04288 ; convenient theorem+proof at https://matroidunion.org/?p=1986 .
- Nelson–van der Pol (2018), *Doubly Exponentially Many Ingleton Matroids*, https://doi.org/10.1137/17M1160094 .
- Project checkpoints [20](20_two_layer_affine_nonlinear_pcc_audit.md), [43](43_matroid_factor_matching_deterministic_2exp.md), [44](44_sparse_paving_matroid_pcc_oracle_equivalence.md), [45](45_pcc_ingleton_fieldsize_and_gf7_edge_gadget.md).

**Bottom line:** With an elementary polynomial-time PCC witness-bit injection plus a classical all-fields zero-pattern counting theorem, we proved an unconditional nonconstructive **no exact linearization over any field** for almost every source graph in a concrete polynomially described YES-instance family. This is materially stronger than finite-field bit-counting, and cleanly identifies the only surviving general algorithmic route as **decision-only** or structurally richer existential encodings.
