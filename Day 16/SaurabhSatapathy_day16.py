# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:18:50 2021

@author: saurabh satapathy
"""
def check(l,n):                            #defining the function check
    k=0
    m=0
    for i in range(n):
        if l[i]%2 == 0 :
            k=k+1  
        else:
            m=m+1
    for j in range(n):
        if k==n-1:
            if l[j]%2 !=0:
                print(l.index(l[j])+1)
        elif m==n-1:
            if l[j]%2 == 0:
                print(l.index(l[j])+1)
                
                
                

t = int(input())              #taking input of number of test cases

for i in range (0,t):
    n=int(input())            #taking input of length of array
    l = list (map(int, input().strip().split()))[:n]
    check(l,n)                #calling the function check