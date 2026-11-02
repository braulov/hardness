# Closed hardness hypotheses after the 2026 sparse binary-CSP algorithms

**Status date:** 2026-11-02. **This is the canonical status ledger for CSP/CEH-related hypotheses in the hardness repository.** This file supersedes *hardness interpretation*, not the mathematical content, of the older CEH, sorting, matching-compiler, and SPACH notes. No research files or branches are deleted.

**Verification boundary.** This status is **conditional on accepting the externally claimed algorithmic theorems**. The downstream parameter calculations and the elementary bounded-degree reduction are independently checkable. This repository has **not** independently rebuilt the Anthropic/OpenAI tensor recursion or Nguyen's Lean development. Do not call the results independently certified merely because the preprints report Lean formalization.

## 1. Primary claimed theorems

1. **Nguyen**, *A Sublinear Treewidth Exponent for Binary Constraint Satisfaction* (Hexagon 2611.00004v1, 2026-11-02), [paper page](https://hexagonmath.org/2611.00004v1), [indexed full-text rendition](https://hub.valency.io/works/W_88675vdy). Its Theorem 1.2 states one deterministic **domain-uniform** exact counting algorithm for *every* complete-table binary CSP of fixed maximum degree $\Delta$, $k$ variables, domain $q\ge2$, length $L$:
   \[
   T(k,q,L)\le A_\Delta L^{p_\Delta}
       q^{C_\Delta k/\sqrt{\log k}}\qquad(k\ge k_\Delta).
   \]
   Crucially, $\Delta$ is fixed and the constants are independent of $q$, $k$, and the relation tables. The paper separately claims a sparse tuple-input algorithm and a literal counterexample to **Marx (2010), Conjecture 1.4**. It reports a Lean development importing Anthropic and OpenAI work; external replay was not performed here.
2. **OpenAI**, *The Exponential Time Hypothesis is False* (2026-10-25), [full tensor theorem source](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex). Assuming the manuscript's **full Boolean tensor-contraction theorem** (not just its separately documented fixed-width Lean theorem), the explicit bit-wire encoding in [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md) yields for arbitrary binary CSP with $k$ variables, $m$ constraints, polynomial domain $q=k^{O(1)}$:
   \[
   \operatorname{poly}(L)\,
   2^{O(((k+m)\log q)/\sqrt{\log((k+m)\log q)})}.
   \]
   For $m=O(k)$ and $q=k^c$, this is $2^{O(k\sqrt{\log k})}=q^{o(k)}$. **This full tensor theorem is an external premise not declared part of the limited fixed-width-CNF Lean scope.** See [note 33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md) and [the separate Nguyen alert](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md).

These are *two derivation paths*, not necessarily two independent underlying proofs: Nguyen credits/imports Anthropic and OpenAI techniques. They agree on the relevant exponent.

## 2. Why sparse means EASY in the strong hypothesis's scale

Even without maximum-degree restriction, any explicitly represented binary CSP on $k$ variables and $m=O(k)$ binary constraints can be converted to degree at most 3:

- Create a variable occurrence $x_{v,e}$ for each incidence of an original constraint with $v$.
- For each original variable, link all its copies by a path of binary equality constraints. Its occurrences need at most two path edges and one original edge each.
- Copy each original relation to the corresponding occurrence pair. Isolated variables are handled by their unary domain checks.

The output has $k'\le2m+k=O(k)$ variables, $m'=O(k+m)$ constraints, **the same domain $q$**, and polynomial-time explicitly generated equality tables. Therefore Nguyen's theorem with $\Delta=3$ implies
\[
T_{\mathrm{sparse}}(k,q,L)
 =\operatorname{poly}(L+k+q)\,
 q^{O(k/\sqrt{\log k})},
\]
where the hidden constant also depends on the fixed upper bound $m/k$ and input representation. For $q=k^{\Theta(1)}$:
\[
\log_2 T=O(k\sqrt{\log k})+O(\log L)
       =o(k\log k).
\]
This is an **exact counting** algorithm in the complete-table model, hence exact decision; deterministic already contradicts deterministic and bounded-error-randomized *hardness* assumptions at this scale.

For completely unrestricted $m$, the analogous bound depends on $k+m$, **not just $k$**. One cannot infer a fast $2^{o(k\log k)}$ algorithm for dense CSP with $m=\Theta(k^2)$.

## 3. Hypothesis ledger

| Hypothesis / proposed source | Decision as of 2026-11-02 | Reason / scope |
|---|---|---|
| **ETH**, and **SETH** in their conventional fixed-width SAT forms | **CONDITIONALLY FALSE under the Oct. 2026 ETH-refutation papers** | Original 3-SAT $2^{o(n)}$ theorem (and linear fixed-$w$ transformations for any fixed $w$); external theorem's independent validity not audited here |
| **SPACH**: no deterministic $q^{o(k)}\operatorname{poly}(L)$ algorithm on sparse degree-3 binary CSP, $q=k^c$ | **CLOSED / CONDITIONALLY REFUTED** | Explicit $q^{O(k/\sqrt{\log k})}$ upper bound |
| **rSPACH**: same excluding bounded-error randomized algorithms | **CLOSED / CONDITIONALLY REFUTED** | Same deterministic upper bound |
| **CEH**, fixed cubic expander, $q=k^c$, no $q^{o(k)}$ algorithm | **CLOSED / CONDITIONALLY REFUTED** | Subclass of degree-3 binary CSP |
| Randomized CEH and variants for *fixed/bipartite/3-regular/expanding* CSP graph with unrestricted explicit relations | **CLOSED whenever they assert no $q^{o(k)}$** | The algorithm covers every bounded-degree instance; extra graph promises cannot restore hardness |
| Any other proposed no-$q^{o(k)}$ hypothesis for sparse binary CSP (including $m=O(k)$ but unbounded max degree) with explicit polynomial-size relations | **CLOSED / CONDITIONALLY REFUTED** | Occurrence-splitting to maximum degree 3 preserves $O(k)$ and $q$ |
| Marx (2010) **literal Conjecture 1.4** forbidding a globally correct $f(G)\,\lVert I\rVert^{o(\operatorname{tw}(G))}$ algorithm on any unbounded-treewidth class | **CLAIMED REFUTED** | Nguyen Theorem 1.1, bounded-degree expanders, $\operatorname{tw}(G)=\Theta(k)$; note arbitrary graph-dependent $f(G)$ |
| Any CEH/SPACH-*based* $q^{o(k)}$ conditional lower-bound argument for polynomial-target HOM / parameterized IS / Set Cover / Dominating Set / Set Packing | **CLOSED AS A HARDNESS ARGUMENT** | Its hardness premise is false if the new algorithms are valid; the **one-way gadget reductions remain correct**, and no general target algorithm follows from reversing them |
| **PCC / RPCC** (arbitrary dense Permutation $k\times k$ Clique), **PSCH** (ordinary polynomial-size Clique) | **NOT REFUTED** | No known $(k+m)=O(k)$ reduction into the easy CSP class; dense graphs have $\Theta(k^2)$ checks. Distinguish their different quantitative hypotheses |
| **LogSAT-A/B** (the proposed *algorithmic statements* about logarithmic-width CNF) | **NOT RESOLVED** | CSP$\to$CNF is the wrong direction to infer a general LogSAT algorithm from a CSP algorithm |
| General sparse (co)graphic full-span feasibility / SGR-CSP and other rank/Span hypotheses | **NOT REFUTED BY THIS RESULT** | No established linear-size reduction into ordinary sparse binary CSP with polynomial domain and appropriate parameter |
| **NoSingleExpSparseCSP** (no $2^{O(k)}$ for $q=k^c$) | **NOT REFUTED** | The exhibited time $2^{O(k\sqrt{\log k})}$ is super-single-exponential; this is a *different, weaker* possible hypothesis, not the strong SPACH |
| Structural conjecture: a SAT-iff **fixed-expander $O(k)$-variable compiler** exists | **STILL OPEN AS A MATHEMATICAL PROBLEM** | The new upper bound removes its hardness motivation, but neither constructs nor excludes the compiler; it would map one easy class to another |

**Pay attention:** An algorithm $q^{O(k/\sqrt{\log k})}$ does **not** contradict a *no $q^{o(k/\log k)}$* lower bound, or an *absence of $2^{O(k)}$* hypothesis. Conversely, the old Marx/ETH conditional statements do not become mathematically incorrect as implications simply because their premise is false; they are no longer useful hardness evidence.

## 4. Consequences for the ongoing reductions and HOM

- The entire CEH/SPACH proof-of-hardness program with the strong $q^{o(k)}$ quantifier is **archived / stopped**, including the hoped-for transfer to bounded-degeneracy HOM. It is not sensible to continue proving SPACH or CEH from a conjecture taken to be hard.
- The sorting-network $O(k\log k)$ fixed-expander simulation, occurrence cycle+matching normal form, linear/matroid/Schur complement compiler attempts, and the tagged-polynomial product identity retain their mathematical meaning. No contradiction: such a compiler may exist, but it no longer creates a hard fixed-expander target.
- **Sparse-source HOM:** if $G$ has $n$ vertices and $O(n)$ edges and target $H$ has $h=n^{O(1)}$ vertices, encode HOM as binary CSP with $k=n,m=O(n),q=h$. Under the theorem,
  \[
  T_{\mathrm{HOM}}=\operatorname{poly}(|G|,|H|)\,h^{O(n/\sqrt{\log n})}.
  \]
  For $h=n^{\Theta(1)}$ this is $2^{O(n\sqrt{\log n})}$, **not** $2^{O(n)}$. This algorithm does not require target degeneracy bounds. General HOM with dense source is not covered by this parameter count.
- **PCC→sparse CSP compilers:** a hypothetical polynomial-time compiler from $k\times k$ PCC into maximum-degree-$O(1)$ binary CSP with $r=o(k\sqrt{\log k})$ variables and polynomial domain, together with Nguyen, implies a $2^{o(k\log k)}$ PCC algorithm. Thus **PCC hardness + Nguyen + such a compiler are mutually incompatible**. This is *not* a proof of the compiler's impossibility; if built, it could instead refute PCC hardness. The earlier compiler lemmas remain mathematics but cannot support new SPACH lower bounds under the premise.
- **Circuit-SAT→sparse CSP** with $r=k+m=o(s/\sqrt{\log s})$ and polynomial domain would similarly yield $2^{o(s)}$ Circuit-SAT for $s$ primary input bits. Hence an input-efficient compiler with these parameters is incompatible with a hypothesized no-$2^{o(s)}$ Circuit-SAT lower bound under the CSP algorithm. Neither Circuit-SAT itself nor its hypothesis has been refuted by the CSP theorem.
- As a structural note, Nguyen also claims a counterexample to the *literal* 2010 conjecture about sublinear-in-treewidth exponents on a specially constructed class of expanders. Do **not** conflate that with the older ETH-conditional $o(\mathrm{tw}/\log\mathrm{tw})$ lower bound.

## 5. Source verification / limitations

- The hexagon **landing page** and a public indexed full-text rendition show the statement and calculations of Nguyen's Theorems 1.1–1.2, including the domain-uniform constants and declared machine model. The PDF endpoint was inaccessible to the reader in this run; **this is not a line-by-line PDF review**.
- The paper states that its Lean artifacts check the downstream CSP results with imported Anthropic and OpenAI modules. We have not checked whether every quantitative imported theorem in the proof chain was independently formalized, or reproduced the native runtime bound.
- The general OpenAI tensor theorem referenced by note 33 is **broader than** the fixed-width #CNF Lean result documented separately. Note 33's Boolean tensorization and parameter implications do not supply a proof of that external theorem.
- Hexagon hosts preprints without certifying correctness. Thus **CLOSED / CONDITIONALLY REFUTED** is the responsible repository classification rather than asserting a community-reviewed unconditional theorem.

## 6. Cross-references

- [Nguyen domain-uniform source audit](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md).
- [Boolean tensorization / independent derivation from the full OpenAI tensor theorem](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).
- [Historical SPACH statement](13_log_width_sat_and_polynomial_alphabet_csp.md).
- [Historical CEH and its five focused logs](ceh/README.md).
- [PCC and compiler branches](14_permutation_clique_sparse_2csp_branch.md), [PSCH](psch/README.md).
- [Existing main README](../README.md).
