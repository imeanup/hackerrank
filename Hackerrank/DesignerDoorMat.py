# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()

N = int(n)
M = int(m)
p = "-"
c = ".|."
w = "WELCOME"

for i in range(N//2):
    print((c*i).rjust(M//2-1, p)+c+(c*i).ljust(M//2-1, p))

print((w).center(M, p))

for i in range(N//2 -1, -1, -1):
    print((c*i).rjust(M//2 -1, p)+c+(c*i).ljust(M//2 -1, p))
