#!/usr/bin/env python3
"""Sanity-check the *semantic* RAM trace gadget for Fisher-Yates.
This tests operation checks plus sorted-memory consistency, NOT a compiled
binary CSP or the AKS sorting-network implementation.
Run: python experiments/39_fisher_yates_ram_trace_sanity.py
"""
import itertools


def trace(k: int, digits: dict[int, int]):
    memory = list(range(1, k + 1))
    records = [(i, 0, "W", i) for i in range(1, k + 1)]
    now = 1
    for i in range(k, 1, -1):
        j = digits[i]
        left, right = memory[i - 1], memory[j - 1]
        records.extend([
            (i, now, "R", left),
            (j, now + 1, "R", right),
            (i, now + 2, "W", right),
            (j, now + 3, "W", left),
        ])
        memory[i - 1], memory[j - 1] = right, left
        now += 4
    records.extend((i, now + i, "R", memory[i - 1]) for i in range(1, k + 1))
    return records, memory


def operation_semantics(records, k, digits):
    if len(records) != 6 * k - 4:
        return False
    if any(records[i - 1] != (i, 0, "W", i) for i in range(1, k + 1)):
        return False
    for i in range(k, 1, -1):
        pos = k + 4 * (k - i)
        a, b, c, d = records[pos : pos + 4]
        j, t = digits[i], 1 + 4 * (k - i)
        if [(r[0], r[1], r[2]) for r in (a, b, c, d)] != [
            (i, t, "R"), (j, t + 1, "R"),
            (i, t + 2, "W"), (j, t + 3, "W")
        ]:
            return False
        if c[3] != b[3] or d[3] != a[3]:
            return False
    now = 1 + 4 * (k - 1)
    return all(records[-k + i - 1][:3] == (i, now + i, "R")
               for i in range(1, k + 1))


def sorted_memory_consistency(records):
    addr, value = None, None
    for new_addr, time, kind, new_value in sorted(records):
        if addr != new_addr:
            if (time, kind, new_value) != (0, "W", new_addr):
                return False
            addr, value = new_addr, new_value
        elif kind == "W":
            value = new_value
        elif kind == "R":
            if value != new_value:
                return False
        else:
            return False
    return True


def accepted(records, k, digits):
    return (operation_semantics(records, k, digits)
            and sorted_memory_consistency(records))


def main():
    for k in range(2, 8):
        count = 0
        for choices in itertools.product(
            *[range(1, j + 1) for j in range(2, k + 1)]
        ):
            digits = dict(zip(range(2, k + 1), choices))
            records, permutation = trace(k, digits)
            assert accepted(records, k, digits)
            assert sorted(permutation) == list(range(1, k + 1))
            for pos, event in enumerate(records):
                corrupted = list(records)
                address, time, kind, old_value = event
                corrupted[pos] = (
                    address, time, kind, (old_value % k) + 1
                )
                assert not accepted(corrupted, k, digits), (
                    "One-record mutation accepted", k, digits, pos
                )
            count += 1
        print(f"K={k}: {count} legal permutations; all single-value mutations rejected")


if __name__ == "__main__":
    main()
