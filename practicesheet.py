#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#



if __name__ == '__main__':

    arr =  [-4,3,-9,0,4,1]
    arr2 = [0,0,0]

    
    for i in arr:
        if i > 0:
            arr2[0] += 1
        elif i < 0:
            arr2[1] += 1
        else:
            arr2[2] += 1
        print(i)
    
    for i in arr2:
        print(i)
        print("{:.{}f}".format(i/len(arr),6))

