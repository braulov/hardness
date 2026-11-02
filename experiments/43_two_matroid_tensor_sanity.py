#!/usr/bin/env python3
"""Checkpoint 43: tensor-wedge DP for two simultaneous linear matroid factors.
Run: python experiments/43_two_matroid_tensor_sanity.py
"""
from itertools import permutations
from random import Random

def insert(basis, vector, p):
    x={key: v%p for key,v in vector.items() if v%p}
    for pivot, row in sorted(basis.items()):
        if pivot in x:
            c=x[pivot]
            for key,val in row.items():
                x[key]=(x.get(key,0)-c*val)%p
                if not x[key]: del x[key]
    if not x: return
    pivot=min(x); inv=pow(x[pivot],-1,p)
    basis[pivot]={key: val*inv%p for key,val in x.items()}

def extend(tensor, vectors, p):
    out={}
    for masks,c in tensor.items():
        states=[((),c)]
        for mask,vec in zip(masks,vectors):
            next_states=[]
            for partial,w in states:
                for a, v in enumerate(vec):
                    if mask>>a&1 or not v: continue
                    sign=-1 if (mask>>(a+1)).bit_count()%2 else 1
                    next_states.append((partial+(mask|(1<<a),),w*v*sign%p))
            states=next_states
        for key,value in states:
            out[key]=(out.get(key,0)+value)%p
    return {key:v for key,v in out.items() if v}

def solve(k,r,v,allowed,p):
    old={0:{(0,)*r:{(0,)*r:1}}}
    for i in range(k):
        new={}
        for mask,basis in old.items():
            for a in range(k):
                if mask>>a&1 or not allowed[i][a]:continue
                target=new.setdefault(mask|(1<<a),{})
                for state in basis.values():
                    insert(target,extend(state,v[i][a],p),p)
        old=new
    return bool(old.get((1<<k)-1,{}))

def independent(vectors,p):
    basis={}
    for vec in vectors:
        insert(basis,{i:c for i,c in enumerate(vec) if c%p},p)
    return len(basis)==len(vectors)

def brute(k,r,v,allowed,p):
    return any(all(allowed[i][pi[i]] for i in range(k)) and
               all(independent([v[i][pi[i]][h] for i in range(k)],p)
                   for h in range(r))
               for pi in permutations(range(k)))

def main():
    p=101
    rng=Random(7113)
    for k in range(2,6):
        for _ in range(50):
            r=2
            v=[[[[rng.randrange(3) for j in range(k)] for h in range(r)]
                 for a in range(k)] for i in range(k)]
            allowed=[[rng.random()<.9 for a in range(k)] for i in range(k)]
            assert solve(k,r,v,allowed,p)==brute(k,r,v,allowed,p)
        print(f"K={k}: 50 two-matroid tests passed")
    print("All 200 tests passed.")

if __name__=="__main__":
    main()
