#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    elevation = 0
    numOfValleys = 0
    
    for step in path:
        tempElevation = elevation
        elevation = elevation+1 if step == 'U' else elevation-1
        if elevation == 0 and tempElevation < 0:
            numOfValleys +=1
    
    return numOfValleys
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
