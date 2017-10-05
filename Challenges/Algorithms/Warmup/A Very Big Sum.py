######################################################################################################## 
# You are given an array of integers of N size . You need to print the sum of the elements in the array, 
# keeping in mind that some of those integers may be quite large. 
# 
# The first line of the input consists of an integer N. The next line contains N space-separated integers 
# N contained in the array. Print a single value equal to the sum of the elements in the array.
#
# Coded by: Jason Rigdon
#########################################################################################################

#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    sum = 0
    for i in range(n):
        sum += ar[i]
    return (sum)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
