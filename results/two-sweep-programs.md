# Two-sweep branching programs: feature spans and exact boundaries

**PROVED.** A deterministic program reads each of p Boolean inputs once in its first sweep and once in an arbitrary second order. Transitions may be irreversible. The first sweep starts at a fixed state and ends at F(x); H_s(x) means the second sweep accepts when started in s. Acceptance is the disjoint union of [F(x)=s]H_s(x). Widths and transition tables are explicit. These results do not apply automatically to unrestricted read-many programs.

## Relative feature-span lemma

Suppose a feature vector Φ(x)∈K^M over an effectively represented field has an explicit initial vector and linear update maps for each input-bit choice in the second order. Assume every first-sweep endpoint indicator f_s=[F=s] is a linear functional of the final features. The coefficients need not be known; the promise and an efficient first-sweep evaluator suffice.

At each state of the second sweep retain a basis **selected from actual reachable feature vectors**, along with their concrete input prefixes. For bit i=b apply its linear map to each representative, send it through the BP transition, and retain a maximal independent subset at each resulting state. Linearity proves inductively that the stored vectors span all reachable features. At accepting states, select at most M actual full assignments spanning the accepted feature space.

For each middle state s, run this construction on H_s, then evaluate the original first sweep on all representatives. If f_s is nonzero on an accepted assignment, it cannot vanish on the whole spanning set. Conversely every returned compatible representative is an actual witness. This gives deterministic SAT and witness search in poly(p,w,M) field operations, including an extra factor for the possible middle states.

**The compression preserves existence, not integer multiplicities.** Replacing all assignments by a vector-space basis is not a counting algorithm. The algorithm must retain actual independent generators, not interpret arbitrary reduced linear combinations as assignments.

## Three useful feature families

**Low Boolean degree.** If every f_s has multilinear degree at most D over F₂, use Φ_S(x)=∏_{i∈S}x_i, |S|≤D, including S=∅. Treat unread variables as zero. Reading i=b maps a coordinate to itself if i∉S and to bΦ_{S\{i}} if i∈S. The maps are linear. There are M=Σ_{j≤D}binom(p,j) coordinates, giving p^{O(D)}poly(p,w) time. No ANF coefficients are required.

For a first sweep in UT_d(F₂), matrix entry (i,j) has degree at most j−i: a product contribution follows a strictly increasing coordinate path. Equality to a fixed group element has degree at most Σ_{i<j}(j−i)=binom(d+1,3). Any efficiently evaluable action inherits this bound by summing disjoint group-element indicators. For the natural action on {(u₁,…,u_{d−1},1)}, the endpoint indicator has the better degree d(d−1)/2. Fixed d gives polynomial SAT against any read-once second sweep; polynomial width and d=O(log p) give subexponential time.

**Product features.** If all f_s lie in the span of explicit products ∏_i h_{ij}(x_i), j≤M, start each feature at one and multiply its coordinate by h_{ij}(b) on reading i=b. These diagonal updates work even with zero factors, and in every read order.

**Affine first sweep.** Over F_q, transitions z↦a_i(x_i)z+t_i(x_i), a_i≠0, give

$$
F(x)=z_0\prod_i a_i(x_i)+\sum_i t_i(x_i)\prod_{j>i}a_j(x_j).
$$

There are p+1 product terms. Since [F=s]=1−(F−s)^{q−1}, products of q−1 terms from these and the constant feature span every indicator. At most 1+binom(p+q,q−1) features suffice. The runtime is p^{O(q)}poly(p,q,w); fixed q is polynomial. In particular AGL(1,3)=S₃ handles any reversible three-state first sweep against an arbitrary second sweep. This is a decision theorem, not exact integer counting.

## Fourier support can be found, rather than supplied

Over F₃ let P_i^b be first-sweep transition matrices. The vector of endpoint Fourier coefficients at α∈F₂^p is

$$
2^{-p}(P_p^0+(-1)^{\alpha_p}P_p^1)\cdots
       (P_1^0+(-1)^{\alpha_1}P_1^1)e_{s_0}.
$$

For a frequency prefix, test whether any extension is nonzero by propagating the span of the prefix vector through both remaining matrices at every step. Dimension is at most the first width. A depth-first traversal keeps only prefixes with a nonzero extension, and visits O(pm) nodes when m frequencies occur in the union of all endpoint supports. Thus the support is enumerable in poly(p,w,m) operations. Parity characters are product features, giving SAT in the same output-sensitive polynomial bound. No assumption about real Fourier coefficients is needed.

## Width two: exact counting is polynomial

Every map on two states is identity, swap, reset-to-zero, or reset-to-one. Each input has a unique last reset position j, with j=0 if none. After that reset, the endpoint is its reset value XOR the parity of later swaps; for j=0 it is the start value XOR all swaps.

For each j and each guessed middle state, run DP through the second read order. Enforce the unary transition-type requirements at j and after j; track the second state, swap parity, and reset value. At the end check endpoint consistency and acceptance. Each accepted input is counted for exactly one j and one middle state. Time is O(p²w) arithmetic operations with O(p)-bit counts. Arbitrary second width and irreversible second transitions are allowed.

The same last-reset argument works when the first maps are constants or members of a supplied small abelian permutation group: track the commutative suffix product. It requires explicit efficient group operations, not merely a promise that the maps generate an abelian group of unspecified size.

## Width three: irreversible transitions can encode 3-SAT

Replace every literal occurrence of a 3-CNF by its own Boolean input. In the first sweep group occurrences by variable; states {0,1,dead} remember the first value and reject mismatches. In the second sweep group by clause: remember whether a literal has already satisfied the clause, reject a failed clause when starting the next, and accept iff the last clause succeeds. Signed literals determine transition truth values; dead is absorbing. A consistent occurrence assignment corresponds uniquely to a source assignment, provided unused source variables are removed (their counting factor is 2^u).

This is a parsimonious reduction with p equal to the number of literal occurrences. To make variable groups of length at most three, use one source copy per occurrence and a directed cycle of implication clauses to enforce equality; each copy occurs once in the original formula and twice in the cycle. The blowup is linear in formula length. Thus width-three two-sweep SAT is NP-complete and counting is #P-complete. This does **not** establish an input-efficient reduction from arbitrary Circuit-SAT, nor a subexponential lower bound without a suitable hypothesis.

A particularly simple endpoint language, ∏_{i=1}^k[a_i=b_i] in interleaved order, has a width-three first sweep. Flattening its tensor across a|b gives I_{2^k}; any explicit product-feature decomposition over any field needs at least 2^k terms. This refutes a universal small **product-feature** representation, not all possible algorithms.

## Easy decision can coexist with hard counting

There is a fixed-width class with an S₃ first-sweep action and arbitrary read-once second sweep for which SAT is polynomial by the feature lemma, but exact counting is #P-hard under metric reductions.

Here is the counting identity supporting the claim. Let A=(12), B=(23), C=(12), r=[A,B]. For Boolean a,b,c, [[A^a,B^b],C^c]=r^{2abc}; its inverse gives r^{abc}. For each clause of a 2-CNF, let a_j,b_j indicate falsity of the two literals. A selector (u_j,v_j)∈{00,10,01} encodes the trit 2u_j+v_j. Multiply the two gadgets to obtain r^{Σ_j(2u_j+v_j)a_jb_j}. Replace every gadget occurrence by a separate input bit. The first sweep implements the permutation word; the second checks equality of copies and valid selector codes. A five-state checker (two remembered bits and a dead state) suffices, giving product width 15.

If x satisfies the formula, all 3^m selectors return the register to its initial state. Otherwise exactly 3^{m−1} do. Consequently

$$
\#\mathrm{BP}=3^{m-1}(2^n+2\#F),\quad m\ge1.
$$

Exact #2SAT can be recovered arithmetically. The use of fresh occurrence inputs is essential: the target parameter is word length, not the original number of source inputs. No complexity-class separation or novelty is claimed.

Provenance: original notes 23 and 30–32 in the [history](https://github.com/braulov/hardness/tree/c994435b692c37958eeff2c997188603dcaeddb6/docs). Reproducible finite checks: `scripts/check_lowdegree_twosweep.py`, `scripts/check_affine_s3_hardness.py`. Related established methods include linear-span propagation for algebraic branching programs and representative families; literature priority of these formulations remains unverified.
