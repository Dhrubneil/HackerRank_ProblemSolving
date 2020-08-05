#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print("Sam's house's starting point: ", s, "unit dist.")
    print("Sam's house's ending point: ", t, "unit dist.")
    print("Position of apple tree: ", a, "unit dist.")
    print("Position of orange tree: ", b, "unit dist.")
    print("Apples fallen: ", m, "unit")
    print("Oranges fallen: ", n, "unit")
    print("Apples' respective positions from tree: ", apples)
    print("Oranges' respective positions from tree: ", oranges)

    apa = []
    ap = 0 
    bpa = []
    bp = 0

    for i in range(len(apples)):
        ap = apples[i] + a 
        apa.append(ap)
    print('Absolute postion of the apples:', apa)

    for i in range(len(oranges)):
        bp = oranges[i] + b 
        bpa.append(bp)
    print('Absolute postion of the apples:', bpa)
    
    ac = 0
    oc = 0

    for i in range(len(apa)):
        if apa[i] in range(s, (t+1)):
            ac += 1
    print("Apple(s) captured:", ac)

    for i in range(len(bpa)):
        if bpa[i] in range(s, t+1)):
            oc += 1
    print("Orange(s) captured", oc)

if __name__ == '__main__':
    st = input("Enter Sam's house's starting and ending position: ").split()

    s = int(st[0])

    t = int(st[1])

    ab = input("Enter the position f apple and orange tree: ").split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input("Enter the number of apples and oranges fallen: ").split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input("Enter apples' distance from apple tree: ").rstrip().split()))

    oranges = list(map(int, input("Enter oranges' distance from orange tree: ").rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
