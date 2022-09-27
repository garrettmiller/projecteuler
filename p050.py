#!/usr/bin/python3

#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

#TODO - Fix this, it's currently not accounting for situations where we don't begin at 2

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

#Start with 2, 3 so we don't have to find them
primeList = [2,3]

#Build a list of primes
for i in range(5,1000000,2):
    if is_prime(i):
        primeList.append(i)

for prime in primeList:
    total = 0
    primeCount = 0
    for otherPrime in primeList:
        total = total + otherPrime
        primeCount = primeCount + 1
        if total == prime:
            print(f"Prime found as sum of consecutive primes: {str(prime)}, with number of primes {str(primeCount)}")
        elif total > prime:
            break
