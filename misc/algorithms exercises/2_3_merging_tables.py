# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
max_lines = max(lines)
rank = [0] * n  # union-by-rank heuristic
parent = [-1] * n

def find(table):
    if parent[table] == -1:
        return table
    parent[table] = find(parent[table])  # path compression
    return parent[table]

def union(destination, source):
    if destination == source:
        return 0
    pd, ps = find(destination), find(source)
    rd, rs = rank[pd], rank[ps]
    if pd == ps:
        return 0
    if rd <= rs:
        parent[pd] = ps
        lines[ps] += lines[pd]
        lines[pd] = 0
        if rd == rs:
            rank[ps] += 1
        return lines[ps]
    else:
        parent[ps] = pd
        lines[pd] += lines[ps]
        lines[ps] = 0
        return lines[pd]


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    unioned_lines = union(destination - 1, source - 1)
    max_lines = max(max_lines, unioned_lines)
    print(max_lines)
