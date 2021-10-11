# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:13:47 2021

@author: saurabh satapathy
"""

def pos_tall(l):              #defining the function pos_talll
    print((l.index(max(l)))+1)

t = int(input())              #taking input of number of test cases

for i in range (0,t):
    n=int(input())            #taking input of number of students in class
    l = list (map(int, input().strip().split()))[:n]
    pos_tall(l)               #calling the function pos_tall