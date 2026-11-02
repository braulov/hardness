# Primary-source audit of the Boolean tensor contraction theorem and a surviving single-exponential CSP hypothesis

**Research date: 2026-11-02.** Distinguish (i) theorem statements checked in source, (ii) elementary independently verified reductions, (iii) unverified deep external algorithms, and (iv) proposed hardness assumptions. Related, partly overlapping notes are [33](33_tensor_contraction_sparse_2csp_and_hardness_triage.md) (main earlier technical triage) and [22](22_domain_uniform_bounded_degree_csp_alert_2026_11_02.md) (Nguyen 2026 claim). **Neither the general contraction proof nor Nguyen's entire Lean overlay has been independently reproduced.** This note clarifies exact source dependencies and proposes a replacement hypothesis; it does not claim a new algorithm.

## 1. Directly inspected theorem statements (SOURCE VERIFIED, not theorem proved)

In OpenAI/math, manuscript `preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex`, theorem `thm:tensor-contraction` states:

- a bipartite network with at most C*s **Boolean bit wires**, at most poly(s) vertices, and vertex degree at most ceil(s^(9/10));
- entries in (Z/2^P0 Z)[V]/(V^ell) with 1<=P0,ell<=C*s;
- for fixed constants C,A,b, each local tensor entry computable in time (s+L)^b * 2^(A*s^0.9) and space (s+L)^b;
- a deterministic exact contraction algorithm in (s+L)^O(1) * 2^O(s/sqrt(log s)) bit operations and polynomial space.

The accompanying full proof appears in the source `build/quantitative-contraction.tex` and contains lemmas for a Cauchy deformation, tapered Hermite recovery and weighted mode enumeration/recursion. We checked presence of these explicit intermediate claims, and the syntactic recursion dependencies, **not their full mathematical correctness**.

The currently stated OpenAI Lean scope at `lean/docs/378.md` is **narrower**: exact counting of fixed-width k-CNF with bound 2^O_k(n (loglog n)^2/sqrt(log n)) times poly(L). It does NOT certify `thm:tensor-contraction` as a formalized theorem in that scope.

Independently, Anthropic/formal-math at pinned revision `16a5ce41304fcdaea4e0be7c132e1c361dc26da5` has real Lean declarations `ExplicitCost.recursionSolves` and `CountedInstance.theRecursionMeetsTheHypothesis` in `eth/proof/rates/CountedRecursion/Main.lean` and `eth/proof/variables/CountedInstance/Main.lean`, respectively. The declarations are theorems assembled from earlier proof components, not merely listed assertions. We fetched these source files, but did NOT replay the build or audit the entire dependency closure. Nguyen, `hexagon:2611.00004v1`, asserts a further domain-uniform finite-machine Lean formalization importing these ingredients, but the new overlay/receipts have NOT been independently inspected here.

## 2. Independently checked CSP->Boolean-network reduction (PROVED, elementary)

Let a binary CSP have v named variables, m explicitly tabulated constraints, and a common domain [q], q>=2. No bound on the primal maximum degree is necessary. Set b=ceil(log_2(q)) and create b Boolean incidence bits for every occurrence of every CSP variable in a relation table and b bits for each original CSP variable's legality test. For every original variable x and bit index j, enforce equality among its copies using a tree of ternary equality tensors, which has O(deg(x)+1) wires/vertices and bounded degree 3 (degree-one and degree-two cases use obvious copy/equality tensors). Encode valid domain elements in a unary arity-b tensor, and each original binary relation in a 2b-port tensor. Make the tensor network bipartite by subdividing each wire once.

Then:
- **bit-wire count** M=O((v+m)*b), including isolated variables;
- number of tensors O((v+m)*b);
- maximum local degree max(2b,b,3)=O(log q);
- local-entry evaluation by equality/legality or one explicit R_e lookup in time poly(input length);
- integer contraction exactly equals #CSP, because every legal original assignment has a UNIQUE extension across copy trees, and illegal ones have weight zero;
- over Z/2^P0 Z with P0=v*b+1, the least residue is the exact nonnegative count because 0<=#CSP<=q^v<=2^(vb)<2^P0.

For q=v^O(1), m=O(v), s=Theta((v+m)*b) satisfies max degree O(log v)<=s^0.9 and P0=O(s). **If** the OpenAI full contraction theorem is correct, its application is valid and yields

    T(v,m,q,L) = poly(L) * 2^O((v+m)*log q / sqrt(log((v+m)*log q))).

In particular m=O(v), q=v^Theta(1):

    T=poly(L)*2^O(v*sqrt(log v))=poly(L)*q^O(v/sqrt(log v)).

No assumption Delta<=3 is necessary in this **linear-edge-count regime**. Thus conditionally refuting SPACH requires only the full OpenAI contraction theorem, not the newly claimed q-uniform Nguyen theorem. Both approaches share tensor-recursion foundations and are NOT independent verifications of one another.

## 3. A slightly wider edge-count regime (NEW PARAMETER OBSERVATION; conditional)

For fixed a>=0, take m=O(v*(log v)^a), q=v^Theta(1). Then M=O(v*(log v)^(a+1)) and the claimed time simplifies to

    T=poly(L) * 2^O(v*(log v)^(a+1/2)).

Hence for **any fixed a<1/2** it is still 2^o(v log v). A proposed no-2^o(v log v) lower bound on CSP with up to v*(log v)^a constraints is therefore ALSO false if the full tensor theorem is correct. At a=1/2 the displayed bound becomes 2^O(v log v) and ceases to refute that proposed lower bound. This calculation does NOT claim a matching lower bound, nor that the transition is sharp for arbitrary algorithms.

## 4. Surviving candidate: NoSingleExpSparseCSP (UNPROVED; randomized variant included)

Choose a fixed positive integer c (one may start with c=1) and define q_v=ceil(v^c). Let S_c be *all* binary CSPs with v variables, m<=3v constraints, maximum primal degree<=3, alphabet [q_v], and explicit tables. Input length is v^O(1).

Define **NSE-SCSP(c)** as:

    There does NOT exist any fixed deterministic machine and constants A,B
    such that for every instance I in S_c,
       time(I) <= 2^(A*v) * |I|^B
    for all sufficiently large v.

Define **rNSE-SCSP(c)** by excluding bounded-error (success >=2/3) randomized machines with the same running-time form on all I in S_c. Randomized exclusion is a stronger conjecture than deterministic exclusion; a deterministic 2^O(v) algorithm refutes both.

For polynomial q, this is equivalent in exponent SCALE to excluding q^{O(v/log v)} poly(L) algorithms (with all fixed constants permitted), **not** merely excluding q^{o(v/log v)} poly(L). Important logical distinction:

    no q^{o(v/log v)} rules out 2^{o(v)}, but DOES NOT rule out 2^{A*v};
    no q^{O(v/log v)} rules out every 2^{A*v} (for any fixed A).

The claimed upper bound q^{O(v/sqrt(log v))}=2^{O(v sqrt(log v))} is compatible with rNSE-SCSP(c). Compatibility does NOT constitute evidence for hardness. If any newer algorithm achieves 2^O(v) on this class, this candidate also fails. The conjecture is independently falsifiable.

A stronger *family* of candidates for beta<1/2 could exclude 2^O(v(log v)^beta) algorithms; the present minimal target beta=0 suffices to conditionally rule out single-exponential HOM after an appropriate reduction.

## 5. Exact HOM transfer template (PROVED CONDITIONAL IMPLICATION; reduction is NOT supplied here)

Suppose for some c there is a polynomial-time, decision-preserving reduction R mapping every I in S_c with v variables to ordinary uncolored graph HOM(G_I,H_I), satisfying:
- |V(G_I)|<=A*v for a constant A independent of v and I;
- |V(H_I)|<=v^B for some fixed B;
- target degeneracy degen(H_I)<=2 (or any specified constant);
- NO use of external unary lists unless eliminated correctly within these parameters.

If there were a uniform algorithm for this resulting HOM class in time 2^(C*|V(G)|)*poly(|V(G)|+|V(H)|), for some fixed C, compose it with R. By |G|=O(v) and h=v^O(1), the total is 2^O(v)*poly(|I|), contradicting NSE-SCSP(c). Same for randomized algorithms against rNSE-SCSP(c); polynomial-time randomized reduction errors must be included and amplified appropriately.

**The source-to-HOM reduction is a substantive OPEN / audit item**, not established by writing this implication. Check actual paper gadget sizes and list removal separately; do not assert degeneracy two or source linearity without a proof. If |G|=O(v log v), the implication rules out 2^O(|G|/log |G|) rather than all 2^O(|G|) solvers.

Also note that the full tensor theorem itself gives fast counting for sparse-source HOM: if |E(G)|=O(|G|), h=poly(|G|), then HOM is sparse binary CSP and has conditional 2^O(|G| sqrt(log |G|)) time independent of target degeneracy. It is not a single-exponential algorithm.

## 6. Next independent audit

A. Verify the correctness, not only the text, of the deep tensor-contraction lemmas from `quantitative-contraction.tex`, especially tapered Hermite precision loss and mode-expansion divisibility; reproducing Nguyen's Lean build without untrusted axioms would be a second route. No such complete check was performed here.

B. Search independently for ANY 2^O(v) CSP algorithm on degree<=3, q=v^c: the new hypothesis would fail if such an algorithm is known.

C. Check an actual CSP->HOM construction with |G|=O(v), h=poly(v), and degen(H)<=2. Avoid presuming that generic relational incidence gadgets remove lists with linear-size pattern and keep degeneracy two; this is the central nontrivial transfer.

D. If any evidence refutes full tensor theorem, return to previous SPACH/CEH branches only after locating the precise failed hypothesis. Retain conditional statements until external claims are validated.
