# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for i in range(N):
    cC = input()
    if (re.match(r"^[456][0-9]{3}?(-?\d{4}){3}$", cC) and not re.search(r"([0-9])(-?\1){3}",cC)):
        print("Valid")
    else:
        print("Invalid")
