#!/bin/python3

# BREAKING THE RECORDS

import math
import os
import random
import re
import sys

#
# Calculate the number of times a player broke their max and min record
#
# Sample input:
# 9 <------------------------Number of games played
# 10 5 20 20 4 5 2 25 1 <----Points scored per game
# Sample output:
# 2 4 <----------------------Number of times record was broken for best and worst games
#

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxRecord = scores[0]
    minRecord = scores[0]
    maxRecordBroken = 0
    minRecordBroken = 0
    for i in range(n):
        if scores[i] > maxRecord:
            maxRecord = scores[i]
            maxRecordBroken += 1
        if scores[i] < minRecord:
            minRecord = scores[i]
            minRecordBroken += 1
    return maxRecordBroken,minRecordBroken

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
