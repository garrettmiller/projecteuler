#!/usr/bin/python3
#The number 3797 has an interesting property. 
#Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
#Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


def is_prime(n):
    upper = int(n**.5)+1
    if n == 1: #Fixed 9/21/2022 - needed to correctly handle 1, which is not prime
        return False
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

truncatablePrimeList = []

for i in range(21,1000000,2):
    compositeFlag = False
    numString = str(i)
    if is_prime(i):
        for x in range((len(numString)),1,-1):
            #print(f"Testing {numString}, and substrings {numString[:x-1]} and {numString[((x-1)*-1):]}")
            if (is_prime(int(numString[:x-1])) == False) or (is_prime(int(numString[((x-1)*-1):])) == False):
                compositeFlag = True
                break
            else:
                continue
        if compositeFlag == False:
            print(f"TRUNCATABLE PRIME FOUND: {numString}")
            truncatablePrimeList.append(i)

print(f"The list of truncatable primes is {truncatablePrimeList} and sum of truncatable primes is: {sum(truncatablePrimeList)}")