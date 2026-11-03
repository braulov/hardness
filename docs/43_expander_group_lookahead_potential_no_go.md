# Expander no-go for disjoint-group lookahead entropy bounds

**2026-11-02. Status: PROVED (elementary combinatorial argument), high-girth extension CONDITIONAL only on the classical Alon–Hoory–Linial irregular Moore bound (a published theorem).** No 2026 ETH/tensor algorithm is used. **Precise scope: a lower bound on the _analytic potential_ of notes 39–40, NOT a computational lower bound on actual group-lookahead DFS or on arbitrary CSP solvers.** The potential's upper-bound analysis may be grossly loose, especially when overlapping group tests are combined.

## Setup

Let \(G=(V,E)\) be a simple \(3\)-regular graph on \(k\) vertices satisfying
\[
 |\delta(X)|\ge\gamma\min(|X|,k-|X|)\qquad(X\subseteq V)
\]
for a fixed edge-expansion \(\gamma>0\). This graph is the fixed topology of the critical Bernoulli random binary CSP with alphabet \(q\), independent relation density \(p=q^{-2/3}\), as in [note 40](40_group_lookahead_boundary_entropy_and_matching.md).

Fix a prefix vertex set \(S\). For vertex-disjoint connected induced groups \(U_i\subseteq V\setminus S\) define
\[
 a_i=|E(U_i,S)|,\qquad
 b_i=|E(U_i,V\setminus(S\cup U_i))|.
\]
The local group-extension first moment is exactly \(q^{(b_i-a_i)/3}\); the product-of-independent-**disjoint**-group Markov bound for expected surviving prefixes has exponent
\[
 \Phi(S;\mathcal U)=\frac13\left(
 |\delta(S)|-\sum_i(a_i-b_i)_+\right).
\tag{1}
\]
The note-40 parameter \(\Phi_r(S)\) minimizes (1) over all disjoint **induced trees** \(U_i\) of size at most \(r\). Selection of these groups is for the *analysis*, independent of relation tables.

## Theorem A: no sublinear disjoint-tree potential, regardless of tree size

Let \(s=\lfloor k/8\rfloor\). For every \(S\subseteq V\) with \(|S|=s\) and every vertex-disjoint family \(\mathcal U\) of induced **trees of arbitrary size** in \(G[V\setminus S]\):
\[
 \boxed{\Phi(S;\mathcal U)\ge \gamma s/3.}
\tag{2}
\]
Consequently for **every** \(r\in[1,k]\) and **every** variable ordering \(\pi\),
\[
 \boxed{\max_{0\le i\le k}\Phi_r(S_i)
       \ge(\gamma/3)\lfloor k/8\rfloor
       =\gamma k/24-O_\gamma(1).}
\tag{3}
\]
In particular, the open proposal in note 40 to find an ordering with \(\max_i\Phi_{C\log k}(S_i)=o(k)\) is **refuted for cubic edge-expanders**, as a *claim about the potential*.

### Proof

Discard any group \(U_i\) with \(a_i\le b_i\), since its credit is zero. Put \(T=\bigcup_iU_i\) and \(R=V\setminus(S\cup T)\).

Because an induced tree \(U_i\) of size \(t_i\) has \(t_i-1\) internal edges, cubic degree counting gives
\[
 a_i+b_i=3t_i-2(t_i-1)=t_i+2.
\]
As \(a_i>b_i\), we have \(t_i+2<2a_i\), so \(t_i<2a_i\). Thus
\[
 |T|<2\sum_i a_i\le2|\delta(S)|
 \le6|S|.
\tag{4}
\]
(With no positive-credit groups, the same estimate holds non-strictly with \(T=\varnothing\).)
Therefore
\[
 |R|=k-s-|T|\ge k-7s\ge s,
 \quad |V\setminus R|\ge s.
\tag{5}
\]
Moreover, after discarding zero-credit groups,
\[
\begin{aligned}
 3\Phi(S;\mathcal U)
 &=|\delta(S)|-\sum_i(a_i-b_i)\\
 &=|E(S,R)|+\sum_i b_i\\
 &\ge|\delta(R)|,
\end{aligned}
\tag{6}
\]
because the second summand counts all edges from \(T\) to \(R\) (and potentially some inter-group edges). By edge expansion,
\[
 3\Phi(S;\mathcal U)\ge\gamma\min(|R|,k-|R|)\ge\gamma s.
\]
QED.

**Interpretation:** If independent tree-local checks seem to remove all frontier entropy, they must leave a substantial untested residual region \(R\), and expansion forces a linear interface from that region into the tested/assigned part.

## Theorem B: quantitative tradeoff for cyclic groups

Permit \(U_i\) to be any vertex-disjoint connected **induced** groups, and define their cyclomatic numbers
\[
 \mu_i=|E(G[U_i])|-|U_i|+1,\qquad
 \mu=\sum_i\mu_i.
\]
For \(|S|=s=\lfloor k/8\rfloor\), the same potential satisfies
\[
 \boxed{
 \Phi(S;\mathcal U)\ge
 \frac{\gamma}{3}(s-2\mu)_+.
 }
\tag{7}
\]
Thus if the analytic potential could ever be \(o(k)\) using *disjoint* connected groups at this prefix, necessarily
\[
 \boxed{\mu\ge k/16-o(k).}
\tag{8}
\]

### Proof

Again discard zero-credit groups. For any remaining connected group of order \(t_i\), its edge count is \(t_i-1+\mu_i\), so
\[
 a_i+b_i=3t_i-2(t_i-1+\mu_i)
      =t_i+2-2\mu_i.
\]
Since \(a_i>b_i\), \(t_i<2a_i+2\mu_i\). Consequently
\[
 |T|<2|\delta(S)|+2\mu\le6s+2\mu,
 \quad
 |R|\ge k-7s-2\mu\ge s-2\mu.
\]
Also \(|V\setminus R|\ge s\), and equation (6) is unchanged because it depends only on group boundaries, not on internal cycles. Therefore
\(3\Phi\ge\gamma\min(|R|,k-|R|)\ge\gamma(s-2\mu)_+\).
QED.

The linear \(\mu\)-requirement is a **necessary structural resource for this first-moment disjoint-packing proof technique**. It is NOT a lower bound on the number of cycles any actual correct CSP algorithm must inspect. In particular, multiple overlapping tests can make correlated deductions not controlled by (1).

## Theorem C: logarithmic girth blocks even cyclic O(log k)-size groups in the same potential framework

Assume in addition that the graph has girth \(g(G)\ge a\log k\) for fixed \(a>0\), and all disjoint connected induced groups have size at most \(r=C\log k\) for fixed \(C\).

Then **uniformly over all such group families**,
\[
 \boxed{\mu=\sum_i\mu_i
       =O_{a,C}\left(\frac{k\log\log k}{\log k}\right)
       =o(k).}
\tag{9}
\]
Consequently, at every prefix \(|S|=\lfloor k/8\rfloor\),
\[
 \boxed{\Phi(S;\mathcal U)\ge\gamma k/24-o(k).}
\tag{10}
\]

### Proof via the irregular Moore bound

Every cyclic group has at least \(g\) vertices, so disjointness implies at most \(k/g=O(k/\log k)\) cyclic groups. For a connected cyclic group of \(t\le C\log k\) vertices and cyclomatic number \(\mu_i\), average degree is
\[
 \bar d=\frac{2(t-1+\mu_i)}t
       =2+\frac{2(\mu_i-1)}t.
\]
The classical Alon–Hoory–Linial **irregular Moore bound** for a graph of girth at least \(g\) and average degree at least 2 gives, with \(j=\lfloor(g-1)/2\rfloor\),
\[
 t\ge(\bar d-1)^j
   =\left(1+\frac{2(\mu_i-1)}t\right)^j.
\]
Because the maximum degree is three, \(0\le 2(\mu_i-1)/t\le1\). Using \(\log(1+x)\ge x/2\) for \(x\in[0,1]\),
\[
 \mu_i\le1+\frac{t\log t}{j}
 \le 1+O_{a,C}(\log\log k).
\]
Summing over at most \(k/g\) cyclic groups gives (9); inserting (9) into Theorem B gives (10).

**External, verified source:** N. Alon, S. Hoory, N. Linial, *The Moore Bound for Irregular Graphs*, Graphs and Combinatorics **18** (2002), 53–57. https://doi.org/10.1007/s003730200002 . A freely accessible author-hosted proof: https://web.math.princeton.edu/~nalon/PDFS/ahl1.pdf .

## Generalization to fixed regular degree

For \(\Delta\ge3\) fixed, use critical relation density \(p=q^{-2/\Delta}\). The group-local extension first moment equals \(q^{(b_R-b_S)/\Delta}\), and the corresponding disjoint-group exponent is \(\Phi_\Delta=(|\delta(S)|-\sum(a_i-b_i)_+)/\Delta\).

For any induced tree group of size \(t\),
\((\Delta-2)t+2=a_i+b_i\); positive credit forces
\[
 t<\frac{2a_i}{\Delta-2}.
\]
Thus \(|T|<2\Delta |S|/(\Delta-2)\). Choosing
\[
 s=\left\lfloor\frac{\Delta-2}{4(\Delta-1)}\,k\right\rfloor
\]
ensures \(|R|\ge s\) and \(|V\setminus R|\ge s\). Therefore
\[
 \boxed{
 \Phi_\Delta(S;\mathcal U)\ge
 \frac{\gamma}{\Delta}
 \left\lfloor\frac{\Delta-2}{4(\Delta-1)}\,k\right\rfloor.
 }
\tag{11}
\]
For \(\Delta=3\), this reduces to (2).

## Overlapping tests: positive association rather than independence

There is also a useful caution from the classical **Harris–FKG inequality**. Fix a prefix assignment \(x_S\) and any two (or finitely many) possibly overlapping groups \(U_1,\dots,U_t\subseteq V\setminus S\). Each event
\[
 A_{U_i}=\{\exists\, y\in[q]^{U_i}\text{ satisfying all internal and prefix-incident constraints}\}
\]
is **increasing** in the independently sampled Bernoulli relation-table entries: changing a forbidden tuple to allowed cannot destroy a local extension. Therefore the product Bernoulli measure implies
\[
 \boxed{
 \Pr\left[\bigcap_{i=1}^{t}A_{U_i}\mid x_S\right]
 \ge\prod_{i=1}^{t}\Pr[A_{U_i}\mid x_S].
 }
\tag{12}
\]
For *disjoint* \(U_i\), the events depend on disjoint edge tables and independence holds, giving equality and the valid note-40 upper bound. For overlapping groups, the events have **nonnegative correlation**, so naively multiplying their local survival probabilities is in general **too optimistic about pruning**, not a valid upper bound on actual survival probability. This is not an impossibility proof for overlapping lookahead: joint conditions still can reject more often than any individual test, and much more refined methods are needed to analyze them.

Classical source: Harris (1960) / FKG (1971), positive association of increasing events under product measures.

## Follow-up: actual overlapping-check failure for a deliberately separated prefix

[Note 44](44_overlapping_tree_lookahead_actual_search_lower_bound_on_spaced_prefix.md) proves a stronger but **order-specific** result. On cubic high-girth expanders, choose a first prefix of size \(s\ge k/46\) whose vertices have pairwise graph distance at least five. For \(r=C\ln k<g(G)-1\) and sufficiently large polynomial alphabet, with high probability **almost every** assignment on that prefix passes *all simultaneously imposed overlapping* connected-tree checks of size \(\le r\) on **every** intermediate prefix. On a constant \(e^{-1}-o(1)\) fraction of random null inputs that are UNSAT, the real DFS with this chosen variable order explores \(q^{\Omega(k)}\) prefixes. The proof uses an explicit anchored-tree second moment, not a disjoint-group factorization. **This does not resolve the optimal-order or data-dependent-order question**, nor does it contradict any \(q^{o(k)}\) tensor algorithm.

## What is / is not closed

**CLOSED negatively:**
- the specific proposal \(\min_\pi\max_i\Phi_{C\log k}(S_i)=o(k)\) for cubic expanders, even if \(C\log k\) is replaced by unlimited tree size;
- the same disjoint-first-moment argument with connected groups of total cyclomatic number \(o(k)\);
- on logarithmic-girth expanders, the same argument allowing **arbitrary connected** groups of size \(O(\log k)\), including cyclic groups, by Theorem C.

**STILL OPEN:**
- true expected running time of the algorithm that checks **all overlapping** connected induced trees of size \(O(\log k)\): independence is lost, so the potential \(\Phi\) may be a very weak upper-bound tool;
- a stronger correlation-aware probabilistic analysis, or globally coupled algebraic/spectral tensor algorithms;
- general lower bounds against randomized polynomial-time algorithms or the \(q^{O(k/\sqrt{\log k})}\) externally claimed tensor contraction;
- the proposed worst-case and distributional SqrtLog-SPACH, which are not proved by these restricted-model results.

**Related context:** Gao–Culberson, *Consistency and Random Constraint Satisfaction Models*, JAIR 28 (2007), 517–557, studies consistency and hard random CSP models (https://new.aaai.org/Library/JAIR/Vol28/jair28-014.php). General context, not a claim that the theorem above appears there.

**Research redirect:** Do not optimize \(\Phi_r\) further on cubic expanders. To find an actual improved average-case algorithm, analyze **joint, overlapping** tests or work directly with the global centered contraction \(W(A)\); proving a new independent packing lemma cannot deliver \(q^{o(k)}\) in this framework.
