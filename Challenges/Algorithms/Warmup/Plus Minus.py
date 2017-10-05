########################################################################################################## 
# Given an array of integers, calculate which fraction of its elements are positive, which fraction of its 
# elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal 
# value of each fraction on a new line.
#
# The first line contains an integer, N, denoting the size of the array. 
# The second line contains N space-separated integers describing an array of numbers (a0, a1, a2,...,an).
#
# Coded by: Jason Rigdon
##########################################################################################################

#!/bin/python3

import sys


n = int(input())
arr = [0 if i is 0 else i/abs(i) for i in map(int, input().split())]

for result in map(arr.count, [1, -1, 0]):
    print(round(result/n, 6))
