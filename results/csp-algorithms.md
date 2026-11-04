# Exact algorithms for structured binary CSP

**PROVED.** Let I be an explicit binary CSP on v variables, m constraints, and domain [q], with input length L. Unary restrictions are allowed. Intersect parallel constraints and absorb self-constraints into unary restrictions. The primal graph is then simple. Polynomial factors below include table size and exact arithmetic. These are sufficient tractability criteria, not hardness measures; no priority claim is made.

## Expand only the non-tree relations

Let A_e be the 0/1 allowed-pair matrix of edge e and r_e its rational rank. A zero matrix makes the instance unsatisfiable. For any spanning forest F, exact counting takes

$$
\operatorname{poly}(L)\prod_{e\notin F}r_e.
\tag{1}
$$

Factor each chord matrix as A_e=U_e V_e with inner dimension r_e. Expanding only these chord factors gives

$$
\#I=\sum_{(j_e:e\notin F)} Z_F(j).
$$

For a fixed mode tuple j, each chord contributes a unary rational weight at each endpoint. The remaining binary interactions form a forest. Root each tree and compute messages

$$
M_{u\to p}(a)=\sum_b w_u(b)A_{up}(b,a)
                       \prod_{t\text{ child of }u}M_{t\to u}(b).
$$

Sum at roots and multiply component counts. Distributing the finite sums proves (1); negative terms are permitted and must be summed exactly.

For bit complexity, choose factorizations using nonsingular minors. Determinant bounds give polynomial-bit entries. Fix **one common denominator per chord** for all products U_e(a,j)V_e(j,b); the square of a common denominator for the two factors suffices. The product of these chord denominators has polynomial bit length and clears every summand simultaneously. Numerator sizes remain polynomial because each term has polynomially many polynomial-bit factors and the number of expanded assignments and modes has polynomial logarithm. This justifies polynomial bit cost per mode, including accumulation; it is not enough simply to count field operations.

Minimizing the exponent means maximizing Σ_{e∈F} log r_e. Kruskal's maximum spanning forest algorithm, sorting by r_e, does this exactly without evaluating logarithms. Thus the computable parameter is

$$
\mu_{\rm rank}(I)=\min_F\sum_{e\notin F}\log_2 r_e.
$$

Since r_e≤q, this is at most (m−v+cc)log₂q. Constant chord ranks on a sparse graph imply single-exponential exact counting.

### Boolean variant

If supplied allowed-pair covers satisfy R_e=⋃_{j=1}^{b_e}S_{ej}×T_{ej}, choose one rectangle only on each chord. Its two endpoint restrictions are unary; solve the forest by ordinary Boolean DP. The decision bound is poly(input plus covers)∏_{e∉F}b_e, again optimized by a maximum spanning forest. Overlapping rectangles prevent direct counting by summing these branches. Finding minimum covers is not assumed easy.

### A necessary negative control

When every relation is a permutation matrix on a connected cubic expander, μ_rank=Θ(v log q). Nevertheless, try q labels at one root, propagate uniquely along a spanning tree, and check the other edges. This is polynomial time. Large rank-cycle cost is **not** a lower bound on solving the instance.

## Other useful exact reductions

Repeatedly eliminate degree-zero, degree-one, and degree-two variables. A degree-two elimination replaces the two incident relations by their Boolean composition, intersecting an existing edge if necessary. It preserves the alphabet and satisfiability, and never increases μ=m−v+cc. The remaining minimum-degree-three graph has v'≤2μ and m'≤3μ. Detect UNSAT separately; μ=0 is polynomial-time decidable. This is a vertex/constraint bound, not a bit kernel independent of q.

Alternatively choose one endpoint from every nonforest edge. At most μ variables are chosen and their deletion leaves a forest; enumerate their labels to obtain q^μ poly(L) decision time. Bounded fibers along a supplied rooted spanning tree yield q∏_{e∈F}d_e time per component, where d_e bounds allowed child values given the parent. Both are standard conditioning arguments.

## Decision quotients can outperform exact rank

Suppose each domain has a supplied partition into classes C_{v,i}, and coarse relations S_e. Require forbidden coarse rectangles to contain no allowed fine pairs. In every allowed rectangle, assume a fixed value at the opposite endpoint forbids at most b_{e,v} candidates in C_{v,i}. If

$$
|C_{v,i}|>\sum_{e\ni v}b_{e,v},
\tag{2}
$$

every coarse solution lifts greedily in any order: previously assigned neighbors exclude fewer values than the class contains. Fine solutions project to coarse solutions. Decision therefore takes poly(L)∏_v r_v with r_v classes. This does **not** preserve counts.

For example R_e=S_e⊗(J_L−I_L), with invertible 0/1 S_e and L>Δ(G), has full rational rank q=rL but reduces to r-label CSP. For S_e=J₃−I₃ it reduces to 3-coloring, so the bound is 3^v poly(L), not polynomial time in general.

### Spectral version

For equally sized classes of size L₀, suppose every allowed block M satisfies

$$
\|M-\rho J\|_{op}\le\lambda,\qquad
L_0^2(\rho/2)^{2\Delta}>4\Delta\lambda^2/\rho^2,
\quad0<\rho<1.
\tag{3}
$$

Every coarse solution again lifts in deterministic polynomial time. For a current neighbor list S, at most 4λ²/(ρ²|S|) choices have fewer than (ρ/2)|S| neighbors in S, since
Σ_a(|N(a)∩S|−ρ|S|)²≤λ²|S|. Maintain all unassigned lists of size at least s*=L₀(ρ/2)^Δ. At the next vertex, at most 4Δλ²/(ρ²s*) values are bad for a remaining neighbor. By (3) this is less than s*, so choose a good value and update lists. Induction proves the claim.

Given rational ρ and λ², the norm certificate is checkable by exact rational positive-semidefiniteness testing. Finding a good partition is an additional task. In the bounded-defect model with r equal classes, ≤t zeros per allowed row/column, and distinct coarse classes separated on some incident edge, concatenated row signatures recover classes whenever L₀−t>2rtΔ: same-class Hamming distances are ≤2rtΔ, different-class distances ≥L₀−t. Verify the resulting certificate before using it.

Neither full rational rank nor many allowed neighbors excludes a small decision quotient. Conversely, arbitrary tables need not admit one.

Provenance: notes 13 (cyclomatic), 36 (structured algorithms), 37 (weighted cycle rank), 42–43 (quotients) in the [original tree](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs). The detailed Hadamard-block construction in old note 43 is retained in history as an explicit example, not needed for these algorithms.
