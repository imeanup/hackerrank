# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    a, b = input().split()
    try:
        c = int(a)//int(b)
        print(c)
    except Exception as e:
        print("Error Code:", e)
