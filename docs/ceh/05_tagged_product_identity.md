# Exact tagged-product identity as a topology-free normal form for sparse CSP

**Research checkpoint, 2026-11-02.** This is a new focused subprogram of the CEH branch. The elementary product identity is proved below; it is closely related to *permutation / multiset checks* used in algebraic proof systems (PLONK). **No linear-size fixed-expander compiler is constructed.** The objective remains the satisfiability-only SPACH→CEH reduction, not optimizing the exact matching compiler.

## 1. Exact reduction to local tests + ONE formal polynomial identity

Input: an arbitrary binary CSP with $k$ original variables, $m=O(k)$ binary constraints, domain $[q]$, $q=k^{O(1)}$. Create $t=2m$ occurrence values $a_i\in[q]$, one per constraint endpoint. Pair the occurrence slots of each constraint so its original relation is still checked locally, with an explicit relation table.

For each original variable, choose a cyclic permutation of all its occurrence positions. Their union gives $\sigma\in S_t$. Thus the copies are consistent iff
\[
a_i=a_{\sigma(i)}\qquad\text{for every }i.
\]

Choose a prime $p>tq$, so $p=\operatorname{poly}(k,q)$ (Bertrand's postulate or an ordinary polynomial-time prime search). Index occurrences $i=0,\dots,t-1$, values $a\in\{0,\dots,q-1\}$, and define the injective map
\[
h(i,a)=iq+a\in\mathbb F_p.
\]
Define the **formal univariate polynomials**
\[
P_a(X)=\prod_{i=0}^{t-1}(X-h(i,a_i)),\qquad
Q_{a,\sigma}(X)=\prod_{i=0}^{t-1}(X-h(\sigma(i),a_i)).
\]

**Exact lemma.**
\[
P_a\equiv Q_{a,\sigma}
\iff a_i=a_{\sigma(i)}\quad\forall i.
\]
Indeed, over a field a monic polynomial determines its multiset of linear roots. Since the tags $i$ are unique and $h$ is injective on pairs $(i,a)$, equality of root multisets forces the value attached to every tag to agree. Conversely, equality along $\sigma$ makes the root multisets equal.

Therefore $\Gamma$ is satisfiable iff there exist $t=O(k)$ occurrence values passing the $m$ pair-local original relations **and the single global formal product identity**. This preserves a polynomial-size base field and encodes all instance-specific graph topology in local constants $\sigma(i)$.

**What is proved:** an exact normal form with an additional *global polynomial-identity predicate*. **What is not proved:** ability to realize that predicate by $O(k)$ binary local constraints on one predetermined constant-degree graph, which is the real CEH goal.

## 2. The tempting $O(k)$ grand-product check is NOT sound

Choose a point $r\in\mathbb F_p$ and replace $P_a\equiv Q_{a,\sigma}$ by $P_a(r)=Q_{a,\sigma}(r)$. Both sides can be computed with $O(t)$ field multiplications along a predetermined path or cycle, and thus have a fixed-size locally-checkable accumulator CSP.

For **fixed already chosen** $a$ violating the identity, Schwartz–Zippel gives error at most $(t-1)/p$ for random $r$. But in the CSP the occurrences $a$ are existentially guessed **after** the reduction has fixed $r$. This reversal of quantifiers makes Schwartz–Zippel insufficient to justify a randomized many-one reduction. A union bound over all $q^t$ potential occurrences would require exponentially large $p$ in the worst case.

**A direct false positive even with our injective $h$.** Let $t=3$, $q=11$, $p=101>tq=33$, $\sigma=(0\,1\,2)$, $r=17$, and $a=(1,3,5)$.
\[
P_a(17)=16\cdot3\cdot(-10)=25\pmod{101},
\]
\[
Q_{a,\sigma}(17)=5\cdot(-8)\cdot12=25\pmod{101},
\]
yet $a_0,a_1,a_2$ are not equal. All six factors are nonzero. Therefore neither a single evaluation nor merely requiring inverses provides an exact identity test.

**Important distinction:** this counterexample establishes that the *local consistency predicate* is not exactly represented by the point check. By itself it does not prove that every randomized reduction using a grand product fails on every hard NO instance; any such stronger claim would require a separate construction and soundness analysis.

This is the same general phenomenon addressed by commitment-before-random-challenge in interactive polynomial permutation arguments. Those protocols cannot be transplanted as ordinary existential CSP constraints without separately establishing binding/soundness.

## 3. A rigorous one-pass accumulator lower bound

Consider a fixed-order scan of $2s$ records arranged as $(x_1,\ldots,x_s,y_1,\ldots,y_s)$ over $[q]$. The goal is exact acceptance iff $x=y$. Even if the verifier is **nondeterministic**, a one-pass finite-state machine needs at least $q^s$ distinct states at the midpoint.

**Fooling-set proof:** For each $x\in[q]^s$, choose an accepting run on $(x,x)$ and let $u_x$ be its midpoint state. If $u_x=u_{x'}$ for $x\ne x'$, splice the first half of the accepting run for $(x,x)$ with the second half of that for $(x',x')$. This accepts $(x,x')$, a contradiction. Thus all $u_x$ are different.

Consequently, a single path-accumulator maintaining $C=O(1)$ polynomial-alphabet field symbols ($q^{O(C)}$ possible states) cannot exactly implement arbitrary matching/equality constraints across such a cut. It needs $\Omega(s\log q)$ bits of state at that cut, i.e. $C=\Omega(s)$ in the fixed polynomial-domain regime.

**Scope:** this rules out single-pass fixed-order accumulator architectures, even with nondeterministic local witnesses. It **does not rule out** distributed checking on a constant-degree *expander*, whose balanced cuts contain $\Theta(s)$ edges and may carry $\Theta(s\log q)$ bits collectively. Nor does it rule out satisfiability-only reductions that change the representation of the source problem.

## 4. A concise sufficient target

Call an **exact locally checkable product-identity compiler** a uniform family of predetermined bounded-degree constraint graphs $B_t$ with $O(t)$ vertices, polynomial alphabet, and designated ports receiving the local pairs $(h(i,a_i),h(\sigma(i),a_i))$, such that its existential local constraints accept *precisely* when
\[
\prod_i(X-u_i)\equiv\prod_i(X-v_i).
\]
It should have constant-degree ports and explicitly enumerable polynomial-size local tables. The root lists are computed locally from $(a_i,\sigma(i))$; no direct permutation routing is allowed as a hidden primitive.

**If such a compiler exists**, compose it with the local $R_e$ tests, overlay a predetermined constant-degree expander with tautological constraints, and apply the constant-size port-cycle splitting from [01_reductions.md](01_reductions.md). This would yield SPACH→fixed-cubic-expander CSP with $O(k)$ variables and polynomial alphabet, proving the desired hardness-hypothesis equivalence with appropriate quantifiers.

This is a **sufficient but stronger** subproblem, not a necessary condition for arbitrary SAT-iff compilers.

## 5. Research directions, with failure tests

- Exact coefficient approach: both polynomials have $O(t)$ coefficients; materializing all intermediate coefficient vectors in an ordinary balanced product tree incurs $\Theta(t\log t)$ coefficient occurrences even before accounting for fast polynomial multiplication. This shows that **the naive coefficient-tree implementation** does not give an $O(t)$ constant-word circuit; it is not an unconditional lower bound for alternative representations.
- Symbolic algebra / implicit product identities: can the equality of two factored univariate polynomials be certified by $O(t)$ locally checked *polynomial-size* field elements without evaluating a random point? Investigate structural constraints in the restricted tagged-factor setting.
- Do **not** assume generic Reed–Solomon evaluation membership has constant-weight linear parity checks: an $[n,d]$ MDS code has dual minimum distance $d+1$, so nonzero linear checks on $O(1)$ coordinates do not certify it when $d=\Theta(n)$.
- Stronger original objective: search directly for decision-preserving local verifiers of *all* CSP relations, without requiring exact matching or product equality. The algebraic factorization is only one attack route.

## 6. Relevant prior art / credits

- Feige–Jozeph, *Universal Factor Graphs* (2012), https://arxiv.org/abs/1204.6484 .
- Austrin–Brown-Cohen–Håstad, *Optimal Inapproximability with Universal Factor Graphs* (SODA 2021 / TALG 2025), https://eccc.weizmann.ac.il/eccc-reports/2019/TR19-151/ .
- PLONK polynomial permutation / grand-product identities: https://eprint.iacr.org/2019/953.pdf .
- Existing sorting bridge: [04_universal_factor_graph_sorting_bridge.md](04_universal_factor_graph_sorting_bridge.md).

**Status at this checkpoint:** exact algebraic normal form PROVED; false positive for single-point evaluation PROVED; one-pass nondeterministic memory lower bound PROVED; fixed-topology $O(k)$ verifier still OPEN.
