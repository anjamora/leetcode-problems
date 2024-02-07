#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr2 = [0,0,0]
    
    for i in arr:
        if i > 0:
            arr2[0] += 1
        elif i < 0:
            arr2[1] += 1
        else:
            arr2[2] += 1
    
    for i in arr2:
        print("{:.{}f}".format(i/len(arr),6))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
