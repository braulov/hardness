# Random fine-lift existence at the binary-CSP threshold: second moment and an algorithmic gap

**2026-11-03. Status:** rigorous elementary second-moment proof for a specified random model; polynomial-time greedy algorithm in a strictly easier density range; **not** a worst-case critical-density CSP algorithm and **not** an established new random-CSP theorem. Related classical random binary CSP thresholds: Frieze–Molloy (2006), https://doi.org/10.1002/rsa.20118, and subsequent growing-domain CSP literature. This note extends the question raised in [spectral universal lifting](43_spectral_quotient_greedy_and_explicit_hadamard_fullrank.md): what if only **one** coarse witness needs a fine lift?

## 1. Model and exact threshold scale

Let $k\to\infty$, $d=\sqrt{\log k}$ (natural logarithm), $q=\lceil k^c\rceil$ for fixed $c>1$, and let the **simple primal graph** be $G\sim G(k,d/k)$. Conditional on $G$, each ordered domain pair $(a,b)\in[q]^2$ is independently declared allowed on each edge with probability
\[
\rho=q^{-\gamma/d},\qquad \gamma>0\text{ fixed}.
\]
All edge tables and entries are mutually independent. Let $Z$ denote the number of satisfying assignments and $m=|E(G)|$. For every fixed $G$,
\[
\mathbf E[Z\mid G]=q^k\rho^m.
\]
As $m=(1+o(1))kd/2$ w.h.p., the annealed first-moment crossover is $\gamma=2$.

**Theorem 1 (fixed-gap SAT--UNSAT transition, for $c>1$).** For every fixed $\varepsilon\in(0,2)$:
- at $\gamma=2-\varepsilon$, $\Pr(Z>0)=1-o(1)$;
- at $\gamma=2+\varepsilon$, $\Pr(Z>0)=o(1)$.

The second statement in fact holds for every $\varepsilon>0$. The result asserts only fixed-gap threshold behavior, not the width of a critical scaling window, or an efficient algorithm near $\gamma=2$.

## 2. Exact second-moment formula conditional on G

For two assignments $x,y\in[q]^k$, put $S=\{v:x_v=y_v\}$. At an edge $uv$, $x$ and $y$ query the **same** random relation entry iff $u,v\in S$. Therefore
\[
\mathbf E[Z^2\mid G]
=\sum_{x,y}\rho^{2m-e_G(S(x,y))}.
\]
Dividing by $\mathbf E[Z\mid G]^2=(q^k\rho^m)^2$ gives the exact identity
\[
\boxed{
\frac{\mathbf E[Z^2\mid G]}{\mathbf E[Z\mid G]^2}
=\sum_{S\subseteq V(G)}
q^{-|S|}(1-q^{-1})^{k-|S|}
\rho^{-e_G(S)}.
}
\tag{1}
\]
Equivalently, the ratio is $\mathbf E_{S\sim\mathrm{Bernoulli}(1/q)^k}[\rho^{-e_G(S)}]$. The empty set contributes $(1-1/q)^k=1-o(1)$ when $c>1$.

## 3. Typical random-graph density profile, uniform over all vertex sets

For any fixed small $\eta>0$, one may choose $\alpha=\alpha(\eta)>0$ such that the following BOTH hold w.h.p. for $G\sim G(k,d/k)$:
\[
e_G(S)\le
\begin{cases}
\eta d|S|,&1\le|S|\le\alpha k,\\
(1+\eta)d|S|^2/(2k),&\alpha k\le|S|\le k.
\end{cases}
\tag{2}
\]

**Proof for small $S$.** Let $s=|S|$, $t=\lceil\eta ds\rceil$. If $t>{s\choose2}$ the bad event is impossible. Otherwise
\[
\Pr[\exists S,\ |S|=s,\ e_G(S)\ge t]
\le {k\choose s}{{s\choose2}\choose t}(d/k)^t
\le \left[\frac{ek}{s}
\left(\frac{es}{2\eta k}\right)^{\eta d}\right]^s
\]
for all sufficiently large k, provided $\alpha<\eta/e$. Put $z=s/k$. The bracket $(e/z)(ez/(2\eta))^{\eta d}$ is increasing in $z$ when $\eta d>1$, and at $z=\alpha$ it is exponentially small in $d$ if $\alpha$ is chosen sufficiently below $2\eta/e$. Summing over all $s\ge1$ proves the first uniform inequality.

**Proof for large $S$.** For a fixed $S$ of size $s\ge\alpha k$, $e_G(S)$ is binomial with mean $d{s\choose2}/k$; a multiplicative Chernoff bound gives
\[
\Pr[e_G(S)>(1+\eta)ds^2/(2k)]
\le\exp(-\Omega_\eta(\alpha^2kd)).
\]
There are at most $2^k$ choices of $S$, and $d\to\infty$, so their union probability tends to zero.

This profile implies $m=(1+o(1))kd/2$ by an ordinary Chernoff estimate as well.

## 4. Proof of the satisfiable side

Fix $\gamma=2-\varepsilon<2$ and $c>1$. Choose $\eta>0$ sufficiently small so
\[
c(1-\gamma\eta)>1,\qquad
\delta:=1-\gamma(1+\eta)/2>0.
\tag{3}
\]
Conditional on a graph obeying (2), split the NONEMPTY subsets in (1) into two classes.

For $0<|S|\le\alpha k$, use $e_G(S)\le\eta d|S|$ and $\rho=q^{-\gamma/d}$:
\[
\sum_{0<|S|\le\alpha k}
q^{-|S|}(1-1/q)^{k-|S|}\rho^{-e(S)}
\le(1+q^{-(1-\gamma\eta)})^k-1=o(1),
\]
because $kq^{-(1-\gamma\eta)}\to0$ by (3).

For $|S|>\alpha k$, use $e_G(S)\le (1+\eta)d|S|^2/(2k)$:
\[
q^{-|S|}\rho^{-e(S)}
\le q^{-|S|+\gamma(1+\eta)|S|^2/(2k)}
\le q^{-\delta|S|}.
\]
Thus the contribution of large $S$ is at most
\[
2^kq^{-\delta\alpha k}=o(1).
\]
The empty-set contribution is $(1-1/q)^k=1-o(1)$; by Cauchy--Schwarz the whole ratio is always at least 1. Therefore
\[
\frac{\mathbf E[Z^2\mid G]}{\mathbf E[Z\mid G]^2}=1+o(1),
\quad
\Pr[Z>0\mid G]\ge\frac{\mathbf E[Z\mid G]^2}{\mathbf E[Z^2\mid G]}=1-o(1).
\]
Averaging over $G$ proves the SAT claim.

For $\gamma=2+\varepsilon$, w.h.p. $m=(1+o(1))kd/2$, so
\[
\mathbf E[Z\mid G]=q^{k-\gamma m/d}
=q^{-(\varepsilon/2+o(1))k}=o(1).
\]
Markov gives the UNSAT claim.

**Caveat:** the $c>1$ restriction in this proof is sufficient to make the NONEMPTY-overlap contribution $o(1)$ by coarse bounding. The argument **does not establish** that $c\le1$ is hard or has a different threshold; that range may permit a sharper second moment.

## 5. Polynomial-time greedy search for gamma < 1

**Theorem 2.** For *every* fixed $c>0$ and $0<\gamma<1$, a deterministic polynomial-time algorithm (given the sampled CSP instance) finds a satisfying assignment with probability $1-o(1)$ over the random input.

First, w.h.p. the random graph has degeneracy at most $(1+\zeta)d$ for every fixed $\zeta>0$. Indeed, apply (2) using small-set constant $\eta<(1+\zeta)/2$ and large-set parameter $\eta'<\zeta$; then every induced graph has average degree at most $(1+\zeta)d$ and hence a vertex of degree at most that. The graph admits a degeneracy ordering with at most $D=(1+\zeta)d$ *earlier* neighbors per vertex.

Choose $\zeta$ so $\gamma(1+\zeta)<1$. For any vertex v and any preassignment of its at most D earlier neighbors, the number of compatible values at v is $\operatorname{Bin}(q,\rho^t)$ for $t\le D$, and the probability it is zero is at most
\[
\exp(-q\rho^D)
\le \exp(-q^{1-\gamma(1+\zeta)})
=\exp(-k^{\Omega(1)}).
\]
A union bound over at most $kq^D$ vertex/previous-neighbor assignments is $o(1)$ because $D=O(\sqrt{\log k})$ and $q=k^c$. Therefore *all* local steps in this fixed graph-dependent degeneracy ordering admit a choice, and a simple deterministic greedy algorithm succeeds w.h.p. It takes $\operatorname{poly}(k,q,m)$ time.

Consequently the proven regime diagram for $c>1$ is:
- $\gamma<1$: SAT w.h.p. **and** polynomial-time greedy solution;
- $1\le\gamma<2$: SAT w.h.p. (for $\gamma<2$ fixed), but this proof does **not** yield a polynomial-time search algorithm;
- $\gamma>2$: UNSAT w.h.p. and first-moment certificate only in the probability-analysis sense (not an efficiently found UNSAT proof).

These are **sufficient guarantees**, not established intrinsic computational thresholds at 1 or 2 for all algorithms.

## 6. What this says about "lift at least one coarse witness"

Let an arbitrary **coarse CSP** on the same random primal graph have some already identified satisfying coarse assignment $(i_v)$. On each edge, for the one selected allowed class pair $(i_u,i_v)$, sample an independent Bernoulli($\rho$) fine relation on fine domains of size $L=k^c$, independent between edges and entries. All other coarse rectangles may be sampled separately; they do not matter for this fixed lift.

Restricted to the fixed coarse solution, the fine lift problem has exactly the distribution of Sections 1–5 with $q=L$. For $c>1$, $\gamma<2$ a **single fixed coarse witness** lifts with probability $1-o(1)$; for $\gamma<1$ the lift can even be found greedily in polynomial time w.h.p.

This is strictly weaker than universal deterministic lifting of **every** coarse assignment. In particular, for $\gamma>1$ and a vertex with about $d$ neighbors, a fixed assignment of all its neighbors has expected compatible fine values $q\rho^d=q^{1-\gamma}=o(1)$, so the universal extension property fails with high probability. This is fully compatible with global SAT w.h.p.

**Crucial distinction:** SAT existence with high probability is NOT an efficient search algorithm and does NOT refute any worst-case critical-density hardness hypothesis. No $q^{o(k)}$ algorithm for all CSP inputs is obtained.

## 7. Prior art and research target

- Alan Frieze and Michael Molloy, *The satisfiability threshold for randomly generated binary constraint satisfaction problems*, Random Structures & Algorithms 28(3), 2006. https://doi.org/10.1002/rsa.20118 . Direct domain/growing-degree hypotheses need comparison before claiming novelty.
- Yun Fan, Jing Shen, Ke Xu, *A general model and thresholds for random constraint satisfaction problems*, Artificial Intelligence 193 (2012). https://doi.org/10.1016/j.artint.2012.08.003 .
- Prior project work: [random threshold first moment and greedy dense-table regime](40_nguyen_grouping_overhead_and_random_csp_greedy.md); [spectral universal fine-lift](43_spectral_quotient_greedy_and_explicit_hadamard_fullrank.md).

**Next open algorithmic target:** close any part of the $\gamma\in(1,2)$ *random-model search gap*, by developing global repair / adaptive decimation / witness-dependent lifting, rather than requiring compatibility with every arbitrary earlier-neighbor assignment. Track time and success probability, and compare rigorously with known results for random growing-domain binary CSP and Model RB.
