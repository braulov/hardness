# Exact CSP planarization: an unconditional quadratic separator barrier

**Branch:** PSCH/B, existential binary relations. **Date:** 2026-11-02.
**Status:** Self-contained proof in a *solution-projection preserving, designated-terminal* model; independent novelty review remains open. It does **NOT** prohibit arbitrary decision-preserving reductions.

## Theorem (exact extension; weighted separators + rectangle covers)

There is an infinite family of satisfiable binary CSP relations R_k, with k designated source variables, constant-sized source alphabet, and O(k) source constraints, such that for every binary CSP extension Ψ_k satisfying:

1. Its primal constraint graph is planar;
2. Each of the k original variables is represented by one distinct **designated terminal variable** (or by a fixed per-terminal decoding map from its alphabet), whose joint projected solution relation is *exactly* R_k;
3. Every other variable is existentially quantified, with arbitrary number of possible extensions per source assignment; binary tables are arbitrary and may be globally preprocessed;
4. The output alphabet has size at most Q, and all unary predicates are counted as constraints (or encoded by attached binary gadgets);

we have
    m = Omega(k^2 / log^2 Q)
for the number of output constraints m, for Q>=2 and arbitrarily large k; in particular, if Q<=k^C with fixed C, then m=Omega(k^2 / log^2 k). For constant Q, this strengthens to m=Omega(k^2).

The bound is uniform in the exact encoding choice; no linearity, fixed code, unique auxiliary extension, or source-instance-independent target table is assumed. **Designated terminals and exact relation projection are essential.**

### Source CSP: independent edge ports

Fix a family of degree-Δ edge expanders H_k=(V_k,E_k), with |V_k|=k and Δ, edge-expansion h>0 independent of k. It is enough to consider an infinite sequence of k for which such expanders exist. The source variable at v∈V_k is x_v∈{0,1}^Δ, one port per incident edge (fix any ordering of ports). For each e=uv impose one binary constraint: the port of x_u corresponding to e equals the port of x_v corresponding to e. There are Δk/2=O(k) constraints and a constant domain size 2^Δ.

Each satisfying source assignment corresponds bijectively to an arbitrary independent collection of edge bits (b_e)_{e∈E_k}. In particular source satisfiability is trivial, but the full solution relation contains a high-dimensional cross-cut equality structure.

### Rectangular lower bound for balanced partitions

For a partition V_k=A ⊔ B ⊔ C with |A|,|B|≥k/4 and |C|=o(k), the projection of R_k to the terminals A∪B (existentially forgetting C) has rectangle-cover number at least 2^{|E(A,B)|}. Indeed, set all non-crossing ports to 0 and let the |E(A,B)| edge bits vary independently. This gives 2^{|E(A,B)|} satisfying pairs (a_b,b_b). If b≠b', the crossed tuple (a_b,b_{b'}) violates at least one port equality, so no 1-rectangle can contain both pairs: a fooling set.

By expansion and bounded degree, if min(|A|,|B|)≥k/4 then
    |E(A,B)| ≥ h k/4 - Δ|C| = Omega(k)
provided |C|=o(k). (Apply expansion to the smaller of A,B; all edges leaving it either reach the other side or C.)

### Planar weighted separator argument

Let n be the number of relevant output CSP variables, counting the k terminals. Remove unconstrained auxiliary variables; then n≤k+2m, up to a constant factor if unary constraints are permitted. The weighted planar separator theorem gives a vertex set S of size at most c sqrt(n) such that, after deleting S, all components contain at most 2k/3 terminals. Assign components to two sides in a way that both sides have at least k/4 terminals, as soon as |S|=o(k). This yields terminal partition A⊔B⊔C with C consisting of the terminals in S, |C|≤|S|, and no output constraint connecting the components assigned to distinct sides.

For each *full assignment* σ∈[Q]^S to the separator, auxiliary variables on the two sides can be chosen independently. Thus the projected relation on terminal groups (A,B), after forgetting C, is a union of at most Q^{|S|} combinatorial rectangles. This stays valid with arbitrary existential witnesses, arbitrary globally preprocessed tables, and per-terminal deterministic decoding.

By the expander-port fooling set, its rectangle-cover number is >=2^{Omega(k)}. Hence
    |S| log_2 Q = Omega(k);
    sqrt(n) log Q = Omega(k);
    n = Omega(k^2 / log^2 Q).
Together with n≤k+2m, this yields m=Omega(k^2/log^2 Q) (if log Q happens to be so large that the bound is O(k), it is vacuous; the interesting regime has log Q=o(sqrt(k))). For the polynomial-alphabet regime it is nontrivial.

The argument by contradiction can be phrased directly: assume m=o(k^2/log^2 Q) with log Q=O(log k); then |S|=o(k/log Q)=o(k), contradicting the separator / rectangle-cover bounds. The constants in Omega can be derived by splitting cases where |S|≥h k/(8Δ), and its complement.

### General separator exponent

Suppose a target graph class admits weighted vertex separators of size O(n^α) for some 0<α<1 (with balanced terminal weights). The same proof yields
    n=Omega((k/log Q)^{1/α})
as long as the terminal count and the corresponding asymptotic regimes support the weighted balanced split. For α=1/2 this is quadratic.

### Separate PSCH-conditional decision-only barrier (not an unconditional corollary)

Suppose a deterministic polynomial-time compiler takes **ordinary** k-Clique on N<=k^2 vertices to planar binary CSP with m constraints and Q=k^{O(1)}. A planar treewidth decomposition and standard DP decide it in time
    2^{O(sqrt(m+k) log k)} poly(k).
Consequently, **under PSCH**, such a compiler cannot always output
    m=o(k^2/log^4 k),
even if it preserves *only* existence of a solution and does not retain original variables as terminals.

This is weaker than the unconditional extension lower bound, but it covers the real decision-only target. It assumes determinism and the **specific PSCH running-time threshold** 2^{o(k/log k)}; weaker exponential-hardness hypotheses need not imply it.

## Interpretation and scope

- This is a true obstruction to using *planar* auxiliary proof graphs as near-linear-size, exact, solution-preserving encodings; it does **not** obstruct sparse **expanders**, which have linear-size balanced separators and can carry Θ(k) independent edge bits.
- Source R_k is already a sparse CSP with O(k) constraints and trivial satisfiability. Thus the difficulty is preserving the **whole relation**, not deciding YES/NO.
- This strengthens the earlier fixed cut / identity-matching example by using bounded-degree expansion to force high rectangle complexity against *every* balanced separator partition chosen by the target planar graph.
- A compiler may evade the unconditional theorem by removing source terminals, abandoning the exact projection, using a nonplanar target graph, or using an alphabet whose logarithm grows sufficiently rapidly.

## References

- Lipton and Tarjan, *A Separator Theorem for Planar Graphs*, SIAM J. Appl. Math. 36(2):177–189 (1979), https://doi.org/10.1137/0136016 .
- Weighted statement explicitly quoted in *Lower Bounds for Planar Arithmetic Circuits*, ITCS 2024, Theorem 10: https://drops.dagstuhl.de/storage/00lipics/lipics-vol287-itcs2024/LIPIcs.ITCS.2024.91/LIPIcs.ITCS.2024.91.pdf .
- Standard constant-degree edge-expander construction/definition: Luca Trevisan, *Expander Constructions*, https://lucatrevisan.github.io/books/expanders.pdf .

**Novelty:** This argument is a standard separator/communication-complexity technique in a particular exact-CSP encoding formalism. Do not claim it as a new lower-bound result without literature audit.
