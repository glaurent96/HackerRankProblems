#!/bin/python3

# PLUS MINUS

import math
import os
import random
import re
import sys

#
# Calculate the ratios of elements that are positive, negative, and zero in the array
# Print result with 6 places after the decimal
#
# Sample input:
# 6
# -4 3 -9 0 4 1
# Sample output:
# 0.500000
# 0.333333
# 0.166667
#

# Complete the plusMinus function below.
def plusMinus(arr):
    l = len(arr)
    p = 0
    n = 0
    z = 0
    solution = []
    for x in arr:
        if x > 0:
            p += 1
        elif x < 0:
            n += 1
        else:
            z += 1
    print("%.6f" % (p/l))
    print("%.6f" % (n/l))
    print("%.6f" % (z/l))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)