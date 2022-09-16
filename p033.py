#!/usr/bin/python3
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
#to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, 
#and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

#TODO - Fix this - returning correct product/answer, but not sure fraction logic is right yet since problem example (49/98) doesn't show up

from fractions import Fraction
import numpy

resultList = []
for numerator in range(10,100):
    for denominator in range(10,100):
        #Make sure we're going to be less than 1
        if denominator > numerator:
            #Make sure there's no zeroes to get rid of "trivial examples"
            if "0" not in (str(numerator)) and "0" not in (str(denominator)): 
                #Make sure an element in numerator matches denominator:
                for numeratorDigit in str(numerator):
                    if numeratorDigit in str(denominator):
                        #Find any common elements between the two operands
                        commonElement = list(set(str(numerator)) & set(str(denominator)))
                        #and if there's exactly one common element, remove it from each:
                        if len(commonElement) == 1:
                            numeratorList = list(str(numerator))
                            denominatorList = list(str(denominator))
                            numeratorList.remove(commonElement[0])
                            denominatorList.remove(commonElement[0])
                        
                            #Then the reduced fractions should be equivalent
                            reduced = Fraction(numerator, denominator)
                            if str(reduced) == str(f"{numeratorList[0]}/{denominatorList[0]}"):
                                print(f"Original Fraction: {numerator}/{denominator}, reduces to {Fraction(numerator, denominator)}")
                                resultList.append(int(denominatorList[0]))

print(f"The denominator of the product of the discovered fractions is: {resultList}, {numpy.prod(resultList)}")
