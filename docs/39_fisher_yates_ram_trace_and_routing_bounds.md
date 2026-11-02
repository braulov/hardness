# Fisher–Yates local decoding, exact RAM-trace verification, and routing barriers

**Research date:** 2026-11-02. **Branch:** PCC short-PCP / critical-size sparse 2-CSP.
**Status:** Two elementary model-specific lower bounds and a positive exact reduction with O(K log K) binary constraints (known offline memory-consistency/sorting-network technique). No claimed literature novelty and, importantly, NO PCC PCP with critical O(K sqrt(log K)) proof/compression has been built.

## A. Exact Fisher–Yates coordinate query lower bounds

Take digits a_j∈[j] for j=2,...,K; start at the identity array [1,...,K] and for j=K,K−1,...,2 swap positions j and a_j. Call final permutation π_a.

**Lemma.** Under DIRECT oracle access to the individual digits a_j, a deterministic algorithm computing π_a(1) exactly on all digit strings must inspect ALL K−1 digits in the worst case.

Proof: baseline a_j=j produces π(1)=1. For EACH index j∈{2,...,K}, change ONLY a_j from j to 1. The resulting permutation sends 1→j. The query transcript along the baseline is identical until this changed digit is inspected, so every j must be queried.

Indeed for each i≥2, π_a(i) depends on every a_j for j≥i (to exhibit the relevance of j>i, put a_j=i, and all other a_r=r; to exhibit j=i, put a_i=1). It is independent of earlier steps j<i, which occur after the final value at position i has been fixed. Thus deterministic exact oracle decoding of coordinate i requires exactly K−i+1 individual queries for i≥2 (and K−1 for i=1); an obvious direct simulator achieves those bounds.

**Randomized extension.** A randomized, possibly adaptive decoder for π(1) with worst-case success probability ≥2/3 needs Ω(K) digit queries. Yao distribution: with probability 1/2 take the identity controls; with probability 1/2 choose j uniformly among 2,...,K and change only a_j to 1. A deterministic t-query procedure on the baseline cannot notice the changed digit with probability greater than t/(K−1) under the second case. Its error on the mixture is at least (1−t/(K−1))/2; to have error ≤1/3 requires t≥(K−1)/3. This is a direct-oracle query bound ONLY, not a lower bound for proof-augmented locally decodable representations, and not a bound for the direct-output representation π(i) stored explicitly as proof positions.

## B. Fixed bounded-degree, disjoint-path permutation routing has Ω(K log K) size

Let U be a FIXED graph of maximum degree Δ=O(1), with K designated inputs and K designated outputs (assume distinct marked terminals or adapt endpoint port types), and suppose EVERY π∈S_K is routable by K vertex-disjoint paths joining input i to output π(i). At each vertex, at most C_Δ=O_Δ(1) local configurations of incident-port pairings/endings can be used in a path family. Global local configurations determine at most one terminal matching, so

    K! ≤ C_Δ^{|V(U)|}
    ⇒ |V(U)| = Ω_Δ(K log K).

This also applies to edge-disjoint routing with bounded-degree vertices and explicit local port pairings. It extends elementary binary 2×2 switching-network counting to any bounded-degree **physical path-routing architecture**. It does NOT apply to arbitrary polynomial-alphabet CSP gadgets storing nonrouting global states, where each vertex can have K^{Θ(1)} choices.

A Pippenger O(K)-edge superconcentrator can link any K' chosen inputs to any K' chosen outputs, but the matching between the two sets is not freely prescribed. Therefore it does not contradict the route-counting bound or replace a Beneš network for labelled permutations.

Sources: Pippenger superconcentrators https://doi.org/10.1137/0206022 ; Beneš networks https://doi.org/10.1049/tje2.12037 .

## C. Exact RAM-transcript CSP for decoding ALL Fisher–Yates output positions

There exists a deterministic polynomial-time construction of a binary CSP whose designated inputs are the legal digits a_2,...,a_K and output terminals x_1,...,x_K and whose existential projection is EXACTLY

   x = FY(a),

with O(K log K) variables and constraints, degree at most 3, and common domain size K^{O(1)}. The construction is a simple case of offline RAM trace checking through an oblivious sorting network. It is NOT an improvement over the earlier O(K log K) Beneš exact AllDifferent extension.

**Detailed construction:**
1. Give a symbolic trace of the straightforward O(K)-operation array algorithm. The array is of length K. There are K initial writes (address i, time 0, value i), four memory events per swap (two reads followed by two writes with fixed microtimestamps) and K final output reads. Hence the transcript contains exactly 6K−4 records, each
      (address∈[K], timestamp∈[O(K)], kind∈{R,W}, value∈[K]).
   Each record has polynomial-size domain K^{O(1)}.
2. Locally constrain each swap's four events to reference the addresses i and a_i and carry the same exchanged values: if reads have values u,v, the writes must write v at i and u at a_i. The two readings preceding both writes give correct simultaneous semantics, including the special case a_i=i where addresses coincide. Final read records output the designated x_i.
3. Use a fixed AKS sorting network with O(K log K) comparison gates to sort all records by (address,timestamp). A compare-and-swap of two records can be encoded as a constant-arity relation over 4 input/output record symbols; compile each such gate into O(1) binary relations by a tuple-state variable with alphabet K^{O(1)}. Split four-port states into equality-connected copies to achieve maximum degree 3.
4. In the final sorted order, consecutive records for a common address must reflect the previous write value when reading; writes update the remembered value. As each address has its fixed time-0 initialization, adjacent-record checks suffice. Addresses/time are unique enough to order records unambiguously; simultaneous duplicate-address events use distinct microtimestamps.
5. All variable fan-out is removed by equality-copy paths. The construction is deterministic and preserves exactly the entire input-to-output relation. With canonical typed gate states each input has a unique valid execution transcript and deterministic comparator outputs.

Why sorting checks alone are insufficient: an isolated write may be overwritten before any read and hence may be changed without violating memory-consistency; local swap-operation semantics MUST also be enforced. Both checks together establish soundness.

**Testing:** a direct implementation of operation semantic and sorted-memory checks exhaustively validated ALL Fisher–Yates control strings for K=2,3,4,5,6,7 (2,6,24,120,720,5040 cases). For each trace every individual mutation of a record's value was rejected by the **conjunction** of these two checks. This tests semantic consistency of the designed records, not a fully instantiated 2-CSP/AKS graph; correctness of the standard comparator gadgets is elementary and checked by argument, not exhaustively.

For a practically small constant-size implementation, Batcher bitonic networks give O(K log² K) constraints instead; the AKS size O(K log K) is asymptotic and has enormous constants.

## D. Why this does NOT solve critical PCC PCP

The output values π(i) are now available in designated O(K) symbols, but forcing their consistency with the K−1 swap controls via the exact RAM trace takes O(K log K) auxiliary proof symbols / constraints. This already exceeds the critical O(K sqrt(log K)) size. Moreover, checking arbitrary PCC edge compatibility still naively requires Θ(K²) binary tests of A_ij(π(i),π(j)). The RAM trace solves ONLY the permutation decoding/consistency half.

If a PCP treats the ENTIRE O(K log K) RAM transcript as a proof of length ell=Θ(K log K), with Q=K^{Θ(1)}, then the generic independent-test union-bound sampler needs

   t ≈ (ell log Q) / log(1/s).

At the critical soundness s=exp(-Θ(sqrt(log K))), this is t=Θ(K log^{3/2}K), far outside the O(K sqrt(log K)) target. Even at extremely small soundness s≈Q^{-2}, the generic union bound needs Θ(ell) samples. [The lower limit s≥Q^{-2} assumes every verifier test has at least one feasible accepting local assignment; precomputed empty tests on NO do not obey it.] This is a limitation of this generic sampling proof, **not a universal lower bound on all PCP samplers** (low-VC structure can reduce t, subject to the previously documented compression barriers).

Thus replacing the short Fisher–Yates digits by a naive full execution transcript cannot produce the critical proof system. One would need a DIFFERENT robust code/PCP of the execution with near-linear size, or avoid exposing the entire execution as independent proof positions, plus the genuinely global adjacency compatibility layer.

## E. One more precise bottleneck and links

A sharpened subproblem is: Can one give a **polynomial-alphabet, O(K sqrt(log K))-size (or O(K))** two-query/existential locally checkable extension of the graph of the RAM function FY(a) while keeping a useful positive robustness guarantee? This is a meaningful structural target, but by itself still would NOT yield PCC compatibility. Standard comparator-only sorting networks cannot achieve o(K log K) for all input orderings: the information-theoretic log(K!) comparison lower bound applies. This lower bound does NOT cover general finite-field arithmetic, richer constraint tables, or nondeterministic/non-comparison verification; don't overstate.

Potential relevant work: low-overhead offline RAM/ORAM and sorting circuits, https://www.wisdom.weizmann.ac.il/~naor/PAPERS/oram_lower.pdf ; note that online cryptographic memory-checker lower bounds are for a DIFFERENT model and do not automatically apply to exact existential CSP proof graphs.

**Research verdict:** proof infrastructure clarified and tested, but no new asymptotic compiler improvement and no critical two-query PCC PCP. Given the already available Beneš O(K log K) exact AllDifferent encoding, further incremental optimization of this *decoding-only* subroutine has limited value unless tied to a simultaneous new global compatibility mechanism.
