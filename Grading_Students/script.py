#!/bin/python3

# GRADING STUDENTS

import math
import os
import random
import re
import sys

#
# If the difference between the grade and the next multiple of 5 is less 3:
# * Round grade up to next multiple of 5
# If the grade is below a 38 no rounding occurs
#
# Sample input:
# 4 <------------Number of students
# 73 <-----------Grade1
# 67 <-----------Grade2
# 38 <-----------Grade3
# 33 <-----------Grade4
# Sample output:
# 75
# 67
# 40
# 33
#

#
# Complete the 'gradingStudents' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    gradesList = []
    for grade in grades:
        if grade >= 38 and grade % 5 > 2:
            # / is used for floating point division (with decimals nums)
            # // is used for integer division (without decimal nums)
            grade = -(-grade//5)*5
            gradesList.append(grade)
        else:
            gradesList.append(grade)
    return gradesList
            

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    print( "Results:")
    for i in range(len(result)):
        print(result[i])
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
