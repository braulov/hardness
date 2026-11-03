# Random-CSP local-repair obstruction, quiet planting, and hidden-witness nonrecoverability

**Date:** 2026-11-03. **Status:** unconditional elementary results for a *specified random model*. This is a follow-up to [the exact second moment and search gap](44_random_binary_csp_second_moment_and_search_gap.md). **No general worst-case CSP algorithm, no polynomial-time search in 1<gamma<2, and no novel literature priority claim.**

## A. Model and distinctions

Let $k\to\infty$, $d=\sqrt{\log k}$, $p=d/k$, $q=\lceil k^c\rceil$ (constant $c>0$) and $\rho=q^{-\gamma/d}$ (constant $\gamma>0$). Generate a simple primal graph $G\sim G(k,p)$ and, conditional on $G$, put independent Bernoulli($\rho$) entries in each explicit binary relation table on each undirected constraint edge.

The **existential search question** for $\gamma\in(1,2)$ differs radically from the property that an arbitrarily selected partial assignment admits a small repair. The latter is generically false in this model.

## B. The fixed-cut boundary-freezing obstruction

**Theorem 1 (no independent freeze-then-repair on any constant-size cut).** Fix constants $a\in(0,1)$ and $\delta>0$. Choose in advance a partition $V=W\dot\cup U$ with $|W|=\lfloor ak\rfloor$. An arbitrary algorithm may inspect the *entire graph G* and *all tables for edges internal to W*, and then produce ANY assignment $x_W$ of the variables in W (e.g., a satisfying assignment for all W-internal constraints). **It may not inspect any cross-edge relation table while choosing $x_W$.** The choice of the *partition* W is fixed in advance, independently of G; the assignment $x_W$ may depend on G. Then, with probability $1-o(1)$ over the graph and cross-edge tables, there is NO extension on U satisfying even all of the constraints crossing W,U.

This holds for **every fixed $\gamma>0$**, including below the normal polynomial-greedy range $\gamma<1$. Thus the obstruction is a property of freezing a random constant fraction without consulting cross-edge tables, not an intrinsic search hardness threshold at gamma=1.

**Proof.** For every $v\in U$, the cross-degree $t_v=\deg_G(v,W)$ has distribution $\operatorname{Bin}(|W|,d/k)$. The $t_v$ are independent across v (their underlying edge indicators are disjoint). Set
\[
t_*=\left\lceil (1+\delta)d/\gamma\right\rceil.
\tag{1}
\]
For any fixed $a,\gamma,\delta$, a simple lower bound on the binomial mass at $t_*$ gives
\[
\pi_k:=\Pr(t_v\ge t_*)\ge e^{-Cd}
\tag{2}
\]
for a constant $C=C(a,\gamma,\delta)>0$ and all sufficiently large k. To check (2), use $\binom{|W|}{t_*}\ge(|W|/t_*)^{t_*}$ and $(1-p)^{|W|-t_*}\ge e^{-2ap k}=e^{-2ad}$ (for large k), yielding $\Pr(t_v=t_*)\ge (ad/t_*)^{t_*}e^{-2ad}=\exp(-O(d))$. Since $d=\sqrt{\log k}=o(\log k)$,
\[
N:=|\{v\in U:t_v\ge t_*\}|\ge \tfrac12(1-a)ke^{-Cd}=k^{1-o(1)}
\tag{3}
\]
with probability $1-o(1)$ by binomial concentration.

Condition on G, the W-internal tables, and the arbitrary resulting $x_W$. The cross-edge relation tables remain mutually independent Bernoulli($\rho$). For any v with $t_v\ge t_*$, the number of labels at v satisfying all t_v crossing constraints with $x_W$ is $\operatorname{Bin}(q,\rho^{t_v})$, so
\[
\Pr[\text{at least one valid label at v}\mid G,x_W]
\le q\rho^{t_v}\le q^{-\delta}.
\tag{4}
\]
For different v the relevant cross-edge tables are disjoint, so these events are conditionally independent. Consequently the probability ALL these N vertices are locally extendible is at most $q^{-\delta N}=o(1)$. This is a NECESSARY condition for a global extension, proving the claim.

**Scope:** (a) The cut W must be selected independently of G for the binomial cross-degree argument. (b) The W-assignment can inspect G and its own internal CSP but not cross-edge tables. (c) If a method uses crossing tables when selecting W-assignment, it creates correlations and is not ruled out. (d) Conditional on a genuinely satisfying FULL assignment, its W-projection of course extends; its choice is heavily correlated with crossing tables.

## C. Huge expected number of extensions, but none with high probability

Let $Z_U$ be the number of assignments to U extending a fixed W-assignment (chosen as in Theorem 1), and put $\tau=1-a$. Conditional on G and x_W but averaging over all tables touching U,
\[
\mathbf E[Z_U\mid G,x_W]=q^{|U|}\rho^{m-e_G(W)}.
\tag{5}
\]
With high probability $m-e_G(W)=(1-a^2+o(1))kd/2$, hence
\[
\boxed{
\mathbf E[Z_U\mid G,x_W]
=q^{\left((1-a)[1-\gamma(1+a)/2]+o(1)\right)k}.
}
\tag{6}
\]
For $\gamma<2$, choose any $0<a<2/\gamma-1$; the exponent is POSITIVE. Nevertheless, Theorem 1 proves $\Pr[Z_U>0]=o(1)$.

Concrete parameters: $\gamma=3/2$, $a=1/10$, giving expectation $q^{(0.1575+o(1))k}$ but extension probability tending to zero. The expectation is dominated by extremely rare favourable cross-edge tables. **A positive first moment is not evidence of a typical boundary extension.**

This is the exact obstruction to an algorithm that (i) solves a large induced sub-CSP without looking at cross constraints, then (ii) tries to repair the remaining randomly selected linear fraction without revising the initial values. It is NOT a lower bound for globally coordinated algorithms.

## D. Quiet planting from the previous second moment

Now additionally assume **$c>1$ and fixed $\gamma<2$**. Let $P$ be the law of the random instance $(G,\{R_e\})$ defined in §A, and $P_{\mathrm{plant}}$ the law obtained by:
1. sampling the same G;
2. sampling a uniformly random hidden assignment $x^*\in[q]^k$;
3. conditioning every edge's table to contain the single required pair $(x^*_u,x^*_v)$ (all other entries remain independent Bernoulli($\rho$));
4. forgetting $x^*$ and outputting only the instance.

For a fixed graph G with m edges and a realized instance I, let $Z(I)$ be the number of satisfying assignments. By direct likelihood calculation,
\[
\boxed{
\frac{P_{\mathrm{plant}}(I\mid G)}{P(I\mid G)}
=\frac{Z(I)}{q^k\rho^m}
=\frac{Z(I)}{\mathbf E_P[Z\mid G]}.
}
\tag{7}
\]
Therefore
\[
d_{\mathrm{TV}}(P_{\mathrm{plant}}(\cdot\mid G),P(\cdot\mid G))
\le\frac12\sqrt{\frac{\mathbf E_P[Z^2\mid G]}{\mathbf E_P[Z\mid G]^2}-1}.
\tag{8}
\]
[Note 44, §4](44_random_binary_csp_second_moment_and_search_gap.md) proves that for $c>1$, $\gamma<2$, the ratio in (8) is $1+o(1)$ on graphs occurring with probability $1-o(1)$. Integrating over the identical graph distributions, using the trivial TV bound 1 on exceptional graphs, yields
\[
\boxed{d_{\mathrm{TV}}(P_{\mathrm{plant}},P)=o(1).}
\tag{9}
\]
This is a **quiet planting** statement. It is a corollary of the exact second moment, and the phenomenon has broad prior art in random CSPs.

**Search consequence:** If any (possibly randomized) algorithm, given *only the instance* I and not $x^*$, outputs *some satisfying assignment* with probability $1-o(1)$ on $P_{\mathrm{plant}}$ in runtime T, the very same algorithm succeeds with probability $1-o(1)$ on P, in the same T. This does NOT prove such an algorithm exists.

## E. Exact recovery of the originally planted witness is information-theoretically impossible

There is a further important distinction: solving the planted instance is **not** the same as recovering the specific planted assignment $x^*$.

For any realized I with Z(I)>0, Bayes' rule and the symmetric planting distribution give
\[
\boxed{\Pr(x^*=x\mid I,G)=
\begin{cases}
1/Z(I),&x\text{ satisfies }I,\\
0,&\text{otherwise}.
\end{cases}}
\tag{10}
\]
Hence, for any estimator $\widehat x(I)$, even with unlimited computational power, its conditional success at recovering the exact original $x^*$ is at most $1/Z(I)$.

In fact the optimal unconditional (given G) success probability is exactly
\[
\boxed{
\sup_{\widehat x}\Pr_{\mathrm{plant}}[\widehat x(I)=x^*\mid G]
=\frac{\Pr_P[Z>0\mid G]}{\mathbf E_P[Z\mid G]}
\le\frac1{q^k\rho^m}.
}
\tag{11}
\]
The equality is achieved by any oracle that outputs a satisfying assignment whenever one exists. This follows from (7) and (10).

Since on typical G, for $\gamma<2$,
\[
q^k\rho^m=q^{(1-\gamma/2+o(1))k},
\]
the maximum exact hidden-witness recovery probability is exponentially tiny,
\[
q^{-(1-\gamma/2+o(1))k}.
\tag{12}
\]
Thus **do not design a planted recovery algorithm aimed at identifying the planted x***. The legitimate goal is to output *any* satisfying assignment; that search task transfers to the unplanted model via (9).

## F. Research triage / literature

- **Proved:** no freeze-then-repair for any preselected constant-density cut whose boundary labels are chosen without crossing tables; the high-degree-tail obstruction persists even when $\mathbf E Z_U$ is exponentially large.
- **Proved assuming note 44's already-established second moment:** quiet planting, TV=o(1) for c>1 and gamma<2.
- **Proved:** exact posterior formula and information-theoretic impossibility of recovering the original planted witness.
- **Not obtained:** polynomial-time or $q^{o(k)}$ search for $1<\gamma<2$; a worst-case CSP or HOM algorithm.
- **Not excluded:** globally correlated assignments that use crossing relations before freezing anything; BP/decimation and global entropy-guided methods; graph-adaptive variable partitions (our fixed-cut theorem does not cover them).
- **Literature:** Liang Li, Tian Liu, Ke Xu, *Exact phase transition of backtrack-free search with implications on the power of greedy algorithms* (arXiv:0811.3055, 2008), proves an exact ratio between backtrack-free and SAT thresholds for **Model RB/RD with different density scaling**, so should not be cited as a theorem for this exact G(k,sqrt(log k)/k) setup. Zhao–Zhang–Zheng–Xu, *Analytical and belief-propagation studies of random CSPs with growing domains*, Phys. Rev. E 85 (2012), DOI 10.1103/PhysRevE.85.016106, reports experimental reinforced-BP successes near the threshold, not a rigorous polynomial-time guarantee.
- **Recommended next algorithmic focus:** attempt an explicit globally coordinated search on the planted distribution (e.g., BP-guided decimation whose choices use **all** crossing constraints), seek a provable invariant, and transfer any success to the unplanted model via quiet planting. Beware that the original planted witness itself is statistically unrecoverable.
