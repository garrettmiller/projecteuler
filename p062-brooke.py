#!/usr/bin/python3
# The cube 41063625 (345^3) can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.
# Brooke gave me this as a birthday challenge in 2026 :) 

# Seems like it would have worked but was prohibitively slow
# Yeah it did but it took like 7 hours lol

from itertools import permutations
import sys

cubeSet = []
smallestCube = 9999999999999
seen = set()
NUM_CUBES = 3

#Build a list of cubes
print("Building cube list...")
for i in range(10,10000):
    cube = i ** 3
    cubeSet.append(cube)
#Make it an actual set
cubeLookup = set(cubeSet)
print("Cube list complete! Starting our search:")

for cube in cubeSet:
    if cube in seen:
        continue
    # print(f"Testing cube {cube}")
    stringNum = str(cube)
    #Get all permutations of that cube and make a list of lists
    permutationAll= {int("".join(p)) for p in permutations(stringNum) if len("".join(p)) == 8}
    permutationCubes = permutationAll.intersection(cubeSet)
    if len(permutationCubes) == NUM_CUBES:
        print(f"Solution found! {min(permutationCubes)} is the smallest cube for which exactly five permutations of its digits are cube.")
        sys.exit(0)
    elif len(permutationCubes) > 1:
        print(f"some cubes: {permutationCubes}")
        seen.update(permutationCubes)
