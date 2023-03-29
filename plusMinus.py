#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0

    for number in arr:
        if number >= 1:
            positives += 1
        elif number == 0:
            zeros += 1
        else:
            negatives += 1

    print(positives/len(arr))
    print(negatives/len(arr))
    print(zeros/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
