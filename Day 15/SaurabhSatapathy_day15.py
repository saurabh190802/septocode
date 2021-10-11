# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:58:21 2021

@author: saurabh satapathy
"""

def check(l,n):                   #defining thenfunction check
    k=0
    for i in range(1,n+1):
       if i not in l:
           print(i)
       else:
           k+=1
    if k==n:
        print(0)
            


t = int(input())              #taking input of number of test cases

for i in range (0,t):
    n=int(input())            #taking input of number of students in class
    l = list (map(int, input().strip().split()))[:n]  #taking input of array of students
    check(l,n)                #calling the check function
    
    