#!/bin/python3

# NUMBER LINE JUMPS

import math
import os
import random
import re
import sys

#
# Input variables are x1,v1,x2,v2
# The first kangaroo starts at location x1 and moves at the rate of v1
# The second kangaroo starts at location x2 and moves at a rate of v2
# If both kangaroos with be eventually be at the same location print YES else NO
#
# Sample input:
# 0 3 4 2
# Sample output:
# YES
#

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return 'NO'
    else:
        if v1 != v2 and (x2-x1)%(v2-v1) == 0:
            return 'YES' 
        else:
            return 'NO'
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
