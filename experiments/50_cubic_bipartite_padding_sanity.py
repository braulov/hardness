#!/usr/bin/env python3
"""Check the cardinality/degree argument of note 50's cubic padding gadget.

No third-party libraries. This checks the exact graph structure, not
the probabilistic Isolation Lemma.

Usage: python3 experiments/50_cubic_bipartite_padding_sanity.py
"""

def check_and_pad(na, nb, edges):
    """Return (number of vertices, number of edges) of cubic completion.

    Original bipartition A=[0,na), B=[na,na+nb).
    """
    n = na + nb
    adj = [set() for _ in range(n)]

    def add(a, b):
        assert a != b and b not in adj[a], (a, b)
        adj[a].add(b)
        adj[b].add(a)

    A, B = set(range(na)), set(range(na, n))
    for a, b in edges:
        assert a in A and b in B
        add(a, b)

    assert max(map(len, adj), default=0) <= 3

    def dummy(side):
        v = len(adj)
        adj.append(set())
        side.add(v)
        return v

    while len(A) < len(B):
        dummy(A)
    while len(B) < len(A):
        dummy(B)

    def stubs(side):
        return [v for v in sorted(side) for _ in range(3-len(adj[v]))]

    a_stubs, b_stubs = stubs(A), stubs(B)
    assert len(a_stubs) == len(b_stubs)

    for old_a, old_b in zip(a_stubs, b_stubs):
        a_g = [dummy(A) for _ in range(3)]
        b_g = [dummy(B) for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if i != 0 or j != 0:  # K_{3,3} minus edge (0,0)
                    add(a_g[i], b_g[j])
        add(old_a, b_g[0])
        add(a_g[0], old_b)

    assert len(A) == len(B)
    assert all(len(adj[v]) == 3 for v in range(len(adj)))
    assert all((v in A) != (w in A) for v in range(len(adj)) for w in adj[v])
    undirected_edges = sum(map(len, adj)) // 2
    assert 2 * undirected_edges == 3 * len(adj)
    assert len(adj) <= 24 * (n + len(edges) + 1)
    return len(adj), undirected_edges


def main():
    samples = [
        (2, 1, [(0, 2), (1, 2)]),
        (3, 3, [(0, 3), (1, 4), (2, 5)]),
        (3, 3, [(0, 3), (0, 4), (1, 3), (2, 5)]),
        (4, 5, [(0, 4), (0, 5), (1, 6), (2, 7), (3, 8)]),
    ]
    for na, nb, edges in samples:
        nv, ne = check_and_pad(na, nb, edges)
        print(f"original A={na} B={nb} m={len(edges)} -> cubic n={nv} m={ne}")

    # Incidence graphs from arbitrary simple source graphs.
    for k in (3, 4, 6, 10):
        original_edges = [(u, v) for u in range(k) for v in range(u+1, k)
                          if (u+2*v) % 3 != 0]
        degrees = [0] * k
        edges = []
        for eid, (u, v) in enumerate(original_edges):
            # For the test use source max degree <=3 only.
            degrees[u] += 1
            degrees[v] += 1
            edges.extend([(u, k+eid), (v, k+eid)])
        if max(degrees) <= 3:
            nv, ne = check_and_pad(k, len(original_edges), edges)
            print(f"incidence k={k} -> cubic n={nv} m={ne}")
    print("OK: every completed graph is simple, bipartite, 3-regular, linear size")


if __name__ == "__main__":
    main()
