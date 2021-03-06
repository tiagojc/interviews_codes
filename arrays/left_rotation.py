# Check out the resources on the page's right side to learn more about arrays. The video tutorial is by Gayle Laakmann
# McDowell, author of the best-selling interview book Cracking the Coding Interview.
# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left
# rotations are performed on array , then the array would become .
# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be
# printed as a single line of space-separated integers.
#
# Function Description
# Complete the function rotLeft in the editor below. It should return the resulting array of integers.
# rotLeft has the following parameter(s):
# An array of integers .
# An integer , the number of rotations.
#
# Input Format
# The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
# The second line contains  space-separated integers .
# Constraints
#
#
#
# Output Format
# Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.



#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    out = list()
    if d >= 1:
        for i in range(d, len(a)):
            out.append(a[i])
        for i in range(0, d):
            out.append(a[i])
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()