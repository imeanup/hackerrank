def PARENT(i):
    p = (i - 1) // 2
    return p if 0 < i else i


def LEFT(i, n):
    l = 2 * i + 1
    return l if l < n else i


def RIGHT(i, n):
    r = 2 * i + 2
    return r if r < n else i


def MAX_HEAPIFY(A, n, i):
    l = LEFT(i, n)
    r = RIGHT(i, n)
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A, n, largest)


def MIN_HEAPIFY(A, n, i):
    l = LEFT(i, n)
    r = RIGHT(i, n)
    if l < n and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < n and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        MIN_HEAPIFY(A, n, smallest)


def BUILD_MAX_HEAP(A, n):
    for i in range((n//2)-1, -1, -1):
        MAX_HEAPIFY(A, n, i)


def BUILD_MIN_HEAP(A, n):
    for i in range((n//2)-1, -1, -1):
        MIN_HEAPIFY(A, n, i)


def MAX_HEAPSORT(A, n):
    BUILD_MAX_HEAP(A, n)
    print("\nMAX_heapsort\n")
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MAX_HEAPIFY(A, i, 0)
        print(A)


def MIN_HEAPSORT(A, n):
    BUILD_MIN_HEAP(A, n)
    print("\nMIN_heapsort\n")
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MIN_HEAPIFY(A, i, 0)
        print(A)


if __name__ == "__main__":
    from random import shuffle

    # A = [x for x in range(-10, 11)]
    A = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    shuffle(A)
    MAX_HEAPSORT(A, len(A))
    MIN_HEAPSORT(A, len(A))



'''def max_heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def build_max_heap(A, n):
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, n, i)


def heapsort(A, n):
    build_max_heap(A, n)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)


if __name__ == "__main__":
    from random import shuffle
    A = [x for x in range(1, 51)]
    # A = [12, 11, 11, 11, 12, 13, 12, 13, 5, 6, 6, 6, 7] 
    # Testing the equal keys, not placed in the same A.parent.left or A.parent.right 
    # in any subtree. Use the BUILD MAX HEAP (line 37, 38) to test the output.
    N = len(A)
    shuffle(A)
    print("\nUnsorted Array\n",A,"\n")
    # build_max_heap(A, N)
    # print(A) # Out: [13, 13, 12, 12, 11, 12, 6, 6, 11, 7, 6, 11, 5]
    heapsort(A, N)
    print("Sorted Array\n", A, "\n")
'''