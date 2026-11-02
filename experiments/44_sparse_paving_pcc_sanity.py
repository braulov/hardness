#!/usr/bin/env python3
"""Checkpoint 44: basis-exchange sanity for the PCC sparse-paving matroid.
All forbidden-permutation families at K=2,3; sampled K=4 families.
"""
from itertools import combinations, permutations
from random import Random

def matching_set(pi,k):
    return frozenset(i*k+a for i,a in enumerate(pi))

def check_matroid(k, bad, rng=None):
    n=k*k
    forbidden={matching_set(pi,k) for pi in bad}
    bases=[frozenset(c) for c in combinations(range(n),k)
           if frozenset(c) not in forbidden]
    assert bases
    if rng is None:
        pairs=((X,Y) for X in bases for Y in bases)
    else:
        pairs=((rng.choice(bases),rng.choice(bases)) for _ in range(50_000))
    for X,Y in pairs:
        for e in X-Y:
            assert any(frozenset((X-{e})|{f}) not in forbidden
                       for f in Y-X), (k,X,Y,e)

def main():
    for k in (2,3):
        choices=list(permutations(range(k)))
        for mask in range(1<<len(choices)):
            bad=[choices[j] for j in range(len(choices)) if mask>>j&1]
            check_matroid(k,bad)
        print(f"K={k}: all {1<<len(choices)} forbidden-permutation patterns valid")
    rng=Random(12)
    choices=list(permutations(range(4)))
    for _ in range(10):
        bad=[pi for pi in choices if rng.random()<.6]
        check_matroid(4,bad,rng)
    print("K=4: 10 random forbidden sets, 50,000 basis-pair checks each")

if __name__=="__main__":
    main()
