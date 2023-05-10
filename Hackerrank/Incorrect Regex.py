# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
for i in range(T):
    val = input()
    try:
        re.compile(val)
        print("True")
    except re.error:
        print("False")
        
