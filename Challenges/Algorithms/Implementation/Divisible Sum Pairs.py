#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    pairs = [0] * k
    count = 0
    for i in ar:
        modValue = i % k
        count += pairs[(k - modValue) % k]
        pairs[modValue] += 1
    return count

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
