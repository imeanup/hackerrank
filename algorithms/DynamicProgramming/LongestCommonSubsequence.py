def LCS_LENGTH(x, y):
    m = len(x)
    n = len(y)
    c = [[0] * (n+1) for _ in range(m+1)] # Improving Code, Pg. 396, state eliminating `b` table.
    b = [[0] * n for _ in range(m)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i-1][j-1] = "↖"
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "↑"
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "←"

    return c[m][n], b


if __name__=="__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    lcs_length_val, b = LCS_LENGTH(X, Y)
    print(lcs_length_val)
    print(b)
