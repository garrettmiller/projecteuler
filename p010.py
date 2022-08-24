#!/usr/bin/python3
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#TODO - test this

primeList = [2]
candidatePrime = 3

def is_prime(n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

while candidatePrime < 2000000:
    if is_prime(candidatePrime):
        primeList.append(candidatePrime)
    candidatePrime = candidatePrime + 1

print(str(sum(primeList)))