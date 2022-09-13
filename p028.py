#!/usr/bin/python3
#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#It can be verified that the sum of the numbers on the diagonals is 101.

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import numpy

#From prtj on StackOverflow, an easy way to make a spiral in numpy:
#Create a standard 1001x1001 array of desired size, starting from 1-on
array = numpy.arange(1,(1001*1001)+1).reshape(1001,1001)

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

spiralArray = to_spiral(array)

#Sum the diagonals in each direction
sum = numpy.sum(spiralArray.diagonal()) + numpy.sum(numpy.fliplr(spiralArray).diagonal())

#Subtract 1 from result so we don't double-count the starting 1
print(f"The sum of the diagonals of a 1001x1001 spiral matrix is: {sum-1}")