# Post-ETH tensor algorithms for HOM/SubISO and surviving hardness scales

**Date:** 2026-11-02  
**Status:** Research checkpoint. Elementary reductions PROVED. Fast runtimes CONDITIONAL on externally claimed tensor counting algorithms, not independently audited here. No new general-purpose CSP or Circuit-SAT algorithm and no new proven lower bound.

## 0. Premises and precise attribution

1. **Nguyen, "A Sublinear Treewidth Exponent for Binary Constraint Satisfaction", 2026-11-02, Theorem 1.2:** claims a deterministic exact counter for complete-table binary CSP on \(K\) variables, alphabet \(q\ge2\), maximum primal degree at most any fixed \(\Delta\), in \(L^{O_\Delta(1)}q^{O_\Delta(K/\sqrt{\log K})}\). The constant is uniform in \(q\). Its result imports the weighted/signed tensor-network recursion of **Claude (Anthropic)** and foundations from OpenAI. The downstream Lean formalization and upstream import boundary require independent audit.
   Source: https://hexagonmath.org/2611.00004v1
   Previous audit: [note 22](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md).
2. **OpenAI 2026 full Boolean tensor-contraction theorem:** conditional \(2^{O(M/\sqrt{\log M})}\) scalar contraction for networks with \(O(M)\) bit-wires and suitable local entry and ring assumptions. Not included in the specifically listed Lean formalization of fixed-width #CNF.
   Source: https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex
   Earlier audit: [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).
3. **Jizhou Guo, "Conditional consequences of a Boolean tensor-contraction theorem: threshold circuits and sparse connectivity", v2, 2026-10-30:** already derives deterministic \(2^{O(N/\sqrt{\log N})}\) algorithms for Hamiltonian cycles/paths, TSP, FVS, Steiner tree, connected vertex cover and connected dominating set on \(O(N)\)-edge graphs, assuming the full tensor theorem. A distinct *randomized* Cut&Count/isolation route requires only the weaker Lean-scoped fixed-width #3-SAT counting theorem and gives \(2^{O(N(\log\log N)^2/\sqrt{\log N})}\). **These are existing conditional reductions, NOT discoveries of the present notebook.**
   Source: https://github.com/aster2024/openai-math-followups/tree/main/tensor-contraction-consequences

We use \(\log(2+x)\) instead of \(\log x\) when small instances matter. Polynomial factors account for complete relation tables and integer-output arithmetic. The asymptotic bounds are not claimed to be practical for relevant input sizes.

## 1. Counting HOM on a sparse source graph — conditional

Let \(G\) be a simple pattern/source graph with \(n\) vertices, \(m\) edges, and \(H\) a simple target graph with \(h\ge2\) vertices. The count \(\#\mathrm{HOM}(G,H)\) is exactly the number of assignments \(f:V(G)\to V(H)\) satisfying one explicit relation \(A_H(f(u),f(v))=1\) per source edge. Common-list variants are unary restrictions.

If \(\deg_G(v)=d>0\), replace \(v\) by \(d\) occurrence copies. Connect them with \(d-1\) binary equality constraints along a path, and attach one original adjacency constraint to each occurrence. Isolated vertices stay as unary-domain variables. There are at most \(n+2m\) variables, at most \(3m\) binary edges, and maximum primal degree at most 3. Each original homomorphism extends **uniquely** to an occurrence-copy assignment. The new common alphabet remains \([h]\), and equality plus adjacency relations have explicit tables of size \(O(h^2)\), so the complete representation is polynomial in \(|G|+|H|\).

**Consequence (if Nguyen Theorem 1.2 is correct):**
\[
  \boxed{\#\mathrm{HOM}(G,H)\text{ computable in }
   \operatorname{poly}(|G|,|H|)\,
   h^{O((n+m)/\sqrt{\log(n+m)})}.}
\]
Compare with direct enumeration \(h^n\); take the minimum. For \(m=O(n)\), \(h=n^{\Theta(1)}\), the new claimed bound is \(2^{O(n\sqrt{\log n})}\). The reduction does not depend on \(\operatorname{degen}(H)\). It also applies to **list homomorphisms** and their counts, via unary domains.

For a connected source \(G\), each image lies in one connected component of \(H\). If the largest such component has size \(h_{\max}\), we may count homomorphisms separately into each component at cost \(\operatorname{poly}(|H|)\,h_{\max}^{O((n+m)/\sqrt{\log(n+m)})}\); this can be substantially smaller than the bound in total \(h\).

## 2. New-to-this-notebook transfer: sparse Subgraph Isomorphism from #HOM

Let \(G\) have \(n\) vertices and \(m\) edges; \(H\) have \(h\ge n\) vertices. We want an **injective edge-preserving** map \(G\hookrightarrow H\), not an induced embedding.

Choose a coloring \(\chi:V(H)\to[n]\). For \(S\subseteq[n]\), define \(H_S=H[\chi^{-1}(S)]\) and compute
\[
 Z_\chi=\sum_{S\subseteq[n]}(-1)^{n-|S|}\#\mathrm{HOM}(G,H_S).
\]

For a homomorphism \(f\), its contribution is
\[
 \sum_{S\supseteq\chi(f(V(G)))}(-1)^{n-|S|}
 = \begin{cases}1&\text{if its image uses all }n\text{ colors},\\0&\text{otherwise.}\end{cases}
\]
There are exactly \(n\) pattern vertices, so a homomorphism using all \(n\) colors is injective. Thus \(Z_\chi\) equals the **nonnegative integer** number of \(\chi\)-colorful subgraph embeddings.

For any fixed embedding \(f\), a uniformly random coloring is injective on its \(n\) images with probability \(n!/n^n=e^{-O(n)}\). Testing \(e^{O(n)}\) independent colorings is a one-sided Monte Carlo decision algorithm with constant success probability (never false YES). Alternatively the classical \(n\)-perfect hash families of Alon–Yuster–Zwick provide deterministic \(2^{O(n)}\operatorname{poly}(h)\) colorings.

Each coloring requires \(2^n\) exact #HOM calls; consequently:

**Consequence (conditional on Nguyen or OpenAI tensor theorem in the polynomial-domain regime):**
\[
 \boxed{
 T_{\mathrm{SubISO}}(G,H)
 =2^{O(n)}
 h^{O((n+m)/\sqrt{\log(n+m)})}
 \operatorname{poly}(|G|,|H|).
 }
\]
For \(m=O(n)\) and \(h=n^{\Theta(1)}\), this is \(2^{O(n\sqrt{\log n})}\); derandomization is possible using known perfect hash families. The method handles any target degeneracy.

**Do not extend this proof to induced SubISO:** requiring nonedge preservation adds up to \(\Theta(n^2)\) constraints on a sparse pattern. The method does not imply a comparable bound for induced embeddings.

The color-coding technique is classical; the only present observation is combining it quantitatively with the newly claimed #HOM upper bound. Reference: Alon–Yuster–Zwick, *Color-coding*, JACM 1995, https://www.math.tau.ac.il/~nogaa/PDFS/col5.pdf

## 3. A hardness scale compatible with the claimed algorithm

Old SPACH / CEH forbid \(q^{o(k)}\) on \(k\)-variable polynomial-domain sparse CSP. They are **conditionally refuted**, see notes 22/33.

A **new proposed** candidate, here called **SqrtLog-SPACH**, is:

> There exists a fixed \(c>0\) such that explicit binary CSP with \(k\) variables, \(O(k)\) constraints, fixed maximum degree 3, and \(q=\lceil k^c\rceil\) admits no uniform deterministic \(q^{o(k/\sqrt{\log k})}\operatorname{poly}(L)\)-time decision algorithm.

State a separate randomized-hardness variant if needed; deterministic vs randomized hardness must not be conflated.

This does not conflict with Nguyen's claimed \(q^{O(k/\sqrt{\log k})}\) upper bound. Under the candidate, a matching worst-case lower bound would identify the exponent up to constants, although there is **no proof** and the truth of the candidate is entirely open.

**Connection to polynomial-target 2-degenerate HOM:** If the project's sparse-CSP-to-HOM gadget does indeed map every instance of this exact source class to \(G\) with \(n=O(k)\), \(m_G=O(k)\), and \(\operatorname{degen}(H)\le2,\ h=k^{O(1)}\), then SqrtLog-SPACH excludes a uniform \(h^{o(n/\sqrt{\log n})}\operatorname{poly}(|G|,|H|)\) HOM algorithm on the gadget family; in particular it excludes \(2^{O(n)}\operatorname{poly}(|G|,|H|)\). **The exact gadget and target-size claim require re-auditing against the project's paper** before turning this into a formal conditional theorem.

One may separately hypothesize **SqrtLog-CEH** on a predetermined cubic expander. It is *stronger as a hypothesis* than unrestricted SqrtLog-SPACH; the known logarithmic-overhead fixed-expander compilation is not enough to transfer the matching \(\sqrt{\log}\)-scale between them. Do not label them equivalent.

## 4. Quantitative hard-source compiler thresholds

Let PCC(K) be permutation \(K\times K\) Clique. Assume a separate no-\(2^{o(K\log K)}\) PCC hardness hypothesis. A polynomial-time, decision-preserving (or appropriately randomized, under randomized PCC hardness) PCC \(\to\) degree-3 CSP compiler with polynomial alphabet \(q'=K^{O(1)}\), \(k'+m'=O(K\sqrt{\log K})\) would imply SqrtLog-SPACH **for the compiler output subclass**, and hence for the general class, provided the output domains meet the selected fixed-exponent regime after harmless padding. Indeed \(k'/\sqrt{\log k'}=O(K)\), so a \(q'^{o(k'/\sqrt{\log k'})}\) algorithm would solve PCC in \(2^{o(K\log K)}\) time.

By contrast, \(k'+m'=o(K\sqrt{\log K})\) is *incompatible* with PCC hardness AND Nguyen's claimed CSP algorithm. The former linear-size PCC compiler is closed **as a hardness transfer route under these simultaneous premises**, not unconditionally as a mathematical construction. The old Beneš AllDifferent gadget has \(O(K\log K)\) size and does not by itself achieve the new target, nor does it handle arbitrary dense PCC adjacency constraints.

For **unrestricted polynomial-size Circuit-SAT**, let \(s\) be the number of primary inputs, \(\operatorname{size}(C)\le s^d\). Suppose a no-\(2^{o(s)}\) Circuit-SAT hypothesis holds. An input-efficient SAT-iff compiler into binary CSP with \(r=k'+m'\) and \(q'=s^{O_d(1)}\) has the new algorithm's time \(2^{O(r\log s/\sqrt{\log r})}\) when \(r\) is polynomial and nontrivial. Therefore \(r=o(s/\sqrt{\log s})\) is incompatible with both the tensor bound and Circuit-SAT hardness; \(r=O(s/\sqrt{\log s})\) is the **quantitatively tight unexcluded target**. If such a compiler existed with a checked \(n_{\mathrm{HOM}}=O(r)\), \(h=\operatorname{poly}(s)\) reduction, a \(2^{O(n_{\mathrm{HOM}})}\) HOM algorithm would refute Circuit-SAT hardness, but the tensor upper bound would only give \(2^{O(s)}\).

## 5. Implications for project priorities

- **ALREADY COVERED externally under stated assumptions:** sparse HC / FVS / connectivity-type algorithms (Guo 2026). Preserve attribution and the distinction between the full tensor theorem and the weaker Lean-scoped fixed-width theorem.
- **NEW DERIVED UPPER BOUNDS:** sparse-source #HOM and ordinary (non-induced) SubISO; test target degeneracy, list restrictions, and disconnected targets further. Establish novelty separately before claiming publication.
- **OPEN / promising hardness route:** SqrtLog-SPACH and its checked reduction to polynomial-target 2-degenerate HOM; this would match the new general HOM exponent and still rule out single-exponential HOM.
- **OPEN and much harder:** arbitrary Circuit-SAT \(\to\) sparse polynomial-domain binary CSP with \(O(s/\sqrt{\log s})\) variables plus constraints.
- **ALTERNATIVE OPEN:** PCC \(\to\) degree-3 sparse CSP with \(O(K\sqrt{\log K})\) size, no longer attempting an unconditionally hardness-preserving linear output.
- **DO NOT REVIVE:** old \(q^{o(k)}\) SPACH/CEH hypotheses, or incorrectly claim that their easy solvability implies easy *general* graph problems via one-way reductions.

**Next checks:** independent audit of the imported Anthropic recurrence, exact CSP-to-HOM 2-degenerate gadget parameters, and comparison with existing #HOM-to-SubISO color coding results to establish priority.
