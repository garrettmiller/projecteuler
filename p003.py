#!/usr/bin/python3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

i = 2
primeList = [1] #1 is always a prime factor
numberToFactor = 600851475143

while i <= numberToFactor:
    #Find if factor
    if (numberToFactor % i != 0):
        i = i + 1
    else:
        numberToFactor //= i
        print(f"Number to factor is {numberToFactor}")
        primeList.append(i)
print(str(primeList))