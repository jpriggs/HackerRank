#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    bird = (sorted(reversed(list(set(ar))), key=ar.count)[-1])
    return(bird)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
