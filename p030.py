#!/usr/bin/python3
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#1634 = 1^4 + 6^4 + 3^4 + 4^4
#8208 = 8^4 + 2^4 + 0^4 + 8^4
#9474 = 9^4 + 4^4 + 7^4 + 4^4
#As 1 = 1^4 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

fifthPowerList = []

#Let's pick a nice big number to test up to, there's a mathier way to figure out this maximum I'm sure.
for i in range(2,1000000):
    loopSum = 0 
    #Go through the digits iteratively
    for x in str(i):
        loopSum = loopSum + int(x)**5
    if loopSum == i:
        fifthPowerList.append(i)

print(f"Numbers that can be expressed as fifth powers of digits are {fifthPowerList} and the sum is {sum(fifthPowerList)}. ")