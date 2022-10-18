from itertools import combinations_with_replacement as c

s,k = input().split()
S = list(s)
S.sort()
res = c(S, int(k))
for j in res:
    print("".join(j))
