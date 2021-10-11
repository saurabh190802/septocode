# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:52:17 2021

@author: saura
"""

def string_test(s):
    c=0
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            c=c+1
    print(c)

t = int(input())
for i in range(0,t):
    s=str(input())
    string_test(s)