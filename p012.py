#!/usr/bin/python3
#The sequence of triangle numbers is generated by adding the natural numbers. 
#So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28

#We can see that 28 is the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?

#function to find divisors from Martijn Pieters and Anivarth on Stack Overflow, modified by me for Python3
def getDivisors(n):
    divisors = [1]
    for i in range(2,int((n**.5))+1):
        if n%i == 0:
            divisors.extend([i,int(n/i)])
    divisors.extend([n])
    return list(set(divisors))

for i in range(1,999999999):
    naturalList = []
    for y in range (1, i):
        naturalList.append(y)
    if len(getDivisors(sum(naturalList))) > 500:
        print(f"Number tested is: {sum(naturalList)}, number of divisors is {len(getDivisors(sum(naturalList)))}")
        print()
        quit()


