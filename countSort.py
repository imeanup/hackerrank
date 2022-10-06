# Explanation link: https://www.javatpoint.com/daa-counting-sort or https://courses.csail.mit.edu/6.006/fall10/lectures/lec10.pdf
# Page 192 COUNTING-SORT(A, B, k)
# 

A = [7,1,3,1,2,4,5,7,2,4,3]
k = 1 + max([x for x in A])

# let C(0...k) be a new array
# for i = 0 to k
#   c[i] = 0
C = [0]*k

# for j = 1 to A.length
#   C[A[j]] += 1
# C[i] now contains the number of elements equal to i.

for j in range(0, len(A)):
    C[A[j]] += 1   
print(f"C: {C}")

''' This takes O(1) time and yeild the desire output
for i in range(1, k):
    C[i] -= C[i-1]
    '''

# for i = 1 to k:
#   C[i] += C[i-1]
# C[i] now contains the number of elements less than or equal to i.
for i in range(1, k):
    C[i] += C[i-1]
print(f"C:  {C}")

B = [0]*len(A)
print(f"B:  {B}")

# for j = A.lenth downto 1:
#   B[C[A[j]]] = A[j]
#   C[A[j]] -= 1
for i in range(len(A)-1, -1, -1):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= 1

''' The algorithm will still work correctly. The order that elements are taken out
of C and ut into B doesn't affect the placement of the element with same key k. To make it stable,
we could place the elements of A into a collection of elements for each cell in arr C. Then, if we use 
FIFO collection, the modification will be stable, if we use LILO, it will be anti-stable.

for i in range(0, len(A)):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= 1
 '''

print(f"B:  {B}")
