# Checkpoint 41 — Boolean rectangle cover as a nonlinear additive feature parameter for PCC

**Date:** 2026-11-02. **Program:** PCC/PSCH, compatibility aggregation.
**Status:** PROVED elementary algorithms, equivalences, exact CSP compiler, and explicit high-ordinary-rank separation; verified by local exhaustive/randomized tests. The central branching idea is a standard independent-set / biclique-cover technique; **no literature novelty asserted**. The discovery of a small cover in arbitrary inputs is an additional NP-hard subproblem. No generic PCC algorithm faster than known baselines or universal critical PCP is claimed.

## 1. Input format and parameter

Consider K×K Permutation Clique. Let V=[K]×[K] be the K² candidate positions. A PCC witness is a permutation π selecting S_π={(i,π(i)):i∈[K]}. Let H be the UNDIRECTED *forbidden-pair graph* on V, with an edge {x,y} when the two distinct-row candidates x,y cannot coexist (whether equal columns are also declared forbidden is immaterial to valid permutations; to keep claims clean, exclude same-row pairs).

Suppose we are GIVEN a cover of E(H) by r complete bipartite subgraphs (bicliques):
     E(H)= union_{t=1}^r (L_t×R_t)
where each pair of candidate positions in L_t×R_t is a genuine forbidden pair, L_t∩R_t=empty, and the notation is undirected. Hence membership in L_t and R_t can be tabulated as two functions [K]×[K]→{0,1}. An equivalent oriented Boolean-matrix factorization of B uses at most 2r oriented rectangles. We do not assume the minimum such cover can be found in polynomial time; the algorithm's input is a supplied explicit cover, or any efficiently constructed cover for a promised class.

## 2. Deterministic 2^r poly(K) PCC algorithm (PROVED)

For each biclique t, any subset S of candidate vertices is independent in H only if S avoids L_t entirely OR avoids R_t entirely; conversely if this condition holds for every t then S contains no forbidden pair. This is the exact identity
  Independent_H(S) iff ∧_t [ (S∩L_t=∅) ∨ (S∩R_t=∅) ].

Enumerate every b∈{0,1}^r. Under b, delete all candidate positions in L_t if b_t=0 and all positions in R_t if b_t=1. Regard surviving positions (i,a) as edges of a bipartite graph between original rows i∈[K] and columns a∈[K]. Test if it contains a perfect matching (polynomial-time bipartite matching). Accept iff at least one of the 2^r branches does.

Correctness:
- If branch has a perfect matching, the selected K positions avoid at least one side of every forbidden biclique, so form an independent set in H, hence a PCC witness.
- If PCC has witness π, for every t choose b_t to exclude one side absent from S_π; that branch retains all positions of π and therefore has a perfect matching.

Running time O(2^r poly(K)), deterministic, no ring/character assumptions, no tensor theorem. The algorithm also reconstructs an actual permutation.

This is stronger than the previous group-algebra determinant algorithm on promised small Boolean cover: if r=O(log K), it is polynomial even when ordinary linear-algebraic rank of B is Θ(K²); if r=O(K), it is single exponential 2^{O(K)} given the cover.

### Nonlinear additive-feature interpretation

For every candidate position x=(i,a), form 2r Boolean features
  phi(x)=(1[x∈L_1],1[x∈R_1],...,1[x∈L_r],1[x∈R_r]).
For a selected permutation S_π, put
  c(S_π)=Σ_{x∈S_π} phi(x) ∈{0,...,K}^{2r}.
Then π is PCC-valid exactly when
  ∀t,  c_{L_t}(S_π)·c_{R_t}(S_π)=0
as an INTEGER equality. This is a nonlinear predicate on a sum of 2r *additive* features, precisely the mechanism sought after checkpoint 40.

The matching/branching algorithm avoids enumerating all (K+1)^{2r} possible sums: each disjunct allows us to delete one side and solve perfect matching, so runtime is 2^r rather than K^{O(r)}. This shortcut uses the monotonicity/OR structure of forbidden pairs; it is not valid for arbitrary quadratic forms or cancellation-based field fingerprints.

## 3. Exact polynomial-alphabet binary CSP compiler (PROVED)

For any PCC instance with a GIVEN r-biclique forbidden-edge cover, create:
- K variables x_i∈[K] encoding selected columns.
- r binary choice variables b_t∈{0,1}, each deciding to avoid L_t or R_t.
- For each t,i a binary relation R_{it}(x_i,b_t) that is satisfied iff (b_t=0 and (i,x_i)∉L_t) OR (b_t=1 and (i,x_i)∉R_t). Total Kr simple binary constraints.
- A deterministic exact AllDifferent extension for (x_1,...,x_K) using a Beneš/sorting network of O(K log K) constant-arity gates and polynomial alphabet. (Equivalently one can use the already proved fixed-network permutation gadget in PSCH notes.)
- Clone high-occurrence x_i,b_t variables by equality chains and convert constant-arity gates into binary tuple-state relations; output max degree <=3 and common alphabet Q=K^{O(1)}.

Thus there is a deterministic, SAT-iff and **exact source-solution-projection** compiler with
    v,m=O(Kr+K log K),  Q=K^{O(1)},  degree<=3.
Every valid original permutation admits at least one branch-choice extension; an invalid one admits none. Solution *counts* are not asserted preserved (there can be multiple b extensions of a valid permutation).

The construction is more direct than the rank-factorization checkpoint 40: it uses input-dependent boolean membership tables, existential 1-bit branch variables, and a standard exact AllDifferent network. At r=O(log K), all graph-compatibility checks fit within O(K log K) constraints and polynomial alphabet. It still does NOT achieve the critical O(K sqrt(log K)) total size because the standard AllDifferent network itself costs O(K log K).

## 4. Exponential separation from ordinary matrix rank (PROVED, explicit)

For K=2^h≥4, split rows and columns into two halves. Let
  L = { (i,a): 1≤i≤K/2, 1≤a≤K/2 },
  R = { (j,b): K/2<j≤K, K/2<b≤K }.
Each has K²/4 positions. Put r=log_2(K²/4)=2h−2. Identify each position of L and each position of R bijectively with a subset of [r]. Declare x∈L and y∈R forbidden iff their associated subsets intersect; all other pairs are compatible. Since rows AND columns used by L,R are disjoint, every forbidden cross-pair is actually co-selectable in some permutation (no spurious same-row or same-column restrictions).

For each t∈[r], the bipartite subgraph between
  L_t={x∈L:t∈S_x},  R_t={y∈R:t∈S_y}
is a biclique of forbidden pairs, and all forbidden pairs are covered. So an r=O(log K) cover is explicit.

In the order of candidate vertices [L,R,rest], the symmetric forbidden matrix is
     B=[ [0,M,0],[M^T,0,0],[0,0,0] ],
where M is the 2^r×2^r non-disjointness matrix M_{S,T}=1[S∩T≠∅].
The disjointness matrix D_{S,T}=1[S∩T=∅] factors as
     D=([ [1,1],[1,0] ])^{⊗r}
and is invertible over ANY field (base determinant −1). Since M=J−D differs by a rank-one matrix from invertible D, rank(M)≥2^r−1; the empty-set row is zero, so rank(M)=2^r−1. Hence over any field
     rank(B)=2(2^r−1)=K²/2−2=Θ(K²),
while the supplied biclique cover has only r=2log_2K−2=O(log K) terms.

Examples verified by modular Gaussian elimination:
  K=4, r=2, rank(B)=6;
  K=8, r=4, rank(B)=30.
Therefore the 2^r matching solver runs in polynomial time even for certain nearly full-rank forbidden matrices.

**Note:** This separation concerns raw rank versus Boolean biclique cover. It does not independently prove a lower bound on the *effective permutation quadratic rank* rho_perm of the same family; rho_perm could be smaller after changing B by identities vanishing on permutations.

## 5. Relationships and generic barriers (PROVED counting statements)

For an oriented Boolean matrix B=OR_{t=1}^s u_t v_t^T, arithmetic inclusion–exclusion over any field gives
     B = Σ_{∅≠I⊆[s]} (−1)^{|I|+1}
           (∏_{t∈I}u_t) (∏_{t∈I}v_t)^T,
so
     rank_F(B)≤2^s−1.
Thus Boolean rank can be logarithmically small even when ordinary rank is Θ(K²), and the construction above approaches this exponential discrepancy (accounting for orientation doubling in an undirected cover).

**Generic high-cover barrier:** There are 2^{Θ(K⁴)} distinct forbidden-pair matrices on Θ(K⁴) row/column-distinct candidate pairs. A cover by r undirected bicliques has a description of at most 2rK² bits (L_t and R_t membership bit-vectors over the K² positions), giving at most 2^{2rK²+O(r log r)} distinct matrices. Thus for some genuine PCC input matrices r=Ω(K²); under a uniform random choice of Θ(K⁴) independent forbidden entries, r=Ω(K²) with probability 1−2^{−Ω(K⁴)}. This is a model-specific encoding/counting barrier, NOT an unconditional or conditional complexity lower bound for decision-only PCC algorithms.

A more permissive coverage condition can ignore edges that no permutation can ever select, but there remain Θ(K⁴) freely variable *co-selectable* forbidden pairs (different rows and columns), so the same counting scaling holds for exact per-permutation forbidden-pair representation. Decision-only reductions can of course discard much more information; this rank/cover argument does NOT prohibit them.

**Finding the cover is separate:** Minimum biclique edge cover is NP-hard, and there are parameterized algorithms with significantly larger dependence on r. If r is a promised property but no cover is given, the bare O(2^r poly K) running time must not be claimed without an algorithm to construct it. Historical ETH-based hardness of *finding* biclique covers no longer supplies a safe premise after the 2026 claims; the structural NP-completeness results remain relevant.

## 6. Proof/tests/reference status

The matching branching algorithm was independently tested against a brute-force permutation search for 1200 random instances across K=3,4,5,6, each formed as a union of up to five random disjoint-row bicliques. Every result agreed. The explicit rank separation was checked for K=4 and K=8 by modular elimination. A reproducible Python experiment is stored at [experiments/41_pcc_biclique_cover_sanity.py](../experiments/41_pcc_biclique_cover_sanity.py).

**Relevant prior literature:** Chandran–Issac–Karrenbauer, *On the Parameterized Complexity of Biclique Cover and Partition*, IPEC 2016, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2016.11 ; Epasto–Upfal, *Efficient Approximation for Restricted Biclique Cover Problems* (2018), https://research.google/pubs/efficient-approximation-for-restricted-biclique-cover-problems/ .

## 7. Main research verdict

**A genuinely positive but structured compatibility mechanism:** Boolean rectangle covers give nonlinear additive features, an O(Kr+KlogK)-constraint exact sparse CSP, and a DETERMINISTIC O(2^r poly K) algorithm that can beat the ordinary-rank group-algebra method by an exponential factor in the parameter.

For arbitrary PCC, the biclique cover can be Ω(K²), and discovering a small cover is itself difficult. This does not solve the critical O(K sqrt(log K)) PCP nor give an unrestricted 2^{O(K)} algorithm.

**Next concrete target:** seek input-dependent covers by a SMALL NUMBER of more expressive, efficiently decidable "forbidden interaction" families, while retaining efficient feasibility after branching (perfect matching). This is a *tractable-union factorization* viewpoint, potentially strictly richer than ordinary rank and Boolean rectangle cover.
