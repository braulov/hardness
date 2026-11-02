# Checkpoint 44 — Arbitrary PCC as sparse-paving matroid-constrained perfect matching

**Date:** 2026-11-02. **Branch:** PCC/PSCH and tractable global factors.
**Status:** Exact deterministic polynomial-time **oracle-model** reduction from arbitrary PCC to perfect matching independent in a rank-K sparse paving matroid, with an elementary Ω(K!) lower bound for any bounded-error randomized algorithm given ONLY the matroid independence/rank oracle. This is a specialization of the classical stable-set/Johnson-graph characterization of sparse paving matroids; priority NOT claimed. Contrasts sharply with [checkpoint 43](43_matroid_factor_matching_deterministic_2exp.md), where EXPLICIT LINEAR representations yield a deterministic 2^{O(K)} solver. No universal PCC compiler into explicit linear matroids and no general fast PCC algorithm is constructed.

## 1. Constructing the matroid from ANY PCC instance

Let E=[K]×[K] be the K² candidate positions. Each permutation π∈S_K yields a K-element subset
    S_π={(i,π(i)) : i∈[K]} ⊆E.
Let P={S_π:π∈S_K} and let C_A⊆P consist of all permutations which FAIL at least one pairwise compatibility constraint of the input PCC graph A.

**Key Johnson property:** For distinct π,σ, they differ on at least TWO rows, since a bijection cannot change just one image. Hence
    |S_π∩S_σ| ≤K−2.
In the Johnson graph J(E,K), whose two vertices X,Y of cardinality K are adjacent iff |X∩Y|=K−1, the collection P is a stable set; so is C_A.

Define a family of K-sets
    Bases_A = binom(E,K) \ C_A.
**Claim:** Bases_A satisfies the matroid basis exchange axiom and defines a rank-K sparse paving matroid M_A.

Direct proof: Bases_A is nonempty (any K-set which is not a permutation is a basis). For B1,B2∈Bases_A, choose e∈B1\B2. Suppose no f∈B2\B1 produces B1−e+f∈Bases_A. If |B2\B1|=1, that unique replacement IS B2, a contradiction. If |B2\B1|≥2, at least two distinct replacements B1−e+f are in C_A; these two K-sets have common (K−1)-set B1−e, contradicting stability of C_A. Hence exchange holds. The classical sparse-paving characterization guarantees this is a sparse paving matroid; equivalently all non-bases of cardinality K are circuit-hyperplanes and their Johnson code has minimum distance 4.

**Oracle:** For X⊆E,
 - |X|<K: independent, return YES;
 - |X|>K: dependent, return NO;
 - |X|=K: if X is not a permutation-set S_π, return YES; if it is, evaluate all binom(K,2) PCC compatibility constraints and return YES iff π is valid.
This is an independence oracle in poly(K) time. Its rank oracle can also be computed in poly(K): rank(X)=min(|X|,K) except rank(S_π)=K−1 when S_π is invalid and |X|=K.

**Reduction:** A PCC permutation π is a clique iff its set of selected bipartite matching edges S_π is independent in M_A. Thus
    PCC(A) YES
      iff there is a perfect matching of K_{K,K} independent in M_A.
The ground set has K² elements, matroid rank K, and oracle query time O(K²) after reading A. The reduction is polynomial-time in the explicit K^4-bit input and preserves the actual set of satisfying permutations exactly.

This theorem allows ANY PCC compatibility graph — no promise on rank, Boolean cover, Ferrers decomposition or degeneracy.

## 2. Ω(K!) oracle lower bound, deterministic AND randomized

Define M_0 by C_0=P (ALL permutation K-sets are declared non-bases). Then no independent perfect matching exists. For each hidden π∈S_K, define M_π by C_π=P\{S_π}; then exactly ONE perfect matching, S_π, is independent.

All M_0 and M_π are valid rank-K sparse paving matroids by Section 1 (their non-bases are stable in Johnson graph).

**Crucial:** The independence and rank oracles of M_0 and M_π give EXACTLY THE SAME ANSWER on every query X⊆E EXCEPT X=S_π. For |X|<K both have rank |X|, for |X|>K both have rank K, for any non-permutation K-set both have rank K, and for a permutation S_σ with σ≠π both have rank K−1. On S_π alone, rank is K−1 for M_0 versus K for M_π.

Thus a deterministic oracle decision tree must query all K! permutations in the worst case to distinguish M_0 from every M_π (or make at least K!−1 queries depending on conventions about promises and output at the last unseen possibility).

For bounded-error randomized algorithms, use a Yao-style distribution: input is M_0 with probability 1/2 and M_π with probability 1/2, where π is uniform in S_K. A deterministic q-query algorithm has identical transcripts on the two cases whenever it did not happen to query S_π, an event of probability at least 1−q/K!. Therefore its average error is at least (1−q/K!)/2. To achieve ≤1/3 error requires q≥K!/3.

Hence
    randomized bounded-error oracle query complexity = Ω(K!)=2^{Ω(K log K)}.
This also holds with full RANK-oracle access, not just independence queries.

**Limit of claim:** The lower bound is for an algorithm that receives the matroid ONLY via its independence/rank oracle. It does NOT apply to one given the explicit PCC adjacency matrix A, a linear representation of M_A, or any richer input-dependent certificate that leaks the hidden π. The constructed matroids need NOT be linearly representable over any small field.

## 3. Conceptual contrast and a precise win-win research target

- Arbitrary PCC reduces EXACTLY to an oracle-specified sparse paving matroid independence condition, with efficient oracle, but query algorithms require Ω(K!) in worst case.
- If one is additionally given an EXPLICIT linear representation v_{ia}∈F^d, d=poly(K), representing the relevant matroid-independence condition on permutation subsets, then [checkpoint 43](43_matroid_factor_matching_deterministic_2exp.md) solves the resulting task deterministically in 2^{O(K)}poly(K,d) time. This is a **radical** difference between general matroid rank oracles and linear representations.

If a polynomial-time decision-preserving compiler mapped EVERY arbitrary PCC input A to a polynomial-dimensional explicitly represented linear matroid M'_A and polynomial-size allowed-position mask on [K]×[K], with
    PCC(A) YES iff M'_A has an independent perfect matching,
then composing it with the deterministic algorithm of checkpoint 43 would yield an unrestricted deterministic 2^{O(K)}poly(K) algorithm for PCC. Under the working (UNPROVED) hypothesis RPCC-H, even the randomized version would contradict PCC hardness. Thus this proposed compiler is a potential **algorithmic breakthrough route** rather than a source of sparse-CSP hardness.

Note: The standard counting obstruction in checkpoint 43 rules out a SINGLE rank-K vector factor over a fixed polynomial field representing EVERY *individual permutation's* validity EXACTLY (there are 2^{Theta(K^4)} distinct PCC solution sets but only 2^{O(K³ logK)} possible rank-K matrices). That restricted counting barrier does not rule out decision-only reductions with polynomial-dimensional vectors and auxiliary preprocessing.

The central missing ingredient is **explicitly representable, sufficiently low-complexity linear dependence constraints that capture PCC compatibility on matching supports**. Sparse paving matroid axioms themselves cause no obstacle; expressible REPRESENTABILITY is the problem.

## 4. Existing literature and novelty caution

- The characterization of rank-K sparse paving matroids as complements of stable sets in Johnson graphs is classical; see Pendavingh–van der Pol, *On the number of matroids compared to the number of sparse paving matroids*, 2017, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i1p8/pdf/ ; and Ferroni, *Matroids are not Ehrhart positive*, Section 5.1, https://doi.org/10.1016/j.aim.2022.108337 .
- The broader oracle-hardness phenomenon is consistent with recent literature on matroid-constrained independent sets, e.g. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2024.22 . We have not surveyed whether this PARTICULAR PCC-to-paving-matroid reformulation was previously explicitly stated.

**Research verdict:** Genuine and simple universal ORACLE factorization of PCC, plus a matching Ω(K!) black-box query lower bound. This is a sharp explanation of why the factor program must prioritize algebraic representations (or decision-only algorithms) rather than arbitrary powerful independence oracles. Neither the general linearization nor the main PCC compiler is solved.
