#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    updatedGrades = []
    for grade in grades:
        gradeDiff = grade % 5
        if gradeDiff > 2 and grade > 37:
            updatedGrades.append(grade + 5 - gradeDiff)
        else:
            updatedGrades.append(grade)
    return(updatedGrades)
    
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))