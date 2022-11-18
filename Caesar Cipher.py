#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase,ascii_uppercase
#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    
    cipher = []
    for i in s:
        if i.isalpha():
            if i.islower():
                ctxt = ascii_lowercase[(ascii_lowercase.index(i) + k)%26]
                cipher.append(ctxt)
            else:
                ctxt = ascii_uppercase[(ascii_uppercase.index(i) + k)%26]
                cipher.append(ctxt)
        else:
            cipher.append(i)

    return "".join(cipher)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
