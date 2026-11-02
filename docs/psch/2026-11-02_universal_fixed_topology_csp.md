# A fixed-topology normal form for bounded-degree binary CSP using Beneš routing

**Date:** 2026-11-02. **Project:** PSCH, Branch B.
**Status:** Elementary constructive lemma (proved modulo the standard rearrangeability of a Beneš switching network), **not a Clique→sparse-CSP compiler**. The result was verified at the routing-only level by exhaustively testing all 2!, 4!, and 8! permutations (40,346 total). Prior-art novelty NOT claimed; this is a standard universal-switching-network trick applied to CSP topology.

## Theorem (fixed universal CSP skeleton)

For every n>=1 there is a deterministic polynomial-time constructible simple graph U_n with

  |V(U_n)|, |E(U_n)| = O(n log(n+2)),
  maximum degree <=3,

such that every explicitly tabulated **binary CSP** Γ with n source variables, domains contained in a common [Q], and a primal constraint multigraph of maximum incidence degree <=3 can be transformed in deterministic polynomial time to a binary CSP Γ' on **exactly the fixed graph U_n**, with common alphabet of size

  Q' <= max(Q^4, O(1)),

whose satisfying assignments project exactly to the satisfying assignments of Γ. This remains valid with unary domain restrictions (absorbed into port constraints), duplicate binary constraints, and unused ports. The topology U_n is independent of the input Γ (including its relation graph). The tables of Γ' ARE allowed to depend on the entire Γ.

An explicitly tabulated output has at most O(n log n)*Q^{O(1)} bits and is constructible in time polynomial in n and Q, hence polynomial in the explicit CSP input length. All source-degree and output-degree bounds refer to constraint incidence, with unary predicates encoded as restrictions of binary port relations.

### Construction

Let p=2^{ceil(log_2(3n))}, so 3n<=p<6n. A fixed p-wire Beneš network has 2 log_2 p-1 switch stages, each with p/2 two-input/two-output switches, in total O(p log p)=O(n log n) switches. Its wiring and switch positions depend only on p.

Place three input wires for each source variable x_v; all three wires carry the same value x_v. Use the remaining p-3n wires as independent dummy symbols. Each source x_v is incident with exactly three input port constraints and therefore has target graph degree 3.

For each original binary constraint e between source variables u,v, assign a **distinct** ordered output pair (2j-1,2j). Since original incidence degree <=3, the number of constraints is at most 3n/2 and there are at least enough output pairs (p/2>=3n/2). Associate its two corresponding input half-edge ports with the two outputs of this assigned pair. Map all unused input ports bijectively to all remaining output positions. We thus obtain a permutation π of the p input wires.

The rearrangeability theorem for the Beneš network provides switch settings to route this permutation. All settings are computable in polynomial time, e.g. recursive alternating 2-edge coloring of the degree-2 bipartite multigraph between input pairs and output pairs. **Crucially, these settings are encoded as input-dependent local relations, not as changes in the topology of the switching network.**

At each real output pair, install one binary checker whose table is exactly the corresponding source relation R_e (with port orientation). All other output pairs have universally accepting checker tables; their checker edges are still present in the fixed topology.

A switch has port symbols a,b (inputs) and c,d (outputs), constrained to c=a,d=b for the assigned straight setting or c=b,d=a for the assigned cross setting. Represent the entire 4-port state by one symbol of a Q^4 alphabet. To make the checker's incidence degree at most 3, replace its 4-port state variable by four equal-valued state copies arranged along a 4-node path, with one binary port-projection relation attached to each copy. The middle copies have degree 3, endpoint copies degree 2. Encode the fixed straight/cross restriction in one of the four port-projection tables, avoiding additional edges or unary constraint slots. A wire-value variable has two adjacent port incidences, or one port incidence plus an output checker; an input source variable has three port incidences. All degrees are <=3.

Exactly 4 port-projection constraints plus 3 state-equality constraints are needed per switch, along with O(p) fixed output-checker and input edges; the total is O(p log p). This defines the same output constraint graph U_n for every Γ of n variables, only the tables vary.

### Equivalence

Given a solution x of Γ, put x_v into all three corresponding network inputs. Route them by the fixed permutation settings. Every output checker for a real edge e receives exactly the two variables' source values, so it accepts; dummy checker relations always accept. The switch tuple states and equality copies give an extension to a solution of Γ'.

Conversely, any solution of Γ' agrees with the forced straight/cross permutation at every switch. Therefore real output checker j sees the original source values x_u,x_v for the corresponding edge e; since the checker accepts, (x_u,x_v)∈R_e. Original unary restrictions were incorporated in input-port relations, so the projected source variables form a solution of Γ. The network settings are fully fixed by the compiler; no unsound alternative routing is available.

## Corollary: fixed topology suffices for the PSCH target up to one logarithm

Suppose a deterministic polynomial-time compiler takes EVERY ordinary k-CLIQUE input on N<=k² vertices to a degree<=3 binary CSP with
  m=O(k log^c k),
  Q=k^{O(1)},
and correctly preserves YES/NO. Discard isolated target variables and pad to n(k)=O(k log^c k) source CSP vertices (introducing harmless unconstrained dummy variables). Apply the universal-topology construction for this fixed n(k).

The composite compiler outputs a binary CSP with the **same** topology U_{n(k)} for all input graphs, with

  m'=O(k log^{c+1}k),
  Q'=k^{O(1)},
  Δ<=3.

Thus allowing the output *constraint graph itself* to depend on G is not an asymptotically essential power for this main research goal at polylog precision. The hard part may be moved entirely into **G-dependent binary tables** on a universal switching-network skeleton.

This **does not** imply an ordinary k-Clique to sparse-CSP reduction exists. It only normalizes the topology of one if it were found.

### Tensor-network formulation

For the fixed topology U_{n(k)} and edge tables R_e^G:[Q']×[Q']->{0,1}, the desired YES/NO condition becomes

  G contains K_k
    iff sum_{z∈[Q']^{V(U_{n(k)})}} prod_{e=uv ∈ E(U_{n(k)})} R_e^G(z_u,z_v) > 0,

where all quantities are nonnegative integers (no cancellation). Each table must be computable from G in deterministic poly(k) time. This is a fixed-skeleton, input-programmable Boolean tensor-network target, often cleaner than permitting G-dependent graph topology.

## Limits and audit caveats

- **Do not call U_n an expander without proof.** It is a highly structured universal switching network, and no explicit edge-expansion or treewidth constant is proved here.
- The network's O(n log n) 2-way switch count is tight for any pure 2-state switch network which can realize all p! permutations: 2^s>=p! implies s=Omega(p log p). This is a restriction of the chosen switching architecture, **not** a universal CSP-size lower bound.
- The output alphabet Q^4 can make explicitly tabulated tables as large as Q^8; still polynomial in the explicitly tabulated source input size when Q=poly(k).
- This normalization **does NOT make fixed-code or polynomial-DNF-catalogue lower bounds automatically apply** to arbitrary compilers. If the original topology depends on G, the computed Beneš control bits may have very complex Boolean dependence on G, and the normalized tables inherit it.
- It preserves all source CSP assignments via projection, but a hypothetical upstream Clique→CSP decision-only reduction need not preserve all clique witnesses, and this normal form does not change that.

## Useful new formulation of next goal

It is enough to compile arbitrary ordinary Clique inputs with N<=k² to fixed-topology G-dependent tables on U_{O(k polylog k)} with Q=k^{O(1)}, whose positive Boolean tensor contraction is nonzero precisely on YES instances. Existing rank/rectangle/threshold summaries, exact-projection counting, polynomial minterm-catalogue and low-characteristic linear-sketch no-go results rule out some special tensor constructions, but none rules out arbitrary input-dependent local tensor tables on this fixed skeleton.

**Status of principal target:** OPEN.

## References

- Beneš (1964), *Optimal Rearrangeable Multistage Connecting Networks*, https://doi.org/10.1002/j.1538-7305.1964.tb04103.x .
- Standard Beneš recursive architecture (2 log p−1 stages and p/2 switches/stage), https://doi.org/10.1049/tje2.12037 .
- Previous [PSCH checkpoint](2026-11-02_full_checkpoint_v7.md) and the [universal quantified selector](2026-11-02_universal_selector_qcsp.md).
