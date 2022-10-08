#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i]:
            tmp = arr[i]
            arr[i] = arr[i-1]
            print(*arr)
            arr[i-1] = tmp
    print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
