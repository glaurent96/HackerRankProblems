#!/bin/python3

# BETWEEN TWO SETS

import math
import os
import random
import re
import sys

#
# Find numbers between the two sets that satify these two conditions:
#   1. The elements of the first array are all factors of the integer being considered
#   2. The integer being considered is a factor of all elements of the second array
#
# Sample input:
# 2 3 <---------State the number of elements that are going to be in each set.
# 2 4 <---------Numbers in set 1
# 16 32 96 <----Numbers in set 2
# Sample output:
# 3 <----------There are 3 numbers in between the two sets that satify the two conditions
#

#
# Complete the 'getTotalX' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    maxA = max(a)
    minB = min(b)
    print('------------------------------------')
    print('First set: ',a)
    print('Second set:',b)
    print('------------------------------------')
    count = 0
    for i in range(maxA, minB + 1):
        print('i:',i)
        for numA in a: # Redundant for loop to understand the logic of one liner for loop below
            if i % numA == 0:
                answer = i % numA
                print(i,'%',numA,'=',answer)
            else:
                answer = i % numA
                print(i,'%',numA,'=',answer)
        isSet1FactorOfI = all([i % numA == 0 for numA in a])
        print('Are the numbers in Set1 factors of i? ',isSet1FactorOfI)
        for numB in b: # Redundant for loop to understand the logic of one liner for loop below
            if numB % i == 0:
                answer = numB % i
                print(numB,'%',i,'=',answer)
            else:
                answer = numB % i
                print(numB,'%',i,'=',answer)
        isFactorOfSet2 = all([numB % i == 0 for numB in b])
        print('Is i a factor of all the numbers in Set2? ',isFactorOfSet2)
        count += isSet1FactorOfI * isFactorOfSet2
        print('Count:',count)
        print('------------------------------------')
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print('Final result: ',total)
    # fptr.write(str(total) + '\n')
    # fptr.close()
