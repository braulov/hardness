# Rank-dual algorithms and local bucket obstruction (2026-11-02)

Status: elementary exact-counting lemmas + a model-restricted combinatorial obstruction. No general algorithm for all critical-density binary CSP is claimed.

Let a binary CSP have k variables, q=k^c values, m=Theta(k sqrt(log k)) constraints, and relation matrices R_e in {0,1}^{q x q}. Write r_e=rank_Q(R_e).

## A. Unconditional rank-dual exact counting

By integer Smith normal form, compute in polynomial bit complexity R_e=A_e B_e with A_e integer q x r_e and B_e integer r_e x q. For vertex v define T_v(j_e: e incident to v)=sum_{a in [q]} product_{e incident to v} F_{e,v}(a,j_e), where F is the appropriate endpoint factor A or B.

Expanding the products proves exact integer identity:
#SAT = sum_{j_e in [r_e] for all e} product_v T_v(j_e: e incident to v).

Modulo 2^P for P=k ceil(log2 q)+1 the count is uniquely recovered. Enumerating edge indices gives unconditional time poly(L,k,q) * product_e r_e. In particular sum_e log r_e=o(k log k) implies q^{o(k)} polynomial-input time. With m=O(k sqrt(log k)), it suffices that every r_e <= 2^{o(sqrt(log k))}, uniformly.

For any supplied U subset of variables, enumerating assignments to U and then using rank-dual counting on the residual gives time poly(L) q^{|U|} product_{e inside V\U} r_e. Thus an efficiently identifiable o(k)-vertex cover of high-rank edges can make a heterogeneous instance easy.

Reference: Kannan–Bachem, Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix (1979), DOI 10.1137/0208040. This rank representation is not claimed novel.

## B. Unconditional sparse-partner enumeration

If every row and column of every relation has at most d allowed partners, pick a spanning tree in each component, try q root values, propagate at most d choices per tree edge, and verify non-tree constraints. This takes poly(L,k) sum_components q*d^{size-1}. Hence d=k^{o(1)} implies q^{o(k)} for q=k^c, regardless of m. Permutation-matrix relations have r_e=q but d=1; full rank alone is not a hardness certificate.

## C. Small-support bucket no-go (restricted architecture)

For fixed eps,delta>0 choose G~G(k,p) with p=sqrt(log k)/k. With high probability m=Theta(k sqrt(log k)) and EVERY vertex subset S of size at most k^{1-eps} spans at most (1+delta)|S| edges. Proof: for s=|S| and t=ceil((1+delta)s), union-bound over S and t candidate edges gives at most [C_delta (sqrt(log k))^{1+delta} (s/k)^delta]^s; summing s<=k^{1-eps} gives o(1).

Partition edges adaptively into buckets E_i with touched vertex supports S_i each of size at most k^{1-eps}. Local sparsity gives sum_i |S_i| >=m/(1+delta). In a RAW-VALUE bucket scheme each bucket receives a q-valued copy per touched vertex and equality-copy wires identify copies of the same variable. At least (sum_i|S_i|-k) log2(q)=Omega(m log q) bit-wires are required. Thus no superconstant wire saving is possible in this restricted scheme for the sampled graphs, even with graph-dependent buckets.

This DOES NOT rule out algebraic mixing, global cancellations, arbitrary tensor networks, or decision-only representations. It directly explains why naive projected-support edge-bucket batching does not automatically improve arbitrary critical-density CSP.

## D. Research status

For full-rank, dense allowed-pair tables on m=k sqrt(log k) edges, both simple rank-dual enumeration and sparse-partner branching may take q^{Theta(k)} or worse. The externally claimed 2026 tensor bound gives only q^{O(k)} at this density. A q^{o(k)} algorithm for all such CSP is OPEN.

Previous notes: docs/12_projected_support_edge_buckets.md, docs/33_tensor_contraction_sparse_2csp_and_hardness_triage.md, docs/35_critical_density_csp_to_degen2_hom.md.
