#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# hh:mm:ssAM or hh:mm:ssPM

def timeConversion(s):
    # Write your code here
    ''' https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes '''
    return datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
