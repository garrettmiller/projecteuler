#!/usr/bin/python3
#Euler discovered the remarkable quadratic formula:

#n^2 + n + 41

#It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 
#However, when n = 40, 40^2 + 40 + 41 = 40(40+1) + 41 is divisible by 41, 
#and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

#The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. 
#The product of the coefficients, −79 and 1601, is −126479.

#Considering quadratics of the form:

#n^2 + an + b, where |a| < 1000 and |b| <= 1000

#where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |-4| = 4)

#Find the product of the coefficients, a and b, for the quadratic expression that produces the 
#maximum number of primes for consecutive values of n, starting with n=0.

#TODO - solve this

maxPrimes = 0
candidatePrime = 0
bestA = 0
bestB = 0
bestN = 0

def isPrime(n):
    upper = int(n ** .5)+1 #Apparently you only need to check as far as n^(1/2)?  Wild.
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

for a in range(-1000,1000):
    for b in range(-1000,1001):
        primeList = []
        for n in range(0,1001):
            checkValue = ((n**2)+(a*n)+b)
            if checkValue > 0 and isPrime(checkValue):
                primeList.append(checkValue)
            else:
                if len(primeList) > maxPrimes:
                    maxPrimes = len(primeList)
                    bestA = a
                    bestB = b
                    bestN = n
                break

print(f"Longest chain of primes was found with a = {bestA}, b = {bestB}, n = {bestN}, and prime chain length {maxPrimes}.")
print(f"Product of {bestA} and {bestB} is: {bestA * bestB}")
