#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    # Write your code here
    len_arr = len(arr)

    if len_arr == 1:
        return 0

    mid = len_arr // 2
    n = len_arr - mid

    left = arr[:mid]
    right = arr[mid:]

    answer = insertionSort(left) + insertionSort(right)

    count_left = 0
    count_right = 0

    for i in range(len_arr):
        if count_left < mid and\
                (count_right >= n or left[count_left] <= right[count_right]):
            arr[i] = left[count_left]
            answer += count_right
            count_left += 1
        elif count_right < n:
            arr[i] = right[count_right]
            count_right += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
