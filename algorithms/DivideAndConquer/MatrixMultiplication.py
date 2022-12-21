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

def SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B):
    # m = len(A)
    # n = len(B[0])
    C = [[0 for i in range(2)] for j in range(2)]
    # if m == 0:
    #     C[0][0] = A[0][0] * B[0][0]

    # else:
    C[0][0] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][0], B[0][0]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][1], B[1][0])
    C[0][1] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][0], B[0][1]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][0], B[1][1])
    C[1][0] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][0], B[0][0]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][1], B[1][1])
    C[1][1] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][0], B[0][1]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][1], B[1][1])

    return C


if __name__ == "__main__":
    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]
    C = SQUARE_MATRIX_MULTIPLY(A, B)
    D = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B)
    print(D)
