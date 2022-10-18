# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, k = input().split()
S = list(s)
S.sort()
for i in range(1, int(k)+1):
    res = list(combinations(S, i))
    for r in res:
        print("".join(r))
