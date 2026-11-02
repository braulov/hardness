# Checkpoint 42 — Ferrers/chain forbidden factors, large-rank separation, and a rainbow frontier

**Research date:** 2026-11-02. **Branch:** PCC/PSCH, tractable-union compatibility interfaces.
**Status:** Self-contained elementary exact algorithm and CSP compiler for **supplied** chain (Ferrers) forbidden-edge factors; strong explicit separation from Boolean biclique cover and ordinary rank; reduction showing that ONE superficially similar color-equality factor is already NP-complete with unary allowed-position masks; and a mixed-factor randomized algorithm using the known Rainbow Matching algorithm. No general PCC compiler or critical PCP produced. Recognition/construction of a minimum factor cover is NOT assumed polynomial. Novelty against factorization/chain-graph literature has NOT been established.

## 1. Ferrers forbidden factors: model

A K×K Permutation Clique selects positions S_pi={(i,pi(i)):i∈[K]}. Assume the forbidden candidate-position pairs are exactly the union of r undirected factor edge sets E_t, with every factor supplied in this form:

- disjoint candidate-position sets L_t,R_t⊆[K]×[K];
- positive integer scores alpha_t:L_t→[M_t], beta_t:R_t→[M_t], M_t=K^{O(1)};
- edge {x,y} belongs to E_t precisely if x∈L_t, y∈R_t and alpha_t(x)>beta_t(y).

A factor is a bipartite CHAIN graph (Ferrers bigraph): its neighborhoods are nested by score threshold, and it contains no induced 2K2. The description is succinct, with O(K² log K) bits per factor, and is checked by comparing every listed forbidden pair if needed.

**Exact threshold lemma.** For any selected set S of positions, S contains no forbidden edge in E_t iff there exists tau_t∈{0,...,M_t} with
    x∈S∩L_t => alpha_t(x)≤tau_t,
    y∈S∩R_t => beta_t(y)≥tau_t.
Proof: no forbidden pair means max(alpha on S∩L)≤min(beta on S∩R). For empty left take maximum 0; for empty right take minimum M_t+1. Choose an integer tau between the two bounds.

**Theorem A (deterministic branching):** Given the above cover, PCC can be solved in
    poly(K) * prod_t (M_t+1) = K^{O(r+1)}
time, and a witness is obtained when one exists.

Proof: enumerate all threshold tuples; remove any candidate (i,a) violating any selected threshold; test perfect matching of the surviving row-column bipartite graph using Hopcroft–Karp or another standard polynomial algorithm. Every valid PCC permutation survives at least one tuple (threshold lemma), and every perfect matching surviving a tuple is compatible with all factors (no false positives).

**Theorem B (exact 2-CSP):** Introduce x_i∈[K] and t-th threshold variable tau_t∈[0,M_t]. For each i,t make the binary table
   R_it(a,tau)=
     ( (i,a)∉L_t or alpha_t(i,a)≤tau )
     AND
     ( (i,a)∉R_t or beta_t(i,a)≥tau ).
This is Kr binary constraints, total alphabets polynomial in K. Add the known O(K log K) exact AllDifferent/permutation network; copy high-degree variables by equality paths and compile constant-arity switch/compare gates into a fixed polynomial-size alphabet. The result is a degree≤3 binary CSP with
   m,v=O(Kr+K log K), Q=K^{O(1)}
whose satisfying projections onto (x_1,...,x_K) are **exactly the PCC-valid permutations**. Multiple tau witnesses may exist for one permutation; exact solution COUNT is not preserved.

As a familiar factorization, Ferrers relations are characterized by nested neighborhoods; the operation of **union** of Ferrers forbidden-edge factors is also equivalent to the complement of an **intersection** of Ferrers allowed-edge relations on the relevant fixed shores. Do NOT confuse this with edge-disjoint Ferrers PARTITION number.

## 2. Strong explicit separation: a single Ferrers factor needs Theta(K²) bicliques

Let K be even, N=K²/4. Pick L={(i,a):i,a≤K/2} and R={(j,b):i,j actually rows/columns both>K/2}, so |L|=|R|=N. Number L as x_1,...,x_N and R as y_1,...,y_N. Declare a cross-pair forbidden iff
     {x_i,y_j} forbidden  <=>  i>j,
and declare all other candidate pairs compatible.

All forbidden pairs are co-selectable in some permutation, because L and R use disjoint sets of rows AND columns. This is ONE Ferrers factor: alpha(x_i)=i, beta(y_j)=j.

**Boolean biclique-cover lower bound:** Consider the N−1 forbidden edges e_i={x_{i+1},y_i}, i∈[N−1]. If i<j, a biclique containing both e_i,e_j would have to contain crossed edge {x_{i+1},y_j}, but i+1≤j, so that edge is allowed. Thus distinct e_i cannot be in one forbidden biclique. This proves bc(H)≥N−1. Conversely, each of x_2,...,x_N yields a star covering all its forbidden edges, so bc(H)=N−1=Θ(K²).

**Ordinary rank:** The N×N cross-adjacency matrix M_{ij}=1[i>j] has rank N−1 over ANY field (row 1 is zero and the submatrix in rows 2..N, columns 1..N−1 is triangular with diagonal 1). The full symmetric K²×K² forbidden matrix has block structure [[0,M,0],[M^T,0,0],[0,0,0]], so rank(B)=2(N−1)=K²/2−2.

Thus
    chain-factor count=1,
    biclique-cover count=K²/4−1,
    rank(B)=K²/2−2.
A matching plus one threshold solves the instance in polynomial time; the previous 2^bc naive biclique-branching algorithm costs exponential in K². The separation is a property of the method, not a lower bound on ALL other algorithms using a biclique cover.

Small cases K=4,8 verified via exact matrix rank: N=4,16 and ranks 6,30.

## 3. General independent-set cover viewpoint

For each forbidden factor H_t on candidate positions, suppose we are explicitly GIVEN a family of b_t subsets I_{t,1},...,I_{t,b_t} of candidate positions such that for EVERY set S of positions:
    S is independent in H_t  <=>  there exists j∈[b_t] with S⊆I_{t,j}.
Equivalently the list can be all maximal independent sets of H_t; a promised correct list can be used, and completeness of an arbitrary supplied list is an additional verification question.

Then branching over choices j_t and testing perfect matching in the intersection of the chosen allowed position sets gives
    poly(K) * prod_t b_t
time. One can also introduce existential choice symbols j_t and Kr binary relations R_it(x_i,j_t)=[(i,x_i)∈I_{t,j_t}], obtaining an exact-projection degree-3 CSP of
    O(K sum? no: K*r+KlogK) constraints
and alphabet at most max(K,b_t)^{O(1)}, provided b_t=poly(K). If b_t are huge, the input and alphabet are not polynomial, so the stated polynomial-domain CSP guarantee does not apply.

Ferrers H_t has an explicit independent-set cover with b_t≤M_t+1 (its threshold upper/lower cut classes), and a biclique has b_t=2 (avoid the left or the right side). This is a systematic **tractable-union factorization**. Merely having "r arbitrary factors" is not sufficient: b_t may be exponential.

## 4. Warning: ONE color-collision factor is already NP-complete

Take a set A⊆[K]×[K] of allowed candidate positions and one color c(i,a) assigned to each allowed position. Forbid pairs of selected candidates iff their colors are EQUAL. Find a permutation selecting only allowed positions with all chosen colors different. This is RAINBOW PERFECT MATCHING in a simple edge-colored bipartite graph. The corresponding equality-color forbidden graph is a union of disjoint cliques (one per color), NOT necessarily a single Ferrers graph.

NP-hardness from the established NP-completeness of size-k RAINBOW MATCHING in bipartite simple edge-colored graphs:
Given bipartite X∪Y, |X|=m, |Y|=n, and target k≤min(m,n), create a balanced bipartite graph with left vertices X plus n−k new dummy rows and right vertices Y plus m−k dummy columns. Its side size is K=m+n−k.
- Preserve original colored X→Y edges.
- Add every X→dummy-column and dummy-row→Y edge with a BRAND-NEW private color for each such edge (different from all original colors).
- Add NO dummy-row→dummy-column edges.
Every perfect matching necessarily uses exactly k original X→Y edges: all n−k dummy rows use Y columns, all m−k dummy columns use X rows. Every rainbow matching of size k in the original graph extends to a rainbow perfect matching using the unique-colored dummy edges; conversely every rainbow perfect matching restricts to k original pairwise vertex-disjoint, pairwise color-distinct edges. This proves polynomial-time equivalence and NP-hardness for a SINGLE color-collision factor plus unary allowed-position restrictions. Membership in NP is immediate.

Thus replacing bicliques by arbitrary "one describable relation" is not a valid tractability theorem. Some one-factor types are genuinely hard. This reduction was independently sanity-tested on 630 small random size-k Rainbow Matching instances against brute permutation enumeration.

Known underlying source: NP-completeness of Rainbow Matching for bipartite colored graphs, see Gupta–Roy–Saurabh–Zehavi, MFCS 2017, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2017.71 , and the cited Itai–Rodeh–Tanimoto reduction.

## 5. A hybrid tractable-union algorithm and CSP compiler

Suppose forbidden interactions consist of:
- r supplied Ferrers factors as in Section 1;
- ONE equality-of-color factor with c(i,a)∈poly(K) distinct colors and allowed positions A.

For each tuple of Ferrers thresholds, delete all disallowed candidate positions and solve the remaining RAINBOW PERFECT MATCHING problem. The known randomized O*(2^K) algorithm for maximum rainbow matching on general graphs (Gupta et al. MFCS 2017, and earlier algebraic sieving) implies a one-sided randomized algorithm with
    time 2^{O(K)} prod_t(M_t+1) poly(K)
         = 2^{O(K+r log K)} poly(K),
given the factorization. Fix a nonzero constant success probability for YES and no false positives; repeat to amplify.

There is also a **deterministic exact source-solution-projection CSP compiler** of
    m,v=O(Kr+KlogK), max degree≤3, Q=K^{O(1)}.
For the color layer, add y_i=c(i,x_i) lookup constraints for allowed positions and enforce AllDifferent both on the chosen COLUMN labels x_i and on the selected COLOR labels y_i using two O(KlogK) sorting/permutation networks (the second network is a distinctness test on polynomial-range colors, not a permutation assertion). Add the Kr Ferrers-threshold relations. Normalize degrees via equality paths.

At r=O(K/log K), this gives a **single-exponential randomized PCC algorithm** and an O(K²/log K)-size exact CSP; at r=O(log K), it gives an O(Klog K)-constraint exact CSP and 2^{O(K)} randomized decision algorithm. The color layer is NP-hard, so one should not claim a polynomial-time algorithm from a constant number of arbitrarily expressive factors.

## 6. Generic high Ferrers-cover barrier (counting only)

Let N=K² candidate positions, and consider the Θ(K⁴) co-selectable unordered candidate pairs with different rows and different columns. They can be independently forbidden, so there are 2^{Θ(K⁴)} exact conflict matrices.

A Ferrers factor is described by L,R memberships and score maps alpha,beta bounded by poly(K); this costs O(N log K)=O(K²log K) bits per factor. An r-factor description therefore has only 2^{O(r K²log K)} possibilities (up to encoding r and constants). Thus there are exact PCC forbidden matrices needing
    r=Omega(K²/log K)
Ferrers factors, and a uniform random choice of all co-selectable forbidden bits has this lower bound with probability 1−2^{−Ω(K⁴)} for sufficiently small implicit constant.

This is strictly a lower bound for EXACT forbidden-pair representation. It does NOT exclude decision-only compilers where a different relation has the same satisfiable/unsatisfiable answer. Likewise an optimal Ferrers cover need not be efficiently discoverable in arbitrary instances.

## 7. Research verdict and next step

We now have TWO genuinely different polynomial/parameterized interfaces:
- Boolean biclique cover: 2^r poly(K) decision, O(Kr+Klog K) CSP;
- Ferrers/chain cover: K^{O(r)} decision, O(Kr+Klog K) CSP, and ONE chain factor can replace Θ(K²) bicliques, with ordinary rank Θ(K²).
We may include a rainbow color-collision layer, obtaining 2^{O(K+r logK)} randomized time and the same asymptotic exact-CSP size.

The next nontrivial problem is **finding** a low-complexity factor cover or a still richer factor class with efficient independent-set-cover enumeration, for nontrivial dense PCC families. The generic counting barrier says a uniformly small exact representation is impossible; decision-only input-dependent compilation remains open.

This is a structural/algorithmic subfamily, NOT a breakthrough to arbitrary PCC, not a refutation of RPCC-H or PSCH, and not a new PCC PCP of size O(Ksqrt(log K)).

## References
- Chain graphs = bipartite 2K2-free with nested neighborhoods, https://mathworld.wolfram.com/ChainGraph.html .
- Ferrers relations and dimension, https://page.math.tu-berlin.de/~felsner/Paper/loc-bip.pdf . NOTE: Ferrers **dimension** often means INTERSECTION of Ferrers relations, whereas the direct forbidden-edge representation here is a UNION.
- Chain-subgraph coverings and partitions, https://combinatorialpress.com/ars-articles/volume-166/edge-partitions-into-induced-2k2-free-bipartite-graphs/ .
- Rainbow Matching NP-completeness and randomized O*(2^k), https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2017.71 .
- Previous checkpoint 41, [Boolean biclique cover](41_boolean_biclique_cover_pcc_compatibility.md).
