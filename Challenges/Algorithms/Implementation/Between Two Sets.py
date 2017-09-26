#!/bin/python3

import sys

def getTotalX(a, b):
    # Complete this function
    #n = number of A values
    #m = number of B values
    #a = array of A values
    #b = array of B values
    counter = 0
    for i in range(max(a), min(b) + 1):
        if all(i % aValue == 0 for aValue in a) and all(bValues % i == 0 for bValues in b):
            counter += 1
    return counter
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
