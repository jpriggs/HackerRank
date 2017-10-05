############################################################################################## 
# Consider a staircase of size n = 4:
#
#    #
#   ##
#  ###
# ####
#
# Observe that its base and height are both equal to n, and the image is drawn using # symbols 
# and spaces. The last line is not preceded by any spaces.
#
# Write a program that prints a staircase of size n.
#
# A single integer, n, denoting the size of the staircase. Print a staircase of size n using # 
# symbols and spaces.
#
# Coded by: Jason Rigdon
################################################################################################

#!/bin/python3

import sys


n = int(input())
for i in range(n):
    print(' ' * (n - i - 1) + '#' * (i + 1))
