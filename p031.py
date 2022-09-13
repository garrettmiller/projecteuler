#!/usr/bin/python3
#In the United Kingdom the currency is made up of pound and pence.  There are eight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

#It is possible to make £2 in the following way:
#1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

#How many different ways can £2 be made using any number of coins?

#Target number of pence to achieve
target = 200

#Values of all UK coins
coins = [1,2,5,10,20,50,100,200]

#Create list of length target + 1
ways = [1] + [0]*target

#Solution using dynamic programming by Mike Molony, deconstructed so I can understand
for coin in coins:
    for i in range(coin, target+1): #Only need to search from current coin value to 200p
        ways[i] = ways[i] + ways[i-coin] #Sum new number of possible ways to previous value

print(f"Ways to make change: {ways[target]} ")