"""
Bottom-up approach, time complexity of O(n^3) and space complexity of O(n^2)
"""


def MATRIX_CHAIN_ORDER(p):
    n = len(p) - 1
    m = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        m[i][i] = 0
        s[i][i] = i
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


"""
time complexity of O(2^n) and space complexity of O(n)
"""


def PRINT_OPTIMAL_PARENTS(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        PRINT_OPTIMAL_PARENTS(s, i, s[i][j])
        PRINT_OPTIMAL_PARENTS(s, s[i][j] + 1, j)
        print(")", end="")


p = [30, 35, 15, 5, 10, 20, 25]
# p = [5, 10, 3, 12, 5, 50, 6]
m, s = MATRIX_CHAIN_ORDER(p)
print(m)
print(s)
PRINT_OPTIMAL_PARENTS(s, 1, 6)
