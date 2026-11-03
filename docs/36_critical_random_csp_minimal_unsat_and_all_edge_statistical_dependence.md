# Critical expander CSP: minimal UNSAT, irredundancy, and all-edge statistical dependence

**2026-11-02. Status:** elementary second-moment and likelihood-ratio theorems **PROVED BELOW**, assuming the specified deterministic expander family exists (standard). This is **not** a \(q^{\Omega(k/\sqrt{\log k})}\) computational lower bound; novelty relative to random CSP literature unverified. Extends [the Poisson and arc-consistency note](35_critical_expander_csp_poisson_and_arc_consistency.md).

## Setup and prior Poisson input

Let \(F_k\) be any fixed simple 3-regular graph with \(k\) vertices, \(m=3k/2\), and uniform edge expansion \(\gamma>0\):
\[
 |\delta(S)|\ge \gamma\min(|S|,k-|S|).
\]
For each edge \(e\), independently include every ordered pair in the binary CSP relation \(R_e\subseteq[q]^2\) with probability \(p=q^{-2/3}\), where \(q=\lceil k^c\rceil\). The probability space is **the full collection of explicit relation table bits**. There are \(q^k\) potential assignments; let \(Z\) count those satisfying all \(m\) edges.

From [note 35](35_critical_expander_csp_poisson_and_arc_consistency.md):
\[
 \mathbb EZ=q^kp^m=1,\qquad
 d_{\mathrm{TV}}(Z,\operatorname{Pois}(1))=o(1)
\]
when \(c>3/\gamma\). Also arc consistency removes nothing with high probability.

For an edge subset \(F\subseteq E(F_k)\), let \(Z_F\) count assignments satisfying **only** edges in \(F\). Then
\[
 \mu_F:=\mathbb EZ_F=q^k p^{|F|}.
\]

## 1. Uniform normalized second-moment bound for every proper subinstance

Write \(S=\{v:\sigma(v)=\tau(v)\}\) for the agreement set of two assignments, and \(e_F(S)=|F\cap E(F_k[S])|\). The two witness indicators share exactly \(e_F(S)\) Bernoulli table entries, hence
\[
  \frac{\mathbb E Z_F^2}{\mu_F^2}
  =\sum_{S\subseteq V}
       q^{-|S|}(1-q^{-1})^{k-|S|}
       q^{(2/3)e_F(S)}.
\tag{1}
\]

Since \(e_F(S)\le e_{E(F_k)}(S)\), expansion and cubic regularity imply, for \(S\notin\{\varnothing,V\}\),
\[
 q^{-|S|+(2/3)e_F(S)}
 \le q^{-(\gamma/3)\min(|S|,k-|S|)}.
\tag{2}
\]
For the diagonal \(S=V\), if \(F\subsetneq E(F_k)\), then \(|F|\le m-1\) and
\[
 q^{-k+(2/3)|F|}\le q^{-2/3}.
\]
The empty-set contribution is \((1-1/q)^k\le1\). Summing the proper nonempty \(S\)'s by their size or complement gives the **uniform** estimate
\[
 \boxed{
 \frac{\operatorname{Var}(Z_F)}{\mu_F^2}
 \le \eta_k:=
 q^{-2/3}
 +2\bigl((1+q^{-\gamma/3})^k-1\bigr)
 \qquad\forall F\subsetneq E(F_k).
 }
\tag{3}
\]
In particular \(\eta_k=O(q^{-2/3}+kq^{-\gamma/3})=o(1)\) whenever \(c>3/\gamma\). This bound is independent of the particular missing edge(s).

## 2. All original constraints are logically essential

For any single edge \(e\), \(Z_{-e}=Z_{E\setminus\{e\}}\) has
\[
 \mathbb EZ_{-e}=q^k p^{m-1}=q^{2/3}.
\]
By (3) and Chebyshev,
\[
 \Pr[Z_{-e}<q^{2/3}/2]\le4\eta_k.
\]
Union bound over all \(m=3k/2\) edges yields
\[
 \Pr[\exists e: Z_{-e}<q^{2/3}/2]
 \le O(kq^{-2/3}+k^2q^{-\gamma/3}).
\]
For \(q=k^c,\ c>6/\gamma\), the RHS tends to zero (as \(\gamma\le3\), this also ensures \(c>3/2\)). Separately \(\mathbb EZ=1\) implies by Markov
\[
 \Pr[Z\ge q^{2/3}/2]\le2q^{-2/3}=o(1).
\]
Therefore, with probability \(1-o(1)\), **every edge satisfies**
\[
 \boxed{Z_{-e}\ge q^{2/3}/2>Z.}
\tag{4}
\]
For each edge \(e\), an assignment that satisfies all other constraints but not \(e\) must exist. Therefore **no original edge constraint is logically implied by the others** (irredundancy) regardless of whether the full CSP is SAT.

Combining (4), arc consistency, and the Poisson theorem:
\[
 \boxed{\Pr[\text{the CSP is edge-minimally UNSAT and arc-consistent}]
 \longrightarrow e^{-1}.}
\tag{5}
\]
Here *edge-minimally UNSAT* means that deleting **any one original binary relation** leaves a satisfiable instance; by monotonicity, every proper constraint subfamily is SAT. This theorem rules out exact SAT-preserving compression by mere deletion of original relations on these inputs; it does **not** rule out substitutions, auxiliary variables, nonlinear encodings, randomized algorithms, or semantic UNSAT certificates not based on proper subinstances.

## 3. Planted vs null: any proper collection of complete edge tables is asymptotically uninformative

Define the **null law** \(\mathsf P\) as above. Define the **planted law** \(\mathsf Q\) by sampling a uniformly random \(\sigma\in[q]^k\), then independently generating all relation-table entries from the null Bernoulli law **conditioned on \(\sigma\) satisfying every edge** (equivalently, force precisely one pair per edge into the relation and sample all other bits independently).

For each fixed \(F\subseteq E\), the marginal \(\mathsf Q_F\) on all table bits of the edges in \(F\) has the exact likelihood ratio relative to the corresponding null marginal \(\mathsf P_F\):
\[
 \boxed{
 \frac{d\mathsf Q_F}{d\mathsf P_F}(R_F)
 =\frac{Z_F(R_F)}{\mu_F}.
 }
\tag{6}
\]
Proof: for fixed \(\sigma\), conditioning on its \(|F|\) required Bernoulli events multiplies the null probability density by
\(\prod_{e\in F}\mathbf1[(\sigma(u),\sigma(v))\in R_e]/p^{|F|}\). Averaging over \(q^k\) uniformly sampled \(\sigma\)'s gives \(q^{-k}p^{-|F|}Z_F=Z_F/\mu_F\).

By Cauchy–Schwarz and (3),
\[
\begin{aligned}
 d_{\mathrm{TV}}(\mathsf Q_F,\mathsf P_F)
 &=\tfrac12\mathbb E_{\mathsf P_F}
     \left|\frac{Z_F}{\mu_F}-1\right|\\
 &\le\tfrac12\sqrt{\frac{\operatorname{Var}(Z_F)}{\mu_F^2}}
 \le \frac12\sqrt{\eta_k}=o(1)
 \qquad\textbf{uniformly for every proper }F\subsetneq E.
\end{aligned}
\tag{7}
\]
Thus even an **unbounded** observer seeing all but one complete relation table has vanishing distinguishing advantage between planted and null, provided it commits to which complete table is missing (or more generally to a predetermined proper set \(F\)).

For the full instance \(F=E\), \(\mu_E=1\), so the likelihood ratio is \(Z\). Because \(Z\Rightarrow \operatorname{Pois}(1)\) and the second moments are uniformly bounded by note 35, the absolute-value function is uniformly integrable, giving
\[
 \boxed{
 d_{\mathrm{TV}}(\mathsf Q,\mathsf P)
 =\tfrac12\mathbb E_{\mathsf P}|Z-1|
 \longrightarrow \tfrac12\mathbb E|\operatorname{Pois}(1)-1|
 =e^{-1}.
 }
\tag{8}
\]
The planted solution count has the size-biased distribution \(\mathsf Q(Z=z)=z\,\mathsf P(Z=z)\) (here \(\mathbb EZ=1\)); hence, in the limit, \(Z_{\mathrm{planted}}\Rightarrow1+\operatorname{Pois}(1)\).

This is an **all-edges statistical phenomenon**: the full relation family has constant planted-vs-null distinction, while *every* proper fixed subfamily loses it asymptotically. It is not a lower bound for algorithms that can inspect partial entries from every edge table, and distinguishing planted vs null is not equivalent to solving individual CSP instances.

### Optional adaptive edge-table query refinement

Suppose an algorithm may adaptively request **whole edge tables**, but must stop before requesting all \(m\) tables. Each event that its final transcript omits a particular edge \(e\) and leads to a given output is measurable from the other \(m-1\) tables. Partitioning by the omitted edge and applying (7) yields a crude total variation upper bound \(m\sqrt{\eta_k}/2\), even for unlimited computation and randomized querying. This tends to zero if \(c>9/\gamma\), since
\[
 m\sqrt{\eta_k}
 = O(kq^{-1/3}+k^{3/2}q^{-\gamma/6})=o(1).
\]
The restriction to **whole-edge-table** queries is essential: an algorithm reading a few entries of *every* edge is outside this bound.

## Further sharpening: all-edge Fourier signal (see note 37)

The conditional-expectation indistinguishability estimates above can be strengthened to an exact \(p\)-biased Fourier statement. [Note 37](37_critical_expander_low_degree_fourier_and_path_saturation.md) computes the full likelihood-ratio spectrum and proves \(\|L^{\le m-1}-1\|_2=o(1)\) for \(m=3k/2\) under \(c>\max(3/2,3/\gamma)\). Thus *any* normalized polynomial statistic of the full explicit input of degree \(<m\) has vanishing difference in planted-vs-null means. The technique is the standard low-degree likelihood-ratio method and does not establish computational hardness. The same note shows path-composition saturation at length four and a simple \(o(q^2)\) individual-bit query lower bound.

## November 3 strengthening: conditionally Poisson after any one missing relation

[Note 47](47_conditional_poisson_after_one_edge_and_endpoint_injectivity.md) upgrades the planted-vs-null indistinguishability in Section 3 to a direct statement about **actual SAT/UNSAT**. Under fixed cubic expansion and logarithmic girth and sufficiently large polynomial alphabet, deleting any edge leaves \((1+o(1))q^{2/3}\) solutions with **distinct endpoint-label pairs**. Conditional on all other \(m-1\) relation tables, reinstating the edge yields an **exact** \(\operatorname{Binomial}(N_e,q^{-2/3})\) full solution count, asymptotically \(\mathrm{Poisson}(1)\). The SAT/UNSAT bit has essentially all its edge-block Hoeffding variance in the full-\(m\)-table component. This yields an order-independent no-prediction theorem for algorithms omitting any complete relation table, **not** a full-input time lower bound. A direct finite identity check is in [experiments/47](../experiments/47_endpoint_collision_formula_sanity.py).

## 4. What this means for the hardness search

- A fixed-expander **random-source distribution** has nontrivial SAT/UNSAT probabilities, but local supports, all proper CSP subinstances, and any proper collection of whole relation tables reveal little global consistency information.
- This provides a stringent **stress test** for new algorithms that only sparsify by deleting original checks, rely on local propagation, or infer planted satisfiability from incomplete constraint sets.
- It does **not** prove the proposed worst-case or average-case SqrtLog-SPACH lower bound; the general Nguyen theorem, if valid, already supplies \(q^{O(k/\sqrt{\log k})}\) for this distribution. We need either a new algorithm improving that exponent, a separate hardness reduction, or a genuinely restricted-model lower bound with precise access rules.
- Novelty of the probability-theoretic construction versus existing random-CSP literature must be checked before a publication claim.

**References:**
- [Poisson and arc-consistency note](35_critical_expander_csp_poisson_and_arc_consistency.md)
- Arratia–Goldstein–Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method* (standard dependency-graph bound), https://doi.org/10.1214/aop/1176991229
- [New tensor/HOM and hardness program](34_tensor_algorithms_for_hom_subiso_and_surviving_hardness.md).
