# Critical random CSP: full-edge Fourier signal, low-degree barrier, and four-step path saturation

**Date:** 2026-11-02.  
**Status:** Internal theorems proved below using elementary Bernoulli Fourier expansion, the second-moment bound in note 35, and Chernoff inequalities. No computational hardness claim. Novelty of the concrete results is **not** established; low-degree likelihood-ratio methodology is established prior art.

This is a continuation of [note 35: Poisson and arc consistency](35_critical_expander_csp_poisson_and_arc_consistency.md) and [note 36: irredundancy and missing-edge planted indistinguishability](36_critical_random_csp_minimal_unsat_and_all_edge_statistical_dependence.md).

## 1. Exact likelihood-ratio Fourier spectrum

Fix a connected simple cubic edge-expander \(F_k=(V,E)\), \(|V|=k\), \(|E|=m=3k/2\), edge expansion \(\gamma>0\). For each \(e=uv\in E\) and \((a,b)\in[q]^2\), independently include \((a,b)\) in its relation with probability \(p=q^{-2/3}\). This defines the **null** law \(\mathsf P_0\) on the \(mq^2\) table bits \(A_{e,a,b}\). The **planted** law \(\mathsf P_1\) draws uniform \(\sigma\in[q]^V\), then forces \((\sigma(u),\sigma(v))\) into every edge table and samples the other entries as in \(\mathsf P_0\).

The full-data likelihood ratio is \(L=d\mathsf P_1/d\mathsf P_0=Z\), the number of satisfying assignments. Indeed, \(\mathbb E_{\mathsf P_0} Z=q^kp^m=1\).

For each table bit use the normalized centered Bernoulli coordinate
\[
 Y_{e,a,b}=\frac{A_{e,a,b}-p}{\sqrt{p(1-p)}}.
\]
Products of distinct \(Y_{e,a,b}\) form the orthonormal \(p\)-biased Fourier basis of \(L^2(\mathsf P_0)\).

**Exact coefficient formula.** For a squarefree monomial \(Y_T=\prod_{t\in T}Y_t\), \(\widehat L(T)=\mathbb E_{\mathsf P_0}[LY_T]\) vanishes if (i) two **different entries of the same edge table** appear or (ii) prescribed endpoint labels of chosen entries disagree at any shared vertex. Otherwise the monomial chooses precisely one pair for each edge \(e\in F\), for a nonempty edge subset \(F\subseteq E\), the prescribed labels are consistent on \(V(F)\), and
\[
 \boxed{\widehat L(T)=q^{-|V(F)|}
 \left(\frac{1-p}{p}\right)^{|F|/2}.}
\tag{1}
\]
The empty monomial has coefficient \(\widehat L(\varnothing)=1\).

*Proof:* For each planted assignment \(\sigma\), \(L=q^{-k}p^{-m}\sum_\sigma\prod_e A_e(\sigma_e)\). On an edge selected by \(T\), the inner product with one centered entry is zero unless it equals \(\sigma_e\); if equal, the ratio of expectations is \(\sqrt{(1-p)/p}\). Two distinct centered entries on the same edge give zero because the planted summand uses exactly one table bit from that edge. Each consistent partial prescription on \(V(F)\) extends to \(q^{k-|V(F)|}\) complete assignments. Summing yields (1).

There are exactly \(q^{|V(F)|}\) coherent edge-label prescriptions for each \(F\) (every vertex of \(V(F)\) is incident to a selected edge). Therefore the squared Fourier norm of the subspace using **exactly** edge-table set \(F\) equals
\[
 \boxed{W(F)=q^{-|V(F)|}\left(\frac{1-p}{p}\right)^{|F|}.}
\tag{2}
\]
In particular, since \(q^kp^m=1\) and \(V(E)=V\),
\[
 \boxed{W(E)=(1-p)^m.}
\tag{3}
\]
This is the entire squared norm of the **degree exactly \(m\)** component: higher-degree Fourier coefficients vanish, because a nonzero monomial chooses at most one table bit per edge.

## 2. All nontrivial low-degree Fourier mass vanishes

Let \(L^{\le D}\) denote orthogonal projection of \(L\) onto table-bit polynomials of total degree at most \(D\). The second-moment bound previously established in note 35 is
\[
 \mathbb E_{\mathsf P_0}L^2
 \le 2+B_k,\qquad
 B_k:=2\left((1+q^{-\gamma/3})^k-1\right).
\tag{4}
\]
Combining Parseval with (3), the squared mass of *all* nonconstant degrees **strictly below \(m\)** is
\[
\begin{aligned}
 \left\|L^{\le m-1}-1\right\|_2^2
 &=\mathbb E_{\mathsf P_0}L^2-1-(1-p)^m\\
 &\le 1-(1-p)^m+B_k\\
 &\le mp+B_k.
\end{aligned}
\tag{5}
\]
Hence, when \(q=\lceil k^c\rceil\) with
\[
 \boxed{c>\max\{3/2,\,3/\gamma\}},
\]
we have \(mp=O(kq^{-2/3})=o(1)\) and \(B_k=O(kq^{-\gamma/3})=o(1)\), giving
\[
 \boxed{\left\|L^{\le m-1}-1\right\|_{L^2(\mathsf P_0)}=o(1).}
\tag{6}
\]
By contrast \(\operatorname{Var}_{\mathsf P_0}(L)=1+o(1)\), since \(Z\Rightarrow\operatorname{Pois}(1)\) and the second moment tends to 2, and \(d_{\rm TV}(\mathsf P_1,\mathsf P_0)\to e^{-1}\).

**Testing corollary, precise scope.** For any real polynomial \(T\) of table bits with degree \(<m\) and \(\operatorname{Var}_{\mathsf P_0}(T)=1\),
\[
 \boxed{\left|\mathbb E_{\mathsf P_1}T-\mathbb E_{\mathsf P_0}T\right|
       \le\sqrt{mp+B_k}=o(1).}
\tag{7}
\]
This follows by Cauchy–Schwarz from \(\mathbb E_{\mathsf P_1}T-\mathbb E_{\mathsf P_0}T=\langle L-1,T-\mathbb E_{\mathsf P_0}T\rangle\).

The bound is not confined to polynomials of a few *edge tables*: it holds for degree \(<3k/2\) polynomials allowed to mix **all** \(mq^2\) input entries. More generally, orthogonality to the full-edge component implies the same normalized correlation bound for any \(T\) lying in the linear span of arbitrary functions of **proper** edge-table subsets, even when their bit degree is very high.

**What is not proved:** no lower bound against arbitrary polynomial-time algorithms, high-degree but efficiently computable statistics (e.g. determinants), arbitrary nonlinear thresholding of low-degree polynomial statistics, SDP/SoS in full generality, or exact SAT decision. A low-degree likelihood-ratio barrier is only a rigorously defined *restricted testing model*. Compare [Kunisky, "Low-Degree Polynomial Testing in Morris Families", PMLR 2021](https://proceedings.mlr.press/v134/kunisky21a/kunisky21a.pdf) and [Kane et al., "Rigorous Implications of the Low-Degree Heuristic"](https://cseweb.ucsd.edu/~dakane/FoolingSymmetricPolys.pdf). We do NOT claim a new methodology.

**Sanity check:** For \(F_k=K_4\) (six edges), an independent explicit enumeration of all \(2^6\) edge subsets and all \(2^4\) vertex-agreement sets numerically confirms that \(\sum_F W(F)=\mathbb E L^2\), e.g. at \(q=100\) both equal approximately \(2.05167733864\), while \(W(E)\approx0.7518895315\). This finite check illustrates but does not prove the asymptotic theorem.

## 3. Four-step relational composition saturates completely

Let \(R_1,\dots,R_\ell\subseteq[q]^2\) be independent Bernoulli-\(p\) random binary relations with \(p=q^{-2/3}\), oriented along a **simple path of distinct constraint edges**. Let \(R^{(\ell)}=R_1\circ\cdots\circ R_\ell\).

For any fixed pair of endpoint labels \((a,b)\), as \(q\to\infty\):
\[
\begin{array}{c|c}
\ell&\Pr[(a,b)\in R^{(\ell)}]\\\hline
1&q^{-2/3}\\
2&1-(1-p^2)^q=(1+o(1))q^{-1/3}\\
3&1-e^{-1}+o(1)\\
4&1-e^{-\Omega(q^{1/3})}.
\end{array}
\tag{8}
\]

**Length 3:** Independently expose the set \(S\) of neighbors of \(a\) via \(R_1\) and the set \(T\) of predecessors of \(b\) via \(R_3\). Both have \(\operatorname{Bin}(q,p)\) cardinalities and \(|S|/q^{1/3},|T|/q^{1/3}\to1\) in probability. Conditional on \(S,T\), a three-edge path exists iff \(R_2\) contains at least one pair in \(S\times T\). Hence
\[
 \Pr[\text{no 3-step path}]=\mathbb E(1-p)^{|S||T|}\to e^{-1}.
\]

**Length 4:** Fix starting label \(a\), let \(S_i\subseteq[q]\) be the labels reachable after step \(i\). Chernoff bounds applied sequentially to disjoint independent edge tables yield, with failure probability \(e^{-\Omega(q^{1/3})}\),
\[
 |S_1|\ge c_1q^{1/3},\quad
 |S_2|\ge c_2q^{2/3},\quad
 |S_3|\ge c_3q
\]
for absolute constants \(c_i>0\). On this event the probability that a fixed terminal \(b\) has no incoming edge from \(S_3\) is at most \(e^{-c_3qp}=e^{-\Omega(q^{1/3})}\). Therefore
\[
 \boxed{\Pr[R^{(4)}\ne[q]^2]\le
       q^2 e^{-\Omega(q^{1/3})}=o(1).}
\tag{9}
\]
A cubic graph on \(k\) vertices has \(O(k)\) oriented simple 4-edge paths, so for any polynomially growing \(q=k^c\) all such length-4 compositions are **simultaneously universal with high probability**.

**Interpretation:** eliminating the internal variables of a *standalone* four-edge path loses all binary endpoint information, even though the **complete** random CSP has constant UNSAT probability and is edge-minimally UNSAT with constant probability. This is a precise obstruction to naive path-composition and local elimination heuristics. It is **not** a proof that all variable elimination or higher-arity/global algorithms fail: different paths share vertices, and their witnesses must agree.

## 4. Bit-probe query lower bound by coupling (optional, weaker than a time lower bound)

Couple the null and planted tables by first sampling all null bits and independent uniform planted assignment \(\sigma\), then switching to 1 the \(m\) required entries \((e,\sigma(u),\sigma(v))\). Consider a possibly randomized adaptive algorithm that probes at most \(T\) individual table bits and sees only their values. Run it on the null tables and use the same internal randomness in the planted copy. Until it probes a forced coordinate, both transcripts agree. Conditional on the null tables and the algorithm's complete null-query sequence, which is independent of \(\sigma\), any queried coordinate coincides with the corresponding forced coordinate with probability \(1/q^2\). Union bound:
\[
 \boxed{
 d_{\rm TV}(\text{null probe transcript},
            \text{planted probe transcript})
 \le T/q^2.
 }
\tag{10}
\]
Thus \(o(q^2)\) **individual bit probes** cannot distinguish with constant advantage, even with unlimited computation between probes. This is an input-access bound only (the explicit input has \(\Theta(kq^2)\) table bits), and is much weaker than a conjectured \(q^{\Omega(k/\sqrt{\log k})}\) running-time lower bound. It does **not** apply if the algorithm is freely given precomputed global summaries or uses a different access model.

## 4a. A precise average-case algorithmic target: additive centered contraction

The unique top-degree component \(W_E\) (as a random variable, rather than its squared norm in equation (3)) is the signed partition function
\[
 \boxed{
 \mathcal W_E(A)=\frac1{q^k}\sum_{\sigma\in[q]^V}
             \prod_{e=uv\in E}
             \frac{A_{e,\sigma(u),\sigma(v)}-p}{p}.
 }
\tag{11}
\]
It is the degree-\(m\) orthogonal projection of the likelihood ratio \(L=Z\). By equations (5)–(6),
\[
 \mathbb E_{\mathsf P_0}
 \left[Z-(1+\mathcal W_E)\right]^2
 \le mp+B_k=o(1).
\tag{12}
\]
Thus for a **random null CSP instance**, with probability \(1-o(1)\), rounding \(1+\mathcal W_E(A)\) to the nearest integer recovers the *exact* solution count \(Z\). More algorithmically, an evaluation routine returning \(\widehat{\mathcal W}_E(A)\) with additive error \(<1/5\) on a \(1-o(1)\) fraction of instances yields an exact average-case counting algorithm by rounding \(1+\widehat{\mathcal W}_E(A)\), with failure probability \(o(1)\). The same works with any fixed success probability after paying that failure rate. **An efficient additive approximation routine is NOT constructed here.** The result applies to the *null distribution*; a corresponding statement for arbitrary adversarial instances or the planted distribution requires new moment estimates.

**Naive Monte Carlo does not help in mean-square.** Sample \(N\) independent uniform assignments \(\sigma^{(i)}\), and average
\[
 g_\sigma(A)=\prod_{e\in E}\frac{A_{e,\sigma(u),\sigma(v)}-p}{p}.
\]
This is conditionally unbiased for \(\mathcal W_E(A)\). A single sample has
\(\mathbb E_{\mathsf P_0,\sigma}[g_\sigma^2]=((1-p)/p)^m=q^k(1-p)^m\), while \(\mathbb E_{\mathsf P_0}[\mathcal W_E^2]=(1-p)^m\). By the total variance formula the **exact expected mean-square estimation error** is
\[
 \boxed{
 \mathbb E_{\mathsf P_0,\sigma}
 \bigl[(\tfrac1N\sum_{i=1}^N g_{\sigma^{(i)}}-\mathcal W_E)^2\bigr]
 =\frac{(q^k-1)(1-p)^m}{N}.
 }
\tag{13}
\]
Therefore this **specific unbiased sampling estimator** requires \(N=\Omega(q^k)\) evaluations for any bounded constant *root-mean-square error*. This is **not** a general sampling lower bound, nor does a large second moment by itself exclude robust/median/importance-sampling procedures with typical-instance success.

The centered matrices \(B_e=A_e-pJ\) are a sparse \(0/1\) random relation matrix minus a rank-one constant matrix. Finding an algebraic/spectral/tensor method that computes the *signed global contraction* (11) to additive \(<1/5\) accuracy in \(q^{o(k/\sqrt{\log k})}\operatorname{poly}(L)\) time on the null distribution would directly refute the proposed average-case critical-expander hardness candidate.

## Further structural audit: flat edge-cut spectrum and two-factor baseline

[Follow-up note 38](38_flat_cut_spectrum_backtracking_barrier_and_two_factor_enumeration.md) computes **all singular values** of the degree-\(m\) global Fourier function \(W(A)\) across an arbitrary edge-table bipartition: exactly \(q^{|B|}\) equal nonzero values, with \(B\) the shared endpoint set. On cubic expanders balanced cuts have \(|B|\ge\gamma k/18\), ruling out small-bond **L2 function-space** decompositions. It also rules out naive edgewise SVD and fixed-order backtracking in precisely specified models; conversely, it gives an unconditional \(q^{k/3}\operatorname{poly}\) expected-time exact solver for the random bipartite cubic model via a perfect matching and cycle-cover enumeration. These observations do not prove computational hardness or contradict any general tensor contraction theorem.

## November 3: strong full-edge block spectrum of the Boolean SAT/UNSAT function

[Note 47](47_conditional_poisson_after_one_edge_and_endpoint_injectivity.md) derives a **different** Fourier statement from the conditional Poisson last-edge theorem: while this note analyzes the *solution count likelihood ratio* \(Z\) in single-table-bit Fourier degree, note 47 analyzes the **Boolean UNSAT indicator** \(U=1_{Z=0}\) in the product space whose coordinates are entire **edge-relation tables**. It proves
\[
 \sum_{\emptyset\ne F\subsetneq E}\|U_F\|_2^2=o(1),\qquad
 \|U_E\|_2^2\to e^{-1}(1-e^{-1})
\]
in the Hoeffding/ANOVA decomposition, for cubic high-girth expanders with sufficiently large polynomial alphabet. The SAT predicate thus behaves like a parity/resilient function at the level of whole edge blocks. This is a strong restricted-statistics structural statement, not a Boolean circuit lower bound.

## 5. Research implication

The random model has a sharp global statistical signature concentrated in full-edge Fourier degree \(m\), while standalone path composition saturates at four edges. Therefore the natural next **algorithmic** target is not local messages or independent short-path projections; it is a method that compresses or evaluates the fully coupled degree-\(m\) multilinear form \(W_E\) faster than the claimed \(q^{O(k/\sqrt{\log k})}\) tensor algorithm. A determinant, signed trace, or global algebraic transformation could still do this efficiently despite degree \(m\), so the low-degree barrier does **not** settle the algorithmic research question.

The matching **hardness** route is to prove lower bounds for well-defined classes of bounded-degree tests (low-degree statistics, limited edge-table access, or restricted tensor contraction architectures), without treating these as unconditional CSP complexity lower bounds.
