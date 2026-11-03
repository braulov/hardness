# Karger cut counting removes expander/girth from conditional Poisson — and exposes easy low-treewidth examples

**2026-11-03. Status:** **PROVED internal deduction** using Karger's classical cut-counting theorem and the exact moments from notes 35–47. This is a major **scope correction** to [note 47](47_conditional_poisson_after_one_edge_and_endpoint_injectivity.md). Novelty of these precise probabilistic consequences has NOT been verified in prior random-CSP literature. There is **no new computational hardness bound**. In fact, an explicit **easy** graph family satisfies every strong statistical conclusion in this note.

## 1. Setup and Karger's theorem

Let \(G\) be **any simple 3-regular, 3-edge-connected** graph on \(k\) vertices, \(|E|=m=3k/2\). No expansion, growing girth, bipartiteness, or large treewidth is assumed. Draw complete binary-relation tables independently with Bernoulli entry probability
\[
 p=q^{-2/3},\qquad q=\lceil k^c\rceil,\qquad c>9.
\]
All constants are absolute; \(c>9\) is a clean sufficient choice for simultaneous all-edge conclusions, not a tight threshold.

Let \(\lambda(G)\ge3\) be the minimum global cut size. Karger's **cut-counting theorem** states that the number of (unordered) cuts of size at most \(d\) is at most \(k^{2d/\lambda(G)}\) for \(d\ge\lambda(G)\). Therefore, the number of nonempty proper vertex sets \(S\) with \(|\delta(S)|=d\) is at most \(2k^{2d/3}\).

Put
\[
 \Xi_G(q)=\sum_{\varnothing\ne S\subsetneq V}q^{-|\delta(S)|/3}.
\]
If \(q>k^2\), sum by cut size:
\[
 \boxed{
 \Xi_G(q)
 \le2\sum_{d=3}^{m}k^{2d/3}q^{-d/3}
 \le\frac{2(k^2/q)}{1-(k^2/q)^{1/3}}
 =O(k^2/q).
 }
\tag{1}
\]
This **one** estimate replaces the girth/expansion analysis of agreement subsets in notes 35–37 and 47. It also shows why edge connectivity, not necessarily expansion, controls the same probabilistic moment bounds.

**External source:** D. R. Karger, [*Random Sampling in Cut, Flow, and Network Design Problems*](https://people.csail.mit.edu/karger/Papers/thesis.pdf), Section 4.7, Cut Counting Theorem 4.7.6; see also [Karger-style cut-counting summary](https://users.cs.duke.edu/~debmalya/papers/stoc11-sparsification.pdf), Theorem 1.5. Exact statement: for minimum cut \(\lambda\), at most \(k^{2\alpha}\) cuts of size at most \(\alpha\lambda\).

## 2. Poisson number of full solutions, without expansion

Let \(Z\) count satisfying assignments. Every assignment uses \(m\) independently sampled relation entries, so
\[
 \mathbb EZ=q^kp^m=1.
\]
Define Bernoulli indicator \(I_\sigma\) for each labeling \(\sigma\in[q]^k\). Its dependency neighborhood consists of assignments \(\tau\) agreeing with \(\sigma\) at both endpoints of at least one edge. The standard dependency-graph Chen–Stein bound has:
\[
 b_1\le m/q^2,\qquad
 b_2\le\sum_{\varnothing\ne S\subsetneq V}q^{-|S|+(2/3)e_G(S)}
 =\Xi_G(q),
\]
where \(e_G(S)=(3|S|-|\delta(S)|)/2\). (Exclude the diagonal \(\tau=\sigma\) from \(b_2\); it is not included in the distinct-pair term.)

Consequently
\[
 \boxed{
 d_{\rm TV}(\mathcal L(Z),\operatorname{Pois}(1))
 \le O(m/q^2+\Xi_G(q))
 =O(k/q^2+k^2/q)=o(1).
 }
\tag{2}
\]
This holds already for \(q\gg k^2\), much less than the \(q\gg k^9\) required below for uniform endpoint-injectivity and adaptive-query statements.

## 3. Delete any edge: many near-solutions but no duplicate endpoint pair

For each \(e=uv\), put \(F=E\setminus\{e\}\), let \(N_e\) be the number of solutions to the CSP restricted to \(F\), and let \(Y_e\) count ordered pairs of distinct such solutions agreeing at \(u,v\). Direct first-moment counting gives the exact identity from note 47:
\[
 \mathbb E Y_e
 =q^{2/3}
 \sum_{\varnothing\ne T\subseteq V\setminus\{u,v\}}
 (1-q^{-1})^{|T|}q^{-|\delta(T)|/3}.
\]
By (1),
\[
 \boxed{
 \mathbb E Y_e\le q^{2/3}\Xi_G(q)=O(k^2q^{-1/3}).
 }
\tag{3}
\]
Union-bounding over all \(m=O(k)\) edges:
\[
 \Pr[\exists e:Y_e>0]
 \le O(k^3q^{-1/3})=o(1)\quad\text{if }c>9.
\tag{4}
\]
Therefore with high probability **every** \(\Gamma_{-e}\) has **injective** solution projection to its two missing-edge endpoints, for every \(e\).

For arbitrary proper edge subset \(F\), the earlier exact second moment formula yields
\[
 \frac{\operatorname{Var}(Z_F)}{(\mathbb EZ_F)^2}
 \le q^{-2/3}+\Xi_G(q)=:\eta_k
 =O(q^{-2/3}+k^2/q).
\tag{5}
\]
Indeed, the exact-agreement term \(S=V\) is \(q^{-k+(2/3)|F|}\le q^{-2/3}\), the \(S=\varnothing\) term is at most one, and all proper nonempty agreement-set terms are bounded by \(\Xi_G(q)\).

For \(F=E\setminus\{e\}\),
\(\mathbb EN_e=q^{2/3}\). Since \(m\eta_k\to0\), Chebyshev plus union bound proves
\[
 \boxed{\max_{e\in E}|N_e/q^{2/3}-1|=o_{\mathsf P}(1).}
\tag{6}
\]

Conditional on all relations except \(R_e\), the full solution count is
\(Z=\sum_{a,b}M_e(a,b)A_e(a,b)\), where the \(A_e(a,b)\)'s are independent Bernoulli-\(p\) bits and the endpoint multiplicities \(M_e\) are zero or one on the injectivity event. Therefore
\[
 \boxed{
 Z\mid R_{-e}\ \stackrel{\rm law}{=}\operatorname{Bin}(N_e,p)
 \ \xrightarrow{\rm TV}\operatorname{Pois}(1)
 \quad\text{uniformly over all }e\text{ on a high-probability event}.
 }
\tag{7}
\]

## 4. Almost-all SAT-bit Hoeffding energy in the **full edge-table** interaction

Let \(U=\mathbf1[Z=0]\) be the UNSAT indicator. As in note 47, define its orthogonal Hoeffding/ANOVA decomposition relative to the \(m\) **whole edge-relation tables**:
\[
 U=\alpha_k+\sum_{\varnothing\ne F\subseteq E}U_F,\qquad
 \alpha_k=\mathbb EU\to e^{-1}.
\]
For a fixed missing edge, the expected conditional TV error from a Poisson(1) law is at most
\[
 \delta_k:=\max_e\mathbb E_{R_{-e}}
       d_{\rm TV}\bigl(\mathcal L(Z\mid R_{-e}),\operatorname{Pois}(1)\bigr)
 \le\max_e\mathbb EY_e+p+\sqrt{\eta_k}
 =O(k^2q^{-1/3}+kq^{-1/2}+q^{-1/3}).
\tag{8}
\]
For \(c>9\), \(m\delta_k=o(1)\). Consequently the ANOVA projection argument from note 47 yields
\[
 \boxed{
 \sum_{\varnothing\ne F\subsetneq E}\|U_F\|_2^2=o(1),\qquad
 \|U_E\|_2^2\to e^{-1}(1-e^{-1}).
 }
\tag{9}
\]
Thus *the Boolean UNSAT bit itself* has essentially all nonconstant \(L^2\) energy in the component involving **every** constraint table, **even without graph expansion**.

Replacing any one full relation table by an independent copy changes the SAT/UNSAT answer with probability
\[
 \boxed{
 \Pr[U\ne U^{(e)}]\to2e^{-1}(1-e^{-1})\approx0.46509
 }
\tag{10}
\]
uniformly over edges, again with no expansion.

For an algorithm adaptively requesting entire edge tables but required to stop with at least one table unread, the first-unqueried-edge partition from note 47 gives
\[
 d_{\rm TV}\bigl(
  (\mathrm{transcript},U),\,
  \mathrm{transcript}\otimes\operatorname{Bernoulli}(e^{-1})
 \bigr)
 \le m\delta_k=o(1).
\]
Therefore no such algorithm can predict SAT/UNSAT with probability greater than \(1-e^{-1}+o(1)\). **This is a restricted input-access bound, not runtime hardness.**

## 5. Critical negative control: cubic prisms have constant treewidth and all the above statistical properties

Let \(G_s=C_s\square K_2\), the circular ladder / *prism graph* on \(k=2s\) vertices, \(s\ge4\).

- It is simple, connected, **3-regular** and **3-edge-connected**. This follows from the Cartesian-product edge connectivity formula, or the fact that it is connected and vertex-transitive of degree 3.
- It has **girth 4**, not logarithmic girth, and **treewidth at most 5**. Explicit path decomposition: write columns as \((a_i,b_i)\), for \(i=0,\dots,s-1\); take bags
\[
 B_i=\{a_0,b_0,a_i,b_i,a_{i+1},b_{i+1}\},
 \qquad 1\le i\le s-2.
\]
Every cycle-edge and rung is in some bag, and each vertex's bags form an interval. Thus \(\operatorname{tw}(G_s)\le5\).
- Arbitrary **exact #CSP** on this graph with alphabet \(q\) is polynomial-time solvable by ordinary dynamic programming over these bags, e.g.
\[
 \boxed{O(kq^6)\text{ arithmetic operations}}
\]
is a conservative upper bound. No randomness, 2026 tensor claims, or conjecture is needed.

Nevertheless, since \(G_s\) is 3-edge-connected, for \(q=k^c,c>9\), the random Bernoulli relation ensemble on \(G_s\) satisfies **all** of (2), (4), (6), (7), (9), and (10): conditional-Poisson last-edge secrecy, full-edge ANOVA spectrum of the SAT bit, and near-maximal influence of resampling every edge.

**This is a decisive sanity check:** neither near-full-edge Fourier degree, inability to predict satisfiability without the final complete table, nor the conditioned Poisson law is by itself evidence of computational hardness. We have an explicit **polynomial-time solvable family with exactly those phenomena**. They measure *statistical globality*, not algorithmic complexity.

For our replacement-ETH / HOM hardness search, the **expander condition remains crucial** to rule out standard bounded-treewidth dynamic programming. The statistical properties above are attractive mathematical curiosities and restricted-model benchmarks, but not a validation of SqrtLog-SPACH or an average-case hardness postulate. Do **not** cite them as affirmative computational-hardness evidence without a separate algorithmic reduction or genuine complexity lower bound.

Note that the **local tree-lookahead gap** in Section 5 of note 47 genuinely *does* use large girth and is **not** claimed for the prism family; the extension dropping girth applies only to the Poisson/endpoint/Fourier statements.

**Finite verification:** [experiments/48_prism_cutcount_and_pathwidth_sanity.py](../experiments/48_prism_cutcount_and_pathwidth_sanity.py) explicitly enumerates all cuts for small cubic prisms, checks 3-edge-connectivity, verifies the Karger bound on \(\Xi_G(q)\), and checks the stated six-vertex bags and interval property; only Python's standard library is used. [experiments/47_endpoint_collision_formula_sanity.py](../experiments/47_endpoint_collision_formula_sanity.py) independently compares the exact collision count as a cut sum and as a direct sum over ordered labeling pairs on \(K_{3,3}\). These are **finite sanity tests**, not proofs of the asymptotic theorem.

## 6. Research redirection

- **Algorithmic:** the polynomially many solutions after deleting one edge could be searched for via output-sensitive enumeration, but the cubic-prism example shows such enumeration is easy on low-treewidth graphs. The challenge is exploiting random tables to handle **linear-treewidth expanders**.
- **Hardness:** do not infer hardness from high Fourier degree / last-edge information secrecy. Seek model-restricted algorithm lower bounds that *actually distinguish* large-treewidth expanders from easy bounded-treewidth 3-edge-connected graphs, or build a surviving worst-case hardness reduction.
- **Source quality:** Karger's cut-counting theorem is published classical mathematics. The applications to this exact random-CSP model are internal proof deductions; novelty and general theorem dependencies should be audited independently before any research claim.

**References:** Karger cut-counting theorem (linked in Section 1); Chen–Stein Poisson approximation as in note 35; Hoeffding/ANOVA product-space decomposition as in note 47.
