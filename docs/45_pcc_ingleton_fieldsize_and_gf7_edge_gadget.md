# Checkpoint 45 — PCC paving matroids are Ingleton; finite-field exact-linearization barrier; a one-edge determinant gadget

**Research date:** 2026-11-03. **Program:** PCC / PSCH linear-matroid compatibility.
**Status:** elementary PROVED theorems (two counting arguments use published Nelson's representable-matroid counting bound and a published characterization of Ingleton sparse paving matroids), plus an explicit rank-K linear construction for **one forbidden candidate pair**. The theorems rigorously distinguish exact matching-support or exact full-matroid representation from a decision-only PCC→linear-matroid compiler. No generic fast PCC algorithm/critical PCP constructed. Novelty relative to the wider matroid/determinantal literature not independently audited.

Related checkpoints:
- [43: determinant and exterior-algebra algorithms for explicitly represented linear-matroid matching](43_matroid_factor_matching_deterministic_2exp.md).
- [44: arbitrary PCC as oracle-specified rank-K sparse paving matroid, and Ω(K!) query lower bound](44_sparse_paving_matroid_pcc_oracle_equivalence.md).
- [20: independent Θ(K^4) PCC compatibility bits with different full solution sets](20_two_layer_affine_nonlinear_pcc_audit.md).

## 1. Every PCC-derived paving matroid satisfies Ingleton (PROVED)

For K≥4 let E=[K]×[K] and P={S_pi : pi∈S_K}, where S_pi={(i,pi(i)):i∈[K]}. For ANY subset C⊆P (not necessarily the invalid permutations of a graph), define rank-K sparse paving matroid M_C on E whose K-element nonbases/circuit-hyperplanes are exactly C. The matroid exists because two distinct permutation sets share at most K−2 elements, so C is a stable set of the Johnson graph.

**THEOREM:** Every M_C satisfies Ingleton's rank inequalities, including ALL M_A built from actual PCC inputs A.

Proof uses the Nelson–van der Pol characterization: a rank-K sparse paving matroid violates Ingleton iff there exist pairwise disjoint I,P1,P2,P3,P4 with |I|=K−4 and |P_j|=2, such that the five K-sets I∪Pi∪Pj for (i,j)∈{(1,2),(1,3),(1,4),(2,3),(2,4)} are nonbases, while the sixth I∪P3∪P4 is a basis. It suffices to rule out even the first THREE nonbases I∪P1∪P2, I∪P1∪P3, I∪P2∪P3. Since each is a permutation:
- I is a partial matching of K−4 distinct rows and columns.
- From the first two, the sets of rows occupied by P2 and P3 are BOTH the complement of the rows occupied by I∪P1; hence P2 and P3 occupy the same two rows.
- Then I∪P2∪P3 contains two positions per each of those two rows and cannot be a permutation, contradiction.
Thus no Ingleton witness exists. For K≤3, the rank-K sparse paving criterion similarly gives no rank-four witness; the nontrivial assertion is K≥4.

**Implication:** An Ingleton/Vámos-minor search can NEVER refute linear representability of one of these M_C. This does NOT prove linear representability; many Ingleton matroids are nonrepresentable.

Source: Nelson–van der Pol, *Doubly Exponentially Many Ingleton Matroids*, SIAM J. Discrete Math. 2018, and their sparse-paving Ingleton characterization; accessible summary https://matroidunion.org/?m=201710 ; DOI https://doi.org/10.1137/17M1160094 .

## 2. Ingleton is insufficient even for the arbitrary forbidden-permutation family (PROVED via Nelson counting)

For a fixed K, EACH subset C⊆P defines a DIFFERENT labeled matroid M_C, so the full family has 2^{K!} members.

Peter Nelson's published bound states that the number of representable matroids on a labeled n-element ground set **over ANY field** is at most 2^{2n^3} (a convenient coarse form, valid for n sufficiently large). For n=K², at most 2^{2K^6} representable matroids exist. Therefore a uniform random C⊆P yields a matroid NONREPRESENTABLE OVER EVERY FIELD with probability at least
    1 − 2^{2K^6−K!}
for sufficiently large K. ALL these matroids satisfy Ingleton by Section 1.

**Crucial scope:** Here C is an ARBITRARY SUBSET of K! permutations. Its membership oracle may require exponential data/time; C need not equal the invalid-permutation set of a PCC graph described by O(K^4) adjacency bits. Thus this all-fields nonrepresentability theorem does **NOT** prove that some polynomial-oracle PCC-derived M_A is nonrepresentable over every field. The latter explicit-source question remains OPEN in this note.

Source: Peter Nelson, *Almost all matroids are non-representable*, BLMS 2018, https://doi.org/10.1112/blms.12141 ; elementary bound and proof https://matroidunion.org/?p=1986 .

## 3. A strong FINITE-FIELD lower bound for actual PCC solution sets (PROVED)

Consider the relaxed exact *matching-support* representation: assign each candidate position (i,a) a vector v_{ia}∈GF(q)^d, with q a prime power, such that
    pi valid PCC iff {v_{1,pi(1)},...,v_{K,pi(K)}} is linearly independent,
for ALL pi∈S_K. Nothing whatsoever is imposed on other K-element subsets. The vector array may depend arbitrarily on the ENTIRE graph A and can be computed using any amount of preprocessing (the lower bound is purely information-theoretic).

**THEOREM:** There is an absolute c>0 and, for infinitely many even K, an explicit distribution on ordinary K×K PCC instances such that with probability 1−2^{−Ω(K^4)} EVERY exact linear-matching-support representation over ANY finite GF(q), with ANY dimension d≥K, must have
    d·log_2(q) >= c K².
The probability and c can be made fully quantitative; the number of allowed representation descriptions is what matters.

Proof:
1. Let K=2s. Partition rows into s regular and s filler rows; columns into s default and s active columns. Independently choose a forbidden bit beta_{ijab} for every pair i<j of regular rows and ordered pair a≠b of active columns. All other pairs are compatible. There are
       M=binom(s,2) s(s−1)=s²(s−1)²/2=(1/32+o(1))K^4
   independently variable bits.
2. These 2^M inputs induce DIFFERENT sets of satisfying permutations. To read beta_{ijab}, choose a permutation mapping i→a,j→b, each other regular row r to its distinct default column r, and filler rows arbitrarily to the remaining columns. No OTHER variable forbidden bit is activated on that permutation. Hence this permutation is valid iff beta_{ijab}=0.
3. For fixed d,q, the total number of K²-vector arrays over GF(q)^d is q^{dK²}, hence at most that many different exact PCC solution sets. For fields q with q≤Q, there are ≤Q different field orders (in fact far fewer), so the combined number is ≤Q^{dK²+1}.
4. For fixed sufficiently small c, union-count all dimensions K≤d≤cK² and all finite-field sizes with log_2 q < cK²/d. For each d the array-description budget is <cK^4 bits, and counting all possible q adds at most cK² bits, with only O(K²) dimensions. Thus the number of PCC solution sets admitting ANY such low-budget exact representation is at most 2^{cK^4+O(K²+log K)}. Choose c<1/64 to stay strictly below M=(1/32+o(1))K^4. The probability of a random beta string having such a representation is ≤2^{−Ω(K^4)}.
5. If d>cK² then d log_2q≥d>cK² automatically, so it need not be included.

This proves the theorem, UNIFORMLY over finite fields and dimension choices.

**Corollaries** (all exact matching-support, NOT decision-only):
  d=K           => q≥2^{Ω(K)};
  d=O(Klog K)   => q≥2^{Ω(K/log K)};
  q=K^{O(1)}    => d=Ω(K²/log K).
In particular, an exact representation of the full rank-K matroid M_A necessarily uses d=K up to span restriction and thus requires exponentially large finite fields on almost all instances of this family. An exponentially large field still has O(K)-bit elements and is NOT by itself too costly for polynomial-time arithmetic or an explicit polynomial-bit matrix; this does not settle decision-only compilation.

**Multiple layer generalization:** If one demands that pi is valid iff its K chosen vectors are independent in EVERY ONE of r given linear-matroid layers, of dimensions d_t over finite fields GF(q_t), the number of possible descriptions is at most
    2^{K² Σ_t d_t log_2 q_t + lower-order field/dimension metadata}.
For a bounded-polynomial number of layers and explicitly represented finite fields, the same hard distribution forces
    Σ_t d_t log_2 q_t=Ω(K²).
If every d_t=K and every q_t≤K^C for fixed C, necessarily
    r=Ω(K/log K)
for exact representation of almost every input. The bound even permits completely input-dependent vector tables.

**Important asymmetry:** The family in Step 1 is easy to satisfy because many default-column permutations avoid the independently variable forbidden pairs. This lower bound has ZERO implication for PCC decision hardness; it quantifies the cost of preserving all individual solution statuses.

## 4. An explicit GF(7), rank-K positive gadget for ONE forbidden candidate pair (PROVED)

Fix distinct rows i≠j and distinct columns a≠b in [K]. Suppose the ONLY restriction on a permutation pi is that NOT(pi(i)=a AND pi(j)=b). We construct v_{h,c}∈GF(7)^K, for every h,c∈[K], with
    det[v_{1,pi(1)},...,v_{K,pi(K)}]=0
      iff pi(i)=a AND pi(j)=b.

Let e_h be standard unit vectors indexed cyclically (e_{K+1}=e_1). Write epsilon=(-1)^K∈GF(7). Define
    v_{h,c}=e_h+theta_{h,c} e_{h+1},
where
    theta_{h,c} =
      1          if h=i,c=a
      2          if h=i,c≠a
      epsilon    if h=j,c=b
      3 epsilon  if h=j,c≠b
      1          otherwise.

The K×K column matrix is cyclic bidiagonal, so
    det[v_{1,x1},...,v_{K,xK}]
      =1+(-1)^{K−1} Π_h theta_{h,x_h}.
The product takes values epsilon, 2epsilon, 3epsilon, or 6epsilon depending on which of the two distinguished row selections is made. In GF(7) only the FIRST is epsilon; hence the determinant vanishes iff the specified forbidden pair is selected. For K=2 the formula remains valid by direct 2×2 calculation.

This is a **matching-support exact** linear-matroid representation of a nontrivial binary graph constraint, with dimension K and FIXED 7-element field.

**Testing:** Independently checked determinants over GF(7) for ALL K=2,3,4,5,6, every pair of distinct rows, every ordered pair of distinct columns and every permutation — 349,840 cases, all passed. Runnable experiment stored at ../experiments/45_single_forbidden_pair_linear_matroid.py.

**Scope:** It does NOT in general represent the full sparse paving M_A: some nonmatching K-element subsets can be linearly dependent. It also does NOT combine arbitrarily many forbidden pairs into a single matroid: representing a CONJUNCTION of constraints would require AND-composition of determinant nonvanishing, not supplied by the construction. Using a separate matroid per source forbidden pair is possible but vastly too expensive.

A useful abstraction: each row vector has the form e_i+theta_i(x_i)e_{i+1}, so the determinant encodes the GLOBAL MULTIPLICATIVE test
    Π_i theta_i(x_i) ≠ (-1)^K.
This connects with the previously analyzed fingerprint/accumulator models, while being a fully static exact finite-field representation for this specific pair predicate.

## 5. Decision-only path and next research goal

Suppose a polynomial-time compiler maps EVERY PCC(K) to a linear-matroid-constrained perfect matching on K rows and K columns with explicitly tabulated vectors in dimension poly(K) over a polynomial-bit finite field, preserving only YES/NO (not the exact valid-permutation set). Checkpoint 43 then implies a DETERMINISTIC 2^{O(K)} poly(K) algorithm for unrestricted PCC. This would refute the separate unproved RPCC-H hypothesis, but cannot be rejected solely by the counting arguments above.

Three precise open directions:
(A) Find a concrete PCC-derived M_A that is provably nonrepresentable over EVERY field; Ingleton cannot be the certificate.
(B) Find an efficient way to compose the one-pair GF(7) determinant gadgets **by AND** without one independent matroid layer per conflict, perhaps via added auxiliary matching positions or a different algebraic family.
(C) Search for a genuinely decision-only linearization that bypasses preserving each valid permutation; its success would be an algorithmic PCC breakthrough.

**Takeaway:** The broad exact matroid construction is structurally Ingleton-compliant, but generic PCC cannot be encoded by a compact finite-field exact vector array at rank K. A single forbidden pair has a surprisingly small explicit determinant gadget, pinpointing COMPOSITION as a central open difficulty rather than primitive local encoding.
