# Binary CSP reduction by cyclomatic number

> **2026-11-02 conditional algorithmic update.** Under the **full, independently unaudited** Boolean tensor-contraction theorem of the October 2026 ETH manuscript, combining the proved \(O(\mu)\)-core below with Boolean tensorization yields \(2^{O(\mu\log q/\sqrt{\log(\mu\log q)})}\operatorname{poly}(|\Gamma|)\) time for polynomial-alphabet explicit binary CSP (and polynomial time at \(\mu=0\)). The classical \(q^\mu\operatorname{poly}\) algorithm below is unconditional. Thus a hypothetical universal polynomial-alphabet Circuit-SAT compiler guaranteeing \(\mu=O(s/\log s)\) would yield a \(2^{o(s)}\) Circuit-SAT algorithm under the tensor theorem, contradicting any assumed no-\(2^{o(s)}\) Circuit-SAT hypothesis. **Do not promote this intermediate target as a compatible hardness route under both premises.** See [precise audit](33_tensor_contraction_sparse_2csp_and_hardness_triage.md).


**Status:** PROVED (elementary combination of standard CSP variable elimination, a graph-counting bound, and cycle-cutset conditioning). **Not claimed as a novel result.**

## Statement and conventions

Let \(\Gamma\) be a finite-domain **binary** CSP. Its variables have domains contained in a common set \(D\), \(|D|=q\). Unary restrictions are allowed, and every binary constraint is represented by an explicit relation \(R_{uv}\subseteq D\times D\). Intersect parallel constraints on the same pair, and absorb self-constraints into unary domains. Let \(G_\Gamma\) be the resulting **simple primal/constraint graph**; write

\[
n=|V(G_\Gamma)|,\quad m=|E(G_\Gamma)|,\quad
c=\operatorname{cc}(G_\Gamma),\quad
\mu=m-n+c.
\]

Here \(\mu\) is the *cyclomatic number* (cycle rank, feedback edge number) of the constraint graph. **Do not confuse this with the cycle rank of a factor/incidence graph for an arity-\(3\) or higher CSP.**

### Proposition 1 (small binary CSP core)

There is a deterministic \(\operatorname{poly}(n,m,q)\)-time procedure that either establishes that \(\Gamma\) is unsatisfiable, or produces a satisfiability-equivalent binary CSP \(\Gamma'\), on the **same domain** \(D\), with

\[
  |V(G_{\Gamma'})|\le 2\mu,\qquad
  |E(G_{\Gamma'})|\le 3\mu.
\]

All remaining constraints have explicit unary or binary tables. When \(\mu=0\), the procedure decides the instance in polynomial time (and an affirmative instance can be represented by the empty CSP).

If one insists on outputting a conventional CSP even when unsatisfiability was detected, output a fixed constant-size UNSAT instance (for example, one variable with empty unary domain). In that formulation the uniform bound is \(O(\mu+1)\), not literally \(2\mu\) when \(\mu=0\). In the statements below, the early UNSAT answer is permitted.

### Proposition 2 (cycle-cutset algorithm)

Every such binary CSP can be decided deterministically in time

\[
  q^{\mu}\operatorname{poly}(n,m,q)
\]

and polynomial space. This applies to arbitrary explicit binary relations (no algebraic or low-rank assumption).

## Proof of Proposition 1: eliminate degree at most two

Maintain unary domains \(U_v\subseteq D\) and at most one relation per unordered pair. The following operations preserve satisfiability:

1. **Degree zero:** if \(U_v=\varnothing\), reject; otherwise remove \(v\).
2. **Degree one, neighbor \(u\):** replace
   \[
   U_u(a)\ \gets\ U_u(a)\land
        \bigvee_{z\in D}\bigl(U_v(z)\land R_{uv}(a,z)\bigr),
   \]
   then delete \(v\).
3. **Degree two, distinct neighbors \(u,w\):** compute
   \[
   S_{uw}(a,b)=\bigvee_{z\in D}
       \bigl(U_v(z)\land R_{uv}(a,z)\land R_{vw}(z,b)\bigr).
   \]
   Delete \(v\) and its two incident edges. Add the binary constraint \(S_{uw}\) on \(u,w\); if an \(uw\)-constraint already exists, intersect the two tables. A degree-two variable with two edges to the same neighbor, if the instance was represented as a multigraph, instead produces a unary condition; it is simpler to consolidate parallel constraints first.

The degree-two operation is Boolean matrix multiplication with a diagonal unary mask. A new \(q\times q\) table can be computed in \(O(q^3)\) time. Domains remain subsets of \(D\); **the alphabet does not grow**. Unary propagation and table intersections are also polynomial. There are at most \(n\) variable eliminations.

Each operation does not increase the cyclomatic number: leaf and isolated-vertex removals preserve it; suppression of a degree-two vertex with two distinct nonadjacent neighbors preserves it; merging with an already present edge can decrease it. Hence \(\mu'\le\mu\) throughout.

If the process does not reject, it terminates with a (possibly empty) simple graph of minimum degree at least three. Write \(n',m',c'\) for its parameters. By the handshake lemma,

\[
  2m'\ge 3n'.
\]

Since \(\mu'=m'-n'+c'\le\mu\),

\[
  \mu'\ge n'/2+c',
  \quad\text{so}\quad
  n'\le 2\mu'-2c'\le2\mu,
\]

and consequently

\[
  m'=\mu'+n'-c'\le3\mu'-3c'\le3\mu.
\]

This proves Proposition 1. The bound is about *numbers of variables and binary constraints*, not necessarily a polynomial kernel in the parameter \(\mu\) **in bits**: explicitly stored relations can use \(\Theta(q^2)\) bits per edge. For fixed \(q\), the core does have \(O(\mu)\) table entries up to constant factors.

## Proof of Proposition 2: condition on at most \(\mu\) vertices

Choose a spanning forest \(T\) of the primal graph. Exactly \(\mu\) edges lie outside \(T\). For each such non-tree edge choose one endpoint, and let \(S\) be the union of all chosen endpoints. Then \(|S|\le\mu\).

Every cycle contains a non-tree edge, and the selected endpoint of that edge belongs to \(S\). Thus \(G_\Gamma-S\) is a forest: \(S\) is a *cycle cutset* (feedback vertex set).

Enumerate the at most \(q^{|S|}\le q^\mu\) assignments to \(S\). Reject an assignment if it violates any unary constraint or any binary constraint with both endpoints in \(S\). Condition all remaining constraints incident with \(S\) into unary domains. The residual instance is a binary CSP on a forest, decidable by ordinary leaf-to-root dynamic programming in \(\operatorname{poly}(n,m,q)\) time. Accept if any cutset assignment extends to a satisfying forest assignment.

This proves the claimed running time. No minimum feedback vertex set needs to be found; choosing endpoints of a fundamental-cycle edge set is enough.

## Tight scope and use in the hardness program

- For a **hypothetical** polynomial-time compiler \(C\mapsto\Gamma_C\) from arbitrary \(s\)-input circuits of size at most \(s^d\), with \(q=s^{O_d(1)}\), the condition \(\mu(\Gamma_C)=o(s/\log s)\) for **all** inputs would yield a \(2^{o(s)}\operatorname{poly}(s)\) Circuit-SAT algorithm via Proposition 2. Thus, *assuming* the corresponding Circuit-SAT hardness hypothesis, no such universal compiler exists with that uniform bound. This is a **conditional worst-case obstruction**, not an unconditional lower bound on every output.
- Conversely, a compiler producing \(\mu(\Gamma_C)=O(s/\log s)\) with polynomial alphabet would yield an \(O(s/\log s)\)-variable, \(O(s/\log s)\)-constraint binary CSP after Proposition 1. This is a possible **intermediate reduction target**, not a construction of such a compiler.
- If it suffices downstream to obtain \(o(s)\) source vertices and edges (e.g. for a proposed CSP-to-HOM reduction whose source size is \(O(k+m)\)), then the weaker goal \(\mu(\Gamma_C)=o(s)\) would suffice *for that size bound*. The later CSP-to-HOM reduction and its target parameters must be checked separately.
- This preprocessing does not reduce a general computation's large cycle rank by itself. In particular, a Tseitin **factor graph** for a general circuit may have \(\Theta(t)\) independent cycles; an arity-\(3\) factor must not be treated as one binary edge without a valid conversion and a fresh parameter audit.
- Degree three is the natural closure boundary: existentially eliminating a degree-three variable can create an essentially ternary relation that is not expressible as a conjunction of binary constraints on the same three boundary variables.

## Prior art and attribution

The result above is presented as a **short derived lemma**, not as a new kernelization theorem. Its components are classical:

1. **Rina Dechter**, *Bucket Elimination: A Unifying Framework for Reasoning*, Artificial Intelligence **113** (1999), 41–85. General exact variable elimination for constraint networks, including existential projection of local relations. [DOI](https://doi.org/10.1016/S0004-3702(99)00059-4); [author-hosted text](https://ics.uci.edu/~csp/r48b.pdf).
2. **Rina Dechter**, *Enhancement Schemes for Constraint Processing: Backjumping, Learning, and Cutset Decomposition*, Artificial Intelligence **41** (1990), 273–312. Classical cycle-cutset conditioning for CSP. [DOI](https://doi.org/10.1016/0004-3702(90)90046-3).
3. **Rina Dechter and Yousri El Fattah**, *Topological Parameters for Time-Space Tradeoff*, Artificial Intelligence **125** (2001), 93–118. Explicit context for conditioning on cycle cutsets and solving the residual tree-structured network. [DOI](https://doi.org/10.1016/S0004-3702(00)00050-3).
4. **Michael James Bannister**, *Lower Bounds and Fixed-Parameter Tractability of Drawing Graphs*, PhD thesis, UC Irvine (2015), §4.3, Lemma 4.1 (printed p. 82). The graph-theoretic bound for a connected minimum-degree-three graph with cycle rank \(\mu\): at most \(2\mu-2\) vertices and \(3\mu-3\) edges. [Thesis](https://escholarship.org/uc/item/7j72h78r).

**Attribution scope:** these references establish the ingredients; they are *not* claimed to state verbatim the combined binary-CSP propositions with exactly the above conventions and bounds.
