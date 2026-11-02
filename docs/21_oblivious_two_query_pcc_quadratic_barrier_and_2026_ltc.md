# Quadratic lower bound for oblivious 2-query compatibility testing, even with polynomial alphabet and randomized tables

**Research iteration 2026-11-02.** Main result is a self-contained elementary model-specific theorem. It is **not** a general lower bound for existential CSP compression, not a result about decision-only randomized reductions, and novelty relative to the coding/PCP literature is NOT established. This follows the two-layer interface audit (note 20) and directly tests the nonlinear LTC + global table idea.

## 1. Strong fixed-encoder model

Fix k>=3 and Q<=k^C with C>=1 independent of k. Let E:S_k -> [Q]^ell be ANY fixed encoding (not assumed linear, systematic, efficient, or locally decodable). Let t fixed tests, where test s reads two specified coordinates (u_s,v_s) of E(pi), potentially the same coordinate. The coordinate pairs may be chosen arbitrarily but must be independent of the input adjacency tables A. For each A, each test receives an **arbitrary input-dependent relation table** R_s^A subset [Q]^2; the table may be computed using ALL k^4 source adjacency bits in polynomial time. There is NO auxiliary existential proof: the only proof of pi is the prescribed E(pi). Assume the exact per-permutation predicate for every graph A:

    pi is a valid Permutation Clique in A
       iff
    for every s, (E(pi)_{u_s},E(pi)_{v_s}) in R_s^A.

**Theorem (PROVED).** Necessarily t=Omega(k^2/(C+1)^2). In particular t=O(k) is impossible for every fixed polynomial alphabet exponent C, even with arbitrarily preprocessed global relation tables. The bound holds without computational assumptions.

This is substantially stronger than the previous tQ^2=Omega(k^4) description-count bound, but rests on a STRICTER encoding model: the codeword is input-independent and uniquely prescribed for each permutation, the query positions are fixed across inputs, and no existential auxiliary values are allowed.

## 2. Proof: single-deleted edges force decoding of the two selected values

For a test s, let

    Y_s(pi)=(E(pi)_{u_s}, E(pi)_{v_s}) in [Q]^2,

and define D_s(pi) subset [k] by: i in D_s(pi) iff every permutation sigma with Y_s(sigma)=Y_s(pi) satisfies sigma(i)=pi(i). Thus D_s(pi) is the set of original row choices fixed by this two-symbol view.

Fix a permutation pi and an arbitrary row pair i<j; put a=pi(i),b=pi(j). Start from the complete k-partite input, then delete exactly the single edge between (i,a) and (j,b), retaining all other edges. Call the new instance A_e.

The invalid permutations on A_e are EXACTLY those sigma with sigma(i)=a and sigma(j)=b. Since pi is invalid, at least one test s rejects Y_s(pi). Since every sigma not selecting that edge must be valid and is therefore accepted by EVERY test, no such sigma can share the rejected two-symbol value Y_s(pi). Hence the entire fiber Y_s^{-1}(Y_s(pi)) is contained in {sigma:sigma(i)=a,sigma(j)=b}, proving i,j in D_s(pi).

Since EVERY i<j must be certified by some test:

    binom(k,2) <= sum_{s=1}^t binom(|D_s(pi)|,2)    (*) for every pi.

## 3. A two-symbol view fixes only O(C) original row choices on average

Draw pi uniformly in S_k. Fix s. There are at most Q^2 possible Y_s values. If one fiber fixes r specific row choices, it contains at most (k-r)! permutations. Thus, for every integer 0<=r<=k,

    Pr_pi[ |D_s(pi)| >= r ] <= min(1, Q^2/(k)_r),

where (k)_r=k(k-1)...(k-r+1). This estimate remains valid when a fiber fixes MORE than r rows, since its size is still <=(k-r)!.

Use the tail-sum identity

    E_pi binom(|D_s(pi)|,2)
        = sum_{r=2}^k (r-1) Pr_pi[|D_s(pi)|>=r].

Choose R=ceil(2C+4), a constant. The sum for r<=R is O(R^2). For R<r<=k/2, (k)_r>=(k/2)^r, and with Q^2<=k^{2C},

    Pr[|D_s|>=r] <= k^{2C}(2/k)^r,

whose summed contribution is o(1) for sufficiently large k with C fixed. For r>k/2, the bound using (k)_{floor(k/2)} shows an exponentially small total contribution. Hence

    E_pi binom(|D_s(pi)|,2) <= O((C+1)^2).

Average inequality (*) over pi:

    binom(k,2) <= t*O((C+1)^2),

so t=Omega(k^2/(C+1)^2), as claimed.

**Why arbitrary preprocessed predicates do not help:** the argument never bounds table computation, table information capacity, algebraic degree, encoding complexity, or field size other than Q<=k^C. It uses only the fact that a fixed test reads two fixed symbols of an oblivious encoding.

## 4. Randomized exact-solution-preserving extension (PROVED, with strict quantifiers)

Suppose a random seed rho, whose distribution is independent of the input A, determines an input-independent encoder E_rho and a family of t input-independent queried coordinate pairs. Relation tables R_{s,rho}^A may be arbitrary input-dependent and randomized. Assume for EVERY input A, with probability at least 2/3 over rho, the resulting test system realizes the correct set of ALL valid permutations simultaneously.

Then the same t=Omega(k^2/(C+1)^2) holds.

Proof. For each single-edge-deleted input A_e, the probability that its entire permutation-solution set is represented correctly is at least 2/3. For a uniform pi and any row pair i<j, e is the deleted edge joining (i,pi(i)) and (j,pi(j)). Whenever the representation is correct for that A_e, some test's fiber at pi must fix both i and j, by Section 2. Let N_rho(pi) denote the number of pairs i<j for which the representation at the corresponding A_e is correct. Then E_{rho,pi}[N_rho(pi)] >=(2/3)binom(k,2). But for every rho,pi,

    N_rho(pi)<=sum_s binom(|D_{s,rho}(pi)|,2).

Apply the bound from Section 3 for each rho and then average over seeds. Therefore t=Omega(k^2/(C+1)^2).

This does **NOT** extend to a randomized reduction preserving only the yes/no satisfiability of A_e: all A_e (k>=3) are YES, and the reduction may reject individual permutations as long as some valid permutation survives. Nor does it cover input-dependent query positions, input-dependent encodings, or existential auxiliary proof variables selected as a function of A and pi.

## 5. Implication for the proposed two-layer compiler

A fixed good code C that encodes each permutation pi as one fixed word E(pi), combined with t=O(k) global input-dependent binary constraint tables operating on two positions of E(pi), CANNOT solve arbitrary PCC while exactly preserving the validity of every pi, even if C has excellent distance/testability and even if the tables use all k^4 input bits.

A genuinely new universal compiler must escape at least one assumption:
  (a) auxiliary existential witnesses for the same pi that can depend on the instance A;
  (b) tests/queries that depend on A, carefully preserving the total budget; or
  (c) only decision-preserving reduction (not a uniform fixed encoding of each source permutation).
These are ALLOWED. The main randomized PCC -> sparse 2-CSP goal remains OPEN.

This theorem also explains why merely inserting a better LTC into the earlier 'linear consistency + global nonlinear checks' plan does not prove a compiler. Good code distance has no effect on the pigeonhole bound for fixed two-symbol views.

## 6. Verified relevant literature: new good two-query LTCs (2026)

Uriya A. First and Stav Lazarovici, *Good Locally Testable Codes with Small Alphabet and Small Query Size*, APPROX/RANDOM 2026 (published Sep 9, 2026). It proves good 2-query LTCs on every fixed alphabet of size >=3, and good 2-query F-linear LTCs on vector-space alphabets of dimension >1. This IS a positive code-theoretic development: 2-query GOOD codes are not precluded when tests are nonlinear and alphabet has >=3 symbols.

Paper: https://arxiv.org/html/2512.16082 ; published DOI: https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.70 .

**Important quantitative caution for our k-log-k-bit witness:** a good code on a FIXED alphabet of size 3 encodes k log k bits into Omega(k log k) symbols. Simply packing b=Theta(log k) fixed-alphabet positions into one poly(k)-alphabet position reduces length to O(k) but need not preserve CONSTANT *block-distance local testability*: a changed packed symbol may alter only one constituent coordinate. The existing theorem, as cited, does not automatically give a family over alphabets growing as k^C with uniform constant gap/rate and an efficiently constructible O(k)-support test set. Both must be audited separately. No claim that this paper already supplies our required code parameters.

One can also compile 3-ary linear consistency checks into O(k) binary CSP using a gate-state alphabet p^3 (note 20). The new 2-query nonlinear LTC option removes the narrow '2-query affine equations cannot make good codes' obstruction, but does not supply compatibility verification.

Related large-alphabet limitation in a DIFFERENT model: Bhattacharyya--Gopi--Tal (RANDOM 2017) proved zero-error 2-query *locally correctable* codes require length >=exp(k/log|Sigma|); this is LCC, NOT LTC. Do not incorrectly apply it to exclude 2-query LTC.

## 7. Next sharp constructive experiment

Try a two-query verifier with *instance-adaptive existential encoding*:

    E_A(pi,w) in [k^C]^{O(k)},

with w an auxiliary witness chosen existentially, all constraints explicit and fixed once A is constructed, and A-dependent relation tables that globally summarize adjacency. Require:
 - for every YES instance some (pi,w) makes all tests pass;
 - for every NO instance no (pi,w) passes;
 - O(k) tests, degree <=3, polynomial alphabet, randomized construction permitted;
 - if claiming a PCP route, validate rejection probabilities against ALL malformed w, not just canonical honest witnesses.

A minimal toy experiment is to examine input-dependent certificate switching on a cubic expander: whether local relations can coordinate a choice of witness routing that checks Theta(k^2) source edges without explicitly transporting each pair. Count the auxiliary entropy and input-dependent table bits. The fixed-encoder theorem identifies a necessary escape hatch, but provides no existence proof.

**Status:** strict lower bound in a restricted oblivious/fixed-encoder model; newly relevant 2026 LTC reference; no arbitrary PCC compiler or rSPACH proof yet.

## 8. Strengthening to ANY fixed number of queries (PROVED)

Nothing in Sections 2--4 uses 'two' except the upper bound Q^2 on the number of local views. If test s reads at most h coordinates of the fixed input-independent encoded permutation, with fixed positions and arbitrary input-dependent h-ary predicates, then the view Y_s has at most Q^h possible values. The same deleted-edge argument forces each row pair i<j to be determined by at least one local view. Thus

    Pr_pi[|D_s(pi)|>=r] <= min(1,Q^h/(k)_r).

When Q<=k^C and h is a fixed constant, the earlier tail argument gives

    E_pi binom(|D_s(pi)|,2)=O((Ch+1)^2),
    t=Omega(k^2/(Ch+1)^2).

In particular **ANY constant-query oblivious encoding with fixed test positions and fixed polynomial alphabet requires quadratic-many tests** for exact per-permutation compatibility on all PCC instances. Increasing arity from two to three or five by itself does not evade the barrier; neither does encoding such a test as an arity-two gadget. The randomized exact-solution-preserving extension works verbatim with Q^h in place of Q^2. This still says NOTHING against input-dependent existential witnesses or mere decision-preserving reductions.
