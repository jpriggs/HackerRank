#!/bin/python3

import sys

def solve(year):
    # Complete this function
    day = 0
    if(year==1918):
        day = (256 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31) + 14)
        return(str(day) + '.' + '09' + '.' + str(year))
    elif(year%4==0 and year%100!=0 and year>1918) or (year%400==0 and year>1918) or (year%4==0 and year<=1917):
        day = str(256 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31))
        return(day + '.' + '09' + '.' + str(year))  
    else:
        day = str(256 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31))
        return(day + '.' + '09' + '.' + str(year))

year = int(input().strip())
result = solve(year)
print(result)
