# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:35:59 2021

@author: saurabh satapathy
"""
def maxPrmimes(n):          #defining the function maxPrmimes
   print(n // 2)
def printAsMaximalPrimeSum( n):  #defining the function printAsMaximalPrimeSum
    l=[]
    if ( n % 2 == 1): 
        l.append(3)
        n -= 3
   
    while ( n>0): 
        l.append(2)
        n -= 2
    l.sort()
    print(*l,sep=" ")
    
t = int(input())              #taking input of number of test cases

for i in range (0,t):
    n = int(input())          #taking input of assigned number
    maxPrmimes(n)             #calling the function maxPrmimes
    printAsMaximalPrimeSum(n) #calling the function printAsMaximalPrimeSum
