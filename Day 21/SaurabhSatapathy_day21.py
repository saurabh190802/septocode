# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 12:11:07 2021

@author: saurabh satapathy
"""
import math

def Log2(x):
    if x == 0:
        return False;
  
    return (math.log10(x) / 
            math.log10(2));
  
def isPowerOfTwo(x):
    return (math.ceil(Log2(x)) == 
            math.floor(Log2(x)));

def highestPowerof2(x):
 
    res = 0;
    for i in range(x, 0, -1):
         
        # If i is a power of 2
        if ((i & (i - 1)) == 0):
         
            res = i;
            break;
    return res;

t = int(input()) #taking input of number of test cases
for i in range(t):
    x = int(input()) #taking input of nnumber of yeasts baker wants
    k=0
    while(x!=0):
         if isPowerOfTwo(x) == True:
             k=k+1
             break
         else:
             s = highestPowerof2(x)
             x=x-s
             k=k+1
    print(k)
            
        
        
    

