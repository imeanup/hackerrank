def COUNTING_SORT(arr, d):
    n = len(arr)
    count = [0] * 10

    """
    Store count of occurrences in count[]
    """
    for i in range(0, n):
        count[(arr[i] // d) % 10] += 1

    """
    Updating the count[i] s.t. count[i] contains actual position
    of this digit in temp[].
    """
    for i in range(1, 10):
        count[i] += count[i - 1]

    """
    Making a temporary array to store the output
    """
    tmp = [0] * n

    """
    Building the output array i.e. temp[]
    """
    for i in range(n - 1, -1, -1):
        tmp[count[(arr[i] // d) % 10] - 1] = arr[i]
        count[(arr[i] // d) % 10] -= 1
    # print("T: ", tmp)

    """
    copying output array to actual array with sorted numbers.
    """
    for i in range(0, n):
        arr[i] = tmp[i]


def RADIX_SORT(A, d):
    """
    for i = 1 to d
        use a stable sort to sort array A on digit i
    """
    MIN = min(A)
    MIN = -MIN if MIN < 0 else 0
    for i in range(len(A)):
        A[i] += MIN
    
    MAX = max(A)

    """
    Instead of passing the digit numbers, d is passed, i.e. d^i
    where i is the current digit number.
    """
    while MAX / d > 1:
        COUNTING_SORT(A, d)
        d *= 10

    for i in range(len(A)):
        A[i] -= MIN


if __name__ == "__main__":
    A = [329, 457, 657, 839, 436, 720, 355]
    RADIX_SORT(A, 1)
    print(A)
