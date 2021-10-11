# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 10:14:32 2021

@author: saurabh  satapathy
"""
import math                        #importing math module 

def nearest_multiple_of_5(n):      #defining nearest_multiple_of_5 function
    return math.ceil(n/5)*5

n = int(input())                   #taking input of number of players
scores=[]                          # initialising an empty list scores
for i in range (0,n):              # taking input of scores to scores list
    s=int(input())
    scores.append(s)
for j in range (0,n):
    if(scores[j]>33):
        if((nearest_multiple_of_5(scores[j])-scores[j]) < 3):
            print(nearest_multiple_of_5(scores[j]))
        else:
            print(scores[j])
    else:
        print(scores[j])






    