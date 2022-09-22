#!/usr/bin/python3
#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
#For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
#If the word value is a triangle number then we shall call the word a triangle word.

#Using a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import csv
import string 

wordList = []
triangleList = []
bigSum = 0
triangleWords = 0

#Build a list of words
with open("p042_words.txt", 'r', newline='\n') as file:
    csvreader = csv.reader(file, quoting=csv.QUOTE_ALL, delimiter=',')
    for row in csvreader:
        for name in row:
            wordList.append(name)

#Build a list of triangle numbers up to 1000
for n in range(1,1000):
    triangleList.append(0.5*(n*(n+1)))

#Then iterate through the wordlist to see if the value is in 

for word in wordList:
    wordSum = 0
    for character in word:
        wordSum = wordSum + (string.ascii_uppercase.index(character)+1)
    if int(wordSum) in triangleList:
        print(f"Triangle word detected: {word}, {wordSum}")
        triangleWords = triangleWords + 1
    
print(f"The number of triangle words in the list is: {triangleWords}")