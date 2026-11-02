#!/usr/bin/env python3
"""Fourier/determinant group algebra for K=3, p=7, r=2, F=GF(64).

Checks 49 Fourier coefficients against all 3! matchings for 100
random seeds on both a YES and a NO low-rank PCC instance.
"""
import itertools
import random

P, K, MOD = 7, 3, 0b1000011  # GF(2^6): x^6+x+1

def mul(a, b):
    c = 0
    for _ in range(6):
        if b & 1: c ^= a
        b >>= 1
        a <<= 1
        if a & 64: a ^= MOD
    return c

def power(a, n):
    c = 1
    while n:
        if n & 1: c = mul(c, a)
        a = mul(a, a)
        n //= 2
    return c

ROOT = next(x for x in range(2, 64) if power(x, P) == 1)
assert len({power(ROOT, i) for i in range(P)}) == P

def det3(a):
    result = 0
    for pi in itertools.permutations(range(K)):
        term = 1
        for i in range(K): term = mul(term, a[i][pi[i]])
        result ^= term  # char 2: permanent == determinant
    return result

def test(weights, seed):
    rng = random.Random(seed)
    coeff = [[rng.randrange(1, 64) for _ in range(K)] for _ in range(K)]
    vectors = list(itertools.product(range(P), repeat=2))
    hats = {}
    for t in vectors:
        a = [[mul(coeff[i][j],
                  power(ROOT, sum(t[h]*weights[i][j][h]
                                  for h in range(2)) % P))
              for j in range(K)] for i in range(K)]
        hats[t] = det3(a)
    decoded = {}
    for s in vectors:
        val = 0
        for t in vectors:
            power_index = -sum(t[h]*s[h] for h in range(2)) % P
            val ^= mul(hats[t], power(ROOT, power_index))
        decoded[s] = val

    direct = dict.fromkeys(vectors, 0)
    valid = False
    for pi in itertools.permutations(range(K)):
        s = tuple(sum(weights[i][pi[i]][h] for i in range(K)) % P
                  for h in range(2))
        term = 1
        for i in range(K): term = mul(term, coeff[i][pi[i]])
        direct[s] ^= term
        if (2*s[0]*s[1]) % P == 0: valid = True

    assert decoded == direct
    accepted = any(c != 0 and (2*s[0]*s[1]) % P == 0
                   for s, c in decoded.items())
    assert not accepted or valid
    return accepted, valid

def main():
    yes = [[(1,0) if (i,j)==(0,0) else (0,1) if (i,j)==(1,1)
            else (0,0) for j in range(K)] for i in range(K)]
    no = [[(1,0) if i==0 else (0,1) if i==1 else (0,0)
           for j in range(K)] for i in range(K)]
    for seed in range(100):
        assert test(yes, seed) == (True, True)
        assert test(no, seed) == (False, False)
    print("OK: 200 trials; 49 Fourier coefficients each match brute force")

if __name__ == "__main__":
    main()
