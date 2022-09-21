#!/usr/bin/python3
#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

#TODO - solve this

dromeList = []

for i in range(1, 1000000):
    stringDrome = str(i)
    if stringDrome == stringDrome[::-1]: #neat little trick to reverse a string
        #Now let's see if it's a palindrome in base 2
        possibleStringBinaryDrome = str(bin(i))
        if possibleStringBinaryDrome[2::] == possibleStringBinaryDrome[:1:-1]:
            print(f"Decimal/Binary Palindrome Found: {stringDrome}, {possibleStringBinaryDrome[2::]}")
            dromeList.append(i)
    
print(str(sum((dromeList))))