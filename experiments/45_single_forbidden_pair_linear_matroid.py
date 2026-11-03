#!/usr/bin/env python3
"""Checkpoint 45: verify GF(7) one-forbidden-pair determinant gadget exhaustively,
and separately verify the independent-bit PCC witness family.

Run: python experiments/45_single_forbidden_pair_linear_matroid.py
"""
from itertools import permutations, combinations

def det_mod_from_columns(columns, p=7):
    k = len(columns)
    matrix = [[columns[c][r] % p for c in range(k)] for r in range(k)]
    determinant = 1
    for j in range(k):
        pivot = next((r for r in range(j, k) if matrix[r][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
            determinant = -determinant
        value = matrix[j][j]
        determinant = determinant * value % p
        inv = pow(value, -1, p)
        for r in range(j+1, k):
            factor = matrix[r][j] * inv % p
            for c in range(j+1, k):
                matrix[r][c] = (matrix[r][c] - factor * matrix[j][c]) % p
    return determinant % p

def vector(k, row, col, i, j, a, b, p=7):
    epsilon = 1 if k % 2 == 0 else p-1
    theta = 1
    if row == i:
        theta = 1 if col == a else 2
    elif row == j:
        theta = epsilon if col == b else 3*epsilon
    vec = [0] * k
    vec[row] = 1
    vec[(row+1)%k] = (vec[(row+1)%k]+theta) % p
    return vec

def check_edge_gadget():
    total = 0
    for k in range(2, 7):
        count = 0
        for i,j in combinations(range(k), 2):
            for a in range(k):
                for b in range(k):
                    if a == b:
                        continue
                    for pi in permutations(range(k)):
                        columns = [vector(k,h,pi[h],i,j,a,b)
                                   for h in range(k)]
                        actual = det_mod_from_columns(columns)
                        bad = pi[i] == a and pi[j] == b
                        assert (actual == 0) == bad, (k,i,j,a,b,pi,actual)
                        count += 1
        total += count
        print(f"K={k}: {count} determinant checks pass")
    assert total == 349840
    print(f"GF(7): {total} exhaustive checks pass")

def check_independent_forbidden_bits():
    for k in (4, 6, 8):
        assert k % 2 == 0
        s = k // 2
        regular = range(s)
        active = range(s, k)
        bits = [(i,j,a,b) for i,j in combinations(regular,2)
                for a in active for b in active if a != b]
        witnesses = []
        for i,j,a,b in bits:
            pi = [-1] * k
            pi[i],pi[j] = a,b
            for h in regular:
                if h not in (i,j):
                    pi[h] = h
            remaining = sorted(set(range(k))-set(pi[:s]))
            pi[s:] = remaining
            assert sorted(pi) == list(range(k))
            active_bits = [(x,y,c,d) for x,y,c,d in bits
                           if pi[x] == c and pi[y] == d]
            assert active_bits == [(i,j,a,b)], (k,(i,j,a,b),active_bits)
            witnesses.append(pi)
        print(f"K={k}: {len(bits)} independently observable forbidden bits")

if __name__ == "__main__":
    check_edge_gadget()
    check_independent_forbidden_bits()
