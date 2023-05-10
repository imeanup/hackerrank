# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://docs.python.org/3/library/itertools.html#itertools.groupby

from itertools import groupby
l= []
s = input()
for res, k in (groupby(s)):
    count = 0
    for i in k:
        if i == res:
            count += 1
    l.append((count,int(res)))
    
print(" ".join(map(str, l)))
