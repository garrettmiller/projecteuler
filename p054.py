#!/usr/bin/python3
#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

#High Card: Highest value card.
#One Pair: Two cards of the same value.
#Two Pairs: Two different pairs.
#Three of a Kind: Three cards of the same value.
#Straight: All cards are consecutive values.
#Flush: All cards of the same suit.
#Full House: Three of a kind and a pair.
#Four of a Kind: Four cards of the same value.
#Straight Flush: All cards are consecutive values of same suit.
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#The cards are valued in the order:
#2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). 
#But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

#The file, p054_poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. 
#You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

from pokerkit import * #using a library might be cheating but oh well
import csv

handList = []
player1Wins = 0

#Build a list of ciphertext
with open("p054_poker.txt", 'r', newline='\n') as file:
    csvreader = csv.reader(file, quoting=csv.QUOTE_ALL, delimiter=' ')
    for row in csvreader:
        for char in row:
            handList.append(char)

#Now lowercase every second character for pokerkit
newHandList = [s[0] + s[1].lower() + s[2:] if len(s) > 1 else s for s in handList]

#Now we evaluate each hand
for i in range(0,len(newHandList),10):
    player1hand = StandardHighHand(''.join(newHandList[i:i+5]))
    player2hand = StandardHighHand(''.join(newHandList[i+5:i+10]))
    if(player1hand > player2hand):
        print(f"Player 1 wins, {player1hand} beats {player2hand}")
        player1Wins += 1

print(f"Of the hands given, Player 1 wins {player1Wins} times.")