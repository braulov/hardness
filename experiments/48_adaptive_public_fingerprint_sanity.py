#!/usr/bin/env python3
"""Checkpoint 48: explicit PCC NO instance and adaptive public-fingerprint collisions.

A given K=2d+2 NO instance contains 2^d special permutations with
violation supports {e0} union {ej: xj=1}. Over F_(2^b)^t, their random
linear fingerprints are precisely an affine subspace of F_2^(b*t).
Every collision corresponds to a FALSE accepting permutation.

Run: python experiments/48_adaptive_public_fingerprint_sanity.py
"""
from itertools import product, permutations
from random import Random

def make_no_instance(k):
    assert k >= 4 and k % 2 == 0
    d = (k-2)//2
    anchors = [2*d, 2*d+1]
    allowed = set()
    for j in range(d):
        block = (2*j, 2*j+1)
        allowed.update((i,a) for i in block for a in block)
    allowed.update((i,i) for i in anchors)

    anchor_a = (anchors[0], anchors[0])
    anchor_b = (anchors[1], anchors[1])
    forbidden_markers = [frozenset((anchor_a, anchor_b))]
    for j in range(d):
        forbidden_markers.append(
            frozenset(((2*j, 2*j+1), anchor_a))
        )
    return allowed, forbidden_markers

def special_permutation(k, bits):
    pi = list(range(k))
    for j, swap in enumerate(bits):
        if swap:
            a,b = 2*j,2*j+1
            pi[a],pi[b] = pi[b],pi[a]
    return pi

def marker_support(pi, forbidden_markers):
    selected = {(i,a) for i,a in enumerate(pi)}
    return frozenset(j for j,edge in enumerate(forbidden_markers)
                     if edge <= selected)

def span_basis(vectors):
    basis = {}
    for v in vectors:
        x = v
        while x:
            lead = x.bit_length()-1
            if lead in basis: x ^= basis[lead]
            else:
                basis[lead]=x
                break
    return basis

def in_span(target, basis):
    x = target
    while x:
        lead = x.bit_length()-1
        if lead not in basis: return False
        x ^= basis[lead]
    return True

def sample_collision(d,bits,trials=10000):
    rng = Random(9000+d*100+bits)
    count = 0
    for _ in range(trials):
        weights = [rng.randrange(1<<bits) for _ in range(d+1)]
        count += in_span(weights[0],span_basis(weights[1:]))
    empirical = count/trials
    if d >= bits:
        lower = 1 - 2**(bits-d)
        assert empirical >= lower-0.04,(d,bits,empirical,lower)
    else:
        upper = 2**(d-bits)
        assert empirical <= upper+0.04,(d,bits,empirical,upper)
    return empirical

def main():
    for k in (4,6,8):
        allowed, markers = make_no_instance(k)
        d=(k-2)//2
        observed=set()
        for bits in product((0,1),repeat=d):
            pi=special_permutation(k,bits)
            assert {(i,a) for i,a in enumerate(pi)} <= allowed
            expected=frozenset([0]+[j+1 for j,v in enumerate(bits) if v])
            actual=marker_support(pi,markers)
            assert actual == expected
            observed.add(actual)
        assert len(observed)==2**d
        # Every permutation is forbidden by at least one edge:
        # either an isolated candidate was selected, or the anchor edge e0
        # is always selected.
        for pi in permutations(range(k)):
            chosen = {(i,a) for i,a in enumerate(pi)}
            if chosen <= allowed: assert 0 in marker_support(pi,markers)
        print(f"K={k}: {2**d} special permutations; genuine NO PCC")

    for d,b in [(4,2),(8,3),(12,4),(5,9),(8,12)]:
        prob = sample_collision(d,b)
        print(f"d={d}, total hash bits={b}: collision fraction={prob:.4f}")
    print("All tests passed")

if __name__ == "__main__":
    main()
