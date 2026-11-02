# Exact matching compiler subprogram — detailed research log

**2026-11-01/02, reconstructed from the CEH conversation.** This is an archival research log, not a collection of verified new theorems. The parent problem is [README.md](README.md); the compiler studied here is **strictly stronger** than the satisfiability-only sparse-CSP → fixed-expander reduction we actually need. See [03_audit_and_next_steps.md](03_audit_and_next_steps.md) for pending checks and possible flaws.

## A. The strong compiler problem and elementary routing

Let $F_K$ be a predetermined cubic expander (in later specializations (F_K=C_K\cup N), a Hamiltonian cycle plus a fixed matching). Given an arbitrary perfect matching $M$ on its labeled vertices, construct explicit local relations on $F_K$, each vertex having boundedly many $q$-valued coordinates. Two public coordinates are $a_v,b_v$.

**Exact-projection requirement (strong):**
$$
\{(a,b):\exists z\ \text{all local constraints hold}\}
=
\{(a,b):b_v=a_{M(v)}\ \forall v\}.
\tag{EC}
$$
Completeness is **for every** $a\in[q]^K$. It is not enough for a random input or for a fingerprint to work for a fixed predetermined witness.

- Ordinary routing: send each source value to its matching partner along a path in the expander. In a bounded-degree graph a random remote matching has total source-to-sink shortest-path length $\Omega(K\log K)$, hence average congestion $\Omega(\log K)$. Standard expander multicommodity routing suggests an upper congestion $O(\log K)$ (algorithmic construction details require a source), giving local domain $q^{O(\log K)}$. For $q=K^c$ this is quasipolynomial, not polynomial. Tables of this size cannot be written in polynomial time.
- Naive global fingerprint: random polynomial identity can distinguish two **fixed** arrays with high probability but cannot soundly certify an existentially chosen pair ((a,b)) at polynomial field size. The witnesses can adapt to the chosen hash and collide.
- Information-through-cuts: if $r_M(S)$ matching pairs cross a cut, the public relation requires $2r_M(S)$ independent scalar equalities. An edge expander has (r_M(S)\le\min(|S|,|\bar S|)\le|\partial_F S|/\beta). Thus constant per-edge capacity is *not* ruled out by elementary cut expansion, despite the log routing load.
- Counting candidate structures: a fixed bounded-degree $K$-vertex support with $C$ field coordinates per vertex and local linear edge relations can represent at most $q^{O(C^2K)}$ distinct such systems. There are $(K-1)!!=2^{\Theta(K\log K)}$ matchings. Hence **if every matching is realizable**, necessarily $C^2\log q=\Omega(\log K)$. This obstructs constant $C$ over a fixed small field, but does not obstruct $q=K^{\Theta(1)}$.

## B. Linear compiler equations

Write all linear local constraints as
$$
A_aa+A_bb+A_zz=0.
$$
Every scalar row touches coordinates of one vertex or two adjacent vertices of $F_K$. Set $x=(a,b)$ and $L_M=(-P_M\ \ I)$, so $L_Mx=0$ iff $b=P_Ma$ (watch the index convention and involution of (M)).

A necessary-and-sufficient criterion for exact projection is:
$$
\operatorname{im}(A_a+A_bP_M)\subseteq\operatorname{im}(A_z),\qquad
\operatorname{rank}[A_z\ A_b]-\operatorname{rank}A_z=K.
\tag{B1}
$$
To see it, quotient the row-equation space by $\operatorname{im}A_z$: the first relation makes the first public coefficient matrix equal to the second times $-P_M$, and the second makes the remaining $K$ output constraints independent.

Alternatively, after choosing a basis of $\ker A_z$ and adding local gauge-fixing $z_v=0$ constraints at selected auxiliary coordinates, the auxiliary solution can be made unique for each legal $a$, without changing public projection. This is a standard linear-algebra observation *for the particular coordinate-local gauge operation*; its use in longer no-go arguments needs re-checking.

### Symmetric quadratic / Schur-complement normal form

If $A_z$ is full column rank, choose generic diagonal weights $W$ (over a sufficiently large field) and form $Q=A^\top WA$. Since each original row is local, $Q$ has only on-vertex and original-edge blocks. With suitable $W$, $\ker Q=\ker A$ and its auxiliary principal block $C=A_z^\top WA_z$ is nonsingular. This gives an effective symmetric Schur complement
$$
S=D-BC^{-1}B^\top,\quad
\ker S=\ker L_M.
$$
The earlier stronger requirement $S=L_M^\top L_M$ is **unnecessary**; the right invariant is the kernel. Equivalently,
$$
S=L_M^\top T_ML_M
\tag{B2}
$$
for some invertible symmetric $T_M\in\mathbb F_q^{K\times K}$. The Schur complement may therefore be dense. Generic-field and characteristic hypotheses of the normalization should be checked in a standalone proof.

A restricted negative attempt: if (B,D) are vertex-block-diagonal, the matching has no edges of $F_K$, and $d\le2$ auxiliary coordinates per vertex, the exact target $S=L_M^\top L_M$ is incompatible with the support of $C$. This is a barrier **only for that restricted exact-S, block-local coupling**, not the general normal form (B2).

### Quotient/subspace version

Let $\pi:\mathbb F_q^r\to\mathbb F_q^r/\operatorname{im}A_z=:V$ and let $H_v$ be the coordinate subspace on checks involving vertex $v$. Put $U_v=\pi(H_v)$. The conversation proposed that for a matched pair (vw), two independent common directions in $U_v\cap U_w$, with all chosen pair-directions jointly independent, characterize the public coefficients (two directed public equalities per undirected matched pair). The stated intuition is valid: matching outputs have to agree as *classes of local equation vectors*. **Audit required:** the original chat claimed a *surjection* from $\ker A_z^{-(v,w)}$ onto $U_v\cap U_w$ after deleting checks incident to (v,w); that surjectivity and the exact dimensional inequality require a careful quotient and gauge analysis.

In the balanced test $d=2$ auxiliary coordinates at each vertex, two scalar checks per expander edge give $r=3K$, $A_z$ has $2K$ columns, $\dim V=K$ if full rank. Chat derived a punctured-rank necessary condition $\operatorname{nullity}(A_z^{-(v,w)})\ge2$ on each remote matched pair and observed generic random local matrices fail it. These are **audit targets**, not a certified impossibility result.

## C. Low-dimensional transfer / network-coding attempts

### Invertible transfers

One special architecture chooses $z_v\in\mathbb F_q^d$ and imposes
$$
z_v=T_{uv}z_u+B_{uv}(a_u,b_u,a_v,b_v),\qquad T_{uv}\in GL_d(\mathbb F_q)
\tag{C1}
$$
on every graph edge. For homogeneous public input these define a flat section / monodromy representation.

The conversation proposed a no-go bound
$$
K\le2+4dD
\tag{C2}
$$
for a remote matching in a 3-vertex-connected graph of diameter $D=O(\log K)$: use a BFS tree, select at most $d$ fundamental-cycle conditions that define the space of parallel sections, cover them by a core $W$ of at most (1+2dD) vertices, pick a matched pair outside $W$, subtract a global homogeneous section, and separate the two local stars. If valid under all hypotheses, (C2) forces $d=\Omega(K/\log K)$ *for this invertible-transfer model*. The generalization to arbitrary extra linear checks satisfying full-state invertible transfer also needs formal scrutiny.

This does **not** rule out partial, singular, or nondeterministic linear relations on edges: ordinary routing transports subsets of a state, not an invertible transfer of the whole state.

### Ordinary and twisted gradients

Specialize (C1) to scalar or repeated potential layers: (z_v-z_u=\omega_{uv}(\text{public endpoint values})). If $F-\{v,w\}$ stays connected and $vw\notin E(F)$, a purported separated-support argument says all local right-hand-side coefficients compatible with $b=P_Ma$ lie in the gradient image individually; the system then imposes no matching relation. A twisted variant $z_v-\lambda_{uv}z_u=\omega_{uv}$, with $\lambda\ne0$, was argued to need $\Omega(K/\log K)$ layers. These should be kept as **claims with proofs to audit**.

## D. Stronger nonlinear separator bounds (public ports fixed)

The simplest generally sound tool here is a gluing lemma. Let $S\subseteq V(F_K)$, let $B=\{v\in S:\exists w\notin S, vw\in E(F_K)\}$ be its *inner vertex boundary*. Choose $M$ matching each vertex of $S$ to a different vertex outside $S$ $possible when (|S|\le K/2)$. Every matched pair crossing the cut imposes two scalar equalities between otherwise independent public coordinates. With public ports fixed at the original vertices and full local alphabet at most $q^C$, gluing two local satisfying assignments with the same boundary state gives the **necessary capacity**
$$
q^{2|S|}\le q^{C|B|},
\quad\text{i.e.}\quad C\ge\frac{2|S|}{|B|}.
\tag{D1}
$$
This works for nonlinear local relations too, but only for this strong *fixed-port exact relation realization*. A construction with public variables moved, extra graph vertices, or preservation of only YES/NO need not satisfy it.

The chat argued that a cubic graph containing a connected $O(\log K)$-vertex subgraph $S_0$ with at least two independent cycles yields $S=N[S_0]$ with $2|B_F(S)|<|S|$, whence $C\ge5$. More precisely, if $|S_0|=s$, $|E(F[S_0])|\ge s+1$, then $|\partial_E S_0|\le s-2$; writing $t=|N(S_0)\setminus S_0|\le s-2$, we get $|B_F(N[S_0])|\le t$ and $2(s+t)>4t$. The existence of a suitable small 2-cycle core and the quantifiers on $F_K,M$ should be verified.

An edge-cut analogue says that if an edge carries at most $r_e$ independent scalar linear equations, then
$$
2|M\cap\partial S|\le\sum_{e\in\partial_F S}r_e.
\tag{D2}
$$
This is a rank-separation consequence for exact linear public matching. It does **not** apply to arbitrary nonlinear constraints by simply counting equations.

## E. Local-subspace/sheaf model

After removing auxiliary gauge freedoms, every legal full local state is a linear function of public $a\in\mathbb F_q^K$: $x_v=T_va$. Let its row space be
$$
W_v\le\mathbb F_q^K,\qquad
P_v=\operatorname{span}(e_v,e_{M(v)})\subseteq W_v,\quad\dim W_v\le C.
$$
For each edge $e=uv\in E(F_K)$, let $I_e=W_u\cap W_v$. Put
$$
\partial:\bigoplus_{uv\in E(F_K)} I_{uv}\longrightarrow
\bigoplus_{v\in V(F_K)}W_v
$$
with (+s,-s) at the endpoints, and let $phi:\bigoplus_v W_v\to\mathbb F_q^K$ \sum coordinates.

The proposed exactness criterion is
$$
\operatorname{im}\partial=\ker\phi.
\tag{E1}
$$
Interpretation: all linear dependences among local forms are generated by edgewise shared-form agreements. Subject to the gauge-fixing/locality argument, (E1) is the correct kernel/rank target of this *subspace realization approach*. It should not be silently treated as a general fact about nonlinear decision-preserving reductions.

### Immediate dimension inequalities

Because $e_vin W_v$, (phi) is surjective, so
$$
\dim\ker\phi=\sum_v\dim W_v-K.
$$
Therefore a necessary consequence of (E1) is
$$
\sum_{e\in E(F_K)}\dim I_e\ge\sum_v\dim W_v-K.
\tag{E2}
$$
For a connected $S$ containing no complete $M$-pair, all (2|S|) public basis vectors from its vertices are independent. Adding $W_v$'s along a spanning tree $T$ gives
$$
2|S|\le\dim\sum_{v\in S}W_v
\le C+\sum_{e\in T}(C-\dim I_e),
$$
and hence
$$
\sum_{e\in T}\big(\dim I_e-(C-2)\big)\le C-2.
\tag{E3}
$$
These dimension calculations are elementary once the $W_v$ model is fixed.

For every cut $S$, (E1) was used to derive an intended identity
$$
\Big(\sum_{v\in S}W_v\Big)\cap
\Big(\sum_{v\notin S}W_v\Big)
=
\sum_{e\in\partial_F S}I_e,
\tag{E4}
$$
and hence $2|M\cap\partial S|\le\sum_{e\in\partial_F S}\dim I_e$. **Audit the equality (E4)**: it depends on the precise chain complex and the images from internal edges; do not use it without checking.

### Influence-connectivity / dense mixing

For each source symbol $a_i$, let $S_i=\{v:T_ve_i\ne0\}$. Gluing whole connected components of $F[S_i]$ implies (i,M(i)) must lie in the same component of $F[S_i]$. Thus $|S_i|\ge\operatorname{dist}_F(i,M(i))+1$. For a remote matching, summing yields
$$
\sum_v\operatorname{nnz}(T_v)=\sum_i|S_i|=\Omega(K\log K).
\tag{E5}
$$
Therefore local linear forms must *mix many original symbols* if $C$ is constant; it rules out sparse literal-copying, not dense linear forms.

### The special $C=5$ program

The chat tested $\dim W_v=5$, publicly required $P_v\subset W_v$, and initial uniform edge intersections $\dim I_e=3$. That would need $\operatorname{rank}\partial=4K$ and an edge-domain dimension (9K/2), i.e. (K/2) kernel dimensions.

* Naive shared 3D global fingerprint: $W_v=P_v+Z$, with one common $Z$ for all vertices. It has large local intersections but does not enforce the matching: along a connected graph only a common 3-vector is glued, leaving too many degrees of freedom.
* If every 3D interface $I_{uv}$ meets both endpoint public 2-spaces trivially, it acts as an invertible $GL_3$ transfer on the auxiliary coordinates, so the invertible-transfer obstacle applies. A hypothetical successful $C=5$ realization must use singular interfaces somewhere, assuming the no-go proof is sound.
* With $S_0$ as in (D1), one common fingerprint value across the boundary $B_F(N[S_0])$ gives a stronger counting contradiction. The conversation recorded the condition $\bigcap_{v\in B}W_v=\{0\}$ for the adversarial matching, but the argument requires carefully accounting for rank and fiber sizes when fixing a common function $f(a)$.
* In a connected matched-pair-free subset $S$, $\dim\sum_{v\in S}W_v=2|S|+\varepsilon(S)$ with $0\le\varepsilon(S)\le3$. Adding a new vertex connected to two previous vertices by *distinct* 3D interfaces decreases $\varepsilon$ at least 1. This is a local dimension-budget constraint, not a no-go proof for every $C=5$ interface arrangement.

### Mixed profile on a Hamiltonian expander

Specialize $F_K=C_K\cup N$. The attempted profile was $dim I_e=3$ on cycle edges, 2 on fixed-matching edges. Then
$$
\sum_e\dim I_e=3K+2(K/2)=4K,
$$
so exactness (E1) would force **injectivity** of $\partial$, rather than producing (K/2) dependencies. For $M=N$ an explicit toy example was proposed:
$$
W_v=\operatorname{span}(e_v,e_{N(v)},e_{v-1},e_{v-2},e_{v-3}),
\tag{E6}
$$
assuming the $N$ endpoints are sufficiently separated along the cycle. For a coordinate $e_i$, the set of vertices containing it forms a path plus one $N$-edge, so edgewise equalities are independent. This *does not handle arbitrary $M$*, and a common global basis change cannot generally make the public coordinates $e_v,e_{M(v)}$ appear in the correct places.

Its matrix implementation uses invertible 3D transitions $z_{v+1}=T_vz_v+U_vp_v+V_vp_{v+1}$ on the cycle, giving $Sz=Bp$, and two linear checks on each edge of $N$, giving the exact condition
$$
\operatorname{rowspan}(C_p+C_zS^{-1}B)
=
\operatorname{rowspan}(-P_M\ I).
\tag{E7}
$$
This *architecture* is restricted to 3 checks per cycle edge and 2 per $N$-edge. The edge-cut capacity (D2) shows failure when a cycle interval contains several internal $N$-edges and $M$ crosses that interval completely: if the interval has $s$ vertices and $t$ internal $N$-edges, $|\partial_N S|=s-2t$, so $2s\le2d+2(s-2t)$ implies $d\ge2t$. With $d=3$, even $t\ge2$ is fatal. This removes (E7) as a universal route under that check budget.

The chat then proposed sharper combinatorial bounds on $C=5$ intersection profiles:
- Periodic-cut lemma yielding $|\partial_N S|\le(3/5)|S|+O(1)$ for a half-size union of at most four cycle intervals; **verify the claimed piecewise-linear inequality before reuse**.
- Uniform $dim I_e\le3$ on $N$: argued impossible for some distant $M$.
- Uniform $dim I_e\ge4$ on $N$: contracting $N$ gives a 4-regular graph and a proposed vertex-separator capacity contradiction.
- Claimed every successful $C=5$ realization for an adversarial $M$ needs $\Omega(K)$ low-intersection cycle edges $(dim I_e\le2)$.
- A suggested $C=6$ homogeneous model: $\dim W_v=6$, $dim I_e=4$ for all edges, desired $\operatorname{rank}\partial=5K$, and $K$ dependencies in the $6K$-dimensional edge-domain.

**All these are restricted-model, chat-level claims, not an impossibility theorem for fixed-topology CSP or CEH.** In particular, no construction for universal $C=6$ was found, and no general no-go for constant $C$ was proved.

## F. Key lesson / stopping rule

The long $C=5$ subprogram was consuming research time without directly addressing the central goal. The strong exact-projection compiler imposes extra public ports and completeness for every $a$, which arbitrary decision-preserving reductions do not need. The tools from this subprogram should be used as **filters on proposed constructions**, not as axioms defining the only possible approach.

In future, for any purported barrier state clearly whether it applies to:
1. arbitrary satisfiability-preserving reductions;
2. exact projections with fixed public ports;
3. local linear realizations;
4. invertible transfers or chosen intersection profiles;
5. a bound on checks per edge / coordinates per vertex.

Only the first would directly threaten the equivalence program.
