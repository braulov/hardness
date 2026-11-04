# Linear-size isolation into unique bipartite cubic CSP

**PROVED using the classical Isolation Lemma.** An explicit binary CSP on k variables, m=O(k) constraints and polynomial domain q has a randomized reduction to binary CSP on a simple bipartite 3-regular graph with K=O(k+m) variables and polynomial domain Q=(kq)^{O(1)}. UNSAT inputs always produce UNSAT outputs; SAT inputs produce a unique-solution output with inverse-polynomial probability. Other outputs on SAT inputs may have multiple solutions. This is a promise reduction, not an always-in-promise mapping.

## Isolate a score

Represent an assignment by its k chosen elements of Ω={(v,a)}, |Ω|=kq. Assign independent weights w_{v,a} uniformly from {1,…,2kq}. The [Mulmuley–Vazirani–Vazirani Isolation Lemma](https://doi.org/10.1007/BF02579206) gives a unique minimum-weight satisfying assignment with probability at least 1/2. Scores lie between k and B=2k²q.

For each threshold t, restrict to total score exactly t. To encode this with linear many variables and constraints, create a score leaf s_v=w_{v,X_v}. A binary addition tree has O(k) internal scores; at each node a tuple variable P=(s_L,s_R) is connected by three binary projection/sum relations to s_L,s_R,s_parent. Pin the root to t. Domains of size at most (B+1)² suffice. Every original assignment determines every auxiliary variable uniquely; score-restricted counts are preserved.

Split high-degree variables into occurrence copies joined by equality paths, with one external occurrence per copy. All degrees become at most three, with O(k+m) total size and unique extensions. Unary domains can be included in incident relations. Handle isolated variables explicitly so an empty domain is never lost.

## Bipartitize and complete degrees, parsimoniously

For each constraint R_{xy}, introduce a variable z_{xy} whose domain is its allowed pairs, and replace the edge by two projection relations x=π₁(z), y=π₂(z). The primal graph becomes simple bipartite, old variables retain degree at most three, and incidence variables have degree two. The domain grows by at most a square. Every satisfying old assignment has exactly one extension.

Balance the two parts by adding forced singleton-valued isolated vertices. Each side now has the same number of missing degree stubs. Pair opposite stubs arbitrarily. For each pair, use a fresh K₃,₃-minus-one-edge gadget: its two degree-two ports are joined to the old vertices on the opposite sides. Every new internal variable is forced to a singleton value; attachment relations accept every legal old value with that singleton. Each gadget fills one stub on each side, is simple and bipartite, and has six new vertices. Thus all degrees become three with linear overhead and unique extensions. This step does not preserve expansion, girth, or a predetermined graph topology.

## Promise and error accounting

Choose t uniformly from {k,…,B} after choosing weights, and output its completed CSP. On a SAT input, conditional on successful isolation, the unique minimum score is selected with probability at least 1/B. Thus the output has exactly one solution with probability at least 1/(2B). On UNSAT, every output has zero solutions.

Alternatively query all B thresholds. With an **exact** oracle for the 0-or-1 promise, accepting if any query accepts gives a one-sided randomized Turing reduction with success at least 1/2 on SAT inputs. Arbitrary oracle behavior on multiple-solution outputs is harmless because those occur only when the source is SAT.

With a **bounded-error randomized promise solver**, amplify its per-query error and take a union bound. This gives a bounded-error randomized source solver. Amplification alone does **not** make its error one-sided: an UNSAT promise instance can still be falsely accepted with small positive probability. This corrects the original note's stronger claim. An additional verified-witness search argument would be needed to establish a one-sided composition.

For q=k^{Θ(1)}, the output has K=Θ(k) after harmless padding and log Q=O(log k). Polynomially many queries preserve the scales 2^{O(k)} and q^{o(k/√log k)}. A solver must cover the resulting fixed polynomial domain exponent, not just a smaller predetermined alphabet class. Randomized reductions justify randomized hardness implications; they do not refute a merely deterministic hardness hypothesis.

This construction does not transfer worst-case hardness to the independent-table random ensemble. Nor does the decision-preserving CSP→HOM construction preserve uniqueness of homomorphisms.

Provenance: [original note 50](https://github.com/braulov/hardness/blob/c994435b692c37958eeff2c997188603dcaeddb6/docs/50_linear_parameter_random_isolation_to_unique_bipartite_cubic_csp.md). The original note's late single-output addendum supersedes its earlier denial of a many-one version. Finite graph check: `py experiments/50_cubic_bipartite_padding_sanity.py`.
