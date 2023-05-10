# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    
    ph = r"^([789]){1}([0-9]){9}$"
    if re.match(ph, input()):
        print("YES")
    else:
        print("NO")
