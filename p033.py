#!/usr/bin/python3
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
#to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, 
#and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

#NOTE - Fixed 9/21/2022 - had to add limit_denominator() to Fractions calls to deal with weird floating point situations causing comparisons to fail

from fractions import Fraction
import numpy

resultNumeratorList = []
resultDenominatorList = []
for numerator in range(10,100):
    for denominator in range(numerator,100):
        #Make sure we're going to be less than 1
        if denominator > numerator:
            #Make sure there's no zeroes to get rid of "trivial examples"
            if "0" not in (str(numerator)) and "0" not in (str(denominator)): 
                #Find any common elements between the two operands
                commonElement = list(set(str(numerator)) & set(str(denominator)))
                    
                #and if there's exactly one common element, remove it from each:
                if len(commonElement) == 1:
                    numeratorList = list(str(numerator))
                    denominatorList = list(str(denominator))
                    numeratorList.remove(commonElement[0])
                    denominatorList.remove(commonElement[0])

                    #Then the reduced fractions should be equivalent
                    reduced = Fraction(numerator, denominator).limit_denominator()
                    reducedAfterRemoval = Fraction(int(numeratorList[0])/int(denominatorList[0])).limit_denominator()
                    if reduced == reducedAfterRemoval:
                        print(f"Original Fraction: {numerator}/{denominator}, reduces to {Fraction(numerator, denominator).limit_denominator()}")
                        resultNumeratorList.append(Fraction(numerator, denominator).limit_denominator().numerator)
                        resultDenominatorList.append(Fraction(numerator, denominator).limit_denominator().denominator)

print(f"The numerators of the discovered fractions are: {resultNumeratorList}, denominators are {resultDenominatorList} product is: {Fraction(numpy.prod(resultNumeratorList),numpy.prod(resultDenominatorList))}")
print(f"So denominator in its lowest common terms would be: {Fraction(numpy.prod(resultNumeratorList),numpy.prod(resultDenominatorList)).denominator}")
