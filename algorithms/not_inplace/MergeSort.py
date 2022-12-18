'''
CLRS Merge Sort Pg: 30 Divide and Conqure
'''

import math, random, numpy

def MERGE_SORT(A, p, r):
    if p < r:
        q = math.floor((p + r)/2)
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q + 1, r)
        MERGE(A, p, q, r)

def MERGE(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    '''
    Let L[1..n1+1] and R[1..n2+1] be new arrays
    '''
    L = [0] * n1
    R = [0] * n2

    '''
    for i = 1 to n1
        L[i] = A[p+i-1]
    for j = 1 to n2
        R[j] = A[q+j]
    '''
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]

    '''
    L[n1+1] = ∞
    R[n2+1] = ∞
    '''
    L.append(math.inf)
    R.append(math.inf)

    i, j = 0, 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

if __name__=="__main__":
    '''
    CLRS Ch: 2 Fg 2.3
    '''
    A = [2, 4, 5, 7, 1, 2, 3, 6]
    MERGE_SORT(A, 0, len(A) - 1)
    print(A)

    '''
    random.seed(1)
    index = int(input("Size: "))
    lower = int(input("Low: "))
    upper = int(input("High: "))
    A = []
    for i in range(index):
        A.append(random.randint(lower, upper))
    MERGE_SORT(A, 0, len(A) - 1)
    print(A)
    '''



'''
# Resource: MIT 
import random

def merge_sort(A, a = 0, b = None):     # Sort sub-array A[a:b]
    if b is None:                       # O(1) initialize
        b = len(A)                      # O(1)

    '''
    'if 1 < b - a' # slows down the process. Start from c = (a+b)//2 
    '''
    if 1 < b - a:                       # O(1) size k = b - a
        c = (a + b + 1) // 2            # O(1) compute center
        merge_sort(A, a, c)             # T(k/2) recursively sort left
        merge_sort(A, c, b)             # T(k/2) recursively sort right
        L, R = A[a:c], A[c:b]           # O(k) copy
        i, j = 0, 0                     # O(1) initialize pointers
        while a < b:                    # O(n)
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):   # O(1) check side
                A[a] = L[i]                                     # O(1) merge from left
                i += 1                                          # O(1) decrement left pointer
            else:
                A[a] = R[j]             # O(1) merge from right
                j += 1                  # O(1) decrement right pointer
            a += 1                      # O(1) decrement merge pointer

            
def merge_sort_(A, a = 0, b = None):    # Sort sub-array A[a:b]
    if b is None:                       # O(1) initialize
        b = len(A)                      # O(1)
    if 1 < b - a:                       # O(1) size k = b - a
        c = (a + b + 1) // 2            # O(1) compute center
        merge_sort(A, a, c)             # T(k/2) recursively sort left
        merge_sort(A, c, b)             # T(k/2) recursively sort right
        L, R = A[a:c], A[c:b]           # O(k) copy
        i, j = len(L), len(R)           # O(1) initialize pointers
        while a < b:                    # O(n)
            if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):   # O(1) check side
                A[b-1] = L[i-1]                               # O(1) merge from left
                i -= 1                                        # O(1) decrement left pointer
            else:
                A[b-1] = R[j-1]                               # O(1) merge from right
                j -= 1                                        # O(1) decrement right pointer
            b = b- 1                                          # O(1) decrement merge pointer

            
if __name__ == "__main__":
    A = [i for i in range(1, 101)]
    random.shuffle(A)
    merge_sort(f"A:  {A}")
    merge_sort_(f"A_: {A}")
    print(A)

'''