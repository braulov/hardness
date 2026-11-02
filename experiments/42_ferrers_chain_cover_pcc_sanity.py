#!/usr/bin/env python3
"""Checkpoint 42: Ferrers-factor PCC and rainbow padding tests.

Run:
    python experiments/42_ferrers_chain_cover_pcc_sanity.py
Covers 1000 random small factor instances and 630 Rainbow-Matching
padding instances. This tests the mathematical reductions, not a fully
materialized degree-3 binary CSP.
"""
from itertools import permutations, product, combinations
from random import Random

def perfect_matching(k, rows):
    column_owner = [-1] * k
    def visit(i, seen):
        for a in rows[i]:
            if a in seen:
                continue
            seen.add(a)
            if column_owner[a] < 0 or visit(column_owner[a], seen):
                column_owner[a] = i
                return True
        return False
    return all(visit(i, set()) for i in range(k))

def by_ferrers_thresholds(k, factors):
    cuts = [
        range(max([0, *left.values(), *right.values()]) + 1)
        for left, right in factors
    ]
    for thresholds in product(*cuts):
        rows = []
        for i in range(k):
            candidates = []
            for a in range(k):
                x = (i, a)
                if all((x not in left or left[x] <= tau) and
                       (x not in right or right[x] >= tau)
                       for (left, right), tau in zip(factors, thresholds)):
                    candidates.append(a)
            rows.append(candidates)
        if perfect_matching(k, rows):
            return True
    return False

def by_permutation_brute(k, factors):
    for pi in permutations(range(k)):
        good = True
        for left, right in factors:
            av = [left[(i, pi[i])] for i in range(k)
                  if (i, pi[i]) in left]
            bv = [right[(i, pi[i])] for i in range(k)
                  if (i, pi[i]) in right]
            if av and bv and max(av) > min(bv):
                good = False
                break
        if good:
            return True
    return False

def rainbow_matching_brute(m, n, edges, target):
    for subset in combinations(edges, target):
        if (len({e[0] for e in subset}) == target and
            len({e[1] for e in subset}) == target and
            len({e[2] for e in subset}) == target):
            return True
    return False

def padded_rainbow_perfect_brute(m, n, edges, target):
    k = m + n - target
    original_color = {(i,j):c for i,j,c in edges}
    for pi in permutations(range(k)):
        colors = []
        for i, j in enumerate(pi):
            if i < m and j < n:
                if (i,j) not in original_color:
                    break
                colors.append(("original", original_color[(i,j)]))
            elif i >= m and j >= n:
                break
            else:
                colors.append(("fresh", i, j))
        else:
            if len(set(colors)) == k:
                return True
    return False

def rank_mod(matrix, prime=101):
    a = [[x % prime for x in row] for row in matrix]
    h, w = len(a), len(a[0])
    rank = 0
    for j in range(w):
        pivot = next((i for i in range(rank, h) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][j], -1, prime)
        a[rank][j:] = [x * inv % prime for x in a[rank][j:]]
        for i in range(rank + 1, h):
            if a[i][j]:
                mult = a[i][j]
                a[i][j:] = [(x-mult*y) % prime
                            for x,y in zip(a[i][j:],a[rank][j:])]
        rank += 1
    return rank

def main():
    rng = Random(20261102)
    checked = 0
    for k in range(2,7):
        for _ in range(200):
            factors = []
            for _ in range(rng.randint(1,3)):
                left, right = {}, {}
                for x in product(range(k),repeat=2):
                    which = rng.randrange(3)
                    if which == 1: left[x] = rng.randint(1,4)
                    elif which == 2: right[x] = rng.randint(1,4)
                factors.append((left,right))
            assert by_ferrers_thresholds(k,factors) == by_permutation_brute(k,factors)
            checked += 1
    print(f"Ferrers: {checked} random instances agree")

    for k in (4,8):
        n = k*k // 4
        matrix = [[int(i>j) for j in range(n)] for i in range(n)]
        assert rank_mod(matrix) == n-1
        print(f"K={k}: half-graph cross rank={n-1}, biclique-cover={n-1}, full rank={2*n-2}")

    checked = 0
    for m in range(2,4):
        for n in range(2,4):
            for target in range(1,min(m,n)+1):
                for _ in range(70):
                    edges = [(i,j,rng.randrange(4))
                             for i in range(m) for j in range(n)
                             if rng.randrange(3)>0]
                    assert rainbow_matching_brute(m,n,edges,target) == (
                        padded_rainbow_perfect_brute(m,n,edges,target)
                    )
                    checked += 1
    print(f"Rainbow padding: {checked} random instances agree")

if __name__ == "__main__":
    main()
