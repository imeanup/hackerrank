# Page 192 COUNTING-SORT(A, B, k)


def COUNTING_SORT(A, B, k):

    """
    let C(0...k) be a new array

    for i = 0 to k
        c[i] = 0

    for j = 1 to A.length
        C[A[j]] = C[A[j]] + 1
    # C[i] now contains the number of elements equal to i.

    for i = 1 to k:
        C[i] = c[i] + C[i-1]
    # C[i] now contains the number of elements less than or equal to i.

    for j = A.lenth downto 1:
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
    """

    C = [0] * k
    for j in range(0, len(A)):
        C[A[j]] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B


if __name__ == "__main__":
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    print("Before ", A)
    k = 1 + max([x for x in A])
    B = [0] * len(A)

    print("After  ", COUNTING_SORT(A, B, k))

""" The algorithm will still work correctly. 
The order that elements are taken out of C and 
put into B doesn't affect the placement of the 
element with same key k. To make it stable, we 
could place the elements of A into a collection 
of elements for each cell in arr C. Then, if we 
use FIFO collection, the modification will be 
stable, if we use LILO, it will be anti-stable.

for i in range(0, len(A)):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= 1
 """

"""
How many interger fall in range[a...b], 
compute C[b]- C[a-1]. This takes O(1) time and 
yeild the desire output.
"""

"""
# From MIT Courseware
# Explanation link: https://www.javatpoint.com/daa-counting-sort or 
# https://courses.csail.mit.edu/6.006/fall10/lectures/lec10.pdf

def counting(A):
    u = 1 + max([x for x in A])
    D = [[] for _ in range(u)]
    for x in A:
        D[x].append(x)
    i = 0
    for chain in D: 
        for x in chain:
            A[i] = x
            i += 1
"""
