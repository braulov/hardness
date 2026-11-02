# Boolean tensor contraction for sparse binary CSP: conditional algorithm and branch triage

**Date:** 2026-11-02.  
**Status:** CONDITIONAL on the **full** Boolean tensor-contraction theorem (Theorem D.1 / \`thm:tensor-contraction\`) in OpenAI's October 25, 2026 manuscript. The elementary CSP-to-tensor construction and all parameter implications below are **proved conditional consequences**, not independent verification of that external theorem. **Do not cite them as unconditional algorithmic facts.**

## 1. External theorem actually used

Source: OpenAI, *The Exponential Time Hypothesis is False* (October 25, 2026), [\`build/quantitative-reduction.tex\`, theorem \`thm:tensor-contraction\`](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex).

In the relevant specialization: a bipartite Boolean tensor network with at most \(CS\) **bit wires**, at most \(\operatorname{poly}(S)\) vertices, maximum local degree \(\le \lceil S^{9/10}\rceil\), entries in \((\mathbb Z/2^{P_0}\mathbb Z)[V]/(V^\ell)\) where \(P_0,\ell\le CS\), and uniformly efficiently computable local entries admits deterministic exact contraction in
\[
  (S+\mathcal L)^{O(1)}
  2^{O(S/\sqrt{\log S})}
\]
time and polynomial space, subject to the theorem's precise local-entry-time bound. The case \(\ell=1\) is explicitly allowed. Here \(\mathcal L\) is the explicit tensor-network description length; the theorem does **not** assert that \(\mathcal L=O(S)\).

**Verification boundary:** [Lean formalization scope, item 378](https://github.com/openai/math/blob/main/lean/docs/378.md) explicitly covers a weaker fixed-width #CNF counting theorem with exponent \(O(n(\log\log n)^2/\sqrt{\log n})\). It does **not** say that this general tensor-contraction theorem has been Lean-formalized. The general tensor theorem therefore remains an **external, independently unaudited premise** in this note.

## 2. Explicit reduction: arbitrary sparse binary CSP to Boolean tensor network

Let \(\Gamma\) have \(k\) variables with domain \([q]\), \(m\) binary constraints, and unary domain restrictions. All relations are **explicit tables**; the input length is \(\mathcal L_\Gamma\ge\Omega(m)\), typically \(O(mq^2\operatorname{polylog}q)\). Assume \(q\ge2\), \(q=k^{O(1)}\), and \(m=O(k)\). Put \(b=\lceil\log_2q\rceil\).

- Encode each CSP value by \(b\) Boolean bits. At each original variable, use an arity-\(b\) validity tensor \([z<q\ \text{and}\ z\in U_v]\) or a corresponding unary block check.
- For each constraint \(R_{uv}\), create an arity-\(2b\) Boolean tensor \(T_{uv}(\mathbf a,\mathbf b)=[(\operatorname{decode}(\mathbf a),\operatorname{decode}(\mathbf b))\in R_{uv}]\).
- For every variable-bit and every incidence, connect the corresponding ports using an equality/copy *tree* of degree at most three. These enforce one shared bit across all occurrences, **with exactly one extension for each shared bit value**. Isolated variables still contribute their valid values through their unary validity tensors.
- Subdivide each wire by a binary equality tensor if needed to make the whole network bipartite. This doubles the wire count only by a constant factor.

The contraction over \(\mathbb Z/2^{P_0}\mathbb Z\) is exactly \(\#\mathrm{SAT}(\Gamma)\bmod 2^{P_0}\). Choose
\[
  P_0=kb+1.
\]
Because \(0\le\#\mathrm{SAT}(\Gamma)\le q^k\le 2^{kb}\), its residue uniquely determines the exact count, including the endpoint \(2^{kb}\).

There are
\[
  M=O((k+m)b)=O((k+m)\log q)
\]
bit wires, a polynomial number of tensor vertices, and maximum degree \(O(\log q)\). Every local entry is computable in \(\operatorname{poly}(\mathcal L_\Gamma,k,\log q)\) time, using only validity checks, equality, and explicit relation-table lookup. For \(q=k^{O(1)}\), \(\log q=O(\log k)\), so the degree restriction \(O(\log q)\le M^{9/10}\) holds for sufficiently large \(k\); finitely many small instances can be brute-forced. Also \(P_0=O(M)\), and \(\ell=1\).

**Conditional theorem (sparse 2-CSP):**
\[
 \boxed{
 T_\Gamma=
 \operatorname{poly}(\mathcal L_\Gamma)\,
 2^{\,O\bigl((k+m)\log q/\sqrt{\log((k+m)\log q)}\bigr)}
 }
\]
for the polynomial-alphabet regime above, with polynomial space. On \(m=O(k)\) and \(q=k^{\Theta(1)}\),
\[
  T_\Gamma=\operatorname{poly}(\mathcal L_\Gamma)
  2^{O(k\sqrt{\log k})}
  =\operatorname{poly}(\mathcal L_\Gamma)\,q^{O(k/\sqrt{\log k})}
  =\operatorname{poly}(\mathcal L_\Gamma)\,q^{o(k)}.
\]
For constant \(q\), the stronger form \(2^{O(k/\sqrt{\log k})}\operatorname{poly}(\mathcal L_\Gamma)\) follows. **The bound is conditional** and should not be indiscriminately extrapolated to arbitrary huge \(q\) without rechecking the theorem's local-degree restriction.

This is an exact **counting** algorithm, hence also a decision algorithm; no randomness, isolation, or numerical cancellation is used.

## 3. Conditional contradiction to SPACH and CEH as currently formulated

[SPACH](13_log_width_sat_and_polynomial_alphabet_csp.md) hypothesizes no deterministic \(q^{o(k)}\operatorname{poly}(\mathcal L_\Gamma)\) algorithm on sparse degree-3 binary CSP over \(q=k^c\), for a fixed \(c>0\).

[CEH](ceh/README.md) hypothesizes the analogous lower bound even on one predetermined cubic expander family with arbitrary explicit binary tables.

Both are **subclasses of the theorem above**. Therefore:
\[
  \text{Full tensor theorem} \implies
  \neg\mathrm{SPACH}\ \land\ \neg\mathrm{CEH}.
\]
The deterministic algorithm also refutes their stated *randomized-hardness* variants (a deterministic algorithm is a bounded-error randomized algorithm with error zero).

**Research status: CLOSED / CONDITIONALLY REFUTED under the full tensor theorem.** Do not use CEH or SPACH as viable sources of \(q^{o(k)}\)-lower bounds while accepting that theorem. The combinatorial fixed-topology compiler problem, explicit reductions, and gadget constructions in the archive are **not** thereby disproved and should not be deleted; they are simply no longer supported by CEH as a hardness motivation.

In particular, the asserted CEH-based *hardness implications* for polynomial-target 2-degenerate HOM, Set Cover, Independent Set, Dominating Set, Set Packing, etc., become **vacuous under this premise**: the reductions may remain mathematically correct, but the source conjecture is false. The theorem does **not** by itself give fast algorithms for these **general target problems** via those one-way reductions.

## 4. Conditional Circuit-SAT compiler no-go and surviving range

Fix \(d\). **Circuit-SAT Hypothesis, input parameter \(s\):** no uniform \(2^{o(s)}\operatorname{poly}(s)\)-time SAT solver for *arbitrary* Boolean circuits with \(s\) primary inputs and at most \(s^d\) gates (quantifiers over \(d\) must be specified; the argument works for each \(d\) where the hypothesis is assumed).

Suppose a polynomial-time, SAT-iff compiler maps such circuits to explicit binary CSP with polynomial domain \(q=s^{O_d(1)}\) and \(r=k+m\) variables plus constraints. Tensorization gives
\[
  T_{\mathrm{CircuitSAT}}(s)
  \le \operatorname{poly}(s)
  2^{\,O\bigl(r\log s/\sqrt{\log(r\log s)}\bigr)}
\]
when the output is polynomial-size (which it is for polynomial \(q\)).

Consequently, a universal compiler with
\[
  \boxed{r=o(s/\sqrt{\log s})}
\]
would contradict the Circuit-SAT Hypothesis, **conditional on the full tensor theorem** (for very small \(r\), the exponent is even smaller). The original target \(k=O(s/\log s),\,m=O(k)\) is in this forbidden range.

**This is not an unconditional no-go theorem.** It is a three-way incompatibility: full tensor theorem + Circuit-SAT Hypothesis + such a universal compiler cannot all hold simultaneously. If the compiler were constructed, it would instead yield a \(2^{o(s)}\) Circuit-SAT algorithm (and invalidate the assumed hypothesis).

The weaker goal
\[
  r=O(s/\log^{1/4}s),\quad q=s^{O_d(1)}
\]
is **not ruled out by this particular bound**, and remains a candidate for conditional \(2^{O(n)}\)-HOM lower-bound transfers if a suitable CSP-to-HOM reduction has source size \(O(r)\) and polynomial-size target. No such universal compiler has been constructed. In particular, arbitrary polynomial-size Circuit-SAT is **not** reduced to this CSP class in the current project.

## 5. Cycle-rank consequence

The proven preprocessing [\`13_binary_csp_cyclomatic_reduction.md\`](13_binary_csp_cyclomatic_reduction.md) either detects UNSAT or reduces a binary CSP of primal cyclomatic number \(\mu\) to \(k'\le2\mu\) variables, \(m'\le3\mu\) edges, **without increasing \(q\)**. Combining that reduction with the external tensor theorem yields, for polynomial \(q\) and valid theorem parameters,
\[
  \boxed{
  T_\Gamma=\operatorname{poly}(\mathcal L_\Gamma)\,
  2^{O(\mu\log q/\sqrt{\log(\mu\log q)})}
  }
\]
for \(\mu\ge1\), with polynomial time for \(\mu=0\); this is *conditional*. The unconditional, previously recorded \(q^\mu\operatorname{poly}\) cycle-cutset algorithm remains correct.

## 6. Sparse HOM consequence and caveat

For \(G\) with \(n\) vertices and \(O(n)\) edges and \(H\) with \(h=n^{O(1)}\) vertices, \(\mathrm{HOM}(G,H)\) is a binary CSP with \(k=n,\ q=h,\ m=O(n)\). The conditional theorem gives
\[
  \boxed{
  T_{\mathrm{HOM}}
  =\operatorname{poly}(|G|,|H|)
    2^{O(n\log h/\sqrt{\log(n\log h)})}.
  }
\]
When \(h=n^{\Theta(1)}\), this is \(2^{O(n\sqrt{\log n})}\operatorname{poly}(|H|)\). It is **not** \(2^{O(n)}\), does not by itself refute a prospective no-single-exponential result, and places no restriction on \(\operatorname{degen}(H)\). When \(h=O(1)\), the exponent instead becomes \(O(n/\sqrt{\log n})\).

A hypothetical Circuit-SAT-to-HOM reduction with \(n+|E(G)|=o(s/\sqrt{\log s})\), polynomial \(h\), and polynomial construction time would likewise contradict the Circuit-SAT Hypothesis under the tensor theorem. Do not infer any quantitative property of the project's existing HOM gadgets without auditing them separately.

## 7. Branch triage (what closes, what survives)

| Branch / proposition | Decision | Reason |
|---|---|---|
| SPACH (deterministic and randomized no-\(q^{o(k)}\) sparse polynomial-alphabet 2-CSP) | **CLOSED, CONDITIONALLY REFUTED** | Tensor solver directly applies |
| CEH (same hardness on a fixed cubic expander) | **CLOSED, CONDITIONALLY REFUTED** | Restriction of sparse binary CSP |
| SPACH/CEH-derived \(q^{o(k)}\)-hardness transfers to polynomial-target HOM and other graph problems | **CLOSED AS HARDNESS ARGUMENTS under premise** | Invalid hardness source, even if the reduction is valid |
| Universal Circuit-SAT \(\to\) sparse 2-CSP with \(k,m=O(s/\log s),q=\operatorname{poly}(s)\) **under Circuit-SAT Hypothesis** | **CLOSED as a compatible ETH-replacement route** | Would refute the very Circuit-SAT hypothesis used as source |
| Seek universal Circuit-SAT \(\to\) CSP with \(k+m=o(s)\) but \(k+m\not=o(s/\sqrt{\log s})\) | **OPEN** | Tensor bound alone does not preclude it |
| Dense PCC / Polynomial-Size Clique Hypothesis, LogSAT-A/B | **NOT REFUTED HERE** | Dense constraint count or different source size defeats the \(M=O(k\log q)\) budget |
| Explicit fixed-expander simulation, Beneš/sorting, matching compilers, rank/permutation identities | **RETAIN AS MATHEMATICAL STRUCTURE; deprioritize hardness motivation** | Tensor theorem is an algorithm, not an impossibility of these reductions |
| General graphic/cographic full-span Span-CSP (SCGS/SGR), unrestricted Set Cover, general HOM, arbitrary Circuit-SAT | **NOT REFUTED HERE** | No established \(O(n)\)-wire tensorization for the rank test or appropriate fine-grained reduction |
| Independent auditing / unconditional proof of full tensor theorem | **HIGH PRIORITY** | Entire new branch closure is contingent on this theorem |

## 8. Sources and historical note

- [OpenAI Oct. 25 manuscript, full tensor theorem (source TeX)](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex).
- [OpenAI October 25 main theorem](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex).
- [Lean scope of the *fixed-width CNF* theorem](https://github.com/openai/math/blob/main/lean/docs/378.md).
- [Previously archived Boolean tensorization of branching programs](22_bp_boolean_tensor_wires_and_width_bottleneck.md).
- [Previous sparse polynomial-alphabet 2-CSP candidate and quantitative discussion](13_log_width_sat_and_polynomial_alphabet_csp.md).
- [Previous CEH fixed-expander branch and reductions](ceh/README.md).
- [Previously proved cyclomatic-number preprocessing](13_binary_csp_cyclomatic_reduction.md).

**Important practice:** do not overwrite the historical research logs. Put the updated conditional status prominently at their top; preserve proofs, counterexamples, and reductions for future use if the external premise changes.
