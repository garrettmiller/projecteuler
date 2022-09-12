#!/usr/bin/python3

#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

#Used for high-precision division
from decimal import *

longestPatternLength = 0
longestRepeatingDivisor = 0
longestPrecision = 0

#From David Zhang on StackOverflow, this could have also been done with RegEx
def repeating(n):
    i = (n+n).find(n,1,-1)
    if i == -1:
        return None
    else:
        return n[:i]

#Check all the numbers at various levels of precision to get longest repeating pattern
for n in range(1,2000):
    getcontext().prec = n
    for z in range(1,1001):
        pattern = repeating(str(Decimal(1)/Decimal(z))[2:])
        if pattern:
            if len(pattern) > longestPatternLength:
                longestPatternLength = len(pattern)
                longestRepeatingDivisor = z
                longestPrecision = n
                print(f"New longest pattern identified, 1/{longestRepeatingDivisor} yields pattern of length {longestPatternLength}, with precision {longestPrecision}")