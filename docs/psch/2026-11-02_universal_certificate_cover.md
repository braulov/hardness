# Universal deletion-certificate cover: what survives arbitrary global precomputation

**2026-11-02; PSCH Branch B.** Status: elementary proved lemma in a fully general **deterministic compiler** model, and an explicit polynomial-time counterexample showing why it DOES NOT imply near-quadratic numbers of constraints. A methodology correction rather than a claim of novelty or progress to a universal reduction.

## Model

Let Comp be a deterministic polynomial-time transformation that maps ordinary k-CLIQUE on graphs with N=k² named vertices to a binary CSP instance with at most m=m(k) constraint slots and polynomially many output variables, alphabet Q=Q(k) (possibly polynomial in k). Its constraint graph and all tables may depend arbitrarily on the whole input graph. It preserves existence of solutions, not necessarily the original solution relation; all output variables may be existentially quantified. Pad constraint slots/variable names/alphabet to fixed polynomial bounds as a function of k so that for each fixed total target assignment z we can define f_{j,z}(G)∈{0,1}, the satisfaction indicator for output slot j. An absent slot is satisfied and domain/unary conditions are counted as slots. This padding is purely for analysis, not part of the output.

For a chosen k-set S, let G_S have exactly the binom(k,2) clique edges E_S=binom(S,2) and all other vertices isolated. Choose an accepting output target assignment z_S to Comp(G_S).

## Theorem (unrestricted local acceptance functions)

For each slot j define the *downward positive certificate size*

  c_j = min{ |F| : F⊆E_S and f_{j,z_S}(G')=1 for every graph G' satisfying F⊆E(G')⊆E_S }.

This quantity exists, since F=E_S is valid for any accepted slot. Then

  sum_{j=1}^m c_j >= binom(k,2).

In fact there is also a first-derivative / downward sensitivity bound. Let
  s_j = |{e∈E_S : f_{j,z_S}(G_S-e)=0}|.
Then
  sum_{j=1}^m s_j >= binom(k,2).
In particular, for each S some slot has
  c_j>= binom(k,2)/m   and   some (possibly different) slot has s_j>=binom(k,2)/m.

### Proof

Choose for each j a minimum positive deletion-certificate F_j of size c_j. If U=union_j F_j is a proper subset of E_S, then on graph G_U with edge set U the same target assignment z_S satisfies every output constraint by the defining property of the F_j. But G_U is a NO instance: all edges lie inside S, and at least one edge of S is absent, so it has no k-clique. Contradiction. Therefore union_j F_j=E_S and sum c_j >=|E_S|.

For sensitivity, for each edge e∈E_S the graph G_S-e is a NO instance. Thus z_S cannot satisfy every output slot on G_S-e, and e belongs to at least one slot's sensitivity set. Summing gives sum s_j>=|E_S|. Since every positive certificate for a predicate must contain all its singly sensitive coordinates, we also have s_j≤c_j.

Both claims allow arbitrary nonlinear source-edge processing, adaptive input-dependent output topology, arbitrary auxiliary variables, and Q as large as desired, provided the fixed-z slot semantics are well-defined by padding. **Neither statement yields a quadratic lower bound on m alone.**

### Consequences for restricted models

If each local acceptance function has downward decision-tree/query complexity ≤d on the deletion cube [∅, E_S] at G_S (in particular if there is a deterministic procedure reading at most d source-edge bits which evaluates it correctly), then c_j≤d and
    m d >=binom(k,2).
This is a generalization of the elementary edge-oracle barrier, but it is **not applicable** to unrestricted polynomial-time global preprocessing: a single table entry may read all Θ(k⁴) input bits.

Likewise if one can bound downward 1-certificate complexity for the local acceptance predicates by c, then m c≥binom(k,2). A low-degree algebraic function and a bounded linear sketch are other restricted ways of constraining the local acceptance predicates, treated separately in companion notes.

## A counterexample: easy predicate, huge DNF, full edge sensitivity

Define g_k(G) to be 1 iff G has a **connected component on exactly k vertices inducing a K_k**. This is computable in polynomial time for arbitrary G: compute connected components and check each size-k component's edges. Consider all N=k²-vertex minimal YES instances G_S (one K_k and N-k isolated vertices), with k≥3. Then

  g_k(G_S)=1, and g_k(G_S-e)=0 for every e∈E_S.

Thus g_k has sensitivity binom(k,2) to clique-edge deletion at EVERY G_S, and the minimal downward certificate has full size binom(k,2). **One polynomial-time predicate** can be responsible for all of those edges, so certificate-cover alone cannot imply m=Omega(k²).

Moreover, any DNF representation of g_k in the full N-vertex adjacency bits needs AT LEAST binom(N,k) terms:
suppose one conjunctive DNF term were true on both G_S and G_T for distinct k-subsets S≠T. Its positive edge literals would all lie in E_S∩E_T=binom(S∩T,2), and its negative edge literals would be absent from both E_S and E_T. Set all input edge bits except its positive literals to zero. The term still accepts, but this graph has edges on at most k-1 vertices and therefore no k-clique component, contradiction. Hence each G_S needs a different DNF term.

With N=k², binom(N,k)=k^{Theta(k)}. Thus a predicate in P can have enormous DNF *and* maximal edge-deletion sensitivity on isolated K_k inputs. This is why the polynomial-catalogue no-go is not remotely a general computational lower bound on polynomial-time relation-table entries.

**Critical caveat:** g_k does NOT decide ordinary k-Clique on unrestricted input graphs: a k-clique need not be an isolated component. This example invalidates a tempting proof strategy, not the desired sparse-CSP compiler.

## The next concrete bottleneck

Try to turn a large-minterm, P-time global predicate like connectedness / perfect matching / rank into a **witness-conditioned** local test without needing a single CSP symbol to store the entire k-vertex selection S. Any accepting output assignment should jointly route/cohere the k chosen vertices across m=O(k polylog k) factor checks with Q=k^{O(1)}, and must work on all YES graphs, not just isolated cliques.

The universal-selector QCSP already solves this with one universal choice but is not an ordinary existential CSP. Beneš/AllDifferent existential compilers work because distinctness is a multiset invariant. Clique compatibility is still the missing structured invariant. A P-time predicate with very many minterms is *necessary for escaping some current restricted no-go results* but by itself is not remotely sufficient.

## Supporting literature

- Jansen–Pieterse, *Optimal Sparsification for Some Binary CSPs Using Low-degree Polynomials*, ACM TOCT 2019, https://doi.org/10.1145/3349618 : explicit illustration that number of constraints and per-constraint encoding length behave differently.
- Other restricted-model PSCH bounds: [polynomial catalogue](2026-11-02_precompiled_test_catalogue_barrier.md), [Davenport sketches](2026-11-02_davenport_linear_sketch_barrier.md), [decision-only output bit budget](2026-11-02_decision_only_bit_budget.md).

**Research verdict:** no new Clique→near-linear-CSP compiler and no general lower bound. We have a universal necessary certificate/sensitivity property, and an exact counterexample to an over-optimistic conclusion from it.
