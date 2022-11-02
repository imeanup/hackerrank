# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter 
l = []
for i in range(int(input())):
    l.append(input())
val = Counter(l).values()
print(len(val))
print(*val)
    
