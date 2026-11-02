#!/usr/bin/env python3
"""Check polynomial swap-derivative test for quadratic permutation identities."""
from itertools import permutations
import random

def brute_zero(T, k, p):
    return all(sum(T[k*i+pi[i]][k*j+pi[j]]
                   for i in range(k) for j in range(k)) % p == 0
               for pi in permutations(range(k)))

def swap_zero(T, k, p):
    def b(i,a,j,c): return T[k*i+a][k*j+c]
    if sum(b(i,i,j,j) for i in range(k) for j in range(k)) % p:
        return False
    for i in range(k):
        for j in range(i+1,k):
            rest_rows=[t for t in range(k) if t not in (i,j)]
            for a in range(k):
                for v in range(k):
                    if a==v: continue
                    rest_cols=[c for c in range(k) if c not in (a,v)]
                    d=(b(i,v,i,v)-b(i,a,i,a)+b(j,a,j,a)-b(j,v,j,v)
                       +2*(b(i,v,j,a)-b(i,a,j,v)))%p
                    def C(t,c):
                        return 2*(b(i,v,t,c)-b(i,a,t,c)+b(j,a,t,c)-b(j,v,t,c))%p
                    if (d+sum(C(t,c) for t,c in zip(rest_rows,rest_cols)))%p:
                        return False
                    if rest_rows:
                        t0,c0=rest_rows[0],rest_cols[0]
                        for t in rest_rows:
                            for c in rest_cols:
                                if (C(t,c)-C(t,c0)-C(t0,c)+C(t0,c0))%p:
                                    return False
    return True

def symmetric(k,p,rng):
    n=k*k
    T=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            T[i][j]=T[j][i]=rng.randrange(p)
    return T

def null_gauge(k,p,rng):
    n=k*k
    T=[[0]*n for _ in range(n)]
    for i in range(n):
        row_i,col_i=divmod(i,k)
        for j in range(i+1,n):
            row_j,col_j=divmod(j,k)
            if row_i==row_j or col_i==col_j:
                T[i][j]=T[j][i]=rng.randrange(p)
    potentials=[rng.randrange(p) for _ in range(k-1)]
    potentials.append(-sum(potentials)%p)
    for i in range(k):
        for a in range(k): T[k*i+a][k*i+a]=potentials[i]
    return T

if __name__=="__main__":
    rng=random.Random(4389)
    for k in range(2,6):
        for _ in range(30):
            T=symmetric(k,17,rng)
            U=null_gauge(k,17,rng)
            V=[[(T[i][j]+U[i][j])%17 for j in range(k*k)]
               for i in range(k*k)]
            assert brute_zero(T,k,17)==swap_zero(T,k,17)
            assert brute_zero(U,k,17) and swap_zero(U,k,17)
            assert brute_zero(V,k,17)==swap_zero(V,k,17)
        print("K=",k,"OK")
