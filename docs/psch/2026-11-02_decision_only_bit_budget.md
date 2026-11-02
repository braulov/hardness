# Decision-only bit-budget lower bound for polynomial-size Clique to sparse CSP

**Date:** 2026-11-02. **Branch:** PSCH/B.
**Status:** PROVED conditional consequence of **Dell–van Melkebeek's established Vertex Cover sparsification lower bound**, not a new unconditional or literature-novel theorem. This lower bound is independent of ETH and PSCH. Source refs below.

## Main result (arbitrary decision-preserving compilers)

Assume NP is not contained in coNP/poly.

Let A be a deterministic polynomial-time mapping that on every instance of ordinary k-CLIQUE on a simple graph with N<=k^2 vertices outputs an equivalent instance of **any** fixed decidable target language. For any fixed eps>0 it is impossible for A to output only O(k^(2-eps)) bits on every such input.

In particular, let the target be an explicitly tabulated binary CSP with m constraints on at most Q values per variable, including unary restrictions or per-variable domains. After deleting unconstrained variables, the output has at most O(m) relevant variables and can be encoded using
  B=O(m Q^2 + m log(m+2))
bits (Q>=2), with Q itself encoded in the output and a standard polynomially bounded uniform encoding. More explicitly, an O(m log Q) term for domains may be added if needed; for explicitly listed finite domains of size at most Q, O(m Q) bits are absorbed by mQ^2.
Thus no such compiler can guarantee
  m(Q^2+log(m+2)) = O(k^(2-eps))
on all inputs.

**Proof by a padding-preserving reduction from Vertex Cover.**
Start with any n-vertex Vertex Cover input (F,l), 0<=l<=n. Add n isolated vertices to F obtaining F'. Let H = complement(F') and set k=2n-l. Then
  VC(F)<=l iff alpha(F')>=2n-l iff omega(H)>=k.
Furthermore n<=k<=2n, and H has N=2n<=k^2 vertices for n>=2. The transformation is polynomial time. Consequently, any O(k^(2-eps))-bit mapping from this restricted ordinary Clique problem to *any* target yields an O(n^(2-eps))-bit polynomial-time compression for n-vertex Vertex Cover. Dell–van Melkebeek exclude that unless NP is contained in coNP/poly. QED.

The elementary reduction was also exhaustively checked on all simple graphs of n=2,3,4 vertices and all 0<=l<=n. (This is just a sanity check and does not replace the proof.)

**Consequences for near-linear CSP:**

- If m=O(k log^c k), then Q=O(k^(1/2-delta)) for any fixed delta>0 is impossible under the assumption. (If an explicit unary/domain encoding changes the low-order terms, it remains subquadratic.)
- More generally, for arbitrary m and Q, there can be no universal deterministic size guarantee mQ^2=O(k^(2-eps)) together with m log(m+2)=O(k^(2-eps)).
- The sought reduction with Q=k^C for C>=1/2 is NOT excluded. In particular, Q=k^2 or k^6 leaves room for tables substantially larger than the hard input.

## Stronger implication for **succinctly represented relations**, regardless of Q

Suppose the compiler outputs *succinct* binary relations: a uniform interpreter, independent of the specific source input, can decode a constraint relation from a descriptor of b bits (a Boolean circuit, a field-formula plus numerical parameters, a bitstring program, etc.). The output specifies the constraint graph, domains and one descriptor per relation. Its total output length is
    B=O(m [b+log(m+2)+log Q])
assuming a shared fixed interpreter and an ordinary finite-variable encoding.

The same Dell–van Melkebeek theorem implies this total bitlength cannot be O(k^(2-eps)) for all instances of ordinary Clique with N<=k^2.

Consequently, if m=O(k log^c k), **there can be no universal compiler whose relation descriptors all have length O(k^(1-delta)) bits** for any fixed delta>0, independent of how large polynomial Q is. In particular, O(polylog k)-bit per-relation algebraic parameter descriptions would be too succinct.

This is not a lower bound on the computational *evaluation* cost of each table, nor on all succinct descriptions of individual YES instances. It is a lower bound on the *total input-dependent output description* of a polynomial-time YES/NO-preserving compiler for ALL inputs. An output may include additional advice, code, or an encoded copy of G; all such bits must be counted. An interpreter with free access to the original G is NOT a standalone compression, so is outside the theorem.

## Comparison with previous notes

- Fixed nonlinear code/query no-go (2026-11-02 full checkpoint v5): unconditional but requires an input-independent encoding/check skeleton AND exact membership for each source assignment.
- Exact-extension representation counting: mQ^2=Omega(k^4) in the explicit-table, fixed-projection model (even arbitrary existential helpers); does NOT cover decision-only transformations.
- Planar expander-port separator no-go: unconditional m=Omega(k^2/log^2Q), but requires preserving the entire designated-terminal solution relation.
- **Here:** no fixed skeleton, no planar restriction, no source terminal projection; arbitrary global input preprocessing and existential variables permitted. The lower bound is only a quadratic **bit-budget** restriction and assumes NP not contained in coNP/poly.
- PSCH + planar low-treewidth algorithms yields a different, **time-based** restriction m not o(k^2/log^4 k) for planar targets with polynomial Q; does not imply or follow from this bit-budget result.

The universal target m=O(k polylog k), Q=k^{O(1)}, max degree 3 remains OPEN. Even this lower bound leaves the regime C>=1/2 unconstrained by output bits.

## What cannot be inferred by naive YES/NO counting

Without a polynomial-time restriction on preprocessing, even a one-bit output is possible: an unbounded compiler could decide Clique and output one of two constant CSP instances. Therefore no unconditional information-only count of YES/NO source instances can rule out arbitrary decision-only encodings. The computational bound is essential; the Dell–van Melkebeek cross-composition/communication machinery supplies it.

## Sources

- Dell–van Melkebeek, *Satisfiability Allows No Nontrivial Sparsification Unless the Polynomial-Time Hierarchy Collapses*, JACM 2014; ECCC TR10-038 https://eccc.weizmann.ac.il/report/2010/038/ .
- Jansen–Pieterse, *Sparsification Upper and Lower Bounds for Graph Problems and Not-All-Equal SAT*, Algorithmica 79:3–28 (2017), section 1.1 explicitly restates the n-vertex Vertex Cover lower bound against compression to any language: https://link.springer.com/article/10.1007/s00453-016-0189-9 .


## Randomized compilers: Drucker's extension

The deterministic Dell–van Melkebeek lower bound above extends to randomized polynomial-time **standalone compression algorithms with two-sided error**. Andrew Drucker, *New Limits to Classical and Quantum Instance Compression*, Theorem 7.11 (2012 ECCC revision 2, SIAM J. Comput. 2015), proves: for each integer d>=2 and eps>0, there is a beta>0 such that a randomized compression of d-uniform hypergraph Clique (or d-Vertex Cover) to O(N^(d-eps)) bits, with success probability at least 1/2+N^(-beta), implies NP subset coNP/poly. For d=2 this is ordinary graph Clique / Vertex Cover; constant success 2/3 is certainly sufficient.

The same n-vertex Vertex Cover -> k-Clique padding with k=Theta(n) and N=2n therefore transfers the **subquadratic bit lower bound** also to randomized compilers for ordinary Clique with N<=k^2, as long as the success probability is at least a fixed constant >1/2 and the output is a standalone instance of a fixed target language.

This specifically constrains the earlier randomized PCP-test-sampling -> CSP pipeline: if m=O(k polylog k) and Q=k^(1/2-delta), then the output has O(k^(2-eps)) bits, contradicting NP not subset coNP/poly even when the sampling is randomized. For Q=k^2 or larger this does **not** exclude the proposed near-linear constraint count.

Scope: Drucker's extension is for probabilistic *compression mappings*, not all oracle communication models. It does not require the target CSP itself to be solvable efficiently. A reduction with free continued access to the original input does not qualify as standalone compression.

Reference: Andrew Drucker, *New Limits to Classical and Quantum Instance Compression*, ECCC TR12-112 revision 2, Theorem 7.11 (PDF pages 45–46), https://eccc.weizmann.ac.il/report/2012/112/ ; published SICOMP 44(5):1443–1479, https://doi.org/10.1137/130927115 .
