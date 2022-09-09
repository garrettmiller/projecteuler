#!/usr/bin/python3

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110; therefore d(220) = 284.
#The proper divisors of 284 are 1,2,4,71 and 142; so d(284) = 220.

#Evaluate the sum of all amicable numbers under 10000.

amicableList = []
amicableCheck = 0 

#Function to find divisors from Martijn Pieters and Anivarth on Stack Overflow, modified by me for Python3, 
#and to remove self from divisors.  Previously used in p012.
def getDivisors(n):
    divisors = [1]
    for i in range(2,int((n**.5))+1):
        if n%i == 0:
            divisors.extend([i,int(n/i)])
    #divisors.extend([n]) #Don't include self for finding amicable numbers
    return list(set(divisors))

for i in range(1,10000):
    amicableCheck = sum(getDivisors(i))
    if (sum(getDivisors(amicableCheck)) == i) and (amicableCheck != i):
        print(f"We found amicable pair {i} and {amicableCheck}")
        amicableList.append(i)
        amicableList.append(amicableCheck)

print(f"Amicable list is: {set(amicableList)}, and sum is {sum(set(amicableList))}")