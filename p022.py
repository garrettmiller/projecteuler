#!/usr/bin/python3

#Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
#Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
#So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

#TODO - solve this

import csv
nameList = []
bigSum = 0

with open("p022_names.txt", 'r', newline='\n') as file:
    csvreader = csv.reader(file, quoting=csv.QUOTE_ALL, delimiter=',')
    for row in csvreader:
        for name in row:
            nameList.append(name)

#make alphabetical
nameList = sorted(nameList)

for index, name in enumerate(nameList, start=1):
    nameScore = 0
    nameSum = 0
    print(f"Name index {index} is {name}")
    for character in name:

        nameScore = nameSum * index
    bigSum = bigSum + nameScore
#print(nameList)