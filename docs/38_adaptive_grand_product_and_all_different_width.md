# Adaptive grand-product failure and exact AllDifferent separator bounds

**Date:** 2026-11-02. **Project:** PCC/PSCH, augmented LTC and compatibility-layer research.
**Status:** Four self-contained elementary theorems about **restricted models**. They are applications of pigeonhole, NFA fooling sets and communication-rectangle/graph-separator arguments; novelty NOT established. None excludes an arbitrary randomized **decision-only** PCC→CSP compiler. They identify why a simple algebraic fingerprint / a low-width existential proof graph cannot solve the missing compatibility interface.

## A. Fatal adaptive-witness counterexample to the grand-product fingerprint

Let K>=4 and M be a *finite commutative monoid* of size R. For ANY map phi:[K]→M, if

    R < binom(K, floor(K/2)),

there is a NONPERMUTATION x∈[K]^K such that x_1=x_2 and

    product_{i=1}^K phi(x_i) = product_{j=1}^K phi(j).

**Proof:** Set h=floor(K/2). Each h-subset A⊂[K] has a product phi(A) in M. There are binom(K,h)>R subsets, hence two different h-subsets A,B have the same product. Replace the elements of A in the baseline permutation [K] by the elements of B. The resulting multiset has size K and unchanged total product (commutativity and associativity only; inverses NOT needed). Every symbol in B\A now appears twice, every symbol in A\B is absent. Since A≠B and |A|=|B|, B\A is nonempty; arrange a repeated symbol in positions 1 and 2. QED.

**Corollary (field evaluations):** For arbitrary public challenges r_1,...,r_t∈F_p and phi(a)=((r_j-a)_{j=1}^t) in the multiplicative monoid F_p^t, if

    p^t < binom(K,floor(K/2)),

there is a nonpermutation x with x_1=x_2 satisfying ALL t grand-product identities

    product_i(r_j-x_i)=product_{a=1}^K(r_j-a),  j=1,...,t.

The challenge values can be chosen by any randomized preprocessing, deterministic procedure, or as arbitrary functions of a *fixed public input*. For EVERY realized challenge tuple a malicious EXISTENTIAL witness x can adapt and pass.

In particular if p=K^{O(1)} then t=Omega(K/log K) is necessary for a single vector-accumulator test to be perfectly binding against all adaptive x. Equivalently the accumulator monoid/state space must have size

    p^t >= binom(K,floor(K/2)) = 2^{K-O(log K)},

so an individual finite-field-vector state cannot be a polynomial-alphabet CSP symbol.

**A FIXED NO source instance that always fools the scheme:** Take variables x_i∈[K], require AllDifferent(x_1,...,x_K) and the separate local condition x_1=x_2. The original instance is UNSAT. Replace only AllDifferent by the grand-product path with one or t public random evaluation points. For each realized seed the theorem supplies an x with x_1=x_2 satisfying the grand products. Set the intermediate prefix-product witness states deterministically to their true values; the target CSP is SAT for EVERY seed. This is stronger than a bad fixed-witness Schwartz–Zippel tail probability: the **existentially quantified witness chooses its values AFTER the seed is exposed**.

For a fixed nonpermutation x chosen BEFORE independent uniform r, polynomial identity testing indeed gives Pr_r[accept]≤K/p. This does not imply Pr_r[exists bad x accepted]≤K/p. This is the same quantifier-order distinction that motivates commitment-before-challenge in interactive permutation / grand-product arguments (e.g. https://triton-vm.org/spec/permutation-argument.html). The theorem is about PUBLIC challenges compiled into a normal existential CSP, not interactive protocols.

**Finite sanity checks:** K=6,p=11,t=1: for all 11 choices r there is an incorrect multiset matching the grand product; K=10,p=11,t=2: for all 121 pairs (r_1,r_2) there is one. At K=6,p=11,r=0, x=(3,3,1,4,4,5) is an explicit counterfeit (both sides have product 5 mod 11).

## B. Stronger barrier for ANY nondeterministic single-pass accumulator

Let Perm_K⊂[K]^K be the language of all K! permutations of [K], and let a layered, position-dependent nondeterministic finite automaton with Q states read x_1,...,x_K in order, accepting **exactly** Perm_K. Then

    Q >= binom(K, floor(K/2)) = 2^{K-O(log K)}.

**Proof:** Let h=floor(K/2). For each h-set A⊂[K] take the valid word w_A=sort(A)concat sort([K]\A) and choose any accepting run. Let q_A be the state at time h on that accepting run. If q_A=q_B for distinct A,B, splice the prefix of A's run to the suffix of B's run. This yields an accepting run on sort(A)concat sort([K]\B), which repeats some symbols and omits others, a contradiction. All states q_A must be distinct.

This includes arbitrary nondeterministic transitions, arbitrary nonlinear checks and arbitrary existential intermediate states, but the proof structure is ONE ordered chain of shared finite-state registers. In CSP terms, a chain of transitions R_i(s_{i-1},x_i,s_i), where the x_i are distinct designated terminals, cannot exactly project to AllDifferent with Q=k^{O(1)}. Each ternary transition may be compiled into a constant-size binary gadget; the bottleneck is the shared state between prefix and suffix. This is a familiar NFA fooling-set argument, not a claim about arbitrary high-treewidth CSP proof graphs.

## C. Treewidth lower bound for exact existential extensions of AllDifferent

**Theorem:** Let Ψ be ANY binary CSP with a graph H of treewidth w, alphabet size at most Q>=2, and K distinct designated variables x_1,...,x_K each having the source domain [K] (or fixed per-terminal decoding maps). Let all other variables be arbitrarily existential. Assume the projection of the satisfying relation to these K terminals is **exactly**

    AllDifferent_K = {(x_1,...,x_K): each value in [K] occurs once}.

Then

    w+1 = Omega(K/log_2 Q).

Proof uses only a standard terminal-weighted treewidth separator and the nondeterministic rectangle-cover fooling set:

1. Weight each original terminal by 1 and every auxiliary vertex by 0. A tree-decomposition centroid bag yields a separator S of size <=w+1 such that each component of H-S contains at most K/2 original terminals. If |S|≥K/12, the bound is already true. Otherwise, group components into sides A,B so each side contains at least K/4 source terminals, with no H-edge between the two sides. Let C=S∩{original terminals}, s=|C|<K/12.

2. Fix all s original terminals in C to s different values. The remaining permissible values constitute U of size K-s. Let a be the smaller of |A∩terminals| and |B∩terminals|; then a>=K/4 and a<=(K-s)/2.

3. For each a-subset T⊂U, build an accepting terminal pair (u_T,v_T) as follows: give the terminals of the a-sized side the elements of T in sorted order, and the terminals of the other side the elements of U\T in sorted order. The completed K-tuple is a permutation, so by exact extension it is accepted.

4. For different T,T', the crossed pair (u_T,v_T') is NOT a permutation: T≠T' have the same cardinality, hence at least one duplicated and one missing value. Therefore the binom(K-s,a) accepting pairs form a fooling set for rectangles.

5. For each fixed assignment to all separator variables S (respecting the fixed terminal assignments in C), the existence of extensions on sides A,B is an independent conjunction: a combinatorial rectangle. The projection to terminals is a union of at most Q^{|S|} such rectangles. Hence

    Q^{|S|} >= binom(K-s,a) >= 2^a >= 2^{K/4}.

Thus |S| log_2 Q>=K/4, while |S|≤w+1. Together with the |S|≥K/12 case this gives w+1=Omega(K/log Q). QED.

**Planar consequence:** a planar graph on n vertices has an O(sqrt(n))-size vertex-weighted balanced separator. Repeating the same rectangle argument directly gives

    n=Omega(K²/log² Q).

After dropping isolated auxiliary variables, n=O(K+m), where m is the number of output constraints. For Q=K^{O(1)}, exact planar AllDifferent extensions therefore need

    m=Omega(K²/log² K).

This is an elementary alternative to the expander-port planar separation example [earlier](psch/2026-11-02_planar_extension_separator_barrier.md); no novelty is claimed. The previous proof also gave a planar bound but for an O(K)-constraint **expander-port CSP** instead of the particularly natural global AllDifferent relation.

**Crucial restrictions:** Designated terminals and exact projection are mandatory. The source permutation may NOT be encoded by a graph-dependent global decoder spread across all target variables. Neither this theorem nor the one-pass NFA theorem precludes a decision-only arbitrary PCC compiler. Also, large treewidth is **necessary for some exact encodings but not sufficient** to build robust compatibility tests.

## D. Consequence for our augmented LTC + compatibility proposal

The natural "random field point + path of prefix products + local correctness checks" gadget is invalid as a standalone existential CSP even on the trivial UNSAT conjunction AllDifferent ∧(x_1=x_2). Replacing the field product with an arbitrary polynomial-state nondeterministic one-pass automaton also cannot exactly enforce AllDifferent. More generally, exact proof graphs of treewidth o(K/log K) cannot carry a polynomial-alphabet exact AllDifferent extension.

**Architectural requirement:** use genuinely non-chain, high-treewidth interactions OR a proof system in which a commitment is bound before the challenge and the soundness quantifier is proved accordingly. A publicly fixed random seed alone is not a binding commitment. The existing Beneš network encoding with O(K log K) edges is a valid exact high-width *candidate* infrastructure, but its improved O(K sqrt(log K)) or O(K) compression and a global input-dependent PCC compatibility verifier are OPEN.

**Important distinction:** A randomized PCP verifier chooses tests after a fixed proof is supplied; its usual soundness is Pr_test[reject proof] over each fixed proof. A randomized CSP **compiler** samples tests and then allows an existential assignment to depend on the sample. The PCP->CSP sampling theorem in [note 18](18_randomized_low_soundness_pcp_to_linear_csp.md) uses a union bound over all proof assignments to repair exactly this distinction; a single grand-product challenge without such uniformity is invalid.

## Sources / provenance

- Triton VM grand-product permutation argument and challenge ordering: https://triton-vm.org/spec/permutation-argument.html
- Fooling-set/rectangle-cover method: https://web.cs.ucla.edu/~sherstov/pdf/mfcs-disjointness.pdf
- Weighted separator framework: https://www.sciencedirect.com/science/article/pii/S0095895623000862
- Planar vertex-weighted separator theorem: https://planarity.org/Klein_separators_in_planar_graphs.pdf

**Bottom line:** Proved two explicit restricted-model obstructions and a robust structural lower bound for exact AllDifferent representations; no critical PCC PCP has been constructed.
