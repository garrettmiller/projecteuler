#!/usr/bin/python3
#The primes 3, 7, 109, and 673 are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
#For example, taking 7 and 109, both 7109 and 1097 are prime.  The sum of these four primes, 792, represents the lowest
#sum for a set of four primes with this property.
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

#Solved, but sloooooow
#Optimization idea: Keep track of two terms which led to an invalid result, and don't even run test_list if those values in there

#New idea - take all the primes, concatenate every one against every other one, see if it's prime, and if so, store it in a set.
#Then when testing the 5 primes, if any concatenation is not in that set, leave it
#then test the ones that remain

from itertools import combinations, permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_list(lst, mySet):
    if any(i not in mySet for i in lst):
        #print(f"Lookup fail - {lst}")
        return False
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
concat_set = set()
lowest_combo = []

# Build a list of valid prime concatenations
for concat in permutations(prime_list,2):
    my_string = ' '
    for x in concat:
        x = str(x)
        my_string += x
        if is_prime(int(my_string)):
            concat_set.add(int(my_string))

print(len(concat_set))

for combo in combinations(prime_list, 5):
    if test_list(set(combo), concat_set):
        current_sum = sum(combo)
        if current_sum < lowest_sum:
            lowest_sum = current_sum
            lowest_combo = combo
            print(f"5-set found: {lowest_combo}, sum is {current_sum}, lowest sum is {lowest_sum}")

print(f"Lowest sum of a 5-set of primes that remain prime with concatenation of any two is {lowest_sum}, made up of {combo}")


