"""
Section 15.3 Pg. 385 -- Top-Down Approach
Without minimum # of scalar multiplications is stored in m 2D array
where m[i][j] represent the minimum # of scalar multiplications required 
to multiply the matrices from i to j.
"""


def RECURSIVE_MATRIX_CHAIN(p, i, j):
    if i == j:
        return 0
    m = float("inf")
    for k in range(i, j):
        q = (
            RECURSIVE_MATRIX_CHAIN(p, i, k)
            + RECURSIVE_MATRIX_CHAIN(p, k + 1, j)
            + (p[i - 1] * p[k] * p[j])
        )
        m = min(m, q)
    return m


"""
Time complexity: O(n^3); Space: O(n^2)
"""


def MEMOIZED_MATRIX_CHAIN(p):
    n = len(p) - 1
    m = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    return LOOKUP_CHAIN(m, p, 1, n)


def LOOKUP_CHAIN(m, p, i, j):
    if m[i][j] < float("inf"):
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = (
                LOOKUP_CHAIN(m, p, i, k)
                + LOOKUP_CHAIN(m, p, k + 1, j)
                + (p[i - 1] * p[k] * p[j])
            )
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]


if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]  # Matrix dimension
    n = len(p) - 1
    print(RECURSIVE_MATRIX_CHAIN(p, 1, n))
    print(MEMOIZED_MATRIX_CHAIN(p))
