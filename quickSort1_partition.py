#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(A):
    # Write your code here
    # pivot = A[0] = 5
    #left = {4,3}, right = {7,8}, equal = {5}
    # order doesn't matter for left and right elements
    sort(A, 0, len(A) -1)
    return A
    
def sort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        sort(A, lo, p-1)
        sort(A, p+1, hi)
    
def partition(A, lo, hi):
    p = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi] = A[hi],A[i]
    return i
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
