# Fixed-topology sparse CSP via sorting networks: an explicit logarithmic-overhead bridge

**Research note, 2026-11-02.** Companion to [CEH checkpoint](README.md). This is a constructive, elementary adaptation of the *universal factor graphs* idea; **not claimed novel**. Status: construction and parameter audit below are mathematically elementary subject to the standard explicit $O(t\log t)$-size sorting network and explicit bounded-degree expander constructions. No $O(k)$-variable compiler is obtained.

## 1. The problem and the missing logarithm

Input $\Gamma$: $k$ variables over $[q]$, $m\le ak$ explicit binary constraints for a fixed constant $a$, with arbitrary relations $R_e\subseteq[q]^2$ and arbitrary constraint-graph topology. Goal: an **input-independent, predetermined cubic bipartite expander** $F_K$ with binary relations that depend on $\Gamma$, satisfying $\Gamma\in\mathrm{SAT}\iff\Gamma'\in\mathrm{SAT}$.

**Constructive logarithmic-overhead theorem (working proof below):**
\[
K=O_a(k\log(k+2)),\qquad Q=(kq)^{O(1)},\qquad
\Gamma\in\mathrm{SAT}\Longleftrightarrow\Gamma'\in\mathrm{SAT},
\]
with a *deterministic polynomial-time* transformation and explicitly writable output tables. For each $k$ and fixed $a$, the graph $F_K$ is independent of $\Gamma$; its construction may use a canonical padding of the network to a chosen admissible size. It may be necessary to index the family by admissible $K(k)$ and pad for arbitrary sizes.

The missing improvement for CEH $\leftrightarrow$ SPACH is $K=O(k)$, not just $O(k\log k)$.

## 2. The fixed word-level verifier

Pad to $m_0=\lceil ak\rceil$ constraints by adding tautological relations (do not change satisfiability). Create $2m_0$ **records**, two for each constraint $e=uv$:
\[
r_{e,u}=(u,a_{e,u}),\qquad r_{e,v}=(v,a_{e,v}),
\]
each in the universe $[k]\times[q]$ of size $kq$. At the fixed initial location for $e$, use the original input to restrict keys to $u,v$ and ensure
\[
(a_{e,u},a_{e,v})\in R_e.
\]
(The test is unary on a state containing both records, or is a binary relation between their states.)

Feed all $2m_0$ records through an **oblivious sorting network** ordered by the key (source variable index); tie-breaking does not matter. The comparator on records $(u,a),(v,b)$ is the deterministic function outputting these records in nondecreasing order of $u,v$.

At the fixed output positions, require
\[
\text{if adjacent sorted records have the same key, their values agree}.
\]
All these tests and all comparator interconnections have a topology independent of the source graph or source relations. Only the initial key restrictions and original $R_e$ tables depend on the instance.

**Correctness.** If $\Gamma$ has a satisfying assignment $x$, choose every incidence value $a_{e,v}=x_v$; the sorting network produces equal values in each key block. Conversely, satisfying initial constraints and final adjacent-equality checks imply all occurrences of any variable have one common value, which satisfies every original $R_e$. Isolated source variables are unconstrained and can be assigned arbitrarily.

## 3. Bounded-degree fixed graph, polynomial alphabet

Use a uniform AKS-type sorting network on $t=2m_0$ records with $O(t\log t)$ comparators and $O(\log t)$ depth. Represent its *whole wire-level verification DAG* as a CSP with one state for each wire occurrence at each layer and one state for each comparator. A comparator state stores four records (two inputs, two outputs), so its alphabet has size at most $(kq)^4$; a unary restriction enforces comparator correctness. A wire-state stores one record; fixed binary equality tests identify the four comparator ports with appropriate neighboring wire-states. Input-pair relation checks and output-adjacent consistency checks contribute only $O(t)$ local constraints.

Thus the skeleton graph $H_t$ has
\[
|V(H_t)|=O(t\log t),\quad |E(H_t)|=O(t\log t),\quad
\Delta(H_t)=O(1).
\]
Its **topology depends only on $t$**, not the assignment of source constraint endpoints. All local alphabets embed into a uniform $Q=(kq)^4$-symbol alphabet; unary restrictions can be absorbed into incident binary relations. All relations have explicitly enumerable polynomial-size truth tables (at most $Q^2$ pairs each), as $q=k^{O(1)}$.

**Technical normalization:** overlay on the same $|V(H_t)|$ base vertices a predetermined cubic expander $X_t$ whose edges carry tautological relations. If needed add dummy base vertices to make the order admissible. Complete the bounded-degree base multigraph $H_t\cup X_t$ (parallel base edges allowed) to an even $D$-regular loopless multigraph for some fixed even $D>\Delta(H_t)+3$. For sufficiently large order, the unused degree stubs can be paired across distinct base vertices; finitely many tiny cases can be hard-coded.

Orient the resulting even-degree graph along Euler tours, so every base vertex has $D/2$ incoming and $D/2$ outgoing edges. Replace each base vertex by an **even $D$-cycle of ports**, assign outgoing outer-edge ports to one cycle parity and incoming ports to the other, enforce equality on its cycle edges, and carry the original/expander/dummy relations on their corresponding outer edges. The result is a **simple, cubic, bipartite** graph (parallel base edges use disjoint port endpoints) with $K=D|V(H_t)|=O(t\log t)$ vertices. It depends only on $t,k,a$ and the canonical network/expander/regularization, never on the source constraint topology or its tables.

**Expansion check.** For $S$ of at most half the ports, let $A$ be base cycles entirely contained in $S$ and $P$ partially contained. Since each base cycle has $D$ ports, $|A|\le |V(H_t)|/2$. Every partial cycle contributes at least two internal cut edges, hence $|\partial S|\ge2|P|$. Expansion of the overlaid cubic expander $X_t$ yields at least $\beta|A|$ base expander edges crossing from $A$, of which at most $3|P|$ can end in partial cycles and possibly fail to cross the port cut. Thus
\[
|\partial S|\ge\max\{2|P|,\ \beta|A|-3|P|\}
\ge c_\beta(|A|+|P|)\ge (c_\beta/D)|S|,
\]
for some constant $c_\beta>0$. The output is a constant-expansion cubic bipartite graph. This is an explicit port-replacement / expander-overlay proof, not a minor argument.

## 4. Why simply optimizing this network cannot remove the logarithm

Any fixed network of $g$ two-input, two-output **switches**, each of which either keeps or swaps two indivisible records, can realize at most $2^g$ input-to-output permutations. An oblivious sorting network on $t$ distinct keys must realize all $t!$ permutations. Therefore
\[
2^g\ge t!,\qquad g\ge\log_2(t!)=\Omega(t\log t).
\]

The restriction to **literal record routing through 2-by-2 switches** is essential. This does **not** rule out fixed-topology reductions based on algebraic mixing, nonlinear existential witnesses, larger internal arity encoded inside a polynomial alphabet, or decision-only compilation of the entire conjunction.

## 5. Quantitative implication for CEH

Suppose there is an algorithm for *this predetermined cubic expander family* at polynomial alphabet $Q$ taking
\[
T(K,Q)=Q^{o(K/\log K)}\operatorname{poly}(|I|).
\]
Composing it with the construction gives arbitrary sparse polynomial-alphabet 2-CSP time
\[
Q^{o((k\log k)/\log(k\log k))}\operatorname{poly}(|I|)
=2^{o(k\log k)}\operatorname{poly}(|I|)=q^{o(k)}\operatorname{poly}(|I|).
\]
Therefore **SPACH** (if true at suitable uniformity/alphabet constants) already rules out such an algorithm for this explicit fixed cubic expander at the **$K/\log K$ scale**. This is a logarithmic-factor weaker fixed-topology hardness consequence than full CEH at scale $K$, not a proof of CEH.

The target's alphabet exponent may differ from the source one; formulate the quantifiers accordingly. Deterministic versus randomized assumptions are separate.

## 6. Relation to the literature

- Feige–Jozeph, *Universal Factor Graphs*, ICALP 2012: https://arxiv.org/abs/1204.6484 . They obtain universal factor graphs using oblivious sorting; their Boolean 3SAT Lemma 1 has $N=O(m\log m\log n)$ variables. Their "subexp-universal" notion and parameter accounting differ from the strong $q^{o(k)}$ requirement here. Our **word-alphabet reformulation** saves the extra $\log n$ factor for the sorting comparator's word computation when arbitrary polynomial-domain tables are allowed; do not call that a published new theorem without literature audit.
- Shlomo Jozeph, *Universal Factor Graphs for Every NP-Hard Boolean CSP*, RANDOM 2014: https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2014.274.
- Austrin–Brown-Cohen–Håstad, *Optimal Inapproximability with Universal Factor Graphs*, SODA 2021: https://eccc.weizmann.ac.il/eccc-reports/2019/TR19-151/ .
- AKS sorting networks: $O(t\log t)$ comparators and $O(\log t)$ depth (classic theorem).

## 7. Research focus after this checkpoint

The truly missing component is a **linear-size, fixed-topology, constant-degree, polynomial-word-alphabet verifier** for the arbitrary $O(k)$-constraint CSP, avoiding the factorial switching-network barrier by operating on **jointly encoded information** rather than literally sorting/routing individual $(\text{key},\text{value})$ records.

Avoid making the exact public matching compiler a mandatory stage. The target reduction need preserve only **SAT iff**, not all witnesses or an explicit correspondence between original variables and designated public ports. The prior linear-algebra and separator tools should be reused as sanity checks on candidate architectures, not mistaken for impossibility results.
