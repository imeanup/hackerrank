def CUT_ROD(p, n):
    if n == 0:
        return 0
    q = -float("inf")
    for i in range(n):
        q = max(q, p[i] + CUT_ROD(p, n - i - 1))
    return q


def MEMOIZED_CUT_ROD(p, n):
    r = [-float("inf") for _ in range(n + 1)]
    return MEMOIZED_CUT_ROD_AUX(p, n, r)


def MEMOIZED_CUT_ROD_AUX(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(n):
            q = max(q, p[i] + MEMOIZED_CUT_ROD_AUX(p, n - i - 1, r))
    r[n] = q
    return q


def BOTTOM_UP_CUT_ROD(p, n):
    r = [None for _ in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -float("inf")
        for i in range(j):
            q = max(q, p[i] + r[j - i - 1])
        r[j] = q
    return r[n]


def EXTENDED_BOTTOM_UP_CUT_ROD(p, n):
    r = [None for _ in range(n + 1)]
    s = [None for _ in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -float("inf")
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i
        r[j] = q
    return (r, s)


def PRINT_CUT_ROD_SOLUTION(p, n):
    r, s = EXTENDED_BOTTOM_UP_CUT_ROD(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]


"""
Ex 15.1-4
"""


def MEMOIZED_CUT_ROD_WITH_SOLUTION(p, n):
    r = [-float("inf") for _ in range(n + 1)]
    s = [0 for _ in range(n + 1)]
    return MEMOIZED_CUT_ROD_AUX_WITH_SOLUTION(p, n, r, s)


def MEMOIZED_CUT_ROD_AUX_WITH_SOLUTION(p, n, r, s):
    if r[n] >= 0:
        return (r[n], s)
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(1, n + 1):
            result = MEMOIZED_CUT_ROD_AUX_WITH_SOLUTION(p, n - i, r, s)
            if q < p[i - 1] + result[0]:
                q = p[i - 1] + result[0]
                s[n] = i
    r[n] = q
    return (r[n], s)


def PRINT_CUT_ROD_SOLUTION(p, n):
    r, s = MEMOIZED_CUT_ROD_WITH_SOLUTION(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = int(input("Length: "))
    # print("Cut Rod: ", CUT_ROD(p, n - 1))
    # print("Memoized Cut Rod: ", MEMOIZED_CUT_ROD(p, n - 1))
    # print("Bottom Up: ", BOTTOM_UP_CUT_ROD(p, n - 1))
    # r, s = EXTENDED_BOTTOM_UP_CUT_ROD(p, n - 1)
    # print(r[n - 1])
    # print(s)
    # print("Extended Bottom Up: ", PRINT_CUT_ROD_SOLUTION(p, n))
    result = MEMOIZED_CUT_ROD_WITH_SOLUTION(p, n)
    print(result[0])
    print(result[1])
