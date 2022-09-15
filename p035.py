#!/usr/bin/python3

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

#NOTE - super slow, I'm sure there's smarter ways to speed this up, would like to try faster prime finding techniques.
#NOTE - finally fixed 9/15/2022, I was using permutations and not rotations, which caused the "number families" to be composite way too often.

import numpy #For rotation

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

LIMIT=1000000
circularPrimeCount = 1 #We're skipping 2 so start this at 1 to account for it
compositeFlag = False

for i in range(3,LIMIT,2): #no need to check evens
    listOfRotations = []
    compositeFlag = False
    numList = []
    rotationList = []
    #Get all permutations of the number at that length
    #EDIT 9/15/2022 - ROTATIONS, not permutations.  That's why this took so long and why it worked sub-100.
    for digit in str(i):
        numList.append(digit)
    
    #Now that we have a list containing our integer, get all rotations and add that to another list
    for x in range(0,len(numList)):
        rotationList.append(numpy.roll(numList,x))

    #Then for each set of numbers in that rotationList,  
    for number in rotationList:
        #reassemble it into an int
        thisNumber = int("".join(number))
        #and throw it into a current list of rotations
        listOfRotations.append(thisNumber)
        #Check each one in that list to determine if each are prime, using a flag value
        for candidatePrime in listOfRotations:
            if is_prime(candidatePrime) == False:
                compositeFlag = True
                break
            else:
                continue
    if compositeFlag == False:
        circularPrimeCount = circularPrimeCount + 1
        print(f"Testing rotations of {i}, which are {listOfRotations} and have found {circularPrimeCount} circular primes so far...")

print(f"The number of circular primes below {LIMIT} is: {circularPrimeCount}.")