#!/usr/bin/python3

#By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example 
#having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
#Consequently 56003, being the first member of this family, is the smallest prime with this property.

#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

#Start with 2, 3 so we don't have to find them
primeList = [2,3]

#Build a list of primes
for i in range(5,1000000,2):
    if is_prime(i):
        primeList.append(i)

#Function to create wildcard strings from Obed Tandadjaja on Medium
def genWildcardStrings(s, index):
    if index > 0:
        wildcards.append(s)
    for x in range(index, len(s)):
        genWildcardStrings(createPlaceholder(s,x), x+1)

#Function to replace a character with asterisks from Obed Tandadjaja on Medium
def createPlaceholder(s, index):
    return s[0:index] + '*' + s[index+1:]

#Go through each prime in the list
for x in range(0, len(primeList)):
    wildcards = []
    #Generate all possible wildcards for a given prime
    genWildcardStrings(str(primeList[x]),0)
    #Then loop through all possible wildcard strings
    for y in range(1, len(wildcards)):
        primeCount = 0 

        #Replace asterisks with 0-9
        for z in range(0,10):
            thisNumber = int(wildcards[y].replace('*', str(z)))
            #Make sure the number isn't reduceable - that it doesn't start with 0
            if len(str(thisNumber)) < len(str(wildcards[y])):
                continue
            if is_prime(thisNumber) == True:
                primeCount = primeCount + 1
        
        #Once count is greater than 8, print and exit
        if primeCount == 8:
            print(f"Starting prime is: {primeList[x]}, wildcard digits are {wildcards[y]}.")
            print(f"Therefore, the first prime of this family would be: {wildcards[y].replace('*',str(1))}")
            exit(0)