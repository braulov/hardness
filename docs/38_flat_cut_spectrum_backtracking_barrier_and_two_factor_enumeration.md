# Critical expander CSP: flat edge-cut Schmidt spectrum, restricted-model barriers, and a 2-factor enumeration baseline

**2026-11-02 research checkpoint.** All calculations below are elementary consequences of the explicitly defined random CSP and known graph/probability theorems; claim **PROVED as a notebook derivation**, **NOT independently reviewed or established as novel**. Lower bounds apply only to exactly specified algorithms/representations. No worst-case or average-case fine-grained hardness hypothesis is proved.

Predecessors: [note 35](35_critical_expander_csp_poisson_and_arc_consistency.md), [note 36](36_critical_random_csp_minimal_unsat_and_all_edge_statistical_dependence.md), [note 37](37_critical_expander_low_degree_fourier_and_path_saturation.md).

## 1. Setup and exact Hilbert-space norm

Let \(G=(V,E)\) be a fixed simple cubic graph, \(|V|=k\), \(m=3k/2\). For each edge \(e=uv\) and ordered label pair \((a,b)\in[q]^2\), independently draw \(A_{e,a,b}\sim\operatorname{Bernoulli}(p)\), \(p=q^{-2/3}\), and form the random binary CSP. Define
\[
 Y_{e,a,b}=\frac{A_{e,a,b}-p}{\sqrt{p(1-p)}}
\]
and the **centered partition function**
\[
 W(A)=\frac1{q^k}\sum_{\sigma\in[q]^V}\prod_{e=uv\in E}
       \frac{A_{e,\sigma(u),\sigma(v)}-p}{p}
     =c\sum_\sigma\prod_eY_{e,\sigma(u),\sigma(v)},
 \qquad
 c=q^{-k}\bigl((1-p)/p\bigr)^{m/2}.
\]
The products for distinct full assignments are different orthonormal basis monomials, so
\[
 \boxed{\mathbb E_0 W^2=q^k c^2=(1-p)^m,\qquad \mathbb E_0W=0.}
\tag{1}
\]
Here \(q^kp^m=1\). From note 37, \(\mathbb E_0[Z-(1+W)]^2=o(1)\) when \(q=k^c\) with \(c>\max\{3/2,3/\gamma\}\).

## 2. Exact flat Schmidt spectrum across **every partition of edge tables**

Choose nonempty \(F\subsetneq E\). Let \(E_1=F\), \(E_2=E\setminus F\). Partition the vertices into
\[
 U=V(E_1)\setminus V(E_2),\quad
 T=V(E_2)\setminus V(E_1),\quad
 B=V(E_1)\cap V(E_2)
\]
(no isolated vertices). For \(b\in[q]^B\), set
\[
 u_b=\sum_{a\in[q]^U}\prod_{e\in E_1}Y_{e,(a,b)|_e},
 \qquad
 v_b=\sum_{t\in[q]^T}\prod_{e\in E_2}Y_{e,(t,b)|_e}.
\]
Then
\[
 W=c\sum_{b\in[q]^B}u_b\otimes v_b
\]
in the Hilbert decomposition \(L^2(\mathsf P_{0,E_1})\otimes L^2(\mathsf P_{0,E_2})\). Because every vertex of \(V(E_i)\) appears in an edge of \(E_i\), distinct assignments to \(V(E_i)\) give distinct orthogonal Fourier monomials. Therefore
\[
 \langle u_b,u_{b'}\rangle=\mathbf1[b=b']q^{|U|},
 \quad
 \langle v_b,v_{b'}\rangle=\mathbf1[b=b']q^{|T|}.
\]
This is already a Schmidt decomposition with \(q^{|B|}\) *equal* singular values:
\[
 \boxed{
 \operatorname{rank}_{E_1|E_2}(W)=q^{|B|},
 \qquad
 \lambda_1=\cdots=\lambda_{q^{|B|}}
 =\sqrt{(1-p)^m/q^{|B|}}.
 }
\tag{2}
\]

**Unrestricted separable-function approximation lower bound.** By Eckart–Young in Hilbert space, for any measurable functions \(a_i(A_{E_1})\), \(b_i(A_{E_2})\) and any \(r\ge0\):
\[
 \boxed{
 \mathbb E_0
 \left[
 W-\sum_{i=1}^r a_i(A_{E_1})b_i(A_{E_2})
 \right]^2
 \ge
 (1-p)^m\max\{0,1-r/q^{|B|}\}.
 }
\tag{3}
\]
The functions \(a_i,b_i\) may be **arbitrary nonlinear/high-degree functions** on their own edge-table sets. The restriction is *only the cross-cut separation rank* \(r\). Exact equality is attained by truncating the Schmidt decomposition. This is an L2 statement for the given product distribution and does **not** imply that arbitrary algorithms or randomized protocols require \(q^{|B|}\) time/communication.

## 3. Expander forces linear-size boundaries at all balanced edge cuts

Suppose \(G\) has edge expansion at least \(\gamma>0\):
\[
 |\delta(S)|\ge\gamma\min(|S|,k-|S|).
\]
If \(|E_1|,|E_2|\ge m/3=k/2\), then
\[
 \boxed{|B|\ge\gamma k/18.}
\tag{4}
\]
Indeed, since \(G\) is 3-regular, \(2|E_1|\le3(|U|+|B|)\) and \(2|E_2|\le3(|T|+|B|)\). Thus \(|U|+|B|\ge k/3\) and \(|T|+|B|\ge k/3\). If \(|B|\ge k/6\), done since \(\gamma\le3\). Otherwise \(|U|,|T|\ge k/6\), and since no edge connects \(U\) directly to \(T\), \(|\delta(U)|\le3|B|\). Expansion implies \(3|B|\ge \gamma k/6\), proving (4).

Every binary/subcubic tree with \(m\) edge-table leaves has a tree edge splitting them into sets both of size \(\ge m/3\). Consequently, for *any* tree tensor decomposition of the **input function** \(W\), some bond across a balanced table cut has exact rank at least
\[
  q^{\gamma k/18}.
\]
More strongly, if an approximating tree tensor network has bond dimensions all \(r=o(q^{\gamma k/18})\), it incurs L2 error \(\ge1-o(1)\) on that cut (for \(q=k^c\) and \(mp=o(1)\)). A constant squared-error goal below \(1/2\) requires one bond dimension \(\Omega(q^{\gamma k/18})\).

**Scope:** this rules out *low-bond-dimension representations of the random-variable function \(W(A)\)*, not general algorithms evaluating \(W\) on a concrete input. Exact/approximate matrix contractions may exploit computational formulas with high separation rank (determinants are a standard warning). Standard background on contraction orders/treewidth: Markov–Shi, https://doi.org/10.1137/050644756 .

**Numerical sanity check:** on \(G=K_4\), \(q=2\), constructing the normalized coefficient flattenings gives (boundary size, rank, singular value): \(B=2\to(4,1/2)\); \(B=3\to(8,1/\sqrt8)\); \(B=4\to(16,1/4)\). These are checks of (2), not its proof.

## 4. A second obstruction: edgewise SVD truncation has almost no Frobenius compression

For each edge, let \(C_e=A_e-pJ\in\mathbb R^{q\times q}\). Its entries are iid centered Bernoulli. With probability \(1-o(1)\) simultaneously for all \(m=O(k)\) edges when \(q=k^c\) for fixed \(c>0\):
\[
 \boxed{
 \|C_e\|_F^2=\Theta(q^2p)=\Theta(q^{4/3}),
 \quad
 \|C_e\|_{\mathrm{op}}^2
 =O(qp\log(kq)+\log^2(kq)).
 }
\tag{5}
\]
The Frobenius bound follows by Chernoff applied to the \(\operatorname{Bin}(q^2,p)\) number of ones. The operator bound follows from rectangular matrix Bernstein (Tropp), variance parameter \(qp(1-p)\), individual-entry norm at most 1, and a union bound over the \(O(k)\) edges:
https://doi.org/10.1007/s10208-011-9099-z .

Since \(qp=q^{1/3}\gg\log^2(kq)\), the second quantity is \(O(q^{1/3}\log(kq))\). Any rank-\(r\) approximation \(\widetilde C_e\) — even the *optimal data-adaptive SVD truncation* — obeys
\[
 \boxed{
 \frac{\|C_e-\widetilde C_e\|_F^2}{\|C_e\|_F^2}
 \ge 1-O\left(\frac{r\log(kq)}q\right)
 }
\tag{6}
\]
provided \(\operatorname{rank}(\widetilde C_e)\le r\) and it is chosen optimally; for a nonoptimal rank-\(r\) approximation the error is only larger. Thus \(r=o(q/\log(kq))\) loses almost all per-edge Frobenius mass. This *alone* does not prove that the final scalar contraction cannot be accurately estimated: cancellation and nonlocal algorithms could bypass per-edge Frobenius approximation.

## 5. Rigorous average-case lower bound for **fixed-order local-check DFS**

Let \(S\subseteq V\), \(|S|=\lfloor k/2\rfloor\), be an arbitrary vertex subset chosen **independently of the random relation tables**. Write \(N_S\) for the number of assignments to vertices \(S\) satisfying all constraints with both endpoints in \(S\). Since \(e(S)=(3|S|-|\delta(S)|)/2\),
\[
 \boxed{
 \mathbb EN_S=q^{|S|}p^{e(S)}
 =q^{|\delta(S)|/3}
 \ge q^{\gamma\lfloor k/2\rfloor/3}.
 }
\tag{7}
\]
For the displayed equality, note \(p=q^{-2/3}\); for odd \(k\) a cubic graph cannot exist, so \(k\) is even and \(|S|=k/2\).

We proved in [note 36, eq. (3)](36_critical_random_csp_minimal_unsat_and_all_edge_statistical_dependence.md) that **every proper edge-subinstance** \(F\subsetneq E\) satisfies
\[
 \frac{\operatorname{Var}(Z_F)}{(\mathbb EZ_F)^2}
 \le\eta_k=q^{-2/3}+2((1+q^{-\gamma/3})^k-1)=o(1)
\]
whenever \(q=k^c\), \(c>3/\gamma\). With \(F=E[S]\), we have \(Z_F=q^{k-|S|}N_S\), so the same concentration bound applies to \(N_S\). By Chebyshev,
\[
 \Pr[N_S\le\frac12 q^{\gamma k/6}]
 \le 4\eta_k=o(1).
\tag{8}
\]

Meanwhile, note 35 proves \(\Pr[Z=0]\to e^{-1}\). Therefore, on a set of instances with probability at least \(e^{-1}-o(1)\), the full CSP is **UNSAT** but has \(\Omega(q^{\gamma k/6})\) consistent assignments on the chosen first half of the variables.

**Corollary (precisely restricted backtracking model).** Any complete depth-first search with a **fixed, input-independent variable ordering** that only prunes a partial assignment when it violates an already fully instantiated original relation, and otherwise enumerates all consistent prefixes before declaring UNSAT, requires
\[
 \boxed{q^{\Omega(k)}}
\]
steps on a constant \(\approx e^{-1}\) fraction of the null input distribution. This holds regardless of the ordering of values. It is **not** a lower bound on DFS with global feasibility lookahead, clause learning, Gaussian elimination, memoization, variable orders depending on table contents, or general algorithms.

## 6. Unconditional average-case **positive baseline**: \(q^{k/3}\) by a 2-factor

Now assume the cubic graph is **bipartite**. Hall's theorem gives a perfect matching \(M\), computable in polynomial time. Deleting \(M\) leaves a spanning 2-regular graph \(G_0\), a disjoint union of cycles, with exactly \(k\) edges. For any fixed input relations, enumerate all assignments satisfying constraints on \(G_0\), then test every matching edge of \(M\) on each enumerated assignment.

A CSP on disjoint cycles can be **preprocessed and enumerated with polynomial delay**: for each cycle fix one of \(q\) starting labels, compute backward Boolean reachability tables to test future completion, and output each consistent label sequence by backtracking along the cycle. Construct the Cartesian product of per-cycle enumerators, with only polynomial overhead per output; detect an empty cycle solution set in polynomial time.

The output count of this enumeration is \(N_0\). For the Bernoulli-\(p\) random relation model,
\[
 \boxed{
 \mathbb EN_0=q^k p^{|E(G_0)|}
 =q^kp^k=q^{k/3}.
 }
\tag{9}
\]
Consequently, the exact SAT decision, witness search, and counting algorithms above have expected runtime
\[
 \boxed{
 \operatorname{poly}(k,q)\left(1+q^{k/3}\right).
 }
\tag{10}
\]
They are correct on **every** input and their expected runtime estimate is over random relation tables. An output-sensitive formulation also holds deterministically: \(\operatorname{poly}(k,q)(1+N_0)\). This is a genuine unconditional algorithmic baseline for the critical distribution but **does not beat** the reported tensor \(q^{O(k/\sqrt{\log k})}\) in the asymptotic exponent.

The comparison illustrates the bottleneck: one can satisfy \(k\) of the \(3k/2\) edges cheaply and explicitly list \(q^{k/3}\) candidates, but imposing the final matching constraints without exponentially many candidates requires a global technique.

## New unconditional average-case improvement (2026-11-02)

The \(q^{k/3}\) 2-factor enumeration in Section 6 is **not** the best simple unconditional expected-time bound for critical iid Bernoulli tables. [Follow-up note 39](39_critical_csp_cutwidth_expected_algorithms.md) proves the exact identity
\(\mathbb E N_S=q^{|\delta(S)|/3}\) for every fixed prefix \(S\), then constructs a table-independent order of cutwidth \(k/4+o(k)\). This gives \(q^{k/12+o(k)}\operatorname{poly}(k,q)\) expected time for exact counting on **any connected cubic graph**. For high-girth triangle-free cubic graphs a sound unary-support forward check lowers the constant to \((14\sqrt7-20)/243\approx0.070126\). The previous restricted fixed-order DFS lower bound still gives \(q^{\Omega(k)}\) for **every order**, but its hidden constant is compatible with these improved exponential upper bounds. None of this challenges the external Nguyen \(q^{o(k)}\) solver.

## 7. Consequences and next live research targets

1. **Close/deprioritize** plain tree tensor truncation of the full-input likelihood ratio, naive fixed-order backtracking, and per-edge low-rank SVD as candidates for average-case \(q^{o(k/\sqrt{\log k})}\) improvements. The proofs restrict exact models; they are *not* no-go results for all contraction algorithms.
2. **Keep open** nonseparable algebraic contraction, randomized hashing, data-dependent high-rank algorithms, fast matrix multiplication over structured subgraphs, and signed/spectral statistics of unbounded degree.
3. Improve the **2-factor enumeration** by processing the third perfect matching without enumerating all \(q^{k/3}\) partial solutions; this is a concrete exact algorithmic challenge. Another route is to approximate the centered contraction \(W\) additively, but (3) shows oblivious low-bond truncation is not the answer.
4. Pursue formal restricted-model lower bounds as evidence about the proposed SqrtLog-SPACH source, but do not promote them to an overall random-CSP hardness theorem.

**Attribution:** the algebraic Schmidt decomposition is the elementary COPY-tensor/graphical-model structure, and the use of treewidth as contraction complexity is classical. The applications and constants are internal research observations. No claim of publication-level novelty is made.
