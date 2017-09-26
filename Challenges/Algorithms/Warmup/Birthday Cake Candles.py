#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    candleCount = 0
    maxNumber = int(max(ar))
    for i in range(n):
        if ar[i] == maxNumber:
           candleCount += 1
    return(candleCount)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
