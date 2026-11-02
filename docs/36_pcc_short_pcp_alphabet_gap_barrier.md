# Short PCC PCP: alphabet/gap barrier from Vertex Cover sparsification

**2026-11-02, PSCH/PCC research, quantitative checkpoint.**

**Status:** elementary parameter-preserving reduction and a conditional corollary of known compression lower bounds (Dell–van Melkebeek; Drucker). No new unconditional PCP construction or sparse CSP compiler. Novelty not audited. **Does not use** the claimed Nguyen/OpenAI tensor theorems.

## Exact reduction VC(n) -> Permutation Clique K=n

Permutation Clique PCC(K) asks whether one may choose positions (i,π(i)) for a permutation π∈S_K such that all selected vertices in different rows are pairwise adjacent.

Given an arbitrary n-vertex graph F and a Vertex Cover threshold ℓ∈[0,n], put K=n, t=n−ℓ. Construct a K×K graph as follows: between rows i,j≤t put an edge between positions (i,a),(j,b) exactly when a≠b and {a,b} is NOT an edge of F; all edges involving a row >t are present. Then

    VC(F)≤ℓ  iff  F has an independent t-set
              iff  PCC(K=n) has a permutation clique.

Proof: the first t selected columns of a solution form the independent set; every independent t-set extends to a permutation by assigning the remaining columns arbitrarily to the other rows. Construction is polynomial in n, with K=n. Exhaustively sanity-checked all graphs with n=2,3,4,5 and ℓ∈[0,n] (6502 pairs).

Therefore n-vertex Vertex Cover compression lower bounds transfer to PCC parameter K: under NP⊄coNP/poly there is no polynomial-time compression into *any fixed target language* of O(K^{2−ε}) bits for any constant ε>0. By Drucker's randomized extension, the same applies to polynomial-time bounded-error randomized compression with constant success probability. These lower bounds are **imported**, not established here.

## Theorem: short two-query PCP alphabet/gap tradeoff

Assume uniformly polynomial-time constructible/samplable, NONADAPTIVE two-query PCC verifiers with:
- ℓ_PCP≤aK proof symbols over an alphabet of size Q≤K^α, α a fixed constant;
- perfect completeness in the same-proof sense (one YES proof passes all tests in the distribution support);
- for NO instances, every proof is accepted with probability ≤s≤1−δ, δ≥K^{−γ};
- each test has at most two queried positions and an explicit Q×Q accepting table constructible in polynomial time, with all input-dependent data generated into the standalone output.

Independently sample

    T = ceil((ℓ_PCP ln Q + ln 3)/ln(1/s))

tests. Perfect completeness makes every sampled YES CSP satisfiable. For each fixed NO proof the probability that all tests pass is ≤s^T; union-bound over Q^{ℓ_PCP} proofs implies a NO CSP with probability ≥2/3. Clone test occurrences and join copies of each proof coordinate by binary equality chains: the resulting binary CSP has O(ℓ_PCP+T) variables/constraints, max degree ≤3, same alphabet Q, and standalone explicit encoding length

    B=O((ℓ_PCP+T)(Q²+log(ℓ_PCP+T)+log Q)).

With ℓ_PCP=O(K), Q≤K^α, δ≥K^{−γ}, and ln(1/s)≥δ:

    T=O(K^{1+γ} log K),
    B=O(K^{1+γ+2α} polylog K).

If 2α+γ<1 then B=O(K^{2−ε}) for some ε>0, contradicting the bounded-error *randomized* compression lower bound for PCC, unless NP⊆coNP/poly.

**Conditional conclusion:**

    NP⊄coNP/poly  =>  2α+γ≥1

is necessary for this family of O(K)-symbol two-query PCPs with NO rejection gap at least K^{−γ}. For constant rejection gap, or soundness exp(−Θ(sqrt(log K))) (gap tends to one), no Q≤K^{1/2−ε} alphabet is possible for any constant ε>0. Q≈sqrt(K) is the first polynomial alphabet scale not excluded by this method; no existence claim is made at that boundary. For fixed α<1/2, the theorem precludes any fixed positive exponent improvement beyond a gap of approximately K^{−(1−2α)} (allowing the usual o(1) exponent slack).

For s=exp(−Θ(sqrt(log K))) and Q=K^α,

    T=O(K sqrt(log K)),
    B=O(K^{1+2α} sqrt(log K)),

so the bit barrier is active exactly for α<1/2.

## Why literal parallel repetition is insufficient

Suppose a base two-query PCP has O(K) positions, polynomial alphabet Q_0=K^a with a>0, and constant soundness s_0<1. Repeating t=Θ(sqrt(log K)) times and literally bundling t old symbols into one new answer, so as to retain two queries, yields Q_new=(Q_0)^t=K^{Θ(sqrt(log K))}, **superpolynomial**.

Starting from Q_0=exp(O(sqrt(log K))) would make bundling polynomial, but such an O(K)-position *constant-gap* base PCP is itself ruled out by the bit-barrier theorem under NP⊄coNP/poly.

This only excludes **literal tuple bundling**; it does not exclude sophisticated derandomized repetition, composition, coding, or algorithms exploiting input-dependent global predicates.

Relevant prior art: Dinur–Meir *Derandomized Parallel Repetition via Structured PCPs*, https://arxiv.org/abs/1002.1606 ; Moshkovitz–Raz *Two-Query PCP with Subconstant Error*, https://eccc.weizmann.ac.il/report/2008/071/ ; Minzer–Zheng *Near Optimal Alphabet-Soundness Tradeoff PCPs*, https://eccc.weizmann.ac.il/report/2024/027/ . None of these high-level statements alone supplies the required PCC-relative ℓ=O(K) short proof.

## Distinct Nguyen/RPCC quantitative restriction

**Separately and only if** Nguyen's new q-uniform CSP counting theorem and RPCC-H are both correct: with a polynomial alphabet Q=K^{Θ(1)} and ℓ_PCP=O(K), achieving soundness s=exp(−ω(sqrt(log K))) via this sampling scheme would generate a degree-3 CSP with o(K sqrt(log K)) variables, hence a 2^{o(K log K)} randomized PCC solver, contradicting RPCC-H. At s=exp(−Θ(sqrt(log K))) one merely gets the compatible upper runtime 2^{O(K log K)}.

Thus the critical speculative target remains: ℓ=O(K), Q=K^a for some fixed a≥1/2, perfect completeness, soundness exp(−Θ(sqrt(log K))), polynomial-time test generation. The Q≥K^{1/2−o(1)} floor comes from standard compression lower bounds; the soundness ceiling comes from the **two additional, currently conjectural/external algorithmic premises**. Do not conflate them.

## Sources
- Dell–van Melkebeek, *Satisfiability Allows No Nontrivial Sparsification Unless the Polynomial-Time Hierarchy Collapses*: https://eccc.weizmann.ac.il/report/2010/038/
- Andrew Drucker, *New Limits to Classical and Quantum Instance Compression*, Theorem 7.11 for graph clique/vertex cover: https://people.csail.mit.edu/andyd/newlimits.pdf ; https://doi.org/10.1137/130927115
- Previously archived parameter window: [note 35](35_domain_uniform_csp_and_critical_pcc_pcp_window.md).

**Status:** This is a conditional restricted-parameter PCP lower bound, not a claim of a new general-purpose lower bound for PCPs.