#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum_min = 1_000_000_000
    sum_max = 0
    sum_total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                pass
            else:
                sum_total += arr[j]
        if sum_total < sum_min:
            sum_min = sum_total
        if sum_total > sum_max:
            sum_max = sum_total
        sum_total = 0
    print(sum_min, sum_max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


# optimal solution:
print(sum(arr) - max(arr), sum(arr) - min(arr))
