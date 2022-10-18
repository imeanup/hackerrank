from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

lis = []   
for v in product(A, B):
    lis.append(v)

for i in lis:
    print(i, end=" ")
