# Direct generalization of our HOM Section 4: ALL sparse binary CSP -> ordinary 2-degenerate HOM with linear source

**2026-11-02, status: PROVED by a direct review/generalization of the reduction in Braulov--Chukhin--Kulikov--Mihajlin, arXiv:2607.09377v1, Sections 4.1--4.2, Lemmas 4.3--4.8. No novelty claimed for the underlying gadgets.** This completes the transfer *reduction* requested in note 34, conditional hardness remaining an independent open conjecture. The paper originally states Theorem 4.2 for SIMPLE BIPARTITE 3-REGULAR CSP because its hardness SOURCE (KMPS 2024) has that form. Its pinning construction and completeness/soundness proofs do NOT use bipartiteness or regularity.

## 1. Formal reduction theorem (PROVED from source-paper lemmas)

Let Gamma be a finite explicit binary CSP with v>=1 variables, m constraints on distinct pairs, common domain [q], and arbitrary allowed relations R_e subseteq [q]^2. Its variable graph need not be bipartite, regular, connected or bounded-degree; only v+m controls output size. Constraints on the same pair can be intersected, self-constraints converted to unary domain restrictions, and unary restrictions incorporated by omitting disallowed value states. Such preprocessing is polynomial, and does not increase m. If unary restrictions are allowed, treat this as part of the theorem.

There is a deterministic polynomial-time many-one reduction to a pair of finite simple loopless undirected graphs (G,H) with:

    Gamma SAT iff G -> H,
    |V(G)| = 255*v + 257*m + 251,
    |V(H)| <= 250*(v+m)+251+5*v*q+7*sum_e |R_e|,
    degen(H)<=2.

Here the displayed exact vertex count for G assumes one vertex per original variable, one per original constraint, distinct types for each, and the full frame with s=10(v+m)+10. For unary-restricted value sets, the target bound only improves. The bound on H counts S_3(H_0), not H_0. In particular |H|=O(v+m+v q+m q^2). Source edge count is also O(v+m). No lists are used.

### Source construction before subdivision

Let T=V(Gamma) disjoint-union E(Gamma), |T|=v+m; s=10|T|+10. Build the frame F_s from Section 4.1 of the paper, with vertices z_0,...,z_s and, for each i=1..s, a_i,b_i,c_i,d_i; ten edges per i: five making the 5-cycle on z_{i-1},a_i,b_i,c_i,d_i and five connecting z_i to each cycle vertex. Let the two pins of type t_j be p_t=z_{10j}, q_t=z_{10j+5}. Each type gets two separated pins; distinct types get distinct pins.

G_0=F_s plus:
- original-variable vertex x_u for each u, joined to p_u and q_u;
- original-constraint vertex y_e for e={u,w}, joined to p_e, x_u, x_w.

H_0=F_s plus:
- value vertex A_{u,a} for each allowed value a of u, joined to p_u and q_u;
- relation-state vertex R_{e,a,b} for each (a,b) in R_e allowed by the endpoints' unary restrictions, joined to p_e, A_{u,a}, A_{w,b}.

The paper's Lemma 4.4 says EVERY hom F_s -> H_0 FIXES every pin z_i for graphs formed with these safe attachments. The proof uses only the local attachment types and pairwise distinct original variable and constraint types, NOT the source constraint graph's 3-regularity or bipartiteness.

Given a satisfying CSP assignment alpha, map frame identically and x_u to A_{u,alpha(u)} and y_e to R_{e,alpha(u),alpha(w)}. Conversely, for phi:G_0->H_0, pinned frame forces x_u into the common neighbor of p_u,q_u, exactly one of the allowed A_{u,a}. For e={u,w}, the common neighbors of p_e, A_{u,alpha(u)}, A_{w,alpha(w)} are exactly the target relation-state vertices R_{e,alpha(u),alpha(w)}. This forces the allowed pair (orientation respected).

**CRITICAL:** m may be Theta(v) with arbitrary incidence degree; each CSP edge creates only ONE source relation vertex and three source edges. The original 3-regular assumption was used only to bound m=3v/2 and invoke KMPS; the same size result follows from m=O(v). For maximum degree <=3 we have m<=3v/2 anyway.

### Three-subdivision and 2-degeneracy

Let S_3(X) replace EACH edge of X by a path of length three. Put G=S_3(G_0), H=S_3(H_0). The paper's Lemma 4.7 proves for ALL finite loopless graphs:

    G_0 -> H_0 iff S_3(G_0) -> S_3(H_0).

The paper's Lemma 4.8 proves degen(S_3(H_0))<=2: every subdivision vertex has degree 2, and after removing all such vertices the original vertices are independent. No list-elimination dependence is hidden here.

### Exact size check

F_s has 5s+1 vertices and 10s edges. Hence

    |V(G_0)| = (5s+1)+v+m = 51(v+m)+51,
    |E(G_0)| = 10s+2v+3m = 100(v+m)+100+2v+3m,
    |V(G)|=|V(G_0)|+2|E(G_0)|=255v+257m+251.

For the target let P=sum_e |R_e|<=m q² (with unary restrictions one may replace vq by total allowed-value count). Then

    |V(H_0)|=(5s+1)+v q+P,
    |E(H_0)|=10s+2v q+3P,
    |V(H)|=(5s+1)+v q+P +2(10s+2v q+3P)
           =25s+1+5v q+7P
           =250(v+m)+251+5v q+7P.

Output can be written in poly(v+m+vq+mq²) time. It is undirected, loopless, and degen(H)<=2, indeed often exactly 2.

## 2. A small computational sanity check (DONE, does not replace the proof)

Implemented the literal F_s + x_u/y_e + A/R gadget on a NONBIPARTITE triangle CSP (v=3,m=3,q=2) with asymmetric equality/inequality relations. Observed |V(G_0)|=357, |E(G_0)|=715, hence |V(S_3(G_0))|=1787, exactly as predicted by 255v+257m+251. For each variable pin pair, its common-neighbor set in H_0 was exactly the two expected value states; for every oriented constraint and (a,b), the intersection of the three required neighborhoods contained exactly R_{e,a,b} if allowed and was empty otherwise. This checks the local soundness claims on a nonbipartite instance; global pin rigidity and 3-subdivision correctness rely on the cited mathematical lemmas, not just this test.

## 3. Conditional randomized no-single-exp HOM lower bound (PROVED logical implication)

Let S_c be the class of ALL max-degree-3 binary CSP on simple graphs with v variables, q=ceil(v^c) and m<=3v/2, for a fixed c>=1.

Assume rNSE-SCSP(c): there is **no bounded-error randomized 2^{O(v)}poly(L) algorithm** for ALL instances in S_c, for ANY fixed exponential constant. This is a NEW UNPROVED hypothesis; its deterministic analogue is strictly weaker.

Our above deterministic reduction maps every such input into ordinary HOM with

    n=|V(G)|=O(v), h=|V(H)|=O(v*q²+v)=v^{O(1)}, degen(H)<=2.

If a bounded-error randomized 2^{O(n)}poly(n+h) algorithm solved ALL such HOM instances, composing it with the deterministic reduction would contradict rNSE-SCSP(c). Thus:

    rNSE-SCSP(c) =>
    no bounded-error randomized 2^{O(n)}poly(n+h) algorithm for
    general ordinary HOM with degen(H)<=2 and h<=n^{2c+1+o(1)}
    (indeed for the more restricted output family), with no assumptions on |E(G)|.

The precise polynomial bound from the formula is h=O(v^{2c+1}); and since n>=255v, certainly h=O(n^{2c+1}). (Lower bounds with h bounded by n^{2c+1} up to a constant factor can be expressed with +epsilon in exponent if needed.)

When c=1, rNSE-SCSP(1) implies no randomized 2^{O(n)}poly(h) HOM algorithm even for degen(H)<=2, h=O(n³), and the constructed G has O(n) edges.

**IMPORTANT:** This is NOW an ACTUAL verified reduction transfer from the proposed assumption, not an unproved reduction template. However the assumption is NOT proved and we have not audited recent literature for a universal 2^{O(v)} randomized algorithm in the class. The new OpenAI full tensor theorem (if true) supplies a 2^{O(v sqrt(log v))} upper bound, which is fully compatible with rNSE-SCSP(c). Our own old ETH-derived lower bounds no longer establish this candidate.

## 4. Why we should avoid the old source-class mismatch

Theorem 4.2 in the paper is stated for bipartite 3-regular constraint graphs because Theorem 4.1 is a **hardness theorem for that restricted source class under ETH**. A hardness statement about *all* max-degree-3 binary CSP does **NOT** imply hardness of the bipartite 3-regular subclass. The correct fix is to observe and prove the gadget generalization in Section 1, which allows the currently proposed broad S_c to transfer directly without an unjustified restriction. Alternatively, define a stronger, separate assumption asserting hardness specifically for the 3-regular bipartite class and invoke Theorem 4.2 literally.

## 5. Implications for future work

1. **This reduction is solved.** Do not invest research time devising a new pinning or list-elimination gadget to meet |G|=O(v), h=poly(v), degen(H)<=2.
2. Main OPEN issue: Is rNSE-SCSP(c) plausible? Search for all known/claimed 2^{O(v)} algorithms for cubic CSP on polynomial alphabets, including using the latest post-ETH counting/tensor advances. Its consistency with a 2^{O(v sqrt(log v))} upper bound is NOT evidence of truth.
3. A stronger contribution would give a natural non-CSP hardness source implying rNSE-SCSP(c), or an algorithm that refutes it, and ultimately yield an independent win-win.
4. A negative or lower-bound outcome from this assumption is CONDITIONAL, not unconditional.
5. Cross-reference our existing [note 34](34_tensor_theorem_primary_source_audit_and_surviving_single_exp.md), [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md), and original [arXiv 2607.09377](https://arxiv.org/abs/2607.09377).
