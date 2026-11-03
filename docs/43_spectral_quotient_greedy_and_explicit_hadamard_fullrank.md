# Spectral greedy lifting and explicitly recoverable full-rank pseudorandom CSP blocks

**Date:** 2026-11-03. **Status:** UNCONDITIONAL elementary spectral greedy algorithm, an exact SAT-iff quotient lemma, and an EXPLICIT binary matrix construction with a full-rank dense spectrum and polynomial-time recovery of hidden 3-color labels. No generic $q^{o(k)}$ algorithm for arbitrary critical-density CSP is claimed. Novelty relative to blow-up/embedding lemmas and pseudorandom CSP algorithms has NOT been independently established. Follows [robust quotients](42_robust_alphabet_quotients_fullrank_dense_csp.md).

## 1. Spectral lifting theorem for arbitrary deterministic relation tables

Let $\Gamma$ be a binary CSP of maximal degree $\Delta$. For each original variable $v$, let its domain be partitioned into classes $C_{v,i}$, each of size $L$. Let $S_e$ be a coarse relation on class labels such that FORBIDDEN coarse rectangles contain no allowed fine pairs. For every ALLOWED coarse pair of edge $e=uv$, write $M_{e,i,j}$ for the $L\times L$ 0/1 submatrix of allowed fine pairs.

Suppose there are $0<\rho<1$ and $\lambda\ge0$ such that for EVERY allowed rectangle,
\[
\|M_{e,i,j}-\rho J_L\|_{\mathrm{op}}\le\lambda.
\tag{1}
\]
(Transpose has the same norm; no randomness or independence is assumed.)

**Spectral greedy-lifting theorem.** If
\[
\boxed{L^2(\rho/2)^{2\Delta}>4\Delta\lambda^2/\rho^2,}
\tag{2}
\]
then EVERY satisfying coarse assignment lifts to a satisfying fine assignment in deterministic polynomial time. Hence the original CSP is satisfiable iff the coarse CSP is satisfiable.

**Proof.** Fix any coarse satisfying assignment and restrict each variable to its selected fine class. For a candidate set $S\subseteq[L]$ on one end of an allowed rectangle $M$, put $E=M-\rho J$. By the operator bound,
\[
\sum_{a\in[L]}\bigl(|N_M(a)\cap S|-\rho|S|\bigr)^2
=\|E{\bf1}_S\|_2^2\le\lambda^2|S|.
\]
Therefore at most
\[
\frac{4\lambda^2}{\rho^2|S|}
\tag{3}
\]
values $a$ have $|N_M(a)\cap S|<(\rho/2)|S|$. The same estimate holds using columns.

Maintain the current candidate list $S_v$ for every unassigned vertex, initially the entire selected class. Visit vertices in any order. If all previous choices preserved the property that every neighbor's list shrank by at most a factor $\rho/2$, then every unassigned list has size at least
\[
s_\star=L(\rho/2)^\Delta.
\]
When choosing $v$, each unassigned neighbor $w$ forbids at most $4\lambda^2/(\rho^2s_\star)$ values in the FULL class of $v$, by (3). Across at most $\Delta$ neighbors the total forbidden set has size at most $4\Delta\lambda^2/(\rho^2s_\star) <s_\star\le|S_v|$, by (2). Thus some $a\in S_v$ is simultaneously good for all remaining neighbors. Choose it, intersect neighbors' lists with their incident compatible values, and continue. This preserves the invariant and satisfies already processed edges. QED.

**Important:** the input is a *certificate*, not an oracle promise: given partitions and coarse relations, verify all forbidden rectangles are zero, all allowed matrices satisfy (1), and inequality (2) holds. For rational $\rho,\lambda^2$ the operator bound can be certified in polynomial bit complexity by exact rational PSD testing of $\lambda^2I-(M-\rho J)^T(M-\rho J)$, or by sufficiently precise eigenvalue approximations with slack. Then solve coarse CSP in $\prod_vr_v$ time and lift greedily in polynomial time. The algorithm is sound on all inputs for which certification succeeds; otherwise fall back to a general exact solver.

**In particular:** when $L$ is polynomial in $k$, $\rho$ is an absolute positive constant, $\lambda=C\sqrt L$ for constant $C$, and $\Delta=o(\log L)$, (2) holds for all sufficiently large $k$. So a spectrally quasirandom dense binary CSP with just ONE class per variable is automatically SAT and greedily solvable in polynomial time. With $r=k^{o(1)}$ coarse labels, the certified algorithm is $r^k\operatorname{poly}(|I|)=q^{o(k)}\operatorname{poly}(|I|)$ for polynomial $q$.

## 2. Explicit full-rank 0/1 matrix of density approximately 3/4 with optimal spectral scale

Let $t\ge1$, $L=2^{2t}$, and $W=\mathbb F_2^{2t}$. Choose an explicit invertible linear map $T:W\to W$ such that
\[
T^2+T+I=0.
\]
For instance use diagonal $2\times2$ blocks $T_2=\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)$. In particular $T^3=I$, $T+I=T^2$, and $T$ has no nonzero fixed vector.

Index rows and columns by $a,b\in W$. Define
\[
\boxed{M_{a,b}=1-[\,a\cdot b=1\text{ AND }a\cdot(Tb)=1\,].}
\tag{4}
\]
The zero row/column supports (where $M$ vanishes) have size zero when $a=0$ and exactly $L/4$ otherwise, because $a$ and $T^Ta$ are linearly independent for nonzero $a$ (likewise for columns). Hence every row and column has at least $3L/4$ ones; every pair of rows or columns has Hamming distance at most $L/2$ (their zero sets each have size at most $L/4$).

Let $H_{a,b}=(-1)^{a\cdot b}$ be Walsh–Hadamard, let $P e_b=e_{Tb}$ be the permutation matrix, and put $Q=I+P-P^2$. Then
\[
4M=3J+HQ.
\tag{5}
\]
Since $P^3=I$, its complex eigenvalues are in $\{1,\omega,\omega^2\}$ with $\omega^3=1$. Consequently eigenvalues of the normal matrix $Q$ are $1,1+i\sqrt3,1-i\sqrt3$ (on whichever eigenspaces occur), so $Q$ is invertible, $\|Q\|_{\rm op}\le2$, and
\[
\boxed{\|M-\tfrac34J\|_{\rm op}
 =\tfrac14\|HQ\|_{\rm op}\le\tfrac12\sqrt L.}
\tag{6}
\]
(Using $3\sqrt L/4$ instead is an easier but weaker bound.)

**Full rational rank.** Since $H^{-1}J=e_0{\bf1}^T$, we have
\[
4M=H(Q+3e_0{\bf1}^T).
\]
Because $Qe_0=e_0$ and $Q$ is invertible, the matrix determinant lemma gives
\[
\det(Q+3e_0{\bf1}^T)
=\det Q(1+3{\bf1}^TQ^{-1}e_0)=4\det Q\ne0.
\]
Thus $\operatorname{rank}_{\mathbb Q}M=L$. All claims are explicit and elementary, no random matrix invertibility theorem is needed.

**Independent finite-case sanity checks:** direct numerical construction for $L=4,16,64$ confirms rank $L$, norm $\sqrt L/2$, row and column degrees in $\{3L/4,L\}$, and maximum row Hamming distance $L/2$.

## 3. Hidden-3-coloring example: full rank and Theta(q) choices per row

Fix $q=3L$. For each constraint edge $e=uv$, start with
\[
R_e=(J_3-I_3)\otimes M,
\tag{7}
\]
and optionally independently permute fine labels on rows/columns at each **edge incidence**, without crossing the three coarse classes. Further arbitrarily permute the entire fine domain of each vertex once, hiding the three classes. These permutations preserve the properties used below.

The coarse relation on three labels is exactly inequality, so $\Gamma_{\rm coarse}$ is ordinary graph **3-COLORING**. Each full $R_e$ has rational rank
\[
\operatorname{rank}R_e=\operatorname{rank}(J_3-I_3)\operatorname{rank}(M)=3L=q.
\]
Every row and column has at least $2(3L/4)=3L/2=\Theta(q)$ allowed partners, so neither the low-rank nor sparse-partner algorithms of [note 36](36_rank_dual_critical_csp.md) explain the solution.

Every allowed $L\times L$ block satisfies (1) with $\rho=3/4$ and $\lambda=\sqrt L/2$. Formula (2) is met whenever
\[
L(3/8)^{2\Delta}>\frac{16\Delta}{9},
\tag{8}
\]
so certainly if $L\ge 4\Delta(8/3)^{2\Delta}$. For $L=k^{\Theta(1)}$ and $\Delta=o(\log k)$, it holds asymptotically. Hence **SAT of fine CSP iff 3-COLORING of its primal graph**, even after all allowed incidence-wise fine permutations.

## 4. Recover hidden class partition in deterministic polynomial time

For any non-isolated vertex v, select ONE incident edge e. Orient R_e as a matrix whose rows are the q fine values of v (transpose if v is the second endpoint). Compare rows by Hamming distance D.

**Same hidden coarse class:** two rows occupy the SAME two allowed opposite-class blocks. In each block their M-rows differ at most L/2 coordinates (permutations do not change this upper bound); the forbidden block contributes zero. Thus D<=L.

**Different hidden coarse classes:** there are TWO opposite coarse-class blocks on which exactly one of the rows has allowed entries, and each allowed M-row contains at least 3L/4 ones. Hence D>=3L/2, independent of fine permutations.

Therefore, with $q=3L$ and **no knowledge of the hidden bijections**, the test
\[
\boxed{a\sim_v a'\iff D(a,a')<5L/4}
\tag{9}
\]
recovers the three classes exactly. On vertices of degree zero the domain is unconstrained, and the variable can be handled separately. The row distances can be tabulated in at most $O(kq^3)$ ordinary operations (or fewer with bitsets). Build coarse relations from the recovered classes, verify spectral, forbidden-block and inequality certificates, solve the resulting three-label CSP in $3^k$, then greedily lift. This gives an *unconditional* solver for this explicitly recognizable class in
\[
\boxed{3^k\operatorname{poly}(|I|)+\operatorname{poly}(|I|)}.
\tag{10}
\]
Because $q=k^c$ and $3^k=q^{o(k)}$, this is a sub-$q^k$ solver.

**Recognition on arbitrary input:** the distance-based relation is not necessarily transitive or may produce wrong class sizes. The algorithm must reject failed partitions and **independently check** every coarse/allowed/forbidden spectral certificate before trusting an output. If certification fails, fall back to an always-correct general solver. Thus no false-positive correctness claim is made for malformed inputs.

## 5. What is actually new to our research program, and what remains open

- The earlier *near-complete allowed rectangles* hypothesis can be replaced by the much weaker *spectral quasirandomness* condition (1). Constant 1/4 of pairs may be forbidden in a typical allowed block.
- The construction provides explicit, **full-rank** and **dense** relations whose low-alphabet quotient is recoverable by polynomial-time row signatures even after adversarially hidden class labels, and after edge-incidence coordinate permutations.
- The proof never invokes Nguyen's externally claimed counting recursion. It is an unconditional SAT algorithm **on a special promised/certified class**, not a solution for every critical-density CSP.
- The spectral condition alone does not imply that one can efficiently *find* arbitrary latent coarse partitions. We solve the explicit Hamming-gap subclass. The special explicit construction and more general certified spectral quotient algorithm are separate results.
- For arbitrary full-rank relation tables without spectral structure the critical-density conjecture and HOM implications remain open. Neither full rank nor dense allowed-partner rows guarantees a hard instance.

**Related results:** Spectral expander mixing and greedy embedding, superregular pairs/blow-up-lemma methodology, and classical dense graph CSP/graph homomorphism ideas. Novelty beyond the elementary argument was not audited. Previous notes [40](40_nguyen_grouping_overhead_and_random_csp_greedy.md) (random dense relations) and [42](42_robust_alphabet_quotients_fullrank_dense_csp.md) (near-complete quotient).


## 6. Critical-density random-table threshold is outside the robust-lifting regime

This is a sharp **limitation of the method**, not a universal CSP lower bound.

Let the constraint graph have average degree $d=\sqrt{\log k}$ and let the random independent relation density be $\rho_\star=q^{-2/d}$, the first-moment satisfiability scale for $m\approx kd/2$ (see [note 40](40_nguyen_grouping_overhead_and_random_csp_greedy.md)). At a vertex with exactly $d$ neighbors, for any fixed assignment of those neighbors, the number of compatible values is binomial with mean
\[
q\rho_\star^d=q\cdot q^{-2}=q^{-1}.
\]
By Markov's inequality, with probability at least $1-q^{-1}$ **no compatible value exists for that fixed neighbor assignment**. Thus the extremely strong property that *every* permitted coarse assignment lifts by local greedy choices is not realistic at the random satisfiability threshold.

In fact, even before checking the spectral certificate, if a coarse quotient has only one class per vertex (so every coarse assignment is trivially allowed), a dense CSP sampled at $\rho_\star$ generally violates the universal neighbor-extension property. The spectral greedy method is therefore an excellent tractability criterion for robust constant-density pseudorandom CSPs, but not a route to a universal near-threshold $q^{o(k)}$ CSP algorithm without a qualitatively different global argument.

**More verification:** Direct exact-integer calculations for the explicit $M$ at $L=4,16$ yield nonzero determinants $1,4096$ respectively. Numerical ranks were checked at $L=4,16,64$. These computations are sanity checks; the symbolic determinant argument in §2 is the proof.
