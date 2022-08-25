#!/usr/bin/python3
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#This is Brooke's prime factorization idea implemented

#Prime factorization algorithm from Will Ness on Stack Overflow
#TODO - debugging required, runs but doesn't give expected result.

factorList = []
y = 1
result = 1

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

for x in range (1,21):
    #TODO - check all of this, how you mash lists together
    for item in prime_factors(x):
        factorList.append(item)
print(str(factorList))

for y in factorList:
    result = result * y

print(str(result))


