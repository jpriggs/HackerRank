########################################################################################################## 
# Colleen is turning n years old! Therefore, she has n candles of various heights on her cake, 
# and candle i has height height(i). Because the taller candles tower over the shorter ones, 
# Colleen can only blow out the tallest candles.
#
# The first line contains a single integer,n, denoting the number of candles on the cake. The 
# second line contains n space-separated integers, where each integer i describes the height of candle i.
# Print the number of candles Colleen blows out on a new line.
#
# Coded by: Jason Rigdon
###########################################################################################################

#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    candleCount = 0
    maxNumber = int(max(ar))
    for i in range(n):
        if ar[i] == maxNumber:
           candleCount += 1
    return(candleCount)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
