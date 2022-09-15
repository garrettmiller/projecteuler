#!/usr/bin/python3

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

#NOTE - super slow, I'm sure there's smarter ways to speed this up
#TODO - fix

#Prime family: [2]
#Prime family: [3]
#Prime family: [5]
#Prime family: [7]
#Prime family: [11]
#Prime family: [13, 31]
#Prime family: [17, 71]
#Prime family: [37, 73]
#Prime family: [79, 97]
#Prime family: [113, 131, 311]
#Prime family: [197, 971, 719]
#Prime family: [199, 991, 919]
#Prime family: [337, 373, 733]
#Prime family: [1193, 1931, 9311, 3119]
#Prime family: [3779, 7793, 7937, 9377]
#Prime family: [11939, 19391, 93911, 39119, 91193]
#Prime family: [19937, 99371, 93719, 37199, 71993]
#Prime family: [193939, 939391, 393919, 939193, 391939, 919393]
#Prime family: [199933, 999331, 993319, 933199, 331999, 319993]

import itertools
import math #import math for speed

def is_prime(n):
    upper = int(math.sqrt(n))+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

limit=1000
circularPrimeCount = 1 #We're skipping 2 so start this at 1
listOfRotations = []
compositeFlag = False

for i in range(3,limit,2): #no need to check evens
    print(f"Testing permutations of {i}, and have found {circularPrimeCount} circular primes so far...")
    digitList = []
    listOfRotations = []
    compositeFlag = False
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
        for candidatePrime in listOfRotations:
            if is_prime(candidatePrime) == False:
                compositeFlag = True
                break
            else:
                continue
    if compositeFlag == False:
        circularPrimeCount = circularPrimeCount + 1
    
print(f"The number of circular primes below {limit} is: {circularPrimeCount}")