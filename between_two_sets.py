#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

'''def getTotalX(a, b):
    # Write your code here
    print(arr)
    print(brr)
    a = arr[0]
    b = brr[0] + 1
    fp = []
    fpf = []
    for num in range(a, b):
        for i in range(len(arr)):
            if num % arr[i] == 0:
                if num not in fp:
                    fp.append(num)
                else:
                    if num not in fpf:
                        fpf.append(num)
    print(fp)
    print(fpf)
    x = 0
    sf = []
    for num in fpf:
        for i in range(len(brr)):
            if brr[i] % num == 0:
                x += 1
                if x == len(brr):
                    sf.append(num)
        x = 0
    print(sf)
    return len(sf)

if __name__ == '__main__':

    first_multiple_input = input("Enter the number of elements/array respectively: ").rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input("Enter the elements of first array: ").rstrip().split()))

    brr = list(map(int, input("Enter the elements of the second array: ").rstrip().split()))

    print(getTotalX(arr, brr))'''

#arr = [[1,2,3], [2,3,4], [1,2,3,4]]
#x = min(arr)
#print(x)

if __name__ == '__main__':

    first_multiple_input = input("Enter the number of elements/array respectively: ").rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input("Enter the elements of first array: ").rstrip().split()))

    brr = list(map(int, input("Enter the elements of second array: ").rstrip().split()))

    a = max(arr)
    b = brr[0] + 1
    fp = []
    for i in range(len(arr)):
        my_list = []
        for num in range(a, b):
            if num % arr[i] == 0:
                my_list.append(num)
                if my_list not in fp:
                    fp.append(my_list)

    print(fp)
    my_len = len(fp[0])
    my_list = []
    if len(fp) == 1:
            my_list = fp[0]

    else:
        for li in fp:
            if len(li) < my_len:
                my_list = li
                my_len = len(my_list)

    print(my_list)
    x = 0
    sf = []
    for num in my_list:
        for i in range(len(brr)):
            if brr[i] % num == 0:
                x += 1
                if x == len(brr):
                    sf.append(num)
        x = 0
    print(sf)
    #for first_array = [3, 6, 9], 9 is not divisible by 6