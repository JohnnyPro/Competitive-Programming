#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    # loop from back to front
    # compare if the previous number is greater than special number
    # if so copy previous number to current then print arr
    # else copy special number to current, print arr then break
    special_num = arr[n-1]
    for i in range(n-1, -1, -1):
        if i == 0:
            arr[i] = special_num
            result = [str(i) for i in arr]
            print(' '.join(result))
        
        elif arr[i-1] >= special_num:
            arr[i] = arr[i-1]
            result = [str(i) for i in arr]
            print(' '.join(result))
            
        else:
            arr[i] = special_num
            result = [str(i) for i in arr]
            print(' '.join(result))
            break
            
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
