#!/usr/bin/env python3
"""Checkpoint 47: sharp source-degree tradeoff and randomized affine bypass.

This tests only the unique-clique promise family A(z), not arbitrary PCC
linearization. Run: python experiments/47_decision_only_linear_degree_sanity.py
"""
from math import comb, ceil


def balanced_groups(m: int, r: int, n: int):
    groups = [[] for _ in range(r * n)]
    for edge in range(m):
        groups[edge % len(groups)].append(edge)
    return groups


def exact_compiler_accepts(mask: int, groups):
    # Diagonal vectors are products of assigned input bits; every
    # off-diagonal vector is zero, so identity is the only candidate.
    return all(all((mask >> edge) & 1 for edge in block)
               for block in groups)


def parity_accept(mask: int, m: int, random_mask: int):
    missing = ((1 << m) - 1) ^ mask
    # Output scalar L_R(z) = 1 + <R,1-z> in F_2;
    # the diagonal output vector is nonzero iff parity is even.
    return (random_mask & missing).bit_count() % 2 == 0


def main():
    for k in range(2, 6):
        m = comb(k, 2)
        r = 2
        n = k
        blocks = balanced_groups(m, r, n)
        d = ceil(m / (r * n))
        assert max(map(len, blocks)) == d
        for z in range(1 << m):
            assert exact_compiler_accepts(z, blocks) == (
                z == (1 << m) - 1
            )
        print(f"K={k}: M={m}; r={r}, N={n}, sharp D={d}; all 2^{m} inputs pass")

        if m <= 6:
            for z in range((1 << m) - 1):
                count = sum(
                    parity_accept(z, m, R) and parity_accept(z, m, S)
                    for R in range(1 << m) for S in range(1 << m)
                )
                assert 4 * count == (1 << (2 * m))
            print("  Two independent affine hashes false-accept exactly 1/4")
        else:
            print("  Two-hash acceptance 1/4 follows from independent uniform parities")
    print("All sanity checks passed")


if __name__ == "__main__":
    main()
