######################################################################################################
# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding 
# points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
# 
# We define the rating for Alice's challenge to be the triplet A = (a0, a1, a2), and the rating for 
# Bob's challenge to be thetriplet B = (b0, b1, b2).
# 
# Your task is to find their comparison points by comparing a0 with b0, a1 with b1, and a2 with b2.
#
# Coded by: Jason Rigdon
######################################################################################################

#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a = (a0 > b0) + (a1 > b1) + (a2 > b2)
    b = (a0 < b0) + (a1 < b1) + (a2 < b2)
    return (a,b)
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
