# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().split()
S = []
for i in s:
    S.append(i) 
res = list(permutations(S, int(k)))
for r in sorted(res):
    print("".join(r))
