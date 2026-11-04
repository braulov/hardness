"""Exact finite check of results/csp-algorithms.md; standard library only.

Compare rational chord expansion and forest messages with brute-force counting.
This is not a test of the asymptotic theorem or a general-purpose CSP solver.
"""

from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def factor(matrix):
    """A = U V: original pivot columns times the nonzero RREF rows."""
    rows = [[F(x) for x in row] for row in matrix]
    n = len(rows)
    pivots = []
    for col in range(n):
        pivot = next((i for i in range(len(pivots), n) if rows[i][col]), None)
        if pivot is None:
            continue
        pos = len(pivots)
        rows[pos], rows[pivot] = rows[pivot], rows[pos]
        scale = rows[pos][col]
        rows[pos] = [x / scale for x in rows[pos]]
        for i in range(n):
            if i != pos:
                scale = rows[i][col]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[pos])]
        pivots.append(col)
    u = [[F(row[j]) for j in pivots] for row in matrix]
    v = rows[:len(pivots)]
    assert all(sum(u[a][j] * v[j][b] for j in range(len(pivots)))
               == matrix[a][b] for a in range(n) for b in range(n))
    return u, v


def count_by_chords(n, q, edges):
    factors = [factor(matrix) for _, _, matrix in edges]
    if any(not v for _, v in factors):
        return F(0)
    parent = list(range(n))

    def find(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    forest, chords = [], []
    for i in sorted(range(len(edges)), key=lambda i: -len(factors[i][1])):
        a, b, _ = edges[i]
        ra, rb = find(a), find(b)
        if ra == rb:
            chords.append(i)
        else:
            parent[ra] = rb
            forest.append(i)
    adj = [[] for _ in range(n)]
    for i in forest:
        a, b, matrix = edges[i]
        adj[a].append((b, matrix))
        adj[b].append((a, list(zip(*matrix))))
    roots = [a for a in range(n) if find(a) == a]
    total = F(0)
    for modes in product(*(range(len(factors[i][1])) for i in chords)):
        weights = [[F(1)] * q for _ in range(n)]
        for i, j in zip(chords, modes):
            a, b, _ = edges[i]
            u, v = factors[i]
            for label in range(q):
                weights[a][label] *= u[label][j]
                weights[b][label] *= v[j][label]

        def message(a, prev):
            values = weights[a][:]
            for b, matrix in adj[a]:
                if b == prev:
                    continue
                child = message(b, a)
                for x in range(q):
                    values[x] *= sum(matrix[x][y] * child[y] for y in range(q))
            return values

        term = F(1)
        for root in roots:
            term *= sum(message(root, -1))
        total += term
    return total


def count_direct(n, q, edges):
    return sum(all(matrix[x[a]][x[b]] for a, b, matrix in edges)
               for x in product(range(q), repeat=n))


def main():
    rng = Random(20261104)
    cases = [(3, 2, []), (2, 2, [(0, 1, [[0, 0], [0, 0]])])]
    mixed = [[1, 1, 0, 1], [1, 0, 1, 0],
             [0, 1, 1, 0], [0, 0, 0, 0]]
    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    _, v = factor(mixed)
    assert any(x < 0 and x.denominator > 1 for row in v for x in row)
    cases.append((3, 4, [(0, 1, identity), (1, 2, identity), (0, 2, mixed)]))
    for _ in range(250):
        n, q = rng.randint(1, 6), rng.randint(2, 4)
        pairs = list(combinations(range(n), 2))
        rng.shuffle(pairs)
        pairs = pairs[:rng.randint(0, min(len(pairs), n + 1))]
        edges = [(a, b, [[rng.randrange(2) for _ in range(q)] for _ in range(q)])
                 for a, b in pairs]
        cases.append((n, q, edges))
    for n, q, edges in cases:
        actual = count_by_chords(n, q, edges)
        expected = count_direct(n, q, edges)
        assert actual == expected, (n, q, edges, actual, expected)
    print(f"OK: {len(cases)} exact rank-cycle counts agree with brute force")
    print("Includes a chord factorization with negative fractional entries.")


if __name__ == "__main__":
    main()
