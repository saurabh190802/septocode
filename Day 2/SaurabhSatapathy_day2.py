# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:19:53 2021

@author: saurabh satapathy
"""
import calendar as c  #importng the calendar library

def noOfDaysInBothYears(a,b): #declaring the noOfDaysInBothYears function
    x=0
    y=0
    if c.isleap(a) :
        x=366
    else:
        x=365
    if c.isleap(b):
        y=366
    else:
        y=365
    print(int(x+y))


t=int(input()) #taking input of number of testcases

for i in range (0,t):
    st = list (map(int, input().strip().split()))[:2]

    a=st[0]
    b=st[1]
    
    noOfDaysInBothYears(a,b) #calling the function noOfDaysInBothYearsnoOfDaysInBothYearsnoOfDaysInBothYears