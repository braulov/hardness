# CEH research status, audit queue, and next experiments

**Checkpoint:** 2026-11-02 (the complete CEH conversation up to the pivot away from optimizing C=5/6). Use alongside [README](README.md), [reductions](01_reductions.md), and [matching-compiler research log](02_matching_compiler_research_log.md).

## 1. What is actually established vs. only proposed

| Statement | Current evidence | Safe status |
|---|---|---|
| Definition of CEH for a fixed explicit cubic expander and polynomial alphabet | Definition only | **CONJECTURE** |
| CEH is a special case of sparse bounded-degree binary CSP | Immediate | **EXACT** |
| CEH + §4 CSP→HOM parameter claims excludes $h^{o(n)}$ for degen ≤2 polynomial targets | Conditional reduction, paper needs parameter recheck | **CONDITIONAL / CHECK** |
| CEH→K-IS, K-Set Cover, K-Dominating Set, K-Set Packing | Explicit gadgets and elementary iff | **ELEMENTARY REDUCTIONS** |
| These implications give hardness for *sparse graph* versions | They do not; IS conflict cliques are dense | **FALSE AS STATED** |
| Fixed-width SAT algorithm applies to arbitrary 3-COL if its 2026 theorem is correct | Direct 3-CNF encoding | **CONDITIONAL ON EXTERNAL ALGORITHM** |
| Exact 2-CSP→log-width CNF | Explicit forbidden-pair clauses | **ELEMENTARY**; also in ../13_log_width_sat_and_polynomial_alphabet_csp.md |
| Sparse CSP→one cycle plus arbitrary matching | Occurrence-port gadget | **ELEMENTARY** (check degeneracies) |
| Sparse CSP→input-dependent cubic expander | Equality-port splitting of overlay | **PROOF SKETCH; VERIFY GADGET DETAILS** |
| Sparse CSP→fixed expanding graph with O$k^{4/3}$ edges | Universal-graph literature-based claim | **VERIFY REFERENCE AND CONSTRUCTIVITY** |
| Fixed bounded-degree expander has an O(k log k) universal minor model with efficient algorithm | Literature-based high-level claim | **VERIFY EXACT THEOREM / ALGORITHM** |
| Fixed cubic topology and arbitrary sparse CSP are fine-grained equivalent | This is precisely the target, no compiler | **OPEN** |
| Exact matching compiler with C=O(1) | No construction; many restricted obstacles | **OPEN** |
| Random-expander-CSP Poisson(1) number of solutions | Chat moment argument | **CLAIM / INDEPENDENT AUDIT NEEDED** |
| Any claimed C=3/4/5/6 model-specific no-go beyond elementary cut counting | Chat-only proofs, some rather delicate | **UNREVIEWED** |

The word **EXACT** means the relation and parameter-preserving map follow from an elementary argument, not that the result is novel. No priority or publication claim has been established.

## 2. The single main research objective

**Oblivious / fixed-topology 2-CSP compiler:**

Input: arbitrary explicit binary CSP with $k$ variables and $O(k)$ constraints, polynomial domain $q=k^{c_0}$, bounded-degree graph (max degree 3 after occurrence splitting).

Output: explicit relations on one predetermined cubic expander $F_{K}$, where $K\le Ck$, alphabet $Q\le(kq)^C$, and output/table-generation time is polynomial in the input length. Require
$$
\Gamma\text{ SAT}\quad\Longleftrightarrow\quad\Gamma'\text{ SAT}.
$$

One-sided randomized reduction is also a possible project **only with exact error model, amplification, and a separately randomized hardness statement**. We do not require preserving the witness values, source graph as a minor, all solutions, or the original named variables.

**Research payoffs if achieved:** For the appropriate quantifiers on fixed polynomial domains, CEH and SPACH become equivalent hardness sources. CEH then gives lower bounds for the reductions in [01_reductions.md](01_reductions.md), including polynomial-target degeneracy-2 HOM if §4's quantitative statement is verified.

**A faster CEH algorithm alone** does *not* generally solve arbitrary sparse CSP: the currently available minor-universal route loses $\Theta(\log k)$ variables. An improvement $Q^{O(K/\log^{1+\varepsilon}K)}$ at fixed expander size $K$ could survive this loss, if a suitable efficient minor embedding exists and the alphabet regime matches; a bare $Q^{o(K)}$ need not.

## 3. Do not follow these dead ends without a new reason

- Trying to rescue 3-COL hardness by dropping bounded degree (the new fixed-width SAT algorithms, if correct, handle dense 3-COL).
- Using $2^{o(N)}$ algorithms for output graphs of $N=\operatorname{poly}(k)$ vertices as though the exponent were $o(k\log k)$.
- Treating *any expander* (or overlaying dummy universal constraints) as the **one fixed graph** required by CEH.
- Concluding that a routing/minor obstruction rules out arbitrary nonlinear, existential, decision-preserving CSP reductions.
- Picking a single exact matching compiler state size $C=5$ or (6) as the main target, rather than any polynomial-domain decision compiler.
- Assuming $q^{O(\log k)}$ is polynomial when $q=k^{c}$: it is quasipolynomial and cannot be explicitly written in polynomial time.
- Treating a field fingerprint as sound against a witness that depends on the sampled hash.
- Mistaking kernel-equivalence of Schur complements for the stronger exact matrix identity, or vice versa.
- Treating random-instance local consistency / mean one solution as average-case or worst-case hardness.
- Inferring SPACH from Clique or Circuit-SAT without a new linear-parameter reduction. PCC/Circuit-SAT work is maintained in other repo branches and excluded from this CEH program.

## 4. Immediate audit tasks before writing a paper

1. **HOM §4:** Verify $n=\Theta(k), h=O(kq^2), \operatorname{degen}(H)\le2$ for every explicit relation encoding, including a simple cubic constraint graph and all subdivisions / auxiliary graph sizes. Compare https://arxiv.org/abs/2607.09377.
2. **Exact fixed expander family:** State on which even $K$ it exists and how it is constructed. If using Hamiltonian expanders $F_K=C_K\cup N$, this is an **additional** promise, not a property of every cubic expander.
3. **Universal-graph references:** Check the precise universal subgraph theorem (Alon–Capalbo etc.), the $O(K)$ vertex $O(K^{4/3})$ edge bounds and the algorithm for embedding. The union with a fixed expander can increase degree; that is acceptable only for the intermediate fixed-higher-degree model.
4. **Minor-universality references:** Check hypotheses of the $O(k\log k)$ embedding theorem and whether the minor model is efficiently findable. Check claims about $K^{\varepsilon}$ degree and linear-size minor universality; don't cite them as established without that inspection.
5. **Exact-projection normal forms:** Audit whether gauge fixing of all auxiliary degrees of freedom by local unary constraints always preserves the necessary edge relation form. Re-derive (B1), Schur complement normalization and the sheaf criterion (E1) independently.
6. **All C=5 numerical lemmas:** Recheck periodically cut averaging, the claimed (3/5) constant, all $O(1)$ rounding terms and matching existence, and the inner-boundary dimension calculation after contraction. Some later arguments rely on earlier claims; do not call the chain proved without a standalone audit.
7. **Random model:** Verify higher factorial moments and the correct treatment of collisions of multiple assignments when claiming the Poisson limit. It would still not prove hardness.
8. **Algorithmic quantifiers:** distinguish no deterministic $q^{o(k)}$, no bounded-error randomized $q^{o(k)}$, nonuniform algorithms, and algorithm families depending on fixed c; record whether $q'$ is exactly $K^{c'}$ or only bounded above.

## 5. Concrete next experiments (main objective first)

### A. Compress the fixed higher-degree universal graph *without* literal routing

We have a promising halfway house: a fixed $U_K$ on $O(k)$ vertices and $O(k^{4/3})$ edges (subject to audit). The original instance activates only $O(k)$ actual relations; the remaining relations are tautologies. Question: can one compile all those **sparse active checks** onto a fixed degree-3 support with $O(k)$ variables via shared witnesses, batch relational products, or algebraic local aggregators? The fixed pattern of potential edges has $k^{4/3}$ density, but the active-edge set is input-dependent and sparse. A naive per-edge port gadget bloats to $k^{4/3}$, and a simple routing map reintroduces the logarithm.

### B. Exploit weaker SAT iff rather than exact public matching

Forget the arbitrary matching as a public permutation. Design an instance-dependent encoding (x_v\mapsto f_v(\text{global witness})), where variables of the new expander need not correspond to original variables. A candidate is acceptable if its constraints imply the existence of *some* original satisfying assignment, and every original satisfying assignment allows *some* extension. It may destroy all other witness-level information.

Track: how many global degrees of freedom survive, does the encoding permit an inappropriate spurious assignment, and can each local table be written explicitly in $(kq)^{O(1)}$ time?

### C. Conditional impossibility for restricted compilation models

Previous tools can prove that any copy-and-route scheme has $\Omega(k\log k)$ total symbol transmissions for some remote matching, while simple cuts permit constant *information-theoretic* capacity. A useful negative result must state its precise syntactic model and should separate routing from algebraic mixing / existential computation. This is supporting work, **not** a substitute for A or B.

### D. A tiny executable testbed

For small fixed 3-regular $F_K$ and arbitrary matching $M$, construct local linear spaces $W_v$, compute their pairwise intersections and the boundary map $\partial$, and check $\operatorname{rank}\partial=\sum_v\dim W_v-K$. Compare candidate C=5/6 interface profiles with the separator bounds. Such experiments can falsify claims and help identify a *pattern* but do not certify universal $K\to\infty$ constructions. Do not allow the computational subproject to displace A/B.

## 6. Source pointers / cross-branches

- This CEH checkpoint: [README](README.md), [reductions](01_reductions.md), [matching compiler](02_matching_compiler_research_log.md).
- Existing SPACH / log-SAT formulation: [../13_log_width_sat_and_polynomial_alphabet_csp.md](../13_log_width_sat_and_polynomial_alphabet_csp.md).
- Other PCC dense-to-sparse research: [../14_permutation_clique_sparse_2csp_branch.md](../14_permutation_clique_sparse_2csp_branch.md), [../15_quadratic_form_and_alldifferent_interface_barriers.md](../15_quadratic_form_and_alldifferent_interface_barriers.md), [../18_randomized_low_soundness_pcp_to_linear_csp.md](../18_randomized_low_soundness_pcp_to_linear_csp.md).
- HOM preprint: https://arxiv.org/abs/2607.09377 .
- Marx-style 2024 sparse 2-CSP method: https://arxiv.org/html/2311.05913v3 .
- Classic code-realization / separator tool: https://arxiv.org/abs/0805.2199 .
- OpenAI 2026 ETH manuscript (independent review ongoing): https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026 .

## 7. Current checkpoint

**What we have:** a narrowly formulated fixed-expander source (CEH), solid elementary conditional reductions to several target problems, explicit \partial equivalences (input-dependent cubic expansion, fixed higher-degree universal graphs as a claimed literature route), and a substantial library of compiler/model-specific mathematical obstructions.

**What we do not have:** an unconditional lower bound, an independent justification of CEH from another hardness assumption, a parameter-optimal sparse CSP to *predetermined cubic expander* decision reduction, a constant-size exact matching compiler, or an audited proof that the latter is impossible.

**Next question to pursue, with priority over C=5/6 algebra:** Can we exploit the fact that only $O(k)$ relations are *active* inside a fixed universal graph with $O(k^{4/3})$ possible edges, to simulate their conjunction using $O(k)$ vertices of a predetermined cubic expander and polynomial domain, without testing the relations one by one along explicit routed paths?
