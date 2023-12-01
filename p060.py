#!/usr/bin/python3
#The primes 3, 7, 109, and 673 are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
#For example, taking 7 and 109, both 7109 and 1097 are prime.  The sum of these four primes, 792, represents the lowest
#sum for a set of four primes with this property.
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from itertools import combinations
from tqdm import tqdm

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_list(a,b):
    lst = [a,b]
    for a, b in combinations(lst, 2):
        if is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a))):
            return True
    return False

prime_list = [3]  # Start with 3
lowest_sum = 999999999

# Build a list of primes
print("Building list of primes...")
for i in tqdm(range(5, 10000, 2)):
    if is_prime(i):
        prime_list.append(i)
print("Prime list built.")
print("==========")
prime_set = set(prime_list)
concat_set = set()
lowest_combo = []

for a in tqdm(prime_set):
    for b in prime_set:
        if b < a:
            continue
        if test_list(a,b):
            for c in prime_set:
                if c < b:
                    continue
                if test_list(a,c) and test_list(b,c):
                    for d in prime_set:
                        if d < c:
                            continue
                        if test_list(a,d) and test_list(b,d) and test_list(c,d):
                            for e in prime_set:
                                if e < d:
                                    continue
                                if test_list(a,e) and test_list(b,e) and test_list(c,e) and test_list(d,e):
                                    print(f"5-set found! {a}, {b}, {c}, {d}, {e}, sum is {a+b+c+d+e}")
