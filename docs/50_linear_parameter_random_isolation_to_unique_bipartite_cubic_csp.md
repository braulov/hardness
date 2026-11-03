# Fine-grained randomized isolation to promise Unique binary CSP on simple bipartite cubic graphs

**Date:** 2026-11-03  
**Status:** PROVED reduction below, modulo the classical Mulmuley–Vazirani–Vazirani Isolation Lemma. This is a **randomized polynomial-query Turing reduction**, NOT a deterministic many-one reduction; no new computational hardness hypothesis is proved. Parameters are made explicit to preserve the \(k/\sqrt{\log k}\) exponent with polynomial domain. Fine-grained priority/novelty among bounded-degree CSP reductions has NOT been exhaustively audited.

## 1. Statement with the correct randomization and promise quantifiers

Let \(\Gamma\) be an **explicit complete-table binary CSP** on \(k\ge2\) variables, \(m=O(k)\) binary constraints, and common alphabet \([q]\) where \(q=k^{O(1)}\). The primal graph may initially have degree three; for general \(m=O(k)\), first perform the exact occurrence-copy reduction below to achieve degree \(\le3\).

Let **promise-UniqueBIP3-CSP** have binary relations with a **simple bipartite 3-regular** primal graph and common polynomial alphabet, under the promise that the number of satisfying assignments is **0 or 1**. On instances with \(2+\) solutions, the oracle may answer arbitrarily.

**Theorem (quantitative Valiant–Vazirani/Isolation Lemma transfer).** There is a randomized polynomial-time oracle procedure making at most \(\operatorname{poly}(k,q)\) calls, each to an explicit promise-UniqueBIP3-CSP instance with
\[
 \boxed{
 K=O(k+m),\qquad M=3K/2,\qquad
 Q=(kq)^{O(1)}.
 }
\tag{1}
\]
If \(\Gamma\) is UNSAT, **every** oracle query is UNSAT, hence under the promise and correctly rejected; the procedure always rejects. If \(\Gamma\) is SAT, with probability at least \(1/2\) over its chosen random weights at least one oracle query has **exactly one** satisfying assignment, hence a correct oracle accepts and the procedure accepts. Repeating independently amplifies success. (If other queries have \(2+\) solutions, their responses are unconstrained, but an acceptance is harmless because the source is SAT.)

For a randomized promise solver with bounded error, amplify its per-query error before polynomially many calls. Thus a **randomized** \(Q^{o(K/\sqrt{\log K})}\operatorname{poly}(L')\)-time promise solver for all polynomial-domain BIP3 instances yields a **randomized one-sided-error** \(q^{o(k/\sqrt{\log k})}\operatorname{poly}(L)\) solver for the source class, since \(K=O(k)\) and \(\log Q=O(\log q)=O(\log k)\) for \(q=k^{\Theta(1)}\). Importantly, this DOES NOT refute a hypothesis excluding only **deterministic** fast algorithms.

## 2. Isolation Lemma on solution assignments

The ground set is
\[
 \Omega=\{(v,a):v\in V(\Gamma),\,a\in[q]\},
 \quad |\Omega|=N=kq.
\]
Each satisfying assignment \(\sigma\) corresponds uniquely to the \(k\)-element subset
\(S_\sigma=\{(v,\sigma(v)):v\in V\}\). Independently draw each weight
\[
 w_{v,a}\sim\operatorname{Unif}\{1,\ldots,2N\}.
\]
The Mulmuley–Vazirani–Vazirani Isolation Lemma implies that if \(\Gamma\) is SAT, with probability at least \(1-|\Omega|/(2N)=1/2\) there is a **unique** solution minimizing
\[
 W(\sigma)=\sum_v w_{v,\sigma(v)}.
\]
All scores are integers between \(k\) and \(B=2kN=2k^2q\). The total number \(B\) of possible thresholds is polynomial.

Classical source: Mulmuley–U. Vazirani–V. Vazirani, *Matching is as easy as matrix inversion*, Combinatorica 7 (1987), 105–113; an explicit Isolation Lemma statement/proof is available in [Jukna, *Extremal Combinatorics*, isolation chapter](https://web.vu.lt/mif/s.jukna/EC_Book_2nd/isolation.html). This is a linear-parameter, polynomial-domain gadgetization of an **old idea**, not a claim that isolation itself is new.

## 3. Deterministic parsimonious encoding of the exact sum \(W(\sigma)=t\) with O(k) binary constraints

For each variable \(v\) create a score variable \(s_v\in[0,B]\), connected by the binary graph relation
\[
 s_v=w_{v,X_v}.
\]
A balanced binary tree over the \(k\) score variables has \(k-1\) internal nodes. For every internal node \(a\) with child score variables \(s_L,s_R\), create its own score variable \(s_a\in[0,B]\) and one pair-variable
\[
 P_a=(s_L,s_R)\in[0,B]^2.
\]
Enforce by **three binary relations** on the edges \(P_a-s_L\), \(P_a-s_R\), \(P_a-s_a\) that the two coordinates equal the child values and \(s_a=P_a^{(1)}+P_a^{(2)}\) (forbid overflow beyond \(B\), which never occurs on legitimate assignments). Root score is restricted to \(s_{\rm root}=t\), via a unary list or a forced singleton dummy and one binary edge.

For each source assignment, the score leaves, all internal scores, and all pair variables are **uniquely determined**. Conversely any satisfying auxiliary assignment projects to a source assignment of exactly score \(t\). Therefore the number of satisfying assignments is **preserved exactly** for each threshold \(t\), and the additional number of variables and edges is \(O(k)\).

Degrees: each pair variable has degree 3; each score variable has degree at most 2 (one edge to its defining pair-variable and one to its parent pair-variable, or one leaf-weight edge and one parent edge). Original variables have their original incidence degree plus one leaf-weight edge. Split original variable occurrences into a path of equality-connected copies, attaching at most one original incident edge to each and the weight edge to an endpoint, so all variable degrees become \(\le3\), with \(O(k+m)\) new copies and edges and **unique extension**. For initially general sparse \(m=O(k)\), this also resolves arbitrary high variable degrees.

The common alphabet needed to encode *every* typed variable is at most
\[
 Q_0=\max\{q,(B+1)^2\}=(kq)^{O(1)}.
\]
Explicit binary table descriptions have size polynomial in \(k,q\). Unary domain conditions can be absorbed into each incident binary relation; for an isolated special variable, add one forced singleton neighbor and an edge. All typed relations are well-defined on the one common alphabet.

The resulting (possibly nonbipartite, nonregular) binary-CSP primal graph is simple, has \(O(k+m)\) vertices and constraints, degree \(\le3\), and exactly the same number of solutions as the score-\(t\) restriction of the source.

## 4. Parsimonious bipartitization without changing asymptotic parameters

Let the current binary CSP have \(V_0\) variables, \(E_0\) constraints and maximum variable degree \(\le3\). For every old binary constraint \(R_{xy}\), create a **new incidence variable** \(z_{xy}\) with values in the tagged set
\[
 D_{z_{xy}}=\{(a,b)\in D_x\times D_y:(a,b)\in R_{xy}\}.
\]
Replace the original constraint by two binary projection constraints
\[
 x=\pi_1(z_{xy}),\qquad y=\pi_2(z_{xy}).
\]
A source satisfying assignment extends uniquely to each \(z_{xy}\). The new graph is **simple and bipartite**: one partition \(A\) consists of old variables, the other \(B\) of new incidence variables. An old variable keeps its previous degree (at most 3), and each incidence variable has degree 2.

The new common alphabet \(Q_1\) must encode ordered pairs of values from \(Q_0\), so \(Q_1\le (Q_0+1)^2=(kq)^{O(1)}\). There are \(O(k+m)\) variables and constraints.

This trick also works on source graphs with parallel constraints: each gets its own fresh incidence variable, so the resulting bipartite graph is simple.

## 5. Parsimonious degree-3 completion without disturbing bipartiteness

Start from any finite simple bipartite graph \(J=(A\sqcup B,E)\) with maximum degree \(\le3\), each vertex having a specified domain in a common alphabet. The binary constraints from Section 4 may be arbitrary.

**Balancing partition sizes.** Add \(|\,|A|-|B|\,|\) *forced singleton-valued isolated* dummy variables to the smaller side, so the two sides have the same number \(n_0\) of vertices. Every new dummy has a unique allowed value; these currently isolated vertices will be connected in the next step.

**Deficit matching.** Give every vertex \(v\) exactly \(3-\deg_J(v)\) labeled open stubs. Each side now has equal total number
\[
 d_A=3n_0-|E|=d_B.
\]
Pair the stubs on the \(A\)-side arbitrarily with the stubs on the \(B\)-side.

For each paired pair of stubs, introduce a fresh 6-vertex **\(K_{3,3}\) minus one edge** gadget. Its designated opposite-partition port vertices \(a_g\in A_g\) and \(b_g\in B_g\) have degree 2, while its other four vertices have degree 3. Connect:
- the chosen old \(A\)-vertex stub to \(b_g\in B_g\);
- the chosen old \(B\)-vertex stub to \(a_g\in A_g\).

All original vertices and all gadget vertices now have degree **exactly 3**. The graph remains **simple bipartite**, because every new port/gadget is fresh. The number of gadgets is \(d_A=O(|A|+|B|)\), and each adds only 6 vertices and \(8+2=10\) edges. The final graph is therefore a simple bipartite 3-regular graph with \(O(k+m)\) vertices.

**Preservation of solutions:** force every new gadget vertex to a unique dummy value \(\bot\). The eight gadget-internal constraints allow only \((\bot,\bot)\); the two incident stub edges permit \((a,\bot)\) or \((\bot,b)\) for *every* legitimate value \(a\in D_{\text{old }A}\), \(b\in D_{\text{old }B}\), respectively. Each old satisfying assignment therefore has a **unique** extension through every dummy gadget, and no old assignment is excluded. This also forces the originally added balancing dummy vertices (which now have incident edges) to their unique values.

The original domains may be encoded in binary relations on every incident edge (or with explicitly supplied unary domains if that is the model), so no non-binary constraint is introduced. The final common alphabet stays polynomial in \(kq\), even with tagged pairs and the special value \(\bot\).

**Important:** The padding preserves **bipartiteness and regularity**, but NOT expansion or high girth (it introduces small \(K_{3,3}\) subgraphs). Do not use it to claim hardness of a **fixed cubic expander family**; it is intended for the HOM paper's class of all simple bipartite 3-regular source CSP graphs.

## 6. Correct promise-oracle usage and fine-grained consequence

For each threshold \(t\in\{k,\ldots,B\}\), construct the parsimonious cubic-bipartite CSP \(\Gamma_t\) of Sections 3–5.

- If the input \(\Gamma\) is UNSAT, every \(\Gamma_t\) has zero solutions; they are all within the promise and all rejected.
- If \(\Gamma\) is SAT and the Isolation Lemma succeeds, its unique minimum-weight solution has some score \(t_\star\). The corresponding \(\Gamma_{t_\star}\) has **exactly one** solution and is within the promise; a correct promise Unique-CSP oracle accepts. Other score buckets can have multiple solutions and are **outside the promise**, but that does not invalidate acceptance on the source-SAT case, since any YES answer there is harmless.

This is a **one-sided-error randomized Turing reduction** with \(\operatorname{poly}(k,q)\) many oracle queries of size \(K=O(k+m)\), \(Q=(kq)^{O(1)}\). No claim of a randomized many-one reduction with a single query is being made.

**Fine-grained statement:** Suppose for some fixed polynomial-domain growth \(q=k^c\) the source class (e.g. general cubic binary CSP, or the original HOM paper's bipartite cubic source) is conjectured to have **no randomized** \(q^{o(k/\sqrt{\log k})}\operatorname{poly}(L)\) decision algorithm. Then **no uniform randomized** promise-UniqueBIP3-CSP algorithm of time \(Q^{o(K/\sqrt{\log K})}\operatorname{poly}(L')\), valid over the relevant polynomial alphabet sizes, can exist: composing the algorithm and this isolation procedure would refute the source hypothesis.

The quantitative bounds are matched to the \(\sqrt{\log}\) scale of the externally claimed Nguyen CSP upper bound. They hold **without assuming Nguyen's theorem**; the only random ingredient is the classical Isolation Lemma.

**Connection to HOM:** Theorem 4.2 of the user's HOM preprint https://arxiv.org/abs/2607.09377 uses binary CSP on simple bipartite 3-regular primal graphs. This construction preserves that exact graph class in the *oracle instances*, making promise UniqueBIP3-CSP a plausible hardness source for HOM if the new randomized SqrtLog hypothesis is adopted. **Do not assert the existing CSP-to-HOM reduction preserves uniqueness of HOM assignments** without separately checking its parsimonious properties; decision equivalence alone suffices for conditional hardness.

## 7. Research significance and limitations

This **does not** show that the specific random Bernoulli critical-expander ensemble is hard: it only demonstrates that in **worst case** the unique-or-unsatisfiable promise does not make sparse polynomial-alphabet CSP easier under parameter-preserving **randomized oracle reductions**. It therefore defeats the simplistic intuition "only polynomially many near-solutions, so brute force should be easy" as a worst-case principle, but it does not construct an average-case algorithm or average-case lower bound.

The basic Valiant–Vazirani and isolation approaches are decades old. The value of the current note is explicit control of **linear variable/constraint blowup, polynomial alphabet, maximum degree 3, and bipartite 3-regular completion** at the relevant fine-grained scale. A dedicated prior-art audit is necessary before claiming novelty or submitting it as an independent contribution.

**References:** L. Valiant and V. Vazirani, *NP is as easy as detecting unique solutions*, Theor. Comput. Sci. 47 (1986), 85–93, https://doi.org/10.1016/0304-3975(86)90135-0 ; K. Mulmuley, U. Vazirani, V. Vazirani, *Matching is as easy as matrix inversion*, Combinatorica 7 (1987), 105–113, https://doi.org/10.1007/BF02579206 .
