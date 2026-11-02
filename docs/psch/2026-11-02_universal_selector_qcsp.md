# A one-universal-variable quantified-CSP compiler for dense constraints

**Status (2026-11-02): elementary, fully explicit reduction; not claimed novel.** Companion to the PSCH research checkpoint v7. This is a result for **quantified** CSP, **not** the desired unquantified binary CSP sparsification.

## Theorem (universal-selector compilation)

Let \(\Gamma\) be an explicitly presented finite **binary** CSP with \(n\) source variables, common domain \([q]\), and \(m\ge1\) indexed binary constraints \(R_t(x_{i_t},x_{j_t})\), \(t\in[m]\), with arbitrary explicit tables \(R_t\subseteq[q]^2\). There is a deterministic polynomial-time equivalent quantified binary CSP \(\Gamma'\) having:

- Prefix \(\exists x_1\cdots\exists x_n\ \forall t\ \exists s_1\cdots\exists s_n\).
- Exactly \(n-1+n+1=2n\) binary constraints, plus unary domain restrictions.
- **Tree-shaped primal graph**: the path \(s_1-\cdots-s_n\), with a leaf \(x_i\) attached to \(s_i\), and an extra leaf \(t\) attached to \(s_1\). Maximum degree \(3\) and treewidth \(1\).
- Domains \(D(x_i)=[q]\), \(D(t)=[m]\), and \(D(s_i)\subseteq[m]\times[q]^2\); thus a common alphabet of size at most \(O(mq^2+q)\).
- Perfect decision equivalence: \(\Gamma\) is satisfiable iff \(\Gamma'\) is true.

### Construction

Each hidden state is \(s_i=(t',u,v)\) and is permitted only when \((u,v)\in R_{t'}\). For each \(i\), place a binary relation between \(x_i\) and \(s_i\), requiring

\[
(i=i_{t'}\implies x_i=u)\ \land\ (i=j_{t'}\implies x_i=v).
\]

Connect consecutive hidden states by equality \(s_i=s_{i+1}\). Connect the one universally quantified selector \(t\) to \(s_1\) by the condition \(t=t'\). If original constraints have repeated variables, the two implications are both imposed. Unary state-domain filtering can be expressed with individual variable domains (or with unary CSP constraints).

### Proof

If \(x\) satisfies all original constraints, then for every universally selected index \(t\), set all hidden states equal to \((t,x_{i_t},x_{j_t})\); this state is permitted and all binary checks hold.

Conversely, if the quantified instance is true, fix its first-block assignment \(x\). For any \(t\), the equality chain and selector edge force the hidden states to agree on \(t'=t\); the two guarded leaf relations force \(u=x_{i_t}\) and \(v=x_{j_t}\). The state-domain restriction therefore implies \((x_{i_t},x_{j_t})\in R_t\). Every original constraint holds.

Constructibility follows from explicit tabulation of the polynomial-size alphabets and relations; a naive implementation uses time polynomial in \(n,m,q\), and hence polynomial in the given explicit-CSP representation (for instance, enumerate every proposed state value and candidate leaf value).

### Direct corollary for ordinary k-Clique

Let \(G\) have \(N\le k^2\) vertices. Take \(n=k\), \(q=N\), one binary incompatibility constraint for each pair \(1\le i<j\le k\), with relation \(R_{ij}=E(G)\) (ordered consistently). The theorem gives a tree-shaped \(\exists\forall\exists\)-QCSP with \(2k\) binary constraints and alphabet \(Q=O(k^2 N^2)=O(k^6)\). This construction works for **ordinary** Clique (no input coloring or partition required).

Consequently **PSCH**, as defined in the checkpoint, implies that this very restricted quantified-CSP family has no deterministic algorithm of time \(2^{o(k/\log k)}\operatorname{poly}(|\Gamma'|)\), with \(k\) equal to the number of initial existential variables (and \(\Theta(k)\) total variables). This is only a straightforward conditional hardness transfer, not a newly established circuit lower bound.

### Why this does not solve dense-to-sparse 2-CSP

The universal selector is essential: it asks to check all original constraints, but the existential hidden states can respond separately to each selected index. Removing \(\forall t\) by enumerating all indices restores \(m\) copies of verification (at least \(\Theta(k^2)\) elementary edge checks for dense Clique). The Beneš/AllDifferent example from checkpoint v7 shows that a *special* family of universally indexed pairwise checks can be compiled away using a different existential certificate in \(O(k\log k)\) constraints. The unknown is whether **arbitrary** dense pair-relations admit such a compiler with \(O(k\operatorname{polylog}k)\) constraints and polynomial alphabet.

This is an instance of a standard quantifier-dependent structural-hardness phenomenon. Gottlob–Greco–Scarcello, *The Complexity of Quantified Constraint Satisfaction Problems under Structural Restrictions* (IJCAI 2005), already prove much stronger general results, including hardness for QCSP on trees and alternation-sensitive PH-completeness. No novelty is claimed for the general existence of a hard tree-shaped QCSP.

**Relevant reference:** https://ijcai.org/proceedings/2005/148

### Precision about complexity class

The special family constructed here belongs to NP: guess the \(x\)-block, enumerate all \(m\) choices for the single universal selector, and solve each existential tree-CSP in polynomial time. Thus this construction **does not** obtain a \(\Sigma_2^P\)-complete family; it embeds an NP-hard source into an NP-complete restricted quantified family.

### Focused next research problem

Find a deterministic polynomial-time **existential quantifier-elimination compiler** taking exactly these selector-tree QCSPs (or just the ordinary-Clique subclass) into unquantified 2-CSPs with \(m'=O(k\operatorname{polylog}k)\), \(q'=k^{O(1)}\), and maximum degree \(\le3\), preserving truth. Must not merely unroll each of the \(\Theta(k^2)\) selector values. This formulation permits input-dependent auxiliary values and preserves YES/NO only. It is equivalent in strength to the desired dense-to-sparse compiler once restricted to the original Clique subclass; not evidence that the compiler exists.

**Small-instance check:** the core forced-state equality was brute-tested for 210 graph/parameter cases (all simple graphs on 2, 3, and 4 vertices with clique sizes 2 through \(N\)). This is a sanity check, not a proof substitute.