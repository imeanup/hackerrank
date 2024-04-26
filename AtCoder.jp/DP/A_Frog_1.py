import sys
from functools import cache
sys.setrecursionlimit(1000000)

N = int(input())
H = list(map(int, input().split()))

@cache
def solve(i):
    if i == 0:
        return 0
    res = float('inf')
    res = min(res, solve(i-1) + abs(H[i] - H[i-1]))
    if i > 1: 
        res = min(res, solve(i-2) + abs(H[i] - H[i-2]))
    return res

print(solve(N-1))