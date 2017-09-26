#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
appleDistances = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orangeDistances = [int(orange_temp) for orange_temp in input().strip().split(' ')]
houseLeft = s
houseRight = t
appleTreeLoc = a
orangeTreeLoc = b
appleHit = 0
orangeHit = 0

for apple in appleDistances:
    appleLocation = appleTreeLoc + apple
    if houseLeft <= appleLocation and houseRight >= appleLocation:
        appleHit += 1
        
for orange in orangeDistances:
    orangeLocation = orangeTreeLoc + orange
    if houseLeft <= orangeLocation and houseRight >= orangeLocation:
        orangeHit += 1
        
print(appleHit)
print(orangeHit)
