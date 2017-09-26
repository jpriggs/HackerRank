#!/bin/python3

import sys

arr = [int(i) for i in input().strip().split(' ')]
print(sum(arr) - max(arr), sum(arr) - min(arr))
