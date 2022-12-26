from Sorting.insertionSort import insertion_sort


def BUCKET_SORT(A):
    """
    let B[0...n-1] be a new array
    n = A.length
    for i = 0 to n-1
        make B[i] an empty list
    for i = 1 to n
        insert A[i] into list B[⌊nA[i]⌋]
    for i = 0 to n-1
        sort list B[i] with insertion sort
    concatenate the lists B[0], B[1], ...., B[n-1] together in order
    """
    B = []
    n = len(A)

    for i in range(n):
        B.append([])

    for i in range(1, n + 1):
        j = int(n * A[i - 1])
        B[j].append(A[i - 1])

    for i in range(n):
        insertion_sort(B[i])
    """
    return [x for i in B for x in i]
    """
    return sum(B, [])  # concatenate (or) join list of lists


if __name__ == "__main__":
    """
    CLRS Page. 201 Fig 8.4 Example
    """
    A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print(BUCKET_SORT(A))
