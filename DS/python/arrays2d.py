#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.

def findMax(arr):
    max_ls = []
    for i in range(0, len(arr)):
        max_ls.append(arr[i])
    return max(max_ls)

def hourglassSum(arr):
    row = 0
    one_hourglass_sum = 0
    mask = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]
    matrix_sums = []
    row_sums = []

    for row_pt in range(0, 4):
        for col_pt in range(0, 4):
            for j in range(0, 3):
                for k in range(0, 3):
                    row_sum = mask[j][k] * arr[row_pt+j][col_pt+k]
                    row = row+row_sum
                one_hourglass_sum = one_hourglass_sum + row
            row_sums.append(one_hourglass_sum)
        matrix_sums.append(row_sums)

    return findMax(matrix_sums)     

if __name__ == '__main__':

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
