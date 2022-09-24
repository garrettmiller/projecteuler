#!/usr/bin/python3
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def is_prime(n):
    upper = int(n**.5)+1
    for i in range(2,upper):
        if (n % i) == 0:
            return False
    return True

#Start with 2, 3 so we don't have to find them
primeList = [2,3]

#Build a list of primes
for i in range(5,10000,2):
    if is_prime(i):
        primeList.append(i)

#Then just test every odd number starting at first odd composite?
for odd in range(9,10000,2):
    solutionFlag = False
    #Make sure it's composite
    if is_prime(odd) == False:
        for prime in primeList:
            #Make sure we're still less than the tested odd for efficiency
            if prime < odd:
                for square in range(1,50):
                    if (prime + (2 * (square**2))) == odd:
                        solutionFlag = True
                        #print(f"Solution found for {prime} + 2*{square}^2 = {odd}, so solutionFlag = {solutionFlag}")
                        break
    else: #If we're prime, disregard
        solutionFlag = True

    if solutionFlag == False:
        print(f"The smallest odd composite that cannot be written as the sum of a prime and 2x a square is: {odd}")
        quit()
