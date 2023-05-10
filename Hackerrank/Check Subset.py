# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for i in range(T):
    A = int(input())
    a = set(map(int, input().split()))
    B = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
