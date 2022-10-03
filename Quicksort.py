def main():
    # A = [2, 8, 7, 1, 3, 5, 6, 4]
    A = [3, 6, 7, 5, 1, 2, 4]
    print(A)
    quicksort(A, len(A))
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
