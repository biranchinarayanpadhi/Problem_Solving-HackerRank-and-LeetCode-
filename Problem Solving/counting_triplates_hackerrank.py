#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the countTriplets function below.
def countTriplets(arr, r):
    count=0
    d2=defaultdict(int)
    d3=defaultdict(int)

    for elem in arr:
        if elem in d3:
            count+=d3[elem]

        if elem in d2: 
            d3[elem*r]+=d2[elem]

        d2[elem*r]+=1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
