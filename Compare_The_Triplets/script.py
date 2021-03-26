#!/bin/python3

# COMPARE THE TRIPLETS

import math
import os
import random
import re
import sys

#
# If a[0] > b[0], a receives a point
# If a[0] = b[0], nobody gets a point
# If a[0] < b[0], b receives a point
#
# Sample input:
# 5 6 7
# 3 6 10
# Sample output:
# 1 1
#

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ap = 0
    bp = 0
    for i,j in zip(a,b):
        if i > j:
            ap += 1
        elif j > i:
            bp += 1
    output = str(ap) + ' ' + str(bp)
    return output
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
