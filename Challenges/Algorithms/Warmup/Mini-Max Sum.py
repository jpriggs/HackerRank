############################################################################################### 
# Given five positive integers, find the minimum and maximum values that can be calculated by 
# summing exactly four of the five integers. Then print the respective minimum and maximum 
# values as a single line of two space-separated long integers.
#
# Input is a single line of five space-separated integers. Print two space-separated long 
# integers denoting the respective minimum and maximum values that can be calculated by summing 
# exactly four of the five integers. (The output can be greater than 32 bit integer.)
#
# Coded by Jason Rigdon
################################################################################################

#!/bin/python3

import sys

arr = [int(i) for i in input().strip().split(' ')]
print(sum(arr) - max(arr), sum(arr) - min(arr))
