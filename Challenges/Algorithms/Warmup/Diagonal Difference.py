########################################################################################################### 
# Given a square matrix of size N x N, calculate the absolute difference between the sums of its diagonals.
#
# The first line contains a single integer, N. The next N lines denote the matrix's rows, with each line 
# containing N space-separated integers describing the columns. Print the absolute difference between the 
# two sums of the matrix's diagonals as a single integer.
#
# Coded by: Jason Rigdon
###########################################################################################################

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
    
