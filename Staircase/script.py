#!/bin/python3

# STAIRCASE

import math
import os
import random
import re
import sys

#
# Sample input:
# 4
# Sample output:
#    #
#   ##
#  ###
# ####
# #
# ##
# ###
# ####
#    ##
#   ####
#  ######
# ########
#

# Complete the staircase function below.
def staircaseUp(n):
    for i in range(n):
        print(" "*(n-i-1)+"#"*(i+1))

def staircaseDown(n):
    for i in range(n):
        print('#'*(i+1))

def staircaseUpDown(n):
    for i in range(n):
        print(" "*(n-i-1)+"#"*(i+1)+'#'*(i+1))

if __name__ == '__main__':
    n = int(input())
    staircaseUp(n)
    staircaseDown(n)
    staircaseUpDown(n)