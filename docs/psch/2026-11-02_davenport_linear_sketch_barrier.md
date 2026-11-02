# Zero-sum barrier for input-oblivious linear sketches inside existential CSP compilers

**Date:** 2026-11-02. **Branch:** PSCH/B, large-table sparse CSP reduction.
**Status:** PROVED in the stated **linear-sketch input-dependence model**, using the classical Davenport constant of elementary Abelian p-groups. This is NOT a universal clique-to-CSP lower bound; literature novelty has not been established.

## Theorem — fixed sketches, unrestricted existential witnesses

Fix k>=2 and a prime p. Let a deterministic yes/no-preserving compiler take ordinary k-Clique instances on N=k² vertices to a CSP with at most m output constraint slots and an arbitrary common alphabet [Q], with arbitrary existential auxiliary variables. Assume output graph topology, variable numbering, and domain are **input-independent**, or more generally that the full Boolean acceptance function of slot j under any *fixed global target assignment* z has the following form:

    f_{j,z}(G) = h_{j,z}( A_{j,z} b(G) + c_{j,z} ),

where b(G)∈{0,1}^{binom(N,2)} is the vector of all source edge bits, A_{j,z} is a matrix with at most r_j rows over F_p, c_{j,z} is a constant vector, and h_{j,z}:F_p^{r_j}->{0,1} is **completely arbitrary**. Critically, the sketch coefficient matrix and postprocessing map are fixed for that slot/witness, i.e. **do not depend on G**. The entire source input may be consulted in computing the sketch, and an individual sketch may involve every input edge.

Then **for every accepting assignment** z* to the output of the minimal YES graph G_S=K_S plus N-k isolated vertices,

    (p-1) sum_{j=1}^m r_j >= binom(k,2).

In particular, if each local table entry inspects at most r affine F_p fingerprints, then

    m r (p-1) >= binom(k,2).

For p=2 and r=1, this forces m>=binom(k,2), regardless of Q, number or structure of existential helper variables, or the complexity of h. For p constant, m=O(k polylog k) needs r=Omega(k/polylog k). For p polynomially large, the bound may be weak or vacuous.

### Proof

Fix any k-set S and let G_S have exactly E_S=binom(S,2) as edges. It has exactly one k-clique. Choose ANY accepting output CSP assignment z*. At z*, concatenate all m linear sketches into one affine map L(b)=A b+c with total dimension R=sum_j r_j. Let v_e∈F_p^R be the column of A for edge e∈E_S.

The classical zero-sum theorem for elementary Abelian groups states
    D((C_p)^R)=1+R(p-1).
Thus whenever |E_S|=binom(k,2)>R(p-1), there is a nonempty edge set F⊆E_S with
    sum_{e∈F} v_e=0  in F_p^R.
Let G'=G_S-F. Its edge vector is b(G')=b(G_S)-1_F. Every selected affine sketch is unchanged:
    L(b(G'))-L(b(G_S))=-sum_{e∈F}v_e=0.
Because the arbitrary postprocessing functions h_{j,z*} see identical sketches, all target constraints still accept the *same* z*. Yet G' lacks a k-clique: the only possible k-set S has a missing edge, and all outside vertices are isolated. Contradiction. Hence binom(k,2)≤R(p-1).

For p=2 there is an elementary linear algebra proof: if R<|E_S|, the columns {v_e} are linearly dependent over F2, yielding a nonempty zero-sum subset immediately.

### Equations, inequalities, arbitrary postprocessing, and large tables

The proof applies not just to **affine equations** [L=0], but to **any arbitrary Boolean predicate** h(L) on r affine measurements. It includes parity equality, inequality, threshold or membership conditions on a finite-field sketch; however, representing an integer zero/nonzero test over **large characteristic** p can evade the bound.

The theorem allows an output binary table with Q²=poly(k) entries, each with *its own* fixed coefficients. On the accepting witness only m entries matter, and their total sketch dimension is what is bounded below. It is thus not a bound on total entries in the compiled instance.

The graph-dependent *choice* of coefficients A(G) would invalidate the argument: removing F could change the sketch itself and the proof would not preserve its values. Similarly, an output topology chosen from G using arbitrary preprocessing is not automatically covered unless the full fixed-z slot acceptance function admits the stated sketch factorization.

### Why this matters jointly with the catalogue lemma

The companion [catalogue bound](2026-11-02_precompiled_test_catalogue_barrier.md) says that a fixed-skeleton compiler with m=O(k polylog k) cannot have every table-bit predicate represented by a polynomial-size catalogue of DNF conditions on source edges: the total number of terms must satisfy M>=k^{Omega(k/sqrt(m))}. This excludes global conjunctions or fixed-subset **nonnegative** defect sums, even when they aggregate many edges.

The new finite-field bound excludes a different route: **one or a bounded number of arbitrary parity/linear fingerprints** per locally tested table entry, even though parity has exponentially large DNF and hence avoids the catalogue restriction.

Taken together, these identify two insufficient mechanisms:
1. Polynomially many prechosen conjunction/absence conditions on source edges;
2. Bounded-dimensional, input-independent linear sketches over a small field, with arbitrary nonlinear postprocessing.

They do NOT rule out adaptive/input-dependent coefficient choices, high-characteristic aggregations, nonlinear sketches of sufficiently high complexity, or general polynomial-time construction of large binary relation tables.

### Context and sources

- Davenport constant for finite Abelian p-groups: for G=⊕_i C_{p^{a_i}}, D(G)=1+Σ_i(p^{a_i}-1). In particular D((C_p)^R)=R(p-1)+1. Reference: https://mathworld.wolfram.com/DavenportConstant.html and Gao–Geroldinger, *Zero-sum problems and coverings by proper cosets*, European Journal of Combinatorics 24 (2003), 531–549, https://doi.org/10.1016/S0195-6698(03)00033-7 .
- Earlier notes on Dell–van Melkebeek/Drucker bit-budget lower bounds and exact-projection/fixed-code barriers: see the PSCH index and v7 full checkpoint.

**Open:** a general polynomial-time, decision-only compiler ordinary k-Clique N<=k² -> bounded-degree 2-CSP with m=O(k polylog k), Q=k^{O(1)}. No such compiler follows from these no-go statements.
