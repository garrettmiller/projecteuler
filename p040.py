#!/usr/bin/python3

#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

longStr = "0."
for i in range(1,1000001):
    longStr = longStr + str(i)

result = int(longStr[(1+1)]) * int(longStr[(10+1)]) * int(longStr[(100+1)]) * int(longStr[(1000+1)]) * int(longStr[(10000+1)]) * int(longStr[(100000+1)]) * int(longStr[(1000000+1)])
print(result)
