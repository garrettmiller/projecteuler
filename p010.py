#!/usr/bin/python3
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#This is SO SLOW lol, not sure if there's a smarter way to do this.

#TODO - test this, takes forever to run

primeList = [2]
candidatePrime = 3
sum = 0

def is_prime(n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

while candidatePrime < 2000000:
    if is_prime(candidatePrime):
        sum = sum + candidatePrime
        print(f"Candidate prime is: {candidatePrime} and Sum is: {sum}")
    candidatePrime = candidatePrime + 2 #no reason to check evens

print(str(sum))
