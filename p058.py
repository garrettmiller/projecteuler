#!/usr/bin/python3
#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 
#8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 =~ 62%.

#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
#If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10?

#TODO - fix this, it's not working correctly for some reason

import numpy
from tqdm import tqdm

#Improved is_prime function from @dawg on Stack Overflow
def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

def to_spiral(A):
    A = numpy.array(A)
    B = numpy.empty_like(A)
    B.flat[base_spiral(*A.shape)] = A.flat
    return B

def base_spiral(rows,cols):
    return spiral_counterclockwise(numpy.arange(rows*cols).reshape(rows,cols))[::-1]

def spiral_counterclockwise(A):
    A = numpy.array(A)
    out = []
    while(A.size):
        out.append(A[0][::-1]) #reverse first row
        A = A[1:][::-1].T #cut off first row and rotate clockwise
    return numpy.concatenate(out)

for i in tqdm(range(2,30000)):
    #From prtj on StackOverflow, an easy way to make a spiral in numpy:
    #Create a standard array of desired size, starting from 1-on
    array = numpy.arange(1,(i*i)+1).reshape(i,i)

    spiralArray = to_spiral(array)

    primeCounter = 0
    totalCounter = -1 #account for 1 being counted twice

    #Get the ratio of primes to non-primes
    for candidatePrime in spiralArray.diagonal():
        if is_prime(candidatePrime):
            primeCounter += 1
        totalCounter += 1
        
    for candidatePrime in numpy.fliplr(spiralArray).diagonal():
        if is_prime(candidatePrime):
            primeCounter += 1
        totalCounter += 1

    primeRatio = (primeCounter/totalCounter)*100
    print(f"Ratios of primes to non-primes along diagonals of spirals of size {i} are: {primeCounter}/{totalCounter},{primeRatio}%")
    if primeRatio < 10:
        exit()