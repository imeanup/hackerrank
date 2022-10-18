# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://docs.python.org/3/library/itertools.html#itertools.permutations
from itertools import permutations

s, k = input().split()
S = []
for i in s:
    S.append(i) 
res = list(permutations(S, int(k)))
for r in sorted(res):
    print("".join(r))
