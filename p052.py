#!/usr/bin/python3

#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

#TODO - fix this, currently not returning a result

from itertools import permutations

for i in range(1,1000000):
    listOfPermutations = []
    permutationSet = set(permutations(str(i)))
    #Then for each set of numbers in that permutationList,  
    for number in permutationSet:
        #reassemble it into an int
        thisNumber = int("".join(number))
        #and throw it into a current list of permutations
        listOfPermutations.append(thisNumber)
    print(f"Now testing i {i} and list {listOfPermutations}")
    if str(2*i) in listOfPermutations and str(3*i) in listOfPermutations and str(4*i) in listOfPermutations and str(5*i) in listOfPermutations and str(6*i) in listOfPermutations:
        print("Result found for x, such that x, 2x, 3x, 4x, 5x, 6x all contain the same digits:",i,2*i,3*i,4*i,5*i,6*i)
        #Quit after smallest value found
        quit()
