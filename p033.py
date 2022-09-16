#!/usr/bin/python3
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
#to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, 
#and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

#TODO - Fix this 

from fractions import Fraction
import numpy

counter = 0
denominatorList = []
for numerator in range(10,100):
    for denominator in range(10,100):
        #Make sure we're going to be less than 1
        if denominator > numerator:
            #Make sure there's no zeroes to get rid of "trivial examples"
            if "0" not in (str(numerator)) and "0" not in (str(denominator)): 
                #Make sure an element in numerator matches denominator:
                for numeratorDigit in str(numerator):
                    if numeratorDigit in str(denominator):

                        #NEED TO FIX THIS - Fraction with common element removed should be equal to same reduced fraction

                        #And see if our fraction with similar elements and no zeroes reduces:
                        reduced = Fraction(numerator, denominator)
                        if(str(f"{numerator}/{denominator}") != str(reduced)):
                            #Make sure the reduced fraction only has length of 1 for numerator/denominator:
                            if reduced.numerator < 10 and reduced.denominator < 10:
                                #If it did reduce, make sure that there are no longer any common elements:
                                for digit in str(reduced.numerator):
                                    if digit in str(reduced.denominator):
                                        break
                                    else:
                                        counter += 1
                                        print(f"Original Fraction: {numerator}/{denominator}, reduces to {Fraction(numerator, denominator)}, index {counter}")
                                        denominatorList.append(denominator)

#I believe we're currently overflowing here, hence why product is 0
print(f"The denominator of the product of the discovered fractions is: {denominatorList}, {numpy.prod(denominatorList)}")
