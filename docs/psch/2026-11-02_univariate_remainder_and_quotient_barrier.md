# A univariate algebraic formulation of ordinary Clique and a quotient-certificate barrier

**Date:** 2026-11-02. **Branch:** PSCH / B, universal-selector elimination.
**Status:** Elementary statements below are proved in the specified model (a computer check of the first equivalence covered all 64 graphs on 4 vertices and all 4^3 ordered 3-tuples over GF(7)); no claim of publication-level novelty. The universal sparse 2-CSP compiler remains **OPEN**.

## 1. One-variable divisibility criterion (proved)

Let G be any *simple undirected* graph with N vertices, indexed by pairwise distinct field elements a_1,...,a_N of F_p, p>max(N,k). Set B(a,b)=1 if a=b or {a,b} is not an edge, and B(a,b)=0 otherwise. For each a, define D(a,Y) as the unique polynomial of degree <N interpolating the function b↦B(a,b) at all vertex labels. A full bivariate interpolation D(X,Y) may be used but is unnecessary for the criterion.

For an ordered k-tuple x=(x_1,...,x_k) of vertex labels, define
    P_x(Y)=prod_{i=1}^k(Y-x_i),
    C_x(Y)=sum_{i=1}^k D(x_i,Y).
Then
    x is a k-clique (all vertices distinct and pairwise adjacent)
    iff P_x divides (C_x-1) in F_p[Y].

Proof: If x is a clique, at every selected root x_j we have C_x(x_j)=1 (only diagonal B(x_j,x_j) contributes); since the x_j are distinct, P_x | (C_x-1). Conversely, if P_x | (C_x-1), then for every j, C_x(x_j)=sum_i B(x_i,x_j)=1 in F_p. The latter is an integer in [1,k], and p>k, hence it is exactly 1 over the integers. Therefore for i≠j the B(x_i,x_j) all vanish, which means selected vertices are distinct and pairwise adjacent. This also handles repeated roots in NO-tuples: divisibility implies vanishing at all roots, which is already impossible for repetitions.

This uses a *univariate* remainder of degree < k, rather than a generic bivariate remainder with k^2 coefficients. However, this should **not** be described as compressing the verification work or the number of necessary scalars beyond every prior encoding: there was already the single-scalar nonnegative-violation sum.

## 2. The scalar trace unifies this identity with the earlier count (proved)

Take p>max(N,k(k-1)). Let A_x=F_p[Y]/(P_x). For any f(Y), the trace of the F_p-linear map multiplication by f in A_x is
    Tr_{A_x/F_p}(m_f)=sum_{j=1}^k f(x_j),
where roots are counted with multiplicity; it holds even when P_x has repeated roots (use a triangular form of multiplication or the companion matrix).

For f=C_x-1, this is
    Tr(m_{C_x-1}) = sum_{i,j} B(x_i,x_j) - k,
exactly the ordered-pair violation count from the corrected sum-check. As an integer this lies in [0,k(k-1)], so with p>k(k-1) trace zero iff x is a clique.

Thus the univariate divisibility form helps organize the algebra, but eliminating the universal test still requires evaluating a graph-dependent dynamic remainder or trace, which is the essential hard step.

## 3. Quotient diversity on YES instances (proved)

Fix N>=k+1 and one k-element set S={s_1,...,s_k} which is a clique. Set all edges between S and outsiders present, except allow each edge {s_1,v}, v∉S, to be independently present/absent. Keep all other choices fixed. There are 2^{N-k} YES graphs with the *same selected clique S*.

For all such graphs, f_G(Y)=C_S(Y)-1 vanishes at each label in S, hence Q_G(Y)=f_G(Y)/P_S(Y) is a polynomial of degree <N-k. For outsider v, C_S(v)=0 if {s_1,v} is present and C_S(v)=1 if it is absent, so
    Q_G(v) = (-1 or 0)/P_S(v).
Since P_S(v) ≠ 0, these two field values differ. Therefore distinct external-edge patterns give distinct Q_G and the set of possible quotient polynomials has cardinality exactly 2^{N-k}.

An explicit coefficient-vector witness for Q_G requires at least N-k bits in the worst case just to identify which quotient it is. Over a field p=k^{O(1)}, it cannot always be represented by O(k polylog k) field coefficients when N=k^2.

A stronger syntactic claim: a fan-in-two arithmetic *straight-line program* with a single input Y and field constants from F_p, producing Q_G as a formal polynomial, has at most (poly(p,s))^s possible descriptions when it uses s gates. Hence describing all 2^{N-k} quotients requires
    s log(ps)=Omega(N-k).
For N=k^2, p=k^{O(1)} and s<=poly(k), SOME quotient Q_G needs s=Omega(k^2/log k) gates.

This is a valid **worst-case representational lower bound for direct quotient circuits**. It does NOT rule out: a short *proof* of mere divisibility without representing Q; an input-dependent precomputed table that directly embeds arbitrarily many graph bits; a CSP encoding with arbitrary auxiliary witnesses and globally compiled binary relations; cryptographic computational commitments; or a decision-only reduction. It is also just a basic counting lower bound, not claimed novel.

## 4. What precisely remains

We require a deterministic polynomial-time transformation from *ordinary* k-Clique on N<=k^2 vertices to an unquantified 2-CSP with m=O(k polylog k), Q=k^{O(1)}, degree<=3, preserving YES/NO. The existential-forall-existential selector formulation in [the previous note](2026-11-02_universal_selector_qcsp.md) has m=O(k) already, but it is not a standard CSP.

Our divisibility identity replaces the universal selector with a polynomial identity. The cost of a naive deterministic algebraic certificate is still quadratic (in the quotient degree), and its naive evaluation uses large interpolation tables. To make real progress one needs a new **input-dependent, non-quotient, existential certificate for divisibility/zero trace** which can be locally checked using near-linear many polynomial-alphabet binary relations.

## 5. Narrow research challenge

For arbitrary graph-induced row interpolants D(a,Y), construct a family of binary relations (which may contain globally preprocessed G-dependent data) on O(k polylog k) variables, each with k^{O(1)} states and maximum degree 3, satisfiable iff
    exists x∈V(G)^k: P_x | (sum_i D(x_i,Y)-1).
It is essential that a proposed proof NOT:
(1) expand a general quotient Q_G into Theta(N) coefficients;
(2) quietly assume that the dynamic modular remainder can be computed in near-linear work;
(3) replace random challenges by existentially chosen ones in sum-check;
(4) apply a lower bound proved only for a fixed code or exact solution projection to general decision-only reductions;
(5) transfer hardness of k×k multicolored Clique as if it automatically followed from ordinary-clique PSCH.

The algebraic trace may also be viewed as a parameterized form of the original nonnegative defect count, so its value is primarily **structural clarification**, not a breakthrough in CSP size.
