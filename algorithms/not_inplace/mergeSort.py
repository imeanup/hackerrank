import random

def merge_sort(A, a = 0, b = None):     # Sort sub-array A[a:b]
    if b is None:                       # O(1) initialize
        b = len(A)                      # O(1)
    if 1 < b - a:                       # O(1) size k = b - a
        c = (a + b + 1) // 2            # O(1) compute center
        merge_sort(A, a, c)             # T(k/2) recursively sort left
        merge_sort(A, c, b)             # T(k/2) recursively sort right
        L, R = A[a:c], A[c:b]           # O(k) copy
        i, j = 0, 0                     # O(1) initialize pointers
        while a < b:                    # O(n)
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):   # O(1) check side
                A[a] = L[i]                                     # O(1) merge from left
                i += 1                                          # O(1) decrement left pointer
            else:
                A[a] = R[j]             # O(1) merge from right
                j += 1                  # O(1) decrement right pointer
            a += 1                      # O(1) decrement merge pointer

            
def merge_sort_(A, a = 0, b = None):    # Sort sub-array A[a:b]
    if b is None:                       # O(1) initialize
        b = len(A)                      # O(1)
    if 1 < b - a:                       # O(1) size k = b - a
        c = (a + b + 1) // 2            # O(1) compute center
        merge_sort(A, a, c)             # T(k/2) recursively sort left
        merge_sort(A, c, b)             # T(k/2) recursively sort right
        L, R = A[a:c], A[c:b]           # O(k) copy
        i, j = len(L), len(R)           # O(1) initialize pointers
        while a < b:                    # O(n)
            if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):   # O(1) check side
                A[b-1] = L[i-1]                               # O(1) merge from left
                i -= 1                                        # O(1) decrement left pointer
            else:
                A[b-1] = R[j-1]                               # O(1) merge from right
                j -= 1                                        # O(1) decrement right pointer
            b = b- 1                                          # O(1) decrement merge pointer

            
if __name__ == "__main__":
    A = [i for i in range(1, 101)]
    random.shuffle(A)
    merge_sort(f"A:  {A}")
    merge_sort_(f"A_: {A}")
    print(A)
