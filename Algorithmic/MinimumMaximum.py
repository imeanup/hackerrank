"""
CLRS: Chapter 9
"""


class Pair:
    def __init__(self):
        self.min = 0
        self.max = 0


"""
Comparisons, Total is 2n-2 comparisons
Linear Search, Time: O(n), Space: O(1)
Total # of comparisons 1+2(n-2)
"""


def getMinMax(arr: list, n: int):
    minmax = Pair()

    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax


"""
Pair comparisons
"""


def _getMinMax(arr):
    n = len(arr)
    if n % 2 == 0:
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i = 2
    else:
        mx = mn = arr[0]
        i = 1

    while i < n - 1:
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
        i += 2
    return mx, mn


"""
CLRS Pg: 215. The total # of comparisons is at most 3⌊n/2⌋.
n -> Even, (3n/2 - 2) comparisons
n -> Odd, 3(n-2)/2 comparisons
Time: O(n), Space: O(lg n)
"""


def _MinMax(arr, low, high):
    arr_Max = arr[low]
    arr_Min = arr[low]

    if low == high:
        arr_Max = arr[low]
        arr_Min = arr[low]
        return arr_Max, arr_Min

    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_Max = arr[low]
            arr_Min = arr[high]
        else:
            arr_Max = arr[high]
            arr_Min = arr[low]
        return arr_Max, arr_Min

    else:
        mid = (low + high) // 2
        arr_Max1, arr_Min1 = _MinMax(arr, low, mid)
        arr_Max2, arr_Min2 = _MinMax(arr, mid + 1, high)
        return max(arr_Max1, arr_Max2), min(arr_Min1, arr_Min2)


if __name__ == "__main__":
    import numpy

    array = numpy.random.randint(3000, size=(20))
    minmax = getMinMax(array, len(array))
    print("Linear Search: ", minmax.min, minmax.max)

    mx, mn = _getMinMax(array)
    print("Pair Comp ", mn, mx)

    arr_Max, arr_Min = _MinMax(array, 0, len(array) - 1)
    print("DnC: ", arr_Min, arr_Max)
