#!/usr/bin/python3

#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). 
#For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. 
#The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
#The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
#If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
#The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#Your task has been made easy, as the encryption key consists of three lower case characters. 
#Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, 
#decrypt the message and find the sum of the ASCII values in the original text.

import csv

cipherList = []
bestList = []
maxProbability = 0

#Frequencies of various characters as they appear in English text, from Cryptopals
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

#Better version of this that uses frequency analysis instead of langdetect
def isItEnglish(input):
    score = 0
    for char in input:
        score = score + CHARACTER_FREQ.get(char.lower(), 0)
    return score

#Build a list of ciphertext
with open("p059_cipher.txt", 'r', newline='\n') as file:
    csvreader = csv.reader(file, quoting=csv.QUOTE_ALL, delimiter=',')
    for row in csvreader:
        for char in row:
            cipherList.append(int(char))

#Let's use the lowercase ASCII range to search
for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            keyList = []
            plainList = []
            outputString = ""
            possibleProbability = 0
            key = chr(a) + chr(b) + chr(c)
            #Make a list of the repeated key as long as the original ciphertext
            while len(keyList) < len(cipherList):
                keyList.append(a)
                keyList.append(b)
                keyList.append(c)
            #Now that we have our keyList, xor each item and see if it's English
            for i in range(0,len(cipherList)):
                plainList.append(cipherList[i] ^ keyList[i])
            for char in plainList:
                outputString = outputString + chr(char)
            testString = ''.join(filter(str.isalpha, outputString)) #only test letters
            possibleProbability = isItEnglish(testString)
            if possibleProbability >= maxProbability:
                print(f"\nNew most likely key/string found! Key: {key} Score: {maxProbability} Output: {outputString}")
                maxProbability = possibleProbability 
                bestList = plainList
print(f"Sum of terms in the plaintext list is: {sum(bestList)}")