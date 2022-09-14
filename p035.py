#!/usr/bin/python3

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

#NOTE - super slow, I'm sure there's smarter ways to speed this up
#TODO - finish testing

import itertools
import math #import math for speed

def is_prime(n):
    upper = int(math.sqrt(n))+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

circularPrimeCount = 0
listOfRotations = []
compositeFlag = False

for i in range(3,1000000,2): #no need to check evens
    print(f"Testing permutations of {i}, and have found {circularPrimeCount+1} circular primes so far...")
    digitList = []
    listOfRotations = []
    #Build a list that we can permute
    for digit in str(i):
        digitList.append(digit)

    #Get all permutations of that list
    permutationList = list(itertools.permutations(digitList))

    #Then for each set of numbers in that permutationList,  
    for number in permutationList:
        #reassemble it into an int
        thisNumber = int("".join(number))
        #and throw it into a current list of rotations
        listOfRotations.append(thisNumber)
        #Check each one in that list to determine if each are prime, initializing a flag value
        compositeFlag = False
        for candidatePrime in listOfRotations:
            if is_prime(candidatePrime) == False:
                compositeFlag = True
                break
            else:
                continue
    if compositeFlag == False:
        circularPrimeCount = circularPrimeCount + 1
    
#Add 1 to result since we're starting from 3
print(f"The number of circular primes below one million is: {circularPrimeCount+1}")