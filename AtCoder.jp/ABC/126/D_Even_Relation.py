from collections import defaultdict
from functools import cache, lru_cache
n = int(input())

g = defaultdict(list)

for _ in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))

color = [-1]*n
seen = set()
stack = [(0, -1, 0, 0)]

while stack:
    v, p, w, c = stack.pop()

    seen.add(v)
    if w & 1:
        color[v] = c ^ 1
    else:
        color[v] = c

    for u, w_u in g[v]:
        if u == p:
            continue
        if u not in seen:
            stack.append((u, v, w_u, color[v]))

for x in color:
    print(x)
