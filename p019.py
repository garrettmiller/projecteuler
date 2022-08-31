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

#TODO - solve this

#Consider using something like the following from Padraic Cunningham on StackOverflow:
ep =  1412673904406

from datetime import datetime

print datetime.fromtimestamp(ep/1000).strftime("%A")
Tuesday


def ep_to_day(ep):
    return datetime.fromtimestamp(ep/1000).strftime("%A")