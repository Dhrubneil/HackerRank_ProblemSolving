import math
import os
import random
import re
import sys

def getTotalX(a, b):
    lcm_num = a[0]
    gcd_num = b[0]

    for i in range(1, len(a)):
        lcm_num = int((lcm_num * a[i])/math.gcd(lcm_num, a[i]))
    
    for i in range(len(b)):
        gcd_num = int(math.gcd(gcd_num, b[i]))

    count = 0

    '''for x in range(lcm_num, gcd_num+1, lcm_num):
        if gcd_num % x == 0:
            count += 1

    return count'''
    my_list = []
    for x in range(lcm_num, gcd_num+1, lcm_num):
        for i in range(len(b)):
            if b[i] % x == 0:
                count += 1
                if count == len(b):
                    my_list.append(x)
        count = 0
    return len(my_list)
if __name__ == '__main__':

    first_multiple_input = input("Enter the number of elements/array respectively: ").rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input("Enter the elements of first array: ").rstrip().split()))

    brr = list(map(int, input("Enter the elements of second array: ").rstrip().split()))

    print(getTotalX(arr, brr))