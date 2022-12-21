'''
Section 4.1 The maximum-subarray problem (Pg: 68 Divide-and-Conquer)
'''

import math

def FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high):
    left_sum = -float('inf')
    sum = 0
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -float('inf')
    sum = 0
    for j in range(mid, high+1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)

def FIND_MAXIMUM_SUBARRAY(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = math.floor((low + high)/2)
        (left_low, left_high, left_sum) = FIND_MAXIMUM_SUBARRAY(A, low, mid)
        (right_low, right_high, right_sum) = FIND_MAXIMUM_SUBARRAY(A, low, mid)
        (cross_low, cross_high, cross_sum) = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)

        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)

        else:
            return (cross_low, cross_high, cross_sum)

if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    a, b, c = FIND_MAXIMUM_SUBARRAY(A, 0, len(A)-1)
    print(max(a, b, c))
    '''
    low = 0
    high = len(A)-1
    mid = math.floor((low + high)/2)
    x, y, z = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
    print(x, y, z)
    '''