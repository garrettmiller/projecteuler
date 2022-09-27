#!/usr/bin/python3

#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

#Start with 2, 3 so we don't have to find them
primeList = [2,3]
resultPrime = 0 
highestPrimeCount = 0 

#Build a list of primes
for i in range(5,1000000,2):
    if is_prime(i):
        primeList.append(i)

#Need to account for situations where we don't start at beginning of primelist
for i in range(1,len(primeList)):
    for prime in primeList[i:]:
        total = 0
        primeCount = 0
        for otherPrime in primeList[i:]:
            total = total + otherPrime
            primeCount = primeCount + 1
            if total > prime:
                break
            elif total == prime and primeCount > highestPrimeCount:
                print(f"Prime found as sum of consecutive primes: {prime}, with number of primes {primeCount}, found beginning at {primeList[i]}, index {i}")
                highestPrimeCount = primeCount
                resultPrime = prime