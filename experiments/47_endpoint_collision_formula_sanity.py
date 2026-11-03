#!/usr/bin/env python3
"""Check note 47's exact endpoint-collision expectation on K_{3,3}.

The graph's girth is only four, so these checks validate the finite
identity, not the asymptotic high-girth expander theorem.

Uses only Python's standard library:
    python3 experiments/47_endpoint_collision_formula_sanity.py
"""
from itertools import product
from math import isclose

K = 6
EDGES = [(u, v) for u in range(3) for v in range(3, 6)]
DELETED_EDGE = (0, 3)
REMAINING = [e for e in EDGES if e != DELETED_EDGE]


def by_disagreement_subsets(q):
    remaining_vertices = [v for v in range(K) if v not in DELETED_EDGE]
    value = 0.0
    for flags in product((0, 1), repeat=len(remaining_vertices)):
        t = {v for v, flag in zip(remaining_vertices, flags) if flag}
        if not t:
            continue
        delta = sum((u in t) != (v in t) for u, v in EDGES)
        value += (q ** (2 / 3)) * ((1 - 1 / q) ** len(t)) * q ** (-delta / 3)
    return value


def by_ordered_pairs_of_assignments(q):
    p = q ** (-2 / 3)
    assignments_by_endpoint_pair = {}
    for sigma in product(range(q), repeat=K):
        endpoint_pair = (sigma[DELETED_EDGE[0]], sigma[DELETED_EDGE[1]])
        assignments_by_endpoint_pair.setdefault(endpoint_pair, []).append(sigma)

    value = 0.0
    for group in assignments_by_endpoint_pair.values():
        for sigma in group:
            for tau in group:
                if sigma == tau:
                    continue
                differing_required_entries = sum(
                    (sigma[u], sigma[v]) != (tau[u], tau[v])
                    for u, v in REMAINING
                )
                value += p ** (len(REMAINING) + differing_required_entries)
    return value


def main():
    for q in (2, 3):
        via_cuts = by_disagreement_subsets(q)
        direct = by_ordered_pairs_of_assignments(q)
        print(f"q={q}: exact-cut-formula={via_cuts:.12f}, direct-pairs={direct:.12f}")
        assert isclose(via_cuts, direct, rel_tol=1e-9, abs_tol=1e-9)
    print("OK: both exact finite first-moment calculations agree")


if __name__ == "__main__":
    main()
