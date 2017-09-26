#!/bin/python3

import sys


n = int(input())
arr = [0 if i is 0 else i/abs(i) for i in map(int, input().split())]

for result in map(arr.count, [1, -1, 0]):
    print(round(result/n, 6))
