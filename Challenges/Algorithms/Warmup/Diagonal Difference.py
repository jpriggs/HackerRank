#!/bin/python3

import sys


n = int(input().strip())
firstSum = 0
secondSum = 0
for i in range(n):
    row = list(map(int, input().strip().split(' ')))
    firstSum += int(row[i])
    secondSum += int(row[(n - i - 1)])
print (abs(firstSum - secondSum))   
    
