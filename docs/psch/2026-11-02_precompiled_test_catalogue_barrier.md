# No-go for polynomial catalogues of precompiled clique tests

**Date:** 2026-11-02. **Branch:** PSCH/B, dense Clique -> sparse binary CSP.
**STATUS:** Both elementary lemmas below are self-contained conditional *syntactic-model* results. They do **NOT** rule out arbitrary polynomial-time compilers with large input-dependent tables, arbitrary graph topology, or high-complexity Boolean predicates. Novelty relative to classical monotone circuit/minterm and knowledge-compilation lower bounds has **NOT** been established.

## Goal, parameters

Input: ordinary k-Clique on arbitrary simple graphs on N=k^2 vertices. Desired transformation: deterministic, polynomial time, decision-preserving binary CSP with m=O(k polylog k), domain Q=k^{O(1)}, Δ<=3. We deliberately allow precomputation to use all Θ(N²)=Θ(k⁴) input bits; the problem is compressing the *number of constraints*, not the number of input bits. The results below concern how input bits influence each target-table entry.

## 1. Algebraic degree trade-off for Boolean constraint acceptance

Fix N=k and let t=binom(k,2) edge bits b_e be unrestricted. On these graphs, k-Clique is exactly AND_t(b)=prod_e b_e.

Suppose an arbitrary deterministic compiler outputs at most m constraint slots, at most M=O(m) relevant variables, domains of size at most Q, and is exactly decision-preserving on all inputs. Pad the slots, variable IDs, and domain to a common size, allowing the output constraint topology, tables and local domains to depend on b. For any fixed target assignment z∈[Q]^M, let f_{j,z}(b)∈{0,1} mean "constraint slot j is satisfied by z in the compiler's output for b"; define any unused slot to accept. Suppose EACH such Boolean function (over the fixed input cube) has multilinear polynomial degree ≤d over a fixed field F.

At the complete input b=1^t there is an accepting assignment z*. On every other b there is no accepting target assignment. Hence:
    prod_{j=1}^m f_{j,z*}(b) = prod_{e=1}^t b_e    for every b∈{0,1}^t.
Uniqueness of multilinear representations over any field gives t≤sum_j deg f_{j,z*}≤md. Thus

    m d >= binom(k,2).

This allows **arbitrary existential proofs**, graph-dependent topology, and arbitrary domain Q, but assumes small degree for the **Boolean acceptance indicator** of each individual check. It does **not** apply to a low-degree field expression whose ZERO-TEST is an indicator of high Boolean degree, e.g. [sum_e(1-b_e)=0 mod p] with p>t. The theorem's source family (graphs on exactly k vertices) is itself easy, so this is a restriction on the stated *syntax of precomputation*, not evidence against general complexity-theoretic feasibility.

## 2. Polynomial-catalogue / DNF-size theorem for arbitrary existential proofs

Fix N=k² and a source graph with independent edge bits X=(x_e)_{e∈binom([N],2)}. Suppose a compiler represents k-Clique using an **input-independent target constraint graph** with m binary constraints (and optional unary constraints counted as slots) and a common domain [Q], possibly with many existential helper variables. The target table bit corresponding to slot j and local symbol pair (a,b) is an arbitrary Boolean DNF of source edge and nonedge literals, with **terms fixed independently of X**. Let M be the **total number of DNF terms in all table entries** (unary entries included). No bound is imposed on how many source-edge literals occur in an individual DNF term.

Then necessarily, for k>=2 and m>=1,

    M >= k^{ceil(k/(2 sqrt(m)))}.

In particular, if M<=k^C for some fixed C, then m=Omega_C(k²). If m=O(k log^c k), then M >= k^{Omega(sqrt(k)/log^{c/2} k)}; for Q=poly(k), at least one table entry has superpolynomial DNF size.

### Proof

For every k-set S⊆[N], let G_S have edge set E_S=binom(S,2) and no other edges. This is a YES-instance with exactly one k-clique. Let z_S be any accepting CSP assignment on G_S. For each of the at most m accepted local entries choose one DNF term true on G_S. Write its positive support F_j⊆E_S and its negative support H_j⊆(binom([N],2)\E_S). Set U=∪_j F_j⊆E_S.

Construct the graph G_U having exactly the edges U. Each chosen DNF term remains true: its positive edges are in U and its negative edges remain absent because U⊆E_S. Because the compiler skeleton is input-independent, the same target assignment z_S is accepted on G_U. By soundness G_U must contain a k-clique. Since U⊆E_S and S is the only possible k-clique, U=E_S.

Therefore every E_S must be expressible as the union of at most m positive supports F chosen from a *fixed catalogue of at most M sets*, each contained in E_S. This works even for **nonmonotone DNF**, because the negative literals remain satisfied when passing from E_S down to U.

Put r=ceil(k/(2 sqrt(m))). If every chosen support F touches fewer than r source vertices, then each has fewer than binom(r,2) edges, so the union has <k²/8 edges, whereas |E_S|=binom(k,2)>=k²/4. Hence for every S, SOME catalogue set F touches at least r vertices and has F⊆E_S, i.e. all its incident vertices are included in S.

For uniformly random k-set S⊆[N], a fixed edge support F touching v>=r vertices is contained in E_S with probability
    (k)_v/(N)_v <= (k/N)^v = k^{-v} <= k^{-r},
and probability zero if v>k. Union-bound over M catalogue terms: 1<=M k^{-r}. Thus M>=k^r. QED.

No restriction on the degrees of target variables or on uniqueness of witness extensions is used. The essential restrictions are (i) **fixed output constraint skeleton** (or a common *polynomial catalogue* of acceptance terms which stays valid when G changes to G_U), and (ii) polynomial **total DNF term count** for the table-bit functions of the input graph.

### Interpreting the result as a lower bound on relation complexity

With m=O(k polylog k), Q=k^C and a fixed skeleton, there are at most O(mQ²) binary table entries. Therefore some table-entry function (as a Boolean function of the *input adjacency bits*) needs at least
    k^{Omega(k/sqrt(m))}/(m Q²)
DNF terms. For m=O(k log^c k), this is superpolynomial.

An entry can still be evaluated in polynomial time and have exponentially long DNF (e.g., a graph reachability predicate, or a polynomial-size CNF with many minterms). Thus the theorem does not prohibit general polynomial-time preprocessing. It rules out a particular broad version of "precompute polynomially many edge-subset checks, then let the CSP witness choose a few". It also shows why checksums over **fixed** nonnegative source-edge subsets cannot solve the universal problem: they are single-term DNFs when the field is larger than the number of summands.

The standard minterm technique for monotone Clique circuit complexity is related background, but no novelty claim is made. References: Arora–Barak *Computational Complexity* Section 13.3 (monotone circuits); Razborov's lower bounds and subsequent developments; source background https://theory.cs.princeton.edu/complexity/circuitlbchap.pdf .

## 3. Why this does not rule out input-dependent table compilation

The supports F_j in the theorem are fixed *before* seeing G. If the table constructor computes a complex input-dependent object and then chooses which source edges a given entry tests, the same witness and term need not survive when the graph changes from G_S to G_U; the proof fails.

Similarly, a Boolean table-bit function with **large DNF complexity** can be calculated in polynomial time using a small CNF, a branching program, graph reachability, determinant, or another algorithm. Polynomial-time precomputation is a much stronger model than polynomial-length DNF catalogues.

**Next plausible direction:** select an input-dependent global predicate with large DNF complexity but efficient evaluation (e.g., reachability-style/linear-algebraic constraints), then try to show that O(k polylog k) such tests on a high-treewidth target proof graph can jointly certify all edges of some k-clique. At present no universal compiler has been obtained.

## 4. Relation to earlier limitations and status

- Output-bit-budget lower bound from Dell–van Melkebeek and Drucker: conditional no subquadratic BIT output for decision-preserving compression; does not exclude m=k polylog, Q=k².
- Exact-projection information bound: mQ²=Omega(k⁴) for a fixed source assignment projection; does not apply to decision-only compilation.
- Fixed-code no-go: Ω(k²) local tests for source-independent coded witness positions, even nonlinear, but not genuine existential auxiliary states.
- Here: potentially arbitrarily many auxiliary states and global table bits, BUT input-dependence must be expressible as a polynomial catalogue of DNF terms.
- Neither theorem produces a lower bound for unrestricted polynomial-time target-table construction. The principal general Clique -> sparse 2-CSP problem remains OPEN.

## Research status

Theorems above were derived as standalone finite combinatorial/algebraic arguments; they have **not** been independently checked against all prior literature. Treat them as internal research notes, not claims of publication-level novelty.
