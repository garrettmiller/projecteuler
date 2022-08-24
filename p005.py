#!/usr/bin/python3
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# This is super inefficient, lol.
# Brooke claims to have a more elegant solution to this involving primes but I want to see it!

i = 20
flag = False

while flag == False:
    for n in range(1,21):
        if (i % n) != 0:
            i = i + 1
            break
        else:
            if n == 20:
                flag = True

print(str(i))

