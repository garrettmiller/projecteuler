#!/usr/bin/python3
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# TODO - test this


possibleTriplet = 0

# Brute force, baby.
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if (a < b) and (b < c):
                possibleTriplet = (a ** 2) + (b ** 2) + (c ** 2)
                if possibleTriplet == 1000:
                    print (f"Triplet found, a = {a}, b = {b}, c = {c}")
