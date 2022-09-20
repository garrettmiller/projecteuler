#!/usr/bin/python3
#The number 3797 has an interesting property. 
#Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
#Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

#TODO - fix this, for some reason "19" is showing up and its truncation check should disqualify it by having "9" in the last digit

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

truncatablePrimeList = []

for i in range(11,100,2):
    compositeFlag = False
    numString = str(i)
    if is_prime(i):
        for x in range((len(numString)-1),1,-1):
            print(f"Testing {numString}, and substrings {numString[:x]} and {numString[(x*-1):]}")
            if (is_prime(int(numString[:x])) == False) or (is_prime(int(numString[(x*-1):])) == False):
                print(f"Composite detected, {int(numString[:x])} or {int(numString[(x*-1)])}")
                compositeFlag = True
                break
            else:
                continue
        if compositeFlag == False:
            print(f"TRUNCATABLE PRIME FOUND: {numString}")
            truncatablePrimeList.append(i)
            
print(f"The list of truncatable primes is {truncatablePrimeList} and sum of truncatable primes is: {sum(truncatablePrimeList)}")