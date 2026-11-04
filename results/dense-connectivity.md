# Dense vertex-connectivity problems from exact counting

**CONDITIONAL algorithm; checked implication, unestablished novelty.** The payoff is subexponential time in the number of vertices of an unrestricted graph. The main parameter observation is that edge constraints need clauses, but no extra Boolean variable per edge. This is an application of existing parity and isolation techniques, not a new general method.

## Statement

Assume deterministic exact counting for width-at-most-four CNF on N variables and encoding length L in

\[
(L+1)^{O(1)}2^{O(N\log\log N/\sqrt{\log N})}. \tag{A}
\]

Then, on simple undirected graphs with n vertices and m edges, each of the following decision problems has an algorithm with no false YES answers, YES probability at least 2/3 on YES instances, and time

\[
\operatorname{poly}(n+m)2^{O(n\log\log n/\sqrt{\log n})}:
\]

* Connected Dominating Set of size at most k;
* Connected Vertex Cover of size at most k;
* Steiner Tree containing specified terminals and using at most k edges, with all edges of unit cost.

The parameter is n, not k or the number of terminals. Budgets can be capped at n (n−1 for a tree). Empty graphs, empty terminal sets, and conventions about empty connected covers are handled directly; below the selected set is nonempty. Logarithmic bounds are asymptotic, with constant-size inputs handled directly.

## Proof

### 1. Connectivity with n potential bits

Fix a root r. Let x_v indicate a selected vertex, require x_r=1 and \(\sum_v x_v\le k\). Introduce z_v, pin z_r=0, and impose

\[
(x_u\land x_v)\Rightarrow(z_u=z_v)\quad(uv\in E),\qquad
\neg x_v\Rightarrow z_v=0\quad(v\ne r).
\]

The first implication is the two clauses
\((\neg x_u\vee\neg x_v\vee\neg z_u\vee z_v)\) and
\((\neg x_u\vee\neg x_v\vee z_u\vee\neg z_v)\).
The second is \((x_v\vee\neg z_v)\).
For a fixed nonempty selected set S containing r, the number of z extensions is exactly

\[
2^{c(G[S])-1}.
\]

Indeed, unselected potentials are zero; selected potentials are constant on each connected component, and the root component is fixed. This number is odd exactly when G[S] is connected. There are O(n+m) clauses of width at most four and only O(n) variables.

The cardinality constraint also costs O(n) gates with unique extensions: compress triples of equal-weight bits with constant-size full adders, reducing the total bit count at each step. At most O(n) compressors leave two O(log n)-bit numbers; add and compare them with O(log n) more gates. Encode the resulting fan-in-two Boolean circuit with equivalences of width at most three and pin its acceptance output. No multiplicity is introduced.

### 2. Domination without neighborhood-size overhead in variables

For each vertex v add a bit t_v and clauses

\[
\neg t_v\vee\neg x_u\qquad(u\in N[v]).
\]

If S dominates v, t_v is forced to zero; otherwise it has two choices. Thus a cardinality-feasible S containing r contributes exactly

\[
2^{c(G[S])-1+d(S)}, \tag{1}
\]

where d(S) is the number of undominated vertices. This is odd exactly for a connected dominating set. These clauses are a parity filter, not a pointwise encoding of domination. Total variables remain O(n), total clauses O(n+m), and maximum width four.

For Connected Vertex Cover, replace this filter by \(x_u\vee x_v\) for each edge. Infeasible covers then have zero extensions; feasible ones have the connectivity multiplicity. For Steiner Tree, fix a terminal root, require all terminals selected, and replace the budget by |S|≤k+1. A connected such S has a spanning tree with at most k edges, and every feasible tree gives such an S. Edge weights cannot be inserted into this argument.

### 3. Isolation of selection bits converts parity into decision

Use the established pairwise-independent families \(h_w:\{0,1\}^n\to\{0,1\}^s\), with O(n) key bits and uniformly constructible O(n)-size bounded-fanin circuits, for 2≤s≤n+1. See [Applebaum, Theorem 2.3](https://eccc.weizmann.ac.il/report/2017/063/download/), attributed to IKOS08/BIO14; Construction 4.4 gives the uniform local-isolation application. A dense random matrix would incur a quadratic gate cost and would not justify the claimed bound.

Choose s uniformly from {2,…,n+1}, then an independent uniform key w and target y. Hardwire w,y and encode h_w(x)=y with uniquely determined gate variables. This adds O(n) variables and width-three clauses. Hash **only x**, leaving the potential and domination witnesses unrestricted.

Let A be the set of valid rooted solutions. For A nonempty, K=|A| and \(s_* = \max(2,\lceil\log_2 K\rceil+1)\) give \(\lambda=K/2^{s_*}\in[1/4,1/2]\). For Z=|A∩h_w^{-1}(y)|, pairwise independence gives

\[
\mathbb E Z=\lambda,\qquad \mathbb E[Z(Z-1)]\le\lambda^2.
\]

Since \(\mathbf1_{Z=1}\ge Z-Z(Z-1)\), the probability of a unique valid selection in the bucket is at least 3/16 conditional on s=s_*, hence at least 3/(16n) overall. This includes K=1.

By (1) and unique extension of the hash and budget gates, the full formula's count modulo two is exactly Z modulo two. Invalid selections contribute even counts or zero. An odd answer therefore certifies existence; if A is empty it is impossible. Repeat independently 6n times: the failure probability is at most \(e^{-18/16}<1/3\). Try all roots for dominating sets and vertex covers; any feasible solution has a root, and an OR of sound YES answers remains sound. Steiner Tree needs only its fixed terminal root.

Each call to (A) has N=O(n) variables and O(n+m) clauses. Polynomially many calls preserve the stated running time. This proves the conditional theorem.

## External premise and review boundary

Sources checked November 4, 2026:

* [Anthropic, MainResults.lean](https://github.com/anthropics/formal-math/blob/main/eth/MainResults.lean) states one machine and constant C, uniform in width a, with exponent \(C\min\{aM/\sqrt{\log M},a^2N\log\log N/\sqrt{\log N}\}\). Taking a=4 gives (A). The file defines the claim; it is not itself a proof. Its distinct-clause/all-variables-occur restrictions are handled by deduplication and removing unused variables while restoring their factor \(2^u\) to the exact count. Small cases are direct. Full proof checking and formal execution were not performed here.
* [OpenAI's formalization scope](https://github.com/openai/math/blob/main/lean/docs/378.md) separately documents the weaker exponent \(N(\log\log N)^2/\sqrt{\log N}\), while reporting (A) for the manuscript. Assuming only that documented weaker bound gives the same graph corollary with the extra log-log factor. The sharper sparse-clause bound cannot be substituted on dense graphs.

The connectivity multiplicity is the established [Cut & Count idea](https://arxiv.org/abs/1103.0534), and linear-size isolation is prior work. The local deduction was already present in [the October 27 research branch](https://github.com/braulov/hardness/blob/5900c687187b3b7796bc87e2010581c37682b95d/research/6.1-winwin/sat_status.md), §§2–5. This note extracts and checks it; it does not claim discovery or publication priority.

The unresolved dependency is the external counting theorem, not a missing weighted-counting lemma in this proof. The result gives randomized decision, not deterministic decision or exact counts of connected solutions. Dense Hamiltonian Cycle and Feedback Vertex Set are not settled by this vertex encoding: their analogous selection/circulation variables can depend on m. No circuit lower bound or replacement hardness hypothesis follows here.

## Literature comparison (November 4, 2026)

**Verdict: not subsumed by the inspected papers; novelty remains unestablished.** Here n always counts vertices and m edges. Polynomial input factors are suppressed. No full external proof or formal build was independently certified in this comparison.

| Primary source | Exact scope relevant here | Does it cover this corollary? |
|---|---|---|
| [OpenAI, October 25 manuscript](https://raw.githubusercontent.com/openai/math/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex), §1 | Deterministic fixed-width exact #SAT supplies (A); graph corollaries count independent sets and fixed-q colorings in 2^{o(n)}, perfect matchings in 2^{o(n+m)}. | Supplies the engine, not an explicit connected-selection application. |
| [Anthropic, 2610.00577v1](https://hexagonmath.org/pdf/2610.00577v1), Corollary 7 and proof, pp. 21–22 | Deterministic counts by cardinality for ordinary dominating sets, vertex covers, independent sets and cliques on arbitrary-density graphs, in O(2^{δn}) for every δ>0. | No connectivity condition or Steiner Tree. The proof shortens neighborhood clauses and uses a linear-size cardinality circuit; it does not impose connectedness. |
| [Tulsyan, 2610.00672v1](https://hexagonmath.org/pdf/2610.00672v1), Table 3, Proposition 11.1, Remark 11.4 | Lists connected VC/DS decision and minimum, with spanning-tree-weighted counts, and Steiner-tree counting/minimum weight. Assuming internal tensor lemmas, for fixed m≤Dn the proposed bound is deterministic 2^{δn} for every δ>0, with bounded degree or additional hub handling. These extensions are marked **sketches, not claimed**. | Closest overlap, but no proved arbitrary-density vertex bound. The template charges crossing edges, U=O(m+g³) for g blobs. Even its stronger, conditionally proved Hamiltonian-cycle bound 2^{O(n log(2+2m/n)/√log n)} is not subexponential in n when m=Θ(n²). |
| [Bhattacharjee, October 29](https://hub.valency.io/works/W_k8mwz4m8), Theorems 5.3, 6.20(i), 8.4 | Deterministic weighted summation of O(N) bounded-arity factors on N bits; weighted ordinary domination on bounded-degree graphs. SNP result uses μ=Σ_i n^{a_i} witness bits, not automatically n. | No connected-selection theorem. Our dense CNF has O(n+m) factors; applying the sparse factor theorem directly loses the vertex-only exponent. An unspecified SNP encoding cannot replace an O(n)-bit connectivity construction. |
| [Gaspers, November 1, 2611.01774v1](https://arxiv.org/html/2611.01774v1), Theorems 1.2–1.3, §2.5 | Arbitrary graphs: one-sided randomized O(1.6991^n) CDS and O(1.6444^n) connected VC; deterministic O(1.7361^n) CDS. Includes weighted variants and polynomial-space guarantees, without assuming the SAT claims. | Different guarantees, still exponential. Section 2.5 explicitly reports no known subexponential consequences for its connectivity problems and notes the Θ(n log n) cost of parent-pointer encodings. This is supporting context, not a novelty certificate. |

The [November polynomial-alphabet CSP theorem](https://hexagonmath.org/2611.00004v1) also does not supply a matching dense-graph statement: its fixed-degree requirement makes direct occurrence splitting cost O(n+m) variables. Existing [October planar algorithms](https://arxiv.org/abs/2610.11944) have stronger deterministic bounds on their restricted graph class, not on arbitrary graphs.

Thus the possible incremental contribution is narrowly **O(n) counting variables despite arbitrary density**, plus isolation giving a single explicit subexponential rate for all three unweighted decision problems. Sparse connectivity applications and the underlying methods already appear in prior work. Search coverage cannot exclude unindexed or later results; this comparison establishes a scope difference, not publication priority.
