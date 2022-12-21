def SQUARE_MATRIX_MULTIPLY(A, B):
    m = len(A)
    n = len(B[0])
    C = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]
    C = SQUARE_MATRIX_MULTIPLY(A, B)
    print(C)