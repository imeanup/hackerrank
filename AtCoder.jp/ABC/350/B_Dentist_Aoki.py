from collections import Counter

N, Q = map(int, input().split())
T = list(map(int, input().split()))

f = Counter(T)
res = N
for v in f.values():
    res -= v % 2
print(res)