def main():
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    print(A)
    quicksort(A)
    print(A)

def quicksort(A, p=0, r=None):
    if r is None:
        r = len(A) - 1
    def _quicksort(A, p, r):
        if p >= r:
            return
        q = partition(A, p, r)
        _quicksort(A, p, q - 1)
        _quicksort(A, q + 1, r)
    return _quicksort(A, p, r)


def partition(A, p, r):
    x = p
    for j in range(p + 1, r + 1):
        if A[j] <= A[p]:
            x += 1
            A[j], A[x] = A[x], A[j]
    A[x], A[p] = A[p], A[x]
    return x
    

if __name__ == "__main__":
    main()
