#!/usr/bin/python3
#Dr. Lee Ricketson's solution to p010 - much much faster than mine.

import numpy as np
import time

max_num = 2000000
start = time.time() 
# Every number from one to max_num. 
# NOTE@garrettmiller - 09/Sept/2022 - added datatype to prevent overflow condition from returning incorrect result on Windows. 
numbers = np.arange(max_num+1, dtype='int64')

is_prime = np.ones_like(numbers) # Start by assuming everything is prime... when we determine a number isn't prime, we'll put zero in the corresponding entry in this array

is_prime[0] = 0
is_prime[1] = 0 # zero and one are not prime

for n in range(2,max_num+1):
    if (is_prime[n]==1):
        is_prime[n::n] = 0 # every multiple of n is not prime (using numpy's array slicing, which is faster than a for loop due to python weirdness)
        is_prime[n] = 1 # The above line will have made is_prime[n] = 0, so reset it to one here

# print(numbers*is_prime) # Uncomment this (and probably shrink max_num by a lot) to check if we're identifying primes correctly
print(numbers)
print(is_prime)
sum = numbers*is_prime
print(np.sum(sum)) # numbers*is_prime has zero in place of all the composite numbers, so summing all the entries gives the sum of the primes

end = time.time() 

print('That took ' + str(end-start) + ' seconds.')