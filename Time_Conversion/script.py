#!/bin/python3

# TIME CONVERSION

import os
import sys

#
# Convert AM/PM time to military time
#
# Sample input:
# 07:05:45PM
# Sample output:
# 19:05:45
#

def timeConversion(s):
    # Counter in s[x:x] starts at 1 not 0
    # For s[:x] counter starts from start until xth element including x
    hour = int(s[:2]) # Selects everything until 2nd element
    # For s[x:] counter starts after x until end
    meridian = s[8:]  # Selects everything after 8th element
    # Special-case '12AM' == 0, '12PM' == 12 not 24
    if (hour == 12):
        hour = 0
    if (meridian == 'PM'):
        hour += 12
    solution = "%02d" % hour + s[2:8]
    return solution

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input("Enter time in AM/PM format for example (07:00:00PM):")
    result = timeConversion(s)
    print(result)
    # f.write(result + '\n')
    # f.close()
