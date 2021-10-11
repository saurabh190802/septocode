# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:23:20 2021

@author: saurabh satapathy
"""
def check(l,n):                   #defining the function check
    num=[]
    k=0
    for i in range(1,n+1):
       if i not in l:
           num.append(i)
       else:
           k+=1
    if k == n:
        print(0)
    else:
        print(*num,sep=" ")
            


t = int(input())              #taking input of number of test cases

for i in range (0,t):
    n = int(input())            #taking input of range
    l = list(map(int, input().strip().split()))[:n]  #taking input of array 
    check(l,n)                #calling the check function
    

