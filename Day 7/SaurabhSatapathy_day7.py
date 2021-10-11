# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:59:59 2021

@author: saurabh satapathy
"""
def count1(inputed_string):          #another approach
    zero = "000000"
    one = "111111"
    if (zero in inputed_string) or (one in inputed_string):
        print("YES")
    else:
        print("NO")

t = int(input())                 #taking input of number of test cases

for i in range (0,t):
    n=int(input())               #taking the length of the string
    inputed_string = str(input())
    count1(inputed_string)                  #calling the count1 function

           #ANOTHER APPROACH

'''def count2(l,n):                     #definig the count function
    c=0
    d=0
    for i in range(0,n-1):
        if l[i]=='0' and l[i+1]=='0':
            c=c+1
        else:
            c=0
        if l[i]=='1' and l[i+1]=='1':
            d=d+1
        else:
            d=0
    if c >= 6 or d>=6:
        print("YES")
    else:
        print("NO")

t = int(input())                 #taking input of number of test cases

for i in range (0,t):
    n=int(input())               #taking the length of the string
    inputed_string = str(input())
    li = list(inputed_string.strip(""))
    count2(li,n)                  #calling the count2 function '''