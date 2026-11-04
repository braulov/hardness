# Graphic span, sparse encodings, and parity

**PROVED.** These are elementary identities and reductions, not new hardness theorems. All graphs are finite; incidence calculations allow parallel edges and exclude loops. Count every vertex, edge occurrence, Boolean variable, and local gate in the size parameter.

## Rank and its dual

For the binary vertex-edge incidence matrix of a graph, a selected edge set Y has

$$
\operatorname{rank} B_Y=|V|-\operatorname{cc}(V,Y).
$$

Within each connected component, tree edges form an independent set of size one less than the component order. Every other edge column is the sum of columns on its tree path. This proves the identity, including isolated vertices and parallel edges. Consequently Y is a forest iff its columns are independent, and it spans the graphic matroid iff it preserves the connected components of the original graph.

For any matroid M on E, duality gives

$$
r_{M^*}(A)=|A|-r_M(E)+r_M(E\setminus A).
$$

Thus Y is independent in M iff E\Y spans M*. Graphic independence and cographic spanning are interchangeable **without expanding a potentially dense cycle-space basis**.

## What the formalism encodes

Sparse (Co)Graphic Span-CSP consists of O(N) Boolean variables and bounded-fanin local gates, a graph description of O(N) total size, and a requirement that the activated elements span a graphic/cographic matroid or their direct sum. Auxiliary gate variables are uniquely determined by their inputs.

* FVS: let x_v indicate a retained vertex. The edges with x_u=x_v=1 must be independent; equivalently their complement spans the cographic matroid. Add the deletion budget.
* Hamiltonian cycle: enforce degree two at every vertex and full graphic rank. A connected 2-factor is a Hamiltonian cycle. Treat fewer than three vertices separately under the usual simple-cycle convention. Directed HC uses indegree and outdegree one and the underlying undirected incidence multigraph.
* Connectivity of a nonempty selected set S: choose exactly one root in S. Add a hub h; activate every induced edge of G[S], and the spoke hv iff v is excluded or is the chosen root. This graph is spanning-connected iff G[S] is connected. An always-active binary tree can replace the hub with linear overhead.

The last construction combines with local domination, vertex-cover, or terminal/budget constraints. Combining it with the cographic FVS encoding gives connected FVS. Direct sums conjoin full-span conditions because each summand's rank is bounded by its own full rank. Arbitrary nonsaturated rank thresholds cannot be conjoined this way.

For sparse input these encodings have linear total size. Degree-two constraints have constant local cost on bounded-degree graphs. Unweighted population counts have linear Boolean-gate size: repeatedly compress three equal-significance bits to two until only two binary numbers remain, then add/compare. Weighted counts require charging bit lengths.

## Coverage is a lift, not a matroid on the sets

Put one star leaf at each universe element. Selecting a set activates a parallel spoke occurrence at each of its incidences. Distinct star spokes are independent, so rank equals the number of covered elements. The cost includes **all set-element incidences**. Likewise one leaf per clause gives a rank representation of CNF satisfaction, with cost for all clause evaluations. Neither construction preserves universe size or number of SAT variables on arbitrary dense inputs.

Coverage as a function of the selected sets is generally not itself matroid rank: one selected set can cover many elements.

## Exact parity identity

For a full-row-rank binary representation A of rank r,

$$
\#\{w\in\mathbb F_2^r:A_Y^Tw=0\}
=2^{r-r(A_Y)}.
$$

Its parity is one exactly when Y spans. Summing over assignments satisfying a local predicate therefore computes the parity of feasible spanning assignments. For graphic matroids, use one anchored vertex per original component and equal endpoint labels on activated edges. For cographic spanning of E\Y, use even-degree edge subsets supported in Y; there are 2^{|Y|-r(B_Y)} such subsets. Sparse graphs give linear total local parity-gate cost, and deterministic Tseitin auxiliaries preserve counts.

**Limitation:** a positive even number of solutions still has parity zero. An exact unweighted #SAT algorithm therefore gives a parity algorithm via this encoding, not automatically decision.

If characteristic-two weighted counting were available at the required cost, the polynomial

$$
P(a)=\sum_{x\text{ feasible}}\prod_{i:x_i=1}a_i
$$

would be nonzero exactly when a feasible assignment exists: distinct Boolean assignments give distinct monomials. Evaluating over a field larger than twice the number of genuine assignment bits gives one-sided identity testing. This is a **CONDITIONAL route**; a weighted-counting engine with the necessary uniformity and size bounds is not supplied here.

## Meaning for hardness

A reduction P→Span transfers a Span algorithm to P. It does not transfer a Span hardness assumption to P. The reverse reductions, a universal fast Span decision algorithm, and a new circuit-lower-bound consequence remain open. None of the identities above establishes novelty or a complexity hypothesis.

Provenance: original notes 01–03 and 09–10, recoverable from the [pre-cleanup tree](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs). Finite cross-check: `py scripts/check_small_instances.py`.
