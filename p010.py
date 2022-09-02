#!/usr/bin/python3
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#This is SO SLOW lol, there's got to be a smarter way to do this.
#Personal NOTE: 8/29/2022 - apparently you only need to check as far as n^(1/2), made this go from about 1 hour to 10 seconds to run lol.

primeList = [2]
candidatePrime = 3
sum = 2 #start at two since we're not finding it, so needs to be added in to begin

def is_prime(n):
    upper = int(n ** .5)+1 #Apparently you only need to check as far as n^(1/2)?  Wild.
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

while candidatePrime < 2000000:
    if is_prime(candidatePrime):
        sum = sum + candidatePrime
        print(f"Candidate prime is: {candidatePrime} and Sum is: {sum}")
    candidatePrime = candidatePrime + 2 #no reason to check evens

print(str(sum))
