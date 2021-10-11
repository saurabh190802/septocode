# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 09:16:44 2021

@author: saurabh satapathy
"""
def slope(arr,n):                        #defining the function slope()
    s=0
    k=max(arr)
    m=arr.index(k)
    
    for i in range(m):
        if not (arr[i]<k and arr[i]<arr[i+1]):
            s=s+1
        
    for i in range(m+1,n-1):
        if not (arr[i]<k and arr[i]>arr[i+1]):
            s=s+1
        
    if s>0:
        print("Gentle")
    else:
        print("Steep")
        
            
t = int(input())              #taking input of number of test cases

for i in range (0,t):
    n = int(input())          #taking input of length of the array
    arr = list(map(int, input().strip().split()))[:n] 
    slope(arr,n)              #calling the function slope()

