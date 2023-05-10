# Enter your code here. Read input from STDIN. Print output to STDOUT
v = input().split()
N, X = int(v[0]), int(v[1])


marks = [map(float, input().split()) for _ in range(X)]
    
for i in zip(*marks):
    print(sum(i)/X)
