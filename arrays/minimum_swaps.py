# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
# You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in
# ascending order.
# For example, given the array  we perform the following steps:
#
# i   arr                     swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
#
# It took  swaps to sort the array.
# Function Description
# Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of
# swaps to sort the array.
# minimumSwaps has the following parameter(s):
# arr: an unordered array of integers
#
# Input Format
# The first line contains an integer, , the size of .
# The second line contains  space-separated integers .
#
# Output Format
# Return the minimum number of swaps to sort the given array.

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(v):
    swaps = 0
    element = 1
    while element < len(v):
        for i in range(element - 1, len(v)):
            if v[i] == element:
                if i != element - 1:
                    v[element - 1], v[i] = v[i], v[element - 1]
                    swaps += 1
                    break
        element += 1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()