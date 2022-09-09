#!/usr/bin/python3
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20×20 grid?

import math
gridSize = 20

#Didn't come up with this one on my own, but apparently you can find paths through a grid by 
#dividing the factorial of 2 * gridSize by the square of the gridSize factorial.

print(int(math.factorial(2*gridSize)/math.factorial(gridSize)**2))