# What exact encodings cannot compress

The barriers here are **rigorous but model-specific**. Here [PCC](../results/permutation-factors.md) means Permutation Clique. They distinguish preserving every source witness from preserving only whether some witness exists. None proves general PCC hardness or excludes arbitrary polynomial-time decision reductions.

## Fixed views of an input-independent permutation code

Fix an encoder E:S_K→[Q]^ℓ, Q≤K^C, and t tests reading at most h fixed positions each, where C,h are constants. The encoder and queried positions are independent of the PCC input A. The test predicates may depend arbitrarily on all of A. Assume that, for every A and π, all tests accept E(π) iff π is valid. No additional existential proof is allowed.

**Theorem.** t=Ω(K²/(Ch+1)²).

For a test view Y_s(π), let D_s(π) be the rows whose values are fixed throughout its fiber. Delete just the source edge selected by π on rows i,j. Some test must reject π. Every permutation not selecting that edge is valid, so the rejecting fiber fixes both i,j. Thus

$$
\binom K2\le\sum_s\binom{|D_s(\pi)|}2.
$$

A view has at most Q^h fibers. A fiber fixing r rows has at most (K−r)! permutations; for uniform π,

$$
\Pr(|D_s|\ge r)\le\min(1,Q^h/(K)_r).
$$

Summing (r−1) times this tail bounds E binom(|D_s|,2) by O((Ch+1)²): cut at any fixed integer above Ch+3, then use (K)_r≥(K/2)^r for r≤K/2 and the exponentially small remaining tail. Average the preceding inequality to finish.

The argument extends to input-independent random encoders/topologies when, for each input, the **whole solution set** is correct with probability at least 2/3: average the number of correctly represented single-deletion instances. It does not extend just from success on a fixed witness, or from correctness of the YES/NO answer.

**Ways around it:** input-dependent encodings, existential auxiliary states, or preserving only existence. Better distance or testability of a fixed code alone does not supply the missing compatibility checks.

## Exact linear representations can fail over every field

**Theorem.** For sufficiently large even K there is a polynomial-time sampleable family of PCC instances for which, with probability 1−2^{-Ω(K⁴)}, no assignment of one vector to each original candidate, in any finite dimension over any field, satisfies

$$
\pi\text{ valid}\iff\{v_{i,\pi(i)}:i\in[K]\}\text{ independent}
\quad\text{for every }\pi.
\tag{1}
$$

All instances in the family are YES. The theorem is about witness labels, not decision difficulty.

Write K=2s. Split rows into s regular and s filler rows, columns into s default and s active columns. Independently choose every forbidden bit between two regular rows selecting distinct active columns; make all other pairs compatible. There are M=binom(s,2)s(s−1)=Θ(K⁴) bits. For each bit choose a designated permutation using its two active choices, default choices at other regular rows, and remaining columns at filler rows. Only that bit affects its validity. Thus the M designated status bits are independent and uniform. The all-default regular assignment always extends to a valid permutation.

Any representation satisfying (1) can be reduced to dimension K over a field extension: multiply by a generic K×d matrix of indeterminates. Each independent matching has a nonzero projected determinant polynomial; finitely many such polynomials have nonzero product. Over the rational-function field all remain nonzero, while dependent sets stay dependent.

Now the M designated determinants of a symbolic K×K² matrix are integer polynomials of degree K, coefficient height one, in K³ variables. [Nelson's all-fields zero-pattern theorem, §2](https://arxiv.org/html/1605.04288v3#S2) bounds their realizable zero/nonzero patterns across **all** characteristics by 2^{O(K³log K)}. One quantitative way to see the substitution: with B=binom(KM+K³,K³), log₂B=O(K³log K); the coefficient-count form of the theorem is satisfied by a pattern bound T=2^{C K³log K} for large fixed C. This is 2^{o(M)}, whereas our source family realizes all 2^M statuses. Hence the fraction representable is at most 2^{O(K³log K)−M}.

The all-fields step is Nelson's extension; the earlier Rónyai–Babai–Ganapathy result is a fixed-field precursor. That attribution matters when fields may vary with the input.

Moreover, for every ε>0 the same union bound with Hamming balls shows that almost every sampled instance has agreement at most (1/2+ε)M with **every** such linear classifier. Consequently no randomized compiler of this form can correctly label each designated permutation with probability 2/3 on every input. Averaging over the seed and designated permutations would contradict the accuracy bound for one of these inputs.

**Ways around it:** change the candidate universe, introduce auxiliary existential choices, or preserve only decision. The theorem supplies no deterministic explicit exceptional instance with a short all-fields certificate; its existence proof is probabilistic. It does not bar conjunctions of arbitrarily many separate matroid factors.

The same counting proof applies to fixed-degree predicates of additive candidate features. Give each candidate r arbitrary field values, sum them over a permutation, and apply an arbitrary polynomial P of fixed degree d to those r sums. There are H=K²r+binom(r+d,d) scalar parameters. Each designated permutation's output is an integer polynomial of degree at most d+1 in those parameters, with coefficient height K^{O_d(1)}. Nelson's theorem gives at most 2^{O_d(H log K)} patterns. Whenever H log K=o(K⁴), almost every source instance defeats even (1/2+ε)-accurate classification, for every fixed ε>0, over every field. In particular r=O(K), d≤3 is ruled out. This is still preservation of the original permutations' validity, not decision-only compression.

Indeed a size-only counting argument cannot exclude unrestricted decision-only compilation: after solving the input, output a fixed YES representation or a fixed NO representation. Both have polynomial size. Any meaningful barrier to *computing* that choice must restrict preprocessing or use a computational hypothesis.

## A decision-only barrier with an explicit degree restriction

Consider PCC inputs A(z) where only diagonal candidates can participate and their M=binom(K,2) pair edges are Boolean bits z. The answer is AND_M(z). Suppose a deterministic compiler uses a fixed N×N output matching universe and r linear-matroid layers over one fixed field. Each vector coordinate is a polynomial of source degree at most D. It need preserve only decision.

**Theorem.** rND≥M. At z=1 choose an accepting output permutation and one nonzero N×N minor f_j in each layer. Their product has degree at most rND, is nonzero at 1, and vanishes at every other Boolean input because that same permutation cannot be accepted there. Its unique multilinear representative is a nonzero scalar times ∏_e z_e, of degree M. Multilinearization cannot raise degree.

This is sharp on this easy input cube: partition the M bits into rN groups and put the product of each group on its corresponding diagonal basis vector; set all off-diagonal vectors to zero. Degree ceil(M/(rN)) suffices.

**Randomization genuinely changes the claim.** Over F₂ choose two independent masks R,S and put 1+R·(1−z), 1+S·(1−z) on two diagonal vectors, leaving the others as basis vectors. Every YES input is accepted; every fixed NO input is accepted with probability 1/4. Coordinates are affine. Thus the deterministic lower bound does not extend to ordinary bounded-error randomized mappings, even on this same cube. High-degree polynomial-time preprocessing is another escape.

## Public fingerprints do not commute with existential choice

A rejection guarantee for each fixed invalid witness does not bound the event that **some** invalid witness passes after the seed is exposed. There is an explicit NO family defeating low-bit public linear hashes of violated pairs.

Let K=2d+2. Permit permutations within d disjoint 2×2 diagonal blocks and fix two anchor positions a,b. Isolate other candidates. Forbid the pair of anchors e₀, and for each block j forbid e_j between its first row's swapped position and anchor a. Other allowed-position pairs are compatible. Every permutation in this universe is invalid, and its violated pairs are exactly {e₀}∪{e_j:x_j=1}, for an arbitrary swap vector x∈{0,1}^d.

Assign independent uniform b-bit hashes α₀,…,α_d to these violated pairs. The hash accepts a permutation precisely when α₀+Σ_j x_jα_j=0 over F₂^b. A fixed permutation passes with probability 2^{-b}. However the b×d random matrix of α₁,…,α_d has full row rank with probability at least 1−2^{b−d}, by a union bound over nonzero left-kernel vectors. On that event **some** permutation passes for every α₀. Thus if d−b→∞ this restricted randomized compiler falsely accepts this NO instance with probability tending to one. It is not sound merely because its per-witness error is small.

This rules out low-bit, obliviously independent, public linear defect hashing as a standalone existential acceptance condition. It does not cover arbitrary input-dependent hashes, added consistency tests, or commitments. In fact the integer number of violations, reduced modulo any prime greater than binom(K,2), is already one exact scalar zero test. The unresolved cost is computing it through a small interface, not the number of scalar outputs.

For a related local product example, let h(i,a)=11i+a in F₁₀₁, σ=(0 1 2), a=(1,3,5), and r=17. The two products

$$
\prod_i(r-h(i,a_i))=16\cdot3\cdot(-10)=25,
\quad
\prod_i(r-h(\sigma(i),a_i))=5\cdot(-8)\cdot12=25
\pmod {101}
$$

agree with all factors nonzero, although the labels are not constant along σ. As formal polynomials, equality would enforce that consistency because the tags are injective. One evaluation does not.

This example refutes exactness of the local point-evaluation gadget; it does not itself refute every randomized reduction using products. Soundness needs a bound uniform over existential witnesses, a genuine commitment mechanism, or some other proved restriction on their choices.

Provenance: original notes 21, 46–48 and CEH note 05. The first and third proofs are elementary; the second explicitly depends on Nelson's established theorem. Earlier linear-code, finite-field counting, and isolated hash failures are superseded by these more general statements where their models agree.
