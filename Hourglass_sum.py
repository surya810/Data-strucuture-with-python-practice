#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    maximum_sum = -99999
    temp_sum = 0
    
    for i in range(6-2):
        for j in range(0,6-2):
            temp_sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]++arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

            if maximum_sum < temp_sum:
                maximum_sum = temp_sum
    return maximum_sum
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
