#!/usr/bin/python3
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
#for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
#and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

pandigitalProducts = []
for i in range(1,1001):
    for x in range(1,10001):
        digitList = []
        pandigitalFlag = False
        product = i*x
        #Roll everything into a list
        for digit in str(i):
            digitList.append(digit)
        for digit in str(x):
            digitList.append(digit)
        for digit in str(product):
            digitList.append(digit)
        #Only continue testing if we're exactly 9 digits long (1-9)
        if len(digitList) == 9:
            #See if we're all unique numbers (1-9) by comparing length against set() length, and make sure there's no 0 since we're doing 1-9 only. 
            if (len(set(digitList)) == len(digitList)) and '0' not in digitList:
                pandigitalProducts.append(product)
                print(f"Pandigital identity found: {i} x {x} = {product}")

print(f"The sum of all products whose multiplicand, multiplier, and product are 1-9 pandigital is: {sum(set(pandigitalProducts))}.")