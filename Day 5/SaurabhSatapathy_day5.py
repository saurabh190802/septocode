# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:07:24 2021

@author: saurabh satapathy
"""
def count(l,n):                  #defining count function to count occurance of elements in array
    v=[]
    for i in range(0,n):
        if l.count(l[i]) == 1:
            v.append(l[i])
    print(*v, sep = " ")
                                 
t = int(input())                #taking input of number of test cases

for i in range (0,t):
    n=int(input())
    l = list (map(int, input().strip().split()))[:n]
    count(l,n)                  #calling count function 
                               
