#!/usr/bin/python3

#There are exactly ten ways of selecting three from five, 12345:

#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

#In combinatorics, we use the notation, 
#(5)
#(3) = 10

#It is not until n = 23 that a value exceeds one-million: 
#(23)
#(10) = 1144066

#How many, not necessarily distinct, values of 
#(n)
#(r) for 1 <= n <= 100, are greater than one million?

from math import comb

count = 0
for n in range(1, 100 + 1):
    for r in range(1, n + 1):
        if comb(n, r) > 1000000:
            count += 1

print(f"There are {count} combinations, not necessarily distinct, for 1 <= n <= 100, that are greater than one million")
