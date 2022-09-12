#!/usr/bin/python3
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
#For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
#By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
#However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#TODO - Solve this

#Function to find divisors from Martijn Pieters and Anivarth on Stack Overflow, modified by me for Python3, 
#and to remove self from divisors.  Previously used in p012.
def getDivisors(n):
    divisors = [1]
    for i in range(2,int((n**.5))+1):
        if n%i == 0:
            divisors.extend([i,int(n/i)])
    #divisors.extend([n]) #Don't include self in list
    return list(set(divisors))

def isPerfect(n):
    if (sum(getDivisors(n)) == n):
        return True
    else:
        return False

def isAbundant(n):
    if (sum(getDivisors(n)) > n):
        return True
    else:
        return False

def isDeficient(n):
    if (sum(getDivisors(n)) < n):
        return True
    else:
        return False

abundantList = []
resultList = []

#All integers greater than 28123 can be written as sum of two abundant numbers 
for i in range(1,28124):
    #Let's create a list of abundant numbers, why not
        if isAbundant(i):
            abundantList.append(i)

for i in range(1,len(abundantList)):
    matchFlag = False
    for y in range(1,len(abundantList)):
        if abundantList[i] + abundantList[y] == i:
            matchFlag = True
            break
    if not matchFlag:
        resultList.append(i)

print(abundantList)
print(sum(resultList))
