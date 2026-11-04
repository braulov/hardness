# Sparse binary CSP and ordinary 2-degenerate homomorphism

**PROVED.** This is a generalization of the construction in [Braulov–Chukhin–Kulikov–Mihajlin, arXiv:2607.09377v1, §4](https://arxiv.org/html/2607.09377v1#S4). Its proof was checked here; no new gadget or novelty is claimed. It is a decision reduction, not a parsimonious reduction.

## The reduction and exact sizes

For any explicit binary CSP with v≥1 variables, m constraints on distinct pairs, and domain size at most q, construct simple loopless undirected graphs G,H such that

$$
I\text{ satisfiable}\iff G\to H,
\quad n=|G|=255v+257m+251,
$$
$$
h=|H|\le250(v+m)+251+5vq+7\sum_e|R_e|,
\quad\operatorname{degen}(G),\operatorname{degen}(H)\le2.
\tag{1}
$$

The source has O(v+m) edges. Unary restrictions simply omit forbidden target values. Intersect parallel constraints first; convert self-constraints to unary restrictions. No lists, colors, or directed relations remain in the HOM instance.

## Pinning, including the global soundness argument

Give each variable and each constraint a distinct type, L=v+m in total. Put s=10L+10. The frame F_s contains z₀,…,z_s and four fresh vertices a_i,b_i,c_i,d_i for each i=1,…,s. Form the 5-cycle C_i=(z_{i−1},a_i,b_i,c_i,d_i), with z_i adjacent to all five cycle vertices. A type j uses pins p_j=z_{10j}, q_j=z_{10j+5}.

Add source variable x_u adjacent to p_u,q_u, and source constraint y_e adjacent to p_e,x_u,x_w for e=(u,w). The target has a value vertex A_{u,a} adjacent to p_u,q_u for every permitted value, and a relation vertex R_{e,a,b} adjacent to p_e,A_{u,a},A_{w,b} for every allowed pair.

Only the z_i with i≥1 have nonbipartite open neighborhoods in the target. All added neighbors of any z_i are isolated inside that neighborhood: distinct types have disjoint, well-separated pins, and relation vertices use endpoint types different from their own. The unique nonbipartite component in N(z_i) is C_i. Neighborhoods of other frame vertices remain bipartite; added value and relation vertices have independent neighborhoods.

For any homomorphism ψ:F_s→H₀, the image of C_i is an odd closed walk in N(ψ(z_i)); hence ψ(z_i)=z_{r_i} for some 1≤r_i≤s. For i≥2, the image of C_i must lie in C_{r_i}, whose only vertex among z₁,…,z_s is z_{r_i−1}. Thus r_{i−1}=r_i−1. The length-s chain forces r_i=i. Every used pin is fixed; z₀ need not be fixed and is not used as a pin.

The common neighbors of p_u,q_u are exactly the value vertices of type u. Therefore a homomorphism chooses one permitted value α(u) for each source variable. A common neighbor of p_e,A_{u,α(u)},A_{w,α(w)} can only be R_{e,α(u),α(w)}: frame vertices cannot see both differently typed values, value vertices have no value neighbors, and the pin fixes the relation type. This forces the allowed pair. Conversely every satisfying assignment gives a homomorphism by fixing the frame and choosing those value/relation vertices. Neither regularity nor bipartiteness of the CSP graph was used.

## Why length-three subdivision preserves HOM

Let S₃(X) replace each edge by a path of length three. The forward implication X→Y ⇒ S₃(X)→S₃(Y) is immediate. For the reverse, orient each edge ab of Y arbitrarily and write its subdivided path a–x–y–b. Define ρ(a)=a, ρ(b)=b, ρ(x)=b, ρ(y)=a. This defines a homomorphism S₃(Y)→Y, and the two neighbors of any internal vertex have the same ρ-image.

In any length-three walk w₀w₁w₂w₃, either w₁ is internal, giving ρ(w₀)=ρ(w₂), or w₁ is original and w₂ is internal, giving ρ(w₁)=ρ(w₃). Hence ρ(w₀)ρ(w₃) is an edge. Restricting ρ∘ψ to original vertices, for ψ:S₃(X)→S₃(Y), produces X→Y. This also handles backtracking walks.

Both subdivisions are 2-degenerate: remove internal degree-two vertices, leaving independent original vertices. With G=S₃(G₀), H=S₃(H₀), the frame has 5s+1 vertices and 10s edges. Thus

$$
|G|=(5s+1+v+m)+2(10s+2v+3m),
$$

and |H| is bounded by (5s+1+vq+P)+2(10s+2vq+3P), P=Σ_e|R_e|. These simplify to (1). Explicit construction is polynomial in the input and displayed output sizes; for polynomial q it is polynomial in v+m.

## The precise algorithmic equivalence

The following **families of algorithmic statements** are equivalent, separately for deterministic and bounded-error randomized algorithms:

* For every fixed c,a, sparse binary CSP with q≤v^c and m≤av has a 2^{O_{c,a}(v)}poly(L) algorithm.
* For every fixed d,a, HOM on 2-degenerate G,H with h≤n^d and |E(G)|≤an has a 2^{O_{d,a}(n)}poly(n+h) algorithm.

The reduction above proves the second statement implies the first, changing fixed exponents and constants. In the other direction, HOM is binary CSP with alphabet V(H) and one relation per source edge. If maximum degree three is required, split a variable into its occurrence copies and join them by an equality path. This uses O(v+m) variables/constraints, has degree at most three, and uniquely extends solutions. Isolated variables and empty domains are handled directly. Both reductions are deterministic and preserve decision error bounds.

The constants may depend on the fixed alphabet exponent and density. This is **not** a single universal exponential constant for arbitrarily growing target exponents, nor an equivalence for dense source HOM. No universal single-exponential algorithm or hardness hypothesis is proved.

## An unconditional counting baseline

For fixed target degeneracy d, orient H acyclically with outdegree at most d and label its outgoing slots by partial functions f₁,…,f_d. Expand each source-edge adjacency indicator as a sum of 2d directed-slot indicators. Cyclic source orientations contribute zero, because every prescribed target step increases the same topological order. In an acyclic term, guessing the source vertices determines the other labels along selected parent arcs; check all other constraints. The sources are independent, so there are at most α(G) guesses. Simplicity of H makes each homomorphism belong to exactly one slot term. The cost is (2d)^m h^{α(G)}poly.

Independently, enumerate images of a vertex cover of size τ(G)=n−α(G); all remaining choices are independent and their numbers multiply. Find a minimum cover by 2^n preprocessing and choose the better method. For h≥1,

$$
\#\mathrm{HOM}\text{ can be computed in }
2^{O_d(n+m)}h^{\lfloor n/2\rfloor}\operatorname{poly}(n,m,h).
$$

Empty graphs/targets are handled directly. This classical orientation/conditioning argument is independent of the recent tensor claims and is much weaker than a single-exponential bound for polynomial h.

Provenance: original notes 34 (HOM algorithms), 35 (general transfer), 37 (equivalence). See [audit scope](../AUDIT.md).
