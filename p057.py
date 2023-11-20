#!/usr/bin/python3
#It is possible to show that the square root of two can be expressed as an infinite continued fraction.

#By expanding this for the first four iterations, we get:

#The next three expansions are 
#3/2 = 1.5
#7/5 = 1.4
#17/12 = 1.41666
#41/29 = 1.41379 

#The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 
#1393/985 is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

#In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
#Solved with Brooke on 11/19/2023 

from fractions import Fraction
import sys

result = 0
sys.setrecursionlimit(1010) #needed so we don't crash

def recursive_fraction(result, iterations, counts):
    numerator = Fraction(result).numerator
    denominator = Fraction(result).denominator
    numLength = len(str(numerator))
    denomLength = len(str(denominator))
    if(numLength > denomLength):
        counts += 1
        print(f'counts = {counts}')
    if iterations == 0:
        return 
    else:
        recursive_fraction(1 + Fraction(1, (1+result)), (iterations-1), counts)
    
recursive_fraction(1, 1000, 0)
