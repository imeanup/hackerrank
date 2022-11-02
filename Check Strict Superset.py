# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
answer = True
for i in range(int(input())):
    N = set(input().split())
    if not A.issuperset(N):
        answer = False
        break
print(answer)
