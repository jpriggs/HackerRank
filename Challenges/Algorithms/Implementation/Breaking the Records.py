#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    highestScore = 0
    lowestScore = 0
    increaseCounter = 0
    decreaseCounter = 0
    gameNumber = 0

    for currentScore in s:
        if gameNumber == 0:
            highestScore = currentScore
            lowestScore = currentScore
        
        if currentScore > highestScore:
            highestScore = currentScore
            increaseCounter += 1
        
         if currentScore < lowestScore:
             lowestScore = currentScore
             decreaseCounter += 1

         gameNumber += 1

    return(increaseCounter, decreaseCounter)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))

