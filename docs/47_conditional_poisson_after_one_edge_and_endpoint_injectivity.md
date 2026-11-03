# Critical random expander CSP: endpoint-injective near-solutions and a conditional Poisson last edge

**2026-11-03. Status:** **PROVED internal derivation** from exact collision counting, girth/expansion, concentration, and standard Poisson approximation. Not independently peer-reviewed or checked for publication novelty. No fine-grained computational hardness lower bound is established. The order-independent *complete-edge-table* query lower bound is **information-theoretic and model-restricted**, not a lower bound for full-input algorithms.

Related prior checkpoints: [35 — Poisson and arc consistency](35_critical_expander_csp_poisson_and_arc_consistency.md), [36 — minimal UNSAT and missing-edge planted/null indistinguishability](36_critical_random_csp_minimal_unsat_and_all_edge_statistical_dependence.md), [37 — Fourier spectrum](37_critical_expander_low_degree_fourier_and_path_saturation.md), [44 — bad-order overlapping tree lookahead](44_overlapping_tree_lookahead_actual_search_lower_bound_on_spaced_prefix.md).

## 1. Ensemble and the strengthened theorem

Let \(G=(V,E)\) be a fixed **simple, 3-regular, \(\gamma\)-edge-expander** on \(k\) vertices with girth
\[
 g(G)\ge a\ln k
\]
for fixed \(a,\gamma>0\). Hence \(m=|E|=3k/2\). For each \(e\in E\), draw its complete relation table \(A_e\in\{0,1\}^{[q]^2}\) with independent Bernoulli-\(p\) entries, where
\[
 q=\lceil k^c\rceil,\qquad p=q^{-2/3}.
\]
Assume \(c>\max\{6,9/\gamma\}\), a generous *sufficient*, not sharp, condition. (For results about one fixed edge only, \(c>\max\{3,3/\gamma\}\) suffices.)

Let \(\Gamma\) be the full CSP, and \(\Gamma_{-e}\) the CSP obtained by deleting edge constraint \(e=uv\). Let \(N_e\) be the number of solutions to \(\Gamma_{-e}\), \(Z\) the number of full solutions, and
\[
 M_e(a,b)=|\{\sigma\in\operatorname{Sol}(\Gamma_{-e}):(\sigma(u),\sigma(v))=(a,b)\}|.
\]

**Theorem A (uniform near-solution rigidity):** With probability \(1-o(1)\) over the independent relation tables, **simultaneously for every edge \(e=uv\)**,
1. \(N_e=(1+o(1))q^{2/3}\);
2. \(M_e(a,b)\in\{0,1\}\) for every \(a,b\in[q]\), i.e. the endpoint projection of \(\operatorname{Sol}(\Gamma_{-e})\) is **injective**;
3. The conditional distribution of the full solution count given all tables except \(R_e\) is
\[
 \boxed{Z\mid(A_f)_{f\ne e}\ \stackrel{\rm law}{=}\operatorname{Binomial}(N_e,p)}
\tag{1}
\]
and is at total-variation distance \(o(1)\) from \(\operatorname{Poisson}(1)\).

The event in (3) is a statement about the *conditional law after seeing the other \(m-1\) tables*. We are not claiming \(Z\) is deterministic given those tables. Condition (1) is exact when (2) holds. The unconditional \(Z\Rightarrow\operatorname{Poisson}(1)\) was previously proved in note 35; the **conditional** version is stronger.

## 2. Exact endpoint-collision expectation

For \(e=uv\), let
\[
 Y_e=\sum_{a,b}M_e(a,b)(M_e(a,b)-1)
\]
count *ordered pairs of distinct* \(\Gamma_{-e}\)-solutions agreeing at both endpoints \(u,v\). We show \(\mathbb E Y_e=o(1/k)\) under Theorem A's parameters.

For two assignments \(\sigma\ne\tau\) which agree at \(u,v\), let
\(T=\{w\in V:\sigma(w)\ne\tau(w)\}\), a nonempty subset of \(V\setminus\{u,v\}\).
The total number of ordered pairs with exact disagreement set \(T\) is
\(q^k(q-1)^{|T|}\).

Write \(d_G(T)=|\{f\in E:f\cap T\ne\varnothing\}|\). Since \(e\cap T=\varnothing\), these are also precisely the edges of \(\Gamma_{-e}\) whose required relation-table entries are *different* for \(\sigma,\tau\). Their simultaneous feasibility probability in \(\Gamma_{-e}\) is
\[
 p^{(m-1)+d_G(T)}.
\]
For cubic \(G\),
\[
 d_G(T)=\frac{3|T|+|\delta(T)|}{2}.
\]
Using \(q^k p^{m-1}=q^{2/3}\), we obtain the **exact identity**
\[
 \boxed{
 \mathbb E Y_e
 =q^{2/3}\!\!
 \sum_{\varnothing\ne T\subseteq V\setminus\{u,v\}}
 (1-q^{-1})^{|T|}\,
 q^{-|\delta(T)|/3}.
 }
\tag{2}
\]

This formula is also a useful finite-instance sanity check. For \(G=K_{3,3}\) (girth 4, not in the asymptotic high-girth theorem) and any edge \(e\), direct subset enumeration yields approximately
\(\mathbb E Y_e=1.122747\) at \(q=10^2\),
\(0.196824\) at \(q=10^4\), and
\(0.040504\) at \(q=10^6\).
The asymptotic proof below uses growing girth, not this example.

### Bounding the sum

Split \(T\) by whether \(t=|T|\) and \(s=k-t\) are smaller than \(g=g(G)\).

- **Small \(T\)**, \(1\le t<g\): \(G[T]\) is a forest; cubic degree-counting gives
\(\delta(T)=t+2\,\operatorname{cc}(G[T])\ge t+2\).
The summand in (2), including its \(q^{2/3}\) prefactor, is at most \(q^{-t/3}\). Summing over all such \(T\) gives
\[
 (1+q^{-1/3})^k-1
 =O(kq^{-1/3}).
\]
- **Small complement**, \(2\le s<g\): since \(u,v\notin T\), the complement \(S=V\setminus T\) contains both endpoints. Its induced subgraph is a forest, and \(\delta(T)=\delta(S)\ge s+2\). Summing over complements containing \(u,v\) yields at most
\[
 q^{-2/3}(1+q^{-1/3})^{k-2}
 =O(q^{-2/3}).
\]
- **Both sides at least \(g\)**: expansion yields
\(\delta(T)\ge\gamma\min(t,k-t)\).
Set \(\rho=kq^{-\gamma/3}\to0\). Then the total contribution is bounded by
\[
 2q^{2/3}\sum_{j\ge g}\binom{k}{j}q^{-\gamma j/3}
 \le 2q^{2/3}e^{\rho}\frac{\rho^g}{g!}
 =k^{-\omega(1)}
\]
because \(g\ge a\ln k\) and \(c>3/\gamma\).

Thus, uniformly over edges \(e\),
\[
 \boxed{
 \mathbb E Y_e
 =O(kq^{-1/3}+q^{-2/3})+k^{-\omega(1)}.
 }
\tag{3}
\]
Under \(c>6\), union-bounding the probability \(Y_e>0\) over all \(m=O(k)\) edges gives
\[
 \Pr[\exists e:Y_e>0]\le m\max_e\mathbb E Y_e=o(1).
\tag{4}
\]
This proves the simultaneous endpoint-injectivity statement.

## 3. All \(N_e\) concentrate simultaneously

For any proper edge subset \(F\subsetneq E\), note 36 established
\[
 \frac{\operatorname{Var}(Z_F)}{(\mathbb EZ_F)^2}
 \le\eta_k:=
 q^{-2/3}+2\bigl((1+q^{-\gamma/3})^k-1\bigr).
\tag{5}
\]
For \(F=E\setminus\{e\}\), \(\mathbb EN_e=q^{2/3}\). Under
\(c>\max\{6,9/\gamma\}\), \(m\eta_k\to0\). Take
\(\epsilon_k=(m\eta_k)^{1/4}\to0\).
Chebyshev and a union bound imply
\[
 \Pr\left[
 \max_{e\in E}|N_e/q^{2/3}-1|>\epsilon_k
 \right]\le m\eta_k/\epsilon_k^2
 =\sqrt{m\eta_k}=o(1).
\tag{6}
\]
Combining (4) and (6) proves assertions (1) and (2) of Theorem A.

Given all \(m-1\) tables \((A_f)_{f\ne e}\), the full solution count is
\[
 Z=\sum_{a,b\in[q]}M_e(a,b)A_e(a,b).
\tag{7}
\]
The remaining table \(A_e\) has independent Bernoulli-\(p\) entries. When each \(M_e(a,b)\in\{0,1\}\), this is exactly \(\operatorname{Binomial}(N_e,p)\). Since \(N_ep=1+o(1)\), the usual binomial-to-Poisson bound gives
\[
 d_{\rm TV}(\mathcal L(Z\mid(A_f)_{f\ne e}),\operatorname{Pois}(1))
 \le N_ep^2+|N_ep-1|
 =o(1)
\tag{8}
\]
uniformly on the high-probability good event. The same argument shows the conditional probability of UNSAT is \(e^{-1}+o(1)\).

A useful *expected* TV bound, avoiding any separate uniform-event selection, is
\[
 \boxed{
 \mathbb E_{A_{-e}}
 d_{\rm TV}(\mathcal L(Z\mid A_{-e}),\operatorname{Pois}(1))
 \le \mathbb E Y_e+p+\sqrt{\eta_k}.
 }
\tag{9}
\]
Indeed, use a unit bound on the collision event, and (8) plus Cauchy–Schwarz on its complement.

## 4. Adaptive whole-edge-table access: no SAT advantage until the final table

Consider an arbitrarily powerful randomized algorithm which may adaptively request **complete edge-relation tables**, and is required on every execution to halt without reading at least one of the \(m\) complete tables. Its transcript includes its internal random coins, queries, responses, and output. Crucially, it **may not** read even a partial entry from an omitted table by another interface.

Let \(\mathsf U=\mathbf1[Z=0]\). From (9), for a fixed omitted \(e\),
\[
 \mathbb E_{A_{-e}}\bigl|
 \Pr[\mathsf U=1\mid A_{-e}]-e^{-1}\bigr|
 \le\mathbb E Y_e+p+\sqrt{\eta_k}.
\tag{10}
\]

For an adaptive transcript event \(B\), split it into events \(B_e\) according to the **first edge \(e\) not queried**. For each fixed \(e\), the event \(B_e\) is measurable using all tables **except \(A_e\)**: simulate the algorithm with those other complete tables and stop if it attempts to query \(e\); whether it halts without querying \(e\) and returns the designated transcript event can be determined without \(A_e\). (Any internal random coins are independent of the CSP input.) Therefore
\[
 |\Pr(B\cap\{\mathsf U=1\})-e^{-1}\Pr(B)|
 \le m\left(\max_e\mathbb EY_e+p+\sqrt{\eta_k}\right).
\tag{11}
\]
By (3), (5), and \(c>\max\{6,9/\gamma\}\), the RHS is \(o(1)\), uniformly over transcript events \(B\). Equivalently,
\[
 \boxed{
 d_{\rm TV}\bigl(
  \mathcal L(\text{transcript},\mathsf U),\,
  \mathcal L(\text{transcript})\otimes\operatorname{Bernoulli}(e^{-1})
 \bigr)=o(1).
 }
\tag{12}
\]

**Corollary:** any such algorithm's SAT/UNSAT prediction succeeds with probability at most
\[
 \boxed{1-e^{-1}+o(1)\approx0.63212+o(1)}
\tag{13}
\]
on this random input distribution, no matter how much computation it performs between whole-table queries. It cannot beat the uninformed strategy "always predict SAT" by a nonvanishing advantage.

**Scope:** Theorem A and the adaptive-table corollary are entirely **information-theoretic**, and reading all \(m\) tables is only \(O(kq^2)\) input access, already polynomial. They **do not** imply a time lower bound for a real CSP solver with the full explicit input, nor for algorithms querying a few individual entries of every table. This is an order-independent strengthening of the previous *planted/null* missing-table indistinguishability in note 36, now directly for the SAT bit and entire solution count.

## 5. The local-to-global gap is unconditional and particularly clean after deleting one edge

For each \(e=uv\), consider \(\Gamma_{-e}\) with **both \(u,v\) fixed** to any prescribed labels \((a,b)\). Let \(r\le g(G)-3\), and consider any connected free-variable set \(U\subseteq V\setminus\{u,v\}\) with \(|U|\le r\).

1. \(G[U]\) is a tree, because \(|U|<g(G)\).
2. **At most one** edge connects \(U\) to \(\{u,v\}\). If two such boundary edges hit the same endpoint, the unique path in \(U\) connecting their free endpoints creates a cycle of length at most \(r+1\). If they hit different endpoints, including \(e=uv\) closes a cycle of length at most \(r+2\). Both contradict \(g(G)>r+2\). The case of both edges incident to the same free endpoint creates a triangle, also excluded.

Under the iid \(p=q^{-2/3}\) model, with high probability **every** row and column of **every** edge table has at least one allowed pair, because
\[
 \Pr[\text{some missing row/column}]
 \le2mq(1-p)^q
 \le2mq\exp(-qp)
 =2mq\exp(-q^{1/3})=o(1).
\tag{14}
\]
When this holds, every connected tree \(U\) with at most one assigned-boundary edge has a local extension for **every** fixed \((a,b)\): choose a compatible root value at its one boundary edge (if any), then propagate root-to-leaf along the tree, choosing a compatible child value on every edge.

Therefore, **simultaneously for every edge \(e=uv\), every pair \((a,b)\in[q]^2\), and every such \(U\)**, the \(\Gamma_{-e}\) tree-group extension test succeeds! This is a *deterministic* consequence of girth and row/column-totality and requires no second moment or union bound over local tests.

Yet by Theorem A, the **true global endpoint projection**
\[
 \{(a,b):\exists\text{ full solution of }\Gamma_{-e}
   \text{ extending }u=a,v=b\}
\]
contains only \((1+o(1))q^{2/3}\) pairs out of \(q^2\): a fraction \(q^{-4/3+o(1)}\). If we reinstate edge \(e\), its random relation has \((1+o(1))q^{4/3}\) allowed pairs, **every one** of which passes the same local free-tree tests after assigning \(u,v\), but only \(Z=O_{\mathsf P}(1)\) of those pairs extend globally (unconditional \(Z\Rightarrow\mathrm{Pois}(1)\)). This gives a vivid *local-vs-global projection gap*, not a lower bound on all global CSP algorithms or optimal-order DFS.

## 5a. Almost all Fourier–Hoeffding variance of the **SAT bit** is at full edge-table degree

The previous Fourier result in [note 37](37_critical_expander_low_degree_fourier_and_path_saturation.md) concerned the *likelihood ratio \(Z\)* in the **individual table-bit** biased Fourier basis. The conditional Poisson theorem above lets us make a distinct and stronger statement about the **Boolean indicator \(U=\mathbf1[Z=0]\)** itself, in the **block** product space whose \(m\) independent coordinates are entire edge-relation tables \(A_e\).

Let \(\alpha_k=\mathbb E U\to\alpha=e^{-1}\), and write the standard orthogonal Hoeffding/ANOVA decomposition on the product of edge-table blocks:
\[
 U=\alpha_k+\sum_{\varnothing\ne F\subseteq E} U_F,
\]
where the \(U_F\)'s are pairwise \(L^2(\mathsf P_0)\)-orthogonal, each depends only on edge tables \(A_F\), and is *completely degenerate* in every coordinate in \(F\). Let \(U_E\) denote the top-order (all-\(m\)-edge) component.

**Theorem B (near-full-edge resilience).** Under the same hypotheses and sufficient bound \(c>\max\{6,9/\gamma\}\),
\[
 \boxed{
 \sum_{\varnothing\ne F\subsetneq E}\|U_F\|_2^2=o(1),
 \qquad
 \|U_E\|_2^2\longrightarrow e^{-1}(1-e^{-1}).
 }
\tag{15}
\]
Equivalently, the centered SAT bit is \(o(1)\) close in \(L^2\) to a function whose edge-block Hoeffding support is *entirely on all \(m=3k/2\) edge tables*:
\[
 \boxed{\|U-\alpha_k-U_E\|_2=o(1).}
\tag{16}
\]

**Proof.** For each edge \(e\), put \(g_e(A_{-e})=\mathbb E[U\mid A_{-e}]\).
By (9), the fact that \(\alpha_k=\mathbb E g_e\), and boundedness \(0\le g_e\le1\),
\[
 \begin{aligned}
 \|g_e-\alpha_k\|_2^2
 &\le \mathbb E|g_e-\alpha_k|\\
 &\le2\left(\mathbb E Y_e+p+\sqrt{\eta_k}\right)
 =:2\delta_k.
 \end{aligned}
\]
Equations (3), (5) and \(c>\max\{6,9/\gamma\}\) imply \(m\delta_k=o(1)\).
But, by orthogonal projection and the ANOVA decomposition,
\[
 g_e-\alpha_k=\sum_{\varnothing\ne F\subseteq E\setminus\{e\}}U_F.
\]
Hence
\[
 \begin{aligned}
 \sum_{e\in E}\|g_e-\alpha_k\|_2^2
 &=\sum_{\varnothing\ne F\subsetneq E}(m-|F|)\|U_F\|_2^2\\
 &\ge\sum_{\varnothing\ne F\subsetneq E}\|U_F\|_2^2.
 \end{aligned}
\]
The left-hand side is \(\le2m\delta_k=o(1)\), proving the first assertion. Finally,
\(\operatorname{Var}(U)=\alpha_k(1-\alpha_k)\to e^{-1}(1-e^{-1})\), and the remaining nonconstant variance is precisely the top-edge component, proving (15)–(16).

**Restricted-algorithm consequence.** Let \(T(A)\) be any mean-zero statistic lying in the linear span of functions of **proper** edge-table subsets (each summand may be arbitrarily nonlinear and high-degree *within* its own subset). Then
\[
 \boxed{
 |\mathbb E[U T]|
 =|\operatorname{Cov}(U,T)|
 \le o(1)\sqrt{\operatorname{Var}(T)}.
 }
\tag{17}
\]
In particular, if an algorithm exposes local features each depending on at most \(d\) full edge tables, then any polynomial combination of these features of **degree \(t\) with \(dt<m\)** (regardless of the number of features or overlaps) lies in this proper-edge subspace and cannot have a constant *normalized linear correlation* with the SAT bit. A connected group test on \(|U|\le r\) free vertices reads at most \(3r\) edge tables, so a polynomial degree \(t<k/(2r)\) in such local-test outputs is covered. **This is NOT a lower bound for arbitrary nonlinear thresholding, adaptive branching after seeing all tables, or unrestricted running time.**

**Maximal edge-block resampling sensitivity.** Let \(U^{(e)}\) be the UNSAT indicator after independently resampling the *entire* relation table on one edge \(e\), keeping all other tables. Conditioned on \(A_{-e}\), the two indicators are independent Bernoulli with success probability \(g_e(A_{-e})\). Therefore
\[
 \Pr[U\ne U^{(e)}]
 =2\mathbb E[g_e(1-g_e)]
 \longrightarrow
 \boxed{2e^{-1}(1-e^{-1})\approx0.4651}
\tag{18}
\]
uniformly over \(e\). Thus the Boolean SAT predicate is asymptotically *maximally sensitive to resampling any one whole edge table*, in the sense that essentially its entire variance is conditional on that table. This is not a paradox: a biased modular sum of independent large-alphabet coordinates can exhibit analogous full-block-degree behavior.

**Attribution:** the orthogonal Hoeffding/ANOVA decomposition, projection identity, and high-degree/resilience interpretation are classical tools in analysis of functions on product spaces. The claim here is their quantitative consequence for the *specific critical random cubic-expander CSP*. Priority relative to prior random-CSP literature has not been audited.

## 6. Algorithmic research question: enumerate polynomially many near-solutions without exponential search

For every deleted edge \(e=uv\), the typical random instance \(\Gamma_{-e}\) has only
\[
 N_e=(1+o(1))q^{2/3}
\]
solutions — **polynomially many** in the explicit alphabet. They have **different** endpoint pairs, and checking the missing edge relation on those pairs computes the exact original solution count and any witness in another \(O(N_e)\) table lookups.

This makes a concrete output-sensitive target:

> Design a correct exact algorithm that enumerates the solutions of \(\Gamma_{-e}\) on the specified random cubic-expander ensemble in expected \(\operatorname{poly}(k,q,N_e)\) time, or in \(q^{o(k/\sqrt{\log k})}\operatorname{poly}(k,q)\) time, **without** traversing the exponentially many consistent prefixes counted in notes 38–39.

Such an algorithm would immediately solve (and exactly count) the full critical random CSP in the same expected time. **No such enumeration algorithm is constructed here.** A small output size alone does **not** imply efficient discovery of the outputs, nor refute any worst-case/average-case hardness hypothesis.

Compared with optimizing disjoint-group entropy potentials, this targets the remaining genuinely global combinatorial search problem: discovering a polynomial-size set of critical near-solutions whose local projections are almost completely uninformative.

## Prior art / attribution

The method is elementary random-CSP second moments plus the standard Le Cam binomial-to-Poisson bound. Similar high-girth consistency phenomena occur in classical work of Gao–Culberson (*Consistency and Random Constraint Satisfaction Models*, JAIR 2007) and in random CSP resolution complexity. **Novelty of the exact endpoint-injectivity and conditional-last-edge statement has not been systematically verified against the literature**, so this is an internal research checkpoint, not a publication priority assertion.

External related reading:
- Gao–Culberson, https://mlanthology.org/jair/2007/gao2007jair-consistency/
- Barbour–Holst–Janson, *Poisson Approximation*, Oxford UP, 1992 (standard Le Cam approximation).
