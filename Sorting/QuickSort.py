from random import randrange as RANDOM

"""Assumption that all permutation of the input # are equally likely."""


def QUICKSORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q - 1)
        QUICKSORT(A, q + 1, r)


""" Random sampling, instead of chosing A[r] as pivot, we will select a 
randomly chosen element from the subarray A[p...r]. We will do so by 
first exchanging element A[r] with an element chosen at random from 
A[p...r]. Pivot be any of the (r - p + 1) elements in the subarray."""


def RANDOMIZED_QUICKSORT(A, p, r):
    if p < r:
        q = RANDOMIZED_PARTITION(A, p, r)
        RANDOMIZED_QUICKSORT(A, p, q - 1)
        RANDOMIZED_QUICKSORT(A, q + 1, r)


def RANDOMIZED_PARTITION(A, p, r):
    i = RANDOM(p, r)
    A[r], A[i] = A[i], A[r]
    return PARTITION(A, p, r)


""" Lomuto Partition """


def PARTITION(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


"""C. A. R. Hoare, line 65 returns the sorted array."""


def HOARE_PARTITION(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while A[j] > x:
            j -= 1

        i += 1
        while A[i] < x:
            i += 1

        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            # print(A)
            return j


"""
Tail recursion, it provided automatically by good complier.
The second recursive call in QUICKSORT is not really necessary; 
we can avoid it by using an iterative control structure.
"""


def TAIL_RECURSIVE_QUICKSORT(A, p, r):
    while p < r:
        # Partition and sort left subarray
        q = PARTITION(A, p, r)
        TAIL_RECURSIVE_QUICKSORT(A, p, q - 1)
        p = q + 1


"""
[2, 8, 7, 1, 3, 5, 6, 4]

def PARTITION(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
        print(A)
    A[i], A[r] = A[r], A[i]
    print(A)


[2, 8, 7, 1, 3, 5, 6, 4]
[2, 8, 7, 1, 3, 5, 6, 4]
[2, 8, 7, 1, 3, 5, 6, 4]
[2, 1, 7, 8, 3, 5, 6, 4]
[2, 1, 3, 8, 7, 5, 6, 4]
[2, 1, 3, 8, 7, 5, 6, 4]
[2, 1, 3, 8, 7, 5, 6, 4]
[2, 1, 3, 4, 7, 5, 6, 8]
"""


def RANDOMIZED_SELECT(A, p, r, i):
    if p == r:
        return A[p]
    q = RANDOMIZED_PARTITION(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return RANDOMIZED_SELECT(A, p, q-1, i)
    else:
        return RANDOMIZED_SELECT(A, q+1, r, i-k)


if __name__ == "__main__":
    A = [2, 8, 7, 1, 3, 5, 6, 4]  # Classic example from CLRS
    TAIL_RECURSIVE_QUICKSORT(A, 0, len(A) - 1)
    print(A)

    """
    PARTITION(A, 0, len(A)-1)
    HOARE_PARTITION(A, 0, len(A) - 1)
    """
    import numpy

    B = numpy.random.randint(20, size=(20))
   
    RANDOMIZED_SELECT(B, 0, len(B)-1, 3)
    print(B)


'''
from random import shuffle

def main():
    A = [i for i in range(1, 101)]
    shuffle(A)
    quicksort(A)
    print(A)
    
def quicksort(A, len):
    sort(A, 0, len - 1)


def sort(A, lo, hi):
    if lo < hi:
        j = partition(A, lo, hi)
        sort(A, lo, j-1)
        sort(A, j+1, hi)

        
def partition(A,lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi] = A[hi], A[i]
    return i


if __name__ == "__main__":
    main()
'''