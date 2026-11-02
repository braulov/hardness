# Critical random cubic-expander CSP: Poisson(1) and local-consistency blindness

**Date:** 2026-11-02.  
**Status:** PROVED elementary expectation and arc-consistency bound; PROVED Poisson approximation by standard Arratia–Goldstein–Gordon dependency-graph theorem (proof below). This is **NOT** a computational lower bound or new hardness assumption justified by evidence. It sharpens/audits an earlier unverified Poisson(1) claim in the CEH research archive.

## 1. Model and critical scaling

Take any family of **simple 3-regular, optionally bipartite**, \(k\)-vertex graphs \(F_k=(V,E)\) with fixed positive edge-expansion \(\gamma>0\):
\[
 |\delta(S)|\ge\gamma\min(|S|,k-|S|),\qquad \forall S\subseteq V.
\]
There are \(m=3k/2\) edges. Fix a common domain \([q]\) and independently include every ordered pair \((a,b)\in[q]^2\) in the binary relation \(R_e\) with probability
\[
 p=q^{-2/3}.
\]
All bits for all edges and pairs are independent. The input consists of complete explicit relation tables of length \(O(kq^2)\), polynomial when \(q=k^c\) for fixed \(c\).

Write \(Z\) for the number of satisfying assignments. For a fixed assignment \(\sigma\in[q]^V\), its \(m\) required relation entries are independent, so
\[
 \mathbb E Z=q^kp^m=q^k q^{-(2/3)(3k/2)}=1.
\]
This is the critical density for which the first moment is neither vanishing nor exploding.

## 2. Exact second moment and expansion bound

For two assignments \(\sigma,\tau\), let \(S=\{v:\sigma(v)=\tau(v)\}\), and write \(e(S)=|E(F_k[S])|\). The two assignments use the **same independent relation table entry** on an edge precisely when *both endpoints belong to* \(S\). Thus
\[
 \Pr[I_\sigma=I_\tau=1]=p^{2m-e(S)}.
\]
There are \(q^k(q-1)^{k-|S|}\) ordered pairs of assignments with exact agreement set \(S\), so
\[
 \boxed{
 \mathbb E Z^2
 =q^{-k}\sum_{S\subseteq V}(q-1)^{k-|S|}
       q^{(2/3)e(S)}.
 }
\]
The \(S=V\) contribution is exactly \(1\), corresponding to identical assignments. The \(S=\varnothing\) contribution is \((1-1/q)^k\).

For \(s=|S|\le k/2\), cubic regularity and edge expansion give
\[
 e(S)=\frac{3s-|\delta(S)|}{2}
 \le (3/2-\gamma/2)s,
\quad\text{hence}\quad
 q^{-s+(2/3)e(S)}\le q^{-\gamma s/3}.
\]
For \(s>k/2\), put \(T=V\setminus S\), \(t=|T|\). The identity \(e(S)=m-3t+e(T)\) gives the same upper bound \(q^{-\gamma t/3}\). Consequently the sum of contributions of all nonempty proper agreement sets obeys
\[
 B_2^\star
 \le 2\sum_{t=1}^{\lfloor k/2\rfloor}\binom{k}{t}q^{-\gamma t/3}
 \le 2\bigl((1+q^{-\gamma/3})^k-1\bigr).
\]
If \(kq^{-\gamma/3}\to0\), e.g. \(q=\lceil k^c\rceil\) with \(c>3/\gamma\), then \(B_2^\star=o(1)\), \((1-1/q)^k=1-o(1)\), and \(\mathbb E Z^2=2+o(1)\).

## 3. Full Poisson(1) limit by dependency graphs (not just the second moment)

For each assignment \(\sigma\), let \(I_\sigma\) indicate that it satisfies all \(m\) constraints. The independent coordinates are the membership bits \(\mathbf1[(a,b)\in R_e]\), over all table entries \(e,a,b\).

Define a dependency neighborhood \(N(\sigma)\) to contain every \(\tau\) such that **at least one original edge has identical ordered label pairs under \(\sigma,\tau\)**. Equivalently, \(e(S)>0\). Outside this neighborhood, the underlying table entries used by \(I_\sigma\) and by the entire family of other indicators are disjoint, so the required dependency-graph condition holds and \(B_3=0\).

The mean is \(\lambda=\mathbb E Z=1\). The usual Arratia–Goldstein–Gordon parameters are
\[
 B_1=\sum_\sigma\sum_{\tau\in N(\sigma)}
       \mathbb E I_\sigma\,\mathbb E I_\tau
 \le \Pr_{\sigma,\tau\text{ uniform}}[e(S)>0]
 \le m/q^2
\]
by a union bound over edges. The second parameter, with \(\tau\ne\sigma\), is
\[
 B_2=\sum_\sigma\sum_{\tau\in N(\sigma)\setminus\{\sigma\}}
       \mathbb E[I_\sigma I_\tau]
 \le B_2^\star
 \le 2\bigl((1+q^{-\gamma/3})^k-1\bigr).
\]
The dependency-graph form of the Chen–Stein bound therefore implies
\[
 \boxed{
 d_{\rm TV}(\mathcal L(Z),\mathrm{Poisson}(1))
 \le O\left(\frac{k}{q^2}
         +(1+q^{-\gamma/3})^k-1\right)=o(1).
 }
\]
This argument makes no unproved independence assumption about overlapping CSP assignments.

**Corollary:** under \(q=k^c,\ c>3/\gamma\),
\[
 \Pr[\Gamma\text{ is UNSAT}]=\Pr[Z=0]\to e^{-1},
\qquad
 \Pr[\Gamma\text{ is SAT}]\to 1-e^{-1}.
\]
So this one explicit distribution on a fixed bounded-degree expander has a **constant density of both YES and NO instances**.

**Source of the approximation theorem:** Arratia, Goldstein, Gordon, *Poisson Approximation and the Chen–Stein Method*, 1989/1990; accessible https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/pacs-1.pdf . The original probabilistic estimates in this note are self-contained; the distributional limit invokes this standard theorem. Publication priority/novelty of this elementary application has not been checked.

## 4. Arc consistency fails almost surely

For a fixed edge \(uv\) and a fixed value \(a\in[q]\) of endpoint \(u\), the chance that no neighbor value \(b\in[q]\) supports \((u=a)\) is
\[
 (1-p)^q\le e^{-pq}=e^{-q^{1/3}}.
\]
The same holds for every column. Union bounding over both endpoints of all \(m\) constraints and all \(q\) values,
\[
 \Pr[\text{some domain value lacks support on some incident edge}]
 \le 2mq\,e^{-q^{1/3}}=o(1)
\]
for any fixed positive polynomial growth \(q=k^c\). Hence *with high probability every value initially has support along every edge*, so ordinary arc consistency removes nothing.

Combining with the Poisson theorem, asymptotically \(\approx e^{-1}\) of the random instances are **UNSAT despite perfect local arc consistency**. This is an actual algorithmic lower-bound counterexample only for this very restricted propagation routine, not for more sophisticated algorithms.

## 5. Candidate source of hardness, and explicit warning

A possible **distributional hypothesis** \(\mathrm{Critical\text{-}Expander\text{-}CSP}_{\sqrt{\log}}\), separate from and stronger than a corresponding worst-case hypothesis, would claim that no uniform randomized \(q^{o(k/\sqrt{\log k})}\operatorname{poly}(L)\)-time algorithm decides this balanced distribution with error at most 0.1. The parameters must fix an explicit **bipartite** cubic expander family, \(\gamma\), and a fixed \(c>3/\gamma\); the algorithm may depend on these choices but not on the random relation tables. The hypothesis is **OPEN and speculative**, not a theorem or evidence by itself.

If such average-case hardness were true, the unconditional reduction in Theorem 4.2 of Braulov–Chukhin–Kulikov–Mihajlin's HOM paper (https://arxiv.org/abs/2607.09377) would in particular forbid a worst-case \(2^{O(n)}\operatorname{poly}\) algorithm for polynomial-target 2-degenerate HOM. This is because a universally correct fast HOM solver composed with that polynomial-time reduction would solve the random source on every instance. Random-instance behavior is not automatically transported as *average-case hardness of the HOM output distribution*, and the reduction's parameters must be applied correctly.

The Poisson and local-consistency results **do not** establish computational hardness: a different algorithm might decide these random CSPs efficiently. The 2026 claimed tensor algorithm already gives \(q^{O(k/\sqrt{\log k})}\), which is compatible with the proposed lower scale.

### Concrete research test

Find an explicit polynomial-time or \(q^{o(k/\sqrt{\log k})}\) exact decision method for this distribution (e.g. a global spectral/coding/rank certificate), OR establish a restricted-model lower bound for fixed-radius constraint propagation or bounded-degree local polynomial statistics. Do not extrapolate to full average-case hardness without a reduction/proof.
