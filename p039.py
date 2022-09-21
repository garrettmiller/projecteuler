#!/usr/bin/python3
#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p ≤ 1000, is the number of solutions maximised?

from collections import Counter

perimeterList = [] 

for a in range(1,500):
    for b in range(1,500):
        #Hooray triangles
        c = (a**2 + b**2)**.5
        if int(c) == c:
            p = a+b+c
            if p <= 1000:
                print(f"Valid right triangle found with sides: {a},{b},{c}, with p={p}")
                #Append it to a list, then we'll just count how many times each perimeter appears
                perimeterList.append(int(p))

counter = Counter(perimeterList)
print(f"The perimeter <= 1000 which yield the greatest number of right triangle solutions is (perimeter, solutions): {counter.most_common(1)})")