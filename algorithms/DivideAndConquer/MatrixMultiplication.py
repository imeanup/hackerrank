def SQUARE_MATRIX_MULTIPLY(A, B):
    m = len(A)
    n = len(B[0])
    C = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C


'''
SQUARE-MATRIX-MULTIPLY-RECURSIVE (A, B)
	n = A.rows
	let C be a new n x n matrix
	if n == 1
		c11 = a11 x b1
	else partition A, B, and C as in equations (4.9)
		C11 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A11, B11)
		    + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A12, B21)       
		C12 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A11, B12)
	        + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A12, B22)        
		C21 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A21, B11)
	        + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A22, B21)        
		C22 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A21, B12)
	        + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A22, B22)
	    return C
'''

# TODO: Fix the bug in the code Not working
def SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B):
    n = len(A)
    C = EMPTY_MATRIX(n)

    if n == 1:
        return A[0][0] * B[0][0]

    step = int(n / 2)

    A11 = SUB_MATRIX(A, 0, 0, step)
    A12 = SUB_MATRIX(A, 0, step, step)
    A21 = SUB_MATRIX(A, step, 0, step)
    A22 = SUB_MATRIX(A, step, step, step)
    B11 = SUB_MATRIX(B, 0, 0, step)
    B12 = SUB_MATRIX(B, 0, step, step)
    B21 = SUB_MATRIX(B, step, 0, step)
    B22 = SUB_MATRIX(B, step, step, step)

    # TODO: line 30, in SQUARE_MATRIX_MULTIPLY_RECURSIVE C11 = SUM(
    C11 = SUM(
        SQUARE_MATRIX_MULTIPLY_RECURSIVE(A11, B11),
        SQUARE_MATRIX_MULTIPLY_RECURSIVE(A12, B21),
    )

    C12 = SUM(
        SQUARE_MATRIX_MULTIPLY_RECURSIVE(A11, B12),
        SQUARE_MATRIX_MULTIPLY_RECURSIVE(A12, B22),
    )

    C21 = SUM(
        SQUARE_MATRIX_MULTIPLY_RECURSIVE(A21, B11),
        SQUARE_MATRIX_MULTIPLY_RECURSIVE(A22, B21),
    )

    C22 = SUM(
        SQUARE_MATRIX_MULTIPLY_RECURSIVE(A21, B12),
        SQUARE_MATRIX_MULTIPLY_RECURSIVE(A22, B22),
    )

    return CREATE(C11, C12, C21, C22)


def SUB_MATRIX(A, row, col, n):
    C = EMPTY_MATRIX(n)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i + row][j + col]
    return C

# TODO: line 64, in SUM return A[i][j] + B[i][j]
# TODO: TypeError: object of type 'int' has no len()
def SUM(A, B):
    n = len(A)
    return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
    
# TODO: TypeError: 'int' object is not subscriptable

def EMPTY_MATRIX(n):
    return [[None] * n for _ in range(n)]


def CREATE(C11, C12, C21, C22):
    size = len(C11)
    C = EMPTY_MATRIX(len(C11) * 2)
    for i in range(size):
        for j in range(size):
            C[i][j] = C11[i][j]
    for i in range(size):
        for j in range(size):
            C[i][j + size] = C12[i][j]
    for i in range(size):
        for j in range(size):
            C[i + size][j] = C21[i][j]
    for i in range(size):
        for j in range(size):
            C[i + size][j + size] = C22[i][j]
    return C


if __name__ == "__main__":
    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]
    C = SQUARE_MATRIX_MULTIPLY(A, B)
    D = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B)
    print(D)
