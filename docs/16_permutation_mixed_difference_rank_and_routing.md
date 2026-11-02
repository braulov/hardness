# Permutation Clique: mixed-difference rank certificate and routing-network lower bound

**Research iteration 2026-11-02. Status: elementary algebraic lemmas with complete proofs; NOT a general CSP impossibility result, and no originality claim.** Complements docs/14_permutation_clique_sparse_2csp_branch.md and docs/15_quadratic_form_and_alldifferent_interface_barriers.md.

## 1. Setup and the proposed quotient rank

Let k=2s be even, let p be a prime with p>k (p>k^2 if the modular zero-test of the 0/1 forbidden-pair count is needed), and work over F_p.

Write X_pi in {0,1}^{k^2} for the flattened permutation matrix. For any k^2-by-k^2 coefficient matrix B, let f_B(pi)=X_pi^T B X_pi.

Let Z_k={K: f_K(pi)=0 for all pi in S_k}, and define

    r_perm(B)=min_{K in Z_k} rank(B+K).

The minimization is NOT known to be easy; its value controls only the bilinear-factorization compiler from doc 15, not general existential encodings.

Fix the subset of *block-preserving* permutations pi=sigma direct_sum tau, sigma,tau in S_s. Left rows and left columns are 1..s, and right rows and right columns are s+1..2s. Let A be the s^2 coordinates (i,a) in the left square and D the s^2 coordinates (s+j,s+b) in the right square. Denote

    C_B=B[A,D] + B[D,A]^T    (an s^2 by s^2 matrix).

Define the s^2-by-(s-1)^2 matrix T whose column indexed (i,a), 1<=i,a<s, is vec(E_{i,a}-E_{i,s}-E_{s,a}+E_{s,s}), the standard basis of the subspace W of s-by-s matrices with every row and column sum equal to zero.

## 2. Mixed-difference certificate (PROVED)

**Lemma.** The (s-1)^2-by-(s-1)^2 matrix

    H_B = T^T C_B T

depends only on the values of f_B on all permutations. In particular, H_{B+K}=H_B for every K in Z_k. Moreover

    r_perm(B) >= ceil(rank(H_B)/2).

**Proof.** For sigma,sigma',tau,tau' in S_s, the mixed finite difference of f_B on block-preserving permutations is

    f_B(sigma,tau)-f_B(sigma',tau)-f_B(sigma,tau')
      +f_B(sigma',tau')
      = (vec(P_sigma)-vec(P_sigma'))^T C_B
        (vec(P_tau)-vec(P_tau')).

If K vanishes on every permutation, all such mixed differences vanish for K. Differences of permutation matrices span W: every 2x2 cycle E_{ia}+E_{jb}-E_{ib}-E_{ja} is the difference of two permutation matrices that agree outside rows i,j, and these cycles span exactly all matrices with row/column sums zero. Thus T^T C_K T=0, proving invariance.

For any M=B+K with rank r, both M[A,D] and M[D,A]^T have rank at most r; hence rank(C_M)<=2r. Multiplication by T on both sides cannot increase rank. Therefore rank(H_B)=rank(H_M)<=2r, and minimize over K.

**Computation.** H_B has (s-1)^2 rows and columns; constructing it uses O(k^4) explicit arithmetic operations via a 16-term mixed difference of entries of C_B. Naive field Gaussian elimination uses O(k^6) operations. No factorial enumeration of permutations, no solution of the minimum-rank optimization problem. The lower bound is sound for every B, and the same idea applies to any balanced pair of independent row/column blocks.

No converse is claimed: a small H_B need not give a small r_perm(B), and even small r_perm does not imply fast decision for an arbitrary PCC instance.

## 3. An explicit forbidden-pair family with r_perm(B)=Omega(k^2) (PROVED)

Index each half by 1..s. Set all entries B to zero except

    B[(i,a),(s+j,s+b)] = [i=j][a=b]

for i,a,j,b in [s]. This is an admissible strictly row-upper-triangular 0/1 forbidden-pair matrix for a PCC instance. For pi=sigma direct_sum tau,

    f_B(pi)= #{i in [s]: sigma(i)=tau(i)}
           = <P_sigma,P_tau>.

Here C_B=I_(s^2), hence H_B=T^T T. For char p>k (in particular p does not divide s), the dot product is nondegenerate on W: W^perp consists of matrices of the form A_(i,a)=u_i+v_a, and W intersects W^perp trivially since s is invertible in F_p. Thus rank(H_B)=dim(W)=(s-1)^2 and

    r_perm(B) >= (s-1)^2/2 = Omega(k^2).

This is an obstruction to *every* bilinear rank-factorization of the exact quadratic objective modulo all permutation identities, not only to naive rank(B). It is still **not** a lower bound for arbitrary decision-preserving existential CSP, and the particular PCC instance is not computationally hard (it admits deranged sigma,tau).

By contrast, the pure AllDifferent collision matrix has raw rank k(k-1) but vanishes on all permutation vectors, so r_perm=0; see doc 15. Both extreme phenomena occur.

## 4. Literal permutation routing cannot use O(k) bounded-degree links at O(1) congestion (PROVED)

**Model.** A graph G of maximum degree Delta>=3 has k distinct input terminal vertices s_1,...,s_k and k distinct output terminals t_1,...,t_k (input/output sets may overlap). A realization of a permutation pi chooses for each i a path from s_i to t_{pi(i)}. Edge congestion counts the number of such paths using each edge, with multiplicity. Require that every pi in S_k can be realized.

**Lemma.** If Delta is a fixed constant and per-edge congestion is <=b, then |E(G)| b=Omega(k log k), with constants depending on Delta. In particular, a graph with O(k) edges cannot route all permutations with constant congestion.

**Proof.** For every input terminal, the number of graph vertices at distance <R is at most O((Delta-1)^R). Pick R=floor((log_{Delta-1} k)/2), so at most O(sqrt(k)) output terminals are closer than R. Under a uniformly random pi in S_k, each input's designated output is uniform among all k outputs. Expected number of pairs at distance >=R is k-O(sqrt(k)). Some permutation therefore has Omega(k) long source-output pairs. Any paths realizing that permutation have total edge-traversal length Omega(k log k). On the other hand congestion <=b implies total edge-traversal length <=b |E(G)|. Therefore b |E(G)|=Omega(k log k).

**Interpretation.** The O(k log k) Beneš network is asymptotically optimal for literal transport with constant-capacity edges and bounded degree. A polynomial-alphabet edge can hold O(1) literal packet labels (each label needs log k bits) under constant-factor domain exponent; transporting Omega(log k) independent packets through each of O(k) edges needs Omega(log^2 k) bits per edge, i.e. quasipolynomial domain. These bounds do NOT rule out more abstract distributed algebraic certificates that do not literally route tokens. They do justify avoiding another attempt to shrink Beneš by replacing switches with a fixed-degree O(k)-edge packet network.

## 5. Research consequences / candidate next experiment

1. Use rank(H_B) as a **cheap, exact, permutation-identity-invariant diagnostic**: an explicit high-rank certificate blocks the entire quadratic bilinear-factorization family; it does not say anything about the existence of decision-only CSP reductions.
2. Investigate special matrices with small mixed ranks for *every* balanced row/column split. Is this close to a tractable family, or can there be high-complexity obstructions invisible to all quadratic split certificates? Do not assume an equivalence.
3. Search for O(k)-constraint polynomial-alphabet gadgets for AllDifferent **not based on literal token routing, streaming fingerprints, or low bilinear rank**. Such a gadget would need nonlocal high-treewidth coherence.
4. For arbitrary PCC compatibility, pursue existential distributed proof systems with exact soundness and bounded query alphabet. Clarify why randomized sum-check verification cannot be existentially quantified over the random challenge without losing soundness.
5. If restricting to QAP-style costs, compare against the established QAP linearization/assignment-polytope literature before asserting novelty.

## Related literature (for context and priority audit)

- Kabadi and Punnen, An O(n^4) Algorithm for the QAP Linearization Problem (2011): https://doi.org/10.1287/moor.1110.0509
- The linearization problem of a binary quadratic problem and its applications (2021): https://link.springer.com/article/10.1007/s10479-021-04310-x
- Karthik, Marx, Pilipczuk, Souza, Conditional Lower Bounds for Sparse Parameterized 2-CSP (2024): https://arxiv.org/abs/2311.05913
- Lokshtanov, Marx, Saurabh, Slightly Superexponential Parameterized Problems (2011): https://doi.org/10.1137/1.9781611973082.60
