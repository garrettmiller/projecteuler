#!/usr/bin/python3
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#What is the 10001st prime number?
#TODO - test this

primeList = [2]
candidatePrime = 3

def is_prime(n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

while len(primeList) < 10001:
    if is_prime(candidatePrime):
        primeList.append(candidatePrime)
    candidatePrime = candidatePrime + 1

print(str(primeList))
