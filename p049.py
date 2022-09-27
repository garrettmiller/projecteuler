#!/usr/bin/python3
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

#TODO - fix this

from itertools import permutations

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

for i in range(1,10000):
    #This feels messy but seems to be the best way I know to get all permutations of an int
    listOfPermutations = []
    permutationList = list(permutations(str(i)))
    #This will track if we found a valid solution or not
    flag = True
    #Then for each set of numbers in that permutationList,  
    for number in permutationList:
        #reassemble it into an int
        thisNumber = int("".join(number))
        #and throw it into a current list of permutations
        listOfPermutations.append(thisNumber)
    for n in range(1,5000):
        #Break if we get too high for efficiency
        if (i+2*n) > 9999:
            break
        termList = []
        termList.append(i)
        termList.append(i+n)
        termList.append(i+(2*n))
        #print(f"TermList is {termList}, and permutations are {listOfPermutations}")
        for term in termList:
            if term not in listOfPermutations or is_prime(term) == False:
                flag = False
                break
            else:
                print(f"Continuing with i {i} and n {n} and termList {termList}...")
        if flag == True:
            print(f"Sequence found: {termList}")
            quit()
