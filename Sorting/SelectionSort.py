from random import shuffle

'''Selection sort can require Ω(n^2)comparisons, but will perform at most O(n) swaps in the worst case. '''

def selection_sort(A):
    for i in range(len(A) - 1, 0, -1):      # O(n) loop over array
        m = i                               # O(1) initial index of max
        for j in range(i):                  # O(i) search for max in A[:i]
            if A[m] < A[j]:                 # O(1) check for larger value
                m = j                       # O(1) new max found
        A[m], A[i] = A[i], A[m]             # O(1) swap

if __name__ == "__main__":
    A = [i for i in range(1, 101)]
    shuffle(A)
    selection_sort(A)
    print(A)
