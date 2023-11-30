#!/usr/bin/python3
#The primes 3, 7, 109, and 673 are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
#For example, taking 7 and 109, both 7109 and 1097 are prime.  The sum of these four primes, 792, represents the lowest
#sum for a set of four primes with this property.
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

#Solved, but sloooooow
#Optimization idea: Keep track of two terms which led to an invalid result, and don't even run test_list if those values in there

#New idea - find the set of 4 primes, then try the set of 5-primes?

from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_list(lst):
    for a, b in combinations(lst, 2):
        if not is_prime(int(str(a) + str(b))) or not is_prime(int(str(b) + str(a))):
            return False
    return True

prime_list = [3]  # Start with 3
lowest_sum = 999999999

# Build a list of primes
for i in range(5, 10000, 2):
    if is_prime(i):
        prime_list.append(i)

prime_set = set(prime_list)

for combo in combinations(prime_list, 4):
    if test_list(combo):
        current_sum = sum(combo)
        if current_sum < lowest_sum:
            lowest_sum = current_sum
            print(f"4-set found: {combo}, sum is {current_sum}, lowest sum is {lowest_sum}")

print(f"Lowest sum of a 5-set of primes that remain prime with concatenation of any two is {lowest_sum}, made up of {combo}")


