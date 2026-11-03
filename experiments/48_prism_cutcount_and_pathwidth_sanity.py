#!/usr/bin/env python3
"""Finite independent checks for note 48's easy cubic-prism control family.

For small circular ladder C_s x K_2: enumerate all cuts to confirm
edge connectivity 3 and the cut-sum bound, and validate the explicit
width-5 path decomposition. No third-party dependencies.

    python3 experiments/48_prism_cutcount_and_pathwidth_sanity.py
"""
from itertools import combinations


def prism(s):
    top = list(range(s))
    bottom = list(range(s, 2 * s))
    edges = set()

    def add(a, b):
        edges.add(tuple(sorted((a, b))))

    for i in range(s):
        j = (i + 1) % s
        add(top[i], top[j])
        add(bottom[i], bottom[j])
        add(top[i], bottom[i])
    return 2 * s, sorted(edges)


def verify_bags(s, edges):
    bags = [
        {0, s, i, s + i, i + 1, s + i + 1}
        for i in range(1, s - 1)
    ]
    assert max(len(b) for b in bags) <= 6
    for a, b in edges:
        assert any(a in bag and b in bag for bag in bags), (a, b)
    for v in range(2 * s):
        indices = [j for j, bag in enumerate(bags) if v in bag]
        assert indices and indices == list(range(indices[0], indices[-1] + 1))
    return len(bags)


def cut_statistics(k, edges, q):
    min_cut = len(edges)
    weighted_cut_sum = 0.0
    for mask in range(1, (1 << k) - 1):
        boundary = sum(bool(mask & (1 << a)) != bool(mask & (1 << b))
                       for a, b in edges)
        min_cut = min(min_cut, boundary)
        weighted_cut_sum += q ** (-boundary / 3)
    assert min_cut == 3
    x = (k * k / q) ** (1 / 3)
    assert x < 1
    karger_bound = 2 * (k * k / q) / (1 - x)
    assert weighted_cut_sum <= karger_bound * (1 + 1e-12)
    return min_cut, weighted_cut_sum, karger_bound


def main():
    for s in (4, 5, 6):
        k, edges = prism(s)
        q = 10000
        bags = verify_bags(s, edges)
        min_cut, sum_value, upper = cut_statistics(k, edges, q)
        print(
            f"columns={s} vertices={k} mincut={min_cut} "
            f"path_bags={bags} max_bag=6 "
            f"Xi({q})={sum_value:.9g} Karger_upper={upper:.9g}"
        )
    print("OK: cubic prisms are 3-edge-connected with the stated width-5 decomposition")


if __name__ == "__main__":
    main()
