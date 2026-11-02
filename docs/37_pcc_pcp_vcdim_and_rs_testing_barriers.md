# PCC PCP: VC-dimension compression tradeoffs and an RS obstruction

**Date:** 2026-11-02. **Status:** elementary conditional deductions from known theorems; no new PCP construction. External 2026 Nguyen algorithm and RPCC hardness are explicitly separate premises. Earlier work: [PCP sampling](18_randomized_low_soundness_pcp_to_linear_csp.md), [VC-dimension](19_vc_dimension_permutation_tests_and_algebraic_dichotomy.md), [critical PCC window](35_domain_uniform_csp_and_critical_pcc_pcp_window.md), [VC→PCC kernelization reduction](36_pcc_short_pcp_alphabet_gap_barrier.md). Novelty not independently checked.

## 1. A crucial improvement to the sampling budget

For any fixed sample of t nonadaptive two-query PCP tests, at most 2t proof positions are ever read. Discard every unused proof position: a satisfying partial assignment on the sampled positions always extends arbitrarily to a full proof. The sampled tests are simultaneously satisfiable iff some full proof passes them.

Thus, after equality-chain occurrence splitting, the sampled standalone binary CSP has O(t) variables and constraints and degree <=3, **not necessarily O(ell+t)** when proof length ell>>t. For an alphabet [Q], and ell=poly(K), t=poly(K), its explicit-table encoding is O(t(Q²+log K)) bits. This matters for low-VC test sampling.

## 2. Universal tradeoff from VC lower bounds on compression

Consider a nonadaptive two-query PCP for K×K Permutation Clique, with uniformly poly(K)-time samplable tests, poly(K) proof positions, alphabet Q<=K^alpha, strong perfect completeness, and rejection gap delta=1-s >=K^(-gamma). For a NO input I, write F_w for the tests rejecting proof w and d_I=VCdim({F_w : w ranges over all proof words}), using the verifier's actual sampling distribution.

Suppose ALL NO inputs obey a uniform bound d_I<=d(K)=O(K^zeta), where zeta>=0 is a fixed constant. Haussler–Welzl random epsilon-net sampling yields
   t=O((d(K)+1)/delta * log(1/delta) + delta^-1 log 3)
    = O(K^(zeta+gamma) polylog K)
tests which with probability >=2/3 hit EVERY NO proof's rejection set. In YES, the same honest proof passes every sample. By Section 1 this is a bounded-error randomized standalone compression of PCC to explicitly tabulated binary CSP of
   B=O(K^(zeta+gamma+2alpha) polylog K)
bits.

There is a deterministic linear-parameter n-vertex Vertex Cover -> PCC(K=n) reduction, and the established Dell–van Melkebeek/Drucker lower bounds prohibit randomized O(K^(2-eps))-bit PCC compression to any language unless NP is contained in coNP/poly. Therefore:
   NP not subset coNP/poly
   => a uniform VCdim upper exponent zeta requires zeta+gamma+2alpha >=2.

This is a statement ruling out a uniform guaranteed upper bound on VCdim across ALL NO inputs; it does **not** claim every individual NO input has large VCdim. For constant gap:
  Q=K^0.5 forbids a uniform VCdim=O(K^(1-eps));
  Q=K^0.6 forbids O(K^(0.8-eps));
  Q=K^0.75 forbids O(K^(0.5-eps)).
The generic upper bound d_I<=ell log_2 Q=O(K log K) when ell=O(K) and Q=poly(K) remains consistent at Q>=sqrt K.

## 3. Stronger conditional tradeoff under Nguyen + RPCC-H

Additional premises:
- Nguyen (2026, externally claimed, not independently replayed): deterministic exact bounded-degree CSP solver poly(L) Q^{O(v/sqrt(log v))}, uniformly in Q.
- RPCC-H: no bounded-error randomized 2^{o(K log K)}poly(K) algorithm for PCC(K).

Consider a PCP with ell=O(K), Q=K^{O(1)}, and constant rejection gap (including soundness exp(-Theta(sqrt(log K)))). If its NO rejection-set families had a uniform computable VCdim upper bound d(K)=o(K sqrt(log K)), an epsilon-net of O(d(K)+1)=o(K sqrt(log K)) tests would suffice. By Section 1 these yield a degree-3 CSP with v=O(d(K)+1), polynomial alphabet. Nguyen would decide it in time
   2^{O(v log K/sqrt(log(v+2)))}poly(K)=2^{o(K log K)}poly(K).
This contradicts RPCC-H.

Hence, assuming both premises, NO proposed critical PCP can guarantee VCdim=o(K sqrt(log K)) uniformly across NO instances. In particular the hoped-for O(K)-VC epsilon-net shortcut is unavailable under those premises. This does not give a lower bound for EVERY NO instance, nor does it verify either premise.

At the critical sampling soundness s=exp(-Theta(sqrt(log K))), the generic union bound already uses O(K sqrt(log K)) tests; the conditional VC obstruction explains why a dramatic reduction of this budget using epsilon-nets would threaten RPCC-H.

## 4. Reed–Solomon's two-query membership trap (unconditional, restricted)

Let C={ (f(a_1),...,f(a_L)) : f∈F_q[X], deg f<d } be a Reed–Solomon code, distinct evaluation points, d>=2. For ANY two distinct coordinates i,j, their pair projection is ALL F_q²: every pair u,v is interpolated by an affine linear polynomial. A 2-query relation-table test intended solely to check membership in C, and required to accept EVERY codeword, must therefore accept EVERY ordered pair at distinct coordinates; same-coordinate queries are automatically satisfied on any word. A randomized collection of such tests cannot reject ANY word outside C.

More generally, for d>=h, projection onto any h distinct coordinates is full by polynomial interpolation; pure h-query code-membership tests accepting every codeword are vacuous.

This excludes the naive approach "RS-encode the full K-row witness, then enforce RS membership by two evaluations and no auxiliary proof". It DOES NOT exclude input-dependent tests accepting only the PCC-valid subset of messages, auxiliary proof variables, nonlinear 2-query LTCs, or higher-query checks. Indeed First–Lazarovici (APPROX/RANDOM 2026) construct good two-query LTCs over alphabets >=3; the result here concerns MDS codes with full pairwise projections, not arbitrary 2-query codes.

## 5. Research recommendation

Do not target a low-VC acceptance pattern for a polynomial-alphabet critical PCC PCP if accepting Nguyen + RPCC-H: such a pattern would allow undersampling and a forbidden fast PCC algorithm. Instead investigate a robust nonlinear input-dependent compatibility layer over an augmented locally testable code with Q=K^a, a>=1/2 and ell=O(K). Precisely quantify soundness against ALL malformed proofs, not only honest codewords, and the test family's VCdim. The local code-consistency problem and global graph-compatibility problem are independent hurdles.

**No short PCP and no universal dense-to-sparse CSP compiler has yet been constructed.**

Sources:
- Haussler–Welzl epsilon-nets: https://www.math.tau.ac.il/~michas/enet.pdf
- Dell–van Melkebeek: https://eccc.weizmann.ac.il/report/2010/038/
- Drucker: https://people.csail.mit.edu/andyd/newlimits.pdf
- Nguyen: https://hexagonmath.org/2611.00004v1
- First–Lazarovici (2026): https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.70
