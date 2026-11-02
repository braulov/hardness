#!/usr/bin/env python3
"""Sanity tests for PCC with forbidden-pair biclique covers.

Run: python experiments/41_pcc_biclique_cover_sanity.py
Tests 1200 random small instances against all permutations, and the
explicit linear-rank vs Boolean-cover separation at K=4,8.
"""
from itertools import permutations, product
from random import Random


def contains_perfect_matching(k, forbidden_positions):
    adj = [[a for a in range(k) if (i, a) not in forbidden_positions]
           for i in range(k)]
    partner = [-1] * k

    def augment(i, seen):
        for a in adj[i]:
            if not seen[a]:
                seen[a] = True
                if partner[a] < 0 or augment(partner[a], seen):
                    partner[a] = i
                    return True
        return False

    return all(augment(i, [False] * k) for i in range(k))


def solve_by_cover(k, bicliques):
    for decisions in product((0, 1), repeat=len(bicliques)):
        deleted = set()
        for (left, right), side in zip(bicliques, decisions):
            deleted.update(left if side == 0 else right)
        if contains_perfect_matching(k, deleted):
            return True
    return False


def exhaustive(k, bicliques):
    forbidden = set()
    for left, right in bicliques:
        for i, a in left:
            for j, b in right:
                if i < j:
                    forbidden.add(((i, a), (j, b)))
                elif j < i:
                    forbidden.add(((j, b), (i, a)))
    for pi in permutations(range(k)):
        if all(((i, pi[i]), (j, pi[j])) not in forbidden
               for i in range(k) for j in range(i + 1, k)):
            return True
    return False


def rank_mod(matrix, p=101):
    a = [[x % p for x in row] for row in matrix]
    n, m = len(a), len(a[0])
    rank = 0
    for column in range(m):
        pivot = next((i for i in range(rank, n) if a[i][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][column], -1, p)
        a[rank][column:] = [(x * inv) % p for x in a[rank][column:]]
        for i in range(rank + 1, n):
            factor = a[i][column]
            if factor:
                a[i][column:] = [
                    (x - factor * y) % p
                    for x, y in zip(a[i][column:], a[rank][column:])
                ]
        rank += 1
        if rank == n:
            break
    return rank


def high_rank_example(k):
    assert k >= 4 and (k & (k - 1)) == 0
    half = k // 2
    left = [(i, a) for i in range(half) for a in range(half)]
    right = [(i, a) for i in range(half, k) for a in range(half, k)]
    r = (len(left)).bit_length() - 1
    assert 2**r == len(left) == len(right)
    b = [[0] * (k*k) for _ in range(k*k)]
    for idx, x in enumerate(left):
        for jdx, y in enumerate(right):
            if idx & jdx:
                a, c = x[0]*k+x[1], y[0]*k+y[1]
                b[a][c] = b[c][a] = 1
    return r, b


def main():
    tests = 0
    for k in range(3, 7):
        rng = Random(k)
        for _ in range(300):
            bicliques = []
            for _ in range(rng.randrange(6)):
                rows = list(range(k))
                rng.shuffle(rows)
                cut = rng.randrange(1, k)
                left_rows, right_rows = rows[:cut], rows[cut:]
                left = {(i, a) for i in left_rows for a in range(k)
                        if rng.random() < 0.4}
                right = {(i, a) for i in right_rows for a in range(k)
                         if rng.random() < 0.4}
                bicliques.append((left, right))
            assert solve_by_cover(k, bicliques) == exhaustive(k, bicliques)
            tests += 1
    print(f"OK: {tests} random PCC instances vs brute permutations")

    for k in (4, 8):
        r, b = high_rank_example(k)
        rank = rank_mod(b)
        assert rank == k*k//2 - 2
        print(f"K={k}: r={r}, ordinary rank={rank}, expected={k*k//2-2}")


if __name__ == "__main__":
    main()
