#!/bin/python3

# DIAGONAL DIFFERENCE

import math
import os
import random
import re
import sys

#
# Return the absolute difference between the sums of the matrix's two diagonals
#
# Sample input:
# 3 <------------Number of row and columns you want in your square
# 11 2 4 <-------Row1
# 4 5 6 <--------Row2
# 10 8 -12 <-----Row3
# Sample output:
# 15
#
# Left diagonal sum: 11 + 5 - 12 = 4
# Right diagonal sum: 4 + 5 + 10 = 19
# Total absolute sum: |4 - 19| = 15
#

#
# Complete the 'diagonalDifference' function below
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    ld = 0
    rd = 0
    for i in range(len(arr)):
        ld += arr[i][i]
        rd += arr[i][len(arr)-i-1]
    return (abs(ld-rd))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
