# Structured permutation constraints and matroid matching

**PROVED.** A K×K Permutation Clique (PCC) instance has one candidate (i,a) per row/column position. A witness is a permutation π; all selected pairs must be compatible. These algorithms require the stated factor descriptions. They are not general PCC algorithms or claims of novelty.

## Forbidden-factor covers reduce to ordinary matching

If forbidden pairs are the union of r supplied bicliques L_t×R_t with disjoint shores, a selected set avoids each factor iff it avoids one of its shores. Branch over 2^r choices, remove the chosen shores from the candidate positions, and test perfect matching in the remaining row-column graph. Correctness follows in both directions from that equivalence. Time is 2^r poly(input).

A supplied Ferrers factor forbids x∈L,y∈R iff α(x)>β(y). A selected set avoids the factor iff some threshold τ has α(x)≤τ for all selected left positions and β(y)≥τ for all selected right positions. Only the ordered distinct scores and endpoints matter, giving O(K²) thresholds per factor. Enumerate thresholds and test perfect matching, in K^{O(r)}poly(input) time. These criteria preserve existence; overlaps between branches do not preserve counts.

The same choices yield exact-projection binary CSP encodings with O(Kr+K log K) variables and constraints, polynomial alphabet, and degree at most three: K row choices, one choice symbol per factor, Kr membership checks, an O(K log K) Beneš permutation network for AllDifferent, and equality paths for high-occurrence symbols. Each constant-arity switch can be converted to a tuple variable with binary projection relations. Multiple routing witnesses are allowed. For arbitrary K, pad to the next power of two with fixed dummy labels. The network cost remains an obstacle to a smaller general compiler.

## Explicit linear-matroid independence is another tractable factor

Each allowed candidate (i,a) is supplied with v_{ia}∈F^d. Seek a perfect matching whose K vectors are independent. For d=K and S⊆[K], |S|=j, maintain

$$
W_S=\operatorname{span}\{v_{1,a_1}\wedge\cdots\wedge v_{j,a_j}:
                           \{a_1,\dots,a_j\}=S\}
\subseteq\Lambda^j F^K.
$$

Start W_∅=span{1}. Append each unused allowed column a by the linear map w↦w∧v_{j+1,a}, combining spans at S∪{a}. At the final state the space is nonzero exactly when some matching is independent: a linear span is zero iff every generating wedge is zero. There are 2^K subset states and each exterior dimension is at most 2^K. Gaussian elimination gives deterministic 2^{O(K)} field operations and exponential space. Self-reduction recovers a witness.

### Reducing the ambient dimension

For d>K, identify v with f_v(X)=Σ_{j<d}v_jX^j. Work in an extension containing an element ω of multiplicative order at least d and K(d−1)+1 distinct evaluation points. Define

$$
\Phi_t(v)=(f_v(t),f_v(\omega t),\dots,f_v(\omega^{K-1}t)).
$$

For a fixed independent K-tuple, column operations give a basis of distinct polynomial degrees d₁<⋯<d_K. The top coefficient of det[Φ_t(v₁),…,Φ_t(v_K)] is a nonzero Vandermonde in ω^{d_j}. Thus this determinant is a nonzero polynomial of degree ≤K(d−1), so at least one of those evaluation points preserves the tuple. Dependence is preserved by every linear map. Try all points and run the exterior DP.

For a finite field given in a standard explicit representation this is deterministic 2^{O(K)}poly(K,d,log|F|) bit time, including field construction. To see the field-size detail: if the base field is too small, enlarge it to size polynomial in K,d, then brute-force irreducibles/elements is polynomial in K,d. If it is already large, use polynomially many distinct explicit elements; fewer than Σ_{j<d}j elements have order below d, and testing the first d−1 powers suffices to find a suitable ω. This does not assume a deterministic primitive-element algorithm in arbitrary large fields.

This is the standard folded-Wronskian argument, related to [deterministic truncation of linear matroids](https://sites.cs.ucsb.edu/~daniello/papers/deterministicTruncationTALG18.pdf) and [rank condensers](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2015.800). The construction and DP are written out to make the particular application checkable.

### Randomized alternative and multiple factors

When d=K, put M_S(:,i)=Σ_{a∈S}y_{ia}v_{ia}. Inclusion–exclusion gives

$$
\sum_{S\subseteq[K]}(-1)^{K-|S|}\det M_S
=\sum_{\pi}\det[v_{1,\pi(1)},\dots,v_{K,\pi(K)}]
                         \prod_i y_{i,\pi(i)}.
$$

Distinct permutations give distinct tag monomials, so the polynomial is nonzero iff a solution exists. Evaluation over a sufficiently large finite extension gives a one-sided randomized O*(2^K) test. Random linear projection first handles d>K, with its error charged separately. This is determinantal sieving, not a new general technique; see [Eiben–Koana–Wahlström](https://arxiv.org/abs/2304.02091).

For r matroids over a common field, replace each wedge by the tensor product of its r wedges. Appending a candidate is still linear, and a pure tensor is nonzero iff every wedge is nonzero. With supplied polynomial-dimensional representations and r fixed, the result remains 2^{O((r+1)K)}poly(input). Rank-condense each layer; distinct characteristics cannot silently be embedded in one common field. Ferrers threshold branching can be composed with this solver.

## What the factors do not prove

High ordinary matrix rank does not imply a hard PCC instance: one Ferrers factor can have rank Θ(K²) and still be handled by polynomially many matching tests. Likewise a single partition matroid can encode color collisions with a full-rank forbidden-pair matrix. Finding a short factorization is separate from solving an instance whose factorization is supplied.

An arbitrary matroid **oracle** is not an explicit linear representation. The sparse-paving construction in the historical notes can encode PCC in a polynomial-time independence oracle; it does not supply the vector coordinates required above. The [all-fields obstruction](../barriers/encoding.md#exact-linear-representations-can-fail-over-every-field) shows why that distinction is substantive.

Provenance: notes 41–46 in the [pre-cleanup tree](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs). Finite checks: `experiments/41_pcc_biclique_cover_sanity.py`, `42_ferrers_chain_cover_pcc_sanity.py`, `43_matroid_permutation_sanity.py`, and `43_two_matroid_tensor_sanity.py`.
