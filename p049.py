#!/usr/bin/python3
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

from itertools import permutations

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

primeList = []

#Build a list of primes to test
for i in range(1001,10000,2):
    if is_prime(i):
        primeList.append(i)

for prime in primeList:
    #This feels messy but seems to be the best way I know to get all permutations of an int
    listOfPermutations = []
    permutationSet = set(permutations(str(prime)))
    #Then for each set of numbers in that permutationList,  
    for number in permutationSet:
        #reassemble it into an int
        thisNumber = int("".join(number))
        #and throw it into a current list of permutations if it's 4 digits
        if len(str(thisNumber)) == 4:
            listOfPermutations.append(thisNumber)

    #Then let's increment each prime by an increasing amount             
    for n in range(1,5000):
        #This will track if we found a valid solution or not
        flag = True
        #Break if we get too high for efficiency
        if (prime+(2*n)) > 9999:
            break
        termList = []
        termList.append(prime)
        termList.append(prime+n)
        termList.append(prime+(2*n))
        for term in termList:
            if term not in listOfPermutations:
                flag = False
                break 
            if is_prime(term) == False:
                flag = False
                break
        #Check our success condition, making sure it's not the problem example 
        if flag == True and 1487 not in termList:
            print(f"Sequence found: {termList}")
            stringNum = ""
            for term in termList:
                stringNum = stringNum + str(term)

print("The number made up of increasing concatenated permutations of a prime which is not the problem example is:")
print(stringNum)