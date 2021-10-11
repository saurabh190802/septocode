# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:08:37 2021

@author: saura
"""
def sq_add(n):                         #defining the function sq_add
    k = sum(int(d)**2 for d in str(n))
    if k==1 :
        print("lucky")
    elif k!=1 and len(str(k))==1:
        print("unlucky")
    else:
        sq_add(str(k))
        
    
t = int(input())

for i in range(0,t):
    n = input()
    sq_add(n)
    
