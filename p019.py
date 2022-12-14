#!/usr/bin/python3

#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#NOTE - this currently doesn't work on Windows due to ints being too large to go into C ints, but works fine on *nix.  Fix another day.

import datetime as dt
sum = 0

#Epoch time for 00:00:00, January 1, 1901
jan011901 = -2177452800
#Epoch time for 23:59:59, December 31, 2000
dec312000 = 978307199

def epoch_to_day_of_week(epoch):
    return dt.datetime.fromtimestamp(epoch).strftime("%A")

def epoch_to_date(epoch):
    return dt.datetime.fromtimestamp(epoch).strftime("%d")

for i in range(jan011901, dec312000, 86400): #Step by a day at a time, I'm sure there's a smarter way to do this but why not
    if (epoch_to_day_of_week(i) == "Sunday") and (epoch_to_date(i) == "01"):
        sum = sum + 1

print(f"The total of Sundays which fell on the first of the month in the 20th century is: {sum}")