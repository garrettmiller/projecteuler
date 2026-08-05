#!/usr/bin/python3
# The cube 41063625 (345^3) can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.
# Brooke gave me this as a birthday challenge in 2026 :) 

# Seems like it would have worked but was prohibitively slow
# Ideas: jump ahead to largest cube, also removing tested cubes from cubeSet 
# (but can't guarantee this is working properly)

from itertools import permutations
from math import cbrt
import sys

cubeSet = []
smallestCube = 9999999999999

#Build a list of cubes
print("Building cube list...")
for i in range(10,10000):
    cube = i ** 3
    cubeSet.append(cube)
#sort and uniquify
cubeSet = sorted(set(cubeSet))
print("Cube list complete! Starting our search:")

#Take each cube in that list of cubes
largest_cube = 8
cubeSetCheck = cubeSet
for cube in cubeSet:
    #print(f"Testing cube {cube}")
    stringNum = str(cube)
    #Get all permutations of that cube and make a list of lists
    permutationSet=set(permutations(stringNum))
    #Then for each permutation of that cube
    cubeCount = 0
    solutionList = []
    for permutation in permutationSet:
        #Ignore this permutation if it begins with a zero
        if permutation[0] == "0":
            continue
        #Collapse the list
        thisNumber = int("".join(permutation))
        #And see if it's in our cube set
        if thisNumber in cubeSetCheck:
            cubeCount += 1
            print(f"For cube {cube}, permuted cube found: {thisNumber}. [cubeCount: {cubeCount}]")
            solutionList.append(thisNumber)
        if cubeCount == 3:
            print(f"Solution found! {min(solutionList)} is the smallest cube for which exactly five permutations of its digits are cube.")
            sys.exit(0)
        elif cubeCount != 0:
            for item in solutionList:
                #print(f"Removing {item} from cubeSet...")
                try:
                    cubeSetCheck.remove(item)
                except:
                    pass
        