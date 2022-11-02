#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

A = []


for _ in range(n):
    matrix_item = input()
    A.append(matrix_item)
B = []
for i in range(m):
    for j in range(n):
        B.append(A[j][i])
        
print(re.sub(r'(?<=\w)\W+(?=\w)', ' ', "".join(B)))
