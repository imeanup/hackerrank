from random import shuffle

''' Insertion sort can require Ω(n^2) comparisons and Ω(n^2) swaps in the worst case. '''

def insertion_sort(A):                    # Insertion sort array A
    for i in range(1, len(A)):            # O(n) loop over array
        j = i                             # O(1) initialize pointer
        while j > 0 and A[j] < A[j -1]:   # O(i) loop over prefix
            A[j-1],A[j] = A[j],A[j-1]     # O(1) swap
            j -= 1                       # O(1) decrement j


if __name__ == "__main__":
    A = [i for i in range(1, 101)]
    shuffle(A)
    insertion_sort(A)
    print(A)
