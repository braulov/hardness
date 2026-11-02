# The small-group trap in Nguyen recursion, plus an unconditional greedy theorem for random CSP tables

**Checkpoint:** 2026-11-02. **Status:** source-dependent parameter audit of the *claimed* Nguyen/Anthropic recursion; unconditional elementary probability theorem about random CSP relations; a first-moment threshold calculation. **No q^{o(k)} algorithm for arbitrary critical-density CSP.** This supersedes the *speculative* suggestion in [note 38](38_multilevel_factorization_and_degree_uniformity.md) that few blocks alone might fix the proof.

## 1. The exact grouping overhead

In [Nguyen 2611.00004v1](https://hexagonmath.org/2611.00004v1), Proposition 3.1 imports from Anthropic a clique counting level with parameters K, rate e_K <= A/sqrt(log_2 K), and g=3K^8 groups. The displayed grouping parameters (17) and (18) are

    lambda = ceil((U+g P/K)/K^2)
    Bprime = ceil(2g P/K)+g^2 B
    Tgroup <= (K^g + Tclique*2^(2g P/K)) * (g(P+B))^C1

with Tclique of exponential rate e_K*K^2*lambda. Thus the *published sufficient runtime estimate* includes both
- rate contribution exp(O((U+gP/K)/sqrt(log K))) from the stated upper bound on e_K; and
- a separate factor exp(O(gP/K)), explicitly in (18).

This is an analysis of an **upper bound**, NOT a runtime lower bound or impossibility proof for all implementations. A much stronger internal clique routine could evade the first obstacle, and a substantially different grouping theorem could evade the second.

## 2. Coarse blocks really have saturated pairwise cover capacity on random critical graphs

Take G~G(k,d/k), d=sqrt(log k), and a **fixed in advance** balanced partition into g groups each of size s=k/g. Suppose g=o(d) and g>=2, with s tending to infinity. For each group pair (A_i,A_j), the bipartite random graph has expected degree lambda=(d/k)*s=d/g -> infinity.

With high probability **every pair** has a matching of size at least s/2. Proof: if maximum matching <s/2, König's theorem supplies a vertex cover of fewer than s/2 vertices, leaving two uncovered subsets each of size >s/2 with no edges. For any given pair the probability some empty s/2 by s/2 rectangle exists is at most

    binom(s,ceil(s/2))^2 * (1-d/k)^(s^2/4)
       <= 4^s * exp(-s*d/(4g)) = exp(-Omega(s*d/g)).

A union bound over <=g^2 group pairs goes to zero since d/g->infinity and s=k/g is large. (Adjust floors/ceilings without changing the conclusion.)

The **constructive vertex-cover factorization** of [note 37](37_joint_block_matching_rank_and_arity.md) allocates b=ceil(log_2q) bits per covered vertex, so every group-pair bond needs at least sb/2 bits in this worst-case interface model; the max group row capacity therefore satisfies

    P >= (g-1)*s*b/2 = Omega(k b),

and U=sum_pair nu_ij*b=Omega(g k b). Nguyen's grouping overhead on this representation is at least

    gP/K=Omega(k b*g/K) = Omega(k b*K^7),     g=3K^8.

Consequently the **numerical runtime guarantee produced by applying (17)-(18)** cannot certify q^{o(k)} for growing K by simply replacing one label per edge with one label per matched cover vertex. Even fixed K gives at best an exp(O(k log q)) scale in this estimate. This is not a theorem that the actual algorithm takes that long.

Moreover, the imported rate is only certified as e_K=O(1/sqrt(log K)). With g=polylog k, its certified saving is sqrt(loglog k), NOT sqrt(log k). A hypothetical contraction theorem retaining a sqrt(log k) saving while allowing g=polylog k would be a genuine new theorem, not a parameter substitution into the published one.

For g much larger than d and blocks small, [note 39](39_adaptive_block_rank_barrier.md) shows even graph-adaptive partitions have sum_pair nu_ij >=m-O(k) with high probability, provided every block has size <=k^{1-eps}. The two regimes leave the shared-latent/multilevel route open but exclude the simplest reuse of the old grouping formula.

## 3. Unconditional greedy theorem for random binary relations

Fix **any simple graph** G on k vertices of maximum degree Delta, domain [q], and a density rho in (0,1). On each constraint edge independently include each ordered value pair with probability rho, independently across all edges/pairs.

**Theorem.** With probability at least

    1 - k*q^Delta*exp(-q*rho^Delta),

every vertex v and every assignment of its neighbors have **at least one** compatible value at v. This is the universal neighborhood-extension property. On that event, *any fixed-order greedy algorithm* that assigns a locally compatible value at each step constructs a globally satisfying assignment in polynomial time.

**Proof.** Fix a vertex v with degree t<=Delta and an assignment to all t neighbors. For each candidate a in [q], the t incident-table entries are independent Bernoulli(rho), so a is compatible with probability rho^t. Different candidate a use disjoint random entries and thus give independent events. The probability no compatible value exists is (1-rho^t)^q <=exp(-q*rho^Delta). There are <=k*q^Delta vertex/neighborhood-assignment combinations. Union bound proves the advertised probability. If extension holds for every full-neighborhood assignment, then it holds for every *partial* earlier-neighbor assignment (complete it arbitrarily), so greedy never gets stuck.

**Corollary.** For q=k^c with fixed c>0, constant rho in (0,1), and Delta=o(log k), the failure probability tends to zero rapidly, as q*rho^Delta=k^{c-o(1)} dwarfs log k+Delta log q. In particular random Bernoulli(1/2) relation tables are *easy* on any prescribed family with Delta=o(log k), even if all relations have rank q and row weights Theta(q).

For G~G(k,d/k) with d=sqrt(log k), an elementary binomial Chernoff union bound gives Delta(G)=O(log k/loglog k) with high probability. Thus the corollary applies to the random critical-density constraint graph as well.

The standard random-matrix theorem (Komlós and successors; see https://arxiv.org/abs/2011.01291 ) says each iid Bernoulli(1/2) q x q relation matrix has full rational rank with probability 1-o(1) as q grows. This means generic full rank and many allowed partners alone do **not** make a CSP random instance hard. Do not claim all m matrices simultaneously full-rank without a quantitative failure bound.

## 4. First-moment location of the nontrivial random-density window

Keep a *deterministic* graph with m=(1+o(1))kd/2 edges and sample relation tables at density rho. Let Z be the number of satisfying assignments. For any graph,

    E[Z]=q^k*rho^m

exactly. The annealed first-moment threshold E[Z]=1 is therefore

    rho_star=q^{-k/m}=q^{-(2+o(1))/d}.

At q=k^c, d=sqrt(log k), this is rho_star=exp(-(2c+o(1))*sqrt(log k)), much smaller than every fixed positive constant, yet q*rho_star=q^{1-o(1)} (so relation rows still have many allowed partners).

If rho=q^{-(2+eps)/d} for constant eps>0, then

    E[Z]=q^{-(eps/2+o(1))*k},

so the instance is **UNSAT with high probability** by Markov's inequality. For rho=q^{-(2-eps)/d}, E[Z]=q^{(eps/2+o(1))*k}; this does NOT by itself imply SAT whp.

Thus a plausible random near-threshold *test distribution* would tune rho around rho_star rather than using iid density 1/2. This is only a suggestion for studying average-case behavior, **not a hard distribution or proof of hardness**. Factor rank and permitted-partner counts can remain large near that threshold (verify rank claims quantitatively if making simultaneous statements).

## 5. Implications

- **Proved unconditional:** universal local extension theorem, greedy success probability, first-moment formula and below-threshold UNSAT.
- **Proved modulo standard graph facts:** coarse group-pair matching bound and its quantitative implication for the *stated* Nguyen grouping runtime estimate.
- **Not proved:** a general sub-q^k algorithm at critical density; an algebraic multi-level factorization; growing-Delta theorem with f(Delta)=o(Delta); SAT whp above the random threshold; any average-case hardness theorem.
- **New priorities:** (a) inspect whether the imported clique routine can support better *capacity-sensitive* grouping than (17)-(18), rather than blindly reducing U, (b) if studying random CSP, focus on near-threshold rho and avoid treating random half-dense constraints as hard, (c) continue to distinguish algorithmic speedups from architecture-specific bottlenecks.

Related: [critical-density HOM source](35_critical_density_csp_to_degen2_hom.md), [joint matching rank](37_joint_block_matching_rank_and_arity.md), [growing-degree criterion](38_multilevel_factorization_and_degree_uniformity.md), [adaptive fine partition barrier](39_adaptive_block_rank_barrier.md).
