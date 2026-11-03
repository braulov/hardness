#!/usr/bin/env python3
"""Exact finite check of note 51's expected close-near-solution-pair identity.

Run: python3 experiments/51_nearsolution_close_pair_formula_sanity.py
The test graph is K_{3,3}, girth 4, so no asymptotic high-girth theorem
is being tested; only the exact counting formula is checked.
"""
from itertools import product
from math import isclose


def main():
    k = 6
    graph = [(u, v) for u in range(3) for v in range(3, 6)]
    removed = (0, 3)
    remain = [edge for edge in graph if edge != removed]

    for q in (2, 3):
        p = q ** (-2 / 3)
        assignments = list(product(range(q), repeat=k))
        radius = k // 2

        direct = 0.0
        for sigma in assignments:
            for tau in assignments:
                if sigma == tau:
                    continue
                if sum(a != b for a, b in zip(sigma, tau)) > radius:
                    continue
                distinct_requirements = sum(
                    (sigma[u], sigma[v]) != (tau[u], tau[v])
                    for u, v in remain
                )
                direct += p ** (len(remain) + distinct_requirements)

        cut_formula = 0.0
        for mask in range(1, 1 << k):
            T = {v for v in range(k) if (mask >> v) & 1}
            if len(T) > radius:
                continue
            delta = sum(
                (u in T) != (v in T) for u, v in graph
            )
            touches_removed = any(v in T for v in removed)
            cut_formula += (
                q ** (2/3) * (1-1/q) ** len(T)
                * q ** (-delta/3 + (2/3) * int(touches_removed))
            )

        print(f"q={q}, direct={direct:.12f}, cut_formula={cut_formula:.12f}")
        assert isclose(direct, cut_formula, rel_tol=2e-9, abs_tol=2e-9)

    print("OK: finite close-pair expectation matches the exact cut sum")


if __name__ == "__main__":
    main()
