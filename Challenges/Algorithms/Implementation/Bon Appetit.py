#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    totalCost = 0
    overcharge = 0
    for i in ar:
        totalCost += i
    totalCost -= ar[k]
    if(totalCost != b*2):
        overcharge = b - (totalCost / 2)
        return(int(overcharge))
    else:
        return("Bon Appetit")
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
