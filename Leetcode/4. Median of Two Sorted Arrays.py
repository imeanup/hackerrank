'''
To find the median of two sorted arrays in O(lg(n+m)) time, use the following algorithm:

Combine the two arrays into a single sorted array.
If the length of the combined array is odd, return the element at index n // 2, where n is the length of the combined array.
If the length of the combined array is even, return the average of the elements at indices n // 2 - 1 and n // 2, where n is the length of the combined array.
'''

def median(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    combined = []
    i = 0
    j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:
            combined.append(arr2[j])
            j += 1
    combined.extend(arr1[i:])
    combined.extend(arr2[j:])
    if (n + m) % 2 == 0:
        return (combined[(n + m) // 2 - 1] + combined[(n + m) // 2]) / 2
    else:
        return combined[(n + m) // 2]

'''
O(lg(min(n,m))) time
'''
def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
    n = len(arr1)
    m = len(arr2)
    if n < m:
        return self.findMedianSortedArrays(arr2, arr1)
    lo = 0
    hi = m * 2
    while lo <= hi:
        mid2 = (lo + hi) // 2
        mid1 = n + m - mid2
        L1 = float('-inf') if mid1 == 0 else arr1[(mid1 - 1) // 2]
        L2 = float('-inf') if mid2 == 0 else arr2[(mid2 - 1) // 2]
        R1 = float('inf') if mid1 == n * 2 else arr1[mid1 // 2]
        R2 = float('inf') if mid2 == m * 2 else arr2[mid2 // 2]
        if L1 > R2:
            lo = mid2 + 1
        elif L2 > R1:
            hi = mid2 - 1
        else:
            return (max(L1, L2) + min(R1, R2)) / 2
    return float('nan')


'''
To do this in O(lg(min(n,m))) time, the following algorithm is useful:

Set L to the index of the first element in the first array, and R to the index of the last element in the first array.
While L <= R, do the following:
Set i to the floor of (L + R) / 2.
Set j to the floor of (n + m + 1) / 2 - i.
If i is too small (i.e., j > 0 and arr1[i - 1] > arr2[j]), set L to i + 1.
If i is too large (i.e., j < m and arr1[i] < arr2[j - 1]), set R to i - 1.
Otherwise, i is the correct value, so continue to the next step.
If n is odd, return max(arr1[i - 1], arr2[j]).
If n is even, return the average of max(arr1[i - 1], arr2[j]) and min(arr1[i], arr2[j - 1]).
'''
def median(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    if n > m:
        arr1, arr2, n, m = arr2, arr1, m, n
    L = 0
    R = n
    while L <= R:
        i = (L + R) // 2
        j = (n + m + 1) // 2 - i
        if j > 0 and i < n and arr1[i] < arr2[j - 1]:
            L = i + 1
        elif i > 0 and j < m and arr1[i - 1] > arr2[j]:
            R = i - 1
        else:
            if i == 0:
                max_left = arr2[j - 1]
            elif j == 0:
                max_left = arr1[i - 1]
            else:
                max_left = max(arr1[i - 1], arr2[j - 1])
            if (n + m) % 2 == 1:
                return max_left
            if i == n:
                min_right = arr2[j]
            elif j == m:
                min_right = arr1[i]
            else:
                min_right = min(arr1[i], arr2[j])
            return (max_left + min_right) / 2
