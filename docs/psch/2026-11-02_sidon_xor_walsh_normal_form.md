# A universal XOR/Walsh normal form for Clique and the spectral-density obstruction

**Date:** 2026-11-02. **PSCH branch:** B (dense Clique -> few large binary tables / FFT-based global verification).
**Status:** Complete elementary derivations below, plus a small computational sanity check. The induced-Cayley-graph universality is classical **Babai–Sós (1985)**, not a new theorem. The spectral-counting and anti-concentration estimates are routine consequences of the construction and are not presented as literature-novel. Crucially, **no** universal near-linear 2-CSP reduction results.

## 1. Polynomial-size Boolean-group embedding of every graph

For an arbitrary simple undirected graph G with N>=2 vertices, let q=2^{ceil(log_2 N)}, so N<=q<2N. Work in F_q and in its additive elementary Abelian 2-group
    A=F_q × F_q  ≅ F_2^{2 log_2 q},
    |A|=q²<4N².
Label the graph vertices by distinct a∈F_q and set
    φ(a)=(a,a³).

**Sidon difference claim:** for distinct a≠b, φ(a)+φ(b) uniquely determines the unordered pair {a,b}.

Proof: let s=a+b≠0 and t=a³+b³. In characteristic 2,
    t=s³+ab s.
Thus ab=(t+s³)/s. The roots of Z²+s Z+ab are exactly {a,b}; therefore the unordered pair is unique. (This is a difference-Sidon set in the exponent-two group A.)

Define the Boolean graph-defect kernel K_G:A->{0,1} by
    K_G(0)=1;
    K_G(φ(a)+φ(b))=1 iff {a,b} is a nonedge of G, for a≠b;
    K_G(w)=0 on all remaining group elements.
The Sidon property shows this is well-defined. For a,b among the N designated labels,
    K_G(φ(a)+φ(b))=1 iff a=b OR {a,b} is a nonedge.
Thus an arbitrary graph appears as the restriction of a translation-invariant (XOR) compatibility relation on A, with **quadratic group-size blowup** and a kernel of O(N²) explicit bits. Constructing the kernel takes polynomial time using a finite-field representation (find an irreducible polynomial deterministically by standard finite-field algorithms or use randomized preprocessing; for q=2^r and r=O(log N), brute enumeration over O(q) polynomial candidates also gives deterministic poly(N) construction).

**Important caveat:** the candidate vertices of the clique MUST be restricted to the labelled parabola φ(V(G)). The full ambient Cayley graph on A may have extra cliques. This does NOT establish ordinary Clique hardness on unrestricted Cayley graphs.

The underlying induced-Cayley embedding is known: L. Babai and V. T. Sós, *Sidon Sets in Groups and Induced Subgraphs of Cayley Graphs*, European J. Combin. 6(2), 101–114 (1985), https://doi.org/10.1016/S0195-6698(85)80001-9 .

## 2. Exact finite-field Walsh identity for clique selection

Fix an odd prime ℓ > max{k(k-1), binom(N,2)+1}; choosing ℓ=poly(N+k) is elementary (Bertrand); ℓ does not divide |A|=2^{2r}. Let x_1,...,x_k be arbitrary (possibly repeated) candidate vertices. Define the occupancy vector X:A->F_ℓ by
    X(g) = # {i:φ(x_i)=g} mod ℓ.
Define convolution (f*g)(w)=Σ_{u∈A} f(u)g(w+u), where +=− in characteristic-2 group.

The violation count is
    V_G(x) = Σ_{i,j=1}^k K_G(φ(x_i)+φ(x_j)) - k
           = Σ_{w∈A} K_G(w) (X*X)(w) - k.
As an integer, V_G(x) lies in [0,k(k-1)] and is zero iff x_i are all distinct and pairwise adjacent. Since ℓ>k(k-1), reduction to F_ℓ preserves this zero/nonzero criterion.

Let χ:A->{+1,-1} be a group character; these are indexed by the 2r-bit dual space. Define the Walsh transform
    hat f(χ)=Σ_{w∈A} f(w)χ(w).
Over F_ℓ we have the exact identity
    Σ_{w∈A} K_G(w)(X*X)(w)
        = |A|^{-1} Σ_{χ} hat K_G(χ) [hat X(χ)]².

Therefore:
    G contains a k-clique
      iff ∃x_1,...,x_k∈V(G):
          |A|^{-1} Σ_{χ∈Â} hat K_G(χ)
             (Σ_i χ(φ(x_i)))²  = k   in F_ℓ.

The proof is Walsh orthogonality / convolution theorem. This gives an exact *translation-invariant quadratic form* for **every** graph (not just low-rank or structured ones). The coefficients hat K_G can all be precomputed in polynomial time O(|A| log|A|); the **bottleneck is evaluating the witness-dependent quadratic sum using only O(k polylog k) binary CSP gates**.

## 3. The selected-vector autocorrelation itself has quadratic support

For any k distinct candidate vertices, the Sidon property implies:
    (X*X)(0)=k,
    (X*X)(φ(x_i)+φ(x_j))=2 for every unordered i<j,
    and (X*X)(w)=0 elsewhere.
These binom(k,2) nonzero off-diagonal locations are ALL DISTINCT. Thus a naive sparse convolution list contains Θ(k²) distinct pair terms. A generic sparse-output computation does not improve that size simply by working in the XOR domain.

## 4. A typical canonical kernel has ALMOST FULL Walsh spectrum (proved)

Let G be a uniformly random graph on N labelled vertices (independent Bernoulli(1/2) edges). Put L=binom(N,2) and M=|A|=q²=Θ(N²). For any fixed Walsh character χ, over the **integers**,
    hat K_G(χ)=1+Σ_{a<b} η_{ab} χ(φ(a)+φ(b)),
where η_{ab}=1 if {a,b} is a nonedge and 0 otherwise, independently Bernoulli(1/2). Since signs are ±1, the distribution is that of
    1 - c_χ + Binomial(L,1/2)
for an integer c_χ. Consequently
    Pr[hat K_G(χ)=0] <= binom(L,floor(L/2))/2^L = O(1/√L)=O(1/N).
Choose ℓ>L+1, so integer Fourier coefficients of magnitude ≤L+1 vanish mod ℓ exactly when the corresponding integer coefficient is 0.

By linearity:
    E[# zero Walsh coefficients] = O(M/N)=O(N).
Markov: with probability 1-O(N^{-1/2}), there are at most O(N^{3/2}) zero coefficients. Hence a random graph's **canonical** kernel has
    |supp(hat K_G)| = M-o(M)
with high probability. The full M×M Cayley convolution matrix has rank equal to this Fourier support size over F_ℓ, so it typically has almost full rank.

This is NOT a lower bound on the complexity of all algorithms that might exploit convolution; ordinary FFT still computes all M coefficients in polynomial time.

## 5. Stronger robustness: changing unused differences does not yield a uniformly sparse spectral representation

Allow arbitrary K':A->F_ℓ subject *only* to prescribed adjacency/non-adjacency values on the L distinct pair differences φ(a)+φ(b); do not constrain K'(0) or the remaining unused group elements. Distinct graphs give distinct prescribed length-L Boolean patterns.

A function K' with at most d nonzero Walsh coefficients is specified by choosing the frequency support and d values from F_ℓ. The total number of such functions is
    Σ_{j≤d} binom(M,j) (ℓ-1)^j ≤ 2^{O(d log(Mℓ)+log(d+1))}.
With M=Θ(N²) and ℓ=N^{O(1)}, this is 2^{O(d log N)}.

But there are 2^L=2^{Θ(N²)} labelled graphs, and distinct graphs require different prescribed pattern restrictions. Therefore for sufficiently small absolute c>0, a 1-2^{-Ω(N²)} fraction of graphs require
    |supp(hat K')| ≥ c N²/log N
for **every** extension K' agreeing with the graph on all pair differences.

Thus even optimally altering the dummy group positions cannot give O(k polylog k) nonzero Fourier modes for generic graphs when N=k²; the lower bound is
    Ω(N²/log N) = Ω(k⁴/log k).
(The canonical K itself typically has Θ(k⁴) nonzero modes by the previous section.)

This lower bound is for **Fourier-sparse extensions of the pairwise compatibility function**, not arbitrary existential CSP certificates or algorithms. It does not address decision-only target-table compilation with non-Fourier modes.

## 6. Parameter and complexity interpretation

For N=k²:
    |A|=Θ(N²)=Θ(k⁴)          (explicit input-dependent kernel is polynomial)
    witness length = k log N = Θ(k log k)
    selected autocorrelation support = binom(k,2)+1 = Θ(k²)
    canonical Walsh support for random G = Θ(k⁴) w.h.p.
    any correct extension has Walsh support Ω(k⁴/log k) for almost all G.

The group size matches the Θ(k⁴) input edge-bit budget up to constants. A binary CSP relation table with Q=k² can already hold Θ(k⁴) arbitrary bits — storage is not the obstacle. The obstacle is enforcing compatibility of the **same k selected vertices** with near-linearly many relational checks.

This also supplies an immediate PSCH-conditional lower bound for the specially structured *labelled Sidon-XOR k-clique* problem: given (K_G, φ(V(G)),k), decide if k distinct permitted labels have all mutual XOR differences allowed. Any deterministic 2^{o(k/log k)} poly(|A|)-time algorithm on these inputs would refute PSCH, by the polynomial embedding above. It says NOTHING about unrestricted k-Clique in the full ambient Cayley graph without a distinguished candidate subset.

## 7. Status / next problem

No reduction to ordinary bounded-degree 2-CSP with m=O(k polylog k), Q=poly(k) is obtained. Our earlier sum-check and universal-selector QCSP remain useful but cannot be made existential merely by selecting random challenges or a few Walsh frequencies.

**Sharp target**: Find a short *input-dependent existential certificate* for the exact scalar Walsh identity which does not materialize Θ(k²) pair differences or Θ(N²) Fourier modes, and whose verification compiles into O(k polylog k) binary constraints with polynomial alphabet. Alternatively prove a model-restricted lower bound for a meaningful class of Walsh-algebraic circuits containing arbitrary G-dependent relation tables.

## Small sanity check

For GF(8) with irreducible polynomial x³+x+1, confirmed injectivity of unordered pair sums of (a,a³) for N=4,6,8. For N=6,k=3 and 40 random graphs with 20 random ordered tuples each, integer Walsh identity matched direct pairwise violation counts (800 tests). This is a coding sanity check, not independent formal proof.
