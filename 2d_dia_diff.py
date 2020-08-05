#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    print('This function expects a 2d array')
    pds = 0
    sds = 0

    for i in range(len(arr)):
        pds += arr[i][i]
        sds += arr[i][(len(arr)-1)-i]

    diff = abs(pds-sds)
    #return f'The difference between primary and secondary diagonal is: {diff}'
    return diff
    
if __name__ == '__main__':
    

    n = int(input('Enter The Number of Row and Column: ').strip())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input(f'Enter Row {i+1}: ').rstrip().split())))
    
    print(arr)

    for i in range(len(arr)):
        print(f'Row {i+1}: ',arr[i])

    print(diagonalDifference(arr))
    