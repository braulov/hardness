# What information actually needs to survive?

The useful common thread is to preserve the observable needed by the algorithm, while proving that the discarded information cannot change its answer. Different observables lead to different valid compressions.

**Existence versus multiplicity.** The feature-span DP keeps actual assignments whose feature vectors span every reachable feature. A linear functional vanishing on the basis vanishes on all assignments; this proves existence preservation. It says nothing about their number. Conversely, rank-cycle expansion keeps signed rational contributions because exact cancellation is part of counting. Treating those summands as independent YES witnesses would be unsound.

**Where cycles matter.** A tree supports arbitrary explicit binary relations and is solved by ordinary DP. The rank-cycle algorithm only decomposes chords, so relation complexity is charged where independent constraints close cycles. This explains why expanding every edge was wasteful. But an expander with permutation relations is still easy: functional propagation defeats the rank measure. A useful parameter certifies an algorithm; it need not certify difficulty when large.

**Decision quotients can discard full-rank detail.** Near-complete or spectrally controlled blocks permit coarse assignments to lift. The fine relation can have full rational rank and many allowed partners per row. The relevant structure is a common coarse labeling plus a proved extension condition, not a low-rank exact representation of all fine assignments. Discovering that labeling is part of the algorithm unless a certificate is supplied.

**Quantifiers explain many failed fingerprints.** A random test rejecting each fixed invalid witness with high probability may still admit a different invalid witness for every seed. In a noninteractive existential CSP, the witness comes after the seed. The fixed-view and all-fields barriers make this issue precise for specific architectures; none justifies a universal impossibility claim about decision reductions.

**Few solutions and global dependence do not measure search cost.** Polynomially many deleted-edge solutions may be hard to locate by available methods, or easy on bounded-treewidth prisms. Conditional Poisson laws, full-edge variance, and arc-consistency failure distinguish information access and propagation models. The prism control prevents converting these statistics into unsupported average-case hardness claims.

**The research opportunity, still speculative.** A useful next algorithm might combine coarse decision quotients, exact propagation, and small residual cycle cost, or find a compact feature space tailored to an intersection of languages. No structural theorem says arbitrary inputs admit such a decomposition. The next contribution must prove a recognition condition, cost decrease, or soundness lemma, rather than just name the desired compressed object.

These insights are supported by the linked proofs in [results](../README.md#established-results) and the restricted [barriers](../README.md#barriers-and-active-directions). The final paragraph is a research proposal, not a theorem.
