from random import shuffle

''' Bubble sort is popular but inefficient sorting algorithm.

CLRS 

*BUBBLESORT(A):
for i = 1 to A.length - 1
    for j = A.length downto i + 1
        if A[j] < A[j - 1]
            exchange A[j] with A[j - 1]        
'''

def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]
    
def bubble_sort(A):
    l = len(A)
    for i in range(l):
        for j in range(0, l-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


if __name__=="__main__":
    A = [x for x in range(-51, 51)]
    shuffle(A)
    print(f"\nArray\n\n{A}")
    bubble_sort(A)
    print(f"\nArray\n\n{A}\n")
