#!/usr/bin/python3
#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

#TODO - Fix this, incomplete

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

for i in range(1,100000):
    factorList = prime_factors(i)
    if len(set(factorList)) == 4:
        print(f"The first four consecutive integers to have four prime factors are: {str(i)}")
        quit()