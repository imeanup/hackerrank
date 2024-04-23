N = int(input())
A = list(map(int, input().split()))

K = []

f = {}
for i in range(N):
    f[A[i]] = i+1

for i in range(N):
    if i + 1 != A[i]:
        j = f[i+1]
        K.append((i+1, j))
        A[i], A[j-1] = A[j-1], A[i]
        f[A[i]] = i+1
        f[A[j-1]] = j
print(len(K))
for x, y in K:
    print(x, y)