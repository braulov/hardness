# Attacking rNSE-SCSP: mild-soundness PCP transfer and exact structured algorithms

**2026-11-02. New claims below are elementary derivations with proofs, NOT an algorithm for arbitrary cubic polynomial-alphabet CSP and NOT a proof of the new hardness conjecture.** Context: notes 33-35 show (conditional on an unverified full tensor-contraction theorem) a 2^{O(v sqrt(log v))} sparse CSP algorithm, and note 35 verifies an O(v)-source, degree-2 target HOM reduction. This note seeks a viable independent source for a **no 2^{O(v)}** randomized sparse CSP conjecture, or an algorithmic attack on it. Randomized algorithms and reductions are explicitly allowed.

## 1. Important weakened PCP requirement: any SUBCONSTANT soundness suffices for no-single-exp transfer (PROVED conditional)

Let PCC(k) be arbitrary k x k Permutation Clique, and **RPCC-H** the unproved assertion that no bounded-error randomized 2^{o(k log k)} poly(k) uniform algorithm solves every instance.

Suppose a polynomial-time, nonadaptive, two-query proof verifier for PCC(k) has:
- proof length ell<=a*k *symbols*;
- common alphabet Q<=k^b for constants a,b;
- input-dependent test distribution samplable in poly(k), local test positions and QxQ relation tables computed in poly(k);
- perfect completeness: on YES there exists ONE proof accepted by EVERY test in the support;
- soundness s(k) on every NO input: EVERY proof is accepted with probability at most s(k), where 0<s(k)<1 and s(k)->0.

By the union-bound sampling theorem in note 18, taking

    t=ceil((ell*ln Q + ln 6)/ln(1/s(k)))

independent tests produces a one-sided randomized equivalent binary CSP with O(ell+t) variables/constraints, degree<=3 after equality cloning, and polynomial alphabet. With ell=O(k), Q=k^O(1), and s=o(1),

    v'=O(k+k log k/log(1/s(k)))=o(k log k).

A bounded-error randomized 2^{A v'} poly(L) algorithm for ALL cubic polynomial-alphabet CSP (a suitably fixed polynomial exponent c, handled by alphabet padding) would therefore solve PCC in randomized 2^{o(k log k)} poly(k) time, contrary to RPCC-H. Thus:

    RPCC-H + the above SHORT-PCP with ANY s=o(1)
       => rNSE-SCSP(c) for a sufficiently large FIXED c.

This is a STRONGER useful consequence than note 18's earlier target s=k^{-Omega(1)} for an O(k)-size compiler. **The PCP itself has not been constructed.** One must not claim RPCC-H alone gives sparse CSP hardness.

Concrete values:
- s=1/2: t=O(k log k), insufficient for no-single-exp transfer;
- s=1/log k: t=O(k log k/loglog k)=o(k log k), SUFFICIENT;
- s=exp(-sqrt(log k)): t=O(k sqrt(log k)), SUFFICIENT;
- s=k^{-0.1}: t=O(k), SUFFICIENT but unnecessarily strong for this goal.

For fixed q'=v'^c, choose c>=b and add O(k) harmless padding positions so v'>=k if required, then extend each nonisolated edge relation to reject labels outside the original Q. This does not increase constraint degree or asymptotic size. Isolated proof positions may be dropped. Randomized errors can be amplified in the reduction and the proposed CSP solver before composition.

### Compatibility window with the externally CLAIMED tensor algorithm (PROVED conditional inequality)

Write g(k)=ln(1/s(k)), and take t=O(k log k/g). With q'=k^{O(1)}, the claimed deterministic CSP solver time is

    2^{O(v' log k/sqrt(log v'))}
      = 2^{O(k sqrt(log k) + k (log k)^(3/2)/g(k))}

for typical v'=Theta(k+k log k/g). If g(k)=omega(sqrt(log k)), the composed solver is 2^{o(k log k)}, contradicting RPCC-H. Therefore, **under BOTH RPCC-H and the full tensor theorem**, such a short PCP is impossible when g=omega(sqrt(log k)). But it may exist when

    1 << g(k) <= O(sqrt(log k)).

Examples s=1/log k and s=exp(-Theta(sqrt(log k))) lie in or at this window. This is an extremely precise target: subconstant error, but not as extreme as inverse-polynomial error. Any claim of an inverse-polynomial-soundness O(k)-symbol verifier under RPCC-H must acknowledge this conditional impossibility.

### Why Moshkovitz--Raz (2010) does not immediately yield it

Moshkovitz--Raz, "Two-Query PCP with Subconstant Error," gives almost-linear proof size **in the 3-SAT instance length**, rather than O(k) positions in the k log k-bit witness for arbitrary PCC. Directly encoding a k x k PCC instance as a general formula has Theta(k^4) adjacency bits and potentially much larger verification circuit size than k. Hence invoking their theorem produces an unsuitable proof-length bound; a **witness-length near-optimal PCP for explicit arbitrary compatibility tables** is the genuine missing step. Their two-query and s=o(1) properties alone do not suffice.

Reference: https://eccc.weizmann.ac.il/report/2008/071/.

A second alternative is a two-query, O(k)-symbol, CONSTANT-gap verifier whose full proof-failure-set system has VC dimension o(k log k), not necessarily O(k). An epsilon net of o(k log k) tests likewise transfers RPCC-H to rNSE-SCSP. This also relaxes note 18's previous VCdim O(k) objective.

## 2. Exact 2^{O(v)} algorithm for low rectangular-cover budget (PROVED)

Let I=(V,E,[q],(R_e)) be any explicit binary CSP. For each oriented edge e=(u,v) suppose a Boolean rectangle cover of its ALLOWED pairs is supplied:

    R_e = union_{j=1}^{r_e} A_{e,j} x B_{e,j}.

For each vector of rectangle choices (j_e)_{e in E}, every constraint becomes TWO unary restrictions x_u in A_{e,j_e}, x_v in B_{e,j_e}. Such a choice is satisfiable iff, for each vertex u, the intersection of the sets demanded by all incident chosen rectangles (and its preexisting unary allowed set) is nonempty. Thus an exact deterministic SAT algorithm runs in

    T <= poly(L+sum_e r_e*q) * product_{e in E} r_e.

Proof of correctness: If I has a satisfying tuple, choose for each edge a rectangle containing its satisfied pair; the tuple meets all resulting unary constraints. Conversely if all unary intersections nonempty for some rectangle choices, choose a value independently for each variable, which satisfies every chosen rectangle and hence all source relations.

For m=O(v), if r_e<=r=O(1) uniformly, this is 2^{O(v)}poly(L) independent of polynomial q. More generally sum_e log_2 r_e=O(v) suffices.

This is a different per-edge algorithm from the *global Boolean rectangle-cover* special case already in docs/psch/, and no originality is asserted.

## 3. Hybrid arbitrary-edge deletion / rectangle algorithm (PROVED)

Let F be exceptional edges whose relation tables may be arbitrary. Pick a vertex cover C of the subgraph (V,F), |C|<=|F| (for each exceptional edge simply choose one endpoint). Enumerate all q^{|C|} labels on C; check edges contained in C, and turn every edge meeting C into a unary restriction on its other endpoint. The remaining edges on V\C are all nonexceptional and have rectangle covers. Apply Section 2 within V\C. Runtime:

    T <= poly(L) * q^{|C|} * product_{e subseteq V\C} r_e.

(Edges entirely in C need only their original membership lookup.) If |F|=O(v/log q), m=O(v), and all other r_e=O(1), the algorithm is 2^{O(v)}poly(L). Thus a counterexample to rNSE-SCSP cannot be forced only by o(v/log v) arbitrary 'hard' edges among constant-rectangle edges: this entire class is single-exponential.

More generally we may minimize the weighted expression

    min_{C subset V} [ |C| log_2 q + sum_{e subset V\C} log_2 r_e ]

provided decompositions are available. Finding the optimal C is not claimed polynomial-time, but a specified C supplies a certificate of the running-time bound.

## 4. Exact spanning-forest branching for bounded fibers, plus rectangle chords (PROVED)

Suppose every edge relation R_e, considered from one endpoint to the other, has max fiber size d_e (for both orientations, or a selected rooted-forest orientation). Choose a spanning forest F of the primal graph. Guess one root value per component (q choices); traverse forest edges and branch among at most d_e allowed continuations. Check every nonforest relation on the resulting tuple. Components are independent, so total runtime is bounded by

    poly(L) * sum_{component K} [q * product_{e in F[K]} d_e].

In particular when d_e=O(1) along the selected forest, this is <=poly(L)q*d^{v-1}=2^{O(v)}poly(L), even if the omitted chord relations have arbitrary high rank/rectangle cover (they are simply checked, not enumerated).

A hybrid combines the schemes: for each nonforest edge e, expand an allowed rectangle cover of size r_e; this imposes unary restrictions. Then traverse the forest, branching at most d_e times on each forest edge. An explicit bound is

    T <= poly(L) * sum_{component K} q * (prod_{e in F[K]} d_e)*(prod_{e in E[K]\F[K]} r_e).

Correctness follows by the same witness-rectangle and forest-extension arguments. Both all-rectangle and all-bounded-fiber are valid special cases. There is no claim that finding the optimal forest and rectangle decompositions is easy. We verified the hybrid algorithm against brute-force enumeration on 300 random instances with n=3..7 and q=2..4; all answers matched.

## 5. Why these algorithms do NOT refute general rNSE-SCSP (PROVED barriers to the METHODS)

Every q x q binary relation can always be covered by q row rectangles, so the default rectangle algorithm takes q^m time. Uniform random binary q x q relation tables typically require Omega(q) rectangles: there are at most 2^{2qr} ordered r-rectangle descriptions, whereas there are 2^{q²} binary tables. For r<=q/4, the fraction representable is at most

    sum_{r<=q/4} 2^{2qr-q²} <= q*2^{-q²/2}.

Thus random tables are extremely far from constant rectangle-cover complexity. Equality also has rectangle cover exactly q but is trivially solvable by propagation, showing high cover is NOT hardness in itself.

For any graph G, the trivial q-row covers and vertex-cover enumeration give a baseline q^{tau(G)}poly(L) (enumerate a minimum vertex cover, check remaining unary constraints). On a 3-regular graph tau(G)>=|E|/3=v/2. Thus these direct representation-based algorithms are not uniformly single-exponential when q=poly(v) and the graph has linear treewidth/large vertex cover.

A blind random restriction of every variable to d=O(1) sampled labels has success probability (d/q)^v on a unique-solution input, requiring q^{Omega(v)} repetitions to retain the unique solution with constant probability. This is a barrier only to **input-oblivious domain thinning**, not an input-dependent algorithm.

## 6. High rectangular complexity does NOT imply hard instances: random dense tables (PROVED easy average-case)

Fix ANY n-vertex degree-Delta primal graph. For each edge e and ordered domain pair (a,b) independently include that pair in R_e with probability p (fixed p>0). Process source vertices in a fixed order. At each vertex u, choose any domain label compatible with all already assigned neighbors, querying only edges to those earlier neighbors. Conditional on the past, for every as-yet unchosen candidate a, the compatibility bits for edges to already assigned neighbors are fresh and independent; the candidate succeeds with probability p^d>=p^Delta. Different candidates have independent fresh bits. Thus

    Pr[greedy fails] <= v(1-p^Delta)^q <= v*exp(-p^Delta q).

For Delta=3 and p=1/2, failure is <=v exp(-q/8), which tends to zero rapidly for q=v^c. The algorithm is polynomial. Hence typical random HIGH Boolean-rectangle-rank relations are EASY, and hard instances must exploit adversarial correlations / structured constraints rather than merely large matrix rank or random-looking entries. This is a distributional theorem, not a worst-case solver.

## 7. Research synthesis

The currently useful dichotomy is not proved: cubic q=poly(v) CSP is 2^{O(v)} in several large structured regimes (constant rectangle budget, bounded fibers on spanning forests, at most O(v/log q) exceptional edges among easy relations, and random dense tables on average). These do not cover ALL tables.

A promising conditional HARDNESS source is RPCC-H plus a witness-length O(k)-symbol, two-query, subconstant-soundness PCP. This is MUCH weaker than the original inverse-polynomial PCP objective and compatible with the externally claimed 2^{O(v sqrt log v)} solver when soundness s is, for example, 1/log k. No construction is given.

For the algorithmic attack, search for a decomposition that combines small-width rectangular structure, bounded fiber propagation, dense random-like regularity, and exact local restrictions with a total cost exp(O(v)). An arbitrary-matrix theorem of this form would DISPROVE rNSE-SCSP and yield a single-exponential HOM algorithm for the reduction's sparse output family, but none is established.

## Literature

- Moshkovitz--Raz, "Two Query PCP with Sub-Constant Error" https://eccc.weizmann.ac.il/report/2008/071/ : two-query subconstant soundness with almost-linear proof in 3SAT instance size, not PCC witness size.
- Carbonnel, "Faster algorithms for graph homomorphism via tractable constraint satisfaction" https://arxiv.org/abs/2602.23000 : 2^{O(n)}poly(h) for H in classes excluding a fixed topological minor, NOT for arbitrary 2-degenerate targets (which may contain 1-subdivisions of arbitrarily large complete graphs).
- Nguyen, "A Sublinear Treewidth Exponent for Binary Constraint Satisfaction" https://hexagonmath.org/2611.00004v1 : claimed uniform q^{O(v/sqrt log v)} exact CSP counting; audit status in notes 22,33,34.
- Our original HOM reduction: https://arxiv.org/abs/2607.09377 ; full generalized bounds in note 35.

## 8. Why the 2026 single-exponential HOM theorem excluding topological minors does NOT solve our specific output family (PROVED)

Clément Carbonnel (2026, arXiv:2602.23000) gives a 2^{O(n)}poly(h) graph-HOM algorithm when the target family excludes some FIXED topological minor. The degree-2 targets H built by our paper's reduction (note 35) do NOT obey this condition in general.

Take a CSP with an edge e={u,w} whose allowed relation is ALL of [q]x[q]. The target H_0 from our HOM reduction contains q value vertices A_{u,a}, q value vertices A_{w,b}, and for each (a,b) a distinct relation vertex R_{e,a,b}, joined to A_{u,a} and A_{w,b}. Ignoring its third pin edge, these vertices form the **1-subdivision of K_{q,q}** as a subgraph. The final target H=S_3(H_0) replaces every edge by a length-three path, so still contains a subdivision of K_{q,q}.

For any t with binom(t,2)<=q, pick t vertices on the left part of K_{q,q} and assign each unordered pair a distinct right-part vertex. Join the two corresponding left vertices by their length-two path via its allocated right vertex. These paths have pairwise internally disjoint vertices. Hence the graph contains a subdivision of K_t, and so does H, for t=Theta(sqrt(q)). When q=v^c tends to infinity, the output family contains arbitrarily large complete graphs as TOPOLOGICAL MINORS despite degen(H)<=2.

Therefore Carbonnel's excluded-topological-minor theorem CANNOT directly be applied uniformly to our entire constructed H family. This is a concrete source of confusion worth avoiding: **2-degeneracy does not imply exclusion of any fixed topological clique**, and our actual target family witnesses the separation.

## 9. Deterministic row-density regime (PROVED)

As an additional very simple algorithm, if the primal max degree is Delta and for each edge e=uv and each fixed endpoint label a, at most gamma*q labels at the other endpoint are forbidden (in BOTH orientations), where gamma<1/Delta, then assign the vertices in ANY order. When choosing u, at most Delta previously assigned neighbors each forbid at most gamma*q labels, so fewer than q labels are forbidden in total; some legal candidate always exists. This finds a satisfying assignment in polynomial time. For Delta=3, gamma<1/3 suffices. This is a worst-case guaranteed row-density criterion, complementary to Section 6's random p=1/2 table theorem.
