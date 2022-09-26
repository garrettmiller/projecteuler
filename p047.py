#!/usr/bin/python3
#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

#Prime factorization algorithm from Will Ness on Stack Overflow
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if (n % i) != 0:
            i = i + 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for i in range(1,1000000):
    consecutiveCounter = 0
    factorList = prime_factors(i)
    if len(set(factorList)) == 4:
        consecutiveCounter = consecutiveCounter +1
        #Now check to see if three more consecutive have four prime factors:
        for n in range(i+1,i+4):
            factorList = prime_factors(n)
            if len(set(factorList)) == 4:
                consecutiveCounter = consecutiveCounter + 1
                continue
            else:
                break

    if consecutiveCounter == 4:
        print(f"The first of the first four consecutive integers to have four prime factors is: {str(i)}")
        quit()           