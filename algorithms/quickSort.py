from random import shuffle

def main():
    A = [i for i in range(1, 101)]
    shuffle(A)
    quicksort(A)
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
