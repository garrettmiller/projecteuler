#!/usr/bin/python3
#Problem 41
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
#For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

from itertools import permutations

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

#I started by running this with 1-9 and began working backwards, primes only appeared in 1-7 set.
#I could have done this iteratively, but, eh.
stringNums = "1234567"
largestPrime = 0
permutationList = list(permutations(stringNums))
for permutation in permutationList:
    thisNumber = int("".join(permutation))
    if is_prime(int(thisNumber)):
        if thisNumber > largestPrime: 
            print(f"New largest pandigital prime found: {thisNumber}")

