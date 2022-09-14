#!/usr/bin/python3
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: As 1! = 1 and 2! = 2 are not sums they are not included.

factorialList = []

import math

#Pick an arbitrarily high number to test to
for i in range(3,1000000):
    localSum = 0
    for digit in str(i):
        localSum = localSum + math.factorial(int(digit))
    if localSum == i:
        factorialList.append(i)

print("All numbers which are equal to sum of the factorials of their digits are: ")
print(factorialList)
print(f"and the sum is: {sum(factorialList)}")