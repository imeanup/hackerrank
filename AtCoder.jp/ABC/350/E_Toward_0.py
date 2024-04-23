from functools import cache, lru_cache

INF = 1e18 + 5

N, A, X, Y = map(int, input().split())

@cache
def solve(N, A, X, Y):
    if N == 0:
        return 0
    res = INF
    res = min(res, X + solve(N//A, A, X, Y), 1.2 * Y + (0.2 * (solve(N//2, A, X, Y) +
            solve(N//3, A, X, Y) + solve(N//4, A, X, Y) + solve(N//5, A, X, Y) + 
            solve(N//6, A, X, Y))))
    
    return res

result = solve(N, A, X, Y)
print("{:.8f}".format(result))