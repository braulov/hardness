#!/usr/bin/env python3
"""Checkpoint 43: exact deterministic wedge-span DP and folded-Wronskian rank condenser.
Run: python experiments/43_matroid_permutation_sanity.py
The code verifies:
  * 500 dimension-K instances against brute permutations;
  * 160 dimension-(K+2) instances with deterministic rank-condensing family.
Both use F_101 (illustrative finite-field implementation).
"""
from itertools import permutations
from random import Random

def add_basis(B, x, p):
    x = {j: v % p for j, v in x.items() if v % p}
    for j, row in sorted(B.items()):
        if j in x:
            c = x[j]
            for a, z in row.items():
                v = (x.get(a, 0) - c*z) % p
                if v: x[a] = v
                else: x.pop(a, None)
    if not x: return False
    j = min(x)
    inv = pow(x[j], -1, p)
    B[j] = {a: v*inv % p for a,v in x.items()}
    return True

def wedge(x, vec, p):
    out = {}
    for mask, coeff in x.items():
        for a, value in enumerate(vec):
            if (mask >> a) & 1 or not value: continue
            sign = -1 if ((mask >> (a+1)).bit_count() % 2) else 1
            dest = mask | (1 << a)
            out[dest] = (out.get(dest, 0) + sign*coeff*value) % p
    return {a: v for a,v in out.items() if v}

def solve(k, vectors, allowed, p):
    old = {0: {0: {0:1}}}  # used-column-mask -> echelon basis of wedge coordinates
    for i in range(k):
        new = {}
        for S, basis in old.items():
            for a in range(k):
                if (S >> a)&1 or not allowed[i][a]: continue
                target = new.setdefault(S | (1 << a), {})
                for x in basis.values():
                    add_basis(target, wedge(x, vectors[i][a], p), p)
        old = new
    return bool(old.get((1 << k)-1, {}))

def rank_mod(A,p):
    rows = [row[:] for row in A]
    n,m = len(rows), len(rows[0])
    r = 0
    for j in range(m):
        pivot = next((i for i in range(r,n) if rows[i][j] % p),None)
        if pivot is None: continue
        rows[r],rows[pivot] = rows[pivot],rows[r]
        inv = pow(rows[r][j],-1,p)
        for i in range(r+1,n):
            f = rows[i][j]*inv % p
            rows[i][j:] = [(a-f*b) % p for a,b in zip(rows[i][j:],rows[r][j:])]
        r += 1
        if r==n: break
    return r

def brute(k,vec,allowed,p):
    d = len(vec[0][0])
    for pi in permutations(range(k)):
        if not all(allowed[i][pi[i]] for i in range(k)): continue
        mat = [[vec[i][pi[i]][j] for i in range(k)] for j in range(d)]
        if rank_mod(mat,p) == k: return True
    return False

def condense(k,d,vec,t,omega,p):
    W = [[pow((pow(omega,i,p)*t)%p,j,p) for j in range(d)] for i in range(k)]
    return [[[sum(W[h][b]*vec[i][a][b] for b in range(d))%p
              for h in range(k)] for a in range(k)] for i in range(k)]

def main():
    p=101
    rng=Random(1977)
    for k in range(2,7):
        for _ in range(100):
            vec=[[[rng.randrange(3) for j in range(k)] for a in range(k)]
                 for i in range(k)]
            allowed=[[rng.random()<.8 for a in range(k)] for i in range(k)]
            assert solve(k,vec,allowed,p) == brute(k,vec,allowed,p)
        print(f"K={k}: 100 exact wedge-DP tests")

    omega=next(g for g in range(2,p) if len({pow(g,j,p) for j in range(p-1)})==p-1)
    rng=Random(13881)
    for k in range(2,6):
        d=k+2
        for _ in range(40):
            vec=[[[rng.randrange(5) for j in range(d)] for a in range(k)]
                 for i in range(k)]
            allowed=[[rng.random()<.7 for a in range(k)] for i in range(k)]
            yes=brute(k,vec,allowed,p)
            found=any(solve(k,condense(k,d,vec,t,omega,p),allowed,p)
                      for t in range(1,k*(d-1)+2))
            assert found == yes
        print(f"K={k}, d={d}: 40 folded-Wronskian tests")
    print("All 660 tests passed.")

if __name__ == "__main__":
    main()
