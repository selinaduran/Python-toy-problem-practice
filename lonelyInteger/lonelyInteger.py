#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# create a dictionary variable
# iterate through the array of integers
    # if current integer does not exist as a key in the dictionary
        # assign it to be a key with a value of 1
    # else, increase key value by 1
# iterate through dictionary and return key whose value is equal to 1

def lonelyinteger(a):
    storage = {}
    for number in a:
        if number not in storage:
            storage[number] = 1
        else:
            storage[number] += 1
    for key in storage:
        if storage[key] == 1:
            return key


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
