#!/usr/bin/python3
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#This is Brooke's prime factorization idea implemented

#Prime factorization algorithm from Will Ness on Stack Overflow

finalList = []
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

for x in range (2,21):
    #Solution should be such that you add 2 to list, you add 3 to list, when it comes to 4, you already have one 2, so you only add a single other one, etc.
    #Start with an empty list.  Loop through 2-20, for each number, get prime factor list.  
    #IF full list of prime factors ALREADY EXISTS in list, THEN continue
    #ELSE add missing digits (Loop through prime factors - IF prime factor is in "master list", create new master list where that item is removed and continue)
    tempList = prime_factors(x)
    tempFactorList = finalList.copy()
    print(f"Prime factors of {x} are {tempList}, finalList is {finalList} and tempFactorList is {tempFactorList}")
    for factor in tempList:
        if factor in tempFactorList:
            tempFactorList.remove(factor)
        else:
            finalList.append(factor)
print(str(finalList))

for y in finalList:
    result = result * y

print(str(result))


