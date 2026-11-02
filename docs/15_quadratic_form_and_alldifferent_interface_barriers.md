# Permutation Clique: quadratic-form compilation and AllDifferent separator barrier

**2026-11-02 research iteration.** Elementary theorems/lemmas with self-contained arguments; novelty is NOT asserted. This complements docs/13_log_width_sat_and_polynomial_alphabet_csp.md and docs/14_permutation_clique_sparse_2csp_branch.md. The full arbitrary PCC -> O(k)-constraint cubic CSP compiler remains OPEN.

## 1. Quadratic obstruction and modular soundness (PROVED)

Let a_i in [k] be one chosen column for every row i. For i<j, let F_ij(a,b) in {0,1} mark an invalid pair (nonadjacency; include repeated-column conflicts if imposing permutation). Index a Boolean vector X by pairs (i,a), where X_(i,a_i)=1 and all other entries zero. Set the strictly row-upper-triangular matrix B_(i,a),(j,b)=F_ij(a,b) for i<j and zero otherwise. Then

    Q(X)=X^T B X=sum_{i<j} F_ij(a_i,a_j).

The integer Q is in [0, binom(k,2)]. Thus for ANY prime p>binom(k,2), Q=0 as an integer iff Q=0 mod p. A prime p in (k^2,2k^2) exists by Bertrand's postulate (for k>=2) and can be found in polynomial time; p has O(log k) bits.

## 2. Rank-r compiler for arbitrary row-choice compatibility (PROVED)

Suppose rank_{F_p}(B)=r and B is explicitly given. By polynomial-time Gaussian elimination, obtain U,V in F_p^{k^2 x r} with B=U V^T. For a row-choice vector a, calculate for t in [r]:

    s_t = sum_{i=1}^k U_(i,a_i),t;
    t_t = sum_{i=1}^k V_(i,a_i),t.

Then Q(a)=sum_{t=1}^r s_t*t_t mod p. This is computable by O(k(r+1)) fan-in-two lookup/add/multiply operations over F_p. Each lookup table is indexed by (i,a_i,t), with polynomial explicit size. Turn bounded-arity arithmetic gates into degree<=3 binary-CSP constraints: a gate-state symbol records its two input word values and output (domain <=p^3), unary validity restricts the gate state to a correct operation, and binary equality/projection relations attach its wires; clone high-fanout wires along equality paths. Consequently:

    v',m'=O(k(r+1)), maximum degree<=3, alphabet k^{O(1)},

and solution existence is equivalent to the original row-choice compatibility predicate, without a permutation requirement. This works for any r including r=0, and is a polynomial-time deterministic construction on explicitly given matrices. It preserves all row-choice assignments under existential projection (auxiliary arithmetic states are actually uniquely determined by the choices).

To handle genuine Permutation Clique, separate F_ij(a,b) into the *ordinary graph-nonedge* predicate and the column collision condition a=b. Compile the nonedge quadratic obstruction using rank r of its matrix and enforce AllDifferent independently using the known O(k log k) Beneš-network CSP gadget from docs/psch/2026-11-02_full_checkpoint_v7.md. Then the total is

    O(k log k + k(r+1))

constraints/variables, max degree <=3 and polynomial alphabet. In particular r=O(1) gives O(k log k), **not O(k)** due to the separate permutation gadget. Unrestricted PCC generally has r=Omega(k^2).

## 3. High matrix rank does not exclude short existential encoding (PROVED)

Let C_(i,a),(j,b)=[i<j][a=b] be the collision predicate. Then

    C=U_k tensor I_k, with U_k(i,j)=[i<j].

The strict upper triangular all-ones matrix U_k has rank k-1 over every field, while rank(I_k)=k. Therefore

    rank(C)=k(k-1).

Yet satisfying Q_C(X)=0 under row-one-hot constraints is exactly AllDifferent and has an O(k log k) polynomial-alphabet degree-3 existential CSP representation by Beneš. The obstacle posed by rank is **specific to bilinear-factorization compilation**. High rank is not an unconditional lower bound on general existential CSP compilation (indeed the present example disproves that inference).

## 4. Nondeterministic streaming lower bound for AllDifferent (PROVED)

Let L_k be the language over alphabet [k] consisting of all words of length k that are permutations. For k even and S subseteq [k] with |S|=k/2, let x_S list S in ascending order and y_S list [k]\S in ascending order. Then x_S y_S is in L_k, while x_S y_T is not in L_k for any S != T.

Consider ANY NFA for L_k (not just deterministic). For each S choose an accepting run for x_S y_S and note its state immediately after x_S. If S != T had the same midpoint state, splicing the two accepting runs would accept x_S y_T, contradiction. Thus

    #states >= binom(k,k/2)=2^{k-O(log k)}.

The same argument applies to a single forward path of existentially guessed states in a CSP or arithmetic checksum verifier: with alphabet k^{O(1)}, one path-state cannot carry enough information. This forbids the proposed short one-register additive accumulator even with nondeterminism. It does NOT forbid a non-path topology like a high-treewidth cubic graph.

## 5. Exact-projection bounded-treewidth obstruction (PROVED with specified interface assumptions)

Claim: for any binary-CSP encoding that contains k *designated original variables* x_1,...,x_k with domain [k], whose projection to these variables is **exactly the permutation relation**, and whose all domains are at most q, the constraint graph has treewidth t=Omega(k/log q), provided q>=2. Auxiliary existential variables are allowed without restrictions on their number.

Proof sketch. A tree decomposition of width t gives a separator Z of at most t+1 variables splitting the terminals x_i by counts; if |Z|=Omega(k) the bound is immediate. Otherwise, choose two disjoint unions of components left/right, with each containing Omega(k) terminals; fix all x_i in Z to distinct values and fix any terminals outside the two selected unions as necessary. Choose a left side with a terminals and a right side containing the complement of those terminals, where a=Theta(k) and k-a=Theta(k). For each a-subset S of available column values, assign the left terminals bijectively to S and the right terminals bijectively to its complement in fixed canonical order; each full assignment is a permutation, so extends to a satisfying CSP assignment. If two different S,T induce the same satisfying assignment on separator Z, combine the left witnesses from S with the right witnesses from T. This creates a valid global CSP assignment projecting to a nonpermutation (some column repeated/missing): contradiction. Therefore different S require different assignments on Z, giving q^{|Z|} >= binom(k-O(|Z|),Theta(k))=2^{Omega(k)}. Hence |Z|=Omega(k/log q) and t=Omega(k/log q).

**Important:** this is a lower bound for exact projection preserving every permutation and every forbidden nonpermutation. It is NOT a lower bound for arbitrary decision-only reduction of a single PCC instance. In particular, an unconstrained AllDifferent instance is satisfiable and could be replaced by a trivial YES instance if only satisfiability preservation is required.

For q=k^{O(1)}, t=Omega(k/log k). The bound rules out constant-treewidth/low-width gadgets as exact AllDifferent encodings but leaves open O(k)-vertex cubic graphs with high treewidth.

## 6. Research interpretation and next experiments

- Rank factorization gives a complete **positive structured theorem** for low-rank ordinary row-choice compatibility.
- The collision term has rank Theta(k^2) but compact nonlinear existential descriptions, so generic rank lower bounds cannot refute the desired compiler.
- The NFA fooling set shows why simply accumulating a field checksum with one polynomial-size state cannot implement AllDifferent exactly.
- Any successful linear-size polynomial-alphabet AllDifferent gadget, if it preserves the entire relation, must have treewidth Omega(k/log k); investigate fixed-degree expander topologies, not one-dimensional accumulators.
- Continue investigating whether one can compile arbitrary NONEDGE quadratic residual on an expander using existential global consistency without expanding the alphabet, and whether high tensor rank can coexist with a linear witness-check circuit. Do not claim a result for unrestricted PCC.
- Both logSAT-A and logSAT-B are affected only via exact quantitative reduction arrows; these lemmas alone imply no new generic SAT algorithms or hardness.

## Outside references

- Karthik--Marx--Pilipczuk--Souza, *Conditional lower bounds for sparse parameterized 2-CSP: A streamlined proof* (SOSA 2024): https://arxiv.org/html/2311.05913v3
- Lokshtanov--Marx--Saurabh, *Slightly Superexponential Parameterized Problems* (SODA 2011): https://epubs.siam.org/doi/10.1137/1.9781611973082.60
- Bessière--Katsirelos--Narodytska--Quimper--Walsh, *Decompositions of All Different, Global Cardinality and Related Constraints* (IJCAI 2009): https://ijcai.org/proceedings/2009/77
