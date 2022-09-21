#!/usr/bin/python3
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

possibleDrome = 0
dromeList = []

for i in range(1, 1000):
    for n in range(1, 1000):
        possibleDrome = i * n
        stringDrome = str(possibleDrome)
        if stringDrome == stringDrome[::-1]: #neat little trick to reverse a string
            print("Palindrome Found: " + stringDrome)
            dromeList.append(possibleDrome)
    
print(str(sorted(set(dromeList))))