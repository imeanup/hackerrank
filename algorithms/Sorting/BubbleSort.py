from random import shuffle

''' Bubble sort is popular but inefficient sorting algorithm.

CLRS 

*BUBBLESORT(A):
for i = 1 to A.length - 1
    for j = A.length downto i + 1
        if A[j] < A[j - 1]
            exchange A[j] with A[j - 1]        
'''

def BUBBLESORT(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]
    
def _BUBBLESORT(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


if __name__=="__main__":
    A = [x for x in range(-51, 51)]
    shuffle(A)
    print(f"\nArray\n\n{A}")
    _BUBBLESORT(A)
    print(f"\nArray\n\n{A}\n")
