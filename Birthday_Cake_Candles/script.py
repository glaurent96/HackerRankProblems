#!/bin/python3

# BIRTHDAY CAKE CANDLES

import math
import os
import random
import re
import sys

#
# First type the number of candles you want on the cake then press enter
# Then type the height of each candle separated by spaces then press enter
# Result: The program will print the number of tallest candles
#
# Sample input:
# 4
# 3 2 1 3
# Sample output:
# 2
#

def birthdayCakeCandles(candles):
    # Write your code here
    return candles.count(max(candles))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()